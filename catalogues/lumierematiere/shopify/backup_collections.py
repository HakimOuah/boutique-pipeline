#!/usr/bin/env python3
"""Sauvegarde avant la passe collections de pièce du 26/08 : collections, appartenances,
fiches (titre, type, tags, variantes, média), menus, redirections, state.json, SEO."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from client import gql  # noqa: E402

OUT = ROOT / "backups" / "2026-08-26-collections"

COLLECTIONS_Q = """
query C($cursor: String) {
  collections(first: 25, after: $cursor) {
    pageInfo { hasNextPage endCursor }
    nodes {
      id handle title sortOrder templateSuffix
      description
      seo { title description }
      image { url altText }
      ruleSet { appliedDisjunctively rules { column relation condition } }
      products(first: 250) { nodes { id handle title } }
    }
  }
}
"""

PRODUCTS_Q = """
query P($cursor: String) {
  products(first: 25, after: $cursor) {
    pageInfo { hasNextPage endCursor }
    nodes {
      id handle title status productType vendor tags
      seo { title description }
      featuredMedia { ... on MediaImage { id image { url altText width height } } }
      media(first: 10) { nodes { ... on MediaImage { id image { url } } } }
      collections(first: 25) { nodes { handle title } }
      options { name values }
      variants(first: 100) {
        nodes { id sku title price selectedOptions { name value } }
      }
    }
  }
}
"""

MENUS_Q = """
query {
  menus(first: 20) {
    nodes {
      id handle title
      items {
        id title type url resourceId
        items { id title type url resourceId
          items { id title type url resourceId }
        }
      }
    }
  }
}
"""

REDIRECTS_Q = """
query R($cursor: String) {
  urlRedirects(first: 250, after: $cursor) {
    pageInfo { hasNextPage endCursor }
    nodes { id path target }
  }
}
"""

THEMES_Q = """
query { themes(first: 20) { nodes { id name role } } }
"""


def paginate(query: str, root: str) -> list[dict]:
    out: list[dict] = []
    cursor = None
    while True:
        data = gql(query, {"cursor": cursor})[root]
        out.extend(data["nodes"])
        if not data["pageInfo"]["hasNextPage"]:
            return out
        cursor = data["pageInfo"]["endCursor"]


def dump(name: str, payload) -> None:
    path = OUT / name
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"  {name} · {path.stat().st_size // 1024} Ko")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    print("=== sauvegarde 2026-08-26-collections ===")

    collections = paginate(COLLECTIONS_Q, "collections")
    dump("collections-avant.json", collections)
    print(f"    {len(collections)} collections")

    products = paginate(PRODUCTS_Q, "products")
    dump("products-avant.json", products)
    print(f"    {len(products)} fiches")

    dump("menus-avant.json", gql(MENUS_Q)["menus"]["nodes"])
    dump("redirects-avant.json", paginate(REDIRECTS_Q, "urlRedirects"))
    dump("themes-avant.json", gql(THEMES_Q)["themes"]["nodes"])

    for local in ("state.json", "collections-seo.json"):
        shutil.copy2(ROOT / local, OUT / f"{Path(local).stem}-avant{Path(local).suffix}")
        print(f"  copie locale {local}")

    print("OK sauvegarde")


if __name__ == "__main__":
    main()
