#!/usr/bin/env python3
"""Tokens DA + logos + copy header/footer/hero sur le thème UNIVERS non publié."""
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

THEME_ID = json.loads((ROOT / "state.json").read_text())["theme_id"]
BRAND = ROOT.parent / "livraisons-visuels-codex" / "brand"
HEADER = "/*\n * ------------------------------------------------------------\n * IMPORTANT: The contents of this file are auto-generated.\n *\n * This file may be updated by the Shopify admin theme editor\n * or related systems. Please exercise caution as any changes\n * made to this file may be overwritten.\n * ------------------------------------------------------------\n */\n"


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
    print(f"  upsert {filename}")


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
                ... on GenericFile { fileStatus }
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


def patch_settings(logo: str, logo_inv: str, favicon: str) -> None:
    data = theme_file("config/settings_data.json")
    cur = data["current"]
    cur["color_palette"] = {
        "background": "#F6F3EC",
        "foreground": "#24211B",
        "color1": "#24211B",
        "color2": "#DDD6C8",
    }
    cur["logo"] = logo
    cur["logo_inverse"] = logo_inv
    cur["favicon"] = favicon
    cur["logo_height"] = 36
    cur["logo_height_mobile"] = 28
    cur["page_width"] = "narrow"
    cur["badge_corner_radius"] = 4
    cur["button_border_radius_primary"] = 8
    cur["button_border_radius_secondary"] = 8
    cur["variant_button_radius"] = 8
    cur["popover_border_radius"] = 8
    cur["card_corner_radius"] = 4
    cur["inputs_border_radius"] = 4
    upsert_theme_file("config/settings_data.json", data)


def patch_header() -> None:
    data = theme_file("sections/header-group.json")
    ann = data["sections"]["header_announcements_9jGBFp"]
    ann["blocks"] = {
        "ann_livraison": {
            "type": "_announcement",
            "settings": {
                "text": "Livraison offerte en France métropolitaine — sans minimum",
                "font": "var(--font-subheading--family)",
                "font_size": "0.75rem",
                "letter_spacing": "normal",
                "case": "none",
            },
            "blocks": {},
        },
        "ann_retours": {
            "type": "_announcement",
            "settings": {
                "text": "Retours sous 30 jours · Paiement sécurisé",
                "font": "var(--font-subheading--family)",
                "font_size": "0.75rem",
                "letter_spacing": "normal",
                "case": "none",
            },
            "blocks": {},
        },
    }
    ann["block_order"] = ["ann_livraison", "ann_retours"]
    ann["settings"]["background_color"] = "#24211B"
    header = data["sections"]["header_section"]["settings"]
    header["show_country"] = False
    header["show_language"] = False
    upsert_theme_file("sections/header-group.json", data)


def patch_footer() -> None:
    data = theme_file("sections/footer-group.json")
    footer = data["sections"]["footer_m9NzUG"]
    footer["blocks"]["group_H6VpwJ"]["blocks"]["text_LWt8Pz"]["settings"]["text"] = (
        "<h2>La lumière, matière par matière</h2>"
    )
    footer["blocks"]["group_H6VpwJ"]["blocks"]["text_f9CFLH"]["settings"]["text"] = (
        "<p>Un e-mail de temps en temps : nouvelles pièces, conseils de diamètre et d'ampoule. Rien de plus.</p>"
        "<p>Lumière Matière — une marque OH Ventures · contact@lumierematiere.fr · +33 7 56 82 80 94<br>"
        "47 rue Vivienne, 75002 Paris · SAV lun–ven 10h–18h (Paris)<br>"
        "OH Ventures, SASU au capital de 1 000 € — SIRET 10315725100010 — TVA FR55103157251</p>"
    )
    footer["settings"]["background_color"] = "#24211B"
    util = data["sections"]["footer_utilities_jLGE8U"]
    util["blocks"]["footer_copyright_jweRK8"]["settings"]["show_powered_by"] = False
    util["blocks"]["social_links_Ew63Kq"]["settings"] = {
        "facebook_url": "",
        "instagram_url": "",
        "youtube_url": "",
        "tiktok_url": "",
        "twitter_url": "",
    }
    util["settings"]["background_color"] = "#24211B"
    upsert_theme_file("sections/footer-group.json", data)


def collection_list_section(section_id: str, title: str, handles: list[str], columns: int) -> dict:
    return {
        "type": "collection-list",
        "blocks": {
            "group_head": {
                "type": "group",
                "name": "header",
                "settings": {
                    "content_direction": "column",
                    "vertical_on_mobile": True,
                    "horizontal_alignment": "flex-start",
                    "vertical_alignment": "center",
                    "horizontal_alignment_flex_direction_column": "flex-start",
                    "vertical_alignment_flex_direction_column": "center",
                    "gap": 12,
                    "width": "fill",
                    "custom_width": 100,
                    "width_mobile": "fill",
                    "custom_width_mobile": 100,
                    "height": "fit",
                    "custom_height": 100,
                    "background_media": "none",
                    "video_position": "cover",
                    "background_image_position": "cover",
                    "border": "none",
                    "border_width": 1,
                    "border_opacity": 100,
                    "border_radius": 0,
                    "padding-block-start": 0,
                    "padding-block-end": 0,
                    "padding-inline-start": 0,
                    "padding-inline-end": 0,
                },
                "blocks": {
                    "title": {
                        "type": "text",
                        "settings": {
                            "text": f"<h2>{title}</h2>",
                            "type_preset": "h3",
                            "font": "var(--font-heading--family)",
                            "font_size": "1rem",
                            "line_height": "normal",
                            "letter_spacing": "normal",
                            "case": "none",
                            "wrap": "pretty",
                            "width": "fit-content",
                            "max_width": "normal",
                            "alignment": "left",
                            "padding-block-start": 0,
                            "padding-block-end": 16,
                            "padding-inline-start": 0,
                            "padding-inline-end": 0,
                        },
                    }
                },
                "block_order": ["title"],
            },
            "static-collection-card": {
                "type": "_collection-card",
                "static": True,
                "settings": {
                    "horizontal_alignment": "flex-start",
                    "vertical_alignment": "flex-end",
                    "placement": "on_image",
                    "border": "none",
                    "border_width": 1,
                    "border_opacity": 100,
                    "border_radius": 0,
                },
                "blocks": {
                    "collection-card-image": {
                        "type": "_collection-card-image",
                        "static": True,
                        "settings": {"image_ratio": "adapt"},
                    },
                    "collection-title": {
                        "type": "collection-title",
                        "settings": {
                            "type_preset": "h5",
                            "font": "var(--font-heading--family)",
                            "font_size": "",
                            "line_height": "normal",
                            "letter_spacing": "normal",
                            "case": "none",
                            "wrap": "pretty",
                            "width": "fit-content",
                            "max_width": "normal",
                            "alignment": "left",
                            "background": True,
                            "background_color": "#F6F3EC",
                            "padding-block-start": 4,
                            "padding-block-end": 4,
                            "padding-inline-start": 8,
                            "padding-inline-end": 8,
                        },
                    },
                },
                "block_order": ["collection-title"],
            },
        },
        "block_order": ["group_head"],
        "settings": {
            "collection_list": handles,
            "layout_type": "grid",
            "carousel_on_mobile": True,
            "columns": columns,
            "mobile_columns": "2",
            "max_collections": len(handles),
            "section_width": "page-width",
            "padding-block-start": 48,
            "padding-block-end": 48,
        },
    }


def patch_index(hero_image: str) -> None:
    data = theme_file("templates/index.json")
    hero = data["sections"]["hero_jVaWmY"]
    hero["settings"]["image_1"] = hero_image
    hero["settings"]["overlay_color"] = "#24211B40"
    hero["blocks"]["text_YLPk4p"]["settings"]["text"] = (
        "<p>Lumière Matière — galerie de matières</p><h1>Chaque matière a sa lumière</h1>"
        "<p>Suspensions et lustres choisis pour leur matière : bambou, rotin, bois, pierre, verre. "
        "Le matériau change la lumière — choisissez d'abord l'ambiance.</p>"
    )
    hero["blocks"]["text_YLPk4p"]["settings"]["type_preset"] = "h1"
    hero["blocks"]["button_H9gpTf"]["settings"]["label"] = "Explorer les matières"
    hero["blocks"]["button_H9gpTf"]["settings"]["link"] = "shopify://collections/all"
    plist = data["sections"]["product_list_fa6P9H"]
    plist["settings"]["collection"] = "selection-199"
    plist["settings"]["max_products"] = 6
    plist["settings"]["background_color"] = "#EFE8DC"
    plist["blocks"]["static-header"]["blocks"]["product_list_text_YFtzcL"]["settings"]["text"] = (
        "<h2>Autour de 199 €</h2>"
    )
    plist["blocks"]["static-header"]["blocks"]["product_list_button_MWeP9V"]["settings"]["label"] = "Tout voir"
    data["sections"]["collections_matieres"] = collection_list_section(
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
    )
    data["sections"]["collections_piece"] = collection_list_section(
        "collections_piece",
        "Par pièce et par forme",
        ["lustres-anneau", "lustres-salon", "plafonniers"],
        3,
    )
    data["order"] = [
        "hero_jVaWmY",
        "collections_matieres",
        "product_list_fa6P9H",
        "collections_piece",
    ]
    upsert_theme_file("templates/index.json", data)


def main() -> None:
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
    print("OK theme", THEME_ID)


if __name__ == "__main__":
    main()
