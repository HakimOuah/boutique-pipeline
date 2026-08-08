#!/usr/bin/env python3
"""Collecte AliExpress read-only pour la salve Kraken catalogue-volume.

Le script interroge le gateway officiel déjà présent dans le dépôt, conserve
au plus dix listings distincts par mot-clé produit et ne réalise aucune
mutation Shopify/DSers.
"""

from __future__ import annotations

import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
GATEWAY = ROOT / "codex-chasse-clusters" / "tools" / "aliexpress_vps_gateway.py"
OUT = Path(__file__).with_name("aliexpress-search-results.json")


QUERIES = {
    "Mercerie créative & arts du fil": [
        ("Couture à la main", "Aiguilles à coudre", "aiguilles à coudre", "sewing needles"),
        ("Machine à coudre", "Aiguilles machine", "aiguilles machine à coudre", "sewing machine needles"),
        ("Couture à la main", "Fils à coudre", "fil à coudre", "sewing thread"),
        ("Fermetures & finitions", "Boutons", "boutons couture", "sewing buttons"),
        ("Fermetures & finitions", "Boutons pression", "bouton pression", "snap buttons sewing"),
        ("Fermetures & finitions", "Pinces à pression", "pince pression", "snap pliers sewing"),
        ("Fermetures & finitions", "Fermetures éclair", "fermeture éclair", "zipper sewing"),
        ("Fermetures & finitions", "Rubans", "ruban couture", "sewing ribbon"),
        ("Fermetures & finitions", "Biais", "biais couture", "bias tape sewing"),
        ("Fermetures & finitions", "Passepoils", "passepoil couture", "piping cord sewing"),
        ("Fermetures & finitions", "Élastiques", "élastique couture", "elastic band sewing"),
        ("Fermetures & finitions", "Dentelles", "dentelle couture", "lace trim sewing"),
        ("Couture à la main", "Épingles", "épingles couture", "sewing pins"),
        ("Couture à la main", "Clips", "clips couture", "sewing clips"),
        ("Outils de coupe & mesure", "Ciseaux", "ciseaux couture", "sewing scissors"),
        ("Outils de coupe & mesure", "Découd-vite", "découd vite", "seam ripper sewing"),
        ("Outils de coupe & mesure", "Craies tailleur", "craie tailleur", "tailor chalk"),
        ("Machine à coudre", "Pieds presseurs", "pied presseur", "sewing machine presser foot"),
        ("Machine à coudre", "Canettes", "canette machine à coudre", "sewing machine bobbins"),
        ("Outils de coupe & mesure", "Mètres ruban", "mètre ruban couture", "measuring tape sewing"),
    ],
    "Scrapbooking & journaling": [
        ("Papiers & albums", "Papiers scrapbooking", "papier scrapbooking", "scrapbook paper"),
        ("Papiers & albums", "Albums", "album scrapbooking", "scrapbook album"),
        ("Tampons & encres", "Tampons", "tampon scrapbooking", "scrapbook stamps"),
        ("Tampons & encres", "Tampons transparents", "tampon transparent scrapbooking", "clear stamps scrapbooking"),
        ("Tampons & encres", "Encres", "encre scrapbooking", "scrapbook ink pad"),
        ("Décorations", "Stickers", "stickers scrapbooking", "scrapbook stickers"),
        ("Décorations", "Washi tape", "washi tape", "washi tape"),
        ("Découpe & outils", "Perforatrices", "perforatrice scrapbooking", "craft paper punch"),
        ("Découpe & outils", "Dies", "dies scrapbooking", "scrapbooking cutting dies"),
        ("Découpe & outils", "Matrices de découpe", "matrice découpe scrapbooking", "scrapbook metal cutting dies"),
        ("Décorations", "Pochoirs", "pochoir scrapbooking", "scrapbook stencils"),
        ("Décorations", "Embellissements", "embellissement scrapbooking", "scrapbook embellishments"),
        ("Décorations", "Fleurs en papier", "fleurs papier scrapbooking", "paper flowers scrapbooking"),
        ("Décorations", "Rubans", "ruban scrapbooking", "scrapbook ribbon"),
        ("Papiers & albums", "Colles", "colle scrapbooking", "scrapbook glue"),
        ("Découpe & outils", "Massicots", "massicot papier", "paper trimmer craft"),
        ("Découpe & outils", "Plioirs", "plioir papier", "bone folder paper"),
        ("Découpe & outils", "Tapis de découpe", "tapis découpe scrapbooking", "scrapbook cutting mat"),
        ("Kits & démarrage", "Kits scrapbooking", "kit scrapbooking", "scrapbook kit"),
        ("Embossage", "Poudres d'embossage", "poudre embossage", "embossing powder"),
    ],
    "Aquariophilie & aquascaping": [
        ("Filtration & circulation", "Filtres", "filtre aquarium", "aquarium filter"),
        ("Filtration & circulation", "Pompes à eau", "pompe aquarium", "aquarium water pump"),
        ("Filtration & circulation", "Pompes à air", "pompe à air aquarium", "aquarium air pump"),
        ("Éclairage & température", "Chauffages", "chauffage aquarium", "aquarium heater"),
        ("Éclairage & température", "Éclairages LED", "éclairage aquarium", "aquarium led light"),
        ("Éclairage & température", "Thermomètres", "thermomètre aquarium", "aquarium thermometer"),
        ("CO2 & paramètres", "Diffuseurs CO2", "diffuseur co2 aquarium", "aquarium co2 diffuser"),
        ("CO2 & paramètres", "Kits CO2", "kit co2 aquarium", "aquarium co2 kit"),
        ("CO2 & paramètres", "Tests d'eau", "test eau aquarium", "aquarium water test kit"),
        ("Entretien", "Aspirateurs de fond", "aspirateur aquarium", "aquarium gravel vacuum"),
        ("Entretien", "Nettoyeurs de vitre", "nettoyeur vitre aquarium", "aquarium glass cleaner"),
        ("Décor & aquascaping", "Décorations", "décoration aquarium", "aquarium decoration"),
        ("Décor & aquascaping", "Plantes artificielles", "plante artificielle aquarium", "aquarium artificial plants"),
        ("Entretien", "Épuisettes", "épuisette aquarium", "aquarium fish net"),
        ("Nourrissage & élevage", "Distributeurs automatiques", "distributeur nourriture poisson", "automatic fish feeder"),
        ("Nourrissage & élevage", "Pondoirs", "pondoir aquarium", "aquarium breeding box"),
        ("Filtration & circulation", "Filtres pour crevettes", "filtre crevette aquarium", "shrimp aquarium filter"),
        ("Filtration & circulation", "Tuyaux", "tuyau aquarium", "aquarium hose"),
        ("Filtration & circulation", "Skimmers de surface", "skimmer aquarium", "aquarium surface skimmer"),
        ("CO2 & paramètres", "Osmolateurs", "osmolateur aquarium", "aquarium auto top off"),
    ],
    "Balade, transport & mobilité du chien": [
        ("Harnais, laisses & colliers", "Harnais", "harnais chien", "dog harness"),
        ("Harnais, laisses & colliers", "Laisses", "laisse chien", "dog leash"),
        ("Harnais, laisses & colliers", "Colliers", "collier chien", "dog collar"),
        ("Harnais, laisses & colliers", "Longes", "longe chien", "long dog leash"),
        ("Harnais, laisses & colliers", "Laisses enrouleurs", "laisse enrouleur chien", "retractable dog leash"),
        ("Sécurité & identification", "Muselières", "muselière chien", "dog muzzle"),
        ("Sécurité & identification", "Médailles", "médaille chien", "dog id tag"),
        ("Promenade & voyage", "Gourdes", "gourde chien", "portable dog water bottle"),
        ("Promenade & voyage", "Gamelles pliables", "gamelle pliable chien", "collapsible dog bowl"),
        ("Transport & voiture", "Sacs de transport", "sac transport chien", "dog carrier bag"),
        ("Transport & voiture", "Housses de voiture", "housse voiture chien", "dog car seat cover"),
        ("Transport & voiture", "Ceintures de sécurité", "ceinture voiture chien", "dog seat belt"),
        ("Mobilité", "Rampes", "rampe chien", "dog ramp"),
        ("Sécurité & identification", "Gilets de sauvetage", "gilet sauvetage chien", "dog life jacket"),
        ("Météo & protection", "Manteaux", "manteau chien", "dog coat"),
        ("Météo & protection", "Imperméables", "imperméable chien", "dog raincoat"),
        ("Météo & protection", "Chaussures", "chaussures chien", "dog shoes"),
        ("Mobilité", "Poussettes", "poussette chien", "dog stroller"),
        ("Mobilité", "Paniers vélo", "panier vélo chien", "dog bike basket"),
        ("Promenade & voyage", "Pochettes à friandises", "pochette friandise chien", "dog treat pouch"),
    ],
    "Perles & création de bijoux": [
        ("Perles", "Perles assorties", "perles pour bijoux", "jewelry making beads"),
        ("Perles", "Rocailles", "perles rocailles", "seed beads jewelry making"),
        ("Perles", "Heishi", "perles heishi", "heishi beads"),
        ("Perles", "Miyuki", "perles miyuki", "miyuki beads"),
        ("Perles", "Lettres", "perles lettres", "letter beads"),
        ("Perles", "Pierres naturelles", "perles naturelles", "natural stone beads"),
        ("Perles", "Verre", "perles verre", "glass beads jewelry making"),
        ("Perles", "Bois", "perles bois", "wooden beads jewelry making"),
        ("Apprêts & fermoirs", "Apprêts", "apprêts bijoux", "jewelry findings"),
        ("Apprêts & fermoirs", "Fermoirs", "fermoir bijoux", "jewelry clasps"),
        ("Apprêts & fermoirs", "Chaînes", "chaine bijoux", "jewelry chain diy"),
        ("Outils & fils", "Pinces", "pince bijoux", "jewelry making pliers"),
        ("Apprêts & fermoirs", "Breloques", "breloque", "jewelry charms"),
        ("Apprêts & fermoirs", "Pendentifs", "pendentif", "jewelry pendants"),
        ("Outils & fils", "Fils élastiques", "fil élastique bracelet", "elastic cord bracelet"),
        ("Apprêts & fermoirs", "Supports de boucles", "support boucle d'oreille", "earring hooks findings"),
        ("Apprêts & fermoirs", "Anneaux", "anneau bijoux", "jewelry jump rings"),
        ("Apprêts & fermoirs", "Connecteurs", "connecteur bijoux", "jewelry connectors"),
        ("Outils & fils", "Aiguilles à perles", "aiguille perles", "beading needles"),
        ("Tissage de perles", "Métiers à tisser", "métier à tisser perles", "bead loom kit"),
    ],
}


def search_one(niche: str, parent: str, collection: str, keyword_fr: str, query_en: str) -> dict:
    command = [
        sys.executable,
        str(GATEWAY),
        "search",
        query_en,
        "--limit",
        "10",
        "--destination",
        "FR",
        "--sort-by",
        "orders",
    ]
    completed = subprocess.run(command, capture_output=True, text=True, timeout=90, check=False)
    base = {
        "niche": niche,
        "parent_collection": parent,
        "collection": collection,
        "keyword_fr": keyword_fr,
        "query_en": query_en,
        "returncode": completed.returncode,
    }
    if completed.returncode != 0:
        return {**base, "ok": False, "error": completed.stderr[-2000:]}
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as error:
        return {**base, "ok": False, "error": f"JSON invalide: {error}", "raw": completed.stdout[-2000:]}
    result = payload.get("result", {})
    items = []
    for item in result.get("items", [])[:10]:
        product_id = str(item.get("product_id", ""))
        if not product_id:
            continue
        items.append(
            {
                **item,
                "listing_url": f"https://www.aliexpress.com/item/{product_id}.html",
                "api_search_status": "API_SEARCH_MATCH",
            }
        )
    return {
        **base,
        "ok": bool(payload.get("ok")),
        "checked_at_utc": result.get("checked_at_utc"),
        "items": items,
    }


def main() -> int:
    tasks = [
        (niche, parent, collection, keyword_fr, query_en)
        for niche, entries in QUERIES.items()
        for parent, collection, keyword_fr, query_en in entries
    ]
    results = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(search_one, *task): task for task in tasks}
        for future in as_completed(futures):
            task = futures[future]
            try:
                results.append(future.result())
            except Exception as error:  # noqa: BLE001 - journaliser sans interrompre la collecte
                results.append(
                    {
                        "niche": task[0],
                        "parent_collection": task[1],
                        "collection": task[2],
                        "keyword_fr": task[3],
                        "query_en": task[4],
                        "ok": False,
                        "error": repr(error),
                    }
                )

    order = {task: index for index, task in enumerate(tasks)}
    results.sort(
        key=lambda row: order.get(
            (
                row["niche"],
                row["parent_collection"],
                row["collection"],
                row["keyword_fr"],
                row["query_en"],
            ),
            10_000,
        )
    )
    product_counts = {}
    for niche in QUERIES:
        seen = set()
        for row in results:
            if row["niche"] != niche:
                continue
            for item in row.get("items", []):
                seen.add(item["product_id"])
        product_counts[niche] = len(seen)

    output = {
        "run_id": "2026-08-08-kraken-catalogue-v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "AliExpress Open Platform / AE-Dropshipper via whitelisted VPS",
        "destination": "FR",
        "mode": "read-only",
        "query_count": len(tasks),
        "product_counts_unique": product_counts,
        "results": results,
    }
    OUT.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "output": str(OUT), "product_counts_unique": product_counts}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
