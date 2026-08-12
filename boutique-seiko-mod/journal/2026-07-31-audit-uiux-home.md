# Audit UI/UX — Accueil Maison Noirmont (`v42pzp-h4` / maisonnoirmont.fr)

Lecture seule. Thème `204248088914` « Maison Noirmont », rôle **MAIN**, non modifié.
Appariement nom ↔ contenu validé par `checksumMd5` sur les 12 fichiers récupérés (`templates/index.json` 4bbd441b…, `sections/header-group.json` 6ced631f…, `sections/footer-group.json` 4f3d1301…, `layout/theme.liquid` 6c174fd4…, `assets/noirmont-custom.css` 605f157f…, `assets/noirmont-megamenu.css` 8aaa4a82…, + `noirmont-collection.css`, `noirmont-see-more-fix.css`, `snippets/meta-tags|fonts|scripts|css-variables`).
Rendu live vérifié au navigateur intégré à **375 × 812** (boutique publique, aucun mot de passe rencontré, aucun saisi) : mesures de cibles tactiles, débordement, `overscroll-behavior`, `font-variant-numeric`, contraste, tiroir ouvert.
Périmètre exclu (non audité) : sliders et avis de démonstration.

---

## layout/theme.liquid

- `layout/theme.liquid:37` - `<body>` sans lien d'évitement ; aucun `[class*=skip-to]` dans le DOM rendu.
- `layout/theme.liquid:52` - `content_for_layout` non enveloppé dans `<main>` ; `document.querySelector('main')` = `null` sur la home.
- `layout/theme.liquid:23,26,29,34` - quatre feuilles Noirmont non minifiées ajoutées au `<head>`, dont `noirmont-see-more-fix.css` **après** `content_for_header` : 4 requêtes bloquantes de rendu en plus des 3 préchargées (203 Ko de CSS servis sur la home).
- `layout/theme.liquid:13-15` - `preload: true` cumulé au `stylesheet_tag` sur reset/base/slider : 3 préchargements en concurrence de priorité avec les polices et l'image LCP.
- `layout/theme.liquid:2` - `lang` correct, `viewport` correct (`width=device-width,initial-scale=1`, pas de `user-scalable=no`). Aucun écart.
- `layout/theme.liquid:37` - header en `position: sticky; top: 0` sans aucune règle `env(safe-area-inset-*)` : **0 occurrence** de `env(safe-area` sur les 203 Ko de CSS.

## sections/header-group.json

- `sections/header-group.json:110-113` - `autoplay: true` / `autoplay_speed: 4` sur 3 annonces, aucun contrôle pause ou lecture : contenu en mouvement automatique non interruptible.
- `sections/header-group.json:110` - `show_arrows: true` : flèches `position: absolute` 40 × 40 à x 10-50 et x 325-365, superposées au bloc de texte de 315 px ; collision visible à 375 px (glyphe par-dessus « Cadran vierge de to… »).
- `sections/header-group.json:110` - flèches d'annonce 40 × 40 (< 44) et `top: 12px`, dans la zone d'encoche, sans safe area.
- `sections/header-group.json:128-130` - bloc bouton `label: "S'abonner"` avec `link: ""` : contrôle sans destination (desktop).
- `sections/header-group.json:498-499` - `header_height: 65` + sticky, cumulé aux 65 px de barre d'annonce : 131 px de chrome fixe avant le hero sur 812 px de haut.
- `sections/header-group.json:420-425` - `drawer_grid` `mobile_only`, 9 collections, 2 colonnes : 10 `<img>` mesurées à boîte nulle et `loading="auto"` — la grille illustrée du tiroir **fermé** est téléchargée au premier rendu.
- `sections/header-group.json:173,284` - `show_arrows: true` sur des `collections-featured` en `layout_type: "grid"` : réglage inerte.
- `sections/header-group.json:507` - `uppercase_menu_items: false` : conforme à la charte (casse normale sur les titres de contenu), pas un écart.
- rendu `.header__menu-mobile` - 24 × 65 px, sans `aria-label`, sans `aria-expanded`, sans `aria-controls` : cible sous 44 × 44, nom accessible = « menu ».
- rendu `.header__icon-search` - 24 × 24 px, sans `aria-label` : nom accessible = « search ».
- rendu `<cart-icon class="header__icon-cart">` - 24 × 24 px, élément personnalisé sans `role`, sans `tabindex`, sans `<a>`/`<button>` : panier non atteignable au clavier, nom accessible = « local_mall ».
- rendu `.header__mobile-menu` (tiroir ouvert) - `role` = null, `aria-modal` = null, `aria-hidden` = null ; `document.activeElement` reste le bouton déclencheur : aucun déplacement du focus, aucun piège de focus.
- rendu `.header__mobile-menu-nav` - défilable (`scrollHeight` 1178 / `clientHeight` 761) avec `overscroll-behavior: auto` : chaînage de défilement vers la page ; **0 occurrence** de `overscroll-behavior` sur l'ensemble du CSS.
- rendu `.header__mobile-menu-overlay.is-open` - `background: rgba(0, 0, 0, 0)` : voile entièrement transparent, aucun assombrissement de la page, fermeture par appui extérieur non signalée.
- rendu global - **0 occurrence** de `touch-action` : pas de `touch-action: manipulation` sur les cibles tactiles.

## templates/index.json

- `templates/index.json:174-175` - `<h1>Votre signature au poignet</h1>` rendu avec `text_style: "h2"` ; rendu mesuré 32 px capitales, identique à `templates/index.json:1782` (« L'allure d'abord », `text_style: "h2"`) : le H1 n'a aucune dominance visuelle au-dessus de la ligne de flottaison.
- `templates/index.json:725,1616` - titres de carte produit balisés `<h2>` et rendus à 16 px : 16 H2 de rang égal aux titres de section (24 px). Le commentaire de `assets/noirmont-custom.css:66` annonce un passage à `<h3>` — non appliqué à la home.
- `templates/index.json:1977-1978,2063,2148` - puces de spécifications « Calibre annoncé », « Acier », « Sans logo » balisées `<p>` avec `text_style: "h2"` : titres visuels sans sémantique (écart inverse du précédent).
- `templates/index.json:654-657` - bouton « Voir toutes les montres » en `show_on_display: "desktop_only"`.
- `templates/index.json:1545-1548` - bouton « Voir les accessoires » en `show_on_display: "desktop_only"` : sur mobile, aucune sortie vers la collection complète depuis les deux carrousels.
- rendu (mécanisme `desktop_only`) - ces deux liens restent dans le DOM à 0 × 0 px, `visibility: visible`, `display: inline-flex` : 2 éléments focalisables de taille nulle dans l'ordre de tabulation mobile.
- `templates/index.json:144-145` - « - 2 000 clients satisfaits » en `desktop_only` : preuve retirée sur mobile ; tiret-moins ASCII au lieu d'un tiret cadratin.
- `templates/index.json:316,340` - les deux badges de confiance du hero partagent le pictogramme `priority` ; groupe en `layout_direction_mobile: "column"`, écart mesuré 10 px entre les deux lignes.
- `templates/index.json:1155,1179,1203` - les trois étapes « Choisissez / Nous préparons / Vous signez » partagent le pictogramme `verified` : aucune différenciation, aucune numérotation d'étape.
- `templates/index.json:1233-1235` - bouton `button_style: "primary"`, `label: "Le configurateur ouvre bientôt"` vers `shopify://pages/configurateur` : le CTA le plus fort de la page ne mène à aucune action, et double le message de la barre d'annonce.
- `templates/index.json:1262,1873` - `image_ratio: "adapt"` sur deux images de section : aucune réservation d'espace, décalage de mise en page au chargement.
- `templates/index.json:383-384` - hero `show_arrows: false` + `show_pagination: true` sur une bannière à une seule diapositive.
- `templates/index.json:31` - `image_filter_opacity: 30` avec `#000000` sur `noirmont-hero.jpg` : sous-titre et badge d'avis posés sur un bracelet acier clair, contraste insuffisant constaté en capture 375 px.
- `templates/index.json:749-750,1640-1641` - `sales_badge: "amount"` + `show_sales_badge_text: false` : « -€90 » rendu `color: rgb(11, 11, 12)`, 14 px, fond transparent, tiret-moins ASCII — l'économie est moins saillante que le prix.
- rendu `.price` / `.compare-at-price` - `font-variant-numeric: normal` ; **0 occurrence** de `font-variant-numeric` sur 203 Ko de CSS : pas de chiffres tabulaires alors que 8 prix s'alignent en rangée de carrousel.
- rendu `.compare-at-price` - `<span>` (pas `<s>`/`<del>`), même couleur `#0B0B0C` et même corps 16 px que le prix actif, distingué par le seul `line-through`, sans libellé pour lecteur d'écran.
- `templates/index.json:2400-2401` - `same_as_desktop: true` alors que `layout_flex_direction_mobile: "row"` + `layout_wrap_mobile: "nowrap"` sont posés sur la section de capture e-mail : réglage contradictoire, inerte aujourd'hui, écrase la section si `same_as_desktop` repasse à `false`.
- `templates/index.json:2367` - rendu `input[name="contact[email]"]` à `font-size: 14px` : zoom automatique de Safari iOS à la mise au point ; label présent mais masqué visuellement (correct).
- rendu bouton d'envoi newsletter - 50 × 50 px, contenu `send`, sans `aria-label`.
- rendu home - 95 `<img>`, 33 en `loading="lazy"` : 62 images non différées sur une page de 7 784 px de haut.
- rendu ordre des titres - `H1` puis 23 `H2` puis 3 `H3` : plan de document plat, noms de produits au même rang que les sections.
- rendu hero - `fetchpriority="high"`, `width`/`height` déclarés, `alt` descriptif sur `noirmont-hero.jpg`. Aucun écart.

## sections/footer-group.json

- `sections/footer-group.json:530-536` - bloc `social-icons` : les 4 liens rendus pointent vers `facebook.com/themefullstack/`, `instagram.com/themefullstack/`, `youtube.com/@themefullstack`, `linkedin.com/company/themefullstack/` — comptes du fournisseur du thème, `target="_blank"` sans `rel="noopener noreferrer"`, sur une boutique publiée.
- `sections/footer-group.json:535-536` - `icon_color: "#ffffff"` (blanc pur, hors palette craie `#FAFAF7`) ; couleur de lien rendue `rgb(0, 0, 238)` — bleu par défaut du navigateur ; cibles 24 × 24 px.
- `sections/footer-group.json:712-717` - bloc `powered-by-fullstack` en `mode: "badge"` : marque et lien sortants du fournisseur de thème en pied de page.
- `sections/footer-group.json:561,579` - colonne titrée « La Maison » alimentée par `main-menu` (Montres, Accessoires, Configurateur, La Maison, FAQ, Contact) : un lien « La Maison » sous un titre « La Maison », libellé de colonne trompeur ; « Informations » alimenté par `footer` duplique FAQ/Contact/La Maison.
- rendu liens de pied - 10 liens de navigation de 20 px de haut, pas vertical 38-39 px : hauteur de cible sous 44 px, espacement inter-cibles ~19 px.
- `sections/footer-group.json:93` - « Comptez généralement 2 à 3 semaines après la commande » : seule mention du délai réel, à ~6 700 px du haut, alors que « Livraison offerte » est promis dès la barre d'annonce et le hero.
- `sections/footer-group.json:448` - bandeau de réassurance en `layout_grid_columns_mobile: 2`, icônes 42 px : correct sur mobile. Aucun écart.

## assets/noirmont-custom.css

- `assets/noirmont-custom.css:87,139` - `min-height: 24px` (desktop) / `69px` (mobile) en dur sur `.product-card .text-block.paragraph` : réserve calibrée sur l'état du catalogue au 25/07 ; tout nom plus long désaligne les prix de la rangée. L'avertissement est consigné :83-86 mais la dette reste.
- `assets/noirmont-custom.css:102,148` - texte du badge « En promotion » à 11 px puis 10 px sur mobile, boîte rendue 101 × 18 px : sous le plancher de 12 px.
- `assets/noirmont-custom.css:107` - filet `rgba(169, 142, 95, 0.55)` (laiton `#A98E5F`) : second accent, hors palette A+B qui n'autorise qu'un accent citron acide `#D6FF3F`.
- `assets/noirmont-custom.css:47,56` - effet de rapproché d'image attaché à `:hover` seul, sans équivalent au tap : inopérant sur mobile alors que le fichier est titré « Mobile d'abord » (:127).
- `assets/noirmont-custom.css:116-117,134-135` - règles `.main-collection .main-collection__products-grid` : chargées sur la home sans y servir.
- `assets/noirmont-custom.css:20-23` - surcharge de `--font-body--size` en `:root` plutôt que par les réglages de typographie du thème : contourne l'échelle mobile de l'éditeur, l'alternative est documentée :16-18 mais non retenue.
- `assets/noirmont-custom.css:51-59` - garde `prefers-reduced-motion: reduce` correctement posé. Aucun écart.

## assets/noirmont-megamenu.css

- `assets/noirmont-megamenu.css:9,101,116,119` - `vert jura #1E3A2F` et `laiton #A98E5F` déclarés comme palette maison : deux accents supplémentaires. `#D6FF3F` : **0 occurrence** sur les 203 Ko de CSS servis.
- `assets/noirmont-megamenu.css:94` - `text-transform: none !important` : correctif de spécificité qui masque un réglage global de casse au lieu de le corriger à la source (même motif dans `noirmont-collection.css` et `noirmont-see-more-fix.css:21-22`).
- `assets/noirmont-megamenu.css:100-101` - changement de couleur de légende sur `:hover` seul, hors `@media (width > 750px)` (contrairement au zoom :71-72) : affordance inatteignable au tap.
- `assets/noirmont-megamenu.css:136-139` - « Nos familles » à 11 px, `rgba(11, 11, 12, 0.55)` : sous le plancher de 12 px, contraste ≈ 4,7:1 (limite).
- `assets/noirmont-megamenu.css:26-27,156-163` - garde-fous `max-width: 100vw` / `overflow-x: clip` efficaces : `scrollWidth` = `clientWidth` = 375, **aucun débordement horizontal** sur la home. Aucun écart.
- rendu vignettes du tiroir - 147 × 138 px : deux des quatre premières vignettes sont des macros extrêmes (lunette, tranche de cadran) qui ne signalent pas la famille.

## Transverse — palette, typographie, focus

- rendu face d'affichage - logo et H1 en didone à fort contraste (empattements filiformes) : la direction A+B spécifie une **grotesque haute en capitales**. Écart de direction typographique.
- rendu couleurs - `rgb(0, 0, 0)` relevé 474 fois en parallèle de l'encre `#0B0B0C` (1 307) : deux noirs concurrents.
- rendu étoiles d'avis - `fill: rgb(0, 182, 122)` = `#00B67A` (SVG Trustpilot du thème) au lieu du `#05b67a` retenu. Décision assumée, valeur non conforme.
- rendu accents - deux accents actifs (`#1E3A2F` 8 occurrences, `#A98E5F` 6) + bleu de lien par défaut sur les icônes sociales, pour un accent unique attendu.
- CSS du thème - `.dialog-modal:focus-visible{outline:none}`, `.select:focus-visible{outline:none;box-shadow:none}`, `.quantity-selector input:focus-visible{outline:none;box-shadow:none}`, `.stories__modal:focus-visible{outline:none}` : anneau de focus supprimé sans remplacement.
- rendu animations - `marquee-motion` correctement borné par `@media (prefers-reduced-motion: no-preference)`. Aucun écart.
- rendu formulaire - `input[type=email]` avec `autocomplete="email"`, `type` correct, `<label for>` présent. Aucun écart.

---

# Classement par impact conversion

## BLOQUANT (3)

| Constat | Justification |
| --- | --- |
| `sections/footer-group.json:530-536` — 4 liens sociaux vers `themefullstack` | Le pied de page d'une boutique publiée envoie le trafic vers les comptes du fournisseur de thème : fuite hors tunnel, en nouvel onglet, sans `rel=noopener`. |
| `sections/footer-group.json:712-717` — badge « Powered by FullStack » | Lien sortant + marque tierce sur une page qui vend un positionnement de maison : contredit la promesse et détourne. |
| `templates/index.json:654-657,1545-1548` — « Voir toutes les montres » / « Voir les accessoires » en `desktop_only` | Sur l'appareil prioritaire, les deux carrousels n'offrent plus aucune sortie vers la collection : le chemin principal vers l'achat est coupé. |

## FORT (11)

| Constat | Justification |
| --- | --- |
| Header mobile : `.header__menu-mobile` 24 × 65, `.header__icon-search` 24 × 24, `<cart-icon>` 24 × 24, sans `aria-label` | Les trois points d'entrée de la navigation mobile sont sous 44 × 44 et sans nom accessible : le taux d'échec au tap frappe la première interaction. |
| `<cart-icon>` sans `role`/`tabindex`/ancre | Le panier, dernière étape avant paiement, est inatteignable au clavier et annoncé « local_mall ». |
| Tiroir sans `role`/`aria-modal`, focus non déplacé, voile `rgba(0,0,0,0)` | La seule navigation mobile n'est pas un dialogue : ni piège de focus, ni assombrissement, ni fermeture signalée. |
| `overscroll-behavior` absent (0/203 Ko) sur tiroir et panier défilables | Le chaînage de défilement fait sauter la page derrière et perdre la position : abandon en pleine navigation. |
| `input[name="contact[email]"]` à 14 px | Safari iOS zoome à la mise au point : l'unique formulaire de capture est déformé au moment de la saisie. |
| 62 images non différées, dont 10 dans le tiroir fermé (`header-group.json:420-425`) | Bande passante mobile consommée avant le premier écran : le LCP du hero se dégrade sur la page d'entrée. |
| `templates/index.json:31` — filtre 30 % sur `noirmont-hero.jpg` | Proposition de valeur et badge d'avis illisibles sur le bracelet acier : le premier écran ne délivre pas son message. |
| `templates/index.json:174-175` vs `:1782` — H1 32 px = H2 32 px | Sans dominance du H1, l'œil ne trouve pas la promesse au-dessus de la ligne de flottaison. |
| `templates/index.json:1233-1235` — CTA primaire « Le configurateur ouvre bientôt » | Le bouton le plus fort de la page ne convertit rien et dilue l'attention réservée à « Découvrir les montres ». |
| `sections/header-group.json:110-113` — autoplay 4 s sans pause + flèches sur le texte | La réassurance livraison défile avant d'être lue et se fait chevaucher par les flèches : preuve gaspillée. |
| Prix sans chiffres tabulaires + prix barré indistinguible du prix actif | La zone de décision est la ligne de prix : colonnes qui dansent d'une carte à l'autre et remise illisible. |

## MOYEN (18)

| Constat | Justification |
| --- | --- |
| `layout/theme.liquid:37,52` — pas de lien d'évitement, pas de `<main>` | Navigation clavier et lecteurs d'écran obligés de traverser annonce, header et tiroir à chaque page. |
| `templates/index.json:1262,1873` — `image_ratio: "adapt"` ×2 | Décalage de mise en page au chargement, mal-clics et frustration en défilement mobile. |
| `templates/index.json:725,1616` — titres produit en `<h2>` | 16 H2 au même rang que les sections : plan de page illisible pour l'assistance et pour le SEO. |
| `templates/index.json:1977-1978,2063,2148` — puces de spécifications en `<p>` stylées h2 | L'appareil pédagogique (calibre, acier, sans logo) n'existe pas dans la structure du document. |
| `templates/index.json:316,340` — pictogramme `priority` dupliqué | Deux réassurances distinctes portent le même signe : la seconde ne se lit plus. |
| `templates/index.json:1155,1179,1203` — pictogramme `verified` ×3 | Un processus en trois étapes sans différenciation ni numérotation ne se comprend pas d'un coup d'œil. |
| `templates/index.json:144-145` — preuve « 2 000 clients » en `desktop_only` | La preuve sociale disparaît sur l'appareil prioritaire ; deux liens 0 × 0 px polluent la tabulation. |
| `sections/footer-group.json:561,579` — colonne « La Maison » contenant « La Maison » | Libellé circulaire qui fait échouer la recherche des pages de confiance en fin de page. |
| Liens de pied de page 20 px de haut, pas 38-39 px | Dix cibles sous 44 px là où se trouvent CGV, retours et contact : friction sur les pages de lever de doute. |
| `assets/noirmont-custom.css:102,148` — badge à 10-11 px | Le signal de promotion est sous le plancher de lisibilité : la remise ne se voit pas. |
| `assets/noirmont-megamenu.css:136-139` — « Nos familles » 11 px à 4,7:1 | L'étiquette qui organise le tiroir mobile est au seuil de lisibilité. |
| Deux accents actifs (`#1E3A2F`, `#A98E5F`), `#D6FF3F` absent | La direction retenue impose un accent unique : trois signaux concurrents diluent le repère d'action. |
| Face d'affichage didone au lieu d'une grotesque haute | Écart de direction typographique sur le logo et le H1 : l'identité promise n'est pas celle rendue. |
| `assets/noirmont-custom.css:47,56` + `megamenu.css:100-101` — affordances `:hover` seules | Sur mobile ces retours n'existent pas : les cartes et vignettes paraissent inertes. |
| `assets/noirmont-custom.css:87,139` — `min-height` en dur | Réserve calibrée sur un instantané du catalogue : le premier nom long désaligne toute la rangée de prix. |
| Vignettes du tiroir en macros extrêmes à 147 px | La grille illustrée du tiroir n'aide pas à choisir une famille : elle occupe l'espace sans orienter. |
| `sections/footer-group.json:93` — délai 2 à 3 semaines à ~6 700 px | Le délai réel n'est découvert qu'après l'achat ou jamais : source de litiges et de retours. |
| `outline: none` sur `:focus-visible` (dialog, select, quantity) + aucun `touch-action` | Parcours clavier sans repère visible et latence de tap de 300 ms sur les cibles. |

## FAIBLE (11)

| Constat | Justification |
| --- | --- |
| `layout/theme.liquid:23,26,29,34` — 4 feuilles bloquantes ajoutées, une après `content_for_header` | Quelques dizaines de millisecondes de rendu bloqué ; sensible seulement en 3G. |
| `layout/theme.liquid:13-15` — `preload` redondant sur 3 feuilles | Concurrence de priorité avec la police et l'image LCP, effet marginal. |
| `sections/header-group.json:128-130` — « S'abonner » avec `link: ""` | Bouton mort, mais desktop uniquement et hors chemin d'achat. |
| `templates/index.json:383-384` — pagination sur bannière à une diapositive | Point orphelin ; bruit visuel sans conséquence fonctionnelle. |
| `sections/header-group.json:173,284` — `show_arrows` inerte en `grid` | Réglage sans effet ; dette de configuration. |
| `templates/index.json:2400-2401` — réglage mobile contradictoire inerte | Sans effet aujourd'hui, mais casse la capture e-mail au premier changement de `same_as_desktop`. |
| `assets/noirmont-custom.css:116-117,134-135` — règles `.main-collection` sur la home | Octets inutiles, aucun effet visible. |
| `assets/noirmont-custom.css:20-23` — surcharge `:root` du corps de texte | Fonctionne, mais contourne l'échelle mobile de l'éditeur : dette de maintenance. |
| `assets/noirmont-megamenu.css:94` — `!important` de casse | Masque un réglage global au lieu de le corriger : dette, pas de symptôme utilisateur. |
| Étoiles d'avis en `#00B67A` au lieu de `#05b67a` | Décision assumée, valeur non conforme au référentiel ; écart imperceptible à l'œil. |
| « -€90 » avec tiret-moins ASCII ; 23 `H2` en plan plat | Détails typographiques et de structure sans effet mesurable sur le taux. |

---

**Total : 43 constats — BLOQUANT 3 · FORT 11 · MOYEN 18 · FAIBLE 11.**
