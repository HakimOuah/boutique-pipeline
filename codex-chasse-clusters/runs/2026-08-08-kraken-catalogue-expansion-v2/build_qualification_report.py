#!/usr/bin/env python3
"""Genere le rapport Markdown du run a partir des sorties validees."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parent
CATALOGUE = RUN_DIR / "final-catalogue-reviewed.json"
GATE = RUN_DIR / "final-catalogue-gate-report.json"
MANUAL_AUDIT = RUN_DIR / "manual-audit-summary.json"
CONCEPTS = RUN_DIR / "competitor-concepts-validation.json"
VOLUMES = RUN_DIR / "keyword-volumes-fr.json"
OUT = RUN_DIR / "rapport-qualification.md"

ORDER = [
    "Balade, transport & mobilité du chien",
    "Mercerie créative & arts du fil",
    "Scrapbooking & journaling",
    "Perles & création de bijoux",
    "Aquariophilie & aquascaping",
]


def main() -> int:
    catalogue = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    gate = json.loads(GATE.read_text(encoding="utf-8"))
    manual_audit = json.loads(MANUAL_AUDIT.read_text(encoding="utf-8"))
    concepts = json.loads(CONCEPTS.read_text(encoding="utf-8"))
    volumes = json.loads(VOLUMES.read_text(encoding="utf-8"))
    origins = Counter((row["niche"], row["candidate_origin"]) for row in catalogue["products"])
    supplier_tiers = Counter((row["niche"], row["supplier_evidence_status"]) for row in catalogue["products"])
    collection_counts = Counter(row["niche"] for row in catalogue["collections"])

    lines = [
        "# Qualification Kraken — arborescence et catalogue fournisseur audité",
        "",
        "Date : 2026-08-08",
        f"Run : `{RUN_DIR.name}`",
        "Mode : lecture seule — aucune mutation Shopify, DSers, GMC ou Google Ads.",
        "",
        "## Verdict",
        "",
        ("**INTÉGRITÉ DU LIVRABLE PASSÉE — OBJECTIFS DE PROFONDEUR PARTIELS**" if gate["integrity_ok"] and not gate["quota_reference_pass"] else "**INTÉGRITÉ ET OBJECTIFS DE PROFONDEUR PASSÉS**" if gate["integrity_ok"] else "**GATE D'INTÉGRITÉ NON PASSÉ**"),
        "",
        f"- {concepts['accepted_after_dedup']} concepts concurrents stricts conservés après nettoyage.",
        f"- {len(volumes['keywords'])} mots-clés business SEMrush France documentés.",
        f"- {manual_audit['machine_products']} listings candidats relus manuellement : {manual_audit['accepted_products']} acceptés et {manual_audit['rejected_products']} rejetés.",
        f"- {gate['products']} fiches produit livrées, avec {gate['unique_ids_by_niche']} couples niche/ID AliExpress uniques.",
        "- Chaque titre produit commence par un mot-clé mesuré; le volume est affiché à côté dans le classeur.",
        "- Les volumes répétés sur plusieurs PDP ne sont pas additionnés au potentiel commercial de la boutique.",
        "- Les écarts aux objectifs de profondeur sont conservés explicitement : aucun faux positif n'a été ajouté pour remplir un quota.",
        "",
        "## Résultat par niche",
        "",
        "| Niche | Mot-clé général | Volume général | Volume commercial nettoyé | Collections | Candidats machine | Acceptés | Objectif indicatif | Écart | Listing qualifié | Listing à vérifier |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for niche in ORDER:
        root = catalogue["root_keywords"][niche]
        lines.append(
            "| " + " | ".join([
                niche,
                root["keyword"],
                f"{root['volume']:,}".replace(",", " "),
                f"{catalogue['clean_totals_by_niche'][niche]:,}".replace(",", " "),
                str(collection_counts[niche]),
                str(catalogue["machine_counts_by_niche"][niche]),
                str(catalogue["counts_by_niche"][niche]),
                str(catalogue["reference_targets_by_niche"][niche]),
                str(catalogue["counts_by_niche"][niche] - catalogue["reference_targets_by_niche"][niche]),
                str(supplier_tiers[(niche, "LISTING_QUALIFIE_NOTE_COMMANDES")]),
                str(supplier_tiers[(niche, "LISTING_SEMANTIQUE_A_VERIFIER")]),
            ]) + " |"
        )

    lines.extend([
        "",
        "## Gates appliqués",
        "",
        "1. Boutique : au moins 30 000 recherches commerciales nettoyées en France; 40 000 constitue la zone de confort.",
        "2. Collection : cœur à partir de 1 000; secondaire à partir de 500; revue entre 300 et 499.",
        "3. PDP : mot-clé mesuré strictement positif, titre aligné et rattachement à une collection mesurée.",
        "4. Catalogue : objectifs indicatifs de 100 ou 200 références selon la niche, sans compter une simple couleur, taille ou quantité comme nouveau produit; les écarts restent visibles.",
        "5. Listing API : pertinence sémantique, prix présent et validation humaine. La note et les commandes déterminent le niveau de preuve fournisseur, sans exclure un listing sémantique qui doit encore être vérifié.",
        "",
        "## Niveaux de preuve",
        "",
        "- `EQUIVALENT_CONCURRENT_API` : produit ou collection concurrente observée, concept générique dédupliqué et listing AliExpress pertinent trouvé.",
        "- `DECOUVERTE_FAMILLE_SEO_API` : listing distinct trouvé dans une famille business déjà mesurée; aucune correspondance PDP concurrente directe n'est affirmée.",
        "- `LISTING_QUALIFIE_NOTE_COMMANDES` : listing aligné, note au moins 4,5 et commandes observées.",
        "- `LISTING_SEMANTIQUE_A_VERIFIER` : listing aligné et prix présent, mais note/commandes encore insuffisantes ou absentes; contrôle exact obligatoire.",
        f"- Répartition des produits acceptés par origine : {sum(origins.values())} lignes. Toutes portent une décision humaine `ACCEPT` et son motif.",
        "- `MANQUANT` : SKU exact, variante, fret France, conformité, prix rendu, marge et CAC d'équilibre restent à valider avant import ou lancement.",
        "",
        "## Limites et prochaine porte",
        "",
        "Ce run prouve une architecture mesurée et un premier catalogue fournisseur audité. Il ne constitue pas une validation commerciale finale et n'atteint pas tous les objectifs indicatifs de profondeur. La prochaine porte doit sélectionner les références prioritaires, puis vérifier le SKU exact, la variante, la livraison France, la conformité, le coût rendu, le prix cible, la marge de contribution et le CAC d'équilibre. Les catégories sécurité, électrique, CO2, métaux et propriété intellectuelle doivent recevoir leur contrôle spécialisé avant publication.",
        "",
        "## Reproduction",
        "",
        "Voir `README.md` dans ce dossier pour l'ordre des scripts et les garde-fous. Le classeur final est généré avec `build_final_workbook.mjs`, puis inspecté et rendu en PNG avant export XLSX.",
        "",
    ])
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"integrity_ok": gate["integrity_ok"], "quota_reference_pass": gate["quota_reference_pass"], "output": str(OUT), "products": gate["products"]}, ensure_ascii=False, indent=2))
    return 0 if gate["integrity_ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
