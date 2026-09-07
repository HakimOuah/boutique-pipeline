import json
from decimal import Decimal
from pathlib import Path


OUT = Path("/tmp/uk-sourcing-ultrasonic-final-20260907")


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
    searches = jsonl(OUT / "search.jsonl")
    details = jsonl(OUT / "details.jsonl")
    freight = jsonl(OUT / "freight-gbp.jsonl")
    details_by_pid = {str(row["product_id"]): row for row in details}
    freight_by_pid = {str(row["product_id"]): row for row in freight}
    selected_skus = {
        "1005013039050983": "12000060152027316",
        "1005010122198699": "12000051217763952",
    }
    candidates = []
    for pid, sku_id in selected_skus.items():
        record = details_by_pid[pid]
        result = result_of(record)
        base = result.get("ae_item_base_info_dto", {})
        store = result.get("ae_store_info", {})
        sku = next(row for row in sku_rows(record) if str(row.get("sku_id")) == sku_id)
        props = sku_props(sku)
        freight_record = freight_by_pid[pid]
        freight_raw = freight_record.get("raw", {})
        freight_result = freight_raw.get("result", freight_raw)
        options = freight_result.get("delivery_options", {}).get("delivery_option_d_t_o", [])
        selected_option = options[0] if pid == "1005010122198699" else next(row for row in options if row.get("code") == "CAINIAO_STANDARD")
        price = money(sku.get("offer_sale_price"))
        fee = money(selected_option.get("shipping_fee_cent"))
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
                    "price_gbp": str(price),
                    "stock_declared": sku.get("sku_available_stock"),
                    "tax_included_flag": sku.get("price_include_tax"),
                },
                "freight_options_raw": options,
                "freight_selected": selected_option,
                "total_gbp_product_plus_shipping": str(price + fee),
            }
        )

    evidence = {
        "mission": "UK compact ultrasonic cleaner final bounded pass",
        "checked_at_local": "2026-09-07 Europe/Paris",
        "destination": "GB",
        "api_scope": {
            "text_search_calls": 2,
            "results_per_text_search_requested": 10,
            "product_get_calls": 3,
            "freight_gbp_direct_calls": 2,
            "read_only": True,
            "no_purchase_or_supplier_contact": True,
        },
        "searches": searches,
        "product_gets": details,
        "freight_gbp_calls": freight,
        "screened_freight_variants": candidates,
        "uk_ready_qualifying_offers": [],
        "near_offers": [
            {
                "product_id": "1005013039050983",
                "sku_id": "12000060152027316",
                "why_not_target": "UK plug documented, but 2 L and 3.5 kg package exceed the 400–800 ml compact target; direct standard freight gives £80.60 total and 6–13 days.",
                "declared": "2 L theoretical; 60 W SKU; description also lists 120 W/150 W heat power; 304 basket; 220–240 V UK plug; stock 100.",
            },
            {
                "product_id": "1005010122198699",
                "sku_id": "12000051217763952",
                "why_not_target": "USB appears in title only; detail text is empty, power property is 1 W and voltage 6 V, so 35 W+ and USB alimentation are not documented.",
                "declared": "301–500 ml property; 1 W; 6 V; stock 7; total £11.28; 4–8 days.",
            },
        ],
        "limitations": [
            "The UK plug offer is not compact 400–800 ml and its API power fields conflict (2L 60W SKU, 120W property, 150W heat power in description).",
            "The USB candidate has no returned description text; its title alone is insufficient to prove USB alimentation.",
            "All prices, stock, electrical claims, basket contents and delivery windows are API declarations; no sample, electrical test, UK adapter, VAT invoice or UK return route was checked.",
            "logistics_info_dto.delivery_time=7 was not used as proof of delivery; direct freight windows were used.",
        ],
    }
    (OUT / "evidence.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")

    report = """# Sourcing UK — nettoyeur ultrasons compact — passe finale — 7 septembre 2026

Deux recherches AliExpress ont été exécutées (`ultrasonic cleaner UK plug`, `ultrasonic cleaner USB`), puis 3 fiches ouvertes et 2 variantes sondées en fret direct GBP vers GB. Aucun achat, adaptateur externe ou contact fournisseur.

## Constat

**Aucun SKU ne satisfait simultanément 35 W+, environ 400–800 ml, alimentation UK/USB documentée, coût rendu ≤£50 et délai API ≤10 jours.**

Quasi-offre UK : [1005013039050983](https://www.aliexpress.com/item/1005013039050983.html), SKU `12000060152027316` (2 L 60 W / 220–240 V UK Plug), stock 100, prix £40.39. La fiche décrit une cuve théorique 2 L, panier inox 304 et puissance 60/120 W (propriété 120 W; chauffage 150 W), mais le colis pèse 3,5 kg. Fret standard direct £40.21, 6–13 jours (`Sep 13 - 20`), total **£80.60**; heavy £37.49 mais 10–41 jours. Hors format et coût cible.

Quasi-offre USB : [1005010122198699](https://www.aliexpress.com/item/1005010122198699.html), SKU `12000051217763952`, stock 7, prix £9.29. Les propriétés déclarent 301–500 ml, **1 W**, 6 V; le mot USB n’apparaît que dans le titre et le détail renvoyé est vide. Fret £1.99, 4–8 jours, total **£11.28**. La puissance 35 W+ et l’alimentation USB ne sont donc pas prouvées.

La troisième fiche ouverte, `1005010241648074`, est USB dans le titre mais ne fournit ni capacité, puissance ni détail exploitable; elle n’a pas été sondée en fret.

Verdict : `TECHNICAL_FAIL` pour le cahier des charges exact; **constat commercial aucun**. Voir `evidence.json`, `search.jsonl`, `details.jsonl` et `freight-gbp.jsonl` pour les réponses brutes. `logistics_info_dto.delivery_time=7` n’a pas été utilisé comme preuve de livraison.
"""
    (OUT / "report.md").write_text(report, encoding="utf-8")
    print("wrote", OUT / "evidence.json", OUT / "report.md", "words", len(report.split()))


if __name__ == "__main__":
    main()
