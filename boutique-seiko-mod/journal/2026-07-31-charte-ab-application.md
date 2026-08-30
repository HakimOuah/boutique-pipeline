---
type: journal
boutique: seiko-mod
date: 2026-07-31
nature: intervention
leviers: [page]
titre: "Application de la charte A+B — thème `204248088914` « Maison Noirmont » (`v42pzp-h4`)"
---

# Application de la charte A+B — thème `204248088914` « Maison Noirmont » (`v42pzp-h4`)

Date : **26/07/2026**. Cible vérifiée avant **et** après écriture : `204248088914` = `UNPUBLISHED`,
`204246548818` (« Helio ») = `MAIN` — **aucune requête d'écriture ne l'a visé**, `204329288018`
(fork obsolète) non plus. Aucun thème publié, aucune commande.

Contrôle en rendu : prévisualisation de `204248088914` sur `maisonnoirmont.fr`, **sans saisie de
mot de passe** (cookie de session déjà présent), à **375 px** et **1280 px**.

## Preuve d'écriture — 7 fichiers, empreintes relues

`themeFilesUpsert` renvoie `upsertedThemeFiles: []` sans `userErrors` : écriture **asynchrone**,
pas un échec. Les empreintes ci-dessous sont celles **relues** sur le thème après coup, et elles
sont égales à l'octet près au md5 des fichiers locaux envoyés.

| Fichier | avant (octets / md5) | après (octets / md5) |
| --- | --- | --- |
| `snippets/price.liquid` | 5682 / `4433d235…f7f4ad` | **5817 / `bf4c9a35…6c99b12e3`** |
| `assets/noirmont-custom.css` | 26131 / `3d0bc925…5dadac1` | **36006 / `4bc50fcb…31abf1800a`** |
| `config/settings_data.json` | 7452 / `18500cab…01c85a50df` | **7547 / `f1f9ad57…2ad1b143b3`** |
| `templates/product.json` | 74803 / `6f7f80df…53fbabc1` | **75216 / `2c1ac846…41f8d53fe41`** |
| `blocks/noirmont-specs.liquid` | *(créé)* | **4163 / `a7dea9d9…029e984d75`** |
| `assets/noirmont-marque.svg` | *(créé)* | **460 / `d909fe1e…723791e357`** |
| Fichier boutique `favicon-noirmont-marque.png` | *(créé)* | `gid://shopify/MediaImage/59699539116370`, 512 × 512 |

Sauvegardes octet-exactes de l'état **avant** : `scratchpad/backup-charte-ab/`
(`snippets__price.liquid`, `assets__noirmont-custom.css`, `config__settings_data.json`,
`templates__product.json`) — md5 de chacune égal au `checksumMd5` live d'avant écriture.
Charges utiles écrites : `scratchpad/work-charte-ab/`.

`assets/noirmont-custom.css` a été écrit **trois fois** (v1 → v2 → v3) : deux défauts trouvés au
rendu et corrigés, décrits aux points 1 et 3. Seule la v3 compte, et c'est elle qui est en ligne.

---

## 1. Le bloc de prix — la demande de Hakim

### Avant, mesuré sur une carte produit à 375 px

Quatre signaux pour un seul fait, trois montants qui se suivent sans hiérarchie ni libellé :

| Élément | Mesure avant |
| --- | --- |
| Badge « **En promotion** » | présent sur **toutes** les cartes en promotion (6 relevés d'un coup sur l'accueil), 12 px, en aplat sur la montre |
| Prix actif `€279` | **16 px / graisse 400** |
| Prix barré `€369` | 13 px / 400 |
| Économie `-€90` | **14 px / 500, fond `rgb(250,250,247)`** — exactement le fond de la carte : aucune forme, aucun libellé, un troisième montant |

Rendu : `€279  €369   -€90`.

### Après, mêmes conditions

Rendu : `€279  ~~€369~~  [ ÉCONOMIE €90 ]`.

| Élément | Mesure après |
| --- | --- |
| Badge « En promotion » | **supprimé** — `show_sales_badge_on_cards` passé à `false` dans `config/settings_data.json`. Relevé : **0 badge de promotion** sur l'accueil, à 375 comme à 1280 px |
| Prix actif | **20 px / graisse 600** à 375 px, **22 px** à 1280 px — contraste **18,81:1** |
| Prix barré | **13 px / graisse 400**, `line-through`, couleur héritée, **aucune opacité** — contraste **18,81:1** (réglage 9.9 de la passe précédente **non touché**, comme demandé) |
| Économie | **pastille citron pleine `#D6FF3F`, texte encre, libellé « ÉCONOMIE » + montant en graisse 700** — contraste **17,08:1** |

Rapport de corps prix actif / prix barré : **1,54×** (20 / 13) contre 1,23× avant.
Contraste minimum relevé sur **les 16 blocs de prix visibles de l'accueil**, prix + barré +
pastille confondus, opacité héritée comprise : **15,50:1** — aux deux largeurs.
Sur la fiche produit la pastille affiche « ÉCONOMIE 23% » (`sales_badge: percentage`).

### Nom accessible — vérifié, pas déduit

| Élément | Valeur mesurée après |
| --- | --- |
| Bloc de prix de la fiche | **« €329 Ancien prix : €429 Économie 23% »** |
| Carte produit de l'accueil | **« €279 Ancien prix : €369 Économie €90 »** |
| Bouton d'ajout au panier | **« Ajouter au panier €329 »** (ancien prix `aria-hidden`, il reste annoncé par le bloc principal juste au-dessus) |

**Le libellé « Ancien prix : » a été sorti du nœud `[data-ref="compare-at-price"]`.**
`assets/product-price.js` réécrit l'`innerHTML` de ce nœud à chaque changement de variante :
tant que le libellé vivait dedans, il disparaissait au premier clic sur une variante. Il est
maintenant dans un `<span class="compare-at-price-wrap">` parent, que le JS ne touche pas.
Le wrap se masque tout seul quand le montant est vide
(`.compare-at-price-wrap:has(.compare-at-price:empty){display:none}`) — **vérifié en rendu** :
montant vidé → `display: none`, montant remis → `display: block`.

### Défaut que j'ai introduit, trouvé au rendu et corrigé (CSS v2)

`.badge--savings { display: inline-flex !important }` **écrasait** la règle
`.badge:has(.badge__savings:empty){display:none}` du snippet. Conséquence : une fiche **sans**
prix barré aurait affiché une pastille « ÉCONOMIE » **vide**. Repris par
`.badge--savings:has(.badge__savings:empty){display:none !important}`.
Vérifié après correction : montant vidé → `display: none` ; remis → `display: flex`.

---

## 2. Le logo

| | Avant | Après |
| --- | --- | --- |
| En-tête mobile 375 px | lettrage de rapport **13,8:1**, plafonné à 179 × 13 px utiles à côté de trois cibles de 44 px | **marque en anneau, 30 × 30 px**, centrée, lien de **44 px** de haut |
| Nom accessible du lien | « Maison Noirmont » | **« Maison Noirmont »** — inchangé |
| En-tête desktop 1280 px | wordmark 300 × 28 px | **wordmark 300 × 28 px — inchangé** |
| Hauteur du bandeau d'en-tête | 65 px + 0,5 px de filet | **`height: 65.5px` — inchangée**, à 375 comme à 1280 px |
| Débordement horizontal | aucun | **aucun** (`scrollWidth − clientWidth = 0` aux deux largeurs) |

Le fichier `scratchpad/brandkit/noirmont-marque.svg` a été **téléversé tel quel** dans le thème
(`assets/noirmont-marque.svg`, 460 o, empreinte relue). Le rendu de l'en-tête n'y puise pas par
requête réseau : le même tracé est embarqué en **masque CSS** dans `noirmont-custom.css` (bloc
10.5) et peint avec `background-color: currentColor` — la marque suit donc le schéma de couleurs
de l'en-tête, exactement comme le `currentColor` du fichier source.

**Le wordmark n'est ni supprimé ni remplacé.** Sous 750 px il est retiré du flux *visuel* par la
technique du texte hors écran (1 px + `clip-path`), ce qui le laisse dans l'arbre d'accessibilité
— d'où le nom accessible préservé. Retirer le bloc 10.5 le fait réapparaître tel quel : le retour
en arrière tient en une suppression de bloc CSS.

**Favicon** : `favicon-noirmont-marque.png`, 512 × 512, marque craie sur carré encre à coins
arrondis (une marque encre sur fond transparent disparaîtrait dans un onglet sombre). Posée sur
la clé `favicon` de `settings_data.json`. Vérifié au rendu : **1 balise `<link rel="icon">`**
servie, contre **0 avant**.

**Non appliqué, volontairement** : l'association marque + wordmark en desktop. Elle était offerte
(« tu peux »), pas demandée ; l'ajouter risquait de toucher à la hauteur du bandeau, que la
consigne demande de ne pas faire bouger. À trancher par Hakim.

---

## 3. La typographie d'affichage

| Rôle | Avant | Après |
| --- | --- | --- |
| Source | `font_from: custom` (3 fichiers `.woff2` téléversés) | **`font_from: shopify`** — la bibliothèque du sélecteur de polices du thème |
| Affichage (h1, h2, h3) | **Bodoni Moda 500** — une didone | **Oswald 500** — grotesque haute et serrée, taillée pour les capitales |
| Sous-titres (h4, h5, h6) | Space Grotesk 500 | Inter 500 |
| Corps | Inter 400 (fichier personnalisé) | Inter 400 (bibliothèque) |

Vérifié au rendu : `--font-heading--family` = `Oswald, sans-serif`, et la fonte est bien
**chargée** (`Oswald/500/loaded` dans `document.fonts`), donc le nom est bien reconnu par la
bibliothèque Shopify — aucune police absente n'a été imposée. `<h1>` de l'accueil : **40 px,
Oswald, casse normale**. Titre de fiche : 24 px, Oswald.

**La casse normale des titres de contenu n'a pas été défaite** : `type_case_h1` et `type_case_h2`
restent à `none`. Les capitales restent là où elles étaient déjà — `type_case_h4` (surtitres),
boutons, badges — et c'est précisément là que la tenue en capitales d'Oswald sert. **Point à
arbitrer par Hakim** : la direction dit « en capitales pour l'affichage » ; forcer les capitales
sur le `<h1>` du hero contredirait la règle « casse normale sur les titres de contenu » posée à
la passe précédente, puisqu'un seul réglage gouverne les deux. Je n'ai pas tranché seul.

### Défaut trouvé au rendu et corrigé (CSS v3) — les chiffres tabulaires

Le changement de police **cassait** les chiffres tabulaires, et la déclaration
`font-variant-numeric: tabular-nums` du bloc 9.8 ne suffisait pas à le voir : **elle était
devenue inopérante**. Largeurs mesurées à 20 px :

| Police | `111111` | `888888` | `000000` | Tabulaire ? |
| --- | --- | --- | --- | --- |
| Inter personnalisé (avant) | 77,81 | 77,81 | 77,81 | **oui** |
| Inter de la bibliothèque Shopify | 47,04 | 72,78 | 75,01 | **non** — identique avec et sans `tabular-nums` : la fonte servie n'expose pas `tnum` |

Correctif : le fichier `inter-400.woff2` **déjà hébergé par la boutique** est réenrôlé sous le nom
`NM Chiffres`, avec un `unicode-range` limité aux chiffres et aux signes qui les accompagnent
(`0-9 , . % € − espace`), et appliqué aux seuls contextes de prix. Les lettres continuent d'être
rendues par l'Inter de la bibliothèque : aucune double police visible.

Vérifié après correction, dans le rendu : prix **76,62 / 76,62 / 76,62**, pastille
**48,13 / 48,13 / 48,13**, prix barré **44,26 / 44,26**. **Tabulaires partout.**

Les clés `custom_type_*` ont été **conservées telles quelles** dans `settings_data.json` : basculer
`font_from` sur `custom` restitue l'état d'avant en une valeur.

---

## 4. Les puces de spécifications

Nouveau bloc `blocks/noirmont-specs.liquid` (nom de schéma « **Puces specs** », 11 caractères —
sous la limite de 25 qui fait rejeter un fichier en silence), inséré dans `templates/product.json`
en position 4 de `sections.main.block_order`, **juste sous le titre** `text_zLqMQw` et au-dessus
du prix. Diff structurel du template : **9 ajouts, 0 suppression**, les seules « modifications »
étant le décalage d'indice des entrées de `block_order`.

Aucune valeur n'est déduite, complétée ni supposée. Rendu mesuré à 375 px :

| Fiche | Puces rendues |
| --- | --- |
| `trente-neuf-classique-cannelee` | **36 MM / 39 MM** · **MIYOTA 8215 / NH35** · **CADRAN ORANGE** |
| `integrale-brun-or-rose-sport-chic` (sans diamètre) | **NH35** · **CADRAN BRUN** — **aucune puce de diamètre** |
| `bracelet-caoutchouc-gaufre` (accessoire) | **aucun nœud `.nm-specs` dans la page** |

Puces : 12 px, capitales, contraste **18,81:1**, couleur héritée du schéma du bloc (donc lisibles
aussi sur les blocs à schéma sombre), chiffres tabulaires.

**« 10 BAR » n'est pas rendu, et c'est délibéré.** L'exemple de la consigne le cite, mais il
n'existe **aucun métachamp d'étanchéité** : les seuls champs réels sont `custom.diametre`,
`custom.calibre` et `custom.couleur_cadran`. Afficher « 10 bar » aurait supposé une valeur — et
serait faux pour les 7 Intégrale, données à 3 bar. De même, aucune puce « AUTOMATIQUE » n'est
déduite du calibre : les 12 chronographes tournent en méca-quartz VK63. Le calibre est affiché
tel qu'il est stocké, ce qui est vrai pour les 53 montres.

---

## Ce qui n'a pas pu être appliqué / est laissé à arbitrage

1. **Les captures avant/après n'ont pas pu être écrites sur le disque.** Le mode « enregistrer »
   de l'outillage navigateur retourne un succès mais ne dépose aucun fichier atteignable. Les
   deux crops ont bien été faits et lus à 375 px — avant : `€279 €369 -€90` sur une seule ligne,
   sans forme ni libellé ; après : `€279`, `€369` barré, puis la pastille citron
   `ÉCONOMIE €90`. À défaut du fichier, toutes les valeurs chiffrées de la section 1 constituent
   la preuve.
2. **Capitales du `<h1>` d'affichage** : non forcées, voir point 3 — un seul réglage gouverne
   titres d'affichage et titres de contenu.
3. **Marque + wordmark en desktop** : non appliqué, voir point 2.
4. **Interlettrage `heading-loose`** (`type_letter_spacing_h1/h2`, 0,03 em) : calibré pour des
   capitales, il reste en place sur des titres passés en casse normale et sur une grotesque
   serrée. Signalé par la passe précédente, toujours non tranché — je ne l'ai pas touché.
5. Le badge « Épuisé » et le badge de métachamp gardent leur mise en forme, mais leur **filet
   citron a été neutralisé** (repassé en encre) : depuis que l'économie porte le citron en aplat,
   le garder ailleurs aurait dédoublé l'accent. Le citron est désormais **le signal unique de la
   remise**.

## Garde-fous respectés

Aucun produit, SKU, prix, variante, média ni mapping DSers approché. **Aucun slider ni avis de
démonstration modifié**, ni le « 2 000 clients satisfaits », ni les trois `review_count: 123`.
Aucune promesse produit non vérifiable introduite — les seuls textes ajoutés sont « Économie »,
« Ancien prix : » et « Cadran », tous des libellés. Aucun thème publié, aucune commande, aucun
mot de passe saisi. Écritures limitées à `204248088914`.

---

# Révision du 26/07/2026 au soir — retour de Hakim sur téléphone

Trois inflexions, appliquées sur le même thème `204248088914` (`UNPUBLISHED` vérifié avant et
après). Deux fichiers réécrits ; le reste de la passe est inchangé.

| Fichier | avant révision | après révision |
| --- | --- | --- |
| `assets/noirmont-custom.css` | 36006 / `4bc50fcb…31abf1800a` | **41510 / `54652d8b…f7f0caa51f4`** |
| `blocks/noirmont-specs.liquid` | 4163 / `a7dea9d9…029e984d75` | **5002 / `bd5013b7…4e6272cb30b`** |
| Fichier boutique `logo-noirmont-mot-encre.png` | *(créé)* | `gid://shopify/MediaImage/59701292499282`, 1284 × 157 |

## R1. Le wordmark reprend l'en-tête, mobile compris

L'anneau seul se lisait comme une icône d'interface — constat de Hakim, appliqué.

| | Avant révision | Après révision |
| --- | --- | --- |
| En-tête mobile 375 px | anneau 30 × 30 px | **lettrage « NOIRMONT », 179 × 22 px** |
| Hauteur de glyphe mobile | — | **22 px**, contre **13 px** pour « MAISON NOIRMONT » à la même largeur : **× 1,85** |
| En-tête desktop 1280 px | wordmark 300 × 28 px | **wordmark 300 × 28 px — inchangé, « MAISON NOIRMONT » entier** |
| Nom accessible du lien | « Maison Noirmont » | **« Maison Noirmont » — entier, inchangé** |
| Bandeau d'en-tête | 65,5 px | **65,5 px — inchangé**, à 375 comme à 1280 |
| Chevauchement d'icônes | aucun | **aucun** ; colonne logo 179 px entre trois cibles de 44 px, `scrollWidth − clientWidth = 0` |

Le problème de dimensionnement est résolu par le **cadrage**, pas par un redessin : le mot
« NOIRMONT » est **découpé dans le lettrage d'origine** (colonnes 1088 → 2372 du fichier
2379 × 172), ce qui fait passer le rapport de **13,83:1 à 8,18:1**. Rien n'a été redessiné, aucune
police de substitution n'a été employée. Le fichier est téléversé dans les fichiers de la
boutique, donc remplaçable par Hakim sans toucher au code.

L'anneau **reste** : favicon (inchangé) et **marque secondaire du pied de page** (22 px, au-dessus
du wordmark, en `currentColor` — mesuré craie sur le pied de page sombre). `assets/noirmont-marque.svg`
reste en place dans le thème.

## R2. Citron acide → cyan électrique, avec règle d'usage

`--nm-citron: #D6FF3F` **supprimée** ; `--nm-cyan: #22D3EE` la remplace. Vérifié au rendu :
**0 règle contenant `#D6FF3F`** dans les feuilles servies, à 375 comme à 1280 px, et la variable
`--nm-citron` n'existe plus.

**Le cyan est la couleur de l'instrument.** Emplois retenus, et eux seuls :

| Emploi | Statut | Mesure |
| --- | --- | --- |
| Trait de cote des puces de spécifications | **cyan** | `inset 2px 0 0 rgb(34,211,238)` — décoratif, l'information est dans le texte |
| Anneau de focus `:focus-visible` | **cyan** | cyan cerné d'un halo d'encre de 6 px |
| `accent-color` (cases, radios) — état actif | **cyan** | — |
| `::selection` — état actif | **cyan** | cyan sur encre, **10,70:1** |
| Pastille « ÉCONOMIE » | **achromatique** | encre sur craie, filet pleine force — **18,81:1** |
| Badges « Épuisé » / métachamp | **achromatique** | filet latéral repassé en encre **à la source** (bloc 9.10), pas seulement écrasé plus bas |
| Boutons d'achat | **jamais touchés** | — |

La pastille d'économie reste **nettement distincte des deux prix** par trois traits cumulés :
elle est **encadrée** (les prix ne le sont pas), son libellé est en **capitales espacées**
(0,1 em), et son montant est en **graisse 700 / 12 px** là où le prix actif fait 20 px / 600 et le
prix barré 13 px / 400 barré. Couleurs héritées du schéma : **18,81:1** sur craie, **11,80:1** sur
bloc sombre. Contraste minimum sur les 16 blocs de prix visibles de l'accueil, prix + barré +
pastille : **15,50:1**, aux deux largeurs.

**Mesure à connaître** : le cyan sur craie ne vaut que **1,72:1**. Il ne peut donc jamais porter
seul une information, et il n'en porte aucune — c'est aussi pourquoi les terminaisons des filets
de cote sont en encre et non en cyan. Sur encre il monte à 10,70:1. À noter, le citron était
**pire** sur ce point (1,05:1 sur craie) : l'anneau de focus y gagne.

Les étoiles d'avis restent en **vert Trustpilot `#05b67a`** — décision de Hakim, non touchée.

## R3. L'appareil technique rendu visible

Un élément technique par zone, pas trois.

- **Puces de spécifications traitées en instruments** (zone fiche produit) — encadré fin
  (1 px à 22 % de la couleur courante), **libellé en capitales espacées** (10 px, 0,18 em :
  « DIAMÈTRE », « CALIBRE », « CADRAN »), **valeur sur sa propre ligne**, et **trait de cote cyan**
  de 2 px en flanc gauche. Rendu mesuré : `DIAMÈTRE / 36 mm / 39 mm` (123 × 42 px),
  `CALIBRE / Miyota 8215 / NH35` (162 × 42), `CADRAN / Orange` (75 × 42). Libellés et valeurs à
  **18,81:1**.
- **Inflexion monospace sur les seules valeurs mesurées** — `ui-monospace` sur diamètre et
  calibre (classe `--mesure`), **pas** sur la couleur de cadran, qui n'est pas une mesure, et
  jamais sur du texte courant. Vérifié tabulaire : `111111` / `888888` / `000000` = **46,66 px**
  pour les trois.
- **Filets de cote en séparateurs** (zone éditoriale) — `.separator-block .separator` reçoit deux
  terminaisons verticales de **1 × 9 px** à ses extrémités, en `currentColor`. Le cyan y a été
  écarté volontairement : à 1,72:1 sur craie il ne se verrait pas à cette taille, et l'accent est
  déjà employé une fois dans la zone produit.

Le libellé « Cadran » est passé du **contenu** vers le **libellé de la puce** : la valeur affichée
est désormais « Orange » et non « Cadran Orange ». Aucune donnée nouvelle, aucune valeur déduite.

## Contrôles de non-régression de la révision

| Contrôle | 375 px | 1280 px |
| --- | --- | --- |
| Débordement horizontal | **0** | **0** |
| Hauteur du bandeau d'en-tête | **65,5 px** | **65,5 px** |
| Badge « En promotion » | **0** | **0** |
| Contraste minimum du bloc de prix (16 cartes) | **15,50:1** | **15,50:1** |
| Chiffres tabulaires (prix, pastille, barré, valeurs mesurées) | **oui** | **oui** |
| Nom accessible du lien logo | **« Maison Noirmont »** | **« Maison Noirmont »** |
| Règles contenant `#D6FF3F` | **0** | **0** |

Cibles de 44 px, focus visible, `<h1>` et hiérarchie de titres, prix barré à ≥ 4,5:1 sans
opacité : **rien de la passe d'accessibilité n'a été défait**. Aucun produit, SKU, prix, variante,
média ni mapping touché ; sliders et avis de démonstration intacts ; aucune valeur de
spécification inventée ; aucun thème publié.

---

# Allègement du 26/07/2026 — après comparaison mobile avec montre-avenue.com

Diagnostic de Hakim, exact : **le traitement d'affichage avait été appliqué au fonctionnel.**
Un seul fichier réécrit, `assets/noirmont-custom.css` : **41510 / `54652d8b…` → 47849 /
`66fb3525…f7fde586cb9`** (empreinte relue). Rien d'autre n'a bougé — ni JSON, ni autre Liquid.

## A1. Oswald redevient une police d'affichage

| Élément | Avant | Après |
| --- | --- | --- |
| Hero (accueil) | Oswald 40 px / 56 px | **Oswald — inchangé** |
| Titres de section | Oswald 24 px / 28 px | **Oswald — inchangé** |
| **Titre produit** | **Oswald 24 px / 500** | **Inter 24 px / 600** — 18,81:1 |
| Bouton d'achat, libellés de variantes, libellés de puces | Inter | **Inter — ils y étaient déjà**, vérifié avant intervention : tous sortaient de `--font-body--family` |

Le conflit didone / grotesque de poster est donc réglé là où il se voyait : le titre produit ne
tient plus le même registre que le wordmark.

## A2. Puces de spécifications — un seul signal au lieu de trois

| | Avant | Après |
| --- | --- | --- |
| Libellé | **CAPITALES**, interlettrage **0,18 em** | **casse normale**, interlettrage normal, 13 px |
| Contenant | **bordure 1 px dure**, angles à 1 px, deux lignes | **fond doux `currentColor` 7 %, aucune bordure, angles 999 px**, une ligne |
| Repère technique | **filet cyan de 2 px en flanc** | **point cyan de 5 px** |
| Valeur mesurée | monospace tabulaire | **monospace tabulaire — conservé** |
| Encombrement (fiche à 375 px) | 3 puces de 42 px de haut, dont 2 sur deux lignes | **3 puces de 31 px** — 123×42 → 202×31, 162×42 → 228×31, 75×42 → 138×31 |
| Contraste libellé / valeur | 18,81:1 | **18,81:1 — inchangé** |

Le côté instrument n'a pas disparu, il a changé de porteur : il vit désormais dans le monospace
de la valeur et le point cyan, pas dans la lourdeur du contenant.

## A3. Sélecteur de variante

| | Avant | Après |
| --- | --- | --- |
| Forme | aplat d'encre, angles 2 px, largeur du conteneur | **contour arrondi 999 px, fond transparent, largeur ajustée au contenu** (« Orange » : 335 → **87 px**) |
| Casse | **CAPITALES**, interlettrage 0,8 px | **casse normale**, interlettrage normal |
| Hauteur | **40 px — sous le plancher tactile** | **44 px sur les 9 pastilles** (gain d'accessibilité au passage) |
| État sélectionné | renversement encre / craie | **filet pleine force + anneau interne de 1 px + fond doux 7 % + graisse 500** contre filet à 26 % / graisse 400 |
| Contraste du libellé | — | **18,81:1 sur les 9 pastilles**, sélectionnées comme non sélectionnées |

L'anneau de focus du bloc 9.1 n'est pas touché : il vise l'`input` radio en `:focus-visible`,
pas le `label`. L'état reste porté nativement par le radio pour les technologies d'assistance,
et visuellement par le poids du filet — jamais par la couleur seule.

## A4. Bouton d'achat

Casse normale, interlettrage ramené de 0,8 px à 0,15 px, angles à 6 px. **Surface et contraste
intacts** : 335 × 50 px à 375 px, craie sur vert `#1E3A2F`, **11,80:1 mesuré**. Il reste
l'élément le plus visible de la page par sa masse, plus par ses capitales.
Sur l'accueil : **7 boutons visibles à 375 px, 0 sous 44 px**, contraste minimum **11,80:1**.

## A5. Respiration

| Conteneur | Avant | Après |
| --- | --- | --- |
| `.product-section__product-info` (13 blocs fonctionnels) | **12 px** | **22 px** (24 px au-dessus de 749 px) |
| `.product-section__content` | 16 px | **24 px** |
| `.variant-picker__options` | — | **20 px** entre groupes d'options |
| Nom d'option → pastilles | — | **8 px** |
| Hauteur de la colonne d'infos produit | 1608 px | **1797 px** — l'air ajouté est visible, pas cosmétique |

Angles adoucis d'un cran sur les surfaces **fonctionnelles seulement** (boutons, champs,
sélecteur de quantité : 0/2 px → 6 px). **Cartes produit et images non touchées** : c'est la
grille qui tient la rigueur, et elle reste.

## La limite tenue

On a allégé la charge visuelle, pas supprimé le point de vue :
**le cyan reste la couleur de l'instrument** (point des puces, anneau de focus, `accent-color`,
`::selection` — jamais un bouton, jamais un badge commercial) ; **les chiffres restent monospace
et tabulaires** ; **les filets de cote restent** (bloc 10.7, terminaisons 1 × 9 px) ; la pastille
« Économie » reste achromatique et distincte.

## Contrôles de non-régression

| Contrôle | 375 px | 1280 px |
| --- | --- | --- |
| Débordement horizontal | **0** | **0** |
| Bandeau d'en-tête | **65,5 px** | **65,5 px** |
| Hero / titres de section en Oswald | **40 / 24 px** | **56 / 28 px** |
| Badge « En promotion » | **0** | **0** |
| Contraste minimum du bloc de prix (16 cartes) | **15,50:1** | **15,50:1** |
| Contraste minimum des boutons visibles | **11,80:1** | **11,80:1** |
| Cibles tactiles sous 44 px (boutons visibles) | **0** | 2 — les deux liens de sortie de collection, **desktop uniquement**, 35 px, hors contexte tactile |
| Pastilles de variante sous 44 px | **0 / 9** | **0 / 9** |
| Chiffres tabulaires (prix, pastille, barré, valeurs mesurées) | **oui** | **oui** |

Étoiles toujours en vert Trustpilot `#05b67a`. Aucun produit, prix, variante, média ni mapping
touché ; sliders et avis de démonstration intacts ; aucune valeur de spécification inventée ;
aucun thème publié. `204248088914` seul écrit, `204246548818` (« Helio ») jamais visé.

---

# Purge du vert forêt et équilibrage des titres — 26/07/2026

Un seul fichier réécrit, `assets/noirmont-custom.css` : **47849 / `66fb3525…` → 54054 /
`8685e465b33a2a539a39531c4fcaf5e8`** (empreinte relue). Blocs 12.1 à 12.4.

## P1. Inventaire du vert `#1E3A2F` et du laiton `#A98E5F` — 28 déclarations

Relevé sur les feuilles **réellement servies** plus un balayage des couleurs **calculées** du DOM
(c'est ce second balayage, et lui seul, qui a fait sortir les deux dernières).

| Source | Vert `#1E3A2F` | Laiton `#A98E5F` | Quoi |
| --- | --: | --: | --- |
| Variables de jeux de couleurs (`<style>` de `color-schemes`, issu de `settings_data.json`) | **8** | **2** | fond + bordure du bouton primaire et du badge secondaire, schémas 1 et 2 ; badge secondaire du schéma 3 en laiton |
| `styles.css` (bundle des `{% stylesheet %}` de sections) | **5** | **3** | barre de livraison (fond, filet, point, mention), icône de réassurance, carte contact, badge « 4× » |
| `noirmont-megamenu.css` | **2** | **1** | survol de légende, lien « Toutes les montres » + son soulignement |
| `noirmont-collection.css` | **2** | **2** | bouton « voir plus » + soulignement, survol des cartes sœurs |
| `<style>` en ligne du tiroir panier | **2** | 0 | `.nm-cart-upsell__title`, `.nm-cart-upsell__price` |
| `noirmont-custom.css` (bloc 5) | 0 | **1** | filet du badge de promotion — **retiré à la source** |
| **Total** | **19** | **9** | **28** |

**Après purge, au rendu : 0 élément peint en vert ou en laiton**, à 375 comme à 1280 px, sur
l'accueil comme sur la fiche produit (balayage de tous les nœuds : `background-color`, `color`,
bordures, `box-shadow`).

Méthode : la purge est portée **là où la couleur est déclarée**. En particulier on ne touche ni
`:root` ni `.color-scheme-3` pour le bouton primaire — le schéma sombre définit le sien en craie
sur encre, et l'écraser depuis `:root` l'aurait rendu encre sur encre, donc invisible. Vérifié :
**0 bouton primaire cassé en schéma sombre**.

## P2. Bouton d'achat — le contraste augmente

| | Avant | Après |
| --- | --- | --- |
| Fond | vert `#1E3A2F` | **encre `#0B0B0C`** |
| Texte | craie `#FAFAF7` | craie `#FAFAF7` |
| **Contraste mesuré** | **11,80:1** | **18,81:1** |
| Surface | 335 × 50 px (375 px) / 540 × 50 px (1280 px) | **inchangée : 335 × 50 / 540 × 50** |
| Casse | casse normale | casse normale |

Il gagne donc en présence, pas seulement en conformité de palette. **Aucun cyan sur ce bouton** :
la règle l'interdit sur un élément commercial, et à 1,72:1 sur fond clair il serait illisible.

## P3. « Livraison gratuite »

| | Avant | Après |
| --- | --- | --- |
| Casse | **CAPITALES** | **casse normale** |
| Couleur | vert `#1E3A2F` | **encre `#0B0B0C`** |
| Contraste | — | **16,93:1** (encre sur `rgb(238,238,235)`, fond du bloc composé, veile d'encre à 5 % comprise) |

L'**acier `#8A9099`** a été essayé pour garder la mention secondaire : **3,06:1 sur craie**, sous
le seuil de 4,5:1 d'un texte. Écarté. La mise en retrait est portée par le corps (12,8 px) et la
graisse, pas par la couleur — même principe que le prix barré du bloc 9.9.
Fond et filet de la barre repassés en encre transparente (5 % et 14 %).

## P4. Équilibrage des retours à la ligne

`text-wrap: balance` sur `h1`, `h2`, `h3`, les titres de blocs de texte et les titres de cartes.
Vérifié au rendu : `text-wrap` calculé = **`balance`**, le titre produit ne laisse plus « 42 » (ni
« cannelée ») seul sur la seconde ligne. **Repli explicite** : la règle est enfermée dans
`@supports (text-wrap: balance)`. Là où la propriété n'existe pas, rien n'est appliqué — le texte
se coupe normalement, simplement sans équilibrage, et aucun autre réglage n'en dépend.

## Contrôles de non-régression

| Contrôle | 375 px | 1280 px |
| --- | --- | --- |
| Éléments peints en vert / laiton | **0** | **0** |
| Bouton d'achat | **18,81:1**, 335 × 50 px | **18,81:1**, 540 × 50 px |
| « Livraison gratuite » | **16,93:1** | **16,93:1** |
| Contraste minimum du bloc de prix (16 cartes) | **15,50:1** | **15,50:1** |
| Contraste minimum des boutons visibles (accueil) | **15,50:1** | **15,50:1** |
| Cibles sous 44 px (boutons, pastilles de variante, icônes d'en-tête) | **0** | **0** |
| Débordement horizontal | **0** | **0** |
| Bandeau d'en-tête | **65,5 px** | **65,5 px** |
| Badge « En promotion » | **0** | **0** |
| `text-wrap` des titres | **balance** | **balance** |
| Étoiles d'avis | **`rgb(5, 182, 122)`** — vert Trustpilot intact | **idem** |

Pastille d'économie toujours achromatique, puces toujours allégées (fond doux, point cyan,
monospace tabulaire), filets de cote, espacements, focus visible : **rien n'a été défait**.
Aucun produit ni prix touché, sliders et avis de démonstration intacts, aucune publication.
`204248088914` seul écrit, `204246548818` (« Helio ») jamais visé.

---

# Purge à la source — 27/07/2026

La purge précédente était une **surcharge**, pas un correctif : le vert et le laiton restaient
dans `config/settings_data.json` et l'éditeur de thème pouvait les faire réapparaître au premier
réenregistrement d'un jeu de couleurs. Corrigé à la source.

| Fichier | avant | après |
| --- | --- | --- |
| `config/settings_data.json` | 7547 / `f1f9ad57e0e67350df125d2ad1b143b3` | **7547 / `e51fe7c4225816f6fd4097b2545cd611`** |
| `assets/noirmont-custom.css` | 54054 / `8685e465b33a2a539a39531c4fcaf5e8` | **54405 / `68f5fae7c77fd4359426adcadb4f624d`** |

Sauvegardes de l'état d'avant : `scratchpad/backup-charte-ab/config__settings_data.AVANT-purge-source.json`
et `assets__noirmont-custom.AVANT-purge-source.css` (md5 égaux aux valeurs « avant » ci-dessus).

## S1. Les 10 valeurs sources, remplacées teinte par teinte et rôle par rôle

Balayage de **tous les chemins de clés** du fichier : les 10 occurrences sont exclusivement dans
les jeux de couleurs. Aucune autre clé du fichier ne porte ces deux teintes.

| Chemin | Avant | Après | Texte associé (non touché) |
| --- | --- | --- | --- |
| `scheme-1/primary_button_background` | `#1E3A2F` | **`#0B0B0C`** | `primary_button_text` = `#FAFAF7` |
| `scheme-1/primary_button_border` | `#1E3A2F` | **`#0B0B0C`** | — |
| `scheme-1/secondary_badge_background` | `#1E3A2F` | **`#0B0B0C`** | `secondary_badge_text` = `#FAFAF7` |
| `scheme-1/secondary_badge_border` | `#1E3A2F` | **`#0B0B0C`** | — |
| `scheme-2/primary_button_background` | `#1E3A2F` | **`#0B0B0C`** | `primary_button_text` = `#FAFAF7` |
| `scheme-2/primary_button_border` | `#1E3A2F` | **`#0B0B0C`** | — |
| `scheme-2/secondary_badge_background` | `#1E3A2F` | **`#0B0B0C`** | `secondary_badge_text` = `#FAFAF7` |
| `scheme-2/secondary_badge_border` | `#1E3A2F` | **`#0B0B0C`** | — |
| `scheme-3/secondary_badge_background` | `#A98E5F` | **`#FAFAF7`** | `secondary_badge_text` = `#0B0B0C` |
| `scheme-3/secondary_badge_border` | `#A98E5F` | **`#FAFAF7`** | — |

⚠️ **Le bouton primaire du schéma 3 n'a pas été touché** : il vaut `#FAFAF7` sur fond `#0B0B0C`,
c'est-à-dire craie sur encre. C'est exactement le piège d'une purge globale, qui l'aurait rendu
encre sur encre donc invisible. **Aucun jeu n'a été aplati sur un autre** : chaque clé a reçu la
valeur qui préserve son rôle dans son jeu.

Contrôle structurel : JSON parsable, **aucun chemin de clé perdu ni ajouté**, exactement
**10 valeurs modifiées**, rien d'autre. Taille inchangée (les deux hex ont la même longueur).
Les trois `stars_icons_color: #05b67a` sont **intacts** — vérifié par comptage avant/après.

## S2. Surcharges retirées

Le bloc **12.1** de `noirmont-custom.css` — **9 surcharges `!important`** de variables
(`--color-primary-button-background/-border/-text` et
`--color-secondary-badge-background/-border/-text` sur les schémas 1 et 2, plus 3 sur le
schéma 3) — est **supprimé**. Vérifié : **0 occurrence de `--color-primary-button` ou
`--color-secondary-badge`** dans la feuille. Le commentaire du bloc reste en place et documente
la correction à la source.

Les surcharges de 12.2 et 12.3 sont **conservées, et ce n'est pas un oubli** : leurs sources sont
le `{% stylesheet %}` de `blocks/noirmont-livraison.liquid` (via `styles.css`),
`blocks/noirmont-confiance.liquid`, `blocks/noirmont-4x.liquid`,
`assets/noirmont-megamenu.css`, `assets/noirmont-collection.css` et un `<style>` en ligne du
tiroir panier — **aucune n'est dans le périmètre de cette passe**. Elles restent à corriger à la
source le jour où ces fichiers seront ouverts : c'est la seule dette de couleur qui subsiste.

## S3. Contrôles en couleurs calculées

Balayage de **tous les nœuds** (`background-color`, `color`, les quatre bordures, `box-shadow`,
`outline-color`, `fill`) — c'est cette méthode, et non la recherche dans les sources, qui avait
fait sortir les deux occurrences absentes de tout fichier servi.

| Contrôle | 375 px | 1280 px |
| --- | --- | --- |
| Éléments peints en vert ou laiton — **fiche produit** | **0** | **0** |
| Éléments peints en vert ou laiton — **accueil** | **0** | **0** |
| Bouton d'achat (schéma clair) | encre, 335 × 50 px, **18,81:1** | encre, 540 × 50 px, **18,81:1** |
| **Bouton primaire en schéma sombre** (hero) | **craie sur encre, 18,81:1 — intact** | **craie sur encre, 18,81:1 — intact** |
| Contraste minimum du bloc de prix | **15,50:1** (accueil) / 18,81:1 (fiche) | **15,50:1** / 18,81:1 |
| Contraste minimum des boutons visibles | **15,50:1** | **15,50:1** |
| Cibles sous 44 px | **0** | **0** |
| Débordement horizontal | **0** | **0** |
| Bandeau d'en-tête | **65,5 px** | **65,5 px** |
| Étoiles d'avis | **`rgb(5, 182, 122)`** — vert Trustpilot intact | **idem** |

Thème `204248088914` seul écrit, `role: UNPUBLISHED` vérifié après écriture,
`processingFailed: false`. `204246548818` (« Helio ») jamais visé. Aucun produit ni prix touché,
sliders et avis de démonstration intacts, aucune publication.
