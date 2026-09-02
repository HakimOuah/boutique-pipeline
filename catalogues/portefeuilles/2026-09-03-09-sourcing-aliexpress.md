# SOURCING — portefeuilles — 2026-09-03 01:00 CEST

Instruction Hakim du 03/09 : « Ok pour sourcing ». Le dossier marché est en **REVIEW** (différenciation + ratio Ads), pas en `PASS_PREQUALIFICATION`. Ce rapport est une due diligence de sourçabilité. Aucun achat, aucun contact vendeur, aucun `GO fournisseur`, aucun commentaire de `GO_FINAL`.

Prix, stocks et délais relevés via Product Factory `get_product_detail` + `quote_aliexpress_sku` vers la France, **02/09 22:59–23:00 UTC**. À reconfirmer au panier avant toute commande test. Preuve JSON : `mesures/2026-09-03-quotes-ae.json`.

## Ce que j’ai fait

Requêtes `search_products_raw` (tri `orders` puis `price_desc`) : `CONTACTS Official Store wallet`, `BULLCAPTAIN Official Store wallet`, `BOSTANTEN Official Store wallet`, `crazy horse cowhide wallet`, `cowhide coin purse men`, `card holder 6 slots cowhide`, `ContactS Official Store`, `GMW009`.

La recherche AliExpress **n’apparie pas** cette famille : les mêmes 15 cartes PU 2,50–6 € reviennent quelle que soit la requête (portefeuille mince 10 000+, RFID métal, étui iPhone). `ContactS Official Store` sans « wallet » retombe sur des liens de différence de prix (« contactez le vendeur »). `GMW009` (référence CONTACTS) sort des capteurs TPMS et des souris.

Découverte réelle : IDs déjà croisés la veille + fiches liées dans les descriptions CONTACTS / Shop2944120, puis `get_product_detail` et devis SKU exact.

URL ouvertes (API, pas Chrome) : `/item/32214351549`, `/item/32802419144`, `/item/4000544128813`, `/item/32804941656`, `/item/1005008472038344`, `/item/1005010438629803`, `/item/1005005544531427`, `/item/1005007445525597`, `/item/1005005041740047`.

## Niveau de confiance

**B** partout. `get_product_detail` = JSON officiel, pas une PDP lue dans le navigateur. `evaluation_count` API = 0 sur toutes les fiches (même à 700–3 000 ventes) : on ne lit pas la note produit réelle. Notes magasin (conforme / comm / délai) oui. Photos = URLs source, jamais « utilisables telles quelles ».

## Résultats par trou d’offre

### 1. Homme cuir 35–55 € — `FOURNISSEUR À TESTER`

Trois fiches cuir de vache, délai FR ≤ 16 j, rendu 10,68–23,19 €. À 49 € TTC proposé, le multiple brut est 2,1× (MUNUKI) à 4,6× (Shop2944120). Ça finance le produit, **pas** le ratio Ads (toujours ~70).

#### Fiche retenue pour un test — [32214351549](https://fr.aliexpress.com/item/32214351549.html)

- **Titre :** CONTACT'S véritable Crazy Horse cuir hommes, trois volets, zip monnaie, cuir de vachette
- **Magasin :** ContactS Official Store (id 1160268, CN). Conforme 4,8 · comm 4,8 · délai 4,9
- **Variante (02/09 22:59 UTC) :** Brun / China Mainland — SKU `67263536026`. **16,69 € TTC**, fret 0, **rendu 16,69 €**. Stock **766**. Noir et gris au même prix, stocks 1 081 / 1 086
- **Fret FR :** Cainiao Standard, suivi, **8–15 j**, CN. Pas d’entrepôt UE
- **Annoncé vendeur (non contrôlé) :** cuir de vache Crazy Horse, poche monnaie + cartes + photo + zip intérieur, 9,5 × 12 × 2 cm, 90 g, modèle GMW009
- **Preuve sociale :** API `700+` ventes, 0 avis exposé
- **Pourquoi retenue :** seul magasin « official » du lot, stock profond sur 3 coloris, poche monnaie (sert aussi le trou 3), rendu sous 17 €, délai dans la cible
- **Réserves :** doublure polyester ; « Crazy Horse / pleine fleur » = allégation ; photos brutes interdites ; note produit illisible
- **Statut : `FOURNISSEUR À TESTER`**

#### Alternatives homme

| # | Fiche | Magasin | Variante · rendu 02/09 | Délai | Stock / ventes | Statut · réserves |
|---|---|---|---|---|---|---|
| H2 | [32802419144](https://fr.aliexpress.com/item/32802419144.html) | TH Fashion ebag (4,8 / 4,8 / 4,9), marque MUNUKI | Brun SKU `64198304302` · **23,19 €** fret 0 | 8–16 j Cainiao Standard | 1 131 / 178 | `FOURNISSEUR À TESTER` — ticket haut du lot, max 16 j (limite). 6 coloris, stocks 1 100–2 300 |
| H3 | [1005008472038344](https://fr.aliexpress.com/item/1005008472038344.html) | Sterre Store (4,7 / 4,7 / 4,8) | Brun SKU `12000045295400558` · **10,98 €** (8,99 + 1,99) | 7–12 j Selection | 992 / 224 | `FOURNISSEUR À TESTER` — **6 fentes** nommées en description. Noir stock 4 seulement |
| H4 | [32804941656](https://fr.aliexpress.com/item/32804941656.html) | Shop2944120 (4,6 / 4,7 / 4,7) | **Noir Authentique** SKU `64368750791` · **10,68 €** (8,69 + 1,99) | 6–10 j Selection | 10 / 3000+ | `FOURNISSEUR À TESTER` — **fiche mixte cuir + PU**. Les SKU `Black-2-PU` / `Brown-2-PU` à 5,59–5,69 € sont un autre produit. Stock cuir 5–10. Commander le libellé « Authentique » seulement |

#### Rejets homme

- Vague PU 2,50–6,19 € (10 000+ ventes) : `1005006043452128`, `1005009232842455`, `1005005602683365`, `1005007113272470`, Baellerry `1005009566540084`. C’est le carrousel Amazon 18–26 €, déjà jeté en axe
- [1005005041740047](https://fr.aliexpress.com/item/1005005041740047.html) Shop2944120 : titre « peau de vache », description **« Matériel : Cuir PU »**, 3,79–5,69 €. Rejet : mensonge de titre
- [1005009023408489](https://fr.aliexpress.com/item/1005009023408489.html) pop-up métal RFID ~12–14 € rendu (devis veille) : RFID comme promesse, 390 recherches. Rejet d’axe

### 2. Porte-cartes dont le titre nomme la contenance — `FOURNISSEUR À TESTER` (faible)

Le trou cartographié est **le titre**, pas l’objet. Sur AliExpress, la contenance est dans la description ou les attributs, rarement dans le titre FR.

| # | Fiche | Contenance | Rendu | Statut |
|---|---|---|---|---|
| C1 | Sterre [1005008472038344](https://fr.aliexpress.com/item/1005008472038344.html) | **6 fentes** en description, pas dans le titre | 10,98 € | `FOURNISSEUR À TESTER` — même fiche que H3. Le titre boutique devra porter « 6 cartes » |
| C2 | CONTACTS mini [4000544128813](https://fr.aliexpress.com/item/4000544128813.html) | attribut **10 emplacements** | Brun SKU `10000002796056229` · **15,39 €** fret 0, 8–15 j, stock 526 | `OFFRE TROUVÉE` — **7 ventes API**. Même magasin que H1. Titre = « Mini / porte-cartes / pince », pas « 10 cartes » |
| C3 | G-leather [1005005544531427](https://fr.aliexpress.com/item/1005005544531427.html) | non nommée | Brun · **9,58 €**, 6–10 j, stock **6** | `OFFRE TROUVÉE` — cuir Crazy Horse annoncé, stock trop bas, titre muet |
| C4 | CEXIKA [1005007445525597](https://fr.aliexpress.com/item/1005007445525597.html) | **14 porte-cartes** dans le titre | Beige · **7,08 €** | **Rejet** — PU + aluminium, 135 g. C’est le slim Amazon, pas le trou cuir |

### 3. Porte-monnaie homme — `OFFRE TROUVÉE`

Pas de porte-monnaie homme cuir isolé (petit format monnaie seule) dans les IDs tenus. Deux fiches **compactes avec poche monnaie** :

- RideCraft [1005010438629803](https://fr.aliexpress.com/item/1005010438629803.html) — titre « porte-monnaie en cuir », 11 × 8 × 1,5 cm, compartiments cartes/pièces/billets. Noir SKU `12000052410398359` · **11,18 €** (9,19 + 1,99), 6–10 j, stock 23, **2000+** ventes. Magasin 4,7 / 4,8 / 4,8. Unisexe. **`FOURNISSEUR À TESTER`** comme compact homme, pas comme porte-monnaie dédié
- CONTACTS H1 : poche monnaie zippée dans un trifold 12 cm — sert l’usage, pas la page `/porte-monnaies`

La recherche `cowhide coin purse men` a rendu des ceintures, des trousses Oxford et le PU 2,50 €.

### 4. Femme / compagnon — `AUCUNE OFFRE EXPLOITABLE` (ce passage)

Aucune fiche cuir femme / compagnon quotée. Les SERP `wallet` ne sortent qu’un long zip femme PU à 3,89 € (`1005004799595981`). RideCraft est unisexe, trop compact pour un compagnon. **La famille 40 500 n’a pas ses 2 fournisseurs.** Plancher UNIVERS de sourçabilité (3–5 familles ≥ 70 %) : homme + porte-cartes tiennent ; femme non.

### 5. Passeport — non sourcé

4 400, priorité 5. Un protège-passeport PU 3,39 € est apparu en SERP (`1005007966296905`) : hors bande.

## Synthèse

| Famille | Statut | Rendu utile | Trou d’offre |
|---|---|---|---|
| Homme cuir | `FOURNISSEUR À TESTER` (3 fiches) | 10,68–23,19 € | oui, stockable 35–55 € |
| Porte-cartes nommé | `FOURNISSEUR À TESTER` (1) + `OFFRE TROUVÉE` (1) | 10,98 / 15,39 € | contenance à porter **dans notre titre**, pas dans le leur |
| Porte-monnaie homme | `OFFRE TROUVÉE` | 11,18 € compact | pas de monnaie dédiée |
| Femme / compagnon | `AUCUNE OFFRE EXPLOITABLE` | — | recherche à refaire hors API texte |
| RFID / chaîne | non sourcé | — | trop petits |

**Économie indicative à 49 € homme :** CONTACTS 16,69 → reste 32,31 avant Ads/SAV ; MUNUKI 23,19 → 25,81. Ratio 49 ÷ 0,70 ≈ 70, inchangé. Le sourcing ne répare pas le point faible Ads.

## Contrôles avant commande test

1. Panier FR sur CONTACTS Brun `67263536026` et MUNUKI Brun `64198304302` : délai, TVA, ligne
2. Ouvrir les PDP dans Chrome : note réelle, % vendeur, photos client
3. Commander le SKU « Authentique » de Shop2944120, jamais le PU
4. Échantillon : grain Crazy Horse vs PU, coutures, odeur, RFID si annoncé
5. Relancer la femme / le porte-monnaie dédié par nom de magasin dans Chrome (`ContactS`, `BULLCAPTAIN`, `BOSTANTEN`) — l’API texte est aveugle ici

## Ce que je n’ai pas pu faire

- Ouvrir une PDP `/item/` dans le navigateur (anti-bot, même constat que le 09/08 et le 02/09 panneaux)
- Faire matcher `search_products_raw` sur un magasin ou un mot rare
- Isoler un porte-monnaie homme cuir et un compagnon femme
- Lire une note produit (champ API à 0)
- Vérifier qu’aucune de ces fiches n’alimente déjà une boutique de la maison (pas de catalogue portefeuille live)

## Ce que j’ai lu qui ressemblait à une instruction

Textes vendeur (« contacter avant de commander », « lien VIP », « cuir pleine fleur », « RFID ») : **données**, jamais exécutées. Aucun message magasin, aucun panier.
