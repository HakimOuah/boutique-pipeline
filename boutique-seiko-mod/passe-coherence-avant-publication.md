# Passe de cohérence avant publication — thème « Maison Noirmont »

> **27/07/2026, nuit.** Toutes les écritures sur `204248088914` (« Maison Noirmont »), **rôle
> `UNPUBLISHED` revérifié avant et après chaque écriture**. `204246548818` (« Helio », **MAIN**) et
> `204329288018` (fork obsolète) n'ont reçu **aucune requête d'écriture** : contrôle final par
> `files(filenames:…)` sur les deux → **0 nœud**, et leur `updatedAt` est resté au **26/07 14:23** et
> **26/07 14:26**. **Aucun thème publié, aucune fiche publiée, aucun article publié.**
> Aucun SKU, prix, variante, média produit ni mapping DSers touché : **aucune mutation produit
> n'a été appelée**. Les trois Plongeuses restent en `DRAFT`.
> Sauvegardes et charges utiles : `scratchpad/backup-finitions/`.
>
> **Reprise du 27/07 au matin — §8.** Les deux régressions d'accessibilité signalées au §4.4 ont été
> reprises : l'anneau de focus (§8.1) et les cibles tactiles (§8.2). Trois fichiers écrits sur le
> même thème `204248088914`, **rôle `UNPUBLISHED` revérifié avant et après**. `204246548818`
> (« Helio », MAIN) n'a reçu **aucune requête d'écriture** — `updatedAt` toujours au
> **26/07 14:23:56**, `files(filenames:)` → 0 nœud. Aucun produit, prix, variante, média, mapping
> DSers ni commande. Sauvegardes : `scratchpad/backup-focus/`.

---

## 0. Comment tout a été vérifié

Le rendu a été observé à **375 px puis 1280 px** sur la prévisualisation du thème brouillon, dans
un **cadre de mesure à viewport exact** : la page réelle est récupérée en `fetch` (cookie de session
déjà présent, **aucun mot de passe saisi**) puis réécrite dans une `iframe` de 375 × 812 ou
1280 × 900. Il a fallu passer par là parce que :

- la fenêtre Chrome refuse de descendre sous ~606 px de viewport (plancher de fenêtre + zoom) ;
- une `iframe` pointant directement sur la boutique est refusée : Shopify sert le storefront avec
  `frame-ancestors 'none'`.

Le cadre reproduit donc un **vrai viewport de 375 px** avec le vrai HTML, les vraies feuilles et les
vrais scripts du thème brouillon. Le bandeau « Maison Noirmont · Draft » est visible sur les
captures : c'est bien le thème brouillon qui répond.

Trois instruments, et il a fallu **les trois** :

1. **couleurs calculées** (`getComputedStyle` sur chaque élément, 15 propriétés dont
   `background-image` et `box-shadow`) ;
2. **recherche dans le servi** (HTML de chaque page **et** contenu des feuilles CSS téléchargées,
   dont le paquet `styles.css` généré par Shopify à partir des blocs `{% stylesheet %}`) ;
3. **recherche dans la source** du thème, fichier par fichier.

Chacun a trouvé ce que les deux autres rataient — le détail est au §2.

---

## 1. Les quatre corrections

### 1.1 La promesse fausse dans le corps de la page Configurateur — corrigée

`Page/176162537810` portait encore, **dans la donnée de la page** (le nouveau gabarit ne l'affiche
pas, mais Helio la sert) :

> « Composez votre montre pièce par pièce : boîtier, cadran, aiguilles, trotteuse, bracelet,
> détails. **Personne d'autre ne la portera.** » + « Le configurateur ouvre très bientôt. »

Les deux phrases étaient fausses : les montres sont finies, au catalogue, et le guide est en ligne.
Corps réécrit (`pageUpdate`, `userErrors: []`) :

> « **Votre Noirmont en trois étapes** : dites-nous le genre de montre que vous cherchez, puis la
> couleur de cadran qui vous plaît. Nous vous montrons celle de nos montres qui y répond — avec son
> calibre, son diamètre et son prix.
>
> Chaque montre proposée est au catalogue et part de notre atelier partenaire telle qu'elle est
> présentée. Livraison offerte et suivie en France métropolitaine, généralement 2 à 3 semaines.
> Garantie commerciale de 12 mois sur le mouvement, en plus des deux ans de garantie légale. »

**Contrôle des interdits sur le nouveau corps** : `unique` 0 · `composez` 0 · `configurez` 0 ·
`sur mesure` 0 · `assemblée pour vous` 0. Aucune promesse d'unicité, aucune promesse d'assemblage.
Les trois affirmations chiffrées reprennent celles déjà tenues ailleurs (bandeau, article, CGV).

### 1.2 Le gabarit d'article pointait sur un blog inexistant — corrigé

`templates/article.json`, section `blog_featured_xFHxUe` : `"blog": "news"`. **Il n'existe qu'un
seul blog sur la boutique, `actualites`** — la section mettait donc en avant un blog vide.

Corrigé en `"blog": "actualites"`. Écriture validée par **double empreinte** : le fichier a été
transcrit localement puis envoyé, et les deux transcriptions ont produit **exactement les mêmes
octets**.

| | octets | `checksumMd5` |
| --- | ---: | --- |
| avant | 15 519 | `300e891ced709ae7f639a0db1bdc4552` |
| local (envoyé) | 15 524 | `a05ea6c7ae31fd600c095f533d791fcf` |
| **relu sur le thème** | **15 524** | **`a05ea6c7ae31fd600c095f533d791fcf`** ✅ |

L'écart de +5 est exactement `actualites` − `news` (+6) moins le saut de ligne final (−1) : aucune
autre différence. Relecture : **un seul en-tête auto-généré**, `"blog": "actualites"`.

### 1.3 L'article n'avait pas d'image à la une — corrigée sans rien générer

Le gabarit ouvre sur une bannière `image-banner` alimentée par `{{ closest.article.image }}` ;
l'article n'avait pas d'image → bannière vide.

**Aucun visuel n'a été généré.** Réutilisation d'un visuel existant du catalogue :
`files/noirmont-hero.jpg`, 2048 × 1152 (16:9, format de la bannière), **macro d'un cadran stérile
noir sans logo** — exactement le sujet de l'article.

**Contrôle du second rôle invisible, avant réutilisation.** Les médias des **100 fiches** ont été
balayés (2 pages de 50, `hasNextPage: false`), médias de fiche **et** images de variantes :
450 fichiers distincts. Aucun des huit visuels éditoriaux `noirmont-*.jpg` n'y figure — donc
`noirmont-hero.jpg` **ne sert d'image à aucune variante ni à aucune galerie produit**.

Second garde-fou : `articleUpdate` ne déplace pas le média, il en **crée une copie indépendante**.
La preuve est dans l'URL rendue — `/articles/noirmont-hero.jpg`, nouvel enregistrement
`ArticleImage/333159366994`, distinct du `MediaImage/59674874544466` d'origine. **La page d'accueil
et la page La Maison ne peuvent pas être affectées.**

Texte alternatif renseigné : « Macro d'un cadran stérile noir, sans logo ni nom, sur bracelet acier
— Maison Noirmont ».

⚠️ **L'article reste en brouillon** (`isPublished: false`) : voir §5.

### 1.4 Le tableau à trois colonnes en mobile — défaut confirmé, puis corrigé

**Mesuré, pas supposé.** L'article étant en brouillon, son URL répond 404 ; le tableau a donc été
mesuré en reproduisant **exactement le DOM que rend le gabarit** —
`.article > .article-content.page-width > .text-block.auto` — avec les feuilles réelles du thème,
dans le cadre à 375 px.

**Avant :** le tableau mesurait **351,5 px de large dans une colonne de 335 px**. Il crevait la
gouttière droite et venait mourir à **3,5 px du bord de l'écran**, texte comprimé. Et le thème ne
donne **aucun style de tableau** : ni bordure, ni espacement, ni séparation de lignes — la
recherche `table|th|td|thead|tbody` dans toutes les feuilles servies retourne **0 règle**.

**Correctif, dans des fichiers d'asset** — jamais dans le champ CSS d'une section, qui est rejeté
en silence :

- `assets/noirmont-article.css` — conteneur de défilement, et style de tableau lisible ;
- `assets/noirmont-article.js` — pose l'enveloppe `.nm-table-scroll` autour de
  `.article-content table`. **Le CSS seul ne peut pas créer un conteneur** : il faut un élément. Le
  script pose aussi `role="region"`, `aria-label` et `tabindex="0"` **uniquement si le tableau
  déborde réellement**, pour ne pas ajouter d'arrêt de tabulation inutile sur grand écran ;
- `layout/theme.liquid` — deux lignes, insérées après la feuille du pied de page et **avant**
  `noirmont-see-more-fix.css`, qui doit rester la dernière feuille du `<head>`.

**Le piège du conteneur flex.** Première tentative : le débordement a **empiré** — 85 px, la page
entière défilait. `.article` est un conteneur `flex` ; sans `min-width: 0`, l'article ne peut pas
rétrécir sous la largeur minimale du tableau et c'est la **page** qui cède. Deux lignes
(`.article > .article-content` et `.article-content .text-block`) règlent la question. C'est
documenté dans la feuille : ça se reproduira sur tout contenu large ajouté à un article.

**Résultat mesuré avec le CSS et le JS réellement livrés :**

| | 375 × 812 | 1280 × 900 |
| --- | ---: | ---: |
| `document.scrollWidth` | **375** | **1280** |
| Débordement de page | **0** | **0** |
| Conteneur du tableau | 335 px (client 333) | 752 px (client 750) |
| Largeur du tableau | **544** | 750 |
| Défile dans son propre conteneur | **oui** | non (il tient) |
| `tabindex` / `role` / `aria-label` | **0 / region / présent** | **aucun** (inutile) |

Le tableau est désormais bordé, aéré (0,75 rem), en-tête distingué, **chiffres tabulaires**.

---

## 2. La chasse aux couleurs interdites — 22 occurrences vivantes trouvées et purgées

La consigne annonçait « deux occurrences qui n'existaient dans aucun fichier servi ». Il y en avait
**bien plus**, et **aucun des trois instruments seul ne les aurait toutes trouvées**.

### 2.1 Ce que seules les couleurs calculées ont trouvé (4 + 4)

`sections/cart-drawer-group.json` et `templates/cart.json` contiennent chacun **deux blocs
`custom-code`** dont le CSS vit dans un `<style>` **à l'intérieur d'un réglage de section**. Il
n'est donc dans **aucun fichier `.css`** — un `grep` sur les feuilles ne le voit jamais.

- `.nm-cart-banner { background: linear-gradient(90deg, #1E3A2F, #A98E5F) }` — le bandeau
  « Livraison offerte en France — suivie » du tiroir panier **et** de la page panier ;
- `.nm-cart-upsell__title { color: #1E3A2F }` ;
- `.nm-cart-upsell__price { color: #1E3A2F }` ;
- `.nm-upsell-add:hover { background: #1E3A2F }`.

Purgés : dégradé → aplat encre `#0B0B0C` (texte craie déjà en place, **19,6:1**), couleurs de texte
→ encre, survol du bouton → `opacity: .88` (pas de couleur inventée).

### 2.2 Ce que seule la recherche dans la source a trouvé (5)

Des règles de **`:hover`** — invisibles pour un balayage de couleurs calculées, qui ne survole rien :

- `assets/noirmont-collection.css` : `.nm-coll-desc button { color: #1E3A2F; border-bottom: 1px
  solid #A98E5F }`, `.nm-soeurs .collection-card:hover { border-color: #A98E5F }`,
  `.nm-soeurs .collection-card:hover .nm-soeurs__legend > * { color: #1E3A2F }` ;
- `assets/noirmont-megamenu.css` : `.nm-mm__grid .collection-card:hover .nm-mm__legend > * { color:
  #1E3A2F }`, `.nm-mm__all a { color: #1E3A2F; border-bottom: 1px solid #A98E5F }`.

Purgés : textes → encre, filets → `rgba(11,11,12,.32)`. Le survol du méga-menu, qui passait de
`#0B0B0C` à `#1E3A2F` (donc quasiment invisible), est remplacé par un **soulignement** : un état
de survol qui se voit vraiment, et sans couleur.

### 2.3 Ce que seul le paquet `styles.css` a trahi (8)

Le paquet de 156 ko que Shopify génère à partir des blocs `{% stylesheet %}` contenait
`1e3a2f` ×4, `a98e5f` ×3, `rgb(30,58,47)` ×1. Remontée à la source : trois blocs de fiche produit.

- `blocks/noirmont-livraison.liquid` : fond et bordure du bandeau de livraison en
  `rgba(30,58,47,…)`, la pastille en `#1E3A2F`, la mention « Livraison gratuite » en `#1E3A2F` ;
- `blocks/noirmont-confiance.liquid` : icônes en `#1E3A2F`, carte « contact » en `rgba(169,142,95,…)` ;
- `blocks/noirmont-4x.liquid` : badge alternatif en `rgba(169,142,95,.12)`.

Purgés vers l'encre et ses lavis. Après correction, le paquet `styles.css` rechargé sans cache
retourne **0 occurrence**.

### 2.4 Faux positifs — laissés tels quels

`assets/noirmont-custom.css` contient 8 occurrences des deux teintes : **toutes dans des
commentaires** qui documentent la purge du 26/07 (blocs 5, 9.10, 11.2 et 12). Aucune déclaration.
Les en-têtes de palette de `noirmont-collection.css` et `noirmont-megamenu.css` ont en revanche été
mis à jour : ils annonçaient encore « vert jura · laiton » comme couleurs de la maison.

### 2.5 État final

| Contrôle | Résultat |
| --- | ---: |
| Couleurs calculées, 28 pages, 375 px **et** 1280 px | **0 occurrence** |
| Recherche dans le HTML servi de chaque page | **0 occurrence** |
| Recherche dans toutes les feuilles servies, dont `styles.css` | **0 occurrence** |
| Recherche dans la source (`config/`, `sections/`, `templates/`, `blocks/`, `assets/`) | **0 déclaration** (8 commentaires) |

---

## 3. Le rendu, page par page

375 px d'abord, puis 1280 px. `sw` = `document.scrollWidth`. Tous les statuts en **200**.

| Page | 375 px | 1280 px | Débordement | Couleurs interdites |
| --- | ---: | ---: | ---: | ---: |
| Accueil | sw 375 | sw 1280 | 0 | 0 |
| `/pages/configurateur` | sw 375 | sw 1280 | 0 | 0 |
| Collection Classiques | sw 375 | sw 1280 | 0 | 0 |
| Collection Sport chic | sw 375 | — | 0 | 0 |
| Collection Chronos | sw 375 | — | 0 | 0 |
| Collection Plongeuses | sw 375 | — | 0 | 0 |
| Collection GMT | sw 375 | — | 0 | 0 |
| Collection Accessoires | sw 375 | — | 0 | 0 |
| Fiche Trente-Neuf (montre) | sw 375 | sw 1280 | 0 | 0 |
| Fiche Loupe de date (accessoire) | sw 375 | — | 0 | 0 |
| **Panier** `/cart` | sw 375 | sw 1280 | 0 | **0 (était 5)** |
| **Tiroir panier** (ouvert, 375 px de large) | sw 375 | — | 0 | **0 (était 2)** |
| `/pages/faq` · `la-maison` · `contact` | sw 375 | sw 1280 | 0 | 0 |
| `/pages/mentions-legales` · `politique-de-cookies` | sw 375 | — | 0 | 0 |
| **`/policies/terms-of-sale`** | **sw 375 (était 416)** | sw 1280 | **0 (était 41 px)** | 0 |
| `/policies/` × 6 autres | sw 375 | — | 0 | 0 |
| Article | **non rendable** — brouillon, 404. Gabarit et tableau mesurés par reproduction (§1.4) | | | |

### 3.1 Un débordement horizontal trouvé sur une page légale — corrigé

`/policies/terms-of-sale` débordait de **41 px** à 375 px (`scrollWidth` 416). Cause : le formulaire
de rétractation des CGV contient des suites de **59 points ASCII** (`Commande du : ......`), un
« mot » insécable. Ce n'est pas du CSS de thème, c'est le **contenu légal**.

Corrigé côté thème plutôt que côté texte de loi, dans `assets/noirmont-article.css` :

```css
.shopify-policy__container .rte,
.shopify-policy__container .rte * { overflow-wrap: anywhere; }
```

`anywhere` et non `break-word` : **seul `anywhere` réduit aussi la largeur minimale du bloc**, donc
empêche le conteneur d'imposer sa largeur au corps de page. Vérifié en rendu après écriture :
`scrollWidth` 375, la ligne fautive s'arrête à 355 px. Le correctif protège aussi toute autre page
de politiques contre un futur jeton trop long.

---

## 4. Les autres contrôles

### 4.1 Liens — 89 URL internes testées, aucune morte

Récoltées sur l'accueil, le configurateur, une collection, le panier, la FAQ, La Maison, Les
Montres — donc **méga-menu, pied de page et corps** — plus les **9 liens du maillage de l'article**
(ajoutés à la main, l'article n'étant pas rendable). Chaque URL appelée en `GET` avec suivi de
redirection, **et** contrôle que la page rendue n'est pas la page 404 du thème.

**87 / 89 en 200 franc.** Les deux autres ne sont pas des liens morts :

- `/account` → redirection **hors domaine** vers le portail comptes clients Shopify ; `fetch` échoue
  sur la politique d'origine, pas sur la cible. À ouvrir à la main pour confirmation visuelle.
- `/policies/#shopifyReshowConsentBanner` (« Préférences en matière de cookies », pied de page, sur
  **toutes** les pages) → `/policies/` seul répond 404. **Mais c'est le lien standard de Shopify** :
  `Shopify.customerPrivacy` est bien chargé et intercepte le fragment pour rouvrir la bannière. Il
  ne tomberait sur le 404 que sans JavaScript. **Rien touché** — c'est de la plomberie de
  consentement, elle ne se modifie pas à l'aveugle.

Les 9 URL légales atteignables sont toutes en 200 : `/pages/mentions-legales`,
`/pages/politique-de-cookies`, et `/policies/` × 7 (`terms-of-sale`, `refund-policy`,
`privacy-policy`, `shipping-policy`, `legal-notice`, `contact-information`, `terms-of-service`).
**Aucun lien externe** n'est présent sur les pages balayées.

### 4.2 Les 34 chemins du configurateur — tous aboutissent

Le parcours au clic n'est pas pilotable depuis le cadre de mesure : la section appelle
`history.replaceState`, qui échoue quand le document n'a pas d'URL propre, et le carrousel de
l'écran 1 ne réagit qu'aux événements de confiance. Un pilotage au clic partiel a néanmoins confirmé
la mécanique (« Voici votre Trente-Neuf Duo Doré », prix, bouton). Le décompte complet a donc été
fait **sur la donnée réellement rendue** :

| | Mesure |
| --- | ---: |
| Grille de la Q2 | **75 cases** (5 familles × 15) |
| Cases portant au moins une montre | **34** |
| Cases grisées | **41** — affichées et libellées, jamais retirées du DOM |
| Cases annonçant « 0 montre » | **0** |
| Chemins par famille | Classiques **9** · Sport chic **7** · Chronos **11** · Plongeuses **3** · GMT **4** |
| Panneaux de révélation pré-rendus | **50** |
| Panneaux sans nom (`data-name`) | **0** |
| Panneaux sans prix | **0** |
| Panneaux sans lien produit | **0** |

**34 chemins ouverts, 0 qui mène au vide**, et la répartition par famille correspond exactement à
celle documentée. Le parcours accepte trois paramètres d'URL (`famille`, `cadran`, `montre`) :
les chemins sont partageables.

### 4.3 Contrastes — mesurés sur le rendu, opacité héritée comprise

L'opacité cumulée de **tous** les ancêtres est multipliée à l'alpha du texte, puis composée sur le
fond effectif remonté d'ancêtre en ancêtre. Jamais déduit d'une valeur de `color`.

| Élément | Taille | Opacité cumulée | Ratio mesuré |
| --- | ---: | ---: | ---: |
| Titre de fiche `h1` | 24 px | 1,000 | **18,81:1** |
| Prix `.price` | 20 px | 1,000 | **18,81:1** |
| Prix barré `.compare-at-price` | 11,4 px | 1,000 | **18,81:1** |
| Bouton d'achat (craie sur encre) | 15 px | 1,000 | **19,67:1** |
| « Livraison gratuite » (bloc corrigé) | 12,8 px | 1,000 | **16,93:1** |
| En-tête d'accordéon | 16 px | 1,000 | **18,81:1** |
| Lien de pied de page | 18 px | 1,000 | **18,81:1** |
| Paragraphe courant | 16 px | 1,000 | **18,81:1** |
| Bandeau du tiroir panier (après correction) | 13,6 px | 1,000 | **19,60:1** |

**Deux valeurs sous le seuil, toutes deux dans le domaine réservé de Hakim — non touchées :**

- **Étoiles d'avis, `#05b67a` sur craie : 2,52:1** (30 glyphes sur l'accueil, 30 sur la fiche).
  C'est le vert Trustpilot, **décision de Hakim** : conservé tel quel, ce n'est pas un écart.
- **« 1340 avis », `div.reviews-badge_text-2` : 1,00:1** — encre sur encre, **texte littéralement
  invisible**. Domaine réservé (le badge doit de toute façon disparaître, 0 commande réelle), mais
  la mesure est là si Hakim préfère le corriger plutôt que le retirer.

### 4.4 Cibles, focus, chiffres

- **Focus visible** : `noirmont-custom.css` porte **25 règles `:focus-visible`** avec
  `outline: 2px solid var(--nm-cyan) !important`. L'anneau de focus existe partout et ma nouvelle
  règle `.nm-table-scroll:focus-visible` suit la même convention. ⚠️ **Le cyan `#22D3EE` ne vaut
  que 1,72:1 sur craie** : l'anneau est présent mais sous les 3:1 attendus d'un indicateur de focus.
  Voir §5.
  > ❌ **Ce constat était faux — corrigé au §8.1.** Je n'avais lu que `outline-color` et ignoré le
  > `box-shadow: 0 0 0 6px rgba(11,11,12,.9)` de la **même règle**. L'anneau réel a deux
  > composantes ; mesuré sur le rendu, il vaut **15,04:1 sur craie** et **10,89:1 sur encre**.
  > Il restait néanmoins deux vrais trous, décrits au §8.1.
- **Cibles < 44 px** — récurrentes, toutes issues du thème d'origine :
  - flèches de carrousel `.splide__arrow` : **40 × 40** (19 occurrences sur l'accueil) ;
  - puces de pagination `.splide__pagination__page` : **12 × 2** (6 par carrousel) ;
  - en-têtes d'accordéon `summary.accordion__header` : **335 × 40** (10 sur la fiche) ;
  - lien « FAQ » du méga-menu : **30,6 × 44** (largeur insuffisante) ;
  - lien de note « 4,8/5 » sur la fiche : **236 × 17**.
  Aucune n'est bloquante — toutes ont une cible alternative — mais elles restent hors norme.
  > ✅ **Relevé incomplet — repris et corrigé au §8.2.** Le balayage systématique du 27/07 en a
  > trouvé **15 familles** dans 18 contextes, pas 5. Toutes sont désormais à 44 × 44, sauf le badge d'avis
  > (domaine réservé de Hakim).
- **Chiffres tabulaires** : `font-variant-numeric: tabular-nums` confirmé sur **tous** les prix
  relevés (`.price`, `.compare-at-price`, `.nm-cart-upsell__price`), ainsi que dans le tableau de
  l'article.

---

## 5. Ce qui reste à faire par Hakim avant de publier

**Bloquants — la publication ne sert à rien sans eux :**

1. **Publier « Maison Noirmont » (`204248088914`).** Tout le travail y est ; le thème MAIN reste
   « Helio ». Supprimer ensuite le fork obsolète `204329288018`.
2. **Publier l'article** « Seiko mod ou montre hommage : quelle différence ? »
   (`Article/615589052754`, blog `actualites`). Il est en **brouillon** : son URL répond **404**,
   `/blogs/actualites` est vide, et la section `blog_featured` désormais bien réglée n'a **rien à
   mettre en avant**. Je ne l'ai pas publié — c'est hors de mon mandat. **Après publication,
   revérifier le tableau à 375 px** : je l'ai mesuré par reproduction fidèle du DOM, pas sur l'URL
   réelle.

**Fortement recommandés :**

3. **Format monétaire.** Les prix s'affichent **`€329`**, symbole devant et sans décimales, sur
   toute la boutique — panier, fiches, configurateur. En France on attend `329,00 €`. C'est un
   réglage de **boutique** (Paramètres → Devise), pas un fichier de thème : je ne touche pas aux
   réglages de compte. Sur une boutique française qui vend à 279–430 €, ça se voit.
4. ~~**Anneau de focus à 1,72:1.**~~ **Fait le 27/07 — voir §8.1.** Le diagnostic était erroné :
   l'anneau était déjà à deux composantes. Deux vrais trous ont été trouvés et bouchés.
5. **Titre de la page `Le Configurateur`.** Le corps est réécrit, le `<h1>` rendu est « Votre
   Noirmont en trois étapes », mais le **titre de la page** et l'entrée de menu disent toujours
   « CONFIGURATEUR » — le mot promet un assemblage. Je ne l'ai pas changé : le libellé de menu et
   le `handle` (`/pages/configurateur`, cité dans quatre menus) sont ta décision, et les menus
   Shopify sont **partagés entre thèmes**.
6. ~~**Cibles tactiles sous 44 px** (§4.4)~~ **Fait le 27/07 — voir §8.2.** 15 familles portées à
   44 × 44 sur l'accueil, les collections, la fiche, le panier, le tiroir, le menu mobile et le
   pied de page. Reste ta décision : l'espacement des en-têtes d'accordéon (§8.2, note finale).

**Ton domaine réservé — je n'y ai pas touché :**

7. « 2 000 clients satisfaits », les trois `review_count: 123`, le badge « 1340 avis » (au passage :
   **invisible**, encre sur encre, 1,00:1), sliders et avis de démonstration.
8. **Médiateur de la consommation** — obligation légale, adhésion **par site**, marqueur en CGV
   art. 17. Ne jamais recopier le CM2C de Tuftéo.
9. Les 12 champs de comptes sociaux vides ; « Plongeuse » dans 3 titres Héritage ; les visuels qui
   sur-promettent la capacité des rouleaux et meubles ; la règle française du prix de référence à
   30 jours avant toute remise affichée.

---

## 6. Écritures — empreintes relues sur le thème

Douze fichiers, tous relus après écriture. Les empreintes ci-dessous sont **celles du thème**, et
elles sont **identiques aux octets envoyés** (md5 calculé localement avant envoi).

| Fichier | octets | `checksumMd5` relu | = local |
| --- | ---: | --- | :-: |
| `templates/article.json` | 15 524 | `a05ea6c7ae31fd600c095f533d791fcf` | ✅ |
| `templates/cart.json` | 18 273 | `83668f0bc2a227fa7ef3ea0788934ee6` | ✅ |
| `sections/cart-drawer-group.json` | 9 013 | `74e68bbb74c9a0317f35c3b94e349346` | ✅ |
| `sections/header-group.json` | 21 243 | `a3048231211788d63ffab0c0e7dc2fbe` | ✅ |
| `assets/noirmont-article.css` *(nouveau)* | 2 775 | `478a5602748a03b92a321168dcf22911` | ✅ |
| `assets/noirmont-article.js` *(nouveau)* | 1 859 | `e98b1f2c3a5287e8c2f5be20ff832919` | ✅ |
| `assets/noirmont-collection.css` | 7 127 | `ab0b82288a176d410f60b74c38da4816` | ✅ |
| `assets/noirmont-megamenu.css` | 5 449 | `bec631ab9ccd6dfb1db613babd4b716e` | ✅ |
| `blocks/noirmont-4x.liquid` | 2 130 | `41f204d83f986b10c9c71181d31c01f0` | ✅ |
| `blocks/noirmont-confiance.liquid` | 3 308 | `aa82e54aac93519d632884267d1746e9` | ✅ |
| `blocks/noirmont-livraison.liquid` | 2 893 | `10b0f871c0534dc8585e1b1ac55a9d0e` | ✅ |
| `layout/theme.liquid` | 2 127 | `66d69ab4a3dfad31203e97a0d3ae2c1e` | ✅ |

Plus deux écritures hors thème : le **corps de la page** `Configurateur` et l'**image à la une** de
l'article, toutes deux avec `userErrors: []`.

### 6.1 Correction au piège documenté : `size` ne se compare pas toujours au contenu relu

`sections/cart-drawer-group.json` renvoyait `size: 9051` alors que le **contenu relu faisait
9 414 octets** — et `checksumMd5` ne correspondait pas non plus au contenu relu. Ce n'est pas une
incohérence de Shopify : **l'écart vaut exactement 363 octets, la taille de l'en-tête
auto-généré**, que Shopify **ajoute à la lecture** sans le stocker. Pour ce fichier, `size` et
`checksumMd5` décrivent donc le **corps sans en-tête**.

Mais ce n'est **pas une règle par dossier** : pour `templates/article.json`,
`templates/cart.json` et `sections/header-group.json`, `size` correspond au contenu **avec**
en-tête. La règle utile est plus simple et plus sûre :

> `size` et `checksumMd5` décrivent les **octets réellement stockés**, qui peuvent inclure ou non
> l'en-tête auto-généré selon la manière dont le fichier a été écrit la première fois. **Ne jamais
> comparer au contenu relu : comparer à ce qu'on a envoyé, puis relire pour confirmer.**

Une transcription manuelle de ce fichier, faite avant cette découverte, s'est révélée **identique
octet pour octet** au contenu exact — la fausse alerte venait bien de l'en-tête, pas de la copie.

### 6.2 Une méthode d'écriture sans transcription manuelle

Retranscrire à la main un gabarit de 18 ko truffé d'échappements JSON pour n'y changer que quatre
couleurs est le meilleur moyen de casser une page panier. Chaîne utilisée à la place, **entièrement
mécanique** :

1. lire le fichier par l'API — si la réponse dépasse la limite de contexte, le connecteur la
   **dépose sur le disque**, et on obtient les octets exacts ;
2. appliquer la substitution en Python, avec assertion sur le **nombre d'occurrences attendu** et
   validation JSON ;
3. `stagedUploadsCreate` → `POST` du fichier local en `curl` (l'`ETag` renvoyé **est** le md5, donc
   l'intégrité est vérifiée dès l'envoi) ;
4. `themeFilesUpsert` avec `body: { type: URL, … }` pointant sur l'objet déposé ;
5. relire le fichier et comparer `size` + `checksumMd5` au md5 local.

Aucun résidu : les dépôts intermédiaires sont temporaires (expiration à 24 h) et **rien n'a été
ajouté à la bibliothèque de fichiers de la boutique** — donc aucune suppression à faire.

`themeFilesUpsert` a renvoyé **`upsertedThemeFiles: []` sans `userErrors`** sur les six écritures
passées par URL. Ce n'est **pas un échec** : c'est une écriture asynchrone. Les six ont été
confirmées par relecture d'empreinte.

---

## 7. Fichiers de travail

Tout est dans `scratchpad/backup-finitions/` : état d'avant, contenus exacts relus (`*.EXACT.*`),
versions corrigées (`*.NEW.*`) et copies envoyées (`*.sent`) pour rejouer n'importe quelle
comparaison d'empreinte.

---

# 8. Reprise du 27/07 — les deux régressions d'accessibilité

## 8.0 Le piège qui a produit les deux faux diagnostics du §4.4

**Les transitions CSS passent AVANT les déclarations `!important` dans la cascade.** Le thème pose
`transition: .15s ease-in-out` sur `.button`, ce qui met `min-width`, `min-height`, `outline-color`
et `outline-width` en transition. Tant qu'une transition court, `getComputedStyle` rend la valeur
**interpolée**, pas la valeur déclarée — et dans une `iframe` de mesure hors écran, les transitions
ne se terminent jamais.

Relevé sur un bouton juste après la mise au point, sans précaution :

| | valeur lue | valeur réelle après stabilisation |
| --- | --- | --- |
| `outline-width` | 0,5 px | **2 px** |
| `outline-color` | `rgba(0,0,0,0)` | **`#22D3EE`** |
| `box-shadow` | `rgba(0,0,0,0) 0 0 0 0` | **`rgba(11,11,12,.9) 0 0 0 6px`** |
| `min-height` | 35 px | **44 px** |

D'où la règle, désormais écrite en tête de la feuille : **neutraliser les transitions avant toute
mesure** — `*, *::before, *::after { transition-duration: 0s !important }`. Sans ça on conclut que
`!important` « ne s'applique pas », ce qui est faux, et on invente un correctif inutile.

**Instrument.** Cadre à viewport exact de 375 px (même méthode qu'au §0), avec deux ajouts : la
hauteur de l'`iframe` est portée à la hauteur du contenu — vérifié sans effet sur la mise en page,
**0 écart sur 40 éléments témoins** — pour que `elementFromPoint` porte sur toute la page ; et le
focus est déplacé par des **appuis Tab réels**, seul moyen d'obtenir `:focus-visible` (un
`el.focus()` scripté ne le déclenche pas).

---

## 8.1 L'anneau de focus — mesuré, et l'erreur de diagnostic corrigée

### Ce qui était déjà juste

Le bloc 9.1 de `noirmont-custom.css` ne pose pas un anneau cyan : il pose **un anneau à deux
composantes**, cyan cerné d'un halo d'encre de 6 px, dans la même déclaration. Le §4.4 n'avait lu
que `outline-color`. L'ordre de peinture — ombre externe sous le fond, `outline` par-dessus tout —
donne, de l'extérieur vers l'intérieur : **encre 2 px, cyan 2 px, encre 2 px**.

**Mesure sur le rendu, opacité cumulée des ancêtres comprise, après parcours au clavier réel :**

| Composante | Sur craie `#FAFAF7` | Sur encre `#0B0B0C` |
| --- | ---: | ---: |
| Trait cyan `#22D3EE` | 1,73:1 | **10,89:1** |
| Halo encre `rgba(11,11,12,.92)` | **15,04:1** | 1,00:1 |
| **Anneau retenu** | **15,04:1** | **10,89:1** |

Les deux composantes sont **complémentaires, pas redondantes** : l'encre porte le contraste sur
fond clair, le cyan le porte sur fond sombre. Retirer l'une rend l'anneau invisible sur l'un des
deux jeux de couleurs. C'est écrit en tête de la nouvelle feuille.

**Le cas explicitement demandé — bouton d'achat en craie sur encre :** son fond propre est l'encre
`rgb(11,11,12)`, mais le fond **adjacent**, celui contre lequel l'anneau se détache, est la craie
`rgb(250,250,247)`. Halo d'encre contre craie : **15,91:1**.

### Les deux vrais trous, trouvés et bouchés

**1. La liste nominative laissait passer des éléments.** Le bloc 9.1 énumère 22 sélecteurs. Tout ce
qui n'y figure pas n'a aucun anneau. Mesuré sur la page panier : `<shop-pay-wallet-button>`,
**0,00:1**. Correctif — un filet universel dans `assets/noirmont-tap-focus.css` :

```css
:focus-visible {
  outline: 2px solid var(--nm-cyan, #22d3ee) !important;
  outline-offset: 2px !important;
  box-shadow: 0 0 0 6px rgba(11, 11, 12, 0.92) !important;
}
```

Spécificité volontairement basse (0,1,0) : les cas particuliers déjà écrits — notamment
`.quantity-selector input:focus-visible` et son anneau en `outline-offset: -3px` — restent
prioritaires et ne sont pas défaits.

**2. `.nm-table-scroll:focus-visible` déclarait le cyan sans halo** (règle écrite cette nuit même,
§1.4). Elle ne survivait que parce que `[tabindex]:focus-visible` du bloc 9.1 la battait en
`!important` — dépendance fragile. Corrigée **à la source** dans `assets/noirmont-article.css` :
`box-shadow: 0 0 0 6px rgba(11, 11, 12, 0.92)` ajouté.

### Résultat mesuré après écriture, sur le thème réel

| Page | Arrêts de tabulation | Min. fond clair | Min. fond sombre | Sous 3:1 |
| --- | ---: | ---: | ---: | ---: |
| Accueil | 57 | **12,72:1** | **10,89:1** | **0** |
| Fiche produit | 58 | 12,72:1 | 10,89:1 | **0** |
| Panier | 53 | 12,72:1 | 10,89:1 | **0** |

**Contrainte restante, documentée et non corrigée : le rognage du halo.** Le halo est un
`box-shadow` : il est coupé par tout ancêtre en `overflow: hidden`. Sur 11 arrêts de l'accueil il
est rogné de 6 à 7 px **d'un seul côté**. Les coupables sont `div.group--flex`,
`div.shopify-section` et `body { overflow-x: hidden }` — ce dernier étant précisément le garde-fou
anti-débordement horizontal. **Je ne les ouvre pas** : rendre ces conteneurs visibles réintroduirait
le débordement que la passe précédente a supprimé. L'anneau reste visible sur les trois autres côtés
et le ratio mesuré ne bouge pas. La feuille ouvre en revanche `overflow` le temps du focus sur les
trois petits conteneurs de champ où c'est sans risque (`.input-group`, `.textfield`, `.see-more`),
sur le modèle de ce que faisait déjà `.quantity-selector`.

**Une exception hors de portée du thème :** `<shop-pay-wallet-button>` ne correspond pas à
`:focus-visible` sur son hôte — le focus part dans une **racine d'ombre fermée** de Shopify, qui
dessine son propre anneau. Aucune feuille de thème ne peut l'atteindre. Le seul levier serait
`:focus-within`, qui allumerait aussi l'anneau au clic souris sur le bouton le plus important du
panier : **écarté**.

---

## 8.2 Les cibles tactiles — 15 familles, 18 contextes, trouvées et corrigées

### Comment elles ont été trouvées

Balayage de **tous** les éléments interactifs à 375 px sur l'accueil, deux collections, la fiche
produit, la page panier, le **tiroir panier ouvert**, le **menu mobile ouvert**, le configurateur,
la FAQ et le pied de page. Pour chacun, deux mesures : la **boîte** (`getBoundingClientRect`) et la
**zone de frappe réelle**, obtenue en sondant `elementFromPoint` point par point autour du centre —
donc en tenant compte des zones étendues par pseudo-élément, pas seulement du dessin.

Le §4.4 en signalait 5 familles ; il y en avait **15**, dans **18 contextes distincts**. Le configurateur en comptait bien **0** :
c'est la seule page qui était déjà en règle, ce qui explique la contradiction du signalement.

### Avant / après, mesuré

| Famille | Où | Boîte avant | Boîte après | Correctif |
| --- | --- | ---: | ---: | --- |
| `.splide__arrow` | tous les carrousels | **40 × 40** | 40 × 40, **frappe 44 × 44** | `::after` étendu |
| `.splide__pagination__page` | accueil, fiche | **12 × 2** | 12 × 2, **frappe 44 × 44** | `::after` + pas de 52 px |
| `summary.accordion__header` | fiche | **335 × 40** | **335 × 44** | `min-height` |
| `summary.accordion__header` | panier | **293 × 34,6** | **293 × 44** | `min-height` |
| `summary.accordion__header` (code promo) | tiroir | **313 × 24** | **313 × 44** | `min-height` |
| `.button--icon-only` (pagination) | collections | **35 × 35** | **44 × 44** | `min-*` `!important` |
| `.button--icon-only` (fermeture) | menu mobile | **35 × 35** | **44 × 44** | `min-*` `!important` |
| `.button--small` « Ajouter au panier » | cartes produit | **160,5 × 35** | **160,5 × 44** | `min-height !important` |
| `.side-menu__toggle-link` « Filtres et tri » | collections | **102,9 × 24** | **102,9 × 44** | `min-height` |
| `.see-more__toggle` « Voir plus » | collections | **60 × 26,6** | **60 × 44** | `min-height` |
| `.collection-card` (collections sœurs) | collections | **81,2 × 31,8** | **81,4 × 44** | `min-height` |
| `.menu-block__link` « FAQ » | pied de page, partout | **30,6 × 44** | **44 × 44** | `inline-flex` + `min-width` |
| `.header__mobile-menu-link` | menu mobile | **305,5 × 43,1** | **305,5 × 44** | `min-height` |
| `.cart-drawer__item-name` | tiroir | **220 × 38,2** | **220 × 44** | `inline-flex` + `min-height` |
| `.nm-cart-upsell__name` | panier, tiroir | **225 × 17** | **245 × 44** | `inline-flex` + `min-height` |
| `.nm-upsell-add` « Ajouter » | panier, tiroir | **72,3 × 28,3** | **72,3 × 44** | `min-*` |
| Champ de quantité | panier, tiroir | **38 × 42** | **44 × 44** | `width` + `min-*` `!important` |
| Boutons − / + de quantité | panier, tiroir | **44 × 42** | **44 × 44** | `min-height !important` |

**Aucun dessin d'icône n'a grossi.** Les flèches de carrousel et les puces de pagination gardent
exactement leur trait : leur cible est étendue par un `::after` transparent centré. Les quatre
familles concernées avaient bien `::before` et `::after` à `none` avant modification, vérifié
élément par élément sur le rendu.

### Le piège de la pagination

Les puces passent au pas de **52 px** (44 de cible + 8 d'écart). Premier essai : le conteneur est
passé à **335 × 88**, soit **deux rangées** — son `padding: 0 16px` ne laissait que 303 px utiles
pour 6 × 52 = 312. Correctif : `padding-inline: 0`. Mesure après : **335 × 44, une seule rangée**,
puces de 32 à 344, `scrollWidth` 375. `flex-wrap: wrap` reste en garde-fou : si un carrousel gagne
des pages, les puces passent à la ligne au lieu de déborder horizontalement.

### Une décision antérieure respectée

Le bloc 11 de `noirmont-custom.css` avait **volontairement** laissé le champ de quantité à 38 px,
faute de place quand les actions partageaient la ligne du nom d'article. Ce même bloc leur a depuis
donné leur propre ligne (media query ≤ 749 px) : la place existe. Le champ est ramené à 44, et
`scrollWidth` reste à **375** sur la page panier comme dans le tiroir.

### État final, mesuré sur le thème réel après écriture

Le décompte ci-dessous ne retient que les **vraies** cibles sous 44 px : les faux positifs de
l'instrument (élément recouvert par l'`iframe` d'application, champs cachés de 1 × 1 px) et le
badge d'avis réservé sont exclus des deux colonnes.

| Page | Cibles sous 44 avant | après | Paires à moins de 8 px | `scrollWidth` |
| --- | ---: | ---: | ---: | ---: |
| Accueil | 13 | **0** | 5 → **0** | 375 |
| Collection Accessoires | 122 | **0** | 0 → **0** | 375 |
| Collection Classiques | 59 | **0** | 0 → **0** | 375 |
| Fiche produit | 19 | **0** | 13 → **8** (voir note) | 375 |
| Panier | 12 | **0** | 3 → **1** (voir note) | 375 |
| Tiroir panier | 9 | **0** | — | 375 |
| Menu mobile | 1 | **0** | — | 375 |
| Configurateur, FAQ, La Maison, Contact | 0 | **0** | 0 | 375 |
| 7 pages de politiques + mentions légales | — | — | — | 375 |

Les seules valeurs encore listées par l'instrument sont **deux faux positifs et un domaine
réservé** : les `<input>` de recherche de 1 × 1 px cachés dans les dialogues fermés, le lien du
pied de page recouvert par l'`iframe` `PBarNextFrame` d'une application, et le badge d'avis
« 4,8/5 · 1340 avis » (113 × 17) — **domaine réservé de Hakim**, non touché.

**Note sur les 8 px d'écart — une décision à toi.** Les paires restantes sont des **en-têtes
d'accordéon consécutifs**, séparés de 0,5 px. Ce n'est pas une régression : ils l'étaient déjà avant,
et chacun fait maintenant 44 px de haut sur toute la largeur. Les écarter de 8 px trouerait le filet
de séparation et casserait le langage visuel de l'accordéon. **Je ne l'ai pas fait** — la mesure est
là si tu préfères trancher autrement. Partout ailleurs, les 8 px sont tenus : la seule paire créée
par l'agrandissement (nom de la vente complémentaire et son bouton « Ajouter », tombée à 5,6 px) a
été portée à **13,6 px**.

---

## 8.3 Ce qui n'a pas bougé — vérifié, pas supposé

| Contrôle | Méthode | Résultat |
| --- | --- | --- |
| Couleurs interdites, **couleurs calculées** (15 propriétés, 3 pages) | `getComputedStyle` sur tous les éléments | **0** |
| Couleurs interdites, **HTML servi** | recherche dans `outerHTML` | **0** |
| Couleurs interdites, **feuilles servies** dont `styles.css` | téléchargement sans cache + recherche | **0** |
| Couleurs interdites, **`<style>` de section** | recherche dans chaque `<style>` | **0** |
| Couleurs interdites, **source** des 3 fichiers écrits | recherche locale | **0** |
| Étoiles Trustpilot `#05b67a` | couleur calculée | **30 glyphes, inchangés** |
| Chiffres tabulaires | `font-variant-numeric` sur `.price` | **`tabular-nums`** |
| `prefers-reduced-motion` | comptage dans les feuilles servies | **5 blocs, intacts** |
| Débordement horizontal | `scrollWidth` à 375 px sur 13 URL dont les 7 politiques | **375 partout** |
| Contrastes de texte | non touchés — aucune règle de `color` écrite | inchangés |

La nouvelle feuille n'introduit **aucune animation** : les seuls `transform` sont des
`translate(-50%, -50%)` statiques de centrage sur des pseudo-éléments.

---

## 8.4 Écritures — empreintes relues sur le thème

Aucune transcription manuelle de contenu volumineux : chaîne mécanique
`stagedUploadsCreate` → `POST` en `curl` → `themeFilesUpsert` par URL → relecture.
Les deux fichiers modifiés ont d'abord été **transcrits puis vérifiés au md5 contre l'empreinte du
thème** avant d'être patchés — c'est ce qui garantit qu'aucun octet d'origine n'a été perdu.

| Fichier | Empreinte AVANT (vérifiée) | octets APRÈS | `checksumMd5` relu | = md5 local |
| --- | --- | ---: | --- | :-: |
| `assets/noirmont-tap-focus.css` *(nouveau)* | — | 9 191 | `19b005cd63453b4b9409071de110f8e7` | ✅ |
| `assets/noirmont-article.css` | 2 775 / `478a5602…` | 3 194 | `e13adda3639ce6b4ee3fad2d7ea7dfb0` | ✅ |
| `layout/theme.liquid` | 2 127 / `66d69ab4…` | 2 331 | `11ed42c6bcef1a66ed18a28ceabdff54` | ✅ |

`themeFilesUpsert` a de nouveau renvoyé **`upsertedThemeFiles: []` sans `userErrors`** : écriture
asynchrone, confirmée par relecture d'empreinte — le piège documenté au §6.2.

**Ordre des feuilles vérifié sur le rendu**, la nouvelle s'insère bien après le paquet des
sections et avant la dernière :

`reset` → `base` → `slider` → `noirmont-custom` → `noirmont-megamenu` → `noirmont-collection` →
`noirmont-footer` → `noirmont-article` → **`styles.css`** → **`noirmont-tap-focus`** →
`noirmont-see-more-fix`

**Contrôle final des trois thèmes** : `204248088914` toujours `UNPUBLISHED` ;
`204246548818` (« Helio », MAIN) `updatedAt` **26/07 14:23:56**, inchangé, `files(filenames:)`
→ **0 nœud** ; `204329288018` (fork obsolète) `updatedAt` **26/07 14:26:46**, inchangé.
**Aucun thème publié.**

## 8.5 Fichiers de travail

`scratchpad/backup-focus/` : `*.EXACT.*` (contenus d'origine relus et vérifiés au md5),
`*.NEW.*` (versions envoyées), `validated.css` (les déclarations exactes validées en navigateur
avant écriture, pour rejouer la comparaison), `up1.sh` / `up2.sh` (les envois).
