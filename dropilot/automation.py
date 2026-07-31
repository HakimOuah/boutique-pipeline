from __future__ import annotations

from pathlib import Path

from .pipeline import run_pipeline


SUPPORTED_SUFFIXES = {".json", ".csv", ".tsv", ".md", ".markdown"}


def process_inbox(
    *,
    inbox: str | Path,
    database_path: str | Path,
    report_directory: str | Path,
    config_path: str | Path | None = None,
) -> list[dict]:
    inbox_path = Path(inbox).resolve()
    inbox_path.mkdir(parents=True, exist_ok=True)
    outcomes: list[dict] = []
    for path in sorted(inbox_path.iterdir()):
        if not path.is_file() or path.suffix.lower() not in SUPPORTED_SUFFIXES:
            continue
        try:
            evaluated, reports = run_pipeline(
                input_path=path,
                database_path=database_path,
                report_directory=report_directory,
                config_path=config_path,
            )
            outcomes.append(
                {
                    "input": str(path),
                    "status": "ok",
                    "products": len(evaluated),
                    "reports": {key: str(value) for key, value in reports.items()},
                }
            )
        except Exception as error:
            outcomes.append({"input": str(path), "status": "error", "error": str(error)})
    return outcomes

