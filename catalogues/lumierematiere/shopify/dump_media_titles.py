"""Dump lecture seule : handle, titre, type, options, prix et médias des 120 fiches."""
from __future__ import annotations

import json
from pathlib import Path

from client import gql

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "titles-media-dump.json"

QUERY = """
query ($c: String) {
  products(first: 25, after: $c, query: "status:active") {
    pageInfo { hasNextPage endCursor }
    nodes {
      id handle title productType
      seo { title description }
      featuredMedia { id alt ... on MediaImage { image { url } } }
      media(first: 10) {
        nodes { id alt ... on MediaImage { image { url } } }
      }
      options { name optionValues { name } }
      variants(first: 1) { nodes { price } }
    }
  }
}
"""


def main() -> None:
    nodes: list[dict] = []
    cursor = None
    while True:
        page = gql(QUERY, {"c": cursor})["products"]
        nodes.extend(page["nodes"])
        if not page["pageInfo"]["hasNextPage"]:
            break
        cursor = page["pageInfo"]["endCursor"]
    OUT.write_text(json.dumps(nodes, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(nodes)} fiches → {OUT.name}")


if __name__ == "__main__":
    main()
