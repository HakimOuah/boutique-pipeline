#!/usr/bin/env python3
"""Dump des fiches actives (titre, image featured, options) + groupes de titres identiques."""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from client import gql  # noqa: E402

QUERY = """
query ($c: String) {
  products(first: 40, after: $c, query: "status:active") {
    pageInfo { hasNextPage endCursor }
    nodes {
      id
      handle
      title
      descriptionHtml
      featuredMedia { ... on MediaImage { image { url width height } } }
      media(first: 6) { nodes { ... on MediaImage { image { url } } } }
      options { id name optionValues { id name } }
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

    out = ROOT / "titles-live-2026-08-25.json"
    out.write_text(json.dumps(nodes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(nodes)} fiches -> {out.name}")

    groups: dict[str, list[dict]] = defaultdict(list)
    for n in nodes:
        groups[n["title"]].append(n)
    dupes = {t: v for t, v in groups.items() if len(v) > 1}
    print(f"{len(dupes)} groupes de titres identiques, {sum(len(v) for v in dupes.values())} fiches")
    for t, v in sorted(dupes.items(), key=lambda kv: -len(kv[1])):
        print(f"\n=== {t}  (x{len(v)})")
        for p in v:
            img = ((p.get("featuredMedia") or {}).get("image") or {}).get("url", "")
            opts = "; ".join(
                f"{o['name']}: " + ", ".join(x["name"] for x in o["optionValues"]) for o in p["options"]
            )
            print(f"  {p['handle']}")
            print(f"    img  {img}")
            print(f"    opts {opts[:400]}")


if __name__ == "__main__":
    main()
