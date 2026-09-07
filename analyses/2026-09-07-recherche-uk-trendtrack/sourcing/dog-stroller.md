# Sourcing AliExpress — poussette pour chien (dog stroller / pram) — UK — 07/09/2026

Rôle : oh-sourcing. Lecture seule, aucune commande ni contact vendeur. Taux de conversion appliqué : **1 EUR = 0,86 GBP**. Brief : poussette chien taille moyenne/grande, charge ≥ 25–30 kg, pliable, roues pneumatiques ou EVA grandes, frein, panier ; cible 99–139 £ ; écarter le léger < 15 kg à 35–50 £.

## 1. Journal des requêtes

### 1a. Audit des 7 identifiants pré-repérés sur la SERP (priorité de l'orchestrateur)

| ID | Titre | Ships From disponibles | Capacité lisible | Verdict |
|---|---|---|---|---|
| 1005007498386796 | LUVODI poussette pliable 4 roues, grands chiens | GB, DE, AU, US (+ doublons FR-vides) | non chiffrée ("grands chiens" seulement) | **Retenue (A) — GB dispo** |
| 1005008330559169 | SucceBuy 66 lbs poussette pliable, freins, panier | GB, PL, FR, CZ, DE, ES, US | **66 lbs ≈ 29,9 kg** (mais texte "petite à moyenne taille" contredit le chiffre) | **Retenue (B) — GB dispo** |
| 1005011811253031 | Pawhut 3 roues, maille, tout-terrain | ES seulement | **20 kg** explicite | Écartée — capacité sous le seuil brief (25–30 kg) ET pas de SKU GB (ES refusé) |
| 1005008579402835 | 3-en-1 pliable, 30 lb, "chiens moyens/petits" | aucune propriété "Ships From" renvoyée (origine non qualifiable) | **30 lb ≈ 13,6 kg** | Écartée — capacité très sous le seuil (produit léger, exclu explicitement par le brief) |
| 1005007905611620 | Pawhut pliable 76,5×52×95 cm | FR seulement, stock 0 | non chiffrée | Écartée — stock 0, pas de GB, gabarit petit chien |
| 1005008917103098 | Porte-animaux à roulettes ≤ 15 lb | CN (pas de propriété Ships From alternative visible) | **15 lb ≈ 6,8 kg** | Écartée — c'est un sac de transport à roulettes pour très petit animal, pas une poussette moyen/grand chien |
| 1005007916878914 | Pawhut 3 roues 109,5×57,5×106,5 cm rouge | ES seulement | non chiffrée | Écartée — pas de GB (ES refusé), capacité non confirmée |

### 1b. Recherches complémentaires (`search`)

| Requête | Tri | Résultats pertinents / 20 |
|---|---|---|
| `poussette chien 30kg` | orders | 0 — bruit poussette bébé (ventilateurs, crochets, jouets) |
| `Pawhut poussette` | orders | 0 — même bruit poussette bébé |
| `pet stroller pneumatic` | orders | 0 — pompes à air vélo/voiture, accessoires poussette bébé |
| `large dog stroller` | orders | 0 — accessoires poussette bébé, harnais |
| `SucceBuy poussette` | orders | 0 — accessoires poussette bébé |
| `remorque vélo chien` | orders | 0 — accessoires vélo génériques, harnais |
| `dog stroller pneumatic wheels` | orders | 0 — accessoires vélo, jouets chien |
| `poussette chien pliable grand` | price_desc | 0 — caravanes, remorques de camping, équipement toilettage pro (bruit "pliable grand") |
| `voiturette pour chien senior` | orders | 0 — jouets, gamelles, harnais |
| `pet stroller large dog detachable` | orders | 0 — accessoires voiture/poussette bébé |
| `chariot animaux domestiques pliable 4 roues` | orders | 0 — mobilier de camping, accessoires voiture |
| `dog bike trailer stroller combo` | orders | 0 — accessoires vélo/poussette bébé |

**Aucune requête `search` testée (12 variantes FR/EN, mots rares conformes à la consigne) n'a fait remonter un seul produit "poussette pour chien" pertinent.** Le mot "poussette" est totalement noyé par les accessoires de poussette bébé (crochets, ventilateurs, moustiquaires) quel que soit le tri ; les formulations anglaises ("dog stroller", "pet stroller") retombent sur les mêmes accessoires génériques pour chiens (gamelles, sacs à crottes, harnais) ou les accessoires vélo. Seul l'audit direct des identifiants pré-repérés par l'orchestrateur (section 1a) a produit des fiches exploitables. Constat cohérent avec l'expérience déjà documentée sur d'autres familles (`ice-bath.md`) : la passerelle `search` ne couvre pas correctement cette niche.

22 appels passerelle au total (7 `variants`, 2 `exact`, 12 `search` + 1 tentative de filtrage local), sous le plafond de 40.

## 2. Fiches retenues (2 — objectif 3–4 non atteint)

### Fiche A — LUVODI poussette pliable à 4 roues, grands chiens (taille XL, entrepôt UK)
- **Titre** : Poussette portable pliable à 4 roues pour grands chiens, animal de compagnie, chat, voyage
- **URL** : https://www.aliexpress.com/item/1005007498386796.html
- **Magasin** : LUVODI HOME Store (CN) — communication 4,8 / conformité 4,8 / expédition 4,9 [A]
- **Note produit (API `variants`/`exact`)** : 0,0 / 0 évaluation enregistrée [A — donnée API], à comparer à la note 4,9 citée par la SERP de l'orchestrateur [B, source distincte non revérifiable ici]
- **Ventes réelles (variants)** : 28 [A]
- **Variante visée** : Couleur "BLANC" (As Picture), Taille XL(90x74x15.5cm), Ships From Royaume-Uni — `offer_sale_price` 134,99 EUR → **116,09 £** [A]
- **Charge max / roues / poids** : non lisible dans le titre ni les propriétés — "grands chiens" est qualitatif, aucun chiffre de charge (kg/lb), aucune mention du type de roue (pneumatique/EVA) [C — absent]
- **Stock (variante XL, GB)** : 46 [A]
- **Variantes** : 12 SKU (3 tailles S/M/L/XL croisées avec 4 origines : GB, DE, AU, US) [A]
- **Fret vers GB (exact)** : gratuit, 4 transporteurs proposés (Hermes/Evri, Royal Mail, XDP Express, Yodel), entrepôt **Royaume-Uni**, délai **2–7 jours** [A]
- **Coût rendu GBP** : 116,09 + 0 = **116,09 £**
- **Confiance** : B — origine GB confirmée et fret rapide gratuit [A], mais capacité de charge et type de roue non confirmés [C], et note produit à 0 évaluation côté API malgré la note citée en amont.

### Fiche B — SucceBuy 66 lbs poussette pliable pour chien (entrepôt UK)
- **Titre** : SucceBuy 66 lbs poussette pour animaux de compagnie pliable chien chiot poussette avec freins panier de rangement support détachable pour chiens de petite à moyenne taille
- **URL** : https://www.aliexpress.com/item/1005008330559169.html
- **Magasin** : SucceBuy Home Garden Overseas Global Store (CN) — communication 4,7 / conformité 4,7 / expédition 4,8 [A]
- **Note produit (API)** : 0,0 / 0 évaluation enregistrée [A — donnée API], vs 4,9 cité par la SERP orchestrateur [B, non revérifiable ici]
- **Ventes réelles (variants)** : **5 seulement** [A]
- **Variante visée** : Couleur "BLANC" (Black), Ships From Royaume-Uni (seule origine, pas de choix de taille) — `offer_sale_price` 111,99 EUR → **96,31 £** [A]
- **Charge max / roues / poids** : **66 lbs ≈ 29,9 kg** annoncé dans le titre (dans la bande basse du seuil brief 25–30 kg) ; freins et panier de rangement confirmés dans le titre ; type de roue (pneumatique/EVA) non précisé [B pour la charge, C pour les roues]. Réserve terminologique : le même titre qualifie le produit "pour chiens de petite à moyenne taille" — contradiction avec le chiffre 66 lbs et avec le positionnement "moyenne/grande taille" du brief.
- **Stock (variante GB)** : **10 seulement** [A]
- **Variantes** : 7 SKU (une seule couleur, 7 origines : GB, PL, FR, CZ, DE, ES, US) [A]
- **Fret vers GB (exact)** : gratuit, mêmes 4 transporteurs (Hermes/Evri, Royal Mail, XDP Express, Yodel), entrepôt **Royaume-Uni**, délai **2–7 jours** [A]
- **Coût rendu GBP** : 96,31 + 0 = **96,31 £**
- **Confiance** : C — origine GB et fret confirmés [A], mais preuve commerciale très faible (5 ventes réelles, stock 10) et incohérence de gabarit dans le titre fournisseur [C].

Les 5 autres identifiants pré-repérés ont été écartés (motifs détaillés section 1a) : capacité sous le seuil (20 kg, 30 lb, 15 lb), absence de SKU livrable en GB (entrepôts ES/FR uniquement, refusés par la règle UE→GB), ou stock nul. Les 12 requêtes `search` complémentaires n'ont produit aucune fiche supplémentaire exploitable (bruit poussette bébé / accessoires génériques chien / vélo, voir section 1b).

## 3. Tableau économique

| Fiche | Coût rendu GBP | Prix visé 99 £ (HT 82,50 £) | Marge @99 £ | Prix visé 119 £ (HT 99,17 £) | Marge @119 £ | Prix visé 139 £ (HT 115,83 £) | Marge @139 £ |
|---|---|---|---|---|---|---|---|
| A — 1005007498386796 (XL, GB) | 116,09 £ | 82,50 £ | **-33,59 £** | 99,17 £ | **-16,92 £** | 115,83 £ | **-0,26 £** |
| B — 1005008330559169 (GB) | 96,31 £ | 82,50 £ | **-13,81 £** | 99,17 £ | +2,86 £ (2,9 %) | 115,83 £ | +19,52 £ (16,9 %) |

Marge = HT − coût rendu ; avant publicité, retours, emballage et toute autre charge. TVA UK 20 % : HT = TTC/1,2. Aucun coût de packaging, de retour ou d'assurance n'a été ajouté (non renvoyé par l'API ; fret déclaré gratuit par le transporteur).

**Lecture** : sur toute la bande de prix visée par le brief (99–139 £), la Fiche A (LUVODI) ne dégage jamais de marge brute positive — son coût rendu (116,09 £) dépasse le HT même au sommet de la fourchette. La Fiche B (SucceBuy) ne devient positive qu'à partir de 119 £, et seulement de façon significative (16,9 %) au sommet de la fourchette (139 £) ; en dessous de 119 £, elle est également négative.

## 4. Réserves

- **Économie marginale ou négative** : aucune des deux fiches ne dégage une marge confortable dans la bande 99–139 £ annoncée par la préqualification. Seule la Fiche B, positionnée au sommet (139 £), atteint ~17 % de marge brute avant publicité — insuffisant pour absorber un test Ads sans optimisation serrée.
- **Preuve commerciale faible** : 28 ventes réelles (Fiche A) et surtout seulement 5 ventes réelles (Fiche B) sur la passerelle — aucune des deux fiches n'a l'historique de ventes d'un produit éprouvé. La note "4,9" citée dans le brief d'origine (SERP orchestrateur) ne se retrouve pas dans les champs `rating`/`evaluation_count` de l'API sourcing (0,0 / 0 sur les deux fiches) — source à traiter avec prudence, écart non résolu ici.
- **Stock limité (Fiche B)** : seulement 10 unités disponibles sur le SKU GB — risque de rupture rapide en cas de test payant, sans garantie de réassort à délai correct.
- **Capacité de charge non confirmée pour la Fiche A** : le titre et les propriétés ne donnent aucun chiffre de charge (kg/lb) ni type de roue — impossible de vérifier objectivement le respect du seuil ≥ 25–30 kg du brief sur cette fiche via l'API.
- **Incohérence de gabarit sur la Fiche B** : le titre fournisseur annonce 66 lbs (≈ 30 kg) tout en qualifiant le produit "pour chiens de petite à moyenne taille" — contradiction non résolue, à vérifier en photos/dimensions avant tout engagement.
- **Type de roues non confirmé** : ni pneumatique ni EVA n'est mentionné explicitement sur aucune des deux fiches — critère structurant du brief non vérifiable via cette passerelle.
- **Délai conforme au seuil de 15 jours** : les deux fiches expédient depuis un entrepôt Royaume-Uni avec livraison 2–7 jours (Hermes/Evri, Royal Mail, XDP Express, Yodel) — sur ce point précis, aucune réserve.
- **Volume colis** : non renvoyé par l'API (poids/dimensions d'expédition absents des réponses `variants`/`exact`) — inconnu pour les deux fiches.
- **Même modèle vendu sur Amazon/B&Q UK** : non vérifié dans ce document (hors périmètre de l'outil sourcing, lecture seule AliExpress) — à croiser avec le travail de cartographie concurrence déjà réalisé en préqualification (SERP mentionnant Pawhut/Aosom déjà présents sur des marketplaces UK sous marque propre, cf. `prequalification-q4.md` §4).
- **Hors saison Q4** : réserve déjà actée en préqualification — le cluster `dog stroller`/`dog pram` UK a un creux hivernal, contrairement à la fenêtre Q4 visée par cette recherche.
- **Recherche `search` improductive** : les 12 requêtes complémentaires (FR/EN, mots rares) n'ont fait remonter aucune fiche supplémentaire pertinente ; le catalogue accessible via cette passerelle pour "poussette chien" semble limité aux fiches déjà repérées en amont par l'orchestrateur — pas de garantie qu'il n'existe pas d'autres offres mieux positionnées hors de cette liste.

## 5. Statut final

**FOURNISSEUR À TESTER**

Une seule fiche (B — SucceBuy, 1005008330559169) combine capacité proche du seuil brief (66 lbs ≈ 30 kg), frein et panier confirmés dans le titre, entrepôt Royaume-Uni avec fret gratuit et livraison rapide (2–7 j), et une marge brute positive — mais seulement au sommet de la fourchette de prix visée (139 £, ~17 % avant publicité) et avec une preuve commerciale très mince (5 ventes réelles, stock 10 unités). La fiche A (LUVODI), mieux dimensionnée en apparence ("grands chiens", 4 roues, entrepôt GB), ne dégage aucune marge positive dans la bande de prix 99–139 £ et ne confirme aucune donnée de charge — elle est conservée en comparaison mais n'est pas exploitable en l'état. Aucune des deux fiches ne peut être positionnée en dessous de 119 £ sans marge négative. Une commande test sur la Fiche B, avec vérification physique du gabarit, du type de roue et de la charge réelle avant tout engagement commercial, est la seule voie restante ; ce dossier ne peut pas être élevé au-delà de ce statut sur la seule base des données API.
