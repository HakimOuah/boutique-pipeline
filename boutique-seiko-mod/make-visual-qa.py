from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
GENERATED = ROOT / "livraisons/visuels-2026-07-25" / "generated"
QA = ROOT / "livraisons/visuels-2026-07-25" / "qa"
QA.mkdir(parents=True, exist_ok=True)

GROUPS = {
    "chronographe": "chrono-",
    "gmt": "gmt-",
    "integrale": "integrale-",
    "heritage": "heritage-",
    "remontoir-bois": "remontoir-bois-",
    "rouleau": "rouleau-",
    "bracelets": "bracelet-",
    "tournevis": "tournevis-",
    "remontoir-collection": "remontoir-collection-",
}

font = ImageFont.load_default()

for group, prefix in GROUPS.items():
    files = sorted(GENERATED.glob(f"{prefix}*.jpg"))
    cells = []
    for file in files:
        image = Image.open(file).convert("RGB")
        image.thumbnail((320, 320))
        cell = Image.new("RGB", (340, 365), "white")
        cell.paste(image, ((340 - image.width) // 2, 0))
        ImageDraw.Draw(cell).text((8, 330), file.stem, fill="black", font=font)
        cells.append(cell)
    cols = 4
    rows = (len(cells) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 340, rows * 365), "#D8D6D1")
    for index, cell in enumerate(cells):
        sheet.paste(cell, ((index % cols) * 340, (index // cols) * 365))
    sheet.save(QA / f"planche-{group}.jpg", quality=92)

watch_files = sorted(
    list(GENERATED.glob("chrono-*.jpg"))
    + list(GENERATED.glob("gmt-*.jpg"))
    + list(GENERATED.glob("integrale-*.jpg"))
    + list(GENERATED.glob("heritage-*.jpg"))
)
crops = []
for file in watch_files:
    image = Image.open(file).convert("RGB")
    width, height = image.size
    crop = image.crop((width * 0.2, height * 0.15, width * 0.8, height * 0.75))
    crop.thumbnail((300, 300))
    cell = Image.new("RGB", (320, 345), "white")
    cell.paste(crop, ((320 - crop.width) // 2, 0))
    ImageDraw.Draw(cell).text((8, 310), file.stem, fill="black", font=font)
    crops.append(cell)
cols = 4
rows = (len(crops) + cols - 1) // cols
sheet = Image.new("RGB", (cols * 320, rows * 345), "#D8D6D1")
for index, cell in enumerate(crops):
    sheet.paste(cell, ((index % cols) * 320, (index // cols) * 345))
sheet.save(QA / "planches-cadrans-zoom.jpg", quality=94)

print(f"{sum(len(list(GENERATED.glob(f'{prefix}*.jpg'))) for prefix in GROUPS.values())} images QA")
