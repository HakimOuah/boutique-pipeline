#!/usr/bin/env python3
"""Validation deterministe du catalogue final avant generation du classeur."""

from __future__ import annotations

import json
import re
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


RUN_DIR = Path(__file__).resolve().parent
SOURCE = RUN_DIR / "final-catalogue-reviewed.json"
OUT = RUN_DIR / "final-catalogue-gate-report.json"

IP_TERMS = {
    "barbie", "disney", "dragon ball", "harry potter", "hello kitty", "lego",
    "marvel", "minecraft", "naruto", "one piece", "pokemon", "sanrio",
    "star wars", "stitch", "super mario", "winnie", "mickey", "minnie",
}


def normalize(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value or ""))
    text = "".join(char for char in text if not unicodedata.combining(char))
    text = text.lower().replace("&", " et ")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def valid_http(value: object) -> bool:
    parsed = urlparse(str(value or ""))
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def orders_number(value: object) -> int:
    match = re.search(r"([\d.,]+)", str(value or ""))
    if not match:
        return 0
    try:
        return int(match.group(1).replace(".", "").replace(",", ""))
    except ValueError:
        return 0


def main() -> int:
    payload = json.loads(SOURCE.read_text(encoding="utf-8"))
    products = payload.get("products", [])
    errors = []
    counts = Counter(row.get("niche") for row in products)
    targets = payload.get("reference_targets_by_niche") or payload.get("targets_by_niche", {})
    quota_gaps = {
        niche: counts[niche] - int(targets.get(niche, 0))
        for niche in payload.get("root_keywords", {})
    }

    ids = Counter((row.get("niche"), str(row.get("aliexpress", {}).get("product_id") or "")) for row in products)
    titles = Counter((row.get("niche"), normalize(row.get("seo", {}).get("product_title"))) for row in products)
    for index, row in enumerate(products, start=1):
        seo = row.get("seo", {})
        item = row.get("aliexpress", {})
        match = item.get("match", {})
        final_keyword_match = item.get("final_keyword_match", {})
        supplier_status = row.get("supplier_evidence_status")
        keyword_status = row.get("keyword_evidence_status")
        product_keyword = normalize(seo.get("product_keyword"))
        collection_keyword = normalize(seo.get("collection_keyword"))
        title = normalize(seo.get("product_title"))
        collection_title = normalize(seo.get("collection_title"))
        row_errors = []
        if row.get("manual_review", {}).get("decision") != "ACCEPT":
            row_errors.append("revue_humaine_accept_absente")
        if not product_keyword or product_keyword not in title:
            row_errors.append("titre_sans_mot_cle_produit")
        if not collection_keyword or collection_keyword not in collection_title:
            row_errors.append("collection_sans_mot_cle")
        if not isinstance(seo.get("product_volume"), int) or seo["product_volume"] <= 0:
            row_errors.append("volume_produit_non_positif")
        if not isinstance(seo.get("collection_volume"), int) or seo["collection_volume"] <= 0:
            row_errors.append("volume_collection_non_positif")
        if not isinstance(row.get("root_volume"), int) or row["root_volume"] <= 0:
            row_errors.append("volume_general_non_positif")
        if not valid_http(item.get("listing_url")):
            row_errors.append("lien_aliexpress_invalide")
        if ids[(row.get("niche"), str(item.get("product_id") or ""))] != 1:
            row_errors.append("product_id_duplique")
        if titles[(row.get("niche"), title)] != 1:
            row_errors.append("titre_seo_duplique")
        if item.get("price") in (None, ""):
            row_errors.append("prix_listing_absent")
        if supplier_status == "LISTING_QUALIFIE_NOTE_COMMANDES":
            try:
                if float(str(item.get("rating")).replace(",", ".")) < 4.5:
                    row_errors.append("note_sous_4_5_pour_tier_qualifie")
            except (TypeError, ValueError):
                row_errors.append("note_manquante_pour_tier_qualifie")
            if orders_number(item.get("orders")) <= 0:
                row_errors.append("commande_absente_pour_tier_qualifie")
        elif supplier_status != "LISTING_SEMANTIQUE_A_VERIFIER":
            row_errors.append("statut_preuve_fournisseur_invalide")
        if not match.get("semantic_ok"):
            row_errors.append("pertinence_semantique_echec")
        if keyword_status == "MOT_CLE_DIRECT_DANS_LISTING":
            if not final_keyword_match.get("semantic_ok"):
                row_errors.append("mot_cle_direct_non_prouve")
        else:
            row_errors.append("statut_preuve_mot_cle_invalide")
        ip_hits = sorted(term for term in IP_TERMS if term in normalize(item.get("title")))
        if ip_hits:
            row_errors.append(f"terme_ip:{','.join(ip_hits)}")
        if row.get("candidate_origin") == "EQUIVALENT_CONCURRENT_API" and not valid_http(row.get("competitor_product_url")):
            row_errors.append("preuve_concurrente_invalide")
        if row_errors:
            errors.append({"row": index, "niche": row.get("niche"), "product_id": item.get("product_id"), "reasons": row_errors})

    report = {
        "ok": not errors,
        "integrity_ok": not errors,
        "products": len(products),
        "counts_by_niche": dict(sorted(counts.items())),
        "reference_targets_by_niche": targets,
        "quota_gaps_by_niche": quota_gaps,
        "quota_reference_pass": all(value >= 0 for value in quota_gaps.values()),
        "unique_ids_by_niche": len(ids),
        "unique_titles_by_niche": len(titles),
        "errors": errors,
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key != "errors"}, ensure_ascii=False, indent=2))
    if errors:
        print(json.dumps({"first_errors": errors[:20]}, ensure_ascii=False, indent=2))
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
