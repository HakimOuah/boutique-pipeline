# Sourcing AliExpress — Chauffage diesel 12 V « all-in-one » (kit UK) — 07/09/2026

Rôle : oh-sourcing. Lecture seule (`aliexpress_vps_gateway.py`), aucun achat/panier/message vendeur/compte. Contexte lu au préalable : `prequalification-q4.md` section 2 (chauffage diesel 12 V, PASS_PREQUALIFICATION, réserves §4 + sécurité).

## 1. Journal

Taux de conversion appliqué : 1 EUR = 0,86 GBP. Tous les appels ont été exécutés en premier plan, séquentiellement, avec 1 s entre appels.

### 1.1 Audit des 8 identifiants fournis par la SERP (`variants`)

| # | product_id | Titre / vendeur | Ventes réelles | Prix réel (EUR) | SKU « Expédié depuis » observés | Verdict GB |
|---|---|---|---|---|---|---|
| 1 | 1005008461231588 | WinterGuard Auto Store, 8000W | 56 | 67,99–76,39 | République Tchèque (seul) | **Refusé** — pas de SKU UK/CN |
| 2 | 1005008755868248 | SucceBuy 5/8KW LCD | 58 | 91,99–99,69 | République Tchèque, Allemagne, Espagne, Pologne, France | **Refusé** — pas de SKU UK/CN |
| 3 | 1005010344657608 | WinterGuard, 5-8KW tout-en-un | 101 | 89,39 | République Tchèque (seul) | **Refusé** |
| 4 | 1005013010684641 | SucceBuy 5/8KW | 9 | 86,69–93,99 | France (seul) | **Refusé** |
| 5 | 1005010429667436 | SucceBuy 5/8KW | 24 | 84,39–91,69 | République Tchèque, France, Allemagne, Pologne, Espagne | **Refusé** |
| 6 | 1005001690776718 | Hcalory Official Store, tout-en-un | 6 | 117,99–145,99 | République Tchèque (seul) | **Refusé** |
| 7 | 1005010382582674 | VEVOR AutoParts Store | 2 | 122,39–124,39 | République Tchèque (seul) | **Refusé** |
| 8 | 1005007769070764 | Hcalory portable, Bluetooth | 3 | 107,39–165,39 | République Tchèque, États-Unis | **Refusé** — États-Unis hors règle (seuls UK/China Mainland livrent GB) |

Constat transversal : **aucun des 8 candidats n'expose de SKU « Royaume-Uni / United Kingdom » ni « China Mainland »**. Les 8 fiches sont fulfillées exclusivement depuis un réseau d'entrepôts UE (République Tchèque en hub principal, complété par Allemagne/Pologne/Espagne/France) ou, pour un cas, un entrepôt US. Confirmation explicite via `exact` sur le SKU République Tchèque du candidat #2 :
```
exact 1005008755868248 --property "Nom de la couleur=noir" --property "Expédié depuis=REPUBLIQUE CZEQUE" --destination GB
→ error: qualification_refused — "Shipping unavailable: code=505 msg=DELIVERY_NOT_AVAILABLE_TO_YOUR_ADDRESS"
```
Ceci confirme la règle connue (SKU UE refusés vers GB) sur ce cluster précis. Les ventes réelles des 8 fiches sont par ailleurs très faibles (2 à 101 unités), cohérent avec un fournisseur qui n'a pas ouvert de route GB pour ce produit.

### 1.2 Recherche d'alternatives UK/CN (`search`)

Requêtes exécutées (2 mots rares, `--destination GB`, union orders + price_desc) : `diesel heater 8kw`, `SucceBuy diesel`, `Hcalory diesel`, `campervan diesel heater`, `diesel 8KW`, `diesel parking heater` (orders + price_desc), `diesel air heater`, `chauffage stationnement diesel`, `SucceBuy` (seul, 0 résultat), `Hcalory 8kw`, `5kw all-in-one`.

Résultat : **aucune requête n'a fait remonter un chauffage diesel 5-8 kW tout-en-one**, malgré la diversité des formulations (FR/EN, marque + volt/puissance, tri par popularité et par prix décroissant). Le moteur de recherche renvoie systématiquement le même corpus d'accessoires automobiles génériques à fort volume de commandes (pompes à carburant, ventilateurs, chalumeaux, convertisseurs de tension) ou, en tri prix décroissant, des équipements industriels lourds sans rapport (bulldozers, groupes électrogènes marins). Deux requêtes ciblant la marque Hcalory ont fait apparaître des **accessoires** de la marque (adaptateur AC/DC, connecteur en Y) mais jamais l'appareil principal. Conclusion : le moteur `search` ne permet pas, sur ce cluster, de découvrir de nouveaux vendeurs UK/CN au-delà des 8 identifiants déjà fournis — la voie de sourcing pour ce produit précis est épuisée avec les outils disponibles.

Requête `CO alarm` (accessoire, tri orders) : a fait remonter deux détecteurs pertinents.
- 1005006775943842 : `variants` a échoué deux fois de suite (`IOPUpstreamError`, ae_code 482) après une nouvelle tentative — déclaré indisponible, écarté par erreur passerelle persistante (règle : réessayer une fois puis déclarer).
- 1005011734811158 (« Détecteur d'alarme CO indépendant… certification UL2034 ») : `variants` puis `exact` réussis, retenu (détail §2).

### 1.3 Requêtes efficaces
`CO alarm` (a produit le seul candidat exploitable de tout le passage) ; `variants` direct sur les 8 identifiants fournis (a produit une lecture complète et sans ambiguïté du problème GB). Les 11 formulations de `search` ciblant le chauffage lui-même n'ont rien produit d'exploitable.

## 2. Fiches retenues

### 2.1 Chauffage diesel — **aucune fiche retenue**

Les 8 candidats identifiés dans la SERP sont tous rejetés pour absence de SKU livrable en GB (voir tableau §1.1). Aucun autre vendeur UK/CN n'a pu être découvert via `search` malgré 11 requêtes variées. Aucune fiche « chauffage » ne peut donc être documentée avec titre/prix/fret GB — la donnée manquante est le fret, pas le produit : les 8 fiches existent, sont vendues (2 à 101 ventes réelles), mais AliExpress refuse explicitement la livraison GB pour toutes leurs variantes.

### 2.2 Détecteur de monoxyde de carbone (CO) — retenu

| Champ | Valeur | Confiance |
|---|---|---|
| Titre | Détecteur d'alarme CO indépendant, détecteur de monoxyde de carbone, alarme haute sensibilité, affichage LCD, alarme CO avec certification UL2034 | A (lu en `variants`/`exact`) |
| URL | https://www.aliexpress.com/item/1005011734811158.html | A |
| Magasin (pays) | Shop 1103832023 Store (CN) — communication 4,8 / conformité 4,7 / vitesse d'expédition 4,8 | A |
| Note produit | Champ `rating` vide dans `variants`/`exact` (0.0, non renseigné à ce niveau) ; note lisible seulement en `search` : 4,7 (`evaluation_rate` 94,7 %) | B — note fiable prise dans `search`, absente des autres endpoints |
| Ventes réelles | 2 000+ (texte `search`, non un compte exact) | B |
| Prix réel | 7,19 EUR → **6,18 £** (`offer_sale_price`, taxes incluses) ; prix de liste 15,63 EUR (2,2×) | A |
| Contenu / caractéristiques | Détecteur CO autonome, écran LCD, certification **UL2034** affichée au titre (norme US — pas une preuve de conformité UK ; à vérifier avant mise en vente, cf. réserves) | C pour la conformité UK |
| Variante | 1 seule couleur (blanc) — pas de variante de propriété « Expédié depuis » associée à ce SKU | A |
| Stock | 46 unités | A |
| Fret GB | AliExpress Selection Premium shipping (Cainiao) — **1,99 EUR (1,71 £)**, livraison 11–15 sept. (4 à 8 jours), suivi disponible, sans franco de port, expédié depuis **CN** (China Mainland, éligible GB) | A |
| Coût rendu | (7,19 + 1,99) EUR × 0,86 = **7,89 £** | A |

Ce détecteur seul ne suffit pas à constituer le kit demandé (chauffage + CO alarm) : il ne peut être présenté comme une offre autonome.

## 3. Tableau économique du kit

**Non calculable.** Le kit visé (chauffage diesel 119–169 £ + détecteur CO) exige un chauffage sourcé et livrable en GB ; aucun n'a été trouvé (§2.1). Seule la ligne détecteur CO est chiffrable isolément :

| Article | Coût rendu GBP | Prix visé (part du kit) | Marge brute avant pub (HT, TVA UK 20 %) |
|---|---|---|---|
| Détecteur CO (1005011734811158) | 7,89 £ | — (accessoire d'un kit non constitué) | non calculable sans prix de vente du kit |
| Chauffage diesel | — (aucune offre GB) | 119–169 £ (visé, prequalification) | non calculable |
| **Kit complet** | **non calculable** | 119–169 £ | **non calculable — bloqué par l'absence de chauffage livrable** |

Rappel méthode (à appliquer dès qu'un chauffage GB sera identifié) : HT = TTC ÷ 1,2 ; marge brute avant pub = prix de vente HT − coût rendu HT des deux composants. Aucun chiffre n'est inventé au-delà de cette formule tant que le second composant manque.

## 4. Réserves

- **Appareil à combustion** : chauffage diesel = déclaration de conformité CE/UKCA du seul vendeur (aucune vérification tierce possible depuis cet outil) ; à trancher par Hakim avant tout test, indépendamment du sourcing.
- **Poids/volume** : non mesuré ici faute de fiche chauffage exploitable ; les fiches EU consultées (République Tchèque) affichaient des poids de colis non extraits par `variants`/`exact` — à vérifier si une route GB apparaît un jour.
- **Délai > 15 j** : sans objet pour le chauffage (aucune offre GB du tout, refus ferme, pas un simple délai long) ; pour le détecteur CO, délai annoncé 4–8 jours (conforme).
- **Même produit sur Amazon UK sous marque chinoise** : rappel de la lecture prequalification (§2, `prequalification-q4.md`) — le produit AliExpress 5-8 kW tout-en-one est déjà vendu 65–100 £ sur Amazon/eBay UK ; combiné à l'absence de route GB directe sur AliExpress, cela renforce l'hypothèse que ces vendeurs alimentent le marché UK via un circuit de revente (Amazon FBA UK, stock déjà importé) plutôt que par expédition directe AliExpress → GB.
- **Certification UL2034 du détecteur CO** : norme américaine (Underwriters Laboratories), pas une preuve de conformité EN 50291 (norme UK/EU pour détecteurs CO domestiques) — à vérifier avant toute mise en vente si le kit devait être reconstitué autrement.
- **Cluster structurellement bloqué pour AliExpress → GB** : les 8 candidats de la SERP, deux vendeurs (SucceBuy, Hcalory, VEVOR, WinterGuard) et 11 requêtes de recherche convergent vers le même constat — ce sous-segment de chauffages diesel 5-8 kW n'a, à ce jour, aucune route d'expédition directe AliExpress vers le Royaume-Uni. Un chauffage diesel n'est probablement pas éligible au fret aérien standard (liquide inflammable résiduel dans le réservoir), ce qui expliquerait le cantonnement à un hub de distribution intra-UE non transposé en GB post-Brexit.

## 5. Statut final

**AUCUNE OFFRE EXPLOITABLE**

Le composant central du kit (chauffage diesel 12 V 5–8 kW) n'a aucune offre livrable en GB parmi les 8 identifiants fournis ni parmi les alternatives cherchées ; le détecteur CO seul (1005011734811158, coût rendu 7,89 £, fret CN 4–8 j) ne constitue pas un kit exploitable sans lui. Aucun GO, aucune recommandation d'achat.
