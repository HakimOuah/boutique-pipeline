#!/usr/bin/env python3
"""Build ae-details-batch1.jsonl from raw MCP response JSON files."""

from __future__ import annotations

import json
from pathlib import Path

from build_ae_details_jsonl import transform

BATCH1_IDS = [
    "1005009535104055",
    "1005008749317565",
    "1005007291942503",
    "1005009962805884",
    "1005008589033589",
    "1005007765962644",
    "1005009022655008",
    "1005007355067987",
    "1005010089191307",
    "1005009660136557",
    "1005009418655463",
    "1005009521236157",
    "1005009039280004",
    "1005009858630923",
    "1005006242583180",
    "1005010542377816",
    "1005010322605780",
    "1005012736761433",
    "1005007582443915",
    "1005008895897170",
    "1005005998420069",
    "1005007707435189",
    "1005008694469688",
    "1005009970623305",
    "1005008876489600",
    "1005009604865596",
    "1005009105607504",
    "1005008599272937",
    "1005012464535545",
    "1005010363477244",
]

RAW_DIR = Path(__file__).parent / "ae-details-batch1-raw"
BATCH2_RAW = Path(__file__).parent / "ae-details-batch2-raw"
AGENT_TOOLS = Path.home() / ".cursor/projects/Users-Hakim-Documents-Boutiques-drop/agent-tools"
OUT = Path(__file__).parent / "ae-details-batch1.jsonl"

_INDEX: dict[str, dict] | None = None


def _product_id(data: dict) -> str:
    return str(
        data.get("ae_item_base_info_dto", {}).get("product_id")
        or data.get("product_id_converter_result", {}).get("main_product_id")
        or ""
    )


def _build_index() -> dict[str, dict]:
    index: dict[str, dict] = {}
    for raw_dir in (RAW_DIR, BATCH2_RAW):
        if not raw_dir.is_dir():
            continue
        for p in raw_dir.glob("*.json"):
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
                pid = _product_id(data)
                if pid:
                    index[pid] = data
            except Exception:
                continue
    if AGENT_TOOLS.is_dir():
        for f in AGENT_TOOLS.glob("*.txt"):
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                pid = _product_id(data)
                if pid and pid in BATCH1_IDS and pid not in index:
                    index[pid] = data
                    RAW_DIR.mkdir(parents=True, exist_ok=True)
                    (RAW_DIR / f"{pid}.json").write_text(
                        json.dumps(data, ensure_ascii=False), encoding="utf-8"
                    )
            except Exception:
                continue
    return index


def load_raw(pid: str) -> dict | None:
    global _INDEX
    if _INDEX is None:
        _INDEX = _build_index()
    return _INDEX.get(pid)


def main() -> int:
    lines: list[str] = []
    ok = 0
    for pid in BATCH1_IDS:
        raw = load_raw(pid)
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
