# Modernisation du design NOIRMONT — d'après montre-avenue

> **25/07/2026** — analyse puis application sur le **thème brouillon 204248088914** (`Maison Noirmont`, FullStack **2.3.0**).
> Boutique de référence : `montre-avenue.com` (FullStack **2.2.0**) — même thème, une version majeure derrière nous.
> Complète `2026-07-25-mining-montre-avenue.md`, qui traitait le **fonctionnel** (pastilles, vente croisée, badges d'attributs). Ce document-ci traite le **visuel**.
> Aucun produit, aucune collection, aucun prix n'a été touché.

---

## 1. Ce qu'ils font — valeurs relevées dans le DOM

Toutes les mesures ci-dessous sont des `getComputedStyle` relevés en direct sur `/collections/montre-homme`, viewport 1280 px.

### 1.1 Le conteneur et la grille

| | montre-avenue | Noirmont (avant) |
|---|---|---|
| `max-width` du conteneur | **1300 px** | 1300 px — *identique* |
| Marges latérales | **40 px** | 40 px — *identique* |
| Padding vertical de section | **50 / 50 px** | 50 / 50 px — *identique* |
| Structure | `grid: 300px 868px`, gap 32 px (**filtres en colonne fixe**) | `flex`, pas de colonne de filtres |
| Colonnes produit | **3 × 278,7 px** | **4 × 288 px** |
| Gouttières | 16 / 16 px | 16 / 16 px |
| Ratio image | **1 / 1** | 1 / 1 — *identique* |

**Le socle de mise en page est déjà le nôtre.** C'est rassurant : rien à porter de ce côté. Les écarts sont ailleurs.

### 1.2 L'échelle typographique réellement utilisée

Sur toute la page collection, ils n'utilisent que **cinq tailles** : 40 / 25 / 22 / 16 / 14 px. C'est un système très retenu — pas de 18, pas de 20, pas de 32.

| Rôle | montre-avenue |
|---|---|
| H1 de collection | 40 px, `Merriweather` 600, interligne 50 px (1,25), **casse normale** |
| H2 de section | 25 px, poids **400** |
| H3 | 22 px, poids 400 |
| **Corps de texte** | **16 px** (`1rem`), interligne **22,4 px (1,4)** |
| Petits libellés / tri | 14 px |
| **Titre de carte produit** | **16 px, poids 500, casse normale**, interligne 22,4 px |
| Prix de carte | 16 px, poids 400 |

### 1.3 Ce qui produit la sensation de « moderne »

C'est un ensemble de quatre gestes, et **aucun n'est une ombre portée** :

1. **Angles très adoucis sur les médias — `border-radius: 26px`** avec `overflow: hidden`, sur un média de 279 px (≈ 9 % de la largeur). C'est le signal visuel le plus fort de la page.
2. **Encre adoucie.** Leur texte n'est jamais du noir pur : `--color-foreground: rgba(0 0 0 / 0.81)`. Et leurs titres sont **teintés en ardoise** `rgb(70, 100, 115)`, pas en noir.
3. **Filets quasi invisibles.** `--color-border: rgba(0 0 0 / 0.06)`.
4. **Zéro ombre, zéro relief.** `box-shadow: none` partout. La seule animation de carte est `transition: transform 0.2s ease-in-out`.

Contrôles de formulaire : `border-radius: 21px` (pilule), hauteur 35 px, texte 14 px. Pastilles de navigation inter-collections : fond `rgb(242, 244, 245)`, filet `rgba(0,0,0,.06)`, rayon 21 px.

### 1.4 Le traitement des filtres

Colonne gauche **permanente de 300 px**, jamais repliée sur desktop. Libellés en **16 px, poids 400, casse normale** — aucune petite capitale, aucun libellé technique. Le bloc de thème `filters-and-sort` propose `inline` / `sidebar` / `menu` ; ils sont en `sidebar`, valeur **par défaut du thème**.

---

## 2. Ce qui nous manquait — diagnostic nommé

Mesures relevées sur notre page collection avant intervention.

| # | Constat | Mesure avant | Pourquoi ça fatigue |
|---|---|---|---|
| **1** | **Titres produit en CAPITALES** | `text-transform: uppercase` hérité du réglage global « casse des H2 » | C'est **le** problème de lisibilité. Les capitales détruisent la silhouette des mots. Sur des noms longs (`QUARANTE-ET-UN BLEU — SPORT CUIR`) le titre passait à 2 lignes sur desktop et **3 lignes sur mobile**. |
| **2** | **Rangées désalignées** | Titres sur 1 ou 2 lignes → prix et boutons à des hauteurs différentes dans une même rangée | Le désordre le plus visible de la page. Une grille qui ne s'aligne pas paraît bricolée. |
| **3** | **Corps de texte à 15 px** | `--font-body--size: 0.9375rem` | Un cran sous eux (16 px). Sur des paragraphes entiers, ça compte. |
| **4** | **Médias quasi carrés** | `border-radius: 2px` | Contre 26 px chez eux. C'est le détail qui date le plus une page en 2026. |
| **5** | **Badge « EN PROMOTION » énorme** | **129 × 27 px**, 13,5 px de texte, aplat craie posé sur la montre — soit **46 % de la largeur de carte**. Sur mobile il couvrait ~65 % de la carte. | Présent sur presque toutes les cartes : la page crie la remise au lieu de montrer des montres. Registre « site de gadgets », pas « maison ». |
| **6** | **Filtres cachés** | `display_mode: "menu"` → un simple bouton « Filtres et tri » | Eux les laissent visibles en permanence. |
| **7** | **4 colonnes** | cartes de 288 px | Images petites pour une maison qui vend de la matière et de la lumière. |
| **8** | **Pagination inutile** | 24 produits/page pour **29 produits** → une page 2 à un seul rang | Friction gratuite. |

---

## 3. Ce que j'ai appliqué — fichier par fichier

### 3.1 `templates/collection.json` — réglages de section et de bloc

Fichier **re-tiré juste avant édition** (checksum `2002c64e…` vérifié inchangé), patché par script, diff contrôlé ligne à ligne : **10 modifications, aucune autre ligne touchée**.

| Chemin | Avant | Après | Effet |
|---|---|---|---|
| `main.settings.grid_columns` | `4` | **`3`** | Cartes 288 → **384 px** (+33 %) |
| `main.settings.products_per_page` | `24` | **`36`** | Les 29 montres sur une seule page, pagination supprimée |
| `main.blocks.filters.settings.display_mode` | `"menu"` | **`"inline"`** | Disponibilité / Prix / Trier visibles au-dessus de la grille |
| titre produit → `settings.text` | `<h2>{{ … }}</h2>` | **`<h3>{{ … }}</h3>`** | Sort le titre de la casse majuscule globale des H2 |
| titre produit → `additional_class` | `""` | `"nm-card-title"` | Crochet CSS |
| galerie → `additional_class` | `""` | `"nm-card-media"` | Crochet CSS |
| quick-add → `additional_class` | `""` | `"nm-card-cta"` | Crochet CSS |
| quick-add → `align_quick_add_together` | `false` | **`true`** | **Réglage natif du thème** : colle les boutons en bas de carte → alignés sur toute la rangée |
| quick-add → `button_shape` | `"default"` | **`"small"`** | Bouton moins lourd |

> Le passage en `<h3>` est ce qui règle la casse : le thème applique `text-transform: var(--font-h2--case)` aux `h2`, et notre réglage global met les H2 en majuscules. Les H3 sont en casse normale. Le corps et la taille du titre continuent de venir du style « paragraphe » du bloc — donc **Inter 16 px**, pas du Bodoni 28 px.

### 3.2 `assets/noirmont-custom.css` — **nouveau fichier**

### 3.3 `layout/theme.liquid` — une ligne ajoutée

```liquid
{% render 'color-schemes' %}

{% # Affinages Noirmont — doit rester après 'css-variables' et 'color-schemes' %}
{{ 'noirmont-custom.css' | asset_url | stylesheet_tag }}
```

Contenu de la feuille, et ce que chaque bloc corrige :

| Règle | Valeur | Corrige |
|---|---|---|
| `:root { --font-body--size: 1rem }` (+ `emphasized` 1.0625, `small` 0.875) | 15 → **16 px** | constat 3 |
| `.product-card .product-card-media-gallery__media--rounded` | `border-radius: 10px` + `overflow: hidden` | constat 4 |
| `.product-card .text-block.paragraph > *` | `text-transform: none`, `letter-spacing: 0`, `line-height: 1.45` | constat 1 |
| `.product-card .text-block.paragraph` | `min-height: 24px` desktop / **69 px** mobile | constat 2 |
| `.product-badges .badge` | 11 px, `padding: 3px 9px`, fond craie 92 %, **filet laiton `rgba(169,142,95,.55)`** | constat 5 |
| `.main-collection .main-collection__products-grid` | `column-gap: 24px`, `row-gap: 44px` (14 / 32 mobile) | gouttières remises à l'échelle des cartes de 384 px |
| `.product-card:hover … img` | `scale(1.03)`, `0.55s`, + `prefers-reduced-motion` | état de survol retenu, sans ombre ni soulèvement |

**Résultat mesuré après application :**

- grille `384px 384px 384px`, gouttières `24px / 44px`
- rayon des médias `10px`, `overflow: hidden`
- titre : `Trente-Neuf Duo Doré — Classique bicolore`, 16 px, `text-transform: none`
- badge **113 × 21 px** (contre 129 × 27)
- **alignement de rangée vérifié** : `priceTop` et `btnTop` strictement identiques sur les 3 cartes de la première rangée
- 29 cartes, plus de pagination

---

## 4. Ce que j'ai écarté, et pourquoi

| Écarté | Raison |
|---|---|
| **La colonne de filtres à 300 px** (leur `sidebar`) | Nous n'avons que **deux filtres** : Disponibilité et Prix. Une colonne de 300 px à moitié vide mangerait un quart de la largeur pour rien. Eux la justifient avec 364 produits et ~57 collections. J'ai pris le **principe** (filtres visibles, pas repliés) via `inline`, et gardé la largeur pour les images. |
| **Le rayon à 26 px** | Transposé à **10 px**. À 26 px sur nos visuels de marbre, la carte devient un galet — registre gadget. 10 px date la page de 2026 sans quitter la retenue de la maison. |
| **L'encre adoucie à 81 %** et les **titres teintés ardoise** | Leur `rgba(0,0,0,.81)` et leur `rgb(70,100,115)` sont *leur* charte. La nôtre fixe l'encre à `#0B0B0C`. Adoucir l'encre aurait été un changement de charte déguisé — hors mandat. |
| **Les contrôles en pilule (21 px)** et les boutons arrondis | Nos boutons à angle vif (`button_border_radius: 0`) sont une signature. Médias adoucis + boutons vifs est un contraste assumé, courant sur le haut de gamme. |
| **Réduire la bannière de collection** | Mesurée : nos produits commencent à ~570 px de haut, les leurs à ~540 px. **L'écart est négligeable**, la bannière n'est pas le problème. Et c'est de la DA — ton terrain. |
| **Modifier `config/settings_data.json`** | C'est le fichier qui porte **toutes tes couleurs et ta typo**, et celui que l'éditeur réécrit. Les deux valeurs globales dont j'avais besoin (taille du corps, rayon) sont obtenues en CSS, sans y toucher. Voir §6. |
| **Masquer le bouton « Ajouter au panier » au survol** | Ça pénaliserait le tactile. Allégé (`small`) et aligné plutôt que caché. |
| **Retirer le badge « En promotion »** | Décision commerciale, pas de design — il vient de tes `compare_at_price`. Je l'ai rendu discret, pas supprimé. Voir §6. |

---

## 5. Captures avant / après

Dossier : `boutique-seiko-mod/preuves/captures-design-2026-07-25/` — PNG 2×, viewport 1280 × 720 (desktop) et 390 × 844 (mobile).

| Fichier | Contenu |
|---|---|
| `avant-collection-desktop.png` / `apres-collection-desktop.png` | **La comparaison principale** — grille cadrée |
| `avant-collection-desktop-haut.png` / `apres-collection-desktop-haut.png` | Haut de page |
| `avant-collection-mobile.png` / `apres-collection-mobile.png` | Mobile 390 px |
| `avant-home-desktop.png` / `apres-home-desktop.png` | Accueil (contrôle de non-régression) |
| `ref-montre-avenue-collection.png` | La référence, cadrée pareil |

> Les captures sont prises en headless authentifié (cookie de mot de passe storefront) via CDP. Le bandeau de prévisualisation Shopify et la fenêtre de consentement cookies sont retirés **du rendu seulement** — aucun consentement n'a été donné ni refusé.

**Ce qu'on voit sur la comparaison desktop** : trois montres larges au lieu de quatre étroites, titres en casse normale sur une seule ligne, prix et boutons parfaitement alignés d'une carte à l'autre, badge réduit à une mention, rangées qui respirent.

**Mobile** : les titres passent de 3 lignes capitales à 2 lignes lisibles, le badge ne couvre plus la montre, et les rangées s'alignent (hauteur de 3 lignes réservée, nécessaire à 163 px de carte).

---

## 6. Ce qui reste à faire

1. **Le badge « En promotion » est sur presque toutes les cartes.** C'est un sujet de merchandising, pas de design : tant que chaque montre porte un `compare_at_price`, la boutique affiche une remise permanente — ce qui affaiblit le positionnement maison et la crédibilité du prix. À arbitrer.
2. **Filtres pauvres.** Nous n'exposons que Disponibilité et Prix, alors que les produits portent déjà les tags `classiques`, `plongeuses`, `sport-chic`, `chronos`, `gmt`, `skx`. Ajouter un filtre **Famille** se fait dans l'app **Search & Discovery** (côté admin, pas côté thème) et rendrait la colonne de filtres enfin utile — c'est le préalable à un éventuel passage en `sidebar`.
3. **Titres sur une ligne — surveillance.** Les 29 noms tiennent sur une ligne à 384 px, d'où `min-height: 24px`. Si un nom passe un jour sur deux lignes, son prix décalera : repasser la valeur à `46px` dans `noirmont-custom.css` et l'alignement est de nouveau garanti quoi qu'il arrive.
4. **Taille du corps de texte.** Elle est forcée en CSS (`:root`). Si tu préfères la voir dans l'éditeur : *Typographie → Taille du paragraphe = 16* (et sa variante mobile), puis supprime le bloc `:root` de la feuille.
5. **Les pastilles de variantes** (chantier n° 1 du minage) ne sont toujours pas là : les cartes ont un bloc swatches actif mais **zéro pastille**, faute de swatch sur les valeurs d'option. Indépendant de ce lot.
6. **La fiche produit et l'accueil** n'ont reçu que les effets globaux (corps à 16 px, médias adoucis, survols). Un passage dédié sur la PDP reste à faire.

---

## 7. Pièges rencontrés — à mémoriser

- **`custom_css` de section fait rejeter le fichier en silence.** Ma première tentative plaçait le CSS dans `sections.main.custom_css` de `templates/collection.json`. `themeFilesUpsert` a répondu `upsertedThemeFiles: []`, `userErrors: []` — **et n'a rien écrit**. Le même fichier, `custom_css` retiré, est passé immédiatement. À ranger à côté du piège connu « nom de schéma de bloc > 25 caractères ». **Sur ce thème, le CSS personnalisé passe par un asset, pas par le JSON de template.**
- **`upsertedThemeFiles: []` ne veut pas dire « en cours ».** J'ai attendu 90 s en vain. C'est un **rejet silencieux**. Le seul contrôle fiable est de re-interroger `size` / `updatedAt` : ici `size` correspond exactement à l'octet près au fichier envoyé.
- **`styles.css` (bundle des sections) est chargé après le `<head>`.** Une feuille ajoutée dans `theme.liquid` perd donc l'arbitrage à spécificité égale. Deux de mes règles (`gap` de grille, rayon des médias) ont été ignorées jusqu'à ce que je passe à des sélecteurs à deux classes. Les règles qui marchaient d'emblée en avaient déjà deux.
- **`size` d'un fichier de thème JSON n'est pas la longueur du contenu renvoyé par l'API** : le template est stocké **minifié** (7 313 o) et l'API le renvoie **indenté** (~13 ko). Ne pas comparer les deux pour vérifier une transcription.
