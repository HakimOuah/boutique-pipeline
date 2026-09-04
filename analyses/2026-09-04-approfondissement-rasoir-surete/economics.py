"""Sensibilités locales A6, sans API ni seuil ajouté au moteur canonique."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ASSUMPTIONS = {
    "status": "HYPOTHESE",
    "vat_rate_scenario": 0.20,
    "payment_rate_scenario": 0.02,
    "payment_fixed_eur_scenario": 0.30,
    "returns_sav_rate_of_ttc_scenario": 0.05,
    "selling_prices_ttc_scenarios": [69, 99, 119],
    "cpc_eur_scenarios": [0.80, 1.20],
    "cvr_scenarios": [0.01, 0.015, 0.02, 0.03],
    "post_ads_contribution_targets_eur": [0, 10],
    "note": "CPC 0.80 arrondi du proxy historique 0.7976 EUR ; 1.20 = stress. Aucun CPC, CVR, régime fiscal, taux de frais/SAV ou prix OH Ventures observé. Coût rendu sur une base fiscale cohérente, frais non récupérables inclus. Contribution cible avant coûts fixes, pas bénéfice net.",
    "historical_cpc_source": "../2026-09-03-qualification-9-produits-pur/dossiers/A6.md",
}

def pre_goods_margin(price):
    a = ASSUMPTIONS
    return (price / (1 + a["vat_rate_scenario"])
            - price * a["payment_rate_scenario"] - a["payment_fixed_eur_scenario"]
            - price * a["returns_sav_rate_of_ttc_scenario"])

def write_csv(name, rows):
    with (ROOT / name).open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

def main():
    caps = []
    for p in ASSUMPTIONS["selling_prices_ttc_scenarios"]:
        for cpc in ASSUMPTIONS["cpc_eur_scenarios"]:
            for cvr in ASSUMPTIONS["cvr_scenarios"]:
                for target in ASSUMPTIONS["post_ads_contribution_targets_eur"]:
                    caps.append(dict(status="HYPOTHESE", selling_price_ttc=p, cpc_eur=cpc,
                        cvr=cvr, expected_cpa_scenario=round(cpc / cvr, 4),
                        post_ads_contribution_target=target,
                        max_product_packaging_shipping_cost=round(pre_goods_margin(p) - cpc / cvr - target, 4)))
    examples = []
    for p, cost in [(69, 15), (99, 25), (119, 35)]:
        margin = pre_goods_margin(p) - cost
        for cpc in ASSUMPTIONS["cpc_eur_scenarios"]:
            examples.append(dict(status="HYPOTHESE", selling_price_ttc=p,
                product_packaging_shipping_cost=cost, contribution_before_ads=round(margin, 4),
                cpc_eur=cpc, break_even_cpa=round(margin, 4), break_even_cvr=round(cpc / margin, 6)))
    write_csv("economics-cost-caps.csv", caps)
    write_csv("economics-break-even.csv", examples)
    (ROOT / "economics-assumptions.json").write_text(json.dumps(ASSUMPTIONS, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
