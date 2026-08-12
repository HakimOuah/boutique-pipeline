from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE_ROOT = Path(
    "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/"
    "boutique-seiko-mod/preuves/preuves-sourcing-api-2026-08-11-agent/"
    "1005007347658552-sources"
)

ROWS = [
    (
        "12000040362692622 | rose - Coffee",
        "rose---Coffee-12000040362692622.webp",
        "cadran-arabe-oriental-date-28-5-v-12000040362692622-rose-coffee.jpg",
    ),
    (
        "12000040362692623 | Rose Black",
        "Rose-Black-12000040362692623.webp",
        "cadran-arabe-oriental-date-28-5-v-12000040362692623-rose-black.jpg",
    ),
    (
        "12000040362692624 | Gold Black",
        "Gold-Black-12000040362692624.webp",
        "cadran-arabe-oriental-date-28-5-v-12000040362692624-gold-black.jpg",
    ),
    (
        "12000040362692625 | Rose White",
        "Rose-White-12000040362692625.webp",
        "cadran-arabe-oriental-date-28-5-v-12000040362692625-rose-white.jpg",
    ),
    (
        "12000040362692629 | Silver Green",
        "Silver-Green-12000040362692629.webp",
        "cadran-arabe-oriental-date-28-5-v-12000040362692629-silver-green.jpg",
    ),
    (
        "12000040362692631 | Silver Pink",
        "Silver-Pink-12000040362692631.webp",
        "cadran-arabe-oriental-date-28-5-v-12000040362692631-silver-pink.jpg",
    ),
]

CANVAS_W = 2400
HEADER_H = 110
ROW_H = 710
LABEL_H = 70
CELL_W = 760
GAP = 30
MARGIN_X = 30


def font(size: int):
    candidates = [
        "/System/Library/Fonts/SFNS.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def fit_square(path: Path, side: int) -> Image.Image:
    with Image.open(path) as im:
        rgb = im.convert("RGB")
        rgb.thumbnail((side, side), Image.Resampling.LANCZOS)
        tile = Image.new("RGB", (side, side), "white")
        tile.paste(rgb, ((side - rgb.width) // 2, (side - rgb.height) // 2))
        return tile


def crop_dial(path: Path, side: int) -> Image.Image:
    with Image.open(path) as im:
        rgb = im.convert("RGB")
        w, h = rgb.size
        # The generated dial occupies roughly 76% of the square. Crop around it
        # only for QA magnification; the full final remains unchanged.
        crop_side = int(min(w, h) * 0.82)
        left = (w - crop_side) // 2
        top = (h - crop_side) // 2
        crop = rgb.crop((left, top, left + crop_side, top + crop_side))
        return crop.resize((side, side), Image.Resampling.LANCZOS)


def main():
    canvas_h = HEADER_H + len(ROWS) * ROW_H
    board = Image.new("RGB", (CANVAS_W, canvas_h), "#ECE9E3")
    draw = ImageDraw.Draw(board)
    title_font = font(40)
    label_font = font(29)
    small_font = font(24)
    draw.text(
        (MARGIN_X, 26),
        "QA source exacte / rendu / zoom — item 1005007347658552",
        fill="#181818",
        font=title_font,
    )

    for idx, (label, source_name, final_name) in enumerate(ROWS):
        y0 = HEADER_H + idx * ROW_H
        draw.rectangle((0, y0, CANVAS_W, y0 + ROW_H - 1), fill="#F7F5F1")
        draw.text((MARGIN_X, y0 + 14), label, fill="#111111", font=label_font)
        cell_y = y0 + LABEL_H
        source = fit_square(SOURCE_ROOT / source_name, CELL_W)
        final = fit_square(ROOT / final_name, CELL_W)
        zoom = crop_dial(ROOT / final_name, CELL_W)
        xs = [MARGIN_X, MARGIN_X + CELL_W + GAP, MARGIN_X + 2 * (CELL_W + GAP)]
        for x, image in zip(xs, (source, final, zoom)):
            board.paste(image, (x, cell_y))
        draw.text((xs[0] + 10, cell_y + 10), "SOURCE EXACTE", fill="#111111", font=small_font)
        draw.text((xs[1] + 10, cell_y + 10), "RENDU 2048", fill="#111111", font=small_font)
        draw.text((xs[2] + 10, cell_y + 10), "ZOOM QA", fill="#111111", font=small_font)
        draw.line((0, y0 + ROW_H - 1, CANVAS_W, y0 + ROW_H - 1), fill="#BEB9B1", width=2)

    out = ROOT / "planche-qa-source-rendu-1005007347658552.jpg"
    board.save(out, format="JPEG", quality=90, optimize=True, progressive=True, icc_profile=None)
    print(out)


if __name__ == "__main__":
    main()
