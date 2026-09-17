# Capacités du thème « Sous Abri » (Self Made Theme, base Dawn OS 2.0)

Thème `gid://shopify/OnlineStoreTheme/199781745023`, rôle `UNPUBLISHED`, boutique `zpeubn-i2.myshopify.com`. Exploration en lecture seule via `graphql_query` le 09/09/2026. Fichiers originaux sauvegardés dans `original/` (templates/*.json, config/settings_data.json, config/settings_schema.json, sections/header-group.json, sections/footer-group.json, 30 sections `.liquid` complètes), schémas `{% schema %}` extraits et validés en JSON dans `original/schemas/*.json`.

**Constat important :** le contenu actuellement en place dans `original/` (announcement bar « Noté 4.8/5 par nos clients », footer avec adresse vide, `templates/index.json` etc.) est un **reliquat de Cosy Cat House**, pas du contenu Sous Abri — normal puisque ce thème vient d'être importé et n'a pas encore été configuré. Rien de cela n'est repris dans `work/` : les avis fictifs et placeholders vides sont volontairement écartés (chasse gardée de Hakim sur les avis).

Un autre chantier existe dans `../theme-work/` (racine `shopify/`) : c'est une préparation pour l'**ancien thème FullStack** `199695565183`, remplacé par Self Made Theme (voir `DECISIONS-2026-09-09.md`). Il utilise des types de sections qui n'existent pas ici (`custom-section`, `comparison-table`, `sa-reviews`) — **non réutilisable tel quel**, mais son contenu rédactionnel (mapping metafields, structure des blocs produit) a servi de référence pour construire `work/`.

---

## 1. Réglages globaux (`config/settings_schema.json`)

### Couleurs
- `color_schemes` (color_scheme_group) : 5 schémas dans ce thème — `background-1`, `background-2`, `accent-1`, `accent-2`, `inverse`. Chaque schéma définit `background`, `background_gradient`, `text`, `title`, `button`, `button_label`, `secondary_button_label`, `link`, `link_hover`, `normal_price_color`, `sale_price_color`, `compare_at_price_color`, `shadow`.
- `body_background_color` (color, défaut `#FFFFFF`) : fond visible derrière les sections.
- Recolorés dans `work/config/settings_data.json` avec `brand-tokens.json` (fond `#F4F1EA`, texte `#1B1F24`, accent `#C8552B`, secondaire `#2F4A5A`, surface `#FFFFFF`) — détail en §7.

### Typographie
- `type_header_font` (font_picker, défaut thème `montserrat_n9` — reliquat CCH) — mis à `archivo_n7` dans `work/`.
- `type_body_font` (font_picker, défaut thème `open_sans_n4`) — mis à `inter_n4` dans `work/`.
- `heading_scale`, `body_scale` (range 100-150, défaut 100).
- **[À VÉRIFIER]** Archivo et Inter sont des polices Google courantes, très probablement dans la bibliothèque de polices Shopify (comme `assistant`, `montserrat`, `open_sans` déjà vus dans ce thème) — à confirmer dans l'éditeur de thème (Typographie) avant push, sinon repli sur la police la plus proche disponible.

### Boutons, cartes, badges
- `buttons_radius` (range 0-40, valeur actuelle 4), `buttons_border_thickness`, `buttons_shadow_*`.
- `card_style` (select `standard`/`card`), `card_color_scheme`, `card_corner_radius`, `card_shadow_*` — cartes produit/collection.
- `badge_position`, `sale_badge_color_scheme`, `sold_out_badge_color_scheme`, `enable_percentage_discount`.
- `page_width` (range 1000-1600, valeur actuelle 1500).
- Aucun réglage global de compte à rebours ou d'urgence dans `settings_schema.json` — cohérent avec l'interdiction du brief.

### Logo, réseaux, paiement
- `settings_schema.logo` : `logo` (image_picker), `logo_width`, `logo_mobile`, `logo_mobile_width`, `favicon`. **[À VÉRIFIER] logo pas encore produit** — `work/config/settings_data.json` laisse `logo: null` (fallback texte `shop.name`).
- `settings_schema.social-media` : liens Facebook/Instagram/YouTube/TikTok/Twitter/Snapchat/Pinterest/Tumblr/Vimeo — tous vides actuellement, aucun compte Sous Abri connu.
- `settings_schema.cart` : `cart_type` (select `notification`/`drawer`/`page`), `enable_free_bar` + `free_delivery_limit` (barre de seuil de livraison offerte — à activer avec un seuil cohérent avec « livraison offerte » sans minimum, donc probablement à désactiver ou fixer à 0).

---

## 2. Groupes header / footer

### `sections/header-group.json` → section `header` (fichier `sections/header.liquid`)
Settings utiles : `logo_position` (`top-left`/`top-center`/`middle-left`/`middle-center`), `menu` (link_list, handle du menu principal), `menu_type_desktop` (`dropdown`/`mega`/`drawer`), `sticky_header_type` (`none`/`on-scroll-up`/`always`/`reduce-logo-size`), `color_scheme`, `menu_color_scheme`, `dropdown_color_scheme`, `parent_collection_background_color`/`parent_collection_color`/`child_collection_background_color`/`child_collection_color` (méga-menu), `enable_search`, `enable_country_selector`, `enable_language_selector`, `mobile_logo_position`, `transparent`. Blocs : `@app` uniquement (pas de blocs de contenu éditables dans le header lui-même — le menu vient du link_list `menu`).

### `sections/announcement-bar.liquid` (dans le groupe header)
Settings : `icon` (`arrow`/`caret`), `auto_rotate`, `change_slides_speed`, `marquee`, `marquee_speed`, `show_line_separator`, `color_scheme`. Bloc `announcement` : `text` (richtext), `link` (url) — illimité en nombre, rotation automatique si `auto_rotate: true`.

### `sections/footer-group.json` → section `footer` (fichier `sections/footer.liquid`)
Settings utiles : `color_scheme`, `footer_card` (+ `border_radius`), `newsletter_enable` + `newsletter_heading`, `enable_follow_on_shop`, `show_social`, `enable_country_selector`, `enable_language_selector`, `payment_enable` (icônes automatiques depuis `shop.enabled_payment_types`), `show_policy` (liste `shop.policies`), `disable_shopify_powered`, `disable_oneclickbrand_credit`, `margin_top`, `padding_top`, `padding_bottom`.
Blocs : `@app`, `link_list` (`heading` inline_richtext, `menu` link_list — **un bloc = un menu**, donc une colonne « Boutique »/« Aide »/« À propos » = un menu Shopify distinct à créer), `brand_information` (`show_social`, utilise `settings.brand_image/brand_headline/brand_description` globaux), `text` (`heading`, `subtext` richtext — utilisé pour les coordonnées OH Ventures), `image` (`image`, `image_width`, `alignment` — si vide, affiche `shop.name` en texte, utile tant que le logo n'existe pas).

---

## 3. Sections utiles (settings et blocs par section)

### `announcement-bar` — voir §2.

### `slideshow`
Settings : `height` (`auto`/`highest_image`/`fixed` + `max_height`), `auto_rotate`, `change_slides_speed`, `loading`, `arrow_position_desktop/mobile`, `arrow_color_desktop/mobile`, `hide_dots`, `keep_text_on_media_mobile`, `display_as_card`, `color_scheme`.
Bloc `slide` (limite 10) : `image`, `video`, `image_mobile`, `video_mobile`, `box_align`/`box_align_mobile` (9 positions), `text_alignment`/`text_alignment_mobile`, `heading` (inline_richtext) + `hn`/`heading_size`, `subheading` (richtext), `primary_button_label/url` + `primary_secondary_style`, `secondary_button_label/url` + `secondary_secondary_style`, `banner_link`, `show_text_box`, `image_overlay_opacity`, `decoration`.

### `image-with-text`
Settings : `image`, `decoration` (`none`/`rectangle`), `video`/`video_url`, `height` (`adapt`/`small`/`medium`/`large`), `desktop_image_width` (`small`/`medium`/`large`), `layout` (`image_first`/`text_first`), `desktop_content_position` (`top`/`middle`/`bottom`), `desktop_content_alignment`/`mobile_content_alignment`, `section_style` (`normal`/`card`/`overlap`/`flush`), `color_scheme`.
Blocs (chacun limité à 1) : `heading` (inline_richtext + `heading_size`/`hn`), `caption` (text + `text_style`/`text_size`), `text` (**richtext**, + `text_style` `body`/`subtitle` — accepte la syntaxe de source dynamique `{{ product.metafields.custom.xxx }}`), `button` (`button_label`, `button_link`).

### `multicolumn`
Settings : `title` (inline_richtext), `heading_size`, `button_label`/`button_link` (bouton global optionnel), `image_width` (`third`/`half`/`full`), `image_ratio`, `columns_desktop` (1-6), `column_alignment`, `background_style` (`none`/`primary`), `columns_mobile` (`1`/`2`), `display_as_card`, `color_scheme`.
Bloc `column` (illimité) : `image`, `title` (inline_richtext), `text` (richtext), `link_label`, `link`.

### `rich-text`
Settings : `border_top`, `desktop_content_position`/`content_alignment` (`left`/`center`/`right`), `narrow_text`, `display_as_card`, `color_scheme`.
Blocs : `heading` (limite 3, inline_richtext + `heading_size`/`hn`), `caption` (limite 3), `text` (limite 3, **richtext** — accepte la source dynamique), `button` (limite 2 — **un seul bloc peut porter 2 boutons** : `button_label`/`button_link`/`button_style_secondary` + `button_label_2`/`button_link_2`/`button_style_secondary_2`).

### `faq`
Settings : `heading`, `heading_size`/`hn`, `description` (richtext), `text_alignment`, `display_as_card`, `color_scheme`.
Blocs : `question` (illimité — `question` text, `answer` richtext, `open_by_default` checkbox), `content` (sous-en-tête de groupe), `divider` (`margin_top`/`margin_bottom`).
**Aucun bloc `custom_liquid`** dans cette section : impossible d'y injecter directement `product.metafields.custom.faq`. Pour la FAQ produit dynamique (metafield unique en HTML `<details>`), utiliser la section **`custom-liquid`** à part (voir `templates/product.json` → section `faq`), pas un bloc de la section `faq`.

### `compare-table`
Settings : `heading_size`/`hn`, `heading`, `content` (richtext, intro), `content_position` (`above`/`left`/`right`), `heading_col_1`/`image_col_1`, `heading_col_2`/`image_col_2`, `display_as_card`, `color_scheme`, `border_radius`.
Bloc `row` (illimité) : `heading` (nom de la ligne), `is_checked_col_1` (checkbox), `is_checked_col_2` (checkbox). **Comparaison uniquement binaire (coché/non coché) sur 2 colonnes** — pas de cellules de texte libre ni de 3e/4e colonne. Le tableau à 4 colonnes de `accueil.md` (prix/délai/déclaration/montage/durée de vie/ce qu'on dit) a donc été simplifié en 5 lignes « Sous Abri » vs « Grande surface de bricolage », toutes vraies et vérifiables (pas de prix chiffrés non vérifiés).

### `compare-image`
Settings : `content_position`, `heading`, `content` (richtext), `label_before`/`image_before`, `label_after`/`image_after`, `color_scheme`. Pas de blocs. Utile pour un avant/après (ex. voiture sous la pluie sans/avec carport) — non retenu dans `work/` (pas de visuel avant/après dans le shot-list), mais disponible si Hakim en produit un.

### `reassurance`
Settings : `heading_size`/`hn`, `heading`, `content` (richtext, intro), `content_alignment`, `column_mobile` (`1`/`2`), `card_style` (`text-below`/`text-right`), `card_background` (+ `card_background_value`), `card_border` (+ `card_border_value`), `card_text_color`, `card_border_radius`, `color_scheme`.
Bloc `item` (illimité) : `icon` (image_picker — pas d'icônes vectorielles prédéfinies, uniquement une image importée), `heading`, `description` (richtext).

### `testimonials`
Settings : `heading`, `heading_size`/`hn`, `text_alignment`, `show_stars` (+ `stars_color`), `show_profile_picture`, `enable_premium_rating` (+ `rating_text`/`rating_number` — note globale type Trustpilot), `columns_desktop`/`columns_tablet`/`columns_mobile`, `enable_desktop_slider`/`enable_mobile_slider`/`enable_auto_slider`, `color_scheme`.
Bloc `testimonial` (illimité) : `author_image`, `author_name`, `author_description`, `rating` (range 1-5), `content` (richtext).
**Dans `work/templates/index.json`, la section `avis` est présente avec `blocks: {}` et `block_order: []` : zéro témoignage, zéro note.** Chasse gardée de Hakim — ne pas ajouter de bloc `testimonial` sans avis réel importé (voir mémoire « Import avis Trustoo »).

### `contact-form`
Settings : `heading` (inline_richtext, vide = titre masqué visuellement mais accessible), `heading_size`/`hn`, `display_as_card`, `color_scheme`. **Aucun bloc.**
Champs **fixes, non personnalisables** dans `sections/contact-form.liquid` : nom, e-mail (obligatoire), téléphone, message. **Pas de champ « sujet » en menu déroulant, pas de champ « numéro de commande », pas de pièce jointe.** Pour le formulaire de contact standard (`page.contact.json`), ce sont les seuls champs disponibles — limitation documentée, à confirmer avec Hakim si un champ sujet est indispensable (nécessiterait alors la même technique `custom-liquid` + `{% form 'contact' %}` que pour le devis).

### `custom-liquid`
Settings : `custom_liquid` (type **liquid**, exécuté — pas juste une valeur dynamique), `color_scheme`, `display_as_card`, `margin_top`/`margin_bottom`, `padding_top`/`padding_bottom`. Pas de blocs.
Usage dans `work/` : (1) `templates/product.json` section `faq`, pour rendre `{{ product.metafields.custom.faq }}` (HTML `<details>` déjà formaté) ; (2) `templates/page.devis.json` section `formulaire-devis`, pour un formulaire `{% form 'contact' %}` avec tous les champs du devis (la section `contact-form` native ne les supporte pas).

### `featured-collection` / `collection-list`
`featured-collection` : affiche les produits d'**une seule** collection (réglages produits : `products_to_show`, `columns_desktop/tablet`, `columns_mobile`, `enable_desktop_slider`, `image_ratio`, `show_secondary_image`, `show_vendor`, `show_rating`, `enable_quick_add`, `show_view_all` + `view_all_style`).
`collection-list` : affiche une **grille de collections** (pas de produits) — c'est celle utilisée pour « nos familles ». Settings : `title`, `show_view_all`, `image_ratio`, `columns_desktop/tablet/mobile`, `show_collection_title`, `title_position` (9 positions), `overlay_opacity`. Bloc `featured_collection` (illimité) : `collection` (picker), `image` (override), `title_color`. **Chaque bloc pointe vers une collection réelle, pas vers une URL libre** — impossible d'y mettre un lien direct vers les pages devis ; d'où la section séparée `familles-devis` (rich-text) dans `work/templates/index.json`.

### `main-collection-banner` / `main-collection-description` / `main-collection-product-grid`
`main-collection-banner` : `show_collection_description`, `show_collection_image` (+ position/masquage mobile), `background`, `border_radius`, `color_scheme`. `main-collection-description` : `display_card`, `collapse` (repliable). `main-collection-product-grid` : `columns_desktop`, `columns_mobile`, `image_ratio`, `show_secondary_image`, `show_vendor`, `show_rating`, `enable_quick_add`, `enable_filtering` (+ `filter_type` `horizontal`/`vertical`/`drawer`), `enable_sorting`, `product_count`, `products_per_page`, `pagination_type` (`pagination`/`load_more`/`infinite_scroll`). Les trois sont liées automatiquement à la collection consultée (pas de picker) — pas de blocs.

### `main-page`
Settings : uniquement `padding_top`/`padding_bottom`. Pas de picker de page : **liée automatiquement à la page consultée** (`page.title`, `page.content`) — c'est la section à utiliser dans `templates/page.json` générique (guide déclaration, guide montage, comparatif, qui-sommes-nous, garantie/SAV, FAQ éditoriale…), le corps de chaque page vivant dans la ressource Shopify Page elle-même, pas dans le template.

### `page`
Settings : `page` (picker — sélectionne une page **différente** de celle affichée), `heading_size`/`hn`, `color_scheme`, `display_as_card`. Utile pour **incruster** le contenu d'une autre page dans une section (ex. teaser « qui sommes-nous » sur l'accueil) — pas utilisé dans `work/` (non demandé par le sitemap), mais disponible.

### `featured-product`
Section « produit isolé » avec picker `product` explicite (utile pour une vignette produit unique hors template produit, ex. un encart accueil) — mêmes types de blocs que `main-product` (title, price, sku, inventory, variant_picker, buy_buttons, description, share, rating, icon-with-text, custom_liquid…) mais nécessite un `product` choisi à la main. Non utilisé dans `work/` (le sitemap ne demande pas de produit vedette sur l'accueil), disponible si besoin.

### `main-product`
Settings : `enable_sticky_info`, `media_size` (`small`/`medium`/`large`), `media_position` (`left`/`right`), `gallery_layout` (`stacked`/`columns`/`slider`/`thumbnail_slider`), `mobile_gallery_layout` (`slider`/`thumbnail_slider`), `image_ratio`, `media_fit` (`contain`/`cover`), `image_zoom` (`lightbox`/`hover`/`none`), `hide_variants`, `enable_video_looping`, `initial_image_behavior`, `display_card`, `color_scheme`.

**Blocs disponibles (limites entre parenthèses) :**
- `title` (1)
- `text` (illimité) — `text` (inline_richtext), `text_style` (`body`/`subtitle`/`uppercase`), `text_color`, `enable_icon` + `icon` (bibliothèque d'icônes intégrée : heart, truck, return, lock, leaf, recycle, shield… ~45 icônes)
- `rich_text` (illimité) — `text` (**richtext**, accepte la source dynamique)
- `price` (1) — `show_taxes`, `price_text_box*`, couleurs/tailles régulier/promo/barré
- `sku` (1), `inventory` (1, + `inventory_threshold`, `show_inventory_quantity`)
- `quantity_selector` (1) — pas de réglage
- `variant_picker` (1) — `picker_type` (`dropdown`/`button`/`bundle`), `show_color_swatches`, `show_free_shipping` (+ `free_shipping_threshold`)
- `linked_variants` (1) — picker de style de variantes liées (pills/boxes/dropdown), non utilisé (pas de variantes liées prévues)
- `personalization` (illimité) — champ de personnalisation payant/gratuit, non utilisé (pas prévu au catalogue)
- `buy_buttons` (1) — `show_dynamic_checkout`, `show_payment_icons`, `show_gift_card_recipient`, `sticky` (barre d'achat collante mobile), `enable_sticky_atc_desktop` (+ styles)
- `description` (1) — `full_width`, `collapse`
- `share` (1) — `share_label`
- `custom_liquid` (illimité)
- `popup` (illimité) — lien texte + `page` (ouvre une modale avec le contenu d'une Page — utile pour un lien « voir les conditions » sans quitter la fiche)
- `rating` (1) — nécessite une app de notation (aucune installée)
- `complementary` (1, produits complémentaires — nécessite Shopify Search & Discovery)
- `icon-with-text` (illimité) — jusqu'à 3 duos icône+titre par bloc (`layout` horizontal/vertical)
- `collapsible` (illimité) — **`heading` (text), `content` (richtext — accepte la source dynamique), `description` (checkbox, affiche aussi `product.description`), `open_by_default` (checkbox), `image`**. C'est le bloc utilisé pour les 7 volets (dimensions/caractéristiques, déclarer, montage, ancrage/vent, ce qu'il ne fait pas, livraison, contenu du colis).
- `timer`/`coupon` : présents dans le schéma mais **volontairement non utilisés** (compte à rebours et coupon factice interdits par le brief : « aucune fausse urgence »).
- `@app` (illimité)

---

## 4. Mapping metafields utilisé dans `work/`

Namespace `custom` (à créer côté Shopify avant le push, hors périmètre de cette mission en lecture seule) :

| Metafield | Type conseillé | Utilisé dans |
|---|---|---|
| `custom.sous_titre` | texte court (ou single_line_text_field) | bloc `text` du `main-product` |
| `custom.specifications` | rich text | collapsible « Dimensions et caractéristiques » |
| `custom.declarer` | rich text | collapsible « Faut-il le déclarer ? » |
| `custom.montage_texte` | rich text | collapsible « Montage » |
| `custom.ancrage_vent` | rich text | collapsible « Ancrage et vent » |
| `custom.ne_fait_pas` | rich text | collapsible « Ce qu'il ne fait pas » |
| `custom.livraison_texte` | rich text | collapsible « Livraison » |
| `custom.contenu_colis` | rich text | collapsible « Contenu du colis » |
| `custom.protege` | rich text | section `image-with-text` « Ce qu'il protège » |
| `custom.faq` | rich text (HTML `<details><summary>…</summary><p>…</p></details>`) | section `custom-liquid` « faq » |
| `custom.texte_seo` (sur **collection**) | rich text | section `rich-text` sous la grille (`templates/collection.json`) |

La syntaxe utilisée dans les fichiers JSON est littéralement `{{ product.metafields.custom.xxx }}` (ou `collection.metafields.custom.texte_seo`) comme valeur du champ — c'est le mécanisme de « source dynamique » de l'éditeur Shopify (voir instruction de la mission), qui ne fonctionne que sur les champs `text`/`richtext`/`inline_richtext`/`url`/`image_picker` des blocs, pas sur les champs `liquid` (ceux-ci exécutent du vrai code Liquid, d'où `{{ product.metafields.custom.faq }}` écrit en toutes lettres dans le bloc `custom-liquid`).

---

## 5. Images de la boutique (`shopify://shop_images/…`)

Lot 1 déjà téléversé (confirmé par `DECISIONS-2026-09-09.md`/`README.md`) : `sousabri-famille-alu.jpg`, `sousabri-famille-tentes.jpg`, `sousabri-famille-devis.jpg`, `sousabri-douleur-grele.jpg`, `sousabri-douleur-soleil.jpg`, `sousabri-comparaison.jpg`.
`sousabri-hero.jpg` (2048×1152, 16:9) — statut **« À PRODUIRE »** dans `shot-list.md` ligne 17 — référencé dans `work/templates/index.json` (section `hero`) en anticipation, mais **[À VÉRIFIER] à ne pas pousser tant que le fichier n'est pas réellement dans les Files Shopify**, sinon l'image-with-text affichera un placeholder.

---

## 6. Menus de navigation requis (à créer avant le push — hors périmètre lecture seule)

- `main-menu` (déjà référencé par le header) : Carports aluminium → `/collections/carport-alu` · Tentes-garages → `/collections/carport-metallique` **[À VÉRIFIER : aucune collection « tentes-garages » dédiée parmi les 11 créées — `carport-metallique` est une correspondance provisoire, à confirmer avec Hakim ou à créer]** · 2 voitures → `/collections/carport-2-voitures` · Camping-car → `/collections/carport-camping-car` · Guides (sous-menu vers les 3 pages guides).
- `footer-boutique`, `footer-aide`, `footer-apropos` : un menu par colonne de pied de page (contenu détaillé dans `annonces-menu-footer.md` §3), requis par le bloc `link_list` de la section `footer` (un bloc = un seul menu, pas de sous-colonnes).

---

## 7. Palette et typographie retenues dans `work/config/settings_data.json`

| Schéma | Fond | Texte/titre | Bouton | Usage prévu |
|---|---|---|---|---|
| `background-1` | `#F4F1EA` (fond de marque) | `#1B1F24` | `#C8552B` | Corps de page par défaut |
| `background-2` | `#FFFFFF` (surface) | `#1B1F24` | `#C8552B` | Cartes, sections alternées, formulaires |
| `accent-1` | `#C8552B` (terracotta) | `#FFFFFF` | `#FFFFFF` sur fond terracotta | CTA final, mise en avant |
| `accent-2` | `#EDE6D8` (crème plus soutenu) | `#1B1F24` | `#C8552B` | Variante douce, non utilisée dans `work/` mais disponible |
| `inverse` | `#2F4A5A` (ardoise, secondaire) | `#FFFFFF` | `#C8552B` | Barre d'annonce, pied de page |

`type_header_font: archivo_n7`, `type_body_font: inter_n4`, `body_background_color: #F4F1EA`. `card_color_scheme`/`collection_card_color_scheme`/`cart_color_scheme` → `background-2`. `sale_badge_color_scheme` → `accent-1`, `sold_out_badge_color_scheme` → `inverse`. `disable_oneclickbrand_credit: true` (retire le crédit agence en pied de page).
