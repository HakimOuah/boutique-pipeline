"""Bercelou : templates/product.json (FullStack) — colonne d'achat + sections alimentées par la fiche."""
import json, copy
orig = json.load(open('product.parsed.json'))
om = orig['sections']['main']

def fiche(part): return {"type": "bercelou-fiche", "settings": {"part": part}}

blocks = {
  "product_media_gallery": om['blocks']['product_media_gallery'],
  "titre": {"type": "text", "name": "t:title", "settings": {"text": "<h1>{{ closest.product.title }}</h1>", "text_style": "h3", "margin_top": 0, "margin_bottom": 0}},
  "prix": {"type": "product-price", "name": "t:price", "settings": {"product": "{{ closest.product }}", "sales_badge": "percentage", "text_style": "h5"}},
  "paiement": fiche("paiement"),
  "benefices": fiche("benefices"),
  "product_form_grYQk6": copy.deepcopy(om['blocks']['product_form_grYQk6']),
  "livraison": fiche("livraison"),
  "reassurance": fiche("reassurance"),
  "paiements_icones": {"type": "payment-methods", "name": "t:payment_methods", "settings": {"alignment_desktop": "flex-start", "alignment_mobile": "flex-start", "icon_size": 34, "margin_top": 0, "margin_bottom": 0}},
  "accordeons": fiche("accordeons"),
}
order = ["titre", "prix", "paiement", "benefices", "product_form_grYQk6", "livraison", "reassurance", "paiements_icones", "accordeons"]

main = {"type": "main-product", "blocks": blocks, "block_order": order,
        "settings": dict(om['settings'], carrousel_sticky=True, product_info_sticky=False, gap=56, padding_top=24, padding_bottom=40)}

reco = copy.deepcopy(orig['sections']['product_recommendations_G8mJVG'])
grp = reco['blocks']['product-card']['blocks']['product_card_group_EcgVgX']
grp['blocks'].pop('rating_stars_nz7WzY', None)
if 'block_order' in grp: grp['block_order'] = [b for b in grp['block_order'] if b != 'rating_stars_nz7WzY']
reco['blocks']['title']['settings']['text'] = "<h2>Vous aimerez aussi</h2>"
reco['blocks']['title']['settings']['text_style'] = "h2"
reco['settings'].update(color_scheme="scheme-4", padding_top=64, padding_bottom=64)

tpl = {"sections": {
  "main": main,
  "bc_detail": {"type": "bercelou-fiche", "settings": {"part": "detail", "color_scheme": "scheme-1"}},
  "bc_avant": {"type": "bercelou-fiche", "settings": {"part": "avant", "color_scheme": "scheme-4"}},
  "bc_faq": {"type": "bercelou-fiche", "settings": {"part": "faq", "color_scheme": "scheme-1"}},
  "product_recommendations_G8mJVG": reco,
}, "order": ["main", "bc_detail", "bc_avant", "bc_faq", "product_recommendations_G8mJVG"]}

s = json.dumps(tpl, ensure_ascii=False, separators=(',', ':'))
open('product.json', 'w').write(s)
print(len(s))
