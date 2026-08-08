#!/usr/bin/env python3
"""Reprend les mesures SEMrush France deja observees dans le run v1."""

from __future__ import annotations

import json
import importlib.util
import re
from datetime import datetime, timezone
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[3]
SOURCE_BUILDER = ROOT / "codex-chasse-clusters/runs/2026-08-08-kraken-catalogue-v1/build_competitor_workbook.mjs"
SOURCE_QUERIES = ROOT / "codex-chasse-clusters/runs/2026-08-08-kraken-catalogue-v1/collect_aliexpress.py"
OUTPUT = RUN_DIR / "keyword-volumes-fr.json"

ROOT_KEYWORDS = {
    "Mercerie créative & arts du fil": ("mercerie", 27100),
    "Scrapbooking & journaling": ("scrapbooking", 27100),
    "Aquariophilie & aquascaping": ("filtre aquarium", 3600),
    "Balade, transport & mobilité du chien": ("harnais chien", 22200),
    "Perles & création de bijoux": ("perles pour bijoux", 720),
}

# Totaux commerciaux nettoyes du run v1. Ils proviennent de clusters plus
# larges que les 100 ancres catalogue et ne doivent pas etre recalcules en
# additionnant les volumes repetes sur chaque PDP.
CLEAN_TOTALS = {
    "Balade, transport & mobilité du chien": 81860,
    "Mercerie créative & arts du fil": 221680,
    "Scrapbooking & journaling": 64740,
    "Perles & création de bijoux": 35770,
    "Aquariophilie & aquascaping": 48320,
}


def extract_volumes(source: str) -> dict[str, int]:
    match = re.search(r"const VOLUMES = (\{.*?\n\});", source, flags=re.S)
    if not match:
        raise RuntimeError("Bloc VOLUMES introuvable dans le builder v1")
    literal = re.sub(r",\s*([}\]])", r"\1", match.group(1))
    payload = json.loads(literal)
    if not all(isinstance(key, str) and isinstance(value, int) for key, value in payload.items()):
        raise RuntimeError("Format VOLUMES inattendu")
    return payload


def keyword_niches() -> dict[str, list[str]]:
    spec = importlib.util.spec_from_file_location("kraken_v1_collect", SOURCE_QUERIES)
    if spec is None or spec.loader is None:
        raise RuntimeError("Impossible de charger les requetes du run v1")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    mapping: dict[str, set[str]] = {}
    for niche, entries in module.QUERIES.items():
        for _parent, _collection, keyword, _query_en in entries:
            mapping.setdefault(keyword, set()).add(niche)
    for niche, (keyword, _volume) in ROOT_KEYWORDS.items():
        mapping.setdefault(keyword, set()).add(niche)
    return {keyword: sorted(niches) for keyword, niches in mapping.items()}


def main() -> int:
    volumes = extract_volumes(SOURCE_BUILDER.read_text(encoding="utf-8"))
    niche_map = keyword_niches()
    rows = [
        {
            "keyword": keyword,
            "volume": volume,
            "niches": niche_map.get(keyword, []),
            "database": "fr",
            "country": "France",
            "observed_at": "2026-08-08",
            "status": "OBSERVE_SEMRUSH_FR",
            "source_run": "2026-08-08-kraken-catalogue-v1",
            "eligible_product_anchor": volume > 0,
            "eligible_collection_core": volume >= 1000,
            "eligible_collection_secondary": volume >= 500,
            "collection_review_zone": 300 <= volume < 500,
        }
        for keyword, volume in sorted(volumes.items())
    ]
    anchor_totals = {
        niche: sum(row["volume"] for row in rows if niche in row["niches"] and row["volume"] > 0)
        for niche in ROOT_KEYWORDS
    }
    output = {
        "run_id": RUN_DIR.name,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "SEMrush France, mesures observees le 2026-08-08 et reprises du run v1",
        "database": "fr",
        "measurement_note": "Valeurs reprises sans re-mesure lorsqu'elles existent deja le meme jour; les nouveaux termes seront ajoutes avec leur propre preuve.",
        "thresholds": {
            "boutique_minimum_clean": 30000,
            "boutique_comfort": 40000,
            "collection_core": 1000,
            "collection_secondary": 500,
            "collection_review_low": 300,
            "product_minimum": None,
        },
        "root_keywords": {
            niche: {"keyword": keyword, "volume": volume}
            for niche, (keyword, volume) in ROOT_KEYWORDS.items()
        },
        "clean_totals_by_niche": CLEAN_TOTALS,
        "measured_anchor_union_by_niche": anchor_totals,
        "keywords": rows,
    }
    OUTPUT.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "output": str(OUTPUT), "keyword_count": len(rows)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
