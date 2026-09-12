# Chasse aux clusters — Famille 8 « Traitement de l'air » — 12 septembre 2026

Agent : `phase0-decouverte`. Mode **PRODUIT PUR** (seuil DataForSEO de l'ordre de 12 500/mois, `PRODUCT-RESEARCH-CRITERIA.md` §1, relu ce jour). Tenant provisoire : `traitement-air`. Aucun candidat créé, aucun jugement de concurrence, aucun prix, aucun sourcing, aucun verdict marché.

Ce rapport rend des volumes France datés et leur composition. L'adressabilité SERP se tranche ailleurs.

Vocabulaire produit **attesté** par un mot-clé mesuré ce jour (ce ne sont **pas** des candidats) : `purificateur d'air` ; `vmc` / `ventilation mécanique contrôlée` ; `vmc double flux` ; `vmc simple flux` ; `vmc hygroréglable` ; `extracteur d'air`.

---

## 1. Entrée / périmètre et checkpoint

- **Famille traitée** : 8 — Traitement de l'air (`familles-exploration.md`, priorité haute, statut `à faire`, graines de départ inchangées).
- **Graines officielles** : `purificateur air`, `ventilation`, `qualité air intérieur`, `filtration air`.
- **Graines dérivées interrogées pendant le balayage** (justification en §5) : `vmc` (désambiguïsation de la graine `ventilation`, contaminée éclairage / anglais / médical) ; `extracteur d air` (tête live 18 100 absente comme tête de la graine officielle).
- **Date et plage des appels** : samedi 12 septembre 2026, 10:19:11 – 10:22:44 heure de Paris.
- **Source unique** : DataForSEO API. Chaque payload porte `location_name: France`, `language_name: French`. Contrôles live : `location_code` 2250, `language_code` fr. Aucune donnée d'un autre pays ni d'une autre langue.
- **Endpoints** :
  - découverte : `dataforseo_labs/google/keyword_suggestions/live` via `scripts/kw_dfs.py` (`--pages 1 --top 40 --json --refresh --sans-temoin`, correspondance plein texte, déduplication MAX du groupe) ;
  - contrôle de tête et témoins : `keywords_data/google_ads/search_volume/live`, `search_partners: false`.
- **Identifiants** : chargés depuis `ecommerce-dropshipping/.env`. Aucune valeur affichée ni copiée.
- **Seuil appliqué** : cluster PRODUIT PUR ≥ 12 500/mois. Aucun assouplissement.
- **Anti-doublon** : `registre-candidats.md` lu ce jour. Voir §6. Registre **non modifié**.
- **Checkpoint quantité / profondeur** (écrit avant la dernière mesure, respecté) :
  - 4 graines officielles, `--pages 1` (1 000 lignes max) ;
  - au plus 2 graines dérivées Labs, seulement si une graine officielle est contaminée ou si une tête live ≥ 12 500 n'a pas de composition Labs ;
  - 1 lot `search_volume/live` ≤ 60 mots ;
  - pas de page 2 ; pas de balayage de la famille 10 (humidité / climatisation) ; pas de SERP.

### Graines Labs

| Graine | Heure Paris | Lignes brutes | Idées dédupliquées | Suggestions annoncées | Coût annoncé (USD) | Statut |
|---|---|---:|---:|---:|---:|---|
| purificateur air | 10:19:32 | 1 000 | 788 | 1 425 | 0,132 | OK |
| ventilation | 10:19:34 | 1 000 | 615 | 16 508 | 0,132 | OK |
| qualité air intérieur | 10:19:35 | 123 | 59 (hors n/a) | 123 | non conservé (échec dédup `kw_dfs.py` sur un n/a) | API complète ; 36 n/a isolés, pas des 0 |
| filtration air | 10:19:35 | 128 | 83 (hors n/a) | 128 | non conservé (même motif) | API complète ; 28 n/a isolés |
| vmc *(dérivée)* | 10:21:13 | 1 000 | 404 | 21 031 | 0,132 | OK |
| extracteur d air *(dérivée)* | 10:22:24 | 735 | 553 (hors n/a) | 735 | non conservé (même motif) | API complète ; 102 n/a isolés |

Plancher de lecture : `purificateur air`, `ventilation` et `vmc` s'arrêtent à 1 000 lignes alors que l'API en annonce davantage. `qualité air intérieur`, `filtration air` et `extracteur d air` sont lues en entier (total_count = lignes).

### Contrôle de têtes `search_volume/live`

| Lot | Heure | Mots-clés demandés | Coût (USD) | Fichier |
|---|---|---:|---:|---|
| tetes-1 | 10:22:01 | 58 | 0,09 | `raw/tetes-1.json` |

Les 58 demandes ont toutes été rendues. Aucun n/a live.

### Témoins `tufting`

| Moment | Heure | Volume | CPC | Série 12 mois (récent → ancien tel que rendu) |
|---|---|---:|---:|---|
| avant première mesure | 10:19:11 | **12 100** | 1,45 | 8100 6600 6600 9900 9900 9900 9900 14800 14800 14800 9900 14800 |
| après dernière mesure | 10:22:44 | **12 100** | 1,45 | identique |

Non nuls, identiques entre eux, identiques au repère historique 12 100 du 29/08/2026. `location_code` 2250, `language_code` fr. Aucun zéro silencieux.

### Coût DataForSEO

Somme des `cost` présents dans les JSON d'API conservés **+** coûts annoncés par `kw_dfs.py` pour les trois passages OK :

- Labs `kw_dfs.py` OK : 0,132 × 3 = **0,396 USD**
- `search_volume/live` (2 témoins + 1 lot de têtes) : 0,09 × 3 = **0,270 USD**

**Coût observé dans les fichiers conservés : 0,666 USD.**

Limite de coût : les trois appels Labs dont la déduplication `kw_dfs.py` s'est arrêtée sur un volume `null` (`qualité air intérieur`, `filtration air`, `extracteur d air`) n'ont pas laissé de champ `cost` dans le cache. Rien n'est extrapolé.

### Convention de lecture

- « Volume » = `search_volume` mensuel France, dernier mois disponible tel que rendu.
- Un **bucket** = une série mensuelle distincte. Google pré-agrège des variantes proches ; deux formulations à série identique comptent une fois (MAX). Toute somme ci-dessous est une somme de buckets à séries distinctes, **jamais** une somme de reformulations du même bucket. **Aucun volume parent n'est attribué à un produit.**
- Volumes « labs » = suggestions DataForSEO Labs après dédup `kw_dfs.py` (MAX du groupe), n/a exclus. Volumes « live » = `search_volume/live`. Les têtes des clusters retenus sont toutes « live ».
- CPC : champ `cpc` DataForSEO. Aucun champ devise dans la réponse live (clés observées : `cpc` seulement). Non relabelisé en EUR.
- Bug observé de `kw_dfs.py` : la clé de regroupement fusionne `purificateur d air` (33 100) et `air purificateur` (170) sous le représentant `air purificateur` à 33 100 (`volume_min` 210). Le live infirme cette fusion. Les volumes de cluster ci-dessous viennent du live pour ces têtes.

Preuves : `analyses/2026-09-12-chasse-clusters-traitement-air/raw/`.

---

## 2. Clusters retenus (≥ 12 500/mois)

Aucun de ces volumes n'additionne des familles d'objets distinctes. Les types, enseignes et marques sont des niveaux ou des exclusions, pas des rallonges pour franchir le seuil. Chaque tête retenue le franchit **seule**.

### 2.1 Purificateur d'air — niveau objet

**Le seuil est franchi par la tête seule : `purificateur d air` / `purificateur d'air` = 33 100 (live, 1 bucket).**

| Mot-clé | Volume | CPC | Source | Note |
|---|---:|---:|---|---|
| purificateur d air | **33 100** | 0,60 | live | tête ; même série que `purificateur d'air` |
| purificateur d'air | 33 100 | 0,60 | live | même bucket → MAX, pas de second compte |

- **Volume total dédupliqué du cluster : 33 100/mois** (1 bucket). Aucune addition.
- **CPC** de la tête : 0,60.
- **Série** (12 mois, ordre API) : 27100 40500 49500 40500 33100 40500 33100 40500 33100 40500 33100 27100.
- **Niveaux de généralité testés (non additionnés)** :

| Mot-clé | Volume live | CPC | Rapport à la tête |
|---|---:|---:|---|
| purificateur | 1 000 | 0,85 | parent nu, sous le seuil |
| purificateur d air hepa | 1 300 | 0,73 | niveau filtre, sous le seuil |
| ioniseur d air | 1 600 | 0,61 | objet voisin, sous le seuil |
| ioniseur | 1 300 | 0,84 | sous le seuil |
| plantes purificateur d air | 720 | 0,17 | sous le seuil |
| purificateur d air ionique | 480 | 0,37 | sous le seuil |
| épurateur d air / épurateur d'air | 390 | 0,82 | synonyme registre ; bucket distinct, sous le seuil |
| air purificateur / purificateur air / épurateur air | 170 | 1,19 | **même série** ; ordre des mots, pas la tête |

- **Méthode de déduplication** : apostrophe `d air` / `d'air` = 1 série. `kw_dfs.py` avait collé cette tête avec `air purificateur` (170) ; le live sépare les objets.
- **Exclus de ce cluster** : marques (`purificateur d air dyson` 6 600, Philips 1 900, Xiaomi 1 000), combo humidificateur 320, filtre HEPA accessoire 210, enseignes labs (Ikea, Boulanger, Darty, Leroy Merlin, Amazon). Doublon registre : voir §6 — volume rendu, **pas une piste à requalifier**.

### 2.2 VMC — niveau catégorie / sigle

**Le seuil est franchi par la tête seule : `vmc` = 49 500 (live).** Même série que `ventilation mécanique contrôlée`.

| Mot-clé | Volume | CPC | Source | Note |
|---|---:|---:|---|---|
| vmc | **49 500** | 0,32 | live | tête |
| ventilation mécanique contrôlée | 49 500 | 0,32 | live | même bucket → MAX |

- **Volume total dédupliqué du cluster : 49 500/mois** (1 bucket). Aucune addition.
- **CPC** de la tête : 0,32.
- **Série** : 40500 40500 49500 49500 40500 49500 60500 74000 60500 74000 60500 60500.
- **Labs** : représentant `vmc` 60 500 — écart labs/live ; le live tranche.
- **Niveaux de généralité testés (non additionnés ici)** : double flux §2.3, simple flux §2.4, hygroréglable §2.5, `vmc salle de bains` 8 100, `bouche vmc` 5 400, `gaine vmc` 4 400.
- **Exclus** : enseignes (`leroy merlin vmc` 4 400 labs, `brico dépôt vmc` 1 900, `castorama ventilation` — série éclairage, §4), marques (`atlantic vmc` 5 400 labs, `aldès vmc` 4 400), pose/entretien/nettoyage, `vmi` 9 900 (objet distinct, sous le seuil).

### 2.3 VMC double flux — niveau spécifique

**Le seuil est franchi par la tête seule : `vmc double flux` = 33 100 (live).** Même série que `vmc double-flux` et `ventilation mécanique contrôlée double flux`. **Non sommé** avec §2.2.

| Mot-clé | Volume | CPC | Source | Note |
|---|---:|---:|---|---|
| vmc double flux | **33 100** | 0,57 | live | tête |
| vmc double-flux | 33 100 | 0,57 | live | même bucket |
| ventilation mécanique contrôlée double flux | 33 100 | 0,57 | live | même bucket |

- **Volume total dédupliqué : 33 100/mois** (1 bucket).
- **Série** : 22200 27100 33100 27100 27100 33100 33100 49500 40500 49500 40500 33100.
- **Non additionné** : `vmc double-flux thermodynamique` 1 900 labs, `prix vmc double flux` 3 600 labs, `installateur vmc double flux` 1 600 labs.

### 2.4 VMC simple flux — niveau spécifique

**Le seuil est franchi par la tête seule : `vmc simple flux` = 18 100 (live).** Même série que `ventilation mécanique contrôlée simple flux`. **Non sommé** avec §2.2 ni §2.3.

| Mot-clé | Volume | CPC | Source | Note |
|---|---:|---:|---|---|
| vmc simple flux | **18 100** | 0,23 | live | tête |
| ventilation mécanique contrôlée simple flux | 18 100 | 0,23 | live | même bucket |

- **Volume total dédupliqué : 18 100/mois** (1 bucket).
- **Série** : 14800 14800 18100 14800 14800 18100 22200 27100 22200 27100 22200 22200.
- **Hygroréglable n'est pas ce bucket** (série distincte, §2.5).

### 2.5 VMC hygroréglable — niveau spécifique

**Le seuil est franchi par la tête seule : `vmc hygroréglable` = 18 100 (live).** Même série que `vmc hygrométrique` et `ventilation mécanique contrôlée hygroréglable`. **Non sommé** avec le simple flux (séries différentes).

| Mot-clé | Volume | CPC | Source | Note |
|---|---:|---:|---|---|
| vmc hygroréglable | **18 100** | 0,33 | live | tête |
| vmc hygrométrique | 18 100 | 0,33 | live | même bucket |
| ventilation mécanique contrôlée hygroréglable | 18 100 | 0,33 | live | même bucket |

- **Volume total dédupliqué : 18 100/mois** (1 bucket).
- **Série** : 12100 12100 12100 14800 14800 18100 18100 22200 22200 27100 22200 18100.
- **Labs** : `vmc simple flux hygroréglables` 5 400 — niveau plus étroit, non sommé.

### 2.6 Extracteur d'air — niveau objet

**Le seuil est franchi par la tête seule : `extracteur d air` / `extracteur d'air` = 18 100 (live, 1 bucket).**

| Mot-clé | Volume | CPC | Source | Note |
|---|---:|---:|---|---|
| extracteur d air | **18 100** | 0,40 | live | tête |
| extracteur d'air | 18 100 | 0,40 | live | même bucket |

- **Volume total dédupliqué : 18 100/mois** (1 bucket). Aucune addition.
- **Série** : 18100 22200 27100 18100 14800 14800 18100 18100 18100 22200 18100 18100.
- **Niveaux (labs, non additionnés)** : `extracteur d air salle de bain` 4 400, `silencieux` 1 600, `hygroréglable` 1 300, `ventilateur extracteur d air` 1 000, `solaire` 1 000, `cuisine` 880.
- **Exclus** : enseignes (Leroy Merlin 590, Brico Dépôt 320, Castorama 210), industriel/pro 590, grow/Prima Klima (n/a), PC, bateau, étable.
- **Méthode** : graine officielle `ventilation` ne remontait que `ventilation extracteur d'air` 1 000 labs. Le live + la graine dérivée établissent la tête 18 100. Pas d'attribution du volume `ventilation` (9 900) à cet objet.

### Règle hiérarchique — récapitulatif (jamais sommé)

| Niveau | Mot-clé | Volume live | CPC | Statut seuil PUR 12 500 |
|---|---|---:|---:|---|
| Objet | purificateur d'air | 33 100 | 0,60 | ≥ seuil (tête seule) ; doublon registre §6 |
| Catégorie | vmc | 49 500 | 0,32 | ≥ seuil (tête seule) |
| Spécifique | vmc double flux | 33 100 | 0,57 | ≥ seuil (tête seule) |
| Spécifique | vmc simple flux | 18 100 | 0,23 | ≥ seuil (tête seule) |
| Spécifique | vmc hygroréglable | 18 100 | 0,33 | ≥ seuil (tête seule) |
| Objet | extracteur d'air | 18 100 | 0,40 | ≥ seuil (tête seule) |
| Parent | ventilation | 9 900 | 0,45 | < seuil ; intention mixte |
| Parent | purificateur | 1 000 | 0,85 | < seuil |
| Graine | qualité de l air intérieur | 480 | 1,44 | < seuil |
| Graine | filtration air | 70 | 2,28 | < seuil |
| Accessoire | bouche vmc | 5 400 | 0,21 | < seuil |
| Accessoire | gaine vmc | 4 400 | 0,31 | < seuil |
| Voisin fam. 10 | humidificateur d air | 33 100 | 0,31 | hors famille 8, non balayé |
| Voisin fam. 10 | déshumidificateur | 74 000 | 0,50 | hors famille 8, non balayé |
| Contamination | ventilation plafond | 246 000 | 0,41 | éclairage, §4 |
| Contamination | ventilation silencieuse | 49 500 | 0,25 | éclairage, §4 |

---

## 3. Clusters écartés (sous le seuil, ou tête sans composition retenue)

| Mot-clé | Volume live | Devenir |
|---|---:|---|
| vmi | 9 900 | sous le seuil ; objet distinct (insufflation) |
| ventilation | 9 900 | parent mixte, sous le seuil |
| vmc salle de bains | 8 100 | sous le seuil (niveau de §2.2) |
| humidificateur (nu) | 8 100 | sous le seuil ; le composé `humidificateur d air` 33 100 est famille 10 |
| atlantic climatisation ventilation | 8 100 | marque + famille 10 |
| bouche / bouches vmc | 5 400 | accessoire, sous le seuil |
| gaine / gaines vmc | 4 400 | accessoire, sous le seuil |
| ventilation vmi | 2 400 | sous le seuil |
| aérateur / aerateur | 1 900 | même série ; sous le seuil |
| ioniseur d air | 1 600 | sous le seuil |
| purificateur d air hepa | 1 300 | sous le seuil |
| ioniseur | 1 300 | sous le seuil |
| purificateur | 1 000 | sous le seuil |
| ventilation poêle à bois | 880 live / 12 100 labs | live tranche : sous le seuil ; écart labs/live |
| plantes purificateur d air | 720 | sous le seuil |
| qualité de l air intérieur | 480 | graine officielle entière sous le seuil |
| purificateur d air ionique | 480 | sous le seuil |
| épurateur d'air | 390 | sous le seuil |
| capteur qualité air intérieur | 70 | sous le seuil |
| qualité air intérieur (sans « de l ») | 70 | sous le seuil |
| filtration air / air filtration | 70 | même série ; graine officielle entière sous le seuil |
| détecteur qualité air intérieur | 50 | sous le seuil |
| local exhaust ventilation | 12 100 | anglais industriel, 400 sous le seuil |

La graine `qualité air intérieur` plafonne à 480 (live tête utile). La graine `filtration air` plafonne à 70. Rien n'est retenu de ces deux graines.

---

## 4. Mots-clés exclus / intentions nettoyées

| Mot-clé ou famille | Volume | Motif |
|---|---:|---|
| ventilation plafond | 246 000 live | **contamination éclairage** : série 450k–1 000k puis chute à 18–33k, parallèle à `plafonnier ventilation`. Pas de l'air traité. |
| plafonnier ventilation | 33 100 live | même famille d'intention (luminaire) |
| ventilation silencieuse | 49 500 live | même profil de série (301k puis 1 600–6 600) : pas rattaché à la VMC (série HVAC plate) |
| colonne ventilation | 27 100 live | même profil (135k puis 590–1 600) |
| castorama ventilation | 9 900 live | enseigne + série éclairage (60 500 puis 210) |
| closed crankcase ventilation | 40 500 live | anglais automobile (PCV), hors famille |
| local exhaust ventilation | 12 100 live | anglais industriel |
| heating ventilation and air conditioning | 6 600 labs | anglais HVAC générique |
| positive pressure ventilation / adaptive servo-ventilation / non invasive ventilation | 9 900–1 900 labs | médical / anglais |
| purificateur d air dyson / philips / xiaomi | 6 600 / 1 900 / 1 000 live | marque |
| ikea / boulanger / darty / amazon / leroy merlin purificateur | 590–260 labs | enseigne |
| atlantic / aldes (VMC) | 5 400–4 400 labs | marque |
| leroy merlin vmc / brico dépôt vmc | 4 400 / 1 900 labs | enseigne |
| entretien / nettoyage / installation / branchement / prix vmc | 3 600–1 300 labs | service / informationnel |
| n/a qualité air intérieur (36 termes : INRS, CEREMA, ANSES, ERP, EHPAD, COFRAC…) | n/a, **pas 0** | B2B / réglementaire / docs ; non traités comme zéros |
| n/a filtration air (28 termes : Jet AFS, Tarkov, hôpital, NBC…) | n/a | pro / jeu / marque |
| n/a extracteur (102 termes : grow, Prima Klima, ATEX, PC…) | n/a | hors particulier ou spec sheet |

Quand le rattachement à un objet unique n'était pas sûr, le mot a été exclu plutôt que collé. Les quatre têtes « ventilation + luminaire » dépassent le seuil **en volume** : elles sont écartées pour **intention**, pas pour volume.

---

## 5. Graines dérivées

Pour l'auto-expansion de la famille **avant** de passer à une autre. Ce ne sont **pas** des clusters constitués (sauf `vmc` et `extracteur d air`, déjà en §2).

| Graine | Origine | Tête live déjà mesurée | À faire en Labs |
|---|---|---:|---|
| vmc | contamination de `ventilation` (éclairage, anglais, médical) | 49 500 — **déjà balayée** ce jour | — |
| extracteur d air | composé 1 000 dans `ventilation` ; live 18 100 | 18 100 — **déjà balayée** | — |
| humidificateur d air | 15 idées / 520 cumulés sur `purificateur air` | 33 100 | **non** : famille 10 `Chauffage, climatisation & humidité` |
| déshumidificateur | 12 idées / 530 cumulés sur `purificateur air` | 74 000 | **non** : famille 10 |
| vmi | thème / voisin VMC | 9 900 | déjà sous le seuil en tête |
| ioniseur | niveau du purificateur | 1 300 / 1 600 | déjà sous le seuil |
| bouche vmc / gaine vmc | accessoires de §2.2 | 5 400 / 4 400 | déjà sous le seuil |
| aérateur | contrôle hiérarchique ventilation | 1 900 | déjà sous le seuil |
| capteur qualité air intérieur | thème de la graine qualité | 70 | déjà sous le seuil |

Ne pas transformer une tête isolée en cluster sans `kw_dfs.py` dédié : la leçon catio interdit d'attribuer le volume d'un parent à une longue traîne. Ne pas lancer la famille 10 depuis ces têtes sans brief.

---

## 6. Doublons registre

Écartés d'office comme **candidats**, même si une tête dépasse le seuil. Les volumes restent dans ce rapport comme faits de mesure, pas comme pistes à requalifier.

| Entrée registre | Statut | Recouvrement ce jour |
|---|---|---|
| Purificateur d'air (syn. purificateur air HEPA, épurateur d'air) | Rejet Hakim 02/08 — déjà testé / retours négatifs, malgré ≥ 35 k pertinent (SEMrush historique) | Tête live **33 100**. HEPA 1 300. Épurateur 390. **Non retenu comme piste.** Reprise uniquement si `reprise motivée` documentée. |
| Humidificateur d'air | Survivant volume SEMrush lot 2–3 (33,1 k, 22/08) | Live `humidificateur d air` **33 100**. Hors famille 8 (famille 10). Non balayé. |
| Déshumidificateur | Lot 1 22/08 (27,1 k SEMrush) + annexe UK 165 000 | Live **74 000**. Hors famille 8 (famille 10). Non balayé. |
| Outillage frigoriste | Vivier famille 1, poche non instruite | Absent des suggestions de ce jour. |

Aucun autre STOP / rejet du registre ne recouvre `vmc`, `vmc double flux`, `vmc simple flux`, `vmc hygroréglable` ou `extracteur d'air`.

---

## 7. Limites et coût réel

- **Témoins** `tufting` 12 100 avant et après, cohérents. CPC témoin 1,45 (était 1,62 le 05/09) ; le volume est le critère de cohérence.
- **Trois n/a Labs** ont arrêté `kw_dfs.py` avant écriture du markdown de coût. Les caches complets sont conservés ; les n/a sont listés, pas convertis en 0.
- **`kw_dfs.py` et l'ordre des mots** : fusion `purificateur d air` + `air purificateur`. Corrigée par le live.
- **Labs vs live** : `vmc` 60 500 labs / 49 500 live ; `ventilation plafond` 201 000 labs / 246 000 live ; `ventilation poêle à bois` 12 100 labs / 880 live. Le live tranche les têtes.
- **Pages Labs** : `--pages 1`. `ventilation` annonce 16 508 suggestions, `vmc` 21 031, `purificateur air` 1 425. La longue traîne au-delà de la première page n'est pas lue.
- **Famille 10** : têtes `humidificateur d air` 33 100 et `déshumidificateur` 74 000 vues en contrôle de tête seulement, pour ne pas les coller à la famille 8. Pas de graine Labs dédiée.
- **Intention / SERP / Trends / Shopping** : non faits (hors rôle). Les exclusions « éclairage » reposent sur la **série mensuelle**, pas sur une SERP.
- **Devise CPC** : champ absent. Non relabelisé en EUR.
- **Coût observé : 0,666 USD.** Coût des 3 Labs n/a non conservé.
- **Registre** : lu, non modifié.
- Aucun contact, panier, Shopify, Ads, Merchant Center, `GO_FINAL` / `WATCH_FINAL` / `NO_GO_FINAL`.

---

## Gate

- Rapport daté du 2026-09-12, sept sections présentes.
- DataForSEO uniquement, France / French, témoins `tufting` 12 100 avant et après, cohérents.
- Six clusters retenus, chacun avec mots-clés, volumes individuels, déduplication, tête seule ≥ 12 500. Aucune addition de familles.
- Exclusions motivées. Aucun candidat non attesté. Aucun verdict marché.
