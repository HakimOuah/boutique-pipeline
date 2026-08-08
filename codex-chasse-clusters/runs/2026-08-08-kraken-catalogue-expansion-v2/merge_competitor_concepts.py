#!/usr/bin/env python3
"""Valide et fusionne les concepts catalogue issus des audits concurrents."""

from __future__ import annotations

import json
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[3]
RUN_DIR = Path(__file__).resolve().parent
OUT = RUN_DIR / "competitor-concepts-merged.json"
REPORT = RUN_DIR / "competitor-concepts-validation.json"

INPUTS = [
    ROOT / "competitor-profiles/workstreams/catalogue-expansion-chien-aquarium.json",
    ROOT / "competitor-profiles/workstreams/catalogue-expansion-mercerie-scrap.json",
    ROOT / "competitor-profiles/workstreams/catalogue-expansion-perles.json",
]

NICHES = {
    "balade transport mobilite du chien": "Balade, transport & mobilité du chien",
    "chien": "Balade, transport & mobilité du chien",
    "aquariophilie aquascaping": "Aquariophilie & aquascaping",
    "aquarium": "Aquariophilie & aquascaping",
    "mercerie creative arts du fil": "Mercerie créative & arts du fil",
    "mercerie": "Mercerie créative & arts du fil",
    "scrapbooking journaling": "Scrapbooking & journaling",
    "scrapbooking": "Scrapbooking & journaling",
    "perles creation de bijoux": "Perles & création de bijoux",
    "perles et creation de bijoux": "Perles & création de bijoux",
    "perles bijoux": "Perles & création de bijoux",
    "perles": "Perles & création de bijoux",
}

REQUIRED = (
    "niche",
    "competitor",
    "competitor_domain",
    "competitor_collection",
    "concept_fr_normalized",
    "distinctness_basis",
    "keyword_fr_candidate",
    "aliexpress_query_en",
    "evidence_status",
    "observed_at",
    "source_url",
)

EVIDENCE = {"OBSERVE_CONCURRENT", "EQUIVALENT_DERIVE"}
COLORS = {
    "beige", "blanc", "blanche", "bleu", "bleue", "brun", "brune",
    "dore", "doree", "gris", "grise", "jaune", "marron", "noir", "noire",
    "orange", "rose", "rouge", "vert", "verte", "violet", "violette",
    "argent", "argente", "multicolore", "transparent", "transparente",
}
VARIANT_WORDS = COLORS | {
    "taille", "coloris", "couleur", "petit", "petite", "moyen", "moyenne",
    "grand", "grande", "xl", "xxl", "xs", "lot", "pack", "set", "piece",
    "pieces", "unite", "unites", "assorti", "assortie", "nouveau", "nouvelle",
    "premium", "pro", "professionnel", "professionnelle", "super", "ultra",
    "maxi", "mini", "classique", "ergonomique",
}

GLOBAL_FORBIDDEN = (
    r"\b(?:e ?book|pdf|formation|cours|tutoriel|tuto|guide numerique|carte cadeau|bon d achat|abonnement)\b",
    r"\b(?:realiser|apprendre|comment faire|patron numerique|telechargement)\b",
)

SCOPE_FORBIDDEN = {
    "Balade, transport & mobilité du chien": (
        r"\b(?:jouet|puzzle|canape|panier couchage|shampoing|toilettage|friandise alimentaire|croquette)\b",
    ),
    "Aquariophilie & aquascaping": (
        r"\b(?:reconditionne|piece detachee|rotor pour pompe|couvercle decantation)\b",
        r"\b(?:nourriture congelee|poisson vivant|crevette vivante|plante vivante|bacteries vivantes)\b",
        r"\blot de \d+\s*(?:x\s*)?(?:crevette|poisson)\b",
    ),
    "Mercerie créative & arts du fil": (
        r"\b(?:produit fini|robe finie|sac fini|vetement fini)\b",
    ),
    "Scrapbooking & journaling": (
        r"\b(?:coloriage a imprimer|fichier de decoupe|modele numerique)\b",
    ),
    "Perles & création de bijoux": (
        r"\b(?:bijou fini de marque|montre|parfum)\b",
    ),
}


def normalize(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value or ""))
    text = "".join(char for char in text if not unicodedata.combining(char))
    text = text.lower().replace("&", " et ")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def canonical_niche(value: object) -> str | None:
    key = normalize(value)
    if key in NICHES:
        return NICHES[key]
    for alias, canonical in NICHES.items():
        if alias in key or key in alias:
            return canonical
    return None


def is_http_url(value: object) -> bool:
    parsed = urlparse(str(value or ""))
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def extract_rows(payload: object) -> list[dict]:
    if isinstance(payload, list):
        return [row for row in payload if isinstance(row, dict)]
    if isinstance(payload, dict):
        for key in ("products", "concepts", "rows", "items"):
            value = payload.get(key)
            if isinstance(value, list):
                return [row for row in value if isinstance(row, dict)]
    return []


def variant_base(value: object) -> str:
    tokens = [
        token
        for token in normalize(value).split()
        if token not in VARIANT_WORDS
        and not re.fullmatch(r"\d+(?:mm|cm|m|g|kg|ml|l)?", token)
    ]
    return " ".join(tokens)


def scope_reasons(row: dict, niche: str) -> list[str]:
    text = " ".join(
        normalize(row.get(field))
        for field in (
            "competitor_collection",
            "competitor_product_title",
            "concept_fr_normalized",
            "keyword_fr_candidate",
        )
    )
    reasons = []
    for pattern in GLOBAL_FORBIDDEN:
        if re.search(pattern, text):
            reasons.append("hors_scope_numerique_contenu_service")
            break
    for pattern in SCOPE_FORBIDDEN.get(niche, ()):
        if re.search(pattern, text):
            reasons.append("hors_scope_niche_ou_non_sourceable")
            break
    return reasons


def main() -> int:
    accepted: list[dict] = []
    rejected: list[dict] = []
    missing_inputs: list[str] = []
    source_counts: dict[str, int] = {}

    for source in INPUTS:
        if not source.is_file():
            missing_inputs.append(str(source.relative_to(ROOT)))
            continue
        payload = json.loads(source.read_text(encoding="utf-8"))
        rows = extract_rows(payload)
        source_counts[str(source.relative_to(ROOT))] = len(rows)
        for index, original in enumerate(rows, start=1):
            row = {key: (value.strip() if isinstance(value, str) else value) for key, value in original.items()}
            reasons = [f"champ_manquant:{field}" for field in REQUIRED if not row.get(field)]
            niche = canonical_niche(row.get("niche"))
            if not niche:
                reasons.append("niche_inconnue")
            if row.get("evidence_status") not in EVIDENCE:
                reasons.append("evidence_status_invalide")
            if not is_http_url(row.get("source_url")):
                reasons.append("source_url_invalide")
            if not normalize(row.get("concept_fr_normalized")):
                reasons.append("concept_vide")
            if not normalize(row.get("keyword_fr_candidate")):
                reasons.append("mot_cle_vide")
            if len(normalize(row.get("aliexpress_query_en")).split()) < 2:
                reasons.append("requete_aliexpress_trop_large")
            if niche:
                reasons.extend(scope_reasons(row, niche))
            if reasons:
                rejected.append({"source": str(source.relative_to(ROOT)), "row": index, "reasons": reasons, "data": row})
                continue
            accepted.append(
                {
                    **row,
                    "niche": niche,
                    "concept_key": normalize(row["concept_fr_normalized"]),
                    "keyword_key": normalize(row["keyword_fr_candidate"]),
                    "variant_base": variant_base(row["concept_fr_normalized"]),
                    "input_source": str(source.relative_to(ROOT)),
                    "input_row": index,
                }
            )

    unique: list[dict] = []
    duplicate_rows: list[dict] = []
    seen_concepts: set[tuple[str, str]] = set()
    seen_source_urls: set[tuple[str, str]] = set()
    for row in sorted(accepted, key=lambda item: (item["niche"], item["concept_key"], item["source_url"])):
        concept_key = (row["niche"], row["concept_key"])
        # `source_url` peut designer le sitemap ou le flux brut commun a de
        # nombreuses lignes. Pour une observation produit, l'URL PDP est la
        # preuve discriminante lorsqu'elle est disponible.
        evidence_url = row.get("competitor_product_url") or row["source_url"]
        source_key = (row["niche"], evidence_url)
        if concept_key in seen_concepts:
            duplicate_rows.append({"reason": "concept_exact_duplique", "data": row})
            continue
        if row["evidence_status"] == "OBSERVE_CONCURRENT" and source_key in seen_source_urls:
            duplicate_rows.append({"reason": "source_produit_duplique", "data": row})
            continue
        seen_concepts.add(concept_key)
        if row["evidence_status"] == "OBSERVE_CONCURRENT":
            seen_source_urls.add(source_key)
        unique.append(row)

    variant_groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for row in unique:
        if row["variant_base"]:
            variant_groups[(row["niche"], row["variant_base"])].append(row)
    variant_alerts = [
        {
            "niche": niche,
            "variant_base": base,
            "count": len(rows),
            "concepts": [row["concept_fr_normalized"] for row in rows],
            "review": "Verifier qu'il s'agit de modeles/matieres/usages distincts et non de couleurs, tailles ou quantites.",
        }
        for (niche, base), rows in variant_groups.items()
        if len(rows) > 1
    ]

    counts = Counter(row["niche"] for row in unique)
    generated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    output = {
        "run_id": RUN_DIR.name,
        "generated_at_utc": generated_at,
        "gate": "concept concurrent distinct avant sourcing AliExpress",
        "counts_by_niche": dict(sorted(counts.items())),
        "concepts": unique,
    }
    validation = {
        "run_id": RUN_DIR.name,
        "generated_at_utc": generated_at,
        "input_counts": source_counts,
        "missing_inputs": missing_inputs,
        "accepted_before_dedup": len(accepted),
        "accepted_after_dedup": len(unique),
        "counts_by_niche": dict(sorted(counts.items())),
        "rejected": rejected,
        "duplicates": duplicate_rows,
        "variant_review_alerts": variant_alerts,
        "gate_200_by_niche": {niche: count >= 200 for niche, count in counts.items()},
    }
    OUT.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": not missing_inputs, "counts_by_niche": dict(counts), "missing_inputs": missing_inputs}, ensure_ascii=False, indent=2))
    return 0 if not missing_inputs else 2


if __name__ == "__main__":
    raise SystemExit(main())
