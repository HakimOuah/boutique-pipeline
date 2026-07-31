# Reconnaissance du thème brouillon « copie-de-fullstack-2-3 » — plan de portage

Date : 21/07/2026 · Mission lecture seule (aucune mutation effectuée) · Périmètre : thème BROUILLON uniquement
Thème inspecté : `gid://shopify/OnlineStoreTheme/188623847809` · rôle `UNPUBLISHED` · préfixe `/t/2` · dernière modif : 21/07/2026 13:36 UTC
Le thème publié Horizon (`gid://shopify/OnlineStoreTheme/188623192449`) n'a **pas** été lu, conformément au périmètre.

---

## 1. Identité du thème de base

| Champ | Valeur |
|---|---|
| Nom | **FullStack** |
| Version | **2.3.0** |
| Auteur | Équipe FullStack |
| Documentation | https://themefullstack.com/ |
| Support | https://themefullstack.com/pages/support |
| `themeStoreId` | `null` → thème **hors Theme Store Shopify** (thème commercial français, uploadé en zip) |

Ce n'est donc **ni Horizon, ni un thème Shopify officiel** : c'est le thème payant FullStack v2.3 (orienté e-commerce FR/dropshipping), dupliqué (« copie-de-fullstack-2-3 »).

### Architecture technique
- **Même génération que Horizon** : architecture « theme blocks » (dossier `blocks/` à la racine, `{% content_for 'blocks' %}`, blocs `@theme`/`@app`, blocs statiques, `{{ closest.product }}`, `{% stylesheet %}` inline). C'est une base moderne, pas un thème vintage 1.0.
- `layout/theme.liquid` minimal : reset.css + base.css + slider.css, snippets `fonts`, `scripts`, `css-variables`, `color-schemes`, Material Icons ; groupes `header-group`, `cart-drawer-group`, `breadcrumbs-group`, `footer-group` ; wishlist et cart drawer conditionnés par settings (`cart_type: drawer` actif).
- Locale par défaut : **`fr.default.json`** (+ en, de, es, it, pl) — thème nativement français, bon point.
- JS vanilla par composant (`product-form.js`, `variant-picker.js`, `quantity-breaks.js`, `delivery-estimation.js`, `sticky-add-to-cart.js`, `splide.js`…).
- Réglages globaux actuels (settings_data) : Poppins (headings/body), radius arrondis (boutons 20px, cartes 22px), `max_page_width` 1300, drawer panier avec ouverture auto à l'ajout.

### Structure de la page produit (template + section)
`sections/main-product.liquid` est une coquille : galerie média statique (`_product-media-gallery`) + colonne d'infos remplie par blocs libres. Réglages : image gauche/droite, largeur colonne, sticky galerie + sticky infos, carrousel plein écran mobile. Le `templates/product.json` de démo empile dans la colonne :
`rating-stars` → `text` (titre) → `product-price` → `text` (description) → `_product-form` (variantes + ATC + accelerated checkout) → `payment-methods` → `accordions` (retour/livraison) → `group` de 3 `icon-with-text` (réassurance) ; puis sous la flottaison : 2 `custom-section` « À propos », `reviews` (6 faux avis), `custom-section` aide+FAQ, `product-recommendations`.

**C'est exactement le même squelette CRO que le modèle Horizon de référence** — l'ordre §15 se reconstruit sans lutte contre le thème.

### Inventaire (241 fichiers)
- **Sections (38)** : main-* complets (product, collection, collections, page, article, blog, search, login…), `custom-section` (générique, très riche — 260 Ko), `custom-code`, `reviews`, `product-recommendations`, `product-featured`, `collection-featured`, `collections-featured`, `image-banner`, `comparison-table`, `marquee`, `blog-featured`, `announcement-bar`, header/footer/cart-drawer/breadcrumbs + groupes JSON, `predictive-search`, `wishlist-drawer`, `password`, `demo-design-system`.
- **Blocs (99)** : publics (`text`, `image`, `video`, `button`, `group`, `icon`, `icon-with-text`, `accordions`, `badges`, `countdown`, `cross-sell`, `custom-code`, `delivery-estimation`, `payment-methods`, `product-price`, `product-inventory`, `rating-stars`, `review`, `reviews-badge`, `slider`, `tabs`, `stories`, `before-after`, `marquee`, `this-pack-contains`, `newsletter-signup`, `popup`, `separator`…) + privés `_product-form`, `_product-variant-picker`, `_product-add-to-cart-button`, `_quantity-breaks`, `_toggle-cross-sell`, `_fake-variant-picker`, mégamenus, cart blocks, etc.
- **Templates (22)** : `index.json`, `product.json`, `collection.json`, `cart.json`, `page.json`, `page.contact.json`, `search.json`, `404.json`, `article/blog`, `password`, `list-collections`, `customers/*`, `gift_card.liquid`. **Aucun template alternatif produit** : `product.kit-tufting.json` et `product.accessoire.json` sont à créer.

---

## 2. Compatibilité avec les codes Horizon de référence : **PARTIELLE (favorable)**

Les blocs de référence (`docs/horizon-product-page-reference/`) sont du HTML/CSS autoportant : ils ne dépendent presque pas des variables Horizon. Points de friction identifiés :

1. **Variables CSS/typo** : les codes utilisent `var(--font-body--family, var(--font-body-family, 'Inter'…))` (doubles fallbacks Horizon). FullStack définit ses propres variables dans `snippets/css-variables.liquid` — à vérifier au build ; au pire le fallback dur s'applique (mauvaise police). À remplacer par la pile FullStack ou par les polices Tuftéo (Fraunces / Nunito Sans, brand-tokens.json).
2. **Couleurs codées en dur Bonum Vitae** (`#0E3A5A`, `#EAF3F1`, `#F7F4EE`, étoiles `#35B6AA`) → à basculer sur la palette Tuftéo (`#FAF4EC` fond, `#3D2C24` texte, `#C4593B` accent, `#8FA98F` secondaire).
3. **Point d'insertion** : Horizon utilisait des blocs « Custom Liquid » ; FullStack offre l'équivalent exact — bloc `custom-code` (insérable dans la colonne produit) et section `custom-code`. Rien à hacker.
4. **Doublons natifs** : FullStack possède déjà des équivalents natifs de plusieurs customs Horizon (voir §4) — dans plusieurs cas, le natif est préférable au portage.
5. **Non portable tel quel (déjà documenté dans la matrice de portabilité de la référence)** : les JSON Horizon, les IDs, l'app block TrustWILL, les images `shopify://` et CDN Bonum Vitae, les coordonnées/notes/avis.

Atout majeur : le **portable-kit Dropilot existe déjà** (`boutique-tufting/shopify/portable-kit/`) — versions indépendantes de Horizon de : paiement fractionné + bénéfices + livraison (`dp-purchase-support.liquid`), réassurance (`dp-reassurance.liquid`), FAQ (`dp-faq.liquid`), icônes (`dp-icon.liquid`), avec locales fr/en/de (clés `dropilot` à fusionner). **C'est la source de portage prioritaire**, devant les extraits bruts Horizon.

---

## 3. Mapping sitemap ⇄ thème FullStack

### 3.1 Home (11 sections du sitemap)

| # Sitemap | Section attendue | Offre FullStack | Verdict |
|---|---|---|---|
| 1 | Hero « Ton premier tapis, guidé pas à pas » + CTA | `image-banner` + bloc `_image-banner` (texte, boutons, icon-with-text) | ✅ natif |
| 2 | Bandeau offre (seulement si offre réelle) | `announcement-bar` (header-group) | ✅ natif — laisser vide au lancement |
| 3 | Vignettes 6 catégories | `collections-featured` / `collection-featured` | ✅ natif |
| 4 | Produit héros kit 229 € (bénéfices ✅ + 🎁) | `product-featured` + blocs `icon-with-text` | ✅ natif |
| 5 | Vidéo « matériel essentiel » | `custom-section` + bloc `video` | ✅ natif — média à produire après échantillon |
| 6 | Débuter en 3 étapes | `custom-section` + `group`/`icon-with-text` (ou `stories`) | ✅ natif |
| 7 | Grille « incontournables » | `collection-featured` (grille produits) | ✅ natif |
| 8 | Bloc Apprendre / Academy | `custom-section` (texte + image + boutons) | ✅ natif |
| 9 | **Avis — bv-avis-clients posée dès le build** (amendement Hakim) | ❌ rien d'équivalent contrôlé (la section `reviews` native = carrousel avec presets de faux avis) | 🔧 **à porter** : `sections/bv-avis-clients.liquid` |
| 10 | FAQ courte 4-6 questions | bloc `accordions` ou `dp-faq` du portable-kit | ✅ natif ou 🔧 portable-kit |
| 11 | Bandeau réassurance footer (4 icônes) | `group` + `icon-with-text`, ou `dp-reassurance` | ✅ natif ou 🔧 portable-kit |

L'`index.json` de démo actuel (proposition de valeur placeholder, « - 2 000 clients satisfaits », « 96 % de clients satisfaits », 6 faux avis « Excellent produit ! », newsletter) est **à reconstruire entièrement** — et ses fausses preuves sociales sont interdites par les garde-fous.

### 3.2 Page produit kit (ordre §15 / content/page-produit-kit-tufting.md)

| Élément §15 | Offre FullStack | Verdict |
|---|---|---|
| Galerie 7 images | `_product-media-gallery` statique (carrousel + vignettes) | ✅ natif |
| Rating-row (masqué si 0 avis) | `rating-stars` natif = note saisie à la main (préréglé 4,5/123 → interdit) ; custom Horizon = valeurs en dur | 🔧 bloc `custom-code` avec `rating-row` adapté, **absent/masqué au lancement** ; ne jamais utiliser le preset natif |
| Titre + sous-titre | blocs `text` (`{{ closest.product.title }}`) | ✅ natif |
| Prix sans barré | `product-price` | ✅ natif |
| Paiement fractionné PayPal/Klarna `[[si actif]]` | rien de natif équivalent | 🔧 `dp-purchase-support` (partie paiement) ou `custom-code` `payment-installments` ré-hébergé (logos à réimporter, plus de CDN Bonum Vitae) |
| 4 bénéfices icônes (spécifiques tufting) | `icon-with-text` natif OU `dp-purchase-support` (bénéfices) | ✅/🔧 — textes du doc contenu, **ne pas recycler l'osmoseur** |
| Séparateur | bloc `separator` | ✅ natif |
| Sélecteur couleur | `_product-variant-picker` (boutons/swatches) | ✅ natif |
| Barre de livraison | **`delivery-estimation` natif (bloc + JS)** — préférable au `delivery-bar.liquid` Horizon (date fictive « +6 jours ») | ✅ natif, paramétré sur délais constatés `[[à confirmer]]` |
| Quantité + Ajouter au panier + Acheter maintenant | `_product-add-to-cart-button` + `_accelerated-checkout` | ✅ natif |
| Réassurance + contact | `dp-reassurance` ou `custom-code` `reassurance-block` (coordonnées Tuftéo réelles) | 🔧 portable-kit |
| Accordéons (description dyn., livraison/retour, fabrication, garantie, contact) | bloc `accordions` + `text` `{{ closest.product.description }}` | ✅ natif — contenus réécrits Tuftéo |
| — Sous la flottaison — | | |
| « Ta première pièce en 5 étapes » | `custom-section` (groupes texte/image) ou `stories`/`tabs` | ✅ natif |
| « Ce qu'il y a dans la boîte » | `custom-section` + `image` (photo échantillon) ou bloc `this-pack-contains` | ✅ natif |
| Comparatif honnête | **`comparison-table` natif** | ✅ natif |
| Entretien (goutte d'huile) | `custom-section` | ✅ natif |
| FAQ 7 objections | `accordions` ou `dp-faq` | ✅/🔧 |
| Avis clients (posés dès le build, masqués si vides) | — | 🔧 `bv-avis-clients` |
| Cross-sell | `product-recommendations` natif (ou `cross-sell`) | ✅ natif |

### 3.3 Page accessoire (`product.accessoire.json`)
Tout est natif : galerie + titre + prix + 2 `icon-with-text` + ATC → `text` description → `product-recommendations` (« Va bien avec » → kit) → réassurance compacte. Aucun portage supplémentaire.

---

## 4. Fichiers à créer ou porter (avec source locale)

| # | Fichier cible dans le thème | Source de référence | Adaptations |
|---|---|---|---|
| 1 | `sections/bv-avis-clients.liquid` | `docs/horizon-product-page-reference/sections/bv-avis-clients.liquid` (copie identique côté `homepage/sections/`) | couleurs → palette Tuftéo ; polices → Fraunces/Nunito Sans ou variables FullStack ; **ajouter un garde `{% if section.blocks.size == 0 %}` pour masquer la section vide** (le code actuel rend le titre même sans avis) ; titre par défaut Tuftéo ; badge « Vérifié » réservé aux avis réels |
| 2 | `sections/dp-purchase-support.liquid` | `boutique-tufting/shopify/portable-kit/sections/` | bénéfices = les 4 du kit tufting (preset actuel = osmoseur, à remplacer) ; paiement fractionné affiché seulement si actif ; livraison = délais constatés |
| 3 | `sections/dp-reassurance.liquid` | portable-kit | politiques réelles Tuftéo (retours, garantie légale, contact) |
| 4 | `sections/dp-faq.liquid` | portable-kit | questions du doc contenu §C.5 |
| 5 | `snippets/dp-icon.liquid` | portable-kit | tel quel |
| 6 | `locales/fr.default.json` (+ en, de) | portable-kit `locales/*` | **fusionner** les clés `dropilot` dans les locales FullStack, ne pas écraser |
| 7 | bloc `custom-code` « rating-row » | `custom-liquid/rating-row.liquid` | note/nb d'avis dynamiques ou à jour manuellement, image d'étoiles réimportée (CDN Bonum Vitae interdit), ancre vers la section avis FullStack ; **absent tant que 0 avis** |
| 8 | bloc `custom-code` « payment-installments » (si retenu au lieu de dp-purchase-support) | `custom-liquid/payment-installments.liquid` | logos PayPal/Klarna réimportés dans les fichiers de la boutique ; format prix locale FR ; seulement si le fractionné est réellement actif |
| 9 | Templates : `product.kit-tufting.json`, `product.accessoire.json`, refonte `index.json` | ordre : `content/page-produit-kit-tufting.md` + `sitemap.md` ; le JSON Horizon (`templates/product.osmoseur.json`) sert de **plan de lecture seulement**, jamais de copie | reconstruits avec les types de sections/blocs FullStack ci-dessus |

Non retenus pour portage : `delivery-bar.liquid` (remplacé par `delivery-estimation` natif, plus honnête), `benefits-osmoseur.liquid` (produit différent), `blocks/buy-buttons.liquid` Horizon (ATC FullStack natif suffit), le kit `cart/` Horizon (le drawer FullStack est complet : progress bar, code promo, note, cross-sell — configuration plutôt que portage ; à traiter en phase panier).

**Total : 4 sections + 1 snippet + 3 fichiers de locales à fusionner + 2 blocs custom-code + 3 templates JSON à construire.**

---

## 5. Risques

1. **Démo FullStack truffée d'éléments interdits par les garde-fous** : `rating-stars` prérempli 4,5/123 avis, « - 2 000 clients satisfaits », « 96 % de clients satisfaits », 12 faux avis « Excellent produit ! » (product.json + index.json), accordéons « Fabrication » génériques. Purge obligatoire avant toute mise en ligne — c'est le risque n°1 de fuite d'une fausse preuve sociale.
2. **`config/settings_data.json` contient des restes du vendeur du thème** : logo FullStack, `instagram_url` themefullstack, et surtout **`klaviyo_enabled: true` avec une clé API publique Klaviyo étrangère** (`pk_ec8555…`) — à désactiver/remplacer avant publication (tracking tiers).
3. **Licence thème** : thème payant hors Theme Store, nom « copie-de- » → vérifier que la licence FullStack couvre cette boutique (à confirmer par Hakim).
4. **Schema/settings** : les customs Horizon ne connaissent pas les `color_scheme` FullStack ; en bloc `custom-code`, les styles inline s'appliquent mais peuvent jurer avec le scheme parent. Uniformiser via la palette Tuftéo au portage. Vérifier `snippets/css-variables.liquid` pour les noms exacts de variables typo.
5. **Traductions** : schéma du thème traduit (clés `t:`) avec fr par défaut — OK ; mais les customs portés sont en dur en français (assumé, boutique FR) ; fusion des locales `dropilot` à faire proprement (risque d'écrasement).
6. **Mobile** : sticky galerie + sticky colonne + carrousel plein écran mobile FullStack — les customs (grille réassurance 3 colonnes, barre livraison, carrousel avis scroll-snap) ont été stylés pour Horizon → QA mobile systématique (breakpoint FullStack : 750 px, identique à la référence).
7. **Typo par défaut Poppins** ≠ charte Tuftéo (Fraunces/Nunito Sans) : à reconfigurer dans les settings (le thème supporte les polices Shopify + custom).
8. **`custom-section.liquid` = 260 Ko** de Liquid générique : sections lourdes à l'édition ; sans impact bloquant, mais surveiller la performance de rendu sur la home à 11 sections.
9. **Paiement fractionné** : ne l'afficher que si PayPal/Klarna réellement actifs sur la boutique (état des paiements à confirmer — non vérifié dans cette mission, hors périmètre thème).

## 6. À confirmer (par Hakim ou en phase build)

- Licence FullStack pour cette boutique.
- Thème cible définitif = ce brouillon FullStack (le sitemap listait encore « thème cible : Horizon ou autre » comme point ouvert — ce rapport documente l'option FullStack).
- Paiement fractionné actif ou non ; politique retours ; prix final 229 €.
- Délais de livraison constatés pour paramétrer `delivery-estimation`.
- Choix avis : bv-avis-clients porté (recommandé, contrôle total + amendement Hakim) vs section `reviews` native (à vider de ses presets si utilisée) — ne garder qu'UN système.
- Noms exacts des variables CSS FullStack (lecture de `snippets/css-variables.liquid` en début de build).
- Comportement de `main-product.liquid` avec blocs `custom-code` imbriqués dans `_product-form` (ordre §15 : barre livraison entre variantes et ATC) — à tester dans l'éditeur.

## 7. Plan de portage ordonné (phase build)

1. **Nettoyage de la base** (sur le brouillon uniquement) : purge des placeholders/faux avis/fausses stats des templates démo ; nettoyage settings_data (logo, Instagram, clé Klaviyo) ; application brand-tokens (couleurs, Fraunces/Nunito Sans, radius à arbitrer).
2. **Portage du socle réutilisable** : copie du portable-kit (4 fichiers + fusion locales), création de `sections/bv-avis-clients.liquid` adaptée (garde « masquée si vide »). Import des assets (logos paiement, étoiles) dans les fichiers de la boutique.
3. **Template `product.kit-tufting.json`** : duplication du `product.json` FullStack, recomposition dans l'ordre §15 (colonne d'achat), puis sections sous la flottaison (5 étapes, boîte, `comparison-table`, entretien, FAQ, bv-avis-clients vide, recommandations). Textes depuis `content/page-produit-kit-tufting.md` (les `[[ ]]` restent des trous tant que l'échantillon n'est pas contrôlé).
4. **Template `product.accessoire.json`** : version courte 100 % native.
5. **Refonte `index.json`** : 11 sections du sitemap avec les natifs mappés en §3.1 + bv-avis-clients vide en position 9.
6. **Header / footer / navigation** : menu 6 entrées, footer sitemap, announcement-bar vide, drawer panier configuré (ouverture auto déjà active).
7. **QA** : mobile 750 px, variantes/prix/panier, absence totale de fausses preuves, accessibilité des accordéons/carrousels, Lighthouse.
8. **Rien n'est publié** : le thème reste brouillon jusqu'à la levée des `[[ ]]` et décision Hakim (le publié Horizon n'est pas touché).
