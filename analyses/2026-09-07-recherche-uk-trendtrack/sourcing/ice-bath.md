# Sourcing AliExpress — cuve de bain froid (ice bath tub) — UK — 07/09/2026

Rôle : oh-sourcing. Lecture seule, aucune commande ni contact vendeur. Taux de conversion appliqué : **1 EUR = 0,86 GBP**.

## 1. Journal des requêtes

| Requête | Tri | Résultats pertinents / 20 |
|---|---|---|
| `ice bath` | orders | 0 — noyé par moules à glaçons, jouets de bain, accessoires cuisine (mot fréquent "bath") |
| `ice bath tub` | orders | 0 — même bruit (moules à glaçons, bombes de bain) |
| `ice bath tub` | price_desc | 0 — machines à glace industrielles, spas gonflables génériques, rien d'exploitable |
| `cold plunge tub` | orders | 0 — accessoires robinetterie, ice packs, adaptateurs de baril IBC |
| `cold plunge tub` | price_desc | 0 — machines à glace industrielles / congélateurs pro |
| `bain froid isolé` | orders | **3 pertinents** — 2 baignoires glacées isolées, 1 baignoire pliable gonflable |
| `cuve glacée portable` | orders | 0 — moules à glaçons, sacs de rangement, ventilateurs |
| `ice barrel` | orders | 0 — uniquement moules/plateaux à glaçons |
| `cold plunge chiller compatible` | orders | 0 — ventilateurs et refroidisseurs PC |
| `baignoire plongeante froide armature` | orders | 0 — jouets de bain, robinetterie |
| `spa plongée froide portable` | orders | 0 — accessoires piscine, pompes |
| `cuve récupération froide athlète` | orders | 0 — bandes de glace, jauges de radiateur auto |
| `baignoire glacée isolation néoprène` | orders | 0 — vêtements "soie glacée" (faux positif linguistique) |
| `cuve bain glacé grande capacité` | orders | 0 — moules à glaçons, gourdes |
| `récupération froide cuve armature acier` | orders | 0 — accessoires cuisine/robinetterie inox |
| `bain de glace isolé grande capacité` | orders | 0 — mêmes 3 produits déjà identifiés en doublon, rien de nouveau |
| `cuve bain froid couvercle rigide` | orders | 0 — accessoires salle de bain |
| `tonneau bois immersion froide` | orders | 0 — accessoires de bar, agitateurs bois ; le produit 1005010151127666 réapparaît (déjà noté) |
| `baril immersion froide inox` | orders | 0 — accessoires cuisine inox |
| `insulated cold plunge tub` (EN) | orders | 0 — thermomètres bain bébé, gourdes isolées |
| `cold therapy tub large capacity` (EN) | orders | 0 — gourdes, seringues, boîtes de rangement |

**Seule requête productive : `bain froid isolé`.** Toutes les variantes testées (FR/EN, marques citées dans la mesure DataForSEO — Lumi, Polar Recovery, Ice Pod non retrouvées) retombent sur le bruit "bain" générique (moules à glaçons, jouets de bain, robinetterie, gourdes isothermes) ou sur l'équipement industriel (machines à glace commerciales) en tri prix décroissant.

## 2. Fiches retenues (3 — objectif 3–5 non atteint)

### Fiche A — « Bain de glace isolé » (baignoire pliable, no-gonflage)
- **Titre** : Bain de glace isolé 1 pièce, baignoire plongeante froide, aucune installation de gonflage nécessaire, compatible avec la douche pour une utilisation intérieure et extérieure
- **URL** : https://www.aliexpress.com/item/1005010151127666.html
- **Magasin** : Shop1103780365 Store (CN) — communication 4,6 / conformité 4,5 / expédition 4,7 [A]
- **Note (search)** : 4,8 / taux de satisfaction 96,9 % [B]
- **Ventes réelles (variants)** : 118 [A]
- **Variante visée** : Gold-M (couleur "GRIS") — `offer_sale_price` 77,99 EUR → **67,07 £** [A]
- **Capacité en litres / couches d'isolation** : non lisible — ni le titre ni les propriétés de variante ("Couleur" = codes Gold/Blue × S/M) ne donnent de volume ni de nombre de couches [C — absent]
- **Couvercle rigide inclus** : non mentionné dans le titre ; "aucune installation de gonflage" suggère une structure semi-rigide mais aucune confirmation de couvercle [C]
- **Stock** : Gold-S 310, Gold-M 291, Blue-S 2, Blue-M 294 [A]
- **Variantes** : 4 (déclarées "Couleur" mais en réalité tailles S/M croisées avec 2 gammes de couleurs — étiquetage confus côté fournisseur) [A]
- **Fret vers GB (exact, variante Gold-M)** : 1,99 EUR (1,71 £), transporteur "AliExpress Selection Shipping for Oversized Goods" (CAINIAO_FULFILLMENT_OVER_WH), entrepôt CN, délai **26–43 jours** (livraison estimée 03–20 oct.) [A]
- **Coût rendu GBP** : 67,07 + 1,71 = **68,78 £**
- **Images SKU renvoyées par l'API** : 4 (une par variante couleur/taille) [A]
- **Réserve délai** : 26–43 jours dépasse largement le seuil de 15 jours.

### Fiche B — « Baignoire glacée Portable » (même famille fournisseur que Fiche A)
- **Titre** : Baignoire glacée Portable, 1 pièce, baignoire pliable pour douche adulte, salle de bain, SPA chaud
- **URL** : https://www.aliexpress.com/item/1005010136368793.html
- **Magasin** : Shop1103677501 Store (CN) — communication 4,7 / conformité 4,5 / expédition 4,7 [A]
- **Note (search)** : 4,8 / taux de satisfaction 96,7 % [B]
- **Ventes réelles (variants)** : 69 [A]
- **Variante visée** : Yellow-S (couleur "GRIS") — `offer_sale_price` 93,69 EUR → **80,57 £** [A]
- **Capacité en litres / couches d'isolation** : non lisible, même absence que Fiche A [C — absent]
- **Couvercle rigide inclus** : non mentionné [C]
- **Stock** : Yellow-M 306, Yellow-S 311, Blue-M 280, Blue-S 5 [A]
- **Variantes** : 4 (même schéma de codage confus S/M × couleurs) [A]
- **Fret vers GB (exact, variante Yellow-S)** : 1,99 EUR (1,71 £), même transporteur oversized, entrepôt CN, délai **26–43 jours** [A]
- **Coût rendu GBP** : 80,57 + 1,71 = **82,28 £**
- **Images SKU renvoyées par l'API** : 4 [A]
- **Réserve** : mêmes codes SKU (14:10/14:691/14:193/14:175) que la Fiche A → très probablement le même produit physique reposté sous deux fiches/magasins différents. Même délai hors seuil.

### Fiche C — « MAYZANEN bain de glace » (gonflable, stock quasi épuisé)
- **Titre** : MAYZANEN bain de glace baignoire pliable Portable épaissir grand seau de bain gonflable adulte thérapie par l'eau en plein air baignoire plongeante froide
- **URL** : https://www.aliexpress.com/item/1005007216132507.html
- **Magasin** : Manleike Two Store (CN) — communication 4,4 / conformité 4,4 / expédition 4,6 [A]
- **Note (search)** : 4,3 / taux de satisfaction 85,2 % [B]
- **Ventes réelles (variants)** : 54 [A]
- **Variante visée** : "noir" (seule couleur) — `offer_sale_price` 63,69 EUR → **54,77 £** [A]
- **Capacité en litres / couches d'isolation** : non lisible ; le titre indique explicitement "gonflable" — exclu par le brief (cuve isolée non-gonflable visée), retenu ici seulement pour comparaison [C]
- **Couvercle rigide inclus** : non mentionné, peu probable vu la nature gonflable [C]
- **Stock** : 2 unités seulement sur l'unique variante — pratiquement en rupture [A]
- **Variantes** : 1 seule (aucun choix de taille/couleur) [A]
- **Fret vers GB (exact)** : 1,99 EUR (1,71 £), transporteur "AliExpress Selection Premium shipping" (CAINIAO_FULFILLMENT_PRE), entrepôt CN, délai **4–8 jours** (livraison estimée 11–15 sept.) — seul délai conforme au seuil [A]
- **Coût rendu GBP** : 54,77 + 1,71 = **56,48 £**
- **Images SKU renvoyées par l'API** : 1 [A]
- **Réserve majeure** : stock = 2 → invendable en l'état, et produit explicitement "gonflable" donc hors du positionnement isolé/rigide visé par le brief.

Note : une 4ᵉ piste — « Meilleure vente : Baignoire portable en bois pour bain froid avec revêtement en acier inoxydable » (product_id 1005011848352020, repérée en tri prix décroissant sur `cold plunge tub`, prix liste 6 051,62 EUR) — a été écartée : l'appel `variants` a échoué deux fois de suite (`IOPUpstreamError`, code 482), fiche probablement dépubliée ou inaccessible. Aucune donnée exploitable, non comptée dans les 3 fiches retenues.

## 3. Tableau économique indicatif

| Fiche | Coût rendu GBP | Prix visé 119 £ (HT 99,17 £) | Marge brute @119 £ | Prix visé 149 £ (HT 124,17 £) | Marge brute @149 £ |
|---|---|---|---|---|---|
| A — 1005010151127666 (Gold-M) | 68,78 £ | 99,17 £ | 30,39 £ (25,5 %) | 124,17 £ | 55,39 £ (37,2 %) |
| B — 1005010136368793 (Yellow-S) | 82,28 £ | 99,17 £ | 16,89 £ (14,2 %) | 124,17 £ | 41,89 £ (28,1 %) |
| C — 1005007216132507 (noir) | 56,48 £ | 99,17 £ | 42,69 £ (35,9 %) | 124,17 £ | 67,69 £ (45,3 %) |

Marge = HT − coût rendu ; avant publicité, retours, emballage et toute autre charge. TVA UK 20 % : TTC/1,2 = HT. Aucun coût de packaging, de retour ou d'assurance n'a été ajouté (non renvoyé par l'API).

## 4. Réserves

- **Différenciation vs Argos/B&Q/Amazon (35–60 £)** : impossible à établir. Aucune des 3 fiches ne confirme dans les données API (titre, variantes) la capacité ≥ 300 L, le nombre de couches d'isolation, la présence d'une armature/structure, ni d'un couvercle rigide ou isolant — les critères mêmes qui justifient un positionnement 119–149 £ au-dessus de la commodité PVC. Sans ces attributs confirmés, rien ne distingue objectivement A et B d'une simple baignoire pliable premium.
- **Poids** : non renvoyé par l'API (ni dans `search`, ni `variants`, ni `exact`) ; pour un produit "grande capacité", le poids conditionne le mode de fret réel — inconnu ici.
- **Délai > 15 jours** : Fiches A et B à 26–43 jours (entrepôt CN, fret "oversized") — hors seuil, réserve bloquante en l'état. Seule la Fiche C respecte le seuil (4–8 j) mais son stock de 2 unités et sa nature gonflable l'excluent du positionnement visé.
- **Entrepôt CN vs UE/UK** : les 3 fiches expédient depuis la Chine (aucun entrepôt UE/UK détecté) — cohérent avec le fret long des fiches A/B.
- **Thermomètre et valve de vidange** : aucune mention dans les titres ou variantes des 3 fiches ; non confirmés.
- **Aucune allégation santé** formulée dans ce document ; les titres sources emploient "thérapie par l'eau" côté fournisseur (Fiche C), à ne pas reprendre tel quel en fiche produit.
- **Doublon probable A/B** : mêmes codes SKU internes (14:10, 14:691, 14:193, 14:175) sur deux boutiques différentes → probablement le même moule/fournisseur usine dupliqué, pas deux offres indépendantes.

## 5. Statut final

**AUCUNE OFFRE EXPLOITABLE**

Aucune fiche trouvée sur la passerelle ne confirme les caractéristiques structurantes du brief (capacité ≥ 300 L, isolation multicouche, structure/armature, couvercle rigide ou isolant, thermomètre, valve de vidange). Les deux fiches les plus proches en positionnement (A, B) ont un délai de livraison GB de 26 à 43 jours, très au-dessus du seuil de 15 jours, et sont probablement la même référence usine dupliquée sur deux boutiques. La seule fiche à délai conforme (C) est en rupture quasi totale (stock 2) et explicitement gonflable, donc hors cible. Le catalogue accessible via cette passerelle ne semble pas porter la catégorie "cuve de bain froid grande capacité isolée" recherchée — seulement des baignoires pliables génériques, des accessoires de glace et de l'équipement industriel de fabrication de glace.
