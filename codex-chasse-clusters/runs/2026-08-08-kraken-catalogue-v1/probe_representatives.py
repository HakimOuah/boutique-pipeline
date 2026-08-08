#!/usr/bin/env python3
"""Valide une variante et un fret France représentatifs par niche."""

from __future__ import annotations

import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
GATEWAY = ROOT / "codex-chasse-clusters" / "tools" / "aliexpress_vps_gateway.py"
OUTPUT = Path(__file__).with_name("representative-exact-probes.json")

REPRESENTATIVES = {
    "Mercerie créative & arts du fil": "1005010018907785",
    "Scrapbooking & journaling": "1005006862775811",
    "Aquariophilie & aquascaping": "1005003808164300",
    "Balade, transport & mobilité du chien": "1005005243849649",
    "Perles & création de bijoux": "1005005028774396",
}


def call(*arguments: str) -> dict:
    completed = subprocess.run(
        [sys.executable, str(GATEWAY), *arguments],
        capture_output=True,
        text=True,
        timeout=90,
        check=False,
    )
    if completed.returncode != 0:
        return {"ok": False, "error": completed.stderr[-2000:]}
    return json.loads(completed.stdout)


def probe(niche: str, product_id: str) -> dict:
    variants_payload = call("variants", product_id)
    if not variants_payload.get("ok"):
        return {"niche": niche, "product_id": product_id, "ok": False, "variants": variants_payload}
    variants = variants_payload.get("result", {}).get("variants", [])
    stocked = [row for row in variants if int(row.get("stock") or 0) > 0]
    if not stocked:
        return {"niche": niche, "product_id": product_id, "ok": False, "error": "Aucune variante en stock", "variants": variants_payload}
    chosen = max(stocked, key=lambda row: (int(row.get("stock") or 0), -float(row.get("offer_sale_price") or row.get("sku_price") or 0)))
    properties = []
    for row in chosen.get("properties", []):
        name = row.get("name")
        if not name:
            continue
        for key in ("raw_value", "value"):
            value = row.get(key)
            selector = f"{name}={value}" if value else None
            if selector and selector not in properties:
                properties.append(selector)
    exact_arguments = ["exact", product_id]
    for value in properties:
        exact_arguments.extend(["--property", value])
    exact_arguments.extend(["--destination", "FR"])
    exact_payload = call(*exact_arguments)
    return {
        "niche": niche,
        "product_id": product_id,
        "ok": bool(exact_payload.get("ok")),
        "selected_properties": properties,
        "variant_count": len(variants),
        "exact": exact_payload,
    }


def main() -> int:
    rows = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(probe, niche, product_id): niche for niche, product_id in REPRESENTATIVES.items()}
        for future in as_completed(futures):
            rows.append(future.result())
    rows.sort(key=lambda row: list(REPRESENTATIVES).index(row["niche"]))
    OUTPUT.write_text(json.dumps({"probes": rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({row["niche"]: row["ok"] for row in rows}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
