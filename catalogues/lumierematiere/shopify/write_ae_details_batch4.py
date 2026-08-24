#!/usr/bin/env python3
"""Build ae-details-batch4.jsonl from raw MCP response JSON files."""

from __future__ import annotations

import json
from pathlib import Path

from build_ae_details_jsonl import transform

BATCH4_IDS = [
    "1005007677565566",
    "1005010330701414",
    "1005009093952116",
    "1005007469843772",
    "1005009966361680",
    "1005007682037279",
    "1005009614975417",
    "1005007308502141",
    "1005007359081498",
    "1005009870837156",
    "1005010120805304",
    "1005007009348096",
    "1005009023077631",
    "1005008004889929",
    "1005010732560098",
    "1005012107253182",
    "4000085689455",
    "1005006171950316",
    "1005010003341706",
    "1005006966366435",
    "1005007476957153",
    "1005007439147017",
    "1005009077246282",
    "1005007455240560",
    "1005007987630766",
    "1005007849233314",
    "1005008712575463",
    "1005006409907106",
    "1005009372254609",
    "1005007771784326",
    "1005006346330664",
]

RAW_DIR = Path(__file__).parent / "ae-details-batch4-raw"
BATCH2_RAW = Path(__file__).parent / "ae-details-batch2-raw"
AGENT_TOOLS = Path.home() / ".cursor/projects/Users-Hakim-Documents-Boutiques-drop/agent-tools"
OUT = Path(__file__).parent / "ae-details-batch4.jsonl"

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
                if pid and pid not in index:
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
    for pid in BATCH4_IDS:
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
