import json

from dropilot.pipeline import run_pipeline
from dropilot.repository import CandidateRepository, transition_status


def test_pipeline_deduplicates_repeated_runs_and_writes_reports(tmp_path):
    source = tmp_path / "input.json"
    source.write_text(
        json.dumps(
            [
                {
                    "product_name": "Fauteuil suspendu",
                    "source": "europages",
                    "category": "garden",
                    "price_sell": 400,
                    "price_source": 90,
                    "legal_eu": True,
                }
            ]
        ),
        encoding="utf-8",
    )
    database = tmp_path / "dropilot.sqlite3"
    reports = tmp_path / "reports"
    first, first_paths = run_pipeline(
        input_path=source, database_path=database, report_directory=reports
    )
    second, _ = run_pipeline(
        input_path=source, database_path=database, report_directory=reports
    )
    assert first[0].inserted is True
    assert second[0].inserted is False
    assert all(path.exists() for path in first_paths.values())
    assert len(CandidateRepository(database).list_candidates()) == 1


def test_status_transition_is_controlled(tmp_path):
    source = tmp_path / "input.json"
    source.write_text(json.dumps({"product_name": "Produit test"}), encoding="utf-8")
    database = tmp_path / "dropilot.sqlite3"
    evaluated, _ = run_pipeline(
        input_path=source, database_path=database, report_directory=tmp_path / "reports"
    )
    fingerprint = evaluated[0].fingerprint
    repository = CandidateRepository(database)
    transition_status(repository, fingerprint, "to_analyze")
    assert repository.list_candidates()[0]["status"] == "to_analyze"

