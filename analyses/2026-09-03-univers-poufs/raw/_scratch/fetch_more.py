#!/usr/bin/env python3
"""Sitemaps enfants + pages discours manquantes (Happers, Casabiloba, Bananair, Iconpouf, BBO)."""
import json
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

RAW = Path(
    "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/"
    "analyses/2026-09-03-univers-poufs/raw"
)
DATE = "2026-09-03"
UA = "Mozilla/5.0 (compatible; OHVentures-market-research/1.0)"


def fetch(url, dest, timeout=40):
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read()
            dest.write_bytes(body)
            return r.status, len(body)
    except Exception as e:
        dest.write_text(f"ERROR {type(e).__name__}: {e}")
        return "err", 0


def parse_locs(xml_bytes):
    try:
        root = ET.fromstring(xml_bytes)
    except Exception:
        return []
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = [el.text for el in root.findall(".//s:loc", ns) if el.text]
    if not locs:
        locs = [el.text for el in root.findall(".//{*}loc") if el.text]
    return locs


def save_locs(slug, name, locs):
    dest = RAW / slug / DATE / "scrapes" / name
    dest.write_text(json.dumps(locs, ensure_ascii=False, indent=2))
    return dest


# --- child sitemaps ---
jobs = [
    ("bananair", "https://bananair.fr/sitemap_pages_1.xml?from=174725300550&to=174725300550", "sitemap_pages.xml"),
    ("bananair", "https://bananair.fr/sitemap_collections_1.xml?from=680660992326&to=690879070534", "sitemap_collections.xml"),
    ("iconpouf", "https://www.iconpouf.fr/sitemap_pages_1.xml?from=701744906627&to=708763419011", "sitemap_pages.xml"),
    ("iconpouf", "https://www.iconpouf.fr/sitemap_collections_1.xml?from=700082684291&to=711191462275", "sitemap_collections.xml"),
    ("casabiloba", "https://www.casabiloba.fr/page-sitemap.xml", "page-sitemap.xml"),
    ("casabiloba", "https://www.casabiloba.fr/product_cat-sitemap.xml", "product_cat-sitemap.xml"),
    ("casabiloba", "https://www.casabiloba.fr/product-sitemap1.xml", "product-sitemap1.xml"),
    ("casabiloba", "https://www.casabiloba.fr/product-sitemap2.xml", "product-sitemap2.xml"),
    ("big-bertha-original", "https://www.bigberthaoriginal.fr/sitemap_pages_1.xml?from=16817415&to=146348802379", "sitemap_pages.xml"),
    ("big-bertha-original", "https://www.bigberthaoriginal.fr/sitemap_collections_1.xml?from=92781635&to=676436509003", "sitemap_collections.xml"),
    ("big-bertha-original", "https://www.bigberthaoriginal.fr/sitemap_blogs_1.xml", "sitemap_blogs.xml"),
]

print("=== child sitemaps ===")
for slug, url, name in jobs:
    dest = RAW / slug / DATE / "scrapes" / name
    code, n = fetch(url, dest)
    locs = parse_locs(dest.read_bytes()) if dest.exists() and dest.stat().st_size > 50 else []
    save_locs(slug, name.replace(".xml", "-locs.json"), locs)
    print(f"  {slug} {name} -> {code} {n} locs={len(locs)}")
    if locs[:8]:
        for u in locs[:12]:
            print(f"      {u}")
    time.sleep(0.2)

# Happers: extract all category/product URLs from existing sitemap
happers_xml = (RAW / "happers" / DATE / "scrapes" / "sitemap.xml").read_bytes()
happers_locs = parse_locs(happers_xml)
save_locs("happers", "sitemap-locs.json", happers_locs)
print(f"\nhappers sitemap locs {len(happers_locs)}")
cats = [u for u in happers_locs if "_c" in u or u.endswith(".html")]
print("happers sample cats/html:")
for u in happers_locs[:40]:
    print(" ", u)

# extra pages
extra_pages = [
    ("bananair", "https://bananair.fr/policies/legal-notice", "legal-notice.html"),
    ("bananair", "https://bananair.fr/policies/refund-policy", "refund-policy.html"),
    ("bananair", "https://bananair.fr/policies/shipping-policy", "shipping-policy.html"),
    ("bananair", "https://bananair.fr/policies/terms-of-service", "terms.html"),
    ("bananair", "https://bananair.fr/policies/privacy-policy", "privacy.html"),
    ("happers", "https://www.happers.fr/expedition-et-retours.html", "expedition-et-retours.html"),
    ("happers", "https://www.happers.fr/professionnels.html", "professionnels.html"),
    ("happers", "https://www.happers.fr/pouf-entant.html", "pouf-enfant.html"),
    ("happers", "https://www.happers.fr/qui-sommes-nous.html", "qui-sommes-nous.html"),
    ("happers", "https://www.happers.fr/conditions-generales-de-vente.html", "cgv.html"),
    ("happers", "https://www.happers.fr/mentions-legales.html", "mentions-legales.html"),
    ("happers", "https://www.happers.fr/pouf-poire_c106570/", "cat-pouf-poire.html"),
    ("happers", "https://www.happers.fr/poufs_c106537/", "cat-poufs.html"),
    ("casabiloba", "https://www.casabiloba.fr/categorie-produit/pouf-poire/", "cat-pouf-poire.html"),
    ("casabiloba", "https://www.casabiloba.fr/categorie-produit/poufs/", "cat-poufs.html"),
]

print("\n=== extra pages ===")
for slug, url, name in extra_pages:
    dest = RAW / slug / DATE / "scrapes" / name
    code, n = fetch(url, dest)
    print(f"  {slug} {name} -> {code} {n}")
    time.sleep(0.25)
