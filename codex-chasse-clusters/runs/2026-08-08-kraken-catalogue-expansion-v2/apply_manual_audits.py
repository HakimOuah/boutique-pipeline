#!/usr/bin/env python3
"""Applique les decisions humaines aux candidats machine sans les remplacer.

Le filtre manuel est une porte finale : une ligne rejetee n'est jamais
remplacee automatiquement par un candidat non relu afin de gonfler un quota.
"""

from __future__ import annotations

import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
ROOT = RUN_DIR.parents[2]
SOURCE = RUN_DIR / "final-catalogue.json"
OUT = RUN_DIR / "final-catalogue-reviewed.json"
REPORT = RUN_DIR / "manual-audit-summary.json"
AUDIT_FILES = [
    ROOT / "competitor-profiles/workstreams/manual-audit-final-chien-aquarium.json",
    ROOT / "competitor-profiles/workstreams/manual-audit-final-mercerie-scrap.json",
    ROOT / "competitor-profiles/workstreams/manual-audit-final-perles.json",
]


def audit_rows(payload: object) -> list[dict]:
    if isinstance(payload, list):
        return [row for row in payload if isinstance(row, dict)]
    if not isinstance(payload, dict):
        return []
    for key in ("rows", "decisions", "products", "audit", "items"):
        value = payload.get(key)
        if isinstance(value, list):
            return [row for row in value if isinstance(row, dict)]
    return []


def normalized_decision(row: dict) -> str:
    value = str(row.get("decision") or row.get("status") or row.get("verdict") or "").strip().upper()
    if value in {"ACCEPT", "ACCEPTE", "ACCEPTED", "KEEP", "OK", "OUI"}:
        return "ACCEPT"
    if value in {"REJECT", "REJETE", "REJECTED", "DROP", "NON"}:
        return "REJECT"
    return value


def reason_text(row: dict) -> str:
    value = row.get("reason") or row.get("reasons") or row.get("motif") or ""
    if isinstance(value, list):
        return "; ".join(str(item) for item in value)
    return str(value)


def main() -> int:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    products = source.get("products", [])
    source_keys = {(row["niche"], str(row["aliexpress"]["product_id"])) for row in products}
    niche_by_product_id = {}
    duplicate_global_ids = set()
    for niche, product_id in source_keys:
        if product_id in niche_by_product_id and niche_by_product_id[product_id] != niche:
            duplicate_global_ids.add(product_id)
        niche_by_product_id[product_id] = niche

    decisions: dict[tuple[str, str], dict] = {}
    errors = []
    for path in AUDIT_FILES:
        if not path.is_file():
            errors.append({"reason": "audit_manquant", "path": str(path)})
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        for row in audit_rows(payload):
            product_id = str(row.get("product_id") or row.get("aliexpress_product_id") or "").strip()
            niche = str(row.get("niche") or "").strip()
            if not niche and product_id and product_id not in duplicate_global_ids:
                niche = niche_by_product_id.get(product_id, "")
            decision = normalized_decision(row)
            key = (niche, product_id)
            if not niche or not product_id:
                errors.append({"reason": "cle_audit_incomplete", "path": str(path), "row": row})
                continue
            if decision not in {"ACCEPT", "REJECT"}:
                errors.append({"reason": "decision_invalide", "path": str(path), "key": key, "decision": decision})
                continue
            if key in decisions:
                errors.append({"reason": "decision_dupliquee", "key": key})
                continue
            decisions[key] = {
                "decision": decision,
                "reason": reason_text(row),
                "audit_file": str(path.relative_to(ROOT)),
            }

    missing = sorted(source_keys - set(decisions))
    unexpected = sorted(set(decisions) - source_keys)
    if missing:
        errors.append({"reason": "produits_sans_decision", "count": len(missing), "examples": missing[:20]})
    if unexpected:
        errors.append({"reason": "decisions_hors_catalogue", "count": len(unexpected), "examples": unexpected[:20]})
    if errors:
        REPORT.write_text(json.dumps({"ok": False, "errors": errors}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"ok": False, "errors": errors[:10]}, ensure_ascii=False, indent=2))
        return 2

    reviewed = []
    rejected = []
    for row in products:
        key = (row["niche"], str(row["aliexpress"]["product_id"]))
        review = decisions[key]
        enriched = {**row, "manual_review": review}
        if review["decision"] == "ACCEPT":
            reviewed.append(enriched)
        else:
            rejected.append({
                "niche": row["niche"],
                "product_id": key[1],
                "keyword": row["seo"]["product_keyword"],
                "supplier_title": row["aliexpress"].get("title"),
                **review,
            })

    counts = Counter(row["niche"] for row in reviewed)
    collection_counts = Counter((row["niche"], row["seo"]["collection_keyword"]) for row in reviewed)
    origin_counts = Counter((row["niche"], row["candidate_origin"]) for row in reviewed)
    reviewed.sort(key=lambda row: (row["niche"], row["seo"]["collection_keyword"], row["catalogue_rank"]))
    generated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    payload = {
        **source,
        "generated_at_utc": generated_at,
        "reviewed_from": SOURCE.name,
        "machine_counts_by_niche": source.get("counts_by_niche", {}),
        "counts_by_niche": {niche: counts[niche] for niche in source["root_keywords"]},
        "reference_targets_by_niche": source.get("targets_by_niche", {}),
        "gate_reference_target_by_niche": {
            niche: counts[niche] >= source.get("targets_by_niche", {}).get(niche, 0)
            for niche in source["root_keywords"]
        },
        "gate_100_by_niche": {niche: counts[niche] >= 100 for niche in source["root_keywords"]},
        "gate_200_by_niche": {niche: counts[niche] >= 200 for niche in source["root_keywords"]},
        "collections": [
            {
                **collection,
                "product_count": collection_counts[(collection["niche"], collection["collection_keyword"])],
            }
            for collection in source.get("collections", [])
            if collection_counts[(collection["niche"], collection["collection_keyword"])] > 0
        ],
        "origin_counts": [
            {"niche": niche, "origin": origin, "count": count}
            for (niche, origin), count in sorted(origin_counts.items())
        ],
        "manual_review": {
            "status": "EXHAUSTIF_SUR_CATALOGUE_MACHINE",
            "reviewed_at_utc": generated_at,
            "reviewed_count": len(products),
            "accepted_count": len(reviewed),
            "rejected_count": len(rejected),
            "audit_files": [str(path.relative_to(ROOT)) for path in AUDIT_FILES],
        },
        "products": reviewed,
    }
    report = {
        "ok": True,
        "generated_at_utc": generated_at,
        "machine_products": len(products),
        "accepted_products": len(reviewed),
        "rejected_products": len(rejected),
        "machine_counts_by_niche": source.get("counts_by_niche", {}),
        "accepted_counts_by_niche": payload["counts_by_niche"],
        "gate_100_by_niche": payload["gate_100_by_niche"],
        "gate_200_by_niche": payload["gate_200_by_niche"],
        "rejection_reasons": dict(Counter(row["reason"] or "MOTIF_NON_RENSEIGNE" for row in rejected)),
        "rejected": rejected,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key not in {"rejected", "rejection_reasons"}}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
