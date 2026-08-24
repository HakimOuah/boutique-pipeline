#!/usr/bin/env python3
"""Pousse les descriptions HTML VOC (copy Fable) vers Shopify. SKU / prix inchangés."""
from __future__ import annotations

import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from client import gql  # noqa: E402

DESC = ROOT.parent / "descriptions"


def product_ids_by_handle() -> dict[str, str]:
    out: dict[str, str] = {}
    cursor = None
    while True:
        data = gql(
            """
            query ($c: String) {
              products(first: 50, after: $c) {
                pageInfo { hasNextPage endCursor }
                nodes { id handle status }
              }
            }
            """,
            {"c": cursor},
        )
        for n in data["products"]["nodes"]:
            if n["status"] == "ACTIVE":
                out[n["handle"]] = n["id"]
        if not data["products"]["pageInfo"]["hasNextPage"]:
            return out
        cursor = data["products"]["pageInfo"]["endCursor"]


def main() -> None:
    ids = product_ids_by_handle()
    files = sorted(DESC.glob("*.html"))
    ok = skip = fail = 0
    for path in files:
        handle = path.stem
        pid = ids.get(handle)
        if not pid:
            print(f"  skip {handle} (pas actif)")
            skip += 1
            continue
        html = path.read_text(encoding="utf-8")
        data = gql(
            """
            mutation U($input: ProductInput!) {
              productUpdate(input: $input) {
                product { id handle }
                userErrors { field message }
              }
            }
            """,
            {"input": {"id": pid, "descriptionHtml": html}},
        )
        errs = data["productUpdate"]["userErrors"]
        if errs:
            print(f"FAIL {handle} {errs}")
            fail += 1
            continue
        ok += 1
        if ok % 20 == 0:
            print(f"  … {ok}")
        time.sleep(0.12)
    print(f"OK {ok} skip {skip} fail {fail}")


if __name__ == "__main__":
    main()
