from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "decor-vierge.png"
OUTPUT = ROOT / "maison-noirmont-carte-cadeau-2048.jpg"
PREVIEW = ROOT / "controle-300px.jpg"
ZOOM = ROOT / "controle-typographie-zoom.png"

BRASS = "#A98E5F"
CANVAS_SIZE = (2048, 2048)
CARD_ANGLE = 2.5


def load_variable_font(path: Path, size: int, variation: str) -> ImageFont.FreeTypeFont:
    font = ImageFont.truetype(str(path), size)
    font.set_variation_by_name(variation)
    return font


def tracked_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, tracking: int) -> float:
    widths = [draw.textlength(character, font=font) for character in text]
    return sum(widths) + tracking * max(0, len(text) - 1)


def draw_centered_tracked(
    draw: ImageDraw.ImageDraw,
    center_x: float,
    y: float,
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: str,
    tracking: int,
) -> None:
    x = center_x - tracked_width(draw, text, font, tracking) / 2
    for character in text:
        draw.text((x, y), character, font=font, fill=fill, anchor="la")
        x += draw.textlength(character, font=font) + tracking


def main() -> None:
    image = Image.open(SOURCE).convert("RGB").resize(CANVAS_SIZE, Image.Resampling.LANCZOS)

    bodoni = load_variable_font(ROOT / "fonts" / "BodoniModa.ttf", 132, "SemiBold")
    inter = load_variable_font(ROOT / "fonts" / "Inter.ttf", 57, "Medium")

    # The layer is centered on the generated card. Rotating the transparent
    # layer preserves the exact font outlines while matching the card's axis.
    text_layer = Image.new("RGBA", (1420, 520), (0, 0, 0, 0))
    draw = ImageDraw.Draw(text_layer)

    title = "MAISON NOIRMONT"
    title_box = draw.textbbox((0, 0), title, font=bodoni)
    title_y = 112 - title_box[1]
    draw.text(
        (text_layer.width / 2, title_y),
        title,
        font=bodoni,
        fill=BRASS,
        anchor="ma",
    )

    draw_centered_tracked(
        draw,
        text_layer.width / 2,
        300,
        "CARTE CADEAU",
        inter,
        BRASS,
        25,
    )

    rotated = text_layer.rotate(
        CARD_ANGLE,
        resample=Image.Resampling.BICUBIC,
        expand=True,
    )
    position = (
        round((image.width - rotated.width) / 2),
        round((image.height - rotated.height) / 2 + 8),
    )
    image.paste(rotated, position, rotated)

    image.save(OUTPUT, "JPEG", quality=90, subsampling=0, optimize=True)

    preview = image.resize((300, 300), Image.Resampling.LANCZOS)
    preview.save(PREVIEW, "JPEG", quality=94, subsampling=0, optimize=True)

    # Tight inspection crop around the complete typographic block.
    zoom = image.crop((250, 680, 1800, 1370))
    zoom.save(ZOOM, "PNG", optimize=True)

    print(f"final={OUTPUT} size={image.size}")
    print(f"preview={PREVIEW} size={preview.size}")
    print(f"zoom={ZOOM} size={zoom.size}")


if __name__ == "__main__":
    main()
