#!/usr/bin/env python3
"""Fetch missing batch-2 AE products via IOP API and build ae-details-batch2.jsonl."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from build_ae_details_jsonl import transform

BATCH2_IDS = [
    "1005009004121862",
    "1005008628934110",
    "1005009384334133",
    "1005008129059364",
    "1005006404886635",
    "1005010475989306",
    "1005010682582321",
    "1005007257830581",
    "1005010522193329",
    "1005010619832012",
    "1005005754453740",
    "1005010089245113",
    "1005008660338324",
    "1005010225434888",
    "1005012474741970",
    "1005008106092465",
    "1005006443343987",
    "1005004827960013",
    "1005008690445794",
    "1005010089073999",
    "1005009207147607",
    "1005006663709819",
    "1005004434024410",
    "1005003284799451",
    "1005006172597704",
    "1005006665717226",
    "1005010114625575",
    "1005010194418494",
    "1005001628784897",
    "1005006907007557",
]

ERRORS = {
    "1005012474741970": "IOPUpstreamError | IOP error: All SKU Unsaleable | request_id=21012d2817875928839347129",
}

DIR = Path(__file__).parent
RAW_DIR = DIR / "ae-details-batch2-raw"
OUT = DIR / "ae-details-batch2.jsonl"


def fetch_via_iop(product_id: str) -> dict | None:
    """Try AliExpress IOP if credentials are available."""
    try:
        repo_root = DIR.parents[3]  # boutique-pipeline
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
    for pid in BATCH2_IDS:
        if pid in ERRORS:
            line = transform(pid, None, ERRORS[pid])
        else:
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
    return 0 if err == 0 or ok > 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
