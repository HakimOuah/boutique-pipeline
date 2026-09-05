#!/usr/bin/env python3
"""Extrait le texte visible des pages discours déjà téléchargées."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path

RAW = Path(
    "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/"
    "analyses/2026-09-03-univers-poufs/raw"
)
DATE = "2026-09-03"
OUT = RAW / "_scratch" / "textes"
OUT.mkdir(parents=True, exist_ok=True)

SKIP = {"script", "style", "noscript", "svg", "path", "nav", "footer"}


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.parts = []
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip += 1
        if tag == "title":
            self._in_title = True

    def handle_endtag(self, tag):
        if tag in SKIP and self.skip:
            self.skip -= 1
        if tag == "title":
            self._in_title = False
        if tag in {"p", "h1", "h2", "h3", "h4", "li", "br", "div", "tr"}:
            self.parts.append("\n")

    def handle_data(self, data):
        if self.skip:
            return
        t = data.strip()
        if not t:
            return
        if self._in_title:
            self.title += t + " "
        self.parts.append(t + " ")


def extract(path):
    raw = path.read_bytes()
    # try utf-8 then latin-1
    for enc in ("utf-8", "latin-1"):
        try:
            html = raw.decode(enc)
            break
        except Exception:
            html = raw.decode("utf-8", errors="ignore")
    p = TextExtractor()
    try:
        p.feed(html)
    except Exception:
        pass
    text = re.sub(r"[ \t]+", " ", "".join(p.parts))
    text = re.sub(r"\n{3,}", "\n\n", text)
    # drop very short cookie-only leftovers
    lines = [ln.strip() for ln in text.splitlines() if len(ln.strip()) > 2]
    # keep unique-ish consecutive
    cleaned = []
    prev = None
    for ln in lines:
        if ln == prev:
            continue
        cleaned.append(ln)
        prev = ln
    return p.title.strip(), "\n".join(cleaned)


FILES = {
    "bbo-homepage": RAW / "big-bertha-original" / DATE / "scrapes" / "homepage.html",
    "bbo-garantie": RAW / "big-bertha-original" / DATE / "scrapes" / "pages_notre-garantie.html",
    "bbo-livraison": RAW / "big-bertha-original" / DATE / "scrapes" / "pages_information-de-livraison.html",
    "bbo-retours": RAW / "big-bertha-original" / DATE / "scrapes" / "pages_retours-remboursements-et-echanges.html",
    "bbo-retractation": RAW / "big-bertha-original" / DATE / "scrapes" / "pages_annulation-et-retours.html",
    "bbo-mentions": RAW / "big-bertha-original" / DATE / "scrapes" / "pages_mentions-legales.html",
    "bbo-about": RAW / "big-bertha-original" / DATE / "scrapes" / "pages_about-us.html",
    "bananair-home": RAW / "bananair" / DATE / "scrapes" / "homepage.html",
    "bananair-legal": RAW / "bananair" / DATE / "scrapes" / "legal-notice.html",
    "bananair-shipping": RAW / "bananair" / DATE / "scrapes" / "shipping-policy.html",
    "bananair-terms": RAW / "bananair" / DATE / "scrapes" / "terms.html",
    "iconpouf-home": RAW / "iconpouf" / DATE / "scrapes" / "homepage.html",
    "iconpouf-about": RAW / "iconpouf" / DATE / "scrapes" / "pages_a-propos-de-nous.html",
    "iconpouf-cgv": RAW / "iconpouf" / DATE / "scrapes" / "pages_cgv.html",
    "iconpouf-livraison": RAW / "iconpouf" / DATE / "scrapes" / "pages_livraison.html",
    "happers-home": RAW / "happers" / DATE / "scrapes" / "homepage.html",
    "happers-expedition": RAW / "happers" / DATE / "scrapes" / "expedition-et-retours.html",
    "happers-pro": RAW / "happers" / DATE / "scrapes" / "professionnels.html",
    "happers-about": RAW / "happers" / DATE / "scrapes" / "qui-sommes-nous.html",
    "happers-poire": RAW / "happers" / DATE / "scrapes" / "cat-pouf-poire.html",
    "casabiloba-home": RAW / "casabiloba" / DATE / "scrapes" / "homepage.html",
    "casabiloba-about": RAW / "casabiloba" / DATE / "scrapes" / "pages_a-propos.html",
    "casabiloba-mentions": RAW / "casabiloba" / DATE / "scrapes" / "pages_mentions-legales.html",
    "casabiloba-contact": RAW / "casabiloba" / DATE / "scrapes" / "pages_contact.html",
    "casabiloba-poire": RAW / "casabiloba" / DATE / "scrapes" / "cat-pouf-poire.html",
}

# also leftover names
for slug, folder in [
    ("iconpouf", RAW / "iconpouf" / DATE / "scrapes"),
    ("casabiloba", RAW / "casabiloba" / DATE / "scrapes"),
]:
    pass

for name, path in FILES.items():
    if not path.exists() or path.stat().st_size < 200:
        print(f"SKIP {name} {path.exists()} size={path.stat().st_size if path.exists() else 0}")
        continue
    title, text = extract(path)
    dest = OUT / f"{name}.txt"
    dest.write_text(f"TITLE: {title}\nSOURCE: {path.name}\nLEN: {len(text)}\n\n{text}")
    print(f"OK {name} title={title[:80]!r} chars={len(text)}")
