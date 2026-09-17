import json
CUSTOM_CODE = {
    "type": "custom-code",
    "settings": {
        "show_on_display": "desktop_and_mobile",
        "custom_liquid": "",
        "margin_top": 0,
        "margin_bottom": 0,
        "additional_class": "",
    },
    "blocks": {},
}

RETURNS_HTML = (
    "<p>Vous avez 30 jours après réception pour renvoyer un luminaire, "
    "sans frais de remise en stock (14 jours de rétractation légale, étendus à 30). "
    "Écrivez à <a href=\"mailto:contact@lumierematiere.fr\">contact@lumierematiere.fr</a> : "
    "on vous indique comment procéder. Si vous changez simplement d’avis, "
    "les frais de retour restent à votre charge. Le remboursement part sous 7 jours "
    "après contrôle du colis.</p>"
)

SHIPPING_HTML = (
    "<p>Livraison offerte en France métropolitaine, Corse incluse, sans minimum. "
    "On prépare le colis en 1 à 2 jours ouvrés si la commande arrive avant 16h00, "
    "heure de Paris. L’acheminement prend 6 à 16 jours ouvrés, soit 7 à 18 jours "
    "au total. Le suivi part par e-mail dès l’expédition.</p>"
)


def custom_code(name: str, liquid: str, margin_bottom: int = 0) -> dict:
    block = json.loads(json.dumps(CUSTOM_CODE))
    block["name"] = name
    block["settings"]["custom_liquid"] = liquid
    block["settings"]["margin_bottom"] = margin_bottom
    return block


def patch_header(header: dict) -> None:
    header["blocks"] = {"banner_franco": custom_code("Bannière livraison", BANNER_LIQUID)}
    header["block_order"] = ["banner_franco"]


def patch_upsell(resume: dict, discount_id: str) -> None:
    discount = resume["blocks"][discount_id]
    resume["blocks"] = {
        discount_id: discount,
        "upsell_pieces": custom_code("Upsell pièces", UPSELL_LIQUID, margin_bottom=10),
    }
    resume["block_order"] = ["upsell_pieces", discount_id]


def patch_accordions(footer: dict) -> None:
    acc = footer["blocks"].get("accordions_UBXTAD")
    if not acc:
        return
    acc["blocks"]["accordion_eYqGh9"]["settings"]["heading"] = "Retours, 30 jours"
    acc["blocks"]["accordion_eYqGh9"]["blocks"]["text_9gnHYi"]["settings"]["text"] = RETURNS_HTML
    acc["blocks"]["accordion_dYtf9Y"]["settings"]["heading"] = "Livraison offerte en France"
    acc["blocks"]["accordion_dYtf9Y"]["blocks"]["text_jGApxp"]["settings"]["text"] = SHIPPING_HTML


def reco_section() -> dict:
    return {
        "type": "collection-featured",
        "blocks": {
            "lm_reco_header": {
                "type": "group",
                "name": "Titre",
                "settings": {
                    "wrap_in_card": False,
                    "color_scheme": "",
                    "width_desktop": 100,
                    "layout_direction_desktop": "row",
                    "layout_gap_desktop": 10,
                    "layout_wrap_desktop": "nowrap",
                    "layout_justify_desktop": "space-between",
                    "layout_align_items_desktop": "center",
                    "same_as_desktop": True,
                    "width_mobile": 100,
                    "layout_direction_mobile": "column",
                    "layout_gap_mobile": 10,
                    "layout_wrap_mobile": "nowrap",
                    "layout_justify_mobile": "flex-start",
                    "layout_align_items_mobile": "flex-start",
                    "margin_top": 10,
                    "margin_bottom": 30,
                },
                "blocks": {
                    "lm_reco_title": {
                        "type": "text",
                        "name": "Titre",
                        "settings": {
                            "text": "<p>Pour le salon</p>",
                            "text_style": "h3",
                            "font_weight": 400,
                            "alignment": "left",
                            "margin_top": 0,
                            "margin_bottom": 0,
                        },
                        "blocks": {},
                    },
                    "lm_reco_btn": {
                        "type": "button",
                        "name": "Bouton",
                        "settings": {
                            "link": "shopify://collections/suspensions-salon",
                            "open_in_new_tab": False,
                            "label": "Voir les suspensions salon",
                            "button_style": "secondary",
                            "button_shape": "small",
                            "icon": "arrow_forward",
                            "icon_custom": "",
                            "icon_position": "end",
                            "margin_top": 0,
                            "margin_bottom": 0,
                        },
                        "blocks": {},
                    },
                },
                "block_order": ["lm_reco_title", "lm_reco_btn"],
            },
            "product-card": {
                "type": "_product-card",
                "static": True,
                "settings": {
                    "wrap_in_card": False,
                    "color_scheme": "",
                    "layout_gap": 15,
                },
                "blocks": {
                    "lm_pc_gallery": {
                        "type": "_product-card-media-gallery",
                        "name": "Galerie",
                        "settings": {
                            "show_slider": False,
                            "media_rounded": True,
                            "media_ratio": "1 / 1",
                        },
                        "blocks": {},
                    },
                    "lm_pc_group": {
                        "type": "_product-card-group",
                        "name": "Infos",
                        "settings": {
                            "wrap_in_card": False,
                            "color_scheme": "",
                            "layout_direction_desktop": "column",
                            "layout_gap_desktop": 5,
                            "layout_wrap_desktop": "nowrap",
                            "layout_justify_desktop": "flex-start",
                            "layout_align_items_desktop": "flex-start",
                            "same_as_desktop": True,
                            "layout_direction_mobile": "column",
                            "layout_gap_mobile": 10,
                            "layout_wrap_mobile": "nowrap",
                            "layout_justify_mobile": "flex-start",
                            "layout_align_items_mobile": "flex-start",
                            "margin_top": 0,
                            "margin_bottom": 0,
                        },
                        "blocks": {
                            "lm_pc_title": {
                                "type": "text",
                                "name": "Titre",
                                "settings": {
                                    "text": "<h2>{{ closest.product.title }}</h2>",
                                    "text_style": "paragraph",
                                    "font_weight": 500,
                                    "alignment": "left",
                                    "margin_top": 0,
                                    "margin_bottom": 0,
                                },
                                "blocks": {},
                            },
                            "lm_pc_price": {
                                "type": "product-price",
                                "name": "Prix",
                                "settings": {
                                    "product": "{{ closest.product }}",
                                    "sales_badge": "amount",
                                    "show_sales_badge_text": False,
                                    "text_style": "paragraph",
                                },
                                "blocks": {},
                            },
                        },
                        "block_order": ["lm_pc_title", "lm_pc_price"],
                    },
                },
                "block_order": ["lm_pc_gallery", "lm_pc_group"],
            },
        },
        "block_order": ["lm_reco_header"],
        "settings": {
            "show_on_display": "desktop_and_mobile",
            "color_scheme": "scheme-1",
            "collection": "suspensions-salon",
            "max_products": 4,
            "layout_type": "grid",
            "grid_columns": 4,
            "grid_columns_mobile": "2",
            "padding_top": 30,
            "padding_bottom": 50,
            "margin_top": 0,
            "margin_bottom": 0,
            "anchor_id": "",
            "additional_class": "",
        },
    }


def assert_no_dashes(blob: str, label: str) -> None:
    if "—" in blob or "–" in blob:
        raise RuntimeError(f"{label}: cadratin restant")


def patch_cart_page(data: dict) -> dict:
    main = data["sections"]["main"]
    patch_header(main["blocks"]["cart_header_blocks"])
    patch_upsell(main["blocks"]["cart_footer_resume_blocks"], "discount_code_3WJdxK")
    patch_accordions(main["blocks"]["cart_footer_blocks"])
    data["sections"]["lm_reco"] = reco_section()
    if "lm_reco" not in data["order"]:
        data["order"] = ["main", "lm_reco"]
    return data


def patch_drawer(data: dict) -> dict:
    drawer = data["sections"]["cart-drawer"]
    patch_header(drawer["blocks"]["cart_header_blocks"])
    patch_upsell(drawer["blocks"]["cart_footer_resume_blocks"], "discount_code_GBacFY")
    pay = drawer["blocks"]["cart_footer_blocks"]["blocks"].get("payment_methods_WRBbVe")
    if pay:
        pay["settings"]["show_on_display"] = "desktop_and_mobile"
    return data


