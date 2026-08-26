#!/usr/bin/env python3
"""Panier Full Stack Lumière Matière — recette 12b (bannière, upsells, accordéons, reco).

Porte le « UpCart maison » (Bonum Vitae / Tuftéo / Maison Noirmont) sur le thème
publié `copie-de-fullstack-2-3`. Remplace la barre de progression à seuil 30 €,
incohérente avec la livraison offerte sans minimum.

Idempotent. N'écrit pas Helio ni UNIVERS.
"""
from __future__ import annotations

import json
import sys
import time
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from apply_fullstack import theme_file, upsert_theme_file  # noqa: E402

BACKUP = ROOT / "backups" / f"{date.today().isoformat()}-cart"

# Quatre matières / usages différents, palier 149–199 €, jamais ceux déjà au panier.
UPSELL_HANDLES = [
    "lustre-anneau-led-led-795468",  # 149 €, compact
    "plafonnier-led-565566",  # plafond bas / couloir
    "suspension-effet-pierre-led-073999",  # minéral
    "suspension-verre-814554",  # verre
]
UPSELL_JOINED = ",".join(UPSELL_HANDLES)

BANNER_LIQUID = """<div class="lm-cart-banner">
  <span>Livraison offerte en France, suivie. 7 à 18 jours ouvrés</span>
</div>
<style>
  .lm-cart-banner{display:flex;align-items:center;justify-content:center;gap:.5rem;margin:0 0 12px;padding:.7rem 1rem;border-radius:12px;background:#24211B;color:#F6F3EC;font-size:.85rem;font-weight:500;text-align:center;box-shadow:inset 3px 0 0 #C08A2D}
</style>"""

UPSELL_LIQUID = f"""<div class="lm-cart-upsell">
{{%- liquid
  assign lm_upsell = '{UPSELL_JOINED}' | split: ','
  assign lm_count = 0
-%}}
  <p class="lm-cart-upsell__title">À regarder aussi</p>
  <div class="lm-cart-upsell__list">
{{%- for h in lm_upsell -%}}
  {{%- if lm_count >= 2 -%}}{{%- break -%}}{{%- endif -%}}
  {{%- assign p = all_products[h] -%}}
  {{%- if p != empty and p.available -%}}
    {{%- assign in_cart = false -%}}
    {{%- for item in cart.items -%}}
      {{%- if item.product.handle == h -%}}{{%- assign in_cart = true -%}}{{%- endif -%}}
    {{%- endfor -%}}
    {{%- unless in_cart -%}}
      {{%- assign v = p.selected_or_first_available_variant -%}}
      <div class="lm-cart-upsell__item">
        <a href="{{{{ p.url }}}}" class="lm-cart-upsell__media">
          <img src="{{{{ p.featured_image | image_url: width: 160 }}}}" alt="{{{{ p.title | escape }}}}" width="56" height="56" loading="lazy">
        </a>
        <div class="lm-cart-upsell__info">
          <a href="{{{{ p.url }}}}" class="lm-cart-upsell__name">{{{{ p.title }}}}</a>
          <div class="lm-cart-upsell__row">
            <span class="lm-cart-upsell__price">{{{{ v.price | money }}}}</span>
            <button type="button" class="lm-upsell-add" data-variant-id="{{{{ v.id }}}}">Ajouter</button>
          </div>
        </div>
      </div>
      {{%- assign lm_count = lm_count | plus: 1 -%}}
    {{%- endunless -%}}
  {{%- endif -%}}
{{%- endfor -%}}
  </div>
</div>
<style>
  .lm-cart-upsell{{margin:0 0 12px}}
  .lm-cart-upsell__title{{font-family:var(--font-heading--family,serif);color:#24211B;font-size:1.05rem;margin:0 0 .8rem}}
  .lm-cart-upsell__list{{display:flex;flex-direction:column;gap:.9rem}}
  .lm-cart-upsell__item{{display:grid;grid-template-columns:56px 1fr;align-items:center;gap:.75rem}}
  .lm-cart-upsell__media{{display:block}}
  .lm-cart-upsell__item img{{width:56px;height:56px;object-fit:cover;border-radius:10px;background:#F6F3EC;display:block}}
  .lm-cart-upsell__info{{display:flex;flex-direction:column;gap:.35rem;min-width:0}}
  .lm-cart-upsell__name{{font-size:.85rem;line-height:1.25;color:#24211B;text-decoration:none}}
  .lm-cart-upsell__row{{display:flex;align-items:center;justify-content:space-between;gap:.5rem}}
  .lm-cart-upsell__price{{font-size:.9rem;font-weight:600;color:#24211B;white-space:nowrap}}
  .lm-upsell-add{{border:0;cursor:pointer;background:#24211B;color:#F6F3EC;font-size:.78rem;font-weight:600;padding:.4rem .85rem;border-radius:999px;white-space:nowrap}}
  .lm-upsell-add:hover{{background:#C08A2D;color:#24211B}}
</style>
<script>
(function(){{
  document.addEventListener('click', function(e){{
    var btn = e.target.closest('.lm-upsell-add');
    if(!btn) return;
    e.preventDefault();
    var id = parseInt(btn.getAttribute('data-variant-id'), 10);
    if(!id) return;
    btn.disabled = true;
    fetch('/cart/add.js', {{method:'POST', headers:{{'Content-Type':'application/json'}}, body: JSON.stringify({{id:id, quantity:1}})}})
      .then(function(r){{ if(!r.ok) throw r; location.reload(); }})
      .catch(function(){{ btn.disabled = false; }});
  }});
}})();
</script>"""

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


def main() -> None:
    BACKUP.mkdir(parents=True, exist_ok=True)
    cart = theme_file("templates/cart.json")
    drawer = theme_file("sections/cart-drawer-group.json")
    (BACKUP / "cart.json.avant").write_text(
        json.dumps(cart, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (BACKUP / "cart-drawer-group.json.avant").write_text(
        json.dumps(drawer, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    cart = patch_cart_page(cart)
    drawer = patch_drawer(drawer)
    assert_no_dashes(json.dumps(cart, ensure_ascii=False), "cart.json")
    assert_no_dashes(json.dumps(drawer, ensure_ascii=False), "cart-drawer-group.json")
    if "Plus que #" in json.dumps(cart) or "Plus que #" in json.dumps(drawer):
        raise RuntimeError("barre de progression encore présente")

    upsert_theme_file("templates/cart.json", cart)
    time.sleep(0.4)
    upsert_theme_file("sections/cart-drawer-group.json", drawer)
    time.sleep(0.8)

    live_cart = theme_file("templates/cart.json")
    live_drawer = theme_file("sections/cart-drawer-group.json")
    for label, live in (("cart", live_cart), ("drawer", live_drawer)):
        blob = json.dumps(live, ensure_ascii=False)
        if "lm-cart-banner" not in blob:
            raise RuntimeError(f"{label}: bannière absente après upsert")
        if "lm-cart-upsell" not in blob:
            raise RuntimeError(f"{label}: upsell absent après upsert")
        if "Plus que #" in blob or "_cart-progress-bar" in blob:
            raise RuntimeError(f"{label}: barre à seuil encore là")
    if "lm_reco" not in live_cart["sections"]:
        raise RuntimeError("section reco absente de cart.json")
    if "30 jours" not in json.dumps(live_cart, ensure_ascii=False):
        raise RuntimeError("accordéon retours non réécrit")
    print("OK panier 12b (bannière + upsells + accordéons + reco salon)")


if __name__ == "__main__":
    main()
