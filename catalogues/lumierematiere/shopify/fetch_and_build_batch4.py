#!/usr/bin/env python3
"""Fetch batch-4 AE products via IOP API and build ae-details-batch4.jsonl."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from build_ae_details_jsonl import transform
from write_ae_details_batch4 import BATCH4_IDS

DIR = Path(__file__).parent
RAW_DIR = DIR / "ae-details-batch4-raw"
OUT = DIR / "ae-details-batch4.jsonl"


def fetch_via_iop(product_id: str) -> dict | None:
    try:
        repo_root = DIR.parents[3]
        sys.path.insert(0, str(repo_root))
        from aliexpress_open_api import get_product  # type: ignore

        return get_product(product_id)
    except Exception:
        return None


def load_raw(pid: str) -> dict | None:
    p = RAW_DIR / f"{pid}.json"
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return None


def save_raw(pid: str, data: dict) -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    (RAW_DIR / f"{pid}.json").write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


def main() -> int:
    lines: list[str] = []
    ok = 0
    for pid in BATCH4_IDS:
        raw = load_raw(pid)
        if raw is None:
            raw = fetch_via_iop(pid)
            if raw:
                save_raw(pid, raw)
        if raw is None:
            line = transform(pid, None, f"raw response not found for {pid}")
        else:
            line = transform(pid, raw)
        if line["error"] is None:
            ok += 1
        lines.append(json.dumps(line, ensure_ascii=False, separators=(",", ":")))
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    err = len(lines) - ok
    print(f"Wrote {len(lines)} lines ({ok} OK, {err} errors) -> {OUT}")
    return 0 if err == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
