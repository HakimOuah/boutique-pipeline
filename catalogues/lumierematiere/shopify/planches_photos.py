#!/usr/bin/env python3
"""Planches-contacts étiquetées des photos principales, pour trancher à l'œil
la matière (papier, osier) et l'échelle avant rattachement aux collections de pièce.

Usage : python3 planches_photos.py [LM-017 LM-022 …]  (défaut : tout le catalogue actif)
Sortie : backups/2026-08-26-collections/planches/planche-NN.jpg
"""
from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "backups" / "2026-08-26-collections" / "planches"
CACHE = ROOT / "backups" / "2026-08-26-collections" / "photos-cache"

ZOOM = "--zoom" in sys.argv
VIGNETTE = 470 if ZOOM else 300
LEGENDE = 40 if ZOOM else 34
COLS = 3 if ZOOM else 5
LIGNES = 2 if ZOOM else 4

FONTS = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
]


def police(size: int):
    for f in FONTS:
        if Path(f).exists():
            try:
                return ImageFont.truetype(f, size)
            except OSError:
                continue
    return ImageFont.load_default()


def telecharger(row: dict) -> Path | None:
    if not row["photo"]:
        return None
    CACHE.mkdir(parents=True, exist_ok=True)
    dest = CACHE / f"{row['lm']}.jpg"
    if dest.exists() and dest.stat().st_size > 1000:
        return dest
    url = row["photo"]
    url += ("&" if "?" in url else "?") + f"width={VIGNETTE * 2}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            dest.write_bytes(resp.read())
    except Exception as err:  # noqa: BLE001
        print(f"  échec {row['lm']}: {err}")
        return None
    return dest


def main() -> None:
    rows = json.loads((ROOT / "catalogue-pieces-2026-08-26.json").read_text(encoding="utf-8"))
    rows = [r for r in rows if r["lm"] and r["status"] == "ACTIVE"]
    voulus = [a.upper() for a in sys.argv[1:] if a.startswith(("LM-", "lm-"))]
    if voulus:
        rows = [r for r in rows if r["lm"] in voulus]
    OUT.mkdir(parents=True, exist_ok=True)

    f_lm = police(22)
    f_txt = police(15)
    par_planche = COLS * LIGNES
    lots = [rows[i : i + par_planche] for i in range(0, len(rows), par_planche)]
    suffixe = "-".join(voulus[:2]) if voulus else ""

    for idx, lot in enumerate(lots, 1):
        cell_h = VIGNETTE + LEGENDE
        planche = Image.new("RGB", (COLS * VIGNETTE, LIGNES * cell_h), "white")
        draw = ImageDraw.Draw(planche)
        for i, row in enumerate(lot):
            cx, cy = (i % COLS) * VIGNETTE, (i // COLS) * cell_h
            path = telecharger(row)
            if path:
                try:
                    img = Image.open(path).convert("RGB")
                    img.thumbnail((VIGNETTE - 4, VIGNETTE - 4))
                    planche.paste(img, (cx + (VIGNETTE - img.width) // 2, cy + 2))
                except Exception as err:  # noqa: BLE001
                    draw.text((cx + 8, cy + 40), f"illisible {err}"[:30], font=f_txt, fill="red")
            d = row["diametres"]
            dtxt = f"O {min(d)}-{max(d)}cm" if len(d) > 1 else (f"O {d[0]}cm" if d else "sans cote")
            draw.text((cx + 6, cy + VIGNETTE + 1), row["lm"], font=f_lm, fill="black")
            draw.text((cx + 78, cy + VIGNETTE + 4), dtxt, font=f_txt, fill="#0044cc")
            draw.text((cx + 6, cy + VIGNETTE + 20), row["title"][:44], font=f_txt, fill="#333333")
            draw.rectangle([cx, cy, cx + VIGNETTE - 1, cy + cell_h - 1], outline="#cccccc")
        nom = f"planche-{'zoom-' if ZOOM else ''}{suffixe or ''}{idx:02d}.jpg"
        planche.save(OUT / nom, quality=88)
        print(f"  {nom} · {len(lot)} fiches : {', '.join(r['lm'] for r in lot)}")


if __name__ == "__main__":
    main()
