# Méga-menu illustré — Maison Noirmont

> **26/07/2026** — thème **brouillon `204248088914`** (« Maison Noirmont ») uniquement.
> Le thème publié (`204246548818`, « Helio ») n'a pas été touché.
> Modèle : `montre-avenue.com`, même thème FullStack 2.2 — on reprend la **structure**, pas la direction artistique.

---

## 1. Le mécanisme retenu, et pourquoi

### Ce que fait montre-avenue, relevé en direct

Leur entrée « Toutes nos montres » est un `<dropdown-component class="header__menu-item--megamenu">` dont le contenu est un
`<div class="custom-megamenu-content custom-megamenu-content--flex">` contenant **un seul bloc natif du thème** :
`block-collections-featured`, réglé à `--grid-columns: 5` / `--grid-columns-mobile: 2`.

Chaque vignette est un `<a class="collection-card">` = un `image-block` (`--ratio: 1`) + un `text-block` portant le titre de la collection.

**Aucun développement, aucune application tierce.** C'est de la configuration de thème pure.

### La chaîne de configuration exacte

```
sections/header-group.json
└── section "header"
    └── block statique  _header-advanced-megamenus   (id figé : header-advanced-megamenus)
        ├── _header-megamenu   « Montres »
        │   ├── collections-featured        (grille 5 colonnes)
        │   │   └── _collection-card  (statique, id figé : collection-card)
        │   │       ├── image   → image = "{{ closest.collection.image }}"
        │   │       └── text    → text  = "<p>{{ closest.collection.title }}</p>"
        │   └── text  → lien « Toutes les montres »
        └── _header-megamenu   « Accessoires »   (même structure, 4 colonnes)
```

### Les deux pièges structurels du thème, découverts en lisant le Liquid

**a) Un méga-menu custom ne se branche PAS sur une entrée du menu.**
Il n'existe aucun réglage `menu_item` / `parent_link` / `link`. Dans `snippets/header-menu-desktop.liquid`, les deux flux sont
disjoints et simplement concaténés :

```liquid
{{ advanced_megamenus }}          <!-- les méga-menus custom, en bloc -->
{% for link in menu.links %} … {% endfor %}   <!-- les liens du link_list -->
```

Un `_header-megamenu` porte son propre libellé (`title`) rendu dans un `<button>` : il **s'ajoute** au menu, il ne remplace rien.
→ Pour éviter un doublon « Montres », il faut retirer l'entrée du link_list.

**b) Or les menus Shopify sont partagés entre tous les thèmes.**
Modifier `main-menu` aurait cassé le menu du **thème publié**. Interdit par le brief.
→ **Deux menus dédiés ont donc été créés**, et seul le thème brouillon pointe dessus. `main-menu` est intact.

**c) Le tiroir mobile ne rend pas les méga-menus.**
`blocks/_header-drawer-menu.liquid` ne connaît que `menu_links` et n'a aucune référence aux méga-menus ; en plus,
`.header__layout-desktop` est en `display: none` sous 1000 px. Deux mécanismes distincts.
→ Traitement mobile séparé, voir §4.

---

## 2. Collections — effectifs recomptés le 26/07

⚠️ Recompte fait **après** le passage en brouillon des 7 fiches mères. `productsCount` de l'API compte les brouillons :
tous les effectifs ci-dessous sont des comptes **ACTIF** (ce que voit réellement un client).

### Familles de montres — existantes, aucune création

| Collection | Handle | Actifs | Total (dont brouillons) |
|---|---|---:|---:|
| Classiques | `classiques` | **15** | 15 |
| Sport chic | `sport-chic` | **14** | 15 |
| Chronos | `chronos` | **12** | 13 |
| Plongeuses | `plongeuses` | **6** | 7 |
| GMT | `gmt` | **6** | 7 |
| Les Montres (repli) | `montres` | **53** | 57 |

Aucune entrée ne mène à une collection vide. Total des 5 familles = 53 = l'effectif de « Les Montres ». Cohérent.

### Accessoires — 4 collections automatiques créées

Étiquettes **réelles** relevées sur les 26 accessoires actifs (aucune inventée) : `remontoirs`, `ecrins`, `bracelets`,
`outils`, `carte-cadeau`. Règle de chaque collection : *étiquette est égale à …*, tri « meilleures ventes ».

| Collection créée | ID | Handle | Étiquette | Actifs au 26/07 |
|---|---|---|---|---:|
| Remontoirs | `690750587218` | `remontoirs` | `remontoirs` | **11** |
| Écrins et rouleaux | `690750619986` | `ecrins-et-rouleaux` | `ecrins` | **9** |
| Bracelets | `690750652754` | `bracelets` | `bracelets` | **10** |
| Outils d'horloger | `690750685522` | `outils-d-horloger` | `outils` | **8** |

38 des 39 accessoires actifs sont couverts. Le 39e est la **carte cadeau** : produit unique, donc **aucune collection créée
pour elle** (la consigne « pas de collection à un seul produit » s'applique) — elle reste dans « Accessoires ».

Les 4 collections sont **publiées** sur *Boutique en ligne* et *Shop* (sans quoi elles seraient invisibles côté client —
piège déjà payé sur cette boutique avec les produits DSers).

Images : une photo produit représentative de chaque famille, reprise du catalogue existant, donc cohérente de fait avec
les visuels en place. Aucune image de collection existante n'a été modifiée.

### Le piège des étiquettes divergentes — anticipé, puis survenu

À la création, ces collections comptaient 11 / 6 / 4 / 4. Le document notait alors le risque suivant : les accessoires
encore en brouillon portaient des étiquettes **d'un autre jeu, au singulier** (`bracelet`, `outillage`, `rangement`,
`coffret`, `entretien`), et n'entreraient donc dans aucune collection s'ils passaient en actif.

C'est exactement ce qui s'est produit : les **13 fiches publiées le 26/07** ne sont entrées dans **aucune** des quatre
collections — les effectifs étaient restés figés à 11 / 6 / 4 / 4. Un méga-menu qui sous-compte, et 13 fiches
introuvables à la navigation.

Corrigé par **ajout d'étiquette uniquement** (`tagsAdd`, aucun autre champ produit touché, anciennes étiquettes
conservées) :

| Étiquette ajoutée | Fiches | Effet |
|---|---:|---|
| `outils` | 4 | Loupe d'horloger, Doigtiers, Outil de mise à taille, Kit d'entretien |
| `bracelets` | 6 | cuir daim, milanais, caoutchouc gaufré, Jubilé 904L, acier massif, Jubilé embouts courbes |
| `ecrins` | 3 | Coffret 6 montres, Étui de voyage rigide, Coussins de présentation |

Contrôle de bouclage : 11 + 9 + 10 + 8 = 38, plus la carte cadeau = 39 — soit exactement les 42 fiches de la collection
« Accessoires » moins les 3 encore en brouillon. Rien ne manque.

> ⚠️ **L'appartenance aux collections automatiques se recalcule en différé.** Juste après le `tagsAdd`, les quatre
> collections renvoyaient encore les anciens effectifs. Ne jamais conclure sur une lecture immédiate : re-sonder.
>
> ⚠️ **Les 3 fiches encore en brouillon** portent toujours les étiquettes de l'ancien jeu. Même piège au prochain
> passage en actif : `Rouleau de Voyage — cuir` (`ecrins`, OK), `Remontoir Collection` et `Remontoir Bois`
> (`remontoirs`, OK) — ces trois-là sont en fait déjà correctes. Le risque porte sur toute **nouvelle** fiche créée
> par un autre agent avec le vocabulaire au singulier.

---

## 3. Ce qui a été écrit — fichiers et menus

### Menus créés (niveau boutique, `main-menu` intact)

| Menu | Handle | Contenu |
|---|---|---|
| Noirmont — desktop (brouillon) | `noirmont-desktop` | Configurateur · La Maison · FAQ · Contact — *Montres et Accessoires sont les deux méga-menus* |
| Noirmont — mobile (brouillon) | `noirmont-mobile` | Arborescence complète : Montres > 5 familles + Toutes les montres · Accessoires > 4 familles + Tous les accessoires · Configurateur · La Maison · FAQ · Contact |

### Fichiers du thème brouillon

| Fichier | Avant | Après | Ce qui change |
|---|---:|---:|---|
| `sections/header-group.json` | 4 030 o | 20 932 o | Les 2 méga-menus, la grille du tiroir mobile, `menu`/`menu_mobile`, `uppercase_menu_items` → `false` |
| `assets/noirmont-megamenu.css` | — | 5 305 o | **Nouveau.** Toute la mise en forme du méga-menu |
| `layout/theme.liquid` | 1 309 o | 1 451 o | Une ligne : chargement de `noirmont-megamenu.css` après `noirmont-custom.css` |

Sauvegardes des trois fichiers dans leur état d'origine :
`scratchpad/backup-theme-megamenu/` (`header-group.json`, `noirmont-custom.css`, `theme.liquid`).

Chaque écriture a été **reconfirmée** par une relecture de `size` + `updatedAt` — `themeFilesUpsert` peut renvoyer une liste
vide sans erreur. Ici la liste était pleine **et** les tailles ont bougé.

> Écart assumé par rapport au brief : le CSS est dans un fichier **séparé** plutôt qu'ajouté à `noirmont-custom.css`.
> Motif : ne pas réécrire 6 Ko de CSS existant pour en ajouter 5 (chaque réécriture intégrale est une occasion de perdre
> du contenu). Le principe de la consigne est respecté — **rien** n'est passé par le champ CSS d'une section, qui est le
> mécanisme qui fait rejeter en silence.

### Casse

`uppercase_menu_items` passe à `false`, et les légendes portent `text-transform: none !important`
(le réglage global de casse des titres remonte partout où il n'est pas neutralisé). Légendes = le titre de la collection,
court et en casse normale : *Classiques, Sport chic, Chronos, Plongeuses, GMT* — *Remontoirs, Écrins et rouleaux,
Bracelets, Outils d'horloger*.

### Charte

Panneau en craie `#FAFAF7`, filet et fond de vignette en pierre `#E7E4DE`, légendes en encre `#0B0B0C` virant au vert jura
`#1E3A2F` au survol, lien de repli souligné laiton `#A98E5F`. Angles de vignette à 10 px — la même valeur que les cartes
produit, pour que le menu ait l'air d'appartenir à la même maison que la grille. Aucun emprunt à leur DA.

---

## 4. Le mobile

Le tiroir mobile ne pouvant pas rendre un méga-menu, il reçoit **deux choses** :

1. l'arborescence complète en accordéons, via le menu `noirmont-mobile` — c'est le chemin de navigation fiable ;
2. sous les liens, une **grille illustrée à 2 colonnes des 9 familles** (5 montres + 4 accessoires), posée dans le bloc
   `_header-drawer-menu-under-menu` — qui accepte les blocs `@theme`, donc `collections-featured`.

Réglée en `show_on_display: mobile_only`, `grid_columns_mobile: "2"` (le tiroir fait 90 vw, plafonné à 400 px : à
3 colonnes les légendes cassent). Garde-fous `max-width: 100%` sur tout le contenu du tiroir.

---

## 5. Contrôle visuel — **validé par Hakim**

Le storefront brouillon est derrière le mot de passe de boutique, et je ne saisis pas de mot de passe dans un formulaire
d'authentification — c'est une limite que je ne lève pas, même quand le mot de passe m'est fourni. J'ai vérifié qu'aucun
contournement n'existe côté API : `OnlineStoreTheme` n'expose pas de lien de prévisualisation partageable.

**Hakim a donc fait la validation visuelle lui-même, desktop et mobile — rendu approuvé.** Aucune capture n'est produite
de mon côté ; les vérifications ci-dessous ont été faites au niveau de la donnée et du fichier :

- effectifs par collection recomptés en statut ACTIF (§2) — aucune vignette ne mène à du vide ;
- écritures reconfirmées par relecture de `size` + `updatedAt` sur chaque fichier ;
- thème publié `Helio` inchangé (fichiers toujours datés du 24/07, antérieurs à l'intervention) ;
- `main-menu` intact, structure vérifiée après coup.

---

## 6. Refonte des pages collection — **faite**

Voir le document dédié : **`2026-07-31-pages-collection-refonte.md`**.

La reconnaissance qui a servi de base :

- **Il n'existe pas de `sections/collection.liquid`.** L'en-tête est une `custom-section` renommée « Bannière de
  collection », id **`custom_section_NyAmKB`**, placée avant `main` dans `templates/collection.json`. Elle contient deux
  `group` frères : `group_Y8NX6K` (deux blocs `text` : le `<h1>` puis la description, bloc `text_GMnLLj`) et
  `group_CgjeTw` (un bloc `image` dont le réglage `image` vaut `{{ closest.collection.image }}`).
  → Pour retirer l'image de l'en-tête, on agit sur **ce bloc** — surtout pas sur les images de collection dans l'admin,
  dont le méga-menu se sert désormais.
- **« Voir plus »** : natif, mais c'est un réglage du **bloc `text`** qui porte la description. Deux mécanismes
  mutuellement exclusifs : `show_read_more` (+ `read_more_length`, qui est une **hauteur en px**, pas un nombre de
  caractères) et `truncate` (+ `truncate_length`, un nombre de **lignes**). Aujourd'hui les deux sont à `false`.
  Les libellés FR « Voir plus / Voir moins » sont déjà en place.
- **Filtres** : bloc `filters-and-sort`, appelé en statique avec l'id `filters`. Le réglage est **`display_mode`**, avec
  trois valeurs : `inline` (état actuel), `sidebar` (défaut du thème, cible), `menu`. En `inline`, `wrap_in_card` et
  `sticky` sont inertes. Passer en `sidebar` comprime la grille à 75 % via `grid-template-columns: 25% / 75%` →
  **garder `grid_columns` à 3 maximum**, il y est déjà.
- **Piège** : les ids de `blocks/group.liquid` sont suffixés `_desktop` / `_mobile` (`width_desktop`,
  `layout_grid_columns_desktop`…) alors que `_header-megamenu-group` utilise les ids courts (`width`,
  `layout_grid_columns`). Une configuration recopiée de l'un vers l'autre est **ignorée en silence**.

---

## 7. Limites constatées

1. **Je n'ai pas vu le rendu moi-même** (§5) : la validation visuelle est celle de Hakim. Tout ce qui précède est
   vérifié au niveau de la donnée et du fichier.
2. **Deux menus de plus dans l'admin.** `noirmont-desktop` et `noirmont-mobile` ne servent qu'au thème brouillon. À la
   publication, soit on bascule `main-menu` sur la même structure, soit on assume les trois menus. À trancher avec Hakim.
3. **Deux vocabulaires d'étiquettes coexistent sur les accessoires** (§2) : le jeu pluriel qui pilote les collections
   (`remontoirs`, `ecrins`, `bracelets`, `outils`) et un jeu singulier/descriptif (`bracelet`, `outillage`, `rangement`,
   `coffret`, `entretien`, `acier`, `cuir`…). Les deux sont désormais portés par les mêmes fiches. **Toute nouvelle fiche
   accessoire doit porter une étiquette du jeu pluriel**, sinon elle est invisible à la navigation. C'est le piège qui a
   déjà coûté un aller-retour.
4. **Desktop et mobile sont deux configurations séparées.** Ajouter une famille demande de la déclarer à trois endroits :
   la grille desktop, le menu `noirmont-mobile`, la grille du tiroir. Sans dispositif de rappel, elles divergeront.
5. **Le méga-menu s'ouvre au survol/clic sur un `<button>`**, pas sur un lien : « Montres » n'est plus cliquable
   directement vers `/collections/montres` en desktop. C'est le comportement de montre-avenue aussi ; le lien de repli
   « Toutes les montres » est là pour ça.
