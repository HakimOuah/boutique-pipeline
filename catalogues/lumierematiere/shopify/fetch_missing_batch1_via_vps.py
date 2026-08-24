#!/usr/bin/env python3
"""Fetch missing batch-1 AE products via Product Factory VPS MCP and save raw JSON."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

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

REMOTE_PY = r'''
import asyncio, json, os, sys
from fastmcp import Client

async def main():
    pid = sys.argv[1]
    async with Client(os.environ.get("MCP_URL", "http://127.0.0.1:8080/mcp"), auth=os.environ.get("MCP_SURFACE_TOKEN")) as client:
        result = await client.call_tool("get_product_detail", {"product_id": pid})
        for attr in ("data", "structured_content"):
            val = getattr(result, attr, None)
            if val:
                print(json.dumps(val, ensure_ascii=False))
                return
        content = getattr(result, "content", None)
        if content:
            print(content[0].text)
            return
        print(json.dumps({"error": "empty MCP response"}))

asyncio.run(main())
'''


def fetch_one(product_id: str) -> dict | None:
    cmd = [
        "ssh",
        "-i",
        str(Path.home() / ".ssh/product_factory_codex_ed25519"),
        "-o",
        "BatchMode=yes",
        "-o",
        f"UserKnownHostsFile={Path.home() / '.ssh/product_factory_known_hosts'}",
        "root@srv1575867.hstgr.cloud",
        f"docker exec -i aliexpress-mcp python - {product_id}",
    ]
    proc = subprocess.run(
        cmd,
        input=REMOTE_PY.encode(),
        capture_output=True,
        text=False,
        timeout=120,
    )
    if proc.returncode != 0:
        err = proc.stderr.decode(errors="replace").strip()
        print(f"  fetch failed {product_id}: {err[:200]}", flush=True)
        return None
    out = proc.stdout.decode(errors="replace").strip()
    if not out:
        print(f"  empty response {product_id}", flush=True)
        return None
    try:
        return json.loads(out)
    except json.JSONDecodeError as exc:
        print(f"  bad JSON {product_id}: {exc}", flush=True)
        return None


def main() -> int:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    fetched = skipped = failed = 0
    for pid in BATCH1_IDS:
        out = RAW_DIR / f"{pid}.json"
        if out.exists():
            skipped += 1
            continue
        print(f"fetching {pid}...", flush=True)
        data = fetch_one(pid)
        if data is None:
            failed += 1
            continue
        if data.get("error"):
            print(f"  API error {pid}: {data['error']}", flush=True)
            failed += 1
            continue
        out.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        fetched += 1
        print(f"  saved {pid}", flush=True)
    print(f"done: fetched={fetched} skipped={skipped} failed={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
