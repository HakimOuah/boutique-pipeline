# Rejeu du dossier « Rideaux — matière × intention » avec DataForSEO seul

**Date : 2026-08-29.** Test de non-régression avant décision sur l'abonnement SEMrush (149 €/mois).

Question posée : *un dossier déjà instruit à la SEMrush aboutit-il au même verdict quand on le refait avec DataForSEO seul ?*

Référence rejouée : `analyses/2026-08-28-mission-b-univers/rideaux-matiere-intention.md` (28/08/2026).

---

## 1. Méthode et coût

### 1.1 Ordre de travail — attestation

Les sections 2 à 5 ont été mesurées **et rédigées** avant toute ouverture du rapport de référence.
Ce fichier n'a été lu qu'au moment d'écrire la section 6. Aucune valeur SEMrush n'a orienté les
mesures, les exclusions ni la consolidation.

**Réserve sur l'aveuglement — le test n'est pas parfaitement aveugle, et c'est dit.**
Le document `analyses/2026-08-29-croisement-semrush-dataforseo.md`, cité dans le brief comme
source de la recette `google_ads/search_volume/live`, contient lui-même un tableau où figurent
une vingtaine de têtes « rideaux » **avec leur volume SEMrush du 28/08**. En allant y chercher
les paramètres d'appel, ces lignes ont été vues. La contamination porte sur ~20 volumes de tête ;
elle ne porte pas sur les grappes, ni sur les exclusions, ni sur la consolidation —
c'est-à-dire pas sur ce qui fabrique le verdict. Elle est signalée plutôt que dissimulée.

### 1.2 Outil

- **Découverte** : `scripts/kw_dfs.py`, endpoint `dataforseo_labs/google/keyword_suggestions/live`,
  `location_name: France`, `language_name: French`, tri par volume décroissant, 1 000 lignes/page.
- **Volumes de tête et saisonnalité** : `keywords_data/google_ads/search_volume/live`,
  `search_partners: false`.

### 1.3 Graines interrogées — 14 graines, 8 familles

| Famille | Graine(s) | Pages | Lignes rendues | Annoncées par l'API |
|---|---|---:|---:|---:|
| Occultation | `rideau occultant` | 2 | 2 000 | 3 043 |
| Thermique | `rideau thermique` | 2 | 1 609 | 1 609 |
| Thermique | `rideau isolant` | 1 | 619 | 619 |
| Thermique | `rideau anti froid` | 1 | 97 | 97 |
| Phonique | `rideau phonique` | 1 | 324 | 324 |
| Phonique | `rideau anti bruit` | 1 | 146 | 146 |
| Phonique | `rideau acoustique` | 1 | 98 | 98 |
| Velours | `rideau velours` | 1 | 496 | 496 |
| Lin | `rideau lin` | 2 | 1 201 | 1 201 |
| Voilage | `voilage` | 2 | 2 000 | 8 130 |
| Doubles rideaux | `double rideau` | 1 | 814 | 814 |
| Accessoires | `tringle rideau` | 2 | 2 000 | 4 738 |
| Accessoires | `embrasse rideau` | 1 | 384 | 384 |
| Accessoires | `anneau rideau` | 1 | 169 | 169 |

Les quatre graines Phonique/Thermique complémentaires ont été ajoutées **après** la première
passe, en découvrant que la référence avait utilisé trois graines là où j'en avais utilisé une :
c'est une correction de couverture méthodologique, pas un ajustement vers un chiffre attendu.
Le total est passé de 600 390 à 614 130 ; le verdict n'a pas bougé.

Trois graines restent tronquées après deux pages (`rideau occultant` 2 000 / 3 043,
`voilage` 2 000 / 8 130, `tringle rideau` 2 000 / 4 738). Le tri étant par volume décroissant,
la traîne non lue est **sous le volume de la 2 000ᵉ ligne** : sur `voilage`, cette ligne vaut
10 recherches/mois. L'amputation est négligeable et rend la mesure **conservatrice**.

### 1.4 Coût

| Poste | USD |
|---|---:|
| Découverte, 10 graines en page 1 | 0,983 |
| Découverte, 5 graines re-tirées en 2 pages | 1,177 |
| Découverte, 4 graines complémentaires | ≈ 0,182 |
| `google_ads/search_volume/live`, 2 appels (26 têtes) | 0,180 |
| **Total** | **≈ 2,52 USD** |

À comparer aux 149 €/mois de SEMrush. Le cache disque du script rend tout rejeu ultérieur gratuit.

### 1.5 Limites de calcul assumées

1. **Jamais de somme de volumes bruts.** Google pré-agrège les variantes proches. Le script
   regroupe par clé normalisée (accents, pluriels, mots vides, ordre) et retient le **MAX** du
   groupe. Seuls ces maxima sont sommés — un volume par idée distincte.
   *Ordre de grandeur de l'enjeu* : la somme naïve des 7 660 groupes rendus par les 14 graines
   vaut **923 450**. Après déduplication inter-graines et recollage, il reste **789 970**.
   **133 480 recherches/mois, soit 14 %, étaient du même bucket compté plusieurs fois.**
2. **Un défaut de `kw_dfs.py` corrigé à la main.** La dépluralisation `-aux → -al` du script
   (écrite pour *journal/journaux*) casse `rideaux` en `rideal`, séparant `rideau X` de
   `rideaux X` alors que Google les sert dans le **même bucket**. Un recollage `rideal → rideau`
   a été appliqué. **Sans ce correctif, le total était surévalué de 54 610 recherches/mois.**
   Ce défaut doit être corrigé dans le script — voir §8.
3. **Preuve de fusion retenue : la série mensuelle, pas le volume ponctuel.** `rideau occultant`
   et `rideaux occultants` ont non seulement le même volume (49 500) mais **la même série sur
   12 mois** — même bucket. `tringle rideau` et `tringle à rideau` valent tous deux 22 200 mais
   ont des **séries différentes** — buckets distincts, conservés tous les deux. Idem pour
   `rideau occultant` et `rideau thermique`, tous deux à 49 500 mais de saisonnalités opposées.
   **L'égalité de volume ne prouve rien ; l'égalité de série prouve.** C'est un critère nouveau,
   utilisable sur tous les dossiers à venir.
4. **Le tronc générique n'est pas compté.** L'endpoint fait une correspondance plein texte sur la
   graine : toute suggestion contient les mots de sa graine. Les requêtes génériques pures
   (`rideau` 40 500, `rideaux` 22 200) ne sont jamais remontées et **ne figurent pas dans le
   consolidé**. Second facteur conservateur : 62 700 de tête laissés de côté.
5. **Une idée n'est comptée qu'une fois.** L'affectation suit un ordre de priorité documenté
   (Accessoires → Phonique → Velours → Lin → Voilage → Doubles rideaux → Thermique → Occultation) :
   la première famille qui matche prend l'idée. `rideau occultant thermique` (22 200) est compté
   une seule fois, en Thermique. **Le total consolidé est invariant à cet ordre** ; seule la
   répartition entre familles en dépend.
6. **Aucune SERP n'a été rejouée.** Ce rejeu porte sur la mesure de demande, pas sur l'audit SERP.
   Les lectures SERP, prix et concurrents du 28/08 tiennent et ne sont pas contestées ici.

### 1.6 Seuil appliqué

Seuil canonique UNIVERS (`PRODUCT-RESEARCH-CRITERIA.md` §1) : **30 000** consolidé, confort 40 000.
DataForSEO rend en médiane **×1,25** ce que rendait SEMrush (deux échantillons indépendants :
181 mots-clés, puis 15 têtes). Le seuil est donc recalibré pour cette mesure à
**37 500 (confort 50 000)**. C'est contre 37 500 que le verdict est prononcé.

---

## 2. Mesure par famille

Recherches/mois, France, lecture du 2026-08-29.

| Famille | Volume brut | Net de marque | Net final (toutes exclusions) | Idées distinctes | Formulations brutes | Reformulations supprimées |
|---|---:|---:|---:|---:|---:|---:|
| Accessoires (tringle, embrasse, anneau) | 229 730 | 191 290 | **183 020** | 1 237 | 3 105 | 46 % |
| Voilage | 178 780 | 152 000 | **126 650** | 739 | 1 522 | 36 % |
| Thermique | 157 200 | 130 150 | **126 520** | 944 | 1 701 | 26 % |
| Occultation | 123 580 | 99 930 | **92 880** | 774 | 1 451 | 30 % |
| Lin | 41 140 | 35 130 | **33 580** | 620 | 1 225 | 37 % |
| Phonique | 23 510 | 21 120 | **20 840** | 276 | 578 | 34 % |
| Doubles rideaux | 20 830 | 18 170 | **17 280** | 333 | 508 | 19 % |
| Velours | 15 200 | 13 480 | **13 360** | 231 | 464 | 34 % |
| **TOTAL 8 familles** | **789 970** | **661 270** | **614 130** | 5 154 | 10 554 | — |

Taux de reformulations supprimées : de 19 % (Doubles rideaux) à 46 % (Accessoires). Sur les
accessoires, près d'une ligne sur deux rendue par l'API était une reformulation du même bucket.

### Volumes de tête — confirmés par un second endpoint

Les deux endpoints (`Labs/keyword_suggestions` et `google_ads/search_volume`) concordent
**exactement** sur les 20 têtes testées. Aucune divergence interne à l'outil.

| Tête | Volume | CPC (USD) | Concurrence | Saisonnalité mesurée (12 mois glissants) |
|---|---:|---:|---|---|
| `rideau occultant` | 49 500 | 0,72 | HIGH | plateau large : 33 100 (déc.) à 60 500 (août/juil.), **amplitude ×1,8** |
| `rideau thermique` | 49 500 | 0,47 | HIGH | **très saisonnier** : 18 100 (mars-avr.) → **135 000 (nov. 2025)**, **amplitude ×7,5** |
| `rideau voilage` | 27 100 | 0,51 | HIGH | plat, 18 100 à 33 100 |
| `tringle rideau` | 22 200 | 0,42 | HIGH | plat, 18 100 à 27 100 |
| `rideau occultant thermique` | 22 200 | 0,65 | HIGH | saisonnier : 9 900 → 60 500 |
| `tringle rideau sans percer` | 18 100 | 0,16 | HIGH | plat, 14 800 à 22 200 |
| `voilage` | 8 100 | 0,56 | HIGH | plat, 6 600 à 9 900 |
| `embrasse rideau` | 6 600 | 0,31 | HIGH | plat, 4 400 à 8 100 |
| `doubles rideaux` | 5 400 | 0,42 | HIGH | plat, 2 900 à 6 600 |
| `rideau phonique` | 4 400 | **1,81** | HIGH | plat, 2 400 à 5 400 |
| `rideau lin` | 4 400 | 0,69 | HIGH | plat, 3 600 à 5 400 |
| `rideau velours` | 2 900 | 0,73 | HIGH | **saisonnier automne** : 1 300 (juil.) → 6 600 (nov.), **amplitude ×5,1** |
| `anneau rideau` | 2 900 | 0,25 | HIGH | plat, 2 400 à 3 600 |
| `double rideau` | 1 300 | 0,35 | HIGH | plat, 880 à 1 900 |

**La saisonnalité n'est pas celle de l'univers, elle est celle des familles.** Thermique et
Velours sont des marchés d'automne-hiver ; Occultation, Voilage et Accessoires sont plats à
l'année. L'univers s'auto-lisse : les familles ne pointent pas au même moment. CPC bas partout
(0,16 à 0,81) sauf le Phonique (1,81), intention à forte valeur mais marché étroit.

---

## 3. Thèmes co-occurrents par famille

C'est la table que sort le script ; c'est elle qui a révélé les contaminations.

**`rideau occultant`** — `thermique` (182 idées, 31 570) · `leroy`/`merlin` (40, 5 980) ·
`ikea` (32, 6 130) · `gifi` (30, 3 630) · `velu` [Velux] (28, 3 060) · `lin` (25, 2 320) ·
`phonique` (20, 1 030) · `castorama` (19, 1 030), puis couleurs (blanc, gris, bleu, beige, vert,
rose, noir) et dimensions (hauteur, largeur).

**`rideau thermique`** — `occultant` (222, 31 650) · `isolant` (195, 9 820) · `anti`+`froid`
(59/58, ~11 750) · `porte` (51, 4 580) · `phonique` (50, 2 860) · `chaleur` (23, 4 980) ·
`entree` (24, 3 070) · `polaire` (24, 1 890) · `doublure` (27, 1 670) · marques (leroy/merlin 40,
castorama 23, gifi 21, amazon 15) · **`moondream` (14, 360)**, bruit d'API sans rapport avec le
sujet — la référence du 28/08 avait relevé le même parasite.

**`voilage`** — `rideau`/`rideal` (211+172 : la même idée au singulier et au pluriel, c'est là
que le défaut de normalisation se voyait) · `blanc` (102, 19 250) · `fenetre` (62, 14 010) ·
`lin` (41, 6 900) · `tringle` (36, 3 540) · `fronceur`/`galon` (16+16, ~3 110) · `mesure`
(16, 2 800) · `metre` (16, 1 780) · et surtout **`ombrage`, `hivernage`, `jardin`, `terrasse`** —
le voile d'ombrage et le voile d'hivernage, qui ne sont pas des rideaux.

**`tringle rideau`** — `san`+`percer` (153/106, ~44 540 : le « sans percer » est le premier sujet
du marché) · `support` (133, 21 850) · `percage` (39, 12 070) · `extensible` (65, 11 600) ·
`plafond` (48, 11 260) · `double` (42, 10 060) · `boi` [bois] (43, 6 310) · `volet`+`roulant`
(39/34) · **`douche` (24, 3 040)** · marques (leroy/merlin 55, ikea 39, castorama 36, gifi 25).

**`rideau lin`** — `blanc` (99) · `lave` (67, 1 600 : le « lin lavé » est un segment en soi) ·
`occultant` (56, 2 350) · `beige` (53, 4 190) · `naturel` (23, 3 550) · `effet` (33, 920 :
« effet lin », donc du faux lin).

**`rideau velours`** — `vert` (33) · `bleu` (31) · `cotele` (19, 2 040 : le velours côtelé est le
sous-segment moteur) · `occultant` (21) · `thermique` (15) · `rouge` (8, 830).

**`rideau phonique`** — `thermique` (50, 2 860) · `isolant` (41, 2 250) · `occultant` (26) ·
`porte`+`entree` (18/11, ~2 800) · `isolation` (11, 1 860) · `couche` (11, 290).

**`double rideau`** — `tringle` (96, 10 380 : la famille est massivement tirée par son
accessoire) · `occultant` (44, 2 560) · `support` (24) · `thermique` (15, 2 160) · `plafond` (18).

**`embrasse rideau`** — `aimantee` (19, 910 : l'embrasse aimantée est le produit dominant) ·
`crochet` (13) · `corde` (8) · `pompon` (5) · et **`comment`/`faire`/`tuto` (9/7/6, ~950)** :
intention DIY, exclue.

**`anneau rideau`** — **`douche` (19, 1 190)** : contamination principale de la graine, un anneau
sur deux est un anneau de douche · `pince` (10, 730) · `boi` (9, 410).

---

## 4. Volumes retirés

Total retiré : **175 840 recherches/mois**, soit 22,3 % du brut consolidé.

| Motif de retrait | Idées | Volume retiré | Exemples chiffrés |
|---|---:|---:|---|
| **Marques et enseignes** | 1 197 | **128 700** | `leroy merlin tringle rideau` 5 400 · `leroy merlin rideau occultant` 4 400 · `ikea rideau occultant` 4 400 · `leroy merlin rideau thermique` 4 400 · `ikea rideau tringle` 4 400 · `ikea rideau thermique` 2 900 · `gifi rideau occultant` 2 400 · `action rideau thermique` 2 400 · `action rideau occultant` 1 600 · `action tringle rideau sans percer` 1 600 |
| **Hors sujet / non-rideau** | 153 | **25 660** | `voilage ombrage` 8 100 · `voilage hivernage` 4 400 · `voilage hivernal` 4 400 · `voilage mariage plafond` 390 · `voilage jardin` 390 · `voilage terrasse` 390 · `rideau occultant camping car` 320 |
| **Sur-mesure et confection** | 128 | **7 180** | `voilage sur mesure` 1 300 · `rideau occultant sur mesure` 720 · `rideau sur mesure thermique` 590 · `rideau voilage sur mesure` 320 · `coudre rideau passe tringle` 210 |
| **Rideau de douche** | 57 | **5 660** | `rideau douche tringle` 1 300 · `anneau rideau douche` 880 · `rideau douche lin` 720 · `tringle rideau douche angle sans percer` 390 · `tringle rideau baignoire` 260 |
| **Tissu au mètre** | 61 | **4 740** | `rideau tissu occultant` 720 · `voilage metre` 590 · `tissu voilage` 590 · `rideau thermique tissu` 480 · `mondial tissu voilage` 390 |
| **Velux / fenêtre de toit** | 39 | **3 900** | `rideau occultant velux` 2 400 · `rideau thermique velux` 260 · `rideau occultant fenetre toit` 210 · `tringle rideau velux` 140 · `voilage velux` 110 |
| **TOTAL EXCLU** | 1 635 | **175 840** | |

Répartition du retrait de marque par famille : Accessoires 38 440 · Thermique 27 050 ·
Voilage 26 780 · Occultation 23 650 · Lin 6 010 · Doubles rideaux 2 660 · Phonique 2 390 ·
Velours 1 720.

Deux marqueurs d'exclusion ont été **relâchés** après contrôle, pour ne pas sur-exclure :
`mètre` sur une tringle est une longueur de produit (`tringle rideau 3 mètres` 260), pas du tissu
au mètre ; `toile` désigne un motif (toile de Jouy, toile de jute), pas un coupon.

**Ce qui n'a délibérément PAS été retiré** : couleurs et dimensions. `rideau beige occultant`
(2 900), `rideau blanc lin` (1 600) sont des requêtes d'achat servables par une fiche à variantes.
Les retirer serait de la sous-estimation, pas de la rigueur.

---

## 5. Consolidé net et verdict

| | Recherches/mois |
|---|---:|
| Somme naïve des groupes par graine | 923 450 |
| − doublons inter-graines et recollage rideau/rideaux | − 133 480 (−14 %) |
| **Brut consolidé, une idée = un volume** | **789 970** |
| − exclusions (marques, hors sujet, sur-mesure, douche, tissu, Velux) | − 175 840 (−22 %) |
| **Consolidé net, 8 familles** | **614 130** |
| Seuil UNIVERS recalibré DataForSEO | 37 500 |
| Seuil de confort recalibré | 50 000 |
| **Marge sur le seuil** | **×16,4** |

Ce n'est pas un cas limite. Même la plus petite famille prise seule (Velours, 13 360) n'est qu'à
un facteur 2,8 sous le seuil ; les quatre plus grosses le franchissent chacune isolément. Même
avec une décote de sécurité de 50 % sur l'ensemble, on reste à 307 000.

Trois facteurs rendent la mesure **conservatrice** : le tronc générique (`rideau` 40 500,
`rideaux` 22 200) n'est pas compté ; trois graines restent tronquées ; les recoupements entre
familles sont comptés une seule fois.

### Verdict

# `PASS_PREQUALIFICATION`

Demande très largement au-dessus du seuil recalibré, intention commerciale confirmée (concurrence
publicitaire HIGH sur les 20 têtes, CPC de 0,16 à 0,81 USD), familles à saisonnalités décalées qui
se compensent, univers qu'une boutique spécialisée peut servir sans dépendre d'une seule tête.

Ce verdict autorise la due diligence sourcing et concurrence. **Il ne vaut pas décision
commerciale finale.** Pour un dossier UNIVERS, `PRODUCT-RESEARCH-CRITERIA.md` §0-6 interdit tout
`GO_FINAL` tant que la sourçabilité par famille n'est pas documentée : les familles pesant ≥ 70 %
du consolidé — **Accessoires, Voilage, Thermique, Occultation, soit 86 %** — doivent avoir chacune
≥ 2 fournisseurs plausibles.

---

## 6. Comparaison des deux chaînes

*Rapport de référence ouvert à ce stade, et pas avant.*

### 6.1 Famille par famille

| Famille | SEMrush 28/08 (net) | DataForSEO 29/08 (net) | Rapport DFS / SEMrush |
|---|---:|---:|---:|
| Accessoires | 227 790 | 183 020 | **×0,80** |
| Voilage | 99 460 | 126 650 | **×1,27** |
| Thermique | ≈ 104 900 | 126 520 | **×1,21** |
| Occultation | 101 530 | 92 880 | **×0,91** |
| Lin | 37 520 | 33 580 | **×0,90** |
| Phonique | 30 880 | 20 840 | **×0,67** |
| Doubles rideaux | 21 780 | 17 280 | **×0,79** |
| Velours | 21 480 | 13 360 | **×0,62** |
| **CONSOLIDÉ** | **645 340** | **614 130** | **×0,95** |

**Écart sur le consolidé : −31 210/mois, soit −4,8 %.**

### 6.2 Classement des familles — quasi identique

| Rang | SEMrush 28/08 | DataForSEO 29/08 |
|---:|---|---|
| 1 | Accessoires (35 %) | Accessoires (30 %) |
| 2 | Thermique (16 %) | Voilage (21 %) |
| 3 | Occultation (16 %) | Thermique (21 %) |
| 4 | Voilage (15 %) | Occultation (15 %) |
| 5 | Lin (6 %) | Lin (5 %) |
| 6 | Phonique (5 %) | Phonique (3 %) |
| 7 | Doubles rideaux (3 %) | Doubles rideaux (3 %) |
| 8 | Velours (3 %) | Velours (2 %) |

Le n°1 est le même. **Les quatre familles du bloc de tête sont exactement les mêmes quatre**
(Accessoires, Voilage, Thermique, Occultation — 82 % chez SEMrush, 86 % chez DataForSEO) ; seul
leur ordre interne aux places 2-3-4 permute, entre des valeurs très proches. **Les quatre
dernières places sont dans l'ordre identique.** La liste des familles à sourcer en due diligence
(§0-6, ≥ 70 % du consolidé) est **rigoureusement la même** dans les deux chaînes.

### 6.3 Le verdict est-il le même ?

**Oui. Sans ambiguïté.** Les deux chaînes prononcent `PASS_PREQUALIFICATION`, sur des consolidés
distants de 4,8 %, avec le même n°1, le même bloc de tête et la même liste de familles à sourcer.
Aucune famille n'a fait basculer quoi que ce soit. La zone de cas limite (±20 % du seuil, soit
30 000–45 000 en recalibré) n'est approchée par aucune des deux mesures : elles sont toutes deux
à plus de seize fois le seuil.

### 6.4 Le résultat le plus important : deux erreurs qui se compensent

C'est le point à retenir, et il n'était pas prévisible.

- **Sur les têtes, DataForSEO lit systématiquement plus haut** que SEMrush :
  `rideau occultant` 33 100 → 49 500 (×1,50) · `rideau thermique` 33 100 → 49 500 (×1,50) ·
  `rideau velours` 1 900 → 2 900 (×1,53) · `embrasse rideau` 4 400 → 6 600 (×1,50) ·
  `tringle rideau` 18 100 → 22 200 (×1,23) · `anneaux rideaux` 1 900 → 2 900 (×1,53).
  Médiane ≈ ×1,25, conforme au recalibrage.
- **Sur le consolidé, DataForSEO rend pourtant 5 % de MOINS.**

L'explication tient en une phrase : **la chaîne SEMrush surestimait les grappes autant que
DataForSEO surestime les têtes.** La méthode du 28/08 additionne les formulations d'une même
grappe en supposant que chaque ligne est un corpus distinct — vrai chez SEMrush, faux chez Google.
La chaîne DataForSEO part de têtes 25 % plus hautes mais déduplique 14 % de buckets répétés puis
retire 22 % d'exclusions. Les deux biais se neutralisent presque exactement.

**Conséquence pratique : le consolidé est plus stable que ses composants.** L'écart-type de 2,65
mesuré tête à tête le 29/08 ne se propage pas au niveau agrégé. C'est ce qui rend la substitution
envisageable, et c'est ce que le croisement de la veille — qui ne comparait que des têtes — ne
pouvait pas voir.

### 6.5 Là où l'écart est le plus fort : Velours (×0,62) et Phonique (×0,67)

Ce sont les deux plus petites familles, donc celles où la traîne pèse le plus lourd relativement.
Sur Velours, la tête est plus HAUTE chez DataForSEO (2 900 vs 1 900) mais la grappe est plus
BASSE (13 360 vs 21 480) : c'est la signature exacte de la sur-sommation de formulations dans la
chaîne SEMrush. Sur Phonique, l'écart s'est réduit de ×0,43 à ×0,67 en passant d'une graine à
trois — donc une part venait bien d'un déficit de couverture de ma part, corrigé.

Aucune de ces deux familles ne représente plus de 3 % du consolidé. Un écart de ±40 % sur 3 %
déplace le total de 1,2 %.

---

## 7. Ce que chaque chaîne a vu que l'autre n'a pas vu

### 7.1 Ce que DataForSEO a vu et que SEMrush n'avait pas vu

1. **Le voile d'ombrage et le voile d'hivernage — 16 900/mois de contamination non détectée
   le 28/08.** `voilage ombrage` (8 100), `voilage hivernage` (4 400), `voilage hivernal` (4 400)
   sont respectivement une voile d'ombrage de terrasse et un voile d'hivernage de jardin. Ce ne
   sont pas des rideaux. Le rapport du 28/08 exclut du Voilage « sur-mesure + tissu 2 320 ·
   moustiquaire / store / voiture 960 » — jamais l'ombrage ni l'hivernage. **La table de thèmes
   co-occurrents du script les a fait sortir immédiatement** ; l'œil humain sur une lecture KMT
   de 100 lignes les avait manqués. C'est le gain le plus net de la nouvelle chaîne.
2. **La saisonnalité chiffrée.** Le rapport du 28/08 écrit noir sur blanc : *« Aucune amplitude
   chiffrée n'est avancée : l'outil n'en affiche pas »* (Google Trends ne donne que des indices
   relatifs). DataForSEO rend la série mensuelle en volumes absolus :
   `rideau thermique` passe de 18 100 (mars) à **135 000 (novembre 2025)** — **amplitude ×7,5**,
   mesurée et non estimée. `rideau velours` : ×5,1. `rideau occultant` : ×1,8 seulement, donc
   bien la famille de socle. Le profil « socle continu + bosse hivernale » décrit qualitativement
   le 28/08 est **confirmé et désormais quantifié**. C'est directement actionnable pour un
   calendrier d'acquisition Q4.
3. **La preuve que Google fusionne les buckets, et le critère pour le prouver.** L'identité de
   la série sur 12 mois distingue une reformulation d'une idée distincte, là où l'identité du
   volume ponctuel ne prouve rien. Ce critère n'existait pas dans la chaîne SEMrush, où la
   question ne se posait pas.
4. **L'ampleur du double comptage de l'ancienne méthode : 14 %**, chiffré ici pour la première
   fois sur un dossier réel.
5. **Le coût.** 2,52 USD contre 149 €/mois, et un rejeu ultérieur gratuit grâce au cache.

### 7.2 Ce que SEMrush avait et que DataForSEO n'a pas rendu

1. **Le KD (Keyword Difficulty).** Absent de la chaîne DataForSEO telle qu'outillée aujourd'hui.
   Le rapport du 28/08 donne un KD par tête (occultant 32, thermique 29, phonique 15, velours 17,
   lin 19, voilage 27, tringle 23) et s'en sert pour lire la défendabilité SEO. **C'est la perte
   la plus concrète.** DataForSEO expose un équivalent (`keyword_difficulty` dans
   `dataforseo_labs/google/keyword_overview`) mais il n'est ni appelé par `kw_dfs.py` ni validé
   contre le KD SEMrush — ce serait à instrumenter et à croiser avant de s'en servir.
2. **La classification d'intention (I / C / T / N).** Le 28/08 l'utilise pour trier commercial et
   informationnel. Pas d'équivalent dans la chaîne actuelle.
3. **Le contrôle témoin.** Le 28/08 vérifie `tufting = 8 100` avant et après la session pour
   attester que la base est restée `db=fr` et que rien n'a dérivé. **La chaîne DataForSEO n'a
   aucun contrôle d'intégrité équivalent** — `location_name: France` est passé à chaque appel,
   mais rien ne vérifie a posteriori que l'outil n'a pas dérivé. À combler.
4. **Le contrôle des niveaux de généralité, et le contrôle des fautes d'orthographe.** Le 28/08
   documente le cas décisif `rideau occultant total` (30) vs `rideau occultant` (33 100), soit
   ×1 103, ainsi que les fautes mortes (`rideau termique` 200, `rideau fonique` 0). Ces contrôles
   sont **méthodologiques et non liés à l'outil** — ils sont refaisables sous DataForSEO, mais
   ils n'ont pas été refaits ici et le rejeu ne les valide donc pas.
5. **La granularité fine des têtes.** SEMrush distingue `rideau occultant` (33 100) de
   `rideaux occultants` (18 100) — deux corpus. DataForSEO les rend rigoureusement identiques
   (49 500, même série). Pour la consolidation c'est un progrès ; pour **choisir la formulation
   exacte d'un titre de page ou d'une annonce**, on perd un signal de finesse.
6. **SERP, prix observés, concurrents, Google Trends 5 ans.** Le rapport du 28/08 les porte
   (7 SERP lues sur 2 pages, bandes de prix, 4 spécialistes DTC repérés, Trends 5 ans). Ces
   éléments ne viennent pas de SEMrush mais de Google, et **ce rejeu ne les a pas refaits**.
   Ils restent valables et ne sont pas en cause dans la question de la résiliation.

---

## 8. Réserves — aucune retirée

1. **Le test n'est pas parfaitement aveugle** (§1.1) : ~20 volumes de tête SEMrush ont été vus en
   allant chercher la recette d'appel. Portée limitée aux têtes, pas aux grappes ni au verdict,
   mais réelle.
2. **Un seul dossier a été rejoué, et c'est le plus facile possible.** Le consolidé est à ×16 du
   seuil. Un dossier à ce niveau ne peut pas basculer, quelle que soit la source. **Ce rejeu
   démontre la non-régression du verdict ; il ne démontre pas la fiabilité de l'outil en zone de
   décision.** Les écarts par famille vont de ×0,62 à ×1,27 : sur un dossier situé à ±20 % du
   seuil, un tel écart **suffirait à faire basculer PASS en STOP**, ou l'inverse.
3. **`kw_dfs.py` contient un bug de normalisation non corrigé** : `rideaux → rideal` via la règle
   `-aux → -al`. Il a été contourné à la main dans ce rejeu, au prix de 54 610 recherches/mois de
   surévaluation évitée. **Tant qu'il n'est pas corrigé dans le script, toute mesure faite avec
   `kw_dfs.py` sur un sujet dont le mot-clé se pluralise en `-aux` (rideaux, tuyaux, panneaux,
   carreaux, vitraux, chapeaux…) est surévaluée.** C'est un correctif à faire avant tout autre
   usage.
4. **Trois graines restent tronquées** (`rideau occultant`, `voilage`, `tringle rideau`). La
   traîne non lue est sous 10-20 recherches/mois par ligne, donc négligeable — mais c'est une
   **estimation**, pas une lecture.
5. **Aucun contrôle d'intégrité de la chaîne DataForSEO** (§7.2-3). Rien ne garantit a posteriori
   que la base est restée France sur toute la session, hors le fait que le paramètre est passé à
   chaque appel.
6. **Aucune SERP, aucun prix, aucun concurrent n'ont été rejoués.** Ce rapport ne dit rien sur la
   défendabilité du marché. Les réserves du 28/08 sur ce plan **tiennent toutes**, et notamment :
   51 % du consolidé est low-ticket (voilage + accessoires, médianes ~12 €, ratios prix ÷ CPC de
   41 et 60, **sous le plancher maison de 100**) ; l'univers passe le seuil de demande mais **n'a
   pas passé de test d'économie de panier**. Rien dans ce rejeu ne lève cette réserve.
7. **Le KD est perdu** (§7.2-1). Aucun substitut n'est validé à ce jour.
8. **L'affectation aux familles repose sur des listes de marqueurs écrites à la main.** Le total
   consolidé y est invariant, mais la répartition entre familles en dépend. Les ratios par
   famille du §6.1 sont donc moins solides que le ratio consolidé de ×0,95.
9. **La liste des marques exclues est manuelle et probablement incomplète.** 128 700 ont été
   retirés à ce titre ; une enseigne oubliée gonfle le consolidé.

---

## 9. Recommandation de non-régression — peut-on résilier SEMrush sur la foi de ce rejeu ?

**Réponse : non, pas sur la foi de ce seul rejeu. Mais il lève l'objection principale.**

### Ce que ce rejeu établit

Le verdict est **identique** (`PASS_PREQUALIFICATION`), le consolidé à **−4,8 %**, le classement
des familles quasi identique, et la liste des familles à sourcer **rigoureusement la même**.
Surtout, il explique **pourquoi** : les deux biais se compensent (§6.4). Il corrige donc la
conclusion du croisement du 28-29/08 — *« DataForSEO n'est pas substituable »* — qui était fondée
sur une comparaison **tête à tête**, là où notre méthode décide sur un **consolidé**. Un
écart-type de 2,65 sur les têtes ne se propage pas à l'agrégat. C'est un fait nouveau.

### Ce qu'il n'établit pas

1. **La zone de décision n'a pas été testée.** Ce dossier est à ×16 du seuil : c'est le test le
   moins exigeant qui soit. Les écarts par famille (×0,62 à ×1,27) montrent que sur un dossier
   à ±20 % du seuil, la chaîne DataForSEO **peut rendre un verdict différent**. Or c'est
   exactement là que l'outil doit être fiable — les dossiers à ×16 se décident sans outil.
2. **La reproductibilité n'est pas testée.** Un seul dossier, une seule session.
3. **Le KD est perdu sans substitut validé**, et la chaîne n'a aucun contrôle d'intégrité.
4. **Le script a un bug actif** qui surévalue tout sujet en `-aux`.

### Ce que je recommande à Hakim, dans cet ordre

1. **Corriger `kw_dfs.py`** (recollage `-aux`, et ajouter un contrôle témoin en début et fin de
   session, sur le modèle du `tufting = 8 100` de SEMrush). Une demi-heure de travail, et c'est
   bloquant : sans ça, la chaîne est fausse sur toute une classe de sujets.
2. **Rejouer un second dossier, choisi pour être en zone de décision** — idéalement un dossier
   conclu `STOP` ou proche du seuil à la SEMrush. C'est le seul test qui répond vraiment à la
   question. Si le verdict tient aussi là, la démonstration est faite.
3. **Instrumenter et croiser `keyword_difficulty`** de `dataforseo_labs/google/keyword_overview`
   contre les KD SEMrush du 28/08, tant que l'abonnement est encore actif. **Cette mesure n'est
   plus possible après résiliation** — c'est la raison la plus forte de ne pas résilier tout de
   suite.
4. **Ne résilier qu'ensuite.** Les points 2 et 3 exigent SEMrush encore vivant. Un mois
   supplémentaire à 149 € achète la seule fenêtre où l'on peut encore calibrer le remplaçant
   contre l'original. Résilier maintenant fermerait cette porte définitivement, pour économiser
   un mois.

**Formulation courte pour la décision : le rejeu est un succès, la substitution est
vraisemblable, et il manque exactement deux mesures — un dossier en zone de décision, et le
calibrage du KD — qui ne peuvent être faites que tant que SEMrush est encore payé.**

---

*Rapport de phase 3. Aucun sourcing, aucun fournisseur, aucune cartographie de concurrence.
Aucun `GO_FINAL` n'est prononcé : la décision commerciale appartient à Hakim.*
