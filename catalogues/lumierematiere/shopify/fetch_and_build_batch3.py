#!/usr/bin/env python3
"""Fetch batch-3 AE products via IOP API and build ae-details-batch3.jsonl."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from build_ae_details_jsonl import transform

BATCH3_IDS = [
    "1005012788134962",
    "1005007456795468",
    "1005003723641905",
    "1005010262892612",
    "1005009844141724",
    "1005005376264869",
    "1005007005677865",
    "1005007805560904",
    "1005009437347688",
    "1005006787841671",
    "1005005437202521",
    "1005003775436718",
    "1005005913394147",
    "1005011786489156",
    "1005004619091815",
    "1005010430446435",
    "1005011548201424",
    "1005009132554061",
    "1005003147651675",
    "1005009654928640",
    "1005007559814554",
    "1005005664442025",
    "1005007548183789",
    "1005007972698635",
    "1005005350922186",
    "1005003449728204",
    "1005010487465027",
    "1005009550992600",
    "1005009786354637",
    "1005009085637673",
]

DIR = Path(__file__).parent
RAW_DIR = DIR / "ae-details-batch3-raw"
OUT = DIR / "ae-details-batch3.jsonl"


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
    for pid in BATCH3_IDS:
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
