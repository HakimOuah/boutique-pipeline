# Sourcing AliExpress — sauna portable à vapeur (tente + générateur) — UK — 07/09/2026

Rôle : oh-sourcing. Base : `prequalification-q4.md` §5 (`REVIEW_PREQUALIFICATION`), candidat validé par l'orchestrateur pour due diligence sourcing exploratoire. Toutes les commandes ont été exécutées en premier plan, séquentiellement, via `codex-chasse-clusters/tools/aliexpress_vps_gateway.py`.

## 1. Journal

| # | Appel | Résultat |
|---|---|---|
| 1 | `variants 1005004832943506` | SMARTMAK Official Store (CN) — « Ensemble sauna vapeur domestique, pot 4L, spa 1 personne, télécommande » — 27 ventes, `offer_sale_price` 159,69 € (liste 290–312 €, ratio ~×1,8). Propriété unique : Couleur (8 coloris). Aucune propriété « Expédié depuis » sur cette fiche. |
| 2 | `variants 1005010499215588` | YourGlobal Shopper Store — « Sauna vapeur 1350W, kit tente pliable » — 14 ventes, 139,39 €. SKU unique **Expédié depuis Allemagne**. |
| 3 | `variants 1005010143241544` | SMARTMAK Official Store (CN) — « Ensemble sauna portable, cuiseur vapeur 3L + télécommande » — 37 ventes, 74,99 € (liste 127,10 €, ratio ~×1,7). 5 coloris, aucune propriété d'expédition sur la liste variants. |
| 4 | `variants 1005009439998335` | Worldly Collective Store (DE) — « Sauna pliable 2,6L, 9 températures » — 11 ventes, 73,46 €. 4 SKU **Italie / France / Espagne / Allemagne** uniquement. |
| 5 | `variants 1005009920141915` | PUMICATE HUB Store (FR) — « Tente 9 températures, générateur 1000W 2,6L » — 14 ventes, 121–133 €. SKU **France / Allemagne** uniquement. |
| 6 | `variants 1005010064889642` | PUMICATE SPACE Store (FR) — « Ensemble 1000W, pot 3L » — 13 ventes, 135,15 €. SKU **Allemagne / France** uniquement. |
| 7 | `variants 1005010676828168` | SMARTMAK Official Store (CN) — « Sauna infrarouge lointain, panneau 660nm » — 33 ventes, 181,69 € (liste 288,40 €). **SKU unique sans propriété** (pas de couleur, pas d'expédition affichée). |
| 8 | `variants 1005006250679265` | Jings Outdoor Store (CN) — « Sauna extérieur, grande fenêtre, bouche de cheminée, tente de pêche » — 17 ventes, 107–137 €. 2 SKU **China Mainland**. Titre et propriétés ne mentionnent aucun générateur vapeur (bouche de cheminée = poêle à bois non fourni) → **tente seule, hors périmètre** (consigne : écarter les tentes seules sans générateur). |
| 9 | `exact 1005010143241544 --property "Couleur=Bleu" --destination GB` | Succès. Fret `CAINIAO_STANDARD_HEAVY`, gratuit, `ship_from_country` **CN**, délai 10–41 j (fenêtre 17/09–18/10). |
| 10 | `exact 1005004832943506 --property "Couleur=MARRON" --destination GB` | Succès. Même transporteur, mêmes conditions : gratuit, CN, 10–41 j. |
| 11 | `exact 1005010676828168 --property "x=y" --destination GB` | `qualification_refused` — aucune propriété à faire correspondre (SKU sans attribut). |
| 12 | `exact 1005010676828168 --property "" --destination GB` | `invalid_request` — property vide refusée par l'outil. **Fret non confirmable pour ce produit** (limite outil, pas limite de conformité). |
| 13–17 | `search` (5 requêtes : « sauna tent generator », « sauna pliable vapeur », « tente sauna générateur » ×2 tris, « sauna vapeur 1350W », « portable sauna 2 person steam generator », « SMARTMAK sauna », « sauna tente chaise pliante télécommande ») | Aucune requête n'a fait remonter les fiches sauna vapeur/tente ciblées : le moteur de recherche dilue sur des mots trop fréquents (« sauna », « tente », « vapeur », « portable ») et renvoie du matériel de camping, des accessoires de sauna (bonnets, thermomètres) ou du matériel de repassage vapeur. **`search` n'a rien apporté d'exploitable sur ce candidat** ; le sourcing repose donc sur les 8 identifiants déjà repérés par l'orchestrateur. |

18 appels utilisés sur le plafond de 40 (respect du délai 1 s entre appels).

**Verdict d'entrepôt** : 5 des 8 candidats sont **rejetés d'office** — SKU exclusivement UE (Allemagne, France, Italie, Espagne) refusés vers GB par la règle de qualification. Seuls les 3 candidats SMARTMAK (magasin CN) passent le filtre pays ; un seul des trois (tente extérieure grande fenêtre) est hors périmètre produit (pas de générateur). Il reste **2 candidats exact-confirmés GB** + **1 candidat fret non confirmable**.

## 2. Fiches retenues

### Fiche A — SMARTMAK « Ensemble sauna portable, cuiseur vapeur 3L + télécommande » — confiance B

- URL : https://www.aliexpress.com/item/1005010143241544.html
- Magasin : SMARTMAK Official Store (Chine) — notation magasin 4,7 communication / 4,6 conformité / 4,7 expédition (`store` object)
- Note produit : non lisible via `variants`/`exact` (limite connue de l'outil — champ toujours à 0,0/0 avis hors `search`) ; note transmise par l'orchestrateur via SERP AliExpress : **4,7**
- Ventes réelles (`sales_count`) : **37**
- Prix réel EUR/GBP : `offer_sale_price` **74,99 €** → **64,49 £** (×0,86) — prix liste affiché 127,10 € (ratio ×1,7, cohérent avec la règle « liste souvent 2× le réel »)
- Contenu lisible (titre + propriétés) : tente de sauna pliable + cuiseur vapeur 3 L + télécommande. Puissance non confirmée par une propriété structurée (absente des SKU) — seule la mention « cuiseur vapeur 3L » figure au titre. Prise/tension non spécifiée par propriété.
- Stock : 267–298 selon coloris (5 coloris)
- Variantes : 5 couleurs (noir, argent, rose, jaune, café), même prix
- Fret GB (`exact`, SKU Couleur=Bleu→noir) : transporteur **CAINIAO_STANDARD_HEAVY** (« AliExpress Shipping for Large Goods by Land »), **gratuit**, `ship_from_country` **CN**, fenêtre livrée **10–41 jours** (17/09–18/10 depuis le 07/09)
- Coût rendu GBP : **64,49 £** (fret gratuit)
- Confiance : **B** — fret et prix confirmés par `exact`, mais puissance/prise non lisibles en propriété structurée, note produit non vérifiable indépendamment, délai maximum (41 j) dépasse largement le seuil de 15 j.

### Fiche B — SMARTMAK « Ensemble sauna vapeur domestique, pot 4L, spa 1 personne » — confiance B (économiquement fragile)

- URL : https://www.aliexpress.com/item/1005004832943506.html
- Magasin : SMARTMAK Official Store (Chine) — mêmes notations magasin que fiche A (même boutique)
- Note produit : non lisible via l'outil ; note SERP transmise par l'orchestrateur : **4,9**
- Ventes réelles : **27**
- Prix réel EUR/GBP : **159,69 €** → **137,33 £** — prix liste 290,35 € (ratio ×1,8)
- Contenu lisible : « ensemble sauna vapeur pour tout le corps », pot à vapeur 4 L, spa 1 personne, télécommande minuterie/température. Pas de mention de chaise pliante ni de puissance en watts dans le titre ou les propriétés ; prise non spécifiée.
- Stock : 188–296 selon coloris (8 coloris)
- Variantes : 8 couleurs, même prix
- Fret GB (`exact`, Couleur=MARRON) : identique à la fiche A — CAINIAO_STANDARD_HEAVY, gratuit, CN, 10–41 j
- Coût rendu GBP : **137,33 £**
- Confiance : **B** sur le fret/prix, mais **coût rendu quasi incompatible avec la fourchette de vente 149–199 £ visée** (voir tableau économique §3) — fiche à écarter en pratique sauf repositionnement > 220 £, hors du placement du dossier.

### Fiche C — SMARTMAK « Sauna infrarouge lointain, panneau 660nm » (secondaire, infrarouge) — confiance C

- URL : https://www.aliexpress.com/item/1005010676828168.html
- Magasin : SMARTMAK Official Store (Chine), même boutique que A/B
- Note produit : non lisible ; note SERP transmise par l'orchestrateur : non communiquée dans le brief pour cet identifiant
- Ventes réelles : **33**
- Prix réel EUR/GBP : **181,69 €** → **156,25 £** — prix liste 288,40 €
- Contenu lisible : sauna infrarouge lointain avec panneau lumineux rouge 660 nm, chauffage 160 °F. SKU unique, **aucune propriété exploitable** (pas de couleur, pas d'expédition affichée).
- Stock : 209
- Variantes : aucune (SKU unique)
- Fret GB : **non confirmable** — l'outil `exact` exige une correspondance `--property nom=valeur`, or ce produit n'expose aucune propriété nommée sur ses SKU ; deux tentatives (`x=y`, propriété vide) ont échoué (`qualification_refused` / `invalid_request`). Impossible d'obtenir transporteur, délai ou confirmation d'expédition GB pour cette fiche avec les outils disponibles.
- Coût rendu GBP : **non calculable** (fret manquant)
- Confiance : **C** — produit du même magasin fiable (CN) que A/B, donc probablement éligible GB, mais **aucune confirmation obtenue** ; fiche non exploitable en l'état pour une décision, à re-tester avec un outil complémentaire ou une commande manuelle du magasin avant toute suite.

### Rejetés (entrepôt UE, non exploitable vers GB)

| ID | Magasin | Entrepôt(s) | Motif |
|---|---|---|---|
| 1005010499215588 | YourGlobal Shopper Store | Allemagne | SKU unique UE → `qualification_refused` implicite vers GB |
| 1005009439998335 | Worldly Collective Store | Italie / France / Espagne / Allemagne | 4 SKU, tous UE |
| 1005009920141915 | PUMICATE HUB Store | France / Allemagne | 2 SKU, tous UE |
| 1005010064889642 | PUMICATE SPACE Store | Allemagne / France | 2 SKU, tous UE |
| 1005006250679265 | Jings Outdoor Store | China Mainland (éligible pays) | **Hors périmètre produit** : tente extérieure à bouche de cheminée (poêle à bois), aucun générateur de vapeur mentionné — exclue par la consigne « écarter les tentes seules sans générateur », indépendamment de l'éligibilité GB |

## 3. Tableau économique (TVA UK 20 %, HT = TTC / 1,2)

| Fiche | Coût rendu GBP | Prix visé TTC | HT (TTC/1,2) | Marge brute avant pub | % de la HT |
|---|---|---|---|---|---|
| A — cuiseur 3L (1005010143241544) | 64,49 £ | 149 £ | 124,17 £ | **59,68 £** | 48 % |
| A — cuiseur 3L | 64,49 £ | 179 £ | 149,17 £ | **84,68 £** | 57 % |
| B — pot 4L (1005004832943506) | 137,33 £ | 149 £ | 124,17 £ | **−13,16 £ (négatif)** | — |
| B — pot 4L | 137,33 £ | 179 £ | 149,17 £ | **11,84 £** | 8 % |
| B — pot 4L | 137,33 £ | 199 £ | 165,83 £ | **28,50 £** | 17 % |
| C — infrarouge (1005010676828168) | non calculable (fret manquant) | — | — | — | — |

Lecture : seule la fiche A dégage une marge brute robuste (48–57 % de la HT) dans la fourchette de vente visée 149–199 £, sous Firzone (289 £) / Pulsio (300 £). La fiche B n'est viable qu'au-delà de 179 £, avec une marge faible à 179 £ (8 %) — à écarter du placement 149–199 £ du dossier ; elle ne redevient confortable qu'au-dessus de 220–230 £, hors fourchette. La fiche C ne peut pas entrer dans le tableau tant que le fret n'est pas confirmé.

## 4. Réserves

- **Appareil électrique à vapeur** : générateur de vapeur (chauffe résistive) — CE/UKCA restent une **déclaration du vendeur**, non vérifiée indépendamment par cette due diligence. Aucune fiche ne mentionne de certification consultable dans les données `variants`/`exact`.
- **Prise UK non confirmée** : aucune des trois fiches SMARTMAK n'expose de propriété « Type de prise / Plug » dans ses SKU (contrairement à la règle générale mentionnée dans le brief). Expédition confirmée depuis China Mainland pour A et B — la prise livrée est vraisemblablement une prise UE/US générique nécessitant un adaptateur, à vérifier avant toute commande test ; ne pas présumer une prise UK native.
- **Aucune allégation santé formulée** dans ce document — les titres produits mentionnent « thérapie de désintoxication » et « relaxation » côté fournisseur ; à reformuler impérativement en copie boutique (détente, pas de promesse thérapeutique).
- **Délai > 15 jours** : la fenêtre de livraison confirmée pour A et B est **10 à 41 jours** (jusqu'à 18/10 depuis le 07/09) — dépasse largement le seuil de 15 jours mentionné dans le brief. C'est la réserve la plus significative du dossier.
- **Kit identique disponible sur Amazon UK** : le brief de préqualification (§5) situe déjà des tentes-sauna vapeur similaires chez B&Q (67–169 £), Homebase (130 £), The Range (71 £), et des marques DTC (Costway/Giantex) — cohérent avec la présence GSB en entrée de gamme déjà notée en phase 3. Non re-vérifié indépendamment dans ce sourcing (hors périmètre de l'agent).
- **Note produit non vérifiable** : les notes 4,9 / 4,7 mentionnées dans le brief de l'orchestrateur (issues de la lecture SERP) n'ont pas pu être recoupées par les outils `variants`/`exact` (champ toujours à 0,0/0 avis — limite connue de la passerelle). Avis à traiter en niveau B tant que non confirmés en fiche produit complète.
- **Fiche C (infrarouge) non instruite** : impossible de confirmer le fret GB avec les outils disponibles ; ne peut pas servir de base à une décision.
- **Recherche `search` improductive** : sept requêtes n'ont fait remonter aucune des fiches sauna-tente ciblées ni d'alternative pertinente — le sourcing de ce dossier repose entièrement sur les 8 identifiants pré-repérés par l'orchestrateur, pas sur une exploration élargie du catalogue.

## 5. Statut final

**FOURNISSEUR À TESTER**

Justification : la fiche A (SMARTMAK, cuiseur vapeur 3L + télécommande, 1005010143241544) dispose d'un coût rendu confirmé (64,49 £, fret gratuit CN), d'une marge brute robuste dans la fourchette de vente visée (48–57 % de la HT à 149–179 £) et de 37 ventes réelles sur un magasin correctement noté. Mais deux réserves substantielles empêchent d'aller plus loin sans vérification supplémentaire : le délai de livraison confirmé (jusqu'à 41 jours) dépasse largement le seuil de 15 jours, et la prise fournie n'est pas confirmée comme prise UK (aucune propriété structurée, expédition Chine continentale). Une commande test (échantillon) est nécessaire avant toute décision d'achat en volume, avec vérification physique de la prise, du délai réel et de la déclaration de conformité CE/UKCA du vendeur. La fiche B n'est pas retenue en l'état (marge négative ou trop faible dans la fourchette 149–179 £). La fiche C (infrarouge) reste hors décision, fret non confirmé.
