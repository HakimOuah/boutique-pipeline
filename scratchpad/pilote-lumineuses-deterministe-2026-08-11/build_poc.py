#!/usr/bin/env python3
"""Deterministic proof-of-concept for the five blocked mounted dial variants.

This script never reads or writes the contractual final-image directory.  It
uses an already QA-passed dial-only witness as the clean plate and the exact
isolated supplier hand-set image as the only source for hand geometry/color.
Each hand is segmented, its principal axis is measured, and the extracted
pixels are rotated rigidly to the requested clock angles.

Pillow only; no generative model, inpainting, cloning, or free redrawing.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageOps


REPO = Path(__file__).resolve().parents[2]
SCRATCH = Path(__file__).resolve().parent
MASKS = SCRATCH / "masks"

HANDSET_B = REPO / (
    "scratchpad/remplacement-photos-aliexpress-92-2026-08-11/"
    "cadran-pilote-33-5-aiguilles-lumineuses/"
    "Sf71e5e2cee0d4162a367ac9a6e5798cb3.webp"
)
CLEAN_DIAL = REPO / (
    "boutique-seiko-mod/livraisons/visuels-codex-2026-08/"
    "cadran-pilote-33-5-aiguilles-lumineuses/"
    "cadran-pilote-33-5-aiguilles-lumineuses-v-black-dial-1.jpg"
)

POC = SCRATCH / "poc-black-dial-1-deterministic.png"
QA = SCRATCH / "poc-black-dial-1-qa-overlay.png"
METRICS = SCRATCH / "poc-black-dial-1-metrics.json"

# Measured central pivot of supplier hand-set B.  It is the center of the
# circular red seconds hub, checked at native 1000 x 1000 resolution.
SOURCE_PIVOT = (445.0, 372.0)

# Clock convention: 0 degrees = 12 h, increasing clockwise.
TARGETS = {"hour": 315.0, "minute": 105.0, "second": 195.0}

# Broad source-axis seeds and geometry corridors.  PCA below refines every
# seed from the actual source pixels before any rotation.
SPECS = {
    "hour": {
        "seed": 310.0,
        "seed_halfwidth": 12.0,
        "along_min": 42.0,
        # The isolated asset's Tandorio mark begins beyond the physical hour
        # hand tip.  Native-pixel inspection places the real tip below 330 px.
        "along_max": 330.0,
        "perp": 38.0,
    },
    "minute": {
        "seed": 58.0,
        "seed_halfwidth": 10.0,
        "along_min": 42.0,
        "along_max": 590.0,
        "perp": 38.0,
    },
    "second": {
        "seed": 184.0,
        "seed_halfwidth": 7.0,
        "along_min": -225.0,
        "along_max": 650.0,
        "perp": 19.0,
    },
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def clock_unit(angle_degrees: float) -> tuple[float, float]:
    radians = math.radians(angle_degrees)
    return math.sin(radians), -math.cos(radians)


def circular_delta(a: float, b: float) -> float:
    return ((a - b + 180.0) % 360.0) - 180.0


def source_strength(rgb: tuple[int, int, int]) -> int:
    # Supplier background is nominal white.  Maximum channel departure keeps
    # pale blue lume and metallic edges that a grayscale threshold would lose.
    r, g, b = rgb
    return max(255 - r, 255 - g, 255 - b)


def keep_components_reaching_pivot_band(
    mask: Image.Image, pivot: tuple[float, float], max_min_radius: float = 70.0
) -> Image.Image:
    """Discard detached print/noise while retaining physical hand material.

    Every real hand half begins at the excluded center-hub band, so its light
    material component reaches r < 70 px.  The supplier logo sits hundreds of
    pixels away and is therefore removed without painting over source pixels.
    """
    cx, cy = pivot
    pixels = mask.load()
    remaining = {
        (x, y)
        for y in range(mask.height)
        for x in range(mask.width)
        if pixels[x, y]
    }
    kept: list[tuple[int, int]] = []
    while remaining:
        seed = remaining.pop()
        component = [seed]
        queue = [seed]
        min_radius = math.hypot(seed[0] - cx, seed[1] - cy)
        for x, y in queue:
            for neighbor in (
                (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                (x - 1, y),                     (x + 1, y),
                (x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
            ):
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    queue.append(neighbor)
                    component.append(neighbor)
                    min_radius = min(
                        min_radius,
                        math.hypot(neighbor[0] - cx, neighbor[1] - cy),
                    )
        if len(component) >= 20 and min_radius <= max_min_radius:
            kept.extend(component)
    result = Image.new("L", mask.size, 0)
    rp = result.load()
    for x, y in kept:
        rp[x, y] = 255
    return result


def broad_pixels(
    image: Image.Image,
    pivot: tuple[float, float],
    seed: float,
    seed_halfwidth: float,
    along_min: float,
    along_max: float,
) -> list[tuple[float, float, int]]:
    cx, cy = pivot
    ux, uy = clock_unit(seed)
    result: list[tuple[float, float, int]] = []
    pixels = image.load()
    radius = max(abs(along_min), abs(along_max)) + 60
    x0 = max(0, int(cx - radius))
    x1 = min(image.width, int(cx + radius + 1))
    y0 = max(0, int(cy - radius))
    y1 = min(image.height, int(cy + radius + 1))
    for y in range(y0, y1):
        for x in range(x0, x1):
            dx, dy = x - cx, y - cy
            along = dx * ux + dy * uy
            if not (along_min <= along <= along_max):
                continue
            angle = math.degrees(math.atan2(dx, -dy)) % 360.0
            # Seconds includes the counterweight exactly opposite its seed.
            d = min(
                abs(circular_delta(angle, seed)),
                abs(circular_delta(angle, (seed + 180.0) % 360.0)),
            )
            if d > seed_halfwidth:
                continue
            strength = source_strength(pixels[x, y])
            if strength >= 7:
                result.append((dx, dy, strength))
    return result


def principal_clock_angle(
    points: list[tuple[float, float, int]], expected: float
) -> float:
    if len(points) < 50:
        raise RuntimeError(f"Insufficient foreground pixels: {len(points)}")
    total = sum(weight for _, _, weight in points)
    mx = sum(x * weight for x, _, weight in points) / total
    my = sum(y * weight for _, y, weight in points) / total
    sxx = sum(weight * (x - mx) ** 2 for x, y, weight in points) / total
    syy = sum(weight * (y - my) ** 2 for x, y, weight in points) / total
    sxy = sum(weight * (x - mx) * (y - my) for x, y, weight in points) / total
    # Principal direction in image Cartesian coordinates (x right, y down).
    phi = 0.5 * math.atan2(2.0 * sxy, sxx - syy)
    vx, vy = math.cos(phi), math.sin(phi)
    angle = math.degrees(math.atan2(vx, -vy)) % 360.0
    opposite = (angle + 180.0) % 360.0
    return angle if abs(circular_delta(angle, expected)) <= abs(
        circular_delta(opposite, expected)
    ) else opposite


def make_hand_layer(
    source: Image.Image,
    pivot: tuple[float, float],
    measured_angle: float,
    spec: dict[str, float],
    name: str,
    masks_dir: Path,
) -> tuple[Image.Image, dict[str, object]]:
    cx, cy = pivot
    ux, uy = clock_unit(measured_angle)
    source_pixels = source.load()
    material = Image.new("L", source.size, 0)
    material_pixels = material.load()
    alpha = Image.new("L", source.size, 0)
    selected = 0
    projections: list[float] = []
    for y in range(source.height):
        for x in range(source.width):
            dx, dy = x - cx, y - cy
            along = dx * ux + dy * uy
            perp = abs(dx * uy - dy * ux)
            if not (spec["along_min"] <= along <= spec["along_max"]):
                continue
            if perp > spec["perp"]:
                continue
            strength = source_strength(source_pixels[x, y])
            if strength < 4:
                continue
            # Matte-aware alpha, retaining pale lume while suppressing WebP
            # background noise.  r<40 is excluded from hand layers and is
            # restored once, from the exact source center cap.
            if math.hypot(dx, dy) < 40.0:
                continue
            # Build the material core first.  This rejects the supplier's
            # near-black Tandorio letters while keeping pale lume, red paint,
            # and bright metal.  Dark hand outlines are restored only when
            # they lie within four source pixels of this physical core.
            if max(source_pixels[x, y]) >= 120 and strength >= 7:
                material_pixels[x, y] = 255

    material = keep_components_reaching_pivot_band(material, pivot)
    allowed = material.filter(ImageFilter.MaxFilter(9))
    allowed_pixels = allowed.load()
    alpha_pixels = alpha.load()
    for y in range(source.height):
        for x in range(source.width):
            if allowed_pixels[x, y] == 0:
                continue
            dx, dy = x - cx, y - cy
            along = dx * ux + dy * uy
            perp = abs(dx * uy - dy * ux)
            if not (spec["along_min"] <= along <= spec["along_max"]):
                continue
            if perp > spec["perp"] or math.hypot(dx, dy) < 40.0:
                continue
            strength = source_strength(source_pixels[x, y])
            if strength < 4:
                continue
            value = min(255, max(0, round((strength - 3) * 21.25)))
            alpha_pixels[x, y] = value
            if value >= 96:
                selected += 1
                projections.append(along)

    # Preserve the source antialiasing without dilating white matte pixels.
    alpha = alpha.filter(ImageFilter.GaussianBlur(0.30))
    layer = source.copy().convert("RGBA")
    layer.putalpha(alpha)
    bbox = alpha.getbbox()
    if bbox is None:
        raise RuntimeError(f"Empty mask for {name}")
    masks_dir.mkdir(parents=True, exist_ok=True)
    alpha.save(masks_dir / f"handset-b-{name}-alpha.png")
    return layer, {
        "measured_source_angle_degrees": round(measured_angle, 5),
        "target_angle_degrees": TARGETS[name],
        "rigid_clockwise_rotation_degrees": round(
            circular_delta(TARGETS[name], measured_angle), 5
        ),
        "mask_bbox": list(bbox),
        "opaque_pixel_count": selected,
        "source_projection_min": round(min(projections), 3),
        "source_projection_max": round(max(projections), 3),
    }


def make_cap(
    source: Image.Image, pivot: tuple[float, float], masks_dir: Path
) -> Image.Image:
    cx, cy = pivot
    alpha = Image.new("L", source.size, 0)
    ap = alpha.load()
    for y in range(max(0, int(cy - 30)), min(source.height, int(cy + 31))):
        for x in range(max(0, int(cx - 30)), min(source.width, int(cx + 31))):
            distance = math.hypot(x - cx, y - cy)
            if distance <= 26.0:
                # The supplier center hub fully covers this circle.  A soft
                # 2 px edge avoids a pasted boundary without changing shape.
                ap[x, y] = 255 if distance <= 24.0 else int((26.0 - distance) * 127.5)
    alpha.save(masks_dir / "handset-b-center-cap-alpha.png")
    layer = source.copy().convert("RGBA")
    layer.putalpha(alpha)
    return layer


def dial_geometry(clean: Image.Image) -> tuple[tuple[float, float], float, list[int]]:
    gray = ImageOps.grayscale(clean)
    dark = gray.point(lambda value: 255 if value < 80 else 0, "L")
    bbox = dark.getbbox()
    if bbox is None:
        raise RuntimeError("Could not locate dark dial")
    left, top, right, bottom = bbox
    center = ((left + right - 1) / 2.0, (top + bottom - 1) / 2.0)
    radius = ((right - left) + (bottom - top)) / 4.0
    return center, radius, [left, top, right, bottom]


def transform_layer(
    layer: Image.Image,
    source_pivot: tuple[float, float],
    measured_angle: float,
    target_angle: float,
    scale: float,
    target_size: tuple[int, int],
    target_center: tuple[float, float],
) -> Image.Image:
    clockwise = circular_delta(target_angle, measured_angle)
    # Pillow positive rotation is visual counter-clockwise; negate clock delta.
    rotated = layer.rotate(
        -clockwise,
        resample=Image.Resampling.BICUBIC,
        center=source_pivot,
        expand=False,
    )
    scaled_size = (
        int(round(rotated.width * scale)),
        int(round(rotated.height * scale)),
    )
    scaled = rotated.resize(scaled_size, Image.Resampling.LANCZOS)
    sx, sy = source_pivot[0] * scale, source_pivot[1] * scale
    offset = (
        int(round(target_center[0] - sx)),
        int(round(target_center[1] - sy)),
    )
    canvas = Image.new("RGBA", target_size, (0, 0, 0, 0))
    canvas.alpha_composite(scaled, offset)
    return canvas


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--hour-max",
        type=float,
        default=SPECS["hour"]["along_max"],
        help="Maximum native-pixel hour-hand projection retained in the mask.",
    )
    parser.add_argument(
        "--suffix",
        default="",
        help="Optional suffix for an isolated QA run; leaves baseline artifacts intact.",
    )
    args = parser.parse_args()
    specs = copy.deepcopy(SPECS)
    specs["hour"]["along_max"] = args.hour_max
    suffix = f"-{args.suffix}" if args.suffix else ""
    poc_path = SCRATCH / f"poc-black-dial-1-deterministic{suffix}.png"
    qa_path = SCRATCH / f"poc-black-dial-1-qa-overlay{suffix}.png"
    metrics_path = SCRATCH / f"poc-black-dial-1-metrics{suffix}.json"
    masks_dir = SCRATCH / (f"masks-{args.suffix}" if args.suffix else "masks")

    SCRATCH.mkdir(parents=True, exist_ok=True)
    masks_dir.mkdir(parents=True, exist_ok=True)
    source = Image.open(HANDSET_B).convert("RGB")
    clean = Image.open(CLEAN_DIAL).convert("RGB")
    target_center, dial_radius, dial_bbox = dial_geometry(clean)

    measured: dict[str, float] = {}
    layers: dict[str, Image.Image] = {}
    metrics: dict[str, object] = {}
    for name, spec in specs.items():
        points = broad_pixels(
            source,
            SOURCE_PIVOT,
            spec["seed"],
            spec["seed_halfwidth"],
            spec["along_min"],
            spec["along_max"],
        )
        angle = principal_clock_angle(points, spec["seed"])
        measured[name] = angle
        layer, data = make_hand_layer(
            source, SOURCE_PIVOT, angle, spec, name, masks_dir
        )
        layers[name] = layer
        data["pca_input_pixel_count"] = len(points)
        metrics[name] = data

    # Preserve the complete hand-set's relative proportions.  The uniform
    # scale maps the supplier minute hand to 72% of the measured dial radius.
    minute_length = float(metrics["minute"]["source_projection_max"])
    scale = (dial_radius * 0.72) / minute_length

    composite = clean.convert("RGBA")
    # Physical stack order: hour below minute, seconds above both, then hub.
    for name in ("hour", "minute", "second"):
        transformed = transform_layer(
            layers[name],
            SOURCE_PIVOT,
            measured[name],
            TARGETS[name],
            scale,
            clean.size,
            target_center,
        )
        composite = Image.alpha_composite(composite, transformed)

    cap = transform_layer(
        make_cap(source, SOURCE_PIVOT, masks_dir),
        SOURCE_PIVOT,
        0.0,
        0.0,
        scale,
        clean.size,
        target_center,
    )
    composite = Image.alpha_composite(composite, cap)
    composite.convert("RGB").save(poc_path, "PNG", optimize=True)

    overlay = composite.convert("RGB")
    draw = ImageDraw.Draw(overlay)
    colors = {"hour": (30, 200, 255), "minute": (255, 190, 0), "second": (255, 50, 100)}
    for name, target in TARGETS.items():
        ux, uy = clock_unit(target)
        length = dial_radius * 0.90
        end = (
            target_center[0] + ux * length,
            target_center[1] + uy * length,
        )
        draw.line([target_center, end], fill=colors[name], width=3)
    cx, cy = target_center
    draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], outline=(255, 255, 0), width=3)
    overlay.save(qa_path, "PNG", optimize=True)

    report = {
        "method": "deterministic segmentation + PCA axis measurement + rigid rotation + uniform compositing",
        "generation_model": None,
        "contractual_final_modified": False,
        "hour_mask_projection_max_requested": args.hour_max,
        "inputs": {
            "exact_isolated_handset_b": str(HANDSET_B.relative_to(REPO)),
            "exact_isolated_handset_b_sha256": sha256(HANDSET_B),
            "qa_passed_clean_dial_witness": str(CLEAN_DIAL.relative_to(REPO)),
            "qa_passed_clean_dial_witness_sha256": sha256(CLEAN_DIAL),
        },
        "source_pivot": list(SOURCE_PIVOT),
        "dial_geometry": {
            "bbox": dial_bbox,
            "center": [round(target_center[0], 3), round(target_center[1], 3)],
            "radius": round(dial_radius, 3),
        },
        "uniform_scale": round(scale, 8),
        "hands": metrics,
        "outputs": {
            "poc": str(poc_path.relative_to(REPO)),
            "poc_sha256": sha256(poc_path),
            "qa_overlay": str(qa_path.relative_to(REPO)),
            "qa_overlay_sha256": sha256(qa_path),
            "masks": {
                path.name: sha256(path) for path in sorted(masks_dir.glob("*.png"))
            },
        },
    }
    metrics_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
