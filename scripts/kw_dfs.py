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

def singulier(mot: str) -> str:
    """Depluralisation francaise grossiere, suffisante pour le regroupement.

    Les mots de INVARIABLES sont laisses tels quels."""
    if mot in INVARIABLES:
        return mot
    if len(mot) > 4 and mot.endswith("aux"):
        return mot[:-3] + "al"
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

def representant(formes):
    """La forme la plus naturelle du groupe : accentuee, courte, bien ordonnee."""
    return sorted(formes, key=lambda k: (
        -sum(1 for c in k if unicodedata.category(c) == "Mn"),  # accents = ecriture correcte
        len(k),
        k,
    ))[0]

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
    os.makedirs(CACHE, exist_ok=True)
    jeton = re.sub(r"\W+", "_", f"{graine}_{location}_{language}_{pages}_{limit}")[:120]
    chemin = os.path.join(CACHE, jeton + ".json")
    if cache and os.path.exists(chemin):
        d = json.load(open(chemin, encoding="utf-8"))
        return [tuple(x) for x in d["lignes"]], d["total"], 0.0
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
        res = (tache.get("result") or [{}])[0]
        if total is None:
            total = res.get("total_count")
        items = res.get("items") or []
        if not items:
            break
        for it in items:
            infos = it.get("keyword_info") or {}
            lignes.append((it["keyword"], infos.get("search_volume") or 0,
                           infos.get("competition_level"), infos.get("cpc")))
        if len(items) < limit:
            break
    json.dump({"lignes": lignes, "total": total}, open(chemin, "w", encoding="utf-8"),
              ensure_ascii=False)
    return lignes, total, cout

# --- Deduplication -----------------------------------------------------------

def dedupliquer(lignes):
    groupes = defaultdict(list)
    for expr, vol, comp, cpc in lignes:
        groupes[cle(expr)].append((expr, vol, comp, cpc))
    sortie = []
    for k, membres in groupes.items():
        vols = [v for _, v, _, _ in membres]
        formes = [e for e, _, _, _ in membres]
        sortie.append({
            "cle": k,
            "expression": representant(formes),
            "volume": max(vols),              # JAMAIS la somme : meme bucket Google
            "volume_min": min(vols),
            "formulations": len(membres),
            "fusionne_par_google": len(set(vols)) == 1 and len(membres) > 1,
            "cpc": next((c for _, _, _, c in membres if c is not None), None),
            "variantes": sorted(set(formes), key=len)[:6],
        })
    return fusion_seconde_passe(sorted(sortie, key=lambda d: -d["volume"]))

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
    a = ap.parse_args()

    blocs, tout, cout = [], {}, 0.0
    for g in a.graines:
        lignes, total, c = suggestions(g, pages=a.pages, cache=not a.refresh)
        cout += c
        groupes = dedupliquer(lignes)
        tout[g] = groupes
        blocs.append(rapport(g, lignes, groupes, total, c, a.top))
        print(f"[{g}] {len(lignes)} lignes -> {len(groupes)} idees ({c:.3f} USD)", file=sys.stderr)

    txt = "\n\n---\n\n".join(blocs) + f"\n\n**Cout total : {cout:.3f} USD**\n"
    if a.out:
        open(a.out, "w", encoding="utf-8").write(txt)
        print(f"-> {a.out}", file=sys.stderr)
    else:
        print(txt)
    if a.json:
        json.dump(tout, open(a.json, "w"), ensure_ascii=False, indent=1)
        print(f"-> {a.json}", file=sys.stderr)

if __name__ == "__main__":
    main()
