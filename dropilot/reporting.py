from __future__ import annotations

import csv
import json
import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from .models import ProductCandidate, ScoringResult


@dataclass
class EvaluatedCandidate:
    product: ProductCandidate
    result: ScoringResult
    fingerprint: str
    inserted: bool

    def flat_dict(self) -> dict:
        row = self.product.to_dict()
        row.update(
            {
                "fingerprint": self.fingerprint,
                "inserted": self.inserted,
                "score": self.result.score,
                "decision": self.result.decision,
                "verdict": self.result.verdict,
                "rejected_by": self.result.rejected_by,
                "flags": " | ".join(self.result.flags),
                "breakdown": json.dumps(self.result.breakdown, ensure_ascii=False, sort_keys=True),
                "penalties": json.dumps(self.result.penalties, ensure_ascii=False, sort_keys=True),
                "required_test_budget": self.result.required_test_budget,
            }
        )
        row.pop("metadata", None)
        return row


def report_stem() -> str:
    return datetime.now(timezone.utc).strftime("recherche-%Y-%m-%dT%H-%M-%S-%fZ")


def write_reports(items: list[EvaluatedCandidate], directory: str | Path) -> dict[str, Path]:
    output_dir = Path(directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = report_stem()
    rows = [item.flat_dict() for item in items]

    json_path = output_dir / f"{stem}.json"
    json_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    csv_path = output_dir / f"{stem}.csv"
    headers = sorted({key for row in rows for key in row}) if rows else []
    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    markdown_path = output_dir / f"{stem}.md"
    lines = [f"# Classement historique indicatif — {stem}", "", "Aucune qualification commerciale : appliquer les critères canoniques du pipeline.", ""]
    for item in sorted(items, key=lambda candidate: candidate.result.score or -1, reverse=True):
        lines.extend(
            [
                f"## {item.product.product_name}",
                f"- Source : {item.product.source}",
                f"- Marché : {item.product.market}",
                f"- Score : {item.result.score if item.result.score is not None else 'rejet direct'}",
                f"- Décision broyeur : {item.result.decision}",
                f"- Qualification actuelle : {item.result.verdict}",
                f"- Drapeaux : {', '.join(item.result.flags) or 'aucun'}",
                f"- Doublon : {'non' if item.inserted else 'oui'}",
                "",
            ]
        )
    markdown_path.write_text("\n".join(lines), encoding="utf-8")
    latest_json = output_dir / "latest.json"
    latest_csv = output_dir / "latest.csv"
    latest_markdown = output_dir / "latest.md"
    shutil.copyfile(json_path, latest_json)
    shutil.copyfile(csv_path, latest_csv)
    shutil.copyfile(markdown_path, latest_markdown)
    return {
        "json": json_path,
        "csv": csv_path,
        "markdown": markdown_path,
        "latest_json": latest_json,
        "latest_csv": latest_csv,
        "latest_markdown": latest_markdown,
    }
