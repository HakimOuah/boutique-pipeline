#!/usr/bin/env python3
"""Télécharge catalogues publics Shopify + pages discours des 4 concurrents (pas BBO)."""
import json
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE = Path(
    "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/"
    "analyses/2026-09-03-univers-poufs/raw"
)
DATE = "2026-09-03"
UA = "Mozilla/5.0 (compatible; OHVentures-market-research/1.0; +https://ohventures.fr)"

COMPETITORS = {
    "bananair": {
        "origin": "https://bananair.fr",
        "pages": [
            "/",
            "/pages/a-propos",
            "/pages/a-propos-de-bananair",
            "/pages/notre-histoire",
            "/pages/mentions-legales",
            "/pages/cgv",
            "/pages/livraison",
            "/pages/livraisons",
            "/pages/retours",
            "/pages/sav",
            "/pages/garantie",
            "/pages/contact",
        ],
    },
    "iconpouf": {
        "origin": "https://www.iconpouf.fr",
        "pages": [
            "/",
            "/pages/a-propos",
            "/pages/a-propos-de-nous",
            "/pages/notre-histoire",
            "/pages/mentions-legales",
            "/pages/cgv",
            "/pages/livraison",
            "/pages/retours",
            "/pages/garantie",
            "/pages/contact",
        ],
    },
    "happers": {
        "origin": "https://www.happers.fr",
        "pages": [
            "/",
            "/pages/a-propos",
            "/pages/qui-sommes-nous",
            "/pages/notre-histoire",
            "/pages/mentions-legales",
            "/pages/cgv",
            "/pages/livraison",
            "/pages/envios",
            "/pages/retours",
            "/pages/devoluciones",
            "/pages/garantie",
            "/pages/contact",
        ],
    },
    "casabiloba": {
        "origin": "https://www.casabiloba.fr",
        "pages": [
            "/",
            "/pages/a-propos",
            "/pages/a-propos-de-nous",
            "/pages/notre-histoire",
            "/pages/mentions-legales",
            "/pages/cgv",
            "/pages/livraison",
            "/pages/retours",
            "/pages/garantie",
            "/pages/contact",
        ],
    },
}

# BBO pages discours seulement (catalogue déjà là)
BBO_PAGES = {
    "origin": "https://www.bigberthaoriginal.fr",
    "pages": [
        "/pages/notre-garantie",
        "/pages/information-de-livraison",
        "/pages/retours-remboursements-et-echanges",
        "/pages/annulation-et-retours",
        "/pages/mentions-legales",
        "/pages/a-propos",
        "/pages/a-propos-de-nous",
        "/pages/notre-histoire",
        "/pages/about-us",
        "/pages/cgv",
        "/pages/contact",
    ],
}


def fetch(url, dest, timeout=40):
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read()
            dest.write_bytes(body)
            return r.status, len(body), r.geturl()
    except urllib.error.HTTPError as e:
        dest.write_bytes(e.read() if e.fp else b"")
        return e.code, 0, url
    except Exception as e:
        dest.write_text(f"ERROR {type(e).__name__}: {e}")
        return "err", 0, url


def shopify_catalog(slug, origin):
    scrapes = BASE / slug / DATE / "scrapes"
    scrapes.mkdir(parents=True, exist_ok=True)
    log = []

    for name, path in [
        ("sitemap.xml", "/sitemap.xml"),
        ("collections.json", "/collections.json?limit=250"),
    ]:
        code, n, final = fetch(origin + path, scrapes / name)
        log.append((name, code, n, final))
        print(f"  {slug} {name} -> {code} {n} {final}")

    # products pagination
    page = 1
    while page <= 20:
        dest = scrapes / f"products-p{page}.json"
        code, n, final = fetch(
            f"{origin}/products.json?limit=250&page={page}", dest
        )
        log.append((f"products-p{page}", code, n, final))
        print(f"  {slug} products p{page} -> {code} {n}")
        if code != 200 or n < 80:
            break
        try:
            data = json.loads(dest.read_text())
            prods = data.get("products") or []
        except Exception:
            break
        if len(prods) < 250:
            break
        page += 1
        time.sleep(0.4)
    return log


def fetch_pages(slug, origin, pages):
    scrapes = BASE / slug / DATE / "scrapes"
    log = []
    for path in pages:
        name = "homepage.html" if path == "/" else path.strip("/").replace("/", "_") + ".html"
        code, n, final = fetch(origin + path, scrapes / name)
        log.append((name, code, n))
        print(f"  {slug} page {path} -> {code} {n}")
        time.sleep(0.25)
    return log


def main():
    all_log = {}
    for slug, cfg in COMPETITORS.items():
        print(f"\n=== {slug} ===")
        all_log[slug] = {
            "catalog": shopify_catalog(slug, cfg["origin"]),
            "pages": fetch_pages(slug, cfg["origin"], cfg["pages"]),
        }
        time.sleep(0.3)
    print("\n=== bbo pages discours ===")
    all_log["big-bertha-original-pages"] = fetch_pages(
        "big-bertha-original", BBO_PAGES["origin"], BBO_PAGES["pages"]
    )
    (BASE / "_scratch" / "fetch-log.json").write_text(
        json.dumps(all_log, ensure_ascii=False, indent=2, default=str)
    )
    print("done")


if __name__ == "__main__":
    main()
