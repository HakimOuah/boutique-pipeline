from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path

from PIL import Image, ImageCms, ImageDraw, ImageFont, ImageOps


WORKBENCH = Path(__file__).resolve().parent
REPO = WORKBENCH.parents[2]
RAW = WORKBENCH / "raw"
FINALIZED = WORKBENCH / "finalized"
QA = WORKBENCH / "qa"
DELIVERY = REPO / "boutique-seiko-mod/livraisons/visuels-codex-2026-08"
TARGET_LIST = WORKBENCH / "targets.txt"

MAPPING = {
    "montre-style-plongeuse-36-cadran-vert-g1.png": "montre-style-plongeuse-36-cadran-vert/montre-style-plongeuse-36-cadran-vert-g1.jpg",
    "montre-style-plongeuse-36-cadran-vert-g2.png": "montre-style-plongeuse-36-cadran-vert/montre-style-plongeuse-36-cadran-vert-g2.jpg",
    "montre-style-plongeuse-36-cadran-vert-g3.png": "montre-style-plongeuse-36-cadran-vert/montre-style-plongeuse-36-cadran-vert-g3.jpg",
    "montre-style-plongeuse-36-cadran-vert-g4.png": "montre-style-plongeuse-36-cadran-vert/montre-style-plongeuse-36-cadran-vert-g4.jpg",
    "montre-style-plongeuse-36-cadran-vert-g5.png": "montre-style-plongeuse-36-cadran-vert/montre-style-plongeuse-36-cadran-vert-g5.jpg",
    "montre-style-plongeuse-36-cadran-vert-v-green-sterile-dial.png": "montre-style-plongeuse-36-cadran-vert/montre-style-plongeuse-36-cadran-vert-v-green-sterile-dial.jpg",
    "montre-style-plongeuse-36-cadran-noir-g3.png": "montre-style-plongeuse-36-cadran-noir/montre-style-plongeuse-36-cadran-noir-g3.jpg",
    "coffret-douze-montres-bois-laque-noir-g2.png": "coffret-douze-montres-bois-laque-noir/coffret-douze-montres-bois-laque-noir-g2.jpg",
    "coffret-douze-montres-bois-laque-acajou-g2.png": "coffret-douze-montres-bois-laque-acajou/coffret-douze-montres-bois-laque-acajou-g2.jpg",
    "malette-quinze-montres-etanche-g3.png": "malette-quinze-montres-etanche/malette-quinze-montres-etanche-g3.jpg",
}


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in (
        Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
        Path("/Library/Fonts/Arial.ttf"),
    ):
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def expected_targets() -> set[Path]:
    return {
        REPO / line.strip()
        for line in TARGET_LIST.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }


def mapped_targets() -> set[Path]:
    return {DELIVERY / relative for relative in MAPPING.values()}


def save_jpeg(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as opened:
        image = ImageOps.exif_transpose(opened).convert("RGB")
        image = image.resize((2048, 2048), Image.Resampling.LANCZOS)
    profile = ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB")).tobytes()
    # Match this delivery lot's documented 2048 px / roughly 467-900 kB envelope.
    # Start high for sparse white-background views, then step down for detailed scenes.
    for quality in range(96, 82, -1):
        image.save(
            destination,
            "JPEG",
            quality=quality,
            optimize=True,
            progressive=False,
            icc_profile=profile,
        )
        if destination.stat().st_size <= 900_000:
            break


def tile(path: Path, label: str, crop: tuple[float, float, float, float] | None = None) -> Image.Image:
    with Image.open(path) as opened:
        image = ImageOps.exif_transpose(opened).convert("RGB")
        if crop:
            left, top, right, bottom = crop
            image = image.crop(
                (
                    round(image.width * left),
                    round(image.height * top),
                    round(image.width * right),
                    round(image.height * bottom),
                )
            )
        image.thumbnail((560, 560), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (580, 620), "#E7E4DE")
    canvas.paste(image, ((580 - image.width) // 2, 10 + (560 - image.height) // 2))
    ImageDraw.Draw(canvas).text((12, 578), label, fill="#101010", font=font(22))
    return canvas


def board(items: list[tuple[Path, str, tuple[float, float, float, float] | None]], columns: int, output: Path) -> None:
    cells = [tile(path, label, crop) for path, label, crop in items]
    rows = (len(cells) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * 580, rows * 620), "#D7D4CD")
    for index, cell in enumerate(cells):
        sheet.paste(cell, ((index % columns) * 580, (index // columns) * 620))
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, "JPEG", quality=88, optimize=True)


def create_qa() -> None:
    finals = {raw_name: FINALIZED / Path(relative).name for raw_name, relative in MAPPING.items()}
    green_names = [name for name in MAPPING if "cadran-vert" in name]
    board(
        [(finals[name], Path(name).stem, None) for name in green_names],
        3,
        QA / "01-cadran-vert-six-vues.jpg",
    )
    board(
        [
            (finals["montre-style-plongeuse-36-cadran-noir-g3.png"], "noir g3 - minuterie", None),
            (finals["coffret-douze-montres-bois-laque-noir-g2.png"], "coffret noir g2", None),
            (finals["coffret-douze-montres-bois-laque-acajou-g2.png"], "coffret acajou g2", None),
            (finals["malette-quinze-montres-etanche-g3.png"], "mallette g3 - 5 x 3", None),
        ],
        2,
        QA / "02-autres-reprises.jpg",
    )
    board(
        [
            (finals["coffret-douze-montres-bois-laque-noir-g2.png"], "noir - cadrans 12 montres", (0.08, 0.42, 0.92, 0.87)),
            (finals["coffret-douze-montres-bois-laque-acajou-g2.png"], "acajou - cadrans 12 montres", (0.08, 0.42, 0.92, 0.87)),
        ],
        2,
        QA / "03-coffrets-cadrans-zoom.jpg",
    )


def install() -> None:
    if expected_targets() != mapped_targets():
        raise RuntimeError("La liste autorisee et le mapping des sorties ne correspondent pas exactement.")
    for raw_name, relative in MAPPING.items():
        source = FINALIZED / Path(relative).name
        target = DELIVERY / relative
        temporary = target.with_name(target.name + ".codex-reprise.tmp")
        shutil.copyfile(source, temporary)
        os.replace(temporary, target)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--install", action="store_true")
    args = parser.parse_args()
    FINALIZED.mkdir(parents=True, exist_ok=True)
    for raw_name, relative in MAPPING.items():
        source = RAW / raw_name
        if not source.exists():
            raise FileNotFoundError(source)
        save_jpeg(source, FINALIZED / Path(relative).name)
    create_qa()
    if args.install:
        install()
    print(f"finalized={len(MAPPING)} installed={args.install} qa={len(list(QA.glob('*.jpg')))}")


if __name__ == "__main__":
    main()
