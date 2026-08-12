#!/usr/bin/env python3
"""POC local, deterministic compositing for NH34 Dial 3 hand.

The mounted SKU photo and the exact naked SKU photo are kept read-only.
Pillow is used for a reproducible affine registration, pixel-difference hand
isolation and rigid rotations around the physical pivot.  Every artifact is
written only under this scratchpad directory.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont, ImageOps, ImageStat


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
MOUNTED = ROOT / "scratchpad/remplacement-photos-aliexpress-92-2026-08-11/cadran-pilote-noir-33-5-nh34/Sf4b20fe9b3534454952eb58b10dfebb4D.webp"
NAKED = ROOT / "scratchpad/remplacement-photos-aliexpress-92-2026-08-11/cadran-pilote-noir-33-5-nh34/S0ddfc7b68b0a4f5dba36efa7cbe34a90Z.webp"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def dark_bbox(image: Image.Image, threshold: int = 80) -> tuple[int, int, int, int]:
    gray = image.convert("L")
    mask = gray.point(lambda v: 255 if v < threshold else 0)
    bbox = mask.getbbox()
    if bbox is None:
        raise RuntimeError("No dark product bbox found")
    return bbox


def naked_hole_centroid(image: Image.Image) -> tuple[float, float]:
    """Centroid of the gray central hole, selected in a conservative center ROI."""
    px = image.convert("RGB").load()
    pts: list[tuple[int, int, float]] = []
    for y in range(400, 550):
        for x in range(400, 580):
            r, g, b = px[x, y]
            value = (r + g + b) / 3
            if 70 < value < 220 and max(r, g, b) - min(r, g, b) < 50:
                pts.append((x, y, value))
    if not pts:
        raise RuntimeError("No central naked hole pixels found")
    # Prefer pixels closest to the median center of the candidate cloud.
    x0 = sum(x for x, _, _ in pts) / len(pts)
    y0 = sum(y for _, y, _ in pts) / len(pts)
    kept = [(x, y, v) for x, y, v in pts if (x - x0) ** 2 + (y - y0) ** 2 < 40**2]
    return (
        sum(x for x, _, _ in kept) / len(kept),
        sum(y for _, y, _ in kept) / len(kept),
    )


def register_naked_to_mounted(
    naked: Image.Image,
    mounted_bbox: tuple[int, int, int, int],
    naked_bbox: tuple[int, int, int, int],
) -> tuple[Image.Image, dict[str, float]]:
    sl, st, sr, sb = mounted_bbox
    nl, nt, nr, nb = naked_bbox
    sx = (sr - sl) / (nr - nl)
    sy = (sb - st) / (nb - nt)
    # Pillow AFFINE coefficients map output coordinates back to input pixels.
    coeffs = (1.0 / sx, 0.0, nl - sl / sx, 0.0, 1.0 / sy, nt - st / sy)
    registered = naked.transform(
        naked.size,
        Image.Transform.AFFINE,
        coeffs,
        resample=Image.Resampling.BICUBIC,
        fillcolor=(245, 245, 245),
    )
    return registered, {
        "scale_x": sx,
        "scale_y": sy,
        "translate_x": sl - sx * nl,
        "translate_y": st - sy * nt,
    }


def direction(angle_clockwise_from_12: float) -> tuple[float, float]:
    rad = math.radians(angle_clockwise_from_12)
    return math.sin(rad), -math.cos(rad)


def corridor_alpha(
    mounted: Image.Image,
    registered_naked: Image.Image,
    pivot: tuple[float, float],
    corridors: list[tuple[float, float, float]],
    diff_threshold: int,
    value_threshold: int,
) -> Image.Image:
    """Extract changed bright pixels inside one or more radial corridors.

    Each corridor is (angle clockwise from 12, maximum radius, half width).
    """
    w, h = mounted.size
    mp = mounted.convert("RGB").load()
    bp = registered_naked.convert("RGB").load()
    raw = Image.new("L", (w, h), 0)
    rp = raw.load()
    cx, cy = pivot
    vectors = [(direction(a), max_r, half_w) for a, max_r, half_w in corridors]
    for y in range(h):
        dy = y - cy
        for x in range(w):
            dx = x - cx
            inside = False
            for (ux, uy), max_r, half_w in vectors:
                along = dx * ux + dy * uy
                perp = abs(dx * uy - dy * ux)
                if -8 <= along <= max_r and perp <= half_w:
                    inside = True
                    break
            if not inside:
                continue
            sr, sg, sb = mp[x, y]
            br, bg, bb = bp[x, y]
            diff = max(abs(sr - br), abs(sg - bg), abs(sb - bb))
            value = (sr + sg + sb) / 3
            if diff >= diff_threshold and value >= value_threshold:
                rp[x, y] = min(255, 100 + (diff - diff_threshold) * 7)
    # Close tiny JPEG gaps and keep a softly antialiased edge.
    raw = raw.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(0.8))
    return raw


def manual_brightness_alpha(
    mounted: Image.Image,
    polygons: list[list[tuple[float, float]]],
    lines: list[tuple[tuple[float, float, float, float], int]],
    ellipses: list[tuple[float, float, float, float]],
    exclusions: list[list[tuple[float, float]]],
    value_threshold: int,
    neutral_only: bool = False,
) -> Image.Image:
    """Trace a conservative visible-piece support, then keep source material pixels.

    The support contains no inferred contour: it only limits where source pixels
    are allowed to become alpha.  JPEG-black surroundings stay transparent.
    """
    support = Image.new("L", mounted.size, 0)
    draw = ImageDraw.Draw(support)
    for polygon in polygons:
        draw.polygon(polygon, fill=255)
    for coords, width in lines:
        draw.line(coords, fill=255, width=width)
    for ellipse in ellipses:
        draw.ellipse(ellipse, fill=255)
    for polygon in exclusions:
        draw.polygon(polygon, fill=0)
    sp = support.load()
    mp = mounted.convert("RGB").load()
    alpha = Image.new("L", mounted.size, 0)
    ap = alpha.load()
    for y in range(mounted.height):
        for x in range(mounted.width):
            if not sp[x, y]:
                continue
            r, g, b = mp[x, y]
            value = (r + g + b) / 3
            if value < value_threshold:
                continue
            if neutral_only and max(r, g, b) - min(r, g, b) > 55:
                continue
            ap[x, y] = min(255, max(0, int((value - value_threshold) * 5.5 + 90)))
    return alpha.filter(ImageFilter.GaussianBlur(0.45))


def layer_from_alpha(source: Image.Image, alpha: Image.Image, pivot: tuple[float, float]) -> Image.Image:
    layer = source.convert("RGBA")
    # Remove the shared hub from individual hands. It is restored once at the end.
    a = alpha.copy()
    draw = ImageDraw.Draw(a)
    cx, cy = pivot
    draw.ellipse((cx - 22, cy - 22, cx + 22, cy + 22), fill=0)
    layer.putalpha(a)
    return layer


def rotate_about(layer: Image.Image, pivot: tuple[float, float], pil_angle: float) -> Image.Image:
    return layer.rotate(
        pil_angle,
        resample=Image.Resampling.BICUBIC,
        center=pivot,
        expand=False,
    )


def circular_hub(source: Image.Image, pivot: tuple[float, float], radius: int = 24) -> Image.Image:
    alpha = Image.new("L", source.size, 0)
    draw = ImageDraw.Draw(alpha)
    cx, cy = pivot
    draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill=255)
    alpha = alpha.filter(ImageFilter.GaussianBlur(0.6))
    layer = source.convert("RGBA")
    layer.putalpha(alpha)
    return layer


def alpha_axis_measure(alpha: Image.Image, pivot: tuple[float, float], expected: float) -> float:
    px = alpha.load()
    cx, cy = pivot
    ux, uy = direction(expected)
    sx = sy = weight = 0.0
    for y in range(alpha.height):
        dy = y - cy
        for x in range(alpha.width):
            a = px[x, y]
            if a < 32:
                continue
            dx = x - cx
            along = dx * ux + dy * uy
            if along < 45:
                continue
            w = a * along
            sx += dx * w
            sy += dy * w
            weight += w
    if weight == 0:
        raise RuntimeError("Cannot measure empty transformed alpha")
    vx, vy = sx / weight, sy / weight
    return math.degrees(math.atan2(vx, -vy)) % 360


def count_bright_overlap(
    base: Image.Image,
    alpha: Image.Image,
    pivot: tuple[float, float],
    min_radius: float = 42,
) -> int:
    bp = base.convert("RGB").load()
    ap = alpha.load()
    cx, cy = pivot
    count = 0
    for y in range(base.height):
        dy = y - cy
        for x in range(base.width):
            if ap[x, y] < 96 or (x - cx) ** 2 + dy**2 < min_radius**2:
                continue
            r, g, b = bp[x, y]
            value = (r + g + b) / 3
            if value > 125:
                count += 1
    return count


def heatmap(diff: Image.Image) -> Image.Image:
    gray = diff.convert("L").point(lambda v: min(255, v * 4))
    black = Image.new("RGB", diff.size, (0, 0, 0))
    red = Image.new("RGB", diff.size, (255, 40, 0))
    return Image.composite(red, black, gray)


def fit_panel(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    return ImageOps.fit(image.convert("RGB"), size, Image.Resampling.LANCZOS)


def make_board(
    source: Image.Image,
    naked: Image.Image,
    registered: Image.Image,
    diff_image: Image.Image,
    masks: dict[str, Image.Image],
    composite: Image.Image,
    pivot: tuple[float, float],
) -> Image.Image:
    panel = 620
    label_h = 70
    canvas = Image.new("RGB", (panel * 3, (panel + label_h) * 3 + 80), (240, 238, 232))
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default(size=26)
    items: list[tuple[str, Image.Image]] = [
        ("SOURCE MONTEE EXACTE", source),
        ("SOURCE NUE EXACTE", naked),
        ("SOURCE NUE RECALEE", registered),
        ("DIFFERENCE x4", heatmap(diff_image)),
        ("MASQUE HEURE", Image.merge("RGB", (masks["hour"],) * 3)),
        ("MASQUE MINUTE", Image.merge("RGB", (masks["minute"],) * 3)),
        ("MASQUE SECONDE", Image.merge("RGB", (masks["second"],) * 3)),
        ("POC COMPOSITE", composite),
        ("QA AXES 315 / 75 / 195", composite.copy()),
    ]
    qa = items[-1][1]
    qd = ImageDraw.Draw(qa)
    cx, cy = pivot
    for angle, color in [(315, (255, 40, 40)), (75, (40, 220, 80)), (195, (60, 120, 255))]:
        ux, uy = direction(angle)
        qd.line((cx, cy, cx + ux * 410, cy + uy * 410), fill=color, width=4)
    qd.ellipse((cx - 8, cy - 8, cx + 8, cy + 8), fill=(255, 255, 0))
    for index, (label, image) in enumerate(items):
        row, col = divmod(index, 3)
        x, y = col * panel, 80 + row * (panel + label_h)
        canvas.paste(fit_panel(image, (panel, panel)), (x, y))
        draw.text((x + 18, y + panel + 18), label, fill=(20, 20, 20), font=font)
    draw.text((24, 22), "POC COMPOSITING DETERMINISTE - NH34 DIAL 3 HAND", fill=(15, 15, 15), font=font)
    return canvas


def main() -> None:
    source_hash_before = sha256(MOUNTED)
    naked_hash_before = sha256(NAKED)
    source = Image.open(MOUNTED).convert("RGB")
    naked = Image.open(NAKED).convert("RGB")
    source_bbox = dark_bbox(source)
    naked_bbox = dark_bbox(naked)
    registered, registration = register_naked_to_mounted(naked, source_bbox, naked_bbox)

    naked_pivot = naked_hole_centroid(naked)
    pivot = (
        registration["scale_x"] * naked_pivot[0] + registration["translate_x"],
        registration["scale_y"] * naked_pivot[1] + registration["translate_y"],
    )
    diff = ImageChops.difference(source, registered)

    # Source pose measured from the exact supplier pixels, pivot to visible tip.
    source_angles = {"hour": 91.8, "minute": 358.6, "second": 166.5}
    target_angles = {"hour": 315.0, "minute": 75.0, "second": 195.0}
    masks = {
        "hour": manual_brightness_alpha(
            source,
            polygons=[[
                (478, 440), (515, 443), (696, 446), (708, 451),
                (716, 460), (739, 467), (765, 469), (765, 480),
                (739, 481), (718, 484), (707, 493), (696, 497),
                (509, 489), (480, 480),
            ]],
            lines=[],
            ellipses=[],
            exclusions=[],
            value_threshold=42,
        ),
        "minute": manual_brightness_alpha(
            source,
            polygons=[[
                (442, 435), (441, 370), (441, 236), (443, 144),
                (453, 120), (461, 98), (472, 96), (484, 118),
                (490, 143), (492, 237), (494, 371), (500, 431),
                (492, 454), (463, 455),
            ]],
            lines=[],
            ellipses=[],
            exclusions=[[
                (430, 333), (446, 324), (460, 331), (468, 348),
                (468, 373), (460, 404), (445, 412), (432, 395),
            ]],
            value_threshold=42,
        ),
        "second": manual_brightness_alpha(
            source,
            polygons=[[
                (570, 834), (583, 832), (586, 875),
                (579, 900), (570, 872),
            ]],
            lines=[((475, 458, 579, 858), 8), ((448, 374, 476, 461), 8)],
            ellipses=[(431, 326, 468, 410)],
            exclusions=[],
            value_threshold=78,
            neutral_only=True,
        ),
    }

    transformed_masks: dict[str, Image.Image] = {}
    transformed_layers: dict[str, Image.Image] = {}
    pil_rotations: dict[str, float] = {}
    for name in ("hour", "minute", "second"):
        clockwise_delta = (target_angles[name] - source_angles[name]) % 360
        if clockwise_delta > 180:
            clockwise_delta -= 360
        pil_angle = -clockwise_delta
        pil_rotations[name] = pil_angle
        layer = layer_from_alpha(source, masks[name], pivot)
        transformed_layers[name] = rotate_about(layer, pivot, pil_angle)
        transformed_masks[name] = transformed_layers[name].getchannel("A")

    composite = registered.convert("RGBA")
    for name in ("hour", "minute", "second"):
        composite = Image.alpha_composite(composite, transformed_layers[name])
    composite = Image.alpha_composite(composite, circular_hub(source, pivot))
    composite_rgb = composite.convert("RGB")

    registered_path = OUT / "dial3-01-nue-recalee.png"
    diff_path = OUT / "dial3-02-difference-x4.png"
    source.save(OUT / "dial3-00-source-montee-copie-technique.png")
    naked.save(OUT / "dial3-00-source-nue-copie-technique.png")
    registered.save(registered_path)
    heatmap(diff).save(diff_path)
    for name, mask in masks.items():
        mask.save(OUT / f"dial3-03-masque-source-{name}.png")
    for name, mask in transformed_masks.items():
        mask.save(OUT / f"dial3-04-masque-cible-{name}.png")
    composite_path = OUT / "dial3-05-poc-composite.png"
    composite_rgb.save(composite_path)
    board = make_board(source, naked, registered, diff, masks, composite_rgb, pivot)
    board_path = OUT / "dial3-06-planche-qa.jpg"
    board.save(board_path, "JPEG", quality=90, optimize=True, progressive=True)

    annulus = Image.new("L", source.size, 0)
    ad = ImageDraw.Draw(annulus)
    cx, cy = pivot
    ad.ellipse((cx - 455, cy - 455, cx + 455, cy + 455), fill=255)
    ad.ellipse((cx - 300, cy - 300, cx + 300, cy + 300), fill=0)
    registration_mae = sum(ImageStat.Stat(diff.convert("L"), annulus).mean)

    measured = {
        name: alpha_axis_measure(transformed_masks[name], pivot, target_angles[name])
        for name in transformed_masks
    }
    overlaps = {
        name: count_bright_overlap(registered, transformed_masks[name], pivot)
        for name in transformed_masks
    }
    report = {
        "poc_id": "poc-deterministic-nh34-dial3-20260811",
        "verdict": "FAIL_STRICT_NON_LIVRABLE",
        "output_is_final": False,
        "scope": "scratchpad only; no existing final/order/master/Shopify/DSers mutation",
        "source_mounted": str(MOUNTED.relative_to(ROOT)),
        "source_naked_exact": str(NAKED.relative_to(ROOT)),
        "input_sha256": {
            "mounted": source_hash_before,
            "naked": naked_hash_before,
        },
        "input_dimensions": {"mounted": source.size, "naked": naked.size},
        "registration": {
            "mounted_dark_bbox": source_bbox,
            "naked_dark_bbox": naked_bbox,
            **registration,
            "pivot_mounted_xy": [round(pivot[0], 3), round(pivot[1], 3)],
            "outer_annulus_mean_absolute_difference": round(registration_mae, 3),
        },
        "rigid_rotations": {
            name: {
                "source_angle_clockwise_from_12": source_angles[name],
                "target_angle_clockwise_from_12": target_angles[name],
                "pillow_rotation_degrees_counterclockwise": pil_rotations[name],
                "measured_output_angle": round(measured[name], 3),
                "absolute_target_error_degrees": round(
                    abs(((measured[name] - target_angles[name] + 180) % 360) - 180), 3
                ),
                "bright_witness_overlap_pixels_excluding_center": overlaps[name],
            }
            for name in ("hour", "minute", "second")
        },
        "artifacts": {
            "registered_naked": registered_path.name,
            "difference_heatmap": diff_path.name,
            "composite_poc": composite_path.name,
            "qa_board": board_path.name,
        },
        "output_sha256": {
            "composite_poc": sha256(composite_path),
            "qa_board": sha256(board_path),
        },
        "input_sha256_after": {
            "mounted": sha256(MOUNTED),
            "naked": sha256(NAKED),
        },
        "blocking_reasons": [
            "Minute measured at 72.186 degrees: 2.814 degrees from the 75-degree target, outside the maximum plus-or-minus 2-degree tolerance.",
            "Second-hand alpha overlaps 79 bright witness pixels outside the center; zero contact is required.",
            "The second-hand tip remains fragmented after conservative source-only isolation.",
            "Pixels hidden where the three hands overlap in the mounted source do not exist in either input and cannot be recovered exactly without inferred reconstruction.",
            "The exact mounted/naked photos require anisotropic registration and retain an outer-annulus MAE of 61.784, so raw subtraction is not artifact-free.",
        ],
        "demonstrated": [
            "Exact naked witness reconstructs the dial background without editing the source files.",
            "Rigid rotations about the physical pivot can place the hour and second axes within plus-or-minus 2 degrees.",
            "Manual conservative source-pixel masks remove most raw-difference ghosts, but do not satisfy strict product-fidelity QA.",
        ],
    }
    report["inputs_unchanged"] = report["input_sha256"] == report["input_sha256_after"]
    report_path = OUT / "dial3-07-rapport-poc.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
