#!/usr/bin/env python3
"""Collecte read-only de listings AliExpress pour les 100 ancres SEO mesurees.

Cette seconde voie de sourcing complete les equivalences produit-par-produit
issues des catalogues concurrents. Elle permet de couvrir les familles dont le
catalogue concurrent public ne fournit pas 200 concepts fonctionnels distincts.
Un ID de listing n'est compte qu'une fois par niche et les signatures qui ne
different que par couleur, taille, quantite ou formulation marketing sont
dedupliquees.
"""

from __future__ import annotations

import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
import unicodedata
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RUN_DIR = Path(__file__).resolve().parent
GATEWAY = ROOT / "codex-chasse-clusters/tools/aliexpress_vps_gateway.py"
QUERY_SOURCE = ROOT / "codex-chasse-clusters/runs/2026-08-08-kraken-catalogue-v1/collect_aliexpress.py"
MATCH_SOURCE = RUN_DIR / "source_aliexpress_catalogue.py"
RAW_OUT = RUN_DIR / "aliexpress-anchor-search.json"
CURATED_OUT = RUN_DIR / "aliexpress-anchor-candidates.json"

COLORS = {
    "argent", "argente", "beige", "blanc", "blanche", "bleu", "bleue",
    "brun", "brune", "dore", "doree", "gris", "grise", "jaune", "marron",
    "noir", "noire", "orange", "rose", "rouge", "transparent", "transparente",
    "vert", "verte", "violet", "violette", "multicolore",
}

SIGNATURE_NOISE = COLORS | {
    "achat", "accessoire", "accessoires", "adapte", "adaptee", "assorti",
    "assortie", "avec", "choix", "couleur", "couleurs", "ensemble", "haute",
    "haute", "qualite", "lot", "lots", "modele", "nouveau", "nouvelle",
    "pack", "piece", "pieces", "premium", "pour", "professionnel",
    "professionnelle", "set", "taille", "tailles", "universel", "universelle",
    "vente", "unite", "unites",
}

EXTRA_QUERIES = {
    "aspirateur aquarium": [
        "fish tank gravel vacuum siphon water changer",
        "aquarium substrate cleaner gravel washer pump",
        "fish tank electric gravel vacuum cleaner",
        "aquarium manual siphon water changer pump",
    ],
    "chauffage aquarium": [
        "submersible fish tank heater thermostat",
        "aquarium heating rod temperature controller",
    ],
    "diffuseur co2 aquarium": [
        "planted aquarium co2 glass diffuser atomizer",
        "fish tank co2 ceramic bubble diffuser",
    ],
    "distributeur nourriture poisson": [
        "automatic fish tank food feeder timer",
        "aquarium fish feeding dispenser programmable",
    ],
    "décoration aquarium": [
        "fish tank aquascape resin ornament cave",
        "aquarium decorative rock hiding tunnel",
        "aquarium resin cave ornament fish hideout",
        "aquarium driftwood tree root decoration",
        "aquarium artificial rock stone landscape ornament",
        "aquarium castle shipwreck bridge decoration",
        "fish tank background poster 3d decoration",
        "aquarium ceramic shelter cave shrimp hide",
        "aquarium moss holder mesh aquascaping",
        "fish tank coral reef resin ornament",
        "aquarium bonsai tree root ornament aquascape",
        "aquarium ceramic shrimp tunnel shelter decoration",
        "aquarium floating log fish hide decoration",
        "aquarium rocky background board decoration",
    ],
    "filtre aquarium": [
        "fish tank internal external sponge filter",
        "aquarium filtration pump bio media filter",
        "aquarium hang on back waterfall filter",
        "aquarium internal corner filter pump",
        "fish tank external canister filter",
        "aquarium undergravel filter plate",
        "aquarium filter media bag holder",
        "aquarium double sponge bio filter",
        "nano aquarium silent internal filter",
        "aquarium surface skimmer filter pump",
        "aquarium top filter box media chamber",
    ],
    "filtre crevette aquarium": [
        "shrimp tank sponge filter intake guard",
        "aquarium shrimp safe bio sponge filter",
    ],
    "kit co2 aquarium": [
        "planted fish tank co2 regulator complete system",
        "aquarium diy co2 generator kit valve gauge",
    ],
    "nettoyeur vitre aquarium": [
        "fish tank algae magnetic glass scraper cleaner",
        "aquarium glass cleaning blade algae tool",
    ],
    "osmolateur aquarium": [
        "aquarium auto top off water level controller pump",
        "fish tank automatic refill ato sensor system",
    ],
    "plante artificielle aquarium": [
        "fish tank plastic artificial aquatic plant decor",
        "aquarium fake silk water grass decoration",
        "aquarium silk plant seaweed ornament",
        "fish tank plastic grass plant landscape",
    ],
    "pompe aquarium": [
        "fish tank submersible circulation water pump",
        "aquarium return pump adjustable flow",
    ],
    "pompe à air aquarium": [
        "quiet fish tank oxygen air pump",
        "aquarium aerator pump usb battery",
    ],
    "pondoir aquarium": [
        "fish tank fry shrimp breeding isolation box",
        "aquarium fish hatchery breeder nursery net",
    ],
    "skimmer aquarium": [
        "fish tank surface protein skimmer inlet",
        "aquarium surface oil film remover skimmer",
    ],
    "test eau aquarium": [
        "fish tank water quality test strips kit",
        "aquarium ph nitrate ammonia testing kit",
    ],
    "thermomètre aquarium": [
        "fish tank digital thermometer probe",
        "aquarium water temperature lcd thermometer",
    ],
    "tuyau aquarium": [
        "fish tank silicone air water tubing hose",
        "aquarium filter clear flexible pipe tube",
    ],
    "éclairage aquarium": [
        "planted fish tank led clip lamp light",
        "aquarium full spectrum waterproof lighting",
        "nano aquarium clip led light",
        "aquarium plant full spectrum led bar",
        "fish tank submersible waterproof light",
        "aquarium hood lamp lighting",
    ],
    "épuisette aquarium": [
        "fish tank small shrimp fish catching net",
        "aquarium telescopic fine mesh net",
    ],
    "ceinture voiture chien": [
        "pet dog car safety seat belt tether",
        "adjustable puppy vehicle safety restraint",
    ],
    "chaussures chien": [
        "pet paw protector anti slip boots",
        "puppy waterproof outdoor booties shoes",
        "dog paw protection winter snow boots",
        "dog anti slip silicone rain shoes",
        "dog hiking protective booties set",
    ],
    "collier chien": [
        "pet puppy adjustable walking collar",
        "personalized dog identification collar",
        "reflective padded dog collar walking",
        "martingale dog training collar",
        "waterproof dog collar outdoor",
        "tactical dog collar handle buckle",
    ],
    "gamelle pliable chien": [
        "portable pet silicone folding food water bowl",
        "collapsible puppy travel feeding bowl",
    ],
    "gilet sauvetage chien": [
        "pet dog swimming flotation life vest",
        "puppy buoyancy safety jacket handle",
    ],
    "gourde chien": [
        "pet puppy portable water dispenser bottle",
        "dog travel drinking bottle bowl",
    ],
    "harnais chien": [
        "no pull pet dog walking harness",
        "reflective puppy chest harness outdoor",
        "tactical dog harness handle outdoor",
        "step in small dog walking harness",
        "dog hiking harness reflective vest",
        "dog car safety harness restraint",
    ],
    "housse voiture chien": [
        "pet dog back seat hammock protector cover",
        "waterproof puppy car rear seat cover",
    ],
    "imperméable chien": [
        "pet puppy waterproof rain jacket",
        "dog outdoor hooded rain suit",
    ],
    "laisse chien": [
        "pet puppy walking training leash",
        "dog rope lead outdoor walking",
        "hands free dog running leash waist",
        "double dog walking leash coupler",
        "bungee dog leash shock absorbing",
        "dog training slip lead leash",
    ],
    "laisse enrouleur chien": [
        "automatic retractable pet puppy leash reel",
        "dog leash retractable tape cord",
    ],
    "longe chien": [
        "pet dog long line training lead",
        "puppy tracking rope leash longline",
    ],
    "manteau chien": [
        "pet puppy winter warm coat jacket",
        "small dog clothes fleece jacket",
        "dog winter puffer coat warm clothes",
        "dog fleece vest coat outdoor clothing",
        "dog thermal jacket cold weather",
    ],
    "muselière chien": [
        "pet dog adjustable breathable basket muzzle",
        "puppy anti bite soft muzzle",
    ],
    "médaille chien": [
        "personalized pet dog name id tag",
        "engraved puppy collar identification tag",
    ],
    "panier vélo chien": [
        "pet dog bicycle front basket carrier",
        "puppy bike basket transport bag",
    ],
    "pochette friandise chien": [
        "pet dog training treat waist pouch",
        "puppy snack reward bag dispenser",
    ],
    "poussette chien": [
        "pet dog cat folding stroller pushchair",
        "puppy travel buggy stroller carrier",
    ],
    "rampe chien": [
        "pet dog car folding mobility ramp stairs",
        "puppy mobility steps bed vehicle",
        "folding dog ramp car boot mobility",
        "dog foam stairs bed sofa mobility",
        "portable dog steps senior pet mobility",
    ],
    "sac transport chien": [
        "pet dog travel carrier backpack bag",
        "puppy breathable transport shoulder bag",
        "airline approved dog soft carrier bag",
        "dog front carrier sling backpack",
        "dog travel trolley carrier bag",
        "dog car seat carrier travel bag",
    ],
    "album scrapbooking": [
        "blank spiral scrapbook photo album diy",
        "kraft scrapbook album black pages",
        "self adhesive scrapbook photo album book",
        "leather scrapbook memory album refillable",
    ],
    "kit scrapbooking": [
        "complete scrapbook supplies kit set",
        "vintage journaling scrapbook paper sticker bundle",
        "scrapbooking starter kit album paper tools",
        "themed scrapbook craft supplies box set",
    ],
    "papier scrapbooking": [
        "scrapbook patterned paper pad set",
        "scrapbooking cardstock paper pack",
        "vintage scrapbook background paper sheets",
        "double sided scrapbook paper collection",
    ],
    "stickers scrapbooking": [
        "scrapbook decorative sticker pack journaling",
        "vintage scrapbooking stickers paper set",
        "planner journal scrapbook sticker sheets",
    ],
    "tampon scrapbooking": [
        "clear silicone scrapbook stamp set",
        "scrapbooking rubber stamps alphabet set",
        "vintage journal clear stamp sheet",
    ],
    "dies scrapbooking": [
        "scrapbook metal cutting dies set",
        "cardmaking scrapbooking die cut stencil",
        "scrapbook frame alphabet cutting die",
    ],
    "massicot papier": [
        "craft paper trimmer guillotine cutter",
        "scrapbook rotary paper cutter board",
    ],
    "perforatrice scrapbooking": [
        "scrapbook craft paper punch shape",
        "decorative paper punch cardmaking",
    ],
    "washi tape": [
        "washi masking tape set journaling",
        "decorative washi tape roll bundle",
        "scrapbook washi paper tape pack",
    ],
    "colle scrapbooking": [
        "scrapbook glue adhesive tape runner",
        "paper craft scrapbooking glue pen set",
    ],
}


def normalize(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value or ""))
    text = "".join(char for char in text if not unicodedata.combining(char))
    text = text.lower().replace("&", " et ")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def atomic_write(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as stream:
            json.dump(payload, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Module introuvable: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def signature(title: object, keyword: str) -> str:
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
    # Une signature ordonnee mais bornee garde les differences de mecanisme,
    # matiere et usage sans etre dominee par une longue liste marketing.
    return " ".join(tokens[:16])


def search_one(task: tuple, limit: int, sort_modes: list[str], evaluator, first_query_only: bool = False) -> dict:
    niche, parent, collection, keyword_fr, query_en = task
    base = {
        "niche": niche,
        "parent_collection": parent,
        "collection": collection,
        "keyword_fr": keyword_fr,
        "query_en": query_en,
    }
    concept = {
        "niche": niche,
        "concept_fr_normalized": keyword_fr,
        "keyword_fr_candidate": keyword_fr,
        "competitor_product_title": keyword_fr,
    }
    # La recherche AliExpress peut etre tres differente selon la langue. Les
    # deux formulations sont donc interrogees et reunies, sans assouplir le
    # controle semantique ni le controle qualite.
    query_variants = list(dict.fromkeys([
        query_en,
        *EXTRA_QUERIES.get(keyword_fr, []),
        keyword_fr,
    ]))
    if first_query_only:
        query_variants = query_variants[:1]
    items_by_id = {}
    attempts = []
    checked_at_utc = None
    any_ok = False
    for matched_query in query_variants:
        for sort_mode in sort_modes:
            command = [
                sys.executable,
                str(GATEWAY),
                "search",
                matched_query,
                "--limit",
                str(limit),
                "--destination",
                "FR",
                "--sort-by",
                sort_mode,
            ]
            completed = subprocess.run(command, capture_output=True, text=True, timeout=90, check=False)
            attempt = {"query": matched_query, "sort_by": sort_mode, "returncode": completed.returncode}
            if completed.returncode != 0:
                attempt["error"] = completed.stderr[-2000:]
                attempts.append(attempt)
                continue
            try:
                payload = json.loads(completed.stdout)
            except json.JSONDecodeError as error:
                attempt["error"] = f"JSON invalide: {error}"
                attempts.append(attempt)
                continue
            result = payload.get("result", {})
            any_ok = any_ok or bool(payload.get("ok"))
            checked_at_utc = result.get("checked_at_utc") or checked_at_utc
            attempt["ok"] = bool(payload.get("ok"))
            attempt["item_count"] = len(result.get("items", []))
            attempts.append(attempt)
            for item in result.get("items", []):
                product_id = str(item.get("product_id") or "")
                if not product_id:
                    continue
                evaluation = evaluator(concept, item)
                candidate = {
                    **item,
                    "product_id": product_id,
                    "listing_url": f"https://www.aliexpress.com/item/{product_id}.html",
                    "matched_query": matched_query,
                    "matched_sort": sort_mode,
                    "match": evaluation,
                    "product_signature": signature(item.get("title"), keyword_fr),
                }
                prior = items_by_id.get(product_id)
                if not prior or candidate["match"]["score"] > prior["match"]["score"]:
                    items_by_id[product_id] = candidate
    items = list(items_by_id.values())
    return {
        **base,
        "ok": any_ok,
        "checked_at_utc": checked_at_utc,
        "attempts": attempts,
        "items": items,
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument(
        "--niche",
        action="append",
        default=[],
        help="Limite la collecte aux niches nommees; peut etre repete.",
    )
    parser.add_argument(
        "--keyword",
        action="append",
        default=[],
        help="Limite la collecte aux mots-cles FR nommes; peut etre repete.",
    )
    parser.add_argument("--resume", action="store_true")
    parser.add_argument(
        "--merge-existing",
        action="store_true",
        help="Fusionne les nouveaux tris avec le snapshot existant sans recompter les IDs.",
    )
    parser.add_argument(
        "--first-query-only",
        action="store_true",
        help="N'interroge que la formulation EN; les recherches existantes restent fusionnees.",
    )
    parser.add_argument(
        "--sort-by",
        action="append",
        choices=("orders", "latest", "price_asc", "price_desc"),
        default=[],
        help="Peut etre repete; par defaut: orders, latest, price_asc.",
    )
    args = parser.parse_args()

    queries = load_module("kraken_v1_queries", QUERY_SOURCE).QUERIES
    evaluator = load_module("kraken_source_matcher", MATCH_SOURCE).evaluate_match
    tasks = [
        (niche, parent, collection, keyword_fr, query_en)
        for niche, entries in queries.items()
        for parent, collection, keyword_fr, query_en in entries
        if not args.niche or niche in args.niche
        if not args.keyword or keyword_fr in args.keyword
    ]
    task_keys = {task[:1] + task[2:4] for task in tasks}

    prior_results = []
    if (args.resume or args.merge_existing) and RAW_OUT.is_file():
        prior = json.loads(RAW_OUT.read_text(encoding="utf-8"))
        prior_results = prior.get("results", [])
    existing = {}
    if args.resume:
        for row in prior_results:
            key = (row.get("niche"), row.get("collection"), row.get("keyword_fr"))
            if key in task_keys and row.get("ok"):
                existing[key] = row

    pending = [task for task in tasks if (task[0], task[2], task[3]) not in existing]
    results = list(existing.values())
    completed_count = 0
    sort_modes = args.sort_by or ["orders", "latest", "price_asc"]
    with ThreadPoolExecutor(max_workers=max(1, min(args.workers, 12))) as executor:
        futures = {
            executor.submit(search_one, task, args.limit, sort_modes, evaluator, args.first_query_only): task
            for task in pending
        }
        for future in as_completed(futures):
            task = futures[future]
            try:
                results.append(future.result())
            except Exception as error:  # noqa: BLE001
                results.append({
                    "niche": task[0],
                    "parent_collection": task[1],
                    "collection": task[2],
                    "keyword_fr": task[3],
                    "query_en": task[4],
                    "ok": False,
                    "error": repr(error),
                })
            completed_count += 1
            if completed_count % 20 == 0:
                print(f"progress={completed_count}/{len(pending)}", flush=True)
            if completed_count % 20 == 0 and not args.merge_existing:
                atomic_write(RAW_OUT, {
                    "run_id": RUN_DIR.name,
                    "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                    "source": "AliExpress Open Platform / AE-Dropshipper via whitelisted VPS",
                    "destination": "FR",
                    "mode": "read-only",
                    "results": results,
                })

    if args.merge_existing:
        prior_by_key = {
            (row.get("niche"), row.get("collection"), row.get("keyword_fr")): row
            for row in prior_results
        }
        merged_results = []
        refreshed_keys = set()
        for row in results:
            key = (row.get("niche"), row.get("collection"), row.get("keyword_fr"))
            refreshed_keys.add(key)
            old = prior_by_key.get(key)
            if not old:
                merged_results.append(row)
                continue
            items_by_id = {
                str(item.get("product_id")): item
                for item in old.get("items", [])
                if item.get("product_id")
            }
            for item in row.get("items", []):
                product_id = str(item.get("product_id") or "")
                prior_item = items_by_id.get(product_id)
                if not prior_item or item.get("match", {}).get("score", 0) > prior_item.get("match", {}).get("score", 0):
                    items_by_id[product_id] = item
            merged_results.append({
                **old,
                **row,
                "ok": bool(old.get("ok") or row.get("ok")),
                "attempts": old.get("attempts", []) + row.get("attempts", []),
                "items": list(items_by_id.values()),
            })
        # Une collecte ciblee ne doit jamais effacer les autres niches du
        # snapshot existant. Les lignes non rafraichies sont conservees telles
        # quelles et restent identifiables par leurs tentatives/date de preuve.
        merged_results.extend(
            row for key, row in prior_by_key.items()
            if key not in refreshed_keys
        )
        results = merged_results

    results.sort(key=lambda row: (row.get("niche", ""), row.get("keyword_fr", "")))
    observed_sort_modes = sorted({
        attempt.get("sort_by")
        for row in results
        for attempt in row.get("attempts", [])
        if attempt.get("sort_by")
    }) or sort_modes
    if args.merge_existing and prior_results and "orders" not in observed_sort_modes:
        observed_sort_modes = sorted([*observed_sort_modes, "orders"])
    raw_payload = {
        "run_id": RUN_DIR.name,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "AliExpress Open Platform / AE-Dropshipper via whitelisted VPS",
        "destination": "FR",
        "mode": "read-only",
        "sort_modes": observed_sort_modes,
        "query_count": len(results),
        "results": results,
    }
    atomic_write(RAW_OUT, raw_payload)

    candidates = []
    used_ids: dict[str, set[str]] = {niche: set() for niche in queries}
    used_signatures: dict[str, set[str]] = {niche: set() for niche in queries}
    for result in results:
        niche = result["niche"]
        ranked = sorted(
            result.get("items", []),
            key=lambda item: (
                item.get("match", {}).get("semantic_ok", False),
                item.get("match", {}).get("supplier_quality_ok", False),
                item.get("match", {}).get("score", 0),
            ),
            reverse=True,
        )
        for item in ranked:
            if not item.get("match", {}).get("semantic_ok") or item.get("price") in (None, ""):
                continue
            product_id = item["product_id"]
            product_signature = item.get("product_signature") or product_id
            if product_id in used_ids[niche] or product_signature in used_signatures[niche]:
                continue
            used_ids[niche].add(product_id)
            used_signatures[niche].add(product_signature)
            candidates.append({
                "niche": niche,
                "parent_collection": result["parent_collection"],
                "collection": result["collection"],
                "keyword_fr": result["keyword_fr"],
                "query_en": result["query_en"],
                "evidence_status": "ALIEXPRESS_DISCOVERY",
                "supplier_evidence_status": (
                    "LISTING_QUALIFIE_NOTE_COMMANDES"
                    if item.get("match", {}).get("supplier_quality_ok")
                    else "LISTING_SEMANTIQUE_A_VERIFIER"
                ),
                "api_checked_at_utc": result.get("checked_at_utc"),
                "aliexpress": item,
            })

    counts = Counter(row["niche"] for row in candidates)
    collection_counts = Counter((row["niche"], row["keyword_fr"]) for row in candidates)
    curated_payload = {
        "run_id": RUN_DIR.name,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "AliExpress Open Platform / AE-Dropshipper via whitelisted VPS",
        "destination": "FR",
        "mode": "read-only",
        "selection_rules": {
            "semantic_match": True,
            "price_present": True,
            "quality_tier_qualified": "note >= 4.5 et commandes > 0",
            "quality_tier_to_check": "pertinence et prix presents; note/commandes insuffisantes",
            "unique_listing_id_per_niche": True,
            "signature_dedup_without_color_size_quantity": True,
            "sort_modes": observed_sort_modes,
        },
        "counts_by_niche": dict(sorted(counts.items())),
        "qualified_counts_by_niche": dict(sorted(Counter(
            row["niche"] for row in candidates
            if row["supplier_evidence_status"] == "LISTING_QUALIFIE_NOTE_COMMANDES"
        ).items())),
        "gate_200_by_niche": {niche: counts[niche] >= 200 for niche in sorted(queries)},
        "counts_by_collection": [
            {"niche": niche, "keyword_fr": keyword, "count": count}
            for (niche, keyword), count in sorted(collection_counts.items())
        ],
        "products": candidates,
    }
    atomic_write(CURATED_OUT, curated_payload)
    print(json.dumps({
        "ok": True,
        "query_count": len(results),
        "counts_by_niche": dict(counts),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
