# Humanisation du texte client — thème Full Stack (25/08/2026)

Boutique `nzefxg-gg.myshopify.com`. Thème de travail **`copie-de-fullstack-2-3`**,
`gid://shopify/OnlineStoreTheme/186708001104`, non publié.
Aperçu : `?preview_theme_id=186708001104`.

Objectif : retirer les marqueurs d'écriture machine du texte affiché au client.
En tête, les tirets cadratin `—` et demi-cadratin `–`, puis la cadence qui les
accompagne (chaîne de titres qui rime, tricolons, ouvertures identiques).

## Surfaces traitées

| Surface | Fichier / ressource | Statut |
|---|---|---|
| Home | `templates/index.json` | 26 textes réécrits |
| Barre d'annonces | `sections/header-group.json` | 2 textes réécrits |
| Pied de page et bandeau de réassurance | `sections/footer-group.json` | 9 textes réécrits |
| Descriptions et SEO de collections | 14 collections Shopify (`collections-seo.json`) | 14 poussées |

Pages CMS et policies : humanisées et poussées par un agent précédent, **non
retouchées ici**.

## Comptage des tirets sur le live

Relevé sur le thème live après travaux, sur les 27 fichiers JSON de
`templates/`, `sections/`, `config/settings_data.json` et `locales/fr*` :

| Fichier | Tirets cadratin | Tirets demi-cadratin |
|---|---|---|
| `templates/index.json` (606 chaînes de settings) | 0 | 0 |
| `sections/header-group.json` (32 chaînes) | 0 | 0 |
| `sections/footer-group.json` (206 chaînes) | 0 | 0 |
| Reste du thème (product, collection, page, FAQ, panier, locales FR…) | 0 | 0 |
| 14 collections live (`descriptionHtml`, `seo.title`, `seo.description`) | 0 | 0 |

**Zéro tiret cadratin ou demi-cadratin dans le texte client.** Les `—` qui
restent dans le dépôt vivent dans des commentaires et docstrings Python, ainsi
que dans les titres d'administration des menus (`Pied de page — Menu
principal`), qui ne s'affichent pas en boutique.

Apostrophes : toutes typographiques (`’`) dans le texte affiché. Deux apostrophes
droites subsistent hors surface client, sur des libellés que le thème ne rend
pas : le nom d'un groupe dans l'éditeur (`Appel(s) à l'action`) et le bouton
`S'abonner` de `sections.header.blocks.button-header`, qui porte
`"disabled": true`.

## Extraits avant → après

### 1. Sous-titre de la sélection 199 € (celui de la capture de Hakim)

`templates/index.json` ·
`sections.collection_featured_JXRpw3…group_TwitGb.blocks.text_6LANC3`

> **Avant** — Une sélection de suspensions et de lustres autour de 199 € — le prix le plus courant du catalogue.
>
> **Après** — C'est le prix qui revient le plus souvent dans le catalogue. Vous y trouverez des suspensions comme des lustres.

Le titre au-dessus reste `Autour de 199 €`, donc le prix est toujours annoncé.
La formulation « autant de suspensions que de lustres » d'une version
intermédiaire a aussi été retirée : elle affirmait une parité de catalogue que
rien ne vérifie.

### 2. Accroche du hero

`sections.image_banner_VXNP89…blocks.text_8GW6GA`

> **Avant** — Lumière Matière — galerie de matières. Suspensions et lustres choisis pour le bambou, le rotin, le bois, la pierre ou le verre. Le matériau change la lumière : commencez par l'ambiance.
>
> **Après** — Chez Lumière Matière, on choisit les suspensions et les lustres pour ce dont ils sont faits. Bambou, rotin, bois, pierre ou verre, c'est la matière qui décide de l'ambiance. Alors commencez par là.

### 3. Titre de la grille matières

`sections.collections_matieres.blocks.title`

> **Avant** — Choisissez la matière, vous choisissez la lumière
>
> **Après** — Par matière

Le parallélisme « Choisissez… vous choisissez… » est la tournure la plus
reconnaissable de la page. Remplacé par l'intitulé qu'un vrai commerçant met
au-dessus d'une grille de rayons, en écho à `Par pièce et par forme` plus bas.

### 4. Titre des bénéfices par pièce

`sections.lm_benefices_piece.blocks.group_principal.blocks.titre`

> **Avant** — Ce que la matière change, pièce par pièce
>
> **Après** — Où voulez-vous de la lumière ?

« Pièce par pièce » disparaît. La question casse aussi la série de titres
déclaratifs et annonce directement les trois cartes (table, salon, plafond bas).

### 5. Titre de l'édito

`sections.custom_section_k9aPjP.blocks.group_XyMggk.blocks.text_34dYXd`

> **Avant** — La matière fait la lumière
>
> **Après** — Ce qu'on regarde avant de mettre une pièce en ligne

### 6. Titre du CTA final

`sections.lm_cta_final.blocks.group_principal.blocks.titre`

> **Avant** — Commencez par la matière
>
> **Après** — À vous de voir

Le hero finit déjà sur « Alors commencez par là » : le même verbe revenait en
bas de page.

### 7. Horaires du SAV dans le hero

`sections.image_banner_VXNP89…blocks.icon_with_text_AdYCCm`

> **Avant** — SAV lun–ven 10h–18h
>
> **Après** — SAV en semaine, de 10h à 18h

### 8. Bloc SAV du bandeau de réassurance

`sections/footer-group.json` ·
`sections.custom_section_k6mNHc.blocks.group_x7TjnR.blocks.text_wDwwwK`

> **Avant** — contact@lumierematiere.fr · +33 7 56 82 80 94 / Contact · lun–ven 10h–18h (Paris) · réponse sous 24 h ouvrées.
>
> **Après** — Écrivez-nous à contact@lumierematiere.fr ou appelez le +33 7 56 82 80 94. Vous pouvez aussi passer par la page Contact. On répond du lundi au vendredi, de 10h à 18h (heure de Paris), sous 24 h ouvrées.

Les trois liens (`mailto:`, `tel:`, `/pages/contact`) restent cliquables.

### 9. Bloc marque du pied de page

`sections.footer.blocks.group_y4aNMX.blocks.text_hzJHEn`

> **Avant** — Lumière Matière, c'est une galerie de matières : suspensions, lustres et plafonniers choisis pour la lumière qu'ils posent dans une pièce. […] SAV lun–ven 10h–18h (heure de Paris)
>
> **Après** — Lumière Matière rassemble des suspensions, des lustres et des plafonniers choisis pour la lumière qu'ils posent dans une pièce. […] SAV ouvert du lundi au vendredi, de 10h à 18h (heure de Paris)

### 10. Barre d'annonces

`sections/header-group.json` ·
`sections.announcement_bar_r8QCCw…blocks.text_Lk3QUw`

> **Avant** — Livraison offerte en France métropolitaine — sans minimum
>
> **Après** — Livraison offerte partout en France métropolitaine, sans minimum d'achat

### 11. Cartes bénéfices : trois ouvertures qui étaient les mêmes

Les trois cartes commençaient toutes par la matière en sujet grammatical.

| Carte | Avant | Après |
|---|---|---|
| Table | Le bambou et le rotin tamisent la lumière et la posent sur le plateau. Le reste de la pièce s'adoucit et les dîners s'étirent. | Le bambou et le rotin tamisent la lumière et la posent sur le plateau. Autour, la pièce s'adoucit, et on reste plus longtemps à table. |
| Salon | Un lustre anneau ou une pièce en bois donne un centre à la pièce. La lumière porte loin sans éblouir ceux qui sont assis dans le canapé. | Là, on cherche un point de repère au milieu de la pièce. Un lustre anneau ou du bois fait l'affaire, et la lumière porte loin sans éblouir ceux qui sont dans le canapé. |
| Plafond bas | Un plafonnier ou du verre clair laisse les volumes respirer. Vous avez de la clarté partout et rien qui pende trop bas. | Pas envie de se cogner la tête. Un plafonnier ou du verre clair éclaire large, et rien ne pend au milieu du passage. |

### 12. Tricolon du guide, étape 1

`sections.lm_guide_choix…blocks.etape_matiere`

> **Avant** — C'est elle qui fait l'ambiance. Les fibres tissées donnent une lumière chaude striée d'ombres, le verre une clarté nette, la pierre un halo dense et calme.
>
> **Après** — C'est elle qui fait l'ambiance. Le bambou et le rotin donnent une lumière chaude, striée d'ombres. Le verre éclaire plus franchement, et la pierre pose un halo dense et calme.

Le verbe sous-entendu deux fois de suite (« le verre une clarté nette, la pierre
un halo ») est un tic de rédaction machine. Trois phrases de longueurs
différentes le remplacent.

À l'étape 2, « Les dimensions exactes sont sur chaque fiche » a également été
retiré : « chaque fiche » revenait trois fois dans la seule section guide.

Le journal complet des 37 réécritures est dans
`backups/2026-08-25-humanisation/journal-2026-08-25.json`, avec les états avant
et après des trois fichiers.

## Chaîne de titres de la home, avant et après

Cinq des neuf titres tournaient autour du couple « matière / lumière ». C'était
l'anaphore la plus visible de la page.

| # | Avant | Après |
|---|---|---|
| 1 | Chaque matière a sa lumière | Chaque matière a sa lumière *(inchangé, ligne de marque)* |
| 2 | Choisissez la matière, vous choisissez la lumière | Par matière |
| 3 | Ce que la matière change, pièce par pièce | Où voulez-vous de la lumière ? |
| 4 | Autour de 199 € | Autour de 199 € |
| 5 | Bien choisir en trois étapes | Bien choisir en trois étapes |
| 6 | Par pièce et par forme | Par pièce et par forme |
| 7 | La matière fait la lumière | Ce qu'on regarde avant de mettre une pièce en ligne |
| 8 | Commencez par la matière | À vous de voir |
| 9 | Un e-mail de temps en temps | Un e-mail de temps en temps |

## Collections : descriptions et SEO

`collections-seo.json`, 14 collections, poussées via
`apply_collections_seo.update_collections()`. `main()` n'a pas été lancé, donc
`templates/collection.json` (déjà branché sur
`{{ closest.collection.description }}`) n'a pas été retouché.

Le problème n'était plus les tirets, déjà absents, mais l'ouverture : les
**14 descriptions sur 14** commençaient par la même structure, « [article] +
mot-clé en gras + verbe + deux-points + explication ». Les deux-points en
première phrase sont passés de 14 sur 14 à 2 sur 14, et chaque page attaque
autrement.

| Collection | Nouvelle première phrase | Forme |
|---|---|---|
| `suspensions-bambou` | Les fibres tissées ne laissent pas passer la lumière, elles la retiennent. | comportement de la matière |
| `suspensions-rotin` | Comparé au bambou, le rotin tire vers le miel et sa courbe est plus souple. | comparaison |
| `suspensions-bois` | Le bois absorbe au lieu de renvoyer. | constat court |
| `suspensions-pierre` | Voilà une lumière qui reste en place. | observation |
| `suspensions-verre` | Avec une suspension verre, la lumière passe à travers… | complément en tête |
| `lustres-effet-cristal` | Un lustre cristal moderne se juge à sa façon de fragmenter la lumière. | mot-clé en tête |
| `lustres-anneau` | Pas d'ampoule visible, pas d'éblouissement direct. | négation |
| `lustres-salon` | Le lustre salon est le point haut de la pièce à vivre. | mot-clé en tête |
| `plafonniers` | Un plafonnier se plaque au plafond, sans câble ni descente… | mot-clé en tête |
| `suspensions-metal` | Regardez une suspension métal allumée au-dessus d'un plan de travail… | impératif |
| `suspensions-deco` | Une suspension déco se choisit d'abord pour sa forme. | mot-clé en tête |
| `lustres-statement` | Il y a des pièces qui demandent un geste. | tournure existentielle |
| `suspensions-modernes` | Une géométrie lisible, une source qui ne se voit pas, rien de superflu autour. | fragment |
| `selection-199` | Les suspensions et lustres autour de 199 € réunis ici traversent tout l'univers de la maison… | mot-clé en tête |

Les formules de clôture, huit fois « X, Y et Z sont indiqués sur chaque fiche »,
ont été variées : impératif (« jetez un œil au diamètre »), sujet inversé (« La
fiche donne le diamètre… »), ou constat (« changent d'un modèle à l'autre »).

Mots-clés France conservés à l'identique dans le champ `keyword` et en gras dans
la première phrase : `suspension bambou`, `suspension rotin`, `suspension bois`,
`suspension pierre`, `suspension verre`, `lustre cristal` (annoncé en « effet
cristal », verre travaillé), `lustre anneau`, `lustre salon`, `plafonnier`,
`suspension métal`, `suspension déco`, `lustre statement`, `suspension design`,
`suspensions et lustres autour de 199 €`.

`seo_title` inchangés (49 à 58 caractères). `seo_description` entre 138 et 149
caractères, sous la coupe de Google. Le H2 interne `Plafonnier ou suspension ?`
de la page plafonniers est conservé.

## Chiffres d'exploitation : intacts

Le script vérifie la présence de ces repères après chaque réécriture et refuse
d'écrire s'ils disparaissent.

| Repère | Où il s'affiche | Vérifié |
|---|---|---|
| Préparation 1 à 2 jours ouvrés | bandeau réassurance | oui |
| Acheminement 6 à 15 jours ouvrés | bandeau réassurance | oui |
| Livraison offerte France métropolitaine, sans minimum | barre d'annonces, bandeau, CTA final | oui |
| Retours 30 jours (14 jours légaux étendus à 30) | barre d'annonces, bandeau, CTA final | oui |
| SAV du lundi au vendredi, 10h à 18h heure de Paris | hero, édito, bandeau, pied de page | oui |
| Réponse sous 24 heures ouvrées | bandeau réassurance | oui |
| contact@lumierematiere.fr | bandeau, pied de page (`mailto:`) | oui |
| +33 7 56 82 80 94 | bandeau, pied de page (`tel:+33756828094`) | oui |
| 47 rue Vivienne, 75002 Paris | pied de page | oui |
| Prix repère 199 € | titre et bouton de la sélection | oui |

Le cut-off de 16h (Paris) et le total de 7 à 17 jours ouvrés vivent dans les
pages et les policies, hors périmètre de ce passage. Rien dans le thème ne les
contredit.

Aucune mention de Google Pay, y compris en négatif. Aucun mot interdit
(« premium », « atelier », « artisanal », AliExpress, Trustpilot, avis inventés)
sur les surfaces client. OH Ventures reste dans les policies uniquement, absent
du pied de page et de la home.

## Pied de page : structure conservée

`patch_footer.verify()` repasse au vert sur le live :

```
{"mailto": true, "tel": true, "contact": true, "menu_principal": true,
 "menu_infos": true, "4_cols": true, "social_off": true,
 "sav_mailto": true, "sav_tel": true}
```

Quatre colonnes façon Montre Avenue, `mailto:` / `tel:` / Contact cliquables,
icônes sociales désactivées, aucune trace de ParcelPanel dans le pied. Les menus
branchés restent `footer-principal` et `footer-informations` ; les menus Helio
`footer` et `main-menu` n'ont pas été modifiés.

## Thèmes non touchés

Relevé `updatedAt` des thèmes de la boutique après travaux :

| Thème | ID | Rôle | Dernière écriture |
|---|---|---|---|
| `copie-de-fullstack-2-3` | 186708001104 | UNPUBLISHED | 25/08/2026 *(cible)* |
| Helio | 186709180752 | **MAIN** | 24/08/2026 |
| Lumière Matière — UNIVERS | 186708066640 | UNPUBLISHED | 24/08/2026 |
| Horizon | 186707771728 | UNPUBLISHED | 24/08/2026 |

**Helio MAIN et le thème UNIVERS n'ont reçu aucune écriture.** Tous les appels
`themeFilesUpsert` de la session passent par `apply_fullstack.THEME_ID`, qui
vaut `gid://shopify/OnlineStoreTheme/186708001104`.

## Fichiers modifiés

| Fichier | Nature |
|---|---|
| `shopify/humanise_theme.py` | seconde passe de réécriture, chaque entrée accepte plusieurs textes de départ, garde-fou `CADENCE_INTERDITE`, journal cumulatif |
| `shopify/collections-seo.json` | 14 descriptions et métadonnées réécrites |
| `shopify/apply_fullstack.py` | littéraux client alignés (titre grille matières, sous-titre, sous-titre 199 €, titre édito) |
| `shopify/patch_home.py` | littéraux client alignés (titres bénéfices et CTA, trois cartes, étapes 1 et 2 du guide, sous-titre grille) |
| `shopify/patch_footer.py` | déjà aligné, aucune modification nécessaire |
| `shopify/backups/2026-08-25-humanisation/` | états avant et après des trois fichiers, journal des 37 réécritures |
| `shopify/HUMANISATION-THEME-2026-08-25.md` | ce rapport |

`apply_fullstack.py`, `patch_home.py` et `patch_footer.py` portent maintenant
exactement le texte du live : une relance partielle ne peut plus ramener les
tirets ni les tournures retirées.

## Idempotence

`python3 humanise_theme.py` peut se relancer : il annonce
`0 textes réécrits`, contrôle les repères d'exploitation, refuse d'écrire s'il
trouve un tiret ou une tournure de la liste `CADENCE_INTERDITE`
(« galerie de matières », « pièce par pièce », « vous choisissez la lumière »,
« La matière fait la lumière », « six façons »).

Deux corrections de robustesse ont été apportées : l'état « avant » n'est plus
capturé qu'une seule fois, et le journal s'ajoute au lieu de s'écraser. Une
relance sans changement effaçait auparavant l'historique. Les sauvegardes et le
journal de la première passe, perdus de cette façon, ont été reconstruits depuis
la table `EDITS` : les fichiers `*.avant-2026-08-25` contiennent bien les tirets
d'origine (2 cadratins et 4 demi-cadratins pour la home, 1 pour l'en-tête, 4
pour le pied de page), les `*.apres-2026-08-25` en sont exempts.

## Scripts à ne pas relancer en entier

- `apply_fullstack.py` (`main()`) réécrit logos, fichiers et réglages.
- `patch_home.py` (`main()`) reconstruit les sections `lm_*` et purge l'ordre.
- `apply_theme.py` porte encore l'ancienne copie Helio, tirets compris
  (« Lumière Matière — galerie de matières »). Il lit son `THEME_ID` dans
  `state.json`, qui pointe aujourd'hui sur le thème Full Stack, mais il cible
  des identifiants de sections Helio (`hero_jVaWmY`, `product_list_fa6P9H`) qui
  n'existent pas dans ce thème : il échouerait sur un `KeyError` avant d'écrire.
  Laissé tel quel, hors périmètre. À supprimer ou à réaligner si la boutique
  reprend un jour ce chemin.
