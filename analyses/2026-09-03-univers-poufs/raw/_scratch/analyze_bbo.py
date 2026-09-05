#!/usr/bin/env python3
"""Analyse catalogue BBO déjà scrapé — pas de re-téléchargement."""
import json
import statistics
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(
    "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/"
    "analyses/2026-09-03-univers-poufs/raw/big-bertha-original/2026-09-03/scrapes"
)
OUT = Path(
    "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/"
    "analyses/2026-09-03-univers-poufs/raw/_scratch"
)
OUT.mkdir(parents=True, exist_ok=True)

# --- collections ---
cols = json.loads((ROOT / "collections.json").read_text())["collections"]
col_rows = []
for c in cols:
    col_rows.append({
        "id": c["id"],
        "handle": c["handle"],
        "title": c["title"],
        "products_count": c.get("products_count") or 0,
        "desc_len": len(c.get("description") or ""),
        "published_at": c.get("published_at"),
    })

# --- products ---
products = []
for i in range(1, 16):
    p = ROOT / f"products-p{i}.json"
    if not p.exists():
        continue
    products.extend(json.loads(p.read_text())["products"])

# unique by id
seen = set()
uniq = []
for pr in products:
    if pr["id"] in seen:
        continue
    seen.add(pr["id"])
    uniq.append(pr)
products = uniq

def prices_of(pr):
    return [float(v["price"]) for v in pr.get("variants", []) if v.get("price") is not None]

def median(xs):
    if not xs:
        return None
    return round(statistics.median(xs), 2)

all_prices = []
for pr in products:
    all_prices.extend(prices_of(pr))

vendor_c = Counter(pr.get("vendor") or "(vide)" for pr in products)
type_c = Counter(pr.get("product_type") or "(vide)" for pr in products)

type_stats = {}
for t, n in type_c.most_common():
    subset = [pr for pr in products if (pr.get("product_type") or "(vide)") == t]
    px = []
    n_var = 0
    n_img = 0
    for pr in subset:
        px.extend(prices_of(pr))
        n_var += len(pr.get("variants") or [])
        n_img += len(pr.get("images") or [])
    type_stats[t] = {
        "n_fiches": n,
        "n_variantes": n_var,
        "n_images": n_img,
        "prix_min": min(px) if px else None,
        "prix_med": median(px),
        "prix_max": max(px) if px else None,
    }

# family mapping by product_type / title keywords
FAMILY_RULES = [
    ("F2", ["enfant", "kids", "bambin", "1-5", "1-6", "2-6", "2-14", "3-14"]),
    ("F6", ["gamer", "gaming"]),
    ("F7", ["extérieur", "exterieur", "outdoor", "jardin", "smartcanvas"]),
    ("F4", ["canapé", "canape", "sofa"]),
    ("F5", ["fauteuil", "relax"]),
    ("F3", ["géant", "geant", "xxl", "mammouth"]),
    ("F8", ["repose", "ottoman", "pied"]),
    ("F9", ["coussin de sol", "grand coussin"]),
    ("F10", ["housse", "rembourrage", "bill", "remplissage", "liner"]),
    ("F1", ["poire", "classique", "bean"]),
]

def family_of(pr):
    blob = " ".join([
        pr.get("product_type") or "",
        pr.get("title") or "",
        " ".join(pr.get("tags") or []),
    ]).lower()
    for fam, kws in FAMILY_RULES:
        if any(k in blob for k in kws):
            return fam
    return "HORS"

fam_stats = {}
for fam in ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "HORS"]:
    subset = [pr for pr in products if family_of(pr) == fam]
    px = []
    for pr in subset:
        px.extend(prices_of(pr))
    types = Counter((pr.get("product_type") or "(vide)") for pr in subset)
    fam_stats[fam] = {
        "n_fiches": len(subset),
        "n_variantes": sum(len(pr.get("variants") or []) for pr in subset),
        "prix_min": min(px) if px else None,
        "prix_med": median(px),
        "prix_max": max(px) if px else None,
        "top_types": types.most_common(8),
    }

# variants vs coloris: how many products have 1 variant (one fiche per color)
n_1var = sum(1 for pr in products if len(pr.get("variants") or []) == 1)
n_multi = len(products) - n_1var
opt_names = Counter()
for pr in products:
    for o in pr.get("options") or []:
        opt_names[o.get("name") or "?"] += 1

# compare_at_price usage
n_compare = 0
for pr in products:
    for v in pr.get("variants") or []:
        if v.get("compare_at_price"):
            n_compare += 1
            break

# created_at span
created = sorted(pr.get("created_at") or "" for pr in products)
published = sorted(pr.get("published_at") or "" for pr in products)

# collection axes
def classify_col(handle, title):
    h = f"{handle} {title}".lower()
    axes = []
    checks = [
        ("type_produit", ["pouf", "poire", "canape", "canapé", "fauteuil", "coussin", "repose",
                          "housse", "plaid", "couverture", "lit", "chaise", "tabouret", "ottoman"]),
        ("destinataire", ["enfant", "bebe", "bébé", "ado", "adulte", "gamer", "bambin"]),
        ("taille", ["geant", "géant", "xxl", "2-places", "3-places", "petit", "gros"]),
        ("matiere", ["velours", "chenille", "boucle", "bouclé", "cuir", "fourrure", "coton",
                     "lin", "mail", "tricot", "smartcanvas", "tissu"]),
        ("couleur", ["bleu", "gris", "noir", "rose", "vert", "creme", "crème", "beige",
                     "marron", "violet", "blanc", "jaune", "orange", "rouge"]),
        ("forme", ["rond", "carre", "carré", "rectangulaire"]),
        ("occasion", ["cadeau", "noel", "noël", "black-friday", "cyber", "ete", "été",
                      "hiver", "printemps", "christmas"]),
        ("budget", ["moins-de", "moins de"]),
        ("usage", ["exterieur", "extérieur", "jardin", "bureau", "chambre", "salon", "lecture"]),
        ("gamme_maison", ["albert", "josephine", "joséphine", "mammouth", "louis", "chloe",
                          "victor", "maya", "noah", "oliver", "cloudsac", "lounge-pug",
                          "big-bertha", "charles"]),
        ("saison", ["ete", "été", "hiver", "printemps", "automne"]),
    ]
    for axe, kws in checks:
        if any(k in h for k in kws):
            axes.append(axe)
    return axes or ["autre"]

axe_cols = defaultdict(list)
for c in col_rows:
    for a in classify_col(c["handle"], c["title"]):
        axe_cols[a].append((c["handle"], c["title"], c["products_count"]))

# empty collections
empty = [c for c in col_rows if c["products_count"] == 0]
huge = [c for c in col_rows if c["products_count"] >= 200]

summary = {
    "n_collections": len(col_rows),
    "n_fiches": len(products),
    "n_variantes": sum(len(pr.get("variants") or []) for pr in products),
    "n_1_variante": n_1var,
    "n_multi_variantes": n_multi,
    "option_names": opt_names.most_common(),
    "n_avec_prix_barre": n_compare,
    "prix_min": min(all_prices) if all_prices else None,
    "prix_med": median(all_prices),
    "prix_max": max(all_prices) if all_prices else None,
    "vendors": vendor_c.most_common(),
    "created_min": created[0] if created else None,
    "created_max": created[-1] if created else None,
    "published_min": published[0] if published else None,
    "published_max": published[-1] if published else None,
    "n_empty_collections": len(empty),
    "empty_handles": [c["handle"] for c in empty],
    "huge_collections": [(c["handle"], c["title"], c["products_count"]) for c in huge],
    "type_stats": type_stats,
    "fam_stats": fam_stats,
    "axes": {k: {"n": len(v), "exemples": v[:12]} for k, v in axe_cols.items()},
    "all_collections": col_rows,
}

(OUT / "bbo-analyse.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2, default=str))

print("=== BBO ===")
print(f"collections {len(col_rows)} | fiches {len(products)} | variantes {summary['n_variantes']}")
print(f"1 variante {n_1var} | multi {n_multi} | prix barre {n_compare}")
print(f"prix {summary['prix_min']} / {summary['prix_med']} / {summary['prix_max']}")
print("vendors", vendor_c.most_common())
print("created", created[0], "->", created[-1])
print("\n=== TYPES (top 25) ===")
for t, n in type_c.most_common(25):
    s = type_stats[t]
    print(f"  {n:4} fiches | {s['n_variantes']:4} var | {s['prix_min']}-{s['prix_med']}-{s['prix_max']} | {t}")
print("\n=== FAMILLES ===")
for fam, s in fam_stats.items():
    print(f"  {fam}: {s['n_fiches']:4} fiches | {s['prix_min']}-{s['prix_med']}-{s['prix_max']} | {s['top_types'][:4]}")
print("\n=== AXES COLLECTION ===")
for a, v in sorted(axe_cols.items(), key=lambda x: -len(x[1])):
    print(f"  {a}: {len(v)}")
print("empty", len(empty), [c['handle'] for c in empty])
print("written", OUT / "bbo-analyse.json")
