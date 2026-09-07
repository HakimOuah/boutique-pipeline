import json
from decimal import Decimal
from pathlib import Path


OUT = Path("/tmp/uk-sourcing-abaya-final-20260907")


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


def money(value):
    return Decimal(str(value)).quantize(Decimal("0.01"))


def main():
    searches = jsonl(OUT / "search.jsonl")
    details = jsonl(OUT / "details.jsonl")
    freight = jsonl(OUT / "freight-gbp.jsonl")
    details_by_pid = {str(row["product_id"]): row for row in details}
    freight_by_pid = {str(row["product_id"]): row for row in freight}
    selected_skus = {
        "1005012235894439": "12000057817723897",
        "1005008650101896": "12000046096249126",
    }
    offers = []
    for pid, sku_id in selected_skus.items():
        record = details_by_pid[pid]
        result = result_of(record)
        base = result.get("ae_item_base_info_dto", {})
        store = result.get("ae_store_info", {})
        sku = next(row for row in sku_rows(record) if str(row.get("sku_id")) == sku_id)
        props = sku_props(sku)
        frow = freight_by_pid[pid]
        fraw = frow.get("raw", {})
        fres = fraw.get("result", fraw)
        options = fres.get("delivery_options", {}).get("delivery_option_d_t_o", [])
        opt = options[0] if options else None
        price = money(sku.get("offer_sale_price"))
        free = bool(opt and opt.get("free_shipping"))
        fee = money(opt.get("shipping_fee_cent")) if opt and opt.get("shipping_fee_cent") is not None else Decimal("0.00")
        offers.append(
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
                "freight_selected": opt,
                "freight_free_shipping": free,
                "freight_fee_gbp_screening": str(fee),
                "freight_fee_field_was_null": bool(opt and opt.get("shipping_fee_cent") is None),
                "total_gbp_product_plus_shipping_screening": str(price + fee),
            }
        )

    evidence = {
        "mission": "UK abaya final lower-cost embroidered/ornate sourcing",
        "checked_at_local": "2026-09-07 Europe/Paris",
        "destination": "GB",
        "api_scope": {
            "text_search_calls": 2,
            "results_per_query_requested": 20,
            "product_get_calls": 3,
            "freight_gbp_direct_calls": 2,
            "read_only": True,
            "no_purchase_or_supplier_contact": True,
        },
        "queries": ["embroidered abaya", "luxury abaya"],
        "searches": searches,
        "product_gets": details,
        "freight_gbp_calls": freight,
        "selected_offers": offers,
        "third_product_not_freighted": {
            "product_id": "1005012408718112",
            "reason": "Adult and Choice with 2 orders, but title says floral embroidery while ae_item_properties declares Decoration=NONE and Item Type=Dresses; no freight call spent.",
        },
        "limitations": [
            "Prices, stock, sales, Choice flag and freight windows are API declarations at capture time; they do not prove received quality, fit, embroidery or repeat availability.",
            "Offer 1005012235894439 title says open-front while properties say whether full opening=No; verify on sample and PDP before any publication.",
            "Offer 1005008650101896 has free_shipping=true but shipping_fee fields are null; total equals product price only as a screening calculation.",
            "No final Elsara-equivalence claim is made; quality, size grading and composition require sample inspection.",
        ],
    }
    (OUT / "evidence.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")

    report = """# Sourcing UK abayas — passe finale prix — 7 septembre 2026

Deux requêtes AliExpress (`embroidered abaya`, `luxury abaya`) ont renvoyé 20 résultats chacune. Trois fiches adultes ont été ouvertes; deux SKU brodés cohérents ont reçu un fret direct GBP vers GB. Aucun achat ni contact fournisseur.

## Offres retenues pour échantillonnage

- [1005012235894439](https://www.aliexpress.com/item/1005012235894439.html), Abaowedding Dress Store (CN), **13 ventes déclarées**, `Choice=yes`, adulte, décoration `Embroidery`, chiffon. SKU `12000057817723897`, Burgundy/M, stock **8**, prix **£27.89**. Fret Selection Premium **£1.99**, 6–10 jours (`Sep 13 - 17`), total **£29.88**. Le titre dit « open-front », mais une propriété dit `whether full opening=No`: à vérifier sur échantillon.
- [1005008650101896](https://www.aliexpress.com/item/1005008650101896.html), Meiya Store (CN), **5 ventes déclarées**, adulte, `Decoration=Embroidery`, `whether full opening=Yes`. SKU `12000046096249126`, Black Cardigan/M, stock **100**, prix **£29.39**. Fret standard **gratuit** (`free_shipping=true`, champs de montant nuls), 6–13 jours (`Sep 13 - 20`), total de screening **£29.39**. Le maximum de délai dépasse légèrement la cible 10 jours.

La troisième fiche ouverte, `1005012408718112`, avait £20.99 et 2 ventes, mais le titre promet une broderie alors que les propriétés déclarent `Decoration=NONE` et `Item Type=Dresses`; aucun fret n’a été consommé.

`TECHNICAL_WATCH`: les deux offres passent le coût rendu cible £40; la première passe aussi la fenêtre ≤10 jours API. Elles ne sont pas déclarées équivalentes à Elsara £85 : composition, tombé, broderie, tailles et qualité doivent être contrôlés par échantillon. Les stocks, ventes, Choice et délais restent déclaratifs.

Voir `evidence.json`, `search.jsonl`, `details.jsonl` et `freight-gbp.jsonl`.
"""
    (OUT / "report.md").write_text(report, encoding="utf-8")
    print("wrote", OUT / "evidence.json", OUT / "report.md", "words", len(report.split()))
    for offer in offers:
        print(offer["product_id"], offer["total_gbp_product_plus_shipping_screening"])


if __name__ == "__main__":
    main()
