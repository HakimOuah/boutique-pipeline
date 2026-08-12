# Audit UI/UX — page produit Maison Noirmont

Boutique `v42pzp-h4` (domaine réel `maisonnoirmont.fr`) · thème `204248088914` **MAIN** · audit **lecture seule**, aucune écriture thème, aucune mutation.
Fiche de référence : `/products/contre-la-montre-panda-inverse-chronographe`.
Référentiels appliqués : Web Interface Guidelines (vercel-labs) + ui-ux-pro-max (`ux`, `typography`, `color`, `icons`, `quick-reference.md`).

**Intégrité des fichiers** — appariement nom ↔ contenu validé par `checksumMd5` sur les 25 fichiers audités, md5 recalculé localement après téléchargement. `templates/product.json` = `027c56cee94730e31dffb2808b617a46`, contenu confirmé sémantiquement comme template produit (blocs `_product-form`, `_product-variant-picker`, `_product-media-gallery` présents ; aucune trace d'`index.json`). Le bug d'appariement de l'API ne s'est pas reproduit.

**Boutique protégée par mot de passe.** Aucun mot de passe n'a été saisi ; la session navigateur était déjà en staff preview. Les mesures live sont donc valides, mais une barre de prévisualisation Shopify de 68 px masquait le bas du viewport (emplacement de la barre d'achat collante).

---

## templates/product.json

- `templates/product.json:56` - titre produit balisé `<p>{{ product.title }}</p>` avec `text_style: "h3"` → **la page produit n'a aucun `<h1>`** (`h1Count: 0` vérifié live). Le nom du produit n'existe que comme paragraphe stylé 24 px/500.
- `templates/product.json:286,326,366,406,446` - les 5 accordéons de la colonne produit sont en `heading_tag: "p"` → aucun titre navigable, la structure de la fiche est invisible au lecteur d'écran et aux moteurs.
- `templates/product.json:862 / 968 / 1270 / 1395` - hiérarchie de titres live : H3 → H2 → H2 → H2 → **H4** → H3. Le document démarre au niveau H3 (« Ils portent Noirmont »), sans H1 ni H2 avant. Un seul véritable saut de niveau au sens WCAG : **H2 « Pourquoi ce prix ? » → H4 « Besoin d'aide ? »**, le niveau H3 est sauté. Les transitions montantes H3→H2 et H4→H3 ne sont pas des sauts et ne sont pas comptées.
- `templates/product.json:16-49` - `reviews-badge` puis `rating-stars` placés **avant** le titre (`block_order` :529-541). Sur mobile le premier texte lu après l'image est un badge d'avis, pas le nom du produit.
- `templates/product.json:378` (dupliqué `:1520`) - l'appareil pédagogique de spécifications est renvoyé à plus tard : « le calibre exact, le diamètre du boîtier […] sont indiqués sur chaque fiche ». Le `39 mm` n'apparaît que dans une puce de l'accordéon Description, soit en **10ᵉ position** de la colonne, après le bouton d'achat — la direction A+B le veut **sous le titre**.
- `templates/product.json:80` - `sales_badge: "percentage"` cumulé au badge galerie `EN PROMOTION` (`:523 show_badges: true`), au prix barré et à la répétition du prix barré dans le bouton → **4 signaux de remise pour un seul fait**, sur la quasi-totalité du catalogue.
- `templates/product.json:173` - `Lorem ipsum dolor sit amet…` stocké dans le popup « Guide des tailles » (bloc parent `disabled: true` :131, donc invisible, mais le texte reste dans le template publié).
- `templates/product.json:150` - `<h1>Guide des tailles</h1>` en dur dans ce même popup enfant du sélecteur de variantes : le seul `<h1>` du template est sémantiquement au mauvais endroit.
- `templates/product.json:212` - `preorder_cart_message: "Livraison à partir du JJ/MM"` → placeholder de date non résolu (bloc préco désactivé, `:210`).
- `templates/product.json:250-252` - le `block_order` de `_product-form` ne contient que le sélecteur de variantes ; bouton d'achat et checkout accéléré sont rendus par `content_for` statique (`blocks/_product-form.liquid:21-22`) et donc **non réordonnables dans l'éditeur**.
- `templates/product.json:235` - `_accelerated-checkout` `disabled: true` → aucun Shop Pay / Apple Pay / Google Pay sur la fiche. Un seul chemin d'achat.
- `templates/product.json:216` - `_product-quantity-selector` `disabled: true` (cohérent pour un article unitaire, signalé pour mémoire).
- `templates/product.json:549-550` - `carrousel_sticky: false` **et** `product_info_sticky: false` : sur desktop la colonne d'achat défile et disparaît, alors que la galerie fait 600 px.
- `templates/product.json:338` et `:1440` - « Comptez généralement **2 à 3 semaines** pour la recevoir », texte dupliqué à l'identique dans la FAQ bas de page. Formulation en semaines, cohérente en ordre de grandeur avec J+14/J+21 mais non alignée sur les dates calculées affichées juste au-dessus.
- `templates/product.json:378,418,991,1600` - promesses génériques en dur, non liées à la variante affichée : liste de calibres (`Seiko NH35, NH34, VK63, Miyota 8215, Mingzhu 2813, PT5000, DG3804`), « garanti 12 mois », « un boîtier acier », « si votre montre est automatique… ». À vérifier fiche par fiche avant tout trafic payant.

## blocks/noirmont-livraison.liquid

- `blocks/noirmont-livraison.liquid:2` et `:96` - `min_days` par défaut à **12** (fallback Liquid *et* défaut de schéma) alors que la règle maison est **J+14**. Le template corrige à 14 (`product.json:257`), mais toute réinitialisation du bloc ou tout nouvel ajout affichera J+12. Seule contradiction de délai codée en dur trouvée.
- `blocks/noirmont-livraison.liquid:31-33,42,52,57` - `rgba(30,58,47,…)` et `#1E3A2F` : fond, bordure, puce et mention « LIVRAISON GRATUITE » en **vert forêt**. Hors direction A+B (encre / craie / un seul accent citron `#D6FF3F`).
- `blocks/noirmont-livraison.liquid:19-23` - dates rendues en `<strong>` sans `font-variant-numeric: tabular-nums`, sans `<time datetime>`, et sans conteneur `aria-live` malgré un contenu qui change de variante à variante.
- `blocks/noirmont-livraison.liquid:9-12` - noms de mois français codés en dur dans un tableau Liquid, alors que le thème embarque 6 locales (`locales/de|en|es|it|pl`). Le bandeau restera en français quelle que soit la langue. WIG : formater les dates via l'API d'internationalisation, jamais en dur.
- `blocks/noirmont-livraison.liquid:3-8` - dates calculées côté Liquid depuis `'now'`. Le rendu est mis en cache par Shopify : la fourchette affichée peut dater de plusieurs heures, voire d'un jour, sans que rien ne le signale.
- `blocks/noirmont-livraison.liquid:37` - `font-size: 0.92rem` → **14,72 px** mesuré, et `:56` `0.8rem` → **12,8 px** pour « LIVRAISON GRATUITE ». Sous le plancher de 16 px sur mobile.
- Vérification live : « Livraison estimée entre le **9 août** et le **16 août** » au 26/07/2026 → **J+14 / J+21 exacts**. Le calcul est juste ; c'est le défaut du schéma qui est à corriger.

## snippets/product-option-value-button.liquid + snippets/css-variables.liquid

- `snippets/css-variables.liquid:368` - `--variant-button-min-height: 40px` → pastilles de variantes mesurées **87×40** et **95×40** px. Sous le minimum de 44×44. C'est le contrôle décisif de la fiche.
- `snippets/css-variables.liquid:390` - `--swatches-size: 30px` → si les pastilles couleur passaient un jour par le mécanisme swatch, elles feraient **30×30** px, très en dessous du seuil.
- `snippets/css-variables.liquid:355` - `--gap-sm: 0.5rem` = 8 px, appliqué à `.variant-picker__option-values` : pile au minimum, avec des cibles déjà trop courtes. Aucune marge d'erreur au pouce.
- `snippets/product-option-value-button.liquid:42` - `outline: 1px solid transparent` posé en permanence, et **aucune règle `:focus-visible` dans tout le fichier** (lignes 21-80) → focus clavier invisible sur les pastilles (vérifié live : `outlineColor: rgba(0,0,0,0)`, `boxShadow: none`).
- `snippets/product-option-value-button.liquid:43` - `transition: all …` : anti-patron WIG explicite, et anime des propriétés de layout.
- `snippets/product-option-value-button.liquid:7-9,60` - indisponibilité portée par `aria-disabled="true"` au lieu de `disabled` : la valeur reste sélectionnable et focusable, avec `opacity: 0.5` (`:62`) qui dégrade encore le contraste.
- Aucun `touch-action: manipulation` sur les pastilles ni sur `body` (vérifié live : `auto` partout) → délai de tap de 300 ms conservé sur le contrôle le plus manipulé de la page.

## snippets/product-swatches.liquid + snippets/swatch.liquid

- `snippets/product-swatches.liquid:19-184` - **`show_swatches: true` (`product.json:118`) est sans effet.** Les trois sources de pastilles sont vides sur le catalogue : `optionValues[].swatch = null` (pas de swatch natif), pas de métachamp `custom.colors` sur le produit (les métachamps réels sont `custom.famille`, `custom.diametre`, `custom.calibre`, `custom.couleur_cadran`, tous `list.single_line_text_field`), et métachamps de variante vides. Le rendu retombe donc sur `product-option-value-button` (`:180-182`). Les métaobjets `dial-color`/`case-color` **ne sont pas branchés** au mécanisme swatch du thème.
- Conséquence favorable à signaler : les variantes s'affichent aujourd'hui en **texte** (« Acier », « Rouge »), pas en pastille de couleur muette. Le risque d'accessibilité « pastille sans libellé » n'est donc **pas** matérialisé — mais il l'est immédiatement dès que les swatches seront branchés, voir les deux points suivants.
- `snippets/swatch.liquid:53` - `aria-label="{{ name }}"` : le nom accessible reçoit le **nom du groupe** (`option-Couleur du cadran`), identique pour toutes les pastilles. La **valeur** n'est jamais annoncée. Défaut latent bloquant dès activation.
- `snippets/swatch.liquid:74` - la pastille est un `<span>` sans texte, porteur d'un seul `--swatch-background` → information transmise par la couleur seule, sans libellé ni `title`.
- `snippets/product-swatches.liquid:132-135` - le chemin métachamps de variante n'active les pastilles que si le nom d'option correspond **exactement** à un alias de la liste (`color, colors, couleur, …`). Une option nommée « Couleur du cadran » ou « Coloris de boîtier » ne matchera jamais.
- `snippets/swatches.liquid:36` - `overflow-x: auto` sur le conteneur de pastilles : zone de défilement horizontal imbriquée, sans affordance ni indicateur, à l'intérieur d'une page à défilement vertical.
- `snippets/swatch.liquid:37-47` - variante carte produit : `<span role="button" tabindex="0">` avec `data-href` mais **aucun gestionnaire clavier**, et `aria-checked` sur `role="button"` (attribut non valide pour ce rôle). Deux anti-patrons WIG.

## blocks/_product-variant-picker.liquid

- `blocks/_product-variant-picker.liquid:73` - `<fieldset>` ouvert sans `<legend>` (confirmé live : `fieldset legend → 0`, `aria-label → null`). Le nom de l'option est un `<div>` décoratif (`:75-77`) → le groupe de boutons radio n'a **aucune étiquette programmatique**.
- `blocks/_product-variant-picker.liquid:45-52` - branche `selects` : `aria-disabled="true"` sur des `<option>`, où seul `disabled` est reconnu.
- `blocks/_product-variant-picker.liquid:9` - le sélecteur entier disparaît si `has_only_default_variant` : sur les fiches mono-variante, la ligne d'options s'efface et la colonne se recompose. Cohérence de gabarit à vérifier sur la famille `trente-neuf-*`.

## blocks/_product-add-to-cart-button.liquid + assets/sticky-add-to-cart.js

- `blocks/_product-add-to-cart-button.liquid:112-116` - **il n'existe qu'un seul bouton d'ajout au panier sur la page** (`[name="add"]` → 1 occurrence live), et il vit à l'intérieur de `<sticky-add-to-cart>`. Il n'y a pas un bouton en flux *plus* une barre collante : c'est le même élément qui bascule entre `static` et `fixed`.
- `blocks/_product-add-to-cart-button.liquid:137-143` - la bascule `data-active` fait passer l'élément de `static` à `position: fixed` : il **quitte le flux**, la colonne d'achat se referme de ~50 px et le contenu saute. Décalage de mise en page à chaque activation.
- `blocks/_product-add-to-cart-button.liquid:138` - `bottom: -150px` appliqué à un élément resté `static` : sans effet. L'état inactif ne glisse pas, il claque.
- `assets/sticky-add-to-cart.js:29` - `isElementInViewport(this.form) || isElementInViewport(this.footer)` : la cible testée est le formulaire **qui contient le bouton lui-même** (`:12`), et un pied de page de 25 Ko souvent partiellement visible. Logique instable par construction. **Constat live : au chargement `data-active="true"`, puis après défilement l'élément est resté `data-active="false"` sur 10 positions testées jusqu'à 4000 px, sans jamais se réactiver.** Le scroll réel au doigt n'a pas pu être simulé (barre de prévisualisation) → à confirmer sur téléphone, mais la cause côté code est identifiée.
- `assets/sticky-add-to-cart.js:17` - écouteur `scroll` sans `{ passive: true }`, sans throttle ni `requestAnimationFrame` : lecture de layout à chaque événement de défilement.
- `assets/sticky-add-to-cart.js:22-26` - `disconnectedCallback` appelle `removeEventListener` avec une **nouvelle fonction anonyme** : l'écouteur n'est jamais retiré (fuite à chaque navigation instantanée).
- Position en flux mesurée : bouton d'achat à **903 px** du haut du document, soit **1,11 hauteur d'écran** à faire défiler. Above the fold en 375×812, on ne voit ni les pastilles, ni le bouton, ni le bandeau livraison — la page est coupée juste après le prix.
- `blocks/_product-add-to-cart-button.liquid:95` - `<span class="button__separator">|</span>` sans `aria-hidden="true"`, et `snippets/price.liquid:78` `<span class="compare-at-price">` sans `aria-hidden` non plus. Le bouton n'a pas d'`aria-label` : son nom accessible dérive entièrement de son contenu et vaut **« Ajouter au panier | €299 €389 »**. Un utilisateur non voyant entend deux montants à la suite, à plat, **sans aucune indication que 389 est un ancien prix**.
- `blocks/_product-add-to-cart-button.liquid:97` - `{% render 'price' %}` dans le bouton → le CTA affiche « AJOUTER AU PANIER | €299 €389 », donc **le prix barré est répété une seconde fois dans l'appel à l'action**, avec le même style que le prix courant.
- Nuance à conserver : le second libellé « Ajouter » (`:89-91`) est en `display: none`, donc exclu de l'arbre d'accessibilité — ce n'est **pas** un doublon audible.
- `blocks/_product-add-to-cart-button.liquid:106` - le spinner de chargement n'est accompagné d'aucune région `aria-live` ni `aria-busy` : l'ajout au panier ne s'annonce pas.
- `blocks/_product-add-to-cart-button.liquid:187` - `transition: all … !important` (bloc Klaviyo) : anti-patron WIG.
- Aucune règle `:focus` / `:focus-visible` ciblant `.button` dans les 1905 règles lisibles ; `.button` porte `outline: transparent solid 1px` en permanence → **focus clavier invisible sur le bouton d'achat** (`outlineColor: rgba(0,0,0,0)`, `boxShadow: none` mesurés au focus).

## snippets/price.liquid + blocks/product-price.liquid

- `snippets/price.liquid:68-83` - `.price` et `.compare-at-price` sont deux `<span>` de même niveau, sans `<s>`/`<del>`, sans libellé masqué (« Prix habituel », « Prix soldé »). Mesuré live : **couleur, taille et graisse identiques** (`#0B0B0C`, 16 px, 400) ; seul `line-through` distingue les deux. Contraste 18,81:1 pour les deux — le problème n'est pas la lisibilité, c'est l'**absence totale de dé-emphase** : « €299 €389 −23% » se lit comme une seule chaîne plate.
- `snippets/price.liquid:64-99` - **aucun `font-variant-numeric: tabular-nums`**. Vérifié sur toute la page : `0` élément en chiffres tabulaires (prix, prix barré, badge −23 %, montant 4×, dates de livraison, compteur d'avis). Chaque changement de variante peut décaler la ligne de prix. Exigence explicite de la charte, non tenue.
- `snippets/price.liquid:68` - le `<span class="compare-at-price">` est **toujours rendu**, même vide, y compris hors promotion → nœud parasite dans l'ordre de lecture.
- `snippets/price.liquid:47` - remise en pourcentage calculée avec `round` sans garde : sur un `compare_at_price` nul ou égal, la valeur peut dégénérer.
- `snippets/price.liquid:87-97` - badge de remise sans texte (`show_sales_badge_text: false`, `product.json:81`) : « −23 % » sort nu, sans « Économisez », donc sans dire de quoi le pourcentage est retranché.

## blocks/_product-media-gallery.liquid + snippets/product-media.liquid

- `snippets/product-media.liquid:26` - `image_tag` appelé **sans `loading:`, sans `sizes` et sans `fetchpriority:`**. Mesuré live sur la première image : les trois attributs sont absents. `image_url: width: 1200` plafonne la base, donc le `srcset` réellement émis offre **7 candidats de 300w à 1200w** (la liste `widths` de `:17` monte à 5000 mais est tronquée par ce plafond).
- `snippets/product-media.liquid:26` - **sans `sizes`, la valeur par défaut est `100vw`** → le navigateur retient la plus grande largeur disponible : `…&width=1200` chargé pour un rendu de **375 × 375 CSS px**, soit **3,2× la taille utile**.
- `snippets/product-media.liquid:26` - aucune image de la galerie ne porte `loading="lazy"` : **les 6 images du slider sont toutes chargées en 1200 px**, donc cinq images invisibles téléchargées en pleine résolution sur mobile. Aucun `<link rel="preload" as="image">` non plus.
- Correction attendue : le trio `sizes` + `fetchpriority="high"` sur la première image + `loading="lazy"` sur les suivantes.
- ⚠️ Réserve : `performance.getEntriesByType('largest-contentful-paint')` ne renvoie rien dans ce contexte. L'élément LCP est **identifié par position et par surface** (image carrée en tête, 46 % de la hauteur d'écran), **pas confirmé par l'API**.
- `blocks/_product-media-gallery.liquid:65,68` - flèches de carrousel : `<button>` sans `aria-label` et sans `type="button"`. Splide retombe sur ses libellés anglais → **« Next slide », « Go to slide 1 », « Go to last slide » sur une boutique française** (vérifié live).
- `blocks/_product-media-gallery.liquid:144` - vignettes de 70×70 px (conformes au seuil tactile), mais les vignettes 5 et 6 portent `tabindex="-1"` → inatteignables au clavier.
- `blocks/_product-media-gallery.liquid:62,128` - `role="group"` sur les deux sliders sans `aria-label` ni `aria-roledescription` : deux groupes anonymes annoncés à la suite.
- Aucun `touch-action: manipulation` sur la galerie ni sur `.splide__track` (`auto` mesuré).
- Points conformes, pour mémoire : `alt` renseigné et descriptif sur **38/38** images, `width`/`height` explicites et `aspect-ratio: 1/1` sur toutes → aucun décalage de mise en page à l'image. `0` erreur console.

## snippets/accordion.liquid

- `snippets/accordion.liquid:79-84` - `.accordion__header` en `padding: var(--margin-sm) 0` sans `min-height` → en-têtes mesurés **335×40** px sur les 6 accordéons. Sous 44 px, alors que c'est le seul mécanisme de lecture du contenu de la fiche.
- `snippets/accordion.liquid:53-56` - avec `heading_tag: "p"` (valeur retenue dans `product.json`), le `<summary>` ne contient qu'un `<p>` : aucun titre exposé.
- `snippets/accordion.liquid:23` - `<details>` natif : ouverture/fermeture clavier correcte, et `open_by_default: true` sur « Description » uniquement. Base saine, c'est la taille de cible qui est en cause.

## blocks/noirmont-4x.liquid

- `blocks/noirmont-4x.liquid:47` - `background: rgba(169, 142, 95, 0.12)` : accent **laiton** sur le badge Klarna. Hors direction A+B.
- `blocks/noirmont-4x.liquid:4` - `nm_variant.price | divided_by: nm_count` : division entière tronquée. Sur un prix non divisible par 4, la somme des 4 mensualités affichées peut être inférieure au prix de jusqu'à 3 centimes.
- `blocks/noirmont-4x.liquid:12-13` - montant sans chiffres tabulaires ; « 4 × » sans espace insécable ; `PayPal` / `Klarna` sans `translate="no"`.
- `blocks/noirmont-4x.liquid:15-18` - noms de prestataires saisis en texte libre, sans lien avec les moyens de paiement réellement activés sur la boutique. **À confirmer que PayPal 4× et Klarna sont bien disponibles au checkout** avant d'annoncer les deux : une mention non honorée au paiement est un abandon garanti.
- `blocks/noirmont-4x.liquid:28` - `font-size: 0.95rem` → 15,2 px mesuré, sous 16 px.

## blocks/noirmont-confiance.liquid

- `blocks/noirmont-confiance.liquid:75` - `color: #1E3A2F` sur les 4 icônes : vert forêt, hors direction.
- `blocks/noirmont-confiance.liquid:91-92` - `rgba(169,142,95,0.10)` / `0.35` sur la carte contact : accent laiton, hors direction.
- `blocks/noirmont-confiance.liquid:68-71` - `font-size: 0.82rem` **+ `opacity: 0.75`** → **13,12 px atténué** mesuré sur les 4 paragraphes. Double pénalité de lisibilité sur le bloc de réassurance, juste après le CTA.
- `blocks/noirmont-confiance.liquid:26` - « Mouvement, couronne, aiguilles : on répare ou on remplace » : promesse de service impliquant un atelier. À valider contre la réalité opérationnelle avant diffusion payante.
- `blocks/noirmont-confiance.liquid:29` - carte entière en `<a href="mailto:">` sans indication visuelle de lien ni `aria-label` : la seule carte cliquable des quatre est indiscernable des trois autres.

## assets/noirmont-custom.css

- `assets/noirmont-custom.css:113` - `border: 1px solid rgba(169, 142, 95, 0.55)` sur le badge « EN PROMOTION » : troisième point d'entrée du laiton. Commentaire du fichier (`:107`) : « le laiton (#A98E5F) — l'accent de la maison » → **le fichier documente un accent qui contredit la direction A+B retenue**.
- `assets/noirmont-custom.css:21-25` - le fichier surcharge `--font-body--size` en `:root` alors qu'un réglage éditeur équivalent existe (documenté `:16-18`) : deux sources de vérité pour la taille du corps de texte.
- `assets/noirmont-custom.css:1-151` - la feuille traite le corps de texte, les cartes produit, la grille de collection et le badge, mais **rien pour la page produit elle-même** : ni taille de pastille, ni chiffres tabulaires, ni focus. Les correctifs de la fiche n'ont pas de point d'accroche existant.

## Direction créative A+B — écart global

- **`#D6FF3F` : 0 occurrence sur toute la page.** Zéro variable CSS, zéro élément calculé, zéro règle dans les 1905 règles lisibles. L'accent citron acide unique de la direction retenue **n'est pas appliqué du tout**.
- À sa place, deux accents non prévus : **vert forêt `#1E3A2F` sur 31 éléments** (bouton d'ajout au panier, bandeau livraison, puce, icônes de confiance, bulle du panier) et **laiton `#A98E5F` sur 5 éléments** (badge promo, badge 4×, carte contact).
- Encre `#0B0B0C` et craie `#FAFAF7` sont conformes. Contrastes mesurés tous largement au-dessus du seuil (bouton 11,80:1 · message livraison 16,94:1 · mention gratuite 10,63:1). **Le problème n'est pas l'accessibilité des couleurs, c'est l'identité :** la fiche est en trichromie vert/laiton/encre, pas en encre/craie + un accent citron.
- Pastille sélectionnée signalée par un remplissage encre `#0B0B0C`, pas par l'accent : l'état sélectionné n'a aucune couleur propre.

## Hors périmètre — signalé sans être audité

- `templates/product.json:802` - un avis de démonstration mentionne « **verre saphir** ». C'est précisément le type de promesse matière non vérifiable à écarter. Les avis relèvent de Hakim ; ce point est reporté à titre de veille véracité, sans recommandation de formulation.
- Bandeau d'annonce du header (`.splide__track` en `overflow: visible`, liste translatée de −229,56 px pour `activeIndex 0`) : deux messages tronqués simultanément et une flèche par-dessus le texte, état stable sur 8 échantillons / 5,6 s, identique en 1280. Ce n'est pas un slider de démonstration mais un défaut de mise en page, et c'est **le premier élément vu sur la fiche**. Reporté ici car hors bloc produit.
- Aucun débordement horizontal du document : `scrollWidth == innerWidth` en 375 **et** en 1280. Point conforme.

---

# Classement par impact conversion

## BLOQUANT — 4

| # | Point | Justification |
|---|---|---|
| 1 | Bouton d'achat unique, collant instable (`assets/sticky-add-to-cart.js:29`, `blocks/_product-add-to-cart-button.liquid:112`) | Il n'y a qu'un seul bouton d'ajout au panier, à 903 px du haut, et le mécanisme censé le ramener au pouce teste un conteneur qui l'englobe : observé bloqué en position inactive sur tout le défilement. Si le collant ne remonte pas sur mobile, l'achat dépend d'un retour en arrière volontaire de l'utilisateur. |
| 2 | Pastilles de variantes à 40 px de haut, espacées de 8 px, sans focus visible (`snippets/css-variables.liquid:368,355`, `snippets/product-option-value-button.liquid:42`) | Le choix de variante est obligatoire avant l'ajout au panier. La cible est sous le seuil de 44 px, à l'écart minimum, sans retour au clavier et sans `touch-action` — mis-taps et sélections involontaires sur le seul contrôle qu'on ne peut pas contourner. |
| 3 | Aucun `<h1>` sur la page produit (`templates/product.json:56`) | Le nom du produit n'est qu'un `<p>`, les 5 accordéons sont en `<p>`, et la première balise de titre de la page est un `H3` d'avis. La fiche n'a pas de titre pour Google ni pour un lecteur d'écran : cela pèse sur l'acquisition organique et sur l'accessibilité, à la racine. |
| 4 | Prix barré strictement identique au prix courant, sans chiffres tabulaires (`snippets/price.liquid:68-83`) | Même encre, même taille, même graisse : la remise ne se voit pas, l'ancrage de prix ne travaille pas, et « €299 €389 −23% » peut se lire comme un prix unique confus. C'est le premier élément visible au-dessus de la ligne de flottaison après le titre. |

## FORT — 7

| # | Point | Justification |
|---|---|---|
| 5 | Accent citron `#D6FF3F` totalement absent, remplacé par vert forêt + laiton (31 + 5 éléments) | La direction A+B validée n'est pas implémentée : la fiche présente une identité différente de celle décidée, y compris sur le bouton d'achat, et l'état sélectionné n'a aucune couleur d'accent propre. |
| 6 | Empilement de 4 signaux de remise permanents (`templates/product.json:80`, `:523`, `assets/noirmont-custom.css:113`) | « EN PROMOTION » + « −23 % » + prix barré + prix barré répété dans le CTA, sur la quasi-totalité du catalogue et en permanence : le point ouvert se tranche contre la crédibilité. À vérifier aussi au regard de la règle française du prix de référence (prix le plus bas des 30 jours précédents) — une boutique neuve n'a pas ce référentiel. |
| 7 | Spécifications pédagogiques reléguées en 10ᵉ position (`templates/product.json:378`, `:1520`) | Le `39 mm` / calibre / compteurs n'apparaît qu'après le bouton d'achat, dans un accordéon. La direction retenue les veut sous le titre : c'est l'argument qui justifie le prix, et il arrive après la décision. |
| 8 | Galerie chargée en 1200 px pour une boîte de 375 px, sans `sizes`, sans `fetchpriority`, sans `lazy` (`snippets/product-media.liquid:26`) | Sans `sizes`, le navigateur retient le plus grand candidat : 3,2× de données inutiles, et **les 6 images du slider** téléchargées en pleine résolution dont cinq invisibles. Sur mobile 4G, chaque dixième de seconde de LCP se paie en taux de rebond. Réserve : l'élément LCP est identifié par position et surface, non confirmé par l'API. |
| 9 | Aucun focus visible sur le bouton d'achat ni sur les pastilles (0 règle `:focus-visible` sur `.button` dans 1905 règles) | Le parcours d'achat complet est inutilisable au clavier sans deviner où l'on se trouve. Blocage d'accessibilité sur le tunnel, et anti-patron WIG explicite. |
| 10 | En-têtes d'accordéon à 40 px et textes de réassurance à 13,12 px à `opacity: 0.75` (`snippets/accordion.liquid:79`, `blocks/noirmont-confiance.liquid:68-71`) | Encre effective ≈ `#3E3E3F` : c'est le motif « gris sur gris » que les deux référentiels sanctionnent. Tout le contenu qui lève les objections — livraison, retours, garantie, calibres — est derrière des cibles trop petites, puis rendu sous le plancher mobile. |
| 11 | Nom accessible du bouton d'achat = « Ajouter au panier \| €299 €389 » (`blocks/_product-add-to-cart-button.liquid:95,97`, `snippets/price.liquid:78`) | Ni le séparateur `\|` ni le prix barré ne portent `aria-hidden`, et le bouton n'a pas d'`aria-label`. Un utilisateur non voyant entend deux montants à plat, sans savoir que 389 est un ancien prix : l'unique CTA de la page est mal annoncé. |

## MOYEN — 7

| # | Point | Justification |
|---|---|---|
| 12 | `min_days` par défaut à 12 dans le bloc livraison (`blocks/noirmont-livraison.liquid:2,96`) | Le template corrige à 14 et l'affichage live est exact (J+14/J+21), mais le défaut du schéma contredit la règle : toute réinitialisation ou tout nouvel ajout du bloc promettra J+12, donc une promesse de délai intenable. |
| 13 | `<fieldset>` sans `<legend>`, swatches à `aria-label` = nom du groupe (`blocks/_product-variant-picker.liquid:73`, `snippets/swatch.liquid:53`) | Le groupe de variantes n'a aucune étiquette programmatique. Aujourd'hui atténué par des libellés texte visibles ; devient bloquant dès que les pastilles couleur seront branchées, puisque la valeur ne serait jamais annoncée. |
| 14 | `show_swatches: true` sans effet, métaobjets `dial-color`/`case-color` non branchés (`snippets/product-swatches.liquid:19-184`) | Le réglage est activé mais aucune des trois sources de swatch n'est alimentée : les coloris s'affichent en texte. Écart entre l'intention produit et le rendu, et travail de métaobjets non exploité. |
| 15 | Corps de texte sous 16 px hors cartes de confiance (`blocks/noirmont-livraison.liquid:37,56`, `blocks/noirmont-4x.liquid:28`) | Bandeau de livraison à **14,72 px**, sa mention de gratuité à **12,8 px**, libellé du 4× à **15,2 px** — alors que racine et `body` sont bien à 16 px et que l'accordéon Description est conforme. Trois informations décisives sous le plancher mobile. |
| 16 | Aucun paiement accéléré (`templates/product.json:235`) | Shop Pay / Apple Pay / Google Pay désactivés : un seul chemin d'achat, sans l'option la plus rapide sur mobile, où elle pèse le plus. |
| 17 | Mentions PayPal / Klarna en texte libre (`blocks/noirmont-4x.liquid:15-18`) | Le bloc affirme deux prestataires de paiement fractionné sans lien avec ce qui est réellement activé au checkout. À confirmer : une promesse de 4× non honorée au paiement fait abandonner au dernier écran. |
| 18 | Colonne d'achat non collante sur desktop (`templates/product.json:549-550`) | Galerie de 600 px face à une colonne d'information plus courte : passé le premier écran, le bouton d'achat disparaît sans rien pour le rappeler. |

## FAIBLE — 7

| # | Point | Justification |
|---|---|---|
| 19 | `Lorem ipsum` et `<h1>Guide des tailles</h1>` stockés dans le popup désactivé (`templates/product.json:150,173`) | Invisible aujourd'hui (bloc parent `disabled`), mais du texte de démo et un `<h1>` mal placé restent dans un template publié : ils s'afficheront à la première réactivation du bloc. |
| 20 | Mois codés en dur en français, pas de `<time>`, pas d'`aria-live` (`blocks/noirmont-livraison.liquid:9-12,19-23`) | Le thème embarque 6 locales ; le bandeau restera francophone. Impact nul tant que la boutique est mono-marché. |
| 21 | Dates de livraison calculées en Liquid et mises en cache (`blocks/noirmont-livraison.liquid:3-8`) | La fourchette affichée peut être décalée d'un jour selon le cache de page, sans indication. Écart faible mais non maîtrisé sur une promesse de date. |
| 22 | Libellés Splide en anglais et vignettes en `tabindex="-1"` (`blocks/_product-media-gallery.liquid:65,68,144`) | « Next slide », « Go to slide 1 » sur une boutique française, et deux vignettes hors du parcours clavier. Cosmétique et accessibilité secondaire. |
| 23 | Division entière du paiement en 4 fois (`blocks/noirmont-4x.liquid:4`) | La somme des 4 mensualités affichées peut être inférieure au prix de jusqu'à 3 centimes. Sans effet à 299 € (74,75 × 4 exact), à surveiller sur d'autres prix. |
| 24 | `transition: all` × 2 et écouteur `scroll` non passif non throttlé (`snippets/product-option-value-button.liquid:43`, `blocks/_product-add-to-cart-button.liquid:187`, `assets/sticky-add-to-cart.js:17,22-26`) | Anti-patrons WIG et coût de rendu au défilement, plus un écouteur jamais retiré. Effet mesurable faible sur une page de cette taille. |
| 25 | `overflow-x: auto` sur le conteneur de pastilles et `<span role="button">` sans clavier (`snippets/swatches.liquid:36`, `snippets/swatch.liquid:37-47`) | Zone de défilement imbriquée sans affordance et faux bouton non focalisable — dormants tant que les swatches ne sont pas branchés. |

**Total : 25 points — 4 BLOQUANT · 7 FORT · 7 MOYEN · 7 FAIBLE.**

Points conformes vérifiés, à ne pas régresser : aucun débordement horizontal en 375 ni en 1280 · `alt` descriptif sur 38/38 images · `width`/`height` + `aspect-ratio` sur toutes les images (aucun CLS image) · 0 erreur console · contrastes tous au-delà de 10:1 · délai live J+14/J+21 exact · `<details>` natif pour les accordéons · pastilles de variantes en `input[radio]` + `<label>` correctement liés.
