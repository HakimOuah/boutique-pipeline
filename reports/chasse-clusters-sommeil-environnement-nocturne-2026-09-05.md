# Chasse aux clusters — Famille 9 « Sommeil & environnement nocturne » — 5 septembre 2026

Agent : `phase0-decouverte`. Mode **PRODUIT PUR** (seuil DataForSEO de l'ordre de 12 500/mois, `PRODUCT-RESEARCH-CRITERIA.md` §1, relu ce jour). Tenant provisoire : `sommeil-environnement-nocturne`. Aucun produit nommé, aucun jugement de concurrence, aucun prix, aucun sourcing, aucun verdict marché.

Ce rapport rend des volumes France datés et leur composition. L'adressabilité SERP se tranche ailleurs.

---

## 1. Entrée

- **Famille traitée** : 9 — Sommeil & environnement nocturne (`familles-exploration.md`, priorité haute, statut `à faire`, graines de départ inchangées).
- **Graines officielles** : `sommeil`, `matelas`, `bruit chambre`, `obscurité chambre`.
- **Graines dérivées interrogées pendant le balayage** (justification en §5) : `rideau occultant` (niveau « famille de produit » de la graine `obscurité chambre`, vide en Labs) ; `surmatelas` (désambiguïsation d'une fusion abusive de `kw_dfs.py`).
- **Date et plage des appels** : samedi 5 septembre 2026, 08:05:40 – 08:10:45 heure de Paris.
- **Source unique** : DataForSEO API. Chaque payload porte `location_name: France`, `language_name: French`. Contrôles live : `location_code` 2250, `language_code` fr. Aucune donnée d'un autre pays ni d'une autre langue.
- **Endpoints** :
  - découverte : `dataforseo_labs/google/keyword_suggestions/live` via `scripts/kw_dfs.py` (`--pages 1 --top 40 --json`, correspondance plein texte, déduplication MAX du groupe) ;
  - contrôle de tête : `keywords_data/google_ads/search_volume/live`, `search_partners: false`.
- **Identifiants** : chargés depuis `ecommerce-dropshipping/.env` par `set -a; source; set +a`. Aucune valeur affichée ni copiée.
- **Seuil appliqué** : cluster PRODUIT PUR ≥ 12 500/mois. Aucun assouplissement.
- **Anti-doublon** : `registre-candidats.md` lu ce jour (dernière mise à jour 4 septembre 2026). Voir §6.

### Graines Labs

| Graine | Heure (approx.) | Lignes brutes | Idées dédupliquées | Suggestions annoncées | Coût annoncé (USD) | Statut |
|---|---|---:|---:|---:|---:|---|
| sommeil | 08:05 | 1 000 | 379 | 48 305 | 0,132 | OK |
| matelas | 08:05 | 1 000 | 282 | 111 698 | 0,132 | OK |
| bruit chambre | 08:05 | 87 | 54 | 87 | 0,022 | OK |
| obscurité chambre | 08:05 puis 08:06 `--refresh` puis dump 08:06:46 | — | — | `total_count` None, `items` None, `items_count` 0, `seed_keyword_data` vide | 0,012 (dump conservé) | API `20000 Ok.` sans suggestions — pas un zéro inventé |
| obscurite chambre *(diagnostic orthographe)* | 08:06:46 | idem | — | idem | 0,012 | même constat |
| obscurité *(diagnostic parent, pas graine officielle)* | 08:06:47 | 367 | — | 367 | 0,05604 | vocabulaire hors chambre (synonymes, mots fléchés, Pokémon) |
| rideau occultant *(dérivée)* | 08:09 | 1 000 | 620 | 3 274 | 0,132 | OK |
| surmatelas *(dérivée)* | 08:09 | 1 000 | 539 | 6 319 | 0,132 | OK |

### Contrôle de têtes `search_volume/live`

| Lot | Heure | Mots-clés demandés | Coût (USD) | Fichier |
|---|---|---:|---:|---|
| tetes-1 | 08:08:36 | 58 | 0,09 | `raw/tetes-1.json` |

Deux têtes demandées non rendues (n/a, **pas 0**) : `matelas bébé`, `oreiller apnée du sommeil`.

### Témoins `tufting`

| Moment | Heure | Volume | CPC | Série 12 mois (récent → ancien tel que rendu) |
|---|---|---:|---:|---|
| avant première mesure | 08:05:40 | **12 100** | 1,62 | 6600 6600 9900 9900 9900 9900 14800 14800 14800 9900 14800 8100 |
| après dernière mesure | 08:10:45 | **12 100** | 1,62 | identique |

Non nuls, identiques entre eux, identiques au repère historique 12 100 du 29/08/2026. `location_code` 2250, `language_code` fr. Aucun zéro silencieux.

### Coût DataForSEO

Somme des `cost` présents dans les JSON d'API conservés **+** coûts annoncés par `kw_dfs.py` pour les cinq passages OK :

- Labs `kw_dfs.py` : 0,132 × 4 + 0,022 = **0,550 USD**
- `search_volume/live` (2 témoins + 1 lot de têtes) : 0,09 × 3 = **0,270 USD**
- dumps Labs de diagnostic : 0,012 + 0,012 + 0,05604 = **0,08004 USD**

**Coût observé dans les fichiers conservés : 0,90004 USD.**

Limite de coût : les deux premiers appels `kw_dfs.py` sur `obscurité chambre` (échec `items` None) n'ont pas laissé de JSON de coût ; le dump ultérieur du même endpoint est à 0,012 USD. Rien n'est extrapolé au-delà.

### Convention de lecture

- « Volume » = `search_volume` mensuel France, dernier mois disponible tel que rendu.
- Un **bucket** = une série mensuelle distincte. Google pré-agrège des variantes proches ; deux formulations à série identique comptent une fois (MAX). Toute somme ci-dessous est une somme de buckets à séries distinctes, **jamais** une somme de reformulations du même bucket.
- Volumes « labs » = suggestions DataForSEO Labs après dédup `kw_dfs.py` (MAX du groupe). Volumes « live » = `search_volume/live`. Les têtes des clusters retenus sont toutes « live ».
- CPC : champ `cpc` DataForSEO, **devise non fournie** par l'endpoint (convention interne : ne pas relabeliser en EUR).
- Bug observé de `kw_dfs.py` : le mot vide `sur` fait fusionner `matelas` et `sur-matelas` sous le représentant `sur-matelas` à 90 500. Le live infirme cette fusion (`matelas` 90 500 ≠ `sur-matelas` 14 800). Les volumes de cluster ci-dessous viennent du live pour ces têtes.

Preuves : `analyses/2026-09-05-chasse-clusters-sommeil-environnement-nocturne/raw/`.

---

## 2. Clusters retenus (≥ 12 500/mois)

Aucun de ces volumes n'additionne des familles d'objets distinctes. Les tailles, enseignes et marques sont des niveaux ou des exclusions, pas des rallonges pour franchir le seuil. Chaque tête retenue le franchit **seule**.

### 2.1 Matelas — niveau objet / catégorie parente literie

**Le seuil est franchi par la tête seule : `matelas` = 90 500 (live).**

| Mot-clé | Volume | CPC | Source | Note |
|---|---:|---:|---|---|
| matelas | **90 500** | 4,84 | live | tête ; série 90500 74000 74000 74000 74000 74000 110000 90500 110000 90500 90500 90500 |

- **Volume total dédupliqué du cluster : 90 500/mois** (1 bucket). Aucune addition.
- **CPC** de la tête : 4,84.
- **Niveaux de généralité testés (non additionnés)** :

| Mot-clé | Volume live | CPC | Rapport à la tête |
|---|---:|---:|---|
| matelas 140x190 | 74 000 | 1,77 | série proche de la tête (pas identique : 8e mois 74 000 vs 90 500) — niveau taille, non sommé |
| matelas 160x200 | 60 500 | 3,41 | série distincte — niveau taille, non sommé |
| 90x190 matelas | 40 500 | 1,01 | niveau taille, non sommé |
| 140x200 matelas | 18 100 | 1,83 | niveau taille, non sommé |
| 180x200 matelas | 18 100 | 3,99 | niveau taille, non sommé |
| 90x200 matelas | 14 800 | 1,40 | niveau taille, non sommé |
| matelas mémoire de forme | 8 100 | 3,34 | sous-seuil, niveau matière/technologie |
| matelas latex | 5 400 | 3,12 | sous-seuil |

- **Méthode de déduplication** : tête live unique. Les tailles ne sont pas fusionnées avec la tête (séries non identiques) et **ne sont pas sommées** avec elle. `kw_dfs.py` avait collé `matelas` avec `sur-matelas` ; le live sépare les objets (voir 2.2).
- **Exclus de ce cluster** : marques (`emma matelas` 201 000), enseignes (`matelas ikea` 14 800), `matelas gonflable` (objet distinct, 2.4), `protège-matelas` (objet distinct, 2.5), `matelas à langer` (objet puériculture), nettoyage / punaises, sommier (tête isolée, §5).

### 2.2 Surmatelas / sur-matelas — même objet, deux buckets Google

Google n'a **pas** fusionné la graphie collée et la graphie à trait d'union (séries différentes). Ce n'est pas une addition de familles distinctes : c'est le même objet « surmatelas ».

| Mot-clé | Volume | CPC | Source | Série (12 mois, ordre API) |
|---|---:|---:|---|---|
| surmatelas | **33 100** | 1,28 | live | 27100 22200 27100 27100 27100 27100 40500 33100 40500 33100 33100 40500 |
| sur-matelas | **14 800** | 1,11 | live | 12100 9900 12100 12100 14800 14800 18100 14800 18100 18100 18100 18100 |
| sur matelas | 14 800 | 1,11 | live | **identique** à `sur-matelas` → MAX, pas de second compte |

- **Volume total dédupliqué : 47 900/mois** (33 100 + 14 800). Tête collée seule : 33 100, déjà au-dessus du seuil. Tête à trait d'union seule : 14 800, déjà au-dessus du seuil.
- **CPC** : 1,28 (collée) / 1,11 (trait d'union).
- **Niveaux de généralité testés (non additionnés au 47 900)** :

| Mot-clé | Volume | Source |
|---|---:|---|
| surmatelas 140x190 | 22 200 | labs |
| surmatelas 160x200 | 14 800 | labs |
| surconfort de matelas 160x200 | 14 800 | live ; série distincte de `sur-matelas` |
| surmatelas à mémoire de forme | 3 600 | labs |
| surmatelas rafraîchissant | 4 400 | labs / live `matelas rafraichissant` 4 400 |
| surmatelas chauffante | 3 600 | labs |
| surmatelas climatisé | 590 | labs |
| surmatelas thermorégulé | 50 | labs |

- **Méthode de déduplication** : `sur matelas` = même série que `sur-matelas` → 1 bucket. `surmatelas` ≠ cette série → 2e bucket. Somme des deux buckets seulement. Tailles et variantes thermiques **non sommées**.
- **Exclus** : enseignes (`ikéa surmatelas` 8 100, Decathlon 5 400, BUT, Conforama), `surmatelas lit parapluie` 9 900 (objet puériculture/voyage), marques (Emma, Tempur, Sofitel). Le STOP registre « surmatelas thermorégulé actif à eau » porte sur une **variante** à 50–4 400, pas sur le cluster entier.

### 2.3 Rideau occultant — niveau famille de produit de la graine « obscurité chambre »

La graine officielle `obscurité chambre` n'a produit **aucune** suggestion Labs (`20000 Ok.`, `items_count` 0) et vaut **10**/mois en live. Le protocole impose de tester plusieurs niveaux : formulation spécifique → famille de produit → parent. Niveau famille de produit, live :

| Mot-clé | Volume | CPC | Source | Note |
|---|---:|---:|---|---|
| rideau occultant | **49 500** | 0,72 | live | tête ; série identique à `rideaux occultants` |
| rideaux occultants | 49 500 | 0,72 | live | même bucket → MAX |
| rideau occultant thermique | 22 200 | — | labs | niveau variante, **non sommé** |

- **Volume total dédupliqué du cluster : 49 500/mois** (1 bucket de tête). Le seuil est franchi par la tête seule.
- **CPC** de la tête : 0,72.
- **Niveaux de généralité testés (non additionnés)** :

| Mot-clé | Volume | Source | Devenir |
|---|---:|---|---|
| obscurité chambre | 10 | live | formulation officielle de la graine — sous le seuil |
| obscurité | 1 000 | live | parent lexical hors chambre (voir dump) |
| occultant | 8 100 | live | parent trop large, sous le seuil cluster |
| store occultant | 12 100 | live | objet distinct (store), sous 12 500 — §3 |
| rideau occultant chambre | 390 | live | longue traîne |
| rideau occultant velux | 2 400 | labs | usage toiture |
| rideau occultant sans percer | 590 | labs | pose |
| rideau enrouleur occultant | 720 | labs | format |
| rideau occultant motorisé | 30 | labs | doublon registre, §6 |
| volet occultant | 480 | live | objet distinct |

- **Méthode de déduplication** : singulier/pluriel live à série identique → MAX 49 500. Variante thermique labs non additionnée (famille proche, pas un second objet, et le seuil n'en a pas besoin).
- **Exclus** : enseignes (`leroy merlin rideau occultant` 4 400, `ikéa` 4 400, Gifi 2 400, Centrakor 1 600, Action 1 600, Castorama 720, La Redoute 880, Amazon 1 300).

### 2.4 Matelas gonflable — objet distinct du matelas de literie

Apparu dans la graine `matelas` (thème co-occurrent `gonflable`, 19 idées). Ce n'est **pas** le même objet que 2.1 (camping / piscine / 1–2 personnes vs literie chambre). Cluster séparé, non additionné à 2.1.

| Mot-clé | Volume | CPC | Source | Note |
|---|---:|---:|---|---|
| matelas gonflable | **49 500** | 0,52 | live | série identique à `matelas gonflables` |
| matelas gonflables | 49 500 | 0,52 | live | même bucket → MAX |

- **Volume total dédupliqué : 49 500/mois**. Tête seule au-dessus du seuil.
- **Niveaux labs (non additionnés)** : `matelas gonflables 2 personnes` 18 100 ; `matelas gonflable 1 personnes` 12 100 ; `matelas gonflables décathlon` 18 100 (enseigne) ; `matelas gonflable.piscine` 6 600 ; `matelas gonflable.action` 6 600 ; `matelas autogonflants` 4 400.
- **Méthode de déduplication** : singulier/pluriel live, série identique → MAX.
- Contamination lisible : Decathlon, Leclerc, Action, Gifi, piscine, camping. Non comptée.

### 2.5 Protège-matelas — objet distinct (housse de protection)

| Mot-clé | Volume | CPC | Source | Note |
|---|---:|---:|---|---|
| protège-matelas | **14 800** | 1,14 | live | série identique à `protege matelas` |
| protege matelas | 14 800 | 1,14 | live | même bucket → MAX |

- **Volume total dédupliqué : 14 800/mois**. Tête seule au-dessus du seuil.
- **Niveaux (non additionnés)** : `protège-matelas 160x200` 4 400 labs ; `alèse matelas` 6 600 live (objet voisin, sous le seuil, non sommé) ; `housse de matelas` 4 400 live (objet voisin).
- **Méthode de déduplication** : accent/espace, série identique → MAX.

---

## 3. Clusters écartés (sous le seuil, ou tête isolée sans composition Labs)

Aucun écart silencieux. Volumes live sauf mention labs.

| Poche | Volume | Motif d'écart |
|---|---:|---|
| store occultant | 12 100 | sous 12 500 ; objet distinct du rideau |
| matelas à langer | 12 100 | sous le seuil ; objet puériculture, pas literie adulte |
| matelas pliable | 9 900 | sous le seuil |
| occultant (parent) | 8 100 | sous le seuil ; trop large |
| matelas mémoire de forme | 8 100 | sous le seuil (niveau de 2.1) |
| alèse matelas | 6 600 | sous le seuil |
| gummies sommeil | 5 400 | sous le seuil ; complément, allégation |
| matelas latex | 5 400 | sous le seuil |
| matelas de sol | 5 400 | sous le seuil |
| matelas rafraichissant | 4 400 | sous le seuil ; voisin du STOP thermorégulé |
| housse de matelas | 4 400 | sous le seuil |
| boules quies sommeil | 3 600 | sous le seuil (forme « sommeil » de la graine) |
| masque de sommeil | 2 900 | sous le seuil ; bucket distinct de `masque sommeil` 1 900 |
| masque sommeil / masques sommeil | 1 900 | même série ; sous le seuil |
| obscurité | 1 000 | parent lexical hors chambre |
| bouchons oreilles sommeil | 1 000 | sous le seuil |
| machine à bruit blanc | 880 | sous le seuil |
| casque anti-bruit sommeil | 720 | sous le seuil |
| machine bruit blanc | 390 | sous le seuil ; série distincte de « machine à bruit blanc » |
| rideau occultant chambre | 390 | sous le seuil |
| volet occultant | 480 | sous le seuil |
| mousse anti-bruit chambre | 140 | sous le seuil ; tête de la graine `bruit chambre` |
| isolation bruit chambre | 110 | sous le seuil |
| bruit chambre | 10 | graine officielle ; série plate à 10 |
| obscurité chambre | 10 | graine officielle ; Labs vide |

La graine `bruit chambre` tout entière plafonne à 140 (labs) / 140 (live tête utile). Rien n'est retenu de cette graine.

---

## 4. Mots-clés exclus des clusters

| Mot-clé ou famille | Volume | Motif |
|---|---:|---|
| emma matelas | 201 000 live | marque |
| apnée du sommeil / apnées sommeil | 60 500 live / 60 500 labs | médical, informationnel, appareillage |
| paralysie sommeil | 33 100 labs | informationnel / médical |
| sommeil (tête) | 27 100 live | parent informationnel (cycles, calculatrices, cliniques) — pas un objet |
| cycle de sommeil / sommeil paradoxal | 14 800 labs | informationnel |
| zzzquil sommeil | 12 100 labs | marque complément |
| symptômes apnée / machine apnée / masque apnée | 12 100 / 9 900 / 9 900 labs | médical |
| cbd sommeil hollyweed | 9 900 labs | marque / allégation |
| halle au sommeil / hall du sommeil | 8 100 / 1 900 labs | enseigne / lieu |
| oreillers apnée du sommeil | 8 100 labs | médical ; live `oreiller apnée du sommeil` = n/a |
| calculatrice sommeil | 8 100 labs | informationnel |
| pediakids / arkorelax / calmosine / mélatonine / homéopathie / fleurs de bach | 6 600 à 1 900 labs | complément / allégation |
| médecin / clinique / centre / spécialiste sommeil | 6 600–2 900 labs | service |
| matelas ikea / ikea matelas 140x190 / but / conforama / leclerc / decathlon (matelas) | 14 800 et sous | enseigne |
| traces punaises de lit matelas | 12 100 labs | nuisible / informationnel, pas l'objet literie |
| matelas nettoyage | 6 600 labs | service / entretien |
| roi matelas / bultex / epeda / tempur / hypnia / tediber / simmons / percko | 12 100–5 400 labs | marque |
| leroy merlin / ikea / gifi / centrakor / action / castorama rideau occultant | 4 400–720 labs | enseigne |
| rideau occultant motorisé | 30 labs | doublon registre (§6) |
| casque anti-bruit (sans « sommeil ») | 33 100 live | tête isolée ; contamination probable chantier/tir — pas rattachée à `bruit chambre` |
| dump `obscurité` (synonyme, mots fléchés, Pokémon, citations) | ≤ 1 000 | hors famille chambre |

Quand le rattachement à un objet unique n'était pas sûr, le mot a été exclu plutôt que collé.

---

## 5. Graines dérivées

Pour l'auto-expansion de la famille **avant** de passer à une autre. Ce ne sont **pas** des clusters constitués (sauf `rideau occultant` et `surmatelas`, déjà en §2).

Justifiées par le balayage de ce jour :

| Graine | Origine | Tête live déjà mesurée | À faire en Labs |
|---|---|---:|---|
| rideau occultant | niveau produit de `obscurité chambre` (Labs vide) | 49 500 — **déjà balayée** ce jour | — |
| surmatelas | fusion `sur` cassée + thème graine matelas | 33 100 / 14 800 — **déjà balayée** | — |
| store occultant | thème / niveau voisin du rideau | 12 100 | composition Labs si reprise |
| oreiller | 6 idées sur la graine `sommeil` (surtout apnée) | 49 500 | oui — cluster non constitué |
| oreiller mémoire de forme | niveau du parent oreiller | 27 100 | oui |
| sommier | thème co-occurrent graine `matelas` (11 idées) | 33 100 | oui |
| couverture lestée | contrôle hiérarchique sommeil / confort ; **absente** des suggestions des 4 graines | 33 100 | oui, si l'auto-expansion l'accepte malgré l'absence Labs amont |
| boules quies | forme « sommeil » 3 600 dans la graine | 33 100 (parent) | oui ; parent vs « sommeil » à séparer |
| bouchons d'oreille | forme « sommeil » 1 000 | 22 200 (parent) | oui |
| bruit blanc | contrôle hiérarchique de `bruit chambre` (graine stérile) ; **absent** des 4 graines | 22 200 | oui ; `machine à bruit blanc` 880 ne porte pas le parent |
| masque de sommeil | 2 900 dans la graine `sommeil` | 2 900 | déjà sous le seuil en tête |

Ne pas transformer ces têtes isolées en clusters sans un passage `kw_dfs.py` dédié : la leçon catio interdit d'attribuer le volume d'un parent à une longue traîne.

---

## 6. Doublons registre

Écartés d'office comme **candidats**, même si une tête dépasse le seuil. Les volumes restent dans ce rapport comme faits de mesure, pas comme pistes à requalifier.

| Entrée registre | Statut | Recouvrement ce jour |
|---|---|---|
| Futon (japonais, matelas, lit) | Rejet phase 2 (02/08) | `futon` = 27 100 live ; `futons matelas` = 3 600 labs. **Non retenu.** Reprise uniquement si `reprise motivée` documentée. |
| A3 — Oreiller / coussin de corps, body pillow | `STOP_PREQUALIFICATION` | Le STOP ne s'étend pas aux oreillers de tête. La tête `oreiller` 49 500 n'est **pas** un cluster constitué ici. Ne pas relancer le body pillow. |
| Surmatelas thermorégulé actif à eau | STOP (≈ 1 170, 16–17/07) | Variantes labs `surmatelas rafraîchissant` 4 400, `climatisé` 590, `thermorégulé` 50. **Ne ferme pas** le cluster surmatelas générique §2.2. |
| Film PDLC opacifiant électrique | STOP | Aucun mot PDLC / smart film dans les graines de ce jour. |
| Rideau/rouleau occultant motorisé simple | trop accessible (table historique) | `rideau occultant motorisé` = 30 labs. Hors cluster §2.3. |
| C5 — Bracelet réveil vibrant | `STOP_PREQUALIFICATION` | Absent des suggestions. Ne pas assimiler aux simulateurs d'aube. |
| Réveil simulateur d'aube / réveil lumière | STOP mesure express lot 1 | Absent des suggestions des graines. |
| U1 Literie parure / housse de couette | famille séparée, à faire | Non balayée ici. Ne pas fusionner avec la famille 9. |

Le dossier rideaux (rejeu 29/08, leçon `rideau occultant` 33 100 SEMrush vs `rideau occultant total` 30) n'est pas une ligne STOP produit ; la mesure live de ce jour sur `rideau occultant` est 49 500 DataForSEO. Ce n'est pas un verdict, c'est un écart d'outil/date.

---

## 7. Limites

- **Graine `obscurité chambre`** : deux appels `kw_dfs.py` + un dump Labs, tous `status_code` 20000, `items` None, `seed_keyword_data` vide. Ce n'est pas un volume 0 inventé. Le live donne 10/mois. Le cluster occultation repose sur le niveau « famille de produit » `rideau occultant`, déclaré comme dérivée.
- **Graine `bruit chambre`** : 87 suggestions, plafond 140. Le vocabulaire réel du bruit de nuit (`bruit blanc`, `boules quies`, `bouchons d'oreille`) n'est **pas** dans cette graine. Têtes isolées en §5, pas des clusters.
- **`kw_dfs.py` et le mot vide `sur`** : fusion `matelas` + `sur-matelas`. Corrigée par le live. Les tableaux §2 ne reprennent pas le représentant labs 90 500 pour le surmatelas.
- **Têtes isolées ≥ 12 500 sans composition Labs** (`oreiller` 49 500, `sommier` 33 100, `couverture lestée` 33 100, `boules quies` 33 100, `casque anti-bruit` 33 100, `bouchons d'oreille` 22 200, `bruit blanc` 22 200, `oreiller mémoire de forme` 27 100) : non promues en clusters retenus. Une promotion silencieuse serait invérifiable.
- **Deux n/a live** : `matelas bébé`, `oreiller apnée du sommeil`. Non traités comme zéros.
- **Devise CPC** : champ absent. Non relabelisé en EUR.
- **Pages Labs** : `--pages 1` (1 000 lignes). `sommeil` annonce 48 305 suggestions, `matelas` 111 698, `rideau occultant` 3 274, `surmatelas` 6 319. La longue traîne au-delà de la première page n'est pas lue.
- **Intention / SERP / Trends / Shopping** : non faits (hors rôle).
- **Coût des deux `kw_dfs.py` en échec** sur `obscurité chambre` : non conservé.
- **Registre** : lu, non modifié.
- Aucun contact, panier, Shopify, Ads, Merchant Center, `GO_FINAL` / `WATCH_FINAL` / `NO_GO_FINAL`.

---

## Gate

- Rapport daté du 2026-09-05, sept sections présentes.
- DataForSEO uniquement, France / French, témoins `tufting` 12 100 avant et après, cohérents.
- Cinq clusters retenus, chacun avec mots-clés, volumes individuels, déduplication, tête seule ≥ 12 500.
- Exclusions motivées. Aucun produit nommé. Aucun verdict marché.
