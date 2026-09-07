import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


OUT = Path("/tmp/uk-sourcing-abayas-20260907")


def jsonl(path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("{"):
            rows.append(json.loads(line))
    return rows


def result_of(record):
    raw = record.get("raw", {})
    return raw.get("result", raw) if isinstance(raw, dict) else {}


def sku_rows(detail):
    container = result_of(detail).get("ae_item_sku_info_dtos", {})
    if isinstance(container, dict):
        return container.get("ae_item_sku_info_d_t_o", [])
    return container if isinstance(container, list) else []


def sku_properties(sku):
    container = sku.get("ae_sku_property_dtos", {})
    if isinstance(container, dict):
        return container.get("ae_sku_property_d_t_o", [])
    return container if isinstance(container, list) else []


def money(value):
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def clean_text(value):
    return " ".join(str(value or "").split())


def main():
    searches = jsonl(OUT / "search.jsonl")
    details = jsonl(OUT / "details.jsonl")
    freight = jsonl(OUT / "freight-gbp.jsonl")
    details_by_pid = {str(row["product_id"]): row for row in details}
    freight_by_pid = {str(row["product_id"]): row for row in freight}

    selected_specs = [
        {
            "product_id": "1005012385271194",
            "sku_id": "12000058264898367",
            "shipping_code": "CAINIAO_STANDARD",
            "family": "ouverte",
        },
        {
            "product_id": "1005012289841477",
            "sku_id": "12000057978139381",
            "shipping_code": "CAINIAO_STANDARD",
            "family": "ensemble 3 pièces brodé",
        },
        {
            "product_id": "1005012471812405",
            "sku_id": "12000058450979863",
            "shipping_code": "CAINIAO_FULFILLMENT_PRE",
            "family": "brodée",
        },
    ]

    offers = []
    for spec in selected_specs:
        detail = details_by_pid[spec["product_id"]]
        res = result_of(detail)
        base = res.get("ae_item_base_info_dto", {})
        store = res.get("ae_store_info", {})
        sku = next(row for row in sku_rows(detail) if str(row.get("sku_id")) == spec["sku_id"])
        props = sku_properties(sku)
        freight_row = freight_by_pid[spec["product_id"]]
        freight_envelope = freight_row.get("raw", {})
        freight_raw = freight_envelope.get("result", freight_envelope)
        options = freight_raw.get("delivery_options", {}).get("delivery_option_d_t_o", [])
        option = next(row for row in options if row.get("code") == spec["shipping_code"])
        price_gbp = money(sku.get("offer_sale_price"))
        fee_gbp = money(option.get("shipping_fee_cent"))
        offers.append(
            {
                "family": spec["family"],
                "product_id": spec["product_id"],
                "ali_url": f"https://www.aliexpress.com/item/{spec['product_id']}.html",
                "title": base.get("subject"),
                "seller": {
                    "id": store.get("store_id"),
                    "name": store.get("store_name"),
                    "country": store.get("store_country_code"),
                    "item_as_described_rating": store.get("item_as_described_rating"),
                    "communication_rating": store.get("communication_rating"),
                    "shipping_speed_rating": store.get("shipping_speed_rating"),
                },
                "sku": {
                    "sku_id": spec["sku_id"],
                    "attr": sku.get("sku_attr"),
                    "properties": [
                        {
                            "name": prop.get("sku_property_name"),
                            "value": prop.get("property_value_definition_name") or prop.get("sku_property_value"),
                        }
                        for prop in props
                    ],
                    "price_gbp": str(price_gbp),
                    "stock_declared": sku.get("sku_available_stock"),
                    "tax_included_flag": sku.get("price_include_tax"),
                },
                "package": res.get("package_info_dto"),
                "freight_api": {
                    "code": option.get("code"),
                    "company": clean_text(option.get("company")),
                    "ship_from_country": option.get("ship_from_country"),
                    "fee": option.get("shipping_fee_format"),
                    "fee_gbp": str(fee_gbp),
                    "currency_returned": option.get("shipping_fee_currency"),
                    "free_shipping": option.get("free_shipping"),
                    "min_delivery_days": option.get("min_delivery_days"),
                    "max_delivery_days": option.get("max_delivery_days"),
                    "delivery_date_desc": option.get("delivery_date_desc"),
                    "tracking": option.get("tracking"),
                    "available_stock": option.get("available_stock"),
                },
                "total_gbp_product_plus_shipping": str(price_gbp + fee_gbp),
            }
        )

    evidence = {
        "mission": "UK abayas open / embroidered / 2-3 piece sets",
        "checked_at_local": "2026-09-07 Europe/Paris",
        "destination": "GB",
        "api_scope": {
            "text_search_calls": len([row for row in searches if row.get("kind") == "text_search"]),
            "text_search_results_per_call": 10,
            "product_get_calls": len(details),
            "freight_calls": len(freight),
            "read_only": True,
            "no_purchase_or_supplier_contact": True,
        },
        "currency": {
            "product_prices": "GBP",
            "freight_prices": "GBP",
            "note": "Freight totals use the direct METHOD_FREIGHT_QUERY call with currency=GBP and locale=en_GB. The helper get_shipping_cost call that returned EUR was superseded and is retained separately as a diagnostic file.",
        },
        "searches": searches,
        "product_gets": details,
        "freight_calls": freight,
        "selected_offers": offers,
        "competitor_observations": [
            {
                "site": "Abayas Boutique",
                "product": "Elsara Embellished Open Abaya",
                "url": "https://abayasboutique.com/product/elsara-embellished-open-abaya/",
                "observed": "£85; 3-piece set (open abaya, hijab, belt), crinkle nida, cascading embellishments.",
                "read_on": "2026-09-07",
            },
            {
                "site": "Abayas Boutique",
                "product": "Nayara Hand-Embroidered Open Abaya",
                "url": "https://abayasboutique.com/product/nayara/",
                "observed": "€131.97 page display; 2-piece set (open abaya and scarf), hand embroidery, nida with chiffon side panels; UK/international shipping, made to order.",
                "read_on": "2026-09-07",
            },
        ],
        "limitations": [
            "Stock, price, delivery window and seller ratings are API declarations captured at the timestamp; they are not a received-sample proof.",
            "All selected shipping routes show ship_from_country=CN; direct freight responses returned GBP as requested.",
            "No sample, fabric/embroidery quality, fit, kit contents beyond the title, VAT invoice, UK returns path or product compliance was verified.",
            "Selected titles contain no third-party licensed brand name; absence of a title mention is not a full IP clearance.",
        ],
    }
    (OUT / "evidence.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")

    report_lines = [
        "# Sourcing UK abayas — 7 septembre 2026",
        "",
        "Passe AliExpress en lecture seule, destination GB, devise produit GBP. Trois requêtes texte ont renvoyé 10 résultats chacune; cinq fiches ont été ouvertes; trois SKU ont été sondés en fret. Les trois offres retenues viennent de trois vendeurs distincts.",
        "",
        "| Offre | Produit / SKU exact | Prix GBP | Stock déclaré | Fret GB / délai API | Total GBP* |",
        "|---|---|---:|---:|---|---:|",
        "| Ouverte | [1005012385271194](https://www.aliexpress.com/item/1005012385271194.html), Black / M, SKU 12000058264898367 | £50.99 | 998 | £12.39, standard, CN; 6–13 j, `Sep 13 - 20` | £63.38 |",
        "| Ensemble brodé 3 pièces | [1005012289841477](https://www.aliexpress.com/item/1005012289841477.html), Beige 3pcs set / M, SKU 12000057978139381 | £42.39 | 100 | £18.48, standard, CN; 6–13 j, `Sep 13 - 20` | £60.87 |",
        "| Brodée | [1005012471812405](https://www.aliexpress.com/item/1005012471812405.html), Black / M, SKU 12000058450979863 | £54.99 | 50 | £1.99, Selection Premium, CN; 6–10 j, `Sep 13 - 17` | £56.98 |",
        "",
        "Les titres API décrivent respectivement une abaya ouverte doublée, un ensemble avec abaya/inner/hijab et une abaya brodée doublée avec ceinture. Prix SKU `offer_sale_price`, taxes incluses selon le drapeau API. *Total = prix produit GBP + fret GBP renvoyé par l’appel direct `METHOD_FREIGHT_QUERY` avec `currency=GBP`, `locale=en_GB`. L’API renvoie les dates sans année; l’appel a été fait le 07/09/2026. Les totaux sont un screening, pas un devis contractuel.",
        "",
        "## Comparaison concurrentielle courte",
        "",
        "Abayas Boutique affiche l’Elsara à £85, en 3 pièces (abaya ouverte, hijab, ceinture), avec crinkle nida et embellissements en cascade: repère direct dans la cible £69–119. La Nayara est affichée €131.97, en 2 pièces, avec broderie main et panneaux chiffon; elle montre un niveau premium supérieur et une fabrication à la commande. Pages lues: [Elsara](https://abayasboutique.com/product/elsara-embellished-open-abaya/) et [Nayara](https://abayasboutique.com/product/nayara/).",
        "",
        "## Lecture technique",
        "",
        "`TECHNICAL_WATCH`: trois SKU exacts ont une réponse fret GB, un stock positif déclaré et un coût rendu API d’environ £56.98–£63.38, compatible avec une vente visée £69–119 avant publicité, retours et TVA. Les vendeurs sont CN; les fiches affichent 0 évaluation sur les deux références principales et 4–5 ventes seulement sur l’ensemble 3 pièces. Aucun échantillon n’a été reçu. La qualité du tissu/broderie, le contenu réel des ensembles, le sizing, la conformité, la facture TVA, les retours UK et la tenue du délai restent `MANQUANT`. Aucun nom de marque tierce n’apparaît dans les titres retenus, ce qui ne constitue pas une clearance IP.",
        "",
        "Aucune commande, panier, message fournisseur ou publication n’a été effectué. Voir `evidence.json` pour les réponses brutes et les paramètres d’appel.",
        "",
    ]
    report = "\n".join(report_lines)
    (OUT / "report.md").write_text(report, encoding="utf-8")
    print("wrote", OUT / "evidence.json", OUT / "report.md")
    print("report_words", len(report.split()))
    for offer in offers:
        print(offer["product_id"], offer["seller"]["name"], offer["total_gbp_product_plus_shipping"])


if __name__ == "__main__":
    main()
