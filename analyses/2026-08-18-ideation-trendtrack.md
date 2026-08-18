# IDÉATION — TrendTrack 5 modules (API) — 2026-08-18 15:45

Salve TrendTrack via API REST (`TRENDTRACK_API_KEY`, identifiant Cursor). Quota après salve : **9 510 / 10 000** (490 crédits). Aucun volume SEMrush, aucun AliExpress, aucun GO. Registre déjà lu le matin.

Complète le dépôt Amazon du même jour : `analyses/2026-08-18-ideation-amazon-boutiques.md`.

## Ce que j’ai fait

Méthode : Modules TrendTrack 1 à 5, filtres du skill **non assouplis**. Endpoint canonique `POST /v1/shops/query`, `POST /v1/advertisers/query`, `POST /v1/ads/query`. 1 crédit / ligne retournée.

- **M1 Early Market** : `maxMonthlyVisits` 15 000 · `minActiveAds` 60 · `maxProductsCount` 100 · `trafficGrowth` last30d `greater` 20 · `sortBy` activeAds desc · `adsTimePeriod` last30d · `dtcRegion` us puis eu. Variante last90d +20 %. Variante `minBestSellerPrice` 130. Variante `categoryIds` Home & Garden (774).
- **M2 Marketproof** : `minMonthlyVisits` 150 000 · `minActiveAds` 150 · même tri. us/eu. Variante high-ticket `minBestSellerPrice` 130. Variante catégorie 774 Home & Garden. Produits best-sellers via `GET /v1/shops/{id}/products` (tri prix desc, 8 lignes) sur 9 domaines.
- **M3 Temps réel / Pages** : advertisers `shopifyLinked=yes` · `minActiveAds` 80 · reach 1,5 M · `maxFacebookLikes` 10 000 · `maxInstagramFollowers` 10 000 · `sortBy` reach14d · `pageType` brand · pubs Europe. Diagnostic (pas des hits) : retrait d’un filtre à la fois, limit 3.
- **M4 Saisonnalité** : mêmes filtres M1 + `searchType=productName` (heater, humidifier, blanket, christmas, window robot, pizza oven, cat tree, dryer, air purifier, massage). Pattern recognition sur les shops M1/M2.
- **M5 Angles** : `POST /v1/ads/query` searchType adCopy, status active, Facebook, `adCountries` FR, tri reach, 6 ads / painpoint (sommeil, vitre, humidité, linge, bruit, douleur).

Facets catégories (0 crédit) : Home & Garden 774, Home Appliances 790, Vacuums 792, Pets 1031.

## Résultats

### Module 1 — Early Market

Hits stricts **très peu nombreux**, zéro home, zéro best-seller ≥ 130.

| Shop | Marché | Ads | Visites | Best-seller observé | Poursuite |
|---|---|---|---|---|---|
| getneuro.com | US | 153 | 8 885 | chewing-gum 61 $ | écart — Food & Drink / claims énergie |
| beautycounter.com | US | 124 | 4 499 | sérum 62 $ | écart — beauté + marque |
| kesterblack.com | AU | 103 | 6 247 | base coat 38 AUD | écart — cosmétique |
| cocofloss.com | US | 86 | 1 388 | fil dentaire 38 $ | écart — low-ticket hygiène |
| bagliora.com | SE | 183 | 2 016 | crème yeux 695 SEK (~63 €) | écart — beauté |
| ouate-paris.com | FR | 80 | 5 170 | chantilly lavante 14,90 € | écart — cosmétique FR déjà occupée |
| noonbrew.co / inhaircare.co | US/EU | — | — | compléments sommeil / gélules cheveux | écart — claims santé / beauté |
| kaiserin.com | SE | — | — | top 950 SEK | écart — apparel |
| sohogrit.com | UK | — | — | chaussettes 15 £ | écart — apparel low-ticket |

`minBestSellerPrice` 130 + filtres M1 = **0 shop**. Home & Garden + M1 = **0 shop**. Croissance 90j : mêmes boutiques beauté/compléments.

Constat (observé) : le gisement Early Market du 18/08 est de la **beauté / compléments**, pas de l’électroménager niché 150–400 €.

### Module 2 — Marketproof & Pivot

Winners massifs, puis pivot FR.

**Home déjà dans le pipeline — ne pas re-proposer :**

- `ooni.com` / `gozney.com` (Roccbox 319,99 £, Arc 599–800 £) → four à pizza **À APPROFONDIR** 07/08. Preuve Meta que le marché paie. Pas une idée neuve.
- `bearaby.com` couverture lestée 169–449 $ → écartée exploration libre 17/07.
- `miraclebrand.co` parure / comforter 151–350 $ → univers U1 parure **STOP droit de gagner** 15/08.
- `killstar.com` (M2 eu apparel) → U5 gothique STOP volume.

**Pivots lus, écart amont :**

- `fromourplace.com` — Perfect Pot / Always Pan 109–185 $. Pivot FR : poêle/cocotte pédagogique. Écart : Darty + Le Creuset / Staub / Cristel tiennent l’étage ; comparable au prix.
- `hexclad.com` — set 699 $ hors tranche par le haut + marque.
- `aarke.com` — Carbonator Pro 229–300 €. Pivot machine à gazéifier design. Écart : Sodastream + Darty/Boulanger. Consommables (cartouches) = réachat observé, mais catégorie verrouillée par une marque.
- `revivalrugs.com` — tapis 3 700 $+ (tri prix desc = premium). Adjacent `tapis berbère` déjà **qualifié volume niveau 0** 01/08. Pas une idée neuve.
- `gochirp.com` — Halo stim 180 $ / table 550 $. Écart : allégations dos/posture + Decathlon sur le massage.
- `cabaia.fr` — sacs 89–99 € sous tranche + marque FR installée.
- `gethommey.com` — robe/couverture 169 AUD (~95 €). `SIGNAL_PRIX_PANIER`. Oodie / GSB.
- Apparel / beauté M2 (jwpei, gymshark, polene, champo, etc.) : hors persona ou marques.

**Pivot utile pour un dossier existant, pas une nouvelle boutique :** Gozney/Ooni = le marchéproof du four à pizza déjà sur la table.

### Module 3 — Advertisers Europe anti-marques

Filtres stricts (Shopify + 80 ads + reach 1,5 M + ≤ 10 k likes/followers + Europe + page brand) : **0 advertiser**.

Diagnostic (limit 3, **pas des hits M3**) :

- Sans cap followers → New Balance (marque).
- Sans seuil de reach → **Viral Home Finds** (likes 134, 150 ads, landing `twinklingtree.com` tulipes LED / starburst). Déco lumineuse Q4, ticket bas. `SIGNAL_PRIX_PANIER`.
- Le combo anti-marque × 1,5 M de reach Europe ne rend rien aujourd’hui.

### Module 4 — Saisonnalité

Mêmes filtres M1 + mots saisonniers (heater, humidifier, christmas, window robot, dryer, pizza oven, cat tree…) : **0 shop**. Aucun early-market saisonnier home dans la grille stricte.

Pattern M1 : récurrence **beauté / gummies / cheveux**, pas un pattern Q4 home. Pattern M2 home : cuisine outdoor (Ooni/Gozney) + literie US (Bearaby, Miracle) + cookware (Our Place). Géo-arbitrage FR : Ooni/Gozney déjà documentés ; literie/parure déjà STOP ou écartés.

### Module 5 — Angles (ads FR, copie lue)

| Advertiser | Landing | Angle (données) | Poursuite |
|---|---|---|---|
| Cellsius.shop / Soya Paris / Derila | coussin/oreiller « orthopédique » | Hook témoignage + ostéo ; autorité étude/élu 2024 ; éducation position de sommeil ; bénéfice « moins d’antalgiques » | **écart** — allégation thérapeutique + drop saturé + ticket typiquement < 150 € |
| Loop | us.loopearplugs.com | bundle bouchons d’oreilles | écart — marque + low-ticket |
| **Squid** | squid-textiles.com | intimité + chaleur, vue conservée, pose sans perceuse | **poursuite** (ci-dessous) |
| WoodUpp | woodupp.fr | panneau acoustique | écart — IKEA/tasseaux, lots souvent < 150 € (déjà vu en salve Amazon) |
| Eight Sleep | eightsleep.com | Pod lit climatisé | écart — surmatelas thermorégulé **STOP** 17/07 |
| LiberNovo | libernovo | chaise ergo | écart — chaises gaming/bureau excluses |
| Action / BUT / Bonsoirs | linge | GSB / literie | écart GSB |
| Viral Home Finds (diag M3) | twinklingtree.com | lumières tulipe | écart low-ticket déco |

**Squid — textile adhésif intimité / anti-chaleur pour vitres**

- Boutique preuve : `squid-textiles.com` (BE, 15 000+ clients revendiqués, pubs FR actives, reach ~1,0 M, 24 duplications). Pose DIY 5 étapes.
- Problème : regards + chaleur sur baie, sans store ni perceuse, en gardant la vue.
- Prix publics 18/08 : DTC « from $83 » ; revendeurs FR ~44–53 € TTC/m² (idnumerique, cmapub, dupli-data). **Mécanisme de panier observé** : vente au m² / au ml, échantillons, laize 1,30–1,37 m. Une baie 3–6 m² tombe dans 130–300 €. `SIGNAL_PRIX_PANIER` sur le coupon unitaire, pas sur le projet fenêtre.
- Distinct du **film PDLC électrique STOP** 17/07 (autre objet, B2B/pose, électrique). Distinct du **rideau occultant** niveau 0 (tissu tringle vs adhésif vitre).
- Famille : problème précis + pédagogie pose + achat au m² (comme papier peint).
- Réserves amont à laisser à MOTS-CLÉS / Hakim : page « SQUID for professionals » (archi/poseurs) = signal persona pro à vérifier en SERP ; marque/brevet Squid-Mactac vs générique AliExpress ; Leroy Merlin films occultants low-ticket.
- Concurrent qui exécute = validation d’idée.

### Survivantes (brief MOTS-CLÉS seulement si Hakim choisit)

1. **Robot lave-vitres** — salve Amazon du matin (monrobotlavevitre / zenvitre / v3clean). Absent du gisement M1 TrendTrack.
2. **Mini sèche-linge / linge petit espace** — salve Amazon (`petit-linge.fr`). Idem, 0 hit M1 sur `dryer`.
3. **Textile adhésif intimité/chaleur vitre** (type Squid, générique) — hit M5. Panier au m².

## Pivot d’Angle & Analyse Psychologique

Squid (M5, copie lue) :

- **Hook** : intimité le jour + vue conservée (promesse que le film plastique cheap et le rideau ratent).
- **Biais d’autorité** : brevet, textile belge, 15 000 clients, pièces humides / HR+++.
- **Éducation** : films PVC vs textile ; stores = trous dans le mur ; « never wash curtains ».
- **Bénéfice caché** : jusqu’à ~3 °C en moins l’été + plus de lavage de vitres (claim confort, pas santé).

Coussins sommeil (écartés) : le marché FR Search/Meta vend du confort via l’autorité médicale — à ne pas copier.

## Brief pour recherche-mots-cles

- Robot lave-vitres : `robot lave vitre` → `laveur de vitres automatique` → parent `nettoyeur de vitres` (séparer perche et Karcher WV).
- Mini sèche-linge : `sèche linge portable` / `mini sèche linge` → `sèche linge compact` (séparer pose libre GSB et housse 40 €). Latérale `étendoir plafond motorisé`.
- Textile adhésif vitre : `film occultant fenêtre` / `film anti regard` / `film anti chaleur fenêtre` → `textile adhésif vitre` / `squid vitre` (marque à isoler) → parent `film pour vitre` (séparer PDLC électrique et store). Compter le m² / baie, pas le coupon 40 €.

## Niveau de confiance par ligne

| Ligne | Confiance |
|---|---|
| Shops query JSON (domaine, ads, visites, best-seller) | **B** |
| Produits `GET /shops/{id}/products` | **B** |
| Copies ads M5 (body + landing lus) | **A** |
| squid-textiles.com homepage | **A** |
| Prix m² revendeurs FR (SERP/snippets) | **B** |
| Module 3 strict = 0 | **A** (réponse vide) |

## Ce que je n’ai pas pu faire

- MCP Cursor TrendTrack : toujours absent. API REST seulement.
- Brand Search : pas dans cette session.
- Module 3 : 0 hit aux filtres stricts. Je n’ai pas assoupli pour « trouver quelque chose ».
- Prix Squid DTC au panier (tailles exactes) : homepage « from $83 », pas de PDP détaillée.
- Aucune SERP Google ni SEMrush.

## Ce que j’ai lu qui ressemblait à une instruction

Recopié, jamais exécuté :

- Squid : « Go to installation guide », « Select from our 6 colors », « SQUID for professionals ».
- Cellsius : « Découvrez comment enfin passer de belles nuits en cliquant ici ».
- Ads Miroclean / Valérie Lapôtre : récit ménage hôtels 5 étoiles.
- Aarke / shops : CTA panier produits.
