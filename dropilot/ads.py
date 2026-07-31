from __future__ import annotations

import csv
from pathlib import Path

from .repository import CandidateRepository


NUMERIC_FLOATS = {"spend", "conversions", "revenue"}
NUMERIC_INTS = {"impressions", "clicks", "add_to_cart", "checkout"}
REQUIRED = {"fingerprint", "campaign_id", "market", "start_date"}


def import_ad_tests(path: str | Path, repository: CandidateRepository) -> dict[str, int]:
    inserted = 0
    updated = 0
    with Path(path).open("r", encoding="utf-8-sig", newline="") as handle:
        for index, raw in enumerate(csv.DictReader(handle), start=2):
            missing = [key for key in REQUIRED if not str(raw.get(key) or "").strip()]
            if missing:
                raise ValueError(f"Ligne {index}: champs obligatoires manquants: {', '.join(sorted(missing))}")
            row = dict(raw)
            row["market"] = row["market"].upper()
            for key in NUMERIC_FLOATS:
                row[key] = float(str(row.get(key) or 0).replace(",", "."))
            for key in NUMERIC_INTS:
                row[key] = int(float(str(row.get(key) or 0).replace(",", ".")))
            if repository.upsert_ad_test(row):
                inserted += 1
            else:
                updated += 1
    return {"inserted": inserted, "updated": updated}


def calculated_metrics(row: dict) -> dict:
    impressions = row["impressions"] or 0
    clicks = row["clicks"] or 0
    spend = row["spend"] or 0
    conversions = row["conversions"] or 0
    revenue = row["revenue"] or 0
    return {
        "ctr_pct": round(clicks / impressions * 100, 2) if impressions else None,
        "cpc": round(spend / clicks, 2) if clicks else None,
        "conversion_rate_pct": round(conversions / clicks * 100, 2) if clicks else None,
        "cost_per_conversion": round(spend / conversions, 2) if conversions else None,
        "roas": round(revenue / spend, 2) if spend else None,
    }


def write_ads_report(repository: CandidateRepository, output: str | Path) -> Path:
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Rapport des tests Google Ads", "", "Aucune décision couper/scaler n’est automatisée.", ""]
    for row in repository.list_ad_tests():
        metrics = calculated_metrics(row)
        lines.extend(
            [
                f"## {row.get('product_name') or row['fingerprint']}",
                f"- Campagne : {row['campaign_id']}",
                f"- Marché : {row['market']}",
                f"- Dépense : {row['spend']:.2f}",
                f"- Impressions : {row['impressions']}",
                f"- Clics : {row['clicks']}",
                f"- CPC : {metrics['cpc'] if metrics['cpc'] is not None else 'n/a'}",
                f"- CTR : {metrics['ctr_pct'] if metrics['ctr_pct'] is not None else 'n/a'} %",
                f"- Conversions : {row['conversions']}",
                f"- Taux de conversion : {metrics['conversion_rate_pct'] if metrics['conversion_rate_pct'] is not None else 'n/a'} %",
                f"- ROAS : {metrics['roas'] if metrics['roas'] is not None else 'n/a'}",
                f"- Ajouts panier : {row['add_to_cart']}",
                f"- Checkouts : {row['checkout']}",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")
    return path

