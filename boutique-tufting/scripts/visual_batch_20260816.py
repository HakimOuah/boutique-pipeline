#!/usr/bin/env python3
"""Utilities for the Tuftéo 2026-08-16 local visual batch.

The script deliberately performs only local image preparation and QA. It has no
Shopify or network integration.
"""

from __future__ import annotations

import argparse
import json
import math
import os
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont, ImageOps


CREAM = "#F7F1E8"
MAX_BYTES = 2_000_000
MIN_SIZE = 1600


def _font(size: int) -> ImageFont.ImageFont:
    candidates = (
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Helvetica.ttf",
    )
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size=size)
    return ImageFont.load_default()


def _fit_on_canvas(image: Image.Image, size: tuple[int, int], background: str = "white") -> Image.Image:
    fitted = ImageOps.contain(image.convert("RGB"), size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", size, background)
    x = (size[0] - fitted.width) // 2
    y = (size[1] - fitted.height) // 2
    canvas.paste(fitted, (x, y))
    return canvas


def make_contact_sheet(
    files: Iterable[Path],
    destination: Path,
    *,
    columns: int = 3,
    tile: int = 620,
    label_height: int = 64,
) -> None:
    items = list(files)
    if not items:
        raise ValueError("No input images")
    rows = math.ceil(len(items) / columns)
    sheet = Image.new("RGB", (columns * tile, rows * (tile + label_height)), "#E8E3DC")
    draw = ImageDraw.Draw(sheet)
    font = _font(28)

    for index, path in enumerate(items):
        row, column = divmod(index, columns)
        x, y = column * tile, row * (tile + label_height)
        with Image.open(path) as source:
            preview = _fit_on_canvas(source, (tile, tile), background="white")
        sheet.paste(preview, (x, y))
        label = path.name
        draw.rectangle((x, y + tile, x + tile, y + tile + label_height), fill="#2D2926")
        draw.text((x + 18, y + tile + 15), label, fill="white", font=font)

    destination.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(destination, "JPEG", quality=91, optimize=True, progressive=True)


def normalize_png(source: Path, destination: Path, size: int = MIN_SIZE) -> None:
    """Square an image on cream and save an optimized PNG under 2 MB.

    Generated images are normally square already. Padding is used only when the
    source is not square; the product is never cropped.
    """
    with Image.open(source) as loaded:
        rgb = loaded.convert("RGB")
        normalized = _fit_on_canvas(rgb, (size, size), background=CREAM)

    destination.parent.mkdir(parents=True, exist_ok=True)
    normalized.save(destination, "PNG", optimize=True, compress_level=9)
    if destination.stat().st_size <= MAX_BYTES:
        return

    # A high-quality adaptive palette keeps texture while meeting the hard GMC
    # transport limit requested for this batch.
    quantized = normalized.quantize(colors=256, method=Image.Quantize.FASTOCTREE)
    quantized.save(destination, "PNG", optimize=True, compress_level=9)
    if destination.stat().st_size > MAX_BYTES:
        raise ValueError(f"{destination.name} remains over 2 MB after optimization")


def make_control_board(files: Iterable[Path], destination: Path) -> None:
    make_contact_sheet(files, destination, columns=5, tile=480, label_height=72)


def audit(directory: Path) -> int:
    mapping_path = directory / "mapping.json"
    if not mapping_path.exists():
        print("FAIL mapping.json missing")
        return 1
    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
    if not isinstance(mapping, list) or len(mapping) != 26:
        print(f"FAIL mapping entries={len(mapping) if isinstance(mapping, list) else 'not-list'}")
        return 1

    required = {"fichier", "handle_produit", "variante", "role"}
    failures: list[str] = []
    names: list[str] = []
    for index, entry in enumerate(mapping, start=1):
        if set(entry) != required:
            failures.append(f"entry {index}: fields={sorted(entry)}")
            continue
        names.append(entry["fichier"])

    if len(set(names)) != 26:
        failures.append("mapping contains duplicate filenames")

    for name in names:
        path = directory / name
        if not path.is_file():
            failures.append(f"missing {name}")
            continue
        try:
            with Image.open(path) as image:
                if image.width != image.height or image.width < MIN_SIZE:
                    failures.append(f"{name}: {image.width}x{image.height}")
                if image.format != "PNG":
                    failures.append(f"{name}: format={image.format}")
        except Exception as exc:  # pragma: no cover - diagnostic path
            failures.append(f"{name}: unreadable ({exc})")
        size = path.stat().st_size
        if size >= MAX_BYTES:
            failures.append(f"{name}: {size} bytes")

    root_pngs = {
        path.name for path in directory.glob("*.png")
        if path.name != "planche-controle-17-cones.png"
    }
    if root_pngs != set(names):
        failures.append(
            "root PNG set differs from mapping: "
            f"extra={sorted(root_pngs - set(names))}, missing={sorted(set(names) - root_pngs)}"
        )

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1
    print("PASS mapping=26 files=26 dimensions>=1600 square format=PNG size<2MB")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    sheet_parser = subparsers.add_parser("contact-sheet")
    sheet_parser.add_argument("destination", type=Path)
    sheet_parser.add_argument("files", type=Path, nargs="+")
    sheet_parser.add_argument("--columns", type=int, default=3)

    normalize_parser = subparsers.add_parser("normalize")
    normalize_parser.add_argument("source", type=Path)
    normalize_parser.add_argument("destination", type=Path)

    board_parser = subparsers.add_parser("control-board")
    board_parser.add_argument("destination", type=Path)
    board_parser.add_argument("files", type=Path, nargs="+")

    audit_parser = subparsers.add_parser("audit")
    audit_parser.add_argument("directory", type=Path)

    args = parser.parse_args()
    if args.command == "contact-sheet":
        make_contact_sheet(args.files, args.destination, columns=args.columns)
        return 0
    if args.command == "normalize":
        normalize_png(args.source, args.destination)
        return 0
    if args.command == "control-board":
        make_control_board(args.files, args.destination)
        return 0
    if args.command == "audit":
        return audit(args.directory)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
