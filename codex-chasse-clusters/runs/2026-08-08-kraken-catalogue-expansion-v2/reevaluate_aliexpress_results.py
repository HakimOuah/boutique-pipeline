#!/usr/bin/env python3
"""Reevalue hors ligne les reponses API apres enrichissement des synonymes.

Aucune nouvelle requete fournisseur n'est lancee. Seuls les blocs `match`
sont recalcules a partir du titre deja conserve et du concept correspondant.
"""

from __future__ import annotations

import importlib.util
import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
CONCEPTS = RUN_DIR / "competitor-concepts-merged.json"
CONCEPT_RAW = RUN_DIR / "aliexpress-concept-search.json"
ANCHOR_RAW = RUN_DIR / "aliexpress-anchor-search.json"
MATCH_SOURCE = RUN_DIR / "source_aliexpress_catalogue.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Module introuvable: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def atomic_write(path: Path, payload: object) -> None:
    handle, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as stream:
            json.dump(payload, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def main() -> int:
    matcher = load_module("kraken_matcher_reevaluation", MATCH_SOURCE)
    concepts_payload = json.loads(CONCEPTS.read_text(encoding="utf-8"))
    concept_map = {(row["niche"], row["concept_key"]): row for row in concepts_payload["concepts"]}
    concept_raw = json.loads(CONCEPT_RAW.read_text(encoding="utf-8"))
    anchor_raw = json.loads(ANCHOR_RAW.read_text(encoding="utf-8"))

    concept_items = 0
    concept_semantic = 0
    concept_quality = 0
    missing_concepts = []
    for result in concept_raw.get("results", []):
        concept = concept_map.get((result.get("niche"), result.get("concept_key")))
        if not concept:
            missing_concepts.append([result.get("niche"), result.get("concept_key")])
            continue
        for item in result.get("items", []):
            item["match"] = matcher.evaluate_match(concept, item)
            concept_items += 1
            concept_semantic += int(item["match"]["semantic_ok"])
            concept_quality += int(item["match"]["semantic_ok"] and item["match"]["supplier_quality_ok"])
    concept_raw["reevaluated_at_utc"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    concept_raw["reevaluation"] = "Synonymes controles par niche/type; aucune nouvelle requete API."
    atomic_write(CONCEPT_RAW, concept_raw)

    anchor_items = 0
    anchor_semantic = 0
    anchor_quality = 0
    for result in anchor_raw.get("results", []):
        concept = {
            "niche": result["niche"],
            "concept_fr_normalized": result["keyword_fr"],
            "keyword_fr_candidate": result["keyword_fr"],
            "competitor_product_title": result["keyword_fr"],
        }
        for item in result.get("items", []):
            item["match"] = matcher.evaluate_match(concept, item)
            anchor_items += 1
            anchor_semantic += int(item["match"]["semantic_ok"])
            anchor_quality += int(item["match"]["semantic_ok"] and item["match"]["supplier_quality_ok"])
    anchor_raw["reevaluated_at_utc"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    anchor_raw["reevaluation"] = "Synonymes controles par niche/type; aucune nouvelle requete API."
    atomic_write(ANCHOR_RAW, anchor_raw)

    print(json.dumps({
        "ok": not missing_concepts,
        "concept_items": concept_items,
        "concept_semantic": concept_semantic,
        "concept_semantic_and_quality": concept_quality,
        "anchor_items": anchor_items,
        "anchor_semantic": anchor_semantic,
        "anchor_semantic_and_quality": anchor_quality,
        "missing_concepts": missing_concepts[:20],
    }, ensure_ascii=False, indent=2))
    return 0 if not missing_concepts else 2


if __name__ == "__main__":
    raise SystemExit(main())
