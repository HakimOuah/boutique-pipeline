#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reconstruit sections/footer-group.json du theme Maison Noirmont (204248088914).
   variant='before' doit redonner md5 3d124046ef3f2115191fd6cbe38c84de (preuve
   que la reconstruction est exacte, donc que le backup est fidele).
   variant='after'  = pied de page transpose sur le modele Tufteo (5 colonnes)."""
import json, hashlib, sys
from collections import OrderedDict as OD

HEADER = (
    "/*\n"
    " * ------------------------------------------------------------\n"
    " * IMPORTANT: The contents of this file are auto-generated.\n"
    " *\n"
    " * This file may be updated by the Shopify admin theme editor\n"
    " * or related systems. Please exercise caution as any changes\n"
    " * made to this file may be overwritten.\n"
    " * ------------------------------------------------------------\n"
    " */\n"
)


def grp_settings(gap_d, align_d, same, gap_m, align_m, mt, mb):
    return OD([
        ("show_on_display", "desktop_and_mobile"),
        ("wrap_in_card", False),
        ("card_link", ""),
        ("color_scheme", ""),
        ("show_card_border", False),
        ("layout_type", "flex"),
        ("width_desktop", 100),
        ("layout_direction_desktop", "column"),
        ("layout_grid_columns_desktop", 3),
        ("layout_gap_desktop", gap_d),
        ("layout_wrap_desktop", "nowrap"),
        ("layout_justify_desktop", "flex-start"),
        ("layout_align_items_desktop", align_d),
        ("same_as_desktop", same),
        ("width_mobile", 100),
        ("layout_direction_mobile", "column"),
        ("layout_grid_columns_mobile", 1),
        ("layout_gap_mobile", gap_m),
        ("layout_wrap_mobile", "nowrap"),
        ("layout_justify_mobile", "flex-start"),
        ("layout_align_items_mobile", align_m),
        ("use_global_container_padding", True),
        ("padding_horizontal", 30),
        ("padding_vertical", 30),
        ("margin_top", mt),
        ("margin_bottom", mb),
        ("additional_class", ""),
    ])


def text_block(text, style, align, name="t:text"):
    return OD([
        ("type", "text"),
        ("name", name),
        ("settings", OD([
            ("show_on_display", "desktop_and_mobile"),
            ("text", text),
            ("text_style", style),
            ("paragraph_font_size", "normal"),
            ("font_weight", 400),
            ("alignment", align),
            ("alignment_mobile", align),
            ("show_read_more", False),
            ("read_more_length", 200),
            ("read_more_text", "Voir plus"),
            ("read_less_text", "Voir moins"),
            ("truncate", False),
            ("truncate_length", 2),
            ("margin_top", 0),
            ("margin_bottom", 0),
            ("additional_class", ""),
        ])),
        ("blocks", OD()),
    ])


def icon_block(icon):
    return OD([
        ("type", "icon"),
        ("name", "t:icon"),
        ("settings", OD([
            ("show_on_display", "desktop_and_mobile"),
            ("icon_type", "icon"),
            ("icon", icon),
            ("icon_custom", ""),
            ("icon_size", 42),
            ("margin_top", 0),
            ("margin_bottom", 0),
            ("additional_class", ""),
        ])),
        ("blocks", OD()),
    ])


def reassurance(gid, icon_id, icon, t1_id, t1, t2_id, t2):
    return (gid, OD([
        ("type", "group"),
        ("name", "t:group"),
        ("settings", grp_settings(5, "center", False, 10, "center", 10, 10)),
        ("blocks", OD([
            (icon_id, icon_block(icon)),
            (t1_id, text_block("<p>%s</p>" % t1, "h6", "center")),
            (t2_id, text_block("<p>%s</p>" % t2, "paragraph", "center")),
        ])),
        ("block_order", [icon_id, t1_id, t2_id]),
    ]))


def menu_block(title, menu):
    return OD([
        ("type", "menu"),
        ("name", "t:menu"),
        ("settings", OD([
            ("show_on_display", "desktop_and_mobile"),
            ("alignment_desktop", "center"),
            ("alignment_mobile", "flex-start"),
            ("title", "<h3>%s</h3>" % title),
            ("title_style", "h6"),
            ("menu", menu),
            ("menu_direction", "column"),
            ("underline_links", False),
            ("margin_top", 0),
            ("margin_bottom", 0),
            ("additional_class", ""),
        ])),
        ("blocks", OD()),
    ])


def build(variant):
    after = variant == "after"

    # ---- section Reassurances (inchangee) ----
    r_blocks = OD([
        reassurance("group_Xb8cmj", "icon_ecqj97", "delivery_truck_speed",
                    "text_6KXXtE", "Livraison offerte",
                    "text_QCNw3n", "En France métropolitaine, avec suivi. Comptez généralement 2 à 3 semaines après la commande."),
        reassurance("group_r6xr7P", "icon_UCtDLw", "encrypted",
                    "text_EqDALK", "Paiement sécurisé",
                    "text_GxU484", "Transactions chiffrées SSL, paiement en toute sécurité."),
        reassurance("group_wMEVzi", "icon_axd3UQ", "verified_user",
                    "text_7DApic", "Garantie 12 mois",
                    "text_ew3NP8", "Mouvement, couronne, aiguilles : on répare ou on remplace, simplement."),
        reassurance("group_x7TjnR", "icon_WcRhTN", "forum",
                    "text_V6AhLH", "Une question ?",
                    "text_wDwwwK", "Notre équipe vous répond en français, généralement sous 24 h ouvrées."),
    ])

    reassurances = OD([
        ("type", "custom-section"),
        ("blocks", r_blocks),
        ("block_order", ["group_Xb8cmj", "group_r6xr7P", "group_wMEVzi", "group_x7TjnR"]),
        ("name", "Réassurances"),
        ("settings", OD([
            ("show_on_display", "desktop_and_mobile"),
            ("color_scheme", "scheme-1"),
            ("wrap_in_card", False),
            ("color_scheme_card", ""),
            ("section_width", "normal"),
            ("layout_type", "grid"),
            ("layout_flex_direction_desktop", "row"),
            ("layout_grid_columns_desktop", 4),
            ("layout_gap_desktop", 30),
            ("layout_wrap_desktop", "nowrap"),
            ("layout_flex_justify_desktop", "flex-start"),
            ("layout_flex_align_items_desktop", "flex-start"),
            ("same_as_desktop", False),
            ("layout_flex_direction_mobile", "row"),
            ("layout_gap_mobile", 20),
            ("layout_wrap_mobile", "nowrap"),
            ("layout_flex_justify_mobile", "flex-start"),
            ("layout_flex_align_items_mobile", "flex-start"),
            ("layout_grid_columns_mobile", 2),
            ("padding_top", 50),
            ("padding_bottom", 50),
            ("margin_top", 0),
            ("margin_bottom", 0),
            ("anchor_id", ""),
            ("additional_class", ""),
        ])),
    ])

    # ---- colonne 1 : marque ----
    brand_text_before = ("<p>Maison Noirmont — des garde-temps au cadran épuré : "
                         "mécaniques automatiques, et chronographes méca-quartz. "
                         "Votre signature au poignet.</p>")
    brand_text_after = (brand_text_before +
                        "<p><a href=\"mailto:contact@maisonnoirmont.fr\">contact@maisonnoirmont.fr</a></p>")

    brand_group = OD([
        ("type", "group"),
        ("name", "t:group"),
        ("settings", grp_settings(20, "flex-start", True, 10, "flex-start", 0, 0)),
        ("blocks", OD([
            ("logo_MKbnJy", OD([
                ("type", "logo"),
                ("name", "t:logo"),
                ("settings", OD([
                    ("show_on_display", "desktop_and_mobile"),
                    ("logo_height", 32),
                    ("inverse", True),
                    ("activate_link", True),
                    ("margin_top", 0),
                    ("margin_bottom", 0),
                    ("additional_class", ""),
                ])),
                ("blocks", OD()),
            ])),
            ("text_hzJHEn", text_block(brand_text_after if after else brand_text_before,
                                       "paragraph", "left")),
            ("social_icons_hQdtRf", OD([
                ("type", "social-icons"),
                ("name", "t:social_icons"),
                ("settings", OD([
                    ("show_on_display", "desktop_and_mobile"),
                    ("icon_color", "#ffffff"),
                    ("icon_size", 24),
                    ("alignment", "flex-start"),
                    ("alignment_mobile", "flex-start"),
                    ("margin_top", 0),
                    ("margin_bottom", 0),
                    ("additional_class", ""),
                ])),
                ("blocks", OD()),
                ("disabled", True),
            ])),
        ])),
        ("block_order", ["logo_MKbnJy", "text_hzJHEn", "social_icons_hQdtRf"]),
    ])

    # ---- colonne 5 : infolettre ----
    nl_title_before = "<p>S'abonner à nos e-mails</p>"
    nl_title_after = "<p>Recevez nos nouveautés</p>"
    nl_group = OD([
        ("type", "group"),
        ("name", "t:group"),
        ("settings", grp_settings(10, "flex-start", True, 10, "flex-start", 0, 0)),
        ("blocks", OD([
            ("text_RtFCiT", text_block(nl_title_after if after else nl_title_before,
                                       "h6", "left", name="t:title")),
            ("newsletter_signup_tUYiRB", OD([
                ("type", "newsletter-signup"),
                ("name", "t:newsletter_signup"),
                ("settings", OD([
                    ("show_on_display", "desktop_and_mobile"),
                    ("newsletter_label", "Adresse email"),
                    ("tag", "newsletter"),
                    ("margin_top", 10),
                    ("margin_bottom", 0),
                    ("additional_class", ""),
                ])),
                ("blocks", OD()),
            ])),
        ])),
        ("block_order", ["text_RtFCiT", "newsletter_signup_tUYiRB"]),
    ])

    # ---- colonnes menus ----
    if after:
        m1 = menu_block("Boutique", "footer-boutique")
        m2 = menu_block("Informations", "footer-informations")
        m3 = menu_block("Légal", "footer-legal")
    else:
        m1 = menu_block("La Maison", "main-menu")
        m2 = menu_block("Informations", "footer")
        m3 = None

    f_blocks = OD()
    f_blocks["group_y4aNMX"] = brand_group
    f_blocks["menu_K3tacq"] = m1
    f_blocks["menu_rnCAbX"] = m2
    if m3 is not None:
        f_blocks["menu_uZq4Lg"] = m3
    f_blocks["group_BxVQwU"] = nl_group
    f_blocks["footer-policy-list"] = OD([
        ("type", "_footer-policy-list"),
        ("static", True),
        ("settings", OD([
            ("show_on_display", "desktop_and_mobile"),
            ("padding_top", 60),
            ("padding_bottom", 0),
            ("additional_class", ""),
        ])),
        ("blocks", OD()),
    ])
    f_blocks["footer-bottom-bar"] = OD([
        ("type", "_footer-bottom-bar"),
        ("static", True),
        ("settings", OD([
            ("show_top_border", False),
            ("layout_grid_columns_desktop", 3),
            ("layout_gap_desktop", 20),
            ("layout_gap_mobile", 20),
            ("layout_grid_columns_mobile", 1),
            ("padding_top", 20),
            ("padding_bottom", 20),
            ("margin_top", 0),
            ("additional_class", ""),
        ])),
        ("blocks", OD([
            ("payment_methods_W3BxcW", OD([
                ("type", "payment-methods"),
                ("name", "t:payment_methods"),
                ("settings", OD([
                    ("show_on_display", "desktop_and_mobile"),
                    ("alignment_desktop", "flex-start"),
                    ("alignment_mobile", "center"),
                    ("icon_size", 35),
                    ("margin_top", 10),
                    ("margin_bottom", 10),
                    ("additional_class", ""),
                ])),
                ("blocks", OD()),
            ])),
            ("copyright_AMhhCc", OD([
                ("type", "copyright"),
                ("name", "t:footer_copyright"),
                ("settings", OD([
                    ("alignment_desktop", "center"),
                    ("alignment_mobile", "center"),
                ])),
                ("blocks", OD()),
            ])),
            ("powered_by_fullstack_xErXcJ", OD([
                ("type", "powered-by-fullstack"),
                ("name", "t:powered_by_fullstack"),
                ("settings", OD([
                    ("show_on_display", "desktop_and_mobile"),
                    ("mode", "badge"),
                    ("alignment_desktop", "flex-end"),
                    ("alignment_mobile", "center"),
                    ("additional_class", ""),
                ])),
                ("blocks", OD()),
                ("disabled", True),
            ])),
        ])),
        ("block_order", ["payment_methods_W3BxcW", "copyright_AMhhCc",
                         "powered_by_fullstack_xErXcJ"]),
    ])

    order = ["group_y4aNMX", "menu_K3tacq", "menu_rnCAbX"]
    if after:
        order.append("menu_uZq4Lg")
    order.append("group_BxVQwU")

    footer = OD([
        ("type", "footer"),
        ("blocks", f_blocks),
        ("block_order", order),
        ("settings", OD([
            ("color_scheme", "scheme-3"),
            ("show_top_border", False),
            ("layout_type", "grid"),
            ("layout_direction_desktop", "row"),
            ("layout_grid_columns_desktop", 5 if after else 4),
            ("layout_gap_desktop", 30),
            ("layout_wrap_desktop", "nowrap"),
            ("layout_justify_desktop", "flex-start"),
            ("layout_align_items_desktop", "flex-start"),
            ("same_as_desktop", False),
            ("layout_direction_mobile", "column"),
            ("layout_grid_columns_mobile", 1),
            ("layout_gap_mobile", 40),
            ("layout_wrap_mobile", "nowrap"),
            ("layout_justify_mobile", "flex-start"),
            ("layout_align_items_mobile", "flex-start"),
            ("padding_top", 50),
            ("padding_bottom", 0),
            ("margin_top", 0),
        ])),
    ])

    doc = OD([
        ("type", "footer"),
        ("name", "t:footer"),
        ("sections", OD([("custom_section_k6mNHc", reassurances), ("footer", footer)])),
        ("order", ["custom_section_k6mNHc", "footer"]),
    ])

    return HEADER + json.dumps(doc, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    base = "/private/tmp/claude-502/-Users-Hakim-Documents-Boutiques-drop/455c6a31-511d-4d11-a937-711aeb4be1b5/scratchpad"
    for v, expect in (("before", "3d124046ef3f2115191fd6cbe38c84de"), ("after", None)):
        s = build(v)
        b = s.encode("utf-8")
        md5 = hashlib.md5(b).hexdigest()
        path = "%s/backup-footer/footer-group.%s.json" % (base, v)
        open(path, "w", encoding="utf-8").write(s)
        ok = "" if expect is None else ("  OK" if md5 == expect else "  !! MISMATCH (attendu %s)" % expect)
        print("%-7s bytes=%d md5=%s%s" % (v, len(b), md5, ok))
