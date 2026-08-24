#!/usr/bin/env python3
"""PDP Full Stack Lumière Matière : template Montre Avenue + données fiche par fiche."""
from __future__ import annotations

import json
import re
import sys
import time
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from apply_fullstack import THEME_ID, theme_file, upsert_theme_file  # noqa: E402
from build_pdp_copy import build_all  # noqa: E402
from client import gql  # noqa: E402

THEME_PDP = ROOT / "theme-pdp"
COPY_PATH = ROOT / "pdp-copy.json"
BRIEF_PATH = ROOT.parent / "briefs" / "2026-08-24-codex-variantes-couleur.md"
LIVRAISON_HTML = (
    "<p>Livraison offerte en France métropolitaine. Préparation <strong>1 à 2 jours ouvrés</strong>, "
    "acheminement <strong>6 à 15 jours ouvrés</strong>, total <strong>7 à 17 jours ouvrés</strong>. "
    "Heure limite : 16h00, heure de Paris.</p>"
    "<p><strong>Retour :</strong> rétractation légale 14 jours, étendue à 30 jours à compter de la réception. "
    "En cas de simple changement d’avis, les frais de retour sont à votre charge. "
    "Aucun frais de réapprovisionnement.</p>"
)
PREFERRED_WH = [
    "allemagne",
    "pologne",
    "france",
    "espagne",
    "tchéquie",
    "pays-bas",
    "belgique",
    "italie",
    "royaume-uni",
]
META_DEFS = [
    ("usps", "USP PDP", "list.single_line_text_field"),
    ("specs", "Caractéristiques PDP", "multi_line_text_field"),
    ("installation", "Installation PDP", "multi_line_text_field"),
    ("benefits", "Bénéfices PDP", "json"),
    ("faq", "FAQ PDP", "json"),
]
LABEL_RULES: list[tuple[str, str]] = [
    (r"—\s*—", "·"),
    (r"\bpi ce\b", "pièce"),
    (r"\b(\d+)\s*pcs\b", r"\1 pièce"),
    (r"\b1pcs\b", "1 pièce"),
    (r"Café frame", "Café"),
    (r"\bGloden\b", "Doré"),
    (r"5Rings", "5 anneaux"),
    (r"\bCeiling\b", "plafonnier"),
    (r"\bPendant Lamp\b", "suspension"),
    (r"\b[Pp]endant\b", "suspension"),
    (r"Light Jaune", "Blanc chaud"),
    (r"Netural Light", "Blanc neutre"),
    (r"3color", "3 teintes"),
    (r"^new\s+", ""),
    (r"\bWalnut\b", "Noyer"),
    (r"\bKhaki\b", "Kaki"),
    (r"\bHemp\b", "Chanvre"),
    (r"\bhead\b", "lumières"),
    (r"6 lights", ""),
    (r"5 lights", ""),
    (r"Lustre-Dia\d+cm\d*", ""),
    (r"Tissu D\d+cm", "Tissu"),
    (r"Blanc-Dia\d+cm", "Blanc"),
    (r"\(\d+rings[^)]*\)", ""),
    (r"Russian Federation", "Russie"),
    (r"\s*·\s*Chine\b", ""),
    (r"\s*·\s*Allemagne\b", ""),
    (r"\s*·\s*Royaume-Uni\b", ""),
    (r"\s*·\s*États-Unis\b", ""),
    (r"-A\s*\d*\b", ""),
    (r"-B\s*\d*\b", ""),
    (r"\bWOOD\b", "Bois"),
    (r"Ampoule non fournie\(E27\)", "Ampoule non fournie (E27)"),
    (r"Ampoule non fournie\(E27\)", "Ampoule non fournie (E27)"),
    (r"\s{2,}", " "),
]


def upsert_theme_text(filename: str, body: str) -> None:
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
        raise RuntimeError((filename, errs))
    print(f"  upsert {filename} ({len(body)} octets)")


def text_settings(html: str) -> dict:
    return {
        "show_on_display": "desktop_and_mobile",
        "text": html,
        "text_style": "paragraph",
        "paragraph_font_size": "normal",
        "font_weight": 400,
        "alignment": "left",
        "alignment_mobile": "left",
        "show_read_more": False,
        "read_more_length": 200,
        "read_more_text": "Voir plus",
        "read_less_text": "Voir moins",
        "truncate": False,
        "truncate_length": 2,
        "margin_top": 0,
        "margin_bottom": 0,
        "additional_class": "",
    }


def accordion(block_id: str, heading: str, source: str, open_default: bool = False) -> dict:
    text_id = f"body{block_id}"
    return {
        "type": "_accordion",
        "settings": {
            "show_on_display": "desktop_and_mobile",
            "heading": heading,
            "open_by_default": open_default,
            "icon": "none",
            "icon_custom": "",
            "additional_class": "",
        },
        "blocks": {
            text_id: {
                "type": "lm-meta-text",
                "settings": {
                    "show_on_display": "desktop_and_mobile",
                    "source": source,
                },
                "blocks": {},
            }
        },
        "block_order": [text_id],
    }


def patch_product_json() -> None:
    data = theme_file("templates/product.json")
    main = data["sections"]["main"]
    blocks = main["blocks"]
    if "rating_stars_Krck47" in blocks:
        blocks["rating_stars_Krck47"]["disabled"] = True
        blocks["rating_stars_Krck47"]["settings"]["hide_rating_when_no_reviews"] = True
    if "text_yQdqF8" in blocks:
        blocks["text_yQdqF8"]["disabled"] = True
    popup = (
        blocks.get("product_form_grYQk6", {})
        .get("blocks", {})
        .get("product_variant_picker_xWC3wF", {})
        .get("blocks", {})
        .get("product-variant-popup", {})
    )
    if popup:
        popup["disabled"] = True
        body = popup.get("blocks", {}).get("text_99rHbT", {}).get("settings")
        if body:
            body["text"] = (
                "<p>Au-dessus d’une table, visez un diamètre nettement plus étroit que le plateau. "
                "Les dimensions exactes sont sur chaque variante. Les photos compressent souvent l’échelle.</p>"
            )
    title = blocks["text_zLqMQw"]["settings"]
    title["text"] = "<h1>{{ closest.product.title }}</h1>"
    title["text_style"] = "h2"
    title["font_weight"] = 600
    blocks["lm_usp_pills"] = {
        "type": "lm-usp-pills",
        "name": "USP",
        "settings": {"show_on_display": "desktop_and_mobile"},
        "blocks": {},
    }
    blocks["accordions_KKUaHK"]["blocks"] = {
        "accdesc": accordion("accdesc", "Description", "description", False),
        "accspecs": accordion("accspecs", "Caractéristiques", "specs"),
        "accship": accordion("accship", "Livraison et retour", "shipping"),
        "accinstall": accordion("accinstall", "Installation", "installation"),
    }
    blocks["accordions_KKUaHK"]["block_order"] = ["accdesc", "accspecs", "accship", "accinstall"]
    trust = blocks["group_dddxG7"]["blocks"]["icon_with_text_Y6hka8"]["settings"]
    trust["text"] = "<p>Retours 30 jours</p>"
    trust["icon"] = "package"
    main["block_order"] = [
        "text_zLqMQw",
        "lm_usp_pills",
        "price_yEeMeb",
        "product_form_grYQk6",
        "payment_methods_BdjpFB",
        "accordions_KKUaHK",
        "group_dddxG7",
    ]
    data["sections"]["lm_pdp_benefits"] = {
        "type": "lm-pdp-benefits",
        "settings": {},
        "blocks": {},
    }
    data["sections"]["lm_pdp_faq"] = {
        "type": "lm-pdp-faq",
        "settings": {},
        "blocks": {},
    }
    data["sections"].pop("custom_section_LBJBG7", None)
    rec = data["sections"]["product_recommendations_G8mJVG"]
    rec["blocks"]["title"]["settings"]["text"] = "<p>Vous aimerez aussi</p>"
    data["order"] = ["main", "lm_pdp_benefits", "lm_pdp_faq", "product_recommendations_G8mJVG"]
    leftover = [k for k in data["sections"] if k not in data["order"]]
    for k in leftover:
        del data["sections"][k]
    upsert_theme_file("templates/product.json", data)


def ensure_metafield_defs() -> None:
    existing = gql(
        """
        query {
          metafieldDefinitions(first: 50, ownerType: PRODUCT, namespace: "custom") {
            nodes { key }
          }
        }
        """
    )
    have = {n["key"] for n in existing["metafieldDefinitions"]["nodes"]}
    for key, name, typ in META_DEFS:
        if key in have:
            continue
        data = gql(
            """
            mutation C($definition: MetafieldDefinitionInput!) {
              metafieldDefinitionCreate(definition: $definition) {
                createdDefinition { id key }
                userErrors { field message }
              }
            }
            """,
            {
                "definition": {
                    "name": name,
                    "namespace": "custom",
                    "key": key,
                    "description": "PDP Lumière Matière",
                    "type": typ,
                    "ownerType": "PRODUCT",
                    "access": {"storefront": "PUBLIC_READ"},
                }
            },
        )
        errs = data["metafieldDefinitionCreate"]["userErrors"]
        if errs:
            print("  warn metafield", key, errs)
        else:
            print("  def", key)
        time.sleep(0.1)


def fetch_products() -> list[dict]:
    nodes: list[dict] = []
    cursor = None
    while True:
        data = gql(
            """
            query ($c: String) {
              products(first: 40, after: $c, query: "status:active") {
                pageInfo { hasNextPage endCursor }
                nodes {
                  id handle title productType
                  featuredMedia { id }
                  media(first: 8) {
                    nodes { id alt ... on MediaImage { image { url } } }
                  }
                  options { id name optionValues { id name } }
                  variants(first: 100) {
                    pageInfo { hasNextPage }
                    nodes {
                      id title sku
                      selectedOptions { name value }
                      image { url }
                    }
                  }
                }
              }
            }
            """,
            {"c": cursor},
        )
        page = data["products"]
        for n in page["nodes"]:
            if n["variants"]["pageInfo"]["hasNextPage"]:
                n["variants"]["nodes"] = fetch_variants(n["id"])
            nodes.append(n)
        if not page["pageInfo"]["hasNextPage"]:
            return nodes
        cursor = page["pageInfo"]["endCursor"]


def fetch_variants(pid: str) -> list[dict]:
    cursor = None
    nodes: list[dict] = []
    while True:
        data = gql(
            """
            query ($id: ID!, $c: String) {
              product(id: $id) {
                variants(first: 100, after: $c) {
                  pageInfo { hasNextPage endCursor }
                  nodes {
                    id title sku
                    selectedOptions { name value }
                    image { url }
                  }
                }
              }
            }
            """,
            {"id": pid, "c": cursor},
        )
        conn = data["product"]["variants"]
        nodes.extend(conn["nodes"])
        if not conn["pageInfo"]["hasNextPage"]:
            return nodes
        cursor = conn["pageInfo"]["endCursor"]


def push_copy(products: list[dict], copies: dict) -> None:
    ok = 0
    for p in products:
        copy = copies.get(p["handle"])
        if not copy:
            print("  skip copy", p["handle"])
            continue
        metafields = [
            {
                "namespace": "custom",
                "key": "usps",
                "type": "list.single_line_text_field",
                "value": json.dumps(copy["usps"], ensure_ascii=False),
            },
            {
                "namespace": "custom",
                "key": "specs",
                "type": "multi_line_text_field",
                "value": copy["specs_html"],
            },
            {
                "namespace": "custom",
                "key": "installation",
                "type": "multi_line_text_field",
                "value": copy["installation_html"],
            },
            {
                "namespace": "custom",
                "key": "benefits",
                "type": "json",
                "value": json.dumps(copy["benefits"], ensure_ascii=False),
            },
            {
                "namespace": "custom",
                "key": "faq",
                "type": "json",
                "value": json.dumps(copy["faq"], ensure_ascii=False),
            },
        ]
        data = gql(
            """
            mutation U($input: ProductInput!) {
              productUpdate(input: $input) {
                product { id }
                userErrors { field message }
              }
            }
            """,
            {
                "input": {
                    "id": p["id"],
                    "title": copy["title"],
                    "descriptionHtml": copy["description_html"],
                    "seo": {
                        "title": copy["seo_title"][:70],
                        "description": copy["seo_description"][:320],
                    },
                    "metafields": metafields,
                }
            },
        )
        errs = data["productUpdate"]["userErrors"]
        if errs:
            print("FAIL copy", p["handle"], errs)
            continue
        ok += 1
        if ok % 20 == 0:
            print(f"  … {ok}")
        time.sleep(0.12)
    print(f"copy OK {ok}/{len(products)}")


def _fold(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


def clean_label(raw: str) -> str:
    s = raw.strip()
    for pat, repl in LABEL_RULES:
        s = re.sub(pat, repl, s, flags=re.I)
    s = re.sub(r"\s*·\s*$", "", s)
    s = re.sub(r"\s+", " ", s).strip(" ·,-")
    s = s.replace("( ", "(").replace(" )", ")")
    return s[:255] if s else raw.strip()[:255]


def uniquify_labels(pairs: list[tuple[str, str, str]]) -> list[tuple[str, str]]:
    seen: dict[str, str] = {}
    out: list[tuple[str, str]] = []
    for vid, new, old in pairs:
        name = new
        n = 2
        while name.lower() in {k.lower() for k in seen}:
            name = f"{new} · {n}"
            n += 1
        seen[name] = vid
        if name != old:
            out.append((vid, name))
    return out


def preferred_warehouse(values: list[str]) -> str | None:
    folded = [(_fold(v), v) for v in values]
    for pref in PREFERRED_WH:
        for f, orig in folded:
            if pref in f:
                return orig
    for f, orig in folded:
        if "chine" not in f and "china" not in f and "united states" not in f and "états-unis" not in f and "etats-unis" not in f:
            return orig
    return values[0] if values else None


def delete_option(pid: str, oid: str) -> None:
    data = gql(
        """
        mutation D($productId: ID!, $options: [ID!]!, $strategy: ProductOptionDeleteStrategy) {
          productOptionsDelete(productId: $productId, options: $options, strategy: $strategy) {
            userErrors { field message }
          }
        }
        """,
        {"productId": pid, "options": [oid], "strategy": "POSITION"},
    )
    errs = data["productOptionsDelete"]["userErrors"]
    if errs:
        print("  warn delete option", errs)


def delete_variants(pid: str, ids: list[str]) -> None:
    for i in range(0, len(ids), 50):
        chunk = ids[i : i + 50]
        data = gql(
            """
            mutation D($productId: ID!, $variantsIds: [ID!]!) {
              productVariantsBulkDelete(productId: $productId, variantsIds: $variantsIds) {
                userErrors { field message }
              }
            }
            """,
            {"productId": pid, "variantsIds": chunk},
        )
        errs = data["productVariantsBulkDelete"]["userErrors"]
        if errs:
            print("  warn delete variants", errs)
        time.sleep(0.15)


def update_option_values(pid: str, option_id: str, pairs: list[tuple[str, str]]) -> None:
    if not pairs:
        return
    data = gql(
        """
        mutation U($productId: ID!, $option: OptionUpdateInput!, $optionValuesToUpdate: [OptionValueUpdateInput!]) {
          productOptionUpdate(
            productId: $productId
            option: $option
            optionValuesToUpdate: $optionValuesToUpdate
          ) {
            userErrors { field message }
          }
        }
        """,
        {
            "productId": pid,
            "option": {"id": option_id},
            "optionValuesToUpdate": [{"id": vid, "name": name} for vid, name in pairs],
        },
    )
    errs = data["productOptionUpdate"]["userErrors"]
    if errs:
        print("  warn labels", errs)


def attach_variant_images(pid: str, variant_ids: list[str], media_id: str) -> None:
    for i in range(0, len(variant_ids), 25):
        chunk = variant_ids[i : i + 25]
        data = gql(
            """
            mutation A($productId: ID!, $variantMedia: [ProductVariantAppendMediaInput!]!) {
              productVariantAppendMedia(productId: $productId, variantMedia: $variantMedia) {
                userErrors { field message }
              }
            }
            """,
            {
                "productId": pid,
                "variantMedia": [{"variantId": vid, "mediaIds": [media_id]} for vid in chunk],
            },
        )
        errs = data["productVariantAppendMedia"]["userErrors"]
        if errs:
            print("  warn media", errs[:2])
        time.sleep(0.12)


def clean_variants(products: list[dict]) -> list[dict]:
    """Nettoie les libellés, retire l’entrepôt, attache une image. SKU DSers inchangés."""
    brief_rows = []
    for p in products:
        handle = p["handle"]
        opts = p["options"]
        variants = p["variants"]["nodes"]
        # Entrepôt standalone
        for opt in opts:
            if opt["name"] != "Entrepôt":
                continue
            names = [v["name"] for v in opt["optionValues"]]
            keep = preferred_warehouse(names)
            if keep and len(names) > 1:
                drop = [
                    v["id"]
                    for v in variants
                    if any(so["name"] == "Entrepôt" and so["value"] != keep for so in v["selectedOptions"])
                ]
                remaining = len(variants) - len(drop)
                if drop and remaining >= 1:
                    print(f"  {handle}: drop {len(drop)} variantes entrepôt, keep {keep}")
                    delete_variants(p["id"], drop)
                    variants = [v for v in variants if v["id"] not in set(drop)]
            if len(opts) > 1:
                delete_option(p["id"], opt["id"])
                print(f"  {handle}: option Entrepôt retirée")
            time.sleep(0.15)
        # Refresh options after warehouse delete? We still have original option value ids for other options.
        for opt in opts:
            if opt["name"] == "Entrepôt":
                continue
            pairs = [(v["id"], clean_label(v["name"]), v["name"]) for v in opt["optionValues"]]
            updates = uniquify_labels(pairs)
            if updates:
                update_option_values(p["id"], opt["id"], updates)
                time.sleep(0.12)
        media_id = None
        media_nodes = p.get("media", {}).get("nodes") or []
        if media_nodes:
            media_id = media_nodes[0]["id"]
        elif p.get("featuredMedia"):
            media_id = p["featuredMedia"]["id"]
        missing = [v["id"] for v in variants if not (v.get("image") or {}).get("url")]
        if media_id and missing:
            attach_variant_images(p["id"], missing, media_id)
        colors = []
        for opt in opts:
            if opt["name"] in {"Couleur", "Finition"}:
                colors = [v["name"] for v in opt["optionValues"]]
        real_colors = [c for c in colors if not re.fullmatch(r"[A-Z0-9_-]{3,}", c)]
        if len(set(c.lower() for c in real_colors)) >= 2:
            brief_rows.append(
                {
                    "handle": handle,
                    "title": p["title"],
                    "colors": colors,
                    "media": len(media_nodes),
                }
            )
    return brief_rows


def write_brief(rows: list[dict]) -> None:
    BRIEF_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Brief Codex — visuels de variantes couleur",
        "",
        "Boutique : **Lumière Matière** (`lumierematiere.fr`). Fond papier `#F6F3EC`, lumière chaude, packshot objet.",
        "Les fiches ont déjà 5 vues Codex (g1–g5) du modèle, **sans distinguo de couleur**. Les sélecteurs de variante n’ont donc rien de fidèle à afficher.",
        "",
        "## Demande",
        "",
        "Pour chaque SKU ci-dessous : **une image packshot par couleur / finition listée**, même cadrage que le g1 existant (objet centré, fond papier, allumé si le modèle est une source LED visible).",
        "Nom de fichier : `{handle}-{slug-couleur}-g1.jpg` (ex. `lustre-anneau-led-led-dore-418494-noir-g1.jpg`).",
        "Ne pas inventer une matière absente du modèle. Ne pas ajouter de texte incrusté.",
        "",
        "## Liste",
        "",
    ]
    for r in rows:
        cols = ", ".join(r["colors"])
        lines.append(f"- `{r['handle']}` — {r['title']} — couleurs : {cols} — médias actuels : {r['media']}")
    lines.append("")
    lines.append(f"{len(rows)} fiches. Une fois les JPEG livrés, les rattacher à la variante Shopify correspondante (SKU DSers inchangé).")
    BRIEF_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"brief {BRIEF_PATH} ({len(rows)} fiches)")


def main() -> None:
    skip_variants = "--skip-variants" in sys.argv
    print("— fichiers thème")
    mapping = {
        "assets/lm-pdp.css": THEME_PDP / "assets" / "lm-pdp.css",
        "blocks/lm-usp-pills.liquid": THEME_PDP / "blocks" / "lm-usp-pills.liquid",
        "blocks/lm-meta-text.liquid": THEME_PDP / "blocks" / "lm-meta-text.liquid",
        "sections/lm-pdp-benefits.liquid": THEME_PDP / "sections" / "lm-pdp-benefits.liquid",
        "sections/lm-pdp-faq.liquid": THEME_PDP / "sections" / "lm-pdp-faq.liquid",
    }
    for dest, src in mapping.items():
        upsert_theme_text(dest, src.read_text(encoding="utf-8"))
    print("— template product.json")
    patch_product_json()
    print("— métachamps")
    ensure_metafield_defs()
    print("— produits")
    products = fetch_products()
    rows = []
    for p in products:
        price = None
        rows.append(
            {
                "id": p["id"],
                "handle": p["handle"],
                "title": p["title"],
                "type": p["productType"],
                "price": price,
                "options": [
                    {"name": o["name"], "values": [v["name"] for v in o["optionValues"]]} for o in p["options"]
                ],
            }
        )
    copies = build_all(rows)
    COPY_PATH.write_text(json.dumps(copies, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"pdp-copy.json {len(copies)} fiches")
    print("— push titres / SEO / metafields")
    push_copy(products, copies)
    if skip_variants:
        print("— variantes ignorées")
        print("OK PDP")
        return
    print("— variantes")
    brief_rows = clean_variants(products)
    write_brief(brief_rows)
    print("OK PDP")


if __name__ == "__main__":
    main()
