#!/usr/bin/env python3
import json, re
from pathlib import Path
from html.parser import HTMLParser
from collections import Counter

RAW = Path("/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/analyses/2026-09-03-univers-poufs/raw")
DATE = "2026-09-03"

# --- DFS overviews ---
print("=== DFS OVERVIEWS ===")
for slug in ["big-bertha-original", "bananair", "iconpouf", "happers", "casabiloba"]:
    d = json.loads((RAW / slug / DATE / "seo" / "domain-rank-overview.json").read_text())
    item = d["tasks"][0]["result"][0]["items"][0]
    o = item["metrics"]["organic"]
    p = item["metrics"]["paid"]
    print(f"{slug}: etv={o['etv']:.0f} kw={o['count']} pos1={o['pos_1']} p2-3={o['pos_2_3']} p4-10={o['pos_4_10']} paid_etv={p['etv']} paid_kw={p['count']}")

print("\n=== ICONPOUF TOP URL ===")
by = json.loads((RAW / "iconpouf" / DATE / "seo" / "ranked-keywords-by-url.json").read_text())
print("sum etv", round(sum(x["etv"] for x in by), 1), "n", len(by))
for row in by[:20]:
    ex = ", ".join(f"{e['kw']} r{e['rank']} v{e['vol']}" for e in (row.get("examples") or [])[:3])
    print(f"  {row['etv']:8.1f} | {row['n_kw']:3} | {row['url']}")
    print(f"           {ex}")

# brand vs generic for each
print("\n=== BRAND KW CHECK ===")
for slug in ["big-bertha-original", "bananair", "iconpouf", "happers", "casabiloba"]:
    compact = json.loads((RAW / slug / DATE / "seo" / "ranked-keywords-compact.json").read_text())
    brand_re = {
        "big-bertha-original": r"bertha|lounge pug|cloudsac",
        "bananair": r"bananair|banabag",
        "iconpouf": r"iconpouf|icon pouf|icon bean|beanbagbazaar",
        "happers": r"happers",
        "casabiloba": r"casabiloba|casa biloba|cotton wood",
    }[slug]
    brand_etv = 0
    brand_n = 0
    total = 0
    for it in compact:
        etv = float(it.get("etv") or 0)
        total += etv
        kw = (it.get("keyword") or "").lower()
        if re.search(brand_re, kw):
            brand_etv += etv
            brand_n += 1
    print(f"{slug}: brand_etv={brand_etv:.0f} ({100*brand_etv/total if total else 0:.1f}%) n={brand_n} / total {total:.0f}")

# prices from Happers / Casabiloba HTML
price_re = re.compile(r"(\d+[.,]\d{2})\s*€|€\s*(\d+[.,]\d{2})|(\d+[.,]\d{2})\s*&euro;")

def prices_in(path):
    raw = path.read_bytes()
    html = raw.decode("utf-8", errors="ignore")
    found = []
    for m in re.finditer(r'(?:itemprop="price"|product:price:amount|price["\']?\s*[:=]\s*["\']?)(\d+(?:[.,]\d+)?)', html, re.I):
        try:
            found.append(float(m.group(1).replace(",", ".")))
        except Exception:
            pass
    # woocommerce / schema
    for m in re.finditer(r'"price"\s*:\s*"?(\d+(?:[.,]\d+)?)"?', html):
        try:
            v = float(m.group(1).replace(",", "."))
            if 5 < v < 2000:
                found.append(v)
        except Exception:
            pass
    for m in re.finditer(r'data-price="(\d+(?:[.,]\d+)?)"', html):
        try:
            found.append(float(m.group(1).replace(",", ".")))
        except Exception:
            pass
    for m in re.finditer(r'>(\d{2,4}[.,]\d{2})\s*€<', html):
        try:
            found.append(float(m.group(1).replace(",", ".")))
        except Exception:
            pass
    return found

print("\n=== PRICES HTML ===")
files = [
    ("happers-poire", RAW/"happers"/DATE/"scrapes"/"cat-pouf-poire.html"),
    ("happers-gamer", RAW/"happers"/DATE/"scrapes"/"cat-pouf-gamer.html"),
    ("happers-enfant", RAW/"happers"/DATE/"scrapes"/"cat-pouf-enfant.html"),
    ("happers-big", RAW/"happers"/DATE/"scrapes"/"cat-big-pouf.html"),
    ("happers-fauteuil", RAW/"happers"/DATE/"scrapes"/"cat-pouf-fauteuil.html"),
    ("happers-home", RAW/"happers"/DATE/"scrapes"/"homepage.html"),
    ("casa-poire", RAW/"casabiloba"/DATE/"scrapes"/"c-poufs-poire.html"),
    ("casa-geant", RAW/"casabiloba"/DATE/"scrapes"/"c-poufs-geants.html"),
    ("casa-fauteuil", RAW/"casabiloba"/DATE/"scrapes"/"c-fauteuils-pouf.html"),
    ("casa-home", RAW/"casabiloba"/DATE/"scrapes"/"homepage.html"),
]
import statistics
for name, p in files:
    px = prices_in(p)
    if not px:
        print(f"{name}: aucun prix parsé")
        continue
    print(f"{name}: n={len(px)} min={min(px)} med={statistics.median(px)} max={max(px)} sample={sorted(set(px))[:15]}")

# happers sitemap product vs cat
locs = json.loads((RAW/"happers"/DATE/"scrapes"/"sitemap-locs.json").read_text())
print(f"\nhappers locs {len(locs)}")
print("  _c", sum(1 for u in locs if "_c" in u))
print("  _p", sum(1 for u in locs if "_p" in u or "_p" in u))
print("  .htm product", sum(1 for u in locs if u.endswith(".htm") or "_p" in u))
print("  .html", sum(1 for u in locs if u.endswith(".html")))
cats = [u for u in locs if "_c" in u]
print("  cats sample")
for u in cats:
    print("   ", u)

# casabiloba products
p1 = json.loads((RAW/"casabiloba"/DATE/"scrapes"/"product-sitemap1-locs.json").read_text())
p2 = json.loads((RAW/"casabiloba"/DATE/"scrapes"/"product-sitemap2-locs.json").read_text())
cats = json.loads((RAW/"casabiloba"/DATE/"scrapes"/"product_cat-sitemap-locs.json").read_text())
prods = [u for u in p1+p2 if "/produit/" in u]
print(f"\ncasabiloba produits {len(prods)} cats {len(cats)}")
print("cats:")
for u in cats:
    print(" ", u)
