#!/usr/bin/env python3
"""Transform AliExpress product.get result dicts into ae-details JSONL lines."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

IMAGE_HASH_RE = re.compile(r"/kf/([^./?;]+)")


def extract_image_hashes(image_urls: str | None) -> list[str]:
    if not image_urls:
        return []
    seen: set[str] = set()
    hashes: list[str] = []
    for part in image_urls.split(";"):
        part = part.strip()
        if not part:
            continue
        match = IMAGE_HASH_RE.search(part)
        if match:
            h = match.group(1)
            if h not in seen:
                seen.add(h)
                hashes.append(h)
    return hashes


def extract_skus(data: dict[str, Any]) -> list[dict[str, Any]]:
    sku_root = data.get("ae_item_sku_info_dtos") or {}
    sku_list = sku_root.get("ae_item_sku_info_d_t_o") or []
    skus: list[dict[str, Any]] = []
    for sku in sku_list:
        skus.append(
            {
                "sku_attr": sku.get("sku_attr"),
                "sku_id": sku.get("sku_id"),
                "offer_sale_price": sku.get("offer_sale_price"),
                "sku_price": sku.get("sku_price"),
                "currency_code": sku.get("currency_code"),
                "price_include_tax": sku.get("price_include_tax"),
            }
        )
    return skus


def transform(product_id: str, data: dict[str, Any] | None, error: str | None = None) -> dict[str, Any]:
    if error or not data:
        return {
            "product_id": product_id,
            "subject": None,
            "image_hashes": [],
            "skus": [],
            "store_country": None,
            "error": error or "unknown error",
        }
    base = data.get("ae_item_base_info_dto") or {}
    multimedia = data.get("ae_multimedia_info_dto") or {}
    store = data.get("ae_store_info") or {}
    return {
        "product_id": product_id,
        "subject": base.get("subject"),
        "image_hashes": extract_image_hashes(multimedia.get("image_urls")),
        "skus": extract_skus(data),
        "store_country": store.get("store_country_code"),
        "error": None,
    }


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: build_ae_details_jsonl.py <output.jsonl> <product_id:raw.json> ...", file=sys.stderr)
        return 1
    out_path = Path(sys.argv[1])
    lines: list[str] = []
    for arg in sys.argv[2:]:
        pid, _, raw_path = arg.partition(":")
        raw = json.loads(Path(raw_path).read_text(encoding="utf-8"))
        if isinstance(raw, dict) and raw.get("error"):
            line = transform(pid, None, str(raw["error"]))
        else:
            line = transform(pid, raw)
        lines.append(json.dumps(line, ensure_ascii=False, separators=(",", ":")))
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    ok = sum(1 for l in lines if json.loads(l)["error"] is None)
    print(f"Wrote {len(lines)} lines ({ok} OK, {len(lines) - ok} errors) -> {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
