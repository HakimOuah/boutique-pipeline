# Sourcing AliExpress — abri à bûches / log store (marché UK)

Rôle : oh-sourcing (lecture seule, gateway VPS). Candidat issu de `prequalification.md` section 5. Taux de change appliqué : 1 EUR = 0,86 GBP.

## 1. Journal des requêtes

Toutes les commandes exécutées en premier plan, séquentielles, 1 s entre appels. Destination `GB`. 24 appels gateway consommés sur un plafond de 40 (18 `search`, 2 `variants` en échec sur le même produit, 1 `variants` réussi, 1 `exact` réussi, 2 tentatives d'appel supplémentaires abandonnées faute de candidats nouveaux).

| # | Requête | Tri | Résultat |
|---|---|---|---|
| 1 | `firewood rack` | orders | Bruit total — mobilier/rangement générique (étagères cuisine, porte-serviettes). Confirme la règle : le tri popularité ne sert à rien ici. |
| 2 | `bûches galvanisé` | price_desc | **Utile** — fait remonter les 2 seuls candidats retenus (voir §2) au milieu de pesages/domes/remorques industriels hors sujet. |
| 3 | `abri bois chauffage métal` | price_desc | Bruit — cuisines extérieures, fours à pizza, conteneurs sur mesure (devis B2B en milliers d'EUR). |
| 4 | `porte-bûches extérieur acier` | price_desc | Bruit — remorques, maisons conteneurs, cuisines extérieures. |
| 5 | `log store metal` | price_desc | Bruit — garages/casiers/armoires métalliques génériques. |
| 6 | `log holder outdoor` | price_desc | Bruit — cuisines extérieures, saunas, tentes de toit. |
| 7 | `firewood storage` | price_desc | Bruit — mobilier de maison, chambres froides, saunas. |
| 8 | `log rack` | price_desc | Bruit — stockage énergie, fours, porte-bagages de toit. |
| 9 | `rack bois de chauffage housse` | price_desc | Bruit — grills, cuisines extérieures, saunas, capotes de voiture. |
| 10 | `log store galvanised` | price_desc | Bruit mais révèle une **famille de abris de jardin acier galvanisé démontables** (même vendeur/gamme type TMG) en tailles 4x9 ft, 6x8 ft, 10x12 ft — aucune taille compatible 1,0–1,5 m. |
| 11 | `housse bûches extérieur` | price_desc | Bruit — housses de voiture, piscines, tentes. |
| 12 | `abri à bûches métallique` | price_desc | Bruit — mêmes cuisines/conteneurs/garages industriels. |
| 13 | `firewood log store cover` | price_desc | Bruit — saunas, fendeuses de bûches industrielles, cuisines extérieures. |
| 14 | `Outsunny bûches` | price_desc | Bruit total — l'appariement associe « Outsunny » à « sunny » (lapins solaires, parapluies, t-shirts Bad Bunny). Requête à écarter. |
| 15 | `abri rangement incliné acier galvanisé` | orders | Bruit — rangement générique. |
| 16 | `abri rangement incliné acier galvanisé` | price_desc | Bruit — conteneurs solaires, maisons modulaires, poulaillers, serres agricoles (devis B2B). |
| 17 | `bûcher extérieur pliable acier` | price_desc | Bruit — remorques de camping, maisons conteneurs. |
| 18 | `porte-bûches intérieur acier` | price_desc | Bruit — cuisines extérieures modulaires. |
| 19 | `panier bûches métal design` | price_desc | Bruit — machines industrielles (paniers plastique, laveuses), présentoirs. |

Constat : le catalogue accessible via cette passerelle ne contient pas de SKU consommateur « log store » métallique démontable UE/UK dans le format visé (1,0–1,5 m, < 20 kg). Les seuls résultats métal/galvanisé de taille comparable sont soit (a) des abris de jardin complets 4x9 ft à 40 ft de la même gamme grossiste type TMG, à prix de devis B2B (des centaines à dizaines de milliers d'EUR, souvent orders vide = jamais vendu à l'unité), soit (b) du bruit générique.

## 2. Fiches retenues

Un seul produit réel exploitable a été identifié ; il ne satisfait pas le critère fret décisif. Un second candidat n'a pas pu être audité (erreur gateway persistante).

### 2.1 Support de bûches fer forgé (indoor/outdoor) — retenu à titre de réserve, **non conforme fret**

- Titre : « Support de rangement de bois de chauffage, support de bûches de cheminée en fer forgé, organisateur de support de bois de chauffage pour usage domestique au feu ou en extérieur »
- URL : https://www.aliexpress.com/item/1005010381135593.html
- Magasin : Shop1103733046 Store (Chine) — notation communication 4.7, expédition 4.7, conformité à la description 4.5 (niveau A, lu dans `variants`/`exact`)
- Note produit et taux d'avis (search) : rating 0.0, evaluation_rate absent — produit sans historique d'avis visible (niveau A, valeur réelle lue telle quelle, non inventée)
- Ventes réelles (`variants`) : `sales_count` = 7 (niveau A)
- Variante : une seule couleur « noir » (`sku_id` 12000052215640997)
- Prix réel variante (`offer_sale_price`, niveau A) : 56,39 EUR → **48,50 £**
- Prix catalogue (`sku_price`, référence non retenue pour le calcul) : 112,78 EUR
- Dimensions/poids/matériau lisibles : non communiqués par l'API (titre seul : fer forgé) — **niveau C, absent, non inventé**
- Stock (niveau A) : 3 unités seulement
- Nombre d'images SKU : 1 image de variante retournée par l'API (niveau A ; galerie complète non accessible en lecture seule)
- Fret vers GB (`exact`, niveau A) :
  - Transporteur : AliExpress Selection Shipping for Oversized Goods (Cainiao)
  - Entrepôt d'expédition : Chine (CN)
  - Coût transport : 1,99 EUR (1,71 £)
  - Délai annoncé : 25 à 42 jours (fenêtre livraison indiquée « oct. 02 – 19 »)
  - Stock disponible à l'expédition : 3
- Coût rendu estimé : 56,39 + 1,99 = 58,38 EUR → **50,21 £** (niveau A pour les deux composantes sommées)

**Verdict fiche : écartée du calcul économique.** Délai 25–42 j très supérieur au seuil de 15 j, entrepôt CN sans retour fret annoncé, stock quasi nul (3 unités, aucune marge d'achat groupé), fiche sans avis ni preuve de traction (7 ventes), boutique générique sans nom de marque. Ne correspond pas non plus au format extérieur galvanisé démontable visé en priorité — au mieux un rack intérieur, catégorie secondaire du brief, mais le fret élimine toute exploitation en l'état.

### 2.2 Abri de rangement incliné acier galvanisé 4x9 pieds — **non audité, erreur gateway persistante**

- Titre : « Abri de rangement incliné en acier galvanisé robuste 4x9 pieds avec porte verrouillable, anti-rongeurs, imperméable et facile à assembler »
- URL : https://www.aliexpress.com/item/1005011643683796.html
- Prix catalogue (`search`, niveau C, non fiable — prix de liste) : 433,25 EUR
- `variants` interrogé deux fois → `IOPUpstreamError` (code AE 604) les deux fois. Conforme à la consigne « réessaie une fois puis déclare la limite » : audit abandonné, aucune donnée de vente, stock, fret ou dimension récupérable.
- Dimensions déclarées dans le titre seul (4x9 pieds ≈ 1,22 m x 2,74 m d'emprise au sol) : très supérieures à la fourchette 1,0–1,5 m visée, et le format « abri de jardin complet » (porte verrouillable, anti-rongeurs) suggère un poids largement > 20 kg. **Écarté sur le principe même sans donnée chiffrée**, faute de pouvoir confirmer ou infirmer par l'API.

Aucune autre fiche n'a atteint le seuil minimal de pertinence (produit réel firewood/log store, prix cohérent, taille compatible) parmi les ~19 requêtes passées.

## 3. Tableau économique

| Fiche | Coût rendu GBP | Prix de vente visé | Marge brute avant pub | TVA UK 20 % (sur prix TTC visé) | Marge nette avant pub |
|---|---|---|---|---|---|
| 2.1 Support fer forgé (56,39 EUR + 1,99 EUR fret = 58,38 EUR → 50,21 £) | 50,21 £ | Hors gabarit du brief (rack, pas d'abri) — pas de prix visé défini par le mandat pour cette catégorie | Non calculable : le brief fixe 119–169 £ pour l'abri extérieur et 59–89 £ pour le rack intérieur haut. En prenant le bas de fourchette rack (59 £) à titre indicatif seulement : marge brute = 59 − 50,21 = **8,79 £**, avant TVA, pub, retours. | Sur 59 £ TTC : TVA = 9,83 £, base HT = 49,17 £ → marge après TVA et coût rendu = **−1,04 £** (déficitaire) | Déficitaire au bas de fourchette |
| 2.2 Abri galvanisé 4x9 ft | Non calculable — aucune donnée `variants`/`exact` obtenue | 119–169 £ (visé brief) | Non calculable | Non calculable | Non calculable |

Aucun coût inventé : les deux lignes ci-dessus montrent qu'aucune marge positive fiable ne peut être établie sur les données réellement collectées. Le calcul indicatif sur la fiche 2.1 est fourni uniquement pour illustrer que même en forçant un rapprochement hors-gabarit (rack vendu comme abri), la marge est nulle ou négative une fois la TVA UK intégrée.

## 4. Réserves

- **Fret, réserve majeure et bloquante** : la seule fiche exploitable expédie depuis la Chine avec un délai de 25 à 42 jours, très au-dessus du seuil de 15 j fixé par le mandat ; aucun entrepôt UE/UK identifié sur l'ensemble du balayage.
- **Entrepôt** : aucun produit du balayage n'a d'entrepôt UE/UK déclaré dans `exact`. Tous les résultats pertinents (rares) sont expédiés de Chine.
- **Délai** : cf. fret ci-dessus, 25–42 j sur la seule fiche auditée avec succès.
- **Montage** : information absente pour les deux candidats (aucune notice, aucun poids/dimension confirmé pour 2.1 ; 2.2 non audité).
- **Rouille** : matériau « fer forgé » (fiche 2.1) sans traitement anticorrosion précisé dans les données API — risque non écarté pour un usage extérieur, alors que le brief exige acier galvanisé/thermolaqué.
- **Stock** : fiche 2.1 à 3 unités seulement — insuffisant pour un test dropshipping soutenu, aucune garantie de réassort.
- **Confiance fournisseur** : boutique « Shop1103733046 Store » générique, 0 avis, 7 ventes seulement — aucun historique solide.
- **Panne technique** : le produit 1005011643683796 (le seul candidat au format « abri » plausible) n'a pas pu être audité — deux échecs `IOPUpstreamError` consécutifs sur `variants`. Il est possible que ce produit soit inaccessible en lecture pour des raisons indépendantes de la recherche (fiche supprimée, restriction régionale) ; à retester plus tard si l'agent en a l'occasion, mais aucune conclusion ne peut en être tirée aujourd'hui.
- **Couverture de la requête** : la marque « Outsunny » a produit un bruit total par appariement lexical fortuit (« sunny ») — les requêtes marque generiques ne sont pas fiables sur ce candidat et n'ont pas été poursuivies pour VEVOR/vidaXL/Relaxdays/Costway faute de signal positif sur les deux premiers tests apparentés.

## 5. Statut final

**AUCUNE OFFRE EXPLOITABLE**

Aucune fiche AliExpress accessible via la passerelle ne réunit à la fois : matériau métal galvanisé/thermolaqué, format démontable carton plat, poids < 20 kg, longueur 1,0–1,5 m, et fret UE/UK ou CN à délai raisonnable. Le seul produit réel audité avec succès (support de bûches fer forgé) est hors gabarit de taille visé, à stock quasi nul, et à délai de livraison 25–42 jours depuis la Chine — incompatible avec le seuil de 15 jours. Le seul candidat au format « abri » plausible n'a pas pu être audité (panne gateway persistante après une nouvelle tentative). Ce dossier ne peut pas progresser vers un test fournisseur en l'état ; il nécessiterait soit un nouveau balayage une fois la panne gateway résolue sur le produit 1005011643683796, soit un accès à un catalogue fournisseur plus large (BigBuy, wholesale UK) hors du périmètre de cette mission.
