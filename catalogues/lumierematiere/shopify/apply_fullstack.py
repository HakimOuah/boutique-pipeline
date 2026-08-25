#!/usr/bin/env python3
"""DA + UX Lumière Matière sur le thème Full Stack non publié « copie-de-fullstack-2-3 »."""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from client import gql  # noqa: E402
from import_catalogue import staged_upload  # noqa: E402

THEME_ID = "gid://shopify/OnlineStoreTheme/186708001104"
THEME_NAME = "copie-de-fullstack-2-3"
STATE = ROOT / "state.json"
BRAND = ROOT.parent / "livraisons-visuels-codex" / "brand"
BACKUP = ROOT / "backups" / "2026-08-24-fullstack-copy"
HEADER = (
    "/*\n * ------------------------------------------------------------\n"
    " * IMPORTANT: The contents of this file are auto-generated.\n *\n"
    " * This file may be updated by the Shopify admin theme editor\n"
    " * or related systems. Please exercise caution as any changes\n"
    " * made to this file may be overwritten.\n"
    " * ------------------------------------------------------------\n */\n"
)

PAPER = "#F6F3EC"
CHARCOAL = "#24211B"
AMBER = "#C08A2D"
WARM = "#EFE8DC"

FILES = [
    "config/settings_data.json",
    "templates/index.json",
    "sections/header-group.json",
    "sections/footer-group.json",
]


def theme_file(filename: str) -> dict:
    data = gql(
        """
        query ($id: ID!, $names: [String!]) {
          theme(id: $id) {
            files(filenames: $names) {
              nodes { filename body { ... on OnlineStoreThemeFileBodyText { content } } }
            }
          }
        }
        """,
        {"id": THEME_ID, "names": [filename]},
    )
    nodes = data["theme"]["files"]["nodes"]
    if not nodes:
        raise RuntimeError(f"missing {filename}")
    raw = nodes[0]["body"]["content"]
    raw = re.sub(r"/\*.*?\*/", "", raw, flags=re.S).strip()
    return json.loads(raw)


def upsert_theme_file(filename: str, data: dict) -> None:
    body = HEADER + json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    payload = gql(
        """
        mutation Upsert($themeId: ID!, $files: [OnlineStoreThemeFilesUpsertFileInput!]!) {
          themeFilesUpsert(themeId: $themeId, files: $files) {
            upsertedThemeFiles { filename }
            userErrors { field message }
          }
        }
        """,
        {
            "themeId": THEME_ID,
            "files": [{"filename": filename, "body": {"type": "TEXT", "value": body}}],
        },
    )
    errs = payload["themeFilesUpsert"]["userErrors"]
    if errs:
        raise RuntimeError(errs)
    print(f"  upsert {filename} ({len(body)} octets)")


def file_create(path: Path, alt: str) -> str:
    url = staged_upload(path, resource="FILE")
    data = gql(
        """
        mutation FileCreate($files: [FileCreateInput!]!) {
          fileCreate(files: $files) {
            files { id fileStatus ... on MediaImage { image { url } } }
            userErrors { field message }
          }
        }
        """,
        {
            "files": [
                {
                    "originalSource": url,
                    "contentType": "IMAGE",
                    "filename": path.name,
                    "alt": alt,
                    "duplicateResolutionMode": "REPLACE",
                }
            ]
        },
    )
    if data["fileCreate"]["userErrors"]:
        raise RuntimeError(data["fileCreate"]["userErrors"])
    fid = data["fileCreate"]["files"][0]["id"]
    for _ in range(20):
        q = gql(
            """
            query ($id: ID!) {
              node(id: $id) {
                ... on MediaImage { fileStatus image { url } }
              }
            }
            """,
            {"id": fid},
        )
        node = q["node"] or {}
        if node.get("fileStatus") == "READY":
            print(f"  file READY {path.name}")
            return f"shopify://shop_images/{path.name}"
        time.sleep(1.5)
    print(f"  file still processing {path.name}, using shopify:// anyway")
    return f"shopify://shop_images/{path.name}"


def backup() -> None:
    BACKUP.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        raw = gql(
            """
            query ($id: ID!, $names: [String!]) {
              theme(id: $id) {
                files(filenames: $names) {
                  nodes { filename body { ... on OnlineStoreThemeFileBodyText { content } } }
                }
              }
            }
            """,
            {"id": THEME_ID, "names": [name]},
        )
        nodes = raw["theme"]["files"]["nodes"]
        if not nodes:
            continue
        dest = BACKUP / name.replace("/", "__")
        dest.write_text(nodes[0]["body"]["content"])
        print(f"  backup {name} -> {dest}")


def scheme(bg: str, fg: str, *, dark: bool = False) -> dict:
    btn_bg = PAPER if dark else CHARCOAL
    btn_fg = CHARCOAL if dark else PAPER
    return {
        "settings": {
            "background": bg,
            "foreground": fg,
            "border": "#ffffff24" if dark else "#24211B17",
            "stars_icons_color": AMBER,
            "primary_button_background": btn_bg,
            "primary_button_text": btn_fg,
            "primary_button_border": btn_bg,
            "secondary_button_background": "rgba(0,0,0,0)" if dark else PAPER,
            "secondary_button_text": PAPER if dark else CHARCOAL,
            "secondary_button_border": PAPER if dark else "#24211B30",
            "primary_badge_background": PAPER if dark else PAPER,
            "primary_badge_text": CHARCOAL,
            "primary_badge_border": "#ffffff24" if dark else "#24211B17",
            "secondary_badge_background": AMBER,
            "secondary_badge_text": "#ffffff",
            "secondary_badge_border": AMBER,
            "input_background": "#3A342C" if dark else "#ffffff",
            "input_text_color": PAPER if dark else CHARCOAL,
            "input_border_color": "#ffffff24" if dark else "#24211B17",
            "selected_input_background": "#3A342C" if dark else "#ffffff",
            "selected_input_text_color": PAPER if dark else CHARCOAL,
            "selected_input_border_color": AMBER,
            "variant_background_color": "#3A342C" if dark else "#ffffff",
            "variant_text_color": PAPER if dark else CHARCOAL,
            "variant_border_color": "#ffffff24" if dark else "#24211B17",
            "selected_variant_background_color": CHARCOAL if not dark else AMBER,
            "selected_variant_text_color": PAPER,
            "selected_variant_border_color": CHARCOAL if not dark else AMBER,
            "tab_background_color": "#3A342C" if dark else "#ffffff",
            "tab_text_color": PAPER if dark else CHARCOAL,
            "tab_border_color": "#ffffff24" if dark else "#24211B17",
            "selected_tab_background_color": AMBER if dark else CHARCOAL,
            "selected_tab_text_color": PAPER,
            "selected_tab_border_color": AMBER if dark else CHARCOAL,
        }
    }


def patch_settings(logo: str, logo_inv: str, favicon: str) -> None:
    data = theme_file("config/settings_data.json")
    cur = data["current"]
    cur["logo"] = logo
    cur["logo_inverse"] = logo_inv
    cur["favicon"] = favicon
    cur["logo_height"] = 36
    cur["logo_height_mobile"] = 28
    cur["font_from"] = "shopify"
    cur["type_heading_font"] = "young_serif_n4"
    cur["type_subheading_font"] = "instrument_sans_n5"
    cur["type_body_font"] = "instrument_sans_n4"
    cur["type_primary_font"] = "instrument_sans_n4"
    cur["custom_type_heading_font"] = ""
    cur["show_advanced_font_settings"] = True
    cur["type_size_paragraph"] = "16"
    cur["type_size_paragraph_mobile"] = "16"
    cur["type_size_h1"] = "48"
    cur["type_size_h2"] = "36"
    cur["type_size_h3"] = "28"
    cur["button_border_radius"] = 8
    cur["button_secondary_border_radius"] = 8
    cur["badge_border_radius"] = 4
    cur["card_border_radius"] = 4
    cur["inputs_border_radius"] = 4
    cur["general_radius"] = "sligthly_rounded"
    cur["force_icons_display"] = False
    cur["show_shopify_pay"] = False
    cur["show_maestro"] = False
    cur["show_twint"] = False
    cur["show_bancontact"] = False
    cur["instagram_url"] = ""
    cur["klaviyo_enabled"] = False
    cur["klaviyo_api_key"] = ""
    cur["activate_wishlist"] = False
    cur["color_schemes"]["scheme-1"] = scheme(PAPER, CHARCOAL)
    cur["color_schemes"]["scheme-2"] = scheme(WARM, CHARCOAL)
    cur["color_schemes"]["scheme-3"] = scheme(CHARCOAL, PAPER, dark=True)
    upsert_theme_file("config/settings_data.json", data)


def patch_header() -> None:
    data = theme_file("sections/header-group.json")
    ann = data["sections"]["announcement_bar_r8QCCw"]
    ann["settings"]["color_scheme"] = "scheme-3"
    ann["blocks"]["announcement_y7tnxm"]["blocks"]["text_Lk3QUw"]["settings"]["text"] = (
        "<p>Livraison offerte en France métropolitaine — sans minimum</p>"
    )
    ann["blocks"]["announcement_VprFGF"]["blocks"]["text_ndz4fN"]["settings"]["text"] = (
        "<p>Retours sous 30 jours · Paiement sécurisé</p>"
    )
    # 3e slide démo « 3x / cadeau » : on le retire
    ann["block_order"] = ["announcement_y7tnxm", "announcement_VprFGF"]
    header = data["sections"]["header"]["settings"]
    header["color_scheme"] = "scheme-1"
    header["show_country"] = False
    header["show_language"] = False
    header["logo_height"] = 36
    header["logo_height_mobile"] = 28
    header["menu"] = "main-menu"
    upsert_theme_file("sections/header-group.json", data)


def patch_footer() -> None:
    data = theme_file("sections/footer-group.json")
    trust = data["sections"]["custom_section_k6mNHc"]
    trust["settings"]["color_scheme"] = "scheme-2"
    texts = {
        "text_6KXXtE": "<p>Livraison offerte</p>",
        "text_QCNw3n": "<p>France métropolitaine, sans minimum. Préparation 1 à 2 jours, acheminement 6 à 15 jours.</p>",
        "text_EqDALK": "<p>Paiement sécurisé</p>",
        "text_GxU484": "<p>Connexion chiffrée SSL. Aucune donnée de carte n’est stockée chez nous.</p>",
        "text_7DApic": "<p>Retours 30 jours</p>",
        "text_ew3NP8": "<p>14 jours légaux, étendus à 30 jours. Aucun frais de réapprovisionnement.</p>",
        "text_V6AhLH": "<p>SAV humain</p>",
        "text_wDwwwK": "<p>contact@lumierematiere.fr · lun–ven 10h–18h (Paris) · réponse sous 24 h ouvrées.</p>",
    }
    for group in trust["blocks"].values():
        for bid, block in (group.get("blocks") or {}).items():
            if bid in texts:
                block["settings"]["text"] = texts[bid]

    footer = data["sections"]["footer"]
    footer["settings"]["color_scheme"] = "scheme-3"
    footer["blocks"]["group_y4aNMX"]["blocks"]["text_hzJHEn"]["settings"]["text"] = (
        "<p>Lumière Matière<br>"
        "contact@lumierematiere.fr · +33 7 56 82 80 94<br>"
        "47 rue Vivienne, 75002 Paris<br>"
        "SAV lun–ven 10h–18h (heure de Paris)</p>"
    )
    footer["blocks"]["menu_K3tacq"]["settings"]["title"] = "<h3>Collections</h3>"
    footer["blocks"]["menu_K3tacq"]["settings"]["menu"] = "main-menu"
    footer["blocks"]["menu_rnCAbX"]["settings"]["title"] = "<h3>Infos</h3>"
    footer["blocks"]["menu_rnCAbX"]["settings"]["menu"] = "footer"
    footer["blocks"]["group_BxVQwU"]["blocks"]["text_RtFCiT"]["settings"]["text"] = (
        "<p>Nouvelles pièces, conseils de diamètre</p>"
    )
    bottom = footer["blocks"]["footer-bottom-bar"]
    if "powered_by_fullstack_xErXcJ" in bottom.get("blocks", {}):
        bottom["blocks"]["powered_by_fullstack_xErXcJ"]["disabled"] = True
    upsert_theme_file("sections/footer-group.json", data)


def collections_featured(
    section_id: str, title: str, handles: list[str], columns: int, subtitle: str = ""
) -> dict:
    section = {
        "type": "collections-featured",
        "blocks": {
            "title": {
                "type": "text",
                "name": "Titre",
                "settings": {
                    "text": f"<h2>{title}</h2>",
                    "text_style": "h3",
                    "font_weight": 400,
                    "alignment": "left",
                    "margin_top": 10,
                    "margin_bottom": 30,
                    "show_on_display": "desktop_and_mobile",
                    "paragraph_font_size": "normal",
                    "alignment_mobile": "left",
                    "show_read_more": False,
                    "truncate": False,
                },
                "blocks": {},
            },
            "collection-card": {
                "type": "_collection-card",
                "static": True,
                "settings": {
                    "wrap_in_card": False,
                    "color_scheme": "",
                    "layout_gap": 10,
                },
                "blocks": {
                    "image": {
                        "type": "image",
                        "settings": {
                            "image": "{{ closest.collection.image }}",
                            "link": "",
                            "image_ratio": "square",
                        },
                    },
                    "text": {
                        "type": "text",
                        "settings": {
                            "text": "<p>{{ closest.collection.title }}</p>",
                            "text_style": "paragraph",
                            "font_weight": 500,
                            "alignment": "left",
                            "margin_top": 0,
                            "margin_bottom": 0,
                        },
                    },
                },
                "block_order": ["image", "text"],
            },
        },
        "block_order": ["title"],
        "settings": {
            "show_on_display": "desktop_and_mobile",
            "color_scheme": "scheme-1",
            "collection_list": handles,
            "max_collections": len(handles),
            "layout_type": "grid",
            "grid_columns": columns,
            "grid_columns_mobile": "2",
            "padding_top": 48,
            "padding_bottom": 48,
            "margin_top": 0,
            "margin_bottom": 0,
            "anchor_id": section_id,
            "additional_class": "",
        },
    }
    if subtitle:
        section["blocks"]["subtitle"] = {
            "type": "text",
            "name": "Sous-titre",
            "settings": {
                "text": f"<p>{subtitle}</p>",
                "text_style": "paragraph",
                "font_weight": 400,
                "alignment": "left",
                "margin_top": 0,
                "margin_bottom": 20,
                "show_on_display": "desktop_and_mobile",
                "paragraph_font_size": "normal",
                "alignment_mobile": "left",
                "show_read_more": False,
                "truncate": False,
            },
            "blocks": {},
        }
        section["block_order"] = ["title", "subtitle"]
    return section


def patch_index(hero_image: str) -> None:
    data = theme_file("templates/index.json")
    hero_block = data["sections"]["image_banner_VXNP89"]["blocks"]["image_banner_dBEabG"]
    hero_block["settings"]["image"] = hero_image
    hero_block["settings"]["image_filter_color"] = CHARCOAL
    hero_block["settings"]["image_filter_opacity"] = 35
    hero_block["settings"]["color_scheme"] = "scheme-3"
    group = hero_block["blocks"]["group_nypGzr"]
    group["blocks"]["reviews_badge_efW9wU"]["disabled"] = True
    group["blocks"]["text_VJtMDF"]["settings"]["text"] = "<h1>Chaque matière a sa lumière</h1>"
    group["blocks"]["text_8GW6GA"]["settings"]["text"] = (
        "<p>Lumière Matière — galerie de matières. Suspensions et lustres choisis pour le bambou, "
        "le rotin, le bois, la pierre ou le verre. Le matériau change la lumière : commencez par l’ambiance.</p>"
    )
    btn = group["blocks"]["group_rFrEU8"]["blocks"]["button_JteLrC"]["settings"]
    btn["label"] = "Explorer les matières"
    btn["link"] = "shopify://collections/all"
    icons = group["blocks"]["group_3Pie6V"]["blocks"]
    icons["icon_with_text_MPKKCD"]["settings"]["text"] = "<p>Paiement sécurisé</p>"
    icons["icon_with_text_AdYCCm"]["settings"]["text"] = "<p>SAV lun–ven 10h–18h</p>"

    feat = data["sections"]["collection_featured_JXRpw3"]
    feat["settings"]["collection"] = "selection-199"
    feat["settings"]["max_products"] = 6
    feat["settings"]["color_scheme"] = "scheme-2"
    head = feat["blocks"]["group_9NwHBp"]["blocks"]["group_TwitGb"]["blocks"]
    head["text_QEHkGh"]["settings"]["text"] = "<h2>Autour de 199 €</h2>"
    head["text_6LANC3"]["settings"]["text"] = (
        "<p>Une sélection de suspensions et de lustres autour de 199 € — le prix le plus courant du catalogue.</p>"
    )

    editorial = data["sections"]["custom_section_k9aPjP"]
    editorial["settings"]["color_scheme"] = "scheme-1"
    ed_blocks = editorial["blocks"]["group_XyMggk"]["blocks"]
    ed_blocks["text_34dYXd"]["settings"]["text"] = "<h2>La matière fait la lumière</h2>"
    benefits = ed_blocks["group_6DLfAU"]["blocks"]["group_BhcLrP"]["blocks"]
    benefits["icon_with_text_DCkFpJ"]["settings"]["text"] = (
        "<p><strong>Matière visible</strong><br/>Bambou tissé, rotin, bois, pierre ou verre : "
        "la texture de la photo est celle qui joue avec la lumière chez vous.</p>"
    )
    benefits["icon_with_text_bFDMHJ"]["settings"]["text"] = (
        "<p><strong>L’échelle d’abord</strong><br/>Diamètre et hauteur de câble : les deux chiffres qui font tenir la pièce.</p>"
    )
    benefits["icon_with_text_D4CKhV"]["settings"]["text"] = (
        "<p><strong>Pose et SAV</strong><br/>Un humain au bout de l’e-mail, lun–ven 10h–18h (Paris).</p>"
    )
    ed_blocks["button_gNYHT8"]["settings"]["label"] = "Notre histoire"
    ed_blocks["button_gNYHT8"]["settings"]["link"] = "shopify://pages/notre-histoire"

    news = data["sections"]["custom_section_qetdex"]
    news["settings"]["color_scheme"] = "scheme-2"
    news["blocks"]["text_JqyRqD"]["settings"]["text"] = "<h3>Un e-mail de temps en temps</h3>"
    news["blocks"]["text_PkpXrD"]["settings"]["text"] = (
        "<p>Nouvelles pièces, conseils de diamètre et d’ampoule. Pas de remise tant qu’aucun code n’existe.</p>"
    )

    data["sections"]["collections_matieres"] = collections_featured(
        "collections_matieres",
        "Choisissez la matière, vous choisissez la lumière",
        [
            "suspensions-bambou",
            "suspensions-rotin",
            "suspensions-bois",
            "suspensions-pierre",
            "suspensions-verre",
            "lustres-effet-cristal",
        ],
        3,
        subtitle=(
            "Bambou, rotin, bois, pierre, verre ou effet cristal : six matières, "
            "six manières d’habiter la même pièce."
        ),
    )
    data["sections"]["collections_piece"] = collections_featured(
        "collections_piece",
        "Par pièce et par forme",
        ["lustres-anneau", "lustres-salon", "plafonniers"],
        3,
    )
    # Ordre de référence = celui de la home enrichie (patch_home.py, 25/08/2026).
    # Les sections lm_* n'existent que dans le index.json live : on les préserve
    # si elles y sont, sans les exiger sur un thème vierge.
    order = [
        "image_banner_VXNP89",
        "collections_matieres",
        "lm_benefices_piece",
        "collection_featured_JXRpw3",
        "lm_guide_choix",
        "collections_piece",
        "custom_section_k9aPjP",
        "lm_cta_final",
        "custom_section_qetdex",
    ]
    data["order"] = [sid for sid in order if sid in data["sections"]]
    for leftover in list(data["sections"]):
        if leftover not in data["order"]:
            del data["sections"][leftover]
    upsert_theme_file("templates/index.json", data)


def main() -> None:
    print("=== backup ===")
    backup()
    print("=== files ===")
    logo = file_create(BRAND / "lumierematiere-logo-primary-charbon.png", "Lumière Matière")
    logo_inv = file_create(BRAND / "lumierematiere-logo-inverse-blanc.png", "Lumière Matière")
    favicon = file_create(BRAND / "lumierematiere-favicon-512.png", "Lumière Matière")
    hero = file_create(BRAND / "lumierematiere-home-hero.jpg", "Suspension bambou allumée au-dessus d'une table")
    print("=== settings ===")
    patch_settings(logo, logo_inv, favicon)
    print("=== header ===")
    patch_header()
    print("=== footer ===")
    patch_footer()
    print("=== index ===")
    patch_index(hero)
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    state["theme_id"] = THEME_ID
    state["theme_name"] = THEME_NAME
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    print("OK theme", THEME_ID)


if __name__ == "__main__":
    main()
