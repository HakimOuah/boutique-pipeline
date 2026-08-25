#!/usr/bin/env python3
"""Remonte les variantes LM-071 sous le plancher de marge.

Le proxy 222,99 € était la médiane des SKU AliExpress, pas le palier d'entrée.
Coûts AE du 26/08/2026 (quote officielle, port 0, +2 € de fret maison) :

  46 cm rond     151,69 → 299 €  (marge OK, inchangé)
  60 cm rond     202,69 → 349 €  (marge OK, inchangé)
  76 cm rond     244,69 → 399 €  (juste au plancher, inchangé)
  100 cm rond    393,69 → 639 €  (était 499, sous l'eau)
  120 cm allongé 265,69 → 429 €  (était 399, sous l'eau)
  180 cm allongé 552,39 → 889 €  (était 499, perte nette)

Plancher : TTC >= (coût + 2) × 1,6, grille en 9 au pas de 10 €.
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from client import gql  # noqa: E402

BACKUP = ROOT / "backups" / f"{date.today().isoformat()}-lm071"
HANDLE = "lustre-cristal-led-dore-202521"
PRODUCT = "gid://shopify/Product/10591495782736"

# taille lue dans le sku_attr DSers → nouveau prix TTC
CIBLES = {
    "Round 46cm": None,  # 299, inchangé
    "Round 60cm": None,
    "Round 76cm": None,
    "Round 100cm": "639.00",
    "Long 120cm": "429.00",
    "Long 180cm": "889.00",
}


def taille(sku: str) -> str | None:
    for key in CIBLES:
        if key in sku:
            return key
    return None


def main() -> None:
    BACKUP.mkdir(parents=True, exist_ok=True)
    data = gql(
        """
        query ($id: ID!) {
          product(id: $id) {
            id handle
            variants(first: 50) {
              nodes { id sku title price }
            }
          }
        }
        """,
        {"id": PRODUCT},
    )["product"]
    if data["handle"] != HANDLE:
        raise RuntimeError(data["handle"])
    (BACKUP / "lm071-avant.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    updates = []
    journal = []
    for v in data["variants"]["nodes"]:
        key = taille(v["sku"])
        if key is None:
            raise RuntimeError(f"taille inconnue: {v['sku']}")
        cible = CIBLES[key]
        if cible is None:
            journal.append((v["title"], v["price"], v["price"], "inchangé"))
            continue
        if v["price"] == cible:
            journal.append((v["title"], v["price"], cible, "déjà à jour"))
            continue
        updates.append({"id": v["id"], "price": cible})
        journal.append((v["title"], v["price"], cible, "hausse"))

    if updates:
        payload = gql(
            """
            mutation ($productId: ID!, $variants: [ProductVariantsBulkInput!]!) {
              productVariantsBulkUpdate(productId: $productId, variants: $variants) {
                productVariants { id price }
                userErrors { field message }
              }
            }
            """,
            {"productId": PRODUCT, "variants": updates},
        )["productVariantsBulkUpdate"]
        if payload["userErrors"]:
            raise RuntimeError(payload["userErrors"])

    apres = gql(
        """
        query ($id: ID!) {
          product(id: $id) {
            variants(first: 50) { nodes { id sku title price compareAtPrice } }
          }
        }
        """,
        {"id": PRODUCT},
    )["product"]
    (BACKUP / "lm071-apres.json").write_text(
        json.dumps(apres, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    for v in apres["variants"]["nodes"]:
        key = taille(v["sku"])
        cible = CIBLES[key]
        if cible and v["price"] != cible:
            raise RuntimeError(f"{v['title']}: {v['price']} ≠ {cible}")
        if v["compareAtPrice"]:
            raise RuntimeError(f"{v['title']}: compareAt renseigné")

    for title, avant, apres_p, decision in journal:
        print(f"  {title}: {avant} → {apres_p} ({decision})")
    print(f"OK LM-071, {len(updates)} variantes écrites")


if __name__ == "__main__":
    main()
