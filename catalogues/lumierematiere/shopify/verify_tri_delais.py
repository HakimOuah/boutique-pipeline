#!/usr/bin/env python3
"""Vérif post-tri délais : live ACTIVE, collections, FAQ, policy, thème."""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from apply_fullstack import theme_file  # noqa: E402
from apply_tri_delais import FAQ_NEW, KEEP, lm_code  # noqa: E402
from client import gql  # noqa: E402

ONLINE = "gid://shopify/Publication/287538413904"

PRODUCTS_Q = """
query($c: String) {
  products(first: 50, after: $c) {
    pageInfo { hasNextPage endCursor }
    nodes {
      id handle status tags
      metafields(first: 20, namespace: "custom") {
        nodes { key value }
      }
      collections(first: 30) { nodes { handle title } }
    }
  }
}
"""

COLL_Q = """
query($c: String, $online: ID!) {
  collections(first: 50, after: $c) {
    pageInfo { hasNextPage endCursor }
    nodes {
      id handle title
      publishedOnPublication(publicationId: $online)
    }
  }
}
"""

POLICY_Q = """
query {
  shopPolicies(first: 10) {
    nodes { type url body }
  }
}
"""


def fetch_products() -> list[dict]:
    out, cursor = [], None
    while True:
        data = gql(PRODUCTS_Q, {"c": cursor})["products"]
        out.extend(data["nodes"])
        if not data["pageInfo"]["hasNextPage"]:
            break
        cursor = data["pageInfo"]["endCursor"]
    return out


def fetch_collections() -> list[dict]:
    out, cursor = [], None
    while True:
        data = gql(COLL_Q, {"c": cursor, "online": ONLINE})["collections"]
        out.extend(data["nodes"])
        if not data["pageInfo"]["hasNextPage"]:
            break
        cursor = data["pageInfo"]["endCursor"]
    return out


def faq_delay(product: dict) -> str:
    for m in product.get("metafields", {}).get("nodes") or []:
        if m["key"] != "faq":
            continue
        try:
            items = json.loads(m["value"])
        except json.JSONDecodeError:
            return m["value"]
        for item in items:
            blob = json.dumps(item, ensure_ascii=False)
            if "acheminement" in blob or "jours ouvrés" in blob:
                return blob
    return ""


def main() -> None:
    products = fetch_products()
    active = [p for p in products if p["status"] == "ACTIVE"]
    drafts = [p for p in products if p["status"] != "ACTIVE"]
    print(f"produits API {len(products)}  ACTIVE {len(active)}  non-ACTIVE {len(drafts)}")

    keep_live = []
    leftover_717 = []
    missing_718 = []
    for p in active:
        sku = lm_code(p.get("tags") or [])
        keep_live.append(sku or p["handle"])
        delay = faq_delay(p)
        if "7 à 17" in delay or "6 à 15" in delay:
            leftover_717.append(sku or p["handle"])
        if FAQ_NEW.split("soit ")[1][:20] not in delay and "7 à 18" not in delay:
            missing_718.append((sku or p["handle"], delay[:80]))

    print("KEEP set", len(KEEP), "live SKU", sorted(x for x in keep_live if str(x).startswith("LM-")))
    extra = sorted(set(keep_live) - KEEP)
    missing = sorted(KEEP - set(keep_live))
    if extra:
        print("ACTIVE hors KEEP", extra)
    if missing:
        print("KEEP absents du live", missing)
    print("FAQ leftover 7–17", leftover_717 or "0")
    print("FAQ sans 7–18", missing_718 or "0")

    by_coll: dict[str, list[str]] = defaultdict(list)
    for p in active:
        sku = lm_code(p.get("tags") or []) or p["handle"]
        for c in p.get("collections", {}).get("nodes") or []:
            by_coll[c["handle"]].append(sku)

    collections = fetch_collections()
    print("\n# collections")
    for c in sorted(collections, key=lambda x: x["handle"]):
        live_n = len(by_coll.get(c["handle"], []))
        pub = "ON" if c["publishedOnPublication"] else "OFF"
        skus = ",".join(sorted(by_coll.get(c["handle"], [])))
        print(f"  {c['handle']:28} {pub:3} live={live_n:2}  {skus}")

    try:
        shop = gql(
            """
            query {
              shop {
                shopPolicies { type url body }
              }
            }
            """
        )["shop"]
        print("\n# policies")
        for policy in shop.get("shopPolicies") or []:
            body = policy["body"] or ""
            hits = [t for t in ("6 à 16", "7 à 18", "6 à 15", "7 à 17") if t in body]
            print(f"  {policy['type']} {policy['url']} {hits or 'no delay tokens'}")
    except RuntimeError as err:
        print("\n# policies GraphQL", err)

    print("\n# thème")
    leftovers = []
    for name in (
        "sections/footer-group.json",
        "templates/index.json",
        "templates/cart.json",
        "sections/cart-drawer-group.json",
        "templates/list-collections.json",
        "sections/header-group.json",
    ):
        blob = json.dumps(theme_file(name), ensure_ascii=False)
        hits = []
        for token in ("6 à 15", "7 à 17", "6–15", "7–17"):
            if token in blob:
                hits.append(token)
        print(f"  {name}: {hits or 'ok'}")
        leftovers.extend((name, t) for t in hits)
        if name == "templates/list-collections.json":
            listing = theme_file(name)["sections"]["main"]["settings"].get("collection_list") or []
            print("  list-collections", listing)

    print("\n# leftovers thème", leftovers or "0")


if __name__ == "__main__":
    main()
