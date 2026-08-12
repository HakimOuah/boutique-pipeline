# Audit visuel du catalogue — Maison Noirmont

Date : 26 juillet 2026 · Boutique `v42pzp-h4` / maisonnoirmont.fr
**Version 3** — standard arbitré par Hakim le 26/07 : galeries **100 % photographiques**, aucune carte typographique, ajout du **porté-poignet**. Conventions de nommage et exclusions alignées sur `2026-07-31-prompt-codex-galeries.md`.

> **Ce document est la feuille de route de Codex.** Le prompt l'y renvoie explicitement : Codex ne produit que ce qui figure ici.
>
> **Aucune écriture n'a été faite sur la boutique.** Le volet de récupération des médias immobilisés a été instruit puis **arrêté au contrôle visuel** — voir §1, c'est le résultat le plus important de cette passe.

---

## 0. Résumé exécutif

| Indicateur | Valeur |
|---|---:|
| Fiches au catalogue | **99** — 92 actives, 7 brouillons, 0 archivée |
| Médias au total | **283** — 203 sur fiches actives, 80 sur les brouillons |
| Médias récupérés depuis les mères | **0** — voir §1 |
| Fiches actives conformes au nouveau standard | **0** sur 92 |
| Fiches à traiter | **90** |
| **Générations à produire** | **230** |
| Cartes composées par code | **0** — supprimées du standard |
| Faces sources à exporter avant lancement | **36** |
| Budget crédits estimé | ≈ **1 585** (1 219 nominal + 30 % de dépassement constaté) |

### Ce qui change par rapport à la version 1

| | v1 — 7 slots + cartes | v3 — 100 % photo |
|---|---:|---:|
| Fichiers à produire | 390 | **230** |
| dont générations | 215 | **230** |
| dont cartes par code | 175 | **0** |
| Crédits réels | ≈ 1 480 | ≈ **1 585** |
| Script de composition perdu | bloquant | **sans objet** |

Le nombre de fichiers baisse de 41 %, mais le budget crédits monte légèrement : les cartes supprimées étaient gratuites, et le **porté-poignet ajoute 52 générations** qui n'existaient nulle part. Le gain n'est donc pas budgétaire, il est opérationnel — plus de script Pillow à réécrire, plus de polices, plus de citations à sourcer, plus d'arbitrage typographique, et le problème de conformité des avis inventés sort des galeries.

### Méthode d'inventaire — le piège de la pagination a été traité

Les connexions média sont plafonnées à 30. L'inventaire a été construit en demandant explicitement `media(first: 30)` **avec `pageInfo { hasNextPage }` sur chaque produit** : aucune fiche ne dépasse 30 médias (maximum observé 27, sur `contre-la-montre-chronographe-panda`), donc `hasNextPage` est `false` partout et rien n'a été tronqué. La pagination produit a été menée en 2 pages de 50 jusqu'à `hasNextPage: false`.

Contrôle : la somme des `mediaCount.count` des 99 fiches vaut **283**, la somme des nœuds média retournés vaut également **283**. Les deux concordent.

> ⚠️ **Correction d'un chiffre du brief initial.** Il annonçait « ~105 fiches actives ». Le comptage réel donne **92 actives** (`productsCount(query:"status:active")` = 92) sur 99 fiches. Les 7 mères en brouillon sont bien 7.

---

## 1. ⛔ Volet « récupération des 80 médias » — instruit, puis arrêté au contrôle

### La consigne

Rattacher aux fiches filles les galeries immobilisées sur les mères en brouillon, pour les 6 mères dont la variante restante est le doublon exact d'une fille — **avec vérification image par image du coloris avant tout rattachement**.

### Le résultat : 0 média rattaché, 0 écriture

**Le contrôle visuel a échoué sur 6 mères sur 6.** Le SKU correspond bien à une fille, mais **l'image ne correspond pas au produit**. Les galeries mères ont été produites *avant* le découpage, depuis les photos fournisseur d'origine — jamais depuis les faces recolorisées des filles. Le SKU n'est donc pas une preuve d'identité visuelle, et c'est exactement le piège que le contrôle image par image devait attraper.

| Mère | Variante restante | Fille visée | Ce que l'image montre réellement | Verdict |
|---|---|---|---|---|
| `contre-la-montre-chronographe-panda` | `14:200000914#M14` « Argent · caoutchouc noir » | `contre-la-montre-argent-chronographe` | cadran **crème panda**, compteurs **noirs**, **bracelet acier**, fond sable | ✗ la fille est cadran **argent**, compteurs **gris**, **caoutchouc noir**, fond craie |
| `integrale-sport-chic-acier` | `14:175#6;…` « Vert » | `integrale-vert-sport-chic-acier` | cadran **bleu** tapisserie, **faux logo flouté à 12 h**, fond sable | ✗ la fille est cadran **vert**, stérile, fond craie |
| `heritage-plongeuse-vintage-42` | `14:200000080#S1;…` « Bleu · lunette bleue » | `heritage-bleu-plongeuse-vintage-42` | cadran **noir**, lunette **noire**, **trace de logo effacé** | ✗ la fille est cadran **bleu**, lunette **bleue** |
| `remontoir-bois` | `14:193#M11011` « Noir laqué » | `remontoir-bois-noir-laque` | coffret **noyer**, **trace de logo effacé** sur le coussin | ✗ la fille est **noir laqué** |
| `rouleau-de-voyage-cuir` | `14:496#WB33` « Cuir bleu marine · 3 montres » | `rouleau-de-voyage-bleu-marine-cuir` | rouleau **cuir brun**, **4 emplacements**, fond sombre | ✗ mauvaise couleur **et** mauvaise capacité |
| `remontoir-collection` | `14:200000080#IB-red-04C` « Bois LED · rouge · 4 montres » | `remontoir-collection-bois-led-rouge` | **vitrine bois 8 rotors**, sans LED, sans rouge | ✗ produit différent |
| `voyageur-gmt-automatique` | 12 variantes, **toutes « siglé »** | — | — | hors périmètre : aucune fille en doublon |

### Trois défauts rédhibitoires, au-delà du coloris

1. **Faux logos.** Les visuels Intégrale, Héritage et Remontoir Bois portent des **traces de logo de marque tierce floutées ou effacées**. C'est le défaut que ce chantier existe pour éliminer : les rattacher le réintroduirait sur des fiches actives et vendues.
2. **Texte incrusté.** Les images « détails et finitions » ne sont pas des photos pures : elles portent un **cartouche typographique brûlé dans l'image** (`Poussoirs chrono · 39 mm`, `36 mm · Maillons acier`). Inutilisables sous un standard 100 % photographique.
3. **Direction artistique différente.** Les galeries mères sont sur fonds **sable, lin, travertin, brun sombre**. Les faces des filles sont sur **craie / pierre**. Les mélanger produirait précisément le « saut » que Hakim veut supprimer.

### Conséquence majeure sur le porté-poignet

**Aucune image du catalogue ne montre une montre au poignet.** Les sept visuels étiquetés « portée » sont des **mises en situation à plat** — montre posée sur une pierre près de gants de cuir, sur un lin roulé près d'un bois flotté, sur une serviette à côté d'un café. Vérifié sur Contre-la-montre, Intégrale, Héritage et Trente-Six.

Le `poignet` est donc **un slot entièrement neuf, à produire 52 fois**. C'est le poste le plus lourd et le plus risqué du chantier.

### Ce qui reste éventuellement récupérable

Les mises en situation des **5 mères actives à traiter** sont déjà sur leur propre fiche, montrent leur propre coloris, et celle de Trente-Six a été vérifiée **stérile**. Elles peuvent servir de `situation` **sans aucun déplacement**.

⚠️ Contrôle individuel obligatoire avant de les compter : deux des quatre mères en brouillon avaient un faux logo sur ce même slot. Le chiffrage ci-dessous les compte **comme absentes**, par prudence. Si les 5 passent, **5 générations en moins**.

---

## 2. Le standard

Conforme à `2026-07-31-prompt-codex-galeries.md`.

### Montres — 4 images, toutes photographiques

| Slot | Fichier | Contenu |
|---|---|---|
| `face` | `<handle>-face.jpg` | Produit seul, de face, centré, fond minéral clair. **Existe partout.** |
| `situation` | `<handle>-situation.jpg` | Le produit posé dans un décor sobre qui suggère l'usage. |
| `macro` | `<handle>-macro.jpg` | Détail rapproché : cannelure de lunette, maillon, boucle, texture de cadran. **Aucun texte incrusté.** |
| `poignet` | `<handle>-poignet.jpg` | **La montre portée.** Slot à risque, cadrage imposé par le prompt. |

### Accessoires — 3 images

| Slot | Fichier | Contenu |
|---|---|---|
| `face` | `<handle>-face.jpg` | Produit seul. **Existe partout.** |
| `situation` | `<handle>-situation.jpg` | L'objet en usage réel : bracelet monté sur une montre, remontoir garni, rouleau ouvert, outil en main. |
| `macro` | `<handle>-macro.jpg` | Grain du cuir, brossage de l'acier, moletage d'un manche. |

Pas de `poignet` sur les accessoires : le bracelet est déjà couvert par `situation`, et un porté sur un doigtier ou une pince à barrettes n'a aucun sens.

### Ce qui disparaît

Plus de carte de caractéristique, plus de carte de preuve sociale, plus de carte de témoignage.

### Direction artistique — inchangée

Fond minéral clair, dégradé **pierre `#E7E4DE` → craie `#FAFAF7`**, lumière douce latérale, ombre portée diffuse, carré **2048 × 2048**, JPEG q90. Le slot `situation` peut introduire un décor, à condition de rester dans cette palette minérale claire.

**Étoiles : vert Trustpilot `#05b67a` — tranché par Hakim, la charte laiton cède.** Sans cartes, cela ne concerne plus que les badges du thème et les blocs d'avis.

---

## 3. Inventaire et manques, fiche par fiche

Chaque fiche montre doit produire `situation`, `macro`, `poignet`. Chaque accessoire doit produire `situation`, `macro`.

### 3.1 Montres — 52 fiches à traiter, 156 générations

**Contre-la-montre — Chronographe · 12 fiches · 36 générations**
État : 1 à 3 faces de coloris + 1 carte témoignage héritée.
`contre-la-montre-argent-chronographe` · `contre-la-montre-blanc-chronographe` · `contre-la-montre-bleu-glacier-chronographe` · `contre-la-montre-champagne-chronographe` · `contre-la-montre-compteurs-bleus-chronographe` · `contre-la-montre-gris-anthracite-chronographe` · `contre-la-montre-noir-chronographe` · `contre-la-montre-panda-inverse-chronographe` · `contre-la-montre-panda-chronographe` · `contre-la-montre-rose-poudre-chronographe` · `contre-la-montre-turquoise-chronographe` · `contre-la-montre-vert-chronographe`

**Héritage — Plongeuse vintage 42 · 3 fiches · 9 générations**
État : face + carte témoignage héritée.
`heritage-bleu-nuit-plongeuse-vintage-42` · `heritage-bleu-plongeuse-vintage-42` · `heritage-vert-plongeuse-vintage-42`

**Intégrale — Sport chic acier · 7 fiches · 21 générations**
État : face + carte témoignage héritée.
`integrale-blanc-argente-sport-chic-acier` · `integrale-bleu-ciel-sport-chic-acier` · `integrale-bleu-nuit-sport-chic-acier` · `integrale-brun-or-rose-sport-chic` · `integrale-noir-sport-chic-acier` · `integrale-turquoise-sport-chic-acier` · `integrale-vert-sport-chic-acier`

**Voyageur — GMT automatique · 6 fiches · 18 générations**
État : face + carte témoignage héritée. **Aucune fiche active n'est « siglé »** — les 3 déclinaisons interdites sont restées en variantes invendables sur la mère en brouillon, l'exclusion est donc sans objet ici.
`voyageur-bicolore-cadran-brun-gmt` · `voyageur-bicolore-gmt-3-maillons` · `voyageur-bicolore-gmt-5-maillons` · `voyageur-or-rose-gmt-5-maillons` · `voyageur-or-gmt-3-maillons` · `voyageur-or-gmt-president`

**Trente-Six — Classique jubilé · 6 fiches · 18 générations**
Filles : face nue uniquement. Mère active : galerie de 7 dont 3 cartes et une macro à texte incrusté.
`trente-six-bleu-classique-jubile` · `trente-six-dore-classique-jubile` · `trente-six-or-integral-classique-jubile` · `trente-six-rose-classique-jubile` · `trente-six-rouge-classique-jubile` · `trente-six-classique-jubile` *(mère active)*

**Trente-Neuf — Classique cannelée · 7 fiches · 21 générations**
`trente-neuf-bleu-mer-classique-cannelee` · `trente-neuf-bleu-classique-cannelee` · `trente-neuf-noir-classique-cannelee` · `trente-neuf-rose-classique-cannelee` · `trente-neuf-rouge-classique-cannelee` · `trente-neuf-vert-classique-cannelee` · `trente-neuf-classique-cannelee` *(mère active)*

**Quarante-et-Un — Sport acier · 7 fiches · 21 générations**
`quarante-et-un-blanc-cuir-sport-acier` · `quarante-et-un-bleu-acier-sport-acier` · `quarante-et-un-bleu-cuir-sport-acier` · `quarante-et-un-noir-jaune-acier-sport-acier` · `quarante-et-un-noir-acier-sport-acier` · `quarante-et-un-noir-cuir-sport-acier` · `quarante-et-un-sport-acier` *(mère active)*

**Trente-Neuf Duo — Classique bicolore · 2 fiches · 6 générations**
`trente-neuf-duo-dore-classique-bicolore` · `trente-neuf-duo-classique-bicolore` *(mère active)*

**Noirmont Un — Plongeuse acier · 2 fiches · 6 générations**
`noirmont-un-bronze-plongeuse` · `noirmont-un-plongeuse-acier` *(mère active)*

### 3.2 Accessoires — 38 fiches, 74 générations

**36 fiches · 2 générations chacune (`situation` + `macro`) · 72**
`barrettes-de-rechange-270` · `bracelet-acier-massif-12-22-mm` · `bracelet-caoutchouc-gaufre` · `bracelet-cuir-daim-degagement-rapide` · `bracelet-fkm-courbe` · `bracelet-fkm-tropical` · `bracelet-jubile-acier-904l-20mm` · `bracelet-jubile-embouts-courbes` · `bracelet-milanais-maille-italienne` · `bracelet-presidentiel-904l` · `bracelet-presidentiel-dore` · `coffret-douze-aluminium` · `coffret-douze-presentation` · `coussins-de-presentation-lot-de-10` · `doigtiers-d-horloger-latex` · `kit-d-entretien-13-pieces` · `loupe-d-horloger` · `loupe-de-date-saphir` · `outil-de-mise-a-taille-de-bracelet` · `pince-a-barrettes` · `remontoir-bois-acajou` · `remontoir-bois-ebene` · `remontoir-bois-noir-laque` · `remontoir-bois-noyer` · `remontoir-collection-bois-beige` · `remontoir-collection-bois-led-noir` · `remontoir-collection-bois-led-rouge` · `remontoir-collection-bois-noir` · `remontoir-collection-cuir-pu` · `remontoir-solo` · `remontoir-vitrine` · `rouleau-de-voyage-bleu-marine-cuir` · `rouleau-de-voyage-brun-cuir` · `rouleau-de-voyage-noir-cuir` · `rouleau-de-voyage-vert-cuir` · `set-tournevis-horloger`

**2 fiches · 1 génération chacune (`macro` seulement) · 2**
`coffret-6-montres-couvercle-verre` et `etui-de-voyage-rigide` — leur photo « ouvert » existante tient lieu de `situation`.

### 3.3 Fiches actives exclues du chantier — 2

| Handle | Raison |
|---|---|
| `noirmont-deux-plongeuse-ceramique` | Exclue par le prompt : ses 7 références n'ont jamais pu être identifiées, le fournisseur utilisant la même photo pour toutes. **Ne rien produire, ne rien deviner.** ⚠️ Elle conservera donc sa galerie héritée de 7 images, cartes comprises — c'est un trou de cohérence assumé, à signaler à Hakim. |
| `carte-cadeau-maison-noirmont` | Produit numérique, visuel unique déjà conforme. |

### 3.4 Les 7 mères en brouillon — signalées, non traitées

| Handle | Médias immobilisés |
|---|---:|
| `contre-la-montre-chronographe-panda` | 27 |
| `integrale-sport-chic-acier` | 14 |
| `voyageur-gmt-automatique` | 13 |
| `heritage-plongeuse-vintage-42` | 10 |
| `remontoir-collection` | 6 |
| `remontoir-bois` | 5 |
| `rouleau-de-voyage-cuir` | 5 |

**80 médias, dont 0 récupérable** (§1). Le plus honnête est de les considérer comme perdus et de ne plus compter dessus.

---

## 4. Chiffrage

| Bloc | Fiches | Générations |
|---|---:|---:|
| Montres | 52 | **156** |
| Accessoires | 38 | **74** |
| **Total** | **90** | **230** |

| | |
|---|---:|
| Cartes par code | **0** |
| Fichiers à produire | **230** |
| Emplacements de galerie servis | 322 (52 × 4 + 38 × 3) |
| Crédits nominaux (230 × 5,3) | ≈ 1 219 |
| **Crédits réels (+30 % constaté)** | ≈ **1 585** |

**Option d'économie :** si les 5 mises en situation des mères actives passent le contrôle de stérilité, **225 générations** (≈ 1 551 crédits).

### Où part le budget

| Slot | Générations | Part |
|---|---:|---:|
| `poignet` — montres | 52 | 23 % |
| `situation` — montres | 52 | 23 % |
| `macro` — montres | 52 | 23 % |
| `macro` — accessoires | 38 | 16 % |
| `situation` — accessoires | 36 | 15 % |

Le porté-poignet pèse près d'un quart du budget **et la totalité du risque technique**. C'est là qu'il faut concentrer le contrôle.

---

## 5. Faces sources à exporter avant lancement — bloquant

Codex n'a pas le droit de se connecter à Shopify. Les **90 faces sources** doivent être en local dans `entrees-faces/`, nommées `<handle>-face.jpg`.

| Origine | Fiches | État |
|---|---:|---|
| `boutique-seiko-mod/livraisons/visuels-2026-07-25/generated/` | 41 | ✅ disponible |
| `boutique-pipeline/scratchpad/noirmont-accessoires-img/` | 13 | ✅ disponible |
| **À exporter depuis le CDN** | **36** | ❌ **bloquant** |

> ⚠️ **36, et non 31.** Le chiffre de 31 qui figure dans le prompt vient de la version 1 de cet audit (19 montres filles + 12 accessoires). Sous le nouveau standard, les **5 mères actives à traiter** ne sont plus conformes — leur macro porte un texte incrusté et aucune n'a de porté-poignet — elles entrent donc dans le chantier et **leur face doit être exportée aussi**. C'est ce document qui fait foi : **36**.

Préfixe CDN : `https://cdn.shopify.com/s/files/1/1094/1893/8706/files/`

### 19 faces de montres filles

| Handle | Fichier CDN |
|---|---|
| `trente-six-bleu-classique-jubile` | `10977448690002-var-bleu.jpg` |
| `trente-six-dore-classique-jubile` | `10977448690002-var-dore.jpg` |
| `trente-six-or-integral-classique-jubile` | `10977448690002-var-or-integral.jpg` |
| `trente-six-rose-classique-jubile` | `10977448690002-var-rose.jpg` |
| `trente-six-rouge-classique-jubile` | `10977448690002-var-rouge.jpg` |
| `trente-neuf-bleu-mer-classique-cannelee` | `10977444430162-var-bleu-mer.jpg` |
| `trente-neuf-bleu-classique-cannelee` | `10977444430162-var-bleu.jpg` |
| `trente-neuf-noir-classique-cannelee` | `10977444430162-var-noir.jpg` |
| `trente-neuf-rose-classique-cannelee` | `10977444430162-var-rose.jpg` |
| `trente-neuf-rouge-classique-cannelee` | `10977444430162-var-rouge.jpg` |
| `trente-neuf-vert-classique-cannelee` | `10977444430162-var-vert.jpg` |
| `quarante-et-un-blanc-cuir-sport-acier` | `10977444495698-var-blanc-cuir.jpg` |
| `quarante-et-un-bleu-acier-sport-acier` | `10977444495698-var-bleu-acier.jpg` |
| `quarante-et-un-bleu-cuir-sport-acier` | `10977444495698-var-bleu-cuir.jpg` |
| `quarante-et-un-noir-jaune-acier-sport-acier` | `10977444495698-var-noir-jaune-acier.jpg` |
| `quarante-et-un-noir-acier-sport-acier` | `10977444495698-var-noir-acier.jpg` |
| `quarante-et-un-noir-cuir-sport-acier` | `10977444495698-var-noir-cuir.jpg` |
| `trente-neuf-duo-dore-classique-bicolore` | `10977448722770-var-dore.jpg` |
| `noirmont-un-bronze-plongeuse` | `10977448558930-var-bronze.jpg` |

### 5 faces de mères actives

| Handle | Fichier CDN |
|---|---|
| `trente-six-classique-jubile` | `10977448690002-1.jpg` |
| `trente-neuf-classique-cannelee` | `10977444430162-1.jpg` |
| `quarante-et-un-sport-acier` | `10977444495698-1.jpg` |
| `trente-neuf-duo-classique-bicolore` | `10977448722770-1.jpg` |
| `noirmont-un-plongeuse-acier` | `10977448558930-1.jpg` |

### 12 faces d'accessoires

| Handle | Fichier CDN |
|---|---|
| `barrettes-de-rechange-270` | `10977444954450-1.jpg` |
| `bracelet-fkm-courbe` | `10977445151058-1.jpg` |
| `bracelet-fkm-tropical` | `10977445183826-1.jpg` |
| `bracelet-presidentiel-904l` | `10977445052754-1.jpg` |
| `bracelet-presidentiel-dore` | `10977445085522-1.jpg` |
| `coffret-douze-aluminium` | `10977444856146-1.jpg` |
| `coffret-douze-presentation` | `10977444888914-1.jpg` |
| `loupe-de-date-saphir` | `10977445216594-1.jpg` |
| `pince-a-barrettes` | `10977444921682-1.jpg` |
| `remontoir-solo` | `10977444626770-1.jpg` |
| `remontoir-vitrine` | `10977444790610-1.jpg` |
| `set-tournevis-horloger` | `10977444987218-1.jpg` |

---

## 6. Nommage et manifeste

- Un fichier par image : **`<handle>-<slot>.jpg`**. Exemple : `trente-neuf-bleu-classique-cannelee-poignet.jpg`.
- Slots montres : `face`, `situation`, `macro`, `poignet`. Slots accessoires : `face`, `situation`, `macro`.
- Manifeste indexé sur **`handle` + `sku`**, exclusivement. **Aucun `variantId`, `mediaId`, `productId` ni GID `gid://shopify/…`.** C'est l'indexation sur identifiant de variante qui, au lot 3, a obligé à refaire 118 correspondances à la main par SKU.
- Aucun fichier partagé entre fiches.

> **Note d'ordonnancement.** Sans préfixe numérique, le tri alphabétique des fichiers d'une fiche donne `face`, `macro`, `poignet`, `situation` — ce n'est pas l'ordre de galerie voulu. L'ordre devra donc être imposé au branchement, à la main ou par script, à partir du champ `slot` du manifeste. Un préfixe (`01-face`, `02-situation`…) l'aurait rendu automatique : à arbitrer si le prompt n'est pas encore parti.

---

## 7. Décisions en attente pour Hakim

1. **46 cartes typographiques restent en ligne sur des fiches actives** — 28 cartes témoignage sur les filles Chronographe / Héritage / Intégrale / Voyageur, et 18 cartes sur les mères actives. Hors du nouveau standard : les laisser crée des galeries à 5 images à côté de galeries à 4. **Je ne les ai pas supprimées**, la suppression de médias n'étant pas autorisée. À trancher.
2. **6 images « détails » à texte incrusté** sur les mères actives (`36 mm · Maillons acier`, etc.) : même sujet, à purger au branchement.
3. **24 faces de coloris dupliquées** entre les mères actives et leurs filles : surplus à nettoyer.
4. **Contrôle de stérilité des 5 mises en situation des mères actives** : si elles passent, 5 générations économisées.
5. **`noirmont-deux-plongeuse-ceramique` est exclue** et gardera une galerie héritée de 7 images avec cartes, au milieu d'un catalogue à 4 photos. Trou de cohérence assumé — à confirmer.
6. **Les 7 mères en brouillon** : leurs 80 médias sont non récupérables. À archiver ou oublier.
7. **Avis clients** : Hakim les conserve pour la cohérence de la boutique, sauf là où c'est absurde — les doigtiers latex sont cités. Ce n'est plus un sujet de galerie, c'est un sujet d'**application des avis par fiche**, à traiter séparément.

---

## 8. Livrable associé

Le prompt à envoyer à Codex est **`2026-07-31-prompt-codex-galeries.md`** (même dossier).

> ⚠️ **`PROMPT-CODEX-galeries-completes.md` est obsolète.** Il porte la version 1 du standard — 7 emplacements, 390 fichiers, 175 cartes typographiques — qui **contredit** l'arbitrage du 26/07. Il n'a volontairement pas été mis à jour, pour éviter deux prompts concurrents. **À supprimer ou archiver avant toute exécution** : s'il tombe entre les mains de Codex, il produira 175 cartes qui ne doivent plus exister et manquera les 52 portés-poignet.
