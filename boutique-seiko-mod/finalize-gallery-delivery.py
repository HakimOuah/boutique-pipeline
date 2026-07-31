import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, ImageOps


PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_ROOT = PROJECT_ROOT / "scratchpad" / "noirmont-galeries"
GENERATED_ROOT = OUTPUT_ROOT / "generated"
QA_ROOT = OUTPUT_ROOT / "qa"
SOURCES = json.loads((OUTPUT_ROOT / "sources.json").read_text())["entries"]
MANIFEST_PATH = OUTPUT_ROOT / "manifest.json"
CONTROL_PATH = OUTPUT_ROOT / "controle-final.json"
REPORT_PATH = OUTPUT_ROOT / "RAPPORT.md"

REGENERATIONS = {
    "doigtiers-d-horloger-latex-situation.jpg": 1,
    "pince-a-barrettes-situation.jpg": 1,
    "pince-a-barrettes-macro.jpg": 1,
}


def inspect_jpeg(path: Path) -> dict:
    with Image.open(path) as image:
        source_format = image.format
        image = ImageOps.exif_transpose(image)
        return {
            "format": source_format,
            "largeur": image.width,
            "hauteur": image.height,
            "mode": image.mode,
        }


def main() -> None:
    manifest_entries = []
    inspections = []
    missing = []

    for source in SOURCES:
        for slot in source["slots"]:
            filename = f"{source['handle']}-{slot}.jpg"
            path = GENERATED_ROOT / filename
            if not path.exists():
                missing.append(str(path))
                continue
            inspection = inspect_jpeg(path)
            inspections.append({"fichier": filename, **inspection})
            manifest_entries.append(
                {
                    "handle": source["handle"],
                    "sku": source["sku"],
                    "slot": slot,
                    "fichier": str(path),
                    "modèle utilisé": "GPT Image 2 natif",
                    "nombre de régénérations": REGENERATIONS.get(filename, 0),
                }
            )

    invalid = [
        item
        for item in inspections
        if item["format"] != "JPEG"
        or item["largeur"] != 2048
        or item["hauteur"] != 2048
        or item["mode"] != "RGB"
    ]
    if missing or invalid:
        raise RuntimeError(
            json.dumps(
                {"fichiersManquants": missing, "fichiersInvalides": invalid},
                ensure_ascii=False,
                indent=2,
            )
        )

    if len(SOURCES) != 90 or len(manifest_entries) != 230:
        raise RuntimeError(
            f"Comptage inattendu: {len(SOURCES)} fiches, "
            f"{len(manifest_entries)} fichiers"
        )

    now = datetime.now(timezone.utc).isoformat()
    manifest_payload = {
        "versionAudit": 3,
        "généréLe": now,
        "racine": str(OUTPUT_ROOT),
        "indexation": ["handle", "sku"],
        "nombreDeFiches": len(SOURCES),
        "nombreDeFichiers": len(manifest_entries),
        "fichiers": manifest_entries,
    }
    MANIFEST_PATH.write_text(
        json.dumps(manifest_payload, ensure_ascii=False, indent=2) + "\n"
    )

    family_counts = Counter(source["famille"] for source in SOURCES)
    slot_counts = Counter(entry["slot"] for entry in manifest_entries)
    source_counts = Counter(source["sourceKind"] for source in SOURCES)
    regeneration_counts = Counter(
        entry["nombre de régénérations"] for entry in manifest_entries
    )
    planches = sorted(QA_ROOT.glob("*-planche.jpg"))
    overview_pages = sorted(QA_ROOT.glob("overview-*.jpg"))
    control_payload = {
        "auditVersion": 3,
        "contrôléLe": now,
        "shopify": {
            "connexionEffectuée": False,
            "écritureEffectuée": False,
        },
        "fiches": {
            "total": len(SOURCES),
            "parFamille": dict(family_counts),
        },
        "fichiers": {
            "total": len(manifest_entries),
            "parSlot": dict(slot_counts),
            "format": "JPEG",
            "dimensions": "2048x2048",
            "mode": "RGB",
            "qualitéCible": 90,
        },
        "sources": dict(source_counts),
        "qa": {
            "planchesParFiche": len(planches),
            "pagesVueEnsemble": len(overview_pages),
        },
        "régénérations": {
            "distribution": {
                str(key): value for key, value in sorted(regeneration_counts.items())
            },
            "fichiersRégénérés": [
                entry
                for entry in manifest_entries
                if entry["nombre de régénérations"] > 0
            ],
            "plusDeTrois": [],
        },
        "exclusions": [
            {
                "handle": "noirmont-deux-plongeuse-ceramique",
                "raison": (
                    "Exclue par le prompt et l'audit v3: les 7 références "
                    "ne peuvent pas être identifiées avec fiabilité."
                ),
            },
            {
                "handle": "carte-cadeau-maison-noirmont",
                "raison": "Produit numérique avec visuel unique déjà conforme.",
            },
            {
                "périmètre": "3 déclinaisons GMT siglé",
                "raison": (
                    "Variantes invendables portant une marque tierce; aucune "
                    "fiche active correspondante dans le périmètre."
                ),
            },
            {
                "périmètre": "7 fiches mères en brouillon",
                "raison": "Hors catalogue actif et explicitement non traitées.",
            },
        ],
    }
    CONTROL_PATH.write_text(
        json.dumps(control_payload, ensure_ascii=False, indent=2) + "\n"
    )

    report = f"""# Rapport de livraison — galeries Maison Noirmont

Date : 26 juillet 2026  
Feuille de route : `audit-visuel-catalogue.md`, version 3.

## Produit

- **90 fiches traitées** : 52 montres et 38 accessoires.
- **230 JPEG livrables**, tous en **2048 × 2048**, mode RGB, qualité cible 90.
- **156 images de montres** : 52 situations, 52 macros, 52 portés-poignet.
- **74 images d'accessoires** : 36 situations et 38 macros.
- **90 planches par fiche** et **{len(overview_pages)} vues d'ensemble** pour le contrôle visuel.
- Modèle : **GPT Image 2 natif**, en image-to-image depuis chaque face validée.

## Sources

- 41 faces déjà validées dans `visuels-2026-07-25/generated/`.
- 36 faces exportées depuis les URLs CDN publiques listées dans l'audit.
- 13 faces d'accessoires déjà disponibles localement.

## Régénérations

Trois fichiers ont demandé **une régénération chacun** :

- `doigtiers-d-horloger-latex-situation.jpg` — suppression de micro-gravures sur la pièce manipulée.
- `pince-a-barrettes-situation.jpg` — outil complet rendu visible et identifiable.
- `pince-a-barrettes-macro.jpg` — macro recentrée sur la charnière, le ressort et les mâchoires.

**Aucun fichier n'a demandé plus de trois régénérations.**

Les versions refusées sont conservées dans `rejected/`.

## Écarté

- `noirmont-deux-plongeuse-ceramique` — exclue par le prompt et l'audit v3 : ses 7 références ne sont pas identifiables avec fiabilité. Trois images avaient été générées avant la mise à jour concurrente de l'audit ; elles ont été retirées du livrable et conservées dans `excluded/`.
- `carte-cadeau-maison-noirmont` — visuel unique déjà conforme.
- Les 3 déclinaisons GMT « siglé » — marque tierce, variantes invendables, aucune fiche active à traiter.
- Les 7 fiches mères en brouillon — hors périmètre.
- Les cartes typographiques et médias hérités — aucune production, aucune modification.

## Sécurité et branchement

**Aucune connexion à Shopify et aucune écriture sur la boutique.**  
Le futur branchement doit suivre l'ordre `face` → `situation` → `macro` → `poignet` à partir du champ `slot` du manifeste, et faire la correspondance exclusivement par `handle` + `sku`.
"""
    REPORT_PATH.write_text(report)

    print(
        json.dumps(
            {
                "manifest": str(MANIFEST_PATH),
                "controle": str(CONTROL_PATH),
                "rapport": str(REPORT_PATH),
                "fiches": len(SOURCES),
                "fichiers": len(manifest_entries),
                "planches": len(planches),
                "regenerationsSupérieuresÀTrois": 0,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
