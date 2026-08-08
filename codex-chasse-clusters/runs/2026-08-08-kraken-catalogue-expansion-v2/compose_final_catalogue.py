#!/usr/bin/env python3
"""Compose un catalogue final de 200 PDP par niche avec preuve SEO et fournisseur.

Priorite 1 : equivalences trouvees pour les produits concurrents observes.
Priorite 2 : listings qualifies trouves dans les familles SEO mesurees.

Le fichier produit reste un plan de catalogue read-only. Un resultat de
recherche AliExpress prouve l'existence d'un listing, pas encore le SKU exact,
le fret France, la conformite ou la marge.
"""

from __future__ import annotations

import importlib.util
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RUN_DIR = Path(__file__).resolve().parent
CONCEPTS = RUN_DIR / "competitor-concepts-merged.json"
CONCEPT_SEARCH = RUN_DIR / "aliexpress-concept-search.json"
ANCHOR_PRODUCTS = RUN_DIR / "aliexpress-anchor-candidates.json"
VOLUMES = RUN_DIR / "keyword-volumes-fr.json"
ASSIGN_SOURCE = RUN_DIR / "assign_catalogue_architecture.py"
MATCH_SOURCE = RUN_DIR / "source_aliexpress_catalogue.py"
OUT = RUN_DIR / "final-catalogue.json"
REPORT = RUN_DIR / "final-catalogue-validation.json"

TARGETS_BY_NICHE = {
    "Aquariophilie & aquascaping": 100,
    "Balade, transport & mobilité du chien": 100,
    "Mercerie créative & arts du fil": 200,
    "Perles & création de bijoux": 200,
    "Scrapbooking & journaling": 100,
}

COLOR_WORDS = {
    "argent", "argente", "beige", "blanc", "blanche", "bleu", "bleue",
    "brun", "brune", "dore", "doree", "gris", "grise", "jaune", "marron",
    "noir", "noire", "orange", "rose", "rouge", "transparent", "transparente",
    "vert", "verte", "violet", "violette", "multicolore",
}

SIGNATURE_NOISE = COLOR_WORDS | {
    "achat", "avec", "choix", "couleur", "couleurs", "ensemble", "haute",
    "qualite", "lot", "lots", "modele", "nouveau", "nouvelle", "pack",
    "piece", "pieces", "premium", "professionnel", "professionnelle", "set",
    "taille", "tailles", "universel", "universelle", "vente", "unite", "unites",
}

RISK_RULES = {
    "Balade, transport & mobilité du chien": [
        (r"harnais|laisse|longe|collier|museliere|ceinture|gilet de sauvetage|rampe|poussette", "SECURITE_ET_CHARGE_A_VALIDER"),
    ],
    "Aquariophilie & aquascaping": [
        (r"chauffage|eclairage|led|pompe|filtre|osmolateur|skimmer", "ELECTRIQUE_ET_ETANCHEITE_A_VALIDER"),
        (r"co2", "PRESSION_CO2_A_VALIDER"),
        (r"traitement|test eau|substrat", "COMPOSITION_ET_BIEN_ETRE_ANIMAL_A_VALIDER"),
    ],
    "Perles & création de bijoux": [
        (r"argent|acier|metal|fermoir|chaine|anneau|crochet|pendentif|breloque", "COMPOSITION_NICKEL_PLOMB_CADMIUM_A_VALIDER"),
        (r"pierre naturelle", "ALLÉGATION_MATIERE_A_VALIDER"),
    ],
    "Mercerie créative & arts du fil": [
        (r"tissu|fil|laine|rembourrage", "MATIERE_ET_COMPOSITION_A_VALIDER"),
    ],
    "Scrapbooking & journaling": [
        (r"colle|encre|poudre", "COMPOSITION_CHIMIQUE_A_VALIDER"),
        (r"tampon|sticker|papier|matrice|die|pochoir", "LICENCE_ET_PROPRIETE_INTELLECTUELLE_A_VALIDER"),
    ],
}


def normalize(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value or ""))
    text = "".join(char for char in text if not unicodedata.combining(char))
    text = text.lower().replace("&", " et ")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Module introuvable: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def orders_number(value: object) -> int:
    match = re.search(r"([\d.,]+)", str(value or ""))
    if not match:
        return 0
    try:
        return int(match.group(1).replace(".", "").replace(",", ""))
    except ValueError:
        return 0


def numeric_value(value: object) -> float:
    try:
        return float(str(value).replace(",", "."))
    except (TypeError, ValueError):
        return 0.0


def product_signature(title: object, keyword: str) -> str:
    keyword_tokens = set(normalize(keyword).split())
    tokens = []
    for token in normalize(title).split():
        if token in keyword_tokens or token in SIGNATURE_NOISE:
            continue
        if re.fullmatch(r"\d+(?:mm|cm|m|g|kg|ml|l|v|w)?", token):
            continue
        if len(token) < 3:
            continue
        tokens.append(token)
    return " ".join(tokens[:18])


def jaccard(left: str, right: str) -> float:
    a, b = set(left.split()), set(right.split())
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def sentence_case(value: str) -> str:
    value = value.strip()
    return value[:1].upper() + value[1:] if value else value


def short_supplier_descriptor(title: object) -> str:
    text = re.sub(r"\s+", " ", str(title or "")).strip(" ,-–—")
    text = re.sub(r"^(?:\d+\s*(?:pcs?|pi[eè]ces?)?\s*[/,-]?\s*)+", "", text, flags=re.I)
    clauses = [part.strip() for part in re.split(r"[,;|]", text) if part.strip()]
    result = clauses[0] if clauses else text
    for clause in clauses[1:]:
        candidate = f"{result}, {clause}"
        if len(candidate) <= 115:
            result = candidate
        else:
            break
    if len(result) > 115:
        result = result[:112].rsplit(" ", 1)[0] + "…"
    return sentence_case(result)


def risk_flag(niche: str, text: str) -> str:
    haystack = normalize(text)
    flags = [flag for pattern, flag in RISK_RULES.get(niche, []) if re.search(pattern, haystack)]
    return "; ".join(dict.fromkeys(flags)) if flags else "CONTROLE_STANDARD_AVANT_IMPORT"


def volume_mapping(concept: dict, volume_payload: dict, assign) -> dict | None:
    volume_map = {normalize(row["keyword"]): row for row in volume_payload["keywords"]}
    niche = concept["niche"]
    candidate_key = normalize(concept.get("keyword_fr_candidate"))
    exact = volume_map.get(candidate_key)
    if exact and niche in exact.get("niches", []) and exact["volume"] > 0:
        row = exact
        status = "MOT_CLE_EXACT_MESURE"
        score = 999
    else:
        haystack = " ".join(str(concept.get(field) or "") for field in (
            "concept_fr_normalized", "keyword_fr_candidate", "competitor_collection",
            "competitor_product_title", "aliexpress_query_fr",
        ))
        candidates = []
        for anchor in volume_payload["keywords"]:
            if niche not in anchor.get("niches", []) or anchor["volume"] <= 0:
                continue
            ok, match_score, _matched = assign.anchor_match(niche, haystack, anchor["keyword"])
            if ok:
                candidates.append((match_score, anchor["volume"], anchor))
        if not candidates:
            return None
        candidates.sort(key=lambda item: (item[0], item[1]), reverse=True)
        score, _volume, row = candidates[0]
        status = "ANCRE_MESUREE_SEMANTIQUE"

    product_keyword = row["keyword"]
    product_volume = row["volume"]
    fallback = assign.COLLECTION_FALLBACKS.get(product_keyword)
    if product_volume >= 300:
        collection_keyword = product_keyword
    elif fallback and normalize(fallback) in volume_map and volume_map[normalize(fallback)]["volume"] > 0:
        collection_keyword = volume_map[normalize(fallback)]["keyword"]
    else:
        collection_keyword = volume_payload["root_keywords"][niche]["keyword"]
    collection_volume = volume_map.get(normalize(collection_keyword), volume_payload["root_keywords"][niche])["volume"]
    return {
        "product_keyword": product_keyword,
        "product_volume": product_volume,
        "collection_keyword": collection_keyword,
        "collection_volume": collection_volume,
        "collection_tier": assign.collection_tier(collection_volume),
        "mapping_status": status,
        "mapping_score": score,
    }


def anchor_mapping(anchor: dict, volume_payload: dict, assign) -> dict:
    volume_map = {normalize(row["keyword"]): row for row in volume_payload["keywords"]}
    niche = anchor["niche"]
    row = volume_map.get(normalize(anchor["keyword_fr"]))
    if row and row["volume"] > 0:
        product_keyword = row["keyword"]
        product_volume = row["volume"]
    else:
        fallback = assign.COLLECTION_FALLBACKS.get(anchor["keyword_fr"])
        fallback_row = volume_map.get(normalize(fallback)) if fallback else None
        if fallback_row and fallback_row["volume"] > 0:
            product_keyword, product_volume = fallback_row["keyword"], fallback_row["volume"]
        else:
            root = volume_payload["root_keywords"][niche]
            product_keyword, product_volume = root["keyword"], root["volume"]
    fallback = assign.COLLECTION_FALLBACKS.get(product_keyword)
    if product_volume >= 300:
        collection_keyword = product_keyword
    elif fallback and normalize(fallback) in volume_map and volume_map[normalize(fallback)]["volume"] > 0:
        collection_keyword = volume_map[normalize(fallback)]["keyword"]
    else:
        collection_keyword = volume_payload["root_keywords"][niche]["keyword"]
    collection_volume = volume_map.get(normalize(collection_keyword), volume_payload["root_keywords"][niche])["volume"]
    return {
        "product_keyword": product_keyword,
        "product_volume": product_volume,
        "collection_keyword": collection_keyword,
        "collection_volume": collection_volume,
        "collection_tier": assign.collection_tier(collection_volume),
        "mapping_status": "ANCRE_API_MESUREE" if row and row["volume"] > 0 else "REPLI_MESURE_POSITIF",
        "mapping_score": 700 if row and row["volume"] > 0 else 500,
    }


def select_balanced(candidates: list[dict], target: int) -> tuple[list[dict], Counter]:
    # Premier passage : un fournisseur par concept concurrent. Deuxieme et
    # troisieme passages : autres listings distincts pour le meme concept.
    # Les decouvertes de famille SEO ferment uniquement le deficit restant.
    stages = sorted(set(row["selection_stage"] for row in candidates))
    selected = []
    rejected = Counter()
    used_ids = set()
    signatures_by_keyword: dict[str, list[str]] = defaultdict(list)
    for stage in stages:
        stage_rows = [row for row in candidates if row["selection_stage"] == stage]
        groups: dict[str, list[dict]] = defaultdict(list)
        for row in stage_rows:
            groups[row["seo"]["product_keyword"]].append(row)
        for rows in groups.values():
            rows.sort(key=lambda row: (
                row["aliexpress"].get("match", {}).get("score", 0),
                orders_number(row["aliexpress"].get("orders")),
                numeric_value(row["aliexpress"].get("rating")),
            ), reverse=True)
        keywords = sorted(groups, key=lambda key: (-groups[key][0]["seo"]["product_volume"], key))
        while keywords and len(selected) < target:
            next_keywords = []
            for keyword in keywords:
                rows = groups[keyword]
                accepted = False
                while rows and not accepted:
                    row = rows.pop(0)
                    product_id = row["aliexpress"]["product_id"]
                    signature = row["product_signature"]
                    if product_id in used_ids:
                        rejected["listing_id_duplique"] += 1
                        continue
                    if not signature:
                        rejected["signature_vide"] += 1
                        continue
                    if any(signature == prior or jaccard(signature, prior) >= 0.94 for prior in signatures_by_keyword[keyword]):
                        rejected["quasi_variante_ou_titre_duplique"] += 1
                        continue
                    used_ids.add(product_id)
                    signatures_by_keyword[keyword].append(signature)
                    selected.append(row)
                    accepted = True
                if rows:
                    next_keywords.append(keyword)
                if len(selected) >= target:
                    break
            keywords = next_keywords
    return selected, rejected


def main() -> int:
    assign = load_module("kraken_assign_catalogue", ASSIGN_SOURCE)
    matcher = load_module("kraken_final_keyword_matcher", MATCH_SOURCE)
    volume_payload = json.loads(VOLUMES.read_text(encoding="utf-8"))
    concepts_payload = json.loads(CONCEPTS.read_text(encoding="utf-8"))
    concept_map = {(row["niche"], row["concept_key"]): row for row in concepts_payload["concepts"]}
    search_payload = json.loads(CONCEPT_SEARCH.read_text(encoding="utf-8"))
    anchor_payload = json.loads(ANCHOR_PRODUCTS.read_text(encoding="utf-8"))

    pools: dict[str, list[dict]] = defaultdict(list)
    mapping_missing = Counter()
    competitor_match_counts = Counter()
    for result in search_payload.get("results", []):
        key = (result.get("niche"), result.get("concept_key"))
        concept = concept_map.get(key)
        if not concept:
            continue
        seo = volume_mapping(concept, volume_payload, assign)
        if not seo:
            mapping_missing[concept["niche"]] += 1
            continue
        relevant = [
            item for item in result.get("items", [])
            if item.get("match", {}).get("semantic_ok") and item.get("price") not in (None, "")
        ]
        relevant.sort(key=lambda item: (
            item.get("match", {}).get("supplier_quality_ok", False),
            item["match"]["score"],
            orders_number(item.get("orders")),
        ), reverse=True)
        # Jusqu'a dix listings distincts peuvent etre consideres pour un meme
        # concept fonctionnel. La selection finale garde l'ID unique et rejette
        # les signatures identiques ou quasi identiques; ce ne sont donc pas
        # dix couleurs/tailles d'une meme fiche fournisseur.
        for index, item in enumerate(relevant[:10]):
            final_keyword_concept = {
                "niche": concept["niche"],
                "concept_fr_normalized": seo["product_keyword"],
                "keyword_fr_candidate": seo["product_keyword"],
                "competitor_product_title": seo["product_keyword"],
            }
            final_keyword_match = matcher.evaluate_match(final_keyword_concept, item)
            if not final_keyword_match.get("required_any_ok", True):
                continue
            if not final_keyword_match.get("semantic_ok"):
                continue
            keyword_evidence_status = "MOT_CLE_DIRECT_DANS_LISTING"
            item = {**item, "final_keyword_match": final_keyword_match}
            descriptor = short_supplier_descriptor(item.get("title"))
            title = f"{sentence_case(seo['product_keyword'])} — {descriptor}"
            pools[concept["niche"]].append({
                "niche": concept["niche"],
                "root_keyword": volume_payload["root_keywords"][concept["niche"]]["keyword"],
                "root_volume": volume_payload["root_keywords"][concept["niche"]]["volume"],
                "parent_collection": concept.get("competitor_collection") or seo["collection_keyword"],
                "competitor": concept.get("competitor"),
                "competitor_domain": concept.get("competitor_domain"),
                "competitor_product_title": concept.get("competitor_product_title"),
                "competitor_product_url": concept.get("competitor_product_url") or concept.get("source_url"),
                "competitor_evidence_status": concept.get("evidence_status"),
                "concept_fr_normalized": concept.get("concept_fr_normalized"),
                "concept_key": concept.get("concept_key"),
                "distinctness_basis": concept.get("distinctness_basis"),
                "candidate_origin": "EQUIVALENT_CONCURRENT_API",
                "selection_stage": index if item.get("match", {}).get("supplier_quality_ok") else 20 + index,
                "supplier_evidence_status": (
                    "LISTING_QUALIFIE_NOTE_COMMANDES"
                    if item.get("match", {}).get("supplier_quality_ok")
                    else "LISTING_SEMANTIQUE_A_VERIFIER"
                ),
                "keyword_evidence_status": keyword_evidence_status,
                "seo": {**seo, "product_title": title, "collection_title": sentence_case(seo["collection_keyword"])},
                "product_signature": product_signature(item.get("title"), seo["product_keyword"]),
                "risk_flag": risk_flag(concept["niche"], f"{concept.get('concept_fr_normalized')} {item.get('title')}"),
                "aliexpress": item,
            })
            competitor_match_counts[concept["niche"]] += 1

    for anchor in anchor_payload.get("products", []):
        seo = anchor_mapping(anchor, volume_payload, assign)
        item = anchor["aliexpress"]
        final_keyword_concept = {
            "niche": anchor["niche"],
            "concept_fr_normalized": seo["product_keyword"],
            "keyword_fr_candidate": seo["product_keyword"],
            "competitor_product_title": seo["product_keyword"],
        }
        final_keyword_match = matcher.evaluate_match(final_keyword_concept, item)
        if not (
            final_keyword_match.get("semantic_ok")
            and item.get("price") not in (None, "")
        ):
            continue
        item = {**item, "final_keyword_match": final_keyword_match}
        descriptor = short_supplier_descriptor(item.get("title"))
        title = f"{sentence_case(seo['product_keyword'])} — {descriptor}"
        pools[anchor["niche"]].append({
            "niche": anchor["niche"],
            "root_keyword": volume_payload["root_keywords"][anchor["niche"]]["keyword"],
            "root_volume": volume_payload["root_keywords"][anchor["niche"]]["volume"],
            "parent_collection": anchor.get("parent_collection") or seo["collection_keyword"],
            "competitor": None,
            "competitor_domain": None,
            "competitor_product_title": None,
            "competitor_product_url": None,
            "competitor_evidence_status": "MANQUANT_CONCURRENT_DIRECT",
            "concept_fr_normalized": anchor.get("keyword_fr"),
            "concept_key": f"api:{anchor.get('keyword_fr')}:{item.get('product_id')}",
            "distinctness_basis": "Listing AliExpress distinct dans une famille SEO mesuree; aucune correspondance PDP concurrente directe affirmee.",
            "candidate_origin": "DECOUVERTE_FAMILLE_SEO_API",
            "selection_stage": 10 if item.get("match", {}).get("supplier_quality_ok") else 30,
            "supplier_evidence_status": anchor.get(
                "supplier_evidence_status",
                "LISTING_QUALIFIE_NOTE_COMMANDES"
                if item.get("match", {}).get("supplier_quality_ok")
                else "LISTING_SEMANTIQUE_A_VERIFIER",
            ),
            "keyword_evidence_status": "MOT_CLE_DIRECT_DANS_LISTING",
            "seo": {**seo, "product_title": title, "collection_title": sentence_case(seo["collection_keyword"])},
            "product_signature": product_signature(item.get("title"), seo["product_keyword"]),
            "risk_flag": risk_flag(anchor["niche"], f"{anchor.get('keyword_fr')} {item.get('title')}"),
            "aliexpress": item,
        })

    selected_all = []
    rejected_counts = {}
    counts = {}
    for niche in sorted(volume_payload["root_keywords"]):
        selected, rejected = select_balanced(pools[niche], TARGETS_BY_NICHE[niche])
        for rank, row in enumerate(selected, start=1):
            row["catalogue_rank"] = rank
        selected_all.extend(selected)
        counts[niche] = len(selected)
        rejected_counts[niche] = dict(rejected)

    selected_all.sort(key=lambda row: (row["niche"], row["seo"]["collection_keyword"], row["catalogue_rank"]))
    collection_counter = Counter((row["niche"], row["seo"]["collection_keyword"]) for row in selected_all)
    origin_counter = Counter((row["niche"], row["candidate_origin"]) for row in selected_all)
    generated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    payload = {
        "run_id": RUN_DIR.name,
        "generated_at_utc": generated_at,
        "database": "fr",
        "source_mode": "read-only",
        "targets_by_niche": TARGETS_BY_NICHE,
        "counts_by_niche": counts,
        "gate_catalogue_by_niche": {niche: count >= TARGETS_BY_NICHE[niche] for niche, count in counts.items()},
        "clean_totals_by_niche": volume_payload["clean_totals_by_niche"],
        "root_keywords": volume_payload["root_keywords"],
        "collections": [
            {
                "niche": niche,
                "collection_title": sentence_case(keyword),
                "collection_keyword": keyword,
                "collection_volume": next(row["seo"]["collection_volume"] for row in selected_all if row["niche"] == niche and row["seo"]["collection_keyword"] == keyword),
                "collection_tier": next(row["seo"]["collection_tier"] for row in selected_all if row["niche"] == niche and row["seo"]["collection_keyword"] == keyword),
                "product_count": count,
            }
            for (niche, keyword), count in sorted(collection_counter.items())
        ],
        "origin_counts": [
            {"niche": niche, "origin": origin, "count": count}
            for (niche, origin), count in sorted(origin_counter.items())
        ],
        "products": selected_all,
    }
    report = {
        "run_id": RUN_DIR.name,
        "generated_at_utc": generated_at,
        "counts_by_niche": counts,
        "targets_by_niche": TARGETS_BY_NICHE,
        "gate_catalogue_by_niche": payload["gate_catalogue_by_niche"],
        "pool_counts_by_niche": {niche: len(rows) for niche, rows in sorted(pools.items())},
        "competitor_qualified_match_candidates_by_niche": dict(competitor_match_counts),
        "mapping_missing_concepts_by_niche": dict(mapping_missing),
        "selection_rejections_by_niche": rejected_counts,
        "unique_listing_ids": len({(row["niche"], row["aliexpress"]["product_id"]) for row in selected_all}),
        "unique_product_titles": len({(row["niche"], normalize(row["seo"]["product_title"])) for row in selected_all}),
        "all_product_volumes_positive": all(row["seo"]["product_volume"] > 0 for row in selected_all),
        "all_collection_volumes_positive": all(row["seo"]["collection_volume"] > 0 for row in selected_all),
        "limitations": [
            "Un resultat de recherche API prouve un listing, pas encore le SKU exact, le fret France, la conformite ou la marge.",
            "Les lignes DECOUVERTE_FAMILLE_SEO_API n'ont pas de correspondance PDP concurrente directe.",
            "Les titres SEO sont des propositions de travail; la verite matiere et les allégations doivent etre confirmees avant import.",
        ],
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "ok": all(payload["gate_catalogue_by_niche"].values()),
        "counts_by_niche": counts,
        "pool_counts_by_niche": report["pool_counts_by_niche"],
        "all_product_volumes_positive": report["all_product_volumes_positive"],
    }, ensure_ascii=False, indent=2))
    return 0 if all(payload["gate_catalogue_by_niche"].values()) else 2


if __name__ == "__main__":
    raise SystemExit(main())
