"""Dump live : produits + variantes avec prix, pour l'alignement Lustria.

Lecture seule. Écrit prix-live-2026-08-26.json.
"""
from __future__ import annotations

import json
from pathlib import Path

import client

HERE = Path(__file__).resolve().parent
OUT = HERE / "prix-live-2026-08-26.json"

QUERY = """
query($cursor: String) {
  products(first: 5, after: $cursor) {
    pageInfo { hasNextPage endCursor }
    nodes {
      id
      handle
      title
      status
      productType
      tags
      variants(first: 250) {
        pageInfo { hasNextPage }
        nodes {
          id
          sku
          title
          price
          compareAtPrice
          selectedOptions { name value }
        }
      }
    }
  }
}
"""


def main() -> None:
    products = []
    cursor = None
    while True:
        data = client.gql(QUERY, {"cursor": cursor})
        conn = data["products"]
        for node in conn["nodes"]:
            if node["variants"]["pageInfo"]["hasNextPage"]:
                raise RuntimeError(f"{node['handle']}: >250 variantes, pagination requise")
            products.append(node)
        if not conn["pageInfo"]["hasNextPage"]:
            break
        cursor = conn["pageInfo"]["endCursor"]

    OUT.write_text(json.dumps(products, ensure_ascii=False, indent=1), encoding="utf-8")
    nvar = sum(len(p["variants"]["nodes"]) for p in products)
    print(f"{len(products)} produits, {nvar} variantes -> {OUT.name}")


if __name__ == "__main__":
    main()
