---
type: journal
boutique: seiko-mod
date: 2026-07-31
nature: intervention
leviers: [page]
titre: "Refonte des pages collection — Maison Noirmont"
---

# Refonte des pages collection — Maison Noirmont

> **26/07/2026** — thème **brouillon `204248088914`** uniquement. Thème publié `Helio` (`204246548818`) non touché.
> Suite de `2026-07-31-megamenu-illustre.md`. Un seul template pilote **toutes** les pages collection : `templates/collection.json`.

---

## 1. Le défaut corrigé

État constaté par Hakim sur `/collections/classiques` : une **grande image de bannière occupait la quasi-totalité de
l'écran** et repoussait la première rangée de produits **sous la ligne de flottaison**. Le visiteur arrivait sur une
photo, pas sur des montres.

Deux défauts secondaires relevés sur la même capture :

- le titre s'affichait en **capitales** — « CLASSIQUES » — alors que le titre réel de la collection est « Classiques ».
  C'était donc une transformation CSS, pas une donnée ;
- le sous-titre et la description étaient corrects : **c'est bien l'image le problème, pas le texte.** Ils sont conservés.

---

## 2. Ce qui a été fait

### a) L'image de bannière — désactivée, pas supprimée

L'en-tête n'est pas une section dédiée : c'est une `custom-section` nommée « Bannière de collection »
(id **`custom_section_NyAmKB`**) contenant deux groupes frères — `group_Y8NX6K` (titre + description) et
**`group_CgjeTw`** (l'image, `{{ closest.collection.image }}`).

Le groupe image porte désormais **`"disabled": true`**. Il reste **entièrement présent** dans le fichier, avec son bloc
`image_nmjifa` et son réglage intact : réactiver la bannière illustrée est un booléen à repasser, aucune reconstruction.

> **Pourquoi désactiver plutôt que supprimer** : les images de collection servent maintenant aux vignettes du méga-menu
> et aux pastilles de collections sœurs. Rien n'a été touché côté admin — la consigne « pas de suppression d'image de
> collection » est respectée à la lettre. Seul l'**affichage** dans la bannière est coupé.

La bannière devient un bandeau de titre : `padding_top`/`padding_bottom` 25 → **18**, alignement `center` → `flex-start`
(centrer un bloc de texte seul, sans image en vis-à-vis, n'avait plus de sens), gouttières 10 → 8. Sur mobile,
`layout_flex_direction_mobile` passe de `column-reverse` à `column` : le `reverse` n'existait que pour poser l'image
au-dessus du texte.

### b) Le titre — casse normale

`text_M3HqKb` reçoit la classe **`nm-coll-title`**, neutralisée en CSS par `text-transform: none !important`.

Le bloc est balisé `<h1>` mais stylé à l'échelle `h2`, et le réglage global de casse des h2 est en majuscules — c'est le
même mécanisme que sur les cartes produit et les légendes du méga-menu. Le titre est donc désormais en casse normale,
cohérent avec les libellés du menu.

### c) Le « Voir plus » — armé, puis réparé

`text_GMnLLj` passe à `show_read_more: true`, `read_more_length: 50`.

⚠️ **`read_more_length` est une hauteur en pixels, pas un nombre de caractères** — et Shopify impose un **plancher à 50**.
Ma première écriture à 48 a été **rejetée** avec un message explicite (`Setting 'read_more_length' can't be less than 50`)
et `upsertedThemeFiles: []` : ici la validation parle, contrairement au rejet silencieux du champ CSS de section.

Le réglage seul ne suffisait pas, pour deux raisons distinctes, toutes deux corrigées.

**1. Il n'y avait rien à replier.** Les descriptions faisaient 1 à 2 lignes. C'est traité par le contenu, §2 g.

**2. Le composant était cassé — découvert en le testant.** Une fois les vraies descriptions en place, le bouton
apparaissait bien, basculait bien son libellé de « Voir plus » à « Voir moins »… et **le texte ne se dépliait jamais**.

Diagnostic mené en direct sur `/collections/plongeuses` :

| Mesure | Avant clic | Après clic (état initial) |
|---|---:|---:|
| Hauteur rendue de `.see-more__content` | 50 px | **50 px** |
| `scrollHeight` (contenu réel) | 246 px | 246 px |
| `max-height` **inline** posé par le script | 50 px | **246 px** |
| `max-height` **calculé** | 50 px | **50 px** |
| Libellé du bouton | Voir plus | Voir moins |

Le script fait donc son travail : il pose bien `max-height: 246px` en style inline et ajoute la classe
`see-more__content--expanded`. Mais la valeur calculée reste à 50 px — et **seule une règle `!important` peut battre un
style inline**. Cette règle vit dans une feuille servie par le CDN du thème, que le CSSOM refuse de lire (feuille
cross-origin) : impossible de la corriger à la source.

Correctif : un fichier dédié **`assets/noirmont-see-more-fix.css`**, chargé en **dernière** feuille du `<head>`, qui rend
la main à l'état déplié que le thème marque lui-même :

```css
.see-more__content.see-more__content--expanded {
  max-height: none !important;
  overflow: visible !important;
}
```

Deux classes de sélecteur pour passer devant une règle à classe unique, et `!important` pour passer devant la sienne.

**Vérifié après correctif, sur la même page** : hauteur **50 px → 246 px**, `max-height` calculé à `none`, libellé
« Voir moins », texte intégralement révélé, et aucun débordement introduit. Le « Voir plus » fonctionne.

### d) Les pastilles de collections sœurs — nouvelle section

Nouvelle section **`collections_soeurs`** (type `collections-featured`), insérée **entre la bannière et la grille**.
Elle permet de rebondir latéralement d'une famille à l'autre sans repasser par le menu.

- **11 collections** : `montres`, `classiques`, `sport-chic`, `chronos`, `plongeuses`, `gmt`, `accessoires`,
  `remontoirs`, `ecrins-et-rouleaux`, `bracelets`, `outils-d-horloger`.

> **Corrigé après retour de Hakim (rév. 2).** La première version les rendait en **carrousel à grandes vignettes
> rondes** : les pastilles sortaient de l'écran des deux côtés, coupées au ras du bord, et les images étaient beaucoup
> trop grosses. Ce n'était pas le montage de montre-avenue.

Version retenue, conforme au modèle : **rangée statique de boutons arrondis**. Vignette ronde de **28 px à gauche**
(24 px sous 750 px), libellé à droite, fin liseré arrondi pierre autour de l'ensemble, **aucune flèche, aucun
défilement**. La rangée passe simplement à la ligne quand elle ne tient pas.

Techniquement : `layout_type` est passé de `slider` à **`grid`** (plus aucun balisage de carrousel n'est produit), et
le CSS reprend la grille du thème en `display: flex` + `flex-wrap: wrap`, pour que chaque bouton fasse la largeur de
son texte au lieu d'occuper une colonne entière. Le libellé est en `white-space: nowrap` : c'est le bouton entier qui
passe à la ligne, jamais le mot.

### e) Les filtres — colonne de gauche

`blocks.filters` : `display_mode` **`inline` → `sidebar`**, et `sticky` **`false` → `true`**.

Le thème bascule alors la grille en `25% / 75%`. `grid_columns` reste à **3** — au-delà, les cartes seraient écrasées par
la perte de 25 % de largeur. La colonne est rendue collante en CSS avec un décalage de 88 px pour démarrer sous le header
collant (65 px) et le fil d'Ariane.

### f) Les produits remontés

`main.settings.padding_top` : 50 → **20**. Cumulé à la disparition de l'image et à la bannière resserrée, c'est ce qui
ramène la première rangée en haut d'écran.

**Mesuré** sur `/collections/montres` : le premier produit démarre à **417 px** du haut de la fenêtre. La première
rangée est entièrement au-dessus de la ligne de flottaison. C'était le défaut de départ ; il est corrigé.

### g) Onze vraies descriptions de collection

C'était la cause de fond du « Voir plus » inerte : il n'y avait rien à replier. Les onze collections ont désormais un
paragraphe substantiel, entre 700 et 950 caractères, écrit dans la voix de la maison.

Règles de marque appliquées, et ce qu'elles ont concrètement interdit :

- **Pédagogie destinée à un particulier.** Chaque description explique un mécanisme plutôt que de le nommer : ce qu'est
  une lunette tournante et *pourquoi* elle ne tourne que dans un sens, ce qu'est un compteur de chronographe, ce qu'est
  l'entrecorne d'un bracelet et comment la mesurer chez soi avec une règle, pourquoi une automatique s'arrête sur une
  commode. Aucun ton de professionnel s'adressant à un pair.
- **Aucune marque tierce.** Les calibres sont cités parce que ce sont des fabricants de composants, donc autorisés :
  NH35, NH34, Miyota 8215, Mingzhu 2813, PT5000, DG3804 — tous relevés dans nos vraies valeurs d'options. Aucun nom de
  marque de design n'apparaît, y compris pour désigner un style de bracelet ou de boîtier.
- **Promesses vérifiables uniquement.** Rien sur l'étanchéité, aucune garantie, aucun matériau que nous ne pouvons pas
  attester. Le cas le plus délicat était les Plongeuses : le texte assume explicitement la limite plutôt que de la
  contourner — « nous n'annonçons pas de profondeur d'immersion. Le dessin est celui d'une montre de plongée ; l'usage
  que nous vous recommandons reste celui d'une montre de tous les jours. » Même prudence sur les remontoirs, décrits en
  « finition bois » et « similicuir » (le produit est en PU) plutôt qu'en bois massif ou en cuir.

Les faits avancés sont tous adossés à des données réelles du catalogue : les diamètres 36 et 39 mm et les fonds acier
ou verre viennent des valeurs d'options, les largeurs de bracelet de 12 à 22 mm de l'inventaire, les effectifs
(six Plongeuses, six Voyageur, douze Contre-la-montre) des comptes vérifiés.

### h) Les filtres de vitrine — non modifiables en l'état

Traité à part, §4 : le chantier est **bloqué**, pour une raison qui n'était pas connue au moment de la demande.

| Fichier | Avant | Après | Nature |
|---|---:|---:|---|
| `templates/collection.json` | 13 060 o | 9 080 o | Bannière, titre, « Voir plus », section sœurs, filtres, paddings |
| `assets/noirmont-collection.css` | — | 7 025 o | **Nouveau** — mise en forme |
| `assets/noirmont-see-more-fix.css` | — | 1 476 o | **Nouveau** — correctif du dépliage |
| `layout/theme.liquid` | 1 451 o | 1 744 o | Deux lignes : chargement des deux feuilles |

Sauvegarde de l'état d'origine : `scratchpad/backup-theme-megamenu/collection.json`.

Les onze collections ont par ailleurs reçu une nouvelle `descriptionHtml` (§2 g). Aucun autre champ de collection n'a
été touché — les images en particulier sont intactes, elles alimentent le méga-menu et les pastilles.

> **Le template a rétréci alors qu'il gagne une section.** L'écart vient du reformatage (l'original mettait chaque
> élément de tableau sur sa propre ligne), pas d'une perte. Je ne me suis pas cru sur parole : un contrôle structurel
> indépendant a diffé l'arbre de clés du fichier écrit contre la sauvegarde.
> **Résultat : 0 chemin de clé perdu**, 84 chemins ajoutés, tous imputables à `collections_soeurs` (83) et au
> `disabled` du groupe image (1). Les 17 points de la checklist sont au vert. Verdict : intègre.

---

## 4. Les filtres de vitrine — bloqué, l'application n'est pas installée

La demande : remplacer « Disponibilité » par des facettes utiles — Prix, Diamètre, Mouvement, Couleur de cadran,
Type/Famille.

### Ce qui bloque

Les filtres de vitrine se configurent dans l'application **Shopify Search & Discovery**. J'ai ouvert l'admin dans la
session Chrome de Hakim — **elle est active, aucun identifiant n'a été saisi** — et l'application **n'est pas
installée** : « Vous n'avez pas installé cette application. »

Conséquence directe, et elle explique la capture : **« Disponibilité » et « Prix » ne sont pas un choix de
configuration, ce sont les facettes par défaut de Shopify** quand l'application est absente. Sans elle, la liste des
facettes n'est pas modifiable — ni par le thème, ni par l'API Admin.

**Je n'ai pas installé l'application moi-même** : installer une application accorde des autorisations sur la boutique,
c'est une décision qui revient à Hakim.

### L'audit préalable — et il change la réponse

Avant même de configurer quoi que ce soit, j'ai inventorié les 92 produits actifs pour vérifier l'unicité et
l'orthographe des valeurs réelles, comme demandé. **Trois des cinq facettes visées ne sont pas alimentées.**

| Facette | Verdict | Fait constaté |
|---|---|---|
| **Prix** | ✅ Prête | Champ natif, aucun préalable |
| **Type / Famille** | ✅ Prête | Les tags `classiques` (15), `sport-chic` (14), `chronos` (12), `plongeuses` (6), `gmt` (6) forment une **partition exacte** des 53 montres. Aucun trou, aucune variante orthographique |
| **Mouvement** | ⚠️ Dégradée | L'option `Mouvement` est propre (4 valeurs, zéro doublon) mais ne couvre que **10 montres sur 53**. Les 15 autres sont sous `Mouvement & fond`, en valeurs composées |
| **Diamètre** | ❌ Absente | N'existe nulle part comme donnée autonome. Présent sur **15 montres sur 53**, toujours enfoui dans une chaîne composée, sous **trois** noms d'options différents |
| **Couleur de cadran** | ❌ Absente | 20 montres sur 53, valeurs composées, et **13 nuances pour 14 produits** — une facette qui ne filtre rien |

⚠️ **Le piège signalé chez eux existe bien chez nous, sous une autre forme.** Pas de doublon d'accent, mais :
`productType` vaut `Montre automatique` pour 41 montres et `Montre chronographe` pour 12 — donc **inutilisable** pour
distinguer les familles. Et surtout, une facette adossée aux tags exposerait aussi `bracelet` **et** `bracelets`,
`outils` **et** `outillage` — exactement deux libellés pour la même chose. Côté accessoires, `Couleur` / `Color` /
`Band Color` cohabitent avec des doublons de casse (`black` / `Black`, `WHITE` / `white`) et ~160 valeurs.

### Ce que je recommande, une fois l'application installée

1. **Retirer Disponibilité** — sans intérêt sur un catalogue quasi intégralement en stock.
2. **Activer Prix.**
3. **Activer Famille**, en restreignant la facette aux 5 tags de famille. Si la restriction n'est pas possible, créer
   d'abord un métachamp `custom.famille` alimenté depuis ces 5 tags — c'est plus propre et cela évite d'exposer les
   tags techniques.
4. **Ne pas activer Diamètre, Mouvement ni Couleur de cadran en l'état.** Une facette qui couvre 19 % du catalogue ou
   qui affiche « Miyota 8215 · 39 mm · fond verre » est pire que pas de facette. Le préalable est un métachamp dédié
   (`custom.diametre`, `custom.calibre`, `custom.couleur_cadran`) renseigné sur les 53 montres — c'est un chantier de
   saisie à part entière, à cadrer séparément.

---

## 5. Contrôle — cette fois, vérifié à l'écran

La session Chrome de Hakim porte déjà le cookie du mot de passe de boutique. **J'ai donc pu voir le rendu par simple
navigation, sans jamais saisir de mot de passe.**

Vérifié en direct sur le thème brouillon :

| Contrôle | Résultat |
|---|---|
| Débordement horizontal desktop — `classiques`, `bracelets`, `montres` | **Aucun** (`scrollWidth` = `clientWidth` = 1920) |
| Pastilles sœurs | 11 boutons, `display: flex` + `flex-wrap: wrap`, vignette **28 px**, **0 flèche** |
| Bouton le plus large | « Écrins et rouleaux » = **176 px** |
| Casse du titre de collection | `text-transform: none` |
| « Voir plus » | 50 px → **246 px**, `max-height: none`, texte entièrement révélé |
| Premier produit sur `/collections/montres` | **417 px** du haut — au-dessus de la ligne de flottaison |
| Thème publié `Helio` | Inchangé, daté du 24/07 |

**Ce que je n'ai PAS pu vérifier — le mobile.** La fenêtre du navigateur ne se laisse pas redimensionner dans cette
session : la page rapporte obstinément 1920 px de large quelle que soit la taille demandée. Le lien de partage de
prévisualisation, qui aurait permis d'ouvrir la page dans un navigateur redimensionnable, est enfermé dans une iframe
cross-origin illisible.

À défaut, un contrôle structurel : le plus large bouton fait **176 px**, donc il tient sans déborder sur un écran de
320 px, et la rangée est déjà en `flex-wrap` (elle passe à deux lignes dès 1920 px, ce qui prouve que le retour à la
ligne fonctionne). **Restent à valider à l'œil sur un vrai téléphone** : le basculement des filtres en modale sous
990 px, et la hauteur totale de la bannière une fois la description dépliée.

---

## 6. Limites constatées

1. **Les filtres restent ceux par défaut** tant que Search & Discovery n'est pas installée (§4).
2. **Trois des cinq facettes demandées ne sont pas alimentées par les données** (§4) et exigent un chantier de saisie
   sur 53 produits avant d'exister.
3. **Deux vocabulaires d'étiquettes cohabitent** sur les accessoires (`bracelet`/`bracelets`, `outils`/`outillage`) et
   `productType` mélange `Accessoire` avec `Bracelet`/`Outillage`/`Rangement`. À réconcilier avant toute facette
   accessoire.
4. **Le mobile n'est pas vérifié à l'écran** (§5).
5. **Les pastilles sœurs sont identiques sur toutes les pages collection.** Un seul template, donc la liste est statique :
   depuis « Bracelets », les pastilles affichent aussi les familles de montres, et « Bracelets » se montre lui-même.
   C'est exactement la limite de montre-avenue. Le lever demanderait des templates de collection distincts.
6. **`grid_columns` est verrouillé à 3** tant que les filtres sont en colonne. Repasser en `inline` libérerait une
   quatrième colonne — arbitrage à trancher visuellement.
7. **Le correctif du « Voir plus » est un contre-feu, pas une réparation à la source** (§2 c). La règle fautive est dans
   une feuille du thème servie par le CDN. Si une mise à jour du thème la change, le correctif deviendra soit inutile,
   soit à réviser — il est isolé dans son propre fichier pour être facile à retirer.
