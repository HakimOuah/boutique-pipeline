#!/usr/bin/env python3
import time, urllib.request
from pathlib import Path

RAW = Path("/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/analyses/2026-09-03-univers-poufs/raw")
DATE = "2026-09-03"
UA = "Mozilla/5.0 (compatible; OHVentures-market-research/1.0)"

pages = [
    ("iconpouf", "https://www.iconpouf.fr/pages/garantie-de-qualite", "pages_garantie-de-qualite.html"),
    ("iconpouf", "https://www.iconpouf.fr/pages/design-britannique", "pages_design-britannique.html"),
    ("iconpouf", "https://www.iconpouf.fr/pages/avis-sur-icon-anciennement-beanbagbazaar", "pages_avis.html"),
    ("iconpouf", "https://www.iconpouf.fr/pages/presse-medias", "pages_presse.html"),
    ("iconpouf", "https://www.iconpouf.fr/pages/faq-1", "pages_faq.html"),
    ("casabiloba", "https://www.casabiloba.fr/mentions-legales/", "mentions-legales.html"),
    ("casabiloba", "https://www.casabiloba.fr/nos-engagements/", "nos-engagements.html"),
    ("casabiloba", "https://www.casabiloba.fr/conditions-generales-de-vente/", "cgv.html"),
    ("casabiloba", "https://www.casabiloba.fr/foire-au-question/", "faq.html"),
    ("casabiloba", "https://www.casabiloba.fr/espace-pros/", "espace-pros.html"),
    ("bananair", "https://bananair.fr/pages/notices", "pages_notices.html"),
    ("big-bertha-original", "https://www.bigberthaoriginal.fr/pages/conditions-generales", "pages_conditions-generales.html"),
    ("big-bertha-original", "https://www.bigberthaoriginal.fr/pages/contactez-nous", "pages_contactez-nous.html"),
    ("happers", "https://www.happers.fr/pouf-gamer_c107049/", "cat-pouf-gamer.html"),
    ("happers", "https://www.happers.fr/pouf-enfant_c106565/", "cat-pouf-enfant.html"),
    ("happers", "https://www.happers.fr/big-pouf_c106552/", "cat-big-pouf.html"),
    ("happers", "https://www.happers.fr/pouf-fauteuil_c106673/", "cat-pouf-fauteuil.html"),
    ("casabiloba", "https://www.casabiloba.fr/c/poufs/poufs-poire/", "c-poufs-poire.html"),
    ("casabiloba", "https://www.casabiloba.fr/c/poufs/poufs-geants/", "c-poufs-geants.html"),
    ("casabiloba", "https://www.casabiloba.fr/c/poufs/fauteuils-pouf/", "c-fauteuils-pouf.html"),
]

for slug, url, name in pages:
    dest = RAW / slug / DATE / "scrapes" / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            dest.write_bytes(r.read())
            print(f"OK {slug} {name} {len(dest.read_bytes()) if False else dest.stat().st_size}")
    except Exception as e:
        dest.write_text(f"ERROR {e}")
        print(f"FAIL {slug} {name} {e}")
    time.sleep(0.3)
