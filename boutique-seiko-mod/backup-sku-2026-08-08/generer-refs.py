#!/usr/bin/env python3
# Génère la correspondance ancien SKU AliExpress -> référence maison NOIR-<TRI>-<n°>
# Déterministe : tri par (trigramme, handle produit, id variante).
import json, re, sys, pathlib

BASE = pathlib.Path(__file__).parent
SRC = BASE / "table-correspondance.jsonl"
OUT = BASE / "correspondance-ancien-nouveau.jsonl"

# handle produit -> trigramme catégorie maison
RULES = [
    (r"^voyageur-", "GMT"),
    (r"^contre-la-montre-", "CHR"),
    (r"^heritage-.*plongeuse|^noirmont-deux-plongeuse", "PLG"),
    (r"^integrale-", "INT"),
    (r"explorateur$", "EXP"),
    (r"aviateur", "AVI"),
    (r"^montre-field-", "FLD"),
    (r"^montre-squelette-", "SQL"),
    (r"^quarante-et-un-", "Q41"),
    (r"^trente-neuf-", "T39"),
    (r"^trente-six-", "T36"),
    (r"^bracelet-fkm-", "FKM"),
    (r"^bracelet-presidentiel-", "PRE"),
    (r"^bracelet-acier-massif", "ACI"),
    (r"^bracelet-caoutchouc-", "CAO"),
    (r"^bracelet-cuir-daim", "DAI"),
    (r"^bracelet-jubile-", "JUB"),
    (r"^bracelet-milanais", "MIL"),
    (r"^barrettes-de-rechange", "BAR"),
    (r"^pince-a-barrettes", "PIN"),
    (r"^set-tournevis-", "TRN"),
    (r"^kit-d-entretien", "KIT"),
    (r"^loupe-de-date-", "LPD"),
    (r"^loupe-d-horloger", "LPH"),
    (r"^doigtiers-", "DOI"),
    (r"^outil-de-mise-a-taille", "OUT"),
    (r"^remontoir-", "REM"),
    (r"^rouleau-de-voyage-", "ROU"),
    (r"^etui-de-voyage-", "ETU"),
    (r"^coffret-", "COF"),
    (r"^coussins-de-presentation", "COU"),
    (r"^carte-cadeau", "CAD"),
]


def trigramme(handle):
    for pat, tri in RULES:
        if re.search(pat, handle):
            return tri
    return None


rows = [json.loads(l) for l in SRC.read_text().splitlines() if l.strip()]

# La carte cadeau est hors périmètre (aucun SKU fournisseur, produit non physique).
cibles = [r for r in rows if (r.get("sku_actuel") or "").strip() != ""]
inconnus = sorted({r["product_handle"] for r in rows if trigramme(r["product_handle"]) is None})
if inconnus:
    sys.exit("Handles sans trigramme: " + ", ".join(inconnus))

def vid(r):
    return int(r["variant_id"].rsplit("/", 1)[-1])

cibles.sort(key=lambda r: (trigramme(r["product_handle"]), r["product_handle"], vid(r)))

compteur = {}
out = []
for r in cibles:
    tri = trigramme(r["product_handle"])
    compteur[tri] = compteur.get(tri, 0) + 1
    r2 = dict(r)
    r2["sku_nouveau"] = f"NOIR-{tri}-{compteur[tri]:03d}"
    out.append(r2)

nouveaux = [r["sku_nouveau"] for r in out]
assert len(nouveaux) == len(set(nouveaux)), "collision de référence maison"

with OUT.open("w") as f:
    for r in out:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print(f"variantes traitees: {len(out)}")
print("par trigramme:", json.dumps(compteur, sort_keys=True))
