from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

import yaml


def _read_rows(path: Path) -> list[dict[str, Any]]:
    if path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data = data.get("items", data.get("products", [data]))
        if not isinstance(data, list):
            raise ValueError("Le fichier source JSON doit contenir une liste")
        return [row for row in data if isinstance(row, dict)]
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _value_at(row: dict[str, Any], dotted_path: str) -> Any:
    value: Any = row
    for segment in dotted_path.split("."):
        if not isinstance(value, dict):
            return None
        value = value.get(segment)
    return value


def map_source_file(input_path: str | Path, mapping_path: str | Path) -> list[dict[str, Any]]:
    mapping = yaml.safe_load(Path(mapping_path).read_text(encoding="utf-8"))
    if not isinstance(mapping, dict) or not isinstance(mapping.get("fields"), dict):
        raise ValueError("Le mapping doit définir une section fields")
    rows = []
    for raw in _read_rows(Path(input_path)):
        target = dict(mapping.get("constants", {}))
        for destination, source in mapping["fields"].items():
            if source:
                target[destination] = _value_at(raw, str(source))
        target["metadata"] = {"source_record": raw}
        rows.append(target)
    return rows


def write_mapped_json(rows: list[dict[str, Any]], output_path: str | Path) -> Path:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return output

