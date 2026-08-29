# Croisement SEMrush x DataForSEO - 181 mots-cles

**Date : 2026-08-29** - Demande par Hakim pour instruire la question de l'abonnement SEMrush (149 EUR/mois).

Source SEMrush : les 4 rapports Mission B du 28/08 (`analyses/2026-08-28-mission-b-univers/`), volumes de **tete** uniquement - aucune somme de grappe n'entre dans la comparaison.  
Source DataForSEO : endpoint `keywords_data/google_ads/search_volume/live`, `location_name: France`, `language_name: French`, `search_partners: false`. **Cout total : 0,09 USD.**

## Verdict

**DataForSEO n'est pas substituable a SEMrush pour notre methode.** Deux raisons, mesurees, pas supposees.

### 1. La divergence est erratique, pas constante - donc pas de coefficient

| Statistique | Rapport DataForSEO / SEMrush |
|---|---|
| Mediane | x1.23 |
| Moyenne | x1.76 |
| **Ecart-type** | **2.65** |
| 1er quartile | x1.00 |
| 3e quartile | x1.52 |
| Etendue | x0.03 a x31.03 |

| Ecart | Mots-cles | Part |
|---|---:|---:|
| Identique | 36 | 19.9 % |
| Dans +/-10 % | 36 | 19.9 % |
| x1,1 a x1,5 | 80 | 44.2 % |
| x1,5 a x3 | 36 | 19.9 % |
| Au-dela de x3 | 11 | 6.1 % |
| DataForSEO plus BAS (< x0,9) | 18 | 9.9 % |

Un ecart-type de 2.65 pour une mediane de 1.23 : appliquer un facteur de conversion n'a aucun sens. Les extremes vont de `diffuseur batonnets` (x0,03) a `limonadiers` (x31,0).

### 2. Google pre-agrege les variantes proches - donc additionner ses volumes double-compte

C'est le point qui tue la substitution. Notre methode de consolidation additionne **les formulations qu'une meme page servirait**. Elle suppose que chaque formulation est un corpus distinct. C'est vrai chez SEMrush ; c'est faux chez Google.

#### Paires accentuees

| Paire | SEMrush | DataForSEO | |
|---|---|---|---|
| `plateau petit dejeuner` / `plateau petit déjeuner` | 590 / 880 | 1300 / 1300 | **fusionne** |
| `planche apero` / `planche apéro` | 9900 / 2900 | 14800 / 14800 | **fusionne** |
| `planche a fromage` / `planche à fromage` | 140 / 590 | 170 / 1300 |  |
| `planche a decouper` / `planche à découper` | 14800 / 6600 | 18100 / 5400 |  |
| `diffuseur batonnets` / `diffuseur bâtonnets` | 1300 / 1000 | 40 / 90 |  |
| `bougie parfumée` / `bougie parfumee` | 12100 / 1600 | 12100 / 1300 |  |
| `bougie cire végétale` / `bougie cire vegetale` | 720 / 720 | 1000 / 1000 |  |
| `desodorisant voiture` / `désodorisant voiture` | 2900 / 2400 | 4400 / 4400 | **fusionne** |
| `tringle a rideau` / `tringle à rideau` | 14800 / 4400 | 22200 / 6600 |  |
| `tire bouchon electrique` / `tire bouchon électrique` | 4400 / 1000 | 5400 / 5400 | **fusionne** |
| `carafe a vin` / `carafe à vin` | 1900 / 1900 | 2400 / 1900 |  |
| `aerateur de vin` / `aérateur de vin` | 3600 / 590 | 8100 / 720 |  |
| `aerateur vin` / `aérateur vin` | 480 / 140 | 590 / 140 |  |
| `decanteur de vin` / `décanteur de vin` | 1300 / 480 | 1600 / 1600 | **fusionne** |
| `decanteur vin` / `décanteur vin` | 880 / 480 | 1000 / 590 |  |
| `decanteur` / `décanteur` | 720 / 390 | 720 / 480 |  |
| `pompe a vin` / `pompe à vin` | 480 / 260 | 480 / 320 |  |
| `verre a vin` / `verre à vin` | 12100 / 2400 | 18100 / 2900 |  |
| `verres a vin` / `verres à vin` | 1600 / 2900 | 18100 / 4400 |  |
| `coffret dégustation vin` / `coffret degustation vin` | 720 / 720 | 1000 / 1000 |  |

Google fusionne **5 paires sur 20**. SEMrush en fusionne 3 sur 20.

#### Paires singulier / pluriel

| Paire | SEMrush | DataForSEO | |
|---|---|---|---|
| `limonadier` / `limonadiers` | 9900 / 390 | 12100 / 12100 | **fusionne** |
| `verre a vin` / `verres a vin` | 12100 / 1600 | 18100 / 18100 | **fusionne** |
| `verres à vin` / `verre à vin` | 2900 / 2400 | 4400 / 2900 |  |
| `verre inao` / `verres inao` | 1300 / 480 | 1600 / 1600 | **fusionne** |

**Google fusionne 3 paires sur 4.** `limonadier` valait 9 900 et `limonadiers` 390 chez SEMrush ; chez DataForSEO les deux valent 12 100 - c'est le meme bucket servi deux fois.

Consequence directe : sur DataForSEO, sommer `limonadier` + `limonadiers` donne 24 200 pour une demande reelle de 12 100. **Notre consolidation par familles produirait des totaux gonfles d'un facteur imprevisible.**

Et la fusion est **imprevisible** : `planche apero` / `planche apero` accentue fusionnent (14 800 / 14 800), mais `aerateur de vin` / `aerateur de vin` accentue restent separes (8 100 / 720). On ne peut ni presumer la fusion, ni presumer la separation.

### Ce sur quoi les deux sources sont d'accord

Les deux decouvertes qui ont retourne les dossiers du 28/08 sont confirmees par une source independante :

- `rideau occultant total` = **30** des deux cotes, contre `rideau occultant` a 33 100 (SEMrush) et 49 500 (DataForSEO). Le facteur x1 100 n'etait pas un artefact d'outil.
- `diffuseur cheveux` = **18 100 des deux cotes**, a l'unite. La contamination seche-cheveux est reelle.

### Effet bucket - les deux, pas seulement Google

DataForSEO rend **35 valeurs distinctes pour 181 mots-cles** (les plus repetees : 1000 x17, 5400 x16, 1300 x15, 320 x10). SEMrush n'est pas meilleur : 97 % de ses valeurs sont partagees avec au moins un autre mot-cle. **Aucune des deux sources ne donne un volume fin** - ce n'est pas un argument pour departager.

## Recommandation

| Usage | Outil | Motif |
|---|---|---|
| Decouverte de vocabulaire (100 lignes, 0 credit) | **SEMrush** | Aucun equivalent teste ; c'est ce qui a trouve le seche-cheveux et le traiteur |
| Consolidation par familles | **SEMrush** | Corpus separes ; l'addition est arithmetiquement valide |
| Controle de vraisemblance sur les tetes | **DataForSEO** | 0,09 USD pour 181 mots-cles ; source Keyword Planner |
| Estimation de ce que Google servira en Ads | **DataForSEO** | C'est l'enchere reelle, variantes proches comprises |
| KD, fonctionnalites SERP, intention | **SEMrush** | Non couvert par l'endpoint teste |

**Sur les 149 EUR/mois** : DataForSEO ne les remplace pas, mais il est assez peu cher pour tourner en complement systematique. Si l'objectif est de sortir de SEMrush, le chantier n'est pas << changer de source de volume >> - c'est **remplacer l'etape de decouverte**, puis **recalibrer les seuils** (10 000 par cluster, 30 000 consolide), qui ont tous ete fixes sur des chiffres SEMrush.

## Reserves

1. 181 mots-cles issus des 4 dossiers UNIVERS du 28/08 - corpus maison, pas un echantillon representatif de tous nos marches.
2. Volumes SEMrush lus le 28/08, DataForSEO le 29/08 : un jour d'ecart, effet suppose nul mais non verifie.
3. Seul l'endpoint `google_ads/search_volume` a ete teste. L'endpoint d'idees de mots-cles, qui serait le vrai substitut a la decouverte, **n'a pas ete evalue**.
4. Extraction automatique des couples depuis les rapports : 26 lignes ambigues ont ete ecartees plutot que devinees.
5. Aucune des deux sources n'a ete confrontee a une troisieme (Search Console, donnees Ads reelles). Sur `diffuseur batonnets` (SEMrush 1 300, DataForSEO 40), **on ne sait pas qui a raison**.

## Annexe - les 181 mots-cles

| Mot-cle | SEMrush | DataForSEO | Rapport |
|---|---:|---:|---:|
| `huile essentielle` | 60500 | 74000 | x1.22 |
| `cave a vin` | 60500 | 74000 | x1.22 |
| `planche` | 40500 | 18100 | x0.45 |
| `bougie` | 40500 | 60500 | x1.49 |
| `rideau` | 40500 | 40500 | x1.00 |
| `rideau occultant` | 33100 | 49500 | x1.50 |
| `rideau thermique` | 33100 | 49500 | x1.50 |
| `rideaux` | 22200 | 22200 | x1.00 |
| `diffuseur` | 18100 | 14800 | x0.82 |
| `rideaux occultants` | 18100 | 49500 | x2.73 |
| `tringle rideau` | 18100 | 22200 | x1.23 |
| `planche a decouper` | 14800 | 18100 | x1.22 |
| `diffuseur huile essentielle` | 14800 | 18100 | x1.22 |
| `tringle a rideau` | 14800 | 22200 | x1.50 |
| `bougie parfumée` | 12100 | 12100 | x1.00 |
| `rideaux voilage` | 12100 | 27100 | x2.24 |
| `tire bouchon` | 12100 | 14800 | x1.22 |
| `verre a vin` | 12100 | 18100 | x1.50 |
| `planche apero` | 9900 | 14800 | x1.49 |
| `rideau occultant thermique` | 9900 | 22200 | x2.24 |
| `rideaux thermiques` | 9900 | 49500 | x5.00 |
| `tringle rideau sans percer` | 9900 | 18100 | x1.83 |
| `limonadier` | 9900 | 12100 | x1.22 |
| `voilage` | 8100 | 8100 | x1.00 |
| `rideaux et voilages` | 8100 | 27100 | x3.35 |
| `planche à découper` | 6600 | 5400 | x0.82 |
| `oenologie` | 6600 | 12100 | x1.83 |
| `plateau bois` | 5400 | 5400 | x1.00 |
| `plateau charcuterie` | 5400 | 8100 | x1.50 |
| `rideau lin` | 5400 | 4400 | x0.81 |
| `art de la table` | 4400 | 5400 | x1.23 |
| `billot` | 4400 | 5400 | x1.23 |
| `rideau thermique anti froid` | 4400 | 5400 | x1.23 |
| `rideau phonique` | 4400 | 4400 | x1.00 |
| `tringle à rideau` | 4400 | 6600 | x1.50 |
| `embrasse rideau` | 4400 | 6600 | x1.50 |
| `double rideaux` | 4400 | 5400 | x1.23 |
| `tire bouchon electrique` | 4400 | 5400 | x1.23 |
| `cave a vin encastrable` | 4400 | 4400 | x1.00 |
| `cave a vin la sommeliere` | 4400 | 6600 | x1.50 |
| `plateau apero` | 3600 | 6600 | x1.83 |
| `parfum d'intérieur` | 3600 | 5400 | x1.50 |
| `brule parfum` | 3600 | 5400 | x1.50 |
| `rideau isolant thermique` | 3600 | 5400 | x1.50 |
| `isolant thermique pour rideaux` | 3600 | 5400 | x1.50 |
| `rideau en lin` | 3600 | 5400 | x1.50 |
| `rideau sur mesure` | 3600 | 5400 | x1.50 |
| `rideaux sur mesure` | 3600 | 5400 | x1.50 |
| `aerateur de vin` | 3600 | 8100 | x2.25 |
| `petite cave a vin` | 3600 | 3600 | x1.00 |
| `cave a vin autour de moi` | 3600 | 6600 | x1.83 |
| `plateau de service` | 2900 | 4400 | x1.52 |
| `planche apéro` | 2900 | 14800 | x5.10 |
| `diffuseur parfum maison` | 2900 | 2900 | x1.00 |
| `parfum d'ambiance` | 2900 | 2900 | x1.00 |
| `parfum voiture` | 2900 | 3600 | x1.24 |
| `desodorisant voiture` | 2900 | 4400 | x1.52 |
| `verres à vin` | 2900 | 4400 | x1.52 |
| `planche charcuterie` | 2400 | 3600 | x1.50 |
| `coffret bougie` | 2400 | 2900 | x1.21 |
| `diffuseur voiture` | 2400 | 2400 | x1.00 |
| `désodorisant voiture` | 2400 | 4400 | x1.83 |
| `rideau anti bruit` | 2400 | 2400 | x1.00 |
| `rideau acoustique` | 2400 | 2400 | x1.00 |
| `ouvre bouteille` | 2400 | 2400 | x1.00 |
| `carafe vin` | 2400 | 2900 | x1.21 |
| `verre à vin` | 2400 | 2900 | x1.21 |
| `fondant parfumé` | 1900 | 2400 | x1.26 |
| `rideau velours` | 1900 | 2900 | x1.53 |
| `rideaux velours` | 1900 | 2900 | x1.53 |
| `anneaux rideaux` | 1900 | 2900 | x1.53 |
| `carafe a vin` | 1900 | 2400 | x1.26 |
| `carafe à vin` | 1900 | 1900 | x1.00 |
| `coffret vin` | 1900 | 1900 | x1.00 |
| `bougie parfumee` | 1600 | 1300 | x0.81 |
| `rideau isolant` | 1600 | 1900 | x1.19 |
| `voilage lin` | 1600 | 1900 | x1.19 |
| `verres a vin` | 1600 | 18100 | x11.31 |
| `verres à vins` | 1600 | 4400 | x2.75 |
| `cave a vin de vieillissement` | 1600 | 1300 | x0.81 |
| `diffuseur batonnets` | 1300 | 40 | x0.03 |
| `rideau isolant phonique` | 1300 | 1300 | x1.00 |
| `tire-bouchon` | 1300 | 14800 | x11.38 |
| `tire bouchon personnalisé` | 1300 | 1300 | x1.00 |
| `decanteur de vin` | 1300 | 1600 | x1.23 |
| `verre inao` | 1300 | 1600 | x1.23 |
| `diffuseur bâtonnets` | 1000 | 90 | x0.09 |
| `senteur maison` | 1000 | 1000 | x1.00 |
| `tire bouchon électrique` | 1000 | 5400 | x5.40 |
| `tire bouchon electronique` | 1000 | 5400 | x5.40 |
| `limonadier personnalisé` | 1000 | 1000 | x1.00 |
| `verre a vin personnalisable` | 1000 | 1000 | x1.00 |
| `verre a vin plastique` | 1000 | 1300 | x1.30 |
| `verre à vin blanc` | 1000 | 1300 | x1.30 |
| `verre à vin rouge` | 1000 | 1600 | x1.60 |
| `œnologie` | 1000 | 12100 | x12.10 |
| `plateau petit déjeuner` | 880 | 1300 | x1.48 |
| `recharge diffuseur` | 880 | 320 | x0.36 |
| `tire bouchon mural` | 880 | 720 | x0.82 |
| `tire bouchon sommelier` | 880 | 1000 | x1.14 |
| `ouvre bouteille electrique` | 880 | 880 | x1.00 |
| `carafe décantation vin` | 880 | 1300 | x1.48 |
| `decanteur vin` | 880 | 1000 | x1.14 |
| `coffret cadeau vin` | 880 | 1000 | x1.14 |
| `coffret pour vin` | 880 | 1900 | x2.16 |
| `coffret vin personnalisé` | 880 | 390 | x0.44 |
| `diffuseur nébulisation` | 720 | 720 | x1.00 |
| `batonnet parfum` | 720 | 880 | x1.22 |
| `bougie cire végétale` | 720 | 1000 | x1.39 |
| `bougie cire vegetale` | 720 | 1000 | x1.39 |
| `rideau anti froid` | 720 | 880 | x1.22 |
| `tire bouchon a levier` | 720 | 320 | x0.44 |
| `tire bouchon a air` | 720 | 880 | x1.22 |
| `limonadier professionnel` | 720 | 880 | x1.22 |
| `carafe à décanter le vin` | 720 | 1300 | x1.81 |
| `carafe à décanter vin` | 720 | 1300 | x1.81 |
| `decanteur` | 720 | 720 | x1.00 |
| `inao verre` | 720 | 1600 | x2.22 |
| `coffret dégustation vin` | 720 | 1000 | x1.39 |
| `coffret degustation vin` | 720 | 1000 | x1.39 |
| `coffret sommelier` | 720 | 720 | x1.00 |
| `accessoire vin` | 720 | 1000 | x1.39 |
| `vin accessoire` | 720 | 1000 | x1.39 |
| `plateau petit dejeuner` | 590 | 1300 | x2.20 |
| `planche à fromage` | 590 | 1300 | x2.20 |
| `bouquet parfumé` | 590 | 390 | x0.66 |
| `rideau lin lavé` | 590 | 880 | x1.49 |
| `tire bouchon bilame` | 590 | 720 | x1.22 |
| `ouvre bouteille personnalisé` | 590 | 590 | x1.00 |
| `aérateur de vin` | 590 | 720 | x1.22 |
| `bouchon vin` | 590 | 880 | x1.49 |
| `bouchon bouteille vin` | 590 | 720 | x1.22 |
| `bouchons à vin` | 590 | 880 | x1.49 |
| `accessoire à vin` | 590 | 1000 | x1.69 |
| `accessoires pour le vin` | 590 | 1000 | x1.69 |
| `vin et accessoires` | 590 | 1000 | x1.69 |
| `plateau ardoise` | 480 | 590 | x1.23 |
| `diffuseur ultrasonique` | 480 | 480 | x1.00 |
| `carafe à vin à décanter` | 480 | 1300 | x2.71 |
| `carafe pour decanter le vin` | 480 | 1300 | x2.71 |
| `carafe décanteur vin` | 480 | 1300 | x2.71 |
| `aerateur vin` | 480 | 590 | x1.23 |
| `décanteur de vin` | 480 | 1600 | x3.33 |
| `décanteur vin` | 480 | 590 | x1.23 |
| `bouchon de bouteille de vin` | 480 | 590 | x1.23 |
| `pompe a vin` | 480 | 480 | x1.00 |
| `verre à vin dégustation` | 480 | 720 | x1.50 |
| `verres inao` | 480 | 1600 | x3.33 |
| `coffret oenologie` | 480 | 480 | x1.00 |
| `accessoires du vin` | 480 | 1000 | x2.08 |
| `coffret senteur` | 390 | 390 | x1.00 |
| `limonadiers` | 390 | 12100 | x31.03 |
| `decanteur a vin` | 390 | 1000 | x2.56 |
| `décanteur` | 390 | 480 | x1.23 |
| `coffret de vin` | 390 | 390 | x1.00 |
| `coffret du sommelier` | 390 | 720 | x1.85 |
| `limonadier sommelier` | 320 | 210 | x0.66 |
| `ouvre bouteille vin` | 320 | 320 | x1.00 |
| `aerateur a vin` | 320 | 590 | x1.84 |
| `vin aerateur` | 320 | 590 | x1.84 |
| `pompe a vide vin` | 320 | 320 | x1.00 |
| `bouchon sous vide vin` | 260 | 320 | x1.23 |
| `bouchon vin sous vide` | 260 | 320 | x1.23 |
| `pompe a vide pour le vin` | 260 | 320 | x1.23 |
| `pompe vin` | 260 | 320 | x1.23 |
| `pompe à vin` | 260 | 320 | x1.23 |
| `coffret sommelier personnalisé` | 260 | 170 | x0.65 |
| `bouchon conservation vin` | 210 | 260 | x1.24 |
| `bouchon pour conserver le vin` | 210 | 260 | x1.24 |
| `bouchon vide air vin` | 210 | 320 | x1.52 |
| `conservateur vin` | 170 | 260 | x1.53 |
| `coffret accessoire vin` | 170 | 210 | x1.24 |
| `planche a fromage` | 140 | 170 | x1.21 |
| `aérateur vin` | 140 | 140 | x1.00 |
| `recharge parfum d'intérieur` | 110 | 140 | x1.27 |
| `parfum interieur maison` | 90 | 40 | x0.44 |
| `coffret parfum maison` | 70 | 90 | x1.29 |
| `appareil pour conserver une bouteille de vin ouverte` | 70 | 20 | x0.29 |
| `abonnement coffret vin` | 70 | 70 | x1.00 |
| `recharge parfum interieur` | 50 | 20 | x0.40 |
| `rideau occultant total` | 30 | 30 | x1.00 |
---

# Addendum — test des endpoints de decouverte DataForSEO

**Date : 2026-08-29**, meme session. Question posee : l'etape de decouverte (le Keyword Magic Tool en expression exacte, 100 lignes, 0 credit) est-elle remplacable ?

Deux endpoints candidats testes sur la meme graine `diffuseur`, avec un critere de reussite unique et non negociable : **retrouver la contamination seche-cheveux** (`diffuseur cheveux` = 18 100), qui est exactement le type de decouverte qui a retourne le dossier du 28/08.

## Resultat

| Endpoint | Lignes | Cout | `diffuseur cheveux` | Verdict |
|---|---:|---:|---|---|
| `keywords_data/google_ads/keywords_for_keywords` | 1 774 | 0,09 USD | **ABSENT** — 0 ligne coiffure sur 1 774 | **Disqualifie** |
| `dataforseo_labs/google/keyword_suggestions` | 1 000 (sur 20 682 annonces) | 0,132 USD | **TROUVE, 18 100** — 89 lignes coiffure | **Viable** |

### Pourquoi le premier est disqualifie

`keywords_for_keywords` est l'outil d'idees de Google Ads : il filtre **semantiquement** sur l'intention publicitaire qu'il infere de la graine. Il ne rend donc que ce qui sert la these commerciale supposee, et masque activement les autres sens du mot. Sur 1 774 lignes, **aucune** ne mentionne les cheveux — alors que les deux autres sources s'accordent sur 18 100 recherches par mois.

C'est exactement l'inverse de ce dont la methode a besoin. La valeur du Keyword Magic Tool en expression exacte est d'etre **mecanique** : il rend tout ce qui contient la chaine, bruit compris. C'est ce bruit qui revele la contamination. Un outil qui nettoie a notre place nous rend aveugles au piege que l'on cherche.

### Pourquoi le second est viable

`keyword_suggestions` fait de la correspondance **plein texte** sur la graine, sans filtre d'intention. Il retrouve la contamination coiffure (89 lignes, 234 420 de volume cumule) et, sur une seconde graine `plateau`, il retrouve **toutes** les decouvertes du 28/08 :

| Decouverte du 28/08 | Retrouvee |
|---|---|
| `plateau charcuterie` (le retournement traiteur) | oui, 8 100 |
| `plateau de beille` (contamination geographique, station de ski) | oui, 22 200 — plus 8 lignes de meteo et webcams |
| `plateau apero`, `plateau bois`, `plateau petit dejeuner` | oui |

Et la profondeur est sans comparaison : **74 527 suggestions annoncees** sur `plateau`, contre 100 lignes par requete chez SEMrush.

## Les deux reserves qui restent

**1. La redondance est massive.** Sur `diffuseur`, 1 000 lignes se reduisent a **410 idees distinctes apres normalisation : 59 % de reformulations**. Le top 10 est dix ecritures de la meme idee, toutes a 18 100. C'est la contrepartie de l'agregation par variantes proches deja documentee plus haut. Elle est **mecaniquement supprimable** (normalisation : accents, pluriels, mots vides, ordre des mots) — c'est du code, pas un obstacle de fond.

**2. Les volumes restent des buckets agreges.** 24 valeurs distinctes pour 1 000 lignes. La regle demontree plus haut tient : **ne jamais sommer les volumes bruts de cet endpoint**, sous peine de compter dix fois le meme bucket. Toute consolidation doit passer par la normalisation d'abord, un volume par idee normalisee ensuite.

## Consequence pour la question des 149 EUR/mois

La substitution n'est plus impossible — elle devient un **chantier chiffrable** :

| Brique | Etat |
|---|---|
| Decouverte de vocabulaire | **Resolue** — `keyword_suggestions`, plus profond que SEMrush |
| Volume de tete | **Resolue** — `google_ads/search_volume`, 0,09 USD les 181 mots-cles |
| Deduplication / normalisation | **A construire** — indispensable, sinon les consolides sont faux |
| Recalibrage des seuils (10 000 cluster, 30 000 consolide) | **A faire** — ils ont ete fixes sur des chiffres SEMrush |
| KD, fonctionnalites SERP, intention | **Non couvert** par les endpoints testes |

Ordre de grandeur de cout : une Mission B mobilise ~26 graines, soit environ **3,50 USD** en `keyword_suggestions`, plus quelques centimes de volumes. Quatre Mission B par mois : environ **15 USD** contre 149 EUR.

**Recommandation** : ne pas resilier avant d'avoir construit et valide la couche de normalisation, puis recalibre les seuils sur un dossier deja mesure aux deux sources. Tant que ces deux briques manquent, une migration produirait des consolides gonfles et des verdicts faux — le cout de l'erreur depasse largement l'economie d'abonnement.

## Reserves de ce test

1. Deux graines seulement (`diffuseur`, `plateau`), choisies parce que leurs pieges etaient deja connus. Un test sur une graine **dont on ignore les pieges** reste a faire — c'est le seul qui prouverait vraiment la capacite de decouverte.
2. `keyword_suggestions` a ete interroge avec `limit: 1000` ; le comportement au-dela (pagination, cout, exhaustivite reelle des 74 527) n'est pas verifie.
3. Le KD, l'intention et les fonctionnalites SERP n'ont pas ete cherches dans les reponses Labs — ils existent peut-etre sur d'autres endpoints, non evalues.
4. Aucune comparaison de fraicheur des donnees entre les deux sources.
