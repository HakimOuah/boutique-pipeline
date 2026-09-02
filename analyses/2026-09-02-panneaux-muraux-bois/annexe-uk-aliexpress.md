# Annexe UK — sourçabilité AliExpress des panneaux à tasseaux vers le Royaume-Uni (02/09/2026)

> **Contrôle exploratoire HORS pipeline**, demandé par Hakim « par pure curiosité » et transmis par l'orchestrateur. Aucun candidat n'est en `PASS_PREQUALIFICATION` sur cette famille ; cette annexe ne prononce **aucun GO fournisseur** et ne commente pas la décision marché. Elle ne contient que des faits logistiques, relevés le **02/09/2026 entre 14:46 et 14:55 (heure de Paris)**. Prix, stocks et délais AliExpress sont dynamiques : tout est à reconfirmer au panier, avec une adresse britannique, avant toute commande test. Aucun achat, aucun panier, aucun contact vendeur, aucune connexion.

**Méthode.** Passerelle API lecture seule `codex-chasse-clusters/tools/aliexpress_vps_gateway.py` (health OK 14:46 ; `variants` puis `exact --destination GB`, avec témoins FR et DE pour vérifier que le paramètre pays est honoré — il l'est : TLGREEN DE→FR et DE→DE passent, GB est refusé). SERP AliExpress `/w/wholesale-acoustic-slat-wall-panel.html?shipFromCountry=UK` lue dans le navigateur intégré, JSON des cartes extrait de `window._dida_config_._init_data_.data.data.root.fields.mods.itemList.content`, pays d'expédition lu dans la trace `pdp_cdi` de chaque carte (niveau B ; « N sold » de tuile = niveau C). Les PDP `/item/` restent inaccessibles dans le navigateur intégré (plafond B+).

## 1. Les trois fiches du rapport du matin : livraison UK impossible

| Fiche | Entrepôts présents dans les variantes (API, 02/09 14:47) | `exact --destination GB` (4 × 120×60) | Témoins |
|---|---|---|---|
| [1005010510383652](https://fr.aliexpress.com/item/1005010510383652.html) TLGREEN Outdoor Store | Allemagne uniquement (2 SKU) | **Refus** `505 DELIVERY_NOT_AVAILABLE_TO_YOUR_ADDRESS` (14:47, idem avec code `UK` 14:48) | FR : 116,99 € TTC, GLS/DHL/DPD DE gratuits 3–10 j (14:48) · DE : 116,99 €, DHL/GLS domestiques gratuits 2–7 j (14:48) |
| [1005012013334317](https://fr.aliexpress.com/item/1005012013334317.html) TWISTERCK LOCAL Store | Allemagne uniquement (4 SKU) | **Refus** `505` (14:47) | — |
| [1005012482573788](https://fr.aliexpress.com/item/1005012482573788.html) Cozzar Store | Pologne uniquement (6 SKU) | **Refus** `505` (14:47) | **DE et PL refusés aussi** (14:48) : la SKU « Pologne » de cette fiche ne livre que la France — fiche ciblée FR |

**Réponse à la question 1 : non.** Aucune des trois fiches ne livre le Royaume-Uni. Leurs entrepôts allemands et polonais ne desservent pas le UK post-Brexit (la SKU est liée à une zone de livraison UE ; pour Cozzar, à la France seule). Pas de port, pas de délai, pas de prix rendu en £ à relever : l'offre n'existe pas pour une adresse britannique.

## 2. Fiches « Ships from United Kingdom » pour « acoustic slat wall panel »

**Piège méthodologique relevé.** Sur le site en contexte France (ship-to FR, EUR), le paramètre `shipFromCountry=UK` affiche bien la puce « Expédié depuis : Royaume-Uni » mais est **relâché silencieusement** : les 59 cartes rendues partaient de CN (20), PL (26), ES (9), DE (4) — zéro UK ; la requête « wood slat wall panel » donnait `totalResults: 2` et 60 cartes de remplissage hors sujet. Il a fallu forcer le contexte de site UK (cookie `aep_usuc_f=site=glo&region=UK&c_tp=GBP&b_locale=en_GB`) pour que le filtre agisse : **62 résultats, 38 cartes lues, toutes « shipFrom: UK », prix en £** (14:52).

**Réponse à la question 2 : oui, des fiches expédiées du UK existent**, mais elles sont peu nombreuses et quasi sans preuve sociale. Trois fiches tasseaux bois relevées :

| # | Fiche | Magasin (sous-notes API) | Variante contrôlée · prix 02/09 | Fret UK (API `exact`, destination GB) | Preuve sociale | Réserves |
|---|---|---|---|---|---|---|
| UK1 | [1005012012896727](https://www.aliexpress.com/item/1005012012896727.html) | **TWISTERCK LOCAL Store** (CN, id 1104728387 · 4,6 / 4,6 / 4,7) — le même vendeur que la fiche DE du matin, version entrepôt UK | `4PCs 120x60cm / Royaume-Uni` **92,69 € TTC** (API 14:53, stock 23 ; liste 319,62 € = remise artificielle) ≈ **£79** au taux implicite du site (0,85) · `2PCs 120x60cm` 61,39 € (stock 14) · `4PCs 120x30cm` 61,39 € = **£52,19 affichés en SERP** (stock 11) · `2PCs 120x30cm` 43,99 € (stock 12) | **Contradiction** : SERP « Ships from UK », mais `exact GB` **refusé** `505` trois fois (14:54, sur 4PCs et 2PCs 120×60). Fret, délai et faisabilité **non établis** par l'API | SERP 4 sold (niveau C) · API 4 ventes · 0 avis · « Early bird deal, only 3 left » contredit par stock 23 (fausse rareté) | À ouvrir en PDP dans un Chrome en contexte UK pour trancher la contradiction ; 0 avis |
| UK2 | [1005011970248727](https://www.aliexpress.com/item/1005011970248727.html) | Shop1105407148 Store (CN, id 1105407148 · 4,9 / 4,8 / 5,0) | `Oak Natural / Royaume-Uni` **132,39 € TTC** (API 14:54, stock 8) = **£112,72 affichés en SERP** (liste £117,43) · **format et nombre de panneaux non exposés par l'API** (titre : « Acoustic Slat Wall Panel … Wooden Slatted 3D Feature Panelling ») | **OK** : DX / GLS / DHL / DPD / Evri / Parcel Force / Royal Mail / Yodel, **tous gratuits, avec suivi, expédiés de GB, 2–6 j** (livraison 04–08 sept.) → **coût rendu 132,39 € ≈ £112,72** pour la variante, TVA annoncée incluse | SERP 3 sold (C) · API 2 ventes · **0 avis** | Format à lire en PDP ; magasin anonyme ; 0 avis |
| UK3 | [1005008523401970](https://www.aliexpress.com/item/1005008523401970.html) | SucceBuy Home Garden Global Store (CN · 4,7 / 4,7 / 4,8) — **produit de marque VEVOR** 1200×600 mm (rejeté ce matin sur la variante CZ à 216,39 €) | 7 « Types » (coloris non nommés) × 10 entrepôts. SKU UK : `Type 7 / Royaume-Uni` **85,69 € TTC** (API 14:54, **stock 1**) ; Types 2, 3, 5 UK 85,69 € et Types 1, 4, 6 UK 104,39–105,69 €, **stock non affiché** · SERP £73,73 | **OK** : Evri 2–5 j, Royal Mail 2–6 j, XDP 7 j, **gratuits, suivi, depuis GB** → **coût rendu 85,69 €** pour le Type 7 | SERP 4 sold, 5★ (C) · API 3 ventes · 0 avis | Marque VEVOR ; stock UK quasi nul (1) ; libellés « Type N » sans nom : contenu de la variante inconnu |

**Autres cartes UK vues dans la même SERP (non contrôlées en API) :** [1005013018779100](https://www.aliexpress.com/item/1005013018779100.html) « Sound Absorbing Wood Slat Acoustic Panels… 3D Fluted » £39,74, livraison gratuite, « only 1 left », 0 sold ; [1005013074875966](https://www.aliexpress.com/item/1005013074875966.html) « Wood Slat Acoustic Panel… Wood Veneer » £23,59, « only 1 left », 0 sold ; [1005012762231460](https://www.aliexpress.com/item/1005012762231460.html) 4 × **240×60 cm** MDF £453,37 (liste £1 462), « only 1 left », 0 sold — seul 240 cm du lot, prix hors marché ; [1005011970268684](https://www.aliexpress.com/item/1005011970268684.html) pack de 12 dalles rainurées 50×50 blanches £146,59, 0 sold (même série d'identifiants que UK2). Le reste du filtre UK est constitué de mousse acoustique, de papier peint « grain bois » autocollant et d'une **vague de ~10 fiches clones « 6 × MDF 120×40×0,6 cm » à £44–66, toutes « only 1 left », 0 sold** (ferme de fiches).

## 3. Synthèse

| Question | Réponse (02/09/2026) |
|---|---|
| Les 3 fiches DE/PL du matin livrent-elles le UK ? | **Non** — refus `505` pour les trois ; entrepôts DE/PL limités à l'UE (Cozzar : France seule) |
| Existe-t-il des fiches expédiées du UK ? | **Oui, 3 fiches tasseaux + quelques clones**, visibles uniquement en contexte de site UK |
| Meilleur point de comparaison UK pour 4 × 120×60 | UK1 TWISTERCK 92,69 € TTC ≈ £79 (vs 108,39 € la même fiche vendeur en DE→FR), **mais fret GB non confirmé par l'API** |
| Seule offre UK tasseaux avec fret vérifié | UK2 Shop1105407148, 132,39 € ≈ £112,72 rendu, 2–6 j, format inconnu, 0 avis ; UK3 VEVOR 85,69 € rendu, stock 1 |
| Preuve sociale UK | 2–4 ventes, 0 avis partout : **rien n'est au niveau « à tester »** sans ouverture PDP et sans reconfirmation panier |

**Statut (vocabulaire verrouillé, à titre indicatif hors pipeline) :** `OFFRE TROUVÉE` pour UK1, UK2, UK3 — éléments essentiels manquants (fret GB contradictoire pour UK1, format pour UK2, contenu de variante et stock pour UK3). Aucune `FOURNISSEUR À TESTER`.

## 4. Limites

- PDP inaccessibles dans le navigateur intégré (anti-bot) : % d'avis positifs vendeur, ancienneté, description, format exact de UK2 et contenu des « Types » VEVOR non lus.
- API `exact` : refus `505` stable sur la SKU UK de TWISTERCK alors que la SERP l'affiche « Ships from UK » — cause inconnue (restriction de la fiche, zone de livraison mal déclarée, ou limite de l'API pour ce vendeur). À trancher en PDP / panier avec adresse UK.
- Prix API en EUR (compte FR) ; les £ sont ceux affichés par la SERP en contexte UK ou une conversion au taux implicite du site (0,85), signalée comme telle.
- Une seule requête SERP contrôlée en contexte UK (« acoustic slat wall panel ») ; « wood slat wall panel » n'a été lue qu'en contexte France (0 fiche UK exploitable).
- Cookie de contexte UK posé dans le navigateur intégré pour la lecture ; aucune action de compte, aucun panier.

*Annexe produite par l'agent phase 4 (sourçabilité) le 02/09/2026, budget 15 min. Données brutes (`variants`, `exact`, JSON SERP) dans le scratchpad de session, non versionnées.*
