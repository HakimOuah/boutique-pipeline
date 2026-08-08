# BrandSearch — étude concurrentielle des cinq niches Kraken

**Date de collecte**: 8 août 2026
**Périmètre**: 20 marques/boutiques, quatre par niche
**Source principale**: MCP BrandSearch
**Données brutes**: `competitor-profiles/raw/brandsearch/2026-08-08/`

## Lecture et limites

- Les visites mensuelles et fourchettes de revenu sont des **estimations BrandSearch**, pas des données marchands. La fourchette de revenu correspond aux scénarios BrandSearch conservateur/optimiste et reste dans la devise locale fournie par l’index; quand la devise manque, elle est signalée.
- Les compteurs Meta sont un snapshot de l’index et peuvent agréger déclinaisons, pays, pages et duplications. Les montants/reach EU sont des estimations de la bibliothèque publicitaire, pas la dépense totale de la marque.
- Fraîcheur observée au préflight: marques jusqu’au 24 juillet 2026, Meta jusqu’au 31 juillet 2026; retard global annoncé de 180,61 h.
- Shopify n’est jamais traité comme une preuve de dropshipping. BrandSearch ne permet pas de confirmer le stock, la fabrication, le fournisseur, le délai réel ou le mode de fulfillment.
- Résultat de classification: **aucun `PROBABLE_DROPSHIP` validé** sur cette seule couche. Les cas sans preuves suffisantes restent `INDETERMINE`.

## Vue d’ensemble

L’échantillon comprend 9 boutiques Shopify, 8 PrestaShop, 2 Magento et 1 WooCommerce. La classification prudente retient 16 `MARQUE_ETABLIE` et 4 `INDETERMINE`; aucun domaine n’atteint le niveau `PROBABLE_DROPSHIP` sans correspondance fournisseur ou preuve logistique supplémentaire. Les références digitales les plus instructives sont Hobbii, Dog Friendly Co., NotebookTherapy et Buce Plant; les références françaises les plus directement transposables sont Inlandsis, Craftine, I‑Perles, Perles Corner, Skaii & Shrimps et Aquaplante.

## Chien — mobilité, promenade et sports canins

Le marché se sépare en deux jobs: résoudre la promenade quotidienne (Dog Friendly Co.) et équiper le chien-athlète (Ruffwear, Non-stop, Inlandsis). Une boutique différenciante doit choisir un wedge clair ou organiser ces jobs comme des univers séparés.

| Domaine | Plateforme | Visites/mois estimées | Revenu/mois estimé BrandSearch | Catalogue indexé | Meta actif/total | Classification |
|---|---:|---:|---:|---:|---:|---|
| [Ruffwear](https://ruffwear.com) | shopify | 287 638 | 836,3 k–1,52 M USD | 143 produits / 2 495 variantes / prix moy. 49,82 USD | 39 / 48 | `MARQUE_ETABLIE` |
| [Non-stop dogwear](https://nonstopdogwear.com) | shopify | 255 179 | 712,4 k–1,29 M USD | 255 produits / 2 944 variantes / prix moy. 178,61 USD | 3 / 4 | `MARQUE_ETABLIE` |
| [Dog Friendly Co.](https://dogfriendlyco.com) | shopify | 495 806 | 1,27 M–2,31 M USD | 214 produits / 367 variantes / prix moy. 92,20 USD | 2 532 / 5 466 | `INDETERMINE` |
| [Inlandsis](https://inlandsis.fr) | prestashop | 16 863 | 41,9 k–76,2 k EUR | 300 produits | 52 / 934 | `MARQUE_ETABLIE` |

### Profils et signaux catalogue

#### Ruffwear

- **Positionnement observé**: Performance outdoor, robustesse et mobilité (« trail tested »).
- **Persona inféré**: Propriétaire sportif qui considère le chien comme un partenaire d’aventure et paie pour un équipement technique fiable.
- **Catalogue**: Bottes, harnais, gilets de flottaison, visibilité, vêtements météo; logique de système par usage.
- **Bestsellers exposés**: Grip Trex™ Dog Boots (49,99 USD); Float Coat™ Dog Life Jacket (99,99 USD); Hi & Light™ Lightweight Dog Harness (49,99 USD); Front Range® Dog Harness (59,99 USD); The Beacon™ Dog Safety Light (39,99 USD)
- **Meta**: 39 / 48 actives/total dans la fiche marque; agrégat historique de 340 entrées, mix 51 vidéo / 289 image.
- **Classification**: `MARQUE_ETABLIE` — Marque technique, catalogue cohérent, ancienneté BrandSearch et forte audience sociale; aucun signal fournisseur exact.

#### Non-stop dogwear

- **Positionnement observé**: Liberté de mouvement, traction et performance canicross/mushing.
- **Persona inféré**: Pratiquant régulier ou compétiteur de sports canins, sensible à l’ergonomie et aux pièces de rechange.
- **Catalogue**: Harnais, vestes, laisses, ceintures humaines, pièces détachées; gamme organisée par sport.
- **Bestsellers exposés**: Canix warm-up pants women's (79,95 NOK); Canix warm-up jacket men's (99,95 NOK); Fjord overall raincoat (109,95 NOK); Trekking fleece dog jacket (64,95 NOK); Trekking rope leash (27,95 NOK)
- **Meta**: 3 / 4 actives/total dans la fiche marque; agrégat historique de 24 entrées, mix 6 vidéo / 18 image.
- **Classification**: `MARQUE_ETABLIE` — Marque technique internationale, avis Trustpilot et assortiment spécialisé; aucune preuve de dropshipping.

#### Dog Friendly Co.

- **Positionnement observé**: Promenade sans stress: anti-traction, mise en place rapide, confort, contrôle et personnalisation.
- **Persona inféré**: Propriétaire urbain frustré par un chien qui tire et qui veut une solution simple, rassurante et esthétique.
- **Catalogue**: Kits de harnais coordonnés par couleur, bundles et personnalisation; profondeur plus faible que le nombre de produits ne le laisse penser.
- **Bestsellers exposés**: Test Bunlde (129,3 USD); Signature Kit - Red - FREE D-Ring (92 USD); Signature Kit - Khaki - FREE D-Ring (92 USD); Signature Kit - Yellow - FREE D-Ring (92 USD); Signature Kit - Burgundy - FREE D-Ring (92 USD)
- **Meta**: 2 532 / 5 466 actives/total dans la fiche marque; agrégat historique de 1 401 entrées, mix 1 096 vidéo / 305 image.
- **Classification**: `INDETERMINE` — DTC Shopify très développé et massivement publicitaire, mais BrandSearch ne prouve ni stock, ni fabrication, ni fournisseur.

#### Inlandsis

- **Positionnement observé**: Sécurité, durabilité et expertise française pour les sports canins.
- **Persona inféré**: Canicrosseur/cani-VTTiste français, amateur sérieux cherchant un matériel éprouvé.
- **Catalogue**: Harnais, barres cani-VTT, colliers, accessoires et pièces; fort potentiel de packs par discipline.
- **Bestsellers exposés**: Necklight - Mousqueton ultra-léger pour chien (2,62 EUR); Polar Quest - Harnais canicross, mushing (32,17 EUR); Bikejor Max - Barre cani-VTT (54,67 EUR); Support supplémentaire Bikejor Max (24,68 EUR); Summit - Collier pour chien (11,18 EUR)
- **Meta**: 52 / 934 actives/total dans la fiche marque; agrégat historique de 79 entrées, mix 29 vidéo / 58 image.
- **Classification**: `MARQUE_ETABLIE` — Positionnement explicite de fabricant français et assortiment canicross cohérent; PrestaShop, pas un simple indice Shopify.

### Implication pour la boutique

Positionnement recommandé: « l’équipement qui respecte le mouvement du chien », avec diagnostic par usage, morphologie et niveau. Collections: promenade anti-traction, randonnée, canicross/cani-VTT, senior/récupération, météo/visibilité. Packs complets et pièces compatibles plutôt qu’une juxtaposition de harnais.

## Mercerie et arts du fil

Les acteurs performants vendent soit l’abondance et le réachat (Hobbii), soit une réussite guidée (Craftine), soit l’expertise matière (Laine et Tricot). Le simple catalogue générique est donc peu défendable.

| Domaine | Plateforme | Visites/mois estimées | Revenu/mois estimé BrandSearch | Catalogue indexé | Meta actif/total | Classification |
|---|---:|---:|---:|---:|---:|---|
| [Craftine](https://craftine.com) | magento | 92 033 | 193,8 k–351,8 k (devise non fournie) | 1 000 produits | 15 / 72 | `MARQUE_ETABLIE` |
| [Atelier de la Création](https://atelierdelacreation.com) | PrestaShop | 50 689 | 109,1 k–198,0 k EUR | ND | 0 / 0 | `MARQUE_ETABLIE` |
| [Hobbii](https://hobbii.com) | shopify | 943 933 | 2,85 M–5,17 M USD | 2 000 produits / 18 354 variantes / prix moy. 9,48 USD | 190 / 4 366 | `MARQUE_ETABLIE` |
| [Laine et Tricot](https://laine-et-tricot.com) | shopify | 45 790 | 116,1 k–210,8 k EUR | 1 430 produits / 8 540 variantes / prix moy. 19,20 USD | 0 / 0 | `MARQUE_ETABLIE` |

### Profils et signaux catalogue

#### Craftine

- **Positionnement observé**: Réussir un projet couture sans blocage grâce au kit, à l’inspiration et à l’accompagnement.
- **Persona inféré**: Couturière débutante/intermédiaire qui veut un résultat concret sans composer elle-même tout le panier.
- **Catalogue**: Box, kits, tissus/coupons, cartes cadeaux; le projet fini est l’unité de merchandising.
- **Bestsellers exposés**: Cadeau Craftine Box (39,99 EUR); La Craftine Box (33,9 EUR); Carte Cadeau Couture Craftine (10 EUR); Produit divers (1 EUR); Coupon Tissu Coton imprimé Arty Fleuris sur fond Blanc - Par coupon de 3 mètres (15 EUR)
- **Meta**: 15 / 72 actives/total dans la fiche marque; agrégat historique de 36 entrées, mix 30 vidéo / 6 image.
- **Classification**: `MARQUE_ETABLIE` — Box propriétaire, catalogue couture profond, Magento et historique publicitaire structuré.

#### Atelier de la Création

- **Positionnement observé**: Sélection de mercerie créative couvrant tissus, fil, tricot et perles.
- **Persona inféré**: Créative multi-pratique qui préfère une boutique de confiance à une marketplace généraliste.
- **Catalogue**: Tissus au mètre, fils, perles et mercerie; inspiration pour la navigation transversale.
- **Bestsellers exposés**: Bestsellers non exposés par BrandSearch.
- **Meta**: 0 / 0 actives/total dans la fiche marque; agrégat historique de 0 entrées, mix 0 vidéo / 0 image.
- **Classification**: `MARQUE_ETABLIE` — Audience et communauté visibles, assortiment spécialisé multi-pratiques; aucune donnée de stock ou fournisseur.

#### Hobbii

- **Positionnement observé**: Choix massif, prix accessibles, modèles gratuits et plaisir communautaire.
- **Persona inféré**: Tricoteuse/crocheteuse fréquente, sensible au choix de couleurs, aux promotions et au renouvellement.
- **Catalogue**: Fils, accessoires, patrons et projets; énorme profondeur de variantes et logique de réachat.
- **Bestsellers exposés**: Twister Halloween (Limited Edition) (38,4 USD); Baby Tommi - Top & Shorts (6,5 USD); NoonChaiTea - Shawl (7,5 USD); LongJingTea - Blanket (7,5 USD); Poppys Baby Blanket Glitter (8 USD)
- **Meta**: 190 / 4 366 actives/total dans la fiche marque; agrégat historique de 1 190 entrées, mix 445 vidéo / 807 image.
- **Classification**: `MARQUE_ETABLIE` — Très forte audience, 2 000 produits indexés, 34 336 avis Trustpilot et activité publicitaire soutenue.

#### Laine et Tricot

- **Positionnement observé**: « Tour du monde de la laine »: fibres, couleurs et marques choisies.
- **Persona inféré**: Passionnée plus experte, prête à payer pour la matière, l’origine et la découverte.
- **Catalogue**: Laines multimarques, accessoires, catalogues et patrons; potentiel de filtres matière/origine/échantillon.
- **Bestsellers exposés**: Cotton Whirl (23,95 EUR); Puzzle The Cat Café – Trevell - 1000 pièces (27,9 EUR); 26_2  No. 2 Lucienne Skirt (4,9 EUR); Fair Isle Knitting Tradition (22,9 EUR); Magical Woodland Knits (20,9 EUR)
- **Meta**: 0 / 0 actives/total dans la fiche marque; agrégat historique de 0 entrées, mix 0 vidéo / 0 image.
- **Classification**: `MARQUE_ETABLIE` — Spécialiste français Shopify avec 1 430 produits et positionnement éditorial distinct.

### Implication pour la boutique

Positionnement recommandé: boutique projet-first. Chaque entrée commence par l’objet à réaliser, puis niveau, durée, taille et style. Kits complets, vidéo courte, patron, quantités calculées et recharge matière. Choisir couture OU tricot/crochet comme wedge initial avant d’élargir.

## Scrapbooking et journaling

Le scrap français visible est très fragmenté et peu puissant digitalement, tandis que NotebookTherapy transforme des fournitures ordinaires en rituel esthétique, collectionnable et cadeau.

| Domaine | Plateforme | Visites/mois estimées | Revenu/mois estimé BrandSearch | Catalogue indexé | Meta actif/total | Classification |
|---|---:|---:|---:|---:|---:|---|
| [Variations Créatives](https://variationscreatives.fr) | PrestaShop | 5 495 | 14,4 k–26,1 k EUR | ND | 0 / 0 | `INDETERMINE` |
| [Florilèges Design](https://florilegesdesign.com) | PrestaShop | 2 294 | 4,9 k–8,8 k EUR | ND | 0 / 0 | `MARQUE_ETABLIE` |
| [Mes P’tits Ciseaux](https://mesptitsciseaux.com) | PrestaShop | 1 002 | 2,2 k–4,0 k (devise non fournie) | ND | 0 / 0 | `INDETERMINE` |
| [NotebookTherapy](https://notebooktherapy.com) | shopify | 211 567 | 659,6 k–1,20 M USD | 483 produits / 855 variantes / prix moy. 39,23 USD | 253 / 401 | `MARQUE_ETABLIE` |

### Profils et signaux catalogue

#### Variations Créatives

- **Positionnement observé**: Mettre en valeur ses photos et souvenirs grâce au scrapbooking.
- **Persona inféré**: Memory keeper qui veut transformer ses photos en objets personnels.
- **Catalogue**: Matériel de scrap, carterie et DIY; détails de profondeur non observés dans BrandSearch.
- **Bestsellers exposés**: Bestsellers non exposés par BrandSearch.
- **Meta**: 0 / 0 actives/total dans la fiche marque; agrégat historique de 0 entrées, mix 0 vidéo / 0 image.
- **Classification**: `INDETERMINE` — Spécialiste français identifié, mais extraction BrandSearch limitée: peu de métriques, aucun bestseller ni activité Meta visible.

#### Florilèges Design

- **Positionnement observé**: Collections françaises de scrapbooking et carterie avec signature créative.
- **Persona inféré**: Scrappeuse passionnée fidèle à des univers graphiques et à des sorties de collection.
- **Catalogue**: Collections créatives propriétaires; opportunité de merchandising par thème/saison.
- **Bestsellers exposés**: Bestsellers non exposés par BrandSearch.
- **Meta**: 0 / 0 actives/total dans la fiche marque; agrégat historique de 0 entrées, mix 0 vidéo / 0 image.
- **Classification**: `MARQUE_ETABLIE` — Créateur/fabricant français explicitement déclaré; métriques digitales modestes mais identité produit propriétaire.

#### Mes P’tits Ciseaux

- **Positionnement observé**: Large choix de matériel pour le scrapbooking et les activités manuelles.
- **Persona inféré**: Pratiquante DIY qui cherche une solution généraliste et pratique.
- **Catalogue**: Assortiment annoncé large mais bestsellers/variantes manquants dans l’index.
- **Bestsellers exposés**: Bestsellers non exposés par BrandSearch.
- **Meta**: 0 / 0 actives/total dans la fiche marque; agrégat historique de 0 entrées, mix 0 vidéo / 0 image.
- **Classification**: `INDETERMINE` — Boutique spécialisée visible, mais BrandSearch n’expose ni catalogue détaillé, ni publicité, ni preuve logistique.

#### NotebookTherapy

- **Positionnement observé**: Rituel esthétique et apaisant: collections saisonnières, unboxing/ASMR, fin de la peur de la page blanche.
- **Persona inféré**: Millennial/Gen Z attirée par le journaling, l’organisation douce, le cadeau et l’esthétique asiatique.
- **Catalogue**: Bullet journals, travel notebooks, stickers, stencils, pochettes; capsules assorties et éditions limitées.
- **Bestsellers exposés**: Tsuki ‘Story of Summer’ Collector’s Edition Luxury Bullet Journal ☾ (46,18 USD); Tsuki ‘Summer Story’ Sticker Set ☾ (17,58 USD); Tsuki ‘Dark Academia’ Limited Edition Bullet Journal ☾ (42,88 USD); Tsuki ‘Light Academia’ Limited Edition Bullet Journal ☾ (42,88 USD); Tsuki ‘Vintage Academia’ Bullet Journal Stamp ☾ (36,28 USD)
- **Meta**: 253 / 401 actives/total dans la fiche marque; agrégat historique de 291 entrées, mix 224 vidéo / 67 image.
- **Classification**: `MARQUE_ETABLIE` — Shopify depuis 2017 dans l’index, 211 k visites estimées, 483 produits et forte activité Meta; le modèle logistique reste non prouvé.

### Implication pour la boutique

Positionnement recommandé: « préserver ses souvenirs et retrouver un moment calme », en français. Trois parcours: mémoire/photos, organisation/planning, détente créative. Capsules saisonnières, kits guidés 30/60/120 minutes, palettes coordonnées et contenu ASMR/tutoriel. Ne pas se battre uniquement sur le nombre de tampons ou stickers.

## Perles et création de bijoux

La profondeur de catalogue est extrême et les bestsellers sont des composants à 1–6 €. Le vrai avantage compétitif vient de la taxonomie, de la compatibilité et de la capacité à faire monter le panier, pas d’un SKU vedette.

| Domaine | Plateforme | Visites/mois estimées | Revenu/mois estimé BrandSearch | Catalogue indexé | Meta actif/total | Classification |
|---|---:|---:|---:|---:|---:|---|
| [I‑Perles](https://i-perles.fr) | shopify | 19 323 | 37,5 k–68,1 k EUR | 2 000 produits / 10 024 variantes / prix moy. 31,62 USD | 6 / 13 | `MARQUE_ETABLIE` |
| [France Perles](https://franceperles.com) | PrestaShop | 54 242 | 99,2 k–180,1 k EUR | ND | 0 / 0 | `MARQUE_ETABLIE` |
| [Dreambeads Online](https://dreambeads-online.com) | Magento | 4 180 | 12,3 k–22,4 k GBP | ND | 0 / 0 | `INDETERMINE` |
| [Perles Corner](https://perlescorner.com) | shopify | 13 785 | 29,4 k–53,3 k EUR | 2 000 produits / 5 685 variantes / prix moy. 5,36 USD | 0 / 45 | `MARQUE_ETABLIE` |

### Profils et signaux catalogue

#### I‑Perles

- **Positionnement observé**: Profondeur technique, achat en gros/détail, avantages pro et tutoriels.
- **Persona inféré**: Créatrice avancée ou micro-entreprise de bijoux qui recherche compatibilité, disponibilité et prix par quantité.
- **Catalogue**: Apprêts, fils, rocailles, Bohême, argent 925, cristal; petits prix et achats répétitifs.
- **Bestsellers exposés**: Boucles d'oreilles Crochets laiton argenté 18mm (10) (1,98 EUR); Beadalon fil élastique elasticity transparent 0,5mm, 5m en sachet sans bobine(5m) (5,14 EUR); Perles facettes de bohème jet 4mm (100) (2,58 EUR); Perles facettes de bohème crystal 4mm (100) (2,58 EUR); Boucles d'oreilles Crochets argent 925 14mm (2) (2,45 EUR)
- **Meta**: 6 / 13 actives/total dans la fiche marque; agrégat historique de 31 entrées, mix 6 vidéo / 25 image.
- **Classification**: `MARQUE_ETABLIE` — 2 000 produits, 10 024 variantes, avis et publicité B2C/B2B; aucune preuve de dropshipping.

#### France Perles

- **Positionnement observé**: Large choix de perles, composants et pierres fines/précieuses.
- **Persona inféré**: Créatrice qui choisit d’abord la matière, la qualité et la disponibilité.
- **Catalogue**: Perles et accessoires; profondeur annoncée importante, mais non détaillée par BrandSearch.
- **Bestsellers exposés**: Bestsellers non exposés par BrandSearch.
- **Meta**: 0 / 0 actives/total dans la fiche marque; agrégat historique de 0 entrées, mix 0 vidéo / 0 image.
- **Classification**: `MARQUE_ETABLIE` — 54 k visites estimées et promesse de plus de 10 000 références; extraction produit et Meta toutefois incomplète.

#### Dreambeads Online

- **Positionnement observé**: Qualité et choix de fournitures pour créer ses bijoux.
- **Persona inféré**: Amatrice de DIY qui cherche une boutique de composants complète.
- **Catalogue**: Perles, charms, pendentifs, fils et apprêts annoncés; profondeur non mesurée.
- **Bestsellers exposés**: Bestsellers non exposés par BrandSearch.
- **Meta**: 0 / 0 actives/total dans la fiche marque; agrégat historique de 0 entrées, mix 0 vidéo / 0 image.
- **Classification**: `INDETERMINE` — Boutique spécialisée Magento, mais faible visibilité et aucune extraction de produits/publicités permettant de qualifier le modèle.

#### Perles Corner

- **Positionnement observé**: Expérience créative premium: pierres naturelles, fabrication européenne, ateliers et tutoriels.
- **Persona inféré**: Créatrice urbaine qui valorise l’esthétique, le conseil, l’expérience en atelier et l’origine.
- **Catalogue**: Perles de Bohême, pierres naturelles, fils, outils; petits composants à assembler en projets.
- **Bestsellers exposés**: Fil de perles de Bohème ronde 5mm Bleu clair opaque (2,4 EUR); 2 Pendentifs fleur asymétrique — verre violet (1,2 EUR); 2 Pendentifs fleur asymétrique — verre bleu persan (1,2 EUR); 2 Pendentifs fleur asymétrique — verre rose (1,2 EUR); Fil de perles de Bohème rondes facettées 4mm Rose et violet irisé mat (2,9 EUR)
- **Meta**: 0 / 45 actives/total dans la fiche marque; agrégat historique de 75 entrées, mix 41 vidéo / 35 image.
- **Classification**: `MARQUE_ETABLIE` — Boutique-atelier parisienne, 2 000 produits Shopify, communauté sociale et historique publicitaire; aucune preuve fournisseur exacte.

### Implication pour la boutique

Positionnement recommandé: « créez un bijou fini sans erreur de compatibilité ». Navigation par projet, style, métal, diamètre et niveau; kits débutants, calculateurs de quantité, bundles assortis et conditionnements pro. Séparer clairement hobby, cadeau et micro-marque.

## Aquariophilie et aquascaping

Les généralistes gagnent par la profondeur et le prix; Buce Plant gagne par l’imaginaire du paysage sous-marin; Skaii gagne par l’expertise crevettes. La compatibilité technique est l’espace de différenciation le plus utile.

| Domaine | Plateforme | Visites/mois estimées | Revenu/mois estimé BrandSearch | Catalogue indexé | Meta actif/total | Classification |
|---|---:|---:|---:|---:|---:|---|
| [Skaii & Shrimps](https://skaii-and-shrimps.fr) | prestashop | 11 258 | 27,8 k–50,5 k (devise non fournie) | 300 produits | 1 / 16 | `MARQUE_ETABLIE` |
| [Aquaplante](https://aquaplante.fr) | PrestaShop | 123 491 | 258,6 k–469,5 k EUR | ND | 0 / 6 | `MARQUE_ETABLIE` |
| [Materiel-Aquatique.com](https://materiel-aquatique.com) | WooCommerce | ND | ND | ND | 0 / 28 | `MARQUE_ETABLIE` |
| [Buce Plant](https://buceplant.com) | shopify | 366 868 | 1,13 M–2,04 M USD | 1 771 produits / 3 489 variantes / prix moy. 177,75 USD | 43 / 43 | `MARQUE_ETABLIE` |

### Profils et signaux catalogue

#### Skaii & Shrimps

- **Positionnement observé**: Expertise crevettes et aquascaping, technicité et prix.
- **Persona inféré**: Éleveur de crevettes/aquascaper déjà initié qui recherche des références très spécifiques.
- **Catalogue**: Sols techniques, accessoires crevettes, oxydation, sélection, consommables; longue traîne experte.
- **Bestsellers exposés**: Chaufferette  40h Heat Pack (1,2 EUR); Epuisette de sélection Noire 40cm - Mailles Fines (11,9 EUR); Oxydator D (28,9 EUR); Glasgarten - Environment Aquarium Soil Fulvic + 4L Powder (21,95 EUR); Ada Bacter Ball (25,9 EUR)
- **Meta**: 1 / 16 actives/total dans la fiche marque; agrégat historique de 15 entrées, mix 6 vidéo / 12 image.
- **Classification**: `MARQUE_ETABLIE` — Spécialiste français très cohérent, 300 produits et historique publicitaire; aucune preuve de stock pour chaque référence.

#### Aquaplante

- **Positionnement observé**: Des milliers de références à petit prix, arrivages et fidélité.
- **Persona inféré**: Aquariophile généraliste sensible au choix, au prix et à la disponibilité.
- **Catalogue**: Plantes, pompes, filtres, éclairage, décoration et accessoires; logique one-stop-shop.
- **Bestsellers exposés**: Bestsellers non exposés par BrandSearch.
- **Meta**: 0 / 6 actives/total dans la fiche marque; agrégat historique de 7 entrées, mix 1 vidéo / 6 image.
- **Classification**: `MARQUE_ETABLIE` — 123 k visites estimées, 2 285 avis Trustpilot et profondeur d’offre annoncée; pas Shopify.

#### Materiel-Aquatique.com

- **Positionnement observé**: Le magasin technique complet avec livraison offerte dès 69 €.
- **Persona inféré**: Aquariophile/bassin qui veut acheter entretien, équipement et consommables au même endroit.
- **Catalogue**: Matériel, plantes, nourriture, soins, bassin; panier construit autour de la compatibilité et du seuil de livraison.
- **Bestsellers exposés**: Bestsellers non exposés par BrandSearch.
- **Meta**: 0 / 28 actives/total dans la fiche marque; agrégat historique de 29 entrées, mix 2 vidéo / 27 image.
- **Classification**: `MARQUE_ETABLIE` — WooCommerce, plus de 5 000 références annoncées et historique Meta; visites et bestsellers absents de BrandSearch.

#### Buce Plant

- **Positionnement observé**: « Aquascaping Super Shop » pour construire un paysage naturel sous l’eau.
- **Persona inféré**: Aquascaper aspirant ou confirmé qui cherche inspiration, choix et compatibilité dans un seul univers.
- **Catalogue**: Plantes, crevettes/escargots, filtration, hardscape et accessoires; mix vivant, consommable et équipement.
- **Bestsellers exposés**: Chihiros - Power Adapter Replacement (14,99 USD); Ramshorn Snails (15,99 USD); Purple King Kong Shrimp (110,99 USD); Ultra Fresh Picky Tropical Fish Flakes (7,99 USD); Hygger Aquarium Biochemical Sponge Filter (13,99 USD)
- **Meta**: 43 / 43 actives/total dans la fiche marque; agrégat historique de 83 entrées, mix 40 vidéo / 54 image.
- **Classification**: `MARQUE_ETABLIE` — 1 771 produits Shopify, forte audience et présence sociale, catalogue aquascaping cohérent; modèle fournisseur exact non observé.

### Implication pour la boutique

Positionnement recommandé: « votre écosystème compatible, du projet à l’entretien ». Parcours par volume de bac, eau douce/crevettes/plantes, niveau et style; kits éclairage/CO₂/sol/plantes, fiches de compatibilité et calendrier d’entretien. Pour un modèle dropshipping, séparer les produits secs des animaux/plantes vivants et qualifier la logistique avant toute sélection.

## Enseignements transversaux pour la différenciation

1. **Les leaders vendent un système ou un résultat.** Harnais + laisse + usage; tissu + patron + tutoriel; journal + stickers + rituel; perles + apprêts compatibles; bac + éclairage + CO₂ + entretien.
2. **Les catalogues de 1 000 à 2 000 références ne sont utiles que si la navigation absorbe la complexité.** Les filtres par usage, matière, compatibilité, dimension, niveau et projet sont un actif produit, pas un détail UX.
3. **Le low ticket appelle des paniers composés.** Bundles, kits, recharges, conditionnements, seuil de livraison, cartes cadeaux et contenus « projet complet » doivent être conçus dès l’arborescence.
4. **Le contenu est une partie de l’offre.** Craftine rassure par l’accompagnement, NotebookTherapy donne une identité émotionnelle, I‑Perles utilise le tutoriel, et les marques canines démontrent l’usage et le confort.
5. **La preuve doit être spécifique à la niche.** Compatibilité et sécurité pour le chien/aquarium; origine et matière pour la laine/perle; rendu final et difficulté pour les loisirs créatifs.
6. **L’importation seule n’est pas une différenciation.** Le catalogue AliExpress devra être traduit en solutions cohérentes, puis vérifié par variante, matière, conformité, livraison France et compatibilité.

## Pistes confrontées au snapshot SEMrush France

Le raccord de 15 domaines est conservé dans `../raw/semrush/2026-08-08/semrush-fr-domain-overview-top-keywords.json` et interprété dans `../etude-concurrentielle-5-niches-2026-08-08.md`.

- **Chien**: harnais anti-traction + confort/morphologie; randonnée/canicross; senior/mobilité; visibilité et météo.
- **Mercerie**: kits couture par vêtement; kits crochet/tricot par niveau; tissus par projet; accessoires calculés avec le patron.
- **Scrap/journaling**: bullet journal débutant; kits mémoire/photo; journaling anti-stress; coffrets saisonniers/cadeaux.
- **Perles**: kit bracelet/collier/boucles; acier inoxydable/hypoallergénique; pierres naturelles; apprêts compatibles; lots pro.
- **Aquascaping**: kit nano aquarium; crevettes; CO₂; éclairage plantes; sol technique; entretien par volume de bac.

## Fichiers de preuve BrandSearch

- `metrics-selected-brands.json`: métriques comparables des 20 domaines.
- `summary-<domaine>.json`: fiche marque + produits + publicités actives.
- `full-<domaine>.json`: fiche marque détaillée.
- `products-<domaine>.json`: bestsellers exposés par BrandSearch.
- `meta-aggregates-<domaine>.json`: agrégats Meta.
- `meta-active-<domaine>.json`: publicités Meta actives récupérées pour les domaines ayant une activité significative.
- `lookup-*.json` et `search-*.json`: découverte et validation des domaines.

## Limite de décision

Cette couche suffit pour construire des hypothèses de catalogue, d’angle et de persona. Elle **ne suffit pas** pour déclarer une boutique dropshipper, copier un produit, attribuer un fournisseur ou considérer une estimation de revenu comme un chiffre réel. Ces décisions exigent le croisement site rendu + SEMrush + correspondance fournisseur exacte + conditions de livraison France.
