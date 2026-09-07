import json
from decimal import Decimal
from pathlib import Path


OUT = Path("/tmp/uk-sourcing-icebath-20260907")


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

    chosen = {
        "1005010151127666": "12000051361428599",
        "1005012520238299": "12000058583359698",
        "1005010161523574": "12000051363809036",
        "1005009944233727": "12000050650202610",
    }
    candidates = []
    for pid, sku_id in chosen.items():
        record = by_pid[pid]
        result = result_of(record)
        base = result.get("ae_item_base_info_dto", {})
        store = result.get("ae_store_info", {})
        sku = next(row for row in sku_rows(record) if str(row.get("sku_id")) == sku_id)
        props = sku_props(sku)
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
                "declared_properties": result.get("ae_item_properties"),
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
                    "price_gbp": sku.get("offer_sale_price"),
                    "stock_declared": sku.get("sku_available_stock"),
                    "tax_included_flag": sku.get("price_include_tax"),
                },
            }
        )

    selected_pid = "1005012520238299"
    selected = next(row for row in candidates if row["product_id"] == selected_pid)
    freight_raw = freight_by_pid[selected_pid].get("raw", {})
    freight_result = freight_raw.get("result", freight_raw)
    options = freight_result.get("delivery_options", {}).get("delivery_option_d_t_o", [])
    selected_option = next(row for row in options if row.get("code") == "CAINIAO_STANDARD")
    selected["freight_options_raw"] = options
    selected["freight_selected"] = selected_option
    selected["total_gbp_product_plus_shipping"] = str(
        money(selected["sku"]["price_gbp"]) + money(selected_option["shipping_fee_cent"])
    )
    selected["declared_volume_liters"] = 330
    selected["declared_dimensions"] = "850 x 750 mm (33.5 x 29.5 in)"
    selected["declared_contents"] = [
        "ice bath tub",
        "carrying bag",
        "thermal cover/lid",
        "manual air pump",
        "water cushion",
    ]

    evidence = {
        "mission": "UK portable cold baths without chiller",
        "checked_at_local": "2026-09-07 Europe/Paris",
        "destination": "GB",
        "api_scope": {
            "product_get_calls": 4,
            "freight_gbp_direct_calls": 4,
            "read_only": True,
            "no_purchase_or_supplier_contact": True,
        },
        "input_search_context": {
            "source": "root-provided summary of prior text search",
            "ids": list(chosen),
            "note": "No new text search was run in this bounded pass.",
        },
        "product_gets": details,
        "freight_gbp_calls": freight,
        "screened_candidates": candidates,
        "selected_complete_offer": selected,
        "limitations": [
            "The selected SucceBuy description declares 330 L, lid/thermal cover, manual pump, water cushion and bag; these remain seller/API claims until a sample is received.",
            "The direct freight route for the selected offer is 6–13 days (Sep 13–20), so it is borderline for a roughly 10-day target; the API does not prove delivery.",
            "logistics_info_dto.delivery_time=7 was not used as a delivery proof because it conflicts with direct freight windows on other SKUs (26–43 and 25–42 days).",
            "No screened candidate has a verified rendered cost below £55: the selected complete offer is £78.19 before returns, VAT and advertising.",
            "No chiller was selected; no sample, UK returns route, VAT invoice, materials test or product compliance review was performed.",
        ],
    }
    (OUT / "evidence.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")

    report = """# Sourcing UK — bain froid portable sans groupe froid — 7 septembre 2026

Contrôle borné AliExpress, destination GB : 4 fiches `product_get`, puis 4 sondes de fret direct `METHOD_FREIGHT_QUERY` en GBP. Aucun chiller, mini-bol visage, achat ou contact fournisseur.

## Offre complète retenue

**SucceBuy Ice Bath Tub**, [produit 1005012520238299](https://www.aliexpress.com/item/1005012520238299.html), Shuerle273 Store (CN). SKU `12000058583359698`, variante `75x80`, stock déclaré **997**, prix **£33.59**. La description API déclare **330 L**, 850 × 750 mm, couvercle thermique, pompe à air manuelle, coussin d’eau et sac de transport. La propriété produit indique « Cover: with lid ».

Fret direct GB choisi : `CAINIAO_STANDARD`, **£44.60**, CN, suivi, fenêtre API **6–13 jours**, `Sep 13 - 20`. Coût rendu API : **£78.19**. Options premium : £87.79 (6–11 jours); option heavy : £40.90 mais 10–41 jours. Le coût cible <£55 n’est donc pas atteint, même si le prix produit seul est bas.

## Autres fiches contrôlées

- `1005010151127666`, £64.99, stock 291 : fiche sans volume, couvercle ou pompe explicités; description contradictoire (« no inflation » puis « inflatable »). Fret direct £1.99 mais **26–43 jours**; le `delivery_time=7` de `logistics_info_dto` n’est pas retenu.
- `1005010161523574`, £55.99, stock 993 : volume déclaré 95 gallons, siège d’eau et 8 barres inox, mais couvercle/pompe non établis. Fret £44.60, 6–13 jours; total £100.59.
- `1005009944233727`, £51.59, stock 22 : propriété « with lid », volume et pompe absents de la description. Fret £1.99 mais **25–42 jours**; total £53.58, non exploitable pour le délai.

`TECHNICAL_WATCH` : une offre complète est documentée, mais elle est au-dessus du coût rendu cible et le délai standard est borderline. Les claims de volume, contenu, stock et délai restent déclaratifs; aucun échantillon ni contrôle de livraison n’a été réalisé.

Voir `evidence.json`, `details.jsonl` et `freight-gbp.jsonl` pour les réponses brutes.
"""
    (OUT / "report.md").write_text(report, encoding="utf-8")
    print("wrote", OUT / "evidence.json", OUT / "report.md", "words", len(report.split()))
    print("selected_total", selected["total_gbp_product_plus_shipping"])


if __name__ == "__main__":
    main()
