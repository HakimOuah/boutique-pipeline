# Configurateur « Votre Noirmont en trois étapes » — implémentation

> **27/07/2026.** Écrit sur le thème **`204248088914` « Maison Noirmont » — `UNPUBLISHED`**, rôle
> revérifié avant et après chaque écriture. **`204246548818` (« Helio ») est MAIN et n'a reçu aucune
> requête d'écriture** ; `204329288018` (fork obsolète) non plus — contrôle final par
> `files(filenames:…)` sur les deux : **0 nœud**. **Aucun thème publié.** Aucun produit, variante,
> prix, média ni métachamp touché : **le mapping DSers est intact**, aucune mutation produit n'a été
> appelée. Sauvegarde de l'état d'avant : `scratchpad/backup-configurateur/ETAT-AVANT.json`.
> Charges utiles : `scratchpad/work-configurateur/`.

---

## 1. Fichiers créés — empreintes relues sur le thème

Les quatre fichiers sont **nouveaux** : aucun fichier existant n'a été modifié, donc aucune
sauvegarde de contenu antérieur n'était nécessaire. `themeFilesUpsert` peut renvoyer
`upsertedThemeFiles: []` sans `userErrors` — c'est une écriture **asynchrone**, pas un échec ; les
empreintes ci-dessous sont celles **relues** sur le thème et comparées aux **octets envoyés**.

| Fichier | octets | `checksumMd5` relu | = md5 local |
| --- | ---: | --- | :-: |
| `sections/noirmont-configurateur.liquid` | **24 083** | `fd0b745c16f6396dd571ce6efb2eaf1a` | ✅ |
| `assets/noirmont-configurateur.css` | **17 049** | `53731fdeca4a117c3a1c4f953592eb61` | ✅ |
| `assets/noirmont-configurateur.js` | **19 797** | `237b541e23b9870e34e102192aabbd35` | ✅ |
| `templates/page.configurateur.json` | **833** | `3316c92efc5f3f18ae0d2d64e0379f2c` | ✅ |

⚠️ **La feuille de style est un fichier `assets/`, pas le champ CSS d'un schéma de section** — ce
dernier est rejeté en silence. Le nom du schéma, `Configurateur Noirmont`, fait **22 caractères**
(la limite silencieuse est à 25). Aucun bloc de schéma n'est déclaré, donc aucun nom de bloc à
dépasser.

### Rattachement de la navigation

L'entrée **CONFIGURATEUR** existait déjà, dans quatre menus, et pointait sur `/pages/configurateur`
(`Page/176162537810`). Seul changement de donnée boutique de toute la mission :
**`templateSuffix: null → "configurateur"`**. Vérifié ensuite :

- `/pages/configurateur` **sans aucun paramètre** rend le configurateur (`data-nm-cfg` présent,
  `<h1>` = « Votre Noirmont en trois étapes ») sur le thème brouillon ;
- le même chemin rendu par **Helio (MAIN)** revient **intact et sans notre section** (189 ko de
  page normale) : Shopify retombe sur le gabarit `page` par défaut quand le suffixe n'existe pas
  dans le thème. La boutique est par ailleurs **protégée par mot de passe**, donc hors ligne.
- Réversible en une mutation : remettre `templateSuffix` à `null`.

---

## 2. Le parcours implémenté

**Trois écrans, deux questions, aucune troisième question.** La grille à quatre questions
(1 362 cases mortes, 36 % du catalogue inatteignable) n'a pas été approchée.

| Écran | Contenu | Source de données |
| --- | --- | --- |
| **1 — la famille** | 5 options illustrées : Classiques, Sport chic, Chronos, Plongeuses, GMT | les 5 collections, `custom.famille` renseigné 100 % |
| **2 — la couleur de cadran** | 1 échappatoire + **14 couleurs**, les présentes d'abord, les absentes ensuite et grisées | `custom.couleur_cadran` |
| **3 — la révélation** | « Voici votre `<Nom>` », la montre en grand, ses specs, le prix, l'achat | fiche produit réelle |

**Les cinq familles passent par la Q2** : tous les chemins ont exactement le même nombre d'écrans.

**L'échappatoire « Peu importe »** ouvre chaque écran 2 (illustrée par une vraie photo de la
famille, jamais du texte seul). Elle existe pour une raison mesurée : sans elle, une montre
dépourvue de `couleur_cadran` serait inatteignable. C'est **une option dans la Q2, pas une
troisième question**.

**Aucune valeur inventée.** Une puce de spécification n'apparaît que si le métachamp existe
(`Diamètre`, `Calibre`, `Cadran`). **L'étanchéité n'a aucun métachamp : rien n'est affiché à ce
sujet.** Les mots `unique`, `composez`, `configurez`, `sur mesure`, `assemblée pour vous` sont
**absents du rendu — vérifié par balayage du texte de la section : 0 occurrence**.

### Résultat des chemins — mesuré sur le rendu

| Indicateur | Mesure |
| --- | ---: |
| **Chemins ouverts** | **34** |
| **Chemins morts** | **0** |
| Chemins par famille | Classiques 9 · Sport chic 7 · Chronos 11 · Plongeuses 3 · GMT 4 |
| Grille de la Q2 | **75 cases** (5 familles × 15 options) |
| Cases **grisées** en Q2 | **41** — affichées, libellées, jamais retirées du DOM |
| **Montres atteignables** | **50 / 50** |
| **Montres cachées** | **0** |
| Écrans finaux sans fiche / sans prix / sans bouton | **0 / 0 / 0** |
| Chemins menant à un **ajout au panier direct** | **16** (variante unique et disponible) |
| Les autres | lien vers la **vraie fiche produit** |
| Résultats par écran | min 1 · max 15 · moyenne **3,00** · 17 écrans à une seule montre |

Un **parcours piloté écran par écran** (clic réel sur chaque option, 34 chemins) avait donné le
même verdict : **34 chemins, 0 mort, 50 montres atteintes**, chaque écran final portant bien un
titre « Voici votre … », un prix et un bouton.

> **⚠️ Écart avec les 26 chemins de `axes-guide-de-choix.md`, et pourquoi.** L'étude comptait 26
> chemins avec une Q2 **conditionnelle** (posée aux 3 grandes familles seulement) sur **53 montres**.
> Ici la Q2 est posée aux **5** familles — comme demandé — d'où 29 chemins de couleur, **plus 5
> échappatoires = 34**. Le catalogue **réellement servi par la vitrine est de 50 montres, pas 53** :
> voir §6, ce n'est pas de notre fait.

---

## 3. L'expérience — géométrie de substitution, pas une page de filtres

**Reprise de la géométrie de Goteia, pas de son mécanisme.** Chez eux la vignette choisie passe à
`opacity: 0` et l'aperçu composé prend sa place au pixel près. Nos vignettes **sont déjà le
résultat fini** : l'emplacement central **est** l'aperçu. Donc :

- **aucune composition par calques**, aucun `previewLayer`, aucun recalage `layerScale/offsetX` ;
- **aucun fondu croisé** — il n'a rien à croiser ;
- le mouvement de substitution est conservé : la rangée glisse en `transform`, l'emplacement qui
  arrive au centre passe de `scale(0.74)` / image à `opacity .68` à `scale(1)` / `opacity 1`.
  La montre **est visible et se met à jour à chaque choix**, dès l'écran 1.

Mesures de géométrie, prises au `getBoundingClientRect` :

| | 375 × 812 | 1280 × 800 |
| --- | ---: | ---: |
| Photo centrale | 255 px | 260 px (écran 3 : 250) |
| Pas du carrousel | 199 px | 208 px |
| Emplacement (cible tactile) | **191 × 307 px** | **200 × 312 px** |
| Écart entre deux cibles voisines | **8 px** exactement ×4 | **8 px** exactement ×4 |
| Centre de la photo vs centre de la fenêtre | 187,5 / **187,5** | 640 / **640** |
| `document.scrollWidth` | **375** | **1280** |

> Un défaut a été trouvé et corrigé ici : sans `grid-template-columns: minmax(0,1fr)`, la photo
> imposait sa largeur à l'emplacement et **débordait vers la droite seulement** (pas du carrousel
> mesuré à 368 px au lieu de 295, aperçu décalé de 32 px). Corrigé, puis remesuré.

---

## 4. Mouvement — valeurs mesurées

| Contrôle | Mesure |
| --- | --- |
| Propriétés animées, **toutes** | **`transform` et `opacity`, rien d'autre** |
| `transition: all` | **0** |
| Animation de `width` / `height` / `margin` / `top` / `left` | **0** |
| Animations **en boucle infinie** | **0** (leur « respiration » à 2,5 s n'est pas reprise) |
| Durée | **220 ms** |
| Courbe | `cubic-bezier(0.2, 0, 0, 1)` — *ease-out* |
| Report de validation après un clic | 260 ms, ramené à **0 ms** si `prefers-reduced-motion` |

**`prefers-reduced-motion` honoré.** La condition servie est exactement
`(prefers-reduced-motion: reduce)`. En appliquant de force le contenu de ce bloc sur la page
rendue, les durées relevées passent de **0,22 s → 0 s** sur la rangée, la photo, l'image et la
barre de progression, et les animations tombent à `none` : **substitution instantanée, aucun
glissement**, le parcours reste entièrement utilisable.

> **Fragilité trouvée et corrigée** — celle que je reprochais à Goteia (nº 15, état transitoire mal
> fermé). L'entrée d'écran animait `opacity: 0 → 1` avec `animation-fill-mode: both`. Dans un
> onglet bridé par le navigateur, l'animation **reste bloquée à 0 % et l'écran entier demeure
> invisible** (mesuré : `opacity: 0` sur l'écran 3, 900 ms après la transition). **La visibilité ne
> doit dépendre d'aucune animation** : l'entrée n'anime plus que `transform` (7 px de montée).
> Revérifié : `opacity` de l'écran 3 = **1**.

---

## 5. Accessibilité — mesures sur le rendu, opacité héritée comprise

### Contrastes

Calculés sur les couleurs **calculées**, en compositant l'opacité de tous les ancêtres.

| Élément | Rapport | Seuil |
| --- | ---: | --- |
| Titre, questions, compteur d'étape | **18,81:1** | ✅ |
| Libellé de l'option **sélectionnée** | **18,81:1** | ✅ |
| Prix, libellés et valeurs de spécification | **18,81:1** | ✅ |
| Bouton d'achat (craie sur encre) | **18,81:1** | ✅ |
| Bandeau **« Indisponible »** | **18,81:1** | ✅ |
| Libellé d'une option **voisine** | 7,44:1 | ✅ |
| **Libellé d'une option grisée** | **7,44:1** | ✅ **≫ 3:1** (Goteia : **1,9:1**) |
| Flèche de pagination désactivée | 7,44:1 | ✅ |

> **Défaut trouvé et corrigé.** Le bandeau « Indisponible » était **enfant** du conteneur d'image et
> héritait de son `opacity: 0.26` → **2,19:1**, soit pire que Goteia. L'opacité a été déplacée sur
> l'`<img>` seule et le bandeau sorti du conteneur : il passe à **18,81:1**. L'échelle reste portée
> par le conteneur, l'opacité par l'image — le libellé et le bandeau ne peuvent plus être fanés.

### Cibles, clavier, focus

| Contrôle | Mesure |
| --- | --- |
| Cibles **sous 44 × 44 px** | **0**, à 375 comme à 1280 (emplacements 191×307, flèches 44×44, boutons h 48, retour h 44) |
| Écart entre cibles | **8 px** |
| Débordement horizontal | **0** (`scrollWidth === innerWidth` à 375 et 1280) |
| Libellés | **toujours visibles**, jamais en survol — bornés à **2 lignes** |
| `tabindex` glissant | **1 seul arrêt de tabulation** par axe, en permanence |
| Flèches ← → | **fonctionnent** ; `Home` → premier, `End` → dernier ; **pas de bouclage**, pas de cul-de-sac |
| `Entrée` / `Espace` | valide et passe à l'écran suivant |
| **Anneau de focus** (`:focus-visible` réellement actif, frappe clavier réelle) | `outline: 2px solid #22D3EE`, `outline-offset: 2px`, halo d'encre `0 0 0 6px rgba(11,11,12,.9)` |
| Opacité de l'élément qui reçoit le focus | **1** — jamais un élément transparent (défaut nº 8 de Goteia) |
| Sémantique | `role="listbox"` / `role="option"` + `aria-selected`, `aria-setsize`, `aria-posinset` |
| Option impossible | `aria-disabled="true"` + `aria-label` explicite (« Cadran blanc — indisponible chez les Classiques »), **jamais retirée du DOM**, jamais `disabled` : elle reste atteignable au clavier |
| Annonces | `role="status" aria-live="polite"` à chaque changement d'écran |
| Sans JavaScript | bloc `<noscript>` renvoyant vers les 5 collections |

---

## 6. Prix et achat — atteignables sans défilement

Référence adverse : chez Goteia, prix à **1 086 px** et « Ajouter au panier » à **1 147 px** sous
une fenêtre de 812.

| Écran de révélation | 375 × 812 | 1280 × 800 |
| --- | ---: | ---: |
| Prix | y **631 → 661** | y **695 → 726** |
| Bouton d'achat | y **673 → 721** | y **738 → 786** |
| Lien « Voir la fiche complète » | y **721 → 765** | visible |
| **Sous la ligne de flottaison ?** | **non** | **non** |

Trois réglages ont été nécessaires pour y arriver, tous mesurés : la promesse d'accroche est
**réservée à l'écran 1**, la puce « Famille » a été retirée (redondante avec le chemin parcouru), et
le prix sous la vignette est masqué sur l'écran 3 puisqu'il est affiché en grand juste dessous.

### Pas de panier maison, pas de produit synthétique

- **Variante unique et disponible → `<form method="post" action="/cart/add">`** avec l'**identifiant
  de la vraie variante**, rendu côté serveur. 16 chemins sur 34 aboutissent à ce cas.
- **Sinon → lien vers la vraie fiche produit**, où le client choisit sa variante.
- Un lien secondaire « Voir la fiche complète » est présent dans tous les cas.
- **Aucune mutation produit, variante, prix ou média n'a été appelée : le mapping DSers n'a pas été
  approché.**

---

## 7. Images — l'anneau, pas les 3,6 Mo

| Mesure | Configurateur NOIRMONT | Goteia |
| --- | ---: | ---: |
| Emplacements dans le DOM | 130 | — |
| Images **réellement chargées** au premier rendu | **5** | 94 |
| **Requêtes d'images** du configurateur | **5** | **110** |
| **Octets d'images** | **201 ko** | **≈ 3 600 ko** |
| Images restées en `loading="lazy"` | **125 / 130** | — |

- **Anneau glissant de ±2** autour de la photo courante : la courante en `fetchpriority="high"`,
  les voisines en `low`. Budget respecté : **5 images en vol**.
- **`loading="lazy"` conservé partout ailleurs**, sur le configurateur comme sur le reste du site.
- **Préchauffage en `requestIdleCallback`** (`timeout: 3000`), borné à **±5 emplacements**,
  **annulable**, et **totalement coupé** sur `saveData`, `prefers-reduced-data: reduce` et 2G.
- **Non-scintillement garanti par `await img.decode()` avant substitution** (budget 420 ms, l'ancienne
  photo restant affichée jusque-là) — **pas** par le volume préchargé. Le pire cas dégrade en attente
  courte, jamais en trou blanc.
- Une seule taille demandée, **720 px**, calée sur l'emplacement (≤ 260 px) × DPR 2. Pas de `w=1000`
  pour un emplacement de 238 px.

---

## 8. Charte

- Encre `#0B0B0C`, craie `#FAFAF7`, pierre `#E7E4DE`, graphite `#55524C`, acier `#8A9099`.
  **Vert forêt et laiton : absents, non réintroduits.**
- **Le cyan `#22D3EE` est la couleur de l'instrument, et rien d'autre** : barre de progression,
  anneau de focus, trait de cote des puces de spécification. Il **ne porte aucune information seule**
  (1,72:1 sur craie — l'information est toujours dans le texte, à 18,81:1) et **ne touche aucun
  bouton d'achat** : le bouton d'achat est en encre pleine.
- Oswald en affichage (`--font-heading--family`), Inter en fonctionnel.
- **Chiffres tabulaires** : compteur d'étape, pagination, prix, diamètre et calibre sont en
  `ui-monospace` + `font-variant-numeric: tabular-nums` — la fonte Inter servie n'expose pas `tnum`,
  l'inflexion monospace est donc le seul moyen fiable, conformément à la convention `--mesure`.

---

## 9. Ce qui reste

1. **⚠️ Trois Plongeuses sont passées en `DRAFT` pendant la session, sans publication sur aucun
   canal** : `noirmont-un-plongeuse-acier`, `noirmont-deux-plongeuse-ceramique`,
   `noirmont-un-bronze-plongeuse`. Elles étaient **`ACTIVE` au début de la mission** et ne le sont
   plus. **Ce n'est pas de mon fait — aucune mutation produit n'a été appelée.** Conséquence : la
   vitrine sert **50 montres et non 53**, les Plongeuses tombent de 6 à 3 fiches et de 3 à 2
   couleurs, et la famille perd le cadran **Noir**. **Décision pour Hakim**, pas pour moi. Dès leur
   repassage en `ACTIVE`, **le configurateur les reprend sans aucune modification de code** : il lit
   les collections, pas une liste figée.
2. Tant que `noirmont-deux-plongeuse-ceramique` est en brouillon, l'échappatoire « Peu importe » n'a
   rien à rattraper. **Elle reste en place** : c'est la garantie qui remet les cachées à zéro dès que
   la fiche revient, et le métachamp `couleur_cadran` de cette montre est toujours vide.
3. **Le corps de la page `configurateur` n'a pas été touché** et contient encore
   « Composez votre montre pièce par pièce […] Personne d'autre ne la portera » — **contraire à la
   charte**. Il n'est **pas rendu** par le nouveau gabarit, mais il le serait par Helio. À réécrire
   quand Hakim voudra ; je ne modifie pas un texte servi par le thème MAIN sans son accord.
4. `quarante-et-un-sport-acier` se contredit toujours (options « acier » et « cuir », description
   « bracelet intégré »). Sans effet sur ce parcours, qui n'utilise pas l'axe bracelet.
5. **Aucune télémétrie posée.** Le jeu d'événements de Goteia (`configurateur_ouvert`,
   `etape_changee`, `option_choisie`, `configurateur_termine`, `ajout_panier`) reste à brancher quand
   un outil de mesure sera choisi.
6. Le partage `?famille=…&cadran=…&montre=…` fonctionne et chaque valeur est **vérifiée contre le
   catalogue** au chargement (repli sur l'écran atteignable le plus proche si une valeur a disparu).
   **Aucun bouton « Partager » n'a été ajouté** : l'URL de la barre d'adresse suffit et se copie.

### Comportement de l'URL — vérifié

Un défaut réel a été trouvé et corrigé : `showPanel` écrivait l'URL en `replaceState` **pendant** la
transition vers l'écran 3, ce qui **écrasait l'entrée d'historique de l'écran 2** et faisait sauter
la question de la couleur au retour. Après correction, la séquence relevée est symétrique :

| Action | URL | Écran |
| --- | --- | --- |
| Chargement | aucun paramètre | 1 |
| Choix de la famille | `famille` | 2 |
| Choix de la couleur | `famille` + `cadran` + `montre` | 3 |
| **Retour navigateur** | `famille` | **2** |
| **Retour navigateur** | aucun paramètre | **1** |
| **Avancer** | `famille` | 2 |
| **Avancer** | `famille` + `cadran` + `montre` | 3 |

Les boutons « ← Retour » de la page délèguent à `history.back()` : un seul comportement, pas deux.
« Recommencer » revient à l'écran 1 avec une URL propre.

---

*Contrôles menés à **375 × 812 d'abord**, puis 1280 × 800, sur le rendu réel de
`maisonnoirmont.fr/pages/configurateur` servi par le thème `204248088914`. Les mesures de largeur
375 px ont été prises dans un cadre de même origine dimensionné à 375 × 812 — les requêtes de média,
`vw` et `svh` s'y évaluent bien sur 375 × 812 —, la fenêtre Chrome de cette machine refusant de
descendre sous ~780 px. Aucun thème publié, aucun produit modifié, aucun mot de passe saisi.*

---

# Refonte du 28/07 — grammaire de pièces (retour de Hakim)

Verdict de Hakim sur la V1 : « aucune illusion de configurer quoi que ce soit » — exact, le
carrousel de produits voisins nommés était un présentoir de catalogue. Refonte complète de la
**présentation** sur la grammaire de la maquette validée (`proto-configurateur-noirmont.html`),
transposée dans la charte actuelle (encre/craie/cyan-instrument, Oswald/Inter — pas le vert
jura/laiton/Bodoni du proto). **Le moteur de la V1 est conservé intégralement.**

## Ce qui a changé

- **Le carrousel de produits est supprimé partout.** Une **seule montre en scène** (carte blanche
  bordée de pierre, note de taille « 36 MM / 39 MM » en dessous — du métachamp, sinon rien),
  photo remplacée à chaque choix après `img.decode()` (budget 420 ms, jamais de trou blanc, un
  ticket invalide les substitutions périmées).
- **Q1 = « Choisissez votre boîtier »** : 5 cartes en **recadrages macro** des photos existantes
  (lunette cannelée, boîtier intégré à vis, compteur + poussoir de chrono, lunette de plongée,
  lunette GMT — `background-size: 300%`, position par famille). Libellés Classique / Sport chic /
  Chronographe / Plongée / GMT + « dès X € ». Jamais une montre entière, jamais un nom.
- **Q2 = « Choisissez votre cadran »** : **pastilles rondes découpées dans les vraies photos**
  (zoom 300 % centré cadran), libellés toujours visibles. Les couleurs absentes restent affichées,
  grisées (découpe seule à 0,26, **libellé à 7,44:1**), `aria-disabled` + raison, focalisables.
- **Récapitulatif permanent « VOTRE COMPOSITION »** sous la scène, trait de cote cyan, texte encre/
  graphite : « **Boîtier** classique · **Cadran** vert · **Mouvement & fond** Miyota 8215 · 36 mm ».
- **Aucun nom de catalogue avant la révélation** — vérifié par balayage du texte rendu des écrans
  1-2 + récapitulatif contre les 50 noms et 50 titres complets : **0 fuite**. Le nom est la
  récompense : « Voici votre Trente-Neuf Vert ».
- **Plusieurs montres sur un chemin** → jamais côte à côte : rangée « Votre cadran, précisément »
  en pastilles-photos anonymes ; basculer change nom, scène, prix, variante. **Plusieurs
  variantes** → réglages en pièces (« VOTRE MOUVEMENT & FOND ») dont les valeurs sont les
  **options Shopify réelles**, résolues contre la table de variantes rendue côté serveur ; chaque
  combinaison aboutit à **une variante réelle** (id vérifié) ; combinaison absente → variante la
  plus proche portant la valeur cliquée, **annoncée** en `aria-live`, jamais en silence.
- **Barre d'achat collante** (prix + « Ajouter au panier ») en bas de fenêtre sur mobile — pire
  cas mesuré (8 réglages) : CTA à **761 → 809 px** dans une fenêtre de 812, contre 1 179 sans elle.
  Piège trouvé : le `.shopify-section` du thème est en `overflow-x: hidden`, ce qui en faisait le
  port de défilement du sticky ; notre enveloppe repasse en `overflow: visible`, la protection
  anti-débordement restant portée par la section (`overflow-x: clip`).

## Fichiers en ligne (empreintes relues = octets envoyés)

| Fichier | octets | md5 |
| --- | ---: | --- |
| `sections/noirmont-configurateur.liquid` | 23 534 | `eb3bbbfe3b42f2709931dac035ae0d2d` |
| `assets/noirmont-configurateur.css` | 15 642 | `0ab421edca0766f0529486742bee768a` |
| `assets/noirmont-configurateur.js` | 22 232 | `f02cfbba210c1a81b54284adf0f644ba` |
| `templates/page.configurateur.json` | 828 | `119029b17a947449e93729aab56da6d3` |

V1 sauvegardée : `scratchpad/backup-configurateur/*.v1-carrousel`. Cible unique `204248088914`
(UNPUBLISHED) ; Helio (MAIN) et le fork n'ont reçu aucune écriture ; rien publié ; aucun produit,
prix, métachamp ni mapping DSers touché.

## Contrôle final, mesuré sur le rendu (375 × 812 puis 1280)

| Contrôle | Résultat |
| --- | --- |
| Chemins ouverts / morts | **34 / 0** |
| Montres atteignables | **50/50**, 41 cases Q2 grisées jamais retirées du DOM |
| Chemins aboutissant à une **variante réelle** au panier | **34/34** (id dans le formulaire `/cart/add`) |
| Fuites de noms avant révélation | **0** (sur 100 noms/titres testés) |
| Mots interdits | **0** |
| `prefers-reduced-motion` | bloc appliqué de force → **toutes transitions à 0 s** |
| `transition: all` / mise en page animée / boucles infinies | **0 / 0 / 0** — `transform`/`opacity`, 220 ms ease-out |
| Cibles < 44 px | **0** ; débordement horizontal **0** (scrollWidth = 375) |
| Clavier | tabindex glissant, flèches, Home/End, Entrée valide ; grisées focalisables mais jamais sélectionnées ; focus cyan + halo d'encre |
| URL / historique | inchangés V1 : `famille`/`cadran`/`montre`, pushState par avancée, Retour symétrique |

Restes inchangés (§9 V1) : les 3 Plongeuses en DRAFT (50 montres servies au lieu de 53 — décision
Hakim), le corps de page « Composez votre montre… » côté Helio, la télémétrie à brancher.

---

# Révision V3 du 29/07 — trois retours de Hakim après essai sur écran

Cible unique **`204248088914` (UNPUBLISHED)**, rôle revérifié avant/après chaque écriture ;
**Helio (MAIN) contrôlé en fin de mission par `files(filenames:…)` : 0 nœud** ; rien publié ;
aucun produit, prix, métachamp ni mapping DSers touché. Sauvegarde de l'état V2 :
`scratchpad/backup-configurateur-v3/`. Fichiers locaux (source de vérité) :
`scratchpad/work-configurateur/`.

## 1. Les couleurs indisponibles sont retirées, plus grisées

Le retour : sur la GMT, 3 cadrans disponibles et **11 tuiles « absente ici »** — l'écran disait
« on n'a presque rien ». La règle « grisé, jamais retiré » était calibrée pour un indisponible
minoritaire ; le ratio s'inversait. **Désormais l'écran 2 ne rend que les couleurs que la famille
porte réellement**, plus « Peu importe » en tête. La grille Q2 passe de 80 cases (41 grisées) à
**34** (5 échappatoires + 29 couleurs). Tuiles grisées, `aria-disabled`, « absente ici » et la
ligne « Les cadrans que ce boîtier ne porte pas… » : supprimés du rendu (le code clavier garde ses
gardes `aria-disabled`, devenues sans objet sur cet écran). Grille resserrée à `minmax(76px, 1fr)`
pour que GMT (« Peu importe » + Noir + Blanc + Brun) tienne en **une seule rangée à 375 px**
(4 × 81 px, tops identiques, mesuré) — le piège du padding conteneur est neutralisé par des pistes
en `fr`.

## 2. Les prix deviennent lisibles : deltas + explication en français

- **Chaque puce de réglage porte son écart** par rapport à l'option la moins chère réellement
  disponible sur la fiche, **calculé côté client depuis les prix réels des variantes** (champ `p`
  en centimes ajouté au JSON de variantes rendu côté serveur — aucune grille en dur). Affiché
  seulement si le prix varie dans le groupe, « +0 € » compris. Mesuré sur 3 échelles différentes :
  GMT 349→417 (+0/+29/+39/+68), Classique cannelée 329→397 (+0/+29/+39/+68), Classique jubilé
  299→328 (+0/+29) — conformes aux prix Admin API relus fiche par fiche.
- **Une ligne d'explication sous chaque groupe** (`.nmc__adjnote`), composée d'un glossaire par
  valeur reconnue : NH34, NH35 (« calibre automatique japonais Seiko »), Miyota 8215 (« Citizen »),
  Mingzhu 2813 et DG3804 (« calibre éprouvé, le plus accessible »), PT5000 (« haute cadence »),
  fond verre / fond acier (texte du brief). **Chaque calibre est nommé séparément** — jamais
  « Seiko NH34 ou DG3804 ». Valeur non reconnue = pas de phrase : rien d'inventé. **Aucune image
  générée** : nous n'avons aucune photo réelle des fonds de boîtier.
- « Votre cadran, précisément » : chaque pastille porte aussi son écart (`data-prix` = prix réel de
  la variante servie) — **seulement quand les prix diffèrent** entre les montres proposées
  (GMT noir et Chronos « Peu importe » : prix identiques → aucun bruit, vérifié).

## 3. Les pastilles « votre cadran, précisément » sont libellées

Ces pastilles n'existent qu'à l'écran de révélation, où le nom est déjà dévoilé : l'interdiction de
fuite ne s'y applique plus. Chaque pastille affiche le **nom court réel** (borné à 3 lignes,
`title` + `aria-label` = titre complet). Si deux montres de la rangée partagent le même nom court
(« Voyageur Bicolore » ×2), le libellé reprend le **sous-titre réel de la fiche** qui porte la
différence : « Voyageur Bicolore · GMT bracelet 5 maillons » / « … 3 maillons » — vérifié sur le
chemin GMT signalé. Pastilles élargies à `minmax(104px, 1fr)` pour loger le texte.
**Au passage : le récapitulatif n'écrase plus la casse des familles** — « Boîtier GMT »,
« Boîtier Classique » (le `toLowerCase()` fautif est retiré).

## Défaut trouvé en route : la barre d'achat ne collait plus

Le `body` du gabarit est en `overflow-x: hidden`, donc `overflow-y` calcule à `auto` : **le body
devenait le port de défilement des éléments collants** (même piège que le `.shopify-section` de la
V2, un cran plus haut) et la barre d'achat mobile défilait avec le contenu au lieu de coller.
Correctif : `body:has(.nmc) { overflow: visible !important; }` — la protection anti-débordement
reste portée par `.nmc` (`overflow-x: clip`). Vérifié après correctif : la barre épingle à
**791 px de bas dans une fenêtre de 812** dès que la fiche défile ; à défilement 0 elle s'arrête au
bord haut de son conteneur (819 px, comportement sticky normal — la fiche commence juste sous la
ligne de flottaison, les libellés ajoutés ayant allongé l'écran 3 mobile). Page réelle recontrôlée
après l'override : défilement intact, débordement horizontal 0.

## Fichiers en ligne (empreintes relues = md5 locaux, écritures asynchrones vérifiées)

| Fichier | octets | md5 |
| --- | ---: | --- |
| `sections/noirmont-configurateur.liquid` | 23 887 | `8673b329a52ef46df305a6d8301bafb0` |
| `assets/noirmont-configurateur.css` | 17 487 | `a494d3af95caac0a4065ace65e34c969` |
| `assets/noirmont-configurateur.js` | 27 974 | `52bbc9fc354cf18cbc97abb2eb84a40c` |

(`templates/page.configurateur.json` non touché. Un premier envoi du JS différait du local de deux
octets cosmétiques — espace insécable et ligne vide ; le local a été aligné sur l'octet près,
`node --check` repassé.)

## Contrôle final — rendu réel du thème brouillon, cadres même-origine 375×812 puis 1280×800

| Contrôle | Résultat |
| --- | --- |
| Chemins ouverts / morts | **34 / 0** (5 « Peu importe » + 29 couleurs) |
| Montres atteignables | **50 / 50**, chaque panneau avec prix + CTA |
| Variante réelle au `/cart/add` | id vérifié sur les bascules (GMT ×2, Classiques, Chronos) |
| Deltas vs prix réels des variantes | conformes sur **3 fiches** (3 échelles différentes) |
| Parcours rejoués par clics réels | GMT/Noir (le cas signalé), Classiques/Vert, Chronos/Peu importe — à 375 **et** 1280 pour GMT |
| Q2 GMT à 375 | **1 rangée de 4** (tops identiques, tuiles 81×103 ≥ 44 px) |
| Débordement horizontal | **0** (scrollWidth = 375 / 1280, et 1710 sur la page réelle) |
| Fuites de nom écrans 1-2 + récap | **0** (50 noms testés) ; mots interdits : **0** |
| 1280 | grille 2 colonnes, scène collante, prix 634→665 et CTA 675→723 dans une fenêtre de 800 |
| Récapitulatif | « Boîtier GMT · Cadran noir · Mouvement & fond … » |

*Contrôles menés dans le Chrome de Hakim (session d'aperçu déjà ouverte — **aucun mot de passe
saisi**), l'aperçu du domaine `myshopify` étant retombé sur `/password`. Deux pièges de mesure
documentés pour la prochaine fois : la barre d'aperçu Shopify détourne les cadres (la retirer du
HTML récupéré avant l'écriture directe dans le cadre de mesure), et `scroll-behavior: smooth` +
un onglet en arrière-plan gèlent le défilement programmatique et les minuteries (forcer
`scroll-behavior: auto` et piloter en synchrone).*
