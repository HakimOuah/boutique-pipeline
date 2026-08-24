#!/usr/bin/env python3
"""Build ae-details-batch3.jsonl from raw MCP response JSON files."""

from __future__ import annotations

import json
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

RAW_DIR = Path(__file__).parent / "ae-details-batch3-raw"
AGENT_TOOLS = Path.home() / ".cursor/projects/Users-Hakim-Documents-Boutiques-drop/agent-tools"
OUT = Path(__file__).parent / "ae-details-batch3.jsonl"


def product_id_from_data(data: dict) -> str | None:
    base = data.get("ae_item_base_info_dto") or {}
    got = str(base.get("product_id") or "")
    if got:
        return got
    conv = data.get("product_id_converter_result") or {}
    return str(conv.get("main_product_id") or "") or None


def load_raw(pid: str) -> dict | None:
    p = RAW_DIR / f"{pid}.json"
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    if AGENT_TOOLS.is_dir():
        for f in AGENT_TOOLS.glob("*.txt"):
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                got = product_id_from_data(data)
                if got == pid:
                    RAW_DIR.mkdir(parents=True, exist_ok=True)
                    p.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
                    return data
            except Exception:
                continue
    return None


def main() -> int:
    lines: list[str] = []
    ok = 0
    for pid in BATCH3_IDS:
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
