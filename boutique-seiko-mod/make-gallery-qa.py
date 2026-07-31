import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_ROOT = PROJECT_ROOT / "scratchpad" / "noirmont-galeries"
SOURCES = json.loads((OUTPUT_ROOT / "sources.json").read_text())["entries"]
QA_ROOT = OUTPUT_ROOT / "qa"
GENERATED = OUTPUT_ROOT / "generated"

THUMB = 380
LABEL = 46
GAP = 12
BG = "#E7E4DE"


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
    ]:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def tile(image_path: Path, label: str) -> Image.Image:
    with Image.open(image_path) as source:
        source = ImageOps.exif_transpose(source).convert("RGB")
        source.thumbnail((THUMB, THUMB), Image.Resampling.LANCZOS)
        canvas = Image.new("RGB", (THUMB, THUMB + LABEL), BG)
        canvas.paste(source, ((THUMB - source.width) // 2, (THUMB - source.height) // 2))
    draw = ImageDraw.Draw(canvas)
    draw.text((10, THUMB + 9), label, fill="#0B0B0C", font=font(20))
    return canvas


def make_product_sheets() -> list[Path]:
    outputs = []
    for entry in SOURCES:
        images = [(Path(entry["entreeFace"]), "01-face")]
        for slot in entry["slots"]:
            candidate = GENERATED / f"{entry['handle']}-{slot}.jpg"
            if candidate.exists():
                images.append((candidate, slot))
        if len(images) == 1:
            continue
        tiles = [tile(image_path, label) for image_path, label in images]
        width = len(tiles) * THUMB + (len(tiles) - 1) * GAP
        sheet = Image.new("RGB", (width, THUMB + LABEL), BG)
        x = 0
        for item in tiles:
            sheet.paste(item, (x, 0))
            x += THUMB + GAP
        output = QA_ROOT / f"{entry['handle']}-planche.jpg"
        sheet.save(output, "JPEG", quality=88, optimize=True)
        outputs.append(output)
    return outputs


def make_overviews() -> list[Path]:
    files = sorted(GENERATED.glob("*.jpg"))
    outputs = []
    per_page = 16
    for page_index in range(0, len(files), per_page):
        page_files = files[page_index:page_index + per_page]
        tiles = [tile(item, item.stem[-34:]) for item in page_files]
        columns = 4
        rows = (len(tiles) + columns - 1) // columns
        sheet = Image.new(
            "RGB",
            (columns * THUMB + (columns - 1) * GAP, rows * (THUMB + LABEL) + (rows - 1) * GAP),
            BG,
        )
        for index, item in enumerate(tiles):
            x = (index % columns) * (THUMB + GAP)
            y = (index // columns) * (THUMB + LABEL + GAP)
            sheet.paste(item, (x, y))
        output = QA_ROOT / f"overview-{page_index // per_page + 1:02d}.jpg"
        sheet.save(output, "JPEG", quality=88, optimize=True)
        outputs.append(output)
    return outputs


def main() -> None:
    QA_ROOT.mkdir(parents=True, exist_ok=True)
    product_sheets = make_product_sheets()
    overviews = make_overviews()
    print(json.dumps({
        "generatedFiles": len(list(GENERATED.glob("*.jpg"))),
        "productSheets": len(product_sheets),
        "overviewPages": len(overviews),
    }, indent=2))


if __name__ == "__main__":
    main()
