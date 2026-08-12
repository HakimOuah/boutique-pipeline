#!/usr/bin/env python3
"""Génère les pastilles (swatches) 156x156 pour les valeurs d'option NOIRMONT."""
import json, os
from PIL import Image, ImageDraw

S = 156
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "swatches")
os.makedirs(OUT, exist_ok=True)


def hx(c):
    c = c.lstrip("#")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def base(bg):
    img = Image.new("RGB", (S, S), hx(bg))
    return img, ImageDraw.Draw(img)


def watch(path, strap, dial, counters=None, accent=None):
    """Fond = bracelet, disque = cadran, 3 petits compteurs."""
    img, d = base(strap)
    r = int(S * 0.40)
    c = S // 2
    d.ellipse([c - r, c - r, c + r, c + r], fill=hx(dial), outline=(255, 255, 255, 60))
    if counters:
        rr = int(S * 0.085)
        for (dx, dy) in [(-0.19, 0.0), (0.19, 0.0), (0.0, 0.20)]:
            cx, cy = c + int(dx * S), c + int(dy * S)
            d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=hx(counters))
    if accent:
        d.line([c, c, c, c - int(S * 0.30)], fill=hx(accent), width=5)
    img.save(path, "PNG", optimize=True)


def bracelet(path, metal, metal2=None, maille="fixe"):
    """Fond = métal (ou bicolore), motif = type de maille."""
    img, d = base(metal)
    if metal2:
        d.rectangle([S // 2, 0, S, S], fill=hx(metal2))
    dark = (0, 0, 0)
    if maille == "fixe":
        for y in range(0, S, 26):
            d.line([0, y, S, y], fill=dark, width=2)
    elif maille == "president":
        for y in range(0, S, 30):
            d.arc([-10, y, S + 10, y + 34], 0, 180, fill=dark, width=3)
    elif maille == "jubile":
        for y in range(0, S, 18):
            d.line([0, y, S, y], fill=dark, width=1)
        for x in range(0, S, 18):
            d.line([x, 0, x, S], fill=dark, width=1)
    elif maille == "3rangs":
        for x in (S // 3, 2 * S // 3):
            d.line([x, 0, x, S], fill=dark, width=3)
    elif maille == "sablee":
        import random
        random.seed(7)
        for _ in range(1400):
            x, y = random.randrange(S), random.randrange(S)
            d.point((x, y), fill=(120, 120, 120))
    img.save(path, "PNG", optimize=True)


def gmt(path, metal, metal2, dial, links):
    """Fond = métal du bracelet (bicolore si metal2), disque = cadran, rainures = maillons."""
    img, d = base(metal)
    if metal2:
        d.rectangle([S // 2, 0, S, S], fill=hx(metal2))
    if links == "president":
        for y in range(0, S, 30):
            d.arc([-10, y, S + 10, y + 34], 0, 180, fill=(0, 0, 0), width=3)
    else:
        step = 20 if links == 5 else 32
        for y in range(0, S, step):
            d.line([0, y, S, y], fill=(0, 0, 0), width=2)
    r = int(S * 0.34)
    c = S // 2
    d.ellipse([c - r, c - r, c + r, c + r], fill=hx(dial), outline=(230, 230, 230))
    img.save(path, "PNG", optimize=True)


SPECS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "specs.json")))

for s in SPECS:
    p = os.path.join(OUT, s["file"])
    k = s["kind"]
    if k == "watch":
        watch(p, s["strap"], s["dial"], s.get("counters"), s.get("accent"))
    elif k == "bracelet":
        bracelet(p, s["metal"], s.get("metal2"), s.get("maille", "fixe"))
    elif k == "gmt":
        gmt(p, s["metal"], s.get("metal2"), s["dial"], s.get("links", 3))
print("OK", len(SPECS), "->", OUT)
