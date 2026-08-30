# Archive des corpus SEMrush — 29/08/2026

**Ces données ne sont plus reproductibles.** L'abonnement SEMrush a été résilié le 29/08/2026. Chaque fichier est une photographie du Keyword Magic Tool en expression exacte, base France, devise EUR, prise le 29/08 avant la coupure.

**33 expressions sur 33 capturées, aucun échec.** 3 300 lignes de mots-clés, 6 177 650 de volume cumulé sur les corpus.

## Ce que contient chaque fichier

| Champ | Sens |
|---|---|
| `total_mots_cles` | La taille du corpus que SEMrush annonce pour cette expression |
| `volume_total` | Le volume que SEMrush annonce pour ce corpus. **Ce n'est pas un volume de famille** — il inclut tout le bruit |
| `barre_par_nombre` | Les tokens co-occurrents et leurs occurrences. **C'est la partie la plus précieuse** : elle porte la structure sémantique du corpus, et aucun autre outil ne la redonne |
| `lignes` | Les 100 premières lignes du tableau : mot-clé, volume, KD, CPC, intention |
| `base`, `devise`, `lu_le` | Contrôlés page par page : `fr` et `EUR` partout |

## Inventaire

### Rideaux — le seul PASS_PREQUALIFICATION du parc

| Expression | Corpus | Volume total | Tokens de barre | Lignes | dont KD absent |
|---|---:|---:|---:|---:|---:|
| `rideau occultant` | 17 570 | 297 700 | 200 | 100 | 0 |
| `rideau thermique` | 6 953 | 216 150 | 100 | 100 | 0 |
| `rideau phonique` | 1 421 | 26 760 | 100 | 100 | 20 |
| `rideau velours` | 3 201 | 38 290 | 50 | 100 | 1 |
| `rideau lin` | 7 228 | 92 760 | 50 | 100 | 0 |
| `voilage` | 60 906 | 385 080 | 50 | 100 | 0 |
| `tringle a rideau` | 9 335 | 90 170 | 50 | 100 | 0 |
| `double rideau` | 13 252 | 120 760 | 50 | 100 | 1 |

### Vin & œnologie

| Expression | Corpus | Volume total | Tokens de barre | Lignes | dont KD absent |
|---|---:|---:|---:|---:|---:|
| `tire bouchon` | 18 734 | 206 370 | 50 | 100 | 0 |
| `limonadier` | 1 781 | 24 660 | 200 | 100 | 61 |
| `carafe vin` | 3 004 | 27 630 | 200 | 100 | 33 |
| `decanteur` | 2 988 | 12 460 | 200 | 100 | 76 |
| `aerateur vin` | 618 | 9 490 | 200 | 100 | 89 |
| `bouchon vin` | 5 366 | 36 000 | 200 | 100 | 7 |
| `verre a vin` | 8 108 | 80 170 | 200 | 100 | 0 |
| `coffret sommelier` | 377 | 2 700 | 200 | 100 | 96 |
| `oenologie` | 17 546 | 72 520 | 200 | 100 | 0 |

### Diffusion olfactive

| Expression | Corpus | Volume total | Tokens de barre | Lignes | dont KD absent |
|---|---:|---:|---:|---:|---:|
| `diffuseur huile essentielle` | 16 627 | 171 030 | 150 | 100 | 0 |
| `diffuseur parfum maison` | 293 | 7 350 | 150 | 100 | 82 |
| `bougie parfumee` | 1 279 | 13 350 | 250 | 100 | 56 |
| `recharge diffuseur` | 1 733 | 13 190 | 150 | 100 | 53 |
| `parfum interieur` | 1 600 | 6 250 | 200 | 100 | 85 |
| `diffuseur voiture` | 1 260 | 18 550 | 150 | 100 | 53 |

### Arts de la table bois

| Expression | Corpus | Volume total | Tokens de barre | Lignes | dont KD absent |
|---|---:|---:|---:|---:|---:|
| `plateau bois` | 15 955 | 118 360 | 150 | 100 | 0 |
| `plateau de service` | 1 767 | 14 860 | 150 | 100 | 59 |
| `planche apero` | 1 312 | 47 800 | 100 | 100 | 5 |
| `dessous de plat` | 6 407 | 24 670 | 200 | 100 | 39 |
| `plateau charcuterie` | 2 269 | 56 310 | 150 | 100 | 1 |

### Candidats suspendus ou à rouvrir

| Expression | Corpus | Volume total | Tokens de barre | Lignes | dont KD absent |
|---|---:|---:|---:|---:|---:|
| `aquarium` | 399 018 | 2 996 130 | 150 | 100 | 0 |
| `aquascaping` | 5 711 | 24 610 | 100 | 100 | 72 |
| `terrarium` | 51 092 | 299 500 | 150 | 100 | 0 |
| `hamac` | 46 811 | 406 710 | 150 | 100 | 0 |
| `coffre de toit` | 20 938 | 219 310 | 150 | 100 | 0 |

## Trois limites à connaître avant de s'en servir

**1. La barre « Par nombre » n'est pas dépliée à la même profondeur partout.** De 50 à 250 tokens selon l'expression, 150 dans la majorité des cas. Le bouton « Afficher plus » de SEMrush ne répond pas de façon fiable à un clic programmatique, et un onglet en arrière-plan est bridé par Chrome. Chaque fichier dit ce qu'il contient ; aucune profondeur n'est présentée pour ce qu'elle n'est pas.

**2. Le KD et l'intention manquent sur une partie des lignes.** SEMrush affiche « Pour afficher les métriques, actualisez la page » sur les mots-clés à faible volume, et actualiser consomme des crédits — ce qui n'avait pas été demandé. Ces lignes portent `kd: null` et une intention vide. Le volume et le CPC, eux, sont ceux affichés. La colonne « dont KD absent » ci-dessus donne l'ampleur, expression par expression : nulle sur les gros corpus, jusqu'à 96 lignes sur 100 pour `coffret sommelier`.

**3. Deux discontinuités dans la barre**, sur `planche apero` (saut de `fabriquer:7` à `geant:4`) et `dessous de plat` (saut de `métal:43` à `chantourner:12`). SEMrush ne charge pas les tokens intermédiaires. Recopié tel quel, sans comblement.

## Ce qu'il ne faut pas en faire

- **Ne pas réutiliser un volume comme s'il était frais.** Ces chiffres sont datés du 29/08/2026. Un chiffre se remesure, ou se cite avec sa date et sa source.

- **Ne pas prendre `volume_total` pour un volume de famille.** C'est le total brut du corpus, bruit compris — sur le témoin `tufting`, SEMrush affichait 78 920 quand la tête réelle valait 8 100. La consolidation par familles reste à faire, ligne par ligne.

- **Ne pas comparer un KD d'ici à un KD DataForSEO.** Ils ne mesurent pas la même chose et ne sont pas convertibles (corrélation de rangs 0,225).

## Voir aussi

`mesures-consolidees.json` / `.csv` dans ce dossier : 287 mots-clés appariés SEMrush × DataForSEO, avec leur ratio. C'est l'étalon de calibrage.

La migration et ses tests : `analyses/2026-08-29-croisement-semrush-dataforseo.md`, `2026-08-29-validation-3-graines-aveugle.md`, `2026-08-29-tests-fenetre-semrush.md`, et les trois rejeux (`rideaux`, `gothique`, `astro`).
