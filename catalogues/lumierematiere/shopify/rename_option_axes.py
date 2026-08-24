#!/usr/bin/env python3
"""Renomme les axes de variante Lumière Matière selon le composant réellement choisi.

Le nom d’option porte le sens ; les valeurs restent courtes (Blanc, Noir, Doré).
SKU / sku_attr DSers inchangés. Idempotent.
"""
from __future__ import annotations

import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from client import gql  # noqa: E402
from position_variants import fetch_all_products  # noqa: E402

THROTTLE = 0.18
DIAM_RE = re.compile(r"^Ø \d+ cm$")
LIGHTS_RE = re.compile(r"^\d+\s+lumières?$", re.I)
WATT_RE = re.compile(r"^\d+\s*W$")
LETTER_RE = re.compile(r"^[A-G]\d*$")
LINE_RE = re.compile(r"(?i)(?:white|black|golden)\s+line")
AMP_ONLY_RE = re.compile(r"(?i)ampoule non fournie|ampoule fournie|no bulb")
GLASS_SKU_RE = re.compile(
    r"(?i)(clear glass|amber glass|smoky|smoke grey|smoke gray|clear light|#L (?:amber|clear|smoke)|gray glass|grey glass)"
)
GLASS_PURE = {"Transparent", "Ambre", "Gris fumé"}
TEMP_VALS = {"Blanc chaud", "Blanc froid", "Blanc neutre", "3 teintes"}


def sku_blob(product: dict) -> str:
    variants = product.get("variants") or []
    if isinstance(variants, dict):
        variants = variants.get("nodes") or []
    return " ".join(v.get("sku") or "" for v in variants)


def values_of(opt: dict) -> list[str]:
    if "optionValues" in opt:
        return [v["name"] for v in opt["optionValues"]]
    return list(opt.get("values") or [])


def is_mashed_couleur(values: list[str]) -> bool:
    for v in values:
        low = v.lower()
        if "lumière" in low or "forme" in low or "base " in low:
            return True
        if " · " in v or " — " in v:
            return True
        if re.match(r"^[A-Z]-", v):
            return True
    return False


def classify_option(product: dict, opt: dict) -> str | None:
    """Nouveau nom, ou None pour ne pas toucher."""
    name = opt["name"]
    values = values_of(opt)
    sku = sku_blob(product)
    handle = product.get("handle") or ""

    if name == "Taille":
        if values and all(DIAM_RE.fullmatch(v) for v in values):
            return "Diamètre"
        if values and all(LIGHTS_RE.fullmatch(v) for v in values):
            return "Lumières"
        if values and all(WATT_RE.fullmatch(v) for v in values):
            return "Puissance"
        return None

    if name == "Éclairage":
        return "Ampoule"

    if name == "Température":
        if values and all(AMP_ONLY_RE.search(v) and v not in TEMP_VALS for v in values):
            existing = {o["name"] for o in product["options"]}
            if "Ampoule" not in existing:
                return "Ampoule"
        return None

    if name != "Couleur":
        return None

    if LINE_RE.search(sku):
        return "Câble"

    if any(v in TEMP_VALS for v in values) and any(v not in TEMP_VALS for v in values):
        return None

    if values and all(LETTER_RE.fullmatch(v) for v in values):
        return "Modèle"

    if any("celadon" in v.lower() or "céladon" in v.lower() for v in values):
        return "Émail"

    if any("Papier" in v or "Soie" in v for v in values):
        return "Abat-jour"

    if values and all(WATT_RE.fullmatch(v) for v in values):
        return "Puissance"

    if is_mashed_couleur(values):
        return "Modèle"

    if set(values) <= GLASS_PURE:
        return "Verre"
    if "verre" in handle and set(values) <= GLASS_PURE | {"Vert", "Brun", "Blanc"}:
        return "Verre"
    if GLASS_SKU_RE.search(sku) and set(values) <= GLASS_PURE | {"Vert", "Brun", "Blanc", "Transparent"}:
        return "Verre"

    return "Finition"


def plan_renames(products: list[dict]) -> list[dict]:
    planned: list[dict] = []
    for p in products:
        existing = {o["name"] for o in p["options"]}
        for opt in p["options"]:
            new_name = classify_option(p, opt)
            if not new_name or new_name == opt["name"]:
                continue
            if new_name in existing:
                planned.append(
                    {
                        "handle": p["handle"],
                        "id": p["id"],
                        "option_id": opt["id"],
                        "from": opt["name"],
                        "to": new_name,
                        "values": values_of(opt),
                        "skip": f"conflit : {new_name} existe déjà",
                    }
                )
                continue
            planned.append(
                {
                    "handle": p["handle"],
                    "id": p["id"],
                    "option_id": opt["id"],
                    "from": opt["name"],
                    "to": new_name,
                    "values": values_of(opt),
                    "option_values": opt.get("optionValues") or [],
                    "skip": None,
                }
            )
            existing.add(new_name)
            existing.discard(opt["name"])
    return planned


def update_option_name(product_id: str, option_id: str, new_name: str, values: list[dict]) -> None:
    data = gql(
        """
        mutation U($productId: ID!, $option: OptionUpdateInput!, $optionValuesToUpdate: [OptionValueUpdateInput!]) {
          productOptionUpdate(
            productId: $productId
            option: $option
            optionValuesToUpdate: $optionValuesToUpdate
          ) {
            userErrors { field message }
          }
        }
        """,
        {
            "productId": product_id,
            "option": {"id": option_id, "name": new_name},
            "optionValuesToUpdate": [{"id": v["id"], "name": v["name"]} for v in values],
        },
    )
    errs = data["productOptionUpdate"]["userErrors"]
    if errs:
        raise RuntimeError(errs)


def main() -> None:
    apply = "--apply" in sys.argv
    print("— fetch produits")
    products = fetch_all_products()
    planned = plan_renames(products)
    skips = [r for r in planned if r["skip"]]
    todo = [r for r in planned if not r["skip"]]
    by_to: dict[str, int] = {}
    for r in todo:
        by_to[r["to"]] = by_to.get(r["to"], 0) + 1
    print(f"{len(todo)} renommages, {len(skips)} conflits")
    print("vers:", by_to)
    for r in skips:
        print(f"  SKIP {r['handle']}: {r['from']} → {r['to']} ({r['skip']})")
    for r in todo:
        print(f"  {r['handle']}: {r['from']} → {r['to']}  [{', '.join(r['values'])}]")
    if not apply:
        print("dry-run (relancer avec --apply)")
        return
    ok = 0
    for r in todo:
        try:
            update_option_name(r["id"], r["option_id"], r["to"], r["option_values"])
            ok += 1
            print(f"  OK {r['handle']}: {r['from']} → {r['to']}")
        except Exception as exc:  # noqa: BLE001
            print(f"  FAIL {r['handle']}: {r['from']} → {r['to']}: {exc}")
        time.sleep(THROTTLE)
    print(f"renommages OK {ok}/{len(todo)}")


if __name__ == "__main__":
    main()
