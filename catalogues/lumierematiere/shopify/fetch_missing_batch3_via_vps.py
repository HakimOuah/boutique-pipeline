#!/usr/bin/env python3
"""Fetch missing batch-3 AE products via Product Factory VPS MCP and save raw JSON."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

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
    for pid in BATCH3_IDS:
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
