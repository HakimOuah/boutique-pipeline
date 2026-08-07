# Phase 4 sourcing AliExpress — batardeau / barrière anti-inondation pour porte

- Run ID : `brandsearch-sourcing-test-20260803-a1`
- Tentative : `a1`
- Date d'observation : 2026-08-03
- Marché de livraison : France
- Cluster : `batardeau-porte`
- Source de vérité fournisseur : AliExpress Open Platform / AE-Dropshipper via VPS Hostinger à IP autorisée
- Périmètre : lecture seule ; aucun panier, achat, message vendeur, import DSers ou mutation Shopify

## Verdict

**AUCUNE_FICHE_EXACTE**

AliExpress est accessible et la recherche a produit des annonces pertinentes. Le verdict n'est donc pas `ACCES_ALIEXPRESS_BLOQUE`.

Douze annonces actives correspondant visuellement au produit ont été récupérées puis vérifiées avec `aliexpress.ds.product.get`. Aucune ne réunit les huit gates fournisseur du rapport marché : aucune fiche ne rend la largeur et la hauteur de retenue explicitement sélectionnables, aucune preuve hydraulique vérifiable n'est exposée dans les données qualifiées et aucune ne documente ensemble joints, supports, mesure, pose, entretien, stockage, pièces d'usure, poids, colis et retours.

Trois SKU peuvent être livrés en France selon `aliexpress.logistics.buyer.freight.calculate`, mais leurs coûts rendus minimaux sont incompatibles avec le marché : **809,11 EUR**, **849,02 EUR** et **2 052,24 EUR**. Cinq autres refusent la livraison France. Quatre fiches n'exposent aucune propriété de variante permettant une sélection exacte par dimensions.

## Gate marché transmis à la phase 4

- `[OBSERVE]` Demande SEMrush France nettoyée : **12 080 recherches/mois**, dont `batardeau` à **9 900**.
- `[OBSERVE]` Prix marché observé : **240–282 EUR TTC** en entrée spécialiste ; **589–699 EUR** pour les systèmes premium/retail.
- `[OBSERVE]` Le marché exige une prise de cotes, un système de joints, des limites d'usage, une pose documentée et une preuve d'étanchéité.
- `[HYPOTHESE]` Une offre à valeur ajoutée pourrait reposer sur le diagnostic photo, le contrôle des cotes, la compatibilité du support et les pièces d'usure.
- `[MANQUANT]` CPC SEMrush France, absent du rapport de phase 3 ; aucune économie publicitaire ne doit être calculée sans lui.

### Spécification minimale obligatoire

1. barrière pour ouverture de porte, pas sac, boudin, digue au sol ni accessoire ;
2. largeur et hauteur de retenue explicitement sélectionnables ;
3. système de joint et conditions de support documentés ;
4. instructions de mesure, pose, entretien et stockage ;
5. rapport d'essai ou protocole hydraulique vérifiable ;
6. pièces d'usure ou de remplacement disponibles ;
7. poids, colis, prix rendu France, délai et politique de retour exacts ;
8. aucune promesse absolue d'absence d'inondation sans limites d'usage.

## Santé de l'accès officiel

- `[OBSERVE]` Gateway : `ok=true` à `2026-08-03T16:46:50Z`.
- `[OBSERVE]` Jeton d'accès annoncé valide jusqu'au `2026-09-01T18:29:47Z` ; refresh token jusqu'au `2026-10-01T18:09:12Z`.
- `[OBSERVE]` Les actions utilisées sont strictement read-only : `search`, `variants` et `exact`.
- `[OBSERVE]` Le tri `price_desc` ajouté au gateway a été testé et fonctionne sur des requêtes acceptées par l'amont AliExpress.

## Recherche AliExpress effectuée

| Requête | Résultat officiel | Lecture |
|---|---|---|
| `door flood barrier`, `water barrier`, `flood gate` | `NGSELECTION_SEARCH_ERROR` | Erreur amont de recherche, pas un blocage d'accès global. |
| `aluminum flooding protection barrier` | `NGSELECTION_SEARCH_ERROR` | Même erreur amont. |
| `aluminum flood barrier` | Réponse valide | Les 20 premiers résultats triés par prix sont hors sujet ; le moteur privilégie le mot `aluminum`. |
| `barrière inondation` | Réponse valide | Surtout bandes silicone, seuils de douche et sacs de sable, donc faux positifs. |
| `batardeau porte` | Réponse valide | Surtout butoirs, joints et accessoires de porte, donc faux positifs. |
| `barrière anti-inondation porte`, `protection inondation porte`, `panneau anti inondation` | `NGSELECTION_SEARCH_ERROR` | Erreur amont selon la formulation. |

Deux fiches candidates ont d'abord été découvertes publiquement, puis rejetées comme non qualifiables par la source officielle :

| Produit découvert | Signal public observé | Contrôle officiel |
|---|---|---|
| [1005011595615813](https://www.aliexpress.com/item/1005011595615813.html) — barrière aluminium empilable pour porte/garage | Pricearchive : 190,08 USD, soit 171,30 EUR indicatifs au crawl | `aliexpress.ds.product.get` renvoie le code `604` ; variante, stock et fret France non vérifiables. |
| [1005011595821310](https://www.aliexpress.com/item/1005011595821310.html) — système temporaire empilable | Pricearchive : 201,36 USD, soit 181,46 EUR indicatifs au crawl | Code officiel `604` ; variante, stock et fret France non vérifiables. |

La recherche visuelle de la première fiche a ensuite remonté douze annonces similaires. Pricearchive n'a servi qu'à découvrir leurs IDs ; toutes les informations de qualification ci-dessous proviennent de l'API officielle AliExpress.

## Tri des douze annonces actives

| ID AliExpress | Titre abrégé / vendeur | Variante exposée | Prix TTC | Stock | Livraison France | Preuve sociale |
|---|---|---|---:|---:|---|---|
| [1005009796174058](https://www.aliexpress.com/item/1005009796174058.html) | Porte de garage amovible aluminium — `Shop1105076092 Store` | `Color: MSFBA` (`raw: Argent`) | 413,39 EUR | 18 | Oui ; min. 1 638,85 EUR | 0 vente, 0 avis, note 0 ; notes vendeur manquantes |
| [1005012444388706](https://www.aliexpress.com/item/1005012444388706.html) | Barrière aluminium de protection — `Shop1105510436 Store` | `Couleur: BLANC` | 185,39 EUR | 20 | **Non**, code 505 | 0 vente, 0 avis ; notes vendeur manquantes |
| [1005012837717459](https://www.aliexpress.com/item/1005012837717459.html) | Barrière aluminium garage/porte — `Strong Combination Machinery Store` | `Couleur: Argent` | 106,99 EUR | 19 | **Non**, code 505 | 0 vente, 0 avis ; notes vendeur manquantes |
| [1005012837715666](https://www.aliexpress.com/item/1005012837715666.html) | Panneau démontable garage — même vendeur | `Couleur: Argent` | 88,39 EUR | 19 | **Non**, code 505 | 0 vente, 0 avis ; notes vendeur manquantes |
| [1005010424377660](https://www.aliexpress.com/item/1005010424377660.html) | Barrière aluminium domestique — `China Home Furnishing Super Factory Specialty Store Store` | `Couleur: white` (`raw: BLANC`) | 170,99 EUR | 20 | Oui ; min. 678,03 EUR | 0 vente, 0 avis ; notes vendeur manquantes |
| [1005011944719612](https://www.aliexpress.com/item/1005011944719612.html) | Barrière aluminium sur mesure — `Shop1105300454 Store` | `Couleur: Aluminum` (`raw: Indigo`) | 550,99 EUR | 82 | Oui ; min. 258,12 EUR | 0 vente, 0 avis ; notes vendeur manquantes |
| [1005012845316005](https://www.aliexpress.com/item/1005012845316005.html) | Barrière personnalisée maison/garage — `Strong Combination Machinery Store` | `Couleur: Argent` | 298,39 EUR | 19 | **Non**, code 505 | 0 vente, 0 avis ; notes vendeur manquantes |
| [1005011629146641](https://www.aliexpress.com/item/1005011629146641.html) | Barrière aluminium domestique — `Little Deer Selected Quality Shopping Store` | `Argent` + `Norme européenne` | 253,69 EUR | 19 | **Non**, code 505 | 0 vente, 0 avis ; vendeur 5,0/5,0/5,0 affiché |
| [1005012837729474](https://www.aliexpress.com/item/1005012837729474.html) | Barrière d'urgence pour porte — `Strong Combination Machinery Store` | Aucune propriété | 122,69 EUR | 19 | Non qualifiée : aucun sélecteur exact | 0 vente, 0 avis ; notes vendeur manquantes |
| [1005012837841105](https://www.aliexpress.com/item/1005012837841105.html) | Système de barrière porte/garage — même vendeur | Aucune propriété | 108,69 EUR | 19 | Non qualifiée : aucun sélecteur exact | 0 vente, 0 avis ; notes vendeur manquantes |
| [1005012837755344](https://www.aliexpress.com/item/1005012837755344.html) | Panneau de contrôle des crues — même vendeur | Aucune propriété | 120,99 EUR | 19 | Non qualifiée : aucun sélecteur exact | 0 vente, 0 avis ; notes vendeur manquantes |
| [1005012837763344](https://www.aliexpress.com/item/1005012837763344.html) | Barrière Hurricane ABS/aluminium — même vendeur | Aucune propriété | 108,69 EUR | 19 | Non qualifiée : aucun sélecteur exact | 0 vente, 0 avis ; notes vendeur manquantes |

`code 505` signifie `DELIVERY_NOT_AVAILABLE_TO_YOUR_ADDRESS` pour la destination France demandée.

## Fiches exactes avec fret France

### 1. 1005009796174058 — rejet

- URL : https://www.aliexpress.com/item/1005009796174058.html
- SKU exact : `12000050788932969`
- Variante : `Color: MSFBA`, valeur brute `Argent`
- Prix produit TTC : **413,39 EUR**
- Fret minimal : **1 638,85 EUR**, EMS suivi, départ Chine, 8–23 jours
- Total rendu minimal : **2 052,24 EUR**
- Stock annoncé : 18
- Produit : 0 vente, 0 avis, note 0,0
- Vendeur : notes manquantes
- `[MANQUANT]` Largeur, hauteur de retenue, poids, dimensions colis, joint, supports compatibles, notice, essai hydraulique, pièces, retours.
- Décision : **prix incompatible** et fiche technique insuffisante.

### 2. 1005010424377660 — rejet

- URL : https://www.aliexpress.com/item/1005010424377660.html
- SKU exact : `12000052368040333`
- Variante : `Couleur: white`, valeur brute `BLANC`
- Prix produit TTC : **170,99 EUR**
- Fret minimal : **678,03 EUR**, FedEx IP suivi, départ Chine, 4–21 jours
- Total rendu minimal : **849,02 EUR**
- Stock annoncé : 20
- Produit : 0 vente, 0 avis, note 0,0
- Vendeur : notes manquantes
- `[MANQUANT]` Mêmes éléments techniques et contractuels que ci-dessus.
- Décision : **prix incompatible** et fiche technique insuffisante.

### 3. 1005011944719612 — rejet

- URL : https://www.aliexpress.com/item/1005011944719612.html
- SKU exact : `12000057096751070`
- Variante : `Couleur: Aluminum`, valeur brute incohérente `Indigo`
- Prix produit TTC : **550,99 EUR**
- Fret minimal : **258,12 EUR**, EMS suivi, départ Chine, 8–23 jours
- Total rendu minimal : **809,11 EUR**
- Stock annoncé : 82
- Produit : 0 vente, 0 avis, note 0,0
- Vendeur : notes manquantes
- `[MANQUANT]` Mêmes éléments techniques et contractuels que ci-dessus.
- Décision : **prix incompatible**, variante sémantiquement incohérente et fiche technique insuffisante.

## Matrice des huit gates

| Gate | Résultat | Preuve |
|---|---|---|
| 1. Vraie barrière de porte | Partiel | Les douze titres décrivent une barrière pour porte/garage ; les bandes silicone et sacs ont été exclus. Le contenu physique exact reste insuffisamment documenté. |
| 2. Largeur + hauteur sélectionnables | **Échec** | Les seules propriétés sont couleur, modèle opaque ou norme ; quatre fiches n'ont aucune propriété. |
| 3. Joints + conditions du support | **Échec** | Non exposés dans les données qualifiées. |
| 4. Mesure, pose, entretien, stockage | **Échec** | Aucune notice vérifiable obtenue. |
| 5. Essai/protocole hydraulique | **Échec** | Aucun rapport ni protocole vérifiable obtenu. |
| 6. Pièces d'usure/remplacement | **Échec** | Aucune disponibilité documentée. |
| 7. Poids, colis, rendu France, délai, retour | **Échec** | Fret et délai exacts obtenus pour trois SKU seulement ; poids, colis et politique de retour manquent. |
| 8. Promesse limitée à l'usage prouvé | Manquant | Les titres ne suffisent pas pour vérifier toutes les promesses de la fiche. |

## Comparaison au marché, sans calcul de marge

| SKU | Total rendu France minimal | Repère marché | Écart descriptif |
|---|---:|---:|---|
| 1005009796174058 | 2 052,24 EUR | 240–699 EUR | Très au-dessus du haut de marché observé. |
| 1005010424377660 | 849,02 EUR | 240–699 EUR | Au-dessus même des systèmes retail premium observés. |
| 1005011944719612 | 809,11 EUR | 240–699 EUR | Au-dessus du haut de marché, avant tout coût opérationnel ou publicitaire. |

Les fiches à 88,39–298,39 EUR qui pourraient sembler compatibles au prix produit ne livrent pas en France ou ne permettent pas de sélectionner une dimension exacte. Elles ne peuvent donc pas servir de base économique.

## Données manquantes critiques

- `[MANQUANT]` Largeur et hauteur exactes par SKU pour les douze annonces.
- `[MANQUANT]` Matériau/alliance vérifié au-delà du titre, épaisseur des panneaux et classe des fixations.
- `[MANQUANT]` Géométrie et matière des joints, tolérance de planéité et supports interdits.
- `[MANQUANT]` Rapport d'essai hydraulique, taux de fuite, hauteur/pression maximale et cycles de réutilisation.
- `[MANQUANT]` Notice de prise de cotes, pose, entretien et stockage en français.
- `[MANQUANT]` Pièces d'usure, poids net, poids colis, dimensions colis, casse et retours.
- `[MANQUANT]` CPC Search France ; la phase 5 ne doit pas être ouverte.

## Décision pipeline

- `[FAIT]` Le marché a passé la phase 3.
- `[FAIT]` AliExpress a été accessible via l'API officielle et douze annonces actives ont été testées.
- `[FAIT]` Zéro annonce satisfait la spécification minimale.
- `[FAIT]` Les trois SKU livrables en France sont aussi incompatibles au prix rendu.
- `[FAIT]` Verdict fournisseur : `AUCUNE_FICHE_EXACTE`.
- `[FAIT]` Transition : `MARKET_VALIDATED -> CLOSED` pour la voie AliExpress dropshipping.
- `[FAIT]` Phase 5 non ouverte ; aucun CPA maximal, aucune marge contributive et aucun GO lancement ne sont inventés.
- `[FAIT]` Aucun produit n'a été importé dans DSers et aucune boutique n'a été modifiée.

Le résultat utile du test est le refus : la demande existe, mais la voie AliExpress observée ne fournit pas actuellement un produit suffisamment qualifiable, sûr et économiquement cohérent.
