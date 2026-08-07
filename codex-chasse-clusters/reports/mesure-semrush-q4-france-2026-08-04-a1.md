# Mesure SEMrush France — radar Q4 international — 4 août 2026

## Résultat exécutif

- **94/94 requêtes** ont été mesurées dans SEMrush, base **France** (`db=fr`), puis actualisées en une fois le 4 août 2026.
- Le compteur observé de mise à jour est passé de **0/1 000** à **94/1 000** ; toutes les lignes affichaient ensuite `Maintenant`.
- Le seuil du pipeline reste **10 000 recherches mensuelles réellement adressables après nettoyage**.
- **Un seul cluster mérite la gate prix/SERP : lunchbox inox / thermos repas**, avec **10 400/mois** dans une lecture famille tous âges, mais seulement **9 940/mois** si l'on retire les requêtes enfant/bébé. C'est donc un **cas limite**, pas un GO marché.
- Les neuf autres concepts restent sous le seuil sur leur intention produit exacte.
- Les totaux bruts de la peinture personnalisée, de la toupie freestyle et du circuit flexible dépassent artificiellement 10 000 uniquement grâce à des requêtes génériques qui ne prouvent pas la variante observée dans Brand Search.
- Aucun sourcing AliExpress, import DSers, changement Shopify ou mutation Notion n'a été lancé.

## Source et méthode

### Observé

- Outil : SEMrush `Vue d'ensemble des mots clés`, analyse groupée.
- Base : France (`db=fr`).
- Taille du lot : 94 requêtes, maximum affiché 100.
- Volumes : moyenne mensuelle affichée par SEMrush.
- CPC du lot groupé : affiché en **USD** par l'écran d'analyse groupée.
- Expansion du cas limite : Keyword Magic Tool France, devise **EUR**.
- Fraîcheur finale : chaque ligne du lot groupé affichait `Maintenant` après actualisation.

### Nettoyage appliqué

Le `noyau exact` conserve seulement les requêtes qui décrivent la forme de produit étudiée. Le `lot élargi` est montré pour détecter les faux positifs, mais ne valide jamais à lui seul la variante.

Sont exclus du volume qualifiant lorsqu'ils ne correspondent pas à l'offre :

- marques et enseignes ;
- accessoires voisins, par exemple le sac isotherme seul ;
- produit techniquement différent, par exemple la lunchbox chauffante ;
- requêtes `avis` et `comparatif` dans l'expansion ;
- termes génériques qui peuvent désigner d'autres produits, par exemple `toupie`, `circuit voiture`, `peinture par numéro` ou `manteau chien` ;
- doublons déjà comptés dans le lot initial.

## Verdict par cluster

| Prio | Cluster | Volume noyau exact | Volume élargi observé | Verdict volume | Lecture honnête |
|---:|---|---:|---:|---|---|
| 1 | Kit poterie maison / couple | **2 050** | 2 120 | `STOP_VOLUME_EXACT` | Le signal Brand Search/Q4 ne se traduit pas en demande Search France suffisante. |
| 2 | Peinture par numéros personnalisée / photo | **120** | 10 850 | `STOP_VOLUME_EXACT` | Les 10 730 recherches voisines portent presque toutes sur la peinture par numéros générique, pas sur la personnalisation. |
| 3 | Kit promenade chien premium | **950** | 3 850 | `STOP_VOLUME_EXACT` | Le terme voisin `harnais anti traction chien` apporte 2 900, mais ne prouve pas le kit assorti. |
| 4 | Lunchbox inox / thermos repas personnalisé | **7 940** avant expansion | **10 400** nettoyé, tous âges | `CONTINUER_PRIX_SERP_CAS_LIMITE` | L'expansion propre ajoute 2 460. Sans les requêtes enfant/bébé, le total redescend à 9 940. L'angle personnalisation seul ne pèse qu'environ 650. |
| 5 | Imperméable / visibilité chien | **2 600** | 7 140 | `STOP_VOLUME_EXACT` | `manteau chien` et `manteau hiver chien` ajoutent 4 540 mais décrivent une catégorie plus large. |
| 6 | Jeu d'ambiance compact / voyage | **1 570** | 1 570 | `STOP_VOLUME_EXACT` | Demande Search insuffisante et mécanique produit encore non définie. |
| 7 | Barrière chien rétractable | **1 950** | 1 950 | `STOP_VOLUME_EXACT` | La variante exacte `barrière chien rétractable` ne fait que 20/mois. |
| 8 | Toupie freestyle | **150** | 10 530 | `STOP_VOLUME_EXACT` | Faux positif majeur : `toupie` + `toupie enfant` apportent 10 380, le freestyle seulement 20. |
| 9 | Circuit voiture flexible | **180** | 13 520 | `STOP_VOLUME_EXACT` | Faux positif majeur : `circuit voiture` et `circuit voiture enfant` dominent ; le flexible fait 140 + 40. |
| 10 | Numéro de maison solaire | **150** | 1 450 | `STOP_VOLUME_EXACT` | `numéro de maison` générique apporte 1 300 ; la variante solaire reste très faible. |

## Cas limite à conserver : lunchbox / thermos repas

### Lot initial — 7 940/mois

| Requête | Volume | KD | CPC USD | Intention SEMrush |
|---|---:|---:|---:|---|
| lunch box isotherme | 5 400 | 17 | 0,23 | I |
| thermos alimentaire | 720 | 20 | 0,24 | I |
| lunch box inox | 590 | 10 | 0,37 | I |
| lunch box personnalisée | 480 | 15 | 1,16 | I |
| thermos repas | 320 | 14 | 0,32 | I |
| bento inox | 170 | 8 | 0,31 | I / T |
| boîte repas isotherme | 140 | 10 | 0,29 | I |
| bento personnalisé | 90 | 15 | 0,54 | I |
| boîte repas inox | 30 | 8 | 0,31 | I |
| boîte à lunch personnalisée | 0 | 20 | n/a | I |
| lunch box gravée | 0 | 19 | n/a | I |

### Expansion Keyword Magic nettoyée — +2 460/mois

Les 48 variantes retenues sont des formulations de produit ou de caractéristique. Les principaux ajouts sont :

| Requête additionnelle | Volume | CPC EUR | Décision |
|---|---:|---:|---|
| lunch box isotherme chaud | 480 | 0,21 | retenue |
| lunch box isotherme enfant | 260 | 0,00 | retenue, mais retirée dans la sensibilité adulte |
| lunch box enfant isotherme | 170 | 0,00 | retenue, mais retirée dans la sensibilité adulte |
| meilleur lunch box isotherme | 110 | 0,18 | retenue, intention commerciale |
| box lunch isotherme | 90 | 0,25 | retenue |
| isotherme lunch box | 90 | 0,29 | retenue |
| meilleure lunch box isotherme | 90 | 0,18 | retenue, intention commerciale |
| lunch box inox isotherme | 70 | 0,29 | retenue |
| lunch box isotherme chaud longue durée | 70 | 0,25 | retenue |
| lunch box isotherme inox | 70 | 0,24 | retenue |
| bento lunch box isotherme | 50 | 0,19 | retenue |
| lunch box isotherme personnalisable | 50 | 0,48 | retenue |
| autres variantes produit propres | 860 | variable | retenues après exclusions |

Le calcul final est :

- lot initial : **7 940** ;
- expansion propre hors doublons : **+2 460** ;
- total famille tous âges : **10 400** ;
- sensibilité sans `enfant` / `bébé` : **9 940** ;
- sous-ensemble explicitement personnalisé ou gravé : environ **650**.

### Exclusions principales de l'expansion

- sacs et sacoches isothermes : accessoire voisin, pas la boîte repas ;
- Decathlon, Ikea, Action, Amazon, Leclerc, Carrefour, Monbento, Qwetch et autres marques/enseignes ;
- lunchbox chauffante : produit électrique différent ;
- requêtes avis et comparatif ;
- requêtes déjà présentes dans le lot initial.

### Verdict du cas limite

`CONTINUER_PRIX_SERP_CAS_LIMITE`, avec deux conditions :

1. la prochaine offre doit adresser la famille lunchbox isotherme / thermos repas, pas reposer uniquement sur la gravure ;
2. le produit doit encore passer le prix France, la SERP, la différenciation, le contact alimentaire, l'étanchéité et la performance thermique.

Le passage au-dessus de 10 000 n'est pas assez robuste pour autoriser directement le sourcing. Il autorise seulement la gate prix/SERP.

## Détail des 94 requêtes du lot groupé

### 1. Kit poterie maison / couple

`kit poterie` 1 000 ; `kit poterie maison` 140 ; `kit poterie adulte` 320 ; `kit poterie autodurcissante` 40 ; `kit argile autodurcissante` 480 ; `kit modelage argile` 70 ; `kit poterie couple` 0 ; `kit créatif couple` 0 ; `kit peinture sur verre` 50 ; `kit peinture verre` 20.

### 2. Peinture par numéros personnalisée

`peinture par numéro personnalisée` 50 ; `peinture par numéros personnalisée` 10 ; `peinture par numéro photo` 40 ; `peinture par numéros photo` 0 ; `tableau à peindre personnalisé` 20 ; `peinture par numéro adulte` 3 600 ; `peinture par numéros adulte` 170 ; `kit peinture par numéro` 260 ; `peinture par numéro couple` 0 ; `peinture par numéro` 5 400 ; `peinture par numéros` 1 300.

### 3. Kit promenade chien premium

`kit promenade chien` 20 ; `ensemble harnais laisse chien` 20 ; `harnais et laisse chien` 210 ; `laisse mains libres chien` 390 ; `laisse ceinture chien` 110 ; `laisse bandoulière chien` 110 ; `laisse multiposition chien` 90 ; `harnais anti traction chien` 2 900 ; `harnais anti tirage chien` 0 ; `kit harnais chien` 0.

### 4. Lunchbox / thermos repas

`lunch box inox` 590 ; `lunch box personnalisée` 480 ; `lunch box isotherme` 5 400 ; `boîte repas inox` 30 ; `boîte repas isotherme` 140 ; `thermos repas` 320 ; `thermos alimentaire` 720 ; `bento inox` 170 ; `bento personnalisé` 90 ; `boîte à lunch personnalisée` 0 ; `lunch box gravée` 0.

### 5. Imperméable / visibilité chien

`imperméable chien` 1 900 ; `manteau imperméable chien` 320 ; `manteau pluie chien` 320 ; `manteau réfléchissant chien` 0 ; `manteau haute visibilité chien` 0 ; `combinaison pluie chien` 30 ; `combinaison imperméable chien` 30 ; `manteau hiver chien` 140 ; `manteau chien` 4 400.

### 6. Jeu d'ambiance compact / voyage

`jeu d'ambiance adulte` 30 ; `jeu de société ambiance` 140 ; `jeu de bluff` 170 ; `jeu de voyage` 590 ; `jeu de voyage famille` 20 ; `jeu compact famille` 0 ; `petit jeu de société` 480 ; `jeu de cartes ambiance` 0 ; `jeu d'ambiance famille` 140.

### 7. Barrière chien rétractable

`barrière chien rétractable` 20 ; `barrière rétractable animaux` 0 ; `barrière chien porte` 0 ; `barrière chien escalier` 720 ; `barrière chien sans perçage` 30 ; `barrière extensible chien` 170 ; `barrière chien camping car` 10 ; `barrière pour chien` 1 000.

### 8. Toupie freestyle

`toupie freestyle` 20 ; `toupie à figures` 0 ; `toupie moderne` 20 ; `toupie de compétition` 0 ; `toupie acrobatique` 20 ; `toupie ficelle` 90 ; `toupie enfant` 480 ; `toupie` 9 900.

### 9. Circuit voiture flexible

`circuit voiture flexible` 140 ; `piste voiture flexible` 40 ; `circuit petites voitures` 210 ; `piste petites voitures` 0 ; `circuit voiture enfant` 4 400 ; `piste voiture enfant` 20 ; `circuit voiture jouet` 590 ; `piste voiture jouet` 20 ; `circuit voiture` 8 100.

### 10. Numéro de maison solaire

`numéro de maison solaire` 70 ; `plaque numéro maison solaire` 10 ; `plaque adresse solaire` 20 ; `numéro de maison lumineux` 30 ; `plaque numéro maison lumineuse` 0 ; `plaque adresse lumineuse` 20 ; `numéro maison éclairé` 0 ; `plaque maison solaire` 0 ; `numéro de maison` 1 300.

## Signaux CPC utiles, sans verdict économique

- La personnalisation lunchbox porte le CPC le plus élevé du lot : `lunch box personnalisée` à **1,16 USD**.
- `peinture par numéro photo` atteint **0,97 USD**, mais son volume n'est que 40.
- `peinture par numéro personnalisée` atteint **0,76 USD**, pour 50 recherches.
- `toupie` atteint 9 900 recherches et 0,87 USD, mais ce signal appartient au terme générique, pas au freestyle.
- `circuit voiture` atteint 8 100 et 0,62 USD, mais ne prouve pas le circuit flexible.

Ces CPC ne valident aucune économie : prix vendu, coût rendu, CVR, marge contributive et CPA maximal restent manquants.

## Décision opérationnelle

### [FAIT]

- mesure SEMrush France des 94 requêtes ;
- actualisation des 94 métriques ;
- nettoyage des intentions voisines ;
- expansion Keyword Magic ciblée du seul cluster proche du seuil ;
- identification d'un cas limite à continuer et de neuf STOP Search exacts.

### [MANQUANT]

Pour la lunchbox / thermos repas uniquement :

1. sonde prix Google Shopping France ;
2. contrôle SERP Search/Shopping et densité marketplaces/DTC ;
3. validation de l'angle d'offre : famille tous âges versus adulte/premium ;
4. différenciation crédible hors simple gravure ;
5. seulement si ces gates passent : AliExpress exact, contact alimentaire, étanchéité, thermique, coût rendu France et délai.

### Interdit à ce stade

- ne pas lancer le sourcing des neuf clusters sous seuil ;
- ne pas présenter la lunchbox comme un GO marché ;
- ne pas additionner les termes génériques aux variantes exactes pour sauver artificiellement un concept ;
- ne pas importer dans DSers ou Shopify sans nouvelle autorisation et preuves produit.
