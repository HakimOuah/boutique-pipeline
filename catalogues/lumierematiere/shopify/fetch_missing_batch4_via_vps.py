#!/usr/bin/env python3
"""Fetch missing batch-4 AE products via Product Factory VPS MCP and save raw JSON."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

MISSING_BATCH4_IDS = [
    "1005007677565566",
    "1005009966361680",
    "1005007682037279",
    "1005009614975417",
    "1005007308502141",
    "1005007359081498",
    "1005009870837156",
    "1005007009348096",
    "1005009023077631",
    "1005008004889929",
    "1005010732560098",
    "1005012107253182",
    "4000085689455",
    "1005006171950316",
    "1005007476957153",
    "1005009077246282",
    "1005007455240560",
    "1005007987630766",
    "1005007849233314",
    "1005008712575463",
    "1005009372254609",
    "1005006346330664",
]

RAW_DIR = Path(__file__).parent / "ae-details-batch4-raw"

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
    for pid in MISSING_BATCH4_IDS:
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
