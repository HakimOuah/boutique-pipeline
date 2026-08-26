#!/usr/bin/env python3
"""Délais DSers/AliExpress FR. Auth = /tmp/dsers-my-products.json (non commité).

Endpoint réel : GET dsers-product-bff/freight
  supply_product_id = id AliExpress
  ship_to_country = FR
"""
from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
TMP = Path("/tmp/dsers-my-products.json")
OUT = Path("/tmp/dsers-freight.json")
BFF = "https://bff-api-01-gw.dsers.com/dsers-product-bff/freight"
APP = "159831080"


def main() -> None:
    dump = json.loads(TMP.read_text())
    token = dump["token"]
    store = dump["storeId"]
    live = json.loads((ROOT / "COHERENCE-2026-08-26.json").read_text())["produits"]

    needed: list[tuple[str, str, str]] = []
    seen: set[str] = set()
    for row in live:
        ae = row.get("ae_id")
        if not ae or ae in seen:
            continue
        seen.add(ae)
        needed.append((row["handle"], ae, row.get("sku") or ""))

    # brouillon LM-125, hors catalogue live
    if "1005009658358794" not in seen:
        needed.append(("applique-murale-travertin-358794", "1005009658358794", "LM-125"))

    def fetch_one(item: tuple[str, str, str]) -> dict:
        handle, ae, sku = item
        q = urlencode(
            {
                "storeId": store,
                "supply_product_id": ae,
                "supplyAppId": APP,
                "ship_to_country": "FR",
            }
        )
        req = Request(
            f"{BFF}?{q}",
            headers={
                "Authorization": f"Bearer {token}",
                "Origin": "https://www.dsers.com",
                "Referer": "https://www.dsers.com/",
                "Accept": "application/json",
            },
        )
        with urlopen(req, timeout=25) as resp:
            data = json.loads(resp.read().decode())
        methods = []
        for row in data.get("data") or []:
            t = row.get("time") or {}
            methods.append(
                {
                    "service": row.get("serviceId"),
                    "company": row.get("companyName"),
                    "min": t.get("min"),
                    "max": t.get("max"),
                    "tracked": row.get("tracking"),
                    "cost": row.get("amount"),
                    "currency": row.get("currency"),
                    "ship_from": row.get("shipFrom"),
                    "ship_to": row.get("shipTo"),
                }
            )
        return {"handle": handle, "sku": sku, "ae": ae, "methods": methods}

    results = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futs = {pool.submit(fetch_one, item): item for item in needed}
        for i, fut in enumerate(as_completed(futs), 1):
            handle, ae, sku = futs[fut]
            try:
                row = fut.result()
            except Exception as exc:
                row = {"handle": handle, "sku": sku, "ae": ae, "error": str(exc)}
                print(f"{i}/{len(needed)} {handle} ERR {exc}", flush=True)
            else:
                tracked = [
                    m for m in row["methods"] if m.get("tracked") and m.get("max") is not None
                ]
                fastest = min(tracked, key=lambda m: (m["max"], m["min"] or 99)) if tracked else None
                flag = " OVER" if fastest and fastest["max"] > 15 else ""
                print(
                    f"{i}/{len(needed)} {sku or handle} "
                    f"{(fastest or {}).get('min','?')}-{(fastest or {}).get('max','?')} "
                    f"{(fastest or {}).get('service','none')}{flag}",
                    flush=True,
                )
            results.append(row)

    results.sort(key=lambda r: (r.get("sku") or "", r.get("handle") or ""))
    OUT.write_text(
        json.dumps({"n": len(results), "results": results}, indent=2, ensure_ascii=False)
    )
    print(f"écrit {OUT} n={len(results)}")


if __name__ == "__main__":
    main()
