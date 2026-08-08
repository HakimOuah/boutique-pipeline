#!/usr/bin/env python3
"""Dédoublonne et classe les résultats AliExpress sans inventer leur pertinence."""

from __future__ import annotations

import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path


SOURCE = Path(__file__).with_name("aliexpress-search-results.json")
OUTPUT = Path(__file__).with_name("curated-products.json")

STOPWORDS = {
    "a",
    "au",
    "aux",
    "de",
    "des",
    "du",
    "en",
    "et",
    "la",
    "le",
    "les",
    "pour",
    "avec",
    "machine",
}

DOMAIN_TOKENS = {
    "Mercerie créative & arts du fil": {"couture", "coudre", "broderie", "tricot", "patchwork", "quilting", "tailleur", "tissu", "artisanat", "bricolage"},
    "Scrapbooking & journaling": {"scrapbooking", "scrapbook", "journal", "artisanat", "bricolage", "album", "carte", "papeterie", "tampon", "embossage", "decoupe", "creatif"},
    "Aquariophilie & aquascaping": {"aquarium", "aquatique", "poisson", "crevette", "aquascaping"},
    "Balade, transport & mobilité du chien": {"chien", "chiot", "canin", "animaux", "animal"},
    "Perles & création de bijoux": {"bijou", "bijoux", "perle", "bracelet", "collier", "joaillerie", "boucle", "breloque"},
}

GENERIC_BY_NICHE = {
    "Mercerie créative & arts du fil": {"couture", "coudre"},
    "Scrapbooking & journaling": {"scrapbooking", "scrapbook"},
    "Aquariophilie & aquascaping": {"aquarium"},
    "Balade, transport & mobilité du chien": {"chien"},
    "Perles & création de bijoux": {"bijou", "bijoux"},
}

IP_MARKERS = {
    "avengers",
    "barbie",
    "batman",
    "bob l eponge",
    "cinnamoroll",
    "demon slayer",
    "disney",
    "dragon ball",
    "frozen",
    "hello kitty",
    "harry potter",
    "kuromi",
    "marvel",
    "mickey",
    "minecraft",
    "minions",
    "my melody",
    "naruto",
    "one piece",
    "pat patrouille",
    "paw patrol",
    "pokemon",
    "reine des neiges",
    "sanrio",
    "snoopy",
    "sonic",
    "spider man",
    "spiderman",
    "star wars",
    "stitch",
    "super mario",
    "winnie",
}


def normalize(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", " ", ascii_value.lower()).strip()


def tokenize(value: str) -> set[str]:
    return {token for token in normalize(value).split() if len(token) >= 3 and token not in STOPWORDS}


def fuzzy_hit(token: str, title_tokens: set[str]) -> bool:
    stem = token[:5] if len(token) >= 5 else token
    return any(candidate.startswith(stem) or stem.startswith(candidate[:5]) for candidate in title_tokens)


def numeric_orders(value: str) -> int:
    digits = re.sub(r"[^0-9]", "", value or "")
    return int(digits) if digits else 0


def relevance(niche: str, keyword: str, title: str) -> tuple[str, int, list[str]]:
    title_tokens = tokenize(title)
    keyword_tokens = tokenize(keyword) - GENERIC_BY_NICHE[niche]
    type_hits = sorted(token for token in keyword_tokens if fuzzy_hit(token, title_tokens))
    domain_hits = sorted(token for token in DOMAIN_TOKENS[niche] if fuzzy_hit(token, title_tokens))
    score = 2 * len(type_hits) + len(domain_hits)
    if type_hits and domain_hits:
        level = "ÉLEVÉE"
    elif type_hits or len(domain_hits) >= 2:
        level = "MOYENNE"
    else:
        level = "FAIBLE"
    return level, score, type_hits + domain_hits


def risk_for(niche: str, collection: str) -> str:
    if niche == "Aquariophilie & aquascaping" and collection in {
        "Pompes à eau",
        "Pompes à air",
        "Chauffages",
        "Éclairages LED",
        "Kits CO2",
        "Distributeurs automatiques",
        "Skimmers de surface",
        "Osmolateurs",
    }:
        return "ÉLECTRIQUE/ÉTANCHÉITÉ — conformité UE, prise, tension et usage immergé à valider"
    if niche == "Balade, transport & mobilité du chien" and collection in {
        "Harnais",
        "Laisses",
        "Longes",
        "Laisses enrouleurs",
        "Muselières",
        "Ceintures de sécurité",
        "Rampes",
        "Gilets de sauvetage",
        "Paniers vélo",
    }:
        return "SÉCURITÉ/CHARGE — tailles, résistance et allégations à valider"
    if niche == "Perles & création de bijoux":
        return "MATIÈRES/PETITES PIÈCES — composition, nickel/plomb/cadmium et allégations pierre à valider"
    if niche == "Mercerie créative & arts du fil" and collection in {"Aiguilles à coudre", "Aiguilles machine", "Épingles", "Ciseaux", "Découd-vite"}:
        return "OBJET COUPANT/POINTU — avertissements et usage enfant à encadrer"
    if niche == "Scrapbooking & journaling" and collection in {"Colles", "Poudres d'embossage"}:
        return "CHIMIQUE/POUSSIÈRES — composition et avertissements à valider"
    return "STANDARD — matière, dimensions, photos et livraison France à valider"


def main() -> int:
    payload = json.loads(SOURCE.read_text(encoding="utf-8"))
    by_product: dict[tuple[str, str], dict] = {}
    for query_row in payload["results"]:
        for item in query_row.get("items", []):
            level, score, hits = relevance(query_row["niche"], query_row["keyword_fr"], item.get("title", ""))
            normalized_title = normalize(item.get("title", ""))
            ip_hits = sorted(marker for marker in IP_MARKERS if marker in normalized_title)
            candidate = {
                "niche": query_row["niche"],
                "parent_collection": query_row["parent_collection"],
                "collection": query_row["collection"],
                "keyword_fr": query_row["keyword_fr"],
                "query_en": query_row["query_en"],
                "checked_at_utc": query_row.get("checked_at_utc"),
                **item,
                "relevance": level,
                "relevance_score": score,
                "relevance_hits": hits,
                "ip_flag": ", ".join(ip_hits),
                "risk": risk_for(query_row["niche"], query_row["collection"]),
            }
            key = (candidate["niche"], str(candidate["product_id"]))
            previous = by_product.get(key)
            candidate_sort = (not bool(ip_hits), score, float(item.get("rating") or 0), numeric_orders(item.get("orders") or ""))
            if previous is None:
                by_product[key] = candidate
                by_product[key]["_sort"] = candidate_sort
            elif candidate_sort > tuple(previous["_sort"]):
                candidate["_sort"] = candidate_sort
                by_product[key] = candidate

    grouped = defaultdict(list)
    for candidate in by_product.values():
        candidate.pop("_sort", None)
        if candidate["ip_flag"]:
            candidate["decision"] = "EXCLURE_IP"
        elif candidate["relevance"] == "FAIBLE":
            candidate["decision"] = "À_VÉRIFIER_PERTINENCE"
        else:
            candidate["decision"] = "RETENIR_API_À_VÉRIFIER"
        grouped[candidate["niche"]].append(candidate)

    selected = []
    summary = {}
    level_rank = {"ÉLEVÉE": 2, "MOYENNE": 1, "FAIBLE": 0}
    for niche, candidates in grouped.items():
        candidates.sort(
            key=lambda row: (
                row["decision"] != "EXCLURE_IP",
                level_rank[row["relevance"]],
                row["relevance_score"],
                float(row.get("rating") or 0),
                numeric_orders(row.get("orders") or ""),
            ),
            reverse=True,
        )
        clean = [row for row in candidates if row["decision"] != "EXCLURE_IP"]
        niche_selected = clean[:130]
        selected.extend(niche_selected)
        summary[niche] = {
            "unique_api": len(candidates),
            "selected": len(niche_selected),
            "relevance": dict(Counter(row["relevance"] for row in niche_selected)),
            "decisions": dict(Counter(row["decision"] for row in niche_selected)),
            "ip_excluded": sum(row["decision"] == "EXCLURE_IP" for row in candidates),
        }

    OUTPUT.write_text(
        json.dumps(
            {
                "run_id": payload["run_id"],
                "source": payload["source"],
                "destination": payload["destination"],
                "summary": summary,
                "products": selected,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
