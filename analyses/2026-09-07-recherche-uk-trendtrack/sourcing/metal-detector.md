# Sourcing AliExpress — Détecteur de métaux débutant adulte (UK) — 07/09/2026

Candidat : PASS_PREQUALIFICATION §3 de `prequalification.md` — kit débutant adulte 129–169 £ (détecteur + pinpointer + pelle/pochette), sous Crawfords 170 £. Cible détecteur : disque étanche 10–11", discrimination, notch, pinpoint, LCD, réglage de sol, 3–5 modes, tige réglable, coût idéal 40–80 €. Pinpointer type GP-Pointer/Pro-Pointer 8–15 €.

Outil : passerelle VPS `aliexpress_vps_gateway.py` (lecture seule). Devise API = EUR, conversion GBP au taux **0,86**. Aucun achat, panier ni contact vendeur.

## 1. Journal des requêtes

| # | Requête | Tri | Résultats pertinents |
|---|---|---|---|
| 1 | `MD-4030 discrimination` | orders | 7 détecteurs MD-4030/MD-5030 pertinents (bruit : diodes/optocoupleurs MOC/MD homonymes) |
| 2 | `MD-4030 discrimination` | price_desc | mêmes fiches, confirme fourchette 30–38 € |
| 3 | `MD-4080 étanche` | orders | 0 pertinent — « étanche » trop fréquent, ramène produits imperméables génériques (clés USB, housses) |
| 4 | `MD-4080 étanche` | price_desc | 0 pertinent — ramène équipements industriels étanches hors sujet (piscines, robots) |
| 5 | `MD-4080 métaux` | orders | 6 pertinents : détecteur DSP haut de gamme (107 €), MD-4030 Pro (34 €), MD-4060 (48 €), GTX5030H (37 €), casque MD-6250/TX-850 (9 €) |
| 6 | `MD-4080 métaux` | price_desc | 4 pertinents : GDS2000 (238–486 €), TX-850L (137 €), T002 (295 €) — au-dessus du budget |
| 7 | `GP-Pointer pinpointer` | orders | 4 pinpointers pertinents (8–17 €) |
| 8 | `GP-Pointer pinpointer` | price_desc | 2 détecteurs complets pertinents (GX850 101 €, MT705 160 €) — trop chers pour l'étage visé |
| 9 | `TX-850 discrimination` | orders | 12+ fiches TX-850/TX850L pertinentes, fourchette large 34–137 € selon variante/pièce détachée |
| 10 | `MD-6350 bobine` | orders | 0 pertinent — référence introuvable dans le catalogue, requête à abandonner |
| 11 | `Sunpow détecteur métaux` | orders | 0 pertinent — marque absente du catalogue interrogé, ramène détecteurs muraux/fuites génériques |
| 12 | `pelle truelle détection` | orders | 0 pertinent pour une pelle dédiée détection — ramène jouets/outils de jardin génériques + 1 pinpointer de plongée (GT120, 20 €) |
| 13 | `pelle détecteur métaux serrated` | orders | 0 pertinent — outillage générique, aucune pelle de détectoriste identifiée |
| 14 | `détecteur discrimination pinpoint enfant` | orders | 5 pertinents, confirme les mêmes pinpointers + 1 alternative notée (bracelet, 17–19 €) |

**Requêtes qui marchent** : deux mots rares combinant une référence technique (MD-4030, MD-4080, TX-850, GP-Pointer) à un mot de métier (discrimination, métaux, pinpointer) — pas un mot seul, même rare, associé à un mot trop fréquent (« étanche » a pollué les requêtes 3–4). `MD-6350` et `Sunpow` n'ont ramené aucune fiche exploitable : soit absents du catalogue interrogé, soit noyés par excès de rareté.

Appels API utilisés : 14 `search` + 13 `variants` (dont 2 échecs `IOPUpstreamError` sur les product_id 1005006003757420 et 1005007636822835, retentés une fois chacun sans succès — limite déclarée pour ces deux fiches, exclues du rapport) + 6 `exact`. Total 33/45.

## 2. Fiches retenues

### DÉTECTEURS

#### D1 — TX-850 / TX-850L LCD (variante « noir ») — pick principal
- Titre listing : « Détecteur de métaux dorés TX 850 TX 850L, pièces et accessoires tels que le accoudoir/pièces de tige/unité de commande/nouveau composant de bobines »
- URL : https://www.aliexpress.com/item/1005006088594948.html
- Magasin : Green Homebuilders Inc (CN) — communication 4,7 / conformité à la description 4,8 / vitesse d'expédition 4,7 (niveau B — notes boutique, pas produit)
- Note produit (search) : 4,4/5, taux de satisfaction 87,7 % — **B**
- Ventes réelles (variants, agrégées tous SKU) : 129 — **A**
- Prix réel variante « noir / 850L LCD » (offer_sale_price) : **76,99 € ≈ 66,21 £** — **A**
- Caractéristiques lisibles : écran LCD, bobine "850L", nom commercial reprend la référence de métier TX-850 (discrimination, détection or/pièces/métal) — titre et image ne confirment pas explicitement 10–11" ni le nombre de modes — **C** pour ces détails
- Stock (SKU noir) : 41 — **A**
- Variantes : listing mélange couleurs de détecteur complet (noir 76,99 €, or 73,69 €, bleu 84,69 €, vert/rouge 66,39 €) **et** pièces détachées sous d'autres couleurs (argent 13,99 € = unité de commande seule probable, violet 17,29 €, rose 0,65 € = câble) — **réserve majeure : risque de confusion pièce détachée / kit complet, voir §4**
- Fret vers GB (SKU noir) : **gratuit** (CAINIAO_STANDARD), livraison 13–20 sept. (6–13 j) ; alternative payante CAINIAO_PREMIUM 48,82 € pour 6–11 j — **A**
- Entrepôt : Chine continentale — **A**
- Coût rendu GBP : 76,99 € + 0 € fret = 76,99 € ≈ **66,21 £**
- Images SKU : non renvoyé par l'API (seule l'image principale par variante est fournie, pas de compte d'images)

#### D2 — MD-5030 LCD étanche — alternative prix
- Titre : « Détecteur de métaux souterrains MD-5030, affichage LCD, fonction de localisation, bobine de recherche étanche haute sensibilité pour pièces de monnaie, reliques, or »
- URL : https://www.aliexpress.com/item/1005010295197503.html
- Magasin : GaugeMaster Tool Store (CN) — communication 4,5 / conformité 4,5 / vitesse 4,6
- Note (search) : 4,6/5, satisfaction 91,7 % — **B**
- Ventes réelles : 66 — **A**
- Prix variante « noir » (MD5030PH) : **39,99 € ≈ 34,39 £** — **A**
- Caractéristiques lisibles : LCD, fonction de localisation, bobine de recherche étanche haute sensibilité — coïncide avec le brief (LCD, écran, bobine étanche) — **B**, pas de mention explicite 10–11" ni nombre de modes
- Stock (SKU noir) : 6 seulement — **A** (faible, à surveiller)
- Variantes couleurs : violet 46,99 €, rose 41,99 €, argent 45,39 €, noir 39,99 €, autres non listées ici
- Fret vers GB : **31,47 €** (CAINIAO_STANDARD), livraison 13–20 sept. (6–13 j) — **A**
- Entrepôt : Chine continentale
- Coût rendu GBP : 39,99 € + 31,47 € = 71,46 € ≈ **61,46 £** (fret représente 79 % du prix produit — pénalise l'économie malgré le prix affiché bas)
- Images SKU : non renvoyé

#### D3 — MD-4030 (référence directe du brief) — réserve délai
- Titre : « MD-4030 détecteur de métaux Portable haute précision détecteur de chasseur détecteur d'or souterrain longueur de métaux réglable chercheur de trésors »
- URL : https://www.aliexpress.com/item/1005009866983478.html
- Magasin : Shop1104082084 Store (CN) — communication 4,7 / conformité 4,5 / vitesse 4,7
- Note (search) : non renvoyée pour ce SKU précis (listing sans note affichée) — **C**
- Ventes réelles : 11 — **A**
- Prix variante « Brun » (seule couleur) : **36,99 € ≈ 31,81 £** — **A**
- Stock : 864 — **A**
- Fret vers GB : 1,99 € mais **AliExpress Selection Shipping for Oversized Goods**, livraison estimée 2–19 oct. (**25 à 42 jours**) — **A**
- Coût rendu GBP : 36,99 € + 1,99 € = 38,98 € ≈ **33,52 £** (le moins cher des trois, mais délai très supérieur au seuil de 15 j — écarté du placement immédiat, gardé en réserve si un entrepôt plus proche apparaît)

#### D4 (non vérifiable) — MD-4030 « 5,0/5, 100 % satisfaction, 10 ventes » et MD-4060 « 48,67 €, 125 ventes »
- product_id 1005006003757420 et 1005007636822835 : `variants` a échoué deux fois (`IOPUpstreamError`, code 482) — prix/fret non confirmables. Repérés en `search` uniquement (confiance **C**), non intégrés au tableau économique.

#### Écarté — GTX5030H
- product_id 1005006104719989, 37 € listés en search, mais `variants` montre **stock = 0** — écarté (rupture).

#### Écarté — ANENG DM3005B « Treasure Hunter Pro »
- product_id 1005010529172659, 15,19 € — titre ne mentionne aucune taille de bobine ni écran LCD ; probablement un boîtier compact type détecteur de sécurité, pas un détecteur à disque 10–11" avec tige réglable. Écarté par prudence (ne correspond pas clairement au brief), à re-questionner seulement si D1/D2/D3 échouent en test.

### PINPOINTERS

#### P1 — pointeur GP avec bracelet et LED — pick principal
- Titre : « Nouveau détecteur de métaux portatif de haute qualité, pointeur GP, tige de positionnement étanche, détection avec Bracelet, lumières LED »
- URL : https://www.aliexpress.com/item/1005008688272536.html
- Magasin : Shop1104335460 Store (CN) — communication 4,7 / conformité 4,7 / vitesse 4,8
- Note (search) : 4,5/5, satisfaction 89,2 % — **B**
- Ventes réelles : 1000+ — **A**
- Prix variante « noir » : **9,69 € ≈ 8,33 £** — **A**
- Caractéristiques lisibles : étanche, bracelet, LED, correspond au type GP-Pointer/Pro-Pointer visé — **B**
- Stock : 826 — **A**
- Fret vers GB : 1,99 € (AliExpress Selection Premium), livraison 13–17 sept. (6–10 j) — **A**
- Coût rendu GBP : 9,69 € + 1,99 € = 11,68 € ≈ **10,04 £**

#### P2 — pointeur « Treasure Hunter » 360° — volume le plus élevé
- Titre : « Treasure Hunter – détecteur de métaux portatif, pointeur, sonde anti-rayures, repérage du métal, étanche, balayage à 360 degrés »
- URL : https://www.aliexpress.com/item/1005009477578138.html
- Magasin : Battery's Store (CN) — communication 4,7 / conformité 4,7 / vitesse 4,8
- Note (search) : 4,4/5, satisfaction 88,0 % — **B**
- Ventes réelles : 3000+ (le plus élevé du lot) — **A**
- Prix variante « Brun » : **11,89 € ≈ 10,23 £** — **A**
- Stock : 32 (plus faible que P1) — **A**
- Fret vers GB : 1,99 €, livraison 11–15 sept. (4–8 j, le plus rapide du lot) — **A**
- Coût rendu GBP : 11,89 € + 1,99 € = 13,88 € ≈ **11,94 £**

#### P3 — pointeur bracelet « 2024 amélioré » — meilleure note produit
- Titre : « Détecteur de métaux portable étanche 2024 amélioré avec bracelet, pointeur de précision II pour détection de métaux sensibles »
- URL : https://www.aliexpress.com/item/33058780213.html
- Magasin : Digger Store (CN) — communication 4,8 / conformité 4,7 / vitesse 4,9
- Note (search) : 4,7/5, satisfaction 94,7 % (meilleure du lot) — **B**
- Ventes réelles : 500+ — **A**
- Prix variante « noir » : **18,69 € ≈ 16,07 £** — **A**
- Stock : 8 (faible) — **A**
- Fret vers GB : 1,99 €, livraison 11–15 sept. (4–8 j) — **A**
- Coût rendu GBP : 18,69 € + 1,99 € = 20,68 € ≈ **17,78 £**

### PELLE / TRUELLE
**Non renvoyée.** Quatre requêtes ciblées (`pelle truelle détection`, `pelle détecteur métaux serrated`, plus les mots-clés croisés dans les recherches détecteur/pinpointer) n'ont ramené aucune pelle ou truelle spécifiquement commercialisée pour la détection de métaux (dents en dentelure, marquage profondeur). Seuls des outils de jardin génériques ou des pelles jouets sont apparus. Le kit proposé se limite donc à détecteur + pinpointer ; une pelle dédiée reste à sourcer séparément si le fournisseur test est retenu.

## 3. Tableau économique indicatif

Composition retenue pour le calcul : **D1 (TX-850, 66,21 £) + P1 (pointeur GP, 10,04 £)**, pas de pelle (non trouvée).

| Poste | Coût rendu GBP |
|---|---|
| Détecteur TX-850 (D1, franco de port CAINIAO_STANDARD) | 66,21 £ |
| Pinpointer GP (P1) | 10,04 £ |
| Pelle/truelle | non trouvée (0 £ — absente du kit) |
| **Coût rendu total du kit** | **≈ 76,25 £** |

| Prix de vente visé (TTC) | HT (÷1,2) | Marge brute avant pub | % de la HT |
|---|---|---|---|
| 129 £ (bas de fourchette brief) | 107,50 £ | 31,25 £ | 29,1 % |
| 149 £ (médian) | 124,17 £ | 47,92 £ | 38,6 % |
| 169 £ (juste sous Crawfords 170 £) | 140,83 £ | 64,58 £ | 45,9 % |

Variante avec D2 (MD-5030) au lieu de D1 : coût rendu détecteur 61,46 £ (moins cher malgré fret payant), + P1 10,04 £ = 71,50 £ total — marge légèrement supérieure, mais stock limité à 6 unités côté fournisseur (D2) contre 41 (D1).

Aucun coût de pelle inventé : absente des deux scénarios faute d'offre trouvée. Aucun coût de pochette/casque mesuré (hors périmètre des requêtes menées).

## 4. Réserves

- **Produit électronique à piles** : déclaration CE/UKCA reste une déclaration du vendeur AliExpress, non vérifiable via cette API en lecture seule — aucune fiche ne mentionne explicitement une conformité UKCA.
- **Risque revente Amazon UK sous marque chinoise** : les titres D1/D2/D3 (TX-850, MD-5030, MD-4030) sont des références génériques largement dupliquées ; probable présence des mêmes détecteurs sous marques comme « Fervor », « Ohmax » ou similaires sur Amazon UK — à vérifier en concurrence, non fait ici (hors périmètre sourcing).
- **Ambiguïté kit complet vs pièce détachée (D1)** : le listing TX-850 (1005006088594948) vend sous une même fiche des couleurs de détecteur complet et des couleurs qui semblent être des pièces détachées (unité de commande seule à 13,99 €, câble à 0,65 €) — le SKU « noir / 850L LCD » à 76,99 € est probablement le kit complet vu son prix et son stock (41), mais ceci n'est pas confirmé formellement par l'API (pas de description longue disponible) — **à vérifier impérativement par une commande test avant tout engagement volume**.
- **Stock faible** sur D2 (6 unités) et P3 (8 unités) — non adapté à un lancement à fort volume sans reconfirmation du réassort.
- **Délai > 15 j** : D3 (MD-4030 à 36,99 €, le moins cher) a un délai de 25 à 42 jours (entrepôt Chine, fret "oversized") — écarté du placement malgré son prix, sauf si un entrepôt UE/UK apparaît pour cette référence.
- **Entrepôt** : toutes les fiches retenues (D1, D2, D3, P1, P2, P3) expédient depuis la Chine continentale ; aucun entrepôt UE/UK identifié pour le détecteur ou le pinpointer dans les requêtes menées.
- **Deux fiches non vérifiables** (MD-4030 « 5,0/100 % » et MD-4060 48,67 €) faute de réponse API après deux tentatives — à retenter plus tard si D1/D2/D3 échouent en test.
- **Absence de pelle dédiée** : le kit visé par le brief (détecteur + pinpointer + pelle/truelle + pochette) n'est complet qu'à 2 éléments sur 3 avec les données obtenues ; sourcing complémentaire nécessaire avant de figer un kit de vente.

## 5. Statut final

**FOURNISSEUR À TESTER**

La fiche D1 (TX-850, 76,99 €/66,21 £ rendu, fret gratuit, stock 41) est la plus solide sur le papier, mais l'ambiguïté kit complet/pièce détachée sur ce listing précis impose une commande test avant tout engagement. D2 (MD-5030) est une alternative de repli avec un fret disproportionné. P1 (pointeur GP à 8,33 £ rendu) est fiable et cohérent avec la cible 8–15 €. Aucune pelle dédiée trouvée — le kit reste incomplet en l'état.
