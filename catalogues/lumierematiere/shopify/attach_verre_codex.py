"""Rattache la livraison Codex verre (26/08/2026) aux 3 fiches Shopify.

Upload g1–g5, retire les photos AliExpress, ordre g1…g5, g1 sur chaque variante.
SKU DSers inchangés. Idempotent : skip si l’alt « vue Codex 1 » est déjà en place.

Les fiches doivent exister (push DSers + apply_verre.py). Sinon le script s’arrête.

    python3 attach_verre_codex.py --dry-run
    python3 attach_verre_codex.py
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from attach_applique_codex import (  # noqa: E402
    already_codex,
    delete_media,
    fetch,
    gallery_files,
    reorder,
    set_variant_media,
    upload_gallery,
)

FICHES = [
    {
        "handle": "suspension-verre-405368",
        "title": "Suspension verre disque boule colorée, cuisine",
    },
    {
        "handle": "suspension-verre-bois-910933",
        "title": "Suspension verre bois, abat-jour chambre",
    },
    {
        "handle": "suspension-verre-538307",
        "title": "Suspension cylindre verre teinté, chambre",
    },
]


def apply_product(spec: dict, dry: bool) -> None:
    handle = spec["handle"]
    print(f"\n== {handle}")
    product = fetch(handle)
    files = gallery_files(handle)
    print(f"  {len(files)} JPEG galerie, {len(product['media']['nodes'])} médias live")
    if already_codex(product):
        print("  déjà Codex, skip")
        return
    if dry:
        print("  [dry] remplacerait les médias AE par g1–g5")
        return

    old_ids = [n["id"] for n in product["media"]["nodes"] if n.get("id")]
    new_ids = upload_gallery(product, spec["title"], files)
    print(f"  upload g1–g5 : {len(new_ids)}")

    g1 = new_ids[0]
    pairs = [(v["id"], g1) for v in product["variants"]["nodes"]]
    set_variant_media(product["id"], pairs)
    print(f"  {len(pairs)} variantes rattachées à g1")

    delete_media(product["id"], old_ids)
    print(f"  {len(old_ids)} photos AliExpress retirées")
    reorder(product["id"], new_ids)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--only", help="handles séparés par des virgules")
    args = parser.parse_args()
    todo = FICHES
    if args.only:
        wanted = {h.strip() for h in args.only.split(",")}
        todo = [s for s in FICHES if s["handle"] in wanted]
    print(f"{'[DRY RUN] ' if args.dry_run else ''}rattachement Codex verre ({len(todo)})")
    for spec in todo:
        apply_product(spec, args.dry_run)


if __name__ == "__main__":
    main()
