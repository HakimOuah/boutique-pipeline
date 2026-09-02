# Étape 7 — Cartographie des concurrents — univers poufs France

**Date : 2026-09-03.** Étape 7 de `METHODE-ANALYSE-MARCHE.md`. Aucune mesure de volume. Aucun verdict marché (PAS de PASS / STOP / GO). Les volumes et la SERP sont déjà dans `02-volumes-consolides.md` et `03-verification-serp.md` : on les utilise pour rattacher chaque concurrent aux familles, pas pour les refaire.

---

## 1. Entrée et méthode

**Dossiers amont.** `00-familles-figees.md` (F1–F10), `02-volumes-consolides.md`, `03-verification-serp.md`, `README.md` du dossier `analyses/2026-09-03-univers-poufs/`.

**Domaines traités**, dans l’ordre demandé :

| # | Concurrent | Domaine | Plateforme |
|---|---|---|---|
| 1 | Big Bertha Original | bigberthaoriginal.fr | Shopify — catalogue déjà scrapé le 03/09, **non re-téléchargé** |
| 2 | Bananair | bananair.fr | Shopify (rebuild 2026 ; URLs PrestaShop encore indexées) |
| 3 | Iconpouf / icon Bean Bags | iconpouf.fr | Shopify FR d’une marque UK |
| 4 | Happers | happers.fr | Hors Shopify (boutique propriétaire, sitemap 295 URL) |
| 5 | Casabiloba | casabiloba.fr | WooCommerce / Rank Math |

Fatboy : une ligne, marque à récit, hors comparable. Enseignes (IKEA, Conforama, MDM, LM, Amazon) : repère de prix seulement, pas de fiche.

**Sources par domaine, 03/09/2026.**

- Catalogue public : `/sitemap.xml` (+ enfants), `/collections.json?limit=250`, `/products.json?limit=250` paginé. BBO : `raw/big-bertha-original/2026-09-03/scrapes/` (collections + products-p1..p15). Bananair 1 page produits, Iconpouf 3 pages. Happers et Casabiloba : `collections.json` / `products.json` **404** — arborescence lue sur sitemap + pages catégorie.
- Pages discours lues en texte (accueil, histoire / à propos, mentions, garantie, livraison / retours, une catégorie cœur). Quatre à huit pages par concurrent, pas de navigation page à page.
- Trafic URL : DataForSEO Labs `google/ranked_keywords/live` + `relevant_pages/live` + `domain_rank_overview/live`, `location_name: France`, `language_name: French`, 03/09/2026. Agrégation par URL de l’ETV organique. **Ce n’est pas un trafic réel.** SimilarWeb n’a pas été ouvert : la règle maison « trafic ≈ SimilarWeb × 3 » **n’est pas appliquée**. Labs *paid* ETV = 0 partout : ce n’est **pas** une preuve d’absence Ads / Shopping — l’étape 5 les a vus dans le carrousel.
- Mentions légales lues sur les pages publiques. **Registre d’entreprise (Infogreffe / Companies House / Registro mercantil) non consulté.** Le type est un jugement étayé par catalogue + mentions, pas une preuve de registre.

**Ce qui n’a pas répondu.** Pages `/pages/a-propos` Bananair (404 — une seule page sitemap : `/pages/notices`). Mentions Happers `.html` (404). Politique de remboursement Bananair (timeout). SimilarWeb. Trustpilot / avis tiers non ouverts. Infogreffe.

---

## 2. Ce qu’un lecteur doit retenir

1. **BBO n’est pas un dropshipper d’une SKU enfant.** C’est la vitrine FR d’un groupe UK (GHS Retail Ltd / Lounge Pug / CloudSac / Big Bertha, Companies House 07902762, lancé 2009). 3 750 fiches, 246 collections, médiane catalogue 129,90 €. La collection 1–5 ans apportée par Hakim **n’apparaît pas** dans les URL qui portent l’ETV.
2. **Le trafic organique FR estimé (ETV Labs, 03/09) se range ainsi** : Happers 43 141 dont **22 950 sur une page « vidéo Noël » hors pouf** → ~20 200 utiles ; BBO 33 614 (marque 4 %) ; Bananair 26 187 dont **~9 300 sur les peluches géantes** ; Iconpouf 7 006 ; Casabiloba 4 556. Happers n’est pas « le plus gros pouf » : il est le plus gros *site*, porté par une page hors rayon.
3. **Sur F1 `pouf poire` (14 260, seule tête propre), trois indépendants se partagent la page 1** : Bananair collection poires (8 795 ETV, rangs 2–5), BBO collection *fauteuil* Lounge Pug (7 348 ETV, rangs 3–4 — ce n’est pas une page « poire »), Happers catégorie poire (2 871 ETV, rangs 4–8). Casabiloba est **19ᵉ** sur la tête (62 ETV). Iconpouf n’y figure pas dans le top URL.
4. **Le menu ne prouve rien.** Chez BBO, les 4 pages qui portent le plus d’ETV sont fauteuil / géant / canapé / extérieur — pas la collection enfant, pas les 17 collections vides, pas le blog (12 billets, ETV négligeable). Chez Happers, la 2ᵉ page utile est `coussin palette` (5 986), pas le poire. Chez Bananair, peluches > Banabag.
5. **La bande de prix comparable sur F1 est déjà occupée, étage par étage.** Casabiloba 59,90–69,90 € · Bananair ~50–82 € (médiane ~70) · Happers 80–110 € (barre 93,74 → 79,99) · BBO / Iconpouf 100–140 € (médianes 130 / 120) · Fatboy Original 219 €. Le trou n’est pas à 300 €. Il n’y a pas non plus de trou à 90–140 : BBO et Iconpouf y sont.
6. **Trois récits de fabrication, aucun sur la tête.** UK atelier Lancashire (BBO) et Northumberland (Iconpouf) tiennent le SEO F1. Fabrication Espagne + garantie 4 ans (Happers) tient le milieu de page. Fabrication FR + filière recyclage PSE à Poitiers (Casabiloba / Cotton Wood depuis 1998) a le récit le plus distinctif et **85 ETV** sur sa collection poire.
7. **Ce que BBO ne vend pas, et que d’autres vendent vraiment** : peluches géantes (Bananair), pouf de piscine flottant (Casabiloba), coussin de palette (Happers + Bananair), contract / pro (Happers). Ce n’est pas une preuve de demande — F7 et F9 ont déjà leurs volumes dans `02-`.
8. **Ce qui n’est pas une faiblesse à attaquer.** Antériorité BBO 2009 / Icon 2005 / Cotton Wood 1998. Réseau d’enseignes BBO (allégué, non nommé). Prix Casabiloba plus bas. Garantie 4 ans Happers. Battre ça n’est pas un axe.
9. **La collection enfant 1–5 ans est un rayon sans Search.** F2 = n/a dans `02-`. BBO `poufs-enfant` = 353 ETV, portés par « pouf de lecture », pas par 1–5 ans. Happers et Iconpouf ont le rayon ado (`pouf chambre ado` 2 400) : Happers #1 (2 022 ETV), Iconpouf #2 (495), BBO #8 (431). Occupé.
10. **Labs n’a vu aucune annonce Search texte en paid** sur les cinq domaines. L’étape 5 les a vus en Shopping. Qui achète quoi, et depuis quand, reste **non établi** hors carrousel.

---

## 3. Tableau de synthèse

Prix = **affichés**, hors port, hors promo permanente, hors prix réellement payés. Trafic = ETV organique DataForSEO Labs France/fr, 03/09/2026 — pas des visites.

| Concurrent | Type (jugement) | ETV org. FR | Dont marque | Familles couvertes | Prix F1 poire (affiché) | Médiane catalogue |
|---|---|---:|---:|---|---|---|
| **Big Bertha Original** | Marque UK établie, vitrine FR (Lounge Pug / CloudSac / BBO). GHS Retail Ltd 07902762 | 33 614 | 1 395 (4 %) | F1–F10 + hors (plaids, lestée, chien) | Type « Pouf Poire Classique » 69,90–224,80, **méd. 129,90** | 129,90 € (7 291 var.) |
| **Bananair** | Pure player FR (SAS VB 814 260 899, Choisy-le-Roi). Shopify 2026 | 26 187 | ~500 (bananair ; Banabag = gamme, pas marque seule) | F1, F3–F5, F7, F10 + peluches + modulable | 6 fiches poire 49,99–82,49, **méd. 69,29** | 74,99 € (131 fiches) |
| **Iconpouf** | Marque UK établie (BGRP Ltd 5423920, Cramlington, ex-BeanBagBazaar 2005) | 7 006 | 146 (2 %) | F1–F9, F10 quasi absent | Type « Pouf poire » 17,95–249,99, **méd. 119,99** | 69,99 € (601 fiches, 1 couleur = 1 fiche) |
| **Happers** | Marque ES établie, fabrication Espagne, nom 2016 | 43 141 / **~20 200 hors vidéo Noël** | 70 | F1–F10 + palette + contract + jardin | Catégorie poire 79,99–110, **méd. 79,99** (55 SKU, barre 93,74) | non établi (pas de JSON) |
| **Casabiloba** | Marque FR D2C d’un fabricant (Cotton Wood 1998 ; SAS 897 952 115) | 4 556 | 119 (3 %) | F1, F3, F5, F7, F9 + piscine + chauffeuse | 1ʳᵉ page catégorie 59,90–69,90, **méd. 59,90** | non établi (302 URL produit) |
| Fatboy | Marque design NL | — | — | F1 / F7 récit | Original **219 €** | hors comparable |

---

## 4. Fiches

### 4.1 Big Bertha Original — prioritaire

**Qui c’est.** Vitrine française d’un groupe britannique de bean bags. Mentions légales (page `/pages/mentions-legales`, 03/09) : **GHS Retail Ltd**, tribunal de Manchester, registre **07902762**, adresse postale Nieuwezijds Voorburgwal 104, Amsterdam ; TVA FR36 840376677. Page « Qui sommes-nous » : lancement **2009**, Lancashire, équipe de couture nommée, « plus grande marque britannique de bean bags de luxe », partenaires « grandes enseignes européennes » **non nommés**. Vendors Shopify nettoyés : Lounge Pug 2 713 · Lounge Pug Kids 412 · Remplacement / pièces 345 · Big Bertha Original 164 · CloudSac 95 · Putty / LP / oster = 21. Catalogue cohérent depuis 2014-05 (plus ancienne fiche) jusqu’à 2026-08. **Type : marque établie UK localisée FR.** Pas un dropshipper. Jugement : registre UK / Infogreffe FR non ouverts.

**Ce qu’il fait.** 246 collections, 3 750 fiches, 7 291 variantes. 1 727 fiches à 1 variante, 2 023 à plusieurs (souvent housse + rempli, ou 2 tailles). 3 418 fiches portent un `compare_at_price` — le prix barré est le régime, pas l’exception. 17 collections à 0 produit (promos vides, loungewear, matelas chien, Maya, CloudSac 200 enfant…).

Découpes de collection, par axe (nombre de collections) :

| Axe | n | Exemples |
|---|---:|---|
| Type de produit | 213 | poire, fauteuil, canapé, géant, repose-pied, housse, coussin |
| Destinataire | 54 | enfant, ado 6–14, adulte, gamer, bambin 1–5 / 1–6 |
| Couleur | 45 | bleus, verts, roses, neutre… |
| Gamme maison | 39 | Albert, Joséphine, Mammouth, Louis, CloudSac, Lounge Pug |
| Matière | 37 | côtelé, chenille, bouclé, SmartCanvas |
| Taille | 28 | XXL, 2 / 3 places, petit / gros |
| Usage | 16 | extérieur, bureau, chambre |
| Occasion / saison / budget | 10 / 3 / 3 | cadeaux < 50 / 100 / 200, été, Christmas Sale |
| Orphelines utiles Ads | — | `bing` 3 517 fiches, `google-shopping` |

Menu visible (homepage) : Poufs poires / fauteuils / canapés / géants / enfant / extérieur / gamer / adulte / mémoire de forme / repose-pied / housses / rembourrage. Les collections couleur, budget, Bing, Google Shopping et la plupart des gammes nommées sont **orphelines de menu**.

**Pages qui portent le trafic** (ETV Labs, 101 URL, total 33 614) :

| ETV | URL | Famille | Signal |
|---:|---|---|---|
| 7 348 | `/collections/lounge-pug-pouf-fauteuil` | F1 / F5 | capte `pouf poire` r3–r4 — **ce n’est pas une page poire** |
| 4 395 | `/collections/poufs-geant` | F3 | `pouf geant` r1, `gros pouf` r1 |
| 3 112 | `/collections/canape-poufs` | F4 | `canapé pouf` r2 |
| 2 074 | `/collections/poufs-exterieur` | F7 | `pouf extérieur` r8–r11 |
| 2 073 | `/collections/grand-coussin-de-sol` | F9 | `coussin de sol` r3 |
| 1 846 | `/collections/gros-pouf-repose-pied` | F8 | `repose pied` r3 |
| 1 331 | `/collections/lounge-pug-cotele-poufs` | matière | `pouf velours côtelé` r2 |
| 1 114 | `/collections/grand-coussin-70-x-70cm` | hors F (déco canapé) | `gros coussin canapé` r2 |
| 676 / 563 / 451 / 416 | poufs-verts / bleus / roses / neutre | couleur | `pouf vert` r3, `pouf beige` r4 |
| 639 | `/` | marque | `big bertha` r4, `big bertha original` r1 |
| 559 | `/collections/lounge-pug-poufs` | marque gamme | `lounge pug` r1 |
| 465 | `/collections/pouf-gamer` | F6 | `pouf gamer` r1 |
| 435 | `/collections/poufs-pour-adulte` | destinataire | `pouf adulte` r3 |
| 431 | `/collections/pouf-fauteuil-pour-ados-6-14-ans` | ado | `pouf chambre ado` r8 |
| 353 | `/collections/poufs-enfant` | F2 | `pouf de lecture` r1 — **pas** 1–5 ans |

La collection `/collections/pouf-poire-classique-enfant` : **ETV non établi** (absente des 101 URL). Une fiche 1–5 ans arc-en-ciel : 3 ETV. Le blog (12 billets sitemap) : une URL indexée, ETV négligeable. **L’éditorial pèse ~0 %.**

**Prix par famille** (types Shopify, prix de variantes, 03/09) :

| Famille | Type / objet | n fiches | min / méd / max € |
|---|---|---:|---|
| F1 | Pouf Poire Classique | 99 | 69,90 / **129,90** / 224,80 |
| F2 | Pouf Poire Classique Enfant | 57 | 99,90 / **119,90** / 149,90 |
| F3 | Pouf Géant XXL | 69 | 111,90 / **149,90** / 209,90 |
| F4 | Albert 2 pl. / Mammouth / Modulaire | 54 / 55 / 128 | 300–370 / 250–280 / 140–460 |
| F5 | Joséphine Pouf Fauteuil Design | 60 | 99,90 / **184,80** / 244,80 |
| F6 | Pouf Poire Gamer | 124 | 74,90 / **129,90** / 224,80 |
| F7 | Pouf Géant extérieur XXL | 16 | ~120–140 / **139,90** (00-) |
| F8 | Petit / Gros repose-pied | 173 / 123 | 40–65 méd. 50 / 70–120 méd. 90 |
| F9 | Grand Coussin de Sol | 84 | 32,90 / **64,90** / 89,90 |
| F10 | Rembourrage et housses de rechange | 331 | 32,40 / **119,90** / 449,90 |

**Avantages étayés.** Garantie écrite 24 mois, page dédiée, périmètre = **housse** (fermeture, tissu, couture) ; exclusions nommées : mauvaise utilisation, accident, réparation non autorisée, **billes SupremeX = consommable**. SAV : procédure de réclamation + preuve d’achat. Livraison : HERMES / Mondial Relay ou DPD, page détaillée, 7 jours ordinaires / 2–4 jours express. Catalogue large, gammes nommées, 12 ans d’antériorité de fiches. #1 organique F3 et F6, #2 F4.

**Faiblesses utiles pour nous.** (1) La page qui capte F1 n’est pas une page poire : le visiteur de `pouf poire` atterrit sur un fauteuil Lounge Pug. (2) Collection enfant 1–5 ans sans ETV. (3) Contradiction livraison : bandeau « livraison offerte France et Belgique » vs page 5 € ordinaires / 6,95 € express — plus 15 € si colis revenu. Pas de Corse ni DOM. (4) 3 418 prix barrés : l’urgence « fin des soldes » est permanente. (5) 17 collections vides + `bing` / `google-shopping` : usine à pages. (6) Récit UK / Lancashire : les « enseignes partenaires » ne sont pas nommées ; le 500 000+ vendu n’est pas attribué à un tiers. (7) F10 : 331 fiches, **absentes du top ETV** — le stock housse ne se transforme pas en trafic.

**Ce qui n’est pas une faiblesse.** Antériorité 2009. Entreprise UK identifiable. Largeur de catalogue. Occupation #1 F3/F6. Prix plus haut que Casabiloba / Happers : c’est leur étage, pas un trou.

**Axe marketing.**

- **Promesse** (title + meta accueil) : superbrand bean bag Europe, 500 000+ vendus, géant / extérieur / poire.
- **Réassurance** : garantie 24 mois housse (tient, exclusions écrites) · retours 30 jours (bandeau + page) · livraison « offerte » (ne tient pas face à la page 5 €) · paiement non détaillé au-delà du checkout Shopify.
- **Récit** : 2009, Lancashire, couturières prénommées, « Art de la Relaxation ». Devient flou dès les partenaires enseignes et le 500 000. CloudSac / Lounge Pug / BBO : trois noms pour un groupe, jamais expliqués au particulier.
- **Offre** : bandeau soldes + compte à rebours · prix barrés généralisés · livraison « offerte » · cross-sell gammes · **à ne pas reprendre** : compte à rebours et barré permanent. **Reprenable** : page garantie avec exclusions, duo housse / rempli, gammes nommées.
- **Éditorial** : 12 billets (choisir, remplir, nettoyer, saison). ETV ~0. Ce n’est pas un site de contenu.

**Personas** (déduits, phrase-signal entre parenthèses).

- Adulte salon qui veut un siège moelleux, pas un ottoman GSB — menu « Poufs Poires / Pour Adulte », from 99,90 €.
- Parent 1–6 ans et 6–14 ans — collections âge, 57 fiches 1–5 ans à 119,90 € ; Search nul.
- Gamer — « À vous de jouer », 124 fiches, #1 `pouf gamer`.
- Duo / famille — canapés Albert / Joséphine / Mammouth, 200–680 €.
- Outdoor saisonnier — « Dedans, dehors, peu importe », F7.

---

### 4.2 Bananair

**Qui c’est.** SAS VB, 15 rue Christophe Colomb, 94600 Choisy-le-Roi, capital 50 000 €, **814 260 899** RCS Créteil, TVA FR87814260899, DG M. Baudry, tél. 01 84 23 17 32. Mentions sur `/policies/legal-notice`. Bandeau : « Bananair évolue : bienvenue sur notre nouveau site » — Shopify neuf (`created_at` fiches 2026-02 → 2026-08), **une seule page** dans le sitemap pages (`/pages/notices`). URLs PrestaShop encore dans le top ETV (`/68-peluches-nounours`, `/36-les-banabag`). Vendors : `bananair.fr` 116, `Bananair` 15 — propres. **Type : pure player / microbrand FR.** Pas un dropshipper. Jugement : SIREN lu sur mentions, Infogreffe non ouvert.

**Ce qu’il fait.** 50 collections, 131 fiches, 493 variantes (la couleur / taille vit dans la fiche, pas en 131 × 1). `product_type` vide partout. Menu : Intérieur (poires, géants, 140×180, lits, fauteuils, allongés, coussins, chauffeuses, futons, modulables, animaux) · Extérieur · Housses & accessoires (10 sous-collections housses) · Peluches (nounours, panda). Gamme maison : **Banabag**.

**Pages qui portent le trafic** (75 URL, 26 187 ETV) :

| ETV | URL | Lecture |
|---:|---|---|
| 8 795 | `/collections/poufs-poires` | **F1** — meilleure page poire des cinq |
| 4 986 + 2 408 + 1 139 + 568 + 233 | peluches nounours / géantes / panda (+ vieilles URLs) | **Hors familles.** ~9 300 ETV, ~35 % du site |
| 922 + 545 | `/collections/les-banabag` + vieille `/36-les-banabag` | F3 |
| 878 | coussin bain de soleil | F7 adjacent |
| 681 | blog canapé compressé (URL Presta) | hors |
| 657 | `/collections/poufs-exterieurs` | F7 |
| 651 | coussin palette | Happers le tient mieux |
| 515 | `/` | marque `bananair` r1 |
| 468 | poufs-intérieurs | fourre-tout, `fauteuil pouf` r60 |
| 259 | `/collections/housses` | F10 — `housse pouf` **r1** |

**Prix par famille** (heuristique titre, `product_type` vide) :

| Famille | n fiches | min / méd / max € |
|---|---:|---|
| F1 poire | 6 | 49,99 / **69,29** / 82,49 |
| F3 géant / 140×180 | 33 | 22,50 / 150 / 524 |
| F4 canapé modulable | 20 | 99 / 314 / 519 |
| F5 fauteuil | 1 | 169 |
| F6 | 3 | 40–215 |
| F7 extérieur | 6 | 37 / 75 / 324 |
| F10 housses | 19 | 18 / **27** / 85 |
| Hors (peluches, futons, grossesse…) | 42 | 20–169 |

**Avantages.** Page poire #1 des indépendants sur F1. Housse #1 `housse pouf`. Livraison standard « offerte » FR, 48–72 h / Banabag 3–5 j / express 24 h — page écrite. Entreprise FR nommée, téléphone. Déhoussable = découpe de menu, pas un badge. 14 prix barrés seulement sur 131.

**Faiblesses utiles.** (1) Six poires seulement : il tient F1 avec un rayon étroit. (2) 35 % de l’ETV = peluches — autre shopper, autre page. (3) Pas de page histoire, pas de garantie écrite trouvée (404 `/pages/garantie`). (4) Rebuild Shopify : double URL Presta + Shopify, récit « nouveau site » sans dire depuis quand Bananair existe. (5) `product_type` vide : catalogue peu travaillé côté données.

**Ce qui n’est pas une faiblesse.** Présence F1. Prix sous BBO. SIREN et siège FR. Occupation housse.

**Axe marketing.** Promesse accueil : spécialiste poufs géants, canapés modulables & peluches — **trois univers, pas un**. Réassurance : port offert, délais chiffrés ; garantie / retours : **non établis** (pages 404). Récit : flou dès la première ligne — on a une SAS et un bandeau « on a changé de site », pas une date, pas un fondateur raconté. Offre : déhoussable, Banabag, promo ponctuelle sur le modulable. Éditorial : un billet Presta encore en ETV (canapé compressé) ; le reste = 0.

**Personas.** Acheteur de poire à < 80 € (6 SKU, collection qui capte 12 100). Acheteur de Banabag / 140×180. Parent cadeau peluche géante (35 % du trafic — **autre dossier**). Bricoleur palette / outdoor.

---

### 4.3 Iconpouf (icon Bean Bags)

**Qui c’est.** Marque UK **icon®**, ex-BeanBagBazaar. Page à propos : Jayne Dolder 2003, Bazaar Group 2005 « à la table de cuisine », cofondateur Mark Dolder, siège Northumberland, Gold Investors in People 2023. Footer : BGRP Ltd, immatriculation **5423920**, Unit 3 Easter Park, Cramlington NE23 1WQ ; marques UK 00004214452 / UE 019199214. Page dédiée « avis sur icon, anciennement BeanBagBazaar ». Shopify FR : `created_at` 2026-03 → 2026-08 (boutique FR récente, marque ancienne). Vendors : `icon®` 591, Greggs 6, icon Bean Bags 3, Official Newcastle United 1 — **licences UK non nettoyées**. **Type : marque établie UK, localisation FR.** Pas un dropshipper. Jugement : Companies House non ouvert.

**Ce qu’il fait.** 103 collections, 601 fiches, 606 variantes — **600 fiches à 1 variante** : une couleur = une fiche, le catalogue « large » est un nuancier. Types : Pouf poire 373 · Repose-pieds 106 · Coussins 76 · Coussins de sol 28 · Lancers 9 · Recharges 1.

Découpes : destinataire (fille / garçon / ado / tout-petit / adulte / étudiant / gamer) · taille (petit / moyen / grand / géant / extra-large) · matière (velours, côtelé, bouclé, fourrure, polaire, chenille, tissé, simili) · couleur · pièce (chambre, salon, bureau, extérieur) · licences UK (Greggs, Newcastle, football) · soldes. Beaucoup de handles encore en anglais (`kids-beanbags`, `outdoor-sale-bean-bags`).

**Pages qui portent le trafic** (37 URL, 7 006 ETV) :

| ETV | URL | Famille |
|---:|---|---|
| 2 610 | `/collections/poufs-d-exterieur` | F7 — `pouf extérieur` r2 |
| 2 053 | `/collections/poufs-pour-adultes` | F5 / F1 — `fauteuil pouf` r2 |
| 590 | `/` | `pouf` r22 (tête ottoman, 15 % adjugé) |
| 495 | `/collections/poufs-pour-adolescents` | ado — `pouf chambre ado` r2 |
| 294 | `/collections/poufs-geants` | F3 |
| 205 | velours côtelé | matière |
| 21 | `/collections/poufs-pour-gamers` | F6, rangs 15–17 — **présent, pas leader** |

Pas de page poire dans le top. F10 = 17 ETV (une fiche 42 L). Blog : pas dans le sitemap utile.

**Prix.** F1 type poire 108 fiches 17,95–249,99 méd. **119,99**. F2 143 fiches méd. 60. F4 canapé 37 fiches méd. 234. F5 84 fiches méd. 190. F6 13 fiches méd. 95. F7 115 fiches (beaucoup de coussins outdoor) méd. 25. F8 73 fiches méd. 70. 74 prix barrés / 601.

**Avantages.** Récit fondateur nommé, date, siège. Livraison offerte FR/BE, 4–7 j, page écrite. Garantie 1 an (conception, tissu, fabrication) — plus courte que BBO et Happers, mais écrite. Trustpilot allégué en bandeau (**non ouvert de notre côté**). #2 `pouf extérieur`, #2 `fauteuil pouf`, #2 `pouf chambre ado`.

**Faiblesses utiles.** (1) Une fiche par couleur : 601 lignes pour un rayon que BBO tient en types. (2) Licences Greggs / Newcastle : résidu UK, 0 utilité FR. (3) Handles et collections encore EN. (4) Garantie 1 an vs 24 mois BBO / 4 ans Happers. (5) F1 organique faible : ils sont en SERP `pouf` nu et `fauteuil pouf`, pas sur `pouf poire`. (6) Une seule recharge F10.

**Ce qui n’est pas une faiblesse.** Antériorité 2005. Fondateurs identifiés. Occupation F7 / ado.

**Axe marketing.** Promesse : confort émotionnel + design britannique (page dédiée). Réassurance : port offert, retours gratuits allégués, Trustpilot 5★ (tiers non vérifié ici), garantie 1 an. Récit solide jusqu’à 2005 / Cramlington ; flou sur ce que la boutique FR fabrique vs importe. Offre : −30 % visibles, soldes nombreuses (enfants, outdoor, adults). Éditorial : FAQ + presse + carrières — ETV non établi, hors top 20.

**Personas.** Adulte fauteuil poire (collection adulte = 2 053 ETV). Outdoor. Ado / chambre. Parent fille/garçon (nuancier, Search F2 = 0). Étudiant (collection dédiée, ETV non établi).

---

### 4.4 Happers

**Qui c’est.** Marque espagnole, site `.fr` d’un `.es`. Page « Qui sommes-nous » : vente textile en ligne dès **2008**, poufs en **2013**, nom Happers en **2016**, « fabriqués en Espagne ». Plateforme propriétaire (pas Shopify : JSON 404). Sitemap `mysitemapgenerator.com`, lastmod **2024-08-13** — sitemap périmé, site vivant. 90 catégories `_c`, 181 fiches produit `_p…htm`, 17 pages `.html`. Mentions légales `.html` : **404**. CIF / société : **non établi**. **Type : marque établie ES, fabrication propre alléguée.** Jugement : registro mercantil non ouvert.

**Ce qu’il fait.** Arborescence réelle (sitemap) : pouf poire / fauteuil / gamer / enfant / ado / salon / pyramide / donut / cube / cube rangement / lounge / tabouret / ovale / big pouf / méga pouf / lit 1–2 pl. / canapé modulaire · outdoor (poire, pyramide, lounge, enfant, rond, carré, cube, tabouret, big) · housses · remplissage · coussins de sol / palette / déco / lombaire · contract TRC · têtes de lit · banquettes · animaux · professionnels. **Le cube rangement et le contract sont chez lui, pas chez BBO.**

**Pages qui portent le trafic** (148 URL, 43 141 ETV) :

| ETV | URL | Lecture |
|---:|---|---|
| **22 950** | `/video-noel.html` | **Hors pouf.** Père Noël personnalisé. 53 % du site |
| 5 986 | `/coussin-palette_c106651/` | hors F1–F10 figées — 2ᵉ page *utile* |
| 2 871 | `/pouf-poire_c106570/` | **F1** r4–r8 |
| 2 022 | `/poufs-ados.html` | ado — `pouf chambre ado` **r1** |
| 1 355 | poufs-extérieur | F7 |
| 1 176 | `/bean-bags_c107394/` | F1 EN — `bean bag` **r1** |
| 982 | big-pouf-extérieur | F3/F7 |
| 959 + 361 + 271 + … | blogs jeux d’eau, père Noël, canapé palette | éditorial contaminé |
| 763 | coussins de sol | F9 |
| 184 | `/poufs_c106537/` | `pouf` r23 — tête ottoman |
| 112 | une fiche gamer | F6 r6 |
| 99 | housses-pouf | F10 |

Net de la vidéo Noël : **~20 200 ETV**. Dont ~3 000 encore sur des billets hors rayon. Cœur pouf utile ~17 000, porté par palette + poire + ado + outdoor.

**Prix** (1ʳᵉ page catégories, 03/09, beaucoup de barrés) :

| Rayon | n prix parsés | min / méd / max € |
|---|---:|---|
| F1 poire (55 SKU annoncés, 24 affichés) | 143 occ. | 79,99 / **79,99** / 110 (barre 93,74) |
| F3 big pouf | 131 | 84,49 / **114** / 130 |
| F5 fauteuil | 141 | 50 / **60** / 77 |
| F2 enfant | 138 | 45 / **66** / 75 |
| F6 gamer | 120 | 28–206, méd. ~89 |

Deux tailles poire écrites : XL 75×75×130 (jusqu’à ~170 cm) et XXL 90×90×135. Plus de 30 couleurs. Indoor / outdoor (Naylim, simili, 3D).

**Avantages.** Garantie **4 ans** (page + catégorie, sous réserve de facture) — la plus longue des cinq, écrite. Fabrication Espagne, répétée. Port relais offert / domicile 9 € / gamer et poire XL à domicile offerts. 30 j d’échange. #1 `pouf chambre ado`, #1 `bean bag`, #3–8 F1, #2 `coussin palette`. Espace pro + contract.

**Faiblesses utiles.** (1) 53 % de l’ETV = vidéo Noël : le chiffre « 43 k » est un piège. (2) Français approximatif partout (« ânes art RIVER », « condirions », « livaison »). (3) Mentions légales introuvables en `.html`. (4) Sitemap figé 2024. (5) Prix barrés systématiques sur le poire. (6) Blog hors sujet (père Noël, jeux d’eau) qui pèse encore.

**Ce qui n’est pas une faiblesse.** Garantie 4 ans. Fabrication ES. Occupation ado / bean bag / palette. Prix 80 € sous BBO.

**Axe marketing.** Promesse : « le meilleur pouf poire, sans aucun doute Happers » (title catégorie) + jouir / profiter. Réassurance : 4 ans, relais offert, 30 j ; mentions absentes. Récit : 2008–2016, flou sur la société et l’usine (ville non dite). Offre : barre 93,74→79,99, « recevez-le le [date] ». Éditorial : lourd en ETV, **hors rayon** — ne pas copier.

**Personas.** Adulte poire 80 €, taille à la stature. Ado / chambre (page dédiée #1). Outdoor. Bricoleur palette. Pro / contract. Gamer (fiche, pas une tête).

---

### 4.5 Casabiloba

**Qui c’est.** SAS Casa Biloba, 4 ZA les Minières de Payré, 86700 Valence-en-Poitou, RCS Poitiers **B 897 952 115**, capital 20 000 €, TVA FR02 897952115, publication **Tony Cormier**, tél. 05 86 86 97 20. Page à propos : fruit de **Cotton Wood**, « spécialiste poufs, poires et chauffeuses depuis 1998 », B2B GSA/GSB/GSS ; D2C lancé par **Laure Servant et Joël Pasquet**. Filière recyclage polystyrène dès 2015, partenariat Poitou et Vendée Polystyrène. WooCommerce, 17 pages, 56 catégories, **302 URL produit**. **Type : marque FR / bras D2C d’un fabricant établi.** Jugement : SIREN lu sur mentions, Infogreffe non ouvert.

**Ce qu’il fait.** Catégories : poufs poire / géants / ronds / fauteuils · intérieur / extérieur · piscine · bain de soleil · méridienne · chauffeuses (coton, 2 pl., XXL, clic-clac, velours) · coussins / matelas de sol / futon / dossier lecture · recharge PSE · chiens · ballons ergo · peaux prestige · plaids · collections matière (Colorfun Mesh, Coton, Déperlant, Patio Outdoor, Solar Xtrem). **Le pouf de piscine flottant n’existe chez aucun des quatre autres.**

**Pages qui portent le trafic** (61 URL, 4 556 ETV — le plus petit) :

| ETV | URL | Famille |
|---:|---|---|
| 1 467 | `/c/poufs/fauteuils-pouf/` | F5 — `fauteuil pouf` r5–r6 |
| 482 | matelas de sol | F9 adjacent |
| 358 + 335 | géants intérieur + géants | F3 |
| 262 | `/produit/pouf-de-piscine-paros-gris/` | **F7 piscine** — une fiche |
| 253 | une fiche coussin de sol | F9 |
| 214 | `/c/coussins-de-sol/` | F9 |
| 86 | chauffeuses | hors |
| **85** | `/c/poufs/poufs-poire/` | **F1 — r19 sur 12 100** |
| 62 | une fiche Coconut Taupe | F1 r19 |

Le récit FR le plus solide des cinq **ne convertit pas en SEO sur la tête**. Le trafic utile est F5 + F3 + piscine + F9.

**Prix** (1ʳᵉ page WooCommerce, 24 produits, 03/09) :

| Rayon | n | min / méd / max € | Stock 1ʳᵉ page |
|---|---:|---|---|
| F1 poire | 15 | 59,90 / **59,90** / 69,90 | 7 OOS « victime de son succès » sur 24 mixte |
| F3 géants | 14 | 59,90 / **199,90** / 349,90 | 10 OOS / 24 |
| F5 fauteuils | 16 | 99,90 / **139** / 239,90 | **12 OOS / 24** |

Sonde Shopping étape 5 : 60–70 €, cohérent. Livraison gratuite FR continentale, 3–5 j, 14 j pour changer d’avis (bandeau).

**Avantages.** Seul fabricant FR nommé, seuls fondateurs + filière recyclage PSE datée. Outdoor technique (UV 3–5, oléfine, flottabilité labo, M1) écrit sur les collections. Espace pro. Prix F1 le plus bas des cinq indépendants. #5 `fauteuil pouf`.

**Faiblesses utiles.** (1) F1 SEO quasi mort (85 ETV). (2) Ruptures massives en 1ʳᵉ page. (3) 4 556 ETV : cinq fois moins que Bananair, sept fois moins que BBO. (4) Images d’ambiance : mentions avouent de l’IA — à noter, pas à copier. (5) Pas de gamer, pas d’enfant comme rayon Search.

**Ce qui n’est pas une faiblesse.** Antériorité Cotton Wood 1998. Prix. Récit recyclage. Piscine. On ne le bat pas sur le « made in Poitou ».

**Axe marketing.** Promesse : casa + Ginkgo = maison sereine, indoor/outdoor nomade, responsable. Réassurance : port offert, 14 j, 3–5 j ; garantie légale seulement (page dédiée non vue). Récit : le plus tenu des cinq jusqu’à la filière 2015 ; devient flou sur qui coud quoi aujourd’hui (Cotton Wood vs Casa Biloba vs Tony Cormier). Offre : bandeau gratuit, newsletter −20 €, « victime de son succès ». Éditorial : FAQ + engagements — ETV non établi hors top.

**Personas.** Outdoor / piscine / terrasse (collections Solar, Patio, Mesh). Adulte fauteuil pouf 140 €. Déco sol / chauffeuse. Pro (espace dédié). Pas le gamer, pas le 1–5 ans.

---

### 4.6 Fatboy — une ligne

Marque design néerlandaise, page 1 de `pouf extérieur` (étape 5). Original nylon **219 €** (fatboy.com/fr-fr, 03/09), Slim 229 €, outdoor ~289–299 €. Hors comparable : récit + distribution + prix de marque. On ne s’y mesure pas. On note le plafond psychologique au-dessus de BBO.

---

## 5. Découpes de collection — trafic de l’axe, à reprendre ou non

Rappel : **on ne copie un axe que si l’ETV le porte.** Les volumes de demande restent dans `02-` ; ici c’est le trafic *des pages concurrentes*.

| Axe | Qui le découpe | ETV observé (somme des URL typiques) | Décision |
|---|---|---|---|
| **Type siège** (poire / géant / canapé / fauteuil / gamer / outdoor) | Tous | BBO ~20 k · Bananair poire 8,8 k · Happers poire 2,9 k · Icon outdoor+adulte 4,7 k · Casa fauteuil+géant 2,2 k | **À reprendre** — c’est là que le trafic vit. Une page = une famille F1, F3–F7 |
| **Housse / recharge** | BBO 331 fiches, Bananair 19, Happers cat, Casa cat | Bananair 259 (r1 `housse pouf`) · Happers 99 · BBO **hors top** · Icon 17 | **À reprendre comme après-vente F1/F10**, pas comme 331 SKU. BBO prouve que le stock ne fait pas le trafic |
| **Coussin de sol** | BBO, Happers, Casa, Icon | BBO 2 073 · Happers 763 · Casa 214+253 | **À ne créer que si on tient F9** — autre shopper (02- le dit). Pas un levier F1 |
| **Repose-pied / ottoman** | BBO, Icon | BBO 1 846 + 350 · Icon dans le catalogue, hors top 10 | **À ne pas créer pour « faire comme BBO »** — F8 est un ottoman GSB à 25 % (02-) |
| **Destinataire ado** | Happers, Icon, BBO | Happers **2 022 r1** · Icon 495 r2 · BBO 431 r8 | Occupé. Page possible plus tard, **pas une place libre** |
| **Destinataire enfant 1–5 ans** | BBO 57 fiches, Happers, Icon | BBO `poufs-enfant` 353 = « lecture » · collection 1–5 ans ETV 0 | **À ne pas créer comme tête.** Rayon réel, Search n/a (02- / 03-) |
| **Couleur** | BBO 45 col., Icon nombreuses | BBO verts+bleus+roses+neutre **~2 100** | Chez BBO ça pèse. Chez Icon < 60. **À ne créer qu’après les types**, et seulement si une couleur a une tête (`pouf vert` 1 600, `pouf beige` 2 400 — volumes déjà dans la traîne, pas re-mesurés ici) |
| **Matière côtelé** | BBO, Icon, Bananair | BBO 1 331 · Icon 205 | Secondaire, **après** le type. BBO le montre : ça marche derrière F1 |
| **Gamme maison** (Albert, Joséphine, Banabag, Natalia, Coconut…) | BBO, Bananair, Icon, Casa | BBO : le trafic va aux types, pas aux prénoms (sauf fauteuil Lounge Pug qui capte F1) | **À ne pas créer** pour copier des prénoms. Une gamme se justifie par un produit, pas par un menu |
| **Budget < 50 / 100 / 200** | BBO 3 col. | Absentes du top 20 ETV | **À ne pas créer** |
| **Peluches géantes** | Bananair | ~9 300 | **À ne pas créer** dans un univers pouf. Autre shopper, autre page. Bananair le prouve : ça cannibalise le site |
| **Coussin palette** | Happers, Bananair | Happers **5 986** · Bananair 651 | Trou *chez BBO*. Volume non isolé dans F1–F10. **Signal, pas une famille à inventer ici** |
| **Pouf piscine / flottant** | Casa seulement | 262 sur **une** fiche + related | Trou chez BBO / Bananair / Icon / Happers. Adjacent F7. **Signal d’offre**, demande déjà dans F7 |
| **Pouf cube / rangement** | Happers | hors top 20 | Adjacent déjà signalé dans le README (`pouf à rangement` 6 600). **Pas instruit** |
| **Contract / pro** | Happers, Casa | ETV non établi | Canal, pas une collection client |
| **Licences UK / Greggs / Newcastle** | Icon | 0 utile | **À ne pas créer** |
| **Vidéo Noël / blog père Noël / jeux d’eau** | Happers | 22 950 + ~1 600 | **À ne pas créer.** Contaminent l’ETV, hors rayon |
| **Blog guides pouf** | BBO 12 billets | ~0 | **À ne pas créer pour le trafic.** BBO l’a fait, ça ne porte rien |
| **Bing / Google Shopping** | BBO | 0 organique utile | Usine interne, pas une collection client |

---

## 6. Ce qu’ils font qu’on ne fait pas

On n’a pas encore de boutique. Lu comme : pratiques observées, et ce qu’on en fait **si** une boutique part.

| Pratique | Qui | Ce qu’on en fait |
|---|---|---|
| Une page type = une famille (poire, géant, canapé, outdoor, gamer) | BBO, Happers, Bananair | Reprendre. C’est l’ETV |
| Page « poire » qui *est* une poire | Bananair, Happers | Reprendre. BBO envoie F1 vers un fauteuil |
| Duo housse / rempli + page F10 | Bananair (r1), BBO (stock sans trafic) | Reprendre l’après-vente, pas l’usine à 331 SKU |
| Déhoussable comme découpe de menu | Bananair | Reprendre l’angle, pas les 35 collections housses |
| Tailles poire calées sur la stature (XL / XXL, cm) | Happers | Reprendre la *structure* d’aide au choix |
| Garantie écrite avec exclusions | BBO 24 mois housse · Happers 4 ans · Icon 1 an | Reprendre le format BBO (exclusions). Ne pas promettre 4 ans sans usine |
| Livraison chiffrée + exceptions (Corse, DOM, relais) | Tous, avec contradictions BBO | Écrire une page qui ne contredit pas le bandeau |
| Récit fabricant + recyclage PSE | Casa seulement | Angle libre sur F1 — eux ne le convertissent pas en SEO |
| Outdoor technique (UV, flottabilité, M1) | Casa | Angle libre vs outdoor générique BBO / Icon |
| Pouf piscine | Casa | Trou d’offre. Demande = part de F7, pas une 11ᵉ famille silencieuse |
| Coussin palette | Happers, Bananair | Trou chez BBO. Hors familles figées |
| Espace pro / contract | Happers, Casa | Plus tard, pas un lancement |
| Compte à rebours + barré permanent | BBO, Happers | **Ne pas reprendre** |
| Une fiche par coloris | Icon, Casa | À éviter : ça gonfle le catalogue sans élargir l’offre |
| Licences football / Greggs | Icon | Ne pas reprendre |
| Peluches en plus du pouf | Bananair | Ne pas reprendre |
| Blog hors sujet pour l’ETV | Happers | Ne pas reprendre |
| 246 collections dont 17 vides + Bing | BBO | Ne pas reproduire l’usine |
| Bandeau « livraison offerte » vs 5 € | BBO | Ne pas recopier la contradiction |

---

## 7. Sourçable chez nos fournisseurs / à écarter / non sourçable

Pas de passe AliExpress (interdite avant GO). Jugement d’offre, pas un sourcing.

**À sourcer en priorité** (présent chez plusieurs indépendants, bande 60–140 €, familles F1/F3/F6/F7/F10) :

- Pouf poire adulte, 1–2 tailles, indoor, déhoussable
- Housse de rechange + sac de billes (F10, Bananair r1)
- Pouf géant / 140×180 (F3)
- Poire gamer (F6, traîne courte mais SERP spécialisée)
- Poire / géant outdoor déperlant (F7, saisonnier)

**Sourçable mais à écarter formellement**

| Objet | Motif |
|---|---|
| Peluche géante / nounours | Autre shopper ; 35 % de l’ETV Bananair ; hors F1–F10 |
| Coussin 47×47, plaid, traversin | Textile enseigne ; BBO en a des centaines, hors cœur |
| Couverture lestée | Déjà au registre (SURVIT) |
| Lit / pouf chien | Autre univers (BBO l’a, collection parfois vide) |
| Pouf cube rangement / coffre | Adjacent mesuré dans le README, GSB, hors familles figées — ne pas l’ajouter en silence |
| Canapé mousse compressée / clic-clac | Bananair / Casa ; autre page, autre logistique |
| Coussin palette | Happers 5 986 ETV mais hors familles ; ne pas l’ériger en famille ici |

**Non sourçable (marque, licence, usine)**

- Fatboy Original et dérivés
- Licences Icon (Greggs, Newcastle, football)
- CloudSac « mémoire de forme » comme nom de gamme
- Garantie 4 ans « fabrication Espagne » Happers — on ne peut pas l’écrire sans l’usine
- Filière recyclage PSE Cotton Wood / Poitou — récit Casa, pas un SKU
- Peaux prestige Casa

---

## 8. Trous d’offre visibles

Ce que le catalogue montre. **Pas une preuve de demande** — les volumes sont dans `02-`.

1. **Housse / recharge comme marque, pas comme entrepôt.** Bananair tient `housse pouf` ; BBO a 331 fiches et 0 ETV F10. Personne n’en fait le récit d’après-vente du poire (sauf BBO qui exclut les billes de la garantie). Place : vendre le siège **et** le consommable, page F10 courte.
2. **Outdoor technique / piscine.** Casa seul sur le flottant, avec specs UV / M1 / oléfine. BBO et Icon font de l’outdoor générique. F7 a 5 940 en B. Place : une page outdoor qui dit l’usage (terrasse, piscine), pas « extérieur » nu.
3. **Récit fabricant FR + recyclage sur la tête `pouf poire`.** Casa l’a, 85 ETV. BBO / Icon sont UK. Happers est ES. Bananair n’a pas d’histoire. La tête est tenue par des vitrines UK et un pure player sans récit. Place de discours, pas de nouvelle famille.
4. **Six poires chez Bananair, 99 chez BBO, 55 chez Happers, 15 visibles chez Casa.** Si on entre, le trou n’est pas « plus de coloris » (Icon en a 600). C’est une poire lisible, tarif 80–110 €, page qui *est* une poire.
5. **Ado occupé, 1–5 ans sans Search.** Ne pas prendre F2 pour une porte. Ne pas prendre l’ado pour une place libre.

**Pas un trou.** L’étage 90–140 € (BBO, Icon). L’étage 60–80 € (Casa, Bananair, Happers). Le 219 € Fatboy. Le canapé pouf 200–680 € BBO (F4 = 1 200 en B).

---

## 9. Ce que je n’ai pas pu établir

- SimilarWeb : inaccessible ici. Règle ×3 **non appliquée**. Aucun « trafic réel » dans ce dossier.
- DataForSEO Labs *paid* = 0 : ne dit pas qui achète en Search / Shopping, ni depuis quand. L’étape 5 a vu BBO, Bananair, Happers, Casa, Icon dans les carrousels.
- Infogreffe / Companies House / Registro mercantil : non ouverts. SIREN / n° UK lus sur mentions publiques seulement.
- Trustpilot Icon, avis Google, presse BBO « enseignes partenaires » : non vérifiés auprès d’un tiers.
- Happers : pas de JSON catalogue, pas de mentions, prix = 1ʳᵉ page de catégorie, sitemap lastmod 2024.
- Casabiloba : 302 URL produit, prix = 24 produits de 1ʳᵉ page par rayon, pas le catalogue entier.
- BBO : API publique plafonnée à 250 × 15 = 3 750 fiches — cohérent avec le sitemap, probablement exhaustif. Collections lues (246), pas le détail de chaque orpheline au-delà du handle.
- Bananair : pages histoire / garantie / retours 404. Politique remboursement : timeout.
- Origine d’expédition réelle (entrepôt UK vs FR vs ES vs CN) : **non établie**. Les adresses légales ne sont pas des entrepôts. Ça bloque tout GO ultérieur sur le hors-gabarit (canapé, 140×180) — déjà noté dans la méthode, pas tranché ici.
- Italpouf, Livedeco, deco-arts, Pouf-pouffe : en page 1 (03-) mais hors brief.

---

## Sources brutes

`boutique-pipeline/analyses/2026-09-03-univers-poufs/raw/<slug>/2026-09-03/` — `scrapes/` (JSON, sitemaps, HTML) et `seo/` (`ranked-keywords-by-url.json`, `relevant-pages.json`, `domain-rank-overview.json`). Analyse BBO : `raw/_scratch/bbo-analyse.json`.
