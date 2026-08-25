#!/usr/bin/env python3
"""Home enrichie Lumière Matière (25/08/2026) — patch chirurgical de templates/index.json.

Rejouable : part du index.json live, ajoute/remplace les sections d'enrichissement,
ne touche ni au hero, ni aux grilles collections, ni à la sélection 199 €.
Ne PAS relancer apply_fullstack.py en entier (il réécraserait logos/settings) ;
son patch_index connaît désormais le même ordre de sections que ce script.
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from apply_fullstack import theme_file, upsert_theme_file  # noqa: E402

BACKUP = ROOT / "backups" / "2026-08-25-home-enrichie"

# Ordre final de la home — la version de référence.
HOME_ORDER = [
    "image_banner_VXNP89",      # hero « Chaque matière a sa lumière »
    "collections_matieres",     # grille 6 matières
    "lm_benefices_piece",       # NOUVEAU — bénéfices par pièce (job-to-be-done)
    "collection_featured_JXRpw3",  # Autour de 199 €
    "lm_guide_choix",           # NOUVEAU — bien choisir en 3 étapes
    "collections_piece",        # grille pièce / forme
    "custom_section_k9aPjP",    # édito « La matière fait la lumière »
    "lm_cta_final",             # NOUVEAU — CTA final + preuves vraies
    "custom_section_qetdex",    # newsletter
]


def text_block(html: str, *, style: str = "paragraph", align: str = "center",
               weight: int = 400, mt: int = 0, mb: int = 0) -> dict:
    return {
        "type": "text",
        "name": "t:text",
        "settings": {
            "show_on_display": "desktop_and_mobile",
            "text": html,
            "text_style": style,
            "paragraph_font_size": "normal",
            "font_weight": weight,
            "alignment": align,
            "alignment_mobile": align,
            "show_read_more": False,
            "read_more_length": 200,
            "read_more_text": "Voir plus",
            "read_less_text": "Voir moins",
            "truncate": False,
            "truncate_length": 2,
            "margin_top": mt,
            "margin_bottom": mb,
            "additional_class": "",
        },
        "blocks": {},
    }


def icon_text_block(icon: str, html: str) -> dict:
    """Icône SVG du thème au-dessus du texte (colonne desktop, rangée mobile)."""
    return {
        "type": "icon-with-text",
        "name": "t:icon_with_text",
        "settings": {
            "show_on_display": "desktop_and_mobile",
            "layout_direction_desktop": "column",
            "layout_gap_desktop": 5,
            "same_as_desktop": False,
            "layout_direction_mobile": "row",
            "layout_gap_mobile": 10,
            "icon_type": "icon",
            "icon": icon,
            "icon_custom": "",
            "icon_size": 32,
            "icon_position": "start",
            "text": html,
            "text_style": "paragraph",
            "font_weight": 500,
            "margin_top": 0,
            "margin_bottom": 0,
            "additional_class": "",
        },
        "blocks": {},
    }


def button_block(label: str, link: str, *, style: str = "primary", mt: int = 5) -> dict:
    return {
        "type": "button",
        "name": "t:button",
        "settings": {
            "show_on_display": "desktop_and_mobile",
            "link": link,
            "open_in_new_tab": False,
            "label": label,
            "button_style": style,
            "button_shape": "default",
            "icon": "none",
            "icon_custom": "arrow_forward",
            "icon_position": "end",
            "margin_top": mt,
            "margin_bottom": 0,
            "additional_class": "",
        },
        "blocks": {},
    }


def group_block(blocks: dict, order: list[str], *, direction: str = "column",
                width: int = 100, gap: int = 10, card: bool = False,
                scheme: str = "", justify: str = "flex-start",
                align: str = "flex-start", align_mobile: str = "flex-start",
                padding: int = 30) -> dict:
    return {
        "type": "group",
        "name": "t:group",
        "settings": {
            "show_on_display": "desktop_and_mobile",
            "wrap_in_card": card,
            "card_link": "",
            "color_scheme": scheme,
            "show_card_border": False,
            "layout_type": "flex",
            "width_desktop": width,
            "layout_direction_desktop": direction,
            "layout_grid_columns_desktop": 3,
            "layout_gap_desktop": gap,
            "layout_wrap_desktop": "nowrap",
            "layout_justify_desktop": justify,
            "layout_align_items_desktop": align,
            "same_as_desktop": False,
            "width_mobile": 100,
            "layout_direction_mobile": "column",
            "layout_grid_columns_mobile": 1,
            "layout_gap_mobile": 15,
            "layout_wrap_mobile": "nowrap",
            "layout_justify_mobile": "flex-start",
            "layout_align_items_mobile": align_mobile,
            "use_global_container_padding": True,
            "padding_horizontal": padding,
            "padding_vertical": padding,
            "margin_top": 0,
            "margin_bottom": 0,
            "additional_class": "",
        },
        "blocks": blocks,
        "block_order": order,
    }


def custom_section(anchor: str, scheme: str, blocks: dict, order: list[str]) -> dict:
    return {
        "type": "custom-section",
        "blocks": blocks,
        "block_order": order,
        "settings": {
            "show_on_display": "desktop_and_mobile",
            "color_scheme": scheme,
            "wrap_in_card": False,
            "color_scheme_card": "",
            "section_width": "normal",
            "layout_type": "flex",
            "layout_flex_direction_desktop": "column",
            "layout_grid_columns_desktop": 3,
            "layout_gap_desktop": 30,
            "layout_wrap_desktop": "nowrap",
            "layout_flex_justify_desktop": "flex-start",
            "layout_flex_align_items_desktop": "center",
            "same_as_desktop": False,
            "layout_flex_direction_mobile": "column",
            "layout_gap_mobile": 10,
            "layout_wrap_mobile": "nowrap",
            "layout_flex_justify_mobile": "flex-start",
            "layout_flex_align_items_mobile": "flex-start",
            "layout_grid_columns_mobile": 1,
            "padding_top": 50,
            "padding_bottom": 50,
            "margin_top": 0,
            "margin_bottom": 0,
            "anchor_id": anchor,
            "additional_class": "",
        },
    }


def carte(icon: str, html: str, cta_label: str, cta_link: str) -> dict:
    """Carte bénéfice : icône + texte + bouton secondaire vers la collection."""
    return group_block(
        {
            "contenu": icon_text_block(icon, html),
            "cta": button_block(cta_label, cta_link, style="secondary", mt=5),
        },
        ["contenu", "cta"],
        width=33, card=True, scheme="scheme-1", gap=10,
        justify="space-between",
    )


def section_benefices() -> dict:
    """Job-to-be-done : ce que la matière change selon l'endroit à éclairer."""
    cartes = group_block(
        {
            "carte_table": carte(
                "lightbulb",
                "<p><strong>Au-dessus de la table</strong><br/>Le bambou et le rotin tamisent "
                "la lumière et la posent sur le plateau : le reste de la pièce s’adoucit, "
                "les dîners s’attardent.</p>",
                "Voir les suspensions bambou", "shopify://collections/suspensions-bambou",
            ),
            "carte_salon": carte(
                "home",
                "<p><strong>Dans le salon</strong><br/>Un lustre anneau ou une pièce en bois "
                "donne un centre à la pièce : la lumière porte loin sans éblouir le canapé.</p>",
                "Voir les lustres salon", "shopify://collections/lustres-salon",
            ),
            "carte_plafond": carte(
                "architecture",
                "<p><strong>Sous un plafond bas</strong><br/>Un plafonnier ou du verre clair "
                "garde les volumes : de la clarté partout, sans rien qui pende trop bas.</p>",
                "Voir les plafonniers", "shopify://collections/plafonniers",
            ),
        },
        ["carte_table", "carte_salon", "carte_plafond"],
        direction="row", gap=20, align="stretch",
    )
    outer = group_block(
        {
            "titre": text_block("<h2>Ce que la matière change, pièce par pièce</h2>", style="h3"),
            "intro": text_block(
                "<p>Le même salon change du tout au tout selon ce qui diffuse la lumière. "
                "Partez de l’endroit à éclairer : la matière suit.</p>"
            ),
            "cartes": cartes,
        },
        ["titre", "intro", "cartes"],
        gap=15, align="center", align_mobile="flex-start",
    )
    return custom_section("lm-benefices", "scheme-2", {"group_principal": outer}, ["group_principal"])


def section_guide() -> dict:
    """Guide « bien choisir » en 3 étapes — rassure le particulier avant la fiche."""
    etapes = group_block(
        {
            "etape_matiere": text_block(
                "<p><strong>1 · La matière</strong><br/>C’est elle qui fait l’ambiance : "
                "fibres tissées pour une lumière chaude striée d’ombres, verre pour une "
                "clarté nette, pierre pour un halo dense et calme.</p>",
                align="left", weight=500,
            ),
            "etape_diametre": text_block(
                "<p><strong>2 · Le diamètre</strong><br/>Mesurez la table ou la zone à "
                "éclairer, puis choisissez nettement plus étroit que le plateau. Chaque "
                "fiche donne les dimensions exactes, pour acheter sans se tromper.</p>",
                align="left", weight=500,
            ),
            "etape_ampoule": text_block(
                "<p><strong>3 · L’ampoule</strong><br/>LED intégrée ou douille (E27, parfois "
                "E14) : chaque fiche le précise. S’il faut une ampoule, une LED blanc chaud "
                "donne la lumière la plus accueillante.</p>",
                align="left", weight=500,
            ),
        },
        ["etape_matiere", "etape_diametre", "etape_ampoule"],
        direction="row", gap=30, align="stretch",
    )
    outer = group_block(
        {
            "titre": text_block("<h2>Bien choisir, en trois étapes</h2>", style="h3"),
            "intro": text_block(
                "<p>Pas besoin d’être du métier : trois décisions suffisent, et la fiche "
                "produit donne les chiffres.</p>"
            ),
            "etapes": etapes,
            "cta": button_block("Toutes les réponses dans la FAQ", "shopify://pages/faq",
                                style="secondary", mt=10),
        },
        ["titre", "intro", "etapes", "cta"],
        gap=15, align="center", align_mobile="flex-start",
    )
    return custom_section("lm-guide-choix", "scheme-3", {"group_principal": outer}, ["group_principal"])


def section_cta_final() -> dict:
    """Dernier appel : preuves vraies (livraison, retours) + deux portes d'entrée."""
    boutons = group_block(
        {
            "cta_tout": button_block("Voir toutes les pièces", "shopify://collections/all",
                                     style="primary", mt=0),
            "cta_199": button_block("La sélection autour de 199 €",
                                    "shopify://collections/selection-199",
                                    style="secondary", mt=0),
        },
        ["cta_tout", "cta_199"],
        direction="row", gap=15, justify="center", align="center", align_mobile="center",
        padding=10,
    )
    outer = group_block(
        {
            "titre": text_block("<h2>Commencez par la matière</h2>", style="h3"),
            "texte": text_block(
                "<p>Livraison offerte en France métropolitaine, retours sous 30 jours : "
                "vous jugez la pièce chez vous, dans votre lumière.</p>"
            ),
            "boutons": boutons,
        },
        ["titre", "texte", "boutons"],
        gap=15, align="center", align_mobile="center",
    )
    return custom_section("lm-cta-final", "scheme-3", {"group_principal": outer}, ["group_principal"])


def main() -> None:
    data = theme_file("templates/index.json")

    BACKUP.mkdir(parents=True, exist_ok=True)
    avant = BACKUP / f"index-avant-{date.today().isoformat()}.json"
    avant.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(f"backup avant -> {avant}")

    # 1. Sous-titre de la grille matières (compréhension en 10 secondes).
    matieres = data["sections"]["collections_matieres"]
    if "subtitle" not in matieres["blocks"]:
        sub = text_block(
            "<p>Bambou, rotin, bois, pierre, verre ou effet cristal : six matières, "
            "six manières d’habiter la même pièce.</p>",
            align="left", mb=20,
        )
        matieres["blocks"]["subtitle"] = sub
        matieres["block_order"] = ["title", "subtitle"]

    # 2. Bloc défensif de l'édito remplacé par un bénéfice positif.
    benefices = (data["sections"]["custom_section_k9aPjP"]["blocks"]["group_XyMggk"]
                 ["blocks"]["group_6DLfAU"]["blocks"]["group_BhcLrP"]["blocks"])
    benefices["icon_with_text_DCkFpJ"]["settings"]["text"] = (
        "<p><strong>Matière visible</strong><br/>Bambou tissé, rotin, bois, pierre ou verre : "
        "la texture de la photo est celle qui joue avec la lumière chez vous.</p>"
    )

    # 3. La sélection 199 € passe en scheme-1 (le bénéfice pièce prend le fond chaud).
    data["sections"]["collection_featured_JXRpw3"]["settings"]["color_scheme"] = "scheme-1"

    # 4. Nouvelles sections.
    data["sections"]["lm_benefices_piece"] = section_benefices()
    data["sections"]["lm_guide_choix"] = section_guide()
    data["sections"]["lm_cta_final"] = section_cta_final()

    data["order"] = list(HOME_ORDER)
    for leftover in list(data["sections"]):
        if leftover not in data["order"]:
            del data["sections"][leftover]

    upsert_theme_file("templates/index.json", data)

    apres = BACKUP / f"index-apres-{date.today().isoformat()}.json"
    apres.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(f"copie versionnée -> {apres}")


if __name__ == "__main__":
    main()
