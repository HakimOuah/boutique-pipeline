#!/usr/bin/env python3
"""Pied de page Full Stack — structure Montre Avenue, mailto / tel / Contact cliquables."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from apply_fullstack import theme_file, upsert_theme_file  # noqa: E402
from client import gql  # noqa: E402

EMAIL = "contact@lumierematiere.fr"
PHONE_DISPLAY = "+33 7 56 82 80 94"
PHONE_TEL = "+33756828094"
CONTACT_PATH = "/pages/contact"

BRAND_HTML = (
    "<p>Lumière Matière rassemble des suspensions, des lustres et des plafonniers "
    "choisis pour la lumière qu’ils posent dans une pièce.</p>"
    f'<p><a href="mailto:{EMAIL}">{EMAIL}</a><br>'
    f'<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br>'
    f'<a href="{CONTACT_PATH}">Contact</a></p>'
    "<p>47 rue Vivienne, 75002 Paris<br>"
    "SAV ouvert du lundi au vendredi, de 10h à 18h (heure de Paris)</p>"
)

SAV_TRUST_HTML = (
    f'<p>Écrivez-nous à <a href="mailto:{EMAIL}">{EMAIL}</a> ou appelez le '
    f'<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.<br>'
    f'Vous pouvez aussi passer par la page <a href="{CONTACT_PATH}">Contact</a>. '
    "On répond du lundi au vendredi, de 10h à 18h (heure de Paris), "
    "sous 24 h ouvrées.</p>"
)

MENU_PRINCIPAL = {
    "handle": "footer-principal",
    "title": "Pied de page — Menu principal",
    "items": [
        {"title": "Accueil", "type": "FRONTPAGE"},
        {"title": "Par matière", "type": "COLLECTIONS"},
        {
            "title": "Lustres",
            "type": "COLLECTION",
            "resourceId": "gid://shopify/Collection/651938988368",
        },
        {
            "title": "Plafonniers",
            "type": "COLLECTION",
            "resourceId": "gid://shopify/Collection/651939021136",
        },
        {
            "title": "Notre histoire",
            "type": "PAGE",
            "resourceId": "gid://shopify/Page/160675103056",
        },
    ],
}

MENU_INFORMATIONS = {
    "handle": "footer-informations",
    "title": "Pied de page — Informations",
    "items": [
        {
            "title": "Contact",
            "type": "PAGE",
            "resourceId": "gid://shopify/Page/160674742608",
        },
        {
            "title": "FAQ",
            "type": "PAGE",
            "resourceId": "gid://shopify/Page/160675135824",
        },
        {
            "title": "Mentions légales",
            "type": "SHOP_POLICY",
            "resourceId": "gid://shopify/ShopPolicy/50191106384",
        },
        {
            "title": "Confidentialité",
            "type": "SHOP_POLICY",
            "resourceId": "gid://shopify/ShopPolicy/50190877008",
        },
        {
            "title": "Politique de remboursement",
            "type": "SHOP_POLICY",
            "resourceId": "gid://shopify/ShopPolicy/50191040848",
        },
        {
            "title": "Politique de livraison",
            "type": "SHOP_POLICY",
            "resourceId": "gid://shopify/ShopPolicy/50191073616",
        },
        {
            "title": "Conditions générales de vente",
            "type": "SHOP_POLICY",
            "resourceId": "gid://shopify/ShopPolicy/50190975312",
        },
    ],
}

CREATE = """
mutation MenuCreate($title: String!, $handle: String!, $items: [MenuItemCreateInput!]!) {
  menuCreate(title: $title, handle: $handle, items: $items) {
    menu { id handle }
    userErrors { field message }
  }
}
"""

UPDATE = """
mutation MenuUpdate($id: ID!, $title: String!, $items: [MenuItemUpdateInput!]!) {
  menuUpdate(id: $id, title: $title, items: $items) {
    menu { id handle }
    userErrors { field message }
  }
}
"""


def _menus_by_handle() -> dict[str, dict]:
    data = gql(
        """
        query {
          menus(first: 50) {
            nodes { id handle title }
          }
        }
        """
    )
    return {m["handle"]: m for m in data["menus"]["nodes"]}


def _raise_errors(payload: dict, key: str) -> None:
    errors = (payload.get(key) or {}).get("userErrors") or []
    if errors:
        print(json.dumps(errors, indent=2, ensure_ascii=False))
        raise SystemExit(1)


def ensure_menu(spec: dict) -> str:
    existing = _menus_by_handle().get(spec["handle"])
    if existing:
        payload = gql(
            UPDATE,
            {
                "id": existing["id"],
                "title": spec["title"],
                "items": spec["items"],
            },
        )
        _raise_errors(payload, "menuUpdate")
        print("menu update", spec["handle"])
        return existing["id"]
    payload = gql(
        CREATE,
        {
            "title": spec["title"],
            "handle": spec["handle"],
            "items": spec["items"],
        },
    )
    _raise_errors(payload, "menuCreate")
    print("menu create", spec["handle"])
    return payload["menuCreate"]["menu"]["id"]


def patch_footer_json() -> None:
    data = theme_file("sections/footer-group.json")
    trust = data["sections"]["custom_section_k6mNHc"]
    trust["settings"]["color_scheme"] = "scheme-2"
    texts = {
        "text_6KXXtE": "<p>Livraison offerte</p>",
        "text_QCNw3n": (
            "<p>Partout en France métropolitaine, sans minimum. "
            "Comptez 1 à 2 jours de préparation, puis 6 à 15 jours d’acheminement.</p>"
        ),
        "text_EqDALK": "<p>Paiement sécurisé</p>",
        "text_GxU484": (
            "<p>La connexion est chiffrée en SSL et aucune donnée de carte n’est "
            "conservée chez nous.</p>"
        ),
        "text_7DApic": "<p>Retours 30 jours</p>",
        "text_ew3NP8": (
            "<p>La loi prévoit 14 jours, nous allons jusqu’à 30. Et aucun frais de "
            "réapprovisionnement.</p>"
        ),
        "text_V6AhLH": "<p>SAV humain</p>",
        "text_wDwwwK": SAV_TRUST_HTML,
    }
    for group in trust["blocks"].values():
        for bid, block in (group.get("blocks") or {}).items():
            if bid in texts:
                block["settings"]["text"] = texts[bid]

    footer = data["sections"]["footer"]
    footer["settings"]["color_scheme"] = "scheme-3"
    footer["settings"]["layout_type"] = "grid"
    footer["settings"]["layout_grid_columns_desktop"] = 4
    footer["settings"]["layout_gap_desktop"] = 30
    footer["settings"]["layout_gap_mobile"] = 40
    footer["settings"]["padding_top"] = 50
    footer["settings"]["padding_bottom"] = 0

    brand = footer["blocks"]["group_y4aNMX"]["blocks"]
    brand["text_hzJHEn"]["settings"]["text"] = BRAND_HTML
    if "social_icons_hQdtRf" in brand:
        brand["social_icons_hQdtRf"]["disabled"] = True

    footer["blocks"]["menu_K3tacq"]["settings"]["title"] = "<p>La boutique</p>"
    footer["blocks"]["menu_K3tacq"]["settings"]["title_style"] = "h6"
    footer["blocks"]["menu_K3tacq"]["settings"]["menu"] = "footer-principal"
    footer["blocks"]["menu_K3tacq"]["settings"]["alignment_desktop"] = "center"
    footer["blocks"]["menu_K3tacq"]["settings"]["alignment_mobile"] = "flex-start"

    footer["blocks"]["menu_rnCAbX"]["settings"]["title"] = "<p>Informations pratiques</p>"
    footer["blocks"]["menu_rnCAbX"]["settings"]["title_style"] = "h6"
    footer["blocks"]["menu_rnCAbX"]["settings"]["menu"] = "footer-informations"
    footer["blocks"]["menu_rnCAbX"]["settings"]["alignment_desktop"] = "center"
    footer["blocks"]["menu_rnCAbX"]["settings"]["alignment_mobile"] = "flex-start"

    footer["blocks"]["group_BxVQwU"]["blocks"]["text_RtFCiT"]["settings"]["text"] = (
        "<p>Recevoir nos e-mails</p>"
    )
    footer["blocks"]["group_BxVQwU"]["blocks"]["newsletter_signup_tUYiRB"]["settings"][
        "newsletter_label"
    ] = "Votre adresse e-mail"

    bottom = footer["blocks"]["footer-bottom-bar"]
    if "powered_by_fullstack_xErXcJ" in bottom.get("blocks", {}):
        bottom["blocks"]["powered_by_fullstack_xErXcJ"]["disabled"] = True

    upsert_theme_file("sections/footer-group.json", data)
    print("footer-group.json écrit")


def verify() -> None:
    data = theme_file("sections/footer-group.json")
    footer = data["sections"]["footer"]
    html = footer["blocks"]["group_y4aNMX"]["blocks"]["text_hzJHEn"]["settings"]["text"]
    sav = None
    for group in data["sections"]["custom_section_k6mNHc"]["blocks"].values():
        block = (group.get("blocks") or {}).get("text_wDwwwK")
        if block:
            sav = block["settings"]["text"]
    checks = {
        "mailto": f'mailto:{EMAIL}' in html,
        "tel": f'tel:{PHONE_TEL}' in html,
        "contact": f'href="{CONTACT_PATH}"' in html,
        "menu_principal": footer["blocks"]["menu_K3tacq"]["settings"]["menu"]
        == "footer-principal",
        "menu_infos": footer["blocks"]["menu_rnCAbX"]["settings"]["menu"]
        == "footer-informations",
        "4_cols": footer["settings"]["layout_grid_columns_desktop"] == 4,
        "social_off": footer["blocks"]["group_y4aNMX"]["blocks"]["social_icons_hQdtRf"].get(
            "disabled"
        )
        is True,
        "sav_mailto": sav is not None and f"mailto:{EMAIL}" in sav,
        "sav_tel": sav is not None and f"tel:{PHONE_TEL}" in sav,
    }
    print("verify", json.dumps(checks, ensure_ascii=False))
    if not all(checks.values()):
        raise SystemExit(1)


def main() -> None:
    ensure_menu(MENU_PRINCIPAL)
    ensure_menu(MENU_INFORMATIONS)
    patch_footer_json()
    verify()
    print("OK footer Montre Avenue — mailto/tel/Contact")


if __name__ == "__main__":
    main()
