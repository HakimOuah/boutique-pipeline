#!/usr/bin/env python3
"""Retire les démos GMC-dangereuses de la PDP Full Stack (faux avis, lorem, horaires faux)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from apply_fullstack import THEME_ID, theme_file, upsert_theme_file, BACKUP, HEADER  # noqa: E402
from client import gql  # noqa: E402

RETURN_HTML = (
    "<p>Rétractation légale 14 jours, étendue à 30 jours à compter de la réception. "
    "Aucun frais de réapprovisionnement. En cas de simple changement d’avis, les frais de retour "
    "sont à votre charge. Détail : politique de remboursement.</p>"
)
SHIP_HTML = (
    "<p>Livraison offerte en France métropolitaine. Préparation 1 à 2 jours ouvrés, "
    "acheminement 6 à 15 jours ouvrés, total 7 à 17 jours ouvrés. "
    "Heure limite 16h00, heure de Paris. Détail : politique d’expédition.</p>"
)
AMP_HTML = (
    "<p>LED intégrée ou douille E27 / E14 selon la variante — c’est indiqué sur la fiche. "
    "Si douille, prévoyez une LED blanc chaud. Coupure du courant avant toute pose ; "
    "faites appel à un électricien si vous n’êtes pas à l’aise.</p>"
)


def backup_product() -> None:
    BACKUP.mkdir(parents=True, exist_ok=True)
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
        {"id": THEME_ID, "names": ["templates/product.json"]},
    )
    nodes = data["theme"]["files"]["nodes"]
    if nodes:
        dest = BACKUP / "templates__product.json"
        dest.write_text(nodes[0]["body"]["content"])
        print("backup", dest)


def main() -> None:
    backup_product()
    data = theme_file("templates/product.json")
    main = data["sections"]["main"]
    if "rating_stars_Krck47" in main["blocks"]:
        main["blocks"]["rating_stars_Krck47"]["disabled"] = True
        main["blocks"]["rating_stars_Krck47"]["settings"]["hide_rating_when_no_reviews"] = True
        main["blocks"]["rating_stars_Krck47"]["settings"]["show_review_count"] = False
        main["blocks"]["rating_stars_Krck47"]["settings"]["review_count"] = 0

    acc = main["blocks"]["accordions_KKUaHK"]["blocks"]
    acc["accordion_mEqYBU"]["blocks"]["text_KyCgAW"]["settings"]["text"] = RETURN_HTML
    acc["accordion_gU7QYn"]["blocks"]["text_zgU7ap"]["settings"]["text"] = SHIP_HTML
    main["blocks"]["group_dddxG7"]["blocks"]["icon_with_text_Y6hka8"]["settings"]["text"] = (
        "<p>Livraison suivie</p>"
    )

    popup = main["blocks"]["product_form_grYQk6"]["blocks"]["product_variant_picker_xWC3wF"]["blocks"][
        "product-variant-popup"
    ]
    popup["disabled"] = True

    help_sec = data["sections"]["custom_section_LBJBG7"]
    help_sec["blocks"]["group_NkNJJg"]["blocks"]["text_FyFaMj"]["settings"]["text"] = (
        "<p>Notre équipe répond du lundi au vendredi, de 10h00 à 18h00 (heure de Paris), "
        "sous 24 heures ouvrées — contact@lumierematiere.fr · +33 7 56 82 80 94.</p>"
    )
    help_sec["blocks"]["group_NkNJJg"]["blocks"]["button_Q3UxFk"]["settings"]["label"] = "Nous écrire"
    help_sec["blocks"]["group_NkNJJg"]["blocks"]["button_Q3UxFk"]["settings"]["link"] = (
        "shopify://pages/contact"
    )
    help_sec["blocks"]["group_NkNJJg"]["blocks"]["button_qUpbgY"]["settings"]["label"] = "FAQ"
    help_sec["blocks"]["group_NkNJJg"]["blocks"]["button_qUpbgY"]["settings"]["link"] = (
        "shopify://pages/faq"
    )
    faqs = help_sec["blocks"]["group_ampbiX"]["blocks"]["accordions_JeK8VW"]["blocks"]
    faqs["accordion_wVm9bk"]["blocks"]["text_b36xbk"]["settings"]["text"] = RETURN_HTML
    faqs["accordion_FDaFgh"]["blocks"]["text_yarNag"]["settings"]["text"] = SHIP_HTML
    faqs["accordion_9NiJU7"]["settings"]["heading"] = "Ampoule et pose"
    faqs["accordion_9NiJU7"]["blocks"]["text_FP3XGi"]["settings"]["text"] = AMP_HTML
    faqs["accordion_ePJYyi"]["settings"]["heading"] = "Annulation"
    faqs["accordion_ePJYyi"]["blocks"]["text_nDYpUH"]["settings"]["text"] = (
        "<p>Tant que la commande n’est pas expédiée, vous pouvez demander son annulation par e-mail. "
        "Une fois partie, suivez la procédure de retour.</p>"
    )
    faqs["accordion_Y8Qaxp"]["settings"]["heading"] = "Matière"
    faqs["accordion_Y8Qaxp"]["blocks"]["text_mNHTMj"]["settings"]["text"] = (
        "<p>Nous décrivons la matière visible sur les photos (bambou, rotin, bois, pierre, verre, "
        "effet cristal). Pas d’atelier artisanal fictif, pas de cristal garanti si la pièce est un effet verre.</p>"
    )

    rec = data["sections"]["product_recommendations_G8mJVG"]
    stars = rec["blocks"]["product-card"]["blocks"]["product_card_group_EcgVgX"]["blocks"].get(
        "rating_stars_nz7WzY"
    )
    if stars:
        stars["disabled"] = True
        stars["settings"]["hide_rating_when_no_reviews"] = True
        stars["settings"]["show_review_count"] = False

    data["order"] = [
        "main",
        "custom_section_LBJBG7",
        "product_recommendations_G8mJVG",
    ]
    for leftover in list(data["sections"]):
        if leftover not in data["order"]:
            del data["sections"][leftover]
    upsert_theme_file("templates/product.json", data)
    print("OK PDP")


if __name__ == "__main__":
    main()
