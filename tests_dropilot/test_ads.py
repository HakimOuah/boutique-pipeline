import csv

from dropilot.ads import calculated_metrics, import_ad_tests, write_ads_report
from dropilot.repository import CandidateRepository


def test_google_ads_metrics_are_imported_without_cut_scale_decision(tmp_path):
    source = tmp_path / "ads.csv"
    with source.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["fingerprint", "campaign_id", "market", "start_date", "spend", "impressions", "clicks", "conversions", "revenue", "add_to_cart", "checkout"],
        )
        writer.writeheader()
        writer.writerow({"fingerprint": "abc", "campaign_id": "123", "market": "fr", "start_date": "2026-07-14", "spend": 100, "impressions": 1000, "clicks": 50, "conversions": 2, "revenue": 400, "add_to_cart": 8, "checkout": 4})
    repository = CandidateRepository(tmp_path / "db.sqlite3")
    assert import_ad_tests(source, repository) == {"inserted": 1, "updated": 0}
    row = repository.list_ad_tests()[0]
    assert calculated_metrics(row)["cpc"] == 2
    assert calculated_metrics(row)["roas"] == 4
    report = write_ads_report(repository, tmp_path / "ads.md")
    assert "Aucune décision couper/scaler" in report.read_text(encoding="utf-8")
