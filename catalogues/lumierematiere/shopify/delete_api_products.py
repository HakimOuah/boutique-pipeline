#!/usr/bin/env python3
"""Supprime les 121 fiches créées par l'API (non liées à DSers). Collections conservées."""
from __future__ import annotations

import json
import sys
import time

ROOT = __import__("pathlib").Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from client import gql  # noqa: E402

STATE = ROOT / "state.json"


def product_ids() -> list[str]:
    ids: list[str] = []
    cursor = None
    while True:
        data = gql(
            """
            query ($cursor: String) {
              products(first: 50, after: $cursor) {
                pageInfo { hasNextPage endCursor }
                nodes { id handle }
              }
            }
            """,
            {"cursor": cursor},
        )
        conn = data["products"]
        for n in conn["nodes"]:
            ids.append(n["id"])
            print(f"  {n['handle']} {n['id']}")
        if not conn["pageInfo"]["hasNextPage"]:
            break
        cursor = conn["pageInfo"]["endCursor"]
        time.sleep(0.3)
    return ids


def delete_one(gid: str) -> None:
    data = gql(
        """
        mutation ($id: ID!) {
          productDelete(input: {id: $id}) {
            deletedProductId
            userErrors { field message }
          }
        }
        """,
        {"id": gid},
    )
    errs = data["productDelete"]["userErrors"]
    if errs:
        raise RuntimeError(errs)
    print(f"  deleted {gid}")


def main() -> None:
    ids = product_ids()
    print(f"=== suppression {len(ids)} produits ===")
    for i, gid in enumerate(ids, 1):
        delete_one(gid)
        if i % 10 == 0:
            print(f"  … {i}/{len(ids)}")
        time.sleep(0.25)
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    state["products"] = {}
    state["products_deleted_at"] = "2026-08-24"
    state["products_deleted_reason"] = "fiches API non liées à DSers — réimport via mapping fournisseur"
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    leftover = gql("""query { productsCount { count } }""")
    print("OK restant", leftover)


if __name__ == "__main__":
    main()
