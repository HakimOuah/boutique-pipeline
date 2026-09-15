"""Homepage Bercelou (Veille douce) built on the FullStack copy index.json structure."""
import json, copy

t = open("index.json").read()
j = json.loads(t[t.index("{"):])
S = j["sections"]
IMG = lambda f: f"shopify://shop_images/{f}"


def text_block(html, style="paragraph", align="left", align_m="left", weight=400, size="normal", mt=0, mb=0):
    return {"type": "text", "name": "t:text", "settings": {
        "show_on_display": "desktop_and_mobile", "text": html, "text_style": style, "paragraph_font_size": size,
        "font_weight": weight, "alignment": align, "alignment_mobile": align_m, "show_read_more": False,
        "read_more_length": 200, "read_more_text": "Voir plus", "read_less_text": "Voir moins", "truncate": False,
        "truncate_length": 2, "margin_top": mt, "margin_bottom": mb, "additional_class": ""}, "blocks": {}}


def button_block(label, link, style="primary", icon_custom="arrow_forward", shape="default"):
    return {"type": "button", "name": "t:button", "settings": {
        "show_on_display": "desktop_and_mobile", "link": link, "open_in_new_tab": False, "label": label,
        "button_style": style, "button_shape": shape, "icon": "none", "icon_custom": icon_custom,
        "icon_position": "end", "margin_top": 0, "margin_bottom": 0, "additional_class": ""}, "blocks": {}}


def group_block(blocks, name="t:group", **kw):
    s = {"show_on_display": "desktop_and_mobile", "wrap_in_card": False, "card_link": "", "color_scheme": "",
         "show_card_border": False, "layout_type": "flex", "width_desktop": 100, "layout_direction_desktop": "column",
         "layout_grid_columns_desktop": 3, "layout_gap_desktop": 10, "layout_wrap_desktop": "nowrap",
         "layout_justify_desktop": "flex-start", "layout_align_items_desktop": "flex-start", "same_as_desktop": True,
         "width_mobile": 100, "layout_direction_mobile": "column", "layout_grid_columns_mobile": 1,
         "layout_gap_mobile": 10, "layout_wrap_mobile": "nowrap", "layout_justify_mobile": "flex-start",
         "layout_align_items_mobile": "flex-start", "use_global_container_padding": True, "padding_horizontal": 10,
         "padding_vertical": 10, "margin_top": 0, "margin_bottom": 0, "additional_class": ""}
    s.update(kw)
    return {"type": "group", "name": name, "settings": s, "blocks": dict(blocks), "block_order": [k for k, _ in blocks]}


def icon_text(icon, html, direction_d="row", direction_m="row", size=24, weight=500):
    return {"type": "icon-with-text", "name": "t:icon_with_text", "settings": {
        "show_on_display": "desktop_and_mobile", "layout_direction_desktop": direction_d, "layout_gap_desktop": 10,
        "same_as_desktop": direction_d == direction_m, "layout_direction_mobile": direction_m, "layout_gap_mobile": 10,
        "icon_type": "icon", "icon": "none", "icon_custom": icon, "icon_size": size, "icon_position": "start",
        "text": html, "text_style": "paragraph", "font_weight": weight, "margin_top": 0, "margin_bottom": 0,
        "additional_class": ""}, "blocks": {}}


def section(blocks, name, scheme="scheme-1", pt=60, pb=60, **kw):
    s = copy.deepcopy(S["custom_section_k9aPjP"]["settings"])
    s.update({"color_scheme": scheme, "layout_type": "flex", "layout_flex_direction_desktop": "column",
              "layout_flex_align_items_desktop": "flex-start", "layout_flex_direction_mobile": "column",
              "layout_gap_desktop": 20, "layout_gap_mobile": 20, "padding_top": pt, "padding_bottom": pb})
    s.update(kw)
    return {"type": "custom-section", "blocks": dict(blocks), "block_order": [k for k, _ in blocks], "name": name, "settings": s}


# ---------- 1. Hero ----------
hero = S["image_banner_VXNP89"]
hb = hero["blocks"]["image_banner_dBEabG"]
hb["settings"].update({"image": IMG("bercelou-hero.jpg"), "image_mobile": IMG("accueil-moment-tetees-nuit-carte.jpg"),
                       "color_scheme": "scheme-3", "banner_height": "large", "banner_height_mobile": "large",
                       "layout_justify": "center", "layout_align_items": "flex-start", "same_as_desktop": False,
                       "layout_justify_mobile": "flex-end", "layout_align_items_mobile": "flex-start",
                       "image_filter_opacity": 35, "image_filter_color": "#141C28", "padding_vertical": 50})
B = hb["blocks"]["group_nypGzr"]["blocks"]
B["reviews_badge_efW9wU"]["disabled"] = True  # badge avis de démo : masqué, pas supprimé (chasse gardée Hakim)
B["group_wibFDH"]["disabled"] = True          # étoiles + « 2 000 clients satisfaits » de démo : masqués
B["text_VJtMDF"]["settings"]["text"] = "<h1>Le fauteuil des vraies nuits, et de tout ce qui vient après</h1>"
B["text_8GW6GA"]["settings"]["text"] = ("<p>Vous vous installez, vous bercez bébé en douceur, vous vous relevez sans le réveiller. "
                                        "Ensuite, le fauteuil reste là où il est beau : dans votre salon.</p>")
g = B["group_rFrEU8"]["blocks"]["button_JteLrC"]["settings"]
g.update({"label": "Trouver mon fauteuil", "link": "shopify://collections/fauteuil-a-bascule", "icon": "none", "icon_custom": "arrow_forward", "icon_position": "end"})
proofs = B["group_3Pie6V"]
base_iwt = copy.deepcopy(proofs["blocks"]["icon_with_text_MPKKCD"])
items = [("icon_with_text_MPKKCD", "local_shipping", "<p>Livraison offerte en France métropolitaine</p>"),
         ("icon_with_text_AdYCCm", "menu_book", "<p>Guide pour bien choisir offert en ligne</p>"),
         ("icon_with_text_pay3x4x", "credit_card", "<p>Paiement en 3 ou 4 fois</p>")]
proofs["blocks"] = {}
for k, icon, html in items:
    b = copy.deepcopy(base_iwt)
    b["settings"].update({"icon": "none", "icon_custom": icon, "text": html})
    proofs["blocks"][k] = b
proofs["block_order"] = [k for k, _, _ in items]

# ---------- 2. Moments ----------
def moment(key, img, title, sub, link):
    return (key, {"type": "image-card", "name": "t:image_card", "settings": {
        "show_on_display": "desktop_and_mobile", "color_scheme": "scheme-3", "image": IMG(img), "card_height": "medium",
        "card_link": link, "image_filter_opacity": 30, "image_filter_color": "#141C28", "layout_justify": "flex-end",
        "layout_align_items": "flex-start", "padding_horizontal": 20, "padding_vertical": 20, "margin_top": 0,
        "margin_bottom": 0, "additional_class": ""},
        "blocks": {key + "_t": text_block(f"<p><strong>{title}</strong></p>", style="h5"),
                   key + "_s": text_block(f"<p>{sub}</p>", size="small")},
        "block_order": [key + "_t", key + "_s"]})

moments = section([
    ("moments_head", group_block([
        ("moments_h2", text_block("<h2>Trouver le fauteuil qui vous ressemble</h2>", style="h2")),
        ("moments_p", text_block("<p>Quatre façons de commencer, selon le moment de vie que vous voulez accompagner.</p>")),
    ])),
    ("moments_grid", group_block([
        moment("m_nuit", "accueil-moment-tetees-nuit-carte.jpg", "Pour les tétées de nuit", "Fauteuils d'allaitement", "shopify://collections/fauteuil-allaitement"),
        moment("m_lecture", "accueil-moment-coin-lecture-carte.jpg", "Pour le coin lecture", "Design et scandinave", "shopify://collections/rocking-chair-design-scandinave"),
        moment("m_detente", "accueil-moment-detente-carte.jpg", "Pour se détendre", "Fauteuils relax", "shopify://collections/fauteuil-relax"),
        moment("m_terrasse", "accueil-moment-terrasse-carte.jpg", "Pour la terrasse", "Rocking chair extérieur", "shopify://collections/rocking-chair-exterieur"),
    ], layout_type="grid", layout_grid_columns_desktop=4, layout_grid_columns_mobile=2, layout_gap_desktop=20,
       layout_gap_mobile=10, same_as_desktop=False)),
], "Moments", scheme="scheme-1", pt=60, pb=40, anchor_id="moments")

# ---------- 3. Critères ----------
crit = S["custom_section_k9aPjP"]
crit["name"] = "Critères"
crit["settings"].update({"color_scheme": "scheme-1", "padding_top": 40, "padding_bottom": 60,
                         "layout_flex_align_items_desktop": "center"})
cg = crit["blocks"]["group_XyMggk"]
cg["settings"].update({"color_scheme": "scheme-2", "wrap_in_card": True, "layout_align_items_desktop": "flex-start",
                       "layout_justify_desktop": "center", "same_as_desktop": True, "padding_horizontal": 30, "padding_vertical": 30,
                       "width_desktop": 50})
cg["blocks"]["text_34dYXd"]["settings"].update({"text": "<h2>Ce qui fait un bon fauteuil à bascule</h2>", "text_style": "h2",
                                                "alignment": "left", "alignment_mobile": "left"})
cg["blocks"]["crit_intro"] = text_block("<p>Cinq points que nous vérifions avant de retenir un modèle. Notre guide les détaille, fiche par fiche.</p>")
col = cg["blocks"]["group_6DLfAU"]["blocks"]["group_BhcLrP"]
col["settings"].update({"wrap_in_card": False, "layout_direction_desktop": "column", "layout_align_items_desktop": "flex-start",
                        "layout_justify_desktop": "flex-start", "same_as_desktop": True, "padding_horizontal": 10,
                        "padding_vertical": 10, "layout_gap_desktop": 15, "color_scheme": ""})
crit_items = [("icon_with_text_DCkFpJ", "accessibility_new", "Se relever facilement, même avec bébé dans les bras"),
              ("icon_with_text_bFDMHJ", "back_hand", "Des accoudoirs qui soutiennent vraiment vos bras"),
              ("icon_with_text_D4CKhV", "airline_seat_recline_extra", "Un dossier qui soutient la tête"),
              ("icon_with_text_crit4", "waves", "Une bascule douce et discrète"),
              ("icon_with_text_crit5", "wash", "Une matière facile à entretenir")]
col["blocks"] = {k: icon_text(icon, f"<p>{txt}</p>", size=26) for k, icon, txt in crit_items}
col["block_order"] = [k for k, _, _ in crit_items]
cg["blocks"]["button_gNYHT8"]["settings"].update({"label": "Lire le guide pour bien choisir",
                                                  "link": "shopify://pages/guide-bien-choisir-fauteuil-allaitement",
                                                  "button_style": "secondary"})
cg["block_order"] = ["text_34dYXd", "crit_intro", "group_6DLfAU", "button_gNYHT8"]
crit["blocks"].pop("video_7eB4wN")
crit["blocks"]["crit_image"] = {"type": "image", "name": "t:image", "settings": {
    "show_on_display": "desktop_and_mobile", "image": IMG("fauteuil-a-bascule-allaitement-teddy-detail.jpg"),
    "show_placeholder": False, "link": "", "image_ratio": "portrait", "image_width_desktop": 100, "image_width_mobile": 100,
    "enable_rounded_corners": True, "margin_top": 0, "margin_bottom": 0, "additional_class": ""}, "blocks": {}}
crit["block_order"] = ["group_XyMggk", "crit_image"]
crit["settings"].update({"layout_flex_direction_desktop": "row", "layout_flex_align_items_desktop": "center"})

# ---------- 4. Sélection ----------
sel = S["collection_featured_JXRpw3"]
sel["settings"].update({"collection": "selection-bercelou", "color_scheme": "scheme-4", "layout_type": "slider",
                        "slider_items": 4, "slider_items_mobile": "1.8", "padding_top": 50, "padding_bottom": 50})
hg = sel["blocks"]["group_9NwHBp"]
hg["settings"]["color_scheme"] = ""
tg = hg["blocks"]["group_TwitGb"]["blocks"]
tg["text_QEHkGh"]["settings"].update({"text": "<h2>Notre sélection pour commencer</h2>", "text_style": "h2"})
tg["text_6LANC3"]["settings"]["text"] = "<p>Huit modèles pour trouver vos repères, de l'allaitement au coin lecture.</p>"
hg["blocks"]["button_DFrQyK"]["settings"].update({"label": "Voir tous les fauteuils", "link": "shopify://collections/fauteuil-a-bascule",
                                                  "button_style": "secondary"})

# ---------- 5. Du berceau au coin lecture ----------
ber = S["custom_section_NkHGLz"]
ber["name"] = "Du berceau au coin lecture"
ber["settings"].update({"color_scheme": "scheme-1", "padding_top": 60, "padding_bottom": 60})
ber["blocks"]["image_mFqbDi"]["settings"].update({"image": IMG("accueil-berceau-coin-lecture-bandeau.jpg"), "show_placeholder": False,
                                                  "image_ratio": "landscape"})
dg = ber["blocks"]["group_DgQq6e"]
dg["settings"].update({"color_scheme": "", "wrap_in_card": False})
dg["blocks"] = {
    "ber_h2": text_block("<h2>Du berceau au coin lecture</h2>", style="h2"),
    "ber_p": text_block("<p>Un fauteuil choisi pour les tétées de nuit n'a pas besoin de ressembler à un meuble de chambre de bébé. "
                        "Nos modèles gardent leur place dans le salon bien après, pour lire, se détendre ou simplement s'asseoir un moment.</p>"),
    "ber_btn": button_block("Voir les fauteuils design et scandinaves", "shopify://collections/rocking-chair-design-scandinave", style="secondary"),
}
dg["block_order"] = ["ber_h2", "ber_p", "ber_btn"]

# ---------- 6. Bandeau nuit : notre méthode ----------
mis = S["custom_section_wxUWmx"]
mis["name"] = "Notre méthode"
mis["settings"]["color_scheme"] = "scheme-3"
mg = mis["blocks"]["group_K88fpM"]["blocks"]
mg["text_EQyUFB"]["settings"]["text"] = "<p>Notre méthode</p>"
mg["text_TmGPC9"]["settings"]["text"] = "<h2>Chaque fauteuil est vérifié avant d'être retenu</h2>"
mg["text_QABwJ9"]["settings"]["text"] = ("<p>Hauteur d'assise, largeur des accoudoirs, hauteur du dossier, matière : "
                                         "nous contrôlons ces points sur chaque modèle, pour qu'il réponde à ce que vous cherchez vraiment. "
                                         "Se relever facilement, avoir le dos soutenu, garder un fauteuil qui reste beau au salon.</p>")

# ---------- 7. FAQ ----------
faq_items = [
    ("Comment choisir entre un fauteuil d'allaitement et un rocking chair design ?",
     "Les deux basculent en douceur. Les modèles de la collection Allaitement mettent l'accent sur des accoudoirs larges et un dossier haut pour les tétées de nuit. Notre guide pour bien choisir détaille les critères."),
    ("La livraison est-elle vraiment offerte ?", "Oui, en France métropolitaine, sur l'ensemble du catalogue."),
    ("Puis-je payer en plusieurs fois ?", "Oui, en 3 fois avec Klarna ou en 4 fois avec PayPal."),
    ("Que se passe-t-il si le fauteuil ne me convient pas ?",
     "Vous disposez de 14 jours après réception pour vous rétracter. Les frais de retour restent à votre charge sur les colis volumineux."),
    ("Le fauteuil arrive-t-il monté ?", "La plupart de nos fauteuils se montent à réception, notice fournie. Le délai et le montage sont précisés sur chaque fiche."),
]
acc_blocks = {}
for i, (q, a) in enumerate(faq_items):
    acc_blocks[f"faq_{i}"] = {"type": "_accordion", "name": "t:accordion", "settings": {
        "show_on_display": "desktop_and_mobile", "heading": q, "heading_tag": "h3", "heading_style": "paragraph",
        "open_by_default": i == 0, "icon": "none", "icon_custom": "", "additional_class": ""},
        "blocks": {f"faq_{i}_a": text_block(f"<p>{a}</p>")}, "block_order": [f"faq_{i}_a"]}
faq = section([
    ("faq_h2", text_block("<h2>Les questions qu'on nous pose le plus</h2>", style="h2")),
    ("faq_acc", {"type": "accordions", "name": "t:accordions", "settings": {"show_on_display": "desktop_and_mobile", "icon": "add",
                 "dividers": True, "additional_class": ""}, "blocks": acc_blocks, "block_order": list(acc_blocks)}),
    ("faq_btn", button_block("Voir toute la FAQ", "shopify://pages/faq", style="secondary")),
], "FAQ", scheme="scheme-1", pt=60, pb=40)

# ---------- 8. CTA final ----------
cta = S["custom_section_qetdex"]
cta["name"] = "Appel final"
cta["settings"].update({"color_scheme": "scheme-1", "padding_top": 40, "padding_bottom": 70})
cta["blocks"]["text_JqyRqD"]["settings"].update({"text": "<h2>Prêt à trouver votre fauteuil ?</h2>", "text_style": "h2"})
cta["blocks"]["text_PkpXrD"]["settings"]["text"] = "<p>Parcourez la sélection ou laissez-vous guider par notre guide pour bien choisir.</p>"
cta["blocks"]["group_cpEwfM"]["blocks"] = {"cta_btn": button_block("Trouver mon fauteuil", "shopify://collections/fauteuil-a-bascule")}
cta["blocks"]["group_cpEwfM"]["block_order"] = ["cta_btn"]

# ---------- assemble ----------
S["moments_bercelou"] = moments
S["faq_bercelou"] = faq
j["order"] = ["image_banner_VXNP89", "moments_bercelou", "custom_section_k9aPjP", "collection_featured_JXRpw3",
              "custom_section_NkHGLz", "custom_section_wxUWmx", "reviews_rXFabc", "faq_bercelou", "custom_section_qetdex"]
out = json.dumps(j, ensure_ascii=False)
for bad in ("Proposition unique", "[marque]", "clients satisfaits", "96%", "Excellent produit"):
    print(bad, bad in out)
open("index.new.json", "w").write(out)
print(len(out))
