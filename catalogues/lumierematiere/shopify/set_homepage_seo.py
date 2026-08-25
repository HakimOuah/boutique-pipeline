#!/usr/bin/env python3
"""Titre SEO, méta-description et image de partage (1200×628) de la page d'accueil.

Idempotent. N'écrit aucun thème. Le logo source reste dans livraisons-visuels-codex/brand
(gitignored) ; l'OG est régénéré à chaque run.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from apply_fullstack import file_create  # noqa: E402
from client import gql  # noqa: E402

BRAND = ROOT.parent / "livraisons-visuels-codex" / "brand"
LOGO = BRAND / "lumierematiere-logo-primary-charbon.png"
OG_PATH = ROOT / "lumierematiere-og-1200x628.jpg"
SHOP_ID = "gid://shopify/Shop/94699356496"

PAPER = (246, 243, 236)  # #F6F3EC
OG_W, OG_H = 1200, 628
LOGO_WIDTH = 880

TITLE = "Suspensions et lustres par matière | Lumière Matière"
META = (
    "Suspensions, lustres et plafonniers choisis pour le bambou, le rotin, "
    "le bois, la pierre ou le verre. Livraison offerte en France, retours 30 jours."
)


def compose_og() -> Path:
    if not LOGO.exists():
        raise RuntimeError(f"logo introuvable : {LOGO}")
    canvas = Image.new("RGB", (OG_W, OG_H), PAPER)
    logo = Image.open(LOGO).convert("RGBA")
    ratio = LOGO_WIDTH / logo.width
    logo = logo.resize((LOGO_WIDTH, round(logo.height * ratio)), Image.Resampling.LANCZOS)
    x = (OG_W - logo.width) // 2
    y = (OG_H - logo.height) // 2
    canvas.paste(logo, (x, y), logo)
    canvas.save(OG_PATH, "JPEG", quality=92, optimize=True, subsampling=0)
    print(f"  OG {OG_PATH.name} {OG_W}×{OG_H} ({OG_PATH.stat().st_size} o)")
    return OG_PATH


def set_metafields(media_gid: str | None) -> None:
    metafields = [
        {
            "ownerId": SHOP_ID,
            "namespace": "global",
            "key": "title_tag",
            "type": "single_line_text_field",
            "value": TITLE,
        },
        {
            "ownerId": SHOP_ID,
            "namespace": "global",
            "key": "description_tag",
            "type": "single_line_text_field",
            "value": META,
        },
    ]
    if media_gid:
        metafields.append(
            {
                "ownerId": SHOP_ID,
                "namespace": "global",
                "key": "social_sharing_image",
                "type": "file_reference",
                "value": media_gid,
            }
        )
    data = gql(
        """
        mutation M($metafields: [MetafieldsSetInput!]!) {
          metafieldsSet(metafields: $metafields) {
            metafields { namespace key type value }
            userErrors { field message }
          }
        }
        """,
        {"metafields": metafields},
    )
    payload = data["metafieldsSet"]
    if payload["userErrors"]:
        raise RuntimeError(payload["userErrors"])
    for mf in payload["metafields"]:
        shown = (mf["value"] or "")[:80]
        print(f"  {mf['namespace']}.{mf['key']} = {shown}")


def verify() -> None:
    data = gql(
        """
        query {
          shop {
            title: metafield(namespace: "global", key: "title_tag") { value }
            desc: metafield(namespace: "global", key: "description_tag") { value }
            og: metafield(namespace: "global", key: "social_sharing_image") {
              value
              reference {
                ... on MediaImage { id image { url width height } }
              }
            }
          }
        }
        """
    )
    shop = data["shop"]
    title = (shop["title"] or {}).get("value")
    desc = (shop["desc"] or {}).get("value")
    if title != TITLE:
        raise RuntimeError(f"titre live ≠ attendu : {title!r}")
    if desc != META:
        raise RuntimeError(f"méta live ≠ attendue : {desc!r}")
    print(f"  vérif titre {len(title)} c / méta {len(desc)} c")
    og = shop["og"]
    if og and og.get("reference") and og["reference"].get("image"):
        img = og["reference"]["image"]
        print(f"  vérif OG {img['width']}×{img['height']} {img['url']}")
    elif og and og.get("value"):
        print(f"  OG gid {og['value']} (référence non résolue)")
    else:
        print("  OG metafield absent (à coller à la main dans Préférences si besoin)")


def main() -> None:
    print(f"titre {len(TITLE)} / 70")
    print(f"méta  {len(META)} / 320")
    if len(TITLE) > 70 or len(META) > 320:
        raise RuntimeError("limite SEO dépassée")
    if "—" in TITLE + META or "–" in TITLE + META:
        raise RuntimeError("cadratin dans le SEO")

    print("— image de partage")
    compose_og()
    media_ref = file_create(OG_PATH, "Lumière Matière")
    print(f"  media {media_ref}")
    gid = None
    img: dict = {}
    for attempt in range(8):
        files = gql(
            """
            query {
              files(first: 5, query: "lumierematiere-og-1200x628.jpg") {
                nodes { id ... on MediaImage { image { url width height } } }
              }
            }
            """
        )
        nodes = files["files"]["nodes"]
        if nodes:
            gid = nodes[0]["id"]
            img = nodes[0].get("image") or {}
            break
        time.sleep(0.6)
    if not gid:
        raise RuntimeError("OG introuvable après upload")
    print(f"  fichier {gid} {img.get('width')}×{img.get('height')}")

    print("— metafields boutique")
    try:
        set_metafields(gid)
    except RuntimeError as err:
        print(f"  warn OG metafield : {err}")
        print("  retry titre + méta seuls")
        set_metafields(None)

    time.sleep(0.4)
    print("— vérif")
    verify()
    print("OK homepage SEO")


if __name__ == "__main__":
    main()
