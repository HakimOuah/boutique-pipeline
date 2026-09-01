# PHASE 3 — DEMANDE PRODUIT PUR Q4 — 2026-09-01

Mode : **PRODUIT PUR**  
Marché : **France / français**  
Seuil canonique : **12 500 recherches mensuelles pertinentes**  
Bande de cas limite : **10 000 à 15 000**  
Brief : produit Q4 facilement offrable, à forte valeur perçue et pertinent toute l’année.  
Source unique de volume et de gate : **DataForSEO**.

## 1. Entrée et méthode

### Fichiers lus

- `PRODUCT-RESEARCH-CRITERIA.md` ;
- `PRODUCT-RESEARCH-PLAYBOOK.md` ;
- `registre-candidats.md` — lu, non modifié ;
- `reports/phase2-filtre-produit-pur-q4-2026-09-01.md`.

### Candidats, périmètre et racines Labs

1. Sac de voyage à compression sous vide intégrée, formats cabine/sac à dos regroupés : `sac compression sous vide`, `sac de voyage compression`.
2. Plaque d’acier de cuisson pain/pizza : `plaque acier cuisson`, `baking steel`.
3. Kit premium de boulangerie au levain : `kit pain levain`, `kit boulangerie`.
4. Remontoir pour montre automatique : `remontoir montre automatique`, `boite remontoir montre`.

Huit graines neuves ont été tirées, soit deux par candidat et moins que le plafond de douze. La découverte utilise `dataforseo_labs/google/keyword_suggestions/live`, `location_name: France`, `language_name: French`, une page par racine. Les têtes et parents décisifs ont été contrôlés en lots avec `keywords_data/google_ads/search_volume/live`, France/français, `search_partners: false`.

### Déduplication et limites du calcul

- Une même idée normalisée n’est comptée qu’une fois ; les variantes proches utilisent le maximum du groupe, jamais leur somme.
- Les deux corpus d’un candidat sont réunis par clé normalisée, avec `MAX` en cas de recoupement.
- Une formulation particulière, le produit fini et le parent restent à des niveaux séparés.
- Les parents ne sont retenus que si la même page peut les servir et si l’intention observée correspond au produit. Aucun volume parent n’est attribué automatiquement au produit spécifique.
- Les marques/enseignes tierces, services, occasion, pièces, accessoires séparés, informationnel non acheteur et familles techniques différentes sont retirés.
- Le volume pertinent est une estimation conservatrice ; les listes complètes sont dans `labs-clusters.json`, et les décisions de rétention dans `cluster-decisions.json`.

## 2. Fiabilité DataForSEO, témoins et coût

### Témoins

- Premier témoin avant toute racine Labs : `tufting = 12 100`.
- Témoin après la passe Labs : `tufting = 12 100`.
- Contrôle groupé des têtes : témoin avant/après `12 100 / 12 100`.
- Contrôle exact des variantes décisives : témoin avant/après `12 100 / 12 100`.

Les témoins sont non nuls et cohérents. Aucun repli de volume vers une autre base n’a été utilisé.

### Coût

- Coût attendu annoncé au brief : environ **0,13 USD par graine Labs**, plus environ **0,09 USD** pour un contrôle groupé, plafond d’arrêt ≈ **1,65 USD**.
- Coût réel Labs lu dans les réponses : **0,165 USD** pour huit racines.
- Premier contrôle groupé, témoins inclus : **0,270 USD**.
- Contrôle exact complémentaire, témoins inclus : **0,270 USD**.
- **Coût réel total : 0,705 USD**, sous le plafond.

### CPC et devise

Les réponses DataForSEO exposent bien le champ numérique `cpc`, mais **aucun champ de devise** n’est présent dans les lignes retournées (`keyword`, `location_code`, `language_code`, `competition`, `cpc`, enchères et séries mensuelles seulement). Il serait interdit de présumer EUR ou USD. Le tableau note donc chaque CPC comme « valeur lue, devise non fournie par l’endpoint ». Le coût API, lui, est explicitement reporté en USD.

## 3. Tableau de décision

| Candidat | Volume brut dédupliqué | Volume pertinent estimé | CPC tête | Série mensuelle / saisonnalité | Publicité et intention | Prix visibles | Orientation gate volume | Statut formel |
|---|---:|---:|---|---|---|---|---|---|
| Sac de voyage à compression intégrée | 7 510 | **1 890** | 0,50, devise non fournie (Labs) ; variante live 0,35, devise non fournie | Besoin voyage visible toute l’année ; les séries DataForSEO suggèrent une activité été et Q4. Google Trends 5 ans indisponible. | `HIGH` dans DataForSEO. Offres produit organiques visibles. Annonces Search texte et carrousel Shopping non confirmés. | 19,95–189,90 € sur 4 repères comparables/adjacents | STOP : très sous 12 500 | **CAS LIMITE — décision Hakim requise**, car Google réel/Trends incomplets |
| Plaque d’acier pain/pizza | 790 | **150** | 0,18, devise non fournie | Série DataForSEO disponible, mais Google Trends 5 ans indisponible ; continuité annuelle non validée par Trends. | `HIGH`. Intention commerciale nette sur `baking steel`, mais parent `plaque pizza` contaminé. Ads texte/Shopping non confirmés. | 27,90–153,95 € ; cœur acier massif observé 48,90–99 € et 92 € | STOP : très sous 12 500 | **CAS LIMITE — décision Hakim requise**, outil Google partiel |
| Kit premium boulangerie au levain | 190 | **130** | 0,19, devise non fournie | Les mots produit sont faibles ; Trends 5 ans indisponible. Le parent `levain` ne peut pas servir de proxy saisonnier au kit. | `HIGH` sur le kit, mais volume minime. Résultats produit spécifiques visibles ; parent `levain` informationnel. Ads texte/Shopping non confirmés. | 24,95–77 € ; majorité des offres visibles sous 50 € | STOP : très sous 12 500 | **CAS LIMITE — décision Hakim requise**, outil Google partiel |
| Remontoir montre automatique | 8 980, parent contrôlé inclus | **7 000** | 1,49, devise non fournie | Série DataForSEO continue avec forte bosse nov.–déc. 2025 (9 900–12 100 sur la tête contre 3 600–5 400 plusieurs autres mois). Trends 5 ans indisponible. | `HIGH`, intention commerciale forte et spécialistes nombreux. Ads texte/Shopping non confirmés. | 99–2 415 € ; spécialistes comparables visibles 99–290 € | STOP : sous 10 000 et sous 12 500 | **CAS LIMITE — décision Hakim requise**, outil Google partiel |

Aucun candidat n’atteint la bande volumique 10 000–15 000. Les statuts formels `CAS LIMITE` viennent uniquement de l’incomplétude obligatoire SERP/Shopping/Trends, pas d’une proximité avec le seuil.

## 4. Détail par candidat

### 4.1 Sac de voyage à compression sous vide intégrée

#### Niveaux testés

| Niveau | Formulation | Volume DataForSEO | Traitement |
|---|---|---:|---|
| Spécifique | `sac a dos compression sous vide` | 1 300 dans Labs ; `n/a` au contrôle live exact | Retenu avec réserve ; `n/a` n’est pas 0 |
| Spécifique, autre écriture | `sac à dos à compression sous vide` | 110 live | Retenu dans le groupe spécifique, sans addition avec le 1 300 |
| Produit fini/format | `sac cabine compression sous vide` | 210 Labs ; `n/a` live exact | Retenu |
| Produit fini/format | `sac de voyage compression sous vide` | 170 Labs ; `n/a` live exact | Retenu |
| Parent | `sac à dos voyage` | 2 400 live | Retiré : bagagerie générique, part intégrée non démontrée |
| Parent | `sac de voyage` | 40 500 live | Retiré : SERP organique de sacs de voyage génériques, matières et marques variées |

Le groupe Labs `sac de voyage à compression` à 1 900 résulte d’une normalisation qui rapproche `sac de compression voyage` et `sac de voyage à compression`. L’ordre des mots change ici le produit : housse de compression séparée versus bagage intégrant la compression. Le 1 900 n’est donc pas attribué au bagage intégré.

#### Mots retenus

- `sac a dos compression sous vide` : 1 300 ;
- format cabine : 210, une seule fois malgré deux formulations proches ;
- `sac de voyage compression sous vide` : 170 ;
- `40x30x20` : 110 ;
- `avec pompe` : 50 ;
- formulation sac à dos de voyage : 30 ;
- dimensions/antivol intégrés : 20.

Estimation pertinente : **1 890/mois**. Elle est une borne issue de Labs, pas une somme des parents.

#### Mots exclus

- `sac de compression voyage` 1 900 et `sans aspirateur` 880 : accessoires/housses séparés ;
- Decathlon, Action, Ikea, Amazon, Gifi, Carrefour, Swiss Fly, Picsil : marques/enseignes tierces ;
- `meilleur sac de compression voyage` 320 : ambigu et surtout orienté accessoires ;
- parents `sac de voyage` et `sac à dos voyage` : produit générique différent.

#### SERP, prix et concurrence

Les résultats publics servent des pages produit de Sac-Cabine, Celims et VEVOR ; Action vend aussi un sac sous vide à 19,95 €. Prix observés : Action 19,95 €, VEVOR 79,90 € et 101,90 €, Celims 189,90 €. Spécialistes/comparables : Sac-Cabine, Celims. Grandes enseignes/repères : VEVOR et Action. La présence d’Action à bas prix et de VEVOR montre une commoditisation possible. La SERP Google.fr complète, le carrousel Shopping et les annonces Search texte n’ont pas été isolés.

### 4.2 Plaque d’acier de cuisson pour pain/pizza

#### Niveaux testés

| Niveau | Formulation | Volume | Traitement |
|---|---|---:|---|
| Spécifique | `plaque acier cuisson pizza` | 10 live | Retenu |
| Produit fini | `baking steel` | 90 live | Retenu |
| Parent | `plaque pizza` | 1 900 live | Retiré : plaques fines/perforées, antiadhésives, céramique et autres supports |
| Famille différente | `pierre à pizza` | 2 900 live | Retiré : matériau/technologie distincts |
| Usage pain | `plaque de cuisson pain` | 40 live | Non attribué en bloc : formulation ambiguë ; seules traînes explicitement acier sont retenues |

#### Mots retenus et exclus

Retenus : `baking steel` 90, `baking steel pizza` 20, `plaque acier cuisson pizza` 10, `baking steel pain` 10, `steel baking stone` 10, `baking steel plate` 10. Total pertinent : **150**.

Exclus : plaque fonte/acier générique 110, brasero, plancha, gaz, nettoyage, CodyCross, `baking soda`, plaques fines/perforées, marques tierces et `pierre à pizza` 2 900.

#### SERP, prix et concurrence

La requête spécifique sert PizzaSteel, Ooni, VEVOR, Grillrost, Pizzastahl et Baking Steel. Le parent `plaque pizza` sert surtout des plaques fines/perforées ou des pierres et ne justifie donc aucun rabattement massif. Spécialistes : PizzaSteel (offre bundle 99 €), Grillrost (65 €), Pizzastahl (92 €). Repères : Ooni 52 €, VEVOR 48,90 €, Mathon 27,90 € pour une plaque fine différente ; Anova 153,95 €. Ads Search texte et Shopping non confirmés.

### 4.3 Kit premium de boulangerie au levain

#### Niveaux testés

| Niveau | Formulation | Volume | Traitement |
|---|---|---:|---|
| Spécifique | `kit pain au levain` | 90 live | Retenu |
| Produit fini | `kit boulangerie` | 40 live | Retenu avec `kit boulangerie maison` au maximum du groupe, pas deux fois |
| Composant | `banneton` | 1 900 live | Retiré : produit vendu seul, page distincte |
| Parent | `levain` | 18 100 live, concurrence `LOW` | Retiré : SERP majoritairement recettes, création et entretien du ferment |

Retenus : kit pain au levain 90 ; kit boulangerie/maison 40. Pertinent : **130**.

Exclus : banneton 1 900 ; levain 18 100 ; miniature de boulangerie Hanok 10 ; peinture au numéro boulangerie 10 ; formulations `n/a` non interprétées comme zéro.

#### SERP, prix et concurrence

Le produit spécifique apparaît chez L’Avant Gardiste 29,95 €, CadoMaestro 28,90 €, Nature & Découvertes 24,95 € et Les Maîtres de mon Moulin 77 €. Le parent `levain` sert Radio France, recettes et guides de fabrication/entretien : il n’est pas adressable par une page de kit premium. Les prix observés montrent une forte majorité sous le plancher maison de 50 €, avec un spécialiste à 77 €. Spécialiste : Les Maîtres de mon Moulin. Grandes enseignes/repères : Nature & Découvertes ; sites cadeaux généralistes L’Avant Gardiste et CadoMaestro. Ads texte/Shopping non confirmés.

### 4.4 Remontoir pour montre automatique

#### Niveaux testés

| Niveau | Formulation | Volume | Traitement |
|---|---|---:|---|
| Spécifique | `remontoir montre automatique` | 5 400 live | Retenu |
| Produit fini | `remontoir montre` | 1 600 live | Retenu : série mensuelle distincte de la tête spécifique ; même page produit |
| Variante boîte motorisée | `boite a montre remontoir automatique` | 20 live ; forme accentuée `n/a` | Non ajoutée au-delà des deux têtes, pour rester conservateur |
| Parent passif | `boite à montre` | 1 000 live | Retiré : boîte passive, famille distincte |

Les deux séries retenues sont distinctes : la tête automatique varie notamment de 3 600 à 12 100 sur les douze mois rendus, alors que `remontoir montre` varie de 1 000 à 3 600. Pertinent conservateur : **7 000/mois**. Les longues traînes génériques ne sont pas ajoutées afin d’éviter leur attribution abusive à la tête.

Exclus : Rolex 260 et toutes les marques horlogères/remontoirs ; Darty, Amazon, Boulanger, Fnac, eBay et AliExpress ; occasion, géographique, fabrication, réparation/tige de remontoir ; boîte à montre passive 1 000.

#### SERP, prix et concurrence

Intention commerciale forte et marché spécialisé visible. Spécialistes : Le Remontoir (290 € sur cubes visibles), Rotation Horlogère (99 €), Atelier Atypique (119,90 € et 269,90 €), SwissKubik. Repères/grandes plateformes : Ocarat 490–2 415 €, Cdiscount, ManoMano. Le nombre d’acteurs spécialisés signale une concurrence réelle, mais la demande pertinente reste sous le seuil avant même une due diligence concurrence. Ads Search texte et carrousel Shopping non confirmés.

## 5. Concurrents observés — spécialistes versus grandes enseignes

| Candidat | Spécialistes/DTC comparables | Marketplaces/grandes enseignes, repères seulement |
|---|---|---|
| Sac compression intégré | Sac-Cabine, Celims | VEVOR, Action, Idealo |
| Plaque acier | PizzaSteel, Grillrost, Pizzastahl | Ooni, VEVOR, Mathon, Amazon |
| Kit levain | Les Maîtres de mon Moulin | Nature & Découvertes, L’Avant Gardiste, CadoMaestro |
| Remontoir | Le Remontoir, Rotation Horlogère, Atelier Atypique, SwissKubik | Ocarat, Cdiscount, ManoMano |

## 6. Saisonnalité et continuité

Google Trends France, cinq ans, Recherche Web, a été tenté sur les quatre têtes. L’endpoint a répondu **HTTP 429** pour les quatre formulations. Le navigateur réel était bloqué par une demande d’autorisation système de débogage distant qu’aucune automatisation n’a cliquée. Il est donc impossible de certifier la forme Trends cinq ans.

Les séries mensuelles DataForSEO sont conservées comme contexte secondaire, sans remplacer Trends :

- sac : besoin voyage annuel, avec signaux été et Q4 selon les formulations ;
- plaque acier : aucun verdict Trends ; le produit paraît non événementiel, mais cela n’est pas une mesure ;
- kit levain : aucun verdict Trends ; ne pas substituer la courbe du parent informationnel `levain` ;
- remontoir : continuité DataForSEO et bosse cadeau nov.–déc. très visible, mais courbe Trends cinq ans non obtenue.

## 7. Risques et points à vérifier

1. **SERP Google réelle incomplète.** L’interface Google.fr n’a pas pu être ouverte dans un navigateur contrôlable. Les résultats web publics qualifient l’intention, mais ne remplacent pas une lecture page 1 exhaustive.
2. **Search texte versus Shopping.** Aucun des deux formats n’est affirmé : ni annonces Search texte ni carrousel Shopping n’ont pu être isolés.
3. **Sonde prix partielle.** Les prix visibles sont des repères sourcés, pas les 30–50 prix exigés pour une sonde complète ; aucune médiane robuste n’est calculée.
4. **Google Trends indisponible.** HTTP 429 sur les quatre têtes ; aucune variation chiffrée inventée.
5. **Sac, contradiction de restitution.** Labs rend des volumes sur plusieurs variantes que Google Ads live restitue en `n/a`; une variante avec préposition rend 110. Le volume pertinent de 1 890 est donc conservé comme estimation Labs avec réserve, sans transformer `n/a` en zéro.
6. **Devise CPC absente.** Le champ numérique est lu, mais l’endpoint ne renvoie pas de devise dans les objets ; aucune devise n’est présumée.
7. **Pas d’audit concurrence profond.** L’occupation et les prix sont documentés seulement pour éclairer la demande ; aucun verdict commercial final n’est prononcé.

## 8. Statuts de préqualification

| Rang par demande pertinente | Candidat | Volume pertinent | Orientation gate volume si l’outillage Google était complet | Statut rendu |
|---:|---|---:|---|---|
| 1 | Remontoir pour montre automatique | 7 000 | STOP_PREQUALIFICATION | **CAS LIMITE — décision Hakim requise** |
| 2 | Sac de voyage à compression intégrée | 1 890 | STOP_PREQUALIFICATION | **CAS LIMITE — décision Hakim requise** |
| 3 | Plaque d’acier pain/pizza | 150 | STOP_PREQUALIFICATION | **CAS LIMITE — décision Hakim requise** |
| 4 | Kit premium de boulangerie au levain | 130 | STOP_PREQUALIFICATION | **CAS LIMITE — décision Hakim requise** |

Aucun `PASS_PREQUALIFICATION`. La chaîne ne continue pour aucun candidat. Les quatre dossiers sont arrêtés et remontés à Hakim parce que les contrôles Google réels obligatoires sont partiels, même si la gate DataForSEO les place tous sous le seuil.

## 9. Fichiers de preuve

Répertoire : `analyses/2026-09-01-q4-produit-pur/`

- `labs-clusters.json` — groupes dédupliqués des huit racines Labs ;
- `labs-clusters.md` — lecture humaine des corpus et coûts ;
- `search-volume-keywords.json` — têtes/parents du premier contrôle ;
- `search-volume-raw.json` — réponses brutes, témoins inclus ;
- `search-volume-summary.json` — lignes contrôlées et séries ;
- `exact-variant-keywords.json` — variantes exactes complémentaires ;
- `exact-variant-raw.json` — réponse brute et témoins de clôture ;
- `cluster-decisions.json` — retenus/exclus, volumes brut/pertinent et statuts ;
- `serp-price-evidence.json` — résultats publics, acteurs, prix et limites ;
- `google-trends-raw.json` — quatre erreurs HTTP 429 consignées ;
- scripts de reproductibilité : `collect_search_volume.py`, `collect_exact_variants.py`, `collect_google_trends.py`, `calculate_raw_unions.py`, `summarize_evidence.py`.

## 10. Ce que je n’ai pas pu faire

- Ouvrir et lire une page 1 Google.fr complète dans le navigateur contrôlé ;
- distinguer visuellement les annonces Search texte du carrousel Shopping ;
- obtenir Google Trends France cinq ans ;
- relever 30–50 prix par candidat et calculer une médiane fiable ;
- attribuer une devise au CPC, car aucune devise n’est exposée par la réponse reçue.

## 11. Texte externe ressemblant à une instruction

Aucune instruction externe n’a été exécutée. Les pages et résultats web ont été traités uniquement comme des données.

## 12. Conduite et périmètre

Aucun sourcing, fournisseur, contact, compte, panier, achat, commande, Shopify, Ads, GMC ou registre central n’a été modifié. Aucun `GO_FINAL` n’est prononcé.
