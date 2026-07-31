# Axes du guide de choix NOIRMONT — combien de questions le catalogue supporte

> **27/07/2026** — étude de données en **lecture seule** sur `maisonnoirmont.fr` (Maison Noirmont, plan Basic).
> Aucun produit, aucun métachamp, aucun média, aucun fichier de thème modifié. Aucune valeur inventée.
> Périmètre : **53 fiches montres actives**. Les 38 accessoires (remontoirs, écrins, bracelets vendus seuls,
> outils) et la carte cadeau sont hors sujet.
> Source des métachamps : `metachamps-montres.md`. Source du modèle de conception : `sourcing-configurateur.md` §2 et §8.

---

## 0. La réponse, en une ligne

**Deux questions. Pas trois.** Un entonnoir `Famille → Couleur de cadran` où la seconde question n'est posée
que pour les trois familles qui comptent plus de dix fiches produit **26 chemins, tous aboutissants (100 %),
une seule montre inatteignable sur 53**. À trois questions on tombe à **13,2 %** de chemins aboutissants et
**11 montres cachées** ; à quatre, à **2,7 %** et **19 montres cachées**, soit 36 % du catalogue devenu
invisible. Le catalogue ne supporte pas quatre axes.

---

## 1. Ce qui est réellement renseigné, sur les 53 montres

| Axe | Source | Remplissage | Valeurs distinctes |
|---|---|---:|---|
| **Famille** | `custom.famille` (dérivé des étiquettes) | **53/53 — 100 %** | 5 : Classiques, Sport chic, Chronos, Plongeuses, GMT |
| **Mouvement** | `custom.calibre` | **53/53 — 100 %** | 7 : NH35, Miyota 8215, Mingzhu 2813, PT5000, NH34, DG3804, VK63 |
| **Bracelet — matière** | *aucun métachamp* — extrait titres + options + descriptions | **48/53 — 91 %** | 4 : Acier, Cuir, Caoutchouc, Intégré |
| **Bracelet — maille** | idem | **48/53 — 91 %** | 7 : Jubilé, Acier 3 maillons, Acier maille n.p., Président, Cuir, Caoutchouc, Intégré |
| **Couleur de cadran** | `custom.couleur_cadran` | **45/53 — 85 %** | 14 : Noir, Blanc, Bleu, Vert, Gris, Brun, Champagne, Argent, Turquoise, Rose, Orange, Ivoire, Rouge, Or |
| **Diamètre** | `custom.diametre` | **44/53 — 83 %** | 5 : 36, 39, 40, 41, 42 mm |
| **Prix** | prix mini de la fiche | **53/53 — 100 %** | 3 tranches : < 300 €, 300-349 €, 350 € et + |

> **Correction de comptage à noter.** `metachamps-montres.md` annonçait « diamètre 43/53 » et « 10 fiches sans
> diamètre ». Le relevé du jour donne **44/53 et 9 fiches sans diamètre** : `Noirmont Deux — Plongeuse céramique`
> porte désormais `["40 mm"]`. Le brief de mission (« 9 sans diamètre ») est le chiffre juste.

### Les trois trous, nommés

| Trou | Nb | Fiches concernées |
|---|---:|---|
| **Sans couleur de cadran** | **8** | `trente-neuf-duo-classique-bicolore` · `noirmont-un-plongeuse-acier` · `noirmont-deux-plongeuse-ceramique` · les **5 Voyageur** (`or-3-maillons`, `or-president`, `bicolore-3-maillons`, `bicolore-5-maillons`, `or-rose-5-maillons`) |
| **Sans diamètre** | **9** | les **7 Intégrale** · `noirmont-un-plongeuse-acier` · `noirmont-un-bronze` |
| **Bracelet non établissable** | **5** | `noirmont-un-plongeuse-acier` · `noirmont-deux-plongeuse-ceramique` · `heritage-bleu` · `heritage-bleu-nuit` · `heritage-vert` |

### Comment le bracelet a été établi, et où ça bloque

Le type de bracelet **n'est pas un champ structuré**. Il a été relevé fiche par fiche, dans cet ordre de fiabilité :
valeurs d'options → titre → description produit. Résultat :

- **Classiques (15/15) — Jubilé.** Explicite dans chaque description, avec sa définition maison : « cinq rangs
  de maillons : deux rangs larges […] de part et d'autre de trois rangs centraux ».
- **Sport chic — Intégré (7 Intégrale), Acier (4), Cuir (4).** `quarante-et-un-sport-acier` est une fiche mère
  qui porte **les deux** (options « bracelet acier » et « bracelet cuir M »). ⚠️ Sa description dit par ailleurs
  « un bracelet intégré au poignet » : **c'est une tournure de prose qui contredit ses propres options**. J'ai
  retenu les options, plus fiables. À corriger éditorialement.
- **Chronos — Acier (9), Caoutchouc (7).** Lu dans les options et les descriptions (« sur bracelet acier ou
  caoutchouc noir »). 5 fiches portent les deux.
- **GMT (6/6) — 3 maillons (2), cinq maillons (3), Président (1).** Seule famille où la **maille** est nommée.
  Les « cinq maillons » sont rangés en **Jubilé** par application de la définition que la boutique donne
  elle-même du jubilé — c'est une normalisation de vocabulaire, pas une déduction sur le produit.
- ⛔ **Plongeuses — 5 fiches sur 6 indéterminables.** `Noirmont Un`, `Noirmont Deux` et les 3 `Héritage` ne
  disent rien du bracelet : ni option, ni titre, ni description. Leurs titres (« Plongeuse acier »,
  « Plongeuse céramique ») qualifient le **boîtier**. Seule `noirmont-un-bronze` est établie (« le cadran noir
  et le bracelet acier »). **Ces 5 fiches sont inatteignables par l'axe bracelet.** Je ne devine pas.

⚠️ **Une invention écartée en cours de route.** Les mentions « bracelet acier brossé et poli » (Quarante-et-Un)
et « bracelet acier » (Chronos, Noirmont Bronze) **ne donnent aucun nombre de rangs**. Elles sont donc classées
`Acier maille n.p.` (non précisée) et **non** « 3 maillons ». Seules les 6 fiches Voyageur comptent leurs maillons.

---

## 2. Le tableau croisé, famille par famille

### Vue d'ensemble

| Famille | Fiches | Variantes | Couleurs | Bracelet (matière) | Diamètres | Mouvements | Prix | Combinaisons couleur×bracelet×Ø réelles |
|---|---:|---:|---|---|---|---|---|---:|
| **Classiques** | 15 | 92 | 8 (+1 ∅) | Acier 15 | 36 · 39 | NH35 15, Miyota 9, Mingzhu 2 | 299-397 € | **18** |
| **Sport chic** | 14 | 23 | 6 | Intégré 7, Acier 4, Cuir 4 | 41 (7 ∅) | NH35 14, Miyota 7 | 299-379 € | **12** |
| **Chronos** | 12 | 20 | 10 | Acier 9, Caoutchouc 7 | 39 | VK63 12 | 299 € | **15** |
| **Plongeuses** | 6 | 43 | 3 (+2 ∅) | Acier 1 (5 ∅) | 42×3, 40×1 (2 ∅) | NH35 6, Miyota 3, PT5000 3, Mingzhu 1 | 279-407 € | **5** |
| **GMT** | 6 | 24 | 1 (+5 ∅) | Acier 6 | 40 | DG3804 6, NH34 6 | 349-417 € | **2** |

### Famille × Couleur de cadran — **42 cases vides sur 70 (60 %)**

| | Argent | Blanc | Bleu | Brun | Champ. | Gris | Ivoire | Noir | Or | Orange | Rose | Rouge | Turq. | Vert |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Classiques** | · | · | **3** | · | **1** | · | · | **2** | **2** | **1** | **2** | **2** | · | **1** |
| **Sport chic** | · | **3** | **4** | **1** | · | · | · | **5** | · | · | · | · | **1** | **1** |
| **Chronos** | **1** | **3** | **1** | · | **1** | **1** | **1** | **2** | · | · | **1** | · | **1** | **1** |
| **Plongeuses** | · | · | **2** | · | · | · | · | **1** | · | · | · | · | · | **1** |
| **GMT** | · | · | · | **1** | · | · | · | · | · | · | · | · | · | · |

### Famille × Bracelet (matière) — **12 cases vides sur 20 (60 %)**

| | Acier | Caoutchouc | Cuir | Intégré |
|---|:-:|:-:|:-:|:-:|
| **Classiques** | **15** | · | · | · |
| **Sport chic** | **4** | · | **4** | **7** |
| **Chronos** | **9** | **7** | · | · |
| **Plongeuses** | **1** | · | · | · |
| **GMT** | **6** | · | · | · |

### Famille × Diamètre — **18 cases vides sur 25 (72 %)**

| | 36 mm | 39 mm | 40 mm | 41 mm | 42 mm |
|---|:-:|:-:|:-:|:-:|:-:|
| **Classiques** | **15** | **15** | · | · | · |
| **Sport chic** | · | · | · | **7** | · |
| **Chronos** | · | **12** | · | · | · |
| **Plongeuses** | · | · | **1** | · | **3** |
| **GMT** | · | · | **6** | · | · |

### Famille × Mouvement — **23 cases vides sur 35 (66 %)**

| | DG3804 | Mingzhu 2813 | Miyota 8215 | NH34 | NH35 | PT5000 | VK63 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **Classiques** | · | **2** | **9** | · | **15** | · | · |
| **Sport chic** | · | · | **7** | · | **14** | · | · |
| **Chronos** | · | · | · | · | · | · | **12** |
| **Plongeuses** | · | **1** | **3** | · | **6** | **3** | · |
| **GMT** | **6** | · | · | **6** | · | · | · |

**Lecture des quatre matrices** : 60 à 72 % des cases sont vides. Le catalogue n'est pas un produit cartésien,
c'est un assemblage de cinq gammes disjointes. Chaque famille impose déjà son diamètre, son calibre et sa
matière de bracelet — **exactement le patron que Goteia applique avec ses 5 configurateurs séparés**
(`sourcing-configurateur.md` §2). Le constat concurrent est vérifié sur nos données.

---

## 3. Chemins morts par profondeur d'entonnoir

Deux lectures coexistent, et il faut les distinguer :

- **La grille naïve** = produit cartésien des valeurs de chaque axe. Le « taux d'aboutissement » est la part de
  cases qui contiennent au moins un produit. C'est la mesure de **combien il faut griser**.
- **L'arbre élagué** = ce que le client voit réellement si chaque choix ne laisse que des options existantes.
  Par construction, **0 chemin mort**. Le nombre qui compte alors est le **nombre de chemins ouverts** et la
  **taille moyenne du résultat**.

### 2 questions

| Ordre | Grille | Ouverts | **Morts** | Taux | Montres cachées | Branchement |
|---|---:|---:|---:|---:|---:|---|
| Prix → Couleur | 42 | 26 | **16** | **61,9 %** | 8 | 3,0 puis 8,7 |
| Couleur → Bracelet | 56 | 28 | **28** | 50,0 % | 11 | 14,0 puis 2,0 |
| Bracelet → Couleur | 56 | 28 | **28** | 50,0 % | 11 | 4,0 puis 7,0 |
| Famille → Prix | 15 | 7 | **8** | 46,7 % | **0** | 5,0 puis 1,4 |
| **Famille → Couleur** | 70 | 28 | **42** | 40,0 % | 8 | 5,0 puis **5,6** |
| Famille → Bracelet | 20 | 8 | **12** | 40,0 % | 5 | 5,0 puis 1,6 |
| Couleur → Diamètre | 70 | 27 | **43** | 38,6 % | 16 | 14,0 puis 1,9 |
| Famille → Mouvement | 35 | 12 | **23** | 34,3 % | **0** | 5,0 puis 2,4 |
| Diamètre → Bracelet | 20 | 6 | **14** | 30,0 % | 13 | 5,0 puis 1,2 |
| Famille → Diamètre | 25 | 7 | **18** | 28,0 % | 9 | 5,0 puis 1,4 |

### 3 questions

| Ordre | Grille | Ouverts | **Morts** | Taux | Cachées |
|---|---:|---:|---:|---:|---:|
| Famille → Couleur → Prix | 210 | 36 | **174** | 17,1 % | 8 |
| **Famille → Bracelet → Couleur** | 280 | 37 | **243** | 13,2 % | 11 |
| Bracelet → Famille → Couleur | 280 | 37 | **243** | 13,2 % | 11 |
| Famille → Couleur → Diamètre | 350 | 32 | **318** | 9,1 % | 16 |
| Famille → Diamètre → Couleur | 350 | 32 | **318** | 9,1 % | 16 |
| Famille → Couleur → Mouvement | 490 | 42 | **448** | 8,6 % | 8 |
| Famille → Bracelet(maille) → Couleur | 490 | 37 | **453** | 7,6 % | 11 |
| Famille → Bracelet → Diamètre | 100 | 7 | **93** | 7,0 % | 13 |

### 4 questions

| Ordre | Grille | Ouverts | **Morts** | Taux | Cachées |
|---|---:|---:|---:|---:|---:|
| Famille → Couleur → Bracelet → Prix | 840 | 42 | **798** | 5,0 % | 11 |
| Famille → Couleur → Bracelet → Mouvement | 1 960 | 54 | **1 906** | 2,8 % | 11 |
| **Famille → Couleur → Diamètre → Bracelet** | 1 400 | 38 | **1 362** | 2,7 % | **19** |
| Famille → Diamètre → Couleur → Bracelet | 1 400 | 38 | **1 362** | 2,7 % | **19** |
| Famille → Couleur → Diamètre → Mouvement | 2 450 | 52 | **2 398** | 2,1 % | 16 |
| Famille → Bracelet(maille) → Couleur → Diamètre | 2 450 | 38 | **2 412** | 1,6 % | **19** |

**Le constat central : ajouter une question ne fait presque plus grossir le nombre de chemins ouverts
(28 → 37 → 38) mais multiplie la grille par cinq à sept.** Passer de 2 à 4 questions, c'est passer de
42 cases à griser à **1 362**, pour gagner **10 chemins ouverts** et perdre **11 montres**.

---

## 4. Le meilleur ordre — vérifié, pas supposé

### Le taux brut est un mauvais juge, et il faut le dire

`Prix → Couleur` affiche le meilleur taux (61,9 %) de tout le lot. **Ce n'est pas un mérite, c'est un artefact
de taille de grille** : Prix n'a que 3 valeurs, donc la grille est petite et sa densité mécaniquement plus
haute. Le même biais fait passer `Famille → Diamètre` (25 cases) pour pire que `Famille → Couleur` (70 cases)
alors qu'il ouvre 7 chemins contre 28. **Le taux ne se compare qu'à profondeur et à taille de grille
comparables.** Les critères qui décident vraiment sont trois : **branchement de la question suivante**,
**montres cachées**, **taille du résultat final**.

### La leçon concurrente est confirmée : la famille d'abord

Mesuré sur nos données, et pour trois raisons chiffrées :

1. **C'est le seul axe à 53/53 avec 0 montre cachée.** Toute autre première question ampute le catalogue dès
   le premier écran : Couleur en premier cache 8 fiches, Diamètre 9, Bracelet 5.
2. **C'est le seul axe qui rend la question suivante possible.** Branchement moyen de la question 2 après
   Famille : **Couleur 5,6** · Mouvement 2,4 · Bracelet-maille 2,0 · Bracelet-matière 1,6 · Diamètre 1,4 ·
   Prix 1,4. Inversement, Couleur en première position ouvre un écran à **14 options** — un mur, pas une question.
3. **La famille absorbe la contrainte technique**, comme chez Goteia : elle fixe le diamètre (5 familles → 1 ou
   2 valeurs), le calibre et la matière de bracelet. Après elle, il ne reste qu'un choix esthétique — et c'est
   exactement la pédagogie au particulier qu'on cherche, pas un formulaire de spécifications.

### Le branchement réel de la question 2, famille par famille

C'est le tableau qui tranche tout. `∅` = fiches sans valeur sur cet axe.

| | Couleur | Bracelet matière | Bracelet maille | Diamètre | Mouvement | Prix | Fiches |
|---|:-:|:-:|:-:|:-:|:-:|:-:|---:|
| **Classiques** | **8** (1 ∅) | 1 | 1 | 2 | 3 | 2 | 15 |
| **Sport chic** | **6** | 3 | 3 | 1 (7 ∅) | 2 | 2 | 14 |
| **Chronos** | **10** | 2 | 2 | 1 | 1 | 1 | 12 |
| **Plongeuses** | 3 (2 ∅) | 1 (5 ∅) | 1 (5 ∅) | 2 (2 ∅) | **4** | 1 | 6 |
| **GMT** | 1 (5 ∅) | 1 | **3** | 1 | 2 | 1 | 6 |

**Une colonne à 1 signifie que la question ne se pose pas** — on afficherait un bouton unique. Sur 30 cases,
**17 valent 1 ou 0**. Seule la colonne Couleur est vivante, et seulement pour les trois grandes familles.

---

## 5. Recommandation chiffrée

### Le design retenu : **2 questions, la seconde conditionnelle**

> **Q1 — « Quel genre de montre cherchez-vous ? »** → 5 familles. Toujours posée.
> **Q2 — « Quelle couleur de cadran ? »** → posée **uniquement** pour Classiques, Sport chic et Chronos
> (les 3 familles de plus de 10 fiches). Plongeuses (6) et GMT (6) vont **directement aux résultats**.

Mesures du design retenu :

| Indicateur | Valeur |
|---|---|
| **Chemins ouverts** | **26** |
| **Chemins morts** | **0 — taux d'aboutissement 100 %** |
| **Montres atteignables** | **52/53** |
| **Montres cachées** | **1** — `trente-neuf-duo-classique-bicolore` (seule Classique sans couleur de cadran) |
| **Produits par écran de résultat** | moyenne **2,08** · min 1 · max 6 |
| **Écrans à un seul produit** | 14 sur 26 |
| Cases à griser dans Q2 | **18 sur 42 offertes** (3 familles × 14 couleurs → 24 ouvertes, 18 grisées) |

### Pourquoi pas trois questions

Une troisième question n'est **légitime que sur 12 des 31 branches** (39 %) — critère : au moins 2 options
réelles **et** aucune fiche vide sur le sous-ensemble. Sur les 19 autres branches elle n'aurait qu'une seule
réponse possible. Et là où elle est légitime, elle réduit un résultat déjà à 2-5 produits vers 1 produit :
elle ne guide plus, elle décide à la place du client.

Si Hakim veut quand même une Q3, la seule forme défendable est **conditionnelle et non bloquante** :

| Après | Q3 légitime | Options |
|---|---|---:|
| Sport chic + Blanc / Bleu / Noir | **Bracelet matière** (acier / cuir / intégré) | 3 |
| Chronos + Blanc / Noir | **Bracelet matière** (acier / caoutchouc) | 2 |
| Classiques + Bleu / Noir / Rose / Rouge | **Prix** (< 300 € / 300-349 €) | 2 |
| Classiques + Or · GMT + 3 maillons / Jubilé | **Mouvement** | 3 / 2 |

Nulle part ailleurs. À présenter comme un **affinage optionnel après les résultats**, jamais comme une étape
obligatoire de l'entonnoir.

### Ce qu'il faut griser

1. **Les 18 couples famille × couleur inexistants** parmi les 42 offerts en Q2 (24 restent ouverts) — la liste est au §6.
2. **Les 42 cases de la grille complète famille × couleur** si jamais la Q2 était posée aux 5 familles.
3. **Toute question dont la famille ne laisse qu'une option** : Bracelet pour Classiques, Plongeuses et GMT ;
   Diamètre pour Sport chic, Chronos et GMT ; Mouvement pour Chronos. Ne pas les griser — **ne pas les afficher**.
4. **La branche `Plongeuses → bracelet`** : 5 fiches sur 6 sans valeur. Elle renverrait 1 produit sur 6.

### L'échappatoire, obligatoire

Une option **« Peu importe / Montrez-moi tout »** sur chaque question ramène le stock caché à **zéro**, à toutes
les profondeurs testées :

| Entonnoir | Cachées sans échappatoire | Avec |
|---|---:|---:|
| Famille → Couleur | 8 | **0** |
| Famille → Bracelet → Couleur | 11 | **0** |
| Famille → Couleur → Diamètre | 16 | **0** |
| Famille → Couleur → Bracelet → Diamètre | 19 | **0** |

C'est la mesure la moins chère du lot : elle coûte une case par écran et récupère jusqu'à 19 fiches.

---

## 6. Les 26 chemins ouverts, et les 18 à griser

| Famille | Couleurs **ouvertes** (nb de produits) | Couleurs à **griser** |
|---|---|---|
| **Classiques** | Bleu (3) · Noir (2) · Or (2) · Rose (2) · Rouge (2) · Champagne (1) · Orange (1) · Vert (1) | Argent, Blanc, Brun, Gris, Ivoire, Turquoise |
| **Sport chic** | Noir (5) · Bleu (4) · Blanc (3) · Brun (1) · Turquoise (1) · Vert (1) | Argent, Champagne, Gris, Ivoire, Or, Orange, Rose, Rouge |
| **Chronos** | Blanc (3) · Noir (2) · Argent (1) · Bleu (1) · Champagne (1) · Gris (1) · Ivoire (1) · Rose (1) · Turquoise (1) · Vert (1) | Brun, Or, Orange, Rouge |
| **Plongeuses** | *pas de Q2* → 6 produits | — |
| **GMT** | *pas de Q2* → 6 produits | — |

---

## 7. Axes à renoncer, et ce qui les rouvrirait

### Renoncer maintenant

| Axe | Pourquoi, mesuré | Statut |
|---|---|---|
| **Diamètre** | Branchement 1,4 après Famille. **3 familles sur 5 n'ont qu'une valeur** (Sport chic 41, Chronos 39, GMT 40) : la question n'existe pas. Et 9 fiches vides — dont **les 7 Intégrale, une gamme entière**. Un client qui coche « 41 mm » ne voit pas les Intégrale. | ⛔ **Pas une question.** À garder en **facette de collection** et en **pastille de fiche**, où l'incomplétude est tolérable. |
| **Bracelet, en axe global** | Aucun métachamp. 5 fiches indéterminables. Branchement 1,6 : une seule valeur pour Classiques, Plongeuses et GMT. | ⛔ **Pas une question globale.** Utilisable en **Q3 conditionnelle** sur Sport chic et Chronos uniquement (§5). |
| **Bracelet, maille fine** (Jubilé / 3 maillons / Président) | **Seule la famille GMT distingue trois mailles.** Partout ailleurs l'axe s'effondre à 1. Et 14 fiches sont en `Acier maille n.p.` — le nombre de rangs n'est pas écrit. | ⛔ **Fermé.** Ne pas ouvrir un axe où 14 fiches sur 48 n'ont pas de valeur nommée. |
| **Mouvement / calibre** | 53/53, 0 caché — techniquement le plus propre. Mais branchement 2,4, et **c'est un axe de spécialiste**. Demander « NH35 ou Miyota 8215 ? » à un particulier, c'est le persona métier qu'on s'interdit. | ⛔ **Pas une question client.** Sauf **Plongeuses**, où c'est le seul axe branchu (4 options) — et là encore, mieux vaut afficher les 6 fiches. |
| **Prix** | 53/53, 0 caché, mais branchement 1,4 après Famille : **3 familles sur 5 n'ont qu'une tranche** (Chronos 299 €, Plongeuses < 300 €, GMT 300-349 €). | ⛔ **Pas une question.** Un tri, pas un filtre. |

### Ce qui deviendrait exploitable — la piste d'action

Trois écritures de données, par ordre de rendement :

| # | Action | Coût | Gain mesuré |
|---|---|---|---|
| **1** | **Créer le métachamp `custom.bracelet`** (liste de texte, comme les quatre autres) et le renseigner sur les 53 montres. **48 valeurs sont déjà établies par cette étude** — il reste à trancher les 5 Plongeuses. | 1 définition + 53 écritures, dont **5 seulement demandent une source** (photos fournisseur DSers ou fiche AliExpress d'origine pour `Noirmont Un`, `Noirmont Deux`, les 3 `Héritage`) | Le bracelet passe de 91 % à 100 % : `Famille → Bracelet → Couleur` cesse de cacher 11 montres. Débloque une **Q3 honnête sur 4 familles au lieu de 2**, et une **facette « Bracelet » en vitrine** — aujourd'hui impossible. |
| **2** | **Renseigner `couleur_cadran` sur les 8 fiches vides.** Les 5 `Voyageur` et `Noirmont Un/Deux` n'annoncent leur cadran nulle part ; `Trente-Neuf Duo` dit « bicolore » du boîtier. **Il faut une source** : visuels produit ou fiche fournisseur. Ne pas déduire — la note de `metachamps-montres.md` sur le cadran brun du `Voyageur Bicolore` reste une supposition, pas une donnée. | 8 contrôles visuels | **C'est le gain le plus direct sur le design retenu** : les cachées passent de 1 à 0, et GMT + Plongeuses deviennent éligibles à la Q2 couleur — donc à un vrai entonnoir à 2 questions sur 5 familles au lieu de 3. |
| **3** | **Renseigner `diametre` sur les 9 fiches vides** — surtout les **7 Intégrale**, qui sont une gamme complète invisible dès qu'on touche à l'axe diamètre. Cote à demander au fournisseur via DSers. | 9 valeurs, 1 demande fournisseur | Ne débloque **pas** une question (le branchement resterait 1,4), mais rend la **facette de collection** honnête et supprime 9 des 16-19 montres cachées des entonnoirs profonds. |

**Ce qui ne se débloquera pas par de la donnée** : aucun métachamp ne rendra le diamètre ou le prix
*branchus*. Le problème n'est pas leur remplissage, c'est que **la famille les détermine déjà**. Les remplir
sert la vitrine et les pastilles ; ça ne crée pas de question.

---

## 8. Ce que cette étude n'établit pas

- **`quarante-et-un-sport-acier` se contredit** : ses options disent « bracelet acier » et « bracelet cuir M »,
  sa description dit « bracelet intégré ». J'ai retenu les options. **La fiche doit être corrigée** avant de
  brancher quoi que ce soit dessus.
- **Le bracelet des 5 Plongeuses reste inconnu**, et je ne l'ai pas déduit du titre — « Plongeuse acier »
  qualifie le boîtier, pas le bracelet.
- **Les tranches de prix sont les miennes** (< 300 / 300-349 / 350 +), calées sur le prix mini de chaque fiche.
  Ce n'est pas une donnée de boutique, c'est un découpage d'analyse.
- **Aucune donnée de trafic ni de vente** n'entre dans ce calcul. L'ordre recommandé est optimal au sens de la
  **couverture du catalogue**, pas de la demande client. Si les mots-clés SEMrush montrent que le diamètre est
  ce que les gens cherchent (`montre 36 mm femme`…), l'arbitrage change — mais alors il faudra d'abord
  remplir les 9 diamètres manquants.
- **Les 38 accessoires sont hors périmètre**, y compris les 8 fiches Bracelet vendues séparément. Elles ne
  peuvent pas servir de source pour l'axe bracelet des montres : ce sont d'autres références.

---

*Étude du 27/07/2026. Lecture seule. Aucune fiche, aucun métachamp, aucun média, aucun fichier de thème
touché. Les 141 valeurs de métachamps relevées sont celles écrites le 26/07 par `metachamps-montres.md`,
à la correction près du diamètre de `Noirmont Deux` (44/53, et non 43).*
