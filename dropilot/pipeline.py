from __future__ import annotations

from pathlib import Path

from .adapters import load_candidates
from .config import load_config
from .normalization import candidate_fingerprint
from .reporting import EvaluatedCandidate, write_reports
from .repository import CandidateRepository
from .scoring import ScoringEngine


def run_pipeline(
    *,
    input_path: str | Path,
    database_path: str | Path,
    report_directory: str | Path,
    source: str | None = None,
    input_format: str | None = None,
    config_path: str | Path | None = None,
) -> tuple[list[EvaluatedCandidate], dict[str, Path]]:
    config = load_config(config_path)
    products = load_candidates(input_path, input_format=input_format, source=source)
    engine = ScoringEngine(config_path)
    repository = CandidateRepository(database_path)
    dedup = config["deduplication"]
    evaluated: list[EvaluatedCandidate] = []
    decisions = {"shortlist": 0, "review": 0, "reject": 0}
    inserted_count = 0

    for product in products:
        result = engine.evaluate(product)
        if product.status == "idea":
            # Legacy ranking does not qualify or reject a commercial opportunity.
            product.status = "to_analyze"
        fingerprint = candidate_fingerprint(
            product,
            ignore_words=dedup["ignore_words"],
            include_angle=bool(dedup["include_angle_in_fingerprint"]),
        )
        inserted = repository.upsert(fingerprint, product, result)
        inserted_count += int(inserted)
        decisions[result.decision] += 1
        evaluated.append(EvaluatedCandidate(product, result, fingerprint, inserted))

    repository.record_run(
        source=source or "mixed",
        input_path=str(input_path),
        received_count=len(products),
        inserted_count=inserted_count,
        duplicate_count=len(products) - inserted_count,
        decisions=decisions,
    )
    reports = write_reports(evaluated, report_directory)
    return evaluated, reports
