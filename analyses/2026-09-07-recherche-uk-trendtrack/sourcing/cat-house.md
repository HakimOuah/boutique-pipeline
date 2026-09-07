# Sourcing AliExpress — Abri à chat extérieur isolé / chauffé + niche à chien — UK — 07/09/2026

Candidat source : `prequalification-q4.md` §1 (`PASS_PREQUALIFICATION`, cluster UK ≈ 28 000/mois chat + complément niche chien plastique). Placement visé : abri isolé **89–129 £**, version chauffée **119–149 £**, niche chien isolée **99–149 £**. Outil : passerelle VPS AliExpress (lecture seule), destination GB, devise EUR → GBP à 0,86.

## 1. Journal des appels (19 appels, foreground, séquentiels, 1 s d'espacement)

| # | Heure UTC | Appel | Résultat |
|---|---|---|---|
| 1 | 16:32:00 | `variants 1005009960200806` | OK — Stone's Store (CN), 400 ventes, 3 SKU (S/M/L), toutes China Mainland |
| 2 | 16:32:11 | `variants 1005009428965763` | OK — daidaidog Store (CN), 23 ventes, 3 SKU (33–42 cm), pas de propriété « Expédié depuis » sur la fiche |
| 3 | 16:32:21 | `variants 1005008240500063` | OK — TUNFAN Store (CN), 16 ventes, « grotte » tissu pliable 35–45 cm, exclu (tente tissu, hors cible isolée) |
| 4 | 16:32:33 | `variants 1005006347474763` | OK — même TUNFAN Store, 3 ventes, doublon de fiche, exclu |
| 5 | 16:32:45 | `variants 1005010759559289` | OK — Stone's Store (CN), 95 ventes, « nid chaud d'hiver », 2 tailles M/L, China Mainland confirmé |
| 6 | 16:32:57 | `variants 1005010455698166` | OK — IMHABBA Official Store (CN), 80 ventes, doublon du même design (revendeur), pas de propriété « Expédié depuis » |
| 7 | 16:33:12 | `variants 1005008069981811` | OK — PawHut / **Aosom ES (EU) Store**, 18 ventes, SKU ship-from Espagne/Italie uniquement → **exclu** (`qualification_refused` vers GB, entrepôt UE) |
| 8 | 16:33:29 | `search "heated cat house" --sort-by orders` | Résultats hors-sujet (tapis de litière, jouets) — pollution confirmée |
| 9 | 16:33:47 | `search "insulated cat shelter" --sort-by orders` | Résultats hors-sujet, quasi identiques à #8 |
| 10 | 16:34:10 | `search "cat house outdoor waterproof" --sort-by price_desc` | Résultats hors-sujet (yachts, remorques, spas — catalogue générique trié prix desc) |
| 11 | 16:34:30 | `search "Aivituvin cat house" --sort-by orders` | Résultats hors-sujet, aucune fiche de la marque |
| 12 | 16:34:50 | `search "insulated dog kennel plastic" --sort-by orders` | Résultats hors-sujet (gamelles, sacs à déjections) |
| 13 | 16:35:17 | `search "cat house outdoor" --sort-by orders` | Résultats hors-sujet, quasi identiques à #8/#9 |
| 14 | 16:35:44 | `search "wooden dog house outdoor" --sort-by orders` | Résultats hors-sujet (jouets, laisses) |
| 15 | 16:37:32 | `search "cat igloo heated" --sort-by orders` | Résultats hors-sujet — 7e requête, même pollution |
| 16 | 16:36:03 | `exact 1005009960200806` (Taille=M, Couleur=GRIS, Expédié depuis=China Mainland) | OK — fret confirmé, CN, 26–43 j (colis surdimensionné) |
| 17 | 16:36:33 | `exact 1005010759559289` (Taille=M 50X40X36CM, Couleur=noir, Expédié depuis=China Mainland) | OK — fret confirmé, CN, 6–10 j |
| 18 | 16:36:48 | `exact 1005010759559289` (Taille=L 55X45X40CM, Couleur=noir, Expédié depuis=China Mainland) | OK — fret confirmé, CN, 4–8 j, mais stock = 1 |
| 19 | 16:37:06 | `exact 1005009428965763` (Taille=36X36X36CM, Couleur=Gris clair) | OK — fret confirmé, CN, 6–10 j |

**Constat outil** : la commande `search` a été testée sur 7 formulations distinctes (anglais générique, paires de mots rares, marques PawHut/Aivituvin, tri orders et price_desc) et a renvoyé à chaque fois un lot quasi identique de produits génériques pour chats (tapis de litière, jouets, gamelles) sans aucun rapport avec la requête — y compris en triant par prix décroissant, qui a fait remonter du matériel industriel sans lien. Le moteur `search` semble ignorer la requête sur ce périmètre (abri chat / niche chien) et renvoyer un flux de meilleures ventes génériques « animaux ». Conséquence : **aucune fiche chauffée (12 V) et aucune niche à chien plastique isolée n'a pu être localisée** par cette voie — ni les 8 identifiants fournis dans la mission n'en contenaient. Ce n'est pas une preuve d'absence sur AliExpress, seulement une limite de l'outil constatée et déclarée après 7 essais (arrêt raisonné, budget d'appels non épuisé : 19/45).

## 2. Fiches retenues (2 exploitables + 1 marginale — aucune version chauffée, aucune niche chien localisée)

### A. Maison chat extérieur toutes saisons — `1005009960200806`
- URL : https://www.aliexpress.com/item/1005009960200806.html
- Magasin : Stone's Store (Chine) — communication 4,8/5, « conforme à la description » 5,0/5 [B]
- Note produit : non disponible via l'API (`rating: 0.0`, `evaluation_count: 0`) — ne pas l'inventer [confiance N/A]
- Ventes réelles : **400** [A — variants API]
- Variante visée : Taille M, Couleur GRIS, Expédié depuis China Mainland — `offer_sale_price` **35,79 €** (le `sku_price` liste 71,43 € = ~2× le prix réel) [A]
- Dimensions/matériau : titre indique isolation thermique été/hiver, base surélevée, imperméable ; matériau exact non confirmé par une propriété structurée (mousse/PE annoncé au brief non vérifié en API) [C]
- Stock : 999 (M) ; 994 (L) ; 7 (S — quasi épuisé) [A]
- Variantes : S / M / L, gris uniquement observé sur ce SKU [A]
- Fret GB (SKU M) : transporteur **AliExpress Selection Shipping for Oversized Goods**, `shipping_fee` **1,99 €**, livraison **26 à 43 jours** (fenêtre annoncée 3–20 oct.), `ship_from_country` CN [A]
- Coût rendu : 35,79 + 1,99 = **37,78 €** ≈ **32,49 £** [A]
- Réserve majeure : délai 26–43 j très supérieur au seuil de 15 j malgré des frais de port faibles — cohérence à vérifier (le tag « oversized » suggère un fret réel plus élevé que 1,99 €, à confirmer avant commande test).

### B. Nid chaud d'hiver pour chat — `1005010759559289` (meilleure fiche)
- URL : https://www.aliexpress.com/item/1005010759559289.html
- Magasin : Stone's Store (Chine) — **même magasin que la fiche A** (concentration fournisseur, cf. réserves) [B]
- Note produit : non disponible via l'API [N/A]
- Ventes réelles : **95** [A]
- Variante visée : Taille M (50×40×36 cm), Couleur noir, Expédié depuis China Mainland — `offer_sale_price` **35,79 €** [A]
- Dimensions/matériau : M 50×40×36 cm / L 55×45×40 cm, isolation thermique au sol annoncée au titre ; matériau exact (mousse/PE) non confirmé par propriété structurée [C]
- Stock : M = 291, L = **1 seule unité** (quasi épuisé) [A]
- Variantes : noir / vert / gris, tailles M et L [A]
- Fret GB (SKU M) : transporteur **AliExpress Selection Premium shipping**, `shipping_fee` **1,99 €**, livraison **6 à 10 jours** (fenêtre 13–17 sept.), `ship_from_country` CN [A]
- Coût rendu : 35,79 + 1,99 = **37,78 €** ≈ **32,49 £** [A]
- Réserve : taille L presque en rupture (stock = 1) ; produit quasi identique en design/photos à un revendeur tiers (`1005010455698166`, IMHABBA Official Store, 80 ventes, mêmes visuels) — probable même usine, à ne pas confondre en cas de rupture.

### C. Maison chat imperméable toutes saisons pliable — `1005009428965763` (candidat marginal, taille réduite)
- URL : https://www.aliexpress.com/item/1005009428965763.html
- Magasin : daidaidog Store (Chine) — communication 4,7/5 [B]
- Note produit : non disponible via l'API [N/A]
- Ventes réelles : **23** (faible, signal de validation limité) [A]
- Variante visée : Taille M (36×36×36 cm), Couleur Gris clair — `offer_sale_price` **42,39 €** [A]
- Dimensions/matériau : cube 36×36×36 cm en taille M (le plus grand, L = 42×42×42 cm, était en rupture sur `variants`), nettement plus petit que les fiches A/B ; à valider contre le besoin réel (abri extérieur pour chat adulte) [C]
- Stock : M = 99 [A]
- Variantes : S/M/L, une seule couleur observée [A]
- Fret GB : transporteur AliExpress Selection Premium shipping, `shipping_fee` 1,99 €, livraison 6–10 jours, CN [A]
- Coût rendu : 42,39 + 1,99 = **44,38 €** ≈ **38,17 £** [A]
- Réserve : dimensions sous la cible « abri isolé » du brief, ventes faibles, prix rendu plus élevé que A/B pour un volume plus petit — candidat de secours seulement.

### Écartés (audités, non retenus)
| ID | Motif |
|---|---|
| 1005008240500063 | « grotte » tissu pliable, 35–45 cm max, 16 ventes — relève de la tente tissu à écarter (brief) |
| 1005006347474763 | doublon du même TUNFAN Store, 3 ventes seulement |
| 1005010455698166 | doublon revendeur de la fiche B (mêmes visuels), 80 ventes, propriété « Expédié depuis » absente sur `variants` — non testé en `exact` (B déjà confirmé CN) |
| 1005008069981811 (PawHut) | Aosom ES (EU) Store — SKU expédiés depuis Espagne/Italie uniquement → `qualification_refused` vers GB ; prix rendu 165–194 € et dimensions 141×141×151 cm hors cible de toute façon |

## 3. Tableau économique (TVA UK 20 %, HT = TTC / 1,2)

| Fiche | Coût rendu GBP | Prix visé TTC | Prix visé HT | Marge brute avant pub |
|---|---|---|---|---|
| A — 1005009960200806 (M, gris) | 32,49 £ | 89 £ | 74,17 £ | **41,68 £** |
| A — idem | 32,49 £ | 129 £ | 107,50 £ | **75,01 £** |
| B — 1005010759559289 (M, noir) | 32,49 £ | 89 £ | 74,17 £ | **41,68 £** |
| B — idem | 32,49 £ | 129 £ | 107,50 £ | **75,01 £** |
| C — 1005009428965763 (M, gris clair) | 38,17 £ | 79 £ | 65,83 £ | **27,66 £** |
| C — idem | 38,17 £ | 109 £ | 90,83 £ | **52,66 £** |

Aucun coût de pub, de retour ou de transaction n'est inclus (hors périmètre de cet agent). Aucune fiche chauffée ni niche à chien n'a pu être chiffrée faute d'avoir localisé une offre exploitable.

## 4. Réserves

- **Recherche `search` dégradée** : 7 requêtes distinctes (génériques, marques, tri prix) ont toutes renvoyé un flux hors-sujet — impossibilité de confirmer ou d'infirmer l'existence d'une version chauffée 12 V ou d'une niche à chien plastique isolée sur AliExpress via cet outil. Une vérification manuelle (navigateur) reste nécessaire avant de conclure à leur absence.
- **Concentration fournisseur** : les deux fiches exploitables (A et B) proviennent du même magasin (Stone's Store, CN) — pas de fournisseur alternatif confirmé en cas de rupture ou de litige.
- **Stock tendu** : taille L de la fiche B à 1 seule unité ; taille S de la fiche A à 7 unités — la taille M reste correctement approvisionnée sur les deux (999 et 291).
- **Délai fiche A** : 26 à 43 jours annoncés (transporteur « colis surdimensionné »), très au-delà du seuil de 15 j malgré des frais de port affichés à 1,99 € — incohérence apparente entre le tag « oversized » et le coût du fret à vérifier avant toute commande test.
- **Isolation/matériau non vérifié en structuré** : les propriétés API ne portent que Taille/Couleur/Expédié depuis ; l'allégation « isolation thermique » ou « mousse/PE » vient uniquement du titre commercial [C], jamais confirmée par une fiche technique.
- **Note produit inaccessible** : `rating` et `evaluation_count` renvoient 0 sur les trois fiches (aucun avis API) — seules les ventes réelles (`sales_count`) servent de signal de validation.
- **Aucune version chauffée trouvée** : la déclaration électrique/CE d'un éventuel coussin chauffant 12 V (vendeur, pas Boutiques Drop) reste une réserve à traiter si une fiche chauffée est localisée plus tard.
- **Volume colis** : les dimensions (jusqu'à 55×45×40 cm) impliquent un colis volumineux — non chiffré en frais de port additionnels au-delà du `shipping_fee` API, à confirmer sur devis réel avant commande test.

## 5. Statut final

**FOURNISSEUR À TESTER**

Meilleure fiche : `1005010759559289` (Stone's Store, « nid chaud d'hiver »), coût rendu **32,49 £**, fret GB **6–10 jours**, entrepôt **China Mainland**, stock M = 291. Marge brute avant pub 41,68–75,01 £ selon le prix affiché (89–129 £). La fiche A (`1005009960200806`, même magasin) offre une économie identique mais un délai de livraison à vérifier (26–43 j annoncés). Aucune version chauffée ni niche à chien n'a pu être confirmée via l'outil de recherche, dont la pertinence s'est révélée dégradée sur ce périmètre après 7 requêtes.
