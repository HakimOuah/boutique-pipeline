from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any

from .models import ProductCandidate


def _load_json(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("products", data.get("items", [data]))
    if not isinstance(data, list):
        raise ValueError("Le JSON doit contenir un objet ou une liste de produits")
    return [item for item in data if isinstance(item, dict)]


def _load_csv(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _load_markdown(path: Path) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8")
    blocks = re.split(r"\n---+\n", text)
    rows: list[dict[str, Any]] = []
    for block in blocks:
        row: dict[str, Any] = {}
        for line in block.splitlines():
            heading = re.match(r"^#+\s+(.+)$", line.strip())
            if heading:
                row["product_name"] = heading.group(1).strip()
                continue
            pair = re.match(r"^-\s*([\w-]+)\s*:\s*(.*)$", line.strip())
            if pair:
                row[pair.group(1).lower().replace("-", "_")] = pair.group(2).strip()
        if row.get("product_name"):
            rows.append(row)
    return rows


def load_candidates(path: str | Path, input_format: str | None = None, source: str | None = None) -> list[ProductCandidate]:
    input_path = Path(path)
    fmt = (input_format or input_path.suffix.lstrip(".")).lower()
    if fmt in {"json"}:
        rows = _load_json(input_path)
    elif fmt in {"csv", "tsv"}:
        rows = _load_csv(input_path)
    elif fmt in {"md", "markdown"}:
        rows = _load_markdown(input_path)
    else:
        raise ValueError(f"Format non supporté : {fmt}")
    candidates: list[ProductCandidate] = []
    errors: list[str] = []
    for index, row in enumerate(rows, start=1):
        enriched = dict(row)
        if source and not enriched.get("source"):
            enriched["source"] = source
        try:
            candidates.append(ProductCandidate.from_mapping(enriched))
        except ValueError as error:
            errors.append(f"ligne {index}: {error}")
    if errors:
        raise ValueError("Entrées invalides : " + "; ".join(errors))
    return candidates
