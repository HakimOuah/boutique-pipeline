# Phase 4 — Sourcing catalogue osmoseur Bonum Vitae — 18 août 2026

Date des relevés : **18/08/2026 00:35–00:45 CEST** (API `checked_at_utc` 2026-08-17T22:35–22:43Z).
Boutique : Bonum Vitae (`kw7vak-g0.myshopify.com`). Fournisseur : AliExpress exclusivement, passerelle lecture seule.

**Rappel obligatoire** : prix, stocks, variantes et délais sont dynamiques. Tous les relevés ci-dessous doivent être reconfirmés au panier DSers pour une adresse française avant toute commande test. Aucun achat, aucun ajout au panier, aucun contact vendeur, aucun import DSers, aucune mutation Shopify. Toute caractéristique (GPD, pH, minéraux, UV, débit) est **annoncée par le vendeur**, non contrôlée sur échantillon.

Preuve : **classe B+** (API `search` + `variants` + `exact` fret FR). Aucune PDP ouverte.

---

## 1. Entrée

Pas un GO marché neuf : le cluster osmoseur est déjà instruit
([`boutique-bonum-vitae/journal/2026-08-17-analyse-marche-osmoseur.md`](../boutique-bonum-vitae/journal/2026-08-17-analyse-marche-osmoseur.md)).
Cette passe complète le **catalogue déjà en vente**, pour qu'il tienne comme celui d'un spécialiste.

**Trou constaté avant sourcing (catalogue public, API Shopify 18/08)** :

| Handle | Statut | Prix | Problème |
|---|---|---|---|
| `osmoseur-ro-600g` | ACTIVE | 299 € | Hero campagne. 4 étapes annoncées (PP, CTO, membrane, T33). **Aucun consommable compatible documenté.** SKU DSers `14:29#600G;200007763:201336342` (entrepôt France). |
| `filtration-par-osmose-inverse-oswnkw-600-gpd-haut-debit` | ACTIVE | 449 € | Même palier 600 GPD, 2,5 L/min annoncé, DN15, Pologne. SKU `14:29#600 GPD;200007763:203372089;…`. |
| `membrane-d-osmose-inverse-ro-cartouche-de-remplacement` | ACTIVE | 17,90–31,90 € | Variantes **50 / 75 / 100 / 150 GPD** (format 1812). **Incompatible avec un 600 GPD** — affiché dans la collection `osmoseurs`. |
| `systeme-d-osmose-inverse-600-gpd-sans-reservoir-oswnkw` | DRAFT | — | Encore du 600 GPD. Ne pas publier. |
| `osmoseur-de-cuisine-shuangli-600g-osmose-inverse` | DRAFT | 380,90 / 406,90 € | Variantes 600 **et 800 GPD**, Pologne. Toujours un clone de palier, pas un 2ᵉ étage de gamme. |

Collection `osmoseurs` : **3 visibles dont 1 consommable faux-ami** (T-07, seuil de 5).

**Candidats de cette passe** (pas un 3ᵉ 600 GPD anonyme) :

1. Consommables des machines déjà vendues (membrane 600 GPD, PP, CTO/PPC, T33, kit annuel).
2. Palier différent : osmoseur **comptoir** (pose nulle) et/ou **reminéralisation** documentée.
3. 800 GPD : noté s'il apparaît, pas l'objectif.

Gateway `health` : OK à 2026-08-17T22:35:53Z. Jeton jusqu'au 2026-09-01.

---

## 2. Par candidat

### 2.1 Kit d'entretien OSWNKW RO600GPD — `FOURNISSEUR À TESTER`

C'est la fiche qui ferme le trou « expert » : un an de pièces **et** l'étage reminéralisant, chez le magasin officiel OSWNKW.

- **URL** : https://fr.aliexpress.com/item/1005005705096746.html
- **Titre annoncé** : « Filtre purificateur d'eau OSWNKW Compatible avec le remplacement d'élément filtrant RO600GPD »
- **Vendeur** : OSWNKW Whole House Water Purification Expert Official Store (CN) — notes boutique 4,8 / 4,8 / 4,8
- **Ventes API** : **103**. Note produit API : 0,0 (compteur d'avis non servi) ; SERP `search` : 4,8★
- **Variante visée** : `Couleur=set` + `Expédié depuis=China Mainland` — `sku_attr` `14:366#set;200007763:201336100`
- **Prix variante (18/08)** : **55,39 €** TTC annoncé. Fret FR Fedex IP : **8,07 €**, suivi, **3–9 jours**, stock **37**. **Coût rendu = 63,46 €**.
- **Pologne** (`Expédié depuis=Pologne`, 51,69 € affiché) : `exact` **refusé — SKU en rupture**.
- **Contenu annoncé sur la vignette kit** (non contrôlé sur échantillon) :
  - PP 5 µm ×2 (6 mois, 4,2 L/min annoncé)
  - PPC composite (PP + charbon) ×2 (6–12 mois)
  - Membrane **Ro3013-600** ×1 (600 GPD annoncé)
  - Cartouche **alcaline minéralisée** (charbon) ×2 — calcium / magnésium / potassium et pH ~7,5 **annoncés par le vendeur**
- **Signaux de risque** :
  1. Compatibilité **OSWNKW 600 GPD** = revendiquée par le magasin officiel. Compatibilité du **RO 600G à 299 €** : **non documentée**. Les visuels boutique sont générés (`Image_generee_*`) : on ne déduit pas le boîtier depuis la photo.
  2. Pologne vide : le 449 € public part de Pologne, le kit part de Chine. Délai et douane à confirmer au panier (TVA déjà dans `tax_included: true`).
  3. Claims pH / minéraux : **ne pas les recopier** tels quels (ligne Anses / GMC). Formuler « cartouche de reminéralisation, goût moins plat » après commande test.
  4. Aucune PDP lue : composition exacte, filetages, notice = commande test.

**Statut : `FOURNISSEUR À TESTER`** — meilleure fiche du lot. Confiance **B+**. Ce n'est pas un GO fournisseur.

Prix de vente envisageable après test (pas un verdict) : **119–149 €** le kit annuel, pour tenir l'argument Waterdrop 105–170 €/an avec une marge brute ~47–57 % sur 63,46 € rendu. À chiffrer en phase 5 / T-H7 si Hakim importe.

### 2.2 Membrane TFC-3013-600 seule — `OFFRE TROUVÉE`

- **URL** : https://fr.aliexpress.com/item/1005006026653705.html
- **Titre** : « 2 pièces 600 gpd … Membrane TFC-3013-600 »
- **Vendeur** : Huang Kai Home Appliance Accessories Store — 4,8 / 4,7 / 4,8
- **Ventes** : 51. Variante unique : **48,59 €** les 2, stock **5**.
- **`exact` fret FR** : refusé (SKU sans propriété — `No SKU matches exactly`).
- **Lecture** : le format 3013-600 **colle au kit officiel** (Ro3013-600). Utile en pièce détachée **si** le kit 2.1 est retenu, pas comme premier SKU. Stock 5 = trop juste pour en faire le consommable hero.

**Statut : `OFFRE TROUVÉE`** (fret et stock). Alternative, pas la fiche à tester en premier.

Fiche voisine `1005006498661694` (XinSanLian, 500+ ventes) : variantes 1812/2012/3012/3013 jusqu'à **400 GPD seulement**. **Pas de 600 GPD.** Écartée pour nos machines.

### 2.3 Reminéralisation hors kit — `OFFRE TROUVÉE` (format à confirmer)

Le kit 2.1 **porte déjà** l'étage alcalin. Les fiches ci-dessous ne servent que si on veut une cartouche seule, ou si le kit ne rentre pas dans le RO 600G.

| Fiche | Relevé 18/08 | Lecture |
|---|---|---|
| [1005006944192709](https://fr.aliexpress.com/item/1005006944192709.html) — alcaline **10 pouces** 4 couches, Waternoble Store 4,6 | Variante `2Pcs 4 in1 Filter` : **21,79 €**, stock 367, fret CN offert, **9–18 j**. 27 ventes. | Boîtier **10″** : nos 600 GPD compactes n'en ont probablement pas. Inutile sans boîtier documenté. |
| [32967120172](https://fr.aliexpress.com/item/32967120172.html) — NCR102 ORP, coronwater Official Store 4,7 | Chine : **23,39 €**, stock 121, fret offert **8–16 j**. Pologne : **rupture** (`exact` refusé). 23 ventes. | Format (T33 vs 10″) **non lu en PDP**. Claims ORP / hydrogène / antioxydant = à jeter à la rédaction. |
| [33008432844](https://fr.aliexpress.com/item/33008432844.html) — charges Maifan / KDF à remplir | 13,49–39,19 €, stocks 1 000+. | DIY. Pas un SKU Claire. **Rejeté.** |

**Statut : `OFFRE TROUVÉE`** — éléments essentiels manquants (format exact, compatibilité boîtier). Ne pas importer tant que le kit 2.1 n'est pas tranché.

### 2.4 Osmoseur 8 étapes 600G inox + UV — `OFFRE TROUVÉE`

- **URL** : https://fr.aliexpress.com/item/1005011837944778.html
- **Titre** : « Purificateur d'eau en acier inoxydable 600G à 8 étapes … filtre UV … consommation directe »
- **Vendeur** : Yami D15 Store — 4,4 / 4,5 / 4,4 (sous le confort habituel)
- **Ventes** : 13. Prise EU : **345,99 €**, stock 988.
- **`exact` fret FR** : refusé (`Ambiguous variant: 2 SKUs match`).
- **Lecture** : toujours du **600 GPD**. Coût ~346 € = pas de marge saine sous 449 €, et ça cannibalise le hero 299 €. L'UV / 8 étapes peuvent porter un palier « plus complet » **plus tard**, pas maintenant.

**Statut : `OFFRE TROUVÉE`**. Pas la pièce qui fait l'expert ce mois-ci.

### 2.5 Osmoseur 8 étapes 800 GPD — `AUCUNE OFFRE EXPLOITABLE`

- **URL** : https://fr.aliexpress.com/item/1005009242052877.html
- Variante `RO System` 220 V : **341,99 €**, stock 98. 9 ventes. Note SERP 2,5★.
- **`exact` FR** : **`DELIVERY_NOT_AVAILABLE_TO_YOUR_ADDRESS`**.

Le brouillon SHUANGLI a déjà une variante 800 GPD : ne pas en empiler une deuxième, surtout non livrable.

### 2.6 Osmoseur de comptoir — `AUCUNE OFFRE EXPLOITABLE` (cette passe)

Requêtes rares testées : `Waterdrop K6`, `Waterdrop N1`, `SimPure Y7`, `Bluevua RO`, `AquaTru classic`, `comptoir osmoseur`, `desktop RO600`, `countertop tankless`, `Viomi RO`, `Mijia RO`, `Scishare RO`, `instant heating RO`, `R2B5`, `nodrill RO`.

L'API a rabattu sur best-sellers hors rayon (cosmétique, arrosage, RAM, NFC). **Aucune fiche comptoir consommateur 400–500 € n'est sortie proprement.** Ce n'est pas « le comptoir n'existe pas » : c'est un trou de **méthode API** sur ce mot. Une passe SERP AliExpress (JSON `_dida_config_`) reste ouverte si Hakim la demande. Pas inventé.

---

## 3. Synthèse consolidée

| # | Candidat | Statut | Fiche | Coût rendu FR | Bloquant restant |
|---|---|---|---|---|---|
| 1 | Kit annuel 600 GPD + remin (OSWNKW) | **`FOURNISSEUR À TESTER`** | [1005005705096746](https://fr.aliexpress.com/item/1005005705096746.html) | **63,46 €** (CN, 3–9 j) | Compat RO 600G ; Pologne vide ; claims pH |
| 2 | Membrane 3013-600 ×2 | `OFFRE TROUVÉE` | [1005006026653705](https://fr.aliexpress.com/item/1005006026653705.html) | 48,59 € (fret non qualifié) | Stock 5 ; `exact` refusé |
| 3 | Alcaline 10″ / NCR102 | `OFFRE TROUVÉE` | 1005006944192709 / 32967120172 | 21,79 € / 23,39 € | Format vs nos boîtiers |
| 4 | 8 étapes 600G UV | `OFFRE TROUVÉE` | 1005011837944778 | 345,99 € (fret ambigu) | Même palier ; vendeur 4,4 |
| 5 | 8 étapes 800 GPD | `AUCUNE OFFRE EXPLOITABLE` | 1005009242052877 | — | Pas de livraison FR |
| 6 | Comptoir sans pose | `AUCUNE OFFRE EXPLOITABLE` | — | — | API muette cette passe |

**Rejets motivés (extrait)** : kit ATWFS 5 étapes **75 GPD** (`1005006717912553`, 270 ventes) — mauvais GPD ; préfiltre / UF OSWNKW-05 et cartouches UF 4+1 — autre machine ; boîtiers 3013 vides ; membranes 50–400 GPD ; charges Maifan DIY ; 800 GPD non livrable.

---

## 4. Contrôles prioritaires avant commande test

1. **Ouvrir le kit 2.1 en DSers brouillon seulement** (case Draft cochée, boutique morte `solinvictuss` décochée, `compareAtPrice` à purger s'il revient).
2. Sur échantillon : les 4 types rentrent-ils dans **l'OSWNKW 449 €** ? Dans le **RO 600G 299 €** ? Photo des boîtiers + filetages avant toute fiche publique.
3. Si le RO 600G est un compact propriétaire (type G2) : le kit ne va **que** sur l'OSWNKW. Dans ce cas le hero 299 € reste sans conso documentée — à dire sur la fiche, pas à mentir.
4. Recalculer le coût annuel affiché (PP 6 mois, PPC 6–12 mois, membrane 12–24 mois, alcaline 12 mois) **après** avoir vu les durées réelles, pas depuis la vignette.
5. Rédaction : zéro « pH 7,5 », zéro « alcalin santé », zéro note AliExpress. Titre du type « Kit d'entretien osmoseur 600 GPD — membrane 3013 + préfiltres + reminéralisation ».
6. Collection `osmoseurs` : **sortir ou débaptiser** la membrane 50 GPD (elle casse la cohérence expert). Le kit, une fois testé, pousse vers le seuil de 5.
7. Ne pas publier les brouillons 600 GPD SHUANGLI / OSWNKW compact.

---

## 5. Limites

- API `search` en mots rares : beaucoup de rabattements (600, GPD, Waterdrop, countertop). Les IDs retenus viennent des requêtes qui ont payé : `OSWNKW undersink`, `OSWNKW osmose`, `OSWNKW 600G`, `alkaline remineral`, `RO600GPD undersink` en `price_desc`.
- Compteurs d'avis produit souvent à 0 côté `variants` ; on cite aussi le `rating` de `search`.
- `exact` a refusé : Pologne kit (rupture), membrane 3013 (SKU nu), 8 étapes 600G (ambiguïté), 800 GPD (pas de livraison FR), alcaline `2Pcs` (2 SKU).
- Aucune SERP HTML AliExpress, aucun Chrome. Le comptoir reste un trou de méthode, pas un verdict marché.
- Aucune phase 5 lancée : un seul `FOURNISSEUR À TESTER`, décision d'import = Hakim.

---

## 6. Ce que Hakim tranche

1. **Importer le kit `1005005705096746` en DSers brouillon ?** (recommandé pour tester, pas pour publier.)
2. Laisser la membrane 50 GPD publique dans `osmoseurs`, la débaptiser, ou la dépublier ?
3. Relancer une passe **comptoir** via SERP AliExpress, ou garder le 299 € + kit comme offre de septembre ?
