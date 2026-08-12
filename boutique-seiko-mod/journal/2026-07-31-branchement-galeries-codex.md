# Branchement des galeries Codex — NOIRMONT — nuit du 26/07/2026

Boutique **Maison Noirmont** (`v42pzp-h4.myshopify.com`, maisonnoirmont.fr) — identité vérifiée par `get-shop-info` avant la première écriture.

> **TOTAL APRÈS LES DEUX PASSES : 85 fiches branchées · 206 médias créés · 0 média supprimé.**
> Première passe (nuit) : 57 fiches, 163 médias. Seconde passe (matin) : 28 fiches accessoires + 3 faces stériles substituées, 43 médias. Détail de la seconde passe tout en bas du document.

**Première passe : 57 fiches branchées · 163 médias créés · 0 média supprimé · 4 fiches écartées · 29 fiches encore en génération chez Codex.**

Sauvegarde préalable : `backup-avant-branchement-galeries-codex.json` (état des médias de chaque fiche cible **avant** toute mutation).
Sauvegarde des fichiers condamnés : `boutique-seiko-mod/backups/backup-details-texte-incruste-2026-07-26/`.

---

## Méthode

Règle de clôture respectée : **aucune fiche branchée sans sa planche `qa/<handle>-planche.jpg`**. Deux vagues ont été traitées ; à la fin de la seconde, les 62 fiches closes par Codex étaient toutes arbitrées, et plus aucune fiche prête n'attendait.

Les planches de Codex font 1556 × 426 px, soit **380 px par vignette** — trop grossier pour juger une main ou un micro-lettrage. J'ai donc régénéré, à partir des mêmes fichiers, des planches de contrôle à **740 px par vignette** (grille 2×2, face en ligne + les 3 slots), et c'est sur celles-là qu'a porté le contrôle, avec recadrages jusqu'à ×20 sur les zones critiques.

> ### 📌 Règle de méthode — le contrôle de stérilité se fait à 740 px minimum, avec zoom
>
> Que six faces à mention « SWISS MADE » soient **déjà publiées** prouve que les contrôles de stérilité précédents avaient un trou : **une planche à 380 px par vignette ne permet pas de lire un micro-lettrage de cadran.** Le texte y est physiquement présent mais indiscernable, et il passe le contrôle.
>
> À partir de maintenant, et pour toute passe visuelle sur cette boutique :
> 1. Le contrôle porte sur des planches à **740 px par vignette au minimum**, jamais sur les planches de génération.
> 2. Tout cadran fait l'objet d'un **recadrage dédié de la zone 5h–7h**, agrandi au moins ×5, lu séparément. C'est là que se logent les mentions d'origine et de marque.
> 3. Un lettrage **atténué, flouté ou fantôme compte comme un lettrage présent**. « Peu visible » n'est pas « absent ».
> 4. Le même barème s'applique aux images déjà en ligne, pas seulement aux nouvelles.

Provenance des faces vérifiée avant de juger la cohérence de coloris : les fichiers `entrees-faces/` sont **bit-identiques** aux images en ligne (hash de perception, distance 0 sur échantillon).

Chaîne technique : `stagedUploadsCreate` (PUT, IMAGE) → `curl -T` avec `content-type: image/jpeg` (163 × HTTP 200) → `productCreateMedia` avec le `resourceUrl` non signé → `productReorderMedia`. Tous les retours `mediaUserErrors` sont vides. Toutes les images sont arrivées en **2048 × 2048**, statut `READY`.

Texte alternatif appliqué : `<Titre du produit> — <sujet> — Maison Noirmont`, avec pour sujets `en situation`, `macro`, `au poignet`.

**Ordre d'affichage.** Beaucoup de fiches portaient déjà, en position 2, un média « témoignage client » héritié de leur mère. La face reste en position 1 (et les faces multi-coloris restent groupées en tête) ; `situation → macro → poignet` s'insère juste après ; les médias hérités sont repoussés en fin de galerie. Vérifié en direct sur échantillon : `contre-la-montre-blanc-chronographe` (3 faces → 3 nouveaux → témoignage), `quarante-et-un-sport-acier`, `trente-neuf-duo-classique-bicolore`, `bracelet-milanais-maille-italienne`. Aucun doublon : chaque fiche a reçu exactement ses 3 (ou 2) fichiers neufs, et les compteurs de médias retournés par l'API correspondent un à un à l'attendu.

---

## Fiches branchées

### Contre-la-montre — chronographe (12 fiches, 36 médias)

| handle | médias après |
|---|---:|
| contre-la-montre-argent-chronographe | 5 |
| contre-la-montre-blanc-chronographe | 7 |
| contre-la-montre-bleu-glacier-chronographe | 5 |
| contre-la-montre-champagne-chronographe | 6 |
| contre-la-montre-compteurs-bleus-chronographe | 5 |
| contre-la-montre-gris-anthracite-chronographe | 5 |
| contre-la-montre-noir-chronographe | 6 |
| contre-la-montre-panda-chronographe | 6 |
| contre-la-montre-panda-inverse-chronographe | 6 |
| contre-la-montre-rose-poudre-chronographe | 5 |
| contre-la-montre-turquoise-chronographe | 6 |
| contre-la-montre-vert-chronographe | 6 |

### Héritage — plongeuse vintage 42 (3 fiches, 9 médias)
`heritage-bleu-plongeuse-vintage-42` 5 · `heritage-bleu-nuit-plongeuse-vintage-42` 5 · `heritage-vert-plongeuse-vintage-42` 5

### Intégrale — sport chic (6 fiches, 18 médias)
`integrale-blanc-argente-sport-chic-acier` 5 · `integrale-bleu-ciel-sport-chic-acier` 5 · `integrale-bleu-nuit-sport-chic-acier` 5 · `integrale-brun-or-rose-sport-chic` 5 · `integrale-noir-sport-chic-acier` 5 · `integrale-turquoise-sport-chic-acier` 5

### Voyageur — GMT (6 fiches, 18 médias)
`voyageur-bicolore-cadran-brun-gmt` 5 · `voyageur-bicolore-gmt-3-maillons` 5 · `voyageur-bicolore-gmt-5-maillons` 5 · `voyageur-or-gmt-3-maillons` 5 · `voyageur-or-gmt-president` 5 · `voyageur-or-rose-gmt-5-maillons` 5

### Trente-Six — classique jubilé (6 fiches, 18 médias)
`trente-six-bleu-classique-jubile` 4 · `trente-six-dore-classique-jubile` 4 · `trente-six-or-integral-classique-jubile` 4 · `trente-six-rose-classique-jubile` 4 · `trente-six-rouge-classique-jubile` 4 · **`trente-six-classique-jubile` (mère active) 16**

### Trente-Neuf (7 fiches, 21 médias)
`trente-neuf-bleu-classique-cannelee` 4 · `trente-neuf-bleu-mer-classique-cannelee` 4 · `trente-neuf-noir-classique-cannelee` 4 · `trente-neuf-rouge-classique-cannelee` 4 · `trente-neuf-vert-classique-cannelee` 4 · `trente-neuf-duo-dore-classique-bicolore` 4 · **`trente-neuf-duo-classique-bicolore` (mère active) 12**

### Quarante-et-Un — sport acier (7 fiches, 21 médias)
`quarante-et-un-blanc-cuir-sport-acier` 4 · `quarante-et-un-bleu-acier-sport-acier` 4 · `quarante-et-un-bleu-cuir-sport-acier` 4 · `quarante-et-un-noir-acier-sport-acier` 4 · `quarante-et-un-noir-cuir-sport-acier` 4 · `quarante-et-un-noir-jaune-acier-sport-acier` 4 · **`quarante-et-un-sport-acier` (mère active) 17**

### Noirmont Un (2 fiches, 6 médias)
`noirmont-un-bronze-plongeuse` 4 · **`noirmont-un-plongeuse-acier` (mère active) 12**

### Accessoires (8 fiches, 16 médias — 2 slots chacun, pas de porté-poignet)
`barrettes-de-rechange-270` 3 · `bracelet-acier-massif-12-22-mm` 3 · `bracelet-caoutchouc-gaufre` 3 · `bracelet-cuir-daim-degagement-rapide` 3 · `bracelet-fkm-courbe` 3 · `bracelet-jubile-acier-904l-20mm` 3 · `bracelet-jubile-embouts-courbes` 3 · `bracelet-milanais-maille-italienne` 3

---

## Fiches écartées — 4

Mises de côté, **rien n'a été branché dessus**, aucune retouche tentée. Les fichiers restent intacts dans `generated/`.

| handle | slot | défaut constaté |
|---|---|---|
| `integrale-vert-sport-chic-acier` | 03-macro | Fragment métallique blanc **flottant** à droite du guichet de date (3h), détaché du rail des minutes, à la place de l'index. Absent de la face, de 02 et de 04. Vérifié moi-même au recadrage : c'est un artefact franc, pas une ombre. |
| `trente-neuf-rose-classique-cannelee` | 02-situation | Micro-lettrage typographique sur le cadran entre 5h et 6h (deux blocs de caractères). Vérifié moi-même : ce sont bien des formes de lettres. Voir aussi la section « SWISS MADE » ci-dessous : la face déjà en ligne porte le même défaut. |
| `trente-neuf-classique-cannelee` (mère active) | 03-macro, 02, 04 | Guichet de date non formé : bulle de verre à bord facetté, aucun chiffre, tache grise flottante ; carré blanc et losange en 02. Le défaut est présent sur la face source et **amplifié** par la génération. |
| `bracelet-fkm-tropical` | 03-macro | Relief anguleux non organique sur le bord droit du bracelet (barre inclinée à hachures régulières + forme en L), étranger au motif de feuilles. Se lit comme un cartouche estampé. Flou et quasi effacé sur la face de référence, **rendu net** par la génération. |

## Hors périmètre — 1

`noirmont-deux-plongeuse-ceramique` : la fiche est prête chez Codex (planche + 3 images présentes dans `generated/`) mais **Noirmont Deux est explicitement exclu de l'intervention**. Rien n'a été branché, rien n'a été retiré. Les 3 images t'attendent.

---

## Médias retirés — aucun

L'audit condamne 6 images « détails et finitions » à texte incrusté sur les mères actives. État réel du chantier :

| mère active | média | remplaçante branchée ? | action |
|---|---|---|---|
| `trente-six-classique-jubile` | `59680093962578` | oui | **non retiré** — voir ci-dessous |
| `quarante-et-un-sport-acier` | `59680004407634` | oui | non retiré |
| `trente-neuf-duo-classique-bicolore` | `59680094159186` | oui | non retiré |
| `noirmont-un-plongeuse-acier` | `59680093405522` | oui | non retiré |
| `trente-neuf-classique-cannelee` | `59680004211026` | **non** (fiche écartée) | pas éligible |
| `noirmont-deux-plongeuse-ceramique` | `59680093602130` | non (hors périmètre) | pas éligible |

**Pourquoi je ne les ai pas supprimés.** Le partage a été vérifié : ces 6 médias n'apparaissent **que** sur leur propre mère dans tout le catalogue (85 fiches relevées en direct). `productDeleteMedia` ne les détacherait donc pas, il les **supprimerait définitivement**. Je ne fais pas de suppression définitive de données sans ton accord direct — la consigne d'un agent ne vaut pas ton accord. Tout est prêt pour que tu le fasses en une commande :

- la copie de `trente-six` est déjà sur disque (`boutique-seiko-mod/backups/backup-details-texte-incruste-2026-07-26/`, 2048 × 2048, 458 Ko) ;
- les 3 autres URL CDN sont dans `backup-avant-branchement-galeries-codex.json`, section `meresActivesPorteusesDuTexteIncruste` ;
- les 4 remplaçantes sont en ligne et en bonne position, donc le retrait ne laissera aucun trou dans les galeries.

---

## ⚠️ À voir en priorité au réveil : « SWISS MADE » sur des faces déjà publiées

Découvert en vérifiant un cas écarté, puis confirmé par un balayage des **91 faces en ligne** (recadrages de la zone 6h à ×2 puis jusqu'à ×20). Ce n'est pas un défaut des images de Codex — c'est un défaut des images **déjà publiées**.

| handle | texte lu sur le cadran | position |
|---|---|---|
| `trente-neuf-bleu-classique-cannelee` | **SWISS** + **MADE** | 6h, de part et d'autre de l'index 6 |
| `trente-neuf-rose-classique-cannelee` | **SWISS** + **MADE** | 6h |
| `trente-neuf-rouge-classique-cannelee` | **SWISS** + **MADE** | 6h |
| `trente-neuf-vert-classique-cannelee` | **SWISS** net, second mot illisible | 6h |
| `trente-neuf-classique-cannelee` | illisible, 5–6 caractères, formes de lettres nettes | 6h |
| `noirmont-deux-plongeuse-ceramique` | illisible, fragment « …TS SS » | 6h / 5h |

Deux raisons de traiter ça vite : ça viole le standard 100 % photo sans texte, et une mention d'origine suisse sur une montre sourcée en dropshipping est une **allégation d'origine fausse** — donc un risque bien au-delà de l'esthétique. Cinq des six cas sont sur la famille `trente-neuf`.

Trois observations connexes du même balayage :
1. **Floutage plutôt que suppression** — `noirmont-un-plongeuse-acier`, `noirmont-deux-plongeuse-ceramique`, `trente-neuf-classique-cannelee`, `trente-six-classique-jubile`, `quarante-et-un-noir-cuir-sport-acier`, `quarante-et-un-sport-acier` portent de larges taches de flou sur le cadran : le lettrage a été masqué, pas retiré. Conforme au standard, mais visible comme défaut d'image.
2. **Résidu probable** — 5 `quarante-et-un` ont un amas de micro-points clairs exactement à l'emplacement du SWISS MADE. Poussé à ×20, aucun contour de lettre : pas compté comme texte, mais c'est probablement le même lettrage effacé.
3. **Hors cadran** — `remontoir-solo-01-face.jpg` porte un lettrage embossé (~7 glyphes, illisible) sur la façade du remontoir. Pas un cadran, mais du texte de marque sur une image publiée.

Je n'ai touché à aucune de ces faces : les retirer laisserait des fiches sans image, et l'arbitrage (regénérer ? retoucher ? masquer ?) t'appartient.

---

## Tentative de régénération des faces « SWISS MADE » — échouée, rien remplacé

Décision prise en cours de nuit : plutôt que supprimer ces faces (ce sont les images principales, les fiches se retrouveraient sans visuel), les **régénérer** stériles en image-to-image, avec nos crédits Higgsfield.

**Les 6 handles concernés**, à savoir pour la suite :

1. `trente-neuf-bleu-classique-cannelee`
2. `trente-neuf-rose-classique-cannelee`
3. `trente-neuf-rouge-classique-cannelee`
4. `trente-neuf-vert-classique-cannelee`
5. `trente-neuf-classique-cannelee` (mère active)
6. `noirmont-deux-plongeuse-ceramique`

**Ce qui a été fait.** Modèle `nano_banana_pro`, résolution 4K, 1:1, image-to-image depuis la face en ligne, aucun inpainting. Deux passes :

| passe | consigne | images | crédits |
|---|---|---:|---:|
| 1 | « une seule modification : cadran vierge », tout le reste identique | 5 (1 par fiche) | 20 |
| 2 | consigne durcie : texte **absent**, « ni atténué, ni flouté, ni partiellement effacé, aucun fantôme, aucune ombre, aucun contour », secteur 5h–7h aussi nu que le secteur 1h–3h | 10 (2 variantes par fiche) | 40 |

**Résultat : échec, sur les deux passes.** Le modèle **atténue le lettrage au lieu de le supprimer.** Sur chaque sortie contrôlée au zoom fort, il reste aux deux emplacements exacts du texte d'origine un fantôme dont la forme des lettres est encore reconnaissable — « SWISS » à gauche, « MADE » à droite. Invisible à taille d'affichage, présent au zoom. C'est exactement le mode d'échec « floutage plutôt que suppression » que j'avais déjà relevé sur 6 autres faces du catalogue, et il ne satisfait pas le critère : *un lettrage atténué compte comme un lettrage présent.*

Tout le reste, en revanche, était bien préservé : boîtier, lunette cannelée, bracelet jubilé, aiguilles et leur position, index, guichet de date, teinte et soleillé du cadran, cadrage, fond, lumière et ombre portée. Le modèle est donc le bon choix pour ce type de reprise — c'est la suppression du texte qui ne passe pas.

**Conséquence : aucune face n'a été remplacée.** Les 15 images sont conservées pour examen dans `scratchpad/noirmont-galeries/faces-steriles-v2/` (passe 1 à la racine, passe 2 dans `p2/`). Les 6 faces en ligne sont intactes.

**Ce que je recommande**, par ordre de préférence :
1. **Reprendre la face à la source** — régénérer la montre entière depuis le prompt d'origine avec l'interdiction de texte en tête de prompt, plutôt que demander à un modèle d'effacer un texte déjà présent. Effacer est manifestement plus dur que ne pas écrire.
2. À défaut, essayer un autre modèle d'édition, ou une passe de suppression suivie d'une **régénération complète** de la zone de cadran plutôt qu'un simple gommage.
3. En dernier recours et si la fiche peut vivre sans, retirer la face — mais c'est ton arbitrage, cf. ci-dessous.

`noirmont-deux-plongeuse-ceramique` **n'a pas été régénéré du tout** : Noirmont Deux est sous interdiction explicite de toute intervention depuis le début de la mission, et cette interdiction n'a pas été levée nommément. Rien n'a été dépensé dessus. Un mot de toi et je la traite comme les autres.

**Crédits Higgsfield** : 355 au départ, **60 consommés**, il en reste ~295.

### Troisième voie tentée : conditionner depuis une sœur stérile

Plutôt que gommer un texte, on repart d'une face **déjà propre** de la même famille et on ne change que la couleur du cadran — la technique de la passe de coloris d'origine. Aucun texte à hériter, et le boîtier, la lunette cannelée, le bracelet jubilé, les aiguilles, le cadrage et la lumière restent ceux de la famille.

**Source retenue : `trente-neuf-bleu-mer-classique-cannelee`**, vérifiée par moi au zoom fort avant usage — l'arc 4h–8h du cadran ne porte que les index bâtons et la minuterie, aucune inscription. (`trente-neuf-noir` est également propre mais son cadran sombre rend le contrôle moins net ; écartée comme source pour cette raison.)

5 générations lancées depuis cette source, une par coloris cible (bleu roi, rose poudré, rouge, vert, champagne), 20 crédits. Fichiers dans `scratchpad/noirmont-galeries/faces-steriles-v3/`, déjà normalisés en 2048 × 2048 et nommés `<handle>-01-face.jpg`, prêts à brancher.

**VERDICT : la voie fonctionne. 5 cadrans sur 5 sont stériles.** Contrôlés sur planche à 1240 px de large, recadrage de l'arc 4h–8h : on n'y voit que les index bâtons et la minuterie gravée. Aucun mot, aucun fantôme, aucune trace à l'emplacement du « SWISS MADE ». Le boîtier, la lunette cannelée, le bracelet jubilé, les aiguilles, le cadrage, le fond et l'ombre sont ceux de la famille — donc homogènes avec les trois autres images de chaque galerie. Le changement de teinte est propre et le soleillé est conservé.

⚠️ **Un point à lever avant de brancher.** Sur les 5 sorties — et déjà sur la face source `trente-neuf-bleu-mer` publiée — un **maillon de bracelet proche du boîtier porte une petite zone texturée/piquetée** qui, à ce niveau d'agrandissement, pourrait être une gravure. Ce n'est pas sur le cadran et c'est **hérité de la source déjà en ligne**, donc ce n'est pas un défaut introduit par cette passe. Mais compte tenu de ce qu'on vient de découvrir sur cette boutique, je n'ai pas voulu mettre en position 1 sur 5 fiches publiées une marque que je n'ai pas formellement identifiée. **À trancher : zoom dédié sur ce maillon, puis branchement si c'est bien un reflet.** Les 5 faces ne sont donc pas encore branchées.

**Crédits** : 80 consommés au total sur les trois passes, ~275 restants.

### `remontoir-solo` — ce que je vois exactement

Sur la face publiée, la façade métallique du socle porte **un mot gravé en creux dans le métal**, pas un texte imprimé ni un simple relief décoratif : environ 7 glyphes, hauts d'à peu près 1 % de la hauteur d'image, accrochant la lumière par leur arête. Ils forment un mot lisible mais dépourvu de sens, qui se lit approximativement **« FLOTOWI »** — typique d'un nom de marque fabriqué par un modèle.

Deux précisions utiles à l'arbitrage :
- c'est une **marque inventée sur le produit**, pas une mention d'origine : le risque n'est pas le même que « SWISS MADE », c'est un problème de charte et de crédibilité, pas une allégation d'origine fausse ;
- juste au-dessus, sur la même arête, il y a une **large tache de flou** : quelque chose d'autre a déjà été masqué à cet endroit, sans être supprimé. La façade a donc déjà subi une retouche partielle.

## Note sur les deux suppressions restées en attente

Deux retraits ont été demandés cette nuit et **aucun des deux n'a été exécuté**, pour la même raison :

1. les 4 images « détails et finitions » éligibles ;
2. les anciennes faces « SWISS MADE », une fois leurs remplaçantes validées.

Dans les deux cas la suppression est **définitive** (médias non partagés), et dans les deux cas l'autorisation m'est venue d'un agent coordinateur, pas de toi. Je ne fais pas de suppression irréversible de données sur cette base : c'est une décision qui te revient, et tu es la seule personne à pouvoir la donner. Rien n'est perdu — sauvegardes locales en place, remplaçantes en ligne pour les « détails », identifiants et URL consignés — et chaque retrait se fait en une commande quand tu le veux.

## Contrôle final

- **Comptage** : les 57 compteurs de médias retournés par l'API correspondent exactement à l'attendu (état d'origine + 3, ou + 2 pour les accessoires). Aucun doublon possible : chaque média branché est un fichier neuf, uploadé une seule fois.
- **Ordre** : vérifié en direct sur 4 cas représentatifs, dont une fiche multi-coloris (3 faces), deux mères actives à galerie longue et un accessoire. Schéma conforme partout : face → situation → macro → poignet → médias hérités.
- **Rendu sur le thème brouillon `204248088914`** : **non vérifiable**. Le storefront répond 302 sur `maisonnoirmont.fr`, et le POST du mot de passe `[RETIRÉ — voir docs/codex-handoff/07-SETUP-AND-SECRETS.md]` sur `/password` renvoie lui aussi 302 sans poser de cookie exploitable. Conformément à la consigne, je n'ai pas insisté. À refaire par toi depuis un navigateur connecté à l'admin.

## Interdits respectés

Aucun SKU, prix, titre, option, variante, statut ni mapping DSers touché. Aucune fiche publiée ni dépubliée. Les **7 mères en brouillon**, **Noirmont Deux** et les **3 GMT « siglé »** n'ont reçu aucune écriture. Aucun fichier de thème modifié. Aucune commande touchée. Toutes les écritures sont des `productCreateMedia` / `productReorderMedia`.

---

## Reste à faire (état à la fin de la première passe — voir la seconde passe ci-dessous)

1. **Traiter les 6 faces « SWISS MADE »** — le point le plus urgent. La voie « régénération par gommage » est un échec démontré (deux passes, 15 images) ; voir la recommandation plus haut : reprendre la face à la source plutôt que gommer.
2. **Arbitrer les suppressions en attente** : 4 images « détails et finitions », et à terme les anciennes faces. Sauvegardes en place, une commande chacune.
3. **Arbitrer les fiches écartées** — régénération ciblée à demander à Codex.
4. **Brancher Noirmont Deux** si tu lèves l'exclusion : galerie et face de remplacement possibles immédiatement.
5. **Relire quelques fiches en rendu** sur le thème brouillon, ce que le mot de passe storefront m'a empêché de faire.

---
---

# SECONDE PASSE — 26/07/2026, matin

Identité de boutique revérifiée par `get-shop-info` avant la première écriture : **Maison Noirmont / maisonnoirmont.fr**.

**28 fiches accessoires branchées sur 29 · 3 faces stériles mises en position 1 · 43 médias créés · 0 média supprimé · 0 crédit Higgsfield dépensé.**

Sauvegarde des anciennes faces avant substitution : `boutique-seiko-mod/backups/backup-faces-swissmade-2026-07-26/` (5 fichiers 2048 × 2048, les 3 substituées + les 2 en attente). Les anciennes faces **restent aussi en ligne**, reléguées en dernière position de leur galerie — rien n'a été supprimé.

---

## 1. Verdict sur la « gravure » du maillon : **c'est une texture, pas une gravure**

La zone signalée par la passe précédente n'est pas sur un maillon de bracelet : elle est **dans une cannelure de la lunette**, vers 5 h sur le pourtour, là où la gorge est la plus sombre. Recadrage ×10 sur `trente-neuf-bleu-mer` : un amas de granules clairs irréguliers remplissant toute la largeur d'une seule cannelure — aucune ligne de base, aucun pas régulier, aucune forme de lettre, tailles hétérogènes.

**Contrôle comparatif décisif** : recadrées **au même pixel**, les six faces de la famille (`bleu-mer`, `noir`, `bleu`, `rose`, `rouge`, `vert`) portent **toutes** le même amas, dans la même cannelure. C'est donc le rendu systématique du modèle pour une gorge en ombre — un grain de brossage —, pas une inscription. Aucune raison de bloquer le branchement à ce titre.

## 2. Les 5 faces de la voie sœur : deux contrôles orthogonaux, mesurés

### Stérilité — mesure d'énergie haute fréquence dans l'empreinte du texte

Passe-haut `gray − gaussien(σ=3)`, énergie `moyenne(|hp|)` mesurée dans les deux empreintes exactes relevées sur `trente-neuf-bleu` en ligne (« SWISS » x 1165-1228 / y 1236-1266 ; « MADE » x 1244-1302 / y 1190-1232), pixels de cadran uni seulement, et témoins pris sur le même cadran du même candidat.

| face | SWISS | MADE | témoin méd. | témoin p95 |
|---|---:|---:|---:|---:|
| **REF** bleu en ligne | **18,6** | **13,1** | 2,3 | 6,6 |
| **REF** rouge en ligne | **23,2** | **15,5** | 2,0 | 6,4 |
| **REF** rose en ligne | **16,3** | 9,3 | 2,3 | 7,8 |
| **REF** vert en ligne | **18,3** | 3,2 | 2,3 | 6,0 |
| **REF** mère en ligne | **16,9** | 2,6 | 3,4 | 7,8 |
| SOURCE bleu-mer (propre) | 9,6 | 8,2 | 2,3 | 6,4 |
| v3 bleu | 9,1 | 7,8 | 1,7 | 5,5 |
| v3 rose | 5,6 | 8,5 | 2,4 | 6,4 |
| v3 rouge | 8,7 | 6,8 | 1,9 | 5,4 |
| v3 vert | 7,3 | 7,3 | 2,1 | 5,3 |
| v3 mère | 7,8 | 8,8 | 2,2 | 5,9 |

Le plancher de 8-10 dans l'empreinte vient du bord de l'index de 6 h et du rail des minutes qu'elle englobe : il est présent aussi sur la source propre. **Les 5 candidats v3 sont au niveau de la source, jamais au-dessus** ; les faces en ligne porteuses de texte sont 2 à 3 fois plus haut. Confirmé visuellement : passe-haut ×8 sur l'empreinte, les glyphes ressortent nettement sur la REF, l'empreinte est vide sur la source et sur les v3.

Le test a en outre été étendu à **tout le disque du cadran**, cellule par cellule (26 px), normalisé par la médiane du cadran de chaque image : **0 cellule de structure ajoutée** sur les 5 candidats. Aucun lettrage nulle part, pas seulement à 6 h.

### Fidélité — recalage, colorimétrie, présence des organes

Corrélation croisée normalisée sur **12 zones témoins** (bracelet haut et bas, cornes, lunette gauche et basse, couronne, fermoir, ombre portée, fond) contre la source `bleu-mer`, plus ΔE76 par zone et carte de structure du cadran.

| face | NCC min | NCC moy | décalage | ΔE moy | structure perdue | structure ajoutée |
|---|---:|---:|---|---:|---:|---:|
| v3 bleu | 0,925 | 0,977 | 0 px | 4,9 | 0 | 0 |
| v3 rouge | 0,921 | 0,977 | 0 px | 6,0 | 0 | 0 |
| v3 vert | 0,919 | 0,978 | 0 px | **3,5** | 0 | 0 |
| v3 rose | 0,619 | 0,920 | ≤1 px | 7,3 | 2 cellules | 0 |
| v3 mère | 0,672 | 0,927 | 0 px | 7,4 | 4 cellules | 0 |

- **Aucun décalage géométrique** : recalage à 0-1 px sur les 12 zones, les 5 faces.
- **Le vert ne s'effondre pas.** Contrairement au candidat de gommage (−25 % de chroma), le v3 vert affiche le ΔE **le plus bas des cinq** (3,5 ; max 4,8). Le biais de génération global (ΔE ≈ 3, fond de pierre inclus) est présent mais sans plus.
- Le NCC bas de `rose` et `mère` porte **uniquement sur la lunette et le rehaut**, qui prennent la teinte du cadran (rosé, doré). Vérifié côte à côte : **les faces rose et champagne déjà publiées font exactement pareil** — c'est un trait de la famille, pas une régression v3.
- **Les 2 cellules « perdues » de rose et les 4 de mère** sont sur le bord gauche du cadran : c'est le contraste du rehaut chromé contre un cadran clair qui chute, pas un organe manquant.
- **Organes vérifiés un par un** : 12 index et 3 aiguilles présents sur les 5 faces (aucune trotteuse disparue, aucun index effacé — les deux défauts qui condamnaient les candidats de gommage). Guichet de date bien formé **avec loupe cyclope** sur les 5.

**VERDICT : les 5 faces v3 passent les deux axes.**

### Ce qui a été branché, et ce que je n'ai pas branché

**Branchées, en position 1 (3 fiches)** : `trente-neuf-bleu-classique-cannelee`, `trente-neuf-rouge-classique-cannelee`, `trente-neuf-vert-classique-cannelee`. Ordre relu en direct : face stérile → situation → macro → poignet → **ancienne face conservée en position 5**. 5 médias chacune, aucun doublon.

**Non branchées malgré un verdict favorable (2 fiches)** : `trente-neuf-rose-classique-cannelee` et `trente-neuf-classique-cannelee` (mère active). Ces deux handles figurent nommément dans la liste des **4 fiches écartées** que la consigne m'interdit de toucher. Je n'ai pas voulu trancher moi-même entre deux consignes contradictoires : leurs faces v3 sont mesurées, validées, prêtes, et il te suffit d'un mot pour que je les branche. Elles gardent pour l'instant leur face « SWISS MADE ».

Fichiers prêts : `scratchpad/noirmont-galeries/faces-steriles-v3/trente-neuf-rose-classique-cannelee-01-face.jpg` et `…/trente-neuf-classique-cannelee-01-face.jpg`.

Remarque mineure sur la face v3 de la mère : son guichet affiche **23** là où les 5 sœurs affichent 28. Sans conséquence, mais c'est une petite dissonance de famille si tu la branches.

## 3. Les 29 accessoires — complètes, partielles, écartées

Contrôle sur planches à **740 px par vignette** (`scratchpad/qa-hd/`), recadrages dédiés jusqu'à ×16 sur chaque cadran, chaque main et chaque mécanisme.

**Règle appliquée, à retenir :** le défaut dominant ne touche pas le produit vendu mais **le décor** — les montres qui garnissent un coffret, un rouleau ou une vitrine, le mouvement posé près d'une loupe. Le prompt de génération exigeait des cadrans stériles ; il a été appliqué au produit et pas au décor. Seuil retenu : un **fantôme faible sur un cadran de décor minuscule** est le rendu de base du modèle et reste acceptable (les faces déjà publiées portent les mêmes marques faibles) ; un **texte structuré et lisible sur un cadran de 90 px ou plus** est un rejet.

### Fiches complètes — 14

Tous les slots produits par Codex sont branchés.

| handle | médias après | slots ajoutés |
|---|---:|---|
| `loupe-de-date-saphir` | 3 | situation + macro |
| `outil-de-mise-a-taille-de-bracelet` | 3 | situation + macro |
| `remontoir-bois-ebene` | 3 | situation + macro |
| `remontoir-bois-noir-laque` | 3 | situation + macro |
| `remontoir-bois-noyer` | 3 | situation + macro |
| `bracelet-presidentiel-904l` | 3 | situation + macro |
| `bracelet-presidentiel-dore` | 11 | situation + macro |
| `coussins-de-presentation-lot-de-10` | 3 | situation + macro |
| `kit-d-entretien-13-pieces` | 3 | situation + macro |
| `loupe-d-horloger` | 3 | situation + macro |
| `set-tournevis-horloger` | 8 | situation + macro |
| `coffret-6-montres-couvercle-verre` | 3 | macro (Codex n'a pas produit de situation) |
| `etui-de-voyage-rigide` | 3 | macro (Codex n'a pas produit de situation) |
| `remontoir-collection-bois-led-noir` | 3 | situation + macro |

Sur `bracelet-presidentiel-dore` et `set-tournevis-horloger`, les images de variante ont été repoussées derrière la situation et la macro, conformément à l'ordre retenu. Sur `coffret-6-montres` et `etui-de-voyage-rigide`, la deuxième photo produit d'origine (ouvert) reste en position 2 et la macro s'ajoute en 3 — la face est en position 1 dans les deux cas.

Signalé sans être bloquant : le `03-macro` de `loupe-de-date-saphir` est un très gros plan du seul bourrelet de base, sans élément optique identifiable. Conforme, mais peu informative — candidate à une reprise ultérieure.

### Fiches partielles — 14

Branchées **sans leur mise en situation**, qui est fautive. La fiche gagne ses images ; il ne manque qu'une situation. Les images fautives n'ont **pas** été branchées, **pas** régénérées, et les fichiers restent intacts dans `generated/`.

| handle | branché | situation non branchée — raison |
|---|---|---|
| `remontoir-bois-acajou` | macro | lettrage de marque sur le cadran de la montre du décor, deux blocs typographiques au-dessus de l'axe des aiguilles, lisible dès ×8 |
| `pince-a-barrettes` | macro | mécanisme invraisemblable : manchon rectangulaire enserrant les deux mors, absent de la face, qui interdirait l'ouverture ; téton hexagonal ne se rattachant à rien |
| `coffret-douze-aluminium` | macro | lettrage de marque sur **huit** cadrans du décor + forme de logo en couronne sur le chronographe, visible dès ×5 |
| `coffret-douze-presentation` | macro | bande de caractères sous l'index de 12 h sur au moins six cadrans, nette à ×20 |
| `doigtiers-d-horloger-latex` | macro | ligne de 6 à 8 glyphes gravés sur la platine du mouvement, en arc autour du balancier |
| `rouleau-de-voyage-bleu-marine-cuir` | macro | logo en couronne et lignes de texte sur les cadrans des montres rangées, lisibles dès ×8 |
| `rouleau-de-voyage-brun-cuir` | macro | idem |
| `rouleau-de-voyage-noir-cuir` | macro | idem |
| `remontoir-collection-cuir-pu` | situation | `03-macro` rejeté : cartouche fantôme à deux lignes sous 12 h, lisible à ×16 — **3,44×** l'énergie des témoins du même cadran (amplitude 26 niveaux de gris contre 2) |
| `remontoir-collection-bois-noir` | situation | `03-macro` rejeté : lettrage sombre **sur le rehaut à 6 h**, de part et d'autre de l'index, le mot de gauche se lit « Swiss ». **4,16×**, amplitude 75 contre 29. Le champ du cadran est propre : le défaut se cache **hors du cadran**, à r ≈ 1,13 R — un balayage limité au cadran le rate |
| `remontoir-collection-bois-led-rouge` | situation | `03-macro` rejeté, **le plus grave du lot** : cartouche de marque **7,14×** et ligne d'origine **5,59×**, chiffres « 12 » et « 6 » lisibles, texte lu directement à ×18 |
| `remontoir-collection-bois-beige` | macro | `02-situation` rejetée pour **artefact structurel** : une seconde paire de charnières sur le chant libre de la porte et un bouton dédoublé — une porte à charnières des deux côtés ne s'ouvre pas. Son cadran de décor porte en outre un cartouche fantôme mesuré à 3,5-6,2× sur 4 des 8 cadrans |
| `remontoir-solo` | macro | `02-situation` rejetée : cartouche à deux lignes sur un cadran de grande taille. **Mesure discordante** : un second contrôle la donne à 1,30× / 1,61× seulement, donc sous le seuil ; devant le désaccord j'ai retenu l'option prudente et ne l'ai pas branchée |
| `remontoir-vitrine` | macro | `02-situation` rejetée : impression clair-sur-sombre **lisible dès ×9** sur les 4 cadrans, même position relative — ligne sous 12 h, mot vers 3 h, mention vers 6 h. Mesuré 3,18× à 4,50× |

### Le seuil de décision, et les trois images branchées qui restent à la limite

La détection a été **mesurée**, pas jugée à l'œil : énergie passe-haut dans la zone suspecte divisée par la médiane de 3 à 4 zones témoins **vierges prises au même rayon sur le même cadran de la même image**. Seuil de détection : **3×**. Deux ancrages étalonnent l'échelle — une zone lue propre à ×20 donne **1,04×**, un cartouche dont le texte se lit à ×18 donne **7,14×**.

Ce garde-fou a évité deux faux positifs : le macro de `led-noir` a d'abord mesuré 9,51× puis 4,98× — c'étaient les **aiguilles** qui traversaient la boîte de mesure, et un étirement de contraste ×20 a montré un champ parfaitement propre.

**Trois mises en situation branchées sont détectées mais restent au palier acceptable** : `remontoir-collection-bois-led-noir` (4,54× sur un cadran, 1,2-2,9× sur les autres), `remontoir-collection-bois-led-rouge` (3,7× à 5,2× sur 4 des 8 cadrans), `remontoir-collection-cuir-pu` (2 cadrans sur 8 au-dessus du seuil). Leurs cadrans de décor mesurent **une soixantaine de pixels** : la marque est détectable à la mesure mais **aucun mot n'y est lisible**, et le même niveau se retrouve sur des faces déjà publiées du catalogue. Je les ai branchées à ce titre et je les consigne ici — c'est la limite connue, pas une régression. À l'inverse, `remontoir-vitrine` 02 (lisible dès ×9) et les trois macros à texte lu à ×13-×18 ont été rejetés.

`remontoir-solo` 02-situation est le seul cas de **désaccord de mesure** : un contrôle y lit un cartouche à deux lignes sur un cadran de grande taille, un autre le mesure à 1,30× / 1,61×, sous le seuil. Devant le désaccord je ne l'ai pas branchée ; sa carte passe-haut montre des amas vaguement glyphiques sous 12 h et vers 6 h. Un œil humain trancherait en dix secondes.

Deux observations connexes, qui ne sont pas des motifs d'exclusion et que je n'ai pas traitées :
- **Le côté des charnières est inversé.** Les faces publiées des 5 meubles articulent la porte à **droite** (bouton de fermeture à gauche) ; les 5 mises en situation l'articulent à **gauche**, alors que la caméra est du même côté. C'est un écart réel mais une porte à gauche n'est pas un mécanisme impossible.
- **La situation de `remontoir-vitrine` ajoute 4 montres** là où la face publiée montre des coussins vides. Changement de mise en scène, pas un défaut.

### Fiche écartée entièrement — 1

| handle | raison |
|---|---|
| `rouleau-de-voyage-vert-cuir` | `02-situation` porte le même défaut de décor que ses trois sœurs, **et** son `03-macro` montre une couture tressée grossière et irrégulière là où la face en ligne et les trois autres coloris ont un point sellier droit et fin. Aucun slot branché. |

### Contrôle rétroactif des 8 accessoires bracelet déjà en ligne — **rien à retirer**

Puisque le défaut porte sur le décor, les 8 mises en situation d'accessoires bracelet branchées lors de la première passe devenaient suspectes par défaut : un bracelet est presque toujours photographié avec une montre. Elles ont donc été recontrôlées.

- **3 images ne montrent aucun cadran** : `bracelet-acier-massif-12-22-mm`, `bracelet-fkm-courbe`, `bracelet-jubile-acier-904l-20mm` — la montre y est vue de dos, fond de boîte.
- **5 images montrent un cadran**, mesuré au même protocole (énergie passe-haut zone / témoins du même cadran) :

| handle | rapport 12 h | rapport 6 h | verdict |
|---|---:|---:|---|
| `bracelet-caoutchouc-gaufre` | 0,24× | 0,67× | stérile |
| `bracelet-cuir-daim-degagement-rapide` | 0,81× | 0,71× | stérile |
| `bracelet-jubile-embouts-courbes` | 1,03× | 0,92× | stérile |
| `bracelet-milanais-maille-italienne` | 1,59× | 1,10× | stérile |
| `barrettes-de-rechange-270` | cadran noir lu à ×3 | — | stérile (index bâtons et aiguilles seuls) |

Tous très en dessous du seuil de 3×. La main visible sur `barrettes-de-rechange-270` a aussi été contrôlée : pouce et index, anatomie correcte, prise cohérente sur la barrette. **Aucune image de la première passe n'est à retirer.**

## 4. `remontoir-solo` — régénération de façade **annulée, 0 crédit dépensé**

La façade métallique de la face publiée porte bien un mot gravé lisible, approximativement « **FLOTOWI** » (marque inventée), avec juste au-dessus une tache de flou qui trahit une retouche antérieure. Mais le contrôle des images générées montre que **ce lettrage n'est pas reproduit** : volet rabattu sur la situation, hors cadre sur la macro. La régénération perdait donc son urgence et les 15 crédits n'ont pas été engagés.

**La face publiée reste fautive** — c'est un arbitrage pour toi, pas une dépense à engager cette nuit. Rappel de qualification : c'est une **marque inventée sur le produit**, pas une mention d'origine ; le risque est de charte et de crédibilité, pas d'allégation d'origine fausse.

## 5. Constat établi sans rien corriger : des images qui promettent plus que le produit

Relevé par l'API sur les valeurs d'option **réellement en vente**, et comptage des emplacements sur les faces déjà publiées. Aucune écriture produit sur ce point — c'est un constat, la décision te revient.

### Rouleaux de voyage — 4 fiches, toutes en écart

Option unique `Capacité`, exactement trois valeurs : `1 montre`, `2 montres`, `3 montres`. **Aucune variante à 4 emplacements n'existe.** Les 4 faces publiées montrent **4 niches** (même rendu recoloré : bornes de niches identiques au pixel près entre coloris, confirmé par profil de luminance). La description dit déjà la vérité — « Existe pour 1, 2 ou 3 montres », « un logement par montre ». **C'est l'image seule qui sur-promet, d'un logement, sur les quatre fiches.**

### Meubles remontoirs — 5 fiches, toutes en écart

| handle | capacités en vente (valeurs API) | max vendu | emplacements sur la face | écart |
|---|---|---:|---:|---|
| `remontoir-collection-bois-beige` | 1, 2, 4, 6 montres | 6 | 8 | +2 |
| `remontoir-collection-bois-noir` | 1, 2, 4, 6 montres | 6 | 8 | +2 |
| `remontoir-collection-cuir-pu` | 2, 4, 6 montres | 6 | 8 | +2 |
| `remontoir-collection-bois-led-noir` | 2, 4 montres | 4 | 8 | **×2** |
| `remontoir-collection-bois-led-rouge` | 2, 4 montres | 4 | 8 | **×2** |

Les 8 emplacements sont 4 étagères × 2 remontoirs. L'hypothèse du reflet est écartée : sur chaque étagère les deux coussins sont des objets distincts (montres différentes, cerclages propres, un bouton/bandeau LED centré entre les deux). Là encore, chaque `descriptionHtml` annonce déjà la vraie capacité — seule l'image sur-promet. **Le cas le plus grave est celui des deux fiches LED, où l'image montre exactement le double de ce qui est achetable.**

Observations secondaires du même relevé, non instruites : le côté des charnières s'inverse entre face et situation sur les 5 meubles, de façon cohérente (probablement voulu pour dégager l'intérieur) ; et la face de `remontoir-collection-bois-led-rouge` montre un meuble acajou à intérieur doré alors que sa description dit « intérieur rouge » — le rouge est sur l'extérieur.

## 6. Contrôle final de la seconde passe

- **Comptage** : les 31 fiches touchées ont été relues en direct. Chaque compteur correspond à l'attendu (état d'origine + le nombre exact de fichiers neufs). Aucun doublon : chaque média branché est un fichier uploadé une seule fois.
- **Ordre** : vérifié en direct sur les 31 fiches touchées. Face en position 1 partout, puis `situation` → `macro` (→ `poignet` pour les montres), médias hérités et images de variante repoussés derrière. Les 3 anciennes faces « SWISS MADE » substituées sont en dernière position, intactes.
- **Chaîne technique** : `stagedUploadsCreate` (PUT, IMAGE) → `curl -T` avec `content-type: image/jpeg` (**43 × HTTP 200**) → `productCreateMedia` avec le `resourceUrl` non signé → `productReorderMedia`. Tous les retours `mediaUserErrors` sont vides.
- **Rapprochement** : fait **par `handle`** exclusivement. Aucun rapprochement par identifiant de variante ou de média.
- **Rendu sur le thème brouillon** : toujours **non vérifiable**. Le storefront répond 302 et le mot de passe ne passe pas. Conformément à la consigne, je n'ai pas insisté. À refaire par toi depuis un navigateur connecté à l'admin.

## 7. Interdits respectés

Aucun SKU, prix, titre, option, variante, statut ni mapping DSers touché. Aucune suppression de média, de fichier ni de donnée. Les **7 mères en brouillon**, **Noirmont Deux**, les **3 GMT « siglé »** et les **4 fiches écartées** n'ont reçu aucune écriture. Aucun fichier de thème modifié. Aucune commande. **0 crédit Higgsfield dépensé** (solde inchangé à ~275). Toutes les écritures sont des `productCreateMedia` / `productReorderMedia`.

---

## ⏳ CE QUI ATTEND HAKIM — liste unique et complète

**Décisions irréversibles, que je refuse de prendre à ta place**

1. **Supprimer ou non les 4 images « détails et finitions » à texte incrusté** sur les mères actives (`trente-six-classique-jubile` 59680093962578, `quarante-et-un-sport-acier` 59680004407634, `trente-neuf-duo-classique-bicolore` 59680094159186, `noirmont-un-plongeuse-acier` 59680093405522). Ces médias ne sont partagés avec aucune autre fiche : `productDeleteMedia` les détruirait définitivement. Remplaçantes déjà en ligne et bien placées, sauvegardes en place. Une commande.
2. **Supprimer ou non les 3 anciennes faces « SWISS MADE »** désormais en dernière position de `trente-neuf-bleu`, `trente-neuf-rouge`, `trente-neuf-vert`. Copies locales dans `boutique-seiko-mod/backups/backup-faces-swissmade-2026-07-26/`. Une commande.

**Un mot de toi et c'est fait dans la minute**

3. **Lever ou non l'interdiction sur `trente-neuf-rose-classique-cannelee` et `trente-neuf-classique-cannelee`** pour brancher leurs faces stériles v3, mesurées et validées sur les deux axes. Sans ce feu vert, ces deux fiches gardent leur « SWISS MADE » en position 1 — c'est le dernier reliquat du problème.
4. **Lever ou non l'exclusion de `noirmont-deux-plongeuse-ceramique`** : ses 3 images de galerie sont prêtes dans `excluded/`, et sa face porte elle aussi un fragment de lettrage à 6 h.

**Arbitrages de fond, plus lourds**

5. **Les images qui promettent plus que le produit** — 4 rouleaux (4 niches montrées, 3 max vendues) et 5 meubles remontoirs (8 emplacements montrés, 4 ou 6 max vendus). Ce n'est pas un défaut de génération : ces faces sont **déjà en ligne**. Un client qui reçoit moins que ce qu'il a vu a un motif de retour légitime. Options : nouvelle face conforme, ou ajustement de l'offre.
6. **La face de `remontoir-solo`**, qui porte la marque inventée « FLOTOWI » gravée dans le métal. Régénération non lancée, 0 crédit engagé, en attente de ton feu vert.
7. **Les 15 images fautives** (14 fiches partielles + `rouleau-de-voyage-vert-cuir`) : elles demandent une reprise avec un prompt corrigé, qui interdise explicitement toute inscription **sur le décor comme sur le produit** — c'est le trou du prompt actuel. À demander à Codex.
8. **Les 4 fiches écartées de la première passe** (`integrale-vert-sport-chic-acier`, `bracelet-fkm-tropical`, plus les deux `trente-neuf` du point 3) : régénération ciblée des slots fautifs.
9. **Le macro de `rouleau-de-voyage-vert-cuir`** (couture tressée incohérente avec la famille) et celui de `loupe-de-date-saphir` (peu informatif) : reprises souhaitables, non bloquantes.

**Limites connues, consignées et non corrigées cette nuit**

10. Les **fantômes de lettrage faibles sur les cadrans de décor minuscules** sont le rendu de base du modèle et sont présents aussi sur des faces déjà publiées. Ne pas les traiter comme une régression ; à revoir seulement si le standard « 100 % photo sans texte » doit s'appliquer au décor.
11. Les **larges taches de flou** relevées sur 6 cadrans du catalogue (lettrage masqué plutôt que retiré) restent en ligne. Conformes au standard, visibles comme défaut d'image.
12. **Trois mises en situation de meubles remontoirs** (`led-noir`, `led-rouge`, `cuir-pu`) portent une marque **détectable à la mesure mais illisible** sur des cadrans de décor d'une soixantaine de pixels. Branchées à ce titre, consignées ici. Voir le détail du seuil plus haut.
13. **`remontoir-solo` 02-situation** reste non branchée sur un **désaccord de mesure** entre deux contrôles. Dix secondes de ton œil suffiraient à trancher.
14. **Le rendu sur le thème brouillon n'a jamais pu être vérifié** : le mot de passe storefront ne passe pas. À faire par toi depuis un navigateur connecté.
