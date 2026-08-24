#!/usr/bin/env python3
"""Dump all Shopify products (DSers push) for overlay matching."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from client import gql  # noqa: E402

OUT = ROOT / "shopify-products-dump.jsonl"

QUERY = """
query Dump($cursor: String) {
  products(first: 50, after: $cursor) {
    pageInfo { hasNextPage endCursor }
    nodes {
      id
      handle
      title
      status
      vendor
      productType
      tags
      descriptionHtml
      onlineStoreUrl
      createdAt
      publishedAt
      seo { title description }
      featuredImage { url }
      media(first: 20) { nodes { ... on MediaImage { id alt } } }
      resourcePublications(first: 10) {
        nodes { isPublished publication { id name } }
      }
      metafields(first: 30) {
        nodes { namespace key type value }
      }
      variants(first: 50) {
        nodes {
          id
          sku
          barcode
          title
          price
          compareAtPrice
          selectedOptions { name value }
          inventoryItem {
            id
            unitCost { amount currencyCode }
            sku
          }
        }
      }
    }
  }
}
"""


def main() -> None:
    cursor = None
    n = 0
    with OUT.open("w", encoding="utf-8") as fh:
        while True:
            data = gql(QUERY, {"cursor": cursor})
            conn = data["products"]
            for node in conn["nodes"]:
                fh.write(json.dumps(node, ensure_ascii=False) + "\n")
                n += 1
            if not conn["pageInfo"]["hasNextPage"]:
                break
            cursor = conn["pageInfo"]["endCursor"]
    print(f"dumped {n} products -> {OUT}")


if __name__ == "__main__":
    main()
