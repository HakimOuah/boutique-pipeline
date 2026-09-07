# Sourcing AliExpress — Urnes funéraires (UK) — 07/09/2026

Rôle : oh-sourcing (lecture seule, passerelle VPS `aliexpress_vps_gateway.py`, aucune commande/contact vendeur/panier). Candidat préqualifié : `analyses/2026-09-07-recherche-uk-trendtrack/prequalification.md`, section 4 (`PASS_PREQUALIFICATION`, réserve densité de spécialistes UK).
Taux de conversion appliqué : **1 EUR = 0,86 GBP** (indiqué par la mission). Devise brute renvoyée par l'API : EUR.

## 1. Journal des requêtes

| # | Requête | Tri | Résultats pertinents (urnes hors bijoux) | Bruit dominant |
|---|---|---|---|---|
| 1 | `urne crémation adulte` | orders | 6/20 | Bijoux de crémation (colliers, pendentifs) : 13/20 |
| 1 | `urne crémation adulte` | price_desc | 15/20 | Incinérateurs industriels, béquilles, jardinières en tête de liste |
| 2 | `urne cendres humaines aluminium` | orders | 4/20 | Cendriers de voiture, réchauds de camping, bijoux : 9/20 |
| 2 | `urne cendres humaines aluminium` | price_desc | 10/20 | Fours de crémation industriels, brûleurs d'encens en tête |
| 3 | `urne laiton émaillé` | orders | **0/20** | Statues laiton (Bouddha, dragon, grenouille), robinetterie — **requête à écarter, aucune urne** |
| 3 | `urne laiton émaillé` | price_desc | 4/20 | Idem, statues et robinetterie haut de gamme |
| 4 | `urne crémation vissée` | orders | 9/20 | Bijoux : 11/20 |
| 4 | `urne crémation vissée` | price_desc | **14/20 — meilleure requête price_desc** | Fours industriels en tête, puis urnes 35–180 € |
| 5 | `urne adulte 200` | orders | 5/20 | Urinoirs portables adulte (faux positif sur « adulte ») : 14/20 |
| 5 | `urne adulte 200` | price_desc | 13/20 | UTV agricoles en tête, puis urnes animaux 15–65 € |
| 6 | `cremation urn adult` | orders | 8/20 | Bijoux : 12/20 |
| 6 | `cremation urn adult` | price_desc | 15/20 | Fours industriels en tête, puis urnes animaux et 1 urne étain 179 € |
| 7 | `urne cendres chien céramique` | orders | 4/20 | Bols/jouets/décoration animaux : 15/20 — **requête inefficace malgré 3 mots rares** |
| 7 | `urne cendres chien céramique` | price_desc | **0/20** | Séchoirs, niches, machines industrielles pour animaux |
| 8 | `urne animal photo` | orders | 2/20 | Ballons, posters, figurines animalières : 18/20 — **inefficace** |
| 8 | `urne animal photo` | price_desc | 4/20 | Figurines de collection haut de gamme |
| 9 | `mini urne keepsake lot` | orders | **0/20** | Décoration miniature de jardin (mini-pots, figurines résine) — **inefficace** |
| 9 | `mini urne keepsake lot` | price_desc | 6/20 | Remorques funéraires industrielles, mini-mobilier |
| 10 | `urne scellée velours` | orders | 1/20 | Pochettes/boîtes à bijoux en velours (le mot « velours » cible l'emballage, pas l'urne) : 19/20 |
| 10 | `urne scellée velours` | price_desc | 1/20 | Machines d'emballage, canapés et costumes en velours |
| 11 | `urne biodégradable` | orders | **11/20 — meilleure requête orders, taux le plus riche en urnes humaines identifiées comme telles** | Sacs poubelle compostables : 9/20 |
| 11 | `urne biodégradable` | price_desc | 13/20 | Toilettes compostables en tête, puis urnes 22–180 € |
| 12 | `urne bois cendres` | orders | 1/20 | Brûle-encens en bois, cendriers, bijoux : 18/20 |
| 12 | `urne bois cendres` | price_desc | 7/20 | Fours industriels puis urnes bois/céramique |
| 13 | `urne columbarium gravée` | orders | 8/20 | Stylos de retouche pour pierres tombales, bijoux : 12/20 |
| 13 | `urne columbarium gravée` | price_desc | **17/20 — meilleur ratio global** | 1 seule ligne hors-sujet (colonne en marbre) |

**Requêtes qui marchent** : `urne crémation vissée` (price_desc), `urne biodégradable` (orders et price_desc), `urne columbarium gravée` (price_desc). **Requêtes à écarter** : `urne laiton émaillé` (0 urne, confond avec statuaire laiton), `urne cendres chien céramique` et `urne animal photo` (le mot « animal »/« chien » + tri orders ramène des accessoires pour animaux vivants, pas des urnes), `mini urne keepsake lot` en tri orders (décoration miniature de jardin), `urne scellée velours` (le mot « velours » cible l'emballage bijoutier, pas l'urne).
44 appels API utilisés sur le plafond de 45 (26 `search`, 8 `variants`, 10 `exact` dont 4 tentatives infructueuses sur une même fiche — voir fiche Animal 1).

## 2. Fiches retenues

### ADULTE 1 — Urne en fer, gamme couleurs, colombaire (fiche RETENUE, meilleure candidate adulte)
- **Titre** : « Urnes de couleur en fer pour cendres humaines, cerceaux pour adultes, urnes pour animaux de compagnie, porte-cendres pour chiens, crémation, urne, souvenir, colombaire, commémoratif pour animaux de compagnie » (titre à double usage adulte/animal dans le libellé fournisseur — confirmé « pour adultes » explicitement).
- **URL** : https://www.aliexpress.com/item/1005010151827662.html
- **Magasin** : Shop1103134560 Store (CN). Notes boutique (confiance A, `variants`) : communication 4,3 / conformité à la description 4,2 / vitesse d'expédition 4,3.
- **Note produit (search)** : non renvoyée par l'API pour cette fiche (champ vide côté `search` — confiance A sur l'absence, pas d'invention).
- **Ventes réelles (variants, confiance A)** : 9.
- **Prix réel des variantes (`offer_sale_price`, confiance A)** : S (Gris clair) 36,99 € → 31,81 £ ; M (Vert clair) 38,99 € → 33,53 £ ; L (Jaune clair) 40,19 € → 34,56 £. Variante visée : **M, 38,99 € = 33,53 £**.
- **Capacité/dimensions/matériau** : fer (« fer » = iron, pas aluminium/laiton au sens strict de la fiche produit source, mais métal avec couvercle vissé confirmé par « colombaire » dans le titre) — capacité en pouces cubes non renvoyée par l'API (confiance C, lisible seulement sur photo/description PDP hors accès).
- **Stock (confiance A)** : S 98 / M 98 / L 94.
- **Variantes** : 3 couleurs (jaune clair, vert clair, gris clair) — pas de taille distincte au sens litres, les codes S/M/L semblent être des étiquettes internes de couleur.
- **Fret vers GB (`exact`, confiance A)** : CAINIAO_STANDARD, gratuit (`free_shipping: true`), expédié de Chine, délai 6–13 j (livraison estimée 13–20 sept.), suivi disponible.
- **Coût rendu GBP** : 33,53 £ (variante M) + 0 £ fret = **33,53 £**.
- **Nombre d'images SKU** : 3 (une par couleur).
- **Niveaux de confiance** : prix/stock/ventes = A ; fret = A ; matériau exact et capacité = C (non confirmés par l'API, à vérifier sur PDP avant commande test).

### ADULTE 2 — Urne céramique « vert Ceram » (fiche à réserve forte, NON prioritaire)
- **Titre** : « Urne de crémation pour adulte, souvenir vert Ceram, pour cendres humaines, chiens, chats, oiseaux, chat, souvenirs pour animaux ».
- **URL** : https://www.aliexpress.com/item/1005008744316921.html
- **Magasin** : DGBG Gift Store (CN). Notes (confiance A) : communication 4,7 / conformité 4,7 / expédition 4,7.
- **Note produit (search, confiance B)** : 4,9 — taux de satisfaction 98,2 %.
- **Ventes réelles (confiance A)** : 36.
- **Prix réel** (confiance A) : Gris clair 14,99 € (stock 0) ; Gris foncé 14,39 € → 12,38 £ (stock 4) ; Bleu ciel 13,59 € (stock 6).
- **Réserve majeure** : le prix réel (12–13 £) et le partage du même gabarit SKU avec des fiches animaux du même fournisseur rendent très improbable qu'il s'agisse d'une urne pleine taille (≥ 200 pouces cubes) malgré la mention « pour adulte » dans le titre — **capacité non confirmée, confiance C, suspicion de mauvais étiquetage marketing fournisseur**.
- **Stock (confiance A)** : critique, 0 à 6 unités selon couleur — invendable en volume.
- **Fret vers GB (`exact`, confiance A)** : CAINIAO_FULFILLMENT_PRE, 1,99 € = 1,71 £, délai 6–10 j, non gratuit.
- **Coût rendu GBP** : 12,38 £ + 1,71 £ = **14,09 £** (variante Gris foncé).
- **Nombre d'images SKU** : 3.
- **Niveaux de confiance** : prix/stock/fret = A ; adéquation au segment adulte pleine taille = C (réserve bloquante).

### ANIMAL 1 — Urne acier inoxydable personnalisée photo (fiche RETENUE)
- **Titre** : « Urnes personnalisées pour animaux de compagnie en acier inoxydable pour cendres de chat et de chien, urnes commémoratives, urne photo pour cendres de chien, pot souvenir pour animaux de compagnie, cadeaux de souvenir ».
- **URL** : https://www.aliexpress.com/item/1005010528598784.html
- **Magasin** : Pety Puppy Paws Store (CN). Notes (confiance A) : communication 4,8 / conformité 4,8 / expédition 4,8.
- **Note produit (search, confiance B)** : 4,9 — taux de satisfaction 97,5 %.
- **Ventes réelles (confiance A)** : 110 — meilleur volume de la sélection.
- **Prix réel (confiance A)** : Gris clair/Vert clair × Taille L / M — 12,99 € à 13,29 € → 11,17–11,43 £.
- **Capacité/dimensions/matériau** : acier inoxydable, personnalisation photo mentionnée au titre (« urne photo ») ; dimensions non renvoyées (confiance C).
- **Stock (confiance A)** : très élevé, 9 987–9 995 selon SKU.
- **Variantes** : 2 couleurs × 2 tailles (L, M).
- **Fret vers GB** : **non renvoyé**. Quatre tentatives `exact` avec les propriétés Couleur/Taille (seules ou combinées) ont toutes échoué (`qualification_refused`, « ambiguous variant » ou « no SKU matches exactly ») — anomalie de la passerelle sur cette fiche, non résolue dans le budget d'appels imparti. Aucun coût de fret inventé.
- **Coût rendu GBP** : incomplet — 11,17–11,43 £ hors fret (fret non renvoyé).
- **Nombre d'images SKU** : 2 (une par couleur).
- **Niveaux de confiance** : prix/stock/ventes = A ; fret = non disponible (échec API documenté, pas d'estimation).

### ANIMAL 2 — Urne céramique en forme de chien/chat, 200 ml (fiche RETENUE)
- **Titre** : « Urne funéraire en céramique pour animaux de compagnie, 200ml, en forme de chien/chat, urnes de crémation pour chien et chat, anti-humidité, souvenirs, oiseau, souris, fournitures pour chiens ».
- **URL** : https://www.aliexpress.com/item/1005010339492490.html
- **Magasin** : MIAOOM Store (CN). Notes (confiance A) : communication 4,6 / conformité 4,5 / expédition 4,7.
- **Note produit (search, confiance B)** : 4,3 — taux de satisfaction 85,0 % (le plus bas de la sélection, à surveiller).
- **Ventes réelles (confiance A)** : 60.
- **Prix réel (confiance A)** : 8,59 € à 9,29 € selon coloris/forme → 7,39–7,99 £. Variante testée en fret : « chien orange » (kaki foncé), 9,29 € → 7,99 £.
- **Capacité (confiance A, titre confirmé par l'API)** : 200 ml — sous la fourchette animale 0,5–1,5 L visée par la mission ; à considérer comme format d'appel/entrée de gamme plutôt que le format central du cluster animal.
- **Stock (confiance A)** : hétérogène — 0 pour « Chat rouge » et « Chat vert », 1 pour « Chat rose », 20 pour « chien orange », « chien vert », « Chat noir », « Chat blanc », 12 pour « chien blanc », 5 pour « chien noir ». Choisir les coloris à stock 20.
- **Fret vers GB (`exact`, confiance A)** : CAINIAO_FULFILLMENT_PRE, 1,99 € = 1,71 £, délai 6–10 j.
- **Coût rendu GBP** : 7,99 £ + 1,71 £ = **9,70 £** (variante « chien orange »).
- **Nombre d'images SKU** : 9 (une par coloris/forme animal).
- **Niveaux de confiance** : prix/stock/ventes/capacité/fret = A.

### MINI-URNE / KEEPSAKE — Petite urne Keepplex pour cendres humaines (fiche RETENUE)
- **Titre** : « Petites urnes commémoratives Keepplex pour cendres humaines, arbre de vie, urnes funéraires pour papa vertébrale » (titre à traduction FR maladroite côté passerelle, sens : petite urne commémorative pour cendres humaines, motif arbre de vie).
- **URL** : https://www.aliexpress.com/item/1005007997724095.html
- **Magasin** : WK Jewelry Store (CN). Notes (confiance A) : communication 4,7 / conformité 4,7 / expédition 4,8.
- **Note produit (search, confiance B)** : 4,7 — taux de satisfaction 94,1 %.
- **Ventes réelles (confiance A)** : 64.
- **Prix réel (confiance A)** : 5,89 € à 6,99 € selon coloris → 5,07–6,01 £. Variante testée en fret : « vert clair », 6,99 € → 6,01 £.
- **Capacité/dimensions** : « petites urnes », explicitement dédiées aux cendres humaines (format keepsake) — dimensions précises non renvoyées par l'API (confiance C).
- **Stock (confiance A)** : hétérogène — 656–668 pour Gris clair/Vert clair/Kaki foncé, mais seulement 4 (Prune) et 8 (Jaune clair). Choisir un coloris à fort stock.
- **Fret vers GB (`exact`, confiance A)** : CAINIAO_FULFILLMENT_PRE, 1,99 € = 1,71 £, délai 6–10 j.
- **Coût rendu GBP** : 6,01 £ + 1,71 £ = **7,72 £** (variante « vert clair »).
- **Nombre d'images SKU** : 6 (une par coloris).
- **Alternative repérée non retenue** : `1005008269271933` — « Mini urne de crémation Keepplex en alliage d'aluminium, 7 couleurs, support commémoratif » — même fournisseur/famille, 1 000+ commandes (le plus populaire de toute la recherche), mais prix réel 2,89–3,19 € (2,49–2,74 £) : formulation « support commémoratif » ambiguë sur la fonction réelle (urne pleine ou simple présentoir), non retenue en fiche principale par prudence.
- **Niveaux de confiance** : prix/stock/ventes/fret = A ; dimensions et matière exacte = C.

## 3. Tableau économique indicatif

Conversion : TTC → HT UK = /1,2 (TVA 20 %). Coûts rendus incluant le fret quand renvoyé par l'API ; « non renvoyé » sinon (aucun coût inventé).

| Fiche | Coût rendu GBP | Prix de vente visé (TTC) | Prix HT (/1,2) | Marge brute avant pub (HT − coût) |
|---|---|---|---|---|
| Adulte 1 — urne fer colombaire | 33,53 £ | 69,00 £ | 57,50 £ | **23,97 £** |
| Adulte 1 — urne fer colombaire | 33,53 £ | 99,00 £ | 82,50 £ | **48,97 £** |
| Adulte 2 — urne céramique « vert Ceram » (réserve capacité) | 14,09 £ | 69,00 £ | 57,50 £ | 43,41 £ (marge théorique élevée mais **fiche non fiable sur la taille réelle** — ne pas utiliser tel quel) |
| Animal 1 — acier inox personnalisée photo | fret non renvoyé — coût partiel 11,17–11,43 £ | 39,00 £ | 32,50 £ | non calculable sans fret confirmé |
| Animal 1 — acier inox personnalisée photo | fret non renvoyé — coût partiel 11,17–11,43 £ | 69,00 £ | 57,50 £ | non calculable sans fret confirmé |
| Animal 2 — céramique chien/chat 200 ml | 9,70 £ | 39,00 £ | 32,50 £ | **22,80 £** |
| Animal 2 — céramique chien/chat 200 ml | 9,70 £ | 69,00 £ | 57,50 £ | **47,80 £** |
| Mini/keepsake — Keepplex cendres humaines | 7,72 £ | 29,00 £ | 24,17 £ | **16,45 £** |
| Mini/keepsake — Keepplex cendres humaines | 7,72 £ | 45,00 £ | 37,50 £ | **29,78 £** |

Marges avant coût publicitaire, frais de plateforme, retours et TVA sur import (droits de douane non calculés — hors périmètre de cette fiche). Ordre de grandeur uniquement.

## 4. Réserves

- **Étanchéité/scellage** : déclarations vendeur uniquement (« scellé », « anti-humidité », « colombaire ») — aucune donnée API ne confirme un joint réel ; à vérifier physiquement avant commande test, en particulier pour l'usage cendres humaines (promesse sensible).
- **Casse céramique** : Animal 2 et l'alternative céramique Adulte 2 sont en céramique — risque de casse au transport international non couvert par les données API (pas de taux de litige renvoyé par `variants`/`exact`).
- **Délai > 15 j pour achat émotionnel urgent** : tous les délais confirmés sont dans la fenêtre 6–13 j (max observé), donc **sous le seuil de 15 j critique** — point favorable, mais à reconfirmer à la commande réelle (les délais API sont des estimations, pas des garanties).
- **Entrepôt CN vs UE/UK** : toutes les fiches retenues expédient depuis la Chine (`ship_from_country: CN`) — aucun entrepôt UE/UK identifié dans cette recherche, ce qui pèse sur le délai pour un achat à caractère émotionnel/urgent.
- **Qualité de gravure/personnalisation** : la fiche Animal 1 mentionne une « urne photo » personnalisée mais aucune donnée API ne décrit le procédé (gravure laser, impression, autocollant) ni sa durabilité.
- **Densité de spécialistes UK** (rappel prequalification §4) confirmée côté offre AliExpress : le catalogue est dominé par la bijouterie de deuil (colliers/pendentifs à 2–5 €) et les urnes animaux ; les urnes adulte pleine taille en aluminium/laiton avec couvercle vissé sont rares et mal indexées — un seul candidat solide (Adulte 1) a été trouvé malgré 13 requêtes et 26 appels `search`.
- **Fiche Animal 1** : le fret n'a pas pu être confirmé (anomalie API `qualification_refused` répétée) — ne pas lancer de commande test sur cette fiche sans revalider le fret par un autre canal.
- **Fiche Adulte 2** : à écarter ou requalifier avant tout usage — le prix réel et le stock suggèrent une taille inadaptée au segment « adulte pleine taille » malgré le titre.

## 5. Statut final

**OFFRE TROUVÉE**

(Une urne adulte exploitable identifiée avec prix, stock, fret confirmés — Adulte 1 ; deux urnes animal exploitables — Animal 2 confirmée intégralement, Animal 1 avec fret à revalider ; une mini-urne/keepsake exploitable — Keepplex cendres humaines. Le marché AliExpress reste pauvre en urnes adulte pleine taille non-bijouterie : un seul candidat solide sur 26 appels de recherche, ce qui appelle une vérification terrain/PDP avant tout achat test.)
