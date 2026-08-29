# Rejeu du dossier « Univers GOTHIQUE / EMO » avec DataForSEO seul — zone de décision

**Date : 2026-08-29.** Test de non-régression avant résiliation de l'abonnement SEMrush.

Question posée : *sur un dossier dont le verdict se joue à quelques milliers de recherches près,
la chaîne DataForSEO rend-elle le même verdict que SEMrush ?*

Le rejeu du dossier rideaux (`analyses/2026-08-29-rejeu-rideaux-dataforseo.md`) a validé la chaîne
à ×16 du seuil — le test le moins exigeant possible. Le présent rejeu est le test manquant, celui
que le §1 de `PRODUCT-RESEARCH-CRITERIA.md` réclame explicitement :
« *Un rejeu sur un dossier proche du seuil, ou conclu STOP, reste à faire.* »

Référence rejouée : `analyses/2026-08-15-niches-univers/U5-gothique/` (3 fichiers, 15/08/2026).

---

## 1. Méthode, graines, coût, contrôle témoin

### 1.1 Attestation d'ordre de travail

Les sections 2 à 5 — mesures, exclusions, consolidation et **verdict** — ont été écrites avant
toute ouverture du dossier `U5-gothique/`. Ce dossier n'a été lu qu'au moment de rédiger la
section 6. Le brief ne communiquait ni le chiffre atteint le 15/08, ni son écart au seuil.

**Réserve sur l'aveuglement.** L'aveuglement porte sur le résultat, pas sur le fait que le dossier
avait été conclu STOP : le brief le dit. Il y a donc un biais d'ancrage possible vers le STOP.
Il est signalé plutôt que dissimulé. Ce qu'il ne contamine pas : les volumes lus, les collapses de
buckets, ni les SERP — c'est-à-dire pas ce qui fabrique le chiffre.

### 1.2 Outillage

- **Découverte** : `scripts/kw_dfs.py`, endpoint `dataforseo_labs/google/keyword_suggestions/live`,
  `location_name: France`, `language_name: French`, tri par volume décroissant.
- **Volumes de tête et séries 12 mois** : `keywords_data/google_ads/search_volume/live`,
  `search_partners: false`, France / français.
- **SERP** : `serp/google/organic/live/advanced`, France / français, desktop, profondeur 20.
  Ce choix remplace la lecture navigateur `hl=fr&gl=fr` : il rend le même contenu de façon
  datable et reproductible, blocs Shopping et prix inclus. **Aucun bloc `paid` n'a été rendu
  sur aucune des 17 SERP** — voir la réserve du §8 sur la lecture des annonces texte.
- **SEMrush n'a pas été ouvert.** Aucun chiffre de ce rapport ne vient d'une autre base que
  DataForSEO / Google Ads France.

### 1.3 Contrôle témoin

`tufting` = **12 100** avant la première mesure et **12 100** après la dernière, à chacune des
quatre passes de découverte (attendu 12 100). Conforme. Aucun zéro silencieux.

### 1.4 Graines interrogées

**Graines du dossier d'origine** (les deux orthographes et les deux nombres) :

| Graine | Pages | Lignes rendues | Annoncées par l'API | Idées après dédup. |
|---|---:|---:|---:|---:|
| `gothique` | 2 | 2 000 | 6 406 | 1 341 |
| `robe gothique` | 1 | 162 | 162 | 116 |
| `vetement gothique` | 1 | 156 | 156 | 103 |
| `vêtement gothique` | 1 | 61 | 61 | 49 |
| `accessoire gothique` | 1 | 11 | 11 | 10 |
| `bijou gothique` | 1 | 8 | 8 | 7 |
| `bijoux gothique` | 1 | 51 | 51 | 37 |
| `decoration gothique` | 1 | 10 | 10 | 9 |
| `décoration gothique` | 1 | 21 | 21 | 16 |
| `corset gothique` | 1 | 25 | 25 | 18 |
| `sac gothique` | 1 | 31 | 31 | 23 |
| `t shirt gothique` | 1 | 16 | 16 | 8 |
| `emo` | 1 | 1 000 | 4 055 | 824 |

**Graines dérivées, ajoutées par la découverte** (les thèmes co-occurrents des graines ci-dessus
les ont fait apparaître ; elles sont signalées comme dérivées) :

`vetement punk` · `chaussure gothique` · `botte gothique` · `collier gothique` · `bague gothique` ·
`maquillage gothique` · `chambre gothique` · `meuble gothique` · `style gothique` ·
`boutique gothique` · `gothique femme` · `gothique homme` · `creepers`.

Deux graines restent tronquées à la profondeur lue : `gothique` (2 000 lignes lues sur 6 406
annoncées) et `emo` (1 000 sur 4 055). Le tri étant par volume décroissant, la traîne non lue est
sous le volume de la dernière ligne lue — 10 recherches/mois dans les deux cas. L'amputation rend
la mesure **conservatrice**, sur une traîne dont la section 4 montre qu'elle est très majoritairement
hors produit.

Ont également été mesurées, **au titre de la règle hiérarchique** (§3.3), 40 têtes parentes ou
adjacentes hors corpus de découverte : `goth`, `gothic`, `punk`, `grunge`, `steampunk`, `new rock`,
`demonia`, `killstar`, `creepers`, `mercredi addams`, `choker`, `collier croix`, `bottes plateforme`,
`y2k`, `pentagramme`, `dark academia`, etc.

### 1.5 Coût

| Poste | USD |
|---|---:|
| Découverte, graine `gothique` (2 pages) | 0,264 |
| Découverte, 12 graines du dossier (1 page) | 0,330 |
| Découverte, 12 graines dérivées (1 page) | 0,313 |
| Découverte, graine `creepers` (1 page) | 0,132 |
| `google_ads/search_volume/live`, 8 appels (≈ 750 mots-clés, séries 12 mois incluses) | 0,720 |
| `serp/google/organic/live/advanced`, 17 SERP | 0,060 |
| **Total** | **≈ 1,82 USD** |

À comparer aux 149 €/mois de SEMrush. Le cache disque de `kw_dfs.py` rend tout rejeu ultérieur gratuit.

### 1.6 Limites de calcul assumées

1. **Jamais de somme de volumes bruts.** Google pré-agrège les variantes proches ; le script
   regroupe par clé normalisée et retient le **MAX** du groupe. Vérifié : sur la seule graine
   `gothique`, 659 lignes sur 2 000 (33 %) étaient des reformulations d'une idée déjà comptée.
2. **Une troisième passe de collapse, faite à la main, que le script ne sait pas faire.**
   La normalisation de `kw_dfs.py` ne rapproche pas deux mots différents. Or Google sert dans le
   **même bucket** des paires comme `botte gothique` / `bottine gothique`, `deco gothique` /
   `decoration gothique`, `sac gothique` / `sacoche gothique`. Preuve retenue : **volume identique
   ET série 12 mois identique**, pas le seul volume ponctuel. Les 12 séries mensuelles des 643
   idées retenues ont donc été tirées et regroupées : **643 idées → 569 buckets, soit 4 710
   recherches/mois (11,6 %) qui étaient du double comptage.** Sans cette passe, le consolidé
   affichait 40 700 au lieu de 35 990 — c'est-à-dire qu'il **passait le seuil de 37 500 à tort**.
   Ce défaut doit être corrigé dans `kw_dfs.py` (§8).
3. **Deux têtes tronquées** (§1.4), dans le sens conservateur.
4. **Aucun bloc `paid`** n'a été rendu par l'API SERP : la concurrence publicitaire est lue par
   la présence de blocs Shopping / `popular_products` et par l'indice `competition` de Google Ads,
   **pas** par des annonces texte confirmées.

---

## 2. Mesure par famille

Périmètre du cluster adressable : les requêtes **produit** portant le vocabulaire de l'univers
(`gothique`, `goth`, `emo`), toutes familles confondues. Le détail des exclusions est en §4.

| Famille | Brut (avant collapse) | Net de marque | Idées distinctes → buckets | Reformulations supprimées |
|---|---:|---:|---:|---:|
| Vêtements | 18 860 | **16 530** | 319 → 281 | 12,4 % |
| Déco / maison | 7 470 | **6 700** | 115 → 104 | 10,3 % |
| Bijoux | 6 370 | **6 160** | 92 → 81 | 3,3 % |
| Chaussures | 5 060 | **3 950** | 56 → 47 | 21,9 % |
| Accessoires | 1 990 | **1 980** | 40 → 39 | 0,5 % |
| Sacs | 950 | **670** | 21 → 17 | 29,5 % |
| **Total** | **40 700** | **35 990** | **643 → 569** | **11,6 %** |

Lecture des colonnes : « brut » = somme des MAX par idée distincte rendue par le script ;
« net de marque » = après la troisième passe de collapse **et** après retrait des requêtes de
marque. La colonne « reformulations supprimées » mesure la seule troisième passe, celle que le
script ne faisait pas.

**Net de marque — les deux chiffres.** À l'intérieur du cluster, les requêtes de marque pèsent
**470 recherches/mois seulement** (Killstar, Punk Rave, Restyle, Devil Fashion, Shein, Amazon,
Etsy, Vinted, EMP, Alchemy, Demonia, AliExpress, Wish confondus) : `emo robot amazon` 170,
`bijoux alchemy gothique` 30, `shein gothique` 30, `amazon robe gothique` 30,
`chaussure gothique demonia` 30, puis 36 lignes à 20 ou moins. La déduction est donc négligeable
et le net ci-dessus vaut aussi bien brut de marque.

**Mais les marques pèsent lourd hors du cluster**, et c'est la lecture utile : `new rock` **22 200**,
`killstar` **9 900**, `demonia` **6 600**, `restyle` 1 600, `emp shop` 1 000, `punk rave` 880,
`devil fashion` 210, `gothicana` 210 — soit **42 600 recherches/mois de demande de marque**, plus
que le cluster générique tout entier. Dans cet univers, le client cherche une enseigne, pas une
catégorie.

**Saisonnalité (lecture qualitative des séries 12 mois).** Socle plat toute l'année avec une bosse
d'automne nette et courte sur les familles habillées : `robe gothique` passe de 880 à 2 900 sur un
seul mois, `corset gothique` de 170 à 480, `deguisement gothique` de 90 à 720, `maquillage gothique`
de 1 000 à 3 600. C'est le pic d'Halloween. Hors ce mois, aucune famille ne progresse : les séries
de `robe gothique`, `vetement gothique`, `bijoux gothique`, `sac gothique` sont plates sur 12 mois.
Le socle est stable — critère UNIVERS « socle ≥ 8 mois » respecté — mais il ne croît pas.

**CPC et concurrence Google Ads.** CPC médian par famille : Vêtements 0,28 $ · Bijoux 0,42 $ ·
Chaussures 0,27 $ · Sacs 0,37 $ · Accessoires 0,23 $ · Déco 0,19 $. `competition` = **HIGH** sur la
quasi-totalité des buckets produit, **LOW** sur toutes les têtes informationnelles. CPC bas et
compétition haute : marché de petits paniers très disputés.

---

## 3. Thèmes co-occurrents par famille — où se lisent les contaminations

C'est le cœur du dossier : le mot « gothique » est en français d'abord un mot d'histoire de l'art,
et « emo » est d'abord un nom de service.

### 3.1 Graine `gothique` (1 341 idées) — les 12 thèmes les plus lourds

| Terme co-occurrent | Idées | Volume cumulé | Nature |
|---|---:|---:|---|
| `style` | 64 | 13 110 | ambigu (§3.2) |
| `cathedrale` | 29 | 8 480 | architecture |
| `architecture` | 22 | 8 200 | architecture |
| `ecriture` | 30 | 7 240 | typographie |
| `quartier` | 18 | 6 400 | Barcelone |
| `art` | 39 | 5 820 | histoire de l'art |
| `lettre` | 41 | 4 710 | typographie |
| `barcelone` | 16 | 3 980 | géographique |
| `maquillage` | 20 | 3 410 | beauté / tutoriel |
| `alphabet` | 14 | 3 290 | typographie |
| `tatouage` | 27 | 3 010 | tatouage |
| `eglise` | 13 | 2 740 | architecture |
| `robe` | 35 | 4 500 | **produit** |
| `vetement` | 23 | 3 210 | **produit** |

Deux thèmes produit sur quatorze. C'est la signature d'un mot-univers accaparé par un autre sens.

### 3.2 Graine `emo` (824 idées) — les 10 thèmes les plus lourds

| Terme | Idées | Volume cumulé | Nature |
|---|---:|---:|---|
| `robot` | 49 | 3 720 | robot de bureau Living AI |
| `style` | 36 | 10 460 | sous-culture (informationnel) |
| `meme` | 26 | 1 530 | mème internet |
| `band` / `music` | 25 | 1 560 | genre musical |
| `roblo` (Roblox) | 18 | 460 | jeu vidéo |
| `midwest` | 14 | 500 | sous-genre musical |
| `hair` / `haircut` | 22 | 920 | coiffure |
| `outfit` | 15 | 420 | **produit** |
| `shirt` | 11 | 410 | **produit** |
| `cross` | 11 | 370 | **produit** |

Et surtout, hors table : `emo tv` **368 000**, `emo games net` 1 000, `emo nivi secure com` 390,
`emo sas` 390, `emo dlsi` 320, `emo avocat` 210, `villa emo` 140, `docteur emo le havre` 110,
`garage emo candé` 110, `emo troyes` 110. Le mot « emo » en France est massivement un nom propre :
service IPTV, robot, cabinet médical, garage, société.

### 3.3 Règle hiérarchique — niveaux testés et niveau retenu

Aucune famille ne passe le seuil sur sa formulation spécifique. Conformément à la règle, les
niveaux parents ont donc tous été mesurés **et testés en SERP** avant toute conclusion.

| Niveau testé | Volume | SERP réelle | Retenu ? |
|---|---:|---|---|
| `gothique` (tête d'univers) | 14 800 | Wikipédia *Architecture gothique*, Wikipédia *Mouvement gothique*, monuments-nationaux.fr, Grand Palais, BnF, CNRTL, Lonely Planet, Radio France, Hérodote. **Zéro marchand, zéro bloc Shopping.** | **Non** |
| `style gothique` | 6 600 | Wikipédia *Architecture gothique*, Grand Palais, BnF, AD Magazine, prepa-architecture.fr, Vikidia. Deux blogs e-commerce en position 3 et 10, en contenu éditorial. **Zéro bloc Shopping.** | **Non** |
| `architecture gothique` / `cathedrale gothique` / `architecte gothique` | 6 600 | — | **Non** |
| `emo` (tête d'univers) | 18 100 | Wikipédia, Reddit, Metalorgie, Spotify, Apple Music, **Indeed (offres d'emploi)**, Google Play, dictionnaires. **Zéro marchand, zéro Shopping.** | **Non** |
| `emo style` / `style emo` / `emo fashion style` | 4 400 | Wikipédia (fr et en), wikiHow, Vogue, Pinterest, Getty Images, blogs. **Un seul marchand sur 16 résultats** (EMP), aucun bloc Shopping. | **Non** |
| `goth` / `gothic` | 9 900 | Wikipédia *Goths* (peuple germanique), Géo, Académie française, Larousse, Cairn, Les Belles Lettres, Vikidia. | **Non** |
| `mercredi addams` | 74 000 | Netflix, Wikipédia, AlloCiné, IMDb, Fandom, programme-tv. Requête « où regarder la série ». | **Non** |
| `creepers` | 14 800 | **100 % marchande** : T.U.K., Underground, Discobole, Indien Boutique, EMP, La Petite Faucheuse, Miss Gothique, 7 blocs `popular_products`, 45–260 €. | **Voir ci-dessous** |
| `collier croix` | 6 600 | Histoire d'Or, Balla Bijoux, Sanctis, Croix Précieuse, aparanjanparis. Bijouterie religieuse grand public. | **Non** |
| `choker` | 5 400 | Zalando, Bershka, Zara, Stradivarius, Vogue. Mode grand public ; EMP Gothicana apparaît 2 fois en Shopping sur 6. | **Non** |
| `bottes plateforme` | 2 900 | Zalando, ASOS, Bershka, Buffalo. Satan Shop apparaît 1 fois sur 7 en Shopping. | **Non** |
| `punk` 18 100 · `grunge` 9 900 · `steampunk` 22 200 · `y2k` 27 100 · `pentagramme` 9 900 · `dark academia` 2 900 | — | Univers voisins ou symboles, non spécifiques au dossier ; les inclure serait redéfinir le dossier, pas le mesurer. | **Non** |

**Le cas `creepers` — la seule décision réellement difficile, et elle est déclarée non tranchée.**
La SERP de `creepers` est intégralement marchande et peuplée de boutiques gothiques françaises :
sur ce seul critère, la règle hiérarchique commanderait de la retenir. Mais deux faits l'interdisent
en l'état :
1. `creepers` et `creeper` (singulier) ont **exactement le même volume et la même série 12 mois** :
   c'est un seul bucket Google. Or `creeper` au singulier en France, c'est Minecraft — la découverte
   le confirme (`creepers minecraft` 3 600, `creepers minecraft lego` 2 400, `creepers from minecraft`
   1 900), tout comme le film *Jeepers Creepers* (5 formulations à 9 900, un seul bucket).
   Attribuer les 14 800 à la chaussure gothique reproduirait exactement l'erreur documentée du
   `bateau amorceur` (5 400 attribués à tort à un segment qui en pesait 4 390).
2. La SERP est tenue par des **marques** que le dropshipping générique ne peut pas servir :
   T.U.K., Demonia, Underground, New Rock.

**Retenu au titre de `creepers` : uniquement les formulations sans ambiguïté** —
`chaussure creepers` 2 400, `creepers homme` 590, `creepers femme` 320 = **3 310**. Elles ne portent
pas le mot « gothique » et n'entrent donc pas dans le consolidé du §5 ; elles y figurent comme
**variante haute**. C'est la plus grosse incertitude du dossier et elle est chiffrée comme telle.

---

## 4. Volumes retirés, chiffrés un par un

Volume brut total rendu par la découverte, après déduplication du script : **632 230**.
Volume retenu : **35 990**. Voici les 632 230 − 35 990 = **596 240** retirés.

### 4.1 « emo » hors sous-culture — 377 700

| Requête | Volume | Ce que c'est |
|---|---:|---|
| `emo tv` | **368 000** | Service IPTV. Série 12 mois de 673 000 à 201 000 : trafic de service, sans rapport avec le dossier |
| `emo robot` | 2 400 | Robot de bureau Living AI |
| `emo games net` | 1 000 | Site de jeux |
| `emo tv online` | 590 | idem `emo tv` |
| `emo emoji` | 590 | Émoticône |
| `emo nivi secure com` | 390 | Portail d'authentification |
| `emo sas` | 390 | Raison sociale |
| `emo pocket` | 320 | Produit Living AI |
| `midwest emo` | 320 | Sous-genre musical |
| `emo dlsi` 320 · `emo kitten` 320 · `emo robot prix` 320 · `emo avocat` 210 · `villa emo` 140 · `docteur emo le havre` 110 · `garage emo candé` 110 · `emo troyes` 110 · `emo hannover` 110 · `dr emo montmain` 70 | ≈ 2 500 | Sociétés, cabinets, lieux |
| 90 autres lignes | ≈ 900 | idem |

À lui seul, `emo tv` représente **58 % du volume brut du dossier**. Un dossier UNIVERS mesuré sans
cette exclusion afficherait 400 000 et serait un faux PASS massif.

### 4.2 Architecture, art et histoire — 51 140

`architecture gothique` 6 600 · `cathedrale gothique` 6 600 · `architecte gothique` 6 600
(**ces trois-là plus `style gothique` sont un seul bucket de 6 600** — volume et série 12 mois
identiques ; comptés une fois, pas quatre) · `gothique amiens` 4 400 · `art gothique` 2 400 ·
`eglise gothique` 1 900 · `expo gothique louvre-lens` 1 000 · `exposition gothique louvre-lens` 1 000 ·
`gothique flamboyant` 1 000 · `art gothique art roman` 720 · `gothique roman` 880 ·
`gothique romantisme` 880 · `architecture style gothique` 590 · `style architectural gothique` 590 ·
`chateau gothique` 480 · `voute gothique` 480 · `vitrail gothique` 390 · `vitraux gothique` 390 ·
`arche gothique` 390 · `gothique peinture` 390 · `peintre gothique` 390 · `manoir gothique` 390 ·
`cathédrale gothique france` 320 · `cathédrale gothique française` 320 · `gothique rayonnant` 320 ·
`fenetre gothique` 320 · `rosace gothique` 170 · `porte gothique` 90 · `maison gothique` 260 ·
+ 210 autres lignes ≈ 11 000.

### 4.3 Écriture, typographie, tatouage — 29 440

`ecriture gothique` 4 400 · `ecrire en gothique` 4 400 · `gothique lettre` 1 900 ·
`lettrage gothique` 1 900 · `alphabet gothique` 1 900 · `gothique police` 1 000 ·
`calligraphie gothique` 880 · `tatoueur gothique` 880 · `gothique tatouage` 880 ·
`ecriture gothique police` 590 · `century gothique` 590 (police *Century Gothic*) ·
`alphabet calligraphie gothique` 480 · `chiffre gothique` 480 · `gothique typo` 480 ·
`typographie gothique` 390 · `ecriture gothique generateur` 320 ·
`calligraphie gothique médiévale` 320 · `t shirt ecriture gothique` 30 ·
+ 127 autres lignes ≈ 7 500.

### 4.4 Têtes d'univers non adressables — 43 800

`emo` **18 100** · `gothique` **14 800** · `style gothique` (bucket architecture) **6 600** ·
`emo style` / `style emo` / `emo fashion style` (un seul bucket) **4 400**.
Justification SERP intégrale en §3.3. Ce sont les quatre plus gros volumes « propres » du dossier,
et aucun n'est achetable.

### 4.5 Culture, musique, média — 13 000

`92i gothique` 2 400 (album de Booba) · `emo meme` 880 · `gothique littérature` 480 ·
`film gothique` 480 · `gothique musique` 390 · `romance gothique` 390 · `catcheur gothique` 320 ·
`catcheuse gothique` 320 · `lorax personnage emo` 320 · `emo rap` 260 · `emo rappers` 260 ·
`emo music bands` 210 · `emo rock bands` 210 · `band emo` 210 · `gothique south park` 110 ·
`emo spongebob` 110 · `gothique ncis` 110 · + 197 lignes ≈ 6 000.

### 4.6 Informationnel hors achat — 9 480

`def gothique` 720 · `dessin gothique` 720 · `fond d'ecran gothique` 590 · `definition gothique` 480 ·
`gothique image` 390 · `emo definition` 390 · `gothique wallpaper` 320 · `fond gothique` 320 ·
`def emo` 320 · `que veut dire emo` 170 · `que veut dire gothique` 140 · `gothic vs emo` 110 ·
`emo vs goth` 110 · + 122 lignes ≈ 5 200.

### 4.7 Géographique et magasin physique — 9 100

`barcelone quartier gothique` 2 900 · `quartier gothique` 2 400 · `boutique gothique paris` 480 ·
`magasin gothique paris` 320 · `hotel barcelone quartier gothique` 210 ·
`quartier gothique barcelone espagne` 170 · `magasin gothique lyon` 140 ·
`magasin gothique autour de moi` 140 · `quartier gothique barcelone itineraire` 110 ·
`soiree gothique paris` 110 · + 88 lignes ≈ 2 100.
Le quartier gothique de Barcelone pèse à lui seul ≈ 6 000.

### 4.8 Maquillage, coiffure, ongles — 6 060

`gothique maquillage` 1 600 · `maquillage femme gothique` 480 · `gothique homme maquillage` 320 ·
`ongle gothique` 320 · `coiffeuse gothique` 320 · `coiffe gothique` 320 · `coiffure gothique` 320 ·
`maquillage gothique halloween` 210 · `maquillage gothique facile` 170 · `gothique makeup` 140 ·
`coupe emo` 390 · `emo hair` 170 · `emo haircut` 170 · + 68 lignes ≈ 1 300.
Retiré sur consigne (« le maquillage tutoriel »), et confirmé par la nature des requêtes :
`facile`, `halloween`, `tuto`. **Réserve** : `gothique maquillage` 1 600 est la 5ᵉ tête produit
potentielle du dossier ; une boutique gothique vend des cosmétiques. Le réintégrer ajouterait
au plus 6 060 et ne suffirait pas à franchir le seuil (35 990 + 6 060 = 42 050, toujours dans la
bande de cas limite).

### 4.9 Marques — 470 (§2) · Services, DIY, occasion — 230

`faire part mariage gothique` 40 · `dessin gothique facile a faire` 30 · `meuble gothique occasion` 20 ·
`patron robe gothique` 20 · `robe gothique occasion` 10 · `vetement gothique occasion` 10 · etc.

### 4.10 Reliquat non classé — ≈ 50 600 sur 1 034 lignes

Traîne à 10–140 recherches/mois : `meuf gothique` 390, `gothique personne` 320,
`gothique mouvement` 390, `blonde gothique` 110, `baka gothique` 110, `gothique latina` 50,
`emo pfp` 70, `emo dti` 110 (*Dress To Impress*, jeu Roblox)… Ni produit, ni exclusion nommée :
requêtes de curiosité, d'image et de vocabulaire. Aucune ligne au-dessus de 400.

### 4.11 Double comptage retiré par la troisième passe — 4 710

Le détail est en §1.6. Les plus lourds : `botte gothique` = `bottine gothique` (720 compté une
fois au lieu de deux), `decoration gothique` = `deco gothique` (480), `bottine femme gothique` =
`botte femme gothique` (320), `robe mariee gothique` = `robe gothique mariage` (260),
`sac gothique` = `sacoche gothique` (210).

---

## 5. Consolidé net, SERP marchandes, et verdict

### 5.1 Consolidé

| Famille | Volume net France, recherches/mois |
|---|---:|
| Vêtements | 16 530 |
| Déco / maison | 6 700 |
| Bijoux | 6 160 |
| Chaussures | 3 950 |
| Accessoires | 1 980 |
| Sacs | 670 |
| **CONSOLIDÉ NET** | **35 990** |

Variante haute, si l'on ajoute les formulations `creepers` non ambiguës (§3.3) : **39 300**.
Variante haute élargie, en réintégrant en outre le maquillage (§4.8) : **45 360**.
Toutes trois sont des estimations, hypothèses de déduplication comprises.

**Seuil applicable : 37 500** (mode UNIVERS, base DataForSEO, confort 50 000) —
`PRODUCT-RESEARCH-CRITERIA.md` §1, décision Hakim du 29/08/2026.
**Bande de cas limite : 30 000 – 45 000** (±20 %).

Le consolidé net **35 990 est à −4,0 % du seuil**, et donc **à l'intérieur de la bande**.
La variante haute 39 300 est **au-dessus du seuil**, et **également dans la bande**.
Aucune des trois lectures ne sort de la bande de cas limite. C'est précisément la situation où
la phase 3 n'a pas le droit de trancher.

### 5.2 Lecture des SERP marchandes

Là où l'intention est commerciale, elle l'est franchement, et la page 1 est déjà pleine.

| Requête | Intention | Blocs Shopping | Prix observés le 29/08/2026 |
|---|---|---|---|
| `vetement gothique` 1 000 | 100 % marchande | 5 `popular_products` | 19,59 – 249 € |
| `robe gothique` 1 300 | 100 % marchande | 6 blocs, 15 produits | 15,99 – 279 € |
| `chaussure gothique` 1 300 | 100 % marchande | 7 blocs | 38 – 173,80 € |
| `bijoux gothique` 590 | marchande | 3 blocs | 7,99 – 43,95 € |
| `decoration gothique` 480 | marchande, teintée Pinterest/Reddit | 4 blocs | 19,30 – 64,99 € |
| `croix gothique` 1 600 | **mixte** : 3 premiers résultats informationnels (« satanique ou chrétien ? », signification) | 4 blocs | 7,55 – 452 € |

**Spécialistes / DTC français tenant la page 1** (ils sont nombreux et souvent en domaine exact) :
Discobole, L'Antre Gothique, L'Esprit Gothique, Miss Gothique, La Petite Faucheuse, Gothyka,
Toonzshop, Pentagramme Shop, Satan Shop, Goth N' Rock, Gotyka, Ma Robe Gothique, Âme Gothique,
boutique-gothique.com, vetement-gothique.fr, chaussure-gothique.com, Dark Medusa, The Other Side,
La Boutique Curieuse, Freaky Pink, NinaNina, Ask & Embla, Grunge Boutik, Indien Boutique,
La Boutique Venue d'Ailleurs.

**Marketplaces et grandes enseignes** (repères seulement) : Amazon.fr, Etsy, Leboncoin,
Leroy Merlin (présent en Shopping sur `decoration gothique`), Idealo, Stylight, Zalando, ASOS,
Bershka, Zara, Stradivarius, Pinterest.

**Acteurs étrangers de taille sur le marché FR** : EMP / EMP-Online.fr (omniprésent, marque propre
*Gothicana*), Impericon, DevilInspired, Attitude Clothing, Killstar, Punk Rave, Demonia, New Rock,
T.U.K., Underground.

Bande de prix dominante : **20 – 110 €**, avec une masse notable sous 30 € (Amazon 7,55 € à 15,99 €,
La Petite Faucheuse 19,59 €, Gothyka 17,45 €). Le plancher de 50 € du §1 des critères n'est tenu
que sur les chaussures et une partie des robes.

### 5.3 Ce que le volume ne dit pas mais que la structure dit

Le plus gros bucket **achetable** de tout le dossier est `croix gothique` à **1 600** —
et son intention est mixte. Viennent ensuite `robe gothique` et `chaussure gothique` à 1 300,
`vetement gothique` à 1 000. Les 35 990 recherches se répartissent sur **569 buckets**, soit
**63 recherches/mois par bucket en moyenne**. Un univers sans aucune tête marchande au-dessus de
1 600 n'offre pas de point d'accroche Shopping : c'est une longue traîne de 569 requêtes, chacune
disputée par une quinzaine de spécialistes français déjà installés, plus EMP.

### 5.4 Verdict

**CAS LIMITE — décision Hakim requise.**

Le consolidé net (35 990) est dans la bande 30 000 – 45 000 ; la variante haute défendable (39 300)
aussi, de l'autre côté du seuil. La règle du §« Cas limite » interdit à la phase 3 de trancher.
Les deux côtés, sans arbitrage :

*Ce qui plaide pour poursuivre*
- 6 familles cohérentes qu'une même boutique sert naturellement — c'est un vrai univers de catalogue.
- Intention 100 % marchande partout où le mot « gothique » qualifie un produit, blocs Shopping
  présents sur les 6 têtes de famille.
- Socle stable sur 12 mois, plus un pic d'automne exploitable (Halloween).
- CPC bas (0,19 – 0,42 $).
- Un consolidé à −4 % du seuil, qui repasse au-dessus avec une hypothèse `creepers` défendable.

*Ce qui plaide pour arrêter*
- **Aucune tête marchande** : le plus gros bucket achetable pèse 1 600, et 569 buckets à 63/mois
  en moyenne ne se travaillent ni en Shopping ni en Search sans un catalogue déjà installé.
- Les deux têtes d'univers (`gothique` 14 800, `emo` 18 100) sont mortes en SERP : encyclopédie,
  architecture, dictionnaire, offres d'emploi. Il n'existe pas de requête générique de marque
  blanche pour entrer sur ce marché.
- **42 600 recherches/mois de demande de marque** hors cluster (New Rock, Killstar, Demonia, EMP…) :
  le client de cet univers cherche une enseigne.
- Page 1 saturée par ≈ 25 spécialistes français, souvent en domaine exact, plus EMP.
- Bande de prix 20 – 110 € avec une masse sous 30 € : sous le plancher de 50 €.
- Confort 50 000 hors d'atteinte, même en variante haute élargie.

Statut de préqualification : **CAS LIMITE**. Aucun `GO_FINAL`, aucun sourcing, aucune cartographie
de concurrence n'est autorisé par ce rapport.

---

## 6. Comparaison des deux chaînes

*Section écrite après ouverture de `analyses/2026-08-15-niches-univers/U5-gothique/` — les sections
1 à 5 ci-dessus n'ont pas été retouchées depuis.*

### 6.1 Ce que disait le 15/08

| Poste | 15/08, SEMrush France |
|---|---:|
| Mesure consolidée, 16 lectures KMT (`02-volume-consolide.md`) | 22 120 |
| + bloc ambigu arbitré en SERP (`03-arbitrage-serp.md`) | + 4 333 |
| **Total U5 corrigé** | **26 453** |
| Plancher UNIVERS base SEMrush | 30 000 |
| Écart | **− 3 547, soit − 11,8 %** |
| Étiquette portée dans `SYNTHESE.md` | **STOP volume, dossier vivant** |

### 6.2 Le verdict est-il le même ?

**Sur le chiffre : oui, à 8 points près. Sur l'étiquette : non, et c'est la règle qui a changé,
pas l'outil.**

| | 15/08 SEMrush | 29/08 DataForSEO |
|---|---:|---:|
| Consolidé net | 26 453 | 35 990 |
| Plancher de sa base | 30 000 | 37 500 |
| **Position relative au plancher** | **88,2 %** | **96,0 %** |
| Bande de cas limite de sa base | 24 000 – 36 000 | 30 000 – 45 000 |
| Dans la bande ? | **oui** | **oui** |
| Étiquette rendue | STOP volume | **CAS LIMITE** |

Les deux chaînes placent le dossier **sous son plancher et à l'intérieur de la bande de ±20 %**.
Elles sont d'accord sur le fond. La différence d'étiquette ne vient pas de la donnée : le rapport
du 15/08 travaillait au cadre Kraken `plancher / confort`, sans la règle « cas limite = ±20 % → ne
pas trancher » qui s'impose aujourd'hui à la phase 3. Rejugé avec la règle d'aujourd'hui, le
26 453 du 15/08 aurait lui aussi dû sortir en **CAS LIMITE**, pas en STOP.

**Contrôle de la calibration du 29/08.** Le facteur documenté est ×1,22–1,25 sur les têtes.
26 453 × 1,25 = **33 066**, contre **35 990** mesurés : **+ 8,8 %**. Sur le consolidé, la
recalibration du seuil (30 000 → 37 500) fait donc bien son travail — l'écart résiduel est du
même ordre que celui observé sur le rejeu rideaux (− 4,8 %), et de signe opposé.

### 6.3 Quelle famille fait basculer, et pourquoi

C'est ici que se trouve le vrai résultat de la session : **le consolidé est stable, les familles ne
le sont pas du tout.** Sur rideaux, les écarts par famille allaient de ×0,62 à ×1,27. Ici :

| Famille | 15/08 SEMrush | 29/08 DataForSEO | Écart |
|---|---:|---:|---:|
| **Décoration / maison** | 260 | 6 700 | **× 25,8** |
| **Sacs + accessoires** | 610 | 2 650 | × 4,34 |
| **Bijoux** | 3 370 | 6 160 | × 1,83 |
| **Textile / vêtements** | 9 790 | 16 530 | × 1,69 |
| **Chaussures** | 7 130 | 3 950 | **× 0,55** |
| Enseigne (`boutique gothique`) | 960 | non retenu | — |
| Bloc ambigu arbitré en SERP | 4 333 | non retenu | — |
| **Total** | **26 453** | **35 990** | **× 1,36** |

Trois causes, et **deux sur trois ne sont pas des différences d'outil** :

**1. Décoration, × 25,8 — une différence de construction de famille, pas de source.**
Le 15/08 a mesuré la famille Déco par une seule liste KMT sur la graine `decoration gothique` :
149 mots-clés, 370 en broad, et le rapport en conclut « *le volume broad de la famille entière est
de 370. Aucune consolidation ne peut la sauver.* » Ce n'est pas la famille entière : c'est la seule
formulation qui contient le mot « décoration ». La famille Déco d'une boutique gothique s'écrit
`meuble gothique` 260, `papier peint gothique` 260, `poupee gothique` 320, `miroir gothique` 210,
`cadre gothique` 210, `chambre gothique` 210, `statue gothique` 170, `tableau gothique` 170,
`lit gothique` 140, `lampe gothique` 140, `lustre gothique` 140, `peluche gothique` 140,
`puzzle gothique` 140, `lampadaire gothique` 140 — 104 buckets qu'aucune requête contenant
« décoration » ne ramène. **Le 15/08 avait lui-même signalé la faille** (« familles listées au
brief et non mesurées »), et son propre §5.3 étiquetait l'extrapolation 26 000–30 000 comme
hypothèse. La chaîne DataForSEO ne mesure pas mieux : elle a été utilisée avec une graine large
(`gothique`, 2 000 lignes) plus un lexique produit, au lieu d'une graine par famille. **Le même
écart serait apparu en refaisant le dossier à la SEMrush avec cette méthode-là.**

**2. Chaussures, × 0,55 — là, c'est bien l'outil, et DataForSEO a raison.**
Le 15/08 additionnait explicitement les variantes d'ordre et de nombre :
« *`chaussure gothique` 880 coexiste avec `gothique chaussure` 590, `chaussures gothiques` 480,
`chaussures gothique` 260, `chaussure gothiques` 210, `chaussur gothique` 170,
`gothique chaussures` 170 : 2 760 au lieu de 880 sur ce seul bloc* », puis ajoutait `botte` 2 060
et `bottine` 1 230 comme familles distinctes. Or `botte gothique` et `bottine gothique` ont
**le même volume et la même série 12 mois** (720, `[480, 390, 480, 390, 480, 590, 880, 1000, 1000,
1000, 1000, 880]`) : c'est un seul bucket Google, servi par une seule page de résultats. Les 7 130
du 15/08 comptent le même bucket jusqu'à sept fois. **C'est le défaut de méthode que la bascule
vers DataForSEO corrige**, et il valait ici ×1,8 sur la famille la plus lourde du dossier de 2026.

**3. Périmètre — les deux rapports n'excluent pas les mêmes choses.**
Le 15/08 sortait du total 18 980 recherches « ambiguës » (`femme gothique`, `gothique homme`,
`style gothique femme`, `gothique sexy`…) puis en réintégrait 4 333 après arbitrage SERP ;
il excluait aussi `croix gothique` (1 300 chez lui, 1 600 chez moi) comme « architecture ou
pendentif, non tranché », le halloween/déguisement, et la robe de mariée. J'ai retenu
`croix gothique` (SERP mixte, documentée) et le déguisement gothique, et exclu au contraire
l'enseigne `boutique gothique` (960) et l'intégralité du bloc femme/homme comme non-produit.
**Ces choix de périmètre pèsent ± 5 000 dans les deux sens et sont indépendants de l'outil.**

### 6.4 Ce sur quoi les deux chaînes tombent exactement d'accord

- **`gothique` nu est une tête morte.** 15/08 : « 2 positions marchandes sur 8, Aperçu IA
  entièrement culturel, Autres questions 4/4 définitionnel ». 29/08 : Wikipédia, monuments
  nationaux, Grand Palais, BnF, CNRTL, zéro bloc Shopping. Même conclusion, deux outils.
- **`emo` ne vaut rien commercialement.** 15/08 : « CPC 0,00 sur 13 700 recherches de style —
  personne n'achète de trafic sur ce terrain », contribution au total = 0. 29/08 : SERP Wikipédia /
  Reddit / Spotify / **Indeed** / Google Play, et 368 000 des 377 700 du bloc `emo` sont un service
  IPTV. Même conclusion.
- **Aucune marque ne pèse dans le cluster.** 15/08 : « aucune marque de la liste de garde n'atteint
  40 recherches/mois ». 29/08 : 470 au total sur tout le corpus. Identique.
- **`92i gothique` = Booba**, classé informationnel des deux côtés.
- **Le quartier gothique de Barcelone et l'architecture** sont exclus des deux côtés.
- **Aucune annonce Search texte n'a pu être confirmée** des deux côtés — voir §8.

---

## 7. La question qui compte : peut-on résilier SEMrush sur cette base ?

**Réponse courte : oui pour la donnée, non pour la méthode — et la méthode a besoin d'un correctif
avant la prochaine mesure.**

**Ce que ce rejeu démontre.** En zone de décision, sur un dossier à moins de 12 % de son plancher,
la chaîne DataForSEO reproduit la position SEMrush relative au seuil à **8 points près** (96,0 %
contre 88,2 %) une fois la recalibration du 29/08 appliquée. Elle place le dossier du même côté du
plancher, dans la même bande de cas limite, et elle reproduit à l'identique les quatre conclusions
qualitatives structurantes (tête `gothique` morte, `emo` sans valeur commerciale, marques nulles
dans le cluster, contamination architecture/typographie). Sur ce qui fabrique un verdict, les deux
chaînes disent la même chose. Le coût est de **1,82 USD** contre 149 €/mois.

**Ce que ce rejeu démontre aussi, et qui est plus important que la comparaison des outils :
la dispersion par famille est bien plus grande que sur rideaux — ×0,55 à ×25,8 contre ×0,62 à ×1,27.**
Aucune décision ne doit être prise sur une famille isolée mesurée par une seule chaîne. Le
consolidé est robuste ; ses composants ne le sont pas.

**Les trois réserves qui conditionnent la résiliation.**

1. **`kw_dfs.py` doit être corrigé avant la prochaine mesure — c'est bloquant.**
   Sans la troisième passe de collapse faite à la main ici, le consolidé affichait **40 700** au
   lieu de 35 990, c'est-à-dire **au-dessus du seuil de 37 500** : un **faux PASS**, dans la zone
   exacte où le faux PASS coûte le plus cher. Le correctif est identifié et testé : fusionner deux
   groupes quand **volume identique ET série 12 mois identique**, ce qui exige de tirer les séries
   `google_ads/search_volume/live` pour tous les mots-clés retenus (coût constaté : 0,18 USD pour
   643 mots-clés). Cette règle est déjà celle du rejeu rideaux ; elle n'est simplement pas dans le
   script.

2. **La construction des familles doit être normalisée, indépendamment de l'outil.**
   L'écart ×25,8 sur la Déco vient d'une graine par famille (15/08) contre graine large + lexique
   produit (29/08). Les deux méthodes sont défendables ; mélangées, elles rendent deux dossiers
   incomparables. En mode UNIVERS, la règle devrait être explicite : **graine large de l'univers
   à 2 pages minimum, PUIS une graine par famille**, jamais l'une sans l'autre.

3. **La lecture des annonces Search reste un trou dans les deux chaînes.**
   Voir §8. Ni le 15/08 ni le 29/08 n'ont pu confirmer une seule annonce texte.

**Recommandation, qui n'est pas une décision.** La résiliation est soutenable sur la base de ce
rejeu, à condition que le point 1 soit corrigé **avant** la prochaine mesure servant de gate.
Tant qu'il ne l'est pas, la chaîne DataForSEO surévalue les consolidés d'environ 12 % — soit
précisément la largeur de l'erreur qui fait passer un dossier de bord.

---

## 8. Réserves — aucune n'est retirée

1. **Aveuglement imparfait.** Le brief indiquait que le dossier avait été conclu STOP le 15/08.
   Biais d'ancrage possible vers le STOP ; les volumes, collapses et SERP n'en dépendent pas.
2. **Deux graines tronquées** : `gothique` (2 000 lignes lues sur 6 406) et `emo` (1 000 sur 4 055).
   Traîne non lue sous 10 recherches/mois. Sens conservateur.
3. **Le collapse de buckets n'a été fait que sur les 643 idées retenues**, pas sur les 2 296 idées
   exclues. Les volumes du §4 sont donc des maxima, pas des nets — cela ne change aucun total
   retenu, mais interdit de citer « 596 240 retirés » comme un chiffre net.
4. **Aucun bloc `paid` rendu par l'API SERP sur les 17 requêtes.** Je ne peux pas en conclure
   qu'aucun annonceur n'achète ces requêtes. Les blocs `popular_products` observés sont des
   **listings Shopping**, pas des annonces texte confirmées. À traiter comme « non observé »,
   exactement comme le 15/08.
5. **`creepers` non tranché** (§3.3) : entre 0 et 14 800 selon la part attribuable à la chaussure
   plutôt qu'à Minecraft et au film *Jeepers Creepers*. Retenu à 3 310 en variante haute seulement.
   C'est la plus grosse incertitude chiffrée du dossier.
6. **`croix gothique` 1 600 à intention mixte** : trois premiers résultats organiques informationnels
   (« satanique ou chrétien ? »), quatre blocs Shopping. Retenu ; le retirer ramène le consolidé à
   34 390 sans sortir de la bande.
7. **Maquillage retiré sur consigne** (6 060). Une boutique gothique vend des cosmétiques ; sa
   réintégration porterait le consolidé à 42 050, toujours dans la bande.
8. **Familles adjacentes écartées sur SERP mais non nulles** : `choker` 5 400, `bottes plateforme`
   2 900, `collier croix` 6 600 comportent chacune une part goth minoritaire, non quantifiable
   sans données de clics. Elles sont un vivier, pas un volume.
9. **Séries mensuelles : l'ordre des 12 mois n'a pas été vérifié** contre le calendrier. La lecture
   de saisonnalité du §2 est qualitative (« un pic d'automne court ») et ne date pas le pic.
10. **Aucun prix relevé hors SERP.** Les fourchettes du §5.2 viennent des blocs Shopping du
    29/08/2026, pas d'une sonde Google Shopping dédiée ni d'une visite marchand.
11. **Aucune cartographie de concurrence n'a été faite.** Le §5.2 compte des apparitions en page 1 ;
    il ne dit rien de l'arborescence, du trafic ni de la nature drop des acteurs cités.
12. **Aucun sourcing, aucun `GO_FINAL`.** Le statut rendu est `CAS LIMITE — décision Hakim requise`.
