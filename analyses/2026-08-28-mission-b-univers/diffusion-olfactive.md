# Mission B — UNIVERS « Diffusion olfactive intérieure »

**Date de toutes les lectures : 28/08/2026.** Mode **UNIVERS**. Seuil applicable :
volume **consolidé par familles ≥ 30 000/mois**, confort 40 000
(`PRODUCT-RESEARCH-CRITERIA.md` §1). Le seuil PRODUIT PUR de 10 000 par cluster ne
s'applique pas ici et n'a pas été utilisé.

Méthode : `METHODE-ANALYSE-MARCHE.md` étapes 2 à 5 + 9, skill `recherche-mots-cles`
(Mission B). Candidat #11 de la shortlist 30×30 du 22/08.

---

## 1. Entrée et méthode

### Source d'entrée

`boutique-pipeline/analyses/2026-08-28-mission-b-univers-preparation.md` §5.2 (plan de
graines), lui-même issu de `shortlist-30-univers.md` du 22/08 (somme indicative 87K,
sonde prix 64,99 €, preuve boutique `ambiance-parfum.com` — 9 ads, 1 754 j d'ancienneté).
Toutes les valeurs de la shortlist sont traitées comme **non revérifiées** et remesurées
ici (catalogue des pièges, contrôle n° 8).

### Outil et paramètres

SEMrush **Keyword Magic Tool**, `?q=<expression>&db=fr&mt=phrase&currency=eur`,
100 lignes par graine, 0 crédit consommé. **Base de données : France. Devise : EUR**
(vérifié dans l'interface à chaque passe, pas déduit de l'URL). Les CPC de ce rapport
sont donc **en euros**, et non en dollars comme le veut l'affichage par défaut de la
maison.

### Contrôle témoin — avant et après

| Moment | Requête | Ligne `tufting` attendue | Lue | Base | Devise |
|---|---|---|---|---|---|
| Avant la première mesure | `?q=tufting&db=fr&mt=phrase` | 8 100 | **8 100** | France | EUR |
| Après la dernière mesure | `?q=tufting&db=fr&mt=phrase` | 8 100 | **8 100** | France | EUR |

Les deux témoins sont conformes : le quota n'était pas épuisé et la session n'est pas
tombée pendant la campagne. Aucun zéro silencieux à craindre sur les lectures ci-dessous.

### Les cinq contrôles, appliqués à chaque passe

1. **Deux orthographes.** Systématique. Résultat non trivial : la règle ne se vérifie pas
   partout, et c'est mesuré, pas supposé. `diffuseur bâtonnets` (3 940) et
   `diffuseur batonnets` (9 020) sont **deux corpus quasi disjoints** — 6 lignes communes
   pour 620 de volume. `bougie parfumée` (48 360) et `bougie parfumee` (10 120) :
   **0 ligne commune**. À l'inverse, `fondant parfumé` / `fondant parfume` et
   `coffret senteur` / `coffret senteurs` rendent **exactement le même corpus**
   (100 lignes communes sur 100). L'orthographe se teste, elle ne se présume pas.
2. **Plusieurs niveaux de généralité.** Trois niveaux par famille, mesurés **séparément
   et jamais additionnés**. Les catégories parentes (`diffuseur`, `bougie`,
   `huile essentielle`) sont mesurées et **entièrement exclues du consolidé** — voir §5.
3. **`n/a` ≠ `0`.** Distingués partout. `n/a` = sous le seuil de restitution SEMrush
   (< 10/mois). Cas particulier rencontré : la grappe `recharge parfum interieur`
   affiche « Pour afficher les métriques, actualisez la page » sur la quasi-totalité de
   ses lignes — ce n'est **ni un zéro ni un n/a**, c'est une **non-restitution
   d'affichage**, signalée comme telle et non convertie en chiffre.
4. **Mot-clé témoin.** Voir tableau ci-dessus.
5. **Plancher de lecture.** Quatre graines ont leur **100ᵉ ligne encore haute** et sont
   donc des **planchers, pas des totaux** : `diffuseur huile essentielle` (100ᵉ = 210),
   `bougie parfumée` (140), `diffuseur` parent (590), `bougie` parent (1 900),
   `huile essentielle` parent (1 600). Signalés ligne par ligne au §2.

### Recoupement : mesuré, jamais estimé

Les 100 lignes de chaque graine ont été **accumulées dans un index unique** au fil de la
campagne (2 656 mots-clés distincts). Un mot-clé déjà vu est **compté une seule fois** et
reste attaché à la première famille qui l'a réclamé. Le recoupement inter-graines est
donc une **mesure**, colonne « déjà vu » du §2, et non une estimation. Jamais un mot dans
deux familles.

### Limites de calcul, dites franchement

- Le total d'une famille est la **somme des lignes retenues une par une**. Le
  « Volume total » affiché par SEMrush en tête de requête n'a **jamais** été utilisé : sur
  le témoin `tufting` il annonce 78 920 quand la tête réelle vaut 8 100.
- Lecture bornée à **100 lignes par graine**. Là où la 100ᵉ ligne est encore haute, le
  chiffre est un plancher.
- Les SERP ont été lues dans le Chrome de Hakim, **avec une session Google connectée**
  (avatar de compte visible). Le mandat demandait une session non connectée : **écart
  déclaré**. La composition des pages 1 relevées est cohérente avec des SERP commerciales
  standard, mais la personnalisation ne peut pas être exclue.
- **Les annonces Search texte n'ont pas pu être isolées.** Les pages 1 comportent 1 à 2
  mentions « Sponsorisé / Annonce », ce qui ne permet pas de distinguer un carrousel
  Shopping sponsorisé d'annonces texte confirmées. Aucune conclusion n'est tirée sur la
  pression publicitaire Search.
- Page 1 seulement : rien n'est affirmé sur la profondeur de la concurrence.
- Les prix relevés sont **datés du 28/08/2026** et lus en page de résultats, pas en fiche
  produit. Certains blocs affichent un prix suivi de frais de port (`30,00` puis `4,90`
  répétés) : ces répétitions n'ont pas été comptées comme des points de prix distincts.

---

## 2. Mesure par graine

KMT expression exacte, `db=fr`, devise EUR, lecture du **28/08/2026**.
`S` = somme des 100 lignes affichées. « Déjà vu » = lignes/volume déjà présents dans
l'index au moment de la lecture (recoupement mesuré).

### Famille F1 — Diffuseur électrique

| Graine | Tête de grappe | Vol. tête | KD | CPC (EUR) | Intention | S (100 l.) | 100ᵉ ligne | Déjà vu |
|---|---|---|---|---|---|---|---|---|
| `diffuseur huile essentielle` | `diffuseur huile essentielle` | **14 800** | 47 | 0,18 | C | **80 750** | **210 → PLANCHER** | — (1ʳᵉ graine) |
| ″ (2ᵉ ligne, même grappe) | `diffuseur huiles essentielles` | 14 800 | 37 | 0,18 | I | — | — | — |
| `diffuseur parfum maison` | `diffuseur parfum maison` | **2 900** | 29 | 0,45 | I | 5 810 | n/a | 100 l. / 5 810 * |
| `diffuseur nébulisation` | `diffuseur huiles essentielles nébulisation` | 720 | 19 | 0,16 | I | 4 040 | n/a | 4 l. / 1 840 |
| `diffuseur ultrasonique` | `diffuseur ultrasonique` | 480 | 16 | 0,19 | I | 2 950 | n/a | 5 l. / 0 |

\* La grappe `diffuseur parfum maison` avait été écrite dans l'index par un appel dont la
réponse a expiré ; la relecture a confirmé les **mêmes 100 lignes et le même S de 5 810**.
Le chiffre est donc doublement lu, pas doublement compté.

Observation : `diffuseur nébulisation` **n'existe pas comme tête** — la formulation
spécifique de la maison ne porte rien, c'est `diffuseur huiles essentielles nébulisation`
qui porte le volume. Le mot de spécialiste ne se cherche pas nu.

### Famille F2 — Parfum d'intérieur / bâtonnets

| Graine | Tête de grappe | Vol. tête | KD | CPC (EUR) | Intention | S (100 l.) | 100ᵉ | Déjà vu |
|---|---|---|---|---|---|---|---|---|
| `parfum d'intérieur` | `parfum d'intérieur` | **3 600** | 25 | 0,43 | I | 15 240 | n/a | 2 l. / 110 |
| `parfum d'ambiance` | `parfum d'ambiance` | **2 900** | 28 | 0,47 | I | 19 180 | n/a | 0 |
| ″ | `parfum d ambiance` | 2 400 | 20 | 0,47 | I | — | — | — |
| ″ | `parfums d ambiance` | 1 900 | 19 | 0,47 | I | — | — | — |
| `diffuseur batonnets` (sans accent) | `batonnet pour diffuseur` | 1 300 | 14 | 0,35 | I | 9 020 | n/a | 6 l. / 620 |
| ″ | `diffuseur batonnet` | 1 300 | 15 | 0,35 | I | — | — | — |
| `diffuseur bâtonnets` (accentué) | `bâtonnets diffuseur` | 1 000 | 15 | 0,31 | I | 3 940 | n/a | 5 l. / 0 |
| `batonnet parfum` | `batonnet parfumé` | 720 | 19 | 0,37 | I | 6 320 | n/a | 35 l. / 4 190 |
| `senteur maison` | `senteur maison` | 1 000 | 30 | 0,46 | I | 5 650 | n/a | 12 l. / 320 |
| `bouquet parfumé` | `bouquet parfumé` | 590 | 15 | 0,45 | I | 5 290 | n/a | 0 |
| `parfum interieur maison` (sans accent) | `parfum interieur maison` | **90** | 30 | 0,42 | I | 90 (55 lignes) | — | 0 |

`bouquet parfumé` est un **mot générique contaminé** (piège n° 3 et n° 4) : les 2ᵉ et 3ᵉ
lignes de sa grappe sont `parfum miss dior blooming bouquet` (390) et
`miss dior blooming bouquet parfum` (320) — du parfum de peau Dior, plus des bouquets de
fleurs. Traité au §4.

### Famille F3 — Recharges

| Graine | Tête de grappe | Vol. tête | KD | CPC (EUR) | Intention | S | 100ᵉ | Déjà vu |
|---|---|---|---|---|---|---|---|---|
| `recharge diffuseur` | `recharge diffuseur parfum` | **880** | 12 | 0,35 | I | 7 760 | n/a | 1 l. / 0 |
| ″ | `air wick recharge pour diffuseur` | 390 | 17 | 0,09 | I | — | — | — |
| `recharge parfum d'intérieur` | `recharge parfum d'intérieur` | **110** | 9 | 0,37 | I | 110 (33 lignes) | — | 0 |
| `recharge parfum interieur` (sans accent) | `recharge parfum interieur` | **50** | 10 | 0,34 | I | Volume total affiché **60** sur 18 mots-clés | — | non fusionné |

Sur la graine sans accent, 17 des 18 lignes affichent
« Pour afficher les métriques, actualisez la page » : **non restituées**, ni `0` ni `n/a`.
Elles n'ont pas été intégrées à l'index, et le volume de 60 est celui affiché par
l'outil, pas une somme reconstruite.

### Famille F4 — Bougies et fondants

| Graine | Tête de grappe | Vol. tête | KD | CPC (EUR) | Intention | S (100 l.) | 100ᵉ | Déjà vu |
|---|---|---|---|---|---|---|---|---|
| `bougie parfumée` (accentué) | `bougie parfumée` | **12 100** | 31 | 0,67 | I | **48 360** | **140 → PLANCHER** | 0 |
| ″ | `bougies parfumées` | 4 400 | 29 | 0,76 | C | — | — | — |
| `bougie parfumee` (sans accent) | `bougies parfumees` | 1 600 | 31 | 0,67 | T | 10 120 | n/a | **0** |
| `brule parfum` | `brule parfum` | **3 600** | 15 | 0,29 | I | 9 490 | n/a | 5 l. / 550 |
| `fondant parfumé` | `fondant parfumé` | **1 900** | 10 | 0,26 | I | 9 140 | n/a | 0 |
| `fondant parfume` (sans accent) | idem | idem | idem | idem | idem | 9 140 | n/a | **100 l. / 9 140 — corpus identique** |
| `bougie cire végétale` | `bougie cire végétale` | 720 | 17 | 0,36 | I | 3 020 | n/a | 0 |
| `bougie cire vegetale` (sans accent) | `cire bougie vegetale` | 720 | 13 | 0,36 | I | 2 200 | n/a | 1 l. / 0 |

### Famille F5 — Coffrets

| Graine | Tête de grappe | Vol. tête | KD | CPC (EUR) | Intention | S | 100ᵉ | Déjà vu |
|---|---|---|---|---|---|---|---|---|
| `coffret bougie` | `coffret bougie` | **2 400** | 16 | 0,45 | I | 12 920 | n/a | 9 l. / 4 920 |
| `coffret senteur` | `coffret senteur` | **390** | 15 | 0,56 | IT | 1 320 | n/a | — |
| `coffret senteurs` | idem | idem | idem | idem | idem | 1 320 | n/a | **100 l. / 1 320 — corpus identique** |
| `coffret parfum maison` | `coffret parfum maison` | **70** | 13 | 0,62 | I | 70 (25 lignes) | — | 0 |

La graine du brief `coffret parfum maison cadeau` a été élargie à
`coffret parfum maison` (formulation plus courte, donc plus englobante en expression
exacte) : elle ne rend que **70**. La demande de coffret existe, mais elle se dit
`coffret bougie`, pas `coffret parfum maison`.

### Famille F6 — Voiture (extension)

| Graine | Tête de grappe | Vol. tête | KD | CPC (EUR) | Intention | S (100 l.) | 100ᵉ | Déjà vu |
|---|---|---|---|---|---|---|---|---|
| `parfum voiture` | `parfum voiture` | **2 900** | 16 | 0,21 | I | 21 590 | n/a | 14 l. / 2 760 |
| `desodorisant voiture` (sans accent) | `desodorisant voiture` | **2 900** | 15 | 0,21 | I | 5 280 | n/a | 0 |
| `diffuseur voiture` | `diffuseur voiture` | **2 400** | 17 | 0,27 | I | 13 970 | n/a | 9 l. / 1 000 |
| `désodorisant voiture` (accentué) | `désodorisant voiture` | **2 400** | 16 | 0,21 | I | 7 960 | n/a | 0 |

### Niveaux parents — mesurés, jamais additionnés au consolidé

| Graine parente | Tête | Vol. | KD | CPC (EUR) | S (100 l.) | 100ᵉ | Déjà couvert par mes familles | Verdict d'adressabilité |
|---|---|---|---|---|---|---|---|---|
| `bougie` | `bougie` | **40 500** | 26 | 0,77 | 419 000 | **1 900 → PLANCHER** | 2 l. / 16 500 | **Non adressable tel quel.** 2ᵉ et 3ᵉ lignes = `bougie de charroux` (18 100) et `les bougies de charroux` (14 800), une marque/lieu. La grappe mélange bougie d'allumage, bougie d'anniversaire, bougie LED, bougie de gâteau. |
| `huile essentielle` | `huile essentielle` | **60 500** | 44 | 0,66 | 347 300 | **1 600 → PLANCHER** | 7 l. / 38 400 | **Non adressable.** ≥ 75 500 de volume explicitement thérapeutique/cosmétique dans les 100 lignes lues — voir §4. |
| `diffuseur` | `diffuseur cheveux` | **18 100** | 24 | 0,14 | 187 990 | **590 → PLANCHER** | 33 l. / **66 680** | **Non adressable tel quel.** La **tête du parent est un sèche-cheveux** : `diffuseur cheveux` 18 100, `seche cheveux diffuseur` 8 100, `diffuseur seche cheveux` 4 400 — **46 910 de contamination coiffure sur 187 990 (25 %)**. |

**Ce que le test hiérarchique donne, dans les deux sens.** Le parent `diffuseur` ne
« libère » aucun volume supplémentaire : 66 680 de son contenu est **déjà** dans mes
familles, et son plus gros bloc restant est du sèche-cheveux. C'est exactement le
contre-exemple `bateau amorceur` : on n'attribue pas 187 990 à la diffusion olfactive.
Symétriquement, aucune famille n'était sous le seuil sur sa formulation spécifique — la
règle hiérarchique n'a donc pas eu à sauver un STOP, elle a servi à **empêcher un faux
positif**.

---

## 3. Consolidation par familles — brut ET net de marque

Règle appliquée : **on additionne ce qu'une même page de collection servirait**, et rien
d'autre. Jamais un mot dans deux familles. Le « brut » est la somme des lignes de la
famille après déduplication inter-graines mesurée ; le « net » est ce qui reste après
retrait des quatre motifs d'exclusion.

Marques et enseignes retirées (liste appliquée mot par mot sur les 2 656 lignes) :
Diptyque · Maison Berger / Lampe Berger · Yankee Candle · Durance · Esteban · Rituals ·
Bougies la Française · Jo Malone · Air Wick · Febreze · Glade · Ambi Pur · Woodwick ·
PartyLite · Scentsy · Cire Trudon · Fragonard · Molinard · Panier des Sens · Mathilde M ·
Lothantique · Baobab · Millefiori · Voluspa · My Jolie Candle · Bougies de Charroux ·
L'Occitane · Yves Rocher · Dior · Chanel · Guerlain · Kenzo · Armani · Lancôme ·
Action · Gifi · Amazon · IKEA · Maisons du Monde · Nature & Découvertes · Aroma-Zone ·
Zara · Sephora · Nocibé · Marionnaud · Lidl · Aldi · Temu · Shein · Leroy Merlin ·
Casa · Centrakor · Stokomani · HEMA · Primark · Muji · Carrefour · Auchan · Leclerc ·
Intermarché · Cdiscount · Søstrene Grene · Flying Tiger · Castorama · Conforama ·
Truffaut · Jardiland · Pylônes · Norauto · Feu Vert · TotalEnergies · Bosch · NGK ·
Michelin.

| Famille | Brut | Marque / enseigne | Hors-sujet | Thérapeutique | DIY / matière première | Informationnel | **Net adressable** |
|---|---|---|---|---|---|---|---|
| **F1** Diffuseur électrique | 91 710 | 10 140 | 260 | 930 | 0 | 0 | **80 380** |
| **F2** Parfum d'intérieur / bâtonnets | 59 490 | 11 570 | 1 110 | 1 070 | 210 | 290 | **45 240** |
| **F3** Recharges | 7 870 | 3 410 | 0 | 70 | 0 | 0 | **4 390** |
| **F4** Bougies et fondants | 81 190 | 2 300 | 900 | 340 | 11 810 | 2 150 | **63 690** |
| **F5** Coffrets | 9 390 | 2 020 | 0 | 0 | 0 | 0 | **7 370** |
| **Sous-total cœur maison (F1–F5)** | **249 650** | **29 440** | **2 270** | **2 410** | **12 020** | **2 440** | **201 070** |
| **F6** Voiture (extension) | 45 040 | 8 020 | 0 | 70 | 0 | 0 | **36 950** |
| **Total F1–F6** | **294 690** | **37 460** | **2 270** | **2 480** | **12 020** | **2 440** | **238 020** |

### Le test « une page ou deux ? », famille par famille

- **F1 et F2 restent séparées.** `diffuseur huile essentielle` (appareil électrique,
  consommable liquide) et `parfum d'intérieur à bâtonnets` (diffusion passive, pas
  d'électricité) sont deux rayons distincts chez tous les spécialistes observés en SERP.
  Deux pages.
- **`parfum d'intérieur` et `parfum d'ambiance` fusionnent dans F2.** Leurs SERP sont
  quasi superposables (§5) : Esteban, Durance, L'Occitane, Mathilde M, Fragonard, Maison
  Berger, Panier des Sens, plus les mêmes comparateurs. Une seule page les sert.
  Recoupement mesuré entre les deux grappes : **0 ligne** — ce sont bien des recherches
  distinctes qu'une page unique capte, cas Noirmont exact.
- **F3 reste séparée de F1 et F2.** Une page « Recharges » est une décision d'offre
  (réachat), pas une variante d'écriture.
- **F4 reste séparée.** Une bougie n'est pas un diffuseur.
- **F5 reste séparée** : le coffret est un mode d'achat (cadeau), il appelle sa page.
- **F6 est une extension, pas une famille du cœur** : elle est comptée à part et le
  consolidé retenu au §6 est donné **avec et sans** elle.

### Réserve chiffrée sur la méthode d'addition — hypothèse prudente

SEMrush restitue des variantes quasi identiques à volume identique
(`diffuseur huile essentielle` 14 800 **et** `diffuseur huiles essentielles` 14 800 ;
`parfum pour bougie` 1 600 **et** `parfums pour bougie` 1 600). La méthode Noirmont
autorise à les additionner — ce sont des recherches distinctes qu'une même page sert —
mais l'honnêteté impose de mesurer ce que vaut le consolidé si l'on **ne garde qu'un
volume par formulation normalisée** (accents, pluriels, ordre des mots et mots-outils
neutralisés, volume maximum retenu) :

| Famille | Net (addition Noirmont) | Net (hypothèse prudente, 1 volume par formulation normalisée) |
|---|---|---|
| F1 | 80 380 | 50 740 |
| F2 | 45 240 | 22 310 |
| F3 | 4 390 | 3 200 |
| F4 | 63 690 | 48 360 |
| F5 | 7 370 | 4 590 |
| **Cœur F1–F5** | **201 070** | **129 200** |
| F6 | 36 950 | 15 910 |
| **Total F1–F6** | **238 020** | **145 110** |

Les deux hypothèses sont données. **Aucune des deux ne change le verdict de volume** :
même la plus prudente franchit le seuil UNIVERS de 30 000 d'un facteur supérieur à 4.

---

## 4. Volume thérapeutique retiré — chiffré et motivé

C'est le piège annoncé sur ce dossier, et il se joue à deux étages.

### Étage 1 — dans les familles retenues : 2 480 retirés

| Famille | Thérapeutique retiré | Exemples mesurés |
|---|---|---|
| F1 | **930** | `diffuseur huile essentielle danger` 390 · `diffuseur huiles essentielles danger` 260 · `diffuseur huile essentielle anti moustique` 210 |
| F2 | **1 070** | requêtes de bienfaits, d'usage sur animaux et de danger |
| F3 | **70** | — |
| F4 | **340** | — |
| F6 | **70** | — |
| **Total retiré du consolidé** | **2 480** | |

Motif du retrait, invariable : l'intention est informationnelle ou sanitaire, pas
transactionnelle déco ; et **les allégations de santé sont un motif de refus Merchant
Center documenté chez nous** (`PRODUCT-RESEARCH-CRITERIA.md` §6, vigilance renforcée sur
les allégations liées à la santé). Un consolidé qui garderait ce volume serait un faux
positif.

### Étage 2 — le vrai gisement thérapeutique est le parent, et il est exclu en totalité

Le parent `huile essentielle` pèse **347 300 sur ses 100 premières lignes**, et c'est un
**plancher** (100ᵉ ligne à 1 600). Sur ces 347 300, **75 500 au minimum sont explicitement
thérapeutiques ou cosmétiques** — soit **21,7 %** —, avec par exemple
`huile essentielle rhume` 4 400, `huile essentielle anti inflammatoire` 2 900,
`huiles essentielle pour le rhume` 2 900.

**Ces 75 500 sont un plancher de détection, pas un total** : il est mesuré par présence
d'un mot de santé explicite. Une requête comme « huile essentielle lavande » ne le
contient pas et relève pourtant, en pratique, du même univers d'aromathérapie.

**Décision : le parent `huile essentielle` est retiré intégralement du consolidé** —
ses 347 300 n'apparaissent nulle part au §3 ni au §6. La boutique peut vendre l'appareil
de diffusion ; elle ne peut pas aller chercher le vocabulaire de l'huile essentielle
sans entrer dans un registre d'allégation qu'elle ne pourra ni écrire ni faire passer en
flux Merchant Center. La SERP confirme (§5) : **`anses.fr` — l'Agence nationale de
sécurité sanitaire — occupe une position organique en page 1 de
`diffuseur huile essentielle`.**

### Autres retraits d'intention, pour mémoire

- **DIY / matière première : 12 020 retirés**, presque tout en F4 —
  `parfum pour bougie` 1 600, `parfums pour bougie` 1 600, `parfums pour bougies` 1 300,
  `bougie cire végétale` 720, `cire bougie vegetale` 720, `cire végétale bougie` 590,
  plus mèches, moules, paraffine, colorants. Ce sont des **fournitures pour fabriquer des
  bougies**, pas des bougies. C'est un autre univers (loisir créatif) et une autre
  boutique.
- **Hors-sujet : 2 270 retirés** — sèche-cheveux, bougie d'allumage, bougie
  d'anniversaire, bougie LED, crème brûlée, Miss Dior Blooming Bouquet, bouquets de
  fleurs.
- **Informationnel : 2 440 retirés** (comment, pourquoi, utilisation, entretien).
  Les requêtes `meilleur…` et `avis…` ont été **conservées** : ce sont des recherches
  commerciales, pas éditoriales.

---

## 5. Vérification SERP par tête de famille

google.fr, `hl=fr&gl=fr`, lecture du **28/08/2026**. Session connectée (écart déclaré au
§1). Les annonces Search texte n'ont **pas** pu être isolées : 1 à 2 mentions
« Sponsorisé / Annonce » par page, indistinguables d'un carrousel Shopping.

### F1 — `diffuseur huile essentielle` (14 800)

- **Ce que Google sert** : des diffuseurs, mais dans l'univers de l'**aromathérapie**,
  pas de la déco.
- **Intention** : oui, commerciale — mais l'écosystème est santé/bien-être.
- **Commercial vs informationnel** : majoritairement commercial, avec **une position
  institutionnelle sanitaire** : `anses.fr`.
- **Qui tient la page 1**
  - *Spécialistes / DTC* : `diffuseurs-dessentielles.com`, `compagnie-des-sens.fr`
  - *Marques d'aromathérapie* : `fr.puressentiel.com`, `pranarom.fr`, `messegue.fr`
  - *Marketplaces / enseignes / comparateurs* : `amazon.fr`, `natureetdecouvertes.com`,
    `gifi.fr`, `idealo.fr`, `ledenicheur.fr`, `cherchons.com`
  - *Institutionnel* : `anses.fr`
- **Bande de prix observée** : 23,17 € → 89,90 €, gros du peloton **28–50 €**.
- **Volume** : **retenu (80 380 net)**, avec la réserve conformité du §4. Motif :
  l'intention d'achat de l'appareil est réelle et commerciale.

### F2 — `parfum d'intérieur` (3 600) et `parfum d'ambiance` (2 900)

- **Ce que Google sert** : exactement le produit — diffuseurs à bâtonnets, sprays,
  parfums de maison.
- **Intention** : oui, pleinement commerciale, et **déco, pas santé**. C'est la famille
  la plus propre du dossier.
- **Commercial vs informationnel** : commercial, une seule position éditoriale
  (`marieclaire.fr` sur `parfum d'intérieur`).
- **Qui tient la page 1**
  - *Spécialistes / DTC* : `smellingood.com`, `atelierlouis.fr`, `cyor.fr`,
    `monparfumdinterieur.com`, `prestigedementon.com`, `parfum-ambiance.fr`,
    `espritprovence.shop`, `terredoc.com`, `jardindefrance.fr`, `parfumdegrasse.com`
  - *Marques installées* : Esteban, Maison Berger, Durance, Lothantique, L'Occitane,
    Mathilde M, Fragonard, Panier des Sens, My Jolie Candle
  - *Marketplaces / enseignes / comparateurs* : `idealo.fr`, `ledenicheur.fr`,
    `lionshome.fr`, `stylight.fr`, `cherchons.com`, `meilleurs.fr`, `action.com`,
    `printemps.com`, `nocibe.fr`
- **Rabattement orthographique** : aucune ligne « Résultats, y compris pour… » relevée.
  `parfum d'intérieur` et `parfum d'ambiance` sont **deux racines qui existent en
  propre**, servies par des pages 1 très proches.
- **Bande de prix observée** : 5,90 → 169,00 €, **cœur 13–23 €**.
- **Volume** : **retenu (45 240 net)**. Intention parfaite, prix problématique.

### F3 — `recharge diffuseur parfum` (880)

- **Ce que Google sert** : des recharges, exactement.
- **Intention** : oui. Réachat, panier récurrent.
- **Qui tient la page 1** : quasi **aucune marketplace généraliste** — que des
  comparateurs (`lionshome.fr`, `idealo.fr`, `cherchons.com`), des marques
  (Panier des Sens, Mathilde M, Durance, Maison Berger, Esteban) et des DTC
  (`plantesetparfums.com`, `terre-de-bougies.com`, `coeurdecigale.com`,
  `natureetbonsens.com`, `viadurini.fr`, `cyor.fr`). **Amazon absent de la page 1.**
- **Bande de prix observée** : 3,90 → 32,00 €, **cœur 5–12 €**.
- **Volume** : **retenu (4 390 net)**, mais la famille ne pèse presque rien seule. Sa
  valeur est un mécanisme de réachat, pas un volume d'acquisition.

### F4 — `bougie parfumée` (12 100)

- **Ce que Google sert** : des bougies parfumées, sans ambiguïté.
- **Intention** : oui, commerciale.
- **Qui tient la page 1**
  - *DTC / spécialistes* : `myjoliecandle.com`, `selmaya-bougies.fr`,
    `bougies-charroux.com`, `bougiesdumonde.fr`, `baija.com`, `matiere-premiere.com`
  - *Marques installées* : Yankee Candle, Maison Berger, Esteban
  - *Marketplaces / enseignes* : `carrefour.fr`, `fr.shopping.rakuten.com`, `idealo.fr`,
    `interflora.fr`, `europages.fr`, `facebook.com`
- **Bande de prix observée** : 2,99 → 290,00 €, **cœur 10–25 €**. Bande très étalée,
  avec un socle massif sous 25 € et quelques pièces à 115 et 290 € sans palier
  intermédiaire visible — **profil bimodal**, piège de l'étape 9.
- **Volume** : **retenu (63 690 net)** pour la mesure, mais **la famille est la plus
  exposée du dossier** : marques historiques installées d'un côté, Carrefour et le
  premier prix de l'autre.

### F5 — `coffret bougie` (2 400)

- **Ce que Google sert** : des coffrets cadeaux de bougies.
- **Intention** : oui, et fortement **offrable** — utile pour Q4.
- **Qui tient la page 1** : très majoritairement des **petits DTC français** —
  `lescreationsdalizea.com`, `essence-c.fr`, `serenity-bougie.fr`, `atelierbougies.com`,
  `saugette.com`, `majoliebougie.com`, `jardindeco.com`, `bougiesdumonde.fr` —
  plus My Jolie Candle, Durance, Yankee, `adopt.com`, `fnac.com`, et les comparateurs.
  **Aucune marketplace dominante.**
- **Bande de prix observée** : 1,50 → 82,00 €, **cœur 13–30 €**.
- **Volume** : **retenu (7 370 net)**.

### F6 — `désodorisant voiture` (2 400) / `parfum voiture` (2 900)

- **Ce que Google sert** : des désodorisants auto de grande distribution.
- **Intention** : oui, mais ce n'est pas le même client ni le même rayon.
- **Qui tient la page 1** : `amazon.fr`, **`norauto.fr`, `feuvert.fr`,
  `eboutique.totalenergies.fr`**, `maniac-auto.com`, `mongrossisteauto.com`,
  `shop.berner.eu`, `theoauto.fr`, plus Yankee Candle, Maison Berger et Esteban en
  débordement. Réseaux d'enseignes auto = configuration §4 (« équivalents généralistes »).
- **Bande de prix observée** : 1,58 → 29,99 €, **cœur 3–7 €**.
- **Volume** : **retiré du consolidé retenu.** Motif : bande de prix incompatible avec le
  périmètre 50–400 € (§1), page 1 tenue par des enseignes auto nationales, et test « une
  page ou deux » tranché en défaveur — c'est un rayon automobile, pas une collection de
  déco olfactive. Retrait de **36 950 net**.

---

## 6. Volume consolidé retenu

| Périmètre | Brut | **Net de marque et d'exclusions** | Hypothèse prudente |
|---|---|---|---|
| **Cœur maison retenu, F1 + F2 + F3 + F4 + F5** | 249 650 | **201 070** | **129 200** |
| F6 voiture — **retiré après SERP** | 45 040 | *36 950 non retenus* | *15 910 non retenus* |
| Parents `diffuseur` / `bougie` / `huile essentielle` — **jamais additionnés** | *954 290 lus* | *0 retenu* | *0 retenu* |

**Consolidé net retenu : 201 070 recherches/mois** (hypothèse prudente : 129 200).

**Confrontation au seuil.** Le seuil UNIVERS de `PRODUCT-RESEARCH-CRITERIA.md` §1 est de
**30 000/mois consolidé par familles, confort 40 000**. Le consolidé net retenu est de
**201 070**, soit **6,7 fois le seuil** ; l'hypothèse la plus prudente donne **129 200**,
soit **4,3 fois le seuil**. La plus petite famille prise seule (F5 coffrets, 7 370) est
sous le seuil, mais **c'est le consolidé qui fait foi en mode UNIVERS**, et quatre
familles sur cinq dépassent chacune 4 000, dont trois dépassent 45 000.

**La porte de volume est franchie très largement, et sans discussion possible.** Nous ne
sommes pas dans la zone de cas limite (24 000–36 000) : aucune décision de volume n'est
à remonter à Hakim.

**Ce qui reste debout, c'est la sourçabilité par famille** (§0.6 des critères : les 3–5
familles pesant ≥ 70 % du consolidé doivent avoir chacune ≥ 2 fournisseurs plausibles).
F1 + F4 + F2 pèsent ensemble **189 310 sur 201 070, soit 94 %** : ce sont ces trois-là que
la phase 4 devra sourcer. Ce n'est pas mon périmètre et je ne l'ai pas instruit.

---

## 7. Bande de prix observée

Relevés en page 1 Google France, **28/08/2026**, en SERP et blocs Shopping, jamais en
estimation.

| Tête | Minimum | Maximum | **Cœur de bande** | Au-dessus du plancher 50 € ? |
|---|---|---|---|---|
| `diffuseur huile essentielle` | 23,17 € | 89,90 € | **28–50 €** | **Partiellement** |
| `diffuseur parfum maison` | 19,99 € | 79,00 € | **25–50 €** | **Partiellement** |
| `coffret bougie` | 1,50 € | 82,00 € | 13–30 € | Non |
| `parfum d'intérieur` | 5,90 € | 169,00 € | 13–23 € | Non |
| `bougie parfumée` | 2,99 € | 290,00 € | 10–25 € | Non |
| `parfum d'ambiance` | 3,90 € | 54,00 € | 12,95–18,95 € | Non |
| `recharge diffuseur parfum` | 3,90 € | 32,00 € | 5–12 € | Non |
| `désodorisant voiture` | 1,58 € | 29,99 € | 3–7 € | Non |

**Contradiction avec la sonde du 22/08, déclarée.** La shortlist 30×30 donne une
**médiane cœur de 64,99 €** sur `diffuseur huile essentielle`. Ma lecture SERP du 28/08
sur la même requête donne un gros du peloton à **28–50 €** et une médiane des trente
prix relevés autour de **44 €**. Les deux lectures ne coïncident pas. Je ne tranche pas
laquelle est la bonne : la sonde du 22/08 lisait Google Shopping, la mienne lit la page
de résultats. Les deux chiffres sont au dossier.

**Ce que la bande dit du panier.** Une seule famille sur cinq — F1, le diffuseur
électrique — a un cœur qui approche le plancher 50 € de `PRODUCT-RESEARCH-CRITERIA.md`
§1, et elle ne le franchit qu'en haut de bande. Les quatre autres ont un cœur entre 5 et
30 €. Cela n'interdit rien en mode UNIVERS — le low ticket est autorisé —, mais cela
**déclenche l'extension obligatoire `catalogue-volume`** du §7 des critères : échantillon
de 30–50 prix sur les catégories cœur, médiane, part sous 10/15 €, et **mécanisme de
panier observé**. Sur ce dossier le mécanisme est plausible et même partiellement visible
(coffrets, recharges, réachat), mais il n'est **pas mesuré** — ce travail n'a pas été
fait ici et doit l'être avant toute décision.

---

## 8. Google Trends — lecture qualitative

`bougie parfumée` / `parfum d'intérieur` / `diffuseur huile essentielle`, France, cinq
dernières années, lu le 28/08/2026. **Lecture qualitative uniquement — aucune variation
chiffrée n'est avancée, l'outil n'en affiche pas dans la vue lue.**

- **Socle** : les trois termes sont présents toute l'année, sans mois mort. L'exigence
  UNIVERS d'un socle ≥ 8 mois est **satisfaite**.
- **`diffuseur huile essentielle`** porte le socle le plus haut des trois toute l'année,
  mais ses pics annuels successifs sont **visiblement décroissants d'une année sur
  l'autre** sur les cinq ans. Signal d'**érosion de fond** — et c'est précisément la
  famille la plus lourde du consolidé (F1, 80 380).
- **`bougie parfumée`** a un socle bas et un **pic de décembre très marqué**, d'amplitude
  stable année après année. Saisonnalité Q4 franche, cohérente avec un usage cadeau.
- **`parfum d'intérieur`** a un socle bas et plat, avec un léger relèvement de fin
  d'année.

Conclusion : l'univers n'est pas 100 % saisonnier, mais il est **structurellement adossé
au Q4** sur sa famille bougie, et sa famille la plus volumineuse est sur une pente
descendante. À porter au dossier de Hakim.

---

## 9. Concurrents observés — spécialistes/DTC vs marketplaces et enseignes

| Famille | Spécialistes / DTC en page 1 | Marketplaces, enseignes et comparateurs |
|---|---|---|
| F1 | `diffuseurs-dessentielles.com`, `compagnie-des-sens.fr` (+ marques Puressentiel, Pranarôm, Messegué) | Amazon, Nature & Découvertes, Gifi, Idealo, LeDenicheur, Cherchons · **+ `anses.fr`** |
| F2 | `smellingood.com`, `atelierlouis.fr`, `cyor.fr`, `monparfumdinterieur.com`, `prestigedementon.com`, `parfum-ambiance.fr`, `espritprovence.shop`, `terredoc.com`, `parfumdegrasse.com`, `jardindefrance.fr` (+ marques Esteban, Berger, Durance, Lothantique, L'Occitane, Mathilde M, Fragonard, Panier des Sens) | Idealo, LeDenicheur, LionsHome, Stylight, Cherchons, Meilleurs, Action, Printemps, Nocibé |
| F3 | `plantesetparfums.com`, `terre-de-bougies.com`, `coeurdecigale.com`, `natureetbonsens.com`, `viadurini.fr`, `cyor.fr` | LionsHome, Idealo, Cherchons · **Amazon absent** |
| F4 | `myjoliecandle.com`, `selmaya-bougies.fr`, `bougies-charroux.com`, `bougiesdumonde.fr`, `baija.com`, `matiere-premiere.com` (+ Yankee Candle, Maison Berger, Esteban) | Carrefour, Rakuten, Idealo, Interflora, Europages, Facebook |
| F5 | `lescreationsdalizea.com`, `essence-c.fr`, `serenity-bougie.fr`, `atelierbougies.com`, `saugette.com`, `majoliebougie.com`, `jardindeco.com` | Fnac, Adopt, Idealo, LeDenicheur, LionsHome |
| F6 *(retirée)* | `maniac-auto.com`, `mongrossisteauto.com`, `theoauto.fr` | Amazon, **Norauto, Feu Vert, TotalEnergies**, Berner |

**Lecture, contrôle n° 6 du catalogue (le KD mesure la densité, pas un verrou).** Les KD
relevés vont de 9 à 47. Le plus élevé, `diffuseur huile essentielle` à KD 47, correspond
à une page 1 où Amazon n'occupe qu'**une** position organique et où l'essentiel est tenu
par des marques d'aromathérapie et deux spécialistes. Ce KD mesure une **densité de
spécialistes**, c'est-à-dire une concurrence de même nature que nous — porte difficile,
pas fermée. Inversement F5 (`coffret bougie`, KD 16) est **la page 1 la plus ouverte du
dossier** : une majorité de très petits DTC français, aucune marketplace dominante.

Sur F2, F3 et F5, la configuration est **favorable au sens de §4** : des indépendants
majoritaires, pas de GSB généraliste installée. Sur F4 la présence de Carrefour et d'un
premier prix à 2,99 € est un signal opposé. Sur F6 la configuration est **rédhibitoire**.

Aucune cartographie de concurrent n'a été produite : c'est l'étape 7 de
`METHODE-ANALYSE-MARCHE.md` (agent `cartographie-concurrence`) et elle n'était pas dans
le mandat.

---

## 10. Réserves — aucune n'est retirée

1. **SERP lues en session Google connectée**, contrairement au mandat. Personnalisation
   des résultats non exclue.
2. **Les annonces Search texte n'ont pas pu être isolées** des blocs Shopping
   sponsorisés. Aucune conclusion sur la pression publicitaire Search n'est tirée, et
   aucune ne doit l'être à partir de ce rapport.
3. **Cinq graines sont des planchers de lecture, pas des totaux** :
   `diffuseur huile essentielle` (100ᵉ ligne à 210), `bougie parfumée` (140), et les trois
   parents. Le consolidé réel est **supérieur** à 201 070, pas inférieur — la réserve joue
   dans le sens favorable, ce qui ne la rend pas moins nécessaire.
4. **Le consolidé additionne des variantes que SEMrush restitue à volume identique.**
   L'hypothèse prudente (129 200) est publiée à côté du chiffre principal (201 070). La
   méthode Noirmont autorise l'addition ; le doute est écrit.
5. **Contradiction de prix non tranchée** entre la sonde du 22/08 (médiane 64,99 € sur
   `diffuseur huile essentielle`) et ma lecture SERP du 28/08 (cœur 28–50 €). Les deux
   sont au dossier.
6. **Le mécanisme de panier n'est pas mesuré.** L'extension `catalogue-volume` du §7 des
   critères (30–50 prix, médiane, part sous 10/15 €, mécanisme de panier observé) reste
   entièrement à faire. Sans elle, aucune économie de boutique n'est démontrée.
7. **Le volume thérapeutique retiré est un plancher de détection** : 75 500 sur le parent
   `huile essentielle` est mesuré par présence d'un mot de santé explicite. La
   contamination réelle du vocabulaire de l'huile essentielle est vraisemblablement
   supérieure, et la présence de `anses.fr` en page 1 le confirme qualitativement.
8. **`bouquet parfumé` reste un mot ambigu partiellement instruit** : sa grappe mélange
   du parfum de peau Dior, des bouquets de fleurs et du diffuseur à bâtonnets. Le tri a
   été fait par liste de marques et de mots hors-sujet, pas par lecture de SERP dédiée.
9. **Aucune cartographie de concurrent** (étape 7), **aucun sourcing** (phase 4), **aucun
   contrôle de sourçabilité par famille** (§0.6 des critères). Le pass ci-dessous
   n'autorise que la due diligence.
10. **`diffuseur huile essentielle` est en érosion pluriannuelle** sur Google Trends,
    et c'est la famille la plus lourde du consolidé. Lecture qualitative seulement.
11. **Rabattement orthographique non vérifié sur toutes les têtes.** Le contrôle « Résultats,
    y compris pour X » n'a été relevé sur aucune des sept SERP lues, mais il n'a pas été
    cherché systématiquement sur les paires accentuées/non accentuées.

---

## 11. Statut de préqualification

### `REVIEW_PREQUALIFICATION`

**Ce n'est pas un cas limite de volume.** Le seuil UNIVERS applicable est de
**30 000/mois consolidé par familles** (`PRODUCT-RESEARCH-CRITERIA.md` §1, confort
40 000). Le consolidé net retenu est de **201 070**, l'hypothèse la plus prudente de
**129 200**. Nous sommes à **4,3 à 6,7 fois le seuil**, très loin de la bande de cas
limite 24 000–36 000. Il n'y a aucune décision de volume à remonter, et appliquer ici le
seuil PRODUIT PUR de 10 000 par cluster aurait été une faute de méthode.

**Le verdict est `REVIEW` et non `PASS` parce que trois obstacles majeurs sont
identifiés, mesurés, et non levables à mon niveau :**

1. **Économie de panier.** Quatre familles sur cinq ont un cœur de bande SERP entre 5 et
   30 €, sous le plancher 50 € de §1. Seul le diffuseur électrique approche la tranche.
   Le low ticket est autorisé en UNIVERS, mais il **déclenche l'extension obligatoire
   `catalogue-volume`**, qui n'a pas été instruite. Une boutique dont le cœur est à 18 €
   n'a pas la même économie qu'une boutique à 65 €, et c'est cette question-là qui décide,
   pas le volume.
2. **Conformité et allégations.** La famille la plus lourde (F1, 80 380 net) est adossée
   au vocabulaire de l'huile essentielle. Son parent porte **≥ 75 500 de volume
   explicitement thérapeutique**, entièrement exclu, et sa page 1 comporte une position
   organique de l'**ANSES**. C'est un risque Merchant Center connu de la maison (§6 des
   critères, vigilance renforcée sur les allégations santé) et il doit être arbitré avant
   d'engager du sourcing.
3. **Densité de marques installées sur la famille bougie.** F4 (63 690 net) est encadrée
   par Yankee Candle, Maison Berger, Diptyque et Charroux d'un côté, et par Carrefour et
   un premier prix à 2,99 € de l'autre. En mode UNIVERS un spécialiste en place est une
   preuve, pas un STOP ; mais un socle de premier prix en grande distribution sur la même
   requête est une configuration §4.

**Ce qui, à l'inverse, plaide fortement pour ce dossier** et doit être lu avec le reste :
F2, F3 et F5 ont des pages 1 tenues par des indépendants, avec **Amazon absent de la page
1 des recharges** — configuration rare ; les CPC sont bas (0,18 à 0,76 € en base France) ;
l'univers a un mécanisme de réachat naturel et une famille cadeau pour le Q4 ; et la
preuve boutique du 22/08 (`ambiance-parfum.com`, 1 754 jours d'ancienneté) montre un
modèle qui tient dans la durée.

**Ce que ce statut autorise et n'autorise pas.** Il autorise la due diligence : sourcing
par famille sur F1, F4 et F2 (94 % du consolidé), extension `catalogue-volume`, et
cartographie des concurrents. **Il ne constitue aucun `GO_FINAL`** — lequel appartient à
Hakim, et reste de toute façon interdit sur un dossier UNIVERS tant que la sourçabilité
par famille n'est pas documentée (`PRODUCT-RESEARCH-CRITERIA.md` §0.6).

### Décisions qui appartiennent à Hakim

1. **Arbitrer le risque prix.** Le cœur de marché est sous le plancher 50 €. Lance-t-on
   l'extension `catalogue-volume` sur ce dossier, ou le plancher prix est-il bloquant ?
2. **Arbitrer le risque conformité F1.** Va-t-on chercher le diffuseur d'huiles
   essentielles en sachant que son écosystème est l'aromathérapie et que l'ANSES est en
   page 1 ?
3. **Trancher la contradiction de prix** entre la sonde Shopping du 22/08 (64,99 €) et la
   lecture SERP du 28/08 (28–50 €).
4. **Confirmer le retrait de F6 (voiture)**, qui coûte 36 950 net au consolidé et que
   j'ai retirée sur la foi de sa SERP (Norauto, Feu Vert, TotalEnergies, cœur 3–7 €).
