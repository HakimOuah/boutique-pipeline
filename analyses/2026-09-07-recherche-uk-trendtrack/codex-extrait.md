# Extrait factuel — dossier Codex UK 5 produits + concurrence approfondie (2026-09-07)

Source : `/Users/Hakim/Downloads/analyse-uk-concurrence-2026-09-07/`. Deux missions Codex :
- `2026-09-07-uk-5-produits/` — mots-clés + sourcing initial (RAPPORT.md du 7/09, avec annexe `passe-initiale/` = première passe antérieure)
- `2026-09-07-uk-concurrence-approfondie/` — concurrence et sourcing approfondis, qui **révise** la qualification initiale

Aucune interprétation ajoutée. Chiffres et citations reproduits tels quels des fichiers sources nommés.

---

## 1. Les 5 candidats Codex

### 1.1 Abayas ouvertes brodées

**a) Volumes** (source : `MOTS-CLES.md`, `totaux-mots-cles-uk.csv`, `mots-cles-a-cibler.csv`)
8 mots-clés retenus. Somme brute/mois **44 940**. Total prudent/mois **37 000**. Sans les racines génériques principales **3 900**.

| Mot-clé | Volume/mois UK | Phase |
|---|---:|---|
| abaya | 33 100 | EXPLORATION |
| abaya for women | 5 400 | EXPLORATION |
| abaya online | 480 | EXPLORATION |
| embellished abaya | 1 000 | COEUR |
| embroidered abaya | 880 | COEUR |
| ladies open abaya | 590 | COEUR |
| open abaya | 2 900 | COEUR |
| womens open abaya | 590 | COEUR |

**b) Sourcing AliExpress** (source : `sourcing-aliexpress.csv`, `RAPPORT.md`)

| Produit | product_id | sku_id | Variante | Achat | Fret | Coût livré GBP | Délai | Stock | Prix de vente hypothèse | Limites |
|---|---|---|---|---:|---:|---:|---|---:|---:|---|
| Abaya ouverte noire | 1005008650101896 | 12000046096249126 | Black Cardigan / M | £29.39 | £0.00 | **£29.39** | 6–13 j | 100 | £79.90 | Cardigan seul ; broderie et ouverture vues sur photo ; pas de hijab/tenue mannequin inclus présumés |
| Abaya bordeaux ornée (alternative occasion) | 1005012235894439 | 12000057817723897 | Burgundy / M | £27.89 | £1.99 | **£29.88** | 6–10 j | 8 | £89.90 | Contradiction ouverture dans les propriétés ; contenu robe/cape à vérifier ; landing occasion seulement, mots-clés hors total initial |

Approfondissement (`SOURCING.md`, `sourcing-verifie-api.csv`) — alternative supplémentaire testée : Abaya alternative noire, product_id 1005009404700712, sku 12000048996914221, £15.29 + £12.63 = **£27.92** livré, stock 299, délai 6–13 j. Réserve : « 0 vente déclarée ; coupe, broderie et tableau de tailles à confirmer ; champ 107 cm ambigu, non interprété ».

**c) Concurrents relevés**

Passe initiale (`RAPPORT.md`, tableau concurrence) : AbayaButh (poignets brodés, £94.99, indisponible/précommande au contrôle), Abaya Elegance (£39.99). Shopify : oui. Indice dropship : « Forme générique comparable ; fulfillment non prouvé ». Preuve Search : annonce AbayaButh/JZB Enterprises LTD, texte et sitelinks abayas ouvertes/luxe.

Approfondissement (`CONCURRENTS-MODE.md`, `concurrents-mode.csv`, `RAPPORT.md`) — 3 concurrents mode inspectés en détail :
- **Abayas Boutique** (abayasboutique.com) : Affiya Bridal Cape Abaya Set – White, 3-piece bridal set, £100.00. Catalogue : 12 entrées Product JSON-LD sur la 1re page + pagination. Plateforme : WooCommerce (pas de marqueur Shopify). SERP organique : #1 sur les deux snapshots (buy abaya uk / abaya dress uk). Search library : « 40102 No Search Results for domain snapshot ; absence of result is not absence of campaigns ».
- **HAWAA** (hawaaclothing.com) : Dusky Plum Spanish Sleeve Abaya, £49.00 sale / £55.00 regular. 12-14 produits visibles. Shopify confirmé (shop/myshopify/cdn.shopify.com). SERP : #2 buy abaya uk, #5 abaya dress uk. Search library : **21 créatifs** (1 août–7 sept 2026).
- **AbayaButh** (abayabuth.com) : Luxury Stardust Veil Three Piece Abaya Set – Midnight Noir, £159.99. 73 URLs produit uniques sur la 1re page, pagination jusqu'à ?page=11. Shopify confirmé. SERP : #8 buy abaya uk, #7 abaya dress uk. Search library : **19 créatifs**.

Nombre d'annonces Search trouvées par domaine : Abayas Boutique = 0 résultat (non concluant) ; HAWAA = 21 ; AbayaButh = 19.

**d) Verdict final de Codex après approfondissement** (`RAPPORT.md`, tableau « Les cinq candidats et la décision ») :
> « À approfondir en priorité sur une coupe précise ; comparaison avec de vraies abayas premium et sets, pas avec leurs accessoires »

Citation complémentaire du corps du rapport :
> « Un cardigan AliExpress seul ne peut pas être présenté comme équivalent à un ensemble complet. […] AbayaButh : 1 187 produits et 154 000 visites mondiales estimées, mais les meilleures ventes affichées sont d'abord des accessoires. Ce trafic ne prouve pas la vente d'abayas premium. »

**e) Saisonnalité Q4** (`trends-q4-summary.json`, ratio Q4 / jan-sept, UK) :
| Année | Ratio |
|---|---:|
| 2023 | ×0.717 |
| 2024 | ×0.645 |
| 2025 | ×0.743 |

Note du rapport : « L'abaya n'a pas de pic Q4 récurrent ; sa demande suit plutôt Ramadan/Eid. »

---

### 1.2 Corsets noirs structurés

**a) Volumes** (source : `MOTS-CLES.md`, `totaux-mots-cles-uk.csv`)
14 mots-clés retenus, deux coupes (overbust / underbust). Somme brute/mois **47 020**. Total prudent/mois **44 290**. Sans les racines génériques principales **3 090**.

| Mot-clé | Volume/mois UK | Phase | Groupe |
|---|---:|---|---|
| black overbust corset | 30 | COEUR | overbust |
| overbust corset | 390 | COEUR | overbust |
| black satin underbust corset | 10 | COEUR | underbust |
| black underbust corset | 210 | COEUR | underbust |
| under breast corset | 1 900 | COEUR | underbust |
| underbust corset | 1 900 | COEUR | underbust |
| black boned corset | 40 | COEUR | steel-boned |
| black corset | 8 100 | EXPLORATION | black-head |
| black satin corset | 210 | COEUR | satin |
| black steel boned corset | 10 | COEUR | steel-boned |
| boned corset | 320 | COEUR | steel-boned |
| corset | 33 100 | EXPLORATION | corset-head |
| satin corset | 480 | COEUR | satin |
| steel boned corset | 320 | COEUR | steel-boned |

**b) Sourcing AliExpress** (`sourcing-aliexpress.csv`, `SOURCING.md`)

| Produit | product_id | sku_id | Variante | Achat | Fret | Coût livré | Délai | Stock | Vente envisagée | Limites |
|---|---|---|---|---:|---:|---:|---|---:|---:|---|
| Corset noir underbust satin, 18 baleines déclarées | 1005007308979912 | 12000040189579875 | Black / M | £18.89 | £1.99 | **£20.88** | 4–8 j | 16 | £79.90 | Tableau M taille 65–70 cm, poitrine 85–90 cm ; matière/acier déclarés, échantillon non testé ; autres tailles à vérifier séparément |
| Corset noir overbust satin long | 1005011724345711 | 12000056361525782 | black / M | £18.29 | £1.99 | **£20.28** | 6–10 j | 11 | £89.90 | Photo longue jusqu'aux hanches. Tableau M taille 70–75 cm, poitrine 85–90 cm ; ne pas copier la mesure poitrine dans la colonne taille. Acier déclaré sans nombre |

Alternative testée en approfondissement (`SOURCING.md`) : Corset underbust alternatif, product_id 1005007463741144, sku 12000040858765475, £12.19 + £9.26 = **£21.45**, stock 989, délai 6–13 j. Réserve : « 4 ventes ; acier déclaré ; photo et qualité non validées physiquement ».

**c) Concurrents relevés**

Passe initiale : Corset Story (overbust orné) £125 + £9.95 express ; Luxe Noir (underbust brocart) $129 USD, livraison mondiale gratuite. Shopify : oui. Indice dropship : « Expédition usine Inde déclarée chez Corset Story ; Luxe Noir se présente comme fabricant. Ce n'est pas une preuve de drop AliExpress ». Preuve Search : annonce texte Luxe Noir, corsets acier, dernière diffusion 29 août.

Approfondissement (`CONCURRENTS-MODE.md`, `concurrents-mode.csv`) — 3 concurrents corsets détaillés :
- **Corset Story** (corset-story.co.uk) : Lace and bead Embellished Corset Overbust ND-118, £125.00 sale / £298.00 regular. 40 URLs produit uniques + pagination jusqu'à ?page=19. Shopify confirmé. SERP : #1 buy corset uk, #8 steel boned corset uk. Promo « 4 for £125 ». Livraison : « Express FedEx/UPS/DHL £9.95, direct from factory India ». Search library : « 40102 No Search Results ; do not infer no campaign ».
- **True Corset** (truecorset.co.uk) : Playgirl Faith Black Waist Training 24 Steel Boned Corset Cincher, £55.95 sale / £90.00 regular. 48 URLs produit + collection annonçant 152 produits. Shopify confirmé. SERP : #2 buy corset uk, #1 steel boned corset uk. Promo « 3 corsets £120 ». Search library : « 40102 No Search Results ».
- **What Katie Did** (whatkatiedid.com) : Demi Corset L4100, £147.50, page en PRE-ORDER au 11 sept 2026. 14 produits JSON-LD uniques. Shopify confirmé. SERP : #3 buy corset uk, #2 steel boned corset uk. Search library : **1 créatif** (CR07943506494572462081, dernière diffusion 2026-09-06 16:59:46 UTC).

Autre repère cité (`RAPPORT.md`) : Luxe Noir, benchmark $119–129, trafic « surtout américain (79 %, UK 8 %) ».

Nombre d'annonces Search trouvées : Corset Story = 0 (non concluant) ; True Corset = 0 (non concluant) ; What Katie Did = 1.

**d) Verdict final de Codex après approfondissement** :
> « À resserrer : concurrents spécialistes et promotions multiachat réduisent l'écart de prix apparent »

Citation complémentaire :
> « Le copy vend une construction précise, un ajustement et un style ; il faut comparer les baleines, le patron et le maintien, pas seulement une silhouette noire. Les promesses de réduction du tour de taille sont des revendications concurrentes, pas des bénéfices validés pour notre source. »

**e) Saisonnalité Q4** (`RAPPORT.md`, tableau Q4 de la mission 5-produits — pas de fichier JSON séparé retrouvé pour corset) :
| Terme | 2023 | 2024 | 2025 |
|---|---:|---:|---:|
| corset | ×1.06 | ×1.28 | ×1.24 |

---

### 1.3 Coffrets et remontoirs de montres (univers, deux offres)

**a) Volumes** (source : `MOTS-CLES.md`, `totaux-mots-cles-uk.csv`)
26 mots-clés retenus. Somme brute/mois **37 800**. Total prudent/mois **19 250** (coffret **9 970** + remontoir **9 280**). Sans les racines génériques principales **4 550**. Aucune des deux offres ne dépasse seule 15 000.

Coffret (`coffret-10`) :
| Mot-clé | Volume/mois | Phase |
|---|---:|---|
| 10 slot watch box | 70 | COEUR |
| 10 watch box | 90 | COEUR |
| watch box | 8 100 | EXPLORATION |
| watch storage box | 1 300 | COEUR |
| wooden watch box | 480 | COEUR |
| wrist watch storage box | 1 300 | COEUR |

Remontoir (`remontoir-double`) :
| Mot-clé | Volume/mois | Phase |
|---|---:|---|
| auto watch winder | 2 400 | COEUR |
| automatic watch winder | 2 400 | COEUR |
| automatic wrist watch winder | 2 400 | COEUR |
| best double watch winder | 20 | COEUR |
| best watch winder | 260 | EXPLORATION |
| double automatic watch winder | 20 | COEUR |
| double watch winder | 260 | COEUR |
| dual watch winder | 90 | COEUR |
| electric watch winder | 20 | COEUR |
| recommended watch winder | 260 | EXPLORATION |
| self winding watch winder | 2 400 | COEUR |
| twin watch winder | 20 | COEUR |
| two watch winder | 20 | COEUR |
| watch winder | 6 600 | EXPLORATION |
| watch winder 2 watches | 90 | COEUR |
| watch winder dual | 90 | COEUR |
| watch winder for 2 watches | 90 | COEUR |
| watch winder for two watches | 20 | COEUR |
| watch winders for automatic watches | 2 400 | COEUR |
| wrist watch winder | 6 600 | EXPLORATION |

**b) Sourcing AliExpress** (`sourcing-aliexpress.csv`, `SOURCING.md`)

| Produit | product_id | sku_id | Variante | Achat | Fret | Coût livré | Délai | Stock | Vente envisagée | Limites |
|---|---|---|---|---:|---:|---:|---|---:|---:|---|
| Coffret finition bois, 10 coussins individuels | 32839469711 | 12000032606672986 | Style 2 | £35.09 | £5.35 | **£40.44** | 6–13 j | 39 857 | £99.90 | 29.8×20.5×10.5 cm déclarés ; couvercle opaque, serrure, 10 coussins vus. Bois/matériaux mixtes ; essence et bois massif non prouvés. Style 1 est différent |
| Remontoir double USB-DC, finition PU noire | 1005008107024816 | 12000043796914430 | W135B Black / China Mainland | £33.49 | £0.00 | **£33.49** | 6–13 j | 9 957 | £99.90 | Deux coussins, boîtier noir PU avec fenêtre. USB-DC déclaré ; câble et prise secteur inclus non confirmés. Garantie 60j distincte de l'estimation 6–13j |

Alternative testée en approfondissement (`SOURCING.md`) : Remontoir 3 emplacements alternatif, product_id 1005008970862209, sku 12000047413849598, £26.69 + £1.99 = **£28.68**, stock **1**, délai 6–10 j. Réserve : « Format différent ; stock 1 : pas une seconde source équivalente du double ». Le rapport initial mentionne aussi un « premier modèle à £30.68 » avec seulement deux unités en stock, écarté comme solution de secours.

**c) Concurrents relevés**

Passe initiale : Aevitas coffret dix montres £206 ; Aevitas remontoir simple £239 actif. Shopify : oui. Indice dropship : « Produits de même famille, construction premium différente ; fulfillment non prouvé ». Preuve Search : annonces coffrets et remontoirs (Single/Double), previews lus.

Approfondissement (`CONCURRENTS-TECHNIQUES.md`, `concurrents-techniques.csv`) — 3 concurrents montres :
- **JQueen Watch Winders** (jqueenwatchwinders.co.uk) : catalogue filtrable 2/5/6/10/12/20 montres, prix visibles £119.99–£239.99. Plateforme indéterminée. Ads Search : aucun résultat.
- **Mozsly** (mozsly.com) : ~12 variantes de remontoirs doubles. Page à $159.99 ; Shopping UK a observé un produit Mozsly à **£118.37**. Shopify détecté. Ads Search : **10 créatifs**, annonceur « 广州比劲网络科技有限公司 ».
- **Rapport London** (rapportlondon.com) : 5 références, Evolution Double Frame £175 (cadre/accessoire, pas un remontoir complet), modèles à £935–£1 045. Shopify détecté. Ads Search : **19 créatifs**, « M.A.Rapport & Co Ltd ».

Prix Shopping supplémentaires cités dans `RAPPORT.md` (approfondi) : « wooden watch box » — Amazon SONGMICS 10 places £21.99, F.Hinds £19.99, MANGO £35.99, Next £19 (formats différents) ; « double watch winder » — F.Hinds £104.99, B&Q £57.99, plusieurs vendeurs Amazon entre £24.99 et £120.85.

Nombre d'annonces Search trouvées : JQueen = 0 ; Mozsly = 10 ; Rapport London = 19.

**d) Verdict final de Codex après approfondissement** :
> « À écarter sur les génériques selon ton filtre grandes enseignes ; les deux demandes ne forment pas un produit unique »

Citation complémentaire :
> « Aevitas prouve un positionnement premium, pas la possibilité de vendre n'importe quelle boîte au même prix. […] Ces alternatives doivent peser davantage que le seul plafond premium d'Aevitas. Le coffret API à £40.44 et le double remontoir à £33.49 ne constituent pas encore une offre différenciée face à ces résultats. »

**e) Saisonnalité Q4** (`trends-montres-ratios.json`) :
| Terme | 2023 | 2024 | 2025 |
|---|---:|---:|---:|
| watch winder | ×1.226 | ×1.301 | ×1.295 |
| watch box | ×1.262 | ×1.297 | ×1.563 |

(Le tableau du `RAPPORT.md` arrondit à ×1.23/×1.30/×1.30 pour watch winder et ×1.26/×1.30/×1.56 pour watch box.)

---

### 1.4 Détecteur adulte TX-850

**a) Volumes** (source : `MOTS-CLES.md`, `totaux-mots-cles-uk.csv`)
14 mots-clés retenus. Somme brute/mois **64 450**. Total prudent/mois **36 230**. Sans les racines génériques principales **9 130**.

| Mot-clé | Volume/mois UK | Phase |
|---|---:|---|
| beginner metal detector | 390 | COEUR |
| best metal detector | 1 300 | EXPLORATION |
| best metal detector for beginners | 590 | EXPLORATION |
| best metal detector uk | 880 | EXPLORATION |
| best starter metal detector | 590 | EXPLORATION |
| buy metal detector | 210 | COEUR |
| metal detector | 27 100 | EXPLORATION |
| metal detector adults | 140 | COEUR |
| metal detector for adults | 140 | COEUR |
| metal detector for beginners | 390 | COEUR |
| metal detector price | 320 | EXPLORATION |
| metal detector uk | 2 900 | EXPLORATION |
| metal detectors | 27 100 | EXPLORATION |
| metal detectors for sale | 2 400 | COEUR |

**b) Sourcing AliExpress** (`sourcing-aliexpress.csv`, `SOURCING.md`)

| Produit | product_id | sku_id | Variante | Achat | Fret | Coût livré | Délai | Stock | Vente envisagée | Limites |
|---|---|---|---|---:|---:|---:|---|---:|---:|---|
| Détecteur adulte TX-850, sans casque | 1005006994695803 | 12000038984545060 | TX-850 | £82.39 | £1.99 | **£84.38** | 4–8 j | 5 | £149.90 | Photo adulte avec canne, accoudoir, LCD, disque 11 pouces. Pile 9 V non incluse ; disque déclaré étanche, boîtier non étanche. Ne pas promettre 2,5 m de profondeur ni sac/casque. Prix concurrent exact £109.99–£155.99 : marge la plus fragile |

Alternative testée en approfondissement (`SOURCING.md`) : TX-850 alternatif, product_id 1005006003820202, sku 12000035270477888, £100.19 + £1.99 = **£102.18**, stock 4, délai 4–8 j. Réserve : « 464 ventes déclarées ; plus cher ; ne pas reprendre profondeur marketing 2,5m ».

**c) Concurrents relevés**

Passe initiale : GadgetShack TX-850 £134.99 ; Garegear TX-850 £109.99 ; Quildinc TX-850 £290.99. Shopify : oui pour Quildinc, autres plateformes distinctes. Indice dropship : « **Indice fort** sur Quildinc : même modèle générique et origine Chine ; Garegear expose aussi une référence AliExpress. Fulfillment non prouvé ». Preuve Search : annonce Spin a Disc, détecteurs, lue le 7 septembre — « ne prouve pas une campagne TX-850 ».

Approfondissement (`CONCURRENTS-TECHNIQUES.md`, `concurrents-techniques.csv`) — 3 concurrents techniques :
- **GadgetShack** : TX-850 £134.99, 5 en stock affiché. Plateforme indéterminée. Ads Search : aucun résultat. Dates de livraison affichées (24–29 juillet 2026) périmées.
- **Garegear** : TX-850 £109.99 (au lieu de £196.04), 26 avis. WooCommerce détecté. Ads Search : aucun résultat.
- **UK Metal Detectors** : comparable spécialiste, produits ~£79.95 à £3 499, aucun TX-850 exact observé. WooCommerce détecté. Ads Search : aucun résultat.

Nombre d'annonces Search trouvées : GadgetShack = 0 ; Garegear = 0 ; UK Metal Detectors = 0 (les trois « indéterminés », pas preuve d'absence).

**d) Verdict final de Codex après approfondissement** :
> « À écarter du premier test : prix exact £109.99 chez Garegear et grandes enseignes sur le générique »

Citation complémentaire :
> « Le même modèle apparaît chez Garegear à £109.99 et GadgetShack à £134.99. L'écart arithmétique entre £109.99 et le coût API livré £84.38 n'est que £25.61 avant fiscalité, frais, retours et publicité : ce n'est pas une marge nette ni un CPA disponible. »

**e) Saisonnalité Q4** : aucun ratio Trends spécifique au « metal detector » ou « TX-850 » n'a été retrouvé dans `trends-q4-summary.json` ni `trends-montres-ratios.json` (ces fichiers couvrent chess set, watch box, watch winder, abaya, et des candidats hors sélection finale). Pas de tableau Q4 dédié au détecteur dans `RAPPORT.md`.

---

### 1.5 Jeu d'échecs pliant en bois (39 cm)

**a) Volumes** (source : `MOTS-CLES.md`, `totaux-mots-cles-uk.csv`)
11 mots-clés retenus. Somme brute/mois **34 370**. Total prudent/mois **17 460**. Sans les racines génériques principales **2 660**.

| Mot-clé | Volume/mois UK | Phase |
|---|---:|---|
| beginner chess set | 110 | COEUR |
| chess set | 14 800 | EXPLORATION |
| chess set for adults | 70 | COEUR |
| chess sets | 14 800 | EXPLORATION |
| foldable chess set | 210 | COEUR |
| folding chess set | 210 | COEUR |
| portable chess set | 320 | COEUR |
| wooden chess set | 1 900 | COEUR |
| wooden chess sets | 1 900 | COEUR |
| wooden folding chess set | 40 | COEUR |
| wooden portable chess set | 10 | COEUR |

**b) Sourcing AliExpress** (`sourcing-aliexpress.csv`, `SOURCING.md`)

| Produit | product_id | sku_id | Variante | Achat | Fret | Coût livré | Délai | Stock | Vente envisagée | Limites |
|---|---|---|---|---:|---:|---:|---|---:|---:|---|
| Échiquier pliant 39cm | 1005008086495961 | 12000043641691985 | chess set | £35.19 | £1.99 | **£37.18** | 4–8 j | 10 | £79.90 | Photos set et pièces ; compte 32/34, finition, essence et lestage non certifiés ; pas de magnétisme attesté |

Alternative testée en approfondissement (`SOURCING.md`) : Échecs 39 cm 3-en-1 alternatif, product_id 1005009215859784, sku 12000048343840400, £32.79 + £6.93 = **£39.72**, stock 997, délai 6–13 j. Réserve : « 12 ventes ; 32 pièces et magnétisme déclarés ; format différent ».

**c) Concurrents relevés**

Passe initiale : Chess.co.uk set pliant bois £79.95 ; British Chess Company autre set bois £99.95. Shopify : oui. Indice dropship : « Set générique comparable ; ni même SKU ni fulfillment établis ». Preuve Search : « Annonces texte Chess & Bridge établies […] aucune annonce "wooden chess set" confirmée dans les six previews contrôlés ».

Approfondissement (`CONCURRENTS-TECHNIQUES.md`, `concurrents-techniques.csv`) — 3 concurrents échecs :
- **Regency Chess** (regencychess.co.uk) : 146 produits exposés, ~£55–£611. Plateforme non précisée. Ads Search : **5 créatifs**, dont « The Regency Chess Company T/A JDS Toys & Games Ltd ».
- **Jaques London** (jaqueslondon.co.uk) : pliant à £42.99 (ancien prix £58.99), en rupture au contrôle. Shopify détecté. Ads Search : **32 créatifs**, « John Jaques and Son Limited ».
- **Chess.co.uk / London Chess Centre** : 8 références bois visibles £75–£695, 43 produits collection pliants ; Alekhine 10×5 pouces à £49.95, en rupture. Shopify détecté. Ads Search : **36 créatifs**, « Chess & Bridge Limited ». Catalogue total 3 863 produits (livres, magazines, accessoires inclus).

Prix Shopping supplémentaires cités dans `RAPPORT.md` (approfondi) : John Lewis £35, Next £50, vendeurs Amazon ~£29–34.

Nombre d'annonces Search trouvées : Regency Chess = 5 ; Jaques London = 32 ; Chess.co.uk = 36.

**d) Verdict final de Codex après approfondissement** :
> « À écarter dans cette version générique : concurrence enseignes/spécialistes et références bon marché »

Citation complémentaire :
> « Le sourceur alternatif est un 3-en-1 à £39.72, pas un produit premium démontré. Le potentiel cadeau/Q4 ne suffit pas à compenser cette concurrence. »

**e) Saisonnalité Q4** (`trends-q4-summary.json`) :
| Année | Ratio |
|---|---:|
| 2023 | ×1.339 |
| 2024 | ×1.726 |
| 2025 | ×1.643 |

Note du rapport initial : « L'échiquier est la piste cadeau Q4 prioritaire de cette passe : produit offrable, set bois pliant, coût livré cohérent avec les prix des spécialistes et saisonnalité répétée. »

---

## 2. Candidats écartés par Codex

### Passe initiale (`annexes/passe-initiale/RAPPORT.md`)

Cette passe antérieure retenait 5 candidats différents des 5 finaux (abayas et échecs communs aux deux passes ; gilet chauffant, bodycam, vision nocturne mis en réserve puis abandonnés).

| Candidat | Motif (une ligne) |
|---|---|
| Gilet chauffant USB sans manches | Réserve initiale, jamais confirmé ; pack batterie séparée nécessaire, aucune promesse de zones/autonomie/puissance validée |
| Bodycam grand public (BOBLOV A22) | Sous 15 000 stricts (14 910 prudent) ; prix ne correspond qu'à la caméra seule, pas de pack 64 Go sourcé ; fiche concurrente citée comme A22 est en réalité une A26 (pas un comparable exact) |
| Vision nocturne numérique IR (INSKAM / GTMEDIA N4) | Sous 15 000 stricts (14 130 prudent) ; preuve Search incomplète ; fiche annonce 4K mais capteur réel 2 MP |
| CarPlay | Peu de demande UK compatible ; générique B&Q à £51.99 face au sourcing livré £54.18 |
| Télescope SV501P | Sourcing £50.48, modèle NatureQuest à £56 hors £3.99 de port ; écart insuffisant |
| Bain froid | Sourcing livré £78.19 contre Polar à £79.99 |
| Haltères réglables | Le fret de la variante complète détruit l'économie ; ne pas retenir le prix d'une poignée seule |
| Gilet lesté | Délais contrôlés de 25–43 jours |
| Nettoyeurs ultrasons | Prises EU sur les offres rapides ou fret trop cher sur les prises UK |
| Microscopes | Offres d'entrée de gamme sous forte pression ; variante AD246SM contredite par description AD246SP et support plastique |
| Bols cristal | Demande trop faible ; offre à prix acceptable limitée à un bol avec 11–18 jours ; le vrai set contrôlé dépassait le budget |
| Diesel heater | Délai et contenu du kit insuffisamment étayés |

### Poursuite / mission 5-produits (`2026-09-07-uk-5-produits/RAPPORT.md`, section « Origine et exclusions »)

| Candidat | Motif (une ligne) |
|---|---|
| Lits/poussettes pour chiens | Délais 25–42 jours |
| Cadre numérique | Le générique concurrent coûte moins que le prix source |
| Miroir | Format non comparable |
| Caméras oiseaux/trail | Sous le seuil de demande |
| Détecteurs compacts enfants | Écartés des mots-clés adultes |
| Coffres Watchmatic (~$15 600) | Cités explicitement comme « pas une preuve de marché midticket » |

Contexte de la poursuite (même fichier) : « 124 lignes électroniques, 30 lignes animaux et des recherches thématiques ciblées, avec recoupements » examinées, sans lister individuellement chaque produit rejeté au-delà des motifs ci-dessus.

---

## 3. Les 7 profils TrendTrack lus par Codex

Source : `TRENDTRACK.md` et `trendtrack.csv` (mission concurrence approfondie).

| Shop | Domaine | Produits indexés | Visites globales estimées/mois | Variation affichée | Part UK | Google indexées | Meta actives | Bestsellers affichés | Trustpilot |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| AbayaButh | abayabuth.com | 1 187 | 154 000 | +23 % | 28 % | 54 | 35 | Bonnets de hijab, hijabs, robes intérieures ; abayas premium plus loin dans le classement | 4.5 / 232 |
| Corset Story UK | corset-story.co.uk | 963 | 19 000 | +40 % | 33 % | ND | 0 | Black Mesh Waspie Underbust ; White Cotton corset top ; Black Corset Shirt | Non disponible |
| Luxe Noir | luxenoir.com | 544 | 12 000 | -14 % | 8 % | 13 | 0 | Lianna brocade overbust ; Constellation overbust ; Danique underbust | 3.8 / 2 |
| Aevitas | aevitas-uk.co.uk | 249 | 8 000 | +37 % | 48 % | 35 | 0 | Remontoir simple carbone ; remontoir double avec rangement ; watch roll cuir vert | 4.8 / 214 |
| Spin a Disc | spinadiscmetaldetectors.com | 845 | 7 000 | -6 % | 100 % | 24 | 21 | Garrett Pro Pointer AT ; gants Garrett ; batterie RNB Power-X | 4.9 / environ 3000 |
| Quildinc | quildinc.co.uk | 25 000 | 8 000 | +32 % | 72 % | ND | ND | Classement apparemment alphabétique : pare-feu Abbey, table BARI, tableau ; « non exploitable comme preuve de ventes » | 2.2 / 85 |
| Chess.co.uk | chess.co.uk | 3 863 | 53 000 | -3 % | 26 % | 44 | ND | Abonnement CHESS Magazine ; Global Chess League ; set plastique Gambit ; Alekhine bois au rang 36 | 4.0 / 3 |

Publicité : les colonnes « Google indexées » et « Meta actives » ci-dessus sont les compteurs affichés dans le profil TrendTrack. Précisions du fichier source :
- « Ces visites sont des estimations mondiales du site entier. Le graphique se termine sur juillet ; la période du pourcentage affiché n'est pas explicitée. Les compteurs Google ne représentent ni les annonces Search actives aujourd'hui ni les dépenses. ND ne signifie pas zéro. Shopify ne prouve pas le dropshipping. »
- « AbayaButh : 35 Meta sur le profil contre 38 dans la liste. »
- « Quildinc : 25 000 peut être un plafond ; son classement semble alphabétique, donc aucun bestseller détecteur établi. »
- « Les prix TrendTrack en dollars ne sont pas repris comme prix de vente UK. »

---

## 4. Limites méthodologiques déclarées par Codex

Compilées depuis les deux rapports (`2026-09-07-uk-5-produits/RAPPORT.md` et `2026-09-07-uk-concurrence-approfondie/RAPPORT.md`) :

- Le total prudent est « une convention de screening pour réduire le double comptage, pas un nombre d'utilisateurs uniques ni une prévision d'impressions ».
- Les racines génériques (`abaya`, `corset`, `watch box`, `watch winder`, `metal detector`, `chess set`) couvrent d'autres variantes et niveaux de prix ; « les groupes très précis ne font pas seuls 15k ».
- Volumes DataForSEO en moyennes mensuelles estimées et arrondies ; CPC en USD alors que les prix produits sont en GBP.
- Cette sélection « qualifie la demande de marché, l'existence d'offres concurrentes et le début du sourcing » mais « ne prouve pas encore une rentabilité publicitaire, la qualité reçue ou le dropshipping effectif des concurrents ».
- Les devis de sourcing partent de Chine ; les délais 4–13 jours « ne sont ni des livraisons réalisées ni du stock UK ».
- Le champ de garantie AliExpress à 35/60 jours « décrit autre chose que la fenêtre estimée ».
- « Les coûts […] ne constituent pas une marge après fiscalité, paiements, retours, SAV et publicité. »
- Prix, fret et stock « devront être rafraîchis lors de la commande ».
- Les relevés organiques UK « ne certifient pas la composition des enchères Search ». Les preuves Ads Transparency établissent de vraies annonces texte, « mais ne donnent pas les mots-clés exacts achetés ni la part d'impressions des enseignes ».
- « Aucun emplacement Shopping sponsorisé n'a été établi dans ces captures. Ce sont des fiches produits observées ; leur présence ne prouve pas que ces marchands achètent ce mot-clé. »
- « Les résultats organiques ne doivent pas être étiquetés Search payant. »
- Les contrôles de bibliothèque publicitaire (nombres de créatifs) « concernent les résultats renvoyés par les contrôles de domaines ; ils ne sont ni les campagnes actives ni les annonces apparues simultanément sur nos mots-clés ».
- « Les contrôles sans résultat (notamment GadgetShack et Garegear) restent indéterminés » — absence de résultat n'est pas preuve d'absence de campagne.
- « Shopify est confirmé pour [9 marchands] […] Pourtant plusieurs sont des spécialistes ou marques établies. » Corset Story annonce une expédition depuis son usine en Inde : « c'est un indice de livraison directe, pas la preuve d'une revente AliExpress. » Conclusion : « aucun concurrent n'est certifié "drop AliExpress" sur la seule base de ces contrôles. »
- Chiffres TrendTrack non exhaustifs : « ne représentent pas des commerçants uniques ni une recherche exhaustive de tout TrendTrack. »
- « Les fichiers intermédiaires sont des preuves de travail, parfois corrigées. Ce rapport et les CSV finaux font foi pour cette mission. »
- Aucune commande fournisseur, aucun contact fournisseur, aucun lancement publicitaire effectué dans les deux missions.
- Volumes de la mission approfondie « repris de la première étude, non remesurés ici. Ils incluent des mots-clés génériques et ne sont pas la demande du SKU exact. »

---

## 5. Filtres TrendTrack utilisés par Codex

Source : `etat-recherche.json` (mission 5-produits) et section « Origine et exclusions » de `2026-09-07-uk-5-produits/RAPPORT.md`.

**Passe initiale élargie (`filters_initial`)**
- Marché : GB principal puis parmi les marchés
- Pixel inclus : Google Ads
- Pixel exclu : Meta
- Prix bestseller minimum : 80 USD
- Lignes examinées : 348

**Passe étendue (`filters_expanded`)**
- Marché : GB principal
- Pixel inclus : Google Ads
- Pixel exclu : aucun (Meta réintégré)
- Prix bestseller minimum : 80 USD
- Lignes examinées : 268 (recoupements avec la passe initiale, pas 616 lignes uniques)

**Dernier élargissement, corsets et Aevitas (`filters_final_expansion`)**
- Marché : GB parmi les marchés
- Meta exclu : non (`meta_excluded: false`)
- Google inclus : non (`google_included: false`)
- Prix bestseller minimum : 80 USD
- Usage : « corsets et recoupement Aevitas »

Description narrative correspondante (`RAPPORT.md`) : « TrendTrack a été parcouru dans Chrome avec UK, Google inclus et Meta exclu, bestseller minimum proche de $80, puis avec les élargissements autorisés : UK parmi les marchés, Meta autorisé, enfin retrait du pixel Google pour les corsets et le recoupement Aevitas. »

Mission approfondie (`RAPPORT.md`) : sept profils TrendTrack lus directement (liste section 3), sans nouveau filtre de balayage décrit — lecture ciblée des fiches shop déjà identifiées.
