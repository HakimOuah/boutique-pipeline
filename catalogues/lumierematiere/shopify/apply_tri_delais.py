#!/usr/bin/env python3
"""Tri délais GMC 26/08 : draft OVER, FAQ 7–18, agrément lustres salon.

  python3 apply_tri_delais.py           # simulation
  python3 apply_tri_delais.py --apply
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from bootstrap_pages import PAGES, POLICIES, existing_pages, upsert_page, upsert_policy  # noqa: E402
from client import gql  # noqa: E402
from import_catalogue import ONLINE, add_to_collection  # noqa: E402
from md_html import md_to_html  # noqa: E402

# 37 OK + 12 LIMITE (reco). Inlivrables et fret > 20 $ / route > 16 j exclus.
KEEP = {
    "LM-007", "LM-014", "LM-016", "LM-018", "LM-020", "LM-022", "LM-024", "LM-027",
    "LM-028", "LM-031", "LM-032", "LM-033", "LM-034", "LM-039", "LM-040", "LM-042",
    "LM-043", "LM-046", "LM-050", "LM-051", "LM-056", "LM-057", "LM-060", "LM-061",
    "LM-062", "LM-076", "LM-081", "LM-082", "LM-083", "LM-088", "LM-091", "LM-093",
    "LM-095", "LM-096", "LM-097", "LM-099", "LM-100", "LM-101", "LM-102", "LM-105",
    "LM-106", "LM-108", "LM-113", "LM-121", "LM-122", "LM-123", "LM-124", "LM-126",
    "LM-127",
}

# Pièces de salon déjà live, à ajouter à lustres-salon (pas des appliques, pas des petits plafonniers).
SALON_GARNISH = {
    "LM-007", "LM-014", "LM-016", "LM-018", "LM-082", "LM-095",
    "LM-099", "LM-108", "LM-113", "LM-121",
}

FAQ_OLD = (
    "l’acheminement prend 6 à 15 jours ouvrés, soit 7 à 17 jours ouvrés au total"
)
FAQ_NEW = (
    "l’acheminement prend 6 à 16 jours ouvrés, soit 7 à 18 jours ouvrés au total"
)

PRODUCTS_Q = """
query($c: String) {
  products(first: 50, after: $c) {
    pageInfo { hasNextPage endCursor }
    nodes {
      id handle status tags
      metafields(first: 20, namespace: "custom") {
        nodes { id key value }
      }
    }
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


def lm_code(tags: list[str]) -> str | None:
    for t in tags or []:
        if t.startswith("LM-") and t[3:].isdigit():
            return t
    return None


def draft_product(gid: str) -> None:
    data = gql(
        """
        mutation U($input: ProductInput!) {
          productUpdate(input: $input) {
            userErrors { field message }
          }
        }
        """,
        {"input": {"id": gid, "status": "DRAFT"}},
    )
    errs = data["productUpdate"]["userErrors"]
    if errs:
        raise RuntimeError(errs)


def set_faq(gid: str, items: list[dict]) -> None:
    data = gql(
        """
        mutation M($metafields: [MetafieldsSetInput!]!) {
          metafieldsSet(metafields: $metafields) {
            userErrors { field message }
          }
        }
        """,
        {
            "metafields": [
                {
                    "ownerId": gid,
                    "namespace": "custom",
                    "key": "faq",
                    "type": "json",
                    "value": json.dumps(items, ensure_ascii=False),
                }
            ]
        },
    )
    errs = data["metafieldsSet"]["userErrors"]
    if errs:
        raise RuntimeError(errs)


def unpublish(gid: str) -> None:
    data = gql(
        """
        mutation U($id: ID!, $input: [PublicationInput!]!) {
          publishableUnpublish(id: $id, input: $input) {
            userErrors { field message }
          }
        }
        """,
        {"id": gid, "input": [{"publicationId": ONLINE}]},
    )
    errs = data["publishableUnpublish"]["userErrors"]
    if errs:
        msg = json.dumps(errs, ensure_ascii=False)
        if "not published" not in msg.lower() and "pas publié" not in msg.lower():
            raise RuntimeError(errs)


def collection_by_handle() -> dict[str, str]:
    data = gql("query { collections(first: 50) { nodes { id handle } } }")
    return {n["handle"]: n["id"] for n in data["collections"]["nodes"]}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    apply = args.apply

    products = fetch_products()
    by_sku = {}
    for p in products:
        sku = lm_code(p.get("tags") or [])
        if sku:
            by_sku[sku] = p

    to_draft = []
    to_keep = []
    for sku, p in sorted(by_sku.items()):
        if sku in KEEP:
            if p["status"] == "ACTIVE":
                to_keep.append(p)
        elif p["status"] == "ACTIVE":
            to_draft.append(p)

    print(f"keep ACTIVE {len(to_keep)}  draft {len(to_draft)}  KEEP set {len(KEEP)}")
    missing_keep = sorted(KEEP - set(by_sku))
    if missing_keep:
        print("KEEP absents du shop", missing_keep)

    if apply:
        for p in to_draft:
            draft_product(p["id"])
            print("DRAFT", lm_code(p["tags"]), p["handle"])
            time.sleep(0.12)
        for p in to_keep:
            raw = None
            for m in p.get("metafields", {}).get("nodes") or []:
                if m["key"] == "faq":
                    raw = m["value"]
                    break
            if not raw:
                print("WARN pas de FAQ", p["handle"])
                continue
            if FAQ_OLD not in raw and "6 à 16" in raw:
                print("FAQ déjà 7–18", p["handle"])
                continue
            if FAQ_OLD not in raw:
                print("WARN FAQ sans phrase délai", p["handle"])
                continue
            set_faq(p["id"], json.loads(raw.replace(FAQ_OLD, FAQ_NEW)))
            print("FAQ", lm_code(p["tags"]), p["handle"])
            time.sleep(0.12)

        coll = collection_by_handle()
        salon_id = coll["lustres-salon"]
        for sku in sorted(SALON_GARNISH):
            p = by_sku.get(sku)
            if not p:
                continue
            add_to_collection(salon_id, p["id"])
            print("SALON", sku, p["handle"])
            time.sleep(0.12)

        # Pampilles et papier : plus aucune fiche live. Handle conservé, canal retiré.
        unpublish(coll["lustres-pampilles"])
        print("UNPUB lustres-pampilles")
        unpublish(coll["suspensions-papier"])
        print("UNPUB suspensions-papier")

        pages_dir = HERE.parent / "pages"
        known = existing_pages()
        for handle, title, filename in PAGES:
            body = md_to_html((pages_dir / filename).read_text(encoding="utf-8"))
            upsert_page(handle, title, body, known)
            print("PAGE", handle)
        for ptype, filename in POLICIES:
            body = md_to_html((pages_dir / filename).read_text(encoding="utf-8"))
            upsert_policy(ptype, body)
        print("policies + pages poussées")
    else:
        print("DRY — SKU à draft :")
        for p in to_draft:
            print(" ", lm_code(p["tags"]), p["handle"])
        print("DRY — salon garnish", sorted(SALON_GARNISH))


if __name__ == "__main__":
    main()
