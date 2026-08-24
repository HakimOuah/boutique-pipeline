#!/usr/bin/env python3
"""Fetch missing batch-2 AE products via Product Factory VPS MCP and save raw JSON."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

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

SKIP_FETCH = {"1005012474741970"}
RAW_DIR = Path(__file__).parent / "ae-details-batch2-raw"

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
    for pid in BATCH2_IDS:
        out = RAW_DIR / f"{pid}.json"
        if out.exists() or pid in SKIP_FETCH:
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
