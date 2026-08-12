#!/usr/bin/env python3
"""Embed sRGB in delivered variant JPEGs using their exact accepted raw PNGs.

The image executor occasionally writes a visually valid 2048 px JPEG without an
embedded ICC profile.  This helper matches each delivered JPEG to the nearest raw
PNG from the same executor session, refuses ambiguous/non-identical matches, then
re-encodes that raw once with mozjpeg/cjpeg and the macOS sRGB profile.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageChops, ImageStat


SRGB_PROFILE = Path("/System/Library/ColorSync/Profiles/sRGB Profile.icc")
FFMPEG = shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg"
CJPEG = shutil.which("cjpeg") or "/opt/homebrew/bin/cjpeg"


def preview(path: Path) -> Image.Image:
    with Image.open(path) as image:
        return image.convert("RGB").resize((128, 128), Image.Resampling.LANCZOS)


def mean_absolute_error(left: Image.Image, right: Image.Image) -> float:
    stats = ImageStat.Stat(ImageChops.difference(left, right))
    return sum(stats.mean) / 3


def encode(raw: Path, target: Path, quality: int) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        dir=target.parent, prefix=f".{target.name}.", suffix=".tmp", delete=False
    ) as tmp:
        temporary = Path(tmp.name)
    try:
        ffmpeg = subprocess.Popen(
            [
                FFMPEG,
                "-loglevel",
                "error",
                "-i",
                str(raw),
                "-vf",
                "scale=2048:2048:flags=lanczos",
                "-f",
                "image2pipe",
                "-vcodec",
                "ppm",
                "-",
            ],
            stdout=subprocess.PIPE,
        )
        assert ffmpeg.stdout is not None
        with temporary.open("wb") as output:
            cjpeg = subprocess.run(
                [
                    CJPEG,
                    "-quality",
                    str(quality),
                    "-optimize",
                    "-progressive",
                    "-sample",
                    "2x2",
                    "-icc",
                    str(SRGB_PROFILE),
                ],
                stdin=ffmpeg.stdout,
                stdout=output,
                check=False,
            )
        ffmpeg.stdout.close()
        ffmpeg_status = ffmpeg.wait()
        if ffmpeg_status or cjpeg.returncode:
            raise RuntimeError(
                f"encoding failed: ffmpeg={ffmpeg_status}, cjpeg={cjpeg.returncode}"
            )
        os.replace(temporary, target)
    finally:
        temporary.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--raw-dir", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    args = parser.parse_args()

    if not SRGB_PROFILE.is_file():
        raise SystemExit(f"missing profile: {SRGB_PROFILE}")
    if not Path(FFMPEG).is_file() or not Path(CJPEG).is_file():
        raise SystemExit("ffmpeg and cjpeg are required")

    entries = json.loads(args.manifest.read_text())
    if not isinstance(entries, list) or not entries:
        raise SystemExit("manifest must be a non-empty JSON array")
    raws = sorted(args.raw_dir.glob("*.png"))
    if not raws:
        raise SystemExit(f"no raw PNG in {args.raw_dir}")
    raw_previews = {raw: preview(raw) for raw in raws}

    matches: list[tuple[Path, Path, float]] = []
    used: set[Path] = set()
    for entry in entries:
        target = args.output_dir / entry["fichier"]
        if not target.is_file():
            raise SystemExit(f"missing delivered file: {target}")
        target_preview = preview(target)
        ranked = sorted(
            (mean_absolute_error(target_preview, image), raw)
            for raw, image in raw_previews.items()
        )
        score, raw = ranked[0]
        if score >= 2.0:
            raise SystemExit(
                f"refusing non-identical match for {target.name}: {raw.name}, MAE={score:.3f}"
            )
        if raw in used:
            raise SystemExit(f"raw reused by multiple targets: {raw}")
        used.add(raw)
        matches.append((target, raw, score))

    for target, raw, score in matches:
        with Image.open(target) as image:
            icc_size = len(image.info.get("icc_profile", b""))
        if icc_size:
            print(f"OK   {target.name}: ICC={icc_size}, raw={raw.name}, MAE={score:.3f}")
            continue
        encode(raw, target, 88)
        if target.stat().st_size < 350_000:
            encode(raw, target, 95)
        if target.stat().st_size > 1_200_000:
            encode(raw, target, 82)
        with Image.open(target) as image:
            size = image.size
            mode = image.mode
            icc_size = len(image.info.get("icc_profile", b""))
        if size != (2048, 2048) or mode != "RGB" or not icc_size:
            raise SystemExit(
                f"invalid normalized output {target}: {size}, {mode}, ICC={icc_size}"
            )
        print(
            f"FIX  {target.name}: {target.stat().st_size} bytes, ICC={icc_size}, "
            f"raw={raw.name}, MAE={score:.3f}"
        )


if __name__ == "__main__":
    main()
