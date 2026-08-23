#!/usr/bin/env python3
"""Finalize the first validated Lumiere Matiere product-image batch."""

import csv
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
GEN = Path("/Users/Hakim/.codex/generated_images/01a02158-0e90-73c1-af37-b5605ebf1a5c")
DEST = ROOT / "lumierematiere" / "livraisons-visuels-codex" / "produits"
CSV = ROOT / "lumierematiere" / "catalogue-dsers.csv"

OUTPUTS = {
    "suspension-bambou-942503": [
        "ce939a5c-b578-4842-8a7c-158888b4d9b9",
        "df46a866-dedc-4810-a490-9a47b3b28143",
        "53d292bd-8089-478a-a8a6-8a5c275df626",
        "4e585ef7-8904-44bc-913a-ef5341db07ee",
        "f7f06640-ff56-4547-a981-0c16188708fe",
    ],
    "suspension-bambou-dore-60cm-805884": [
        "481fd5b5-7ab4-4b20-8be8-8b7bbad30bdb",
        "ba85961e-35d1-4ac1-a278-e09ed5d5383b",
        "28da6478-9e69-46d3-9aaf-f01d2486d922",
        "2eef5a0d-678d-4c63-ad91-33ea792a639a",
        "c647d38c-5177-47f1-8d1c-d0e0ed595ed9",
    ],
    "suspension-bambou-45cm-962644": [
        "d9864403-d181-4c8d-a8a9-184e7d76fb7b",
        "1d06d564-4618-409a-be91-0c83da8b0f7b",
        "dcdd583e-ea75-46d3-8211-43386785ec88",
        "12444320-efbb-488c-88d6-5c4f7f4b587e",
        "48a68102-bdb3-4471-8675-758f59d70038",
    ],
    "suspension-bambou-067987": [
        "9091c597-f2fc-4b55-ba83-a76b75be4e27",
        "86c05b11-1499-4c1b-840f-51c499cd6422",
        "d463caad-290b-4674-837e-2c10554c3b3c",
        "f8532f55-0d55-4240-a906-237cdcae7130",
        "1f726bf0-5949-4f6f-a20c-ca38ecff55a2",
    ],
    "suspension-bambou-led-80-cm-191307": [
        "f7155bfb-5201-4217-906e-8dc5124db8db",
        "54ae63a0-0c69-4e5e-92e9-13393341bf01",
        "4ef208df-eb74-4f6b-afa6-dc838e5161ce",
        "bfb83573-9358-45d7-ac29-99930e12e43e",
        "5df750e3-80d6-4efa-8636-18dac07f893e",
    ],
}

SLOTS = [
    "g1-hero-allume",
    "g2-silhouette-angle-matiere",
    "g3-macro-matiere",
    "g4-lifestyle",
    "g5-qualite-lumiere",
]


def main() -> None:
    with CSV.open(encoding="utf-8-sig", newline="") as stream:
        rows = {row["handle"]: row for row in csv.DictReader(stream)}

    for handle, generated_ids in OUTPUTS.items():
        row = rows[handle]
        product_dir = DEST / handle
        product_dir.mkdir(parents=True, exist_ok=True)
        source = f"catalogues/lumierematiere/sources-fournisseur/{row['supplier_id']}/01.jpg"
        images = []

        for index, generated_id in enumerate(generated_ids, start=1):
            filename = f"{handle}-g{index}.jpg"
            subprocess.run(
                [
                    "sips", "-s", "format", "jpeg", "-s", "formatOptions", "88",
                    "-z", "2048", "2048", str(GEN / f"exec-{generated_id}.png"),
                    "--out", str(product_dir / filename),
                ],
                check=True,
                stdout=subprocess.DEVNULL,
            )
            images.append({"fichier": filename, "slot": SLOTS[index - 1], "source": source})

        manifest = {
            "brand": "lumierematiere",
            "sku": row["sku"],
            "handle": handle,
            "collection": row["collection"],
            "supplier_id": row["supplier_id"],
            "images": images,
            "ecartes": [
                "Premiere passe g2-g5 rejetee: variantes de silhouette ou de couleur entre les photos fournisseur 02-05. Regeneration depuis le g1 canonique valide."
            ],
        }
        (product_dir / "manifeste.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        (product_dir / "compte-rendu.md").write_text(
            f"# Compte-rendu — {handle}\n\n"
            f"- SKU : `{row['sku']}`\n"
            f"- Collection : {row['collection']}\n"
            f"- Source canonique : `{source}`\n"
            "- Livraison : 5 JPEG sRGB, 2048 x 2048, g1 a g5.\n"
            "- Methode : g1 compose depuis la source fournisseur ; g2 a g5 derives du g1 valide pour verrouiller silhouette, finition et coloris.\n"
            "- QA : aucune personne, aucun texte, logo vendeur, badge, filigrane ou cote incrustee.\n"
            "- Ecarte : premiere passe g2 a g5, incoherente entre variantes fournisseur.\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
