"""Rattache la livraison Codex appliques (26/08/2026) aux fiches Shopify.

Pour chaque handle livré : upload g1–g5, suppression des photos AliExpress,
ordre g1…g5, packshots de teinte sur les variantes, cover de collection.

SKU DSers inchangés. Idempotent : skip si l'alt « vue Codex » est déjà en place.

    python3 attach_applique_codex.py --dry-run
    python3 attach_applique_codex.py
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from attach_variant_packshots import wait_media  # noqa: E402
from client import gql  # noqa: E402
from import_catalogue import publish, staged_upload  # noqa: E402

LIVRAISON = HERE.parent / "livraisons-visuels-codex"
PRODUITS = LIVRAISON / "produits"
TEINTES = LIVRAISON / "variantes-couleur"
COVER = LIVRAISON / "brand" / "lumierematiere-collection-appliques-murales.jpg"

# handle, titre, mapping variante → fichier (None = g1 de la galerie)
FICHES = [
    {
        "handle": "applique-murale-pierre-588683",
        "title": "Applique murale galet beige pierre, chambre",
        "teintes": {},  # trois diamètres, même galerie
    },
    {
        "handle": "applique-liseuse-pierre-311650",
        "title": "Applique murale liseuse pierre et bois, chambre",
        "teintes": {
            "Bois clair": TEINTES / "applique-liseuse-pierre-311650" / "applique-liseuse-pierre-311650-bois-clair-g1.jpg",
            "Noyer": None,
        },
    },
    {
        "handle": "applique-double-travertin-474088",
        "title": "Applique murale double travertin, 2 lumières",
        "teintes": {
            "Bois clair": None,
            "Noyer": TEINTES / "applique-double-travertin-474088" / "applique-double-travertin-474088-noyer-g1.jpg",
        },
    },
]


def fetch(handle: str) -> dict:
    data = gql(
        """
        query($h: String!) {
          productByHandle(handle: $h) {
            id handle title status
            media(first: 50) {
              nodes { ... on MediaImage { id alt image { url } } }
            }
            variants(first: 20) {
              nodes { id title selectedOptions { name value } }
            }
          }
        }
        """,
        {"h": handle},
    )
    product = data.get("productByHandle")
    if not product:
        raise RuntimeError(f"fiche introuvable : {handle}")
    return product


def already_codex(product: dict) -> bool:
    alts = [(n.get("alt") or "") for n in product["media"]["nodes"]]
    return any("vue Codex 1" in a for a in alts)


def gallery_files(handle: str) -> list[Path]:
    folder = PRODUITS / handle
    files = [folder / f"{handle}-g{n}.jpg" for n in range(1, 6)]
    missing = [p.name for p in files if not p.exists()]
    if missing:
        raise FileNotFoundError(f"{handle}: {missing}")
    return files


def upload_gallery(product: dict, title: str, files: list[Path]) -> list[str]:
    media = []
    for i, path in enumerate(files, start=1):
        src = staged_upload(path, resource="IMAGE")
        media.append(
            {
                "originalSource": src,
                "alt": f"{title}, vue Codex {i}",
                "mediaContentType": "IMAGE",
            }
        )
        time.sleep(0.12)
    payload = gql(
        """
        mutation($productId: ID!, $media: [CreateMediaInput!]!) {
          productCreateMedia(productId: $productId, media: $media) {
            media { ... on MediaImage { id status } }
            mediaUserErrors { field message }
          }
        }
        """,
        {"productId": product["id"], "media": media},
    )["productCreateMedia"]
    if payload["mediaUserErrors"]:
        raise RuntimeError(payload["mediaUserErrors"])
    ids = [m["id"] for m in payload["media"] if m and m.get("id")]
    if len(ids) != 5:
        raise RuntimeError(f"attendu 5 médias, reçu {len(ids)}")
    wait_media(product["id"], ids)
    return ids


def delete_media(product_id: str, media_ids: list[str]) -> None:
    if not media_ids:
        return
    payload = gql(
        """
        mutation($productId: ID!, $mediaIds: [ID!]!) {
          productDeleteMedia(productId: $productId, mediaIds: $mediaIds) {
            mediaUserErrors { field message }
          }
        }
        """,
        {"productId": product_id, "mediaIds": media_ids},
    )["productDeleteMedia"]
    errs = payload["mediaUserErrors"]
    if errs:
        print("  warn delete", errs)


def reorder(product_id: str, media_ids: list[str]) -> None:
    moves = [{"id": mid, "newPosition": str(i)} for i, mid in enumerate(media_ids)]
    payload = gql(
        """
        mutation($id: ID!, $moves: [MoveInput!]!) {
          productReorderMedia(id: $id, moves: $moves) {
            userErrors { field message }
          }
        }
        """,
        {"id": product_id, "moves": moves},
    )["productReorderMedia"]
    if payload["userErrors"]:
        print("  warn reorder", payload["userErrors"])


def upload_one(product_id: str, title: str, path: Path, alt: str) -> str:
    src = staged_upload(path, resource="IMAGE")
    payload = gql(
        """
        mutation($productId: ID!, $media: [CreateMediaInput!]!) {
          productCreateMedia(productId: $productId, media: $media) {
            media { ... on MediaImage { id } }
            mediaUserErrors { field message }
          }
        }
        """,
        {
            "productId": product_id,
            "media": [
                {
                    "originalSource": src,
                    "alt": alt,
                    "mediaContentType": "IMAGE",
                }
            ],
        },
    )["productCreateMedia"]
    if payload["mediaUserErrors"]:
        raise RuntimeError(payload["mediaUserErrors"])
    mid = payload["media"][0]["id"]
    wait_media(product_id, [mid])
    return mid


def set_variant_media(product_id: str, pairs: list[tuple[str, str]]) -> None:
    if not pairs:
        return
    payload = gql(
        """
        mutation($productId: ID!, $variants: [ProductVariantsBulkInput!]!) {
          productVariantsBulkUpdate(productId: $productId, variants: $variants) {
            userErrors { field message }
          }
        }
        """,
        {
            "productId": product_id,
            "variants": [{"id": vid, "mediaId": mid} for vid, mid in pairs],
        },
    )["productVariantsBulkUpdate"]
    if payload["userErrors"]:
        raise RuntimeError(payload["userErrors"])


def apply_product(spec: dict, dry: bool) -> None:
    handle = spec["handle"]
    print(f"\n== {handle}")
    product = fetch(handle)
    files = gallery_files(handle)
    print(f"  {len(files)} JPEG galerie, {len(product['media']['nodes'])} médias live")
    if already_codex(product):
        print("  déjà Codex, skip galerie")
        return
    if dry:
        print("  [dry] remplacerait les médias AE par g1–g5")
        return

    old_ids = [n["id"] for n in product["media"]["nodes"] if n.get("id")]
    new_ids = upload_gallery(product, spec["title"], files)
    print(f"  upload g1–g5 : {len(new_ids)}")

    teinte_ids: dict[str, str] = {}
    for valeur, path in spec["teintes"].items():
        if path is None:
            continue
        if not path.exists():
            raise FileNotFoundError(path)
        alt = f"{spec['title']}, {valeur.lower()}"
        teinte_ids[valeur] = upload_one(product["id"], spec["title"], path, alt)
        print(f"  upload teinte {valeur}")

    g1 = new_ids[0]
    pairs = []
    for variant in product["variants"]["nodes"]:
        valeur = next((o["value"] for o in variant["selectedOptions"]), variant["title"])
        mid = teinte_ids.get(valeur, g1)
        pairs.append((variant["id"], mid))
    set_variant_media(product["id"], pairs)
    print(f"  {len(pairs)} variantes rattachées")

    delete_media(product["id"], old_ids)
    print(f"  {len(old_ids)} photos AliExpress retirées")
    reorder(product["id"], new_ids)


def apply_cover(dry: bool) -> None:
    print("\n== cover collection")
    if not COVER.exists():
        raise FileNotFoundError(COVER)
    data = gql(
        'query { collectionByHandle(handle: "appliques-murales") { id image { url } } }'
    )["collectionByHandle"]
    if dry:
        print("  [dry] poserait lumierematiere-collection-appliques-murales.jpg")
        return
    src = staged_upload(COVER, resource="IMAGE")
    payload = gql(
        """
        mutation($input: CollectionInput!) {
          collectionUpdate(input: $input) {
            collection { id image { url } }
            userErrors { field message }
          }
        }
        """,
        {
            "input": {
                "id": data["id"],
                "image": {"src": src, "altText": "Appliques murales"},
            }
        },
    )["collectionUpdate"]
    if payload["userErrors"]:
        raise RuntimeError(payload["userErrors"])
    publish(data["id"])
    print("  cover posée")


def draft_mismatch(dry: bool) -> None:
    """LM-126 est en ligne avec des photos d'un autre produit (bloc / cylindre,
    pas galet + équerre E27). Codex a refusé d'inventer. On la retire de la vitrine."""
    print("\n== LM-126 mismatch")
    product = fetch("applique-murale-pierre-metal-147598")
    print(f"  statut actuel : {product['status']}")
    if product["status"] == "DRAFT":
        print("  déjà en brouillon")
        return
    if dry:
        print("  [dry] passerait en brouillon")
        return
    payload = gql(
        """
        mutation($product: ProductUpdateInput!) {
          productUpdate(product: $product) {
            product { id status }
            userErrors { field message }
          }
        }
        """,
        {"product": {"id": product["id"], "status": "DRAFT"}},
    )["productUpdate"]
    if payload["userErrors"]:
        raise RuntimeError(payload["userErrors"])
    print("  passé en brouillon : photos AE ≠ copy (galet + équerre E27)")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    print(f"{'[DRY RUN] ' if args.dry_run else ''}rattachement Codex appliques")
    for spec in FICHES:
        apply_product(spec, args.dry_run)
    apply_cover(args.dry_run)
    draft_mismatch(args.dry_run)


if __name__ == "__main__":
    main()
