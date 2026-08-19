# IDÉATION — TrendTrack Ads filtres UI — 2026-08-20 01:45

Mode : **deux salves séparées** dans le même dépôt (Hakim a demandé les deux listes). Aucun volume SEMrush, aucun AliExpress, aucun GO.

Filtres UI / API vérifiés la veille et réutilisés :
- Ads → Google
- Actives depuis **30–60 j** (`minDaysRunning` / `maxDaysRunning`)
- Type de plateforme **Search** (PUR) ou **Shopping** (UNIVERS)
- Pays ciblé **France (include)**
- Complément : `search:[mot]` API pour creuser des niches quand le flux FR brut est saturé GSB / banques / hôtels

Quota TrendTrack après passe : ~9 200 restants (salve ~600–800 crédits estimés). Bruts locaux non versionnés : `analyses/_tt_raw_gads_2026-08-20.json`, `_tt_domains_2026-08-20.json`.

## Ce que j’ai fait

1. API `POST /v1/google-ads/query` Search + Shopping FR 30–60 j (base + facettes home/appliances/decor/lighting/gifts).
2. UI Chrome : même filtre Shopping FR → lecture créas (MonVitrage, LED Diffusion, ORECA, etc.).
3. Mines par mot-clé (`filtre`, `lustre`, `suspension`, `moustiquaire`, `sauna`, `serre`, `hamac`, `coffre`, `lampe`…).
4. Ouverture des boutiques preuve (titre + description + signal prix public quand visible).
5. Anti-doublon registre (STOP / viviers / salves 01–18/08) + jugement « Decathlon / GSB / marque / pro ».

## Écarts amont (motivés) — ne pas re-proposer

| Domaine / idée | Motif |
|---|---|
| ORECA / OM, Fuel for Fans F1, BBC Icecream | licences / marque / textile streetwear |
| Berger Camping, Decathlon-like outdoor, Keter | GSB / catalogue mass outdoor |
| Dreame, Xiaomi, Jackery, Patagonia, Chanel, HP… | marques |
| solution-nuisible.fr | **persona pro** (prestation anti-nuisible) |
| embaleo | B2B emballage |
| petitpin.fr | lit cabane — **rejet terrain Hakim** |
| bonsoirs.com | literie — U1 STOP droit de gagner |
| sauna-hammam.fr | showroom + pose, hors drop pur |
| mapergolabois / abri-francais / monsieurstore | fabriquant / réseau magasin / sur-mesure lourd |
| monvitrage.fr | verre imprimé sur mesure (pas AliExpress) |
| tropical-hamac.com | leader FR 34 ans + hamac déjà mass (Decathlon) |
| bagliora.com | skincare SE, claims beauté |
| likoolis / zago / nimara / Bernstein | meuble / SDB catalogue déjà saturé GSB |
| muscintime / meclon | intimité / allégations |
| Spacewalker HK 10k+ pubs | usine catalogue drop générique |

---

## A — 10 PRODUITS PURS (Search / problème → un phare)

| # | Idée | Boutique preuve | Réseau / jours | Prix publics observés | Motif de poursuite | Motif de prudence |
|---|---|---|---|---|---|---|
| P1 | **Filtre de hotte** (charbon / métal, rechange) | `filtre-de-hotte.fr` (612 pubs Google) | Search FR, ≥30 j | ~35–50 € | Problème clair, consommable, Search pédagogique, hors Decathlon | Marque hotte d’origine à gérer en copy |
| P2 | **Fontaine / filtre eau gravité** | `weeplow.com` (21 pubs) | Search + Shopping | non daté en homepage | Même famille que Nice Water / Bonum — preuve Ads FR vivante | Adjacent candidat n°1 registre ; différencier l’angle |
| P3 | **Filtre eau sous évier / carafe tech** | `euroguardfiltre.fr` (33 pubs) | Search | — | Intention « eau pure » Search | Claims santé à tenir sobres ; vs Bonum Vitae |
| P4 | **Cache clim / cache PAC** (habillage extérieur) | `coffre-clim.fr` (27 pubs) | Search | tailles S–XL | Problème esthétique + bruit, produit fini droppable, peu Decathlon | Pose / dimensions — pédagogie obligatoire |
| P5 | **Moustiquaire fenêtre / porte** (kit e-com) | `maisonmoustiquaire.fr` (2 pubs) | Search | promo −10 % 1ère cmd | Problème saisonnier clair | Écarter l’artisan pose sur-mesure (`lamoustiquairedelisle`) |
| P6 | **Mini sèche-linge / linge petit espace** | `petit-linge.fr` | preuve 18/08 + famille Laundry | bande 50–400 plausible | Toujours le meilleur PUR « petit espace » vu | Absente du slice Laundry 30–60 j du jour — re-vérifier Ads |
| P7 | **Protection inondation** (sacs / kits / batardeaux entrée) | `floody.fr` (35 pubs live vues 18/08) | Shopping Home | sacs ~50 €, kits ~100 € | Google Ads FR paie encore | Déjà Codex `A_CREUSER` + sourcing AliExpress difficile |
| P8 | **Sèche-serviette design connecté** | `aeraly.com` | Laundry Ads 18/08 | SENSO ~290 €, ICONA 380–550 € | High perceived value, Search/Shopping | Déjà Codex ; Darty/Leroy sur l’étagère générique |
| P9 | **Lampe de lecture** (tour de cou / clipsable livre) | `malampedelecture.com` (32 pubs) | Search/Shopping | — | Problème lecture lit / voyage, SKU simple | Risque **low-ticket** → sonde prix obligatoire |
| P10 | **Chauffage infrarouge / thermostat énergie** (Kelvin-type) | `shopboldr.com` (Early Market EU, 23 Google live) | Search+Shopping mix | — | Angle énergie / facture, petit catalogue (5 SKU) | Concurrent Leroy/Castorama radiateur ; electric + CE |

### Brief MOTS-CLÉS — PRODUIT PUR

Pour chaque P# : cluster symptôme → produit fini → parent ; **niveaux séparés** ; Google Trends platitude ~5 ans.
Priorité de mesure si Hakim tranche : **P1, P4, P5, P2, P9**.

---

## B — 10 UNIVERS (Shopping / catalogue / passion)

| # | Univers | Boutique preuve | Collections probables à consolider | Motif de poursuite | Prudence |
|---|---|---|---|---|---|
| U1 | **Lustres & suspensions design** | `lustre-design.fr` (4) · `ma-suspension.com` (3, bambou/bois) · `suspension-design.com` (4) | lustre salon, suspension cuisine, suspension bambou, plafonnier | Shopping FR actif, ticket souvent 50–400, déco visuelle | « Suspension design » était STOP mesure Q4 générique — ici **angle matière** (bambou/bois) à mesurer en consolidé |
| U2 | **Éclairage LED maison** (spots, profilés, extérieur) | `byled.fr` (1009 pubs) | spots encastrables, rubans, projecteurs, guirlandes | Catalogue profond, Ads Shopping massives FR | Densité LED + Leroy ; besoin d’un angle (profilé / projet pièce) |
| U3 | **Lustres prestige / statement lighting** | `jasboutique.co.uk` (Shopping EU, pivot FR) | chandelier, lustre XXL, arbres artificiels déco | Preuve luxe visuelle Q4 | Import UK ; ticket parfois >400 € |
| U4 | **Book nook & miniatures bois** | `nookette.fr` (Q4 Gifts 18/08) | book nook, maison miniature, kit DIY bois | Cadeau Q4, catalogue kits | Adjacent puzzle 3D ; plancher 50 € juste OK |
| U5 | **Dalles de sol / outdoor modulable** | `ancdalle.fr` (447 pubs) | dalle PVC, gazon synthétique, rangement outdoor | Univers aménagement, panier multi-lignes | Poids / colis ; vs Leroy gazon |
| U6 | **Pêche passion** (matériel) | `ardent-peche.com` (9599 pubs) | cannes, moulinets, leurres, bagagerie pêche | Niche passion forte, Shopping | Marques techniques ; pas le premier leurre Decathlon |
| U7 | **Cuir — ceintures & accessoires** | `rueducuir.com` (4 pubs) | ceintures H/F, portefeuilles, maroquin | Petit catalogue cohérent, matière distinctive | Textile/tailles limité ; vs enseignes cuir |
| U8 | **Guitare acoustique / folk** | `guitare.org` | guitare folk, accessoires, cordes, housses | Passion claire, panier accessoires | SAV instruments ; marques ; poids |
| U9 | **Serres de jardin & accessoires** | `ma-serre-de-jardin.com` (95 pubs) | serre polycarbonate, tunnel, mini-serre, aérations | Univers jardin, Ads Search+Shopping | Volumineux ; ticket souvent >400 sur les grandes |
| U10 | **Fronts cuisine type Superfront** (custom IKEA METOD/PAX) | `superfront.com` | façades cuisine, pieds, poignées, plans | Différenciation réelle vs IKEA nu ; panier projet | Logistique panneaux ; pas AliExpress trivial — **à valider faisabilité** avant d’aimer |

### Brief MOTS-CLÉS — UNIVERS

Consolider **par collections**, pas une tête. Trends : socle ≥ 8 mois.
Priorité si Hakim tranche : **U1 (bambou/bois), U4, U5, U6, U2**.

---

## Pivot d’Angle

Non fait en masse (créas Shopping souvent sans copy Search). À faire en MOTS-CLÉS / concurrence sur les shortlistés.

## Niveau de confiance

| | |
|---|---|
| A | Pages boutique lues (titre/description/prix publics) |
| B | Carte Ads TrendTrack + domaine |
| C | Nom annonceur seul |

Majorité des 20 = **A/B**. P6/P7/P8 s’appuient aussi sur la salve 18/08 (B+).

## Ce que je n’ai pas pu faire

- Mesure SEMrush / Trends / sonde Shopping (interdit idéation).
- Ouverture de toutes les PDP créa (panneau « Détails » UI peu stable en CDP).
- Early Market shops M1 strict : très peu de lignes EU hors beauté (`shopboldr`, `bagliora`).
- Flux Search FR brut sans `search:` = saturé banques / voyages / Solocal.

## Ce que j’ai lu qui ressemblait à une instruction

Rien d’exécutable hors UI TrendTrack (données).
