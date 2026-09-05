#!/usr/bin/env python3
"""
Decouverte de mots-cles via DataForSEO Labs, avec deduplication.

Remplace l'etape Keyword Magic Tool de SEMrush (expression exacte, 100 lignes).

Pourquoi ce script existe : DataForSEO restitue les volumes de Google, qui
**pre-agrege les variantes proches** (accents, pluriels, ordre des mots,
mots vides). Une meme demande revient donc sous 5 a 15 formulations portant
TOUTES le meme volume. Sommer ces lignes compte le meme bucket plusieurs
fois. Ce script normalise, regroupe, et ne garde qu'un volume par idee.

Regle non negociable appliquee ici :
    volume d'un groupe = MAX du groupe, jamais la somme.

Endpoint retenu : dataforseo_labs/google/keyword_suggestions
  -> correspondance PLEIN TEXTE sur la graine, sans filtre d'intention.
L'endpoint keywords_data/google_ads/keywords_for_keywords est volontairement
ecarte : il filtre semantiquement et masque les contaminations (teste le
29/08/2026 sur `diffuseur` -> 0 ligne coiffure sur 1 774, alors que
`diffuseur cheveux` vaut 18 100).

Usage :
    export DATAFORSEO_LOGIN=... DATAFORSEO_PASSWORD=...
    python3 kw_dfs.py "hamac" --pages 2 --out rapport.md
    python3 kw_dfs.py "hamac" "terrarium" --json brut.json
"""
import os, sys, json, base64, re, unicodedata, argparse, urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone

LAST_PROVENANCE = {}

API = "https://api.dataforseo.com/v3/"
COUT_PAR_PAGE = 0.132  # USD, constate le 29/08/2026 pour limit=1000

# --- Normalisation -----------------------------------------------------------

MOTS_VIDES = {
    "de","du","des","le","la","les","pour","a","au","aux","en","et","un","une",
    "d","l","dans","avec","sur","par","ou","est","son","sa","ses","ce","cet",
    "cette","mon","ma","mes","the","of","to","in",
}

def sans_accent(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")

# Mots francais invariables se terminant par -s ou -x : les depluraliser produit
# des formes fausses (tennis -> tenni, bois -> boi, prix -> pri) qui rendent la
# table des themes illisible. Constate le 29/08/2026 sur les graines `paddle`
# et `hamac`.
INVARIABLES = {
    "tennis","bois","prix","temps","souris","colis","pays","mois","corps","cours",
    "jus","os","dos","bras","poids","gaz","choix","croix","voix","noix","flux",
    "houx","roux","doux","faux","ananas","matelas","repas","bas","gras","las",
    "ras","tas","vis","avis","devis","puits","tapis","paradis","permis","radis",
    "velours","univers","divers","express","business","fitness","access","abs",
    "plus","moins","sans","dans","lors","alors","toujours","parfois","autrefois",
}

# Pluriels en -aux dont le singulier finit par -au (et non -al).
PLURIELS_EN_AU = {
    "tuyaux","noyaux","etaux","joyaux","boyaux","preaux","fleaux","aveux",
}

def singulier(mot: str) -> str:
    """Depluralisation francaise grossiere, suffisante pour le regroupement.

    Les mots de INVARIABLES sont laisses tels quels."""
    if mot in INVARIABLES:
        return mot
    # -eaux -> -eau : rideaux, panneaux, chapeaux, bateaux, carreaux. Sans
    # exception connue. Bug corrige le 29/08/2026 : la regle -aux -> -al
    # transformait `rideaux` en `rideal`, le separant de `rideau` alors que
    # Google sert les deux dans le meme bucket (54 610/mois de surevaluation
    # sur le rejeu du dossier rideaux).
    if len(mot) > 4 and mot.endswith("eaux"):
        return mot[:-1]
    if len(mot) > 4 and mot.endswith("aux"):
        # -aux est ambigu : chevaux->cheval, bocaux->bocal, mais tuyaux->tuyau.
        return mot[:-1] if mot in PLURIELS_EN_AU else mot[:-3] + "al"
    if len(mot) > 3 and mot.endswith("x"):
        return mot[:-1]
    if len(mot) > 3 and mot.endswith("s") and not mot.endswith("ss"):
        return mot[:-1]
    return mot

def cle(expr: str) -> str:
    """Cle de regroupement : accents, pluriels, mots vides et ordre neutralises."""
    mots = [singulier(m) for m in re.findall(r"\w+", sans_accent(expr).lower())]
    mots = [m for m in mots if m not in MOTS_VIDES]
    return " ".join(sorted(mots)) or sans_accent(expr).lower().strip()

def _nb_accents(k: str) -> int:
    """Compte les accents. NFD obligatoire : en NFC, `e` est un seul codepoint de
    categorie Ll, jamais Mn — le comptage renvoyait 0 partout et la preference
    pour l'ecriture accentuee ne s'appliquait pas (bug corrige le 29/08/2026,
    il faisait choisir `vet gothique` plutot que `vetement gothique`)."""
    return sum(1 for c in unicodedata.normalize("NFD", k)
               if unicodedata.category(c) == "Mn")

def representant(formes):
    """La forme la plus naturelle du groupe : ecriture accentuee, mots entiers,
    formulation courte. On prefere la forme la plus longue a nombre de mots egal,
    parce qu'une forme courte est souvent une abreviation tronquee."""
    def cle_tri(k):
        mots = k.split()
        return (-_nb_accents(k), len(mots), -len(k), k)
    return sorted(formes, key=cle_tri)[0]

# --- Appel API ---------------------------------------------------------------

def _auth():
    login, pwd = os.environ.get("DATAFORSEO_LOGIN"), os.environ.get("DATAFORSEO_PASSWORD")
    if not login or not pwd:
        raise SystemExit("DATAFORSEO_LOGIN et DATAFORSEO_PASSWORD doivent etre definis "
                         "dans l'environnement. Aucune valeur de repli n'est codee en dur.")
    return "Basic " + base64.b64encode(f"{login}:{pwd}".encode()).decode()

CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".cache_kw_dfs")

def suggestions(graine, pages=1, limit=1000, location="France", language="French",
                cache=True):
    """Retourne (lignes, total_annonce, cout). Une ligne = (expression, volume).

    Les reponses sont mises en cache sur disque : relancer une graine deja
    interrogee ne coute rien. Utiliser cache=False pour rafraichir."""
    global LAST_PROVENANCE
    os.makedirs(CACHE, exist_ok=True)
    jeton = re.sub(r"\W+", "_", f"{graine}_{location}_{language}_{pages}_{limit}")[:120]
    chemin = os.path.join(CACHE, jeton + ".json")
    if cache and os.path.exists(chemin):
        with open(chemin, encoding="utf-8") as f:
            d = json.load(f)
        LAST_PROVENANCE = dict(d.get("provenance") or {})
        LAST_PROVENANCE["from_cache"] = True
        lignes = [tuple(x[:4]) + (tuple(x[4]),) if len(x) > 4 else tuple(x)
                  for x in d["lignes"]]
        return lignes, d["total"], 0.0
    lignes, total, cout = [], None, 0.0
    for p in range(pages):
        corps = [{
            "keyword": graine, "location_name": location, "language_name": language,
            "include_serp_info": False, "limit": limit, "offset": p * limit,
            "order_by": ["keyword_info.search_volume,desc"],
        }]
        req = urllib.request.Request(
            API + "dataforseo_labs/google/keyword_suggestions/live",
            data=json.dumps(corps).encode(),
            headers={"Authorization": _auth(), "Content-Type": "application/json"})
        rep = json.load(urllib.request.urlopen(req, timeout=300))
        cout += rep.get("cost") or 0.0
        tache = rep["tasks"][0]
        if tache.get("status_code") != 20000:
            raise SystemExit(f"DataForSEO a refuse la tache : {tache.get('status_message')}")
        # Un `result` vide n'est PAS un marche sans mots-cles : c'est une reponse
        # incomplete de l'API, observee par intermittence le 29/08/2026. Confondre
        # les deux fabrique un zero silencieux — exactement ce que le controle
        # temoin est cense empecher. On distingue donc les deux cas.
        brut = tache.get("result")
        if not brut:
            raise SystemExit(
                f"REPONSE VIDE de DataForSEO sur `{graine}` (page {p + 1}) : le champ "
                "`result` est absent. Ce n'est pas un resultat a zero, c'est une "
                "reponse incomplete. Relancer avec --refresh ; ne rien ecrire tant "
                "que la reponse n'est pas complete.")
        res = brut[0]
        if total is None:
            total = res.get("total_count")
        items = res.get("items")
        if items is None:
            raise SystemExit(
                f"REPONSE SANS `items` sur `{graine}` (page {p + 1}), alors que "
                f"total_count = {total}. Reponse incomplete, pas un zero. Relancer.")
        if not items:
            if p == 0 and (total or 0) > 0:
                raise SystemExit(
                    f"ZERO LIGNE sur `{graine}` alors que l'API annonce "
                    f"total_count = {total}. Incoherence : ne rien ecrire.")
            break
        for it in items:
            infos = it.get("keyword_info") or {}
            serie = tuple(m.get("search_volume")
                          for m in (infos.get("monthly_searches") or []))
            lignes.append((it["keyword"], infos.get("search_volume"),
                           infos.get("competition_level"), infos.get("cpc"), serie))
        if len(items) < limit:
            break
    LAST_PROVENANCE = {"fetched_at": datetime.now(timezone.utc).isoformat(),
                       "endpoint": "dataforseo_labs/google/keyword_suggestions/live",
                       "location_name": location, "language_name": language,
                       "keyword": graine, "pages": pages, "limit": limit, "from_cache": False}
    json.dump({"lignes": lignes, "total": total, "provenance": LAST_PROVENANCE}, open(chemin, "w", encoding="utf-8"),
              ensure_ascii=False)
    return lignes, total, cout

# --- Controle temoin ---

# Valeur du temoin relevee le 29/08/2026, base France, langue francaise.
# Reference historique seulement ; le controle exige des reponses valides
# et la coherence avant/apres, pas un volume immuable.
TEMOIN, TEMOIN_ATTENDU = "tufting", 12100

def verifier_temoin(strict=True, reference=None):
    """Retourne (volume_lu, conforme). Valide la reponse et, si fournie, la reference avant mesure."""
    corps = [{"keywords": [TEMOIN], "location_name": "France",
              "language_name": "French", "search_partners": False}]
    req = urllib.request.Request(
        API + "keywords_data/google_ads/search_volume/live",
        data=json.dumps(corps).encode(),
        headers={"Authorization": _auth(), "Content-Type": "application/json"})
    rep = json.load(urllib.request.urlopen(req, timeout=120))
    tasks = rep.get("tasks") or []
    if rep.get("status_code") not in (None, 20000) or not tasks or tasks[0].get("status_code") != 20000:
        raise SystemExit("CONTROLE TEMOIN IMPOSSIBLE : erreur API ou tache invalide.")
    res = tasks[0].get("result")
    if not res:
        raise SystemExit(
            "CONTROLE TEMOIN IMPOSSIBLE : reponse vide de DataForSEO. "
            "Ce n'est pas un echec du temoin, c'est une reponse incomplete. "
            "Relancer avant d'ecrire le moindre chiffre.")
    lu = res[0].get("search_volume")
    conforme = (isinstance(lu, int) and not isinstance(lu, bool) and lu > 0
                and res[0].get("keyword") == TEMOIN
                and (reference is None or lu == reference))
    if strict and not conforme:
        raise SystemExit(
            f"CONTROLE TEMOIN EN ECHEC : `{TEMOIN}` = {lu}, reference avant mesure {reference}.\n"
            "Reponse invalide ou temoins incoherents ; cause a diagnostiquer. Aucun chiffre ne doit "
            "etre ecrit tant que ce controle n'est pas conforme.")
    return lu, conforme

# --- Deduplication -----------------------------------------------------------

def dedupliquer(lignes):
    groupes = defaultdict(list)
    for ligne in lignes:
        expr, vol, comp, cpc = ligne[0], ligne[1], ligne[2], ligne[3]
        serie = ligne[4] if len(ligne) > 4 else ()
        if vol is None:
            raise SystemExit(f"VOLUME MANQUANT pour `{expr}` : null ne vaut pas zero. "
                             "Conserver la reponse, verifier ce terme avant consolidation.")
        groupes[cle(expr)].append((expr, vol, comp, cpc, serie))
    sortie = []
    for k, membres in groupes.items():
        vols = [m[1] for m in membres]
        formes = [m[0] for m in membres]
        series = [m[4] for m in membres if len(m) > 4 and m[4]]
        sortie.append({
            "cle": k,
            "expression": representant(formes),
            "volume": max(vols),              # JAMAIS la somme : meme bucket Google
            "volume_min": min(vols),
            "formulations": len(membres),
            "fusionne_par_google": len(set(vols)) == 1 and len(membres) > 1,
            "cpc": next((m[3] for m in membres if m[3] is not None), None),
            "serie": series[0] if series else (),
            "variantes": sorted(set(formes), key=len)[:6],
        })
    return fusion_par_serie(fusion_seconde_passe(sorted(sortie, key=lambda d: -d["volume"])))

def cle_agressive(k: str) -> str:
    """Cle plus tolerante : accord en genre et consonnes doublees neutralises."""
    mots = []
    for m in k.split():
        m = re.sub(r"(.)\1", r"\1", m)        # essentielle -> esentiele
        m = re.sub(r"e$", "", m) if len(m) > 4 else m   # essentielle -> essentiell
        mots.append(m)
    return " ".join(sorted(mots))

def fusion_seconde_passe(groupes):
    """Regroupe ce que la normalisation stricte a laisse passer.

    Deux groupes ne sont fusionnes que si leur cle agressive coincide ET que
    Google leur attribue le MEME volume — cette egalite est la preuve qu'il
    s'agit du meme bucket, pas une supposition de notre part."""
    par_cle = defaultdict(list)
    for g in groupes:
        par_cle[(cle_agressive(g["cle"]), g["volume"])].append(g)
    sortie = []
    for membres in par_cle.values():
        if len(membres) == 1:
            sortie.append(membres[0]); continue
        base = max(membres, key=lambda g: g["formulations"])
        base = dict(base)
        base["formulations"] = sum(m["formulations"] for m in membres)
        base["expression"] = representant([m["expression"] for m in membres])
        base["fusionne_par_google"] = True
        vus, var = set(), []
        for m in membres:
            for v in m["variantes"]:
                if v not in vus:
                    vus.add(v); var.append(v)
        base["variantes"] = var[:6]
        sortie.append(base)
    return sorted(sortie, key=lambda d: -d["volume"])

def fusion_par_serie(groupes):
    """Fusionne deux groupes que seule la serie 12 mois revele comme un meme bucket.

    Trouve par le rejeu du dossier gothique (29/08/2026) : sans cette passe, le
    consolide affichait 40 700 au lieu de 35 990, soit un **faux PASS** au-dessus
    du plancher de 37 500. Deux formulations que Google sert dans le meme bucket
    portent exactement la meme serie mensuelle — c'est une empreinte, bien plus
    discriminante que le volume seul.

    Trois garde-fous, parce qu'une fusion a tort coute aussi cher qu'un doublon :
      - volume identique ET serie identique ;
      - la serie doit avoir au moins 3 valeurs distinctes (une serie plate ou
        vide n'est pas une empreinte, c'est un hasard) ;
      - les deux groupes doivent partager au moins un mot significatif.
    """
    par_emp = defaultdict(list)
    for g in groupes:
        serie = g.get("serie") or ()
        emp = (g["volume"], serie) if None not in serie and len(set(serie)) >= 3 else ("_", id(g))
        par_emp[emp].append(g)

    sortie = []
    for membres in par_emp.values():
        if len(membres) == 1:
            sortie.append(membres[0]); continue
        # regroupe par recouvrement lexical : un groupe ne fusionne qu'avec ceux
        # qui partagent un mot avec lui
        restants, paquets = list(membres), []
        while restants:
            base = restants.pop(0)
            paquet, mots = [base], set(base["cle"].split())
            for autre in restants[:]:
                if mots & set(autre["cle"].split()):
                    paquet.append(autre); restants.remove(autre)
            paquets.append(paquet)
        for paquet in paquets:
            if len(paquet) == 1:
                sortie.append(paquet[0]); continue
            base = dict(max(paquet, key=lambda g: g["formulations"]))
            base["formulations"] = sum(g["formulations"] for g in paquet)
            base["expression"] = representant([g["expression"] for g in paquet])
            base["fusionne_par_google"] = True
            base["fusion_serie"] = True
            vus, var = set(), []
            for g in paquet:
                for v in g["variantes"]:
                    if v not in vus:
                        vus.add(v); var.append(v)
            base["variantes"] = var[:6]
            sortie.append(base)
    return sorted(sortie, key=lambda d: -d["volume"])

def themes(groupes, graine, mini=2):
    """Tokens qui accompagnent la graine — c'est la que la contamination se voit."""
    jetons = set(cle(graine).split())
    c = Counter()
    vol = defaultdict(int)
    for g in groupes:
        for m in g["cle"].split():
            if m in jetons or len(m) < 3:
                continue
            c[m] += 1
            vol[m] += g["volume"]
    return [(m, n, vol[m]) for m, n in c.most_common() if n >= mini]

# --- Rapport -----------------------------------------------------------------

def rapport(graine, lignes, groupes, total, cout, top=40):
    nz = [l for l in lignes if l[1] > 0]
    red = len(nz) - len(groupes)
    L = [f"## Graine `{graine}`\n",
         f"- Lignes brutes rendues : **{len(lignes)}** (dont {len(nz)} avec volume > 0)",
         f"- Suggestions annoncees par l'API : **{total}**",
         f"- Idees distinctes apres deduplication : **{len(groupes)}**",
         f"- Reformulations supprimees : **{red}** ({red / max(len(nz),1) * 100:.0f} %)",
         f"- Groupes ou Google a fusionne les variantes : "
         f"**{sum(1 for g in groupes if g['fusionne_par_google'])}**",
         f"- Cout : **{cout:.3f} USD**\n",
         "### Themes co-occurrents — c'est ici que la contamination se lit\n",
         "| Terme | Idees | Volume cumule |", "|---|---:|---:|"]
    for m, n, v in themes(groupes, graine)[:25]:
        L.append(f"| `{m}` | {n} | {v:,} |".replace(",", " "))
    L += ["", f"### Top {top} idees dedupliquees\n",
          "| Idee | Volume | Formulations | Fusionne |", "|---|---:|---:|---|"]
    for g in groupes[:top]:
        L.append(f"| `{g['expression']}` | {g['volume']:,} | {g['formulations']} | "
                 f"{'oui' if g['fusionne_par_google'] else ''} |".replace(",", " "))
    return "\n".join(L)

# --- CLI ---------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Decouverte de mots-cles DataForSEO, dedupliquee.")
    ap.add_argument("graines", nargs="+")
    ap.add_argument("--pages", type=int, default=1, help=f"pages de 1000 (~{COUT_PAR_PAGE} USD/page)")
    ap.add_argument("--top", type=int, default=40)
    ap.add_argument("--out", help="fichier markdown")
    ap.add_argument("--json", help="fichier JSON des groupes")
    ap.add_argument("--refresh", action="store_true", help="ignorer le cache")
    ap.add_argument("--sans-temoin", action="store_true",
                    help="sauter le controle temoin (deconseille)")
    a = ap.parse_args()

    temoin_avant = None
    if not a.sans_temoin:
        temoin_avant, _ = verifier_temoin()
        print(f"[temoin] {TEMOIN} = {temoin_avant} avant mesure — conforme", file=sys.stderr)

    blocs, tout, cout, provenance = [], {}, 0.0, {}
    for g in a.graines:
        lignes, total, c = suggestions(g, pages=a.pages, cache=not a.refresh)
        cout += c
        provenance[g] = dict(LAST_PROVENANCE)
        if not LAST_PROVENANCE.get("fetched_at"):
            raise SystemExit("Cache historique non date : --refresh requis pour une nouvelle mesure decisionnelle.")
        groupes = dedupliquer(lignes)
        tout[g] = groupes
        blocs.append(rapport(g, lignes, groupes, total, c, a.top))
        print(f"[{g}] {len(lignes)} lignes -> {len(groupes)} idees ({c:.3f} USD)", file=sys.stderr)

    if not a.sans_temoin:
        temoin_apres, _ = verifier_temoin(reference=temoin_avant)
        print(f"[temoin] {TEMOIN} = {temoin_apres} apres mesure — conforme", file=sys.stderr)
        blocs.append(f"## Controle temoin\n\n`{TEMOIN}` = **{temoin_avant}** avant la "
                     f"premiere mesure et **{temoin_apres}** apres la derniere "
                     f"(reference historique {TEMOIN_ATTENDU}, non immuable). Temoins coherents ; "
                     "les controles de chaque resultat restent necessaires.")

    txt = "\n\n---\n\n".join(blocs) + f"\n\n**Cout suggestions : {cout:.3f} USD (controles live en supplement)**\n"
    if a.out:
        open(a.out, "w", encoding="utf-8").write(txt)
        print(f"-> {a.out}", file=sys.stderr)
    else:
        print(txt)
    if a.json:
        json.dump(tout, open(a.json, "w"), ensure_ascii=False, indent=1)
        meta = {"observed_at": datetime.now(timezone.utc).isoformat(), "graines": provenance,
                "temoin_avant": temoin_avant, "temoin_apres": None if a.sans_temoin else temoin_apres,
                "controle_temoin_effectue": not a.sans_temoin, "cout_suggestions_usd": cout}
        with open(a.json + ".meta.json", "w") as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)
        print(f"-> {a.json}", file=sys.stderr)

if __name__ == "__main__":
    main()
