#!/usr/bin/env python3
"""Rattache les produits sources a des ancres SEO mesurees en France."""

from __future__ import annotations

import json
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
SOURCE = RUN_DIR / "catalogue-sourced.json"
VOLUME_SOURCE = RUN_DIR / "keyword-volumes-fr.json"
OUTPUT = RUN_DIR / "catalogue-architecture.json"
UNMAPPED = RUN_DIR / "catalogue-architecture-unmapped.json"

CONTEXT = {
    "Balade, transport & mobilité du chien": {"chien", "chiens", "chiot", "chiots", "canin"},
    "Aquariophilie & aquascaping": {"aquarium", "aquariophilie", "aquascaping", "aquatique"},
    "Mercerie créative & arts du fil": {"couture", "coudre", "mercerie"},
    "Scrapbooking & journaling": {"scrapbooking", "scrapbook", "journaling"},
    "Perles & création de bijoux": {"bijou", "bijoux", "perle", "perles"},
}

SYNONYMS = [
    {"aiguille", "aiguilles"}, {"anneau", "anneaux"}, {"bouton", "boutons"},
    {"canette", "canettes"}, {"ciseau", "ciseaux"}, {"collier", "colliers"},
    {"connecteur", "connecteurs"}, {"fermoir", "fermoirs"}, {"fil", "fils"},
    {"filtre", "filtres"}, {"harnais", "baudrier"}, {"laisse", "longe"},
    {"pince", "pinces"}, {"pompe", "pompes"}, {"ruban", "rubans"},
    {"chausson", "chaussons", "chaussure", "chaussures", "bottine", "bottines"},
    {"thermometre", "thermostat", "temperature"},
    {"eclairage", "lampe", "led"},
    {"chaine", "chaines"}, {"breloque", "breloques"}, {"pendentif", "pendentifs"},
]

COLLECTION_FALLBACKS = {
    "ruban couture": "biais couture",
    "dentelle couture": "biais couture",
    "épingles couture": "aiguilles à coudre",
    "clips couture": "aiguilles à coudre",
    "craie tailleur": "mètre ruban couture",
    "pied presseur": "canette machine à coudre",
    "tampon transparent scrapbooking": "tampon scrapbooking",
    "encre scrapbooking": "tampon scrapbooking",
    "dies scrapbooking": "perforatrice scrapbooking",
    "matrice découpe scrapbooking": "massicot papier",
    "pochoir scrapbooking": "perforatrice scrapbooking",
    "embellissement scrapbooking": "stickers scrapbooking",
    "ruban scrapbooking": "papier scrapbooking",
    "colle scrapbooking": "papier scrapbooking",
    "plioir papier": "massicot papier",
    "poudre embossage": "tampon scrapbooking",
    "nettoyeur vitre aquarium": "aspirateur aquarium",
    "plante artificielle aquarium": "décoration aquarium",
    "épuisette aquarium": "aspirateur aquarium",
    "pondoir aquarium": "décoration aquarium",
    "filtre crevette aquarium": "filtre aquarium",
    "skimmer aquarium": "filtre aquarium",
    "osmolateur aquarium": "pompe aquarium",
    "ceinture voiture chien": "housse voiture chien",
    "panier vélo chien": "sac transport chien",
    "pochette friandise chien": "gourde chien",
    "apprêts bijoux": "chaine bijoux",
    "fermoir bijoux": "chaine bijoux",
    "fil élastique bracelet": "perles pour bijoux",
    "anneau bijoux": "chaine bijoux",
    "connecteur bijoux": "chaine bijoux",
    "aiguille perles": "métier à tisser perles",
}


def normalize(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value or ""))
    text = "".join(char for char in text if not unicodedata.combining(char))
    text = text.lower().replace("&", " et ")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def stem(token: str) -> str:
    if len(token) > 5 and token.endswith("es"):
        return token[:-2]
    if len(token) > 4 and token.endswith("s"):
        return token[:-1]
    return token


def tokens(value: object) -> list[str]:
    stop = {"a", "au", "aux", "avec", "de", "des", "du", "en", "et", "la", "le", "les", "pour", "sans", "sur", "un", "une"}
    return [stem(token) for token in normalize(value).split() if len(token) >= 3 and token not in stop]


def token_match(left: str, right: str) -> bool:
    if stem(left) == stem(right):
        return True
    if len(left) >= 5 and len(right) >= 5 and left[:5] == right[:5]:
        return True
    return any(left in group and right in group for group in SYNONYMS)


def anchor_match(niche: str, text: str, keyword: str) -> tuple[bool, float, list[str]]:
    text_tokens = tokens(text)
    keyword_tokens = tokens(keyword)
    context = {stem(token) for token in CONTEXT[niche]}
    identity = [token for token in keyword_tokens if token not in context]
    if not identity:
        identity = keyword_tokens
    matched = [token for token in identity if any(token_match(token, candidate) for candidate in text_tokens)]
    exact = normalize(keyword) in normalize(text)
    ok = bool(identity) and len(matched) == len(identity)
    score = len(matched) * 50 + (35 if exact else 0) + len(identity) * 3
    return ok, score, matched


def sentence_case(value: str) -> str:
    return value[:1].upper() + value[1:] if value else value


def collection_tier(volume: int) -> str:
    if volume >= 1000:
        return "COEUR"
    if volume >= 500:
        return "SECONDAIRE"
    if volume >= 300:
        return "REVUE_300_499"
    return "PDP_SEULEMENT"


def main() -> int:
    sourced = json.loads(SOURCE.read_text(encoding="utf-8"))
    volume_payload = json.loads(VOLUME_SOURCE.read_text(encoding="utf-8"))
    volume_rows = volume_payload["keywords"]
    volume_map = {normalize(row["keyword"]): row for row in volume_rows}
    anchors_by_niche = {
        niche: [row for row in volume_rows if niche in row.get("niches", []) and row["volume"] > 0]
        for niche in CONTEXT
    }

    mapped = []
    unmapped = []
    for product in sourced.get("products", []):
        if product.get("source_status") != "API_MATCH_QUALIFIE":
            unmapped.append({"reason": "fournisseur_aliexpress_manquant", "product": product})
            continue
        candidate_key = normalize(product.get("keyword_fr_candidate"))
        exact_row = volume_map.get(candidate_key)
        if exact_row and product["niche"] in exact_row.get("niches", []) and exact_row["volume"] > 0:
            keyword_row = exact_row
            mapping_status = "MOT_CLE_EXACT_MESURE"
            mapping_score = 999
        else:
            haystack = " ".join(
                str(product.get(field) or "")
                for field in (
                    "concept_fr_normalized",
                    "keyword_fr_candidate",
                    "competitor_collection",
                    "competitor_product_title",
                    "aliexpress_query_fr",
                )
            )
            candidates = []
            for row in anchors_by_niche[product["niche"]]:
                ok, score, matched = anchor_match(product["niche"], haystack, row["keyword"])
                if ok:
                    candidates.append((score, row["volume"], row, matched))
            if not candidates:
                unmapped.append({"reason": "mot_cle_mesure_introuvable", "candidate": product.get("keyword_fr_candidate"), "product": product})
                continue
            candidates.sort(key=lambda item: (item[0], item[1]), reverse=True)
            mapping_score, _volume, keyword_row, _matched = candidates[0]
            mapping_status = "ANCRE_MESUREE_SEMANTIQUE"

        product_keyword = keyword_row["keyword"]
        product_volume = keyword_row["volume"]
        fallback = COLLECTION_FALLBACKS.get(product_keyword)
        if product_volume >= 300:
            collection_keyword = product_keyword
        elif fallback and normalize(fallback) in volume_map:
            collection_keyword = volume_map[normalize(fallback)]["keyword"]
        else:
            root = volume_payload["root_keywords"][product["niche"]]
            collection_keyword = root["keyword"]
        collection_row = volume_map.get(normalize(collection_keyword))
        if collection_row:
            collection_volume = collection_row["volume"]
        else:
            root = volume_payload["root_keywords"][product["niche"]]
            collection_volume = root["volume"]
        if collection_volume <= 0:
            unmapped.append({"reason": "collection_sans_volume", "product": product})
            continue

        concept = str(product["concept_fr_normalized"]).strip()
        keyword_title = sentence_case(product_keyword)
        product_title = keyword_title if normalize(keyword_title) == normalize(concept) else f"{keyword_title} — {concept}"
        mapped.append(
            {
                **product,
                "seo": {
                    "product_title": product_title,
                    "product_keyword": product_keyword,
                    "product_volume": product_volume,
                    "collection_title": sentence_case(collection_keyword),
                    "collection_keyword": collection_keyword,
                    "collection_volume": collection_volume,
                    "collection_tier": collection_tier(collection_volume),
                    "mapping_status": mapping_status,
                    "mapping_score": mapping_score,
                },
            }
        )

    mapped_counts = Counter(row["niche"] for row in mapped)
    collection_counts = Counter((row["niche"], row["seo"]["collection_keyword"]) for row in mapped)
    architecture = {
        "run_id": RUN_DIR.name,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "database": "fr",
        "clean_totals_by_niche": volume_payload["clean_totals_by_niche"],
        "counts_mapped_by_niche": dict(sorted(mapped_counts.items())),
        "gate_200_by_niche": {niche: mapped_counts[niche] >= 200 for niche in sorted(CONTEXT)},
        "collections": [
            {
                "niche": niche,
                "collection_keyword": keyword,
                "collection_title": sentence_case(keyword),
                "collection_volume": next(row["seo"]["collection_volume"] for row in mapped if row["niche"] == niche and row["seo"]["collection_keyword"] == keyword),
                "collection_tier": next(row["seo"]["collection_tier"] for row in mapped if row["niche"] == niche and row["seo"]["collection_keyword"] == keyword),
                "product_count": count,
            }
            for (niche, keyword), count in sorted(collection_counts.items())
        ],
        "products": mapped,
    }
    missing_groups: dict[str, Counter] = defaultdict(Counter)
    for row in unmapped:
        product = row["product"]
        missing_groups[product["niche"]][str(row.get("candidate") or product.get("keyword_fr_candidate") or "MANQUANT")] += 1
    report = {
        "run_id": RUN_DIR.name,
        "generated_at_utc": architecture["generated_at_utc"],
        "count": len(unmapped),
        "grouped_candidates": {
            niche: [{"candidate": candidate, "count": count} for candidate, count in counter.most_common()]
            for niche, counter in missing_groups.items()
        },
        "rows": unmapped,
    }
    OUTPUT.write_text(json.dumps(architecture, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    UNMAPPED.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "mapped_by_niche": dict(mapped_counts), "unmapped": len(unmapped)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
