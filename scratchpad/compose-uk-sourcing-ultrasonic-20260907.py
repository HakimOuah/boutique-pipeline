import json
from decimal import Decimal
from pathlib import Path


OUT = Path("/tmp/uk-sourcing-ultrasonic-20260907")


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


def sku_props(sku):
    container = sku.get("ae_sku_property_dtos", {})
    if isinstance(container, dict):
        return container.get("ae_sku_property_d_t_o", [])
    return container if isinstance(container, list) else []


def text_detail(base):
    try:
        mobile = json.loads(base.get("mobile_detail", "{}"))
    except Exception:
        return ""
    return " ".join(
        str(module.get("data", {}).get("content", ""))
        for module in mobile.get("moduleList", [])
        if module.get("type") == "text"
    )


def money(value):
    return Decimal(str(value)).quantize(Decimal("0.01"))


def main():
    details = jsonl(OUT / "details.jsonl")
    freight = jsonl(OUT / "freight-gbp.jsonl")
    by_pid = {str(row["product_id"]): row for row in details}
    freight_by_pid = {str(row["product_id"]): row for row in freight}
    selected_skus = {
        "1005007383813023": "12000040528232915",
        "1005009784385341": "12000050245030735",
        "1005010394741290": "12000052268170470",
    }
    candidates = []
    for pid, sku_id in selected_skus.items():
        record = by_pid[pid]
        result = result_of(record)
        base = result.get("ae_item_base_info_dto", {})
        store = result.get("ae_store_info", {})
        sku = next(row for row in sku_rows(record) if str(row.get("sku_id")) == sku_id)
        props = sku_props(sku)
        freight_record = freight_by_pid[pid]
        freight_raw = freight_record.get("raw", {})
        freight_result = freight_raw.get("result", freight_raw)
        options = freight_result.get("delivery_options", {}).get("delivery_option_d_t_o", [])
        selected_option = options[0] if options else None
        price = money(sku.get("offer_sale_price"))
        fee = money(selected_option.get("shipping_fee_cent")) if selected_option else None
        products = result.get("ae_item_properties", {}).get("ae_item_property", [])
        candidates.append(
            {
                "product_id": pid,
                "ali_url": f"https://www.aliexpress.com/item/{pid}.html",
                "title": base.get("subject"),
                "seller": {
                    "id": store.get("store_id"),
                    "name": store.get("store_name"),
                    "country": store.get("store_country_code"),
                    "item_as_described_rating": store.get("item_as_described_rating"),
                    "communication_rating": store.get("communication_rating"),
                    "shipping_speed_rating": store.get("shipping_speed_rating"),
                },
                "sales_count_declared": base.get("sales_count"),
                "evaluation_count_declared": base.get("evaluation_count"),
                "product_rating_declared": base.get("avg_evaluation_rating"),
                "logistics_info_raw": result.get("logistics_info_dto"),
                "package_info_raw": result.get("package_info_dto"),
                "declared_properties": products,
                "description_text": text_detail(base),
                "sku": {
                    "sku_id": sku_id,
                    "attr": sku.get("sku_attr"),
                    "properties": [
                        {
                            "name": prop.get("sku_property_name"),
                            "value": prop.get("property_value_definition_name") or prop.get("sku_property_value"),
                        }
                        for prop in props
                    ],
                    "price_gbp": str(price),
                    "stock_declared": sku.get("sku_available_stock"),
                    "tax_included_flag": sku.get("price_include_tax"),
                },
                "freight_options_raw": options,
                "freight_selected": selected_option,
                "total_gbp_product_plus_shipping": str(price + fee) if fee is not None else None,
            }
        )

    evidence = {
        "mission": "UK compact consumer ultrasonic cleaner",
        "checked_at_local": "2026-09-07 Europe/Paris",
        "destination": "GB",
        "api_scope": {
            "product_get_calls": 3,
            "freight_gbp_direct_calls": 3,
            "read_only": True,
            "no_purchase_or_supplier_contact": True,
        },
        "input_product_ids": list(selected_skus),
        "product_gets": details,
        "freight_gbp_calls": freight,
        "screened_candidates": candidates,
        "uk_ready_qualifying_offers": [],
        "near_offers_but_not_uk_ready": [
            {
                "product_id": "1005007383813023",
                "sku_id": "12000040528232915",
                "reason": "EU plug only; no UK plug or USB documented.",
                "capacity": "600 ml",
                "power": "35 W",
                "frequency": "40 kHz",
                "contents_or_basket": "cleaning basket stated in description; no USB.",
                "product_price_gbp": "30.39",
                "stock_declared": 6,
                "freight_gbp": "1.99",
                "delivery_api": "4–8 days; Sep 11 - 15",
                "total_gbp": "32.38",
            },
            {
                "product_id": "1005009784385341",
                "sku_id": "12000050245030735",
                "reason": "EU plug only; description explicitly says only EU plug 220 V; no UK plug or USB documented.",
                "capacity": "800 ml",
                "power": "35 W",
                "frequency": "40 kHz",
                "contents_or_basket": "matching basket stated in description; no USB.",
                "product_price_gbp": "30.29",
                "stock_declared": 9,
                "freight_gbp": "1.99",
                "delivery_api": "4–8 days; Sep 11 - 15",
                "total_gbp": "32.28",
            },
        ],
        "excluded": [
            {
                "product_id": "1005010394741290",
                "reason": "EU plug only and mini retainer/denture cleaner; description says 180 ml while property says <300 ml, so not the requested broader compact consumer offer.",
            }
        ],
        "limitations": [
            "All three selected freight variants are EU plug 220 V; no UK plug or USB variant is documented in the returned SKU/detail data.",
            "The direct freight call returns 4–8 days; logistics_info_dto.delivery_time=7 was not treated as delivery proof.",
            "Capacity, power, CE/ROHS/EMC and basket claims are supplier/API declarations; no sample, electrical test, UK adapter, VAT invoice or UK return route was checked.",
            "A sale at £89–129 would require a verified UK-ready electrical offer and credible premium execution; these checks do not establish either.",
        ],
    }
    (OUT / "evidence.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")

    report = """# Sourcing UK — nettoyeur ultrasons compact — 7 septembre 2026

Passe AliExpress en lecture seule : 3 `product_get`, puis 3 frets directs `METHOD_FREIGHT_QUERY` en GBP vers GB. Aucun achat ni contact fournisseur.

## Constat qualifiant

**Aucun SKU UK-ready qualifiant.** Les trois fiches contrôlées proposent une alimentation secteur 220 V avec variante EU; aucune prise UK ni alimentation USB n’est documentée.

Deux quasi-offres sont techniquement compactes et économiques, mais nécessitent un adaptateur non fourni et non vérifié :

- [1005007383813023](https://www.aliexpress.com/item/1005007383813023.html), BALASHOV Direct Store : SKU EU `12000040528232915`, stock 6, **£30.39** + fret GB **£1.99**, total **£32.38**, fenêtre API **4–8 jours** (`Sep 11 - 15`). Déclaré : 600 ml, 35 W, 40 kHz, cuve inox, panier de nettoyage; alimentation AC 220–240 V. Le détail annonce aussi « fast logistics 15–25 days » : contradiction conservée.
- [1005009784385341](https://www.aliexpress.com/item/1005009784385341.html), Cooskr Korea Store : SKU EU `12000050245030735`, stock 9, **£30.29** + **£1.99**, total **£32.28**, fenêtre **4–8 jours**. Déclaré : 800 ml, cuve 150×85×65 mm, 35 W, 40 kHz, panier assorti; le détail dit explicitement « only EU plug 220v ».

La troisième fiche, [1005010394741290](https://www.aliexpress.com/item/1005010394741290.html), est exclue : EU plug, mini nettoyeur denture/retainer UV, capacité contradictoire **180 ml** dans le texte contre **<300 ml** dans les propriétés.

`TECHNICAL_FAIL` pour le critère UK/USB; constat commercial : aucun. Les deux quasi-offres restent sous £45 rendu et sous 10 jours API, mais une vente £89–129 ne peut pas être retenue sans alimentation UK/USB et preuve premium. Les claims de puissance, panier, capacité, CE/ROHS/EMC, stock et délai restent déclaratifs; `logistics_info_dto.delivery_time=7` n’est pas une preuve de livraison.

Voir `evidence.json`, `details.jsonl` et `freight-gbp.jsonl` pour les réponses brutes.
"""
    (OUT / "report.md").write_text(report, encoding="utf-8")
    print("wrote", OUT / "evidence.json", OUT / "report.md", "words", len(report.split()))


if __name__ == "__main__":
    main()
