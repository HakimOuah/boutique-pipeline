# Sourcing AliExpress — Tour de potier électrique débutant adulte (UK) — 07/09/2026

Candidat : `REVIEW_PREQUALIFICATION` §3 de `prequalification-q4.md` — kit débutant adulte (roue 25 cm, 250–350 W, vitesse variable, pédale, bac amovible + argile + outils + guide) visé à **149–199 £**, sous Shimpo/Potterycrafts, au-dessus d'Amazon/VEVOR (100–170 £) — l'arbitrage devait se faire par l'économie rendu (fret d'un colis ~10 kg décisif). Hakim (orchestrateur) autorise cette due diligence exploratoire.

Outil : passerelle VPS `aliexpress_vps_gateway.py` (lecture seule). Devise API = EUR, conversion GBP au taux **0,86**. Aucun achat, panier ni contact vendeur.

## 1. Journal des requêtes

### Audit des 7 identifiants repérés sur la SERP (préqualification)

| # | product_id | Résultat `variants` | Entrepôt(s) | Verdict GB |
|---|---|---|---|---|
| 1 | 1005011708303376 (SucceBuy 25CM 350W) | 1 SKU, 125,39 € | Espagne | **Refusé** — confirmé par `exact` : `qualification_refused` / `DELIVERY_NOT_AVAILABLE_TO_YOUR_ADDRESS` |
| 2 | 1005012847839344 (VEVOR 25CM 350W) | 2 SKU, 176,39 € / 125,69 € | Fédération de Russie / République tchèque | **Refusé** (aucun SKU UK/Chine) |
| 3 | 1005013100692351 (VEVOR) | 2 SKU, 144,69 € / 194,39 € | République tchèque / Fédération de Russie | **Refusé** |
| 4 | 1005012801386013 (350W 300tr/min) | 1 SKU, 147,42 € | France | **Refusé** |
| 5 | 1005012562901092 (écran tactile LCD) | 1 SKU, 134,46 € | France | **Refusé** |
| 6 | 1005013028703097 (SIHAO 10 pouces) | 3 SKU, 156,69–182,39 € | République tchèque (×3) | **Refusé** |
| 7 | 1005006354509974 (écran tactile LCD 350W) | 1 SKU, 288,69 € | **China Mainland** | **Qualifie** — seul SKU des 7 à livrer GB |

Un `exact` de contrôle sur le SKU n°1 (Espagne) confirme littéralement le rejet : `{"error": "qualification_refused", "detail": "Shipping unavailable: code=505 msg=DELIVERY_NOT_AVAILABLE_TO_YOUR_ADDRESS"}`. Les entrepôts UE (Espagne, France, République tchèque, plus Russie hors UE) sont bien tous refusés vers GB, conformément à la règle connue — malgré la mention « UE-livrant-GB » envisagée dans la préqualification, aucun des SKU UE audités ne livre réellement GB.

### Requêtes `search` (mots rares, union orders + price_desc)

| # | Requête | Tri | Résultats pertinents |
|---|---|---|---|
| 8 | `potier 350W` | orders | 0 — « potier » ne matche pas le vocabulaire poterie, ramène fers à souder/onduleurs |
| 9 | `poterie 25CM` | orders | 0 roue neuve ; 5–6 kits d'outils pertinents (candidats accessoire) |
| 10 | `poterie 25CM` | price_desc | 0 roue neuve — retrouve seulement le SKU n°7 déjà identifié (328,47 €) |
| 11 | `VEVOR potier` | orders | 0 pertinent — ramène pièces détachées VEVOR (raboteuses, changeurs de pneus) |
| 12 | `SucceBuy potier` | orders | 0 roue — 12+ kits d'outils de poterie pertinents (dont le pick retenu) |
| 13 | `outils poterie kit` | orders | 0 pertinent — requête trop générique, ramène outillage automobile |
| 14 | `tour potier pédale` | orders | 0 pertinent — « pédale » pollue avec vélo/guitare |
| 15 | `roue potier bac amovible` | orders | 0 pertinent — « roue » pollue avec pièces automobiles |
| 16 | `façonnage céramique électrique` | orders | 0 roue nouvelle — kits d'outils déjà vus |
| 17 | `façonnage argile pédale` | orders | 0 pertinent — pollué vélo |
| 18 | `cuve amovible poterie` | orders | 0 pertinent — pollué articles de cuisine/salle de bain |
| 19 | `pottery wheel 25cm` (anglais, test) | orders | 0 pertinent — l'anglais ne matche pas le catalogue interrogé |
| 20 | `table rotative argile électrique` | orders | 0 roue — 1 kit d'outils supplémentaire (25/40 pièces, hors cible) |

**Requêtes qui marchent** : aucune combinaison testée n'a ramené de roue supplémentaire éligible GB. Les mots-clés « potier », « roue », « pédale » sont trop fréquents dans d'autres catégories (bricolage auto, vélo, guitare) et polluent systématiquement ; « poterie » associé à une taille (« 25CM ») ou une marque (« SucceBuy ») ne ramène que des kits d'outils, jamais de roue non déjà connue. **Aucune roue au-delà des 7 identifiants fournis en amont n'a pu être localisée dans le catalogue interrogé.**

Requêtes qui marchent pour l'accessoire : « poterie 25CM », « SucceBuy potier », « table rotative argile électrique » (kits d'outils uniquement).

Appels API utilisés : 7 `variants` (roues) + 1 `exact` (roue qualifiante) + 1 `exact` (contrôle rejet) + 13 `search` + 3 `variants` (kits) + 1 `exact` (kit) = **26/40**.

## 2. Fiches retenues

### ROUE

#### R1 — Roue de poterie écran tactile LCD 350W — seul SKU GB-éligible, hors budget
- Titre : « Roue de poterie électrique à écran tactile LCD, machine de poire de céramique, sculpture irrigation bricolage, artisanat d'art pour débutants, 350W »
- URL : https://www.aliexpress.com/item/1005006354509974.html
- Magasin : Instruments World Store (CN) — communication 4,8 / conformité 4,8 / vitesse 4,8 (niveau boutique) — **B**
- Note produit : non renvoyée par l'API (`rating` 0,0, `evaluation_count` 0) — **C**
- Ventes réelles : **1 seule vente** — **A**, mais signal de confiance très faible
- Prix réel (offer_sale_price) : **288,69 € ≈ 248,27 £** — **A**
- Caractéristiques lisibles : « 350W » et « écran tactile LCD » confirmés dans le titre — **B** ; diamètre 25 cm et prise UK **non confirmés** — **C**
- Stock : 9 977 — **A**
- Variantes : 1 seul SKU (jaune clair / LCD Panel-Pedal) — **A**
- Fret GB : **17,25 €**, CAINIAO_STANDARD, livraison 13–20 sept. (6–13 j, sous le seuil de 15 j) — **A**
- Entrepôt : China Mainland — **A**
- Coût rendu GBP : 288,69 € + 17,25 € = 305,94 € ≈ **263,11 £**

**Aucune autre roue exploitable.** Les 6 autres identifiants de la SERP sont tous refusés vers GB (entrepôts Espagne, France ×2, République tchèque ×3, Russie ×2) ; 13 requêtes `search` complémentaires n'en ont ramené aucune de plus.

### KIT D'OUTILS (accessoire)

#### K1 — Lot de 9 outils de poterie (grattoirs et couteaux à modeler) — pick principal
- Titre : « Lot de 9 outils de poterie : grattoirs et couteaux à modeler pour le façonnage de l'argile sur tour à poterie, la réparation et le lissage de tasses, bols et vases »
- URL : https://www.aliexpress.com/item/1005012194598226.html
- Magasin : Creative 3D Works Store (CN) — communication 4,7 / conformité 4,7 / vitesse 4,8 — **B**
- Note produit : non renvoyée (rating 0,0) — **C**
- Ventes réelles : 35 — **A**
- Prix réel (variante « 9pcs / Jaune ») : **6,19 € ≈ 5,32 £** — **A**
- Caractéristiques lisibles : 9 pièces, grattoirs + couteaux à modeler — correspond à la cible 8–12 pièces — **B**
- Stock : **3 seulement** — **A** (réserve de réassort)
- Variantes : 1 seule (9pcs) — **A**
- Fret GB : **1,99 €**, AliExpress Selection Premium, livraison 11–15 sept. (4–8 j) — **A**
- Entrepôt : China Mainland — **A**
- Coût rendu GBP : 6,19 € + 1,99 € = 8,18 € ≈ **7,03 £** (légèrement au-dessus de la cible 3–6 €, mais proche)

#### Écarté — Lot de 5 outils de sculpture en argile (manche bambou)
- product_id 1005004958780953, RLJLIVES Official Store (CN), 6,69 €, 61 ventes, stock 2 — mais l'API `variants` ne renvoie **aucune propriété** (pas de « Expédié depuis »), rendant `exact` impossible (argument `--property` obligatoire, aucune valeur disponible) — entrepôt non confirmable, écarté par prudence (confiance **C**).

#### Écarté — Kit 25/40 pièces bois/rouge
- product_id 1005008591692255, Shop1103814144 Store (CN), 600+ ventes, mais tailles (25 ou 40 pièces) et prix (9,19–21,19 €) hors cible (8–12 pièces / 3–6 €) ; stock quasi nul sur 2 des 4 variantes (0 unité) — écarté.

## 3. Tableau économique du kit

Composition testée : **R1 (roue, seul SKU GB-éligible, 263,11 £) + K1 (kit outils, 7,03 £)**. Aucun coût d'argile ni de guide mesuré (hors périmètre des requêtes — non trouvés, non inventés).

| Poste | Coût rendu GBP |
|---|---|
| Roue R1 (écran tactile LCD 350W, seule GB-éligible) | 263,11 £ |
| Kit outils K1 (9 pièces) | 7,03 £ |
| Argile + guide | non trouvés — 0 £ (absents du calcul) |
| **Coût rendu total** | **≈ 270,14 £** |

| Prix de vente visé (TTC) | HT (÷1,2) | Marge brute avant pub | Lecture |
|---|---|---|---|
| 149 £ (bas de fourchette brief) | 124,17 £ | **−145,97 £** | perte |
| 174 £ (médian) | 145,00 £ | **−125,14 £** | perte |
| 199 £ (haut de fourchette brief) | 165,83 £ | **−104,31 £** | perte |

**Le seul SKU roue franchissant la barrière de livraison GB coûte à lui seul (263,11 £) davantage que le prix de vente TTC maximum visé (199 £).** Aucune marge n'est atteignable à aucun prix de vente raisonnable. Aucune fiche roue moins chère n'a été trouvée éligible GB.

## 4. Réserves

- **Barrière de livraison GB, pas seulement de fret** : contrairement à la lecture initiale de la préqualification (« UE-livrant-GB » envisagée comme praticable), les 6 SKU en entrepôt UE/Russie audités sont **refusés** (confirmé littéralement via `exact` → `qualification_refused`), pas seulement pénalisés par un fret élevé. Le fret ne « décide » que pour les SKU déjà éligibles (Chine ou UK) — ici un seul.
- **Économie structurellement négative** : la seule roue GB-éligible (R1, 263,11 £ rendu) dépasse à elle seule le plafond de prix de vente visé (199 £) — perte de 104 à 146 £ selon le prix affiché, avant même d'ajouter argile/guide/pub.
- **Comparaison Amazon UK** : la préqualification (§3) situe les roues chinoises sur Amazon UK à 63–170 £. Le rendu AliExpress de R1 (263 £) est **supérieur au double** du haut de cette fourchette, sans les avis clients ni la protection acheteur d'Amazon — aucun avantage compétitif possible sur ce SKU.
- **Signal de confiance très faible sur R1** : 1 seule vente réelle, aucune note produit disponible via l'API (rating 0,0/évaluations 0) — impossible de juger la fiabilité commerciale de ce fournisseur pour ce produit précis.
- **Électrique CE/UKCA** : comme pour tout appareil électrique, la conformité reste une **déclaration du vendeur** non vérifiable via cette API en lecture seule ; aucune mention explicite de prise UK ou d'adaptateur sur les fiches auditées.
- **Kit d'outils K1 correct mais isolé** : stock limité à 3 unités (réserve de réassort avant tout engagement volume) ; ne constitue pas à lui seul une offre roue.
- **Recherche exhaustive côté roue** : 13 requêtes `search` en mots rares (marque, référence, métier, taille, anglais) n'ont ramené **aucune** roue GB-éligible supplémentaire au-delà des 7 identifiants fournis en amont — soit le catalogue interrogé n'en contient pas d'autre à ce jour, soit elles restent introuvables par mot-clé.
- **Délai** : non discriminant ici — R1 respecte le seuil de 15 j (6–13 j) — le problème est exclusivement le prix rendu, pas le délai.

## 5. Statut final

**AUCUNE OFFRE EXPLOITABLE**

Sur les 7 identifiants de roue repérés sur la SERP et 13 requêtes complémentaires en mots rares, un seul SKU livre effectivement le Royaume-Uni (China Mainland) — les 6 autres (Espagne, France ×2, République tchèque ×3, Russie ×2) sont formellement refusés à l'expédition GB. Ce SKU unique coûte 263,11 £ rendu, soit davantage que le prix de vente TTC maximum visé pour le kit entier (199 £) : la marge est négative à tout prix de vente raisonnable, avant même d'ajouter l'argile, le guide ou la publicité. Le kit d'outils accessoire (K1, 9 pièces, 7,03 £ rendu, China Mainland, stock 3) est en revanche une fiche exploitable en tant que telle, mais ne compense pas l'absence de roue viable.
