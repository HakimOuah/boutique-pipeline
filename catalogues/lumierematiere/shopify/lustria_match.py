"""Appariement Lumière Matière <-> Lustria et calcul des prix cibles (étape 9).

Produit `prix-alignement-plan-2026-08-26.json`, consommé par `align_prices.py`
et par la rédaction du rapport. Aucune écriture Shopify ici.

Règles (brief Hakim, 26/08/2026) :
  - cible = médiane des comparables Lustria x 0,90 ;
  - terminaison en 9, euros entiers, grille au pas de 10 € ;
  - plancher de marge sur base HT (TVA 20 %) : coût DSers + 2 € de fret,
    marge >= max(40 € HT ; 25 % du HT) ;
  - aucun comparable -> on ne touche pas au prix ;
  - cible sous le plancher -> on ne descend pas ;
  - cible au-dessus du prix actuel -> on ne monte pas (voir NOTE HAUSSE) ;
  - les paliers de taille gardent leur écart relatif.

NOTE HAUSSE — décision de cadrage, à valider par Hakim. Le mandat est de se
placer *sous* Lustria. Sur beaucoup de fiches la médiane comparable est si haute
que la cible à -10 % passe au-dessus de notre prix actuel : appliquer la formule
mécaniquement serait une hausse de prix, ce que le brief n'autorise nulle part
(le jeu de décisions attendu est baisse / inchangé / bloqué par la marge). Ces
lignes sont donc laissées intactes et comptées à part.
"""
from __future__ import annotations

import csv
import json
import re
import statistics
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIVE = HERE / "prix-live-2026-08-26.json"
LUSTRIA = HERE / "lustria-catalogue-2026-08-25.json"
DSERS = HERE.parent / "catalogue-dsers.csv"
PLAN = HERE / "prix-alignement-plan-2026-08-26.json"

TVA = 1.20
FRET = 2.00
MARGE_EUR_MIN = 40.0
MARGE_PCT_MIN = 0.25
REMISE = 0.90
POOL_MIN = 3          # en dessous, aucune médiane défendable
POOL_CONFORT = 8      # au-dessus, l'appariement est jugé solide
SPREAD_LARGE = 3.0    # p75/p25 au-delà duquel la médiane est peu représentative


# --------------------------------------------------------------------------- #
# normalisation
# --------------------------------------------------------------------------- #
def deaccent(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def tokens(*parts: str) -> set[str]:
    blob = deaccent(" ".join(parts).lower())
    return set(re.findall(r"[a-z]+", blob))


def quantiles(vals: list[float]) -> tuple[float, float, float]:
    v = sorted(vals)

    def q(f: float) -> float:
        i = f * (len(v) - 1)
        lo = int(i)
        hi = min(lo + 1, len(v) - 1)
        return v[lo] + (v[hi] - v[lo]) * (i - lo)

    return q(0.25), statistics.median(v), q(0.75)


# --------------------------------------------------------------------------- #
# axe 1 — type de luminaire
# --------------------------------------------------------------------------- #
# Lustria range ses lustres sous « Suspension Luminaire » (2 390 fiches contre
# 1 seule typée « Lustre ») : c'est un même marché, le luminaire suspendu. Le
# plafonnier est un marché distinct — médiane 139,90 chez eux contre 279,90 en
# suspension. On ne mélange pas les deux.
TYPE_SUSPENDU = "suspendu"
TYPE_PLAFONNIER = "plafonnier"

LUSTRIA_TYPE_MAP = {
    "Suspension Luminaire": TYPE_SUSPENDU,
    "Lustre": TYPE_SUSPENDU,
    "Luminaire Plafonnier": TYPE_PLAFONNIER,
}
LUSTRIA_TYPE_EXCLUS = {
    "Veilleuse", "Lampe de Chevet", "Lampe de Table",
    "Lampadaire", "Applique Murale", "Luminaire Extérieur", "Projecteur Galaxie",
}
# Garde-fou : leur champ `type` est parfois faux (des appliques murales sont
# typées « Luminaire Plafonnier »). Le handle tranche contre le type.
HANDLE_HORS_MARCHE = re.compile(
    r"\b(applique|appliques|veilleuse|veilleuses|lampadaire|lampadaires|chevet|"
    r"projecteur|projecteurs|spot|spots|borne|bornes|ruban|rubans|bandeau|"
    r"guirlande-lumineuse|ampoule|ampoules|abat-jour-seul|douille|interrupteur|"
    r"transformateur|telecommande|rail|rails|exterieur|exterieure|exterieurs|"
    r"solaire|solaires|etanche|jardin|terrasse|liseuse|lampe-de-bureau|"
    r"lampe-a-poser|lampe-de-table|miroir)\b"
)


def type_lustria(prod: dict) -> str | None:
    h_tokens = set(deaccent(prod["h"].lower()).split("-"))
    if HANDLE_HORS_MARCHE.search("-" + "-".join(sorted(h_tokens)) + "-"):
        return None
    t = prod["type"]
    if t in LUSTRIA_TYPE_EXCLUS:
        return None
    if t in LUSTRIA_TYPE_MAP:
        return LUSTRIA_TYPE_MAP[t]
    # 38 fiches sans type : on tranche sur le handle, sinon on écarte.
    if {"suspension", "lustre", "suspendu", "suspendue"} & h_tokens:
        return TYPE_SUSPENDU
    if "plafonnier" in h_tokens:
        return TYPE_PLAFONNIER
    return None


def type_nous(titre: str) -> str:
    first = deaccent(titre.lower()).split()[0]
    return TYPE_PLAFONNIER if first.startswith("plafonnier") else TYPE_SUSPENDU


# --------------------------------------------------------------------------- #
# axe 2 — matière
# --------------------------------------------------------------------------- #
# Ordre = priorité : la matière de l'abat-jour porte le prix et la requête. Le
# métal arrive en dernier parce que presque toute monture en contient.
MATIERES: list[tuple[str, set[str]]] = [
    ("bambou",    {"bambou", "bambous"}),
    ("rotin",     {"rotin", "osier", "paille", "raphia", "jonc", "vannerie", "wicker",
                   "tresse", "tressee", "tresses", "tressees"}),
    ("corde",     {"corde", "cordes", "chanvre", "jute", "sisal", "abaca", "macrame"}),
    ("travertin", {"travertin", "travertins", "albatre"}),
    ("pierre",    {"pierre", "pierres", "marbre", "marbres", "galet", "galets", "beton",
                   "onyx", "ardoise", "stuc", "platre"}),
    ("ceramique", {"ceramique", "ceramiques", "porcelaine", "gres", "faience",
                   "terracotta", "terre", "argile", "email", "emaillee", "emaille"}),
    ("cristal",   {"cristal", "cristaux", "pampille", "pampilles", "pendeloque", "facettes"}),
    ("verre",     {"verre", "verres", "opaline", "opalines", "opalin", "opalins",
                   "souffle", "soufflee", "borosilicate", "fume", "fumee"}),
    ("bois",      {"bois", "noyer", "chene", "teck", "rondin", "rotin"}),
    ("textile",   {"tissu", "tissus", "soie", "lin", "coton", "papier", "textile",
                   "plisse", "plissee", "washi", "voile"}),
    ("acrylique", {"acrylique", "acryliques", "resine", "plexiglas", "pmma", "silicone"}),
    ("metal",     {"metal", "metaux", "laiton", "aluminium", "cuivre", "chrome", "chromee",
                   "fer", "inox", "acier", "metallique"}),
]

# Matières voisines : même famille sensorielle, même bande de prix constatée.
VOISINES: list[set[str]] = [
    {"bambou", "rotin", "corde", "bois"},
    {"travertin", "pierre", "ceramique"},
    {"verre", "cristal", "acrylique"},
    {"textile", "acrylique"},
    {"metal", "acrylique"},
]


def matiere(tk: set[str]) -> str | None:
    for nom, mots in MATIERES:
        if mots & tk:
            return nom
    return None


def voisines_de(m: str) -> set[str]:
    out: set[str] = set()
    for groupe in VOISINES:
        if m in groupe:
            out |= groupe
    out.discard(m)
    return out


# --------------------------------------------------------------------------- #
# axe 3 — forme, qui tient lieu de classe de taille
# --------------------------------------------------------------------------- #
# Lustria ne publie ni dimension ni nombre de lumières : 0 handle sur 5 928 porte
# un « cm », 4 portent un nombre de lumières. La forme est le seul substitut
# mesurable de la classe de taille, des deux côtés.
FORMES: list[tuple[str, set[str]]] = [
    ("anneau",   {"anneau", "anneaux", "cercle", "cercles", "spirale", "spirales", "boucle",
                  "boucles", "circulaire", "circulaires", "couronne", "concentriques"}),
    ("lineaire", {"lineaire", "lineaires", "barre", "barres", "reglette", "rectangulaire",
                  "rectangulaires", "billard", "tube", "tubes"}),
    ("multi",    {"cascade", "grappe", "grappes", "guirlande", "boules", "globes", "gouttes",
                  "lanternes", "branches", "sputnik", "bras", "petales", "lampes",
                  "lumieres", "feuilles", "palets", "perles", "cones", "vagues", "etages"}),
    ("globe",    {"boule", "globe", "sphere", "bulle", "ballon", "goutte"}),
    ("dome",     {"dome", "cloche", "coupole", "tambour", "abat", "cone", "conique",
                  "corolle", "soucoupe", "disque", "chapeau", "cylindrique", "cylindre",
                  "coupelle", "tonneau", "ovale", "vague", "fleur", "festonnee", "nervuree"}),
]


def forme(tk: set[str]) -> str | None:
    for nom, mots in FORMES:
        if mots & tk:
            return nom
    return None


# --------------------------------------------------------------------------- #
# axe 4 — nombre de lumières
# --------------------------------------------------------------------------- #
MULTI_MOTS = {"cascade", "grappe", "grappes", "guirlande", "boules", "globes", "gouttes",
              "lanternes", "branches", "sputnik", "bras", "lampes", "lumieres", "anneaux",
              "palets", "perles", "cones", "vagues", "etages", "pampilles", "petales",
              "multiple", "concentriques"}


def multiplicite(tk: set[str]) -> str:
    """« multi » = composition à plusieurs sources ou plusieurs modules."""
    return "multi" if MULTI_MOTS & tk else "mono"


# --------------------------------------------------------------------------- #
# terminaison psychologique
# --------------------------------------------------------------------------- #
def arrondi_9(x: float) -> int:
    """Euro entier terminant par 9, grille au pas de 10 €, au plus proche."""
    return max(9, int(round((x - 9) / 10.0)) * 10 + 9)


# --------------------------------------------------------------------------- #
# marge
# --------------------------------------------------------------------------- #
def ht(ttc: float) -> float:
    return ttc / TVA


def marge_ht(ttc: float, cout: float) -> float:
    return ht(ttc) - (cout + FRET)


def plancher_marge(ttc: float) -> float:
    return max(MARGE_EUR_MIN, MARGE_PCT_MIN * ht(ttc))


def prix_plancher(cout: float) -> int:
    """Plus petit prix de la grille en 9 qui tient les deux planchers."""
    rendu = cout + FRET
    # marge >= 40 € HT      -> TTC >= 1,2 x (rendu + 40)
    # marge >= 25 % du HT   -> TTC >= 1,2 x rendu / 0,75
    mini = max(TVA * (rendu + MARGE_EUR_MIN), TVA * rendu / (1 - MARGE_PCT_MIN))
    p = arrondi_9(mini)
    while p < mini:
        p += 10
    return p


# --------------------------------------------------------------------------- #
# chargement
# --------------------------------------------------------------------------- #
def charge_nous() -> list[dict]:
    live = [p for p in json.loads(LIVE.read_text(encoding="utf-8")) if p["status"] == "ACTIVE"]
    dsers = {r["handle"]: r for r in csv.DictReader(DSERS.open(encoding="utf-8"))}
    out = []
    for p in live:
        row = dsers[p["handle"]]
        variants = p["variants"]["nodes"]
        paliers = sorted({float(v["price"]) for v in variants})
        tk_titre = tokens(p["title"])
        tk_fourn = tokens(row["supplier_title"])
        # Notre titre d'abord. Beaucoup de lustres LED n'y nomment aucune matière :
        # la fiche fournisseur sert alors de source secondaire, tracée.
        mat, mat_src = matiere(tk_titre), "titre"
        if mat is None:
            mat, mat_src = matiere(tk_fourn), "fiche fournisseur"
        if mat is None:
            mat_src = "non nommée"
        diam = sorted({int(m) for v in variants for o in v["selectedOptions"]
                       for m in re.findall(r"(\d+)\s*cm", o["value"])})
        lum = sorted({int(m) for v in variants for o in v["selectedOptions"]
                      for m in re.findall(r"(\d+)\s*(?:lumi|anneau|globe|boule|tete|branch)",
                                          o["value"], re.I)})
        out.append({
            "sku": row["sku"],
            "handle": p["handle"],
            "product_id": p["id"],
            "titre": p["title"],
            "famille": p["productType"],
            "cout": float(row["cost_proxy_ae"]),
            "paliers": paliers,
            "prix_actuel": paliers[0],
            "n_var": len(variants),
            "type": type_nous(p["title"]),
            "matiere": mat,
            "matiere_source": mat_src,
            "forme": forme(tk_titre),
            "multi": multiplicite(tk_titre),
            "diam_max": max(diam) if diam else None,
            "lumieres_max": max(lum) if lum else None,
            "variants": [{"id": v["id"], "price": float(v["price"])} for v in variants],
        })
    out.sort(key=lambda r: r["sku"])
    return out


def charge_lustria() -> list[dict]:
    src = json.loads(LUSTRIA.read_text(encoding="utf-8"))["produits"]
    out = []
    for p in src:
        t = type_lustria(p)
        if t is None or not p.get("prix"):
            continue
        tk = tokens(p["h"], p["t"], *p["tags"])
        out.append({
            "h": p["h"], "prix": float(p["prix"]), "nvar": p["nvar"],
            "type": t, "matiere": matiere(tk), "forme": forme(tk),
            "multi": multiplicite(tk),
        })
    return out


# --------------------------------------------------------------------------- #
# appariement
# --------------------------------------------------------------------------- #
def apparie(nous: dict, lustria: list[dict]) -> dict:
    """Critères du plus fin au plus grossier ; on retient le premier qui tient.

    Un critère dont notre propre valeur est inconnue n'est pas un critère : on
    ne l'utilise pas comme filtre (apparier `forme=None` sur `forme=None` serait
    un accident, pas une justification).
    """
    base = [x for x in lustria if x["type"] == nous["type"]]
    mat, frm, mul = nous["matiere"], nous["forme"], nous["multi"]
    essais: list[tuple[str, str, list[dict]]] = []

    def ajoute(qualite: str, mats: set[str] | None, avec_forme: bool, avec_multi: bool) -> None:
        libelle = ["type"]
        pool = base
        if mats is not None:
            pool = [x for x in pool if x["matiere"] in mats]
            libelle.append("matiere voisine" if qualite == "approximatif" else "matiere")
        if avec_forme and frm:
            pool = [x for x in pool if x["forme"] == frm]
            libelle.append("forme")
        if avec_multi:
            pool = [x for x in pool if x["multi"] == mul]
            libelle.append("nb lumieres")
        essais.append((qualite, "+".join(libelle), pool))

    if mat:
        for f, m in ((True, True), (True, False), (False, True), (False, False)):
            ajoute("franc", {mat}, f, m)
        vois = voisines_de(mat)
        if vois:
            for f, m in ((True, True), (True, False), (False, False)):
                ajoute("approximatif", vois, f, m)
    elif frm:
        # Corps LED sans matière nommée ni chez nous ni chez eux : la forme est
        # le seul axe mesurable. Appariement volontairement dit approximatif.
        for f, m in ((True, True), (True, False)):
            ajoute("approximatif", None, f, m)
    # Ni matière ni forme : `type` seul, ou `type` + mono/multi, ne justifie rien.
    # La ligne sort en « aucun comparable » et son prix ne bouge pas.

    # `essais` est déjà rangé du plus fin au plus grossier, franc avant
    # approximatif. On prend le critère le plus fin qui porte assez de
    # comparables pour qu'une médiane veuille dire quelque chose ; on ne relâche
    # un axe que lorsque le pool fin est trop mince (POOL_CONFORT), et on ne
    # descend jamais sous POOL_MIN.
    for seuil in (POOL_CONFORT, POOL_MIN):
        for qualite, critere, pool in essais:
            if len(pool) >= seuil:
                return {"qualite": qualite, "critere": critere, "pool": pool}
    return {"qualite": "aucun", "critere": f"aucun pool >= {POOL_MIN} fiches", "pool": []}


def paliers_cibles(paliers: list[float], cible_min: int) -> list[int]:
    """Rebase les paliers sur la cible en conservant l'écart relatif."""
    base = paliers[0]
    out = [cible_min]
    for p in paliers[1:]:
        out.append(arrondi_9(cible_min * p / base))
    for i in range(1, len(out)):          # l'ordre strict des paliers est intouchable
        if out[i] <= out[i - 1]:
            out[i] = out[i - 1] + 10
    return out


def construis_plan() -> dict:
    nous = charge_nous()
    lustria = charge_lustria()
    lignes = []
    for n in nous:
        app = apparie(n, lustria)
        pool = app["pool"]
        plancher = prix_plancher(n["cout"])
        ligne = {
            **{k: n[k] for k in ("sku", "handle", "product_id", "titre", "famille", "cout",
                                 "paliers", "prix_actuel", "n_var", "type", "matiere",
                                 "matiere_source", "forme", "multi", "diam_max",
                                 "lumieres_max", "variants")},
            "qualite": app["qualite"],
            "critere": app["critere"],
            "pool_n": len(pool),
            "marge_avant": round(marge_ht(n["prix_actuel"], n["cout"]), 2),
            "marge_avant_pct": round(100 * marge_ht(n["prix_actuel"], n["cout"])
                                     / ht(n["prix_actuel"]), 1),
            "prix_plancher": plancher,
            "marge_actuelle_conforme": marge_ht(n["prix_actuel"], n["cout"])
            >= plancher_marge(n["prix_actuel"]) - 1e-9,
        }

        if not pool:
            ligne.update({
                "decision": "inchange_sans_comparable",
                "comparable_h": None, "comparable_prix": None, "comparable_med": None,
                "comparable_p25": None, "comparable_p75": None,
                "cible_brute": None, "cible": None,
                "prix_retenu": int(n["prix_actuel"]),
                "paliers_cibles": [int(p) for p in n["paliers"]],
                "marge_apres": ligne["marge_avant"],
                "marge_apres_pct": ligne["marge_avant_pct"],
                "confiance": "n/a",
                "motif": f"aucun pool Lustria de {POOL_MIN} fiches ou plus sur ces axes",
                "pool_exemples": [],
            })
            lignes.append(ligne)
            continue

        prix_pool = sorted(x["prix"] for x in pool)
        p25, med, p75 = quantiles(prix_pool)
        temoin = min(pool, key=lambda x: (abs(x["prix"] - med), x["h"]))
        cible_brute = med * REMISE
        cible = arrondi_9(cible_brute)

        if cible >= n["prix_actuel"]:
            decision, retenu = "inchange_deja_sous_cible", int(n["prix_actuel"])
            motif = (f"cible {cible} € au-dessus de notre prix {int(n['prix_actuel'])} € : "
                     f"deja {100 * (1 - n['prix_actuel'] / med):.0f} % sous leur mediane, "
                     "aucune hausse")
        elif cible < plancher:
            decision, retenu = "bloque_marge", int(n["prix_actuel"])
            motif = (f"cible {cible} € sous le plancher {plancher} € "
                     f"(cout rendu {n['cout'] + FRET:.2f} €) — prix conserve")
        else:
            decision, retenu = "baisse", cible
            motif = f"mediane {med:.2f} € x 0,90 = {cible_brute:.2f} € arrondi a {cible} €"

        spread = (p75 / p25) if p25 else float("inf")
        if app["qualite"] == "franc" and len(pool) >= POOL_CONFORT and spread <= SPREAD_LARGE:
            confiance = "haute"
        elif len(pool) < POOL_CONFORT or spread > SPREAD_LARGE:
            confiance = "faible"
        else:
            confiance = "moyenne"

        ligne.update({
            "decision": decision,
            "comparable_h": temoin["h"],
            "comparable_prix": temoin["prix"],
            "comparable_med": round(med, 2),
            "comparable_p25": round(p25, 2),
            "comparable_p75": round(p75, 2),
            "comparable_spread": round(spread, 2),
            "cible_brute": round(cible_brute, 2),
            "cible": cible,
            "prix_retenu": retenu,
            "paliers_cibles": paliers_cibles(n["paliers"], retenu),
            "marge_apres": round(marge_ht(retenu, n["cout"]), 2),
            "marge_apres_pct": round(100 * marge_ht(retenu, n["cout"]) / ht(retenu), 1),
            "confiance": confiance,
            "motif": motif,
            "pool_exemples": [{"h": x["h"], "prix": x["prix"]} for x in
                              sorted(pool, key=lambda y: y["prix"])[:8]],
        })
        lignes.append(ligne)

    return {
        "genere_le": "2026-08-26",
        "source_lustria": "lustria-catalogue-2026-08-25.json — 5 928 fiches, lu le 25/08/2026",
        "lustria_retenus": len(lustria),
        "regle": {
            "remise": REMISE, "tva": TVA, "fret": FRET,
            "marge_min_eur_ht": MARGE_EUR_MIN, "marge_min_pct_ht": MARGE_PCT_MIN,
            "terminaison": "euro entier terminant par 9, grille au pas de 10 €",
            "pool_min": POOL_MIN, "pool_confort": POOL_CONFORT,
            "hausses": "interdites — cible au-dessus du prix actuel = ligne inchangee",
        },
        "lignes": lignes,
    }


if __name__ == "__main__":
    import collections

    plan = construis_plan()
    PLAN.write_text(json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(plan['lignes'])} lignes -> {PLAN.name}")
    for champ in ("decision", "qualite", "confiance", "critere"):
        print(f"{champ:10s}", dict(collections.Counter(l[champ] for l in plan["lignes"])))
