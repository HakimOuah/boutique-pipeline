#!/usr/bin/env python3
"""Generate deterministic PNG brand marks from the approved visual briefs."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
ORYS = ROOT / "orysbain" / "livraisons-visuels-codex" / "brand"
LM = ROOT / "lumierematiere" / "livraisons-visuels-codex" / "brand"
SANS = "/System/Library/Fonts/Avenir Next.ttc"
SERIF = "/System/Library/Fonts/Supplemental/Baskerville.ttc"


def font(path: str, size: int, index: int = 0) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size, index=index)


def save_orysbain(path: Path, color: str, favicon: bool = False) -> None:
    size = (512, 512) if favicon else (1800, 520)
    im = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if favicon:
        box = (82, 82, 430, 430)
        width = 28
        d.ellipse(box, outline=color, width=width)
        for y in (192, 256, 320):
            d.line((160, y, 352, y), fill=color, width=22)
    else:
        box = (70, 85, 405, 420)
        width = 24
        d.ellipse(box, outline=color, width=width)
        for y in (190, 252, 314):
            d.line((145, y, 330, y), fill=color, width=20)
        d.text((490, 151), "ORYSBAIN", fill=color, font=font(SANS, 150, 0), stroke_width=0)
    im.save(path, format="PNG", optimize=True)


def save_lm(path: Path, color: str, halo: str | None, favicon: bool = False) -> None:
    size = (512, 512) if favicon else (2000, 620)
    im = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if favicon:
        cx, cy, r = 256, 288, 116
        d.line((cx, 70, cx, cy-r), fill=color, width=22)
        if halo:
            d.ellipse((cx-r-28, cy-r-28, cx+r+28, cy+r+28), outline=halo, width=12)
        d.ellipse((cx-r, cy-r, cx+r, cy+r), outline=color, width=24)
    else:
        cx, cy, r = 220, 322, 120
        d.line((cx, 55, cx, cy-r), fill=color, width=18)
        if halo:
            d.ellipse((cx-r-28, cy-r-28, cx+r+28, cy+r+28), outline=halo, width=10)
        d.ellipse((cx-r, cy-r, cx+r, cy+r), outline=color, width=20)
        d.text((430, 105), "LUMIÈRE", fill=color, font=font(SERIF, 145, 0))
        d.text((437, 300), "MATIÈRE", fill=color, font=font(SANS, 105, 0))
    im.save(path, format="PNG", optimize=True)


def main() -> None:
    ORYS.mkdir(parents=True, exist_ok=True)
    LM.mkdir(parents=True, exist_ok=True)
    save_orysbain(ORYS / "orysbain-logo-primary-ardoise.png", "#26343C")
    save_orysbain(ORYS / "orysbain-logo-inverse-blanc.png", "#FFFFFF")
    save_orysbain(ORYS / "orysbain-logo-mono-cuivre.png", "#B25A28")
    save_orysbain(ORYS / "orysbain-favicon-512.png", "#26343C", favicon=True)
    save_lm(LM / "lumierematiere-logo-primary-charbon.png", "#24211B", "#C08A2D")
    save_lm(LM / "lumierematiere-logo-inverse-blanc.png", "#FFFFFF", None)
    save_lm(LM / "lumierematiere-logo-mono-ambre.png", "#C08A2D", None)
    save_lm(LM / "lumierematiere-favicon-512.png", "#24211B", "#C08A2D", favicon=True)


if __name__ == "__main__":
    main()
