# Phase 4 sourcing — panneaux muraux décoratifs bois (modèle The Panel Hub) — 2026-09-02

> **Nature de ce rapport : contrôle de SOURÇABILITÉ (niveau 2 — fiches existantes et vérifiées), pas une phase 4 de pipeline.**
> Aucun candidat n'est en `PASS_PREQUALIFICATION` : la mesure DataForSEO et la sonde prix tournent en parallèle. Hakim a demandé aujourd'hui, en toutes lettres, de « regarder les produits dispo sur AliExpress » pour ce type de produit ; l'orchestrateur `/qualifie-idees` a transmis cette instruction. Ce rapport répond donc à la question « existe-t-il des fiches AliExpress exploitables, et à quelles conditions logistiques ? » — il ne prononce **aucun GO fournisseur** (qui exigerait une commande test reçue et contrôlée) et ne commente pas la décision marché.
>
> Rappel du registre (01/09/2026) : « Panneaux muraux bois géométriques » et « Panneaux muraux aspect roche » sont en `REJET PHASE 2` (peu offrable, quantité, logistique). Le type 1 (tasseaux acoustiques) n'a pas d'entrée au registre à ce jour.

**Relevés du 02/09/2026 entre 14:17 et 14:32 (heure de Paris).** Prix, stocks, délais et variantes AliExpress sont dynamiques : tout doit être reconfirmé au panier pour une adresse française avant toute commande test. Aucun achat, aucun panier, aucun contact vendeur, aucune connexion.

## 1. Entrée

- Candidats reçus : aucun `PASS_PREQUALIFICATION`. Instruction explicite de Hakim (02/09/2026) transmise par l'orchestrateur `/qualifie-idees` : contrôle de sourçabilité sur trois types de panneaux muraux, par ordre de priorité :
  1. **Panneau acoustique à tasseaux bois sur feutre** (« acoustic slat wall panel », 240×60 ou 120×60 cm, placage chêne/noyer, feutre noir/gris) — le cœur.
  2. Panneau mural 3D bois géométrique (carrés concentriques, triangles, nid d'abeille).
  3. Panneau aspect roche / pierre en PU léger.
- Rapport de phase 3 : **aucun** (mesure en cours). Référence de format : `reports/validation-semrush-2026-07-17.md` § « Suivi du sourcing AliExpress ».
- Modèle commercial de référence : The Panel Hub (US), packs de 4 panneaux 249–1 141 $ soit ~62–285 $ le panneau (chiffres du brief ; le site n'est pas une boutique Shopify, `products.json` inaccessible, non re-relevé).

### Méthode et niveau de preuve

- **SERP AliExpress FR** rendue côté serveur dans le navigateur intégré (`/w/wholesale-<mots>.html?SortType=total_tranpro_desc`), JSON des 60 cartes extrait de `window._dida_config_._init_data_.data` : prix promo/liste, note, `tradeDesc` (champ séparé, pas de collage note/ventes), **pays d'expédition** (`shipFrom`), tags (« Offre lève-tôt, plus que 1 », « Livraison gratuite »…). 8 SERP lues : `acoustic slat wall panel`, `panneau acoustique tasseaux bois`, `panneau acoustique lamelles bois feutre`, `wood slat acoustic panel 120x60`, `akupanel 240x60`, `3d wood wall panel walnut mosaic`, `panneau mural pierre pu polyurethane`, `pu stone wall panel faux stone`. Deux requêtes FR (`panneau mural bois 3d géométrique massif`, `panneau mural 3d bois massif hexagonal`) ont rendu 0 résultat.
- **Passerelle API lecture seule** (`codex-chasse-clusters/tools/aliexpress_vps_gateway.py`, health OK à 14:16) : `variants` (prix réel `offer_sale_price` TTC, stock par SKU, ventes, magasin et ses trois sous-notes) et `exact` (fret vers la France : transporteur, gratuit ou frais, délai min/max). 22 appels `variants`, 17 appels `exact`. L'endpoint `search` de cette API a été essayé sur 23 requêtes en mots rares (« slat felt », « akupanel », « tasseaux feutre », « PET lattes », « pu stone veneer »…) : **il ne sert pas cette famille** (tri par popularité, aucun mot rare propre) — 2 fiches pertinentes sur ~800 lignes. Toute la découverte vient de la SERP.
- **API avis publique** (`feedback.aliexpress.com/pc/searchEvaluation.do`) : note moyenne, nombre d'avis, pays des acheteurs, texte. 17 fiches interrogées.
- **Plafond de preuve : B+** (SERP JSON + API variants/exact + API avis). Les pages produit `/item/` ne chargent pas dans le navigateur intégré (anti-bot connu, constat 09/08/2026) : aucune fiche n'est en classe A. La montée en A (photos HD, % d'avis positifs du vendeur, description complète) se fait dans le Chrome de Hakim.
- **Écart connu** : le compteur « N vendus » de la SERP et le `sales_count` de l'API divergent parfois fortement (ex. 35 vs 2, 306 vs 33). Les deux sont donnés ; aucun n'est confirmé en PDP.

## 2. Par type de produit

### Type 1 — Panneau acoustique à tasseaux bois sur feutre — `FOURNISSEUR À TESTER`

**Constat général (02/09/2026).** La catégorie existe sur AliExpress FR mais elle est **jeune** : la plupart des fiches ont des identifiants récents (`10050120…`–`10050130…`), 0 à 35 ventes affichées, 0 à 2 avis. L'offre exploitable est portée par **des magasins enregistrés en Chine avec entrepôts en Allemagne ou en Pologne**, qui vendent le **format 120×60 cm par lots de 2 ou 4**, port gratuit, livraison 2–10 jours, sans douane (intra-UE). Le format **240 cm n'existe pas à un coût rendu exploitable** (voir § 240 cm).

#### Fiche retenue pour un test — [1005010510383652](https://fr.aliexpress.com/item/1005010510383652.html)

- **Titre :** « Panneaux acoustiques à lattes de bois 120x60x2.1cm, lot de 4 pour un décor élégant, réduction du bruit, panneau texturé 3D »
- **Magasin :** TLGREEN Outdoor Store (id 1103669508, pays d'enregistrement CN, entrepôt Allemagne). Sous-notes API : article conforme 4,7 · communication 4,8 · rapidité 4,8. Ce magasin figurait déjà dans le rapport du 17/07/2026 (canapé modulaire enfant) avec 95,7 % d'avis positifs — à reconfirmer sur la PDP, non exposé par l'API.
- **Variante contrôlée (02/09, 14:25) :** `Classic Oak` / `120 x 60 cm - 4 Pcs` / `Allemagne` / 4 pièces / 2,1 cm — SKU 12000052711468926. Variante `Black Oak` identique (SKU …927). **Prix de la variante : 116,99 € TTC** (`tax_included: true`), prix de liste 354,52 € (remise affichée artificielle). **Stock : 50 par coloris.** Soit **29,25 € le panneau 120×60**.
- **Fret vers la France (API `exact`, 02/09, 14:27) :** GLS DE Pan-European 3–7 j (livraison 05–09 sept.), DHL DE Pan-European 3–8 j, DPD DE 3–8 j — **tous gratuits, avec suivi, expédiés d'Allemagne**. **Coût rendu : 116,99 € le lot de 4** (TVA annoncée incluse ; à confirmer au panier).
- **Preuve sociale :** SERP « 35 vendus », note 5,0 · API `variants` : 2 ventes · API avis : **1 avis** (Espagne, 16/01/2026, 5★, sans texte). Faible.
- **Caractéristiques annoncées par le vendeur (non contrôlées) :** MDF + feutre, épaisseur 2,1 cm, « texturé 3D ». Ni classement feu, ni essence de placage, ni composition du feutre annoncés dans les données lues.
- **Signaux de risque :**
  - **libellés SKU recyclés** : les `raw_value` de l'API disent « Rouge », « BLANC », « 12x12x1" », « 6 pièces », « 1,2 cm » derrière les valeurs affichées « Classic Oak », « 120×60 », « 4 », « 2,1 cm » → la fiche a été créée en réutilisant la structure d'un autre produit ; l'avis unique porte d'ailleurs le SKU « BLANC 12x12x1" ». Le contenu réel du colis doit être vérifié sur échantillon ;
  - écart 35 ventes (SERP) vs 2 (API) ;
  - un seul avis, aucun texte, aucune photo client ;
  - tag « Meilleur prix sur des offres similaires » (agrégation d'offres).
- **Pourquoi retenue :** seule fiche du lot avec à la fois un stock réel (50), un fret UE gratuit vérifié en API, un avis client et un vendeur déjà croisé par la maison. Prix au panneau (29,25 €) dans la fourchette du lot.
- **Statut : `FOURNISSEUR À TESTER`** — jamais « validé ». Le vendeur est sous le seuil de preuve sociale souhaité (critères § Protocole AliExpress : commandes suffisantes), donc « à tester avec justification » : justification = seule offre UE complète et cohérente de la catégorie au 02/09.

#### Alternatives contrôlées (type 1)

| # | Fiche | Magasin (entrepôt) | Variante contrôlée · prix 02/09 | Fret FR (API `exact`) | Preuve sociale | Statut · réserves |
|---|---|---|---|---|---|---|
| A2 | [1005012845809901](https://fr.aliexpress.com/item/1005012845809901.html) | TLGREEN Outdoor Store (DE) | `Classic Oak` ou `Black Oak` · 4 × 120×60×2,1 cm · **107,39 €** TTC (liste 357,97), stock 20–24 · 26,85 €/panneau | même entrepôt DE que la fiche retenue ; `exact` non appelé | SERP 4 vendus, pas de note · API 4 ventes · 0 avis | `OFFRE TROUVÉE` — même produit, 9,60 € moins cher, mais 0 avis ; tag « Offre lève-tôt, plus que 2 » contredit par le stock API (20–24) = fausse rareté |
| A3 | [1005012013334317](https://fr.aliexpress.com/item/1005012013334317.html) | TWISTERCK LOCAL Store (CN, entrepôt DE) · 4,6 / 4,6 / 4,7 | `4PCs 120x60cm` **108,39 €** (27,10 €/panneau, stock 21) · `2PCs 120x60cm` 72,39 € (stock 18) · `4PCs 120x30cm` 71,39 € · `2PCs 120x30cm` 53,39 € | DHL / DPD / GLS DE, **gratuit, 3–10 j** (05–12 sept.), suivi | SERP 10 vendus, 5,0 · API 10 ventes · **2 avis** (DE, 11/06/2026, 5★) | `FOURNISSEUR À TESTER` — second choix ; propose aussi le 120×30 ; prix de liste 349,65 € (remise artificielle) ; « Prix le plus bas en 90 jours » |
| A4 | [1005012532048355](https://fr.aliexpress.com/item/1005012532048355.html) | A-GREEN Store (CN, entrepôt DE) · 4,7 / 4,7 / 4,7 | `Classic Oak 4Pcs` 120×60×2,1 **105,39 €** (26,35 €/panneau) · 2 pcs 59,99 € · coloris Classic / Black / Grey oak · stock 19 | DPD DE, GLS DE, **gratuit, 3–10 j** | SERP 4 vendus · API 3 ventes · **0 avis** | `OFFRE TROUVÉE` — 0 avis ; libellé SKU « Classic Oak 24Pcs » incohérent ; « 39,39 € économisés » sur liste 210,78 € |
| A5 | [1005012482573788](https://fr.aliexpress.com/item/1005012482573788.html) | Cozzar Store (PL) · 4,6 / 4,6 / 4,7 | `4 Piece-Walnut Brown` 120×60 **78,02 €** (19,50 €/panneau, stock 8) · 2 pcs 49,16 € (stock 9–10) · Oak Black / Oak White · « placage bois véritable » annoncé | Seller Shipping PL, **gratuit, 2–9 j** (04–11 sept.), suivi | SERP 5 vendus, pas de note · API 5 ventes · **0 avis** | `OFFRE TROUVÉE` — le moins cher du lot, mais 0 avis et stock faible (8–10) ; « placage véritable » à contrôler sur échantillon |
| A6 | [1005012992024170](https://fr.aliexpress.com/item/1005012992024170.html) | IdealHouse Home Store (DE) · 4,6 / 4,7 / 4,7 | lot de 2 × **120×30×2,1 cm** chêne, MDF + feutre polyester · **32,85 €** API (16,40 €/pièce ; SERP 26,28 €) · stock 44 | DHL DE 2–7 j, GLS 3–8 j, DPD 3–10 j, **gratuit** | 0 vente · 0 avis | `OFFRE TROUVÉE` — intéressant comme **format compact** ; « Offre lève-tôt, plus que 1 » contredit par stock 44 |
| A7 | [1005012091989887](https://fr.aliexpress.com/item/1005012091989887.html) | Artpanel (expédié France, SERP) | dalle **60×60×2 cm** lattes bois + feutre · **62,69 €** SERP (liste 118,19) | non relevé : **API `variants` en erreur 604** (fiche non lisible) | 0 vente · pas de note | `OFFRE TROUVÉE` — seule dalle 60×60 bois+feutre expédiée de France ; à ouvrir en PDP dans Chrome |

#### Rejets motivés (type 1)

- **Format 240 cm — aucune offre exploitable au 02/09/2026 :**
  - [1005012301855585](https://fr.aliexpress.com/item/1005012301855585.html), [1005012301891474](https://fr.aliexpress.com/item/1005012301891474.html), [1005012306268182](https://fr.aliexpress.com/item/1005012306268182.html), [1005012301841612](https://fr.aliexpress.com/item/1005012301841612.html) — WEILIANGYAO Store (FR), lames 2400×200 mm à **339,10 / 480,50 / 579,70 / 671,26 €** ; fret FR gratuit (Colissimo, Chronopost, GLS… 1–10 j) mais **0 vente, 0 avis, sous-notes vendeur 3,8 / 3,9 / 4,3 (sous seuil)**, libellé de variante « army green » pour un panneau noyer, prix ×2 à ×4 du marché. Même magasin pour les 1200×600 à 157–184 € ([1005012306254314](https://fr.aliexpress.com/item/1005012306254314.html), [1005012357338307](https://fr.aliexpress.com/item/1005012357338307.html), [1005012353464000](https://fr.aliexpress.com/item/1005012353464000.html)). Rejet : vendeur sous seuil + fiche incohérente + prix.
  - [1005011895332475](https://fr.aliexpress.com/item/1005011895332475.html) — Shop1105406137 (CN), 4 lames 108"×11" (≈ 274×28 cm) « Rustic Walnut » 205,99 € : fret FR **FedEx IE 672,64 €, 64–74 jours** (meilleure option) → impraticable.
  - [1005009583663717](https://fr.aliexpress.com/item/1005009583663717.html) — « Akupanel » 240×60 cm 142,99 € (CN) : `exact` renvoie **`DELIVERY_SERVICE_EXCEPTION` — aucune livraison France**, variantes « Contact us for a… » (fiche B2B), 0 vente.
  - [1005012085435362](https://fr.aliexpress.com/item/1005012085435362.html) — 4 lames 94,49"×12" (≈ 240×30 cm) 164,39 € (CN) : SKU sans propriétés, fret non calculable, 0 vente.
  - [1005008523401970](https://fr.aliexpress.com/item/1005008523401970.html) — VEVOR 1200×600 (CZ) 216,39 €, 4 ventes, 5,0 : produit de marque VEVOR, prix hors fourchette du lot ; non retenu.
- **Vague de fiches clones DE à 149–232 €** pour 4 × 115×60 ou 120×60 ([1005012498627419](https://fr.aliexpress.com/item/1005012498627419.html), [1005012193392245](https://fr.aliexpress.com/item/1005012193392245.html), [1005012688692688](https://fr.aliexpress.com/item/1005012688692688.html), [1005012737631037](https://fr.aliexpress.com/item/1005012737631037.html), [1005012657856985](https://fr.aliexpress.com/item/1005012657856985.html), [1005012800680940](https://fr.aliexpress.com/item/1005012800680940.html), [1005012797969278](https://fr.aliexpress.com/item/1005012797969278.html), [1005012172829493](https://fr.aliexpress.com/item/1005012172829493.html), [1005012652513475](https://fr.aliexpress.com/item/1005012652513475.html), [1005012266440587](https://fr.aliexpress.com/item/1005012266440587.html)) : toutes à 186,45 € ou proche, 0 vente, « Offre lève-tôt, plus que 1 » systématique (fausse rareté). Rejet : prix ×1,7 des fiches retenues sans preuve.
- **Fiches CN « à coller » low-ticket** ([1005012595248809](https://fr.aliexpress.com/item/1005012595248809.html) 32,59 € 4 pcs noyer, [1005013061675416](https://fr.aliexpress.com/item/1005013061675416.html) 36,59 €, [1005012587033495](https://fr.aliexpress.com/item/1005012587033495.html) 20,99 € lot de 10/20, [1005011941364353](https://fr.aliexpress.com/item/1005011941364353.html) « MDF Akupanel » 22,19 €, fiches à 0,60–0,86 € l'unité) : autocollants ou petites lattes minces, pas le produit Panel Hub ; expédition Chine ; 0–1 vente. Rejet : hors type.
- **Feutre seul sans tasseaux** ([1005012720892530](https://fr.aliexpress.com/item/1005012720892530.html) ABIGAILY, DE, 4 dalles 60×60 feutre 28,79 €, fret DHL/GLS DE gratuit 3–10 j, 1 avis ES 19/08/2026 ; [1005012344787982](https://fr.aliexpress.com/item/1005012344787982.html) SELL TIME2, PL, 24 dalles feutre 51,78 €, DPD PL gratuit 3–9 j, SERP 56 vendus 5,0, API 40, 5 avis 100 %) : produits corrects et logistique UE vérifiée, mais **pas de bois** → hors type 1 ; notés comme **complément de gamme possible** (dalles acoustiques).
- **Mousse acoustique** (TOUO et consorts, 60 % des cartes SERP) : hors sujet.

### Type 2 — Panneau mural 3D bois géométrique (mosaïque noyer) — `FOURNISSEUR À TESTER`

**Constat.** Une seule famille de fiches domine : les **dalles mosaïque 30×30 cm en noyer noir / hêtre massif** d'un même magasin, GlowingVision Store, expédiées de Chine. Pas de 120×60 ; pas d'entrepôt UE relevé. Volumes de vente les plus élevés du dossier (SERP 300+), mais API à 33–37 ventes.

#### Fiche retenue pour un test — [1005011899324690](https://fr.aliexpress.com/item/1005011899324690.html)

- **Titre :** « Panneau mural en bois de noyer noir naturel, diffuseur acoustique 3D, mosaïque en bois massif pour la maison, le bureau, la chambre, décoration murale rétro »
- **Magasin :** GlowingVision Store (id 1100250086, CN). Sous-notes : conforme 4,6 · communication 4,8 · rapidité 4,8. Trois autres fiches du même magasin contrôlées (ci-dessous).
- **Variantes contrôlées (02/09, 14:26) :** 14 motifs (A–N). `1Pcs` / `A (30x30cm)` SKU 12000057861896275 : **28,19 € TTC** (liste 56,38). Autres 30×30 : 28,79–41,19 €. **60×30 cm** (J–N) : 47,19–52,69 €. **Stock : ~3 550 par SKU.**
- **Fret vers la France (API `exact`, 02/09, 14:29) :** Expédition standard AliExpress **gratuite, 13–21 j** (15–23 sept.) · Premium 21,16 €, 12–16 j · SG Air 2,45 €, 17–24 j · FedEx 94 € / UPS 115 €. **Coût rendu : 28,19 € la dalle 30×30 en standard**, soit ≈ 313 €/m² ; un mur équivalent à un panneau 120×60 = 8 dalles ≈ 225 € rendu.
- **Preuve sociale :** SERP 306 vendus, 5,0 · API 33 ventes · **2 avis** (FR 30/04/2026, JP 27/04/2026, 5★).
- **Signaux de risque :** délai hors cible (13–21 j) ; aucune photo client ; « Personnalisable » (fabrication à la commande possible) ; libellés de SKU des avis (« Style A », « Shining Gold ») ≠ libellés actuels.
- **Statut : `FOURNISSEUR À TESTER`** — fiche complète (prix, stock, fret, avis), réserves : délai Chine > 15 j, prix au m² élevé, format dalle ≠ panneau Panel Hub.

#### Alternatives contrôlées (type 2)

| # | Fiche | Magasin | Variante · prix 02/09 | Fret FR | Preuve sociale | Statut · réserves |
|---|---|---|---|---|---|---|
| B2 | [1005010235139168](https://fr.aliexpress.com/item/1005010235139168.html) | GlowingVision (CN) | 12 motifs `Black Walnut Type A–L` 1 pc · **25,19–44,79 €** · stock ~3 550 | non appelé (même magasin/mode que B1) | SERP 300 vendus 5,0 · API 37 · **4 avis** (ES, US, FR, PL) 100 % | `FOURNISSEUR À TESTER` — équivalent de la fiche retenue, meilleure preuve sociale (4 avis dont 1 FR) |
| B3 | [1005008757153361](https://fr.aliexpress.com/item/1005008757153361.html) | GlowingVision (CN) | `Black Walnut` / `1Pcs(30x30cm)` **32,99 €** · `Rubber Wood` 33,19 € · stock ~3 500 | Standard **gratuit 9–19 j** · Premium 18,75 € 7–11 j | SERP 121 vendus 4,6 · API 9 · **5 avis, 4,6** — 1 neutre (CH, 21/10/2025) : « je pensais qu'ils avaient une base adhésive, ce n'est pas le cas ; lourds, pas clair sur quoi/comment fixer » | `OFFRE TROUVÉE` — avis utile : **la fixation n'est pas fournie/claire**, point à cadrer dans l'offre |
| B4 | [1005012123058446](https://fr.aliexpress.com/item/1005012123058446.html) | GlowingVision (CN) | petits carrés noyer `1Pcs(30x30cm)` **23,59 €** · stock 3 500 | non appelé | SERP 163 vendus 5,0 · API 11 · 4 avis (CH) 100 % | `OFFRE TROUVÉE` |
| B5 | [1005005228563285](https://fr.aliexpress.com/item/1005005228563285.html) | (non interrogé en API) | triangles 3D bois massif **22,39 €** SERP | non relevé | SERP 89 vendus 5,0 · 5 avis 100 % dont 2 FR (« je ne m'attendais pas à quelque chose de plié, néanmoins satisfaite de la qualité » ; « conforme à sa description très beau produit ») | `OFFRE TROUVÉE` — confiance B (SERP + avis seulement) |

**Rejets (type 2) :** [1005012571827640](https://fr.aliexpress.com/item/1005012571827640.html) MeiJu 60×60 « piège à basses » 95,69–238,99 €, 3 ventes (prix) ; [1005008514969851](https://fr.aliexpress.com/item/1005008514969851.html) 188,39 €, 2 ventes (prix, 0 avis) ; autocollants et papiers peints grain bois (hors type) ; ~15 fiches clones noyer 25–95 € à 0 vente.

### Type 3 — Panneau aspect roche / pierre PU — `OFFRE TROUVÉE`

**Constat.** Deux sous-familles, toutes expédiées de Chine, aucun entrepôt UE relevé : (a) **grandes dalles PU 60×120 cm** (le format Panel Hub) à 16–33 € produit mais **fret France non calculable ou 31–35 €**, 0–9 ventes ; (b) **petites dalles 25×45 cm** (10–20 mm) à 14–66 €, fret gratuit ou 1,99 €, 9–18 j, un peu de preuve sociale — mais produit low-ticket, très différent du modèle. La SERP est saturée par ~40 fiches clones « pierre PU » à 29–61 € créées en série (ids `10050122847…`–`10050122914…`), 0 vente, tag « 6× sans frais » — signature d'une ferme de fiches.

| # | Fiche | Magasin | Variante · prix 02/09 | Fret FR (API `exact`) | Preuve sociale | Statut · réserves |
|---|---|---|---|---|---|---|
| C1 | [1005010804254235](https://fr.aliexpress.com/item/1005010804254235.html) | Grace Decoration And Building Materials Store (CN) · sous-notes **non affichées** | dalle **60×120 cm** · ép. 2 cm **16,29 €** · ép. 4 cm **20,39 €** · 30 SKU coloris **sans nom distinct** · stock ~200/SKU | **non calculable** : `exact` refuse (« Ambiguous variant: 15 SKUs match ») — le pays et le coût de port restent inconnus | SERP 42 vendus 5,0 · API 9 · 1 avis (SG, 25/03/2026) | `OFFRE TROUVÉE` — élément essentiel manquant (fret) ; à ouvrir en PDP dans Chrome pour lire le port FR |
| C2 | [1005012284619823](https://fr.aliexpress.com/item/1005012284619823.html) | Bework Select0957 Store (CN) · sous-notes non affichées | panneau **1220×600 mm** `colors` **33,19 €** · stock 500 | SG Air **30,87 €** 12–19 j · Large goods by land 31,90 € 13–34 j · Standard 35,22 € 8–16 j · express 364–485 € → **coût rendu 64–68 €** | 0 vente · 0 avis | `OFFRE TROUVÉE` — référence de coût de port d'un 122×60 depuis la Chine ; aucune preuve |
| C3 | [1005008476569958](https://fr.aliexpress.com/item/1005008476569958.html) | CHEE LYEE Store (CN) · 4,5 / 4,6 / 4,6 | dalles **25×45 cm ép. 10 mm** · 5 pcs `Hw-P1` **36,99 €** (30,99–37,79 selon motif) · 10 pcs 58,99–65,99 € · stock ~1 000 | AliExpress Selection Standard **1,99 €, 7–13 j** → 5 pcs (0,56 m²) ≈ 39 € rendu (≈ 70 €/m²) | SERP 22 vendus 5,0 · API 9 · 1 avis ES (08/05/2026) : « ne pèse rien, très facile à installer » | `OFFRE TROUVÉE` — logistique correcte, mais low-ticket et format ≠ modèle |
| C4 | [1005008552190365](https://fr.aliexpress.com/item/1005008552190365.html) | MY-W_33-y Store (CN) · 4,5 / 4,6 / 4,6 | dalle **25×45 cm ép. 2 cm** · 1 pc **14,69 €** · 5 pcs 28,19 € · 10 pcs 56,39 € · stock ~1 000 | Standard **gratuit 9–18 j** · Large goods 31,90 € 24–39 j | SERP 102 vendus 5,0 · API 4 · **11 avis 100 %** (ES 9, IT, FR) — mais textes : « arrivé avec un petit éclat sur le côté », « retourné : trop cher, une seule pièce livrée » | `OFFRE TROUVÉE` — meilleure preuve sociale du type 3 ; **casse d'angle et ambiguïté de quantité** signalées par les clients |

**Rejets (type 3) :** [1005009762959761](https://fr.aliexpress.com/item/1005009762959761.html) « pierre culturelle PU 300×100 cm » 4 367,99 € (prix absurde, 0 vente) ; [1005009279935070](https://fr.aliexpress.com/item/1005009279935070.html) 306,69 € (0 vente) ; [1005012828573281](https://fr.aliexpress.com/item/1005012828573281.html) 228,99 € (0 vente) ; la vague clone `10050122847…`–`10050122914…` (0 vente, ferme de fiches) ; [1005008699568287](https://fr.aliexpress.com/item/1005008699568287.html) roche PU pour terrarium 24,39 € note 3,3 (hors usage, note sous seuil) ; autocollants et papiers peints « fausse pierre » (hors type, low-ticket).

## 3. Synthèse consolidée

| Type | Statut (vocabulaire verrouillé) | Meilleure fiche | Variante · prix 02/09 | Coût rendu FR | Délai · origine | Preuve sociale | Confiance |
|---|---|---|---|---|---|---|---|
| 1. Tasseaux bois sur feutre | **`FOURNISSEUR À TESTER`** | [1005010510383652](https://fr.aliexpress.com/item/1005010510383652.html) TLGREEN | 4 × 120×60×2,1 cm Classic/Black Oak · **116,99 €** TTC | **116,99 €** le lot (port gratuit) · 29,25 €/panneau | **3–8 j · Allemagne** (GLS/DHL/DPD) | SERP 35 / API 2 ventes · 1 avis 5★ | B+ |
| 1. (2ᵉ choix) | `FOURNISSEUR À TESTER` | [1005012013334317](https://fr.aliexpress.com/item/1005012013334317.html) TWISTERCK | 4 × 120×60 · **108,39 €** (2 pcs 72,39 ; 120×30 dès 53,39) | 108,39 € (gratuit) · 27,10 €/panneau | 3–10 j · Allemagne | 10 ventes · 2 avis 5★ | B+ |
| 1. (moins cher) | `OFFRE TROUVÉE` | [1005012482573788](https://fr.aliexpress.com/item/1005012482573788.html) Cozzar | 4 × 120×60 Walnut Brown · **78,02 €** | 78,02 € (gratuit) · 19,50 €/panneau | 2–9 j · Pologne | 5 ventes · 0 avis | B+ |
| 2. 3D bois géométrique | **`FOURNISSEUR À TESTER`** | [1005011899324690](https://fr.aliexpress.com/item/1005011899324690.html) GlowingVision | dalle 30×30 motif A · **28,19 €** (60×30 : 47,19–52,69 €) | 28,19 € (standard gratuit) ; +21,16 € en Premium | **13–21 j · Chine** (12–16 j Premium) | SERP 306 / API 33 · 2 avis 5★ (1 FR) | B+ |
| 3. Aspect roche PU | **`OFFRE TROUVÉE`** | [1005008552190365](https://fr.aliexpress.com/item/1005008552190365.html) MY-W_33-y (petites dalles) ; grand format : [1005012284619823](https://fr.aliexpress.com/item/1005012284619823.html) | 25×45×2 cm · 1 pc **14,69 €** / 5 pcs 28,19 € ; 122×60 : **33,19 €** | 14,69 € (gratuit) ; 122×60 : **64–68 €** (port 31–35 €) | 9–18 j · Chine ; 122×60 : 8–34 j | 11 avis 100 % (casse signalée) ; 122×60 : 0 vente | B+ |

**Comparaison au modèle Panel Hub** (brief : ~62–285 $ le panneau, packs de 4 à 249–1 141 $) : le lot de 4 panneaux 120×60 rendu en France coûte **78–117 €** sur AliExpress (19,50–29,25 €/panneau), soit environ le tiers du prix de vente d'entrée Panel Hub par panneau. La fourchette Google Shopping France n'a pas été mesurée ici — **case laissée à l'orchestrateur / sonde prix**.

### Réponse nette à la question logistique

1. **Expédition vers la France : oui**, pour le type 1 uniquement depuis des **entrepôts UE** (Allemagne : TLGREEN, TWISTERCK LOCAL, A-GREEN, IdealHouse ; Pologne : Cozzar) — transporteurs GLS / DHL / DPD / Seller PL, **port gratuit, suivi, 2–10 jours**, sans douane. Les types 2 et 3 partent de **Chine** (9–21 j en standard).
2. **Coût rendu pour 1 panneau 120×60 :** aucune fiche UE ne vend le 120×60 à l'unité ; le plus petit conditionnement est **2 panneaux : 49,16 € (PL) à 72,39 € (DE)**, soit 24,60–36,20 € l'unité. À l'unité stricte, seul le **120×30** existe (lot de 2 à 32,85 €, DE, soit 16,40 € la pièce).
3. **Coût rendu pour un lot de 4 panneaux 120×60 :** **78,02 € (PL, 0 avis) / 105,39–108,39 € (DE) / 107,39–116,99 € (DE, TLGREEN)** — port inclus, TVA annoncée incluse (`tax_included: true`), à confirmer au panier.
4. **Délai :** 2–10 jours depuis DE/PL (livraison annoncée 04–12 septembre pour une commande du 02/09).
5. **Format 240 cm = hors gabarit, non sourçable au 02/09 :** les seules fiches 240 cm sont (a) un vendeur français à 339–671 € la lame, sous seuil et incohérent ; (b) des fiches chinoises dont le fret France vaut 672 € et 64–74 jours, ou qui **refusent la livraison France** (`DELIVERY_SERVICE_EXCEPTION`). Le 240 cm dépasse la longueur colis standard des réseaux GLS/DHL/DPD ; les entrepôts UE ne stockent que du 120 cm.
6. **Formats qui règlent le gabarit :** **120×60 cm** (standard des entrepôts UE, lots de 2/4) ; **120×30 cm** (DE, lot de 2 à 32,85 €, ou 2/4 chez TWISTERCK à 53,39/71,39 €) ; **60×60 cm** (Artpanel expédié de France 62,69 €, fiche non lisible par l'API ; feutre nu 60×60 DE 28,79 € les 4) ; **30×30 cm** (dalles mosaïque bois, Chine, 23–41 €). Le 120×60 est le format qui reproduit le mieux l'offre Panel Hub avec une logistique UE.

## 4. Contrôles prioritaires avant commande test

1. **Reconfirmer au panier** (adresse FR, sans commander) : prix TTC réel des SKU `Classic Oak / 120×60 / 4 Pcs` de 1005010510383652 et 1005012013334317, TVA, port, délai affiché.
2. **Ouvrir les PDP dans le Chrome de Hakim** (montée en classe A) : % d'avis positifs et ancienneté des magasins TLGREEN, TWISTERCK LOCAL, Cozzar, GlowingVision (non exposés par l'API) ; description complète ; photos HD ; conditions de retour (retour gratuit 15 j ?) et protection acheteur.
3. **Contenu exact de la variante** sur échantillon : nombre de panneaux, dimensions et épaisseur réelles, **placage bois véritable vs mélaminé/PVC** (annoncé « placage véritable » chez Cozzar, « aspect bois » chez A-GREEN, « plaqué MDF » chez TLGREEN A2), composition et couleur du feutre, lattes collées ou emboîtées.
4. **Libellés SKU recyclés** (TLGREEN : « Rouge / BLANC / 12x12x1" / 6 pièces / 1,2 cm » en valeurs brutes) : risque d'erreur de préparation en entrepôt ; à lever par la commande test.
5. **Emballage et casse** : panneaux MDF 120×60 en colis GLS/DHL ; angles et feutre ; les avis du type 3 signalent déjà des éclats. Peser et mesurer le colis reçu (base du calcul de retour/SAV).
6. **Fixation** : vis, colle ou clips inclus ? L'avis neutre du type 2 (B3) dit explicitement que la fixation n'est ni fournie ni claire. Les crochets/clips pour tasseaux existent en fiches séparées (SERP `akupanel 240x60`, 2,5–10 €).
7. **Caractéristiques annoncées à ne pas reprendre comme faits** : « acoustique / réduction du bruit », « MDF », « feutre polyester », « placage véritable », « ignifuge » — aucune donnée de classement feu (Euroclasse) ni de fiche technique lue ; à demander/contrôler avant toute publication.
8. **Écart ventes SERP/API** (35 vs 2 ; 306 vs 33) à trancher en PDP.
9. **Anti-doublon fournisseur** : aucune boutique de la maison (Tuftéo, Bonum Vitae, Noirmont) n'est sur cette famille ; TLGREEN Outdoor Store a déjà été relevé le 17/07/2026 sur un autre produit (canapé enfant), sans commande passée à notre connaissance.

## 5. Limites

- **PDP non ouvertes** : anti-bot AliExpress dans le navigateur intégré (constat 09/08/2026 reconduit) ; aucune fiche en classe A ; plafond **B+**. Pas de CAPTCHA rencontré sur les SERP.
- **Passerelle API** : `search` inutilisable sur cette famille (aucun mot rare, tri par popularité — 23 requêtes, 2 fiches pertinentes) ; `variants` en erreur 604 sur la fiche Artpanel FR (1005012091989887) ; `exact` refuse les fiches à coloris sans libellé distinct (1005010804254235 : « 15 SKUs match ») et les fiches sans propriétés (1005012085435362) ; `DELIVERY_SERVICE_EXCEPTION` sur l'Akupanel 240×60 CN ; `sales_count` API ≠ « vendus » SERP sans que l'on sache lequel fait foi ; % d'avis positifs vendeur et ancienneté **non exposés** (seulement trois sous-notes).
- **Deux SERP FR vides** (« panneau mural bois 3d géométrique massif », « panneau mural 3d bois massif hexagonal ») : le vocabulaire FR naturel ne matche pas ; les requêtes EN ont servi.
- **The Panel Hub** : site non-Shopify (Next.js), `products.json` indisponible, catalogue non re-relevé ; les prix du brief sont repris tels quels.
- **Google Shopping France** : non mesuré (hors périmètre de ce contrôle ; sonde prix en cours ailleurs).
- **Catégorie jeune** : toutes les fiches UE ont 0–35 ventes et 0–2 avis ; aucune ne dépasse les seuils de preuve sociale souhaités. Aucune ne peut donc être présentée comme validée — au mieux « à tester avec justification ».
- **Ce que j'ai lu qui ressemblait à une instruction** : rien, hormis les mentions vendeur « Contact us for a… » dans les variantes de 1005009583663717 (non suivies).

---

*Rapport produit par l'agent phase 4 (sourçabilité) le 02/09/2026. Données brutes de la session (JSONL `search`, `variants`, `exact`, JSON avis) dans le scratchpad de session, non versionnées.*
