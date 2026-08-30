#!/usr/bin/env python3
"""Pose productType + categorie taxonomie Shopify sur le catalogue Tufteo.

La categorie Shopify est ce que l'app Google & YouTube traduit en
google_product_category dans le flux Shopping. productType part tel quel
en product_type. Les deux etaient vides sur 38 fiches sur 40.
"""
import json, subprocess, sys, textwrap

STORE = "et0hua-w1.myshopify.com"
PREFIX = "gid://shopify/TaxonomyCategory/"

# titre exact -> (id categorie taxonomie, product_type)
MAP = {
    "Tufting gun 2-en-1 Cut & Loop":                    ("ae-2-1-4-16",        "Machine à tufter"),
    "Kit Tufting Complet":                              ("ae-2-1-1-7",         "Kit de tufting"),
    "Tondeuse électrique pour tapis":                   ("ae-2-1-4-16",        "Tondeuse à tapis"),
    "Kit tondeuse + guide de tonte":                    ("ae-2-1-4-16",        "Tondeuse à tapis"),
    "Ciseaux électriques sans fil de sculpture":        ("ae-2-1-4-4-1",       "Ciseaux électriques de sculpture"),
    "Ciseaux pélican pour tufting":                     ("ae-2-1-4-4-1-1",     "Ciseaux de tufting"),
    "Lames de remplacement pour tondeuse (lot de 12)":  ("ae-2-1-3-1",         "Lames de rechange pour tondeuse"),
    "Guide de tondeuse":                                ("ae-2-1-3",           "Accessoire de tondeuse à tapis"),
    "Pièces détachées pour tufting gun":                ("ae-2-1-3",           "Pièces détachées de machine à tufter"),
    "Équilibreur de ressort (spring balancer)":         ("ae-2-1-3",           "Équilibreur de ressort"),
    "Bobineuse à laine":                                ("ae-2-1-4-18-6-2",    "Bobineuse à laine"),
    "Enfile-laine pour tufting gun (lot de 5)":         ("ae-2-1-4-18-3-2",    "Enfile-laine"),
    "Brosse de finition":                               ("ae-2-1-4-18-1",      "Brosse de finition pour tapis"),
    "Spatule à colle pour tufting":                     ("ae-2-1-4",           "Spatule à colle"),
    "Grippers — bandes de fixation (lot de 8)":         ("ae-2-1-4-10",        "Bandes de fixation pour cadre de tufting"),
    "Toile primaire de tufting (lignes repères)":       ("ae-2-1-2-14-1-1-2",  "Toile de tufting"),
    "Toile premium polyester":                          ("ae-2-1-2-14-1-1-2",  "Toile de tufting"),
    "Tissu de finition":                                ("ae-2-1-2-14-2",      "Tissu de dossage pour tapis"),
    "Tissu de finition antidérapant":                   ("ae-2-1-2-14-2",      "Tissu de dossage antidérapant"),
    "Ruban de finition tissé pour bordures (10 m)":     ("ae-2-1-7-3",         "Ruban de finition pour tapis"),
    "Ruban adhésif de finition":                        ("ae-2-1-2-5",         "Ruban adhésif de finition"),
    "Miroir acrylique pour tufting":                    ("ae-2-1-2-4",         "Miroir acrylique pour tufting"),
    "Fil acrylique en cône pour tufting":               ("ae-2-1-2-6-4",       "Fil à tufter"),
}
FIL_COULEUR = ("ae-2-1-2-6-4", "Fil à tufter")   # les 17 « Fil acrylique tufting — <couleur> »


def cli(query, muter=False):
    cmd = ["shopify", "store", "execute", "--store", STORE, "--json", "--query", query]
    if muter:
        cmd.append("--allow-mutations")
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = r.stdout
    i = out.find("{")
    if i < 0:
        sys.exit("Reponse CLI illisible :\n" + out + r.stderr)
    return json.loads(out[i:])


def cible(titre):
    return MAP.get(titre) or (FIL_COULEUR if titre.startswith("Fil acrylique tufting —") else None)


produits = cli("{ products(first: 60) { nodes { id title } } }")["products"]["nodes"]

lots, courant = [], []
inconnus = []
for p in produits:
    c = cible(p["title"])
    if not c:
        inconnus.append(p["title"]); continue
    courant.append((p, c))
    if len(courant) == 10:
        lots.append(courant); courant = []
if courant:
    lots.append(courant)

if inconnus:
    print("NON MAPPES (laisses tels quels) :")
    for t in inconnus:
        print("   -", t)
    print()

if "--ecrire" not in sys.argv:
    print("DRY-RUN — relancer avec --ecrire\n")
    for lot in lots:
        for p, (cat, pt) in lot:
            print(f'  {cat:20} {pt:42} {p["title"]}')
    print(f"\n{sum(len(l) for l in lots)} fiches a mettre a jour")
    sys.exit(0)

ok = ko = 0
for n, lot in enumerate(lots, 1):
    parts = []
    for i, (p, (cat, pt)) in enumerate(lot):
        parts.append(textwrap.dedent(f'''
          m{i}: productUpdate(product: {{
            id: "{p["id"]}"
            category: "{PREFIX}{cat}"
            productType: {json.dumps(pt, ensure_ascii=False)}
          }}) {{
            product {{ title productType category {{ fullName }} }}
            userErrors {{ field message }}
          }}'''))
    res = cli("mutation {" + "".join(parts) + "\n}", muter=True)
    for i, (p, _) in enumerate(lot):
        r = res.get(f"m{i}") or {}
        errs = r.get("userErrors") or []
        if errs:
            ko += 1
            print(f'  ECHEC  {p["title"][:45]} -> {errs}')
        else:
            ok += 1
            pr = r["product"]
            print(f'  ok     {pr["productType"]:40} {pr["category"]["fullName"].split(" > ")[-1][:30]:32} {pr["title"][:40]}')
    print(f"-- lot {n}/{len(lots)}")

print(f"\n{ok} fiches mises a jour, {ko} en echec")
