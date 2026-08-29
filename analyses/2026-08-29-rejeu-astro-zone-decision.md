# Rejeu en zone de décision — univers « Déco astro / ciel étoilé », DataForSEO seul

**Date de mesure : 2026-08-29** (session ouverte le 29/08 ; l'horloge machine a basculé à
2026-08-30 00:59 CEST pendant la rédaction — toutes les lectures API sont datées du 29/08 au sens
du jour de travail, et l'écart est signalé plutôt que masqué).

Test de non-régression **en zone de décision**, avant résiliation de l'abonnement SEMrush.
Le rejeu « rideaux » du 29/08 a validé la chaîne DataForSEO sur un dossier à ×16 du seuil.
Ce rejeu-ci porte sur un dossier **conclu STOP le 15/08/2026 à faible distance du plancher** :
c'est le cas où un écart de mesure peut retourner un verdict.

**Périmètre** : déco astronomique — projecteurs de ciel étoilé, veilleuses, lampes lune, posters
et cartes du ciel, système solaire décoratif. **Hors périmètre : les télescopes** (dossier séparé,
conclu STOP le 15/08 sur la concurrence).

---

## 1. Entrée, méthode, coût, contrôle témoin

### 1.1 Ordre de travail — attestation d'aveuglement

Les sections 1 à 6 ont été **mesurées et rédigées avant toute ouverture** de
`analyses/2026-08-15-niches-univers/U4-astronomie/`. Ni le volume atteint le 15/08, ni l'écart
au seuil, ni le détail des familles n'étaient connus au moment de fixer le verdict de la §6.

Trois précautions prises pour préserver l'aveuglement :

- `registre-candidats.md` n'a pas été lu. Un simple comptage (`grep -c`) confirme que le dossier
  y a bien 3 occurrences — l'anti-doublon est établi — **sans qu'aucune valeur n'ait été lue**.
- Les trois documents du 29/08 cités comme sources de recette
  (`croisement-semrush-dataforseo`, `test-aveugle-et-deduplication`, `validation-3-graines-aveugle`)
  ont été grepés pour `astro|ciel|etoil|lune|galaxie|planetarium|systeme solaire|veilleuse` :
  **zéro occurrence**. Aucune contamination par ce canal, contrairement au rejeu rideaux où
  ~20 têtes SEMrush avaient été vues.
- Le rapport de référence du 15/08 n'a été ouvert qu'à la §7.

**Aveuglement jugé complet sur ce dossier.**

### 1.2 Outil — DataForSEO seul, SEMrush non utilisé

- **Découverte** : `scripts/kw_dfs.py`, endpoint `dataforseo_labs/google/keyword_suggestions/live`,
  `location_name: France`, `language_name: French`, tri volume décroissant, 1 000 lignes/page.
  Normalisation, regroupement et **MAX du groupe** appliqués par le script.
- **Volume de tête, CPC, concurrence, série 12 mois** :
  `keywords_data/google_ads/search_volume/live`, `search_partners: false`, France / français.
- **SERP** : `serp/google/organic/live/advanced`, France / français, desktop, profondeur 20.
  *(La navigation directe vers google.fr a été refusée par l'environnement ; l'audit SERP passe
  donc par l'API SERP de DataForSEO — même outil déclaré, lecture non connectée. Conséquence
  méthodologique : voir la réserve R3 en §9.)*

**Aucune requête SEMrush n'a été émise sur cette tâche.**

### 1.3 Graines interrogées — 16 graines

| Graine | Pages | Lignes rendues | Annoncées par l'API | Idées après dédup |
|---|---:|---:|---:|---:|
| `projecteur galaxie` | 1 | 165 | 165 | 119 |
| `ciel étoilé` | 2 | 1 005 | 1 005 | 739 |
| `ciel etoile` | 1 | 434 | 434 | 359 |
| `lampe lune` | 1 | 438 | 438 | 304 |
| `lampe galaxie` | 1 | 65 | 65 | 53 |
| `veilleuse` | 3 | 3 000 | 12 681 | 2 005 |
| `carte du ciel` | 1 | 814 | 814 | 604 |
| `système solaire` | 2 | 2 000 | 3 770 | 1 259 |
| `systeme solaire` | 2 | 1 393 | 1 393 | 1 106 |
| `poster astronaute` | 1 | 2 | 2 | 2 |
| `planétarium` | 2 | 1 643 | 1 643 | 1 160 |
| `planetarium` | 2 | 2 000 | 2 528 | 1 666 |
| `astronaute` | 2 | 2 000 | 3 319 | 1 471 |
| `galaxie` | 1 | 1 000 | 1 000+ | 544 |
| `poster espace` | 1 | 19 | 19 | 16 |
| `deco astronomie` | 1 | 4 | 4 | 4 |

Les onze graines du brief ont été interrogées **dans les deux orthographes** demandées. Trois
graines complémentaires ont été ajoutées pour instruire les pièges annoncés (`galaxie` seul,
`poster espace`, `deco astronomie`) — ajout de couverture, pas ajustement vers un chiffre attendu.

Deux graines restent tronquées : `veilleuse` (3 000 lues sur 12 681 annoncées) et `planetarium`
(2 000 sur 2 528). Le tri étant par volume décroissant, la traîne non lue est sous le volume de la
dernière ligne lue ; l'amputation rend la mesure **conservatrice**. Elle porte de surcroît sur les
deux graines les plus massivement hors périmètre (puériculture / lieux).

### 1.4 Coût

| Poste | USD |
|---|---:|
| Découverte, 16 graines, 24 pages au total | ≈ 2,94 |
| `google_ads/search_volume/live`, 22 têtes + séries 12 mois | 0,090 |
| SERP `organic/live/advanced`, 7 requêtes | 0,025 |
| Contrôles témoin (≈ 26 appels) | ≈ 0,20 |
| **Total** | **≈ 3,25 USD** |

À comparer aux 149 €/mois de SEMrush. Le cache disque rend tout rejeu ultérieur gratuit.

### 1.5 Contrôle témoin — conforme, mais avec deux incidents à déclarer

`tufting` = **12 100** attendu, France / français.

| Moment | Lecture |
|---|---|
| Avant la première mesure (lot 1) | 12 100 — conforme |
| Encadrement de chacun des 9 lots | 12 100 — conforme |
| Après la dernière mesure | 12 100 — conforme |

**Deux incidents transitoires sont survenus et doivent être consignés.** À deux reprises
(après `ciel étoilé --pages 2`, puis après le lot `galaxie / poster espace / deco astronomie`),
le contrôle témoin de sortie a renvoyé **`None`** — un tableau `result` vide, et non une valeur
fausse. Le script s'est arrêté comme prévu et **aucun chiffre n'a été écrit**. Un re-test immédiat
(4 puis 6 appels consécutifs) a rendu 12 100 à chaque fois : incident d'API ponctuel, ni quota
épuisé ni changement de base. **Les deux lots concernés ont été intégralement refaits en
`--refresh`, encadrés par deux témoins conformes**, et ce sont ces lectures-là qui sont utilisées.

Ce comportement est une **réserve d'outillage réelle** (voir §9, R1) : le même `None` sur un appel
de données, et non sur le témoin, produirait un zéro silencieux.

### 1.6 Limites de calcul assumées

1. **Jamais de somme de volumes bruts.** Regroupement par clé normalisée, **MAX du groupe**.
   Enjeu mesuré ici : la somme des bruts graine par graine vaut **1 407 190** ; après
   déduplication inter-graines il reste **1 126 330**. **280 860 recherches/mois, soit 20 %,
   étaient le même bucket compté plusieurs fois.** Sur 14 424 formulations, 10 218 idées
   distinctes subsistent — **29 % de reformulations supprimées**, et 1 268 groupes où Google sert
   explicitement les variantes au même volume.
2. **Le classement s'opère sur l'expression réelle, pas sur la clé normalisée.** La
   dépluralisation du script transforme `décès` en `dece` et `planètes` en `planete` : écrire les
   règles d'exclusion contre la clé produit des faux négatifs silencieux. Deux autres pièges ont
   été corrigés en cours de route et méritent d'être écrits : `étoile` contient `toile`
   (rabattait toute la famille « ciel étoilé » vers les posters) et `astronaute` contient `astro`
   (rabattait toute la famille astronaute vers l'astrologie). **Le matching de classement doit se
   faire à frontière de mot, jamais en sous-chaîne libre.**
3. **Le tronc générique n'est pas remonté par l'endpoint.** La correspondance est plein texte sur
   la graine : les têtes ont donc été mesurées séparément au `search_volume`. Elles sont adjugées
   une par une en §6, pas noyées dans les familles.
4. **Une idée n'est comptée qu'une fois.** L'affectation suit un ordre de priorité documenté
   (exclusions d'abord, puis Projecteur → Lampe/veilleuse → Ciel étoilé → Carte du ciel →
   Poster/déco murale → Plafond/kit → Objet déco → Planétarium). Le total consolidé est invariant
   à cet ordre ; seule la répartition entre familles en dépend.
5. **Aucune donnée d'une base autre que France.** Aucun sourcing, aucune cartographie de
   concurrence, aucun `GO_FINAL`.

### 1.7 Seuil appliqué

`PRODUCT-RESEARCH-CRITERIA.md` §1, mode **UNIVERS**, **décision Hakim du 29/08/2026** :
plancher **37 500** en base DataForSEO (confort 50 000) — recalibrage du 30 000 SEMrush par le
facteur médian ×1,25 mesuré sur trois échantillons concordants.
**Bande de cas limite : 30 000 – 45 000** (±20 %).

C'est contre **37 500** que le verdict est prononcé.

---

## 2. Mesure par famille

Recherches/mois, France, lecture du 2026-08-29. **Têtes génériques exclues** de ce tableau : elles
sont adjugées séparément en §6 après lecture de leur SERP.

| Famille adressable | Brut | Net de marque | Net final | Idées | Formulations | Reform. supprimées |
|---|---:|---:|---:|---:|---:|---:|
| F3 — Lampe / veilleuse astro | 14 310 | 12 330 | **12 050** | 399 | 551 | 28 % |
| F1 — Projecteur ciel étoilé / galaxie | 12 620 | 11 460 | **11 320** | 200 | 288 | 31 % |
| F9 — Ciel étoilé, traîne produit | 15 480 | 15 350 | **4 860** | 228 | — | 19 % |
| F5 — Poster / déco murale astro | 4 020 | 3 770 | **3 510** | 90 | 113 | 20 % |
| F6 — Objet déco astro (mobile, puzzle, globe) | 9 240 | 9 040 | **2 890** | 101 | — | 21 % |
| F2 — Ciel étoilé plafond / kit fibre optique | 1 940 | 1 890 | **1 870** | 46 | 64 | 28 % |
| F8 — Planétarium **produit** | 136 470 | 134 910 | **1 370** | 90 | — | 16 % |
| F4 — Carte du ciel **produit** | 1 130 | 1 130 | **700** | 33 | 48 | 31 % |
| **TOTAL familles, hors têtes** | **195 210** | **189 880** | **38 570** | 1 187 | — | — |

L'écart entre « net de marque » et « net final » est l'essentiel de l'histoire de ce dossier :
**189 880 → 38 570, soit 80 % du volume retiré après les marques.** Ce n'est pas du nettoyage de
marque, c'est du nettoyage d'**intention** : lieux, scolaire, pop-culture, informationnel.
Sur F8 en particulier, 134 910 net de marque tombent à 1 370 — le mot `planétarium` désigne un
lieu, pas un produit.

### Volumes de tête — endpoint `google_ads/search_volume/live`

| Tête | Volume | CPC (USD) | Concurrence | Lecture |
|---|---:|---:|---|---|
| `système solaire` / `systeme solaire` | 60 500 | 0,06 | MEDIUM | scolaire pur, CPC plancher |
| `galaxie` | 27 100 | 0,49 | LOW | racine polluée |
| `planetarium` (sans accent) | 22 200 | 0,94 | LOW | lieu |
| `astronaute` | 22 200 | 0,19 | LOW | informationnel / actualité |
| `veilleuse` | 14 800 | 0,40 | HIGH | commercial, mais puériculture |
| `ciel étoilé` / `ciel etoile` | 12 100 | 0,39 | LOW | mixte, dominante informationnelle |
| `planétarium` (accentué) | 12 100 | 0,36 | LOW | lieu |
| `carte du ciel` | 5 400 | 1,00 | MEDIUM | astrologie + carte gratuite |
| `projecteur ciel étoilé` | 1 900 | 0,22 | HIGH | **produit, intention pure** |
| `lampe lune` | 1 900 | 0,36 | HIGH | **produit, intention pure** |
| `projecteur galaxie` | 1 300 | 0,13 | HIGH | produit |
| `carte du ciel étoilé` | 480 | 1,33 | HIGH | produit personnalisé |
| `lampe galaxie` | 390 | 0,18 | HIGH | produit |
| `poster espace` | 170 | 0,85 | HIGH | produit, marginal |
| `deco astronomie` | 90 | 0,22 | HIGH | produit, marginal |
| `planetarium maison` | 90 | 0,14 | HIGH | produit, marginal |
| `poster astronaute` | 30 | 0,37 | HIGH | produit, marginal |
| `lampe de lune` | 30 | 0,40 | HIGH | reformulation faible |
| `planétarium à la maison` | — | — | — | **aucune donnée rendue** |

**Le signal le plus net du dossier tient dans deux colonnes de ce tableau.** Les têtes à gros
volume sont toutes en concurrence `LOW`/`MEDIUM` avec un CPC de 0,06 à 0,49 — signature d'un
marché où personne n'enchérit parce qu'il n'y a rien à vendre. Les seules requêtes en concurrence
`HIGH` sont celles à intention produit — et elles plafonnent à 1 900.

---

## 3. Thèmes co-occurrents par famille

C'est la table qui a révélé les contaminations. Format : `terme` idées/volume cumulé.

**F1 — Projecteur astro** : `projecteur` 181/8 720 · `galaxie` 84/2 620 · `etoile` 68/6 390 ·
`ciel` 62/5 840 · `planetarium` 32/1 260 · `astronaute` 26/1 240 · `lampe` 21/450 ·
`projection` 17/2 580 · `led` 15/160 · `veilleuse` 11/860 · `plafond` 9/400 · `360` 7/110.
Famille homogène, aucune contamination — c'est le cœur produit du dossier.

**F3 — Lampe / veilleuse astro** : `lampe` 288/6 720 · `lune` 237/4 970 · `etoile` 64/2 830 ·
`ciel` 59/1 550 · `veilleuse` 45/3 410 · `led` 39/870 · `astronaute` 37/2 500 · `galaxie` 32/840 ·
`demi` 14/970. Le `demi` est le piège : **`lampe demi-lune` = lampe UV d'onglerie**, 520/mois,
sortis (§4).

**F9 — Ciel étoilé, traîne** : `ciel`/`etoile` 320/6 950 · `reserve` 15/370 (réserve
internationale de ciel étoilé — tourisme) · `peinture` 10/420 (technique DIY) · `noel` 8/450
(*Noël sous un ciel étoilé*, téléfilm) · `mariage` 8/600 (prestation de location) ·
`photoshop` 6/20. Traîne mixte, nettoyée en §4.

**F6 — Objet déco astro** : `systeme`/`solaire` 78/4 390 · `maquette` 29/2 390 · `mobile` 25/720 ·
`astronaute` 25/760 · `puzzle` 24/620 · `figurine` 9/280 · `couette` 6/150 · `housse` 5/130.
Le `maquette` domine et c'est du **projet scolaire** (`fabriquer`, `à imprimer`, `montessori`,
`facile`), sorti en §4.

**F5 — Poster / déco murale** : `ciel`/`etoile` 31/840 · `poster` 25/670 · `systeme`/`solaire`
20/710 · `astronaute` 18/900 · `espace` 15/400 · `deco` 14/520 · `tableau` 11/400 ·
`papier peint` 10/980. Famille propre mais minuscule.

**F2 — Ciel étoilé plafond / kit** : `etoile` 33/1 630 · `plafond` 19/1 010 · `fibre optique`
14/440 · `kit` 13/540 · `phosphorescent` 4/40 · `scintillant` 3/30. La plus petite famille, mais
la plus pure en intention d'achat.

**F8 — Planétarium produit** : `planetarium` 1 190/16 530 · `projector` 61/680 · `star` 31/290 ·
**`museum` 27/280 · `show` 21/150 · `ticket` 20/130 · `hamburg` 12/190**. Les trois derniers
disent tout : ce qui reste après le filtre « villes françaises » est **du planétarium étranger**,
toujours un lieu. Filtré à nouveau en §4.

**F4 — Carte du ciel produit** : `ciel`/`carte` 33/700 · `etoile` 10/110 · `constellation` 9/300 ·
`astronomie` 6/220 · `personnalisee` 1/20. Le mot `personnalisée` — qui est le produit vendable —
pèse **20 recherches/mois**.

---

## 4. Volumes retirés, chiffrés un par un

| Bloc exclu | Volume | Idées | Motif |
|---|---:|---:|---|
| **X3 — Pop-culture / homonymes de `galaxie`** | **264 910** | 691 | *Gardiens de la Galaxie* (33 100 + 9 900 + 6 600 + 4 400 + 3 600), Galaxie Amnéville, Mario Galaxy, Galaxie Enseignement supérieur (5 400, plateforme de recrutement universitaire), Radio Galaxie, Galaxie Sushi/Wok/Pêche, Ford Galaxie, Samsung Galaxy, Andromède, M81/M51/M33 |
| **H — Hors univers astro** (dont veilleuse puériculture) | **256 560** | 1 880 | `veilleuse bébé` 27 100, `veilleuse` 14 800, `veilleuse tortue` 3 600, Pabobo, Momcozy, VTech, Cloud b, `veilleuse coranique`, `veilleuse Stitch`, prises murales, bruit blanc |
| **R — Racines et reste astro non attribuable** | **179 190** | 1 789 | têtes génériques `planete système solaire` 27 100, `galaxie` 27 100, `astronaute` 22 200, `ciel étoilé` 12 100 — adjugées séparément en §6 |
| **X1 — `planétarium` = LIEU** | **119 290** | 707 | Nantes 8 980, Strasbourg 7 230, Paris 12 830, Reims 4 090, Rennes 5 790, Vaulx-en-Velin 3 480, Saint-Étienne 3 150, Cité des sciences, Cité de l'espace, Palais de la découverte, Vulcania, Nançay, Pic du Midi, Griffith, Adler Chicago, Hamburg, Copenhague, Prague + `horaires`, `tarifs`, `billets`, `séances`, `programme`, `à proximité`, `near me` |
| **X2 — Scolaire / informationnel** | **64 680** | 893 | `pdf`, `évaluation`, `exercice`, `CM1`/`CM2`/`CE2`/`6ème`, `schéma`, `légende`, `trace écrite`, `combien de planètes`, `ordre des planètes`, `plus grande/petite/chaude/froide planète`, `C'est pas sorcier`, `maquette à imprimer` |
| **X7 — Informationnel / culturel** | **50 770** | 558 | `ciel étoilé ce soir`, `Van Gogh`, `photo`, `fond d'écran`, `wallpaper`, `4K`, `coloriage`, `citation`, `tatouage`, `étoile de plus dans le ciel` (avis de décès), `5 lettres` (mots croisés), `pleine lune`, `éclipse`, `étoile filante` |
| **X6 — `astronaute` métier / actualité** | **42 850** | 311 | `astronaute française Sophie Adenot` 8 100, `astronaute française` 5 400, `cosmonaute`, `Artemis 2`, `devenir astronaute`, `salaire`, `combinaison`, `casque`, Michael Collins, Thomas Pesquet |
| **X5 — Marques et enseignes** | **42 470** | 635 | Nature & Découvertes, Cdiscount, Amazon, Action, Maisons du Monde, BUT, Ikea, Sega/Homestar, Bresser, National Geographic (liste minimale du brief) + Leroy Merlin, Castorama, Gifi, Fnac, Darty, Conforama, Leclerc, Temu, Lidl, Lego, Playmobil, Buki, Clementoni, Legami, Vertbaudet, Orchestra, Aubert, Oxybul |
| **X10 — Automobile** | **11 250** | 133 | `ciel étoilé voiture` 4 400, `kit ciel étoilé voiture` 320, ciel de toit Golf 4/5/6/7, Mégane 4, Rolls-Royce, feux de veilleuse, ampoules |
| **X13 — Astrologie** | **7 670** | 66 | `carte du ciel astrologique`, `astrotheme`, `astrodienst`, `thème astral`, `natal`, `ascendant` |
| **X12 — Déguisement** | **3 420** | 52 | `déguisement astronaute`, `costume`, `mascotte`, `gonflable` |
| **X9 — Énergie solaire (homonyme)** | **1 600** | 67 | `système solaire combiné`, `photovoltaïque`, `panneau solaire`, pompe à chaleur |
| **X11 — Lampe d'onglerie (homonyme)** | **520** | 5 | `lampe demi-lune ongles`, `onglerie`, `cils` |
| **H — Puériculture générique résiduelle** | **400** | 10 | |
| **X8 — Télescopes (hors périmètre déclaré)** | **20** | 3 | |
| **Retraits fins intra-familles** | **6 890** | — | F9 : `Noël sous un ciel étoilé` 390, `peinture ciel étoilé` 370, réserves internationales 180, Rolls-Royce 110, PNG/Photoshop 90, villes, Ninho — total **2 090**. F6 : `maquette système solaire` 1 300 + `fabriquer` 320 + `facile` 170 + `à imprimer` 140 + DIY/Montessori — total **2 710**. F8 : planétariums étrangers, *Planétarium Ghost Travel* (manga), *La La Land* — total **2 090** hors tête. |

### Les quatre pièges annoncés au brief — instruits et chiffrés

1. **`planétarium` = lieu.** Confirmé sans ambiguïté. Volume lieu identifié : **119 290**
   (+ 22 200 de tête, + ~2 090 de lieux étrangers résiduels). Volume **produit** :
   **1 370/mois**, soit **1,1 % du champ `planétarium`**. La SERP (§5) ne laisse aucune place au
   doute : 12 blocs `local_pack`, un knowledge graph « Planétarium », zéro résultat marchand.
2. **`galaxie` seul est inexploitable en racine.** Confirmé et pire qu'annoncé. 27 100 de tête,
   **264 910 de champ pop-culture**. Les Gardiens de la Galaxie pèsent à eux seuls ≈ 57 600 ;
   s'y ajoutent une plateforme de recrutement universitaire (Galaxie Enseignement supérieur,
   5 400), une salle de spectacle (Amnéville), un jeu Nintendo, une radio, un restaurant, une
   voiture Ford et les smartphones Samsung. **Racine écartée.**
3. **`poster espace` et le rabattement « La Poste ».** Le rabattement **n'a pas eu lieu** :
   DataForSEO rend `poster espace` = **170/mois** avec 19 suggestions seulement, toutes
   thématiquement cohérentes. Le piège est réel sur d'autres outils ; il ne s'est pas matérialisé
   ici. En revanche le constat est plus dur que le piège : `poster espace` 170,
   `poster astronaute` 30, `poster galaxie` 70, `affiche astronaute` 40 — **la famille poster
   n'existe pas commercialement en France.**
4. **`astronaute` et `système solaire` sont scolaires et informationnels.** Confirmé.
   `système solaire` 60 500 : SERP à 100 % Wikipédia / CNES / Canopé / Vikidia / Lumni /
   Maxicours / maitrelucas.fr « pour CM1 CM2 » / Larousse, avec AI overview et knowledge graph —
   **zéro résultat marchand, zéro bloc Shopping**. CPC 0,06 USD, ce qui est la signature
   arithmétique d'un marché sans annonceur. `astronaute` 22 200 : tiré par l'actualité
   (Sophie Adenot, Artemis 2) et l'orientation métier. **Volume non adressable : sorti.**

---

## 5. Vérification SERP — France, français, session non connectée, 2026-08-29

### `projecteur ciel étoilé` — 1 900 — **commercial pur**
**Intention** : achat, sans ambiguïté. **8 blocs `popular_products`** (carrousels produits
sponsorisés), PAA d'aide au choix (« Quel est le meilleur projecteur lumineux ? »).
**Prix observés** : 11,99 · 13,24 · 13,99 · 15,69 · 16,53 · 16,99 · 18,03 · 18,99 · 19,99 ·
20,98 · 21,21 · 22,66 · 24,71 · 24,99 · 25,99 · 28,99 · 29,99 · 31,28 · 31,69 · 31,79 · 32,54 ·
34,93 · 34,95 · 34,99 · 39,73 · 39,99 · 40,90 · 41,10 · 41,51 · 41,99 · 45,81 · 46,59 · 47,99 ·
48,99 · 49,99 · 53,99 · 59,90 · 59,99 · 69,99 €.
**39 prix relevés, médiane 31,69 €. 35 des 39 sont sous 50 €.**
- *Spécialistes / DTC* : science-labs.com (O1), lustria.fr (O6), lapouleapois.fr (O9),
  kitcieletoile.com, MyBouddha, Déco Science, Prix Malin, Bigshopper, Shoparize, CleverlyFound.
- *Marketplaces / enseignes* (repères) : Amazon, Leroy Merlin, Fnac, Darty, Cdiscount,
  Nature & Découvertes, Action, Cultura, Vertbaudet, Kaufland, ManoMano.
- Éditorial : bfmtv.com « Meilleurs projecteurs étoiles 2026 — guide d'achat », idealo.

### `ciel étoilé` — 12 100 — **dominante informationnelle**
**Aucun bloc `popular_products`, aucun bloc `paid` détecté.** Blocs : images, PAA, 19 organiques.
PAA entièrement informationnel (« Comment savoir quelle étoile on voit ? », « Quel est le ciel
étoilé ce soir ? »).
Top 12 organiques : stelvision.com (carte du ciel temps réel), **kitcieletoile.com (marchand
spécialiste)**, observatoire-interactif.com, Pinterest ×2, Amazon, **pixlumshop.fr (marchand)**,
magnific.com (banque d'images), YouTube, National Geographic, Wikipédia, edouard-cribier.fr.
**2 résultats marchands sur 12.** C'est la base de l'adjudication de §6.

### `planetarium` — 22 200 — **navigationnel / lieu, zéro commerce**
**12 blocs `local_pack`** (Vulcania, Nantes, Jardin des sciences, Cité de l'espace, Nançay,
Cité des sciences, Palais de la découverte, Peiresc…), knowledge graph « Planétarium »,
PAA « Quel est le plus grand Planétarium de France ? ».
Organiques : planetarium.nantesmetropole.fr, cite-sciences.fr, planetarium.saint-etienne.fr,
planetariumvv.com, cite-espace.com, reims.fr, espace-sciences.org, aix-planetarium.fr, Wikipédia,
cosmocite.fr, unistra.fr, museeairespace.fr.
**Aucun marchand, aucun bloc produit. Part adressable : 0 %.**

### `système solaire` — 60 500 — **scolaire pur, zéro commerce**
AI overview, knowledge graph, PAA (« Comment retenir les 8 planètes ? »).
Organiques : Wikipédia, CNES, Réseau Canopé, ESA, Vikidia, Maxicours (Collège Physique-Chimie),
Lumni, astrojuniors.fr, maitrelucas.fr (CM1 CM2), Larousse, National Geographic.
**Aucun marchand, aucun bloc produit. Part adressable : 0 %.**

### `carte du ciel` — 5 400 — **astrologie + carte gratuite**
Aucun bloc produit. Organiques : stelvision.com, application Google Play, astronomes.com,
**monoeuvre.fr « Carte du ciel étoilé personnalisée −49 % » (marchand)**,
observatoire-interactif.com, noovomoi.ca (astrologie), odysseysdream.com (astrologie),
istockphoto, Skychart (logiciel libre), **boutique.afastronomie.fr (association)**, Pinterest
« Carte Du Ciel Astrologie », evozen.fr (astrologie).
PAA : « Comment interpréter la carte du ciel ? », « Où puis-je trouver une carte du ciel gratuite
en direct ? ». **Le mot français « carte du ciel » veut d'abord dire thème astral, ensuite carte
céleste temps réel gratuite, et seulement en quatrième position un poster vendu.**

### `lampe lune` — 1 900 — **commercial pur**
**8 blocs `popular_products`**. **Prix observés** : 14 · 15,15 · 16,95 · 18,26 · 18,79 · 18,86 ·
18,88 · 19,65 · 20,99 · 21,50 · 22,20 · 22,80 · 23,59 · 23,60 · 23,97 · 23,99 · 24,99 · 25,86 ·
25,99 · 26,31 · 26,99 · 27,76 · 31,36 · 32,61 · 34,32 · 34,88 · 34,93 · 39,99 · 44,99 · 70,99 ·
73,90 · 165,99 · 175,08 €. **33 prix relevés, médiane 24,99 €.** Les seuls prix > 70 € sont les lampes
« en lévitation » et deux références isolées.
- *Spécialistes / DTC* : lustria.fr, enseigneplus.fr, celekado.com (personnalisation photo),
  lampephoto.fr, MyBouddha, Déco Science.
- *Marketplaces / enseignes* : Nature & Découvertes (O1), Leroy Merlin, Conforama, Amazon, Fnac,
  Darty, Castorama, Cdiscount, ManoMano, Vertbaudet.

### `veilleuse` — 14 800 — **commercial, mais univers puériculture**
3 blocs `popular_products`. Prix 5,99 à 36,99 €.
Spécialistes : madouceveilleuse.com (« N°1 en France »), lenny-et-alba.com, larmoiredebebe.com,
Le Petit Souk, Emmie-Sphère. Enseignes : Leroy Merlin, Castorama, Vertbaudet, Orchestra,
Autour de Bébé, Carrefour, Nature & Découvertes.
**L'intention est « chambre de bébé », pas « déco astronomique ».** Un seul produit astro
apparaît dans les carrousels (`Little l — veilleuse lune blanche`, 27,90 €).
**Cette famille appartient à un autre univers : sortie du périmètre.**

### Saisonnalité — lecture qualitative
Séries 12 mois (`google_ads/search_volume`, août 2025 → juillet 2026) :
`ciel étoilé` est **plat** — 9 900 à 18 100, pointes en août et décembre, amplitude ×1,8.
`projecteur ciel étoilé` est **nettement saisonnier Q4** — creux à 720 en juin, **pointes à 4 400
en novembre et décembre**, amplitude ×6,1. C'est un produit-cadeau de Noël, ce qui est cohérent
avec le positionnement Q4 recherché ; c'est aussi la fenêtre la plus concurrentielle.
`système solaire` suit le **calendrier scolaire** — 90 500 en septembre et janvier, 40 500 en
juillet : preuve supplémentaire, indépendante de la SERP, que ce volume est celui d'élèves.
`planétarium` est plat, sans signature commerciale.

---

## 6. La question de méthode : DataForSEO fusionne-t-il `ciel etoile` et `ciel étoilé` ?

Point demandé explicitement au brief. La mémoire maison retient un écart **jusqu'à ×8 sur
SEMrush** entre formes accentuée et non accentuée. Critère de preuve retenu (issu du rejeu
rideaux) : **l'égalité de volume ne prouve rien, l'égalité de la série mensuelle prouve.**

| Paire | Volume accentué | Volume non accentué | CPC | Séries 12 mois identiques ? | Conclusion |
|---|---:|---:|---|---|---|
| `ciel étoilé` / `ciel etoile` | 12 100 | 12 100 | 0,39 / 0,39 | **oui, mois par mois** | **même bucket** |
| `projecteur ciel étoilé` / `projecteur ciel etoile` | 1 900 | 1 900 | 0,22 / 0,22 | **oui, mois par mois** | **même bucket** |
| `système solaire` / `systeme solaire` | 60 500 | 60 500 | 0,06 / 0,06 | **oui, mois par mois** | **même bucket** |
| `planétarium` / `planetarium` | 12 100 | **22 200** | 0,36 / **0,94** | **NON** | **buckets distincts** |

Séries comparées pour la paire divergente (juil. 2026 → août 2025) :
`planétarium` : 12 100 · 9 900 · 12 100 · 14 800 · 12 100 · 18 100 · 12 100 · 12 100 · 12 100 ·
14 800 · 8 100 · 9 900.
`planetarium` : 18 100 · 12 100 · 18 100 · 22 200 · 18 100 · 27 100 · 18 100 · 18 100 · 27 100 ·
27 100 · 14 800 · 22 200.
La forme non accentuée est **strictement supérieure chaque mois**, dans un rapport de 1,4 à 2,2 ;
les deux séries sont corrélées mais jamais égales, et le CPC est presque triplé.

### Réponse

**Non, DataForSEO ne fusionne pas systématiquement les accents — mais il les fusionne dans la
grande majorité des cas, et bien plus souvent que SEMrush.** Trois paires sur quatre sont
rigoureusement le même bucket Google : même volume, même CPC, même concurrence, même série
mensuelle au mois près. **Sur ces paires-là, interroger les deux orthographes est inutile, et
sommer les deux serait une double comptabilisation pure.**

La quatrième paire diverge pour une raison identifiable : **`planetarium` sans accent n'est pas
une variante orthographique du français, c'est un mot d'une autre langue.** Il s'écrit ainsi en
anglais, en allemand et en néerlandais, et le champ non accentué remonte effectivement
`hamburg planetarium`, `copenhagen planetarium`, `adler planetarium chicago`, `planetarium near
me`, `planetarium projector` — des requêtes émises depuis la France mais pas en français. Le CPC
à 0,94 contre 0,36 confirme qu'on regarde deux populations différentes. *(Hypothèse explicative,
cohérente avec les données ; elle n'est pas démontrée par l'outil.)*

### Règle opérationnelle à retenir pour tous les dossiers

1. **Interroger les deux orthographes reste obligatoire** — le coût est nul (cache) et le cas
   `planétarium` montre que la divergence existe.
2. **Trancher par la série mensuelle, jamais par le volume seul.** Séries identiques → un seul
   bucket, on garde une seule idée. Séries différentes → deux buckets, on garde le **MAX**, jamais
   la somme, tant qu'il n'est pas prouvé qu'ils sont disjoints.
3. **Suspecter la divergence quand la forme non accentuée est aussi un mot étranger**
   (`planetarium`, `parasol`, `festival`, `menu`…). C'est là que le risque de sur-comptage se
   loge, pas sur les accents français ordinaires.
4. Conséquence pour la comparaison d'outils : l'écart ×8 observé sur SEMrush entre `ciel etoile`
   et `ciel étoilé` **ne se reproduit pas ici**. Sur ce point précis, **DataForSEO est plus fidèle
   au comportement réel de Google que SEMrush**, et le protocole SEMrush « interroger les deux et
   additionner » aurait ici surévalué la famille de 12 100 recherches/mois.

---

## 7. Consolidé net et verdict — écrit avant toute lecture du 15/08

### Adjudication des têtes génériques, justifiée par la SERP

| Tête | Volume | Part adressable retenue | Volume retenu | Justification SERP |
|---|---:|---:|---:|---|
| `système solaire` | 60 500 | 0 % | 0 | SERP 100 % encyclopédique et scolaire ; CPC 0,06 ; saisonnalité scolaire |
| `galaxie` | 27 100 | 0 % | 0 | racine polluée, champ à 264 910 de pop-culture |
| `planetarium` | 22 200 | 0 % | 0 | 12 `local_pack`, knowledge graph, zéro marchand |
| `astronaute` | 22 200 | 0 % | 0 | actualité et orientation métier |
| `veilleuse` | 14 800 | 0 % | 0 | commercial mais univers puériculture, autre boutique |
| `ciel étoilé` | 12 100 | **25 %** | **3 025** | 2 marchands sur 12 organiques, aucun bloc produit |
| `carte du ciel` | 5 400 | **15 %** | **810** | 1 marchand produit + 1 boutique associative sur 12 ; dominante astrologie |

### Consolidé

| | Volume |
|---|---:|
| Familles adressables, hors têtes (§2) | 38 570 |
| Têtes adjugées par SERP | 3 835 |
| **CONSOLIDÉ NET ADRESSABLE** | **42 405** |

### Sensibilité — le verdict tient-il si j'ai mal adjugé les têtes ?

| Scénario | Consolidé | vs seuil 37 500 |
|---|---:|---|
| **Strict** — têtes à 0 % | 38 570 | +3 % |
| **Retenu** — `ciel étoilé` 25 %, `carte du ciel` 15 % | **42 405** | **+13 %** |
| **Large** — `ciel étoilé` 50 %, `carte du ciel` 30 % | 46 240 | +23 % |

Les trois scénarios sont **au-dessus du plancher 37 500 et en dessous du confort 50 000**.
Deux des trois tombent **à l'intérieur de la bande de cas limite 30 000 – 45 000**.

### Verdict

> ## CAS LIMITE — décision Hakim requise
>
> Consolidé net **42 405/mois**, contre un plancher UNIVERS de **37 500** et une bande de cas
> limite de **30 000 – 45 000** (`PRODUCT-RESEARCH-CRITERIA.md` §1, décision Hakim du 29/08/2026).
> **42 405 est dans la bande.** Je ne tranche pas le volume.

**Éléments du côté « ça passe » :**
- Le consolidé dépasse le plancher dans les trois scénarios de sensibilité, y compris le plus
  sévère (38 570).
- Deux familles ont une intention d'achat pure, une SERP saturée de blocs produits et une
  concurrence publicitaire `HIGH` : projecteur ciel étoilé (11 320) et lampe/veilleuse astro
  (12 050) — **23 370 à elles deux, soit 55 % du consolidé.**
- Des spécialistes DTC existent et tiennent la page 1 (science-labs.com, lustria.fr,
  kitcieletoile.com, lampephoto.fr, celekado.com) : la preuve qu'une boutique spécialisée peut
  exister est faite.
- Saisonnalité Q4 marquée sur le produit cœur (×6,1 en novembre-décembre), cohérente avec le cap
  Q4 2026.

**Éléments du côté « ça ne passe pas » :**
- **La barrière prix est franche et elle ne relève pas d'une appréciation.** Médiane observée
  31,69 € sur `projecteur ciel étoilé`, 24,99 € sur `lampe lune` ; 35 des 39 prix relevés sur le
  produit cœur sont sous 50 €. `PRODUCT-RESEARCH-CRITERIA.md` §1 fixe la cible à
  **50–400 € TTC** et exclut explicitement le gadget. **Le cœur du dossier est structurellement
  sous le plancher de prix.**
- **La domination des enseignes généralistes est celle que le §4 rejette nommément.** Amazon,
  Leroy Merlin, Fnac, Darty, Cdiscount, Conforama, Castorama, ManoMano, Action, Nature &
  Découvertes et Vertbaudet occupent la totalité des carrousels produits sur les deux têtes
  commerciales.
- **Le consolidé est fragile par construction** : 80 % du volume net de marque a dû être retiré
  pour cause d'intention (189 880 → 38 570). Un dossier dont la mesure repose sur un tri d'aussi
  forte amplitude est par nature moins robuste qu'un dossier où le volume brut est déjà propre.
- Quatre des cinq plus gros volumes du champ (`système solaire`, `galaxie`, `planetarium`,
  `astronaute`) sont à **exactement zéro** d'adressable. L'univers « astro » a l'apparence d'un
  grand marché et n'en est pas un.

**Ce que je recommande à Hakim de trancher** : le volume passe le plancher, mais de peu et par une
reconstruction fragile ; **le prix et la concurrence, eux, échouent sans ambiguïté aux §1 et §4.**
Si la porte de volume était la seule, ce dossier mériterait un `REVIEW`. Compte tenu du plancher
de prix 50 € et de l'occupation GSB, ma lecture technique penche vers
`STOP_PREQUALIFICATION`, **mais je n'exerce pas cette bascule à la place de Hakim tant que le
volume est en zone limite.**

---

## 8. Comparaison des deux chaînes

Référence ouverte **après** la rédaction de la §7 :
`analyses/2026-08-15-niches-univers/U4-astronomie/02-volume-consolide-u4b.md`
(15/08/2026, SEMrush Keyword Magic Tool, base France `db=fr`, `mt=phrase`, 18 requêtes, 0 crédit).

### 8.1 Les deux verdicts

| | 15/08 — SEMrush | 29/08 — DataForSEO |
|---|---|---|
| Seuil applicable | 30 000 (confort 40 000) | 37 500 (confort 50 000) |
| Consolidé retenu | **24 830** (périmètre strict A) | **42 405** |
| Périmètre le plus large mesuré | 30 970 (périmètre C) | 47 095 (après complétion, §8.4) |
| Distance au seuil | **−17 %** | **+13 %** |
| Verdict | **STOP volume** — « sous les 30 000 dès qu'on s'en tient au cœur du sujet », déficit 5 170 | **CAS LIMITE — décision Hakim requise** |

> ### Le verdict bascule.
> Le 15/08 concluait **STOP** avec un déficit de 5 170 sur un plancher de 30 000.
> Le 29/08 rend un consolidé **au-dessus** de son plancher recalibré, dans la bande de cas limite.
> **La chaîne DataForSEO ne reproduit pas le verdict SEMrush en zone de décision.**
> C'est un échec du test de non-régression, et il est écrit tel quel.

### 8.2 Famille par famille — où l'écart se loge

Les deux mesures utilisent des découpages proches mais pas identiques. Correspondances établies
après lecture ; « attendu » = valeur SEMrush × 1,25 (facteur médian de calibration du 29/08).

| Famille | SEMrush 15/08 (net de marque) | DataForSEO 29/08 (net final) | Attendu ×1,25 | Écart réel |
|---|---:|---:|---:|---:|
| Projecteurs d'ambiance | 13 460 | 11 320 | 16 825 | **×0,84** |
| Lampes et veilleuses | 7 510 | 12 050 | 9 388 | **×1,60** |
| Kit ciel étoilé fibre optique plafond | 2 510 | 1 870 | 3 138 | **×0,75** |
| Stickers étoiles phosphorescentes | 2 280 | *(graine non interrogée)* | 2 850 | **lacune, §8.4** |
| Objets décoratifs + planétarium produit | 1 080 | 4 260 | 1 350 | ×3,9 |
| Carte du ciel imprimée | 470 | 1 510 | 588 | ×3,2 |
| Décoration murale | 390 | 3 510 | 488 | **×9,0** |
| Textile de maison | 110 | *(fondu dans objets déco)* | 138 | — |
| Maquette système solaire | 3 160 | **0** — sortie comme scolaire | 3 950 | **divergence de périmètre** |
| **`ciel étoilé` comme famille propre** | **non isolée** | **7 885** | — | **famille nouvelle** |

**Les écarts ne vont pas tous dans le même sens, et c'est le point important.** Sur les deux
familles les mieux définies des deux côtés — projecteurs et kit fibre optique — **DataForSEO rend
moins que SEMrush** (×0,84 et ×0,75), alors que la calibration prédisait ×1,25. L'outil ne gonfle
pas mécaniquement. Les écarts massifs (×3,2, ×3,9, ×9,0) portent tous sur des familles que le
15/08 avait déclarées quasi vides et qui pèsent peu en absolu.

### 8.3 Quelle famille fait basculer le verdict

Décomposition de l'écart entre le périmètre le plus large du 15/08 (30 970) et le consolidé du
29/08 (42 405) :

| Contribution | Δ |
|---|---:|
| **`ciel étoilé` érigé en famille propre** (traîne produit 4 860 + 25 % de la tête 3 025) | **+7 885** |
| Objets déco + carte du ciel + décoration murale (9 280 contre 1 940) | +7 340 |
| Lampes et veilleuses au-dessus de la calibration (12 050 contre 7 510, ×1,60) | +4 540 |
| Maquette système solaire, comptée le 15/08, sortie le 29/08 comme scolaire | −3 160 |
| Projecteurs (−2 140) et kit fibre optique (−640), sous la calibration | −2 780 |
| Stickers phosphorescents, graine non interrogée en aveugle (§8.4) | −2 280 |
| Textile de maison, fondu dans « objets déco » | −110 |
| **Écart total** | **+11 435** |

La décomposition boucle exactement : 42 405 − 30 970 = 11 435.

> **La famille qui fait basculer le verdict est `ciel étoilé` traité comme une famille à part
> entière.** Le 15/08 ne l'a jamais isolée : il a versé 3 570 de `ciel étoilé` dans la famille
> « projecteurs » et n'a pas compté le reste du champ (`ciel étoilé chambre`, `ciel étoilé
> mariage`, `tissu ciel étoilé`, `ciel étoilé prix`, ni aucune part de la tête à 12 100).
>
> **Contrôle décisif : si l'on retire cette seule famille du consolidé du 29/08, on obtient
> 34 520 — sous le plancher de 37 500, soit exactement le même verdict STOP qu'au 15/08.**

Autrement dit : **le désaccord entre les deux chaînes n'est pas un désaccord sur les chiffres,
c'est un désaccord sur le périmètre.** Les deux outils lisent la même chose sur les familles
communes ; ils divergent parce que les deux analystes n'ont pas découpé l'univers de la même
façon. Le facteur ×1,25 recalibre un seuil ; **il ne protège contre rien de tout cela.**

### 8.4 Une lacune de couverture — et sa correction, qui n'est plus en aveugle

Le rapport du 15/08 a utilisé 18 graines, dont six que je n'avais pas interrogées :
`étoiles phosphorescentes`, `projecteur etoile`, `veilleuse etoile`, `figurine astronaute`,
`globe lune`, `housse de couette espace`. Deux d'entre elles portaient un volume réel.
**Cette lacune a été comblée après lecture de la référence : la correction n'est donc plus en
aveugle, et elle est présentée séparément du verdict de la §7, qui reste le résultat du test.**

| Graine ajoutée | Apport net nouveau (après dédup contre le corpus existant et retrait des marques) |
|---|---:|
| `projecteur étoile` | +2 670 (`projecteur étoile` 1 300, `plafond étoile projecteur` 1 000, `lampe projecteur étoile` 260) |
| `étoiles phosphorescentes` | +2 020 (`étoiles phosphorescentes` 1 300, `+ plafond` 390) |
| `figurine astronaute` / `globe lune` / `housse de couette espace` | 170 / 70 / 110 — déjà couverts ou négligeables |

Consolidé après complétion : **47 095/mois** (+11 % sur le chiffre en aveugle). Il sort de la bande
de cas limite par le haut, mais **reste sous le confort de 50 000**.

### 8.5 Le résultat le plus utile de la session : SEMrush a sur-compté les variantes non accentuées

Le rapport du 15/08 présente comme une **« découverte majeure »** le fait que
« les variantes non accentuées sont des lignes KMT distinctes » et attribue **6 350 recherches sur
les 13 460 de la famille projecteurs** à des formulations non accentuées « jamais lues » —
`ciel etoile projecteur` 1 300 étant donné comme « invisible depuis une lecture de `ciel étoilé` ».

La §6 de ce rapport démontre l'inverse au niveau du volume Google. Sept paires testées :

- `projecteur ciel étoilé` / `projecteur ciel etoile` : 1 900 / 1 900, **séries mensuelles
  identiques mois par mois** ;
- `projecteur étoile` / `projecteur etoile` / `projecteur étoiles` : 1 300 / 1 300 / 1 300,
  séries identiques ;
- `veilleuse étoile` / `veilleuse etoile` : 880 / 880, séries identiques ;
- `étoiles phosphorescentes` / `etoiles phosphorescentes` / `étoile phosphorescente` :
  1 300 / 1 300 / 1 300, séries identiques ;
- `ciel étoilé` / `ciel etoile` : 12 100 / 12 100, séries identiques ;
- `système solaire` / `systeme solaire` : 60 500 / 60 500, séries identiques ;
- seule exception : `planétarium` / `planetarium`, 12 100 / 22 200, séries **différentes** — et
  pour une raison de langue, pas d'accent (§6).

**Ce sont, sur ces six paires, le même bucket Google.** SEMrush les sert comme des lignes KMT
distinctes parce que son corpus est indexé sur la chaîne de caractères ; Google, lui, sert une
seule demande. **Additionner les deux, comme l'a fait la consolidation du 15/08, compte deux fois
la même recherche.**

C'est très probablement la cause de l'inversion la plus contre-intuitive de la §8.2 : la famille
projecteurs mesure **11 320 chez DataForSEO contre 13 460 chez SEMrush**, alors que DataForSEO
rend d'ordinaire ×1,25. Le sur-comptage accentué/non accentué explique l'essentiel de la
différence, et il joue **dans le sens qui gonfle** le dossier du 15/08.

**Conséquence pratique, et elle est franche :** le protocole SEMrush maison — « interroger les
deux orthographes et additionner » — **est erroné**, et il l'a été sur tous les dossiers où il a
été appliqué. La note mémoire `variantes-sans-accent-kmt.md` (écart jusqu'à ×8 entre
`ciel etoile` et `ciel étoilé`) décrit un artefact de l'index SEMrush, **pas une réalité de la
demande française**. La règle correcte est celle de la §6 : interroger les deux, **trancher par la
série mensuelle**, garder le MAX, ne jamais sommer.

---

## 9. La question qui compte : peut-on résilier SEMrush sur cette base ?

### 9.1 Réponse à la question posée

**Non — pas *sur cette base*. Le test de non-régression en zone de décision échoue : le verdict
bascule.** Un dossier conclu STOP à −17 % du plancher SEMrush ressort à +13 % du plancher
DataForSEO. La chaîne ne reproduit pas le verdict là où on l'attendait le plus.

### 9.2 Mais la cause n'est pas celle qu'on redoutait

Le risque anticipé au §1 de `PRODUCT-RESEARCH-CRITERIA.md` était que **la dispersion tête à tête**
de DataForSEO (écart-type 2,65, étendue ×0,03 à ×31) fasse basculer un verdict serré. **Ce n'est
pas ce qui s'est passé.** Sur les familles que les deux chaînes découpent pareil, les chiffres
concordent, et DataForSEO rend même **moins** que SEMrush sur les deux familles cœur.

Les trois causes réelles de la bascule, dans l'ordre de leur poids :

1. **Le périmètre, pas l'outil (+7 885, soit 69 % de l'écart).** Le 15/08 n'a jamais érigé
   `ciel étoilé` en famille. Retirez cette famille et les deux chaînes rendent le même STOP.
   **Un analyste SEMrush qui aurait découpé comme moi aurait trouvé au-dessus du seuil, lui aussi.**
2. **Une erreur de méthode côté SEMrush qui gonflait le 15/08 (§8.5)** — l'addition des variantes
   accentuées et non accentuées. Elle joue en sens inverse, et elle rendait la mesure du 15/08
   *plus généreuse* qu'elle n'aurait dû l'être. Le vrai STOP du 15/08 était donc encore plus net
   que ce que le rapport affiche.
3. **Une lacune de couverture de mon côté (§8.4)**, révélée par la référence : deux graines
   manquantes valant 4 690 nets.

**Aucune de ces trois causes n'est un défaut de DataForSEO comme source de volume.** Deux d'entre
elles sont des défauts de méthode, symétriques, un de chaque côté.

### 9.3 Ce que je recommande

- **Sur le plan de la donnée de volume, la résiliation est défendable.** DataForSEO a rendu ici
  16 graines, 10 218 idées, 7 SERP, des séries mensuelles et un contrôle témoin, pour **≈ 3,4 USD**
  contre 149 €/mois. Sur les familles comparables, il concorde. Il a de surcroît **corrigé une
  erreur de méthode que SEMrush entretenait** (les accents).
- **Sur le plan du protocole, la résiliation ne doit pas être adossée à ce test.** Ce rejeu montre
  que **la variable qui décide d'un dossier en zone limite est le découpage en familles, pas
  l'outil.** Tant que la liste des familles n'est pas figée *avant* la mesure, deux passages du
  même dossier — avec le même outil — pourront rendre deux verdicts. C'est le chantier à ouvrir,
  et il est indépendant de SEMrush.
- **Trois garde-fous à écrire avant de couper**, faute de quoi on perdra le filet sans avoir
  installé le remplaçant :
  1. **Liste des familles arrêtée et écrite avant la première mesure**, avec ce qui est dedans et
     ce qui est dehors ; toute famille ajoutée en cours de route est signalée comme telle.
  2. **Règle des accents de la §6** substituée au protocole actuel dans le playbook et dans la
     note mémoire `variantes-sans-accent-kmt.md`, qui est à corriger.
  3. **Adjudication des têtes génériques par SERP obligatoire et chiffrée**, avec le tableau de
     sensibilité de la §7. C'est ce qui a évité ici de porter 60 500 de `système solaire` scolaire
     et 22 200 de `planetarium`-lieu au crédit du dossier.
- **Et une réserve de calendrier** : le seuil DataForSEO de 37 500 repose sur un facteur ×1,25
  établi sur **trois échantillons**. Ce rejeu en fournit un quatrième, et il n'est **pas
  concordant** : ×0,84 et ×0,75 sur les deux familles cœur. Le facteur mérite d'être ré-estimé
  avant que le seuil recalibré ne serve à trancher d'autres dossiers serrés.

### 9.4 Et le dossier astro lui-même ?

**Le statut `STOP` du 15/08 ne doit pas être levé sur la foi de ce rejeu.** Le consolidé passe le
plancher, mais :
- il le passe **par une famille que la mesure de référence n'avait pas retenue** ;
- il ne passe **jamais le seuil de confort** (50 000), dans aucun des scénarios ;
- et surtout, **le dossier échoue à deux critères qui ne dépendent d'aucun outil** : la médiane de
  prix observée est de 25 à 32 € contre un plancher de 50 € (§1 des critères), et les carrousels
  produits sont intégralement tenus par Amazon, Leroy Merlin, Fnac, Darty, Cdiscount, Conforama,
  Castorama, ManoMano, Action et Nature & Découvertes — la liste que le §4 rejette nommément.

Ma recommandation reste celle de la §7 : **CAS LIMITE sur le volume, décision Hakim** ; et une
lecture technique qui, prix et concurrence compris, penche vers `STOP_PREQUALIFICATION`.

---

## 10. Réserves — aucune retirée

**R1 — L'API DataForSEO renvoie par intermittence un `result` vide.** Deux occurrences en une
session (§1.5). Le contrôle témoin les a attrapées les deux fois **parce qu'il était en position
de sortie**. Le même vide sur un appel de données produirait un **zéro silencieux** indétectable :
une graine reviendrait à 0 idée et serait lue comme « famille inexistante ». `kw_dfs.py` ne
distingue aujourd'hui pas « 0 résultat » de « résultat vide par incident ». **À corriger dans le
script avant de faire de DataForSEO la source unique.**

**R2 — L'aveuglement a été rompu volontairement en §8.4.** Les +4 690 de complétion de couverture
ont été mesurés après lecture de la référence. Le verdict du test reste celui de la §7 (42 405) ;
le 47 095 est un addendum documenté, pas un résultat de test.

**R3 — L'audit SERP est passé par l'API, pas par un navigateur.** La navigation directe vers
google.fr a été refusée par l'environnement. Conséquence : **je ne peux pas isoler les annonces
Search texte.** Les blocs lus sont des `popular_products` — des carrousels produits sponsorisés.
Je ne les présente jamais comme des annonces texte confirmées. La densité publicitaire Search
réelle sur `projecteur ciel étoilé` et `lampe lune` reste **non vérifiée**.

**R4 — Deux graines restent tronquées.** `veilleuse` (3 000 lignes lues sur 12 681 annoncées) et
`planetarium` (2 000 sur 2 528). Le tri par volume décroissant rend l'amputation conservatrice, et
elle porte sur les deux graines les plus hors périmètre — mais elle n'est pas nulle.

**R5 — L'adjudication des têtes est un jugement, pas une mesure.** Les 25 % retenus sur
`ciel étoilé` et les 15 % sur `carte du ciel` sont des estimations fondées sur le comptage des
résultats marchands en page 1. Le tableau de sensibilité de la §7 en donne l'amplitude
(38 570 → 46 240) ; aucun de ces chiffres n'est une lecture d'outil.

**R6 — Le facteur de calibration ×1,25 est contredit par ce dossier.** ×0,84 sur les projecteurs,
×0,75 sur le kit fibre optique. Le seuil de 37 500 en dépend directement. Ce rejeu ne suffit pas à
le réviser, mais il ne le confirme pas.

**R7 — Le tronc générique n'est pas remonté par l'endpoint de découverte.** Les têtes ont dû être
mesurées séparément. Une tête oubliée est invisible, et rien dans l'outil ne le signale.

**R8 — Aucune donnée d'aucune autre base que France.** Aucun sourcing, aucune fiche fournisseur,
aucune cartographie de concurrence, aucun `GO_FINAL`. Aucune requête SEMrush.

**R9 — Le classement en familles a été écrit puis corrigé trois fois** (§1.6). Les deux premières
versions comportaient des faux positifs de sous-chaîne (`étoile`→`toile`, `astronaute`→`astro`).
La version retenue travaille à frontière de mot sur l'expression réelle. Un classement
automatique reste un classement automatique : les 27 % de volume situés sous 300 recherches/mois
n'ont pas été audités ligne à ligne.

**R10 — Écart de date.** Session ouverte et mesurée le 2026-08-29 ; l'horloge machine indiquait
2026-08-30 00:59 CEST pendant la rédaction. Le nom de fichier et l'en-tête suivent la consigne du
brief (29/08) ; l'écart est signalé ici plutôt que masqué.
