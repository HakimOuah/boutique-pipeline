# Chasse aux clusters — Panneaux muraux bois (mode CIBLÉ) — 2 septembre 2026

Agent : `phase0-decouverte`, mode CIBLÉ (qualification express d'une idée apportée par Hakim, pas un balayage de famille). Idée de départ : panneaux muraux décoratifs en bois sur le modèle de thepanelhub.com (trois types : tasseaux bois sur feutre, 3D géométrique bois, aspect roche). Mesure en **PRODUIT PUR** (seuil 12 500/mois, `PRODUCT-RESEARCH-CRITERIA.md` §1) ; niveaux UNIVERS « revêtement mural décoratif » (plancher 37 500) rendus **séparément, jamais sommés**.

Ce rapport ne propose aucun produit, ne juge ni concurrence ni adressabilité, ne rend aucun verdict. Il rend des volumes France datés et leur composition. L'adressabilité des têtes mixtes se tranche en `phase3-demande` sur SERP réelle.

---

## 1. Entrée

- **Famille traitée** : « panneaux muraux bois » (hors `familles-exploration.md` — entrée par l'idée, chemin A, mesure express avant tout filtre qualitatif).
- **Date et plage des appels** : mardi 2 septembre 2026, 14h16 – 14h20 (heure de Paris). Horodatage de chaque appel ci-dessous.
- **Source unique** : DataForSEO API. Chaque payload porte `location_name: France`, `language_name: French` (constaté dans le code de `kw_dfs.py` lignes 138 et 198-199, et dans `params` des JSON `tetes-1.json` / `tetes-2.json` / `temoin-*.json`). Aucune donnée d'un autre pays ni d'une autre langue.
- **Endpoints** :
  - découverte : `dataforseo_labs/google/keyword_suggestions/live` via `scripts/kw_dfs.py`, `--pages 1 --top 40 --json`, correspondance plein texte, déduplication MAX du groupe ;
  - contrôle de tête : `keywords_data/google_ads/search_volume/live`, `search_partners: false`, via un script horodaté du scratchpad (`dfs_live.py`).
- **Identifiants** : chargés depuis `ecommerce-dropshipping/.env` par `set -a; source; set +a`. Aucune valeur affichée ni copiée.

### Graines passées dans `kw_dfs.py`

| Graine | Heure | Lignes brutes | Idées dédupliquées | Suggestions annoncées | Coût annoncé (USD) |
|---|---|---:|---:|---:|---:|
| panneau acoustique | 14:16:44 | 1 000 | 725 | 1 001 | 0,132 |
| panneau tasseaux | 14:16:46 | 35 | 22 | 35 | 0,016 |
| panneau mural bois | 14:16:48 | 287 | 163 | 287 | 0,046 |
| panneau mural 3d | 14:16:51 | 131 | 93 | 131 | 0,028 |
| revêtement mural bois | 14:16:54 | 73 | 54 | 73 | 0,021 |
| panneau mural décoratif *(dérivée 1)* | 14:17:56 | 168 | 118 | 168 | 0,032 |
| lambris *(dérivée 2)* | 14:19:20 | 1 000 | 423 | 7 736 | 0,132 |

Graine « tasseaux bois mural » du brief : passée en contrôle de tête (110/mois) plutôt qu'en découverte, la graine « panneau tasseaux » couvrant déjà l'objet. Dérivée 1 justifiée par le thème co-occurrent `décoratif` (28 idées / 8 730 cumulés sur la graine « panneau mural bois »). Dérivée 2 = catégorie parente de la règle hiérarchique du brief, et le témoin de contamination GSB/PVC.

### Contrôles de tête `search_volume/live`

| Lot | Heure | Mots-clés | Coût (USD) | Fichier |
|---|---|---:|---:|---|
| tetes-1 | 14:17:49 | 36 | 0,09 | scratchpad `tetes-1.json` |
| tetes-2 | 14:19:15 | 78 | 0,09 | scratchpad `tetes-2.json` |

### Témoins `tufting`

| Moment | Heure | Volume | CPC | Série 12 mois (ancien → récent) |
|---|---|---:|---:|---|
| avant première mesure | 14:16:44 | **12 100** | 1,62 | 8100 14800 9900 14800 14800 14800 9900 9900 9900 9900 6600 6600 |
| après dernière mesure | 14:19:50 | **12 100** | 1,62 | identique |

Conformes et cohérents entre eux (identiques au témoin de l'orchestrateur à 14h1x). Chacun des 7 passages de `kw_dfs.py` a en outre tiré son propre témoin avant et après (14 lectures, toutes à 12 100, conformes strictes). Aucun zéro silencieux, aucune réponse vide.

### Coût DataForSEO

- **Observé** : 0,407 USD (7 passages `kw_dfs.py`, coût annoncé par le script) + 0,36 USD (4 appels `search_volume/live` explicites : 2 témoins + 2 lots de têtes, 0,09 chacun) = **0,767 USD**.
- **Déduit, non observé** : les 14 témoins internes de `kw_dfs.py` ne sont pas inclus dans le coût annoncé par le script ; au tarif observé de 0,09 USD par appel identique, ≈ 1,26 USD supplémentaires. Total déduit ≈ **2,03 USD**.

### Convention de lecture

- « Volume » = `search_volume` mensuel France, dernier mois disponible tel que rendu par l'API.
- Un **bucket** = une série mensuelle distincte. Google pré-agrège des variantes proches sous une même série ; deux formulations à série identique comptent une fois (MAX). Toute somme ci-dessous a été vérifiée bucket par bucket : **aucune ligne comptée deux fois** (vérification programmatique des séries, 2/09 14h20).
- Volumes « labs » = lus dans les suggestions DataForSEO Labs ; volumes « live » = recontrôlés par `search_volume/live`. Les têtes et mots décisifs sont tous « live ».

---

## 2. Clusters retenus (≥ 12 500/mois)

### 2.1 Panneau tasseaux bois — **niveau spécifique** (type 1 du brief, « slat wall panel »)

**Le seuil est franchi par la tête seule : `panneau tasseaux bois` = 14 800.** Aucune addition n'est nécessaire.

| Mot-clé | Volume | CPC (EUR) | Source | Note |
|---|---:|---:|---|---|
| panneau tasseaux bois | **14 800** | 0,32 | live | tête ; série 18100 14800 18100 18100 14800 22200 18100 14800 14800 14800 9900 12100 |
| panneau tasseaux | 3 600 | 0,39 | live | bucket distinct (série propre) |
| panneau tasseaux de bois | 590 | 0,41 | labs | |
| panneau mural tasseau bois | 590 | 0,37 | labs | |
| panneau bois tasseaux | 480 | 0,35 | live | ordre des mots — bucket distinct de la tête |
| panneau tasseaux bois mural | 480 | 0,48 | live | |
| panneau en tasseaux de bois | 390 | 0,22 | labs | |
| panneau de tasseaux | 390 | 0,25 | labs | |
| panneau tasseaux noir | 320 | 0,59 | live | |
| panneau décoratif tasseaux bois | 260 | 0,31 | labs | |
| panneau tasseaux acoustique | 260 | 0,56 | live | |
| panneau mural tasseaux | 170 | 0,44 | live | |
| panneau acoustique tasseaux | 140 | 0,81 | live | |
| panneau acoustique tasseaux bois | 140 | 0,99 | labs | |
| panneau tasseaux bois fond noir | 30 | 0,25 | labs | |

- **Volume total dédupliqué : 22 640/mois** (15 buckets distincts, séries vérifiées). Tête seule : 14 800.
- **CPC moyen** (pondéré par volume) : ≈ 0,34 EUR. Concurrence Google Ads : HIGH sur toutes les têtes.
- **Saisonnalité observée** sur la tête : 9 900 – 12 100 en fin de série (deux derniers mois) contre 14 800 – 22 200 sur les dix précédents ; le pic 22 200 est le 6e mois de la série.
- **Méthode de déduplication** : `kw_dfs.py` avait regroupé 6 formulations sous 14 800 (MAX) ; le contrôle live montre que ces 6 formulations portent 6 séries différentes — le regroupement par ordre des mots n'était pas un bucket Google unique. Le MAX a protégé le chiffre ; le tableau ci-dessus rend chaque bucket avec son volume propre.
- **Exclus de ce cluster** (voir §4) : enseignes (`panneau tasseaux leroy merlin` 1 600, `panneau tasseaux bois leroy merlin` 720, `centrakor` 720, `castorama` 260, `atmosphera` 140, `colva` 90+10), tasseaux bruts / mur DIY (`mur tasseaux bois` 2 400, `tasseau mural` 1 900, `mur en tasseaux` 210, `tasseaux bois mural` 110), lattes (`panneau latte bois mural` 260 — hésitation, compté en 2.3).

### 2.2 Panneau acoustique — **niveau famille**

**Tête seule : `panneau acoustique` = 22 200**, au-dessus du seuil. Mais c'est un bucket **à intention mixte** (le mot recouvre la mousse studio, les panneaux de bureau B2B, l'isolation et les panneaux déco bois) : l'adressabilité de la tête est à trancher en phase 3. Ci-dessous, le **cœur mural/déco** du cluster, sans les contaminations listées en §4.

| Mot-clé | Volume | CPC (EUR) | Source |
|---|---:|---:|---|
| panneau acoustique | **22 200** | 0,78 | live |
| panneau acoustique mural | 5 400 | 0,75 | live |
| panneau acoustique muraux | 1 600 | 1,01 | labs |
| panneau acoustique décoratif | 880 | 0,77 | live |
| panneau acoustique blanc | 480 | 0,53 | live |
| panneau acoustique mural décoratif | 390 | 0,74 | live |
| panneau acoustique noir | 390 | 1,03 | live |
| panneau acoustique design | 320 | 1,24 | live |
| panneau acoustique mural à coller | 320 | 0,36 | labs |
| panneau acoustique chambre | 260 | 0,26 | live |
| tête de lit panneau acoustique | 260 | 0,19 | live |
| panneau acoustique pas cher | 260 | 0,43 | live |
| panneau acoustique 240x60 | 210 | 0,69 | live |
| panneau acoustique salon | 140 | 0,30 | live |
| panneau acoustique tête de lit | 110 | 0,39 | live |

- **Volume total dédupliqué (cœur mural/déco) : 33 220/mois** (15 buckets distincts). Tête seule : 22 200.
- **CPC moyen** pondéré : ≈ 0,77 EUR — plus du double du cluster tasseaux.
- **Saisonnalité** de la tête : 27 100 sur 4 mois du milieu de série, 12 100 sur les deux derniers.
- **Sous-famille « panneau acoustique bois »** : mesurée à part en §3.1 (11 780, sous le seuil) et **non additionnée** ici. Les séries de `panneau acoustique bois` (9 900) et de `panneau tasseaux bois` (14 800) sont distinctes : deux buckets, deux formulations. Observation (déduite, à vérifier en SERP) : le vocabulaire retail français des panneaux à tasseaux est souvent « panneau acoustique » (Atmosphera, Centrakor, Action apparaissent sous les deux graines) — ce recouvrement commercial ne justifie pas une addition ; il justifie une lecture SERP.
- **Contamination lisible dans les suggestions** (non comptée) : bureau/open space 1 070 cumulés (9 idées, CPC jusqu'à 3,78), isolation 1 290 (24 idées), mousse 780 (18 idées), plafond 2 550 (29 idées), studio 400 (11 idées), extérieur 1 290 (14 idées), suspendu 390, absorbant 390, fabriquer/pose/fixer/comment ≈ 1 970 cumulés, accessoires (LED 480+320, étagère 390, colle 390+320). Détail §4.

### 2.3 Panneau mural bois — **niveau famille**

**Tête seule : `panneau mural bois` = 12 100, soit 400 sous le seuil.** Le cluster le franchit par les **buckets d'ordre des mots de la même expression** (`panneau bois mural` 8 100, `panneau de bois mural` 1 600, `panneau mural en bois` 1 000 — séries vérifiées distinctes) et par ses qualificatifs déco/intérieur. Ce n'est pas l'addition d'une famille voisine : même objet, mêmes mots.

| Mot-clé | Volume | CPC (EUR) | Source |
|---|---:|---:|---|
| panneau mural bois | **12 100** | 0,30 | live |
| panneau bois mural | 8 100 | 0,34 | labs |
| panneau mural bois décoratif intérieur | 4 400 | 0,32 | live |
| panneau mural décoratif bois *(6 formulations fusionnées par Google, 1 série)* | 2 400 | 0,31 | labs |
| panneau de bois mural | 1 600 | 0,37 | labs |
| panneau mural en bois | 1 000 | 0,27 | labs |
| panneau mural bois intérieur | 720 | 0,45 | labs |
| panneau mural bois 240x60 | 390 | 0,47 | live |
| panneau latte bois mural | 260 | 0,19 | live |
| panneau décoratif mural bois | 170 | 0,56 | labs |
| panneau mural bois noir | 110 | 0,34 | live |
| panneau mural bois blanc | 110 | 0,31 | labs |
| panneau mural bois noyer | 90 | 0,40 | live |
| panneau mural bois salon | 90 | 0,23 | live |
| panneau mural bois chambre | 90 | 0,13 | live |
| panneau mural bois 120x60 | 90 | 0,28 | labs |
| panneau mural bois 250 cm | 90 | 0,72 | labs |
| panneau bois massif mural / foncé mural / noyer mural | 10 + 10 + 10 | — | labs |

- **Volume total dédupliqué : 31 840/mois** (20 buckets distincts). Tête seule : 12 100 (sous seuil).
- **CPC moyen** pondéré : ≈ 0,32 EUR.
- **Non comptés ici pour éviter le double compte** : `panneau mural tasseau bois` 590 et `panneau tasseaux bois mural` 480 (déjà dans 2.1), `panneau mural bois 3d` 880 (segment 3D, §3.2).
- **Exclus** (§4) : enseignes (`action` 880, `ikea` 720, `leroy merlin` 480+480, `brico dépôt` 260+260, `centrakor` 260+110, `castorama` 110+110, `gifi` 70), imitation/effet bois (140+110), salle de bain (110+70+40), extérieur (260 labs / 40 live), `habillage mural bois` 1 000 (terme voisin, objet incertain — hésitation → exclu, noté en §5).

### 2.4 Lambris bois — **niveau catégorie parente, objet différent**

Mesuré parce que la règle hiérarchique du brief le nomme comme parent. **Ce n'est pas un panneau** : lames rainurées vendues au m², catégorie GSB. Rendu ici parce qu'il dépasse le seuil ; il ne s'additionne à aucun cluster ci-dessus.

| Mot-clé | Volume | CPC (EUR) | Source |
|---|---:|---:|---|
| lambris bois | **14 800** | 0,15 | live |
| lambris | 12 100 | 0,17 | live |
| lambris bois mural | 2 900 | 0,17 | labs |
| lambris bois plafond | 2 900 | 0,17 | labs |
| lambris plafond | 2 900 | 0,16 | live |
| lambris mural | 1 900 | 0,20 | live |
| lambris bois blanchi | 1 300 | 0,20 | labs |
| lambris à peindre | 1 300 | 0,22 | labs |
| lambris blanchi | 1 000 | 0,21 | labs |
| lambris bois intérieur | 720 | 0,17 | live |
| lambris mdf | 720 | 0,17 | labs |
| lambris peuplier | 590 | 0,49 | labs |
| lambris chêne | 320 | 0,25 | live |
| lambris de bois | 70 | 0,14 | labs |

- **Volume total dédupliqué : 43 520/mois** (14 buckets). Tête seule : 14 800.
- **CPC moyen** ≈ 0,17 EUR — le plus bas de tout le rapport.
- **Contamination massive** lue dans les thèmes co-occurrents de la graine : `pvc` 135 idées / 50 570 cumulés (`lambris pvc` 12 100, `lambris plafond pvc` 6 600, `lambris extérieur pvc` 2 900, `lambris mural pvc` 2 900…), `plafond` 62 idées / 24 650, GSB (`brico dépôt` 7 430, `leroy merlin` 5 040, `castorama` 590+590), `sous-toiture` 3 650, `pose`/`poser`/`comment`/`peindre` ≈ 11 000 cumulés. Le mot nu `lambris` (12 100) est à intention mixte PVC/bois/plafond.

### Règle hiérarchique — récapitulatif des niveaux (jamais sommés)

| Niveau | Mot-clé | Volume live | CPC | Statut seuil PUR 12 500 |
|---|---|---:|---:|---|
| Spécifique | panneau tasseaux bois | 14 800 | 0,32 | ≥ seuil (tête seule) |
| Spécifique | panneau acoustique bois | 9 900 | 0,73 | < seuil (cluster 11 780) |
| Spécifique | panneau acoustique tasseaux | 140 | 0,81 | < seuil |
| Famille | panneau acoustique | 22 200 | 0,78 | ≥ seuil (tête mixte) |
| Famille | panneau mural bois | 12 100 | 0,30 | tête < seuil de 400 ; cluster 31 840 ≥ seuil |
| Famille | panneau mural décoratif | 12 100 | 0,29 | tête < seuil de 400 (niveau parent du 2.3, non cumulé) |
| Parente | panneau mural | 18 100 | 0,32 | mot nu, intention mixte (PVC, salle de bain, 3D…) |
| Parente | revêtement mural | 9 900 | 0,32 | < seuil |
| Parente | revêtement mural bois | 2 400 | 0,30 | < seuil |
| Parente | lambris bois / lambris | 14 800 / 12 100 | 0,15 / 0,17 | ≥ seuil, objet différent |
| Voisin | claustra bois / claustra bois intérieur / claustra intérieur | 33 100 / 12 100 / 8 100 | 0,26 / 0,28 / 0,24 | objet différent (cloison/brise-vue), non balayé |
| Voisin | parement pierre / parement pierre intérieur / plaquette de parement / parement mural | 12 100 / 6 600 / 4 400 / 2 400 | 0,22 / 0,19 / 0,18 / 0,23 | objet différent (pierre réelle, GSB) |

### Lecture UNIVERS « revêtement mural décoratif » (plancher 37 500) — niveaux séparés

Le brief demande ce qu'il faudrait pour une lecture UNIVERS, sans additionner. Ce qui est **observé** : les têtes des familles candidates à un même catalogue sont `panneau mural` 18 100, `panneau mural décoratif` 12 100, `panneau mural bois` 12 100, `panneau acoustique` 22 200, `revêtement mural` 9 900, `lambris bois` 14 800, `parement pierre` 12 100, `claustra bois intérieur` 12 100. Ce qui **manque** pour une consolidation UNIVERS conforme au §0.6 des critères : la consolidation par familles nettes de marque et de SERP (papier peint, parement, lambris et claustra sont des objets, des fournisseurs et des logistiques différents), puis la sourçabilité par famille. Ce rapport ne consolide pas ; il rend les têtes pour que la Mission B UNIVERS, si elle est lancée, parte de chiffres datés.

---

## 3. Clusters écartés (sous le seuil)

### 3.1 Panneau acoustique bois — sous-famille spécifique (type 1 sous vocabulaire « acoustique »)

| Mot-clé | Volume | CPC | Source |
|---|---:|---:|---|
| panneau acoustique bois (= `panneau acoustique en bois` = `panneau bois acoustique`, même série) | 9 900 | 0,73 | live |
| panneau acoustique bois 240x60 | 210 | 0,75 | labs |
| décoratif panneau acoustique bois | 210 | 0,57 | labs |
| panneau de bois acoustique | 170 | 0,54 | labs |
| panneau acoustique mural bois | 140 | 0,89 | live |
| panneau acoustique bois mural | 110 | 1,83 | live |
| panneau mural acoustique bois | 110 | 0,41 | labs |
| panneau acoustique noyer | 110 | 1,53 | labs |
| panneau acoustique bois noir | 110 | 1,21 | labs |
| panneau bois acoustique mural / en bois acoustique / bois blanc | 90 × 3 | — | labs |
| bois 260 cm / 250 x 60 | 70 × 2 | — | labs |
| chêne / bois massif / bois 250 / fond blanc / bois 300 cm / panneau mural bois acoustique | 50 × 6 | — | labs |

**Total dédupliqué : 11 780/mois** (20 buckets) — **720 sous le seuil**. Tête seule 9 900. Écarté en tant que cluster autonome ; **non additionné** au cluster 2.1 malgré la proximité commerciale (voir observation en 2.2). Exclus de cette liste : `perforé` (110, produit pro différent), `fibre de bois` (90, matériau d'isolation), enseignes (ikea 210, leroy merlin 210+210, brico 170, castorama 90+50, action 70, centrakor 70, atmosphera 50), pose/fabriquer (70+50), colle (50).

### 3.2 Panneau mural 3D (type 2 du brief, « GroovePanel »)

| Mot-clé | Volume | CPC | Source |
|---|---:|---:|---|
| panneau mural 3d (= `3d panneau mural`) | 1 600 | 0,38 | live |
| panneau 3d mural | 880 | 0,37 | labs |
| panneau mural 3d bois (= `panneau mural bois 3d`) | 880 | 0,23 | live |
| panneau mural décoratif 3d / panneau mural 3d salon / panneau mural relief | 170 × 3 | — | labs/live |
| panneau 3d bois | 110 | 0,43 | live |
| panneau décoratif mural 3d / panneau mural 3d à peindre | 90 × 2 | — | live |
| noir / blanc / chambre / vague / mdf / tête de lit | 40+40+30+20+10+0 | — | labs |

**Total dédupliqué : 4 340/mois** — ×2,9 sous le seuil. `panneau mural géométrique` et `panneau mural bois géométrique` : **aucune donnée** rendue par Google Ads (volume `None`). Contamination du segment : PVC (6 idées), adhésif/autocollant (110+30+20), polystyrène (50), Maghreb (`tunisie`, `maroc`, `algérie` ≈ 60 cumulés), moule (20).

### 3.3 Panneau aspect pierre / roche (type 3 du brief, « RockSurface »)

| Mot-clé | Volume | CPC | Source |
|---|---:|---:|---|
| panneau mural effet pierre | 390 | 0,24 | live |
| panneau mural pierre | 320 | 0,31 | live |
| panneau imitation pierre | 320 | 0,24 | live |
| panneau pierre mural | 90 | 0,31 | live |
| panneau mural 3d roche | 50 | 0,27 | live |
| panneau mural 3d effet pierre | 40 | 0,34 | labs |
| panneau mural aspect pierre | 10 | 0,20 | live |
| panneau 3d mural pierre | 10 | 0,31 | labs |

**Total dédupliqué : 1 230/mois** — ×10 sous le seuil. Le vocabulaire réel de la pierre murale intérieure est `parement` (`parement pierre` 12 100, `parement pierre intérieur` 6 600, `plaquette de parement` 4 400, `parement mural` 2 400) : objet différent (pierre reconstituée ou naturelle en plaquettes, GSB), non additionné.

### 3.4 Revêtement mural bois

| Mot-clé | Volume | CPC | Source |
|---|---:|---:|---|
| revêtement mural bois (= `revêtement bois mural` = `bois revêtement mural`) | 2 400 | 0,30 | live |
| revêtement mural en bois | 320 | 0,24 | labs |
| revêtement mural bois à coller | 170 | 0,16 | live |
| salon / tasseau bois / chambre / vertical / design | 70+70+40+20+10 | — | labs |

**Total dédupliqué : 3 100/mois** — ×4 sous le seuil. Parent `revêtement mural` 9 900 (mot nu, sous seuil).

### 3.5 Formulations spécifiques « tasseaux + acoustique »

`panneau acoustique tasseaux` 140, `panneau tasseaux acoustique` 260, `panneau acoustique tasseaux bois` 140, `panneau mural acoustique tasseaux bois` 10, `panneau acoustique bois tasseaux` et `panneau acoustique lattes bois` = aucune donnée. La formulation « acoustique tasseaux » du brief n'existe pas comme tête : elle vaut 140–260 et est comptée dans 2.1.

---

## 4. Mots-clés exclus des clusters (avec motif)

| Mot-clé | Volume | Motif d'exclusion |
|---|---:|---|
| panneau acoustique leroy merlin / leroy merlin panneau acoustique / panneau acoustique mural leroy merlin / panneau acoustique bois leroy merlin / panneau bois acoustique leroy merlin | 1 600 / 390 / 320 / 210 / 210 | enseigne GSB |
| panneau tasseaux leroy merlin / panneau tasseaux bois leroy merlin / panneau mural bois leroy merlin / panneau mural bois décoratif intérieur leroy merlin / panneau mural 3d leroy merlin / revêtement mural bois leroy merlin | 1 600 / 720 / 480 / 480 / 480 / 90 | enseigne GSB |
| panneau acoustique mural ikea / ikea panneau acoustique / panneau acoustique bois ikea / panneau mural bois ikea / panneau mural décoratif intérieur ikea | 1 000 / 320 / 210 / 720 / 390 | marque |
| panneau acoustique atmosphera / atmosphera panneau acoustique / panneau tasseaux atmosphera / panneau acoustique bois atmosphera | 590 / 320 / 140 / 50 | marque |
| panneau tasseaux centrakor / panneau mural bois centrakor / centrakor panneau acoustique / panneau acoustique bois centrakor | 720 / 260+110 / 260 / 70 | enseigne |
| panneau mural bois action / panneau acoustique action / panneau mural décoratif action / panneau acoustique bois action | 880 / 390 / 140+50 / 70 | enseigne |
| panneau acoustique brico dépôt / panneau tasseaux castorama / panneau acoustique castorama / panneau mural bois brico dépôt / castorama / gifi | 480 / 260 / 390 / 260 / 110 / 70 | enseigne GSB |
| colva (panneau décoratif tasseaux bois colva, panneau tasseaux colva) / wodewa / orac / angly | 90+10 / 10 / 10 / 10 | marque |
| mousse acoustique / panneau mousse acoustique / panneau de mousse acoustique / panneau acoustique mousse | 8 100 / 390 / 110 / 110 | mousse low-ticket, studio — objet différent |
| panneau acoustique studio (+ musique, home studio, enregistrement) | 260 + 40 + 40 + 30 | studio / pro |
| panneau acoustique bureau / pour bureau / bureau ikea / open space | 480 / 480 / 50 / 20 | B2B (CPC 3,78) |
| isolation phonique / panneau isolation acoustique / panneau pour isolation acoustique / panneau acoustique isolant / isolation acoustique murale | 14 800 / 480 / 480 / 480 / 70 | travaux, isolation — objet différent |
| panneau acoustique plafond / pour plafond / suspendu / absorbant | 1 900 / 1 900 / 390 / 390 | plafond, baffle, absorbant technique — objet différent |
| panneau acoustique extérieur / exterieur / fabriquer panneau acoustique extérieur | 880 / 880 / 30 | écran anti-bruit extérieur — objet différent |
| panneau acoustique porte | 210 | objet différent |
| panneau acoustique salle de bain / panneau acoustique pvc / panneau acoustique 3d | 50 / 20 / 50 | contaminations mineures, objet différent |
| panneau bois perforé acoustique / panneau acoustique fibre de bois | 110 / 90 | produit pro / matériau d'isolation |
| panneau acoustique laine de roche (3 formulations) | 90 × 3 | isolant, objet différent |
| led pour panneau acoustique / led panneau acoustique / étagère pour panneau acoustique / colle panneau acoustique / colle pour panneau acoustique / accessoires panneau acoustique / crochet pour panneau acoustique | 480 / 320 / 390 / 390 / 320 / 210 / 170 | accessoire, pas l'objet |
| fabriquer panneau acoustique (+ « un », tasseau bois) / pose panneau acoustique / poser / pose leroy merlin / comment fixer / fixer / comment couper / panneau acoustique diy / fabrication | 210+210+50 / 140 / 140 / 90 / 110 / 70 / 30 / 170 / 210 | informationnel / tutoriel de pose / DIY |
| location panneau acoustique / panneau acoustique occasion | 0 / 20 | location / occasion |
| mur tasseaux bois / tasseau mural / mur en tasseaux / tasseaux bois mural | 2 400 / 1 900 / 210 / 110 | tasseaux bruts, mur DIY — objet différent du panneau fini (hésitation → exclu ; à lire en SERP phase 3) |
| habillage mural bois / habillage mural / panneau habillage mural bois | 1 000 / 1 900 / 140 | terme générique (planches, lambris, panneaux) — hésitation → exclu |
| panneau mural effet bois / panneau mural imitation bois / revêtement mural effet bois / imitation bois / polystyrène effet bois | 140 / 110 / 90 / 70 / 10 | imitation, pas du bois |
| panneau mural bois salle de bain / panneau mural salle de bain effet bois / revêtement mural bois salle de bain / panneau mural salle de bain / panneau mural pvc | 110 / 70 / 70 / 9 900 / 4 400 | PVC salle de bain — objet différent |
| panneau mural 3d pvc / adhésif / autocollant / auto adhésif / polystyrène / panneau décoratif mural pvc / panneau mural décoratif intérieur pvc | 90 / 110 / 30 / 20 / 50 / 110 / 90 | PVC, adhésif low-ticket |
| panneau mural 3d tunisie prix / maroc / algérie / belgique ; revêtement mural bois maroc / tunisie | 10 / 20 / 10 / 10 ; 10 / 10 | hors France (mot-clé), volume marginal |
| panneau bois mural extérieur / panneau décoratif mural extérieur / panneau mural bois décoratif extérieur / revêtement bois mural extérieur / lambris extérieur | 260 labs (40 live) / 480 / 30 / 40 / 1 300 | extérieur — objet différent |
| panneau décoratif mural papier peint / panneau mural décoratif isolant thermique / panneau mural décoratif douche / cuisine | 90 / 50 / 50 / 30 | objet différent |
| quel revêtement mural derrière un poêle à bois / revêtement mural derrière poêle à bois / revêtement mural poêle à bois | 20 / 20 / 0 | informationnel, protection poêle |
| moule panneau mural 3d / comment peindre panneau mural 3d | 20 / 0 | fabrication / informationnel |
| lambris pvc (et 135 idées PVC, 50 570 cumulés) / lambris plafond pvc / lambris extérieur pvc / lambris mural pvc / lambris pvc salle de bains / sous-toiture | 12 100 / 6 600 / 2 900 / 2 900 / 1 600 / 720+590 | PVC, plafond, toiture — objets différents du bois |
| brico dépôt lambris (bois / pvc / nu) / lambris leroy merlin (+ pvc, bois) / castorama lambris (+ pvc) | 1 300 / 1 300 / 1 000 ; 1 300 / 1 000 / 1 000 ; 590 / 590 | enseigne GSB |
| poser lambris pvc plafond / lambris pose / peinture lambris vernis / lambris à peindre (compté 2.4 comme produit) | 880 / 720 / 480 | informationnel / pose |
| claustra bois / claustra bois intérieur / claustra intérieur | 33 100 / 12 100 / 8 100 | objet différent (cloison, brise-vue) — voir §5 |
| parement pierre / parement pierre intérieur / plaquette de parement / parement mural | 12 100 / 6 600 / 4 400 / 2 400 | objet différent (pierre en plaquettes, GSB) |

Aucun mot-clé exclu n'entre dans un total de la section 2.

---

## 5. Graines dérivées (auto-expansion)

Thèmes co-occurrents et termes connexes rendus par DataForSEO Labs autour des clusters retenus. Volumes indiqués = déjà mesurés en contrôle de tête ce jour ; « non mesuré » = à passer si la famille est poursuivie.

- **Autour de 2.1 tasseaux** : `claustra bois intérieur` (12 100 ; `claustra bois` 33 100 largement extérieur, `claustra intérieur` 8 100) — même esthétique tasseaux, objet cloison ; poche voisine non balayée, à traiter comme famille séparée. `mur tasseaux bois` / `tasseau mural` (2 400 / 1 900) — DIY tasseaux bruts, à lire en SERP pour savoir si les panneaux finis y répondent. `tête de lit panneau acoustique` / `panneau mural bois tête de lit` (260 / aucune donnée) — usage tête de lit. `panneau tasseaux noir` (320), `noyer` (110+90), `chêne` (50+320 lambris) — finitions.
- **Autour de 2.2 acoustique** : `panneau acoustique plafond` (1 900) et `suspendu` (390) — segment plafond, à balayer séparément si intérêt ; `panneau acoustique chambre` (260) ; `panneau acoustique à coller` (320) ; accessoires `led` / `étagère` / `colle` (480 / 390 / 390) — signal d'extensions de gamme, pas de volume produit.
- **Autour de 2.3 panneau mural bois** : `habillage mural bois` (1 000) et `habillage mural` (1 900) — termes à lire en SERP ; `panneau latte bois mural` (260) ; `panneau mural bois 240x60` / `120x60` / `250 cm` (390 / 90 / 90) — formats ; `panneau mural décoratif salon` (590), `chambre` (140).
- **Catégorie parente déco** : `panneau mural décoratif intérieur` (4 400), `panneau décoratif mural` (1 900 — bucket distinct de `panneau mural décoratif` 12 100), `panneau mural` (18 100 mot nu).
- **Pierre** : `parement pierre intérieur` (6 600), `plaquette de parement` (4 400) — famille pierre réelle, distincte du « panneau aspect roche » mesuré à 1 230.
- **Non mesuré, signalé par les suggestions** : `papier peint` (4 idées / 130 cumulés sur la graine décoratif — famille voisine déjà au registre, voir §6), `moulure murale` / `tasseaux décoratifs` (aucune graine passée).

---

## 6. Doublons registre

- **« Panneaux muraux bois géométriques »** — `REJET PHASE 2` du 01/09/2026 (motif qualitatif : peu offrable, quantité, logistique ; **sans volume mesuré**). Correspond au type 2 du brief. Mesuré aujourd'hui sur **demande explicite de Hakim (reprise motivée)** : cluster 3D à 4 340/mois (§3.2), sous le seuil — la mesure confirme a posteriori l'écart, pour un motif différent (volume).
- **« Panneaux muraux aspect roche »** — `REJET PHASE 2` du 01/09/2026 (logistique et pose ; sans volume mesuré). Type 3 du brief. Reprise motivée : 1 230/mois (§3.3), sous le seuil.
- Le type 1 (tasseaux / acoustique bois) **n'a aucune entrée au registre** : ni STOP, ni rejet, ni vivier. C'est le seul des trois types qui franchit le seuil.
- Voisins présents au registre, **non doublons** (objets différents) : `papier peint panoramique sur mesure` (À APPROFONDIR phase 3, 40 500 exact) — famille voisine d'un éventuel UNIVERS « revêtement mural décoratif » ; `cimaise / packs d'accrochage` (candidat n°3) ; `panneau japonais` (STOP lot 30×30 — rideau, homonyme sans rapport) ; `verrière atelier` (STOP mesure express) ; `microciment / enduit décoratif` (poche non instruite, ≈ 1 900).

---

## 7. Limites

- **Intention non disponible** : `keyword_suggestions` et `search_volume/live` ne rendent pas d'intention de recherche exploitable ; l'écart commercial/informationnel a été fait sur le vocabulaire (comment, pose, fabriquer, diy…), pas sur un champ API.
- **Têtes à intention mixte** : `panneau acoustique` (22 200) recouvre mousse, bureau, isolation et déco bois dans un seul bucket ; `panneau mural` (18 100) et `lambris` (12 100) recouvrent PVC et bois. La part adressable de ces têtes ne peut pas se lire dans DataForSEO ; c'est le travail SERP de phase 3.
- **Deux clusters à moins de 5 % du seuil** : `panneau acoustique bois` 11 780 (−720) écarté, `panneau mural bois` tête 12 100 (−400) retenu grâce à ses buckets d'ordre des mots. La zone de décision est étroite — la nuance du 29/08 (dispersion tête à tête, ×0,62 à ×1,27 par famille) s'applique pleinement.
- **Regroupement par ordre des mots** : `kw_dfs.py` fusionne des formulations que Google sert parfois dans des buckets distincts (6 séries sous le groupe 14 800). Le MAX a protégé la tête ; les totaux de cluster ont été recalculés bucket par bucket à partir des séries live/labs. Les volumes « labs » n'ont pas tous été recontrôlés en live (les têtes et mots décisifs l'ont été ; les longues queues < 300 restent en lecture Labs).
- **Séries mensuelles** : les 12 mois rendus ne sont pas datés dans ce rapport (l'API rend année/mois ; les JSON du scratchpad les conservent). La baisse des deux derniers mois sur toutes les têtes (ex. panneau acoustique 12 100 vs 27 100) peut être saisonnière ou refléter un mois en cours incomplet — non tranché ici, à croiser avec Google Trends avant tout GO (PLAYBOOK).
- **Graines non passées** : « tasseaux bois mural » (contrôle de tête seulement, 110), « claustra » (têtes seulement, non balayé — 2 dérivées maximum atteintes), « papier peint », « moulure », « parement » (têtes seulement).
- **Aucune donnée** rendue par Google Ads pour : `panneau mural géométrique`, `panneau mural bois géométrique`, `panneau mural bois relief`, `panneau mural bois tête de lit`, `panneau acoustique bois tasseaux`, `panneau acoustique lattes bois`.
- **Coût** : le coût des 14 témoins internes de `kw_dfs.py` est déduit (≈ 1,26 USD), non rendu par le script.
- **Fichiers sources** archivés dans `analyses/2026-09-02-panneaux-muraux-bois/` : 7 paires `.md`/`.json` de graines (groupes dédupliqués avec variantes, séries et CPC), `tetes-1.json`, `tetes-2.json`, `temoin-avant.json`, `temoin-apres.json` (réponses `search_volume/live` horodatées, paramètres inclus). Les réponses brutes Labs sont dans le cache local `scripts/.cache_kw_dfs/` (non versionné).
- Ce rapport n'a **pas été commité** par l'agent (sous-agent d'une session orchestrée) ; le commit et le push relèvent de l'orchestrateur, sur `boutique-pipeline`.
