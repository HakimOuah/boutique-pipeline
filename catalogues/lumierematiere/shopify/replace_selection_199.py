#!/usr/bin/env python3
"""Remplace « Autour de 199 € » par « Pour le salon » et dépublie selection-199.

Home + panier pointent vers `suspensions-salon`. Redirection 301 de l'ancien
handle. Idempotent. N'écrit ni Helio ni UNIVERS.
"""
from __future__ import annotations

import json
import sys
import time
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from apply_fullstack import theme_file, upsert_theme_file  # noqa: E402
from client import gql  # noqa: E402
from import_catalogue import ONLINE  # noqa: E402

BACKUP = ROOT / "backups" / f"{date.today().isoformat()}-selection-salon"
COLL_OLD = "gid://shopify/Collection/651939184976"
TITLE = "<h2>Pour le salon</h2>"
SUB = (
    "<p>Les suspensions qui tiennent une pièce à vivre. Bambou, rotin, verre, "
    "pierre ou métal, choisis pour le salon.</p>"
)
CTA = "Voir les suspensions salon"
LINK = "shopify://collections/suspensions-salon"


def assert_no_dashes(blob: str, label: str) -> None:
    if "—" in blob or "–" in blob:
        raise RuntimeError(f"{label}: cadratin restant")


def patch_home(data: dict) -> dict:
    feat = data["sections"]["collection_featured_JXRpw3"]
    feat["settings"]["collection"] = "suspensions-salon"
    head = feat["blocks"]["group_9NwHBp"]["blocks"]["group_TwitGb"]["blocks"]
    head["text_QEHkGh"]["settings"]["text"] = TITLE
    head["text_6LANC3"]["settings"]["text"] = SUB
    btn = feat["blocks"]["group_9NwHBp"]["blocks"]["button_DFrQyK"]["settings"]
    btn["label"] = CTA
    if "link" in btn:
        btn["link"] = LINK

    cta = data["sections"].get("lm_cta_final")
    if cta:
        boutons = (
            cta["blocks"]["group_principal"]["blocks"]["boutons"]["blocks"]
        )
        if "cta_199" in boutons:
            settings = boutons["cta_199"]["settings"]
            settings["label"] = CTA
            settings["link"] = LINK
    return data


def patch_cart(data: dict) -> dict:
    reco = data["sections"]["lm_reco"]
    reco["settings"]["collection"] = "suspensions-salon"
    reco["blocks"]["lm_reco_header"]["blocks"]["lm_reco_title"]["settings"][
        "text"
    ] = "<p>Pour le salon</p>"
    reco["blocks"]["lm_reco_header"]["blocks"]["lm_reco_btn"]["settings"][
        "link"
    ] = LINK
    reco["blocks"]["lm_reco_header"]["blocks"]["lm_reco_btn"]["settings"][
        "label"
    ] = CTA
    return data


def unpublish_selection() -> None:
    data = gql(
        """
        mutation Unpub($id: ID!, $input: [PublicationInput!]!) {
          publishableUnpublish(id: $id, input: $input) {
            userErrors { field message }
          }
        }
        """,
        {"id": COLL_OLD, "input": [{"publicationId": ONLINE}]},
    )
    errs = data["publishableUnpublish"]["userErrors"]
    if errs:
        msg = json.dumps(errs, ensure_ascii=False)
        if "already" not in msg.lower() and "déjà" not in msg.lower():
            raise RuntimeError(errs)
    print("  selection-199 dépubliée")


def redirect() -> None:
    existing = gql(
        """
        query {
          urlRedirects(first: 50, query: "path:/collections/selection-199") {
            nodes { id path target }
          }
        }
        """
    )["urlRedirects"]["nodes"]
    for n in existing:
        if n["path"] == "/collections/selection-199" and n["target"] == "/collections/suspensions-salon":
            print("  redirection déjà en place")
            return
    payload = gql(
        """
        mutation Redir($input: UrlRedirectInput!) {
          urlRedirectCreate(urlRedirect: $input) {
            urlRedirect { id path target }
            userErrors { field message }
          }
        }
        """,
        {
            "input": {
                "path": "/collections/selection-199",
                "target": "/collections/suspensions-salon",
            }
        },
    )["urlRedirectCreate"]
    if payload["userErrors"]:
        raise RuntimeError(payload["userErrors"])
    print("  301 /collections/selection-199 → /collections/suspensions-salon")


def main() -> None:
    BACKUP.mkdir(parents=True, exist_ok=True)
    home = theme_file("templates/index.json")
    cart = theme_file("templates/cart.json")
    (BACKUP / "index.json.avant").write_text(
        json.dumps(home, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (BACKUP / "cart.json.avant").write_text(
        json.dumps(cart, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    home = patch_home(home)
    cart = patch_cart(cart)
    for label, blob in (("home", home), ("cart", cart)):
        text = json.dumps(blob, ensure_ascii=False)
        assert_no_dashes(text, label)
        if "Autour de 199" in text or "autour de 199" in text:
            raise RuntimeError(f"{label}: mention 199 encore présente")
        if "selection-199" in text:
            raise RuntimeError(f"{label}: handle selection-199 encore cité")

    upsert_theme_file("templates/index.json", home)
    time.sleep(0.4)
    upsert_theme_file("templates/cart.json", cart)
    time.sleep(0.6)

    live_home = theme_file("templates/index.json")
    live_cart = theme_file("templates/cart.json")
    home_blob = json.dumps(live_home, ensure_ascii=False)
    cart_blob = json.dumps(live_cart, ensure_ascii=False)
    if "Pour le salon" not in home_blob or "suspensions-salon" not in home_blob:
        raise RuntimeError("home: Pour le salon / suspensions-salon absents")
    if "Autour de 199" in home_blob or "selection-199" in home_blob:
        raise RuntimeError("home: ancienne sélection encore là")
    if "Pour le salon" not in cart_blob or "suspensions-salon" not in cart_blob:
        raise RuntimeError("cart: Pour le salon / suspensions-salon absents")
    if "Autour de 199" in cart_blob or "selection-199" in cart_blob:
        raise RuntimeError("cart: ancienne sélection encore là")

    unpublish_selection()
    redirect()
    print("OK sélection 199 remplacée par Pour le salon")


if __name__ == "__main__":
    main()
