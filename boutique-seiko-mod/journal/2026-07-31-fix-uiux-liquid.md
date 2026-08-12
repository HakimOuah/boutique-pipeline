# Correctifs Liquid — thème `204248088914` « Maison Noirmont » (`v42pzp-h4`)

État : **10 fichiers `.liquid` écrits et vérifiés par empreinte.** Aucun `.json`, aucun `assets/`.
Cible confirmée avant la première écriture : `204248088914` = `UNPUBLISHED`, `204246548818`
« Helio » = `MAIN` (jamais touché), `204329288018` = fork obsolète (jamais touché).

Sauvegardes : `scratchpad/backup-theme-uiux-liquid/` — 10 fichiers, chacun vérifié
**octet à octet** contre le `checksumMd5` du live *avant* modification (convention `.liquid` :
empreinte sur les octets bruts, confirmée sur les 10).

| Fichier | avant (o / md5) | après (o / md5) |
| --- | --- | --- |
| `blocks/_product-media-gallery.liquid` | 13448 / `8a8a5f59…3e932e` | 14231 / `9347079c…630bc` |
| `blocks/_product-add-to-cart-button.liquid` | 11605 / `83acac5d…ded0b1` | 11654 / `22885468…b41af` |
| `blocks/image.liquid` | 6892 / `344f9028…7cec5` | 7030 / `f24143d8…45f70` |
| `blocks/noirmont-livraison.liquid` | 2893 / `d6f1c586…2a7bd02` | 2893 / `f57b7043…4a545e` |
| `sections/announcement-bar.liquid` | 5091 / `e5096931…7b7dc` | 5908 / `d6ee110f…c82fed` |
| `sections/main-product.liquid` | 7280 / `3f0c448f…2aa07` | 7280 / `f65d981e…c9667` |
| `snippets/image.liquid` | 763 / `7bd30ab0…fdf5a1` | 1149 / `69eaf3f2…25f413` |
| `snippets/price.liquid` | 4424 / `ee050a71…5cc99` | 5682 / `4433d235…7f4ad` |
| `snippets/product-media.liquid` | 2101 / `1a14ecc2…a2569` | 2753 / `978eb727…16d606` |
| `snippets/swatch.liquid` | 4270 / `565bdad5…83982b9` | 4300 / `edc7d91c…c22675` |

Relecture finale : les 10 empreintes renvoyées par l'API sont **identiques** aux empreintes
calculées localement sur mes fichiers de travail. 10 concordantes, 0 écart.

---

## Point 1 — Images : la fiche ne télécharge plus qu'une seule vue

### Cause racine exacte
`blocks/_product-media-gallery.liquid` appelait `{% render 'product-media' %}` **sans `sizes`**.
`snippets/product-media.liquid` transmettait ce `sizes` vide à `image_tag` : l'attribut n'était
donc pas émis, la valeur par défaut `100vw` s'appliquait, et le navigateur retenait le plus grand
candidat du `srcset`. Aucun `loading` nulle part → les 6 vues étaient chargées en pleine
résolution, y compris les 5 invisibles.

### Ce qui a changé
- **`snippets/product-media.liquid`** — deux nouveaux paramètres `loading` et `fetch_priority` ;
  `sizes` reçoit un défaut réaliste `(min-width: 750px) 50vw, 100vw` ; les **deux** appels
  `image_tag` (cas image et repli de vidéo) émettent désormais `loading` et `fetchpriority`.
- **`blocks/_product-media-gallery.liquid`** — la boucle distingue la première vue des suivantes :
  `forloop.index == 1` → `loading="eager"` + `fetchpriority="high"` ; toutes les autres →
  `loading="lazy"`. Le `sizes` réaliste est passé explicitement.
- **`snippets/image.liquid`** — paramètre `loading` ajouté, défaut `lazy`, sauf si
  `fetch_priority == 'high'` (alors `eager`) : le hero ne peut pas être différé par erreur.
- **`blocks/image.liquid`** — `loading: 'lazy'` ajouté, ce qui rend au passage valide le
  `sizes: 'auto, …'` déjà présent (`sizes="auto"` n'est licite que sur une image `lazy`).
  `sizes` utilise maintenant les largeurs réellement configurées du bloc
  (`image_width_desktop/mobile`) au lieu de `100vw` codé en dur.

### Deux défauts supplémentaires trouvés et corrigés
1. **`fetch_priority` n'est pas un argument reconnu par `image_tag`.** Le thème l'utilisait déjà
   dans `snippets/image.liquid` ; Shopify le recopiait tel quel et produisait
   `fetch_priority="high"`, **attribut HTML invalide donc ignoré par le navigateur**. C'est
   l'explication du constat de l'audit « `fetchpriority` absent partout ». Le bon nom est
   `fetchpriority`. Corrigé dans `snippets/image.liquid` et `snippets/product-media.liquid`.
   Mesure : `fetch_priority=` présent **0 fois** après correction, `fetchpriority="high"` **1 fois**.
2. **`sizes` des vignettes invalide.** `sizes: 'auto, 110, (width >750px) 160'` — `110` sans unité
   et une condition média non conforme : la valeur entière était rejetée, repli `100vw`, les
   6 vignettes se chargeaient donc en grand elles aussi. Remplacé par
   `(min-width: 750px) 160px, 110px`, et `loading: 'lazy'` ajouté.

### Mesures avant / après
| | avant (audit) | après (mesuré au rendu) |
| --- | --- | --- |
| Fiche produit — vues de galerie téléchargées | 6 / 6, pleine résolution | **1 / 5** (`complete && naturalWidth>0`) |
| Fiche produit — `loading` sur les vues | absent | 1 × `eager`, 4 × `lazy` |
| Fiche produit — `fetchpriority` | absent | 1 × `high` (la première vue seulement) |
| Fiche produit — images non différées | — | 4 / 37 (logos + hero, volontaire) |
| Home — images non différées | **62 / 95** | **5 / 96** (2 logos, hero, 1 visuel, logo de pied) |
| Home — images réellement téléchargées | — | **5 / 96** |
| Attribut invalide `fetch_priority=` | 100 % des appels | 0 |

Les 10 images du tiroir fermé du header sont couvertes : elles passent par `blocks/image.liquid`.

---

## Point 2 — Le bouton d'achat s'annonce correctement

### Ce qui a changé
- **`blocks/_product-add-to-cart-button.liquid`** —
  `<span class="button__separator" aria-hidden="true">|</span>`.
- **`snippets/price.liquid`** — le prix barré reçoit un libellé réservé aux lecteurs d'écran :
  `<span class="compare-at-price__label">Ancien prix : </span>`, masqué visuellement par une
  règle ajoutée dans le `{% stylesheet %}` du snippet lui-même (`clip-path: inset(50%)`), afin de
  ne dépendre d'aucun fichier `assets/` — l'agent CSS travaille dessus en parallèle.
- **`snippets/price.liquid` + le bouton** — nouveau paramètre `compare_at_aria_hidden`.

### Pourquoi ce paramètre : un piège découvert au rendu
Le libellé masqué **survit** dans le bloc de prix principal, mais **disparaît à l'intérieur du
bouton** : le JS du thème (`data-ref="compare-at-price"`) réécrit le contenu de ce nœud à la
sélection de variante et emporte le `<span>` enfant. Le nom accessible du bouton restait donc
« Ajouter au panier €379 €499 ».

Conformément à l'option prévue dans la consigne (« ou `aria-hidden` sur le barré si l'information
reste accessible ailleurs »), le bouton passe maintenant `compare_at_aria_hidden: true` : l'ancien
prix y est retiré de l'arbre d'accessibilité — c'est un **attribut sur l'élément**, que la
réécriture JS ne peut pas effacer — et il reste annoncé, avec son libellé, par le bloc de prix
principal situé juste au-dessus.

### Mesure avant / après du nom accessible
| | valeur |
| --- | --- |
| avant | `Ajouter au panier | €299 €389` (deux montants à plat) |
| après (mesuré) | **`Ajouter au panier €379`** |
| bloc de prix principal (mesuré) | **`Ancien prix : €429`** |

Le « Ajouter » en double n'a pas été signalé ni touché : il vient d'un span en `display: none`,
déjà hors de l'arbre d'accessibilité — conforme à la consigne.

---

## Point 3 — Le `<h1>`

### Ce qui a changé, dans mon périmètre
**`sections/main-product.liquid`** — le **préréglage** de la section produit portait
`"text": "<h2>{{ closest.product.title }}</h2>"` avec `"text_style": "h3"`. C'est la source du
défaut : toute nouvelle section produit naissait sans `<h1>`. Corrigé en `<h1>…</h1>` +
`"text_style": "h1"`.

### Constat important à faire remonter
`blocks/text.liquid` **ne produit jamais de balise de titre** : `text_style` n'est qu'une classe
CSS posée sur un `<div>`, le niveau de titre vient du contenu `richtext` lui-même. Aucun réglage
ne peut donc créer un `<h1>` — seul le contenu du champ le peut.

**Or, au rendu, la fiche a bien exactement un `<h1>` = le titre du produit** (`h1Count: 1`,
`<h1>Intégrale Brun or rose — Sport chic`), et l'ordre des titres est sain :
H1 → H2 Description → H2 Livraison & retours → H2 Calibres → H2 Garantie → H2 Contact.
Ce n'est **pas mon fait** : `templates/product.json` contient déjà `<h1>` dans le champ du titre
et `heading_tag: h2` sur les accordéons. Le fichier a donc été modifié entre l'audit
(`h1Count: 0` relevé à 16 h 20) et ma vérification. À recouper avec l'agent JSON pour éviter un
retour en arrière.

### Ce qui reste (hors périmètre Liquid)
L'enveloppe du `<h1>` est encore `class="text-block h3"` → le `<h1>` **s'affiche à 28 px**, taille
de H3. La sémantique et le SEO sont réglés, pas la dominance visuelle. Une seule valeur à changer,
dans `templates/product.json` : `text_style` du bloc titre `"h3"` → `"h1"`.

---

## Point 4 — Bandeau d'annonce du header

### Ce qui a changé — `sections/announcement-bar.liquid`
Tout tient dans ce fichier (balisage + son `{% stylesheet %}`), sans toucher `assets/slider.css`
qui appartient à l'agent CSS :
- `.announcement-bar__content .splide__track { overflow: hidden }` — la piste clippe. C'est la
  correction du symptôme central : sans elle les annonces voisines restaient visibles, tronquées
  de part et d'autre de l'annonce active.
- `.announcement-bar__content .splide__slide { min-width: 0 }` — une annonce ne se laisse plus
  comprimer par le contenu de ses voisines.
- Nouvelle classe conditionnelle `announcement-bar__content--with-arrows`, posée **seulement**
  quand le slider et les flèches sont réellement rendus (`section.blocks.size > 1 and
  section.settings.show_arrows`), avec `margin-inline: 46px` sur la piste : les flèches, en
  position absolue, disposent d'une gouttière et ne peuvent plus se superposer au texte.

### Mesures avant / après
| | avant (audit) | après (mesuré) |
| --- | --- | --- |
| `overflow` de `.splide__track` | `visible` | **`hidden`** |
| `transform` de `.splide__list` à `activeIndex 0` | `translate(-229,56 px)` | **`matrix(1, 0, 0, 1, 0, 0)`** — décalage nul |
| Messages visibles simultanément | 2, tronqués | **1** (« Livraison offerte en France métropolitaine ») |
| Gouttière réservée aux flèches | 0 | **46 px** de chaque côté |

Vérifié identique sur la fiche produit **et** sur la home.

---

## Point 5 — Comptes `themefullstack` : la consigne visait le mauvais fichier

**`blocks/social-icons.liquid` ne contient aucun compte par défaut.** Vérifié en entier : les
13 liens sortent tous de `settings.*_url` (réglages de thème), chacun sous garde `!= blank`. Il
n'y a **rien à retirer dans ce fichier** — et rien n'a été inventé.

Les quatre comptes viennent de **deux fichiers `.json`, hors de mon périmètre** :

| Emplacement | Clé | Valeur par défaut |
| --- | --- | --- |
| `config/settings_schema.json:2737` | `facebook_url` | `https://www.facebook.com/themefullstack/` |
| `config/settings_schema.json:2743` | `instagram_url` | `https://www.instagram.com/themefullstack/` |
| `config/settings_schema.json:2754` | `youtube_url` | `https://www.youtube.com/@themefullstack` |
| `config/settings_schema.json:2770` | `linkedin_url` | `https://www.linkedin.com/company/themefullstack/` |
| `config/settings_data.json:77` | `instagram_url` | `https://www.instagram.com/themefullstack/` |

C'est le même mécanisme que celui trouvé par l'agent JSON pour `type_size_h1_mobile` : la clé
absente de `settings_data.json` retombe sur le défaut du schéma. **Attention** : `instagram_url`
est en plus **inscrit en dur dans `settings_data.json`** — vider le défaut du schéma ne suffira
donc pas pour Instagram, il faut aussi vider la valeur stockée. Le diagnostic de l'agent JSON
(« ce sont les comptes par défaut de `blocks/social-icons.liquid` ») est à corriger sur ce point.

Le masquage du bloc reste la bonne mesure conservatoire tant qu'aucun compte Noirmont n'existe.

---

## Point 6 — Délai de livraison J+14

**`blocks/noirmont-livraison.liquid`** — `min_days` corrigé **aux deux endroits** : le défaut du
schéma (`"default": 12` → `14`) et le repli Liquid (`| default: 12` → `14`), pour qu'ils ne
divergent pas. Taille inchangée (2893 o), empreinte changée — preuve que l'écriture a bien eu lieu.

Rendu mesuré le 26 juillet : « Livraison estimée entre le **9 août** et le **16 août** » =
**J+14 / J+21**, conforme à la promesse tenue partout ailleurs.

Le nom du schéma reste « Barre de livraison » (18 caractères, sous la limite de 25 qui fait
rejeter un fichier en silence). Aucun nom de schéma créé ou allongé dans cette passe.

---

## Point 7 — Libellé des pastilles de variantes

**`snippets/swatch.liquid`** — `aria-label="{{ name }}"` (le nom du groupe) →
`aria-label="{{ value }}"` (la couleur). Le nom du groupe est déjà porté par le libellé d'option
qui précède le groupe de radios ; le répéter sur chaque pastille masquait la seule information
utile.

Ajouté au passage sur la variante `swatches_for_product_card` (le `<span role="button">` des
cartes produit) : elle n'avait **aucun** `aria-label`.

Défaut latent, comme annoncé : les métaobjets `dial-color` / `case-color` ne sont pas branchés,
donc rien de visible aujourd'hui — la correction est en place pour le jour du branchement.

---

## Ce qui reste — par destinataire

### À l'agent JSON (ou à qui détiendra les `.json`)
1. `config/settings_schema.json` — vider les 4 défauts `themefullstack` (lignes ci-dessus).
2. `config/settings_data.json:77` — vider `instagram_url`, sinon Instagram survit au point 1.
3. `templates/product.json` — `text_style` du bloc titre `"h3"` → `"h1"` : c'est la dernière
   valeur qui manque pour que le `<h1>` ait sa dominance visuelle (28 px aujourd'hui).
4. À recouper : `templates/product.json` a changé depuis l'audit (le `<h1>` et les `heading_tag:
   h2` des accordéons y sont déjà). Vérifier qui l'a écrit avant de réappliquer une charge utile
   préparée plus tôt, sous peine d'écraser ce gain.

### Dans mon périmètre, volontairement non fait
- **`blocks/social-icons.liquid` — `rel="noopener noreferrer"` manquant sur les 13 ancres
  `target="_blank"`.** Défaut réel (tabnabbing), signalé par l'agent JSON. Hors des 7 points
  confiés, et le fichier fait 19,7 Ko de tracés SVG qu'il faudrait retranscrire intégralement
  pour une réécriture d'une ligne : le rapport risque/bénéfice ne le justifiait pas dans cette
  passe, le bloc étant par ailleurs masqué. Correction triviale à appliquer en même temps que
  le point 5.
- `blocks/_product-media-gallery.liquid` — les flèches de carrousel (`<button>` sans `aria-label`
  ni `type="button"`, libellés Splide anglais sur une boutique française) et l'`| escape` sur le
  `image_tag` des vignettes, dont le comportement m'a paru suspect mais qui rend correctement :
  je ne l'ai pas touché pour ne pas modifier un rendu qui fonctionne. Hors des 7 points.
- `blocks/noirmont-livraison.liquid` — mois français codés en dur (6 locales embarquées),
  pas de `<time>`, corps de texte à 14,72 px. Hors des 7 points.

### Contrôle non concluant
Le rendu **n'a pas pu être mesuré à 375 × 812**. La fenêtre Chrome est en plein écran
(`innerWidth` bloqué à 1710 px, `outerWidth: 0`) ; `resize_window` renvoie un succès mais
n'a aucun effet sur le viewport, et aucun outil d'émulation d'appareil n'était disponible.
Les trois contrôles demandés ont donc été faits à **1710 px** :
- **galerie : une seule image chargée** — indépendant de la largeur (différé), acquis ;
- **`<h1>` présent** — indépendant de la largeur, acquis ;
- **bandeau lisible** — un seul message, décalage nul, gouttière de 46 px. L'audit relevait le
  même défaut « identique en 1280 », la correction est donc démontrée hors mobile ; le mécanisme
  employé (`overflow: hidden` + gouttière) ne dépend pas de la largeur.

**Reste à confirmer d'un coup d'œil à 375 px de large** (vrai mobile ou émulation d'appareil) :
le rendu visuel du bandeau et l'absence de chevauchement des flèches.

---

## Garde-fous respectés
Aucun `.json`, aucun `assets/`. Aucun produit, SKU, prix, variante, média ni mapping DSers
approché. Aucun slider ni avis de démonstration modifié. Aucune promesse produit non vérifiable
introduite — le seul texte ajouté est « Ancien prix : », un libellé d'accessibilité.
Aucun thème publié, aucune commande. Écritures limitées à `204248088914` ; `204246548818`
(`MAIN`) et `204329288018` n'ont reçu aucune requête d'écriture.
