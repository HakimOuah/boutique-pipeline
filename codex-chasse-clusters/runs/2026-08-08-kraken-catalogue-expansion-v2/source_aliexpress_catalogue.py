#!/usr/bin/env python3
"""Source chaque concept catalogue via le gateway AliExpress officiel read-only.

Le script conserve la reponse de recherche, evalue la pertinence semantique du
listing et impose un ID fournisseur unique par niche. Il ne valide pas a lui
seul le SKU exact, le fret France, la conformite ni les economics.
"""

from __future__ import annotations

import argparse
import json
import math
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
SOURCE = RUN_DIR / "competitor-concepts-merged.json"
RAW_OUT = RUN_DIR / "aliexpress-concept-search.json"
SOURCED_OUT = RUN_DIR / "catalogue-sourced.json"

STOPWORDS = {
    "a", "avec", "aux", "d", "de", "des", "du", "en", "et", "la", "le",
    "les", "pour", "sans", "sur", "un", "une", "piece",
    "pieces", "accessoire", "accessoires", "produit", "produits", "modele",
    "creation", "creatif", "creative", "diy", "bricolage", "fourniture",
    "fournitures", "professionnel", "professionnelle", "premium", "universel",
    "universelle", "assorti", "assortie", "nouveau", "nouvelle",
    "vite",
}

CONTEXT_WORDS = {
    "Balade, transport & mobilité du chien": {
        "chien", "chiens", "chiot", "chiots", "canin", "animaux", "animal",
        "compagnie", "promenade", "balade", "transport", "mobilite",
    },
    "Aquariophilie & aquascaping": {
        "aquarium", "aquariophilie", "aquascaping", "aquatique", "poisson",
        "poissons", "crevette", "crevettes", "bassin", "eau",
    },
    "Mercerie créative & arts du fil": {
        "couture", "mercerie", "coudre", "textile", "tissu", "tissus", "fil",
        "fils", "broderie", "tricot", "crochet", "art", "artisanat",
    },
    "Scrapbooking & journaling": {
        "scrapbooking", "scrapbook", "journaling", "journal", "papier", "papiers",
        "carterie", "album", "albums", "artisanat",
    },
    "Perles & création de bijoux": {
        "perle", "perles", "bijou", "bijoux", "bracelet", "bracelets", "collier",
        "colliers", "pendentif", "pendentifs", "boucle", "oreille", "joaillerie",
    },
}

# Le contexte faible ci-dessus aide au scoring. Cette seconde grille est un
# verrou d'acceptation : un homonyme hors niche (chaussures humaines, pompe de
# piscine, pince d'electricien, etc.) ne peut plus etre retenu uniquement parce
# qu'un mot de type produit coincide.
HARD_CONTEXT_WORDS = {
    "Balade, transport & mobilité du chien": {
        "chien", "chiens", "chiot", "chiots", "canin", "dog", "dogs",
        "puppy", "puppies", "animal", "animaux",
    },
    "Aquariophilie & aquascaping": {
        "aquarium", "aquariums", "aquariophilie", "aquascaping", "aquascape",
        "aquatique", "aquatiques", "poisson", "poissons", "fish", "fishtank",
        "crevette", "crevettes", "shrimp",
    },
    "Mercerie créative & arts du fil": {
        "couture", "coudre", "sewing", "mercerie", "textile", "tissu",
        "tissus", "broderie", "embroidery", "tricot", "knitting",
        "patchwork", "quilting", "tailleur",
    },
    "Scrapbooking & journaling": {
        "scrapbooking", "scrapbook", "scrapbooks", "journaling", "journal",
        "journals", "carterie", "cardmaking", "planner", "planificateur",
    },
    "Perles & création de bijoux": {
        "perle", "perles", "bead", "beads", "bijou", "bijoux", "jewelry",
        "jewellery", "bracelet", "bracelets", "collier", "colliers",
        "necklace", "necklaces", "pendentif", "pendentifs", "breloque",
        "breloques",
    },
}

INHERENT_CONTEXT_FREE_KEYWORDS = {
    "washi tape",
    "poudre embossage",
    "plioir papier",
}

KEYWORD_REQUIRED_ANY = {
    "metre ruban couture": {
        "mesure", "mesurer", "mesurant", "metrique", "regle", "corps",
        "centimetre", "centimetres", "pouce", "pouces", "measure",
        "measuring", "metric", "ruler", "body", "inch", "inches",
    },
    "impermeable chien": {
        "manteau", "veste", "vetement", "vetements", "habit", "habits",
        "cape", "combinaison", "coat", "jacket", "clothes", "clothing",
        "raincoat", "poncho",
    },
    "medaille chien": {
        "nom", "identification", "identifiant", "personnalise", "personnalisee",
        "grave", "gravee", "name", "identity", "personalized", "custom",
        "engraved", "id",
    },
    "sac transport chien": {
        "transport", "voyage", "caisse", "cage", "carrier", "travel",
        "transportation",
    },
    "ceinture voiture chien": {
        "voiture", "automobile", "siege", "securite", "vehicle", "car",
        "seat", "seatbelt", "tether",
    },
    "fermeture eclair": {
        "curseur", "tete", "tirette", "extracteur", "reparation", "remplacement",
        "glissiere", "rouleau", "metre", "zipper", "slider", "puller", "repair",
        "replacement", "roll",
    },
    "perles bois": {"perle", "perles", "bead", "beads"},
    "perles lettres": {"perle", "perles", "bead", "beads"},
    "perles miyuki": {"perle", "perles", "bead", "beads"},
    "perles naturelles": {"perle", "perles", "bead", "beads"},
    "perles pour bijoux": {"perle", "perles", "bead", "beads"},
    "perles rocailles": {"perle", "perles", "bead", "beads"},
    "perles verre": {"perle", "perles", "bead", "beads"},
}

KEYWORD_FORBIDDEN_ANY = {
    "chaussures chien": {"breloque", "breloques", "charms", "bracelet", "bracelets", "croc", "baume", "creme", "hydratante"},
    "collier chien": {"paracorde", "parachute", "fabrication", "matiere", "material", "airtag", "etui", "housse", "localisateur", "gps", "etiquette", "etiquettes"},
    "harnais chien": {"autocollant", "autocollants", "etiquette", "etiquettes", "sticker", "stickers", "patch"},
    "gourde chien": {"parfum", "lotion", "maquillage", "atomiseur", "shampoing", "cosmetique"},
    "impermeable chien": {"cage", "niche", "toilette", "chenil", "kennel"},
    "manteau chien": {"harnais", "laisse", "harness", "leash"},
    "rampe chien": {"barriere", "cloture", "portail", "gate", "fence"},
    "decoration aquarium": {"vase", "pot", "taxidermie", "squelette", "filtre", "eponge", "aquarium intelligent", "aquarium autonettoyant"},
    "filtre aquarium": {"industriel", "industrielle", "transformation", "surimi", "pate"},
    "pompe aquarium": {"connecteur", "raccord", "tuyau", "valve", "vanne"},
    "fermeture eclair": {"pied de biche", "pied presseur", "presser foot", "escarpin", "chaussure", "chaussures", "machine d emballage", "sac de rangement", "boite de rangement"},
    "fil a coudre": {"enfile aiguille", "enfileur", "threader"},
    "aiguilles a coudre": {"enfile aiguille", "enfileur", "threader"},
    "aiguilles machine a coudre": {"enfile aiguille", "enfileur", "threader"},
    "dentelle couture": {"robe", "robes", "mariee", "mariage", "nappe", "tablecloth"},
    "album scrapbooking": {"autocollant", "autocollants", "sticker", "stickers", "coin", "coins", "angle", "angles", "pochoir", "pochoirs", "protecteur", "protecteurs", "tampon", "tampons", "matrice", "matrices", "timbre", "timbres"},
    "papier scrapbooking": {"coupe papier", "coupe-papier", "machine de decoupe", "outil de gaufrage", "perforatrice", "massicot"},
}

IP_TERMS = {
    "barbie", "death note", "disney", "dragon ball", "harry potter", "hello kitty", "lego",
    "marvel", "minecraft", "naruto", "one piece", "pokemon", "sanrio", "star wars",
    "stitch", "super mario", "winnie", "mickey", "minnie",
}

SYNONYM_GROUPS = [
    {"chien", "chiens", "chiot", "chiots", "canin", "dog", "puppy"},
    {"aquarium", "aquatique", "fish", "poisson", "poissons"},
    {"perle", "perles", "bead", "beads"},
    {"bijou", "bijoux", "jewelry", "jewellery"},
    {"couture", "coudre", "sewing"},
    {"papier", "papiers", "paper"},
    {"harnais", "harness"},
    {"laisse", "leash", "lead"},
    {"collier", "collar"},
    {"fermoir", "fermoirs", "clasp", "clasps"},
    {"aiguille", "aiguilles", "needle", "needles"},
    {"tampon", "tampons", "stamp", "stamps"},
    {"ruban", "rubans", "ribbon", "ribbons"},
    {"bouton", "boutons", "button", "buttons"},
    {"pompe", "pompes", "pump", "pumps"},
    {"filtre", "filtres", "filter", "filters"},
    {"bottine", "bottines", "botte", "bottes", "chausson", "chaussons", "chaussure", "chaussures", "chaussette", "chaussettes", "shoe", "shoes", "boot", "boots", "sock", "socks"},
    {"gourde", "bouteille", "flacon", "bottle"},
    {"gamelle", "bol", "mangeoire", "bowl"},
    {"pliable", "pliante", "pliant", "repliable", "folding", "foldable", "collapsible"},
    {"medaille", "etiquette", "plaque", "tag"},
    {"pochette", "poche", "sac", "pouch", "bag"},
    {"friandise", "friandises", "recompense", "recompenses", "treat", "treats", "snack", "snacks"},
    {"impermeable", "pluie", "raincoat", "waterproof", "pluviale"},
    {"manteau", "veste", "coat", "jacket"},
    {"gilet", "veste", "vest"},
    {"sauvetage", "flottaison", "flottabilite", "flottant", "flottante", "bouee", "natation", "swimming", "float", "floating", "floatation", "flotation", "life"},
    {"rampe", "escalier", "marches", "ramp", "steps"},
    {"housse", "protection", "couverture", "hamac", "cover", "hammock", "protector"},
    {"voiture", "auto", "siege", "car", "vehicle", "seat", "backseat"},
    {"sac", "caisse", "cage", "carrier", "bag", "backpack"},
    {"transport", "voyage", "travel", "carrier"},
    {"panier", "corbeille", "basket", "carrier"},
    {"velo", "bicyclette", "cycle", "bike", "bicycle"},
    {"poussette", "chariot", "stroller", "pram", "buggy"},
    {"ceinture", "sangle", "belt", "tether"},
    {"longe", "longline"},
    {"enrouleur", "retractable", "retractile", "automatique", "automatic", "reel"},
    {"museliere", "muzzle"},
    {"thermometre", "temperature", "thermometer"},
    {"aspirateur", "siphon", "vacuum", "cleaner"},
    {"chauffage", "chauffe", "heater", "heating"},
    {"eclairage", "lampe", "light", "lighting"},
    {"nettoyeur", "grattoir", "raclette", "aimant", "cleaner", "scraper"},
    {"epuisette", "filet", "net"},
    {"pondoir", "elevage", "breeding"},
    {"osmolateur", "remplissage", "remplisseur", "appoint", "niveau", "recharge", "ato", "refill", "topoff", "level"},
    {"diffuseur", "atomiseur", "diffuser", "atomizer"},
    {"distributeur", "mangeoire", "feeder", "dispenser"},
    {"nourriture", "alimentation", "food", "feed"},
    {"decoration", "decor", "ornement", "ornemental", "ornament"},
    {"plante", "plantes", "herbe", "herbes", "vegetation", "feuillage", "plant", "plants", "grass", "weed", "foliage"},
    {"artificielle", "artificiel", "factice", "simule", "simulee", "emulation", "fake", "artificial", "simulation"},
    {"vitre", "vitres", "verre", "fenetre", "glass", "window"},
    {"air", "oxygene", "aeration", "bulle", "bulles", "oxygen", "aerator", "bubble", "bubbles"},
    {"tuyau", "tube", "hose", "pipe"},
    {"skimmer", "ecumeur"},
    {"bandelette", "bandelettes", "test", "tester"},
    {"substrat", "sol", "soil"},
    {"dies", "die", "matrice", "matrices"},
    {"massicot", "coupe", "trimmer"},
    {"plioir", "folder"},
    {"washi", "masking"},
    {"tape", "ruban", "band"},
    {"embossage", "embosser", "gaufrage", "embossing"},
    {"stickers", "sticker", "autocollant", "autocollants"},
    {"encre", "encrage", "ink"},
    {"decoud", "decouseur", "ripper"},
    {"presseur", "biche", "presser"},
    {"canette", "bobine", "bobbin"},
    {"metre", "mesure", "mesurer", "measure", "measuring"},
    {"pince", "pinces", "pliers"},
    {"pression", "snap", "press"},
    {"biais", "oblique", "bias"},
    {"passepoil", "cordon", "piping"},
    {"apprets", "appret", "findings"},
    {"rocailles", "rocaille", "miyuki", "seed"},
    {"heishi", "disque", "rondelle"},
    {"naturelle", "naturel", "pierre", "gemme", "gemstone"},
    {"verre", "cristal", "glass", "crystal"},
    {"metier", "tissage", "loom"},
    {"crochet", "support", "hook"},
    {"anneau", "anneaux", "ring", "rings"},
    {"connecteur", "entretoise", "connector"},
    {"fermoir", "mousqueton", "clasp"},
    {"colle", "adhesif", "adhesive", "glue"},
    {"encre", "encrage", "ink", "pad"},
    {"fleur", "fleurs", "flower", "flowers"},
    {"papier", "paper", "cardstock"},
    {"massicot", "coupe", "trimmer", "cutter"},
    {"perforatrice", "perforateur", "punch"},
    {"plioir", "rainure", "folder", "creasing"},
    {"poudre", "powder"},
    {"tapis", "mat", "pad"},
    {"transparent", "clear"},
    {"embellissement", "ornement", "embellishment", "charm"},
    {"kit", "ensemble", "lot", "set", "bundle"},
]


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


def tokens(value: object) -> list[str]:
    return [
        token for token in normalize(value).split()
        if len(token) >= 3 and token not in STOPWORDS and not token.isdigit()
    ]


def token_matches(left: str, right: str) -> bool:
    if left == right:
        return True
    for group in SYNONYM_GROUPS:
        if left in group and right in group:
            return True
    return False


def count_orders(value: object) -> int:
    match = re.search(r"([\d.,]+)", str(value or ""))
    if not match:
        return 0
    number = match.group(1).replace(".", "").replace(",", "")
    try:
        return int(number)
    except ValueError:
        return 0


def as_float(value: object) -> float | None:
    try:
        return float(str(value).replace(",", "."))
    except (TypeError, ValueError):
        return None


def evaluate_match(concept: dict, item: dict) -> dict:
    title = normalize(item.get("title"))
    title_tokens = tokens(title)
    context_title = re.sub(r"\bsans couture\b", " ", title)
    context_title_tokens = tokens(context_title)
    concept_tokens = tokens(concept.get("concept_fr_normalized"))
    keyword_tokens = tokens(concept.get("keyword_fr_candidate"))
    competitor_tokens = tokens(concept.get("competitor_product_title"))
    context = CONTEXT_WORDS[concept["niche"]]
    identity = []
    for token in keyword_tokens + concept_tokens:
        if token not in context and token not in identity:
            identity.append(token)
    if not identity:
        identity = list(dict.fromkeys(keyword_tokens + concept_tokens))
    identity_matches = [
        token for token in identity
        if any(token_matches(token, title_token) for title_token in title_tokens)
    ]
    keyword_matches = [
        token for token in keyword_tokens
        if any(token_matches(token, title_token) for title_token in title_tokens)
    ]
    competitor_matches = [
        token for token in competitor_tokens
        if any(token_matches(token, title_token) for title_token in title_tokens)
    ]
    context_matches = [
        token for token in context
        if any(token_matches(token, title_token) for title_token in title_tokens)
    ]
    identity_required = max(1, math.ceil(min(len(identity), 5) * 0.67))
    ip_hits = sorted(term for term in IP_TERMS if term in title)
    rating = as_float(item.get("rating"))
    evaluation_rate = as_float(item.get("evaluation_rate"))
    orders = count_orders(item.get("orders"))
    exact_keyword = normalize(concept.get("keyword_fr_candidate")) in title
    exact_concept = normalize(concept.get("concept_fr_normalized")) in title
    hard_context_matches = [
        token for token in HARD_CONTEXT_WORDS[concept["niche"]]
        if any(token_matches(token, title_token) for title_token in context_title_tokens)
    ]
    coverage = len(identity_matches) / max(1, len(identity))
    score = (
        len(identity_matches) * 34
        + len(keyword_matches) * 12
        + len(competitor_matches) * 3
        + min(len(context_matches), 2) * 8
        + coverage * 45
        + (30 if exact_keyword else 0)
        + (45 if exact_concept else 0)
        + (min(math.log10(orders + 1), 4) * 2)
        + (max(0.0, (rating or 0) - 4.0) * 6)
    )
    inherent_context_free = normalize(concept.get("keyword_fr_candidate")) in INHERENT_CONTEXT_FREE_KEYWORDS
    keyword_key = normalize(concept.get("keyword_fr_candidate"))
    required_any = KEYWORD_REQUIRED_ANY.get(keyword_key, set())
    required_any_ok = not required_any or any(token in title_tokens for token in required_any)
    if keyword_key == "album scrapbooking":
        required_any_ok = (
            title.startswith("album ")
            or " album photo" in f" {title}"
            or "scrapbook album" in title
            or "livre de souvenirs" in title
            or any(token in title_tokens for token in {"classeur", "binder", "book", "pages"})
        )
    forbidden_hits = sorted(
        term for term in KEYWORD_FORBIDDEN_ANY.get(keyword_key, set())
        if normalize(term) in title
    )
    strict_context_ok = bool(hard_context_matches) or exact_keyword or inherent_context_free
    if concept["niche"] == "Aquariophilie & aquascaping" and (
        "aquarium" in keyword_key or keyword_key == "distributeur nourriture poisson"
    ):
        strict_context_ok = (
            "aquarium" in title_tokens
            or "aquariums" in title_tokens
            or "fishtank" in title_tokens
            or "aquascape" in title_tokens
            or "aquascaping" in title_tokens
            or ("fish" in title_tokens and "tank" in title_tokens)
            or "reservoir de poisson" in title
            or "reservoir de poissons" in title
        )
    if concept["niche"] == "Balade, transport & mobilité du chien" and "chien" in keyword_key:
        dog_context = {
            "chien", "chiens", "chiot", "chiots", "canin", "dog", "dogs",
            "puppy", "puppies", "animal", "animaux",
        }
        strict_context_ok = any(token in title_tokens for token in dog_context)
        if not strict_context_ok and ("pet" in title_tokens or "pets" in title_tokens):
            strict_context_ok = not ({"plastique", "plastic", "bouteille", "flacon"} & set(title_tokens))
        if "hot dog" in title or "production line" in title or "ligne de production" in title:
            strict_context_ok = False
    semantic_ok = (
        len(identity_matches) >= identity_required
        and strict_context_ok
        and required_any_ok
        and not forbidden_hits
    )
    supplier_quality_ok = (
        rating is not None and rating >= 4.5
        and orders > 0
        and item.get("price") not in (None, "")
    )
    return {
        "score": round(score, 3),
        "semantic_ok": semantic_ok and not ip_hits,
        "supplier_quality_ok": supplier_quality_ok,
        "identity_tokens": identity,
        "identity_matches": identity_matches,
        "identity_required": identity_required,
        "keyword_matches": keyword_matches,
        "context_matches": context_matches,
        "hard_context_matches": hard_context_matches,
        "inherent_context_free": inherent_context_free,
        "required_any_ok": required_any_ok,
        "forbidden_hits": forbidden_hits,
        "strict_context_ok": strict_context_ok,
        "ip_hits": ip_hits,
        "rating": rating,
        "evaluation_rate": evaluation_rate,
        "orders_numeric": orders,
    }


def call_search(concept: dict, limit: int, first_query_only: bool = False) -> dict:
    queries = []
    for candidate in (
        concept.get("aliexpress_query_en"),
        concept.get("aliexpress_query_fr"),
        concept.get("keyword_fr_candidate"),
    ):
        if candidate and normalize(candidate) not in {normalize(value) for value in queries}:
            queries.append(str(candidate))
    if first_query_only:
        queries = queries[:1]
    base = {
        "niche": concept["niche"],
        "concept_key": concept["concept_key"],
        "query": queries[0] if queries else "",
    }
    items_by_id: dict[str, dict] = {}
    attempts = []
    checked_at_utc = None
    any_ok = False
    for query_index, query in enumerate(queries):
        command = [
            sys.executable,
            str(GATEWAY),
            "search",
            query,
            "--limit",
            str(limit),
            "--destination",
            "FR",
            "--sort-by",
            "orders",
        ]
        completed = subprocess.run(command, capture_output=True, text=True, timeout=90, check=False)
        attempt = {"query": query, "returncode": completed.returncode}
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
            match = evaluate_match(concept, item)
            candidate = {
                **item,
                "product_id": product_id,
                "listing_url": f"https://www.aliexpress.com/item/{product_id}.html",
                "matched_query": query,
                "query_priority": query_index,
                "match": match,
            }
            prior = items_by_id.get(product_id)
            if not prior or candidate["match"]["score"] > prior["match"]["score"]:
                items_by_id[product_id] = candidate
        if any(
            item["match"]["semantic_ok"] and item["match"]["supplier_quality_ok"]
            for item in items_by_id.values()
        ):
            break
    items = list(items_by_id.values())
    items.sort(key=lambda row: (row["match"]["semantic_ok"], row["match"]["supplier_quality_ok"], row["match"]["score"]), reverse=True)
    return {
        **base,
        "ok": any_ok,
        "checked_at_utc": checked_at_utc,
        "attempts": attempts,
        "items": items,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--niche", action="append", default=[])
    parser.add_argument("--resume", action="store_true")
    parser.add_argument(
        "--first-query-only",
        action="store_true",
        help="N'interroge que la requete EN precise; utile apres correction manuelle du corpus.",
    )
    args = parser.parse_args()

    payload = json.loads(SOURCE.read_text(encoding="utf-8"))
    all_concepts = payload.get("concepts", [])
    concepts = list(all_concepts)
    if args.niche:
        wanted = {normalize(value) for value in args.niche}
        concepts = [row for row in concepts if normalize(row["niche"]) in wanted]

    existing: dict[tuple[str, str], dict] = {}
    prior_results: list[dict] = []
    if args.resume and RAW_OUT.is_file():
        prior = json.loads(RAW_OUT.read_text(encoding="utf-8"))
        prior_results = prior.get("results", [])
        expected_queries = {
            (row["niche"], row["concept_key"]): normalize(row.get("aliexpress_query_en"))
            for row in concepts
        }
        existing = {
            (row["niche"], row["concept_key"]): row
            for row in prior_results
            if row.get("ok")
            and normalize(row.get("query")) == expected_queries.get((row.get("niche"), row.get("concept_key")))
            and any(
                item.get("match", {}).get("semantic_ok")
                and item.get("match", {}).get("supplier_quality_ok")
                for item in row.get("items", [])
            )
        }

    pending = [row for row in concepts if (row["niche"], row["concept_key"]) not in existing]
    results = list(existing.values())
    completed_count = 0
    with ThreadPoolExecutor(max_workers=max(1, min(args.workers, 12))) as executor:
        futures = {
            executor.submit(call_search, concept, args.limit, args.first_query_only): concept
            for concept in pending
        }
        for future in as_completed(futures):
            concept = futures[future]
            try:
                results.append(future.result())
            except Exception as error:  # noqa: BLE001
                results.append({
                    "niche": concept["niche"],
                    "concept_key": concept["concept_key"],
                    "query": concept.get("aliexpress_query_en"),
                    "ok": False,
                    "error": repr(error),
                })
            completed_count += 1
            if completed_count % 20 == 0:
                print(f"progress={completed_count}/{len(pending)}", flush=True)
                atomic_write(
                    RAW_OUT,
                    {
                        "run_id": RUN_DIR.name,
                        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                        "source": "AliExpress Open Platform / AE-Dropshipper via whitelisted VPS",
                        "destination": "FR",
                        "mode": "read-only",
                        "results": sorted(results, key=lambda row: (row["niche"], row["concept_key"])),
                    },
                )

    if args.niche and prior_results:
        refreshed = {(row.get("niche"), row.get("concept_key")) for row in results}
        results.extend(
            row for row in prior_results
            if (row.get("niche"), row.get("concept_key")) not in refreshed
        )
    results.sort(key=lambda row: (row["niche"], row["concept_key"]))
    raw_payload = {
        "run_id": RUN_DIR.name,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "AliExpress Open Platform / AE-Dropshipper via whitelisted VPS",
        "destination": "FR",
        "mode": "read-only",
        "query_count": len(results),
        "results": results,
    }
    atomic_write(RAW_OUT, raw_payload)

    result_map = {(row["niche"], row["concept_key"]): row for row in results}
    used_ids: dict[str, set[str]] = {niche: set() for niche in CONTEXT_WORDS}
    concept_candidates = {}
    for concept in all_concepts:
        result = result_map.get((concept["niche"], concept["concept_key"]), {})
        concept_candidates[(concept["niche"], concept["concept_key"])] = [
            item for item in result.get("items", [])
            if item["match"]["semantic_ok"] and item["match"]["supplier_quality_ok"]
        ]

    selected_by_concept = {}
    # Les concepts avec peu d'alternatives passent d'abord afin d'eviter qu'un
    # terme large ne monopolise leur seul listing pertinent.
    allocation_order = sorted(
        all_concepts,
        key=lambda row: (
            row["niche"],
            len(concept_candidates[(row["niche"], row["concept_key"])]),
            -(
                concept_candidates[(row["niche"], row["concept_key"])][0]["match"]["score"]
                if concept_candidates[(row["niche"], row["concept_key"])] else 0
            ),
            row["concept_key"],
        ),
    )
    for concept in allocation_order:
        key = (concept["niche"], concept["concept_key"])
        available = [
            item for item in concept_candidates[key]
            if item["product_id"] not in used_ids[concept["niche"]]
        ]
        selected = available[0] if available else None
        selected_by_concept[key] = selected
        if selected:
            used_ids[concept["niche"]].add(selected["product_id"])

    sourced = []
    for concept in sorted(all_concepts, key=lambda row: (row["niche"], row["concept_key"])):
        key = (concept["niche"], concept["concept_key"])
        result = result_map.get(key, {})
        selected = selected_by_concept[key]
        sourced.append(
            {
                **concept,
                "source_status": "API_MATCH_QUALIFIE" if selected else "MANQUANT_MATCH_QUALIFIE",
                "aliexpress": selected,
                "qualified_candidate_count": len(concept_candidates[key]),
                "search_ok": bool(result.get("ok")),
                "search_checked_at_utc": result.get("checked_at_utc"),
            }
        )

    counts_total = Counter(row["niche"] for row in sourced)
    counts_sourced = Counter(row["niche"] for row in sourced if row["source_status"] == "API_MATCH_QUALIFIE")
    sourced_payload = {
        "run_id": RUN_DIR.name,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "AliExpress Open Platform / AE-Dropshipper via whitelisted VPS",
        "destination": "FR",
        "mode": "read-only",
        "counts_total_by_niche": dict(sorted(counts_total.items())),
        "counts_sourced_by_niche": dict(sorted(counts_sourced.items())),
        "gate_200_sourced_by_niche": {niche: counts_sourced[niche] >= 200 for niche in sorted(counts_total)},
        "products": sourced,
    }
    atomic_write(SOURCED_OUT, sourced_payload)
    print(json.dumps({
        "ok": True,
        "queries": len(results),
        "counts_total_by_niche": dict(counts_total),
        "counts_sourced_by_niche": dict(counts_sourced),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
