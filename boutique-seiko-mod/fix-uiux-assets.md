# Correctifs UI/UX — assets — Maison Noirmont

Thème **`204248088914` « Maison Noirmont »**, rôle **UNPUBLISHED** au moment des écritures
(Hakim l'a dépublié en cours de mission ; `Helio` / `204246548818` est repassé MAIN et n'a **pas** été touché).
Périmètre tenu : **`assets/` uniquement** — 1 CSS + 6 JS. Aucun `.json`, aucun `.liquid`, aucun `snippets/`.
Sources : `audit-uiux-home.md`, `audit-uiux-panier.md`. Contrôle en rendu : navigateur intégré, **375 × 812**,
prévisualisation de `204248088914` (bandeau « Maison Noirmont · Draft » visible, **aucun mot de passe saisi**).

## Preuve d'écriture

`checksumMd5` **et** `size` relus après écriture et comparés aux octets bruts locaux — les 7 fichiers concordent.

| Fichier | Octets | checksumMd5 (après) |
|---|---|---|
| `assets/noirmont-custom.css` | 26 131 | `3d0bc9251693bea703b20db685dadac1` |
| `assets/cart-drawer.js` | 14 889 | `3e1960e8db4941555f7a1fffcf383eda` |
| `assets/cart-discount.js` | 10 604 | `ea725060f2ebbdd9c62d4e8de8be4af3` |
| `assets/sticky-add-to-cart.js` | 8 085 | `222d120a0f3ada3e26fad725c88e7a4c` |
| `assets/cart.js` | 6 855 | `22cdc8a34799793d8a4bbedac96023a8` |
| `assets/cart-icon.js` | 4 372 | `99d304e1026cdd00f9275b90bf5ccf8d` |
| `assets/toast-notification.js` | 4 066 | `e51b4cd59d7b469c371830b1e255a5de` |

⚠️ **Un `themeFilesUpsert` a répondu « connecteur injoignable » et n'avait rien écrit** (CSS resté à la version
précédente, 24 396 octets). Détecté par relecture, réémis, revérifié. `size` et `checksumMd5` comparés aux
octets bruts prouvent bien l'écriture pour les `.css` / `.js` — mais seulement si on relit après **chaque** envoi.

Sauvegardes des 7 originaux : `scratchpad/backup-theme-uiux-assets/` — chacune vérifiée md5-identique à la
version du thème avant modification (ex. `cart-drawer.js` = `f67075a055a55ae2da2ebdcc1f122afc`).

---

## `assets/sticky-add-to-cart.js` — bouton d'achat collant (priorité absolue)

Réécrit. Le diagnostic initial (« teste le formulaire au lieu du bouton ») était juste mais incomplet : **trois**
causes cumulées, les deux dernières trouvées en rendu seulement.

1. **Mauvais repère.** Le thème ne rend qu'**un seul** bouton d'achat, et il est **à l'intérieur** de
   `<sticky-add-to-cart>`. L'élément passe en `position: fixed` quand `data-active="true"` : sa position en flux
   disparaît (`offsetParent` → `null`). On ne peut donc mesurer ni le formulaire (813→1219 px) ni le bouton
   lui-même (bascule permanente). → **ancre de hauteur nulle insérée juste avant l'élément** : placée avant, elle
   ne bouge pas quand la barre se détache. Bord haut stable à 1227 px, utilisé comme seuil.
2. **Les événements de défilement n'arrivaient jamais.** Le thème pose `overflow-x` sur `<body>` ; un `scroll`
   émis par `<body>` ne remonte pas jusqu'à `window`. L'écouteur `window.addEventListener('scroll')` d'origine
   ne se déclenchait **pas une seule fois** après le chargement. → `IntersectionObserver` + écouteurs sur le
   conteneur réellement défilant.
3. **`isElementInViewport()` est faux ici.** Il calcule avec `window.pageYOffset`, bloqué à 0 quand `<body>`
   défile ; et appelé avec `null` (cas `[data-ref="footer"]` absent) il lève un `TypeError` sur `offsetTop`,
   exception qui tombait pile au moment de l'activation. → géométrie `getBoundingClientRect()`, juste quel que
   soit l'élément qui défile. L'import de `@theme/utilities` est retiré.

Bonus : l'ancre reprend la hauteur du bouton quand la barre se détache — supprime le saut de 50 px du contenu.
Écouteurs passifs, une mesure par frame (l'ancien était non passif et jamais retiré).

**Avant / après, balayage sur une page de 9 801 px (seuil calculé 1 277 px) :**

| Défilement | 0 | 600 | 1 200 | 1 270 | 1 290 | 1 500 | 3 000 | 5 000 | 7 000 | 8 508 |
|---|---|---|---|---|---|---|---|---|---|---|
| Avant | inactif | inactif | inactif | inactif | inactif | inactif | inactif | inactif | inactif | inactif |
| Après | inactif | inactif | inactif | inactif | **actif** | **actif** | **actif** | **actif** | **actif** | inactif (pied de page) |

À 5 000 px : `position: fixed`, `bottom: 0px`, barre 738→812 px (au ras du bas), bouton **335 × 50 px
entièrement à l'écran**. Avant : jamais activé sur dix positions jusqu'à 4 000 px.

## `assets/cart-drawer.js`

- **Bug du message d'erreur corrigé.** `message: message` référençait une variable inexistante →
  `ReferenceError` avalé par le `.catch`. Vérifié en rendu : évaluer `message` nu lève bien `ReferenceError`.
  Remplacé par `cartErrorMessage()`, qui lit `errors` (tableau / chaîne / objet) **puis `description` puis
  `message`**. Décisif : sur ce thème les vraies erreurs (HTTP 422) arrivent en `description`/`message` et
  **jamais** en `errors` — un simple `errors.join()` n'aurait donc rien affiché non plus.
  Vérifié bout en bout : réponse 422 → toast rendu « Le paramètre line n'est pas valide. »
- **Boîte de dialogue réelle** : `role="dialog"`, `aria-modal="true"`, `aria-label` repris du titre
  (mesuré : « Panier (1) »). Reposés après chaque `renderCartContents`, qui remplace tout le HTML.
- **`Escape` ferme** (vérifié : `defaultPrevented = true`, passage en `is-closing`).
- **Focus confiné** sur `Tab` / `Shift+Tab` (vérifié : `preventDefault` sur les deux ; 17 éléments focusables,
  du bouton fermer au bouton Commander), focus déplacé dans le tiroir à l'ouverture et **restitué au
  déclencheur** à la fermeture.
- **Fermeture parasite au clavier corrigée** : `#onBackdropClick` faisait un test géométrique sur
  `clientX/clientY` ; une activation clavier synthétise un clic à `0,0`, toujours jugé « hors dialogue », donc le
  tiroir se fermait dès qu'on touchait la quantité au clavier. Remplacé par un test d'appartenance au DOM.
- Fermeture alignée sur `--animation-speed` (250 ms au lieu de 125 ms).
- Noms accessibles français sur supprimer / − / + / champ quantité (ils annonçaient « delete », « remove »,
  « add »), ligatures Material passées en `aria-hidden`.
- En cas d'erreur, le champ reprend la dernière quantité confirmée par le serveur.

## `assets/cart.js`

- **`reload()` qui détruisait le message corrigé.** `.finally(() => window.location.reload())` rechargeait à
  chaque changement de quantité, **y compris en erreur** : le toast était détruit avant lecture. Le rechargement
  n'a plus lieu qu'en cas de succès ; en erreur le message reste affiché, est annoncé, et la quantité revient à
  la dernière valeur confirmée.
- Même `cartErrorMessage()` (donc les dépassements de stock en `description` sont enfin visibles).
- Écouteurs sur références stables (les `removeEventListener` recevaient de nouvelles fonctions fléchées).
- Noms accessibles français, comme dans le tiroir.

## `assets/toast-notification.js`

`role="status"` + `aria-live="polite"` + `aria-atomic="true"`, posés dès l'upgrade (une région live doit
préexister à la modification de son contenu). Vérifié en rendu sur `/cart`. `textContent` remplace
`innerHTML`. Erreur affichée 6 s au lieu de 3 s, minuteur non empilé, écouteur retiré au détachement.

## `assets/cart-discount.js`

- `autocapitalize="characters"`, `autocorrect="off"`, `spellcheck="false"`, `autocomplete="off"`,
  `enterkeyhint="done"` posés en JS (le bloc ne les transmettait pas au snippet `textfield`).
  **Mesuré sur `/cart` : les cinq attributs présents, champ à 16 px.**
- **La saisie n'est plus effacée** en cas d'erreur : elle est conservée, sélectionnée, le focus revient au champ,
  et le repère d'erreur ne s'évapore plus au bout de 2 s (retiré quand l'acheteur corrige).
- Retrait d'une remise : le `<span>` non focusable devient `role="button"` + `tabindex="0"` + nom accessible,
  activable Entrée / Espace.
- « Appliquer » reçoit `type="button"` et `Entrée` est gérée explicitement : même comportement sur `/cart` et
  dans le tiroir (avant : soumettait le formulaire panier sur la page, ne faisait rien dans le tiroir).

## `assets/cart-icon.js`

`<cart-icon>` était un élément personnalisé sans `role`, sans `tabindex`, sans `<a>`/`<button>` : le panier
n'était **pas atteignable au clavier** et s'annonçait « local_mall ». Devient `role="button"`, `tabindex="0"`,
activable Entrée / Espace, nom accessible dynamique. **Mesuré : `aria-label="Panier, 1 article"`, ligature
`aria-hidden="true"`.**

## `assets/noirmont-custom.css` — bloc 9 ajouté

| Correctif | Avant | Après (mesuré à 375 px) |
|---|---|---|
| Anneau de focus `:focus-visible` | `outline: none` sans remplacement (select, dialog-modal, stories, quantité, textfield) | anneau citron 2 px + halo encre 6 px, **22 sélecteurs**, `!important` |
| Hamburger | 24 × 65 | **44 × 44** |
| Recherche | 24 × 24 | **44 × 44** |
| Panier | 24 × 24 | **44 × 44** |
| Écarts entre cibles d'en-tête | 16 px sur cibles de 24 px | **8 px** sur cibles de 44 px |
| Fermer le tiroir | 24 × 24 | **44 × 44** |
| Supprimer un article | 35 × 35 verrouillé par `max-*` | **44 × 44** (`max-*` levés) |
| Quantité − / + | 33 × 33 | **44 × 42**, sélecteur 128 × 44 |
| Écart supprimer ↔ quantité | 5 px | **8 px** |
| Liens de pied de page | 20 px de haut | **42 px** |
| `touch-action` | 0 occurrence | `manipulation` sur toutes les cibles (mesuré) |
| `overscroll-behavior` | 0 occurrence | `contain` sur tiroir panier + nav mobile (mesuré) |
| `env(safe-area-inset-bottom)` | 0 occurrence | pied du tiroir, nav mobile, barre d'achat |
| Voile du tiroir | `rgba(0, 0, 0, 0)` | **`rgba(11, 11, 12, 0.55)`** (tiroir panier et menu mobile) |
| Champs de saisie | 14 px → zoom iOS | **16 px** (`--inputs-font-size: 1rem` + sélecteur renforcé) |
| `font-variant-numeric` | 0 occurrence | `tabular-nums` sur prix, totaux, sous-totaux (mesuré) |
| Prix barré | même corps que le prix actif ; **2,97:1** sur craie et **1,28:1** sur fond sombre (opacité comprise) | 13 px contre 16 px, couleur héritée, opacité neutralisée → **18,81:1** / **11,80:1** |
| Accent hors charte | filet laiton `#A98E5F` sur le badge promo | repère **citron `#D6FF3F`**, badge remonté à 12 px |
| `prefers-reduced-motion` | ne couvrait pas le tiroir | animations du tiroir et du menu mobile neutralisées |

**En-tête, le défaut le plus visible.** Mesuré avant : logo 319 × 24 px, hamburger 20→64 px et logo 28→347 px
sur la même bande — **les icônes étaient dessinées par-dessus le lettrage**. Le logo est un lettrage de
1162 × 84 px, soit 332 px de large pour 24 px de haut, presque toute la rangée : tant que sa colonne est en
`auto` il impose sa largeur et écrase les colonnes latérales. Colonnes passées en `auto minmax(0,1fr) auto`,
le logo s'adapte à proportions conservées. **Après : grille `96px 179px 44px`, écarts de 8 px, `noOverlap: true`,
aucun débordement horizontal (`scrollWidth = clientWidth = 375`), hauteur de bandeau inchangée (65 px).**

---

## Régressions que j'ai introduites, trouvées en rendu et corrigées

1. **Défilement vertical mort.** Ma première version posait `html, body { overflow-x: clip }` comme garde-fou.
   `overflow-x: clip` laisse `overflow-y` à `visible`, ce qui **retire au document son statut de conteneur de
   défilement** : `scrollTop` bloqué à 2,5 px sur 9 679 px, et par ricochet la barre d'achat ne pouvait plus
   s'activer. Règle supprimée, garde-fou limité aux éléments du tiroir. Commentaire d'avertissement laissé en 9.12.
2. **Colonnes d'en-tête écrasées à 0.** `minmax(0, 1fr)` sur les colonnes latérales les laissait tomber à 0 px et
   les icônes se superposaient au logo. Corrigé par `auto minmax(0,1fr) auto`.
3. **Nom d'article coupé de 44 px** dans le tiroir : le thème pose `width: calc(100% + 60px)` et, à spécificité
   égale, `styles.css` étant chargé après ma feuille, sa règle gagnait. Sélecteur renforcé en
   `.cart-drawer .cart-drawer__item-name`.

## Contraste du prix barré — ma correction était fausse, refaite et mesurée

Un balayage de contraste du coordinateur a montré que ma première version **aggravait** le problème.
Deux erreurs, la seconde plus grave que la première :

**a) L'opacité composée, invisible pour un calcul fait sur la couleur.** J'avais posé
`color: rgba(11, 11, 12, 0.62)` et annoncé 5,6:1 — ratio calculé sur la seule valeur de `color`. Or le thème
applique **en plus** `opacity: 0.7` sur `.compare-at-price` lui-même. Les deux se composent : alpha effectif
0,62 × 0,7 = **0,43**. Le `opacity: 1` que j'avais mis n'avait pas d'effet, faute de `!important`.

**b) Couleur codée en dur, cassée sur schéma sombre.** L'encre en dur donnait de l'encre sur le fond vert
`#1E3A2F` des blocs à schéma sombre — **1,28:1**, un ancien prix quasiment invisible. C'est le pire ratio
constaté, et il venait de moi.

**Correction retenue** — déhiérarchisation par la **taille et la graisse uniquement**, jamais par l'opacité :
`color: inherit !important` (la couleur suit le schéma du bloc, clair comme sombre),
`opacity: 1 !important` (neutralise le 0,7 du thème), `font-size: 0.8125em`, `font-weight: 400`, line-through.

**Ratios effectifs, opacité comprise, mesurés sur le rendu** (chaîne d'opacité des ancêtres multipliée, couleur
composée sur le fond opaque réel, formule WCAG) :

| Contexte | Avant | Après | Seuil 4,5:1 |
|---|---|---|---|
| Fiche produit, fond craie `rgb(250,250,247)` | **2,97:1** | **18,81:1** | ✅ |
| Bloc à schéma sombre, fond `rgb(30,58,47)` | **1,28:1** | **11,80:1** | ✅ |
| Accueil, cartes produit, fond craie | 2,97:1 | **18,81:1** | ✅ |
| Accueil, cartes sur fond `rgb(231,228,222)` | 2,97:1 | **15,50:1** | ✅ |

16 prix barrés visibles sur l'accueil, **tous ≥ 4,5:1**, aux deux largeurs (375 et 1280).
`opacity` résiduelle sur un `.compare-at-price` : **aucune**. Hiérarchie conservée : 13 px / 400 contre
16 px / 400 pour le prix actif sur craie, 12,19 px / 400 contre 15 px / **500** sur fond sombre — le prix barré
est plus petit, jamais plus gras, et barré.

**Leçon** : un ratio de contraste ne se déduit pas de `color`. Il faut composer l'alpha **et** la chaîne
d'`opacity` des ancêtres sur le fond opaque réel — c'est l'opacité qui détruit le contraste sans se voir.

## Étoiles d'avis — écart assumé, documenté, non corrigé

Les icônes `star_rate` sont en vert Trustpilot `#05b67a` (`rgb(5,182,122)`), **décision de Hakim** : la couleur
n'est pas touchée. Ratio relevé ≈ **2,52:1**, consigné comme **écart assumé**, pas comme défaut.

Il m'était demandé de poser `aria-hidden="true"` **si** la note chiffrée est affichée à côté. **Vérifié en
rendu : la condition n'est pas remplie**, et poser l'attribut aurait supprimé de l'information.

- Les **29** icônes `star_rate` de la page sont **toutes** dans `.rating__stars`, à l'intérieur des **cartes
  d'avis individuelles** (`.review` — « Julien D. », « Éric P. »). Mesuré sur chacune : leur portée `.rating`
  ne contient **aucune note chiffrée**, aucun texte masqué (`.visually-hidden`), aucun `aria-label`, aucun
  `role`. Les étoiles y sont le **seul** porteur de la note de cet avis : les masquer l'effacerait pour un
  lecteur d'écran au lieu de dédoublonner.
- Le seul endroit où « **4,8/5** » est bien affiché en texte à côté d'étoiles est `.reviews-badge`
  (`.reviews-badge_text-1`) — le **badge d'avis de démonstration**, famille réservée à Hakim, non touché.
  Ses étoiles sont d'ailleurs des SVG, pas des ligatures `star_rate` : elles ne sont pas la source du 2,52:1.

**Recommandation, non appliquée** (elle tomberait dans les avis de démonstration, hors périmètre) : plutôt que
`aria-hidden`, donner une **valeur accessible** à chaque `.rating` (`role="img"` + `aria-label="Note : 5 sur 5"`).
Cela ajoute l'information au lieu de la retirer, et règle le « pas de couleur seule » proprement.

**Bandeau d'annonce** : mesuré à **18,81:1**. Le constat de l'audit était faux, rien à corriger — non touché.

## Non corrigé / à trancher

- **Lisibilité du logo mobile.** Le chevauchement est réglé, proportions respectées, mais un lettrage de rapport
  13,8:1 ne peut pas dépasser **179 px de large soit 13 px de haut** à 375 px à côté de trois cibles de 44 px
  (96 + 44 + 16 px de gouttières sur 335 px utiles). Aller plus loin exige un **logo mobile plus ramassé**
  (monogramme, ou lettrage sur deux lignes) — c'est la clé `logo` / `header-group.json`, **hors de mon
  périmètre**, je n'y ai pas touché. À réattribuer si Hakim veut le nom plus grand.
- **Bandeau de réassurance à 3,0:1** (`templates/cart.json:29`, `sections/header-group.json:31`) : dégradé et
  couleur de texte définis en **JSON**, en style inline. Non corrigeable proprement depuis un asset. Reste à
  l'agent JSON — cible 4,5:1.
- **Icônes sociales** : règles de couleur (`color: inherit`, contre le bleu `rgb(0,0,238)`) et de cible 44 px
  déployées, mais **`.social-icon-block` n'existe plus dans le DOM** (home et fiche produit) — le bloc a
  vraisemblablement été retiré par l'agent JSON. Règles inertes, à vérifier s'il revient.
- **Suppression d'article sans confirmation ni annulation**, et **`min: -1`** qui transforme le « − » en bouton de
  suppression à quantité 1 : `min` est passé par les `.liquid` (`cart-drawer.liquid:170`, `cart.liquid:178`).
  J'ai fiabilisé le message et le retour de quantité, mais **le filet (confirmation ou annulation) reste à faire**.
- **Erreurs de code promo en toast lointain** plutôt qu'en message sous le champ : demanderait un nœud DOM
  supplémentaire dans le `.liquid`.
- **Anneau de focus et déplacement du focus : non observables** dans le navigateur automatisé — le document n'y
  reçoit jamais le focus clavier réel (`activeElement` reste sur `<body>`, `:focus-visible` ne matche jamais,
  `element.focus()` sans effet). Vérifiés autrement : règle présente dans la feuille servie avec ses
  déclarations exactes, et gestionnaires prouvés actifs (`preventDefault` sur Tab / Shift+Tab, Escape ferme).
  **À confirmer d'un coup de Tab sur un vrai appareil.**
- **Paiement express et logos de paiement absents du tiroir**, **pas de CTA collant sur `/cart`**, **titre
  dupliqué**, **footer sur panier vide**, **format monétaire `€12,90`** : tous pilotés par JSON ou Liquid.

## Notes de propreté

- Un thème **`204329288018` « BROUILLON fix-uiux-assets 26-07 »** a été créé quand les écritures sur le thème
  publié étaient encore bloquées par la politique du connecteur. Il porte une version **antérieure** des
  correctifs et **n'a plus aucune valeur** : ne pas le publier, **à supprimer**.
- Un article a été ajouté au panier pour mesurer le tiroir et la page `/cart`, puis le panier a été vidé
  (`item_count: 0`). Aucune commande, aucun achat. Aucun produit, prix, variante, média ni mapping DSers touché.
  Sliders et avis de démonstration non modifiés. Étoiles d'avis laissées en vert Trustpilot.
