import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  SpreadsheetFile,
  Workbook,
} from "/Users/Hakim/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs";

const runDir = path.dirname(fileURLToPath(import.meta.url));
const outputDir = path.resolve(runDir, "../../outputs/2026-08-08-kraken-concurrence-v1");
const outputPath = path.join(outputDir, "5-niches-kraken-etude-concurrentielle-2026-08-08.xlsx");
const previewDir = path.join(outputDir, "previews");

const api = JSON.parse(await fs.readFile(path.join(runDir, "aliexpress-search-results.json"), "utf8"));
const curated = JSON.parse(await fs.readFile(path.join(runDir, "curated-products.json"), "utf8"));
const probes = JSON.parse(await fs.readFile(path.join(runDir, "representative-exact-probes.json"), "utf8"));
const semrush = JSON.parse(
  await fs.readFile(
    path.resolve(runDir, "../../../competitor-profiles/raw/semrush/2026-08-08/semrush-fr-domain-overview-top-keywords.json"),
    "utf8",
  ),
);

const VOLUMES = {
  "aiguilles à coudre": 480,
  "aiguilles machine à coudre": 390,
  "fil à coudre": 1300,
  "boutons couture": 320,
  "bouton pression": 3600,
  "pince pression": 590,
  "fermeture éclair": 4400,
  "ruban couture": 260,
  "biais couture": 2400,
  "passepoil couture": 1600,
  "élastique couture": 390,
  "dentelle couture": 90,
  "épingles couture": 140,
  "clips couture": 50,
  "ciseaux couture": 2400,
  "découd vite": 1300,
  "craie tailleur": 110,
  "pied presseur": 260,
  "canette machine à coudre": 1000,
  "mètre ruban couture": 720,
  "papier scrapbooking": 1300,
  "album scrapbooking": 1600,
  "tampon scrapbooking": 320,
  "tampon transparent scrapbooking": 30,
  "encre scrapbooking": 70,
  "stickers scrapbooking": 590,
  "washi tape": 2400,
  "perforatrice scrapbooking": 480,
  "dies scrapbooking": 170,
  "matrice découpe scrapbooking": 40,
  "pochoir scrapbooking": 140,
  "embellissement scrapbooking": 90,
  "fleurs papier scrapbooking": 0,
  "ruban scrapbooking": 20,
  "colle scrapbooking": 140,
  "massicot papier": 2900,
  "plioir papier": 140,
  "tapis découpe scrapbooking": 0,
  "kit scrapbooking": 880,
  "poudre embossage": 50,
  "filtre aquarium": 3600,
  "pompe aquarium": 5400,
  "pompe à air aquarium": 480,
  "chauffage aquarium": 1900,
  "éclairage aquarium": 590,
  "thermomètre aquarium": 590,
  "diffuseur co2 aquarium": 480,
  "kit co2 aquarium": 880,
  "test eau aquarium": 390,
  "aspirateur aquarium": 2400,
  "nettoyeur vitre aquarium": 140,
  "décoration aquarium": 1600,
  "plante artificielle aquarium": 210,
  "épuisette aquarium": 70,
  "distributeur nourriture poisson": 1600,
  "pondoir aquarium": 140,
  "filtre crevette aquarium": 20,
  "tuyau aquarium": 480,
  "skimmer aquarium": 260,
  "osmolateur aquarium": 260,
  "harnais chien": 22200,
  "laisse chien": 5400,
  "collier chien": 9900,
  "longe chien": 4400,
  "laisse enrouleur chien": 590,
  "muselière chien": 6600,
  "médaille chien": 1900,
  "gourde chien": 2400,
  "gamelle pliable chien": 390,
  "sac transport chien": 2400,
  "housse voiture chien": 720,
  "ceinture voiture chien": 170,
  "rampe chien": 2400,
  "gilet sauvetage chien": 1900,
  "manteau chien": 4400,
  "imperméable chien": 1900,
  "chaussures chien": 590,
  "poussette chien": 4400,
  "panier vélo chien": 210,
  "pochette friandise chien": 260,
  "perles pour bijoux": 720,
  "perles rocailles": 590,
  "perles heishi": 1300,
  "perles miyuki": 2400,
  "perles lettres": 480,
  "perles naturelles": 880,
  "perles verre": 720,
  "perles bois": 1300,
  "apprêts bijoux": 170,
  "fermoir bijoux": 260,
  "chaine bijoux": 880,
  "pince bijoux": 880,
  "breloque": 4400,
  "pendentif": 9900,
  "fil élastique bracelet": 210,
  "support boucle d'oreille": 590,
  "anneau bijoux": 110,
  "connecteur bijoux": 70,
  "aiguille perles": 170,
  "métier à tisser perles": 720,
};

const SUMMARY = [
  {
    rank: 1,
    niche: "Balade, transport & mobilité du chien",
    verdict: "GO CONDITIONNEL",
    score: 84,
    cleanVolume: 81860,
    grossVolume: 81860,
    trendAverage: 11,
    trendChange: 0.028,
    serp: "Shopping + spécialistes + comparateurs",
    competitors: "Ruffwear; Milk&Pepper; boutiques spécialisées; comparateurs",
    risk: "Charge, tailles et allégations sécurité sur harnais/laisses/voiture",
    next: "Lancer d'abord promenade non critique; valider séparément les produits de sécurité",
  },
  {
    rank: 2,
    niche: "Mercerie créative & arts du fil",
    verdict: "GO CONDITIONNEL",
    score: 78,
    cleanVolume: 221680,
    grossVolume: 221680,
    trendAverage: 40,
    trendChange: -0.235,
    serp: "Shopping + nombreuses merceries spécialisées",
    competitors: "Atelier de la Création; Mercerie Durand; Rascol; Craftine",
    risk: "Concurrence installée; objets pointus; vérité matière/dimensions",
    next: "Angle kits débutants + filtres techniques; privilégier accessoires plutôt que tissus",
  },
  {
    rank: 3,
    niche: "Scrapbooking & journaling",
    verdict: "GO CONDITIONNEL",
    score: 80,
    cleanVolume: 64740,
    grossVolume: 135140,
    trendAverage: 15,
    trendChange: -0.059,
    serp: "Shopping + boutiques spécialisées + tutoriels",
    competitors: "Custodeco; La Fée du Scrap; La Fourmi Créative",
    risk: "Propriété intellectuelle sur motifs; colles/poudres; requêtes informationnelles",
    next: "Cœur albums/journaling/découpe; exclure personnages et motifs sous licence",
  },
  {
    rank: 4,
    niche: "Perles & création de bijoux",
    verdict: "GO CONDITIONNEL",
    score: 72,
    cleanVolume: 35770,
    grossVolume: 47870,
    trendAverage: 75,
    trendChange: -0.068,
    serp: "Shopping + grossistes et spécialistes DIY",
    competitors: "Perles&Co; Perles à Tout Va; Dreambeads",
    risk: "Composition, nickel/plomb/cadmium, petites pièces, pierres naturelles",
    next: "Rester sur fantaisie DIY; bannir les allégations matière non documentées",
  },
  {
    rank: 5,
    niche: "Aquariophilie & aquascaping",
    verdict: "GO CONDITIONNEL",
    score: 68,
    cleanVolume: 48320,
    grossVolume: 122320,
    trendAverage: 2,
    trendChange: -0.173,
    serp: "Shopping + spécialistes + marques techniques",
    competitors: "Aquael; Oase; boutiques aquariophiles; comparateurs",
    risk: "Électricité, étanchéité, CO2 et bien-être animal",
    next: "Première vague non électrique; conformité renforcée avant pompes/chauffages/LED",
  },
];

const PRIORITY_COMPETITION_ROWS = [
  [
    1,
    "Scrapbooking & journaling",
    64740,
    "Modérée côté France; forte preuve DTC internationale",
    "Souvenir-first, kits modulaires, palettes et preuve couleur",
    "PRIORITÉ TEST",
    "Valider kit modulable, licences et panier"
  ],
  [
    2,
    "Balade, transport & mobilité du chien",
    81860,
    "Spécialistes techniques forts; un probable dropshipper faible en SEO",
    "France-first par scénario et morphologie",
    "GO CONDITIONNEL",
    "Commencer sur accessoires non critiques"
  ],
  [
    3,
    "Mercerie créative & arts du fil",
    221680,
    "Très élevée: autorités historiques et méga-catalogues",
    "Projet-first, mini-kits, quantité calculée",
    "GO CONDITIONNEL",
    "Choisir couture accessoires OU crochet/tricot"
  ],
  [
    4,
    "Perles & création de bijoux",
    35770,
    "Forte autorité Perles & Co; longue traîne transactionnelle",
    "Bijou-first, compatibilité, lots et preuve métal",
    "GO CONDITIONNEL",
    "Sous confort 40k; modéliser AOV low ticket"
  ],
  [
    5,
    "Aquariophilie & aquascaping",
    48320,
    "Autorités SEO/paid et forte technicité",
    "Système compatible par volume, niveau et style",
    "GO CONDITIONNEL",
    "Sec/non électrique en première vague"
  ]
];

const COMPETITOR_BASE_ROWS = [
  {
    "niche": "Chien",
    "name": "Fenril",
    "domain": "fenril.fr",
    "url": "https://www.fenril.fr/",
    "classification": "SPECIALISTE_STOCK",
    "tech": "PrestaShop",
    "visits": 5372,
    "catalogue": "176 produits indexés",
    "meta": null,
    "angle": "Expertise sports de traction",
    "merch": "Navigation par discipline, kits techniques, multi-marques",
    "weakness": "Moins centré transport/senior; univers très technique",
    "persona": "Pratiquant canicross/cani-VTT"
  },
  {
    "niche": "Chien",
    "name": "Polytrans",
    "domain": "polytrans.fr",
    "url": "https://www.polytrans.fr/",
    "classification": "MARQUE_ETABLIE",
    "tech": "ND",
    "visits": null,
    "catalogue": "> 3 800 références revendiquées",
    "meta": null,
    "angle": "Exhaustivité technique historique",
    "merch": "Chien/chat, particuliers/pros, marque propre et promotions",
    "weakness": "Surcharge et dilution du projet mobilité",
    "persona": "Propriétaire exigeant / professionnel"
  },
  {
    "niche": "Chien",
    "name": "Non-stop Dogwear",
    "domain": "nonstopdogwear.com",
    "url": "https://www.nonstopdogwear.com/fr/",
    "classification": "MARQUE_ETABLIE",
    "tech": "Shopify",
    "visits": 255179,
    "catalogue": "255 produits indexés",
    "meta": 3,
    "angle": "Performance, liberté de mouvement, outdoor",
    "merch": "Systèmes par sport, sizing, contenu athlète",
    "weakness": "Prix, friction taille/retour, trafic FR très brandé",
    "persona": "Duo humain-chien sportif"
  },
  {
    "niche": "Chien",
    "name": "Boutiquechien",
    "domain": "boutiquechien.fr",
    "url": "https://boutiquechien.fr/",
    "classification": "PROBABLE_DROPSHIP — confiance moyenne",
    "tech": "Shopify",
    "visits": 1331,
    "catalogue": "1 308 produits indexés",
    "meta": 0,
    "angle": "Accessoires utiles et rassurants",
    "merch": "Catalogue horizontal, pages SEO génériques, livraison 7–12 j",
    "weakness": "Faible preuve et autorité; fournisseur non prouvé",
    "persona": "Propriétaire généraliste"
  },
  {
    "niche": "Chien",
    "name": "Dog Friendly Co.",
    "domain": "dogfriendlyco.com",
    "url": "https://dogfriendlyco.com/",
    "classification": "INDETERMINE",
    "tech": "Shopify",
    "visits": 495806,
    "catalogue": "214 produits indexés",
    "meta": 2532,
    "angle": "Promenade anti-traction simple et esthétique",
    "merch": "Kits coordonnés, couleurs, personnalisation, Meta massif",
    "weakness": "Modèle fournisseur/stock non prouvé",
    "persona": "Propriétaire urbain frustré par la traction"
  },
  {
    "niche": "Mercerie",
    "name": "Rascol",
    "domain": "rascol.com",
    "url": "https://www.rascol.com/",
    "classification": "MARQUE_ETABLIE / STOCKISTE",
    "tech": "PrestaShop",
    "visits": null,
    "catalogue": "> 60 000 références revendiquées",
    "meta": null,
    "angle": "Autorité, choix, conseil technique",
    "merch": "Mega-menu, guides, calculateurs, UGC, fidélité",
    "weakness": "Trop de choix pour un premier projet",
    "persona": "Pratiquante engagée"
  },
  {
    "niche": "Mercerie",
    "name": "Atelier de la Création",
    "domain": "atelierdelacreation.com",
    "url": "https://atelierdelacreation.com/",
    "classification": "MARQUE_ETABLIE / OMNICANAL",
    "tech": "PrestaShop",
    "visits": 50689,
    "catalogue": "ND",
    "meta": 0,
    "angle": "Sélection premium, style et conseil magasin",
    "merch": "Tissus, fils, perles, kits, tutos, cours et retrait",
    "weakness": "Parcours difficulté/temps incomplet",
    "persona": "Créative multi-pratique"
  },
  {
    "niche": "Mercerie",
    "name": "Craftine",
    "domain": "craftine.com",
    "url": "https://craftine.com/",
    "classification": "MARQUE_ETABLIE",
    "tech": "Magento",
    "visits": 92033,
    "catalogue": "1 000 produits indexés",
    "meta": 15,
    "angle": "Créer avec confiance",
    "merch": "Box bimestrielle, kits, patrons, tissus et remises",
    "weakness": "Kit/tailles contestés; dépendance à l'urgence",
    "persona": "Couturière débutante/intermédiaire"
  },
  {
    "niche": "Mercerie",
    "name": "Hobbii",
    "domain": "hobbii.com",
    "url": "https://hobbii.com/",
    "classification": "MARQUE_ETABLIE",
    "tech": "Shopify",
    "visits": 943933,
    "catalogue": "2 000 produits / 18 354 variantes",
    "meta": 190,
    "angle": "Choix massif, prix, modèles gratuits, communauté",
    "merch": "Fils, patrons, projets, promotions et réachat couleur",
    "weakness": "Difficile à battre en profondeur/prix",
    "persona": "Tricoteuse/crocheteuse fréquente"
  },
  {
    "niche": "Mercerie",
    "name": "Laine et Tricot",
    "domain": "laine-et-tricot.com",
    "url": "https://laine-et-tricot.com/",
    "classification": "MARQUE_ETABLIE",
    "tech": "Shopify",
    "visits": 45790,
    "catalogue": "1 430 produits / 8 540 variantes",
    "meta": 0,
    "angle": "Tour du monde de la laine",
    "merch": "Fibres, origine, marques choisies, patrons",
    "weakness": "Moins guidé par résultat pour la novice",
    "persona": "Passionnée matière experte"
  },
  {
    "niche": "Scrap",
    "name": "Scrapmalin",
    "domain": "scrapmalin.com",
    "url": "https://www.scrapmalin.com/",
    "classification": "MARQUE_ETABLIE / STOCKISTE",
    "tech": "42stores + Algolia",
    "visits": null,
    "catalogue": "> 80 000 références revendiquées",
    "meta": null,
    "angle": "Choix et prix malins",
    "merch": "Multi-loisirs, promos et profondeur extrême",
    "weakness": "Spécialité diluée; SEO très bruité",
    "persona": "Créative prix/choix"
  },
  {
    "niche": "Scrap",
    "name": "La Fourmi Créative",
    "domain": "lafourmicreative.fr",
    "url": "https://www.lafourmicreative.fr/",
    "classification": "MARQUE_ETABLIE / STOCKISTE",
    "tech": "PrestaShop",
    "visits": 40775,
    "catalogue": "ND",
    "meta": 0,
    "angle": "Nouveautés de marques et créativité",
    "merch": "Collections, saisons, promos, club et port bas",
    "weakness": "Irritants stock/SAV; transformation peu guidée",
    "persona": "Scrappeuse collectionneuse"
  },
  {
    "niche": "Scrap",
    "name": "Fée du Scrap",
    "domain": "feeduscrap.fr",
    "url": "https://www.feeduscrap.fr/",
    "classification": "MARQUE_ETABLIE / SPECIALISTE",
    "tech": "OASIS Commerce",
    "visits": null,
    "catalogue": "> 11 000 références revendiquées",
    "meta": null,
    "angle": "Album complet, expertise et communauté",
    "merch": "Kits signés, tutos, marques, thèmes, techniques",
    "weakness": "Port/ruptures; UX fonctionnelle",
    "persona": "Scrappeuse confirmée"
  },
  {
    "niche": "Scrap",
    "name": "Florilèges Design",
    "domain": "florilegesdesign.com",
    "url": "https://florilegesdesign.com/",
    "classification": "MARQUE_ETABLIE / FABRICANT",
    "tech": "PrestaShop",
    "visits": 2294,
    "catalogue": "ND",
    "meta": 0,
    "angle": "Collections françaises coordonnées",
    "merch": "Univers propriétaires, Muses, kits, tutos, revendeurs",
    "weakness": "Faible AOV unitaire; dépendance aux drops",
    "persona": "Passionnée fidèle aux collections"
  },
  {
    "niche": "Scrap",
    "name": "NotebookTherapy",
    "domain": "notebooktherapy.com",
    "url": "https://notebooktherapy.com/",
    "classification": "MARQUE_ETABLIE",
    "tech": "Shopify",
    "visits": 211567,
    "catalogue": "483 produits / 855 variantes",
    "meta": 253,
    "angle": "Rituel esthétique, calme et collection",
    "merch": "Capsules saisonnières, ASMR, éditions limitées",
    "weakness": "Modèle international à localiser; logistique non prouvée",
    "persona": "Millennial/Gen Z journaling et cadeau"
  },
  {
    "niche": "Perles",
    "name": "Perles & Co",
    "domain": "perlesandco.com",
    "url": "https://www.perlesandco.com/",
    "classification": "MARQUE_ETABLIE / SPECIALISTE",
    "tech": "ND",
    "visits": null,
    "catalogue": "> 2 500 tutoriels; catalogue profond",
    "meta": null,
    "angle": "Projet DIY de A à Z et contenu",
    "merch": "Tutoriels filtrés, coût/durée/niveau et liste matériel",
    "weakness": "Moat éditorial massif; abondance informationnelle",
    "persona": "Débutante à experte"
  },
  {
    "niche": "Perles",
    "name": "France Perles",
    "domain": "franceperles.com",
    "url": "https://www.franceperles.com/fr/",
    "classification": "MARQUE_ETABLIE",
    "tech": "PrestaShop",
    "visits": 54242,
    "catalogue": "> 10 000 références revendiquées",
    "meta": 0,
    "angle": "Pierres, origine et expertise matière",
    "merch": "Guides pierres, B2C/B2B, photos et transparence",
    "weakness": "Intention info; éviter allégations santé non prouvées",
    "persona": "Créatrice orientée matière"
  },
  {
    "niche": "Perles",
    "name": "Perles à Tout Va",
    "domain": "perlesatoutva.fr",
    "url": "https://perlesatoutva.fr/",
    "classification": "MARQUE_ETABLIE / OMNICANAL",
    "tech": "Shopify",
    "visits": null,
    "catalogue": "> 2 000 références revendiquées",
    "meta": null,
    "angle": "Semi-grossiste accessible et créatif",
    "merch": "Petits lots, pro, tarifs dégressifs, ateliers, XRF annoncé",
    "weakness": "Composition complète du bijou encore à guider",
    "persona": "Passionnée ou micro-marque"
  },
  {
    "niche": "Perles",
    "name": "I‑Perles",
    "domain": "i-perles.fr",
    "url": "https://i-perles.fr/",
    "classification": "MARQUE_ETABLIE",
    "tech": "Shopify",
    "visits": 19323,
    "catalogue": "2 000 produits / 10 024 variantes",
    "meta": 6,
    "angle": "Profondeur technique détail/gros",
    "merch": "Apprêts, fils, rocailles, argent 925, lots",
    "weakness": "Complexité pour la débutante",
    "persona": "Créatrice avancée / pro"
  },
  {
    "niche": "Perles",
    "name": "Perles Corner",
    "domain": "perlescorner.com",
    "url": "https://perlescorner.com/",
    "classification": "MARQUE_ETABLIE",
    "tech": "Shopify",
    "visits": 13785,
    "catalogue": "2 000 produits / 5 685 variantes",
    "meta": 0,
    "angle": "Expérience créative premium",
    "merch": "Pierres, Europe revendiquée, ateliers, tutoriels",
    "weakness": "Low ticket à rentabiliser par projets/réachat",
    "persona": "Créatrice urbaine premium"
  },
  {
    "niche": "Aquarium",
    "name": "Aquaplante",
    "domain": "aquaplante.fr",
    "url": "https://www.aquaplante.fr/",
    "classification": "MARQUE_ETABLIE / STOCKISTE",
    "tech": "PrestaShop",
    "visits": 123491,
    "catalogue": "> 475 plantes + matériel",
    "meta": 0,
    "angle": "Choix, prix et caution spécialiste",
    "merch": "Plantes, vivant, matériel, marques techniques, magasin",
    "weakness": "Qualité perçue/SAV et surcharge",
    "persona": "Aquariophile one-stop-shop"
  },
  {
    "niche": "Aquarium",
    "name": "Materiel-Aquatique",
    "domain": "materiel-aquatique.com",
    "url": "https://materiel-aquatique.com/",
    "classification": "SPECIALISTE / HYBRIDE POSSIBLE",
    "tech": "WooCommerce",
    "visits": null,
    "catalogue": "> 5 000 références revendiquées",
    "meta": 0,
    "angle": "Prix, choix et expédition France",
    "merch": "Matériel, plantes, entretien, bassin et entrepôt",
    "weakness": "Réputation polarisée; vivant/stock partenaire",
    "persona": "Acheteur prix et profondeur"
  },
  {
    "niche": "Aquarium",
    "name": "Skaii & Shrimps",
    "domain": "skaii-and-shrimps.fr",
    "url": "https://www.skaii-and-shrimps.fr/",
    "classification": "MARQUE_ETABLIE / STOCKISTE",
    "tech": "PrestaShop",
    "visits": 11258,
    "catalogue": "300 produits indexés",
    "meta": 1,
    "angle": "Technicité, stock et emballage",
    "merch": "Aquascaping, crevettes, premium, 99% stock revendiqué",
    "weakness": "Taxonomie lourde; statut Meta contradictoire",
    "persona": "Aquascaper/éleveur initié"
  },
  {
    "niche": "Aquarium",
    "name": "Shrimp-Delice",
    "domain": "shrimp-delice.fr",
    "url": "https://www.shrimp-delice.fr/",
    "classification": "SPECIALISTE_STOCK",
    "tech": "PrestaShop",
    "visits": 3654,
    "catalogue": "ND",
    "meta": 0,
    "angle": "Sélection crevettes par besoin",
    "merch": "Verticale étroite, contenu et consommables récurrents",
    "weakness": "Portée et preuve externe limitées",
    "persona": "Débutant/initié crevettes"
  },
  {
    "niche": "Aquarium",
    "name": "Buce Plant",
    "domain": "buceplant.com",
    "url": "https://buceplant.com/",
    "classification": "MARQUE_ETABLIE",
    "tech": "Shopify",
    "visits": 366868,
    "catalogue": "1 771 produits / 3 489 variantes",
    "meta": 43,
    "angle": "Aquascaping Super Shop et paysage naturel",
    "merch": "Plantes, hardscape, vivant, accessoires, inspiration",
    "weakness": "International; vivant/logistique à ne pas copier",
    "persona": "Aquascaper aspirant ou confirmé"
  }
];

const SEMRUSH_DOMAIN_META = {
  "perlesandco.com": [
    "Perles",
    "Moat de marque + tutoriels et guides larges"
  ],
  "franceperles.com": [
    "Perles",
    "Matières/pierres et paid search actif"
  ],
  "perlesatoutva.fr": [
    "Perles",
    "Collections transactionnelles précises"
  ],
  "rascol.com": [
    "Mercerie",
    "Autorité et catégories techniques"
  ],
  "craftine.com": [
    "Mercerie",
    "Box/kits + contenus débutants"
  ],
  "atelierdelacreation.com": [
    "Mercerie",
    "Mot générique mercerie + fort moat local"
  ],
  "scrapmalin.com": [
    "Scrap",
    "Trafic large et fortement bruité"
  ],
  "lafourmicreative.fr": [
    "Scrap",
    "Marque + catégories scrap"
  ],
  "feeduscrap.fr": [
    "Scrap",
    "Longue traîne très focalisée"
  ],
  "fenril.fr": [
    "Chien",
    "Longue traîne canicross/cani-VTT"
  ],
  "nonstopdogwear.com": [
    "Chien",
    "Trafic France surtout brandé/produits techniques"
  ],
  "boutiquechien.fr": [
    "Chien",
    "Catalogue énorme mais autorité quasi nulle"
  ],
  "aquaplante.fr": [
    "Aquarium",
    "Contenu, catalogue et paid search"
  ],
  "materiel-aquatique.com": [
    "Aquarium",
    "Catégories commerciales par matériel/volume"
  ],
  "skaii-and-shrimps.fr": [
    "Aquarium",
    "Marque + crevettes/aquascaping spécialisé"
  ]
};

const COMPETITOR_KEYWORD_ROWS = [
  [
    "Perles",
    "perlesandco.com",
    "perle",
    "I",
    "1",
    12100,
    "https://www.perlesandco.com/",
    "Head term + forte marque; intention mixte"
  ],
  [
    "Perles",
    "perlesandco.com",
    "scrapbooking",
    "I",
    "2",
    27100,
    "https://www.perlesandco.com/ressources/ft22121-le-scrapbooking-qu-est-ce-que-c-est.html",
    "Moat informationnel adjacent"
  ],
  [
    "Perles",
    "perlesandco.com",
    "jesmonite",
    "I",
    "1",
    8100,
    "https://www.perlesandco.com/ressources/ft39191-qu-est-ce-que-la-jesmonite.html",
    "Extension loisirs créatifs"
  ],
  [
    "Perles",
    "franceperles.com",
    "perle",
    "I",
    "7",
    12100,
    "https://www.franceperles.com/fr/",
    "Head term"
  ],
  [
    "Perles",
    "franceperles.com",
    "jade",
    "I",
    "10",
    22200,
    "https://www.franceperles.com/fr/409-jade",
    "Guide matière"
  ],
  [
    "Perles",
    "franceperles.com",
    "turquoise africaine",
    "I",
    "1",
    590,
    "https://www.franceperles.com/fr/turquoise-africaine-histoire-origine-vertus-composition-signification-et-rechargement.htm",
    "Longue traîne pierre"
  ],
  [
    "Perles",
    "perlesatoutva.fr",
    "breloque",
    "I",
    "1",
    4400,
    "https://perlesatoutva.fr/collections/breloques",
    "Collection commerciale"
  ],
  [
    "Perles",
    "perlesatoutva.fr",
    "perles miyuki",
    "I",
    "1",
    2400,
    "https://perlesatoutva.fr/collections/perles-miyuki",
    "Collection matière/marque"
  ],
  [
    "Perles",
    "perlesatoutva.fr",
    "grossiste en perles",
    "I",
    "3",
    5400,
    "https://perlesatoutva.fr/",
    "Segment pro"
  ],
  [
    "Mercerie",
    "rascol.com",
    "mannequin couture",
    "I",
    "1",
    8100,
    "https://www.rascol.com/mannequin-couture-reglable-c-110",
    "Collection technique"
  ],
  [
    "Mercerie",
    "rascol.com",
    "tricotin",
    "I/T",
    "2",
    14800,
    "https://www.rascol.com/tricotins-metiers-a-tisser-c-320",
    "Catégorie forte"
  ],
  [
    "Mercerie",
    "rascol.com",
    "aiguilles circulaires",
    "I",
    "1",
    1900,
    "https://www.rascol.com/aiguilles-a-tricoter-circulaires-c-519",
    "Collection transactionnelle"
  ],
  [
    "Mercerie",
    "craftine.com",
    "mercerie",
    "T",
    "4",
    27100,
    "https://www.craftine.com/mercerie.html",
    "Head term concurrentiel"
  ],
  [
    "Mercerie",
    "craftine.com",
    "kit couture",
    "I",
    "3",
    2900,
    "https://www.craftine.com/patrons-de-couture/kits-couture.html",
    "Projet/kit"
  ],
  [
    "Mercerie",
    "craftine.com",
    "kits couture",
    "I",
    "2",
    1300,
    "https://www.craftine.com/kits-couture.html",
    "Collection commerciale"
  ],
  [
    "Mercerie",
    "atelierdelacreation.com",
    "kit crochet",
    "C",
    "1",
    4400,
    "https://www.atelierdelacreation.com/253-kits-crochet",
    "Projet/kit"
  ],
  [
    "Mercerie",
    "atelierdelacreation.com",
    "couture pour debutants",
    "I",
    "1",
    2900,
    "https://www.atelierdelacreation.com/blog/99-comment-debuter-couture-tutoriels-gratuits-debutants",
    "Contenu acquisition débutante"
  ],
  [
    "Mercerie",
    "atelierdelacreation.com",
    "ecusson thermocollant",
    "I",
    "2",
    3600,
    "https://www.atelierdelacreation.com/164-ecussons-thermocollants",
    "Collection produit"
  ],
  [
    "Scrap",
    "scrapmalin.com",
    "scrapbooking",
    "I",
    "ND",
    27100,
    "https://blog.scrapmalin.com/2023/07/scrapbooking-comment-demarrer-le-scrapbooking/",
    "Trafic ciblé limité face au bruit"
  ],
  [
    "Scrap",
    "scrapmalin.com",
    "albums and scrapbooks",
    "I",
    "2",
    1600,
    "https://www.scrapmalin.com/store/album-papeterie/albums-kits-scrap/albums-de-scrapbooking",
    "Collection commerciale"
  ],
  [
    "Scrap",
    "scrapmalin.com",
    "stitch coloriage",
    "I",
    "ND",
    12100,
    "https://www.scrapmalin.com/product/bebe-stitch",
    "Exemple de bruit/licence"
  ],
  [
    "Scrap",
    "lafourmicreative.fr",
    "scrapbooking",
    "I",
    "3",
    27100,
    "https://www.lafourmicreative.fr/11-scrapbooking",
    "Catégorie cœur"
  ],
  [
    "Scrap",
    "lafourmicreative.fr",
    "papier pour scrapbooking",
    "I",
    "1",
    1000,
    "https://www.lafourmicreative.fr/115-papiers-scrapbooking",
    "Collection transactionnelle"
  ],
  [
    "Scrap",
    "lafourmicreative.fr",
    "album scrapbooking",
    "I",
    "2",
    1600,
    "https://www.lafourmicreative.fr/417-albums-scrap",
    "Collection transactionnelle"
  ],
  [
    "Scrap",
    "feeduscrap.fr",
    "dies",
    "I",
    "1",
    3600,
    "https://www.feeduscrap.fr/100-fee-du-scrap/dies-c2242.html",
    "Technique forte"
  ],
  [
    "Scrap",
    "feeduscrap.fr",
    "papier scrapbooking",
    "I",
    "1",
    1300,
    "https://www.feeduscrap.fr/100-fee-du-scrap/papiers-c2131.html",
    "Collection cœur"
  ],
  [
    "Scrap",
    "feeduscrap.fr",
    "kits for scrapbooking",
    "I",
    "1",
    590,
    "https://www.feeduscrap.fr/kits/kits-avec-tutoriels-c2042.html",
    "Longue traîne kit"
  ],
  [
    "Chien",
    "fenril.fr",
    "cani vtt attelage",
    "I",
    "3",
    5400,
    "https://www.fenril.fr/7-materiel-cani-vtt",
    "Discipline technique"
  ],
  [
    "Chien",
    "fenril.fr",
    "harnais canicross",
    "I",
    "2",
    2900,
    "https://www.fenril.fr/6-materiel-canicross",
    "Collection cœur"
  ],
  [
    "Chien",
    "fenril.fr",
    "laisse canicross",
    "C/I",
    "2",
    1300,
    "https://www.fenril.fr/6-materiel-canicross",
    "Composant du système"
  ],
  [
    "Chien",
    "nonstopdogwear.com",
    "chaussure chiens",
    "C/I",
    "1",
    1600,
    "https://www.nonstopdogwear.com/fr/collections/bottines",
    "Produit technique"
  ],
  [
    "Chien",
    "nonstopdogwear.com",
    "chausson chien",
    "I",
    "2",
    1900,
    "https://www.nonstopdogwear.com/fr/collections/bottines",
    "Synonyme capté"
  ],
  [
    "Chien",
    "nonstopdogwear.com",
    "harnais traction pour chien",
    "I",
    "3",
    480,
    "https://www.nonstopdogwear.com/fr/collections/harnais",
    "Longue traîne traction"
  ],
  [
    "Chien",
    "boutiquechien.fr",
    "panier chien xxl",
    "C",
    "17",
    1600,
    "https://boutiquechien.fr/products/panier-chien-xxl-indestructible",
    "Position faible"
  ],
  [
    "Chien",
    "boutiquechien.fr",
    "pulseur chien",
    "I",
    "30",
    5400,
    "https://boutiquechien.fr/collections/pulseur-chien",
    "Grande demande, position très faible"
  ],
  [
    "Chien",
    "boutiquechien.fr",
    "laisse mains libres pour chien",
    "I",
    "11",
    720,
    "https://boutiquechien.fr/collections/laisse-mains-libres-pour-chiens",
    "Longue traîne pertinente"
  ],
  [
    "Aquarium",
    "aquaplante.fr",
    "carpe koi",
    "I",
    "5",
    18100,
    "https://www.aquaplante.fr/10000920-carpes-koi-japonaises",
    "Vivant/bassin"
  ],
  [
    "Aquarium",
    "aquaplante.fr",
    "plantes aquaterrarium",
    "I/T",
    "1",
    1600,
    "https://www.aquaplante.fr/10001281-plantes-de-terrarium",
    "Collection spécialisée"
  ],
  [
    "Aquarium",
    "aquaplante.fr",
    "aquaplante",
    "N",
    "1",
    9900,
    "https://www.aquaplante.fr/",
    "Poids de marque"
  ],
  [
    "Aquarium",
    "materiel-aquatique.com",
    "pompe aquarium",
    "I",
    "1",
    5400,
    "https://materiel-aquatique.com/categorie-produit/materiel/pompe-aquarium/pompe-eau-aquarium/",
    "Collection commerciale forte"
  ],
  [
    "Aquarium",
    "materiel-aquatique.com",
    "meuble aquarium",
    "I",
    "1",
    4400,
    "https://materiel-aquatique.com/categorie-produit/aquarium/meuble-pour-aquarium/",
    "Collection forte"
  ],
  [
    "Aquarium",
    "materiel-aquatique.com",
    "aquascaping",
    "I",
    "1",
    2900,
    "https://materiel-aquatique.com/tutos-et-astuces/aquascaping-lart-de-creer-un-aquarium-naturel/",
    "Contenu top-funnel"
  ],
  [
    "Aquarium",
    "skaii-and-shrimps.fr",
    "crystal red shrimps",
    "I",
    "4",
    6600,
    "https://www.skaii-and-shrimps.fr/371-les-caridinas",
    "Spécialisation crevettes"
  ],
  [
    "Aquarium",
    "skaii-and-shrimps.fr",
    "racine aquarium",
    "I",
    "2",
    1000,
    "https://www.skaii-and-shrimps.fr/283-les-racines",
    "Hardscape commercial"
  ],
  [
    "Aquarium",
    "skaii-and-shrimps.fr",
    "kit co2 aquarium",
    "I",
    "3",
    880,
    "https://www.skaii-and-shrimps.fr/141-kits-co2",
    "Kit technique"
  ]
];

const PERSONA_ROWS = [
  [
    "Chien",
    "Propriétaire actif et protecteur",
    "Étayé provisoire — 10 points VOC",
    "Sortir/voyager sans chute, rupture, surchauffe ou mauvaise taille",
    "Nouvelle activité, voyage, chien senior/réactif",
    "Solidité, morphologie, chaleur, retours, règles transport",
    "Le prix ne garantit pas la solidité; dimensions cabine variables",
    "Diagnostic morphologie/usage + échange taille + preuves",
    "raw/persona-chien-mobilite/2026-08-08/reviews/community-voc.md"
  ],
  [
    "Aquarium",
    "Aquariophile projet anxieux de l’erreur",
    "Étayé provisoire — 10 points VOC",
    "Construire un bac beau et stable dont les composants fonctionnent ensemble",
    "Premier bac, upgrade, algues, mortalité",
    "Compatibilité, cyclage, qualité reçue, coût total, SAV",
    "Rapidité ≠ fraîcheur; difficulté affichée peut être fausse",
    "Matrice compatibilité + photo lot + protocole",
    "raw/persona-aquascaping/2026-08-08/reviews/community-voc.md"
  ],
  [
    "Mercerie",
    "Débutante orientée résultat",
    "Provisoire — 4+ sources",
    "Réussir un premier projet sans maîtriser le jargon",
    "Projet vu en vidéo, cadeau, réparation",
    "Mauvais outil/matière, patron complexe, surachat",
    "Est-ce vraiment débutant? Tout est-il inclus?",
    "Mini-kit + vidéo + quantité + support",
    "raw/voc-mercerie/2026-08-08/reviews/sources.md"
  ],
  [
    "Mercerie",
    "Créative sélective",
    "Provisoire — 4+ sources",
    "Trouver une combinaison précise sans kit imposé",
    "Projet personnel, matière/couleur précise",
    "Épaisseur, couleur, provenance, comparaison",
    "Prix sans preuve; matière impossible à apprécier",
    "Configurateur, échantillons, palettes, bundles modifiables",
    "raw/voc-mercerie/2026-08-08/reviews/sources.md"
  ],
  [
    "Scrap",
    "Gardienne d’un souvenir",
    "Provisoire — 4+ sources",
    "Transformer photos/événement en album ou cadeau cohérent",
    "Mariage, naissance, voyage, anniversaire",
    "Ne sait pas quoi acheter, couleur réelle, kit générique",
    "Le résultat semblera amateur ou dépareillé",
    "Événement → palette → format → niveau",
    "raw/voc-scrapbooking/2026-08-08/reviews/sources.md"
  ],
  [
    "Scrap",
    "Scrappeuse collectionneuse",
    "Provisoire — 4+ sources",
    "Obtenir nouveautés et compléments exacts",
    "Drop de collection, saison, rupture",
    "Stock faux, port, SAV, classement",
    "Alternative non compatible; retard",
    "Alertes, stock réservé, filtres collection/technique",
    "raw/voc-scrapbooking/2026-08-08/reviews/sources.md"
  ],
  [
    "Perles",
    "Débutante orientée bijou",
    "Provisoire — moyenne, 7+ sources",
    "Créer un premier bracelet/collier portable",
    "Envie DIY, cadeau, modèle vu en ligne",
    "Fil, trou, aiguille, pince, sertissage, quantité",
    "Tout inclus? Compatible? Budget total?",
    "Kit précis + palette + vidéo + recharges",
    "raw/voc-perles/2026-08-08/reviews/sources.md"
  ],
  [
    "Perles",
    "Créatrice régulière / micro-marque",
    "Provisoire — moyenne, 4+ signaux",
    "Produire de façon répétable avec qualité/coût maîtrisés",
    "Réassort, petite série, vente",
    "Rupture, lot irrégulier, finition, composition",
    "Authenticité, conformité, disponibilité future",
    "Lots gradués, fiches techniques, alternatives compatibles",
    "raw/voc-perles/2026-08-08/reviews/sources.md"
  ]
];

const DIFFERENTIATION_ROWS = [
  [
    "Scrapbooking & journaling",
    "Hypermarchés de fournitures vs marque-rituel internationale",
    "Préserver ses souvenirs et retrouver un moment calme",
    "Événement → ambiance → format → niveau → kit modulable",
    "Vues couleur/matière, liste exacte, stock réel, résultat fini",
    "Nombre de stickers et licences risquées",
    "Kit figé vs personnalisable; projet vs produit",
    "Propriété intellectuelle, AOV/port"
  ],
  [
    "Mobilité du chien",
    "Spécialistes performance + généraliste probable dropship",
    "Équipement juste selon morphologie et vraie vie",
    "Scénario → chien → fréquence → système compatible",
    "Guide 3 mesures, tests/attestations, délai/origine, retour taille",
    "Promesse sécurité générique ou conformité cabine universelle",
    "Diagnostic vs grille; échange taille",
    "Produits critiques, tailles, retours"
  ],
  [
    "Mercerie créative",
    "Autorités historiques et méga-catalogues",
    "Réussir du premier coup sans perdre son style",
    "Projet → niveau → durée → matière → quantité",
    "Projet testé, échantillon, compatibilité, tutoriel",
    "Copier 60k références ou tissu générique",
    "Mini-kit vs gros kit; matière visible",
    "Variantes, logistique matière, concurrence"
  ],
  [
    "Perles & bijoux",
    "Moat éditorial + grossistes techniques",
    "Choisissez le bijou; panier compatible calculé",
    "Bijou → style → mesure → métal → budget",
    "Macro, tolérances, composition, test disponible",
    "Allégations santé pierre ou matière non documentée",
    "Compatibilité garantie; panier essai vs pro",
    "Métaux, petites pièces, low ticket"
  ],
  [
    "Aquascaping",
    "Généralistes prix/profondeur + spécialistes crevettes",
    "Aquascape cohérent du premier coup",
    "Projet/volume → paramètres → composants → entretien",
    "Matrice SKU, photo lot, expédition, protocole",
    "Vivant/électricité sans gate; simple guerre de prix",
    "Kit compatible vs composants seuls",
    "Électricité, CO2, vivant, casse"
  ]
];

const SERP_ROWS = [
  ["Mercerie créative & arts du fil", "mercerie en ligne", "Oui", "Atelier de la Création; Mercerie Durand; Rascol; Craftine", "SERP transactionnelle et très spécialisée", "https://www.google.com/search?q=mercerie+en+ligne&hl=fr&gl=fr"],
  ["Mercerie créative & arts du fil", "kit broderie", "Oui", "Brodé Serré; Britney Pompadour; spécialistes broderie", "Sous-collection claire, forte promesse débutant", "https://www.google.com/search?q=kit+broderie&hl=fr&gl=fr"],
  ["Scrapbooking & journaling", "scrapbooking", "Oui", "Custodeco; La Fée du Scrap", "Mix informationnel/marchand; Shopping présent", "https://www.google.com/search?q=scrapbooking&hl=fr&gl=fr"],
  ["Scrapbooking & journaling", "album scrapbooking", "Oui", "La Fourmi Créative; boutiques spécialisées", "Intention produit plus nette que le head term", "https://www.google.com/search?q=album+scrapbooking&hl=fr&gl=fr"],
  ["Aquariophilie & aquascaping", "filtre aquarium", "Oui", "Aquael; Oase; spécialistes aquarium", "SERP très marchande et technique", "https://www.google.com/search?q=filtre+aquarium&hl=fr&gl=fr"],
  ["Aquariophilie & aquascaping", "aquascaping", "Oui", "Spécialistes aquascaping + guides", "Mix matériel, guides et services", "https://www.google.com/search?q=aquascaping&hl=fr&gl=fr"],
  ["Balade, transport & mobilité du chien", "harnais chien", "Oui", "Ruffwear; Milk&Pepper; comparateurs", "Forte concurrence mais intention produit massive", "https://www.google.com/search?q=harnais+chien&hl=fr&gl=fr"],
  ["Balade, transport & mobilité du chien", "sac transport chien", "Oui", "Boutiques spécialisées + comparateurs", "Sous-collections par poids et usage visibles", "https://www.google.com/search?q=sac+transport+chien&hl=fr&gl=fr"],
  ["Perles & création de bijoux", "perles bijoux", "Oui", "Perles&Co; Perles à Tout Va", "SERP partagée entre fournitures DIY et bijoux finis", "https://www.google.com/search?q=perles+bijoux&hl=fr&gl=fr"],
  ["Perles & création de bijoux", "kit création bijoux", "Oui", "Dreambeads; spécialistes DIY", "Intention kit nette, propice au panier moyen", "https://www.google.com/search?q=kit+cr%C3%A9ation+bijoux&hl=fr&gl=fr"],
];

const TREND_URL = "https://trends.google.com/trends/explore?date=today%205-y&geo=FR&q=mercerie%2Cscrapbooking%2Caquariophilie%2Cperles%2Charnais%20chien";
const SEMRUSH_URL = "https://fr.semrush.com/analytics/keywordoverview/?db=fr";

const workbook = Workbook.create();
const summarySheet = workbook.worksheets.add("Synthèse");
const collectionsSheet = workbook.worksheets.add("Arborescence");
const productsSheet = workbook.worksheets.add("Produits");
const qaSheet = workbook.worksheets.add("Sourcing QA");
const evidenceSheet = workbook.worksheets.add("SERP & Trends");
const methodSheet = workbook.worksheets.add("Méthode & limites");
const priorityCompetitionSheet = workbook.worksheets.add("Priorités concurrence");
const competitorsSheet = workbook.worksheets.add("Concurrents");
const semrushCompetitionSheet = workbook.worksheets.add("SEMrush concurrence");
const personasSheet = workbook.worksheets.add("Personas & VOC");
const differentiationSheet = workbook.worksheets.add("Différenciation");

const COLORS = {
  navy: "#16324F",
  blue: "#2F75B5",
  green: "#2E8B57",
  lightGreen: "#E2F0D9",
  amber: "#F4B183",
  lightAmber: "#FFF2CC",
  red: "#C00000",
  lightRed: "#FCE4D6",
  lightBlue: "#DDEBF7",
  gray: "#F2F2F2",
  white: "#FFFFFF",
  border: "#D9E2F3",
};

function colLetter(number) {
  let value = number;
  let output = "";
  while (value > 0) {
    const remainder = (value - 1) % 26;
    output = String.fromCharCode(65 + remainder) + output;
    value = Math.floor((value - 1) / 26);
  }
  return output;
}

function titleBand(sheet, title, subtitle, endColumn) {
  sheet.showGridLines = false;
  sheet.mergeCells(`A1:${endColumn}1`);
  sheet.getRange(`A1:${endColumn}1`).values = [[title]];
  sheet.getRange(`A1:${endColumn}1`).format = {
    fill: COLORS.navy,
    font: { bold: true, color: COLORS.white, size: 16 },
    verticalAlignment: "center",
  };
  sheet.getRange("A1").format.rowHeight = 32;
  sheet.mergeCells(`A2:${endColumn}2`);
  sheet.getRange(`A2:${endColumn}2`).values = [[subtitle]];
  sheet.getRange(`A2:${endColumn}2`).format = {
    fill: COLORS.lightBlue,
    font: { color: COLORS.navy, italic: true, size: 10 },
    wrapText: true,
    verticalAlignment: "center",
  };
  sheet.getRange("A2").format.rowHeight = 34;
}

function addTable(sheet, startRow, headers, rows, name) {
  const endRow = startRow + rows.length;
  const endCol = colLetter(headers.length);
  sheet.getRange(`A${startRow}:${endCol}${endRow}`).values = [headers, ...rows];
  const table = sheet.tables.add(`A${startRow}:${endCol}${endRow}`, true, name);
  table.style = "TableStyleMedium2";
  table.showFilterButton = true;
  return { table, endRow, endCol };
}

function median(values) {
  const numbers = values.filter(Number.isFinite).sort((a, b) => a - b);
  if (!numbers.length) return null;
  const middle = Math.floor(numbers.length / 2);
  return numbers.length % 2 ? numbers[middle] : (numbers[middle - 1] + numbers[middle]) / 2;
}

function excelText(value) {
  return value ? String(value) : "";
}

function displayUtc(value) {
  if (!value) return "";
  const [datePart, rawTime = ""] = String(value).replace("+00:00", "").split("T");
  const [year, month, day] = datePart.split("-");
  return `${day}/${month}/${year} • ${rawTime.slice(0, 8)} UTC`;
}

function decodeDelivery(value) {
  return String(value || "").replaceAll("ao&ucirc;t", "août");
}

const probeByNiche = Object.fromEntries(probes.probes.map((row) => [row.niche, row]));
const productsByNiche = Object.groupBy(curated.products, (row) => row.niche);
const summaryRows = SUMMARY.map((row) => {
  const products = productsByNiche[row.niche] || [];
  const usable = products.filter((item) => item.decision === "RETENIR_API_À_VÉRIFIER").length;
  const prices = products.map((item) => Number(item.price)).filter(Number.isFinite);
  return [
    row.rank,
    row.niche,
    row.verdict,
    row.score,
    row.cleanVolume,
    row.grossVolume,
    row.cleanVolume - 40000,
    row.trendAverage,
    row.trendChange,
    row.serp,
    products.length,
    usable,
    median(prices),
    probeByNiche[row.niche]?.ok ? "VARIANTE + FRET FR OK" : "NON VALIDÉ",
    row.risk,
    row.next,
  ];
});

titleBand(
  summarySheet,
  "5 niches Kraken — France — 8 août 2026",
  "Lecture : volumes SEMrush FR observés, SERP/Trends contrôlés et sourcing AliExpress read-only. Tous les verdicts restent conditionnels jusqu'à validation fournisseur, conformité et economics.",
  "P",
);
addTable(
  summarySheet,
  4,
  ["Rang", "Niche", "Verdict", "Score /100", "Volume nettoyé", "Volume brut ciblé", "Écart vs 40k", "Indice Trends moyen", "Tendance récente", "SERP", "Candidats API", "Pertinence moyenne/élevée", "Prix API médian €", "Probe exact", "Risque principal", "Prochaine action"],
  summaryRows,
  "SummaryTable",
);
summarySheet.freezePanes.freezeRows(4);
summarySheet.getRange("A4:P9").format.wrapText = true;
summarySheet.getRange("D5:D9").setNumberFormat("0");
summarySheet.getRange("E5:G9").setNumberFormat("#,##0");
summarySheet.getRange("I5:I9").setNumberFormat("0.0%");
summarySheet.getRange("M5:M9").setNumberFormat("0.00 €");
summarySheet.getRange("E5:E9").conditionalFormats.add("dataBar", { color: COLORS.blue, gradient: true });
summarySheet.getRange("I5:I9").conditionalFormats.addCustom("=I5<0", { font: { color: COLORS.red }, fill: COLORS.lightRed });
summarySheet.getRange("I5:I9").conditionalFormats.addCustom("=I5>=0", { font: { color: COLORS.green }, fill: COLORS.lightGreen });
summarySheet.getRange("A4:P9").format.autofitRows();
const summaryWidths = [7, 34, 18, 10, 15, 16, 14, 17, 15, 28, 14, 22, 16, 22, 42, 48];
summaryWidths.forEach((width, index) => {
  summarySheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});
const volumeChart = summarySheet.charts.add("bar", {
  chartType: "bar",
  title: "Volume mensuel nettoyé par niche",
  hasLegend: false,
});
volumeChart.title = "Volume mensuel nettoyé par niche";
volumeChart.hasLegend = false;
volumeChart.setPosition("R3", "Y18");
const volumeSeries = volumeChart.series.add("Volume nettoyé");
volumeSeries.categoryFormula = "'Synthèse'!$B$5:$B$9";
volumeSeries.formula = "'Synthèse'!$E$5:$E$9";
volumeSeries.fill = COLORS.blue;

const productCountByKey = new Map();
for (const product of curated.products) {
  const key = `${product.niche}|||${product.keyword_fr}`;
  productCountByKey.set(key, (productCountByKey.get(key) || 0) + 1);
}
const collectionRows = api.results.map((row) => {
  const volume = VOLUMES[row.keyword_fr] ?? 0;
  let tier = "LONGUE TRAÎNE / PDP";
  let gate = "< 300 : ne pas ouvrir seule au lancement";
  if (volume >= 1000) {
    tier = "CŒUR";
    gate = "GO collection cœur";
  } else if (volume >= 500) {
    tier = "SECONDAIRE";
    gate = "GO collection secondaire";
  } else if (volume >= 300) {
    tier = "TOLÉRANCE ±200";
    gate = "GO conditionnel / regrouper";
  }
  const key = `${row.niche}|||${row.keyword_fr}`;
  return [
    `${row.niche} > ${row.parent_collection} > ${row.collection}`,
    row.niche,
    row.parent_collection,
    row.collection,
    row.keyword_fr,
    volume,
    tier,
    gate,
    productCountByKey.get(key) || 0,
    row.query_en,
    "SEMrush FR — 2026-08-08",
    displayUtc(row.checked_at_utc),
  ];
});
titleBand(
  collectionsSheet,
  "Arborescence des cinq boutiques",
  "Le volume est celui du mot-clé exact affecté à la collection. Règle Kraken mise à jour : cœur ≥ 1 000; secondaire 500–1 000; tolérance à partir de 300; les termes plus faibles servent de sous-collection/PDP et ne justifient pas seuls une collection de lancement.",
  "L",
);
addTable(
  collectionsSheet,
  4,
  ["Chemin", "Niche", "Collection parente", "Collection", "Mot-clé FR", "Volume mensuel FR", "Niveau", "Décision architecture", "Produits candidats", "Requête API", "Source volume", "Contrôlé UTC"],
  collectionRows,
  "CollectionsTable",
);
collectionsSheet.freezePanes.freezeRows(4);
collectionsSheet.freezePanes.freezeColumns(2);
collectionsSheet.getRange("A4:L104").format.wrapText = true;
collectionsSheet.getRange("F5:F104").setNumberFormat("#,##0");
collectionsSheet.getRange("L5:L104").setNumberFormat("@");
collectionsSheet.getRange("F5:F104").conditionalFormats.add("colorScale", {
  criteria: [
    { type: "lowestValue", color: COLORS.lightRed },
    { type: "percentile", value: 50, color: COLORS.lightAmber },
    { type: "highestValue", color: COLORS.lightGreen },
  ],
});
[52, 32, 27, 26, 30, 16, 20, 30, 18, 30, 24, 22].forEach((width, index) => {
  collectionsSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

const productsSorted = [...curated.products].sort((a, b) =>
  a.niche.localeCompare(b.niche, "fr") ||
  a.parent_collection.localeCompare(b.parent_collection, "fr") ||
  a.collection.localeCompare(b.collection, "fr") ||
  (b.relevance_score - a.relevance_score) ||
  String(a.product_id).localeCompare(String(b.product_id)),
);
const productRows = productsSorted.map((row, index) => [
  index + 1,
  row.niche,
  row.parent_collection,
  row.collection,
  row.keyword_fr,
  VOLUMES[row.keyword_fr] ?? 0,
  row.title,
  Number(row.price) || null,
  row.currency || "EUR",
  Number(row.rating) || null,
  row.orders || "",
  row.relevance,
  row.decision,
  row.risk,
  row.listing_url,
  row.image || "",
  `ID-${row.product_id}`,
  displayUtc(row.checked_at_utc),
]);
titleBand(
  productsSheet,
  `${curated.products.length} produits candidats — liens AliExpress de contrôle`,
  "Le volume correspond au mot-clé produit/collection ayant servi à trouver le listing, pas au titre AliExpress complet. API_SEARCH_MATCH = listing trouvé; seules les cinq lignes documentées dans Sourcing QA ont une variante et un fret France vérifiés.",
  "R",
);
addTable(
  productsSheet,
  4,
  ["#", "Niche", "Collection parente", "Collection", "Mot-clé produit FR", "Volume FR", "Titre AliExpress", "Prix API", "Devise", "Note", "Commandes", "Pertinence lexicale", "Décision", "Risque / contrôle", "Lien AliExpress", "Image", "Product ID", "Contrôlé UTC"],
  productRows,
  "ProductsTable",
);
productsSheet.freezePanes.freezeRows(4);
productsSheet.freezePanes.freezeColumns(2);
productsSheet.getRange(`A4:R${productRows.length + 4}`).format.wrapText = true;
productsSheet.getRange(`F5:F${productRows.length + 4}`).setNumberFormat("#,##0");
productsSheet.getRange(`H5:H${productRows.length + 4}`).setNumberFormat("0.00");
productsSheet.getRange(`J5:J${productRows.length + 4}`).setNumberFormat("0.0");
productsSheet.getRange(`Q5:Q${productRows.length + 4}`).setNumberFormat("@");
productsSheet.getRange(`R5:R${productRows.length + 4}`).setNumberFormat("@");
productsSheet.getRange(`L5:L${productRows.length + 4}`).dataValidation = { rule: { type: "list", values: ["ÉLEVÉE", "MOYENNE", "FAIBLE"] } };
productsSheet.getRange(`M5:M${productRows.length + 4}`).dataValidation = { rule: { type: "list", values: ["RETENIR_API_À_VÉRIFIER", "À_VÉRIFIER_PERTINENCE", "EXCLURE_IP"] } };
productsSheet.getRange(`L5:M${productRows.length + 4}`).conditionalFormats.addCustom('=$L5="FAIBLE"', { fill: COLORS.lightAmber, font: { color: "#7F6000" } });
productsSheet.getRange(`M5:M${productRows.length + 4}`).conditionalFormats.addCustom('=$M5="RETENIR_API_À_VÉRIFIER"', { fill: COLORS.lightGreen, font: { color: COLORS.green } });
[6, 34, 26, 25, 28, 13, 78, 11, 9, 9, 12, 18, 26, 50, 52, 48, 20, 22].forEach((width, index) => {
  productsSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

const qaRows = probes.probes.map((row) => {
  const result = row.exact?.result || {};
  const option = result.freight?.options?.[0] || {};
  return [
    row.niche,
    `ID-${row.product_id}`,
    row.ok ? "OK" : "ÉCHEC",
    (row.selected_properties || []).join(" | "),
    result.exact_sku?.sku_id ? `SKU-${result.exact_sku.sku_id}` : "",
    Number(result.exact_sku?.offer_sale_price) || null,
    result.exact_sku?.currency || "",
    Number(result.exact_sku?.stock) || null,
    option.shipping_fee || "",
    decodeDelivery(option.delivery_date),
    option.tracking === true ? "Oui" : "Non",
    option.ship_from_country || "",
    `https://www.aliexpress.com/item/${row.product_id}.html`,
    displayUtc(result.checked_at_utc),
  ];
});
titleBand(
  qaSheet,
  "Sourcing QA — un probe exact par niche",
  "Ces cinq lignes démontrent le chemin complet API : listing → variantes → SKU exact → stock → fret France. Elles ne généralisent pas ce statut aux 627 autres candidats.",
  "N",
);
addTable(
  qaSheet,
  4,
  ["Niche", "Product ID", "Statut", "Propriétés exactes", "SKU ID", "Prix exact", "Devise", "Stock", "Fret France", "Livraison annoncée", "Suivi", "Expédié de", "Lien", "Contrôlé UTC"],
  qaRows,
  "ExactProbeTable",
);
qaSheet.freezePanes.freezeRows(4);
qaSheet.getRange("A4:N9").format.wrapText = true;
qaSheet.getRange("F5:F9").setNumberFormat("0.00");
qaSheet.getRange("B5:B9").setNumberFormat("@");
qaSheet.getRange("E5:E9").setNumberFormat("@");
qaSheet.getRange("N5:N9").setNumberFormat("@");
[34, 20, 12, 46, 22, 12, 9, 10, 15, 22, 10, 13, 52, 22].forEach((width, index) => {
  qaSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

titleBand(
  evidenceSheet,
  "SERP et Google Trends",
  "Shopping a été observé sur les dix requêtes testées. Google Trends est un indice relatif : il sert à lire la direction, jamais à remplacer les volumes SEMrush.",
  "H",
);
addTable(
  evidenceSheet,
  4,
  ["Niche", "Requête SERP", "Shopping", "Acteurs visibles", "Lecture", "URL SERP"],
  SERP_ROWS,
  "SerpTable",
);
const trendRows = SUMMARY.map((row) => [row.niche, row.trendAverage, row.trendChange, "France — cinq ans", TREND_URL]);
addTable(
  evidenceSheet,
  17,
  ["Niche", "Indice moyen comparé", "Variation 52 points récents vs initiaux", "Période", "URL Trends"],
  trendRows,
  "TrendsTable",
);
evidenceSheet.freezePanes.freezeRows(4);
evidenceSheet.getRange("A4:F14").format.wrapText = true;
evidenceSheet.getRange("A17:E22").format.wrapText = true;
evidenceSheet.getRange("C18:C22").setNumberFormat("0.0%");
[34, 28, 12, 46, 45, 76].forEach((width, index) => {
  evidenceSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

titleBand(
  methodSheet,
  "Méthode, sources et limites",
  "Ce classeur sépare l'observé, le calculé et ce qui reste à valider avant toute mutation commerciale.",
  "D",
);
const methodRows = [
  ["[OBSERVÉ] Volumes", "SEMrush France, base FR, 8 août 2026. Volume moyen mensuel du mot-clé exact.", SEMRUSH_URL, "Les totaux sont des sommes d'expressions distinctes, non des utilisateurs dédupliqués."],
  ["[CALCULÉ] Volume nettoyé", "Exclusion des termes manifestement ambigus : album photo/sticker pour Scrapbooking; aquarium seul pour Aquariophilie; perle au singulier pour Bijoux.", "", "Le brut ciblé reste affiché à côté du nettoyé."],
  ["[RÈGLE] Demande boutique", "30 000 minimum; 40 000 zone de confort. Collection cœur ≥ 1 000; secondaire 500–1 000; tolérance ±200.", "Corpus privé La Méthode Kraken", "Aucun seuil universel imposé aux PDP."],
  ["[OBSERVÉ] SERP", "Dix SERP Google France contrôlées : présence Shopping et boutiques spécialisées dans les cinq niches.", "Voir onglet SERP & Trends", "Une SERP est un instantané et doit être rafraîchie avant lancement."],
  ["[OBSERVÉ] Trends", "France, cinq ans; indices comparatifs et variation directionnelle.", TREND_URL, "Google Trends n'est pas un volume absolu."],
  ["[OBSERVÉ] AliExpress", `100 recherches API; destination FR; tri commandes; ${curated.products.length} IDs uniques sélectionnés après dédoublonnage et exclusions IP.`, "AliExpress Open Platform / AE-Dropshipper via VPS autorisé", "Le moteur peut renvoyer du bruit : les lignes FAIBLE sont à contrôler ou supprimer."],
  ["[OBSERVÉ] Probe exact", "Un produit par niche validé jusqu'au SKU, stock et option de fret France.", "Voir onglet Sourcing QA", "Les autres liens restent au statut API_SEARCH_MATCH."],
  ["[MANQUANT] Economics", "Coût rendu France exact, marge, frais Shopify/Ads, retours et SAV pour chaque SKU.", "", "À calculer après shortlist humaine de 20–30 produits par niche."],
  ["[MANQUANT] Conformité", "Documents CE/REACH, contact matière, sécurité animale, étanchéité et preuves fournisseurs selon la niche.", "", "Aucune allégation ne doit être publiée sans preuve."],
  ["[NON AUTORISÉ ICI] Mutations", "Aucune création Shopify, import DSers, activation GMC ou dépense Google Ads n'a été faite.", "", "Le classeur est un livrable de recherche et de contrôle."],
];
addTable(
  methodSheet,
  4,
  ["Statut", "Définition / preuve", "Source", "Limite / action suivante"],
  methodRows,
  "MethodTable",
);
methodSheet.freezePanes.freezeRows(4);
methodSheet.getRange("A4:D14").format.wrapText = true;
[32, 92, 70, 72].forEach((width, index) => {
  methodSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});
methodSheet.getRange("A5:A14").conditionalFormats.addCustom('=LEFT($A5,10)="[MANQUANT]"', { fill: COLORS.lightAmber, font: { color: "#7F6000", bold: true } });
methodSheet.getRange("A5:A14").conditionalFormats.addCustom('=LEFT($A5,9)="[OBSERVÉ]"', { fill: COLORS.lightGreen, font: { color: COLORS.green, bold: true } });

const semrushByDomain = Object.fromEntries(semrush.domains.map((row) => [row.domain, row]));
const competitorRows = COMPETITOR_BASE_ROWS.map((row) => {
  const seo = semrushByDomain[row.domain];
  return [
    row.niche,
    row.name,
    row.domain,
    row.url,
    row.classification,
    row.tech,
    row.visits,
    row.catalogue,
    row.meta,
    seo?.summary?.organic_traffic || "ND",
    seo?.summary?.organic_keywords || "ND",
    row.angle,
    row.merch,
    row.weakness,
    row.persona,
    "08/08/2026",
  ];
});

titleBand(
  priorityCompetitionSheet,
  "Priorités après étude concurrentielle",
  "Classement du meilleur premier test opérable, pas de la taille absolue du marché. Les cinq niches restent conditionnelles jusqu’au sourcing exact, à la conformité et aux economics.",
  "G",
);
addTable(
  priorityCompetitionSheet,
  4,
  ["Priorité", "Niche", "Volume FR nettoyé", "Lecture concurrence", "Right to win testable", "Gate", "Condition suivante"],
  PRIORITY_COMPETITION_ROWS,
  "PriorityCompetitionTable",
);
const crossPatternRows = [
  ["Résultat avant produit", "Chaque leader relie plusieurs composants à un usage ou projet.", "Construire la navigation autour du job client."],
  ["Low ticket = panier", "Composants, consommables et accessoires isolés ne portent pas le CAC.", "Bundles, lots, recharges et seuil de livraison."],
  ["Compatibilité", "Taille, matière, dimensions ou système créent le principal risque perçu.", "Diagnostic, calculateur et garantie bornée."],
  ["Preuve spécifique", "Une preuve générique ne répond pas aux peurs de la niche.", "Protocole matière/taille/lot/composition par catégorie."],
  ["Contenu marchand", "Le meilleur contenu fabrique une nomenclature ou un panier.", "Tutoriel → liste exacte → substitutions compatibles."],
  ["Volume ≠ autorité", "Boutiquechien : 1 308 produits mais 151 visites organiques FR estimées.", "Prioriser cohérence, interliens et demande réelle."],
];
addTable(
  priorityCompetitionSheet,
  12,
  ["Pattern", "Observation", "Conséquence pour la boutique"],
  crossPatternRows,
  "CrossPatternsTable",
);
priorityCompetitionSheet.freezePanes.freezeRows(4);
priorityCompetitionSheet.getRange("A4:G9").format.wrapText = true;
priorityCompetitionSheet.getRange("A12:C18").format.wrapText = true;
priorityCompetitionSheet.getRange("C5:C9").setNumberFormat("#,##0");
priorityCompetitionSheet.getRange("F5:F9").conditionalFormats.addCustom('=$F5="PRIORITÉ TEST"', { fill: COLORS.lightGreen, font: { color: COLORS.green, bold: true } });
[10, 38, 18, 48, 52, 22, 46].forEach((width, index) => {
  priorityCompetitionSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

titleBand(
  competitorsSheet,
  "25 concurrents — catalogue, marketing et signaux de traction",
  "BrandSearch et SEMrush fournissent des estimations tierces. Shopify est un indice technique, jamais une preuve de dropshipping. PROBABLE_DROPSHIP reste sans fournisseur confirmé.",
  "P",
);
addTable(
  competitorsSheet,
  4,
  ["Niche", "Concurrent", "Domaine", "URL", "Classification", "Technologie", "Visites BrandSearch", "Catalogue", "Meta actives", "Trafic organique FR", "Mots-clés organiques", "Angle / positionnement", "Merchandising", "Faiblesse / whitespace", "Persona inféré", "Snapshot"],
  competitorRows,
  "CompetitorsTable",
);
competitorsSheet.freezePanes.freezeRows(4);
competitorsSheet.freezePanes.freezeColumns(2);
competitorsSheet.getRange(`A4:P${competitorRows.length + 4}`).format.wrapText = true;
competitorsSheet.getRange(`G5:G${competitorRows.length + 4}`).setNumberFormat("#,##0");
competitorsSheet.getRange(`I5:I${competitorRows.length + 4}`).setNumberFormat("#,##0");
competitorsSheet.getRange(`E5:E${competitorRows.length + 4}`).conditionalFormats.addCustom('=ISNUMBER(SEARCH("PROBABLE_DROPSHIP",$E5))', { fill: COLORS.lightAmber, font: { color: "#7F6000", bold: true } });
[14, 25, 26, 42, 34, 18, 20, 34, 14, 20, 20, 42, 52, 52, 38, 14].forEach((width, index) => {
  competitorsSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

const semrushSummaryRows = semrush.domains.map((row) => {
  const meta = SEMRUSH_DOMAIN_META[row.domain] || ["Non classé", "À interpréter"] ;
  return [
    meta[0],
    row.domain,
    Number(row.summary.authority_score) || null,
    row.summary.organic_traffic,
    row.summary.organic_keywords,
    row.summary.paid_traffic,
    row.summary.paid_keywords,
    row.summary.referring_domains,
    row.summary.backlinks,
    meta[1],
    row.positions_url,
  ];
});
titleBand(
  semrushCompetitionSheet,
  "SEMrush France — concurrents et mots-clés visibles",
  "Snapshot du 8 août 2026 : Domain Overview et premières lignes visibles d’Organic Research. Ce n’est pas un export exhaustif ni une donnée analytics marchand.",
  "K",
);
addTable(
  semrushCompetitionSheet,
  4,
  ["Niche", "Domaine", "AS", "Trafic organique", "Mots-clés organiques", "Trafic payant", "Mots-clés payants", "Domaines référents", "Backlinks", "Lecture", "URL SEMrush"],
  semrushSummaryRows,
  "SemrushSummaryTable",
);
addTable(
  semrushCompetitionSheet,
  23,
  ["Niche", "Domaine", "Mot-clé", "Intention", "Position", "Volume FR", "URL positionnée", "Interprétation"],
  COMPETITOR_KEYWORD_ROWS,
  "SemrushKeywordsTable",
);
semrushCompetitionSheet.freezePanes.freezeRows(4);
semrushCompetitionSheet.freezePanes.freezeColumns(2);
semrushCompetitionSheet.getRange(`A4:K${semrushSummaryRows.length + 4}`).format.wrapText = true;
semrushCompetitionSheet.getRange(`A23:H${COMPETITOR_KEYWORD_ROWS.length + 23}`).format.wrapText = true;
semrushCompetitionSheet.getRange(`C5:C${semrushSummaryRows.length + 4}`).setNumberFormat("0");
semrushCompetitionSheet.getRange(`F24:F${COMPETITOR_KEYWORD_ROWS.length + 23}`).setNumberFormat("#,##0");
semrushCompetitionSheet.getRange(`F24:F${COMPETITOR_KEYWORD_ROWS.length + 23}`).conditionalFormats.add("dataBar", { color: COLORS.blue, gradient: true });
[15, 28, 10, 18, 20, 17, 18, 20, 18, 48, 72].forEach((width, index) => {
  semrushCompetitionSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

titleBand(
  personasSheet,
  "Personas et voix du client",
  "Personas provisoires issus d’avis et communautés publiques. Ils sont étayés, mais restent à confirmer par entretiens français et tests de concept de première main.",
  "I",
);
addTable(
  personasSheet,
  4,
  ["Niche", "Persona", "Confiance", "Job", "Déclencheurs", "Pains", "Objections", "Offre attendue", "Source VOC"],
  PERSONA_ROWS,
  "PersonasTable",
);
personasSheet.freezePanes.freezeRows(4);
personasSheet.freezePanes.freezeColumns(2);
personasSheet.getRange(`A4:I${PERSONA_ROWS.length + 4}`).format.wrapText = true;
[16, 34, 30, 48, 40, 52, 46, 52, 66].forEach((width, index) => {
  personasSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

titleBand(
  differentiationSheet,
  "Différenciation à tester — cinq concepts",
  "Chaque promesse est une hypothèse de travail. La preuve, le sourcing exact, l’économie et la conformité doivent être construits avant publication.",
  "H",
);
addTable(
  differentiationSheet,
  4,
  ["Niche", "Pattern concurrentiel", "Promesse proposée", "Architecture", "Preuve nécessaire", "À ne pas copier", "Premier test", "Risque principal"],
  DIFFERENTIATION_ROWS,
  "DifferentiationTable",
);
differentiationSheet.freezePanes.freezeRows(4);
differentiationSheet.getRange("A4:H9").format.wrapText = true;
[34, 48, 52, 56, 58, 48, 48, 42].forEach((width, index) => {
  differentiationSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

await fs.mkdir(previewDir, { recursive: true });

const keyInspection = await workbook.inspect({
  kind: "table",
  range: "Synthèse!A1:P12",
  include: "values,formulas",
  tableMaxRows: 12,
  tableMaxCols: 16,
  maxChars: 12000,
});
await fs.writeFile(path.join(outputDir, "inspection-synthese.ndjson"), keyInspection.ndjson, "utf8");

const competitionInspection = await workbook.inspect({
  kind: "table",
  range: "Priorités concurrence!A1:G18",
  include: "values,formulas",
  tableMaxRows: 20,
  tableMaxCols: 8,
  maxChars: 16000,
});
await fs.writeFile(path.join(outputDir, "inspection-concurrence.ndjson"), competitionInspection.ndjson, "utf8");

const formulaErrors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 300 },
  summary: "final formula error scan",
});
await fs.writeFile(path.join(outputDir, "formula-error-scan.ndjson"), formulaErrors.ndjson, "utf8");

const previewRanges = {
  "Synthèse": "A1:Y18",
  "Arborescence": "A1:L32",
  "Produits": "A1:R28",
  "Sourcing QA": "A1:N10",
  "SERP & Trends": "A1:H23",
  "Méthode & limites": "A1:D15",
  "Priorités concurrence": "A1:G18",
  "Concurrents": "A1:P29",
  "SEMrush concurrence": "A1:K32",
  "Personas & VOC": "A1:I12",
  "Différenciation": "A1:H9",
};
for (const [sheetName, range] of Object.entries(previewRanges)) {
  const preview = await workbook.render({ sheetName, range, scale: 0.85, format: "png" });
  const bytes = new Uint8Array(await preview.arrayBuffer());
  await fs.writeFile(path.join(previewDir, `${sheetName.replaceAll(/[^a-zA-Z0-9]+/g, "-")}.png`), bytes);
}

const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(outputPath);
await fs.rm(`${outputPath}.inspect.ndjson`, { force: true });

console.log(JSON.stringify({ outputPath, previewDir, sheets: Object.keys(previewRanges), productRows: productRows.length }, null, 2));
