import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  SpreadsheetFile,
  Workbook,
} from "/Users/Hakim/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs";

const runDir = path.dirname(fileURLToPath(import.meta.url));
const outputDir = path.resolve(runDir, "../../outputs/2026-08-08-kraken-catalogue-v1");
const outputPath = path.join(outputDir, "5-niches-kraken-france-2026-08-08.xlsx");
const previewDir = path.join(outputDir, "previews");

const api = JSON.parse(await fs.readFile(path.join(runDir, "aliexpress-search-results.json"), "utf8"));
const curated = JSON.parse(await fs.readFile(path.join(runDir, "curated-products.json"), "utf8"));
const probes = JSON.parse(await fs.readFile(path.join(runDir, "representative-exact-probes.json"), "utf8"));

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
