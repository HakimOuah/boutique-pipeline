#!/usr/bin/env python3
"""Sonde AliExpress exacte à exécuter dans le conteneur MCP du VPS.

Le script importe le client officiel déjà installé dans ``aliexpress-mcp``.
Il ne lit ni n'affiche directement les secrets : ceux-ci restent injectés par
Docker dans l'environnement du conteneur. Il échoue fermé si la variante est
absente ou ambiguë, si le stock est inconnu/nul, ou si aucun fret France n'est
retourné.

Exemple depuis le VPS, après avoir copié le fichier dans le conteneur :

    docker exec aliexpress-mcp python /tmp/aliexpress_vps_exact_probe.py
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from datetime import datetime, timezone
from typing import Any, Iterable, Mapping


DEFAULT_PRODUCT_ID = "1005010249362754"
DEFAULT_PROPERTIES = ("white sterile", "36mm-glass back")


class QualificationError(RuntimeError):
    """La preuve fournisseur ne permet pas de qualifier le SKU demandé."""


def _items(value: Any, *keys: str) -> list[Mapping[str, Any]]:
    if isinstance(value, list):
        return [item for item in value if isinstance(item, Mapping)]
    if isinstance(value, Mapping):
        for key in keys:
            nested = value.get(key)
            if isinstance(nested, list):
                return [item for item in nested if isinstance(item, Mapping)]
            if isinstance(nested, Mapping):
                return [nested]
    return []


def _compact(value: Any) -> str:
    return "".join(char for char in str(value or "").casefold() if char.isalnum())


def _properties(sku: Mapping[str, Any]) -> list[dict[str, Any]]:
    raw = _items(
        sku.get("ae_sku_property_dtos")
        or sku.get("aeop_s_k_u_propertys")
        or sku.get("aeop_s_k_u_property_list")
        or [],
        "ae_sku_property_d_t_o",
        "aeop_sku_property",
    )
    return [
        {
            "name": prop.get("sku_property_name"),
            "value": (
                prop.get("property_value_definition_name")
                or prop.get("sku_property_value")
            ),
            "raw_value": prop.get("sku_property_value"),
            "image": prop.get("sku_image"),
        }
        for prop in raw
    ]


def _sku_rows(detail: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    return _items(
        detail.get("ae_item_sku_info_dtos") or [],
        "ae_item_sku_info_d_t_o",
        "aeop_ae_product_sku",
    )


def _property_matches(selector: str, prop: Mapping[str, Any]) -> bool:
    name = _compact(prop.get("name"))
    values = {_compact(prop.get("value")), _compact(prop.get("raw_value"))}
    if not selector:
        return False
    if any(selector in value for value in values if value):
        return True
    if not name or not selector.startswith(name):
        return False
    remainder = selector[len(name):]
    return bool(remainder) and any(remainder in value for value in values if value)


def select_exact_sku(
    detail: Mapping[str, Any], required_properties: Iterable[str]
) -> tuple[Mapping[str, Any], list[dict[str, Any]]]:
    selectors = [_compact(value) for value in required_properties if _compact(value)]
    if not selectors:
        raise QualificationError("Au moins une propriété de variante est requise")

    matches: list[tuple[Mapping[str, Any], list[dict[str, Any]]]] = []
    for sku in _sku_rows(detail):
        props = _properties(sku)
        if all(
            any(_property_matches(selector, prop) for prop in props)
            for selector in selectors
        ):
            matches.append((sku, props))

    if not matches:
        raise QualificationError(
            "Aucun SKU ne correspond exactement à : "
            + " + ".join(required_properties)
        )
    if len(matches) != 1:
        raise QualificationError(
            f"Variante ambiguë : {len(matches)} SKU correspondent aux propriétés"
        )

    sku, props = matches[0]
    sku_id = str(sku.get("sku_id") or "")
    if not sku_id.isdigit():
        raise QualificationError("Identifiant SKU numérique manquant")
    try:
        stock = int(sku.get("sku_available_stock"))
    except (TypeError, ValueError) as exc:
        raise QualificationError("Stock numérique du SKU manquant") from exc
    if stock <= 0:
        raise QualificationError("SKU hors stock")
    return sku, props


def _delivery_options(freight: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    return _items(
        freight.get("delivery_options") or [],
        "delivery_option_d_t_o",
        "delivery_option_dto",
    )


def _true(value: Any) -> bool:
    return value is True or str(value).casefold() == "true"


def build_record(
    product_id: str,
    destination: str,
    detail: Mapping[str, Any],
    sku: Mapping[str, Any],
    properties: list[dict[str, Any]],
    freight: Mapping[str, Any],
) -> dict[str, Any]:
    if not _true(freight.get("success")):
        raise QualificationError(
            "Fret indisponible : "
            f"code={freight.get('code')} msg={freight.get('msg')}"
        )
    options = _delivery_options(freight)
    if not options:
        raise QualificationError("Aucune option de livraison retournée pour la France")

    base = detail.get("ae_item_base_info_dto") or {}
    store = detail.get("ae_store_info") or {}
    stock = int(sku["sku_available_stock"])
    return {
        "checked_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "source": "AliExpress Open Platform / AE-Dropshipper depuis le VPS whitelisté",
        "destination": destination.upper(),
        "product": {
            "product_id": str(base.get("product_id") or product_id),
            "title": base.get("subject"),
            "status": base.get("product_status_type"),
            "rating": base.get("avg_evaluation_rating"),
            "evaluation_count": base.get("evaluation_count"),
            "sales_count": base.get("sales_count"),
            "store": {
                "id": store.get("store_id"),
                "name": store.get("store_name"),
                "country": store.get("store_country_code"),
                "item_as_described_rating": (
                    store.get("item_as_described_rating")
                    or store.get("item_as_descriped_rating")
                ),
                "communication_rating": store.get("communication_rating"),
                "shipping_speed_rating": store.get("shipping_speed_rating"),
            },
        },
        "exact_sku": {
            "sku_id": str(sku.get("sku_id")),
            "sku_attr": sku.get("sku_attr") or sku.get("id"),
            "properties": properties,
            "stock": stock,
            "offer_sale_price": sku.get("offer_sale_price"),
            "sku_price": sku.get("sku_price"),
            "currency": sku.get("currency_code"),
            "tax_included": sku.get("price_include_tax"),
        },
        "freight": {
            "success": True,
            "code": freight.get("code"),
            "message": freight.get("msg"),
            "options": [
                {
                    "code": option.get("code"),
                    "company": option.get("company"),
                    "shipping_fee": (
                        option.get("shipping_fee_format")
                        or option.get("shipping_fee_cent")
                    ),
                    "currency": option.get("shipping_fee_currency"),
                    "free_shipping": option.get("free_shipping"),
                    "min_delivery_days": option.get("min_delivery_days"),
                    "max_delivery_days": option.get("max_delivery_days"),
                    "delivery_date": option.get("delivery_date_desc"),
                    "ship_from_country": option.get("ship_from_country"),
                    "tracking": option.get("tracking"),
                    "available_stock": option.get("available_stock"),
                }
                for option in options
            ],
        },
    }


async def qualify(
    product_id: str, required_properties: Iterable[str], destination: str
) -> dict[str, Any]:
    # Ces imports existent dans l'image officielle aliexpress-mcp, pas sur tous
    # les postes clients. Les garder ici permet de tester le parseur hors VPS.
    from src.aliexpress_client import AliExpressClient
    from src.config import load_config

    config = load_config()
    async with AliExpressClient(config.aliexpress) as client:
        detail = await client.get_product_details(product_id)
        sku, properties = select_exact_sku(detail, required_properties)
        freight = await client.get_shipping_cost(
            product_id=product_id,
            sku_id=str(sku["sku_id"]),
            country_code=destination.upper(),
            quantity=1,
        )
    return build_record(
        product_id, destination, detail, sku, properties, freight
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Qualifier une variante AliExpress exacte depuis le VPS whitelisté."
    )
    parser.add_argument("--product-id", default=DEFAULT_PRODUCT_ID)
    parser.add_argument("--property", action="append", dest="properties")
    parser.add_argument("--destination", default="FR")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    properties = args.properties or list(DEFAULT_PROPERTIES)
    try:
        record = asyncio.run(qualify(args.product_id, properties, args.destination))
    except (QualificationError, RuntimeError, ValueError) as exc:
        print(f"QUALIFICATION_REFUSED: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
