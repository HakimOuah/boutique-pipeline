#!/usr/bin/env python3
"""Analyse catalogues Shopify Bananair + Iconpouf + extraire sitemap URLs."""
import json
import statistics
from collections import Counter, defaultdict
from pathlib import Path

RAW = Path(
    "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/"
    "analyses/2026-09-03-univers-poufs/raw"
)
DATE = "2026-09-03"
OUT = RAW / "_scratch"


def median(xs):
    return round(statistics.median(xs), 2) if xs else None


def load_products(slug):
    scrapes = RAW / slug / DATE / "scrapes"
    products = []
    for p in sorted(scrapes.glob("products-p*.json")):
        try:
            products.extend(json.loads(p.read_text()).get("products") or [])
        except Exception:
            continue
    seen, uniq = set(), []
    for pr in products:
        if pr["id"] in seen:
            continue
        seen.add(pr["id"])
        uniq.append(pr)
    return uniq


def load_cols(slug):
    p = RAW / slug / DATE / "scrapes" / "collections.json"
    if not p.exists() or p.stat().st_size < 20:
        return []
    try:
        return json.loads(p.read_text()).get("collections") or []
    except Exception:
        return []


FAMILY_RULES = [
    ("F2", ["enfant", "kids", "bambin", "bébé", "bebe", "ado"]),
    ("F6", ["gamer", "gaming"]),
    ("F7", ["extérieur", "exterieur", "outdoor", "jardin", "terrasse"]),
    ("F4", ["canapé", "canape", "sofa"]),
    ("F5", ["fauteuil", "relax"]),
    ("F3", ["géant", "geant", "xxl", "mammouth"]),
    ("F8", ["repose", "ottoman", "pied"]),
    ("F9", ["coussin de sol", "grand coussin", "coussin sol"]),
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


def prices_of(pr):
    return [float(v["price"]) for v in pr.get("variants", []) if v.get("price") is not None]


def analyse(slug):
    products = load_products(slug)
    cols = load_cols(slug)
    all_px = []
    for pr in products:
        all_px.extend(prices_of(pr))
    vendor = Counter(pr.get("vendor") or "(vide)" for pr in products)
    ptype = Counter(pr.get("product_type") or "(vide)" for pr in products)
    n_1var = sum(1 for pr in products if len(pr.get("variants") or []) == 1)
    n_compare = sum(
        1 for pr in products
        if any(v.get("compare_at_price") for v in pr.get("variants") or [])
    )
    created = sorted(pr.get("created_at") or "" for pr in products)
    fam = {}
    for f in ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "HORS"]:
        subset = [pr for pr in products if family_of(pr) == f]
        px = []
        for pr in subset:
            px.extend(prices_of(pr))
        fam[f] = {
            "n_fiches": len(subset),
            "prix_min": min(px) if px else None,
            "prix_med": median(px),
            "prix_max": max(px) if px else None,
            "types": Counter((pr.get("product_type") or "(vide)") for pr in subset).most_common(6),
            "titres": [pr.get("title") for pr in subset[:8]],
        }
    type_stats = {}
    for t, n in ptype.most_common():
        subset = [pr for pr in products if (pr.get("product_type") or "(vide)") == t]
        px = []
        for pr in subset:
            px.extend(prices_of(pr))
        type_stats[t] = {
            "n": n,
            "n_var": sum(len(pr.get("variants") or []) for pr in subset),
            "min": min(px) if px else None,
            "med": median(px),
            "max": max(px) if px else None,
        }
    col_rows = [{
        "handle": c.get("handle"),
        "title": c.get("title"),
        "n": c.get("products_count") or 0,
        "desc_len": len(c.get("description") or ""),
    } for c in cols]
    sample = []
    for pr in products[:15]:
        sample.append({
            "title": pr.get("title"),
            "vendor": pr.get("vendor"),
            "type": pr.get("product_type"),
            "handle": pr.get("handle"),
            "n_var": len(pr.get("variants") or []),
            "n_img": len(pr.get("images") or []),
            "prices": prices_of(pr),
            "tags": pr.get("tags"),
        })
    return {
        "n_fiches": len(products),
        "n_variantes": sum(len(pr.get("variants") or []) for pr in products),
        "n_1var": n_1var,
        "n_compare": n_compare,
        "prix_min": min(all_px) if all_px else None,
        "prix_med": median(all_px),
        "prix_max": max(all_px) if all_px else None,
        "vendors": vendor.most_common(),
        "created_min": created[0] if created else None,
        "created_max": created[-1] if created else None,
        "n_collections": len(col_rows),
        "collections": col_rows,
        "type_stats": type_stats,
        "fam": fam,
        "sample": sample,
        "all_titles": [pr.get("title") for pr in products],
    }


for slug in ("bananair", "iconpouf"):
    data = analyse(slug)
    (OUT / f"{slug}-analyse.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2)
    )
    print(f"\n=== {slug} ===")
    print(f"fiches {data['n_fiches']} var {data['n_variantes']} 1var {data['n_1var']} compare {data['n_compare']}")
    print(f"prix {data['prix_min']} / {data['prix_med']} / {data['prix_max']}")
    print("vendors", data["vendors"][:8])
    print("created", data["created_min"], "->", data["created_max"])
    print("collections", data["n_collections"])
    for c in data["collections"]:
        print(f"  {c['n']:4} | {c['handle']} | {c['title']}")
    print("types:")
    for t, s in list(data["type_stats"].items())[:20]:
        print(f"  {s['n']:4} | {s['min']}-{s['med']}-{s['max']} | {t}")
    print("familles:")
    for f, s in data["fam"].items():
        if s["n_fiches"]:
            print(f"  {f}: {s['n_fiches']} {s['prix_min']}-{s['prix_med']}-{s['prix_max']} {s['types'][:3]}")
