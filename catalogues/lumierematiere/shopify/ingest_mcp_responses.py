#!/usr/bin/env python3
"""Ingest MCP get_product_detail responses into ae-details-batch2-raw/.

Usage:
  python3 ingest_mcp_responses.py responses.jsonl

Each line: compact JSON object (full MCP result dict).
Product id is read from ae_item_base_info_dto.product_id.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

RAW_DIR = Path(__file__).parent / "ae-details-batch2-raw"


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: ingest_mcp_responses.py <responses.jsonl>", file=sys.stderr)
        return 1
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    path = Path(sys.argv[1])
    count = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        data = json.loads(line)
        pid = str(
            data.get("ae_item_base_info_dto", {}).get("product_id")
            or data.get("product_id_converter_result", {}).get("main_product_id")
            or ""
        )
        if not pid:
            print(f"skip line without product_id", file=sys.stderr)
            continue
        out = RAW_DIR / f"{pid}.json"
        out.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        count += 1
        print(f"saved {pid}")
    print(f"ingested {count} responses -> {RAW_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
