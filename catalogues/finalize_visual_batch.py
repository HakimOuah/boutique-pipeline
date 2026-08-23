#!/usr/bin/env python3
"""Finalize a validated canonical-g1 visual batch for either catalogue."""

import argparse
import csv
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--brand", choices=("orysbain", "lumierematiere"), required=True)
    parser.add_argument("--mapping", type=Path, required=True)
    args = parser.parse_args()

    brand_root = ROOT / args.brand
    with (brand_root / "catalogue-dsers.csv").open(encoding="utf-8-sig", newline="") as stream:
        catalogue = {row["handle"]: row for row in csv.DictReader(stream)}
    mappings = json.loads(args.mapping.read_text(encoding="utf-8"))
    output_root = brand_root / "livraisons-visuels-codex" / "produits"

    if args.brand == "lumierematiere":
        slots = [
            "g1-hero-allume", "g2-silhouette-angle-matiere", "g3-macro-matiere",
            "g4-lifestyle", "g5-qualite-lumiere",
        ]
    else:
        slots = [
            "g1-hero-packshot", "g2-trois-quarts-structure", "g3-detail-commande-finition",
            "g4-lifestyle-salle-de-bain", "g5-usage-serviettes",
        ]

    for item in mappings:
        row = catalogue[item["handle"]]
        product_dir = output_root / item["handle"]
        product_dir.mkdir(parents=True, exist_ok=True)
        images = []
        for index in range(1, 6):
            filename = f"{item['handle']}-g{index}.jpg"
            subprocess.run(
                [
                    "sips", "-s", "format", "jpeg", "-s", "formatOptions", "88",
                    "-z", "2048", "2048", item[f"g{index}"], "--out", str(product_dir / filename),
                ],
                check=True,
                stdout=subprocess.DEVNULL,
            )
            images.append({"fichier": filename, "slot": slots[index - 1], "source": item["source_relative"]})

        manifest = {
            "brand": args.brand,
            "sku": row["sku"],
            "handle": row["handle"],
            "supplier_id": row["supplier_id"],
            "images": images,
            "ecartes": [],
        }
        if args.brand == "lumierematiere":
            manifest["collection"] = row["collection"]
        (product_dir / "manifeste.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        (product_dir / "compte-rendu.md").write_text(
            f"# Compte-rendu — {row['handle']}\n\n"
            f"- SKU : `{row['sku']}`\n"
            f"- Source canonique : `{item['source_relative']}`\n"
            "- Livraison : 5 JPEG RGB, 2048 x 2048, g1 a g5.\n"
            "- Methode : g1 compose depuis la source fournisseur ; g2 a g5 derives du g1 canonique pour verrouiller l'identite produit.\n"
            "- Contraintes : aucun texte, logo vendeur, badge, filigrane, cote, visage, main ou corps.\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
