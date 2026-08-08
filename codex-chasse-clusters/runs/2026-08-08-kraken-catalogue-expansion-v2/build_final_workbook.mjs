import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const artifactToolCandidates = [
  process.env.CODEX_ARTIFACT_TOOL_PATH,
  path.join(os.homedir(), ".cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs"),
].filter(Boolean);
let artifactToolPath;
for (const candidate of artifactToolCandidates) {
  try {
    await fs.access(candidate);
    artifactToolPath = candidate;
    break;
  } catch {
    // Continue vers le candidat suivant.
  }
}
if (!artifactToolPath) {
  throw new Error("artifact-tool introuvable; definir CODEX_ARTIFACT_TOOL_PATH vers artifact_tool.mjs");
}
const { SpreadsheetFile, Workbook } = await import(pathToFileURL(artifactToolPath).href);

const runDir = path.dirname(fileURLToPath(import.meta.url));
const repoDir = path.resolve(runDir, "../../..");
const outputDir = path.resolve(runDir, "../../outputs/2026-08-08-kraken-catalogue-expansion-v2");
const outputPath = path.join(outputDir, "5-niches-kraken-arborescence-catalogue-verifie-2026-08-08.xlsx");
const previewDir = path.join(outputDir, "previews");

const catalogue = JSON.parse(await fs.readFile(path.join(runDir, "final-catalogue-reviewed.json"), "utf8"));
const validation = JSON.parse(await fs.readFile(path.join(runDir, "final-catalogue-gate-report.json"), "utf8"));
const volumes = JSON.parse(await fs.readFile(path.join(runDir, "keyword-volumes-fr.json"), "utf8"));
const concepts = JSON.parse(await fs.readFile(path.join(runDir, "competitor-concepts-merged.json"), "utf8"));
const conceptValidation = JSON.parse(await fs.readFile(path.join(runDir, "competitor-concepts-validation.json"), "utf8"));
const previousWorkbookBuilderSource = await fs.readFile(
  path.resolve(runDir, "../2026-08-08-kraken-catalogue-v1/build_competitor_workbook.mjs"),
  "utf8",
);

function extractJsonArrayConstant(name) {
  const match = previousWorkbookBuilderSource.match(new RegExp(`const ${name} = (\\[.*?\\n\\]);`, "s"));
  if (!match) throw new Error(`Tableau ${name} introuvable dans le run v1`);
  return JSON.parse(match[1]);
}

const PRIORITY_COMPETITION_ROWS = extractJsonArrayConstant("PRIORITY_COMPETITION_ROWS");
const COMPETITOR_BASE_ROWS = extractJsonArrayConstant("COMPETITOR_BASE_ROWS");
const PERSONA_ROWS = extractJsonArrayConstant("PERSONA_ROWS");
const DIFFERENTIATION_ROWS = extractJsonArrayConstant("DIFFERENTIATION_ROWS");

await fs.mkdir(outputDir, { recursive: true });
await fs.mkdir(previewDir, { recursive: true });

const RANKING = [
  {
    rank: 1,
    niche: "Balade, transport & mobilité du chien",
    verdict: "GO CONDITIONNEL",
    angle: "Mobilité sûre France-first par scénario, morphologie et usage outdoor",
    competition: "Spécialistes techniques forts; Boutiquechien probable dropship, confiance moyenne",
    risk: "Charge, tailles et allégations de sécurité",
  },
  {
    rank: 2,
    niche: "Mercerie créative & arts du fil",
    verdict: "GO CONDITIONNEL",
    angle: "Boutique project-first, kits personnalisables et preuve matière/quantité",
    competition: "Autorités historiques, stockistes et méga-catalogues",
    risk: "Concurrence installée; vérité matière et dimensions",
  },
  {
    rank: 3,
    niche: "Scrapbooking & journaling",
    verdict: "GO CONDITIONNEL",
    angle: "Souvenir-first, kits modulaires et navigation par événement/résultat",
    competition: "Spécialistes établis; aucune preuve solide de dropshipper dominant",
    risk: "Licences, motifs protégés et produits chimiques",
  },
  {
    rank: 4,
    niche: "Perles & création de bijoux",
    verdict: "GO CONDITIONNEL",
    angle: "Compatibilité, composition et projets guidés plutôt que simple catalogue",
    competition: "Grossistes/spécialistes très installés; aucun dropshipper validé",
    risk: "Nickel, plomb, cadmium et allégations de pierres/métaux",
  },
  {
    rank: 5,
    niche: "Aquariophilie & aquascaping",
    verdict: "GO CONDITIONNEL",
    angle: "Aquascape guidé par résultat, compatibilité et preuve qualité réelle",
    competition: "Spécialistes techniques forts; aucun dropshipper probable établi",
    risk: "Électricité, étanchéité, CO2 et bien-être animal",
  },
];

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

function normalizeText(value) {
  return String(value || "")
    .normalize("NFD")
    .replaceAll(/\p{Diacritic}/gu, "")
    .toLowerCase()
    .replaceAll(/[^a-z0-9]+/g, " ")
    .trim();
}

function slugify(value) {
  return normalizeText(value).replaceAll(" ", "-");
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
  sheet.getRange("A2").format.rowHeight = 42;
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

function numberValue(value) {
  const parsed = Number(value);
  return Number.isFinite(parsed) ? parsed : null;
}

function volumeTier(volume) {
  if (volume >= 1000) return "CŒUR";
  if (volume >= 500) return "SECONDAIRE";
  if (volume >= 300) return "REVUE 300–499";
  return "PDP / REPLI";
}

const workbook = Workbook.create();
const summarySheet = workbook.worksheets.add("Synthèse");
const architectureSheet = workbook.worksheets.add("Arborescence");
const productsSheet = workbook.worksheets.add("Produits SEO");
const sourcingSheet = workbook.worksheets.add("Sourcing AliExpress");
const competitionSheet = workbook.worksheets.add("Preuves concurrence");
const volumeSheet = workbook.worksheets.add("Volumes SEMrush");
const qaSheet = workbook.worksheets.add("Contrôles QA");
const methodSheet = workbook.worksheets.add("Méthode & limites");
const prioritiesSheet = workbook.worksheets.add("Priorités concurrence");
const profilesSheet = workbook.worksheets.add("Profils concurrents");
const personasSheet = workbook.worksheets.add("Personas");
const differentiationSheet = workbook.worksheets.add("Différenciation");

const products = [...catalogue.products].sort((a, b) =>
  (RANKING.find((row) => row.niche === a.niche)?.rank || 99) - (RANKING.find((row) => row.niche === b.niche)?.rank || 99)
  || b.seo.collection_volume - a.seo.collection_volume
  || a.seo.collection_keyword.localeCompare(b.seo.collection_keyword, "fr")
  || a.catalogue_rank - b.catalogue_rank,
);

const summaryRows = RANKING.map((row) => {
  const root = catalogue.root_keywords[row.niche];
  return [
    row.rank,
    row.niche,
    row.verdict,
    catalogue.clean_totals_by_niche[row.niche],
    null,
    null,
    catalogue.reference_targets_by_niche[row.niche],
    null,
    null,
    null,
    null,
    root.keyword,
    root.volume,
    row.competition,
    row.angle,
    row.risk,
  ];
});
titleBand(
  summarySheet,
  "5 niches Kraken — arborescence SEO et catalogue sourceable",
  "France, 8 août 2026. Catalogue relu ligne par ligne après collecte API. L’objectif de référence, le livré et l’écart restent séparés; chaque listing demeure soumis à validation du SKU, du fret France, de la conformité et de la marge.",
  "P",
);
const summaryTable = addTable(
  summarySheet,
  4,
  ["Rang", "Niche", "Verdict", "Volume commercial nettoyé", "Écart vs 30k", "Produits livrés", "Objectif de référence", "Écart catalogue", "Équivalents concurrents", "Découvertes API", "Collections", "Mot-clé général", "Volume général", "Concurrence", "Angle différenciant", "Risque principal"],
  summaryRows,
  "SummaryFinalTable",
);
for (let row = 5; row <= summaryTable.endRow; row += 1) {
  summarySheet.getRange(`E${row}`).formulas = [[`=D${row}-30000`]];
  summarySheet.getRange(`F${row}`).formulas = [[`=COUNTIF('Produits SEO'!$B:$B,B${row})`]];
  summarySheet.getRange(`H${row}`).formulas = [[`=F${row}-G${row}`]];
  summarySheet.getRange(`I${row}`).formulas = [[`=COUNTIFS('Produits SEO'!$B:$B,B${row},'Produits SEO'!$S:$S,"EQUIVALENT_CONCURRENT_API")`]];
  summarySheet.getRange(`J${row}`).formulas = [[`=COUNTIFS('Produits SEO'!$B:$B,B${row},'Produits SEO'!$S:$S,"DECOUVERTE_FAMILLE_SEO_API")`]];
  summarySheet.getRange(`K${row}`).formulas = [[`=COUNTIF('Arborescence'!$B:$B,B${row})-1`]];
}
summarySheet.freezePanes.freezeRows(4);
summarySheet.freezePanes.freezeColumns(2);
summarySheet.getRange(`A4:P${summaryTable.endRow}`).format.wrapText = true;
summarySheet.getRange(`D5:M${summaryTable.endRow}`).setNumberFormat("#,##0");
summarySheet.getRange(`D5:D${summaryTable.endRow}`).conditionalFormats.add("dataBar", { color: COLORS.blue, gradient: true });
summarySheet.getRange(`F5:F${summaryTable.endRow}`).conditionalFormats.addCustom("=$F5>=$G5", { fill: COLORS.lightGreen, font: { color: COLORS.green, bold: true } });
summarySheet.getRange(`F5:F${summaryTable.endRow}`).conditionalFormats.addCustom("=$F5<$G5", { fill: COLORS.lightRed, font: { color: COLORS.red, bold: true } });
[7, 38, 18, 20, 14, 14, 16, 14, 20, 18, 13, 28, 16, 46, 52, 48].forEach((width, index) => {
  summarySheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

const architectureRows = [];
for (const ranking of RANKING) {
  const root = catalogue.root_keywords[ranking.niche];
  architectureRows.push([
    "ACCUEIL",
    ranking.niche,
    "/",
    root.keyword.charAt(0).toUpperCase() + root.keyword.slice(1),
    root.keyword,
    root.volume,
    "MOT-CLÉ GÉNÉRAL",
    catalogue.clean_totals_by_niche[ranking.niche],
    products.filter((row) => row.niche === ranking.niche).length,
    "Accueil / ancre générale",
  ]);
  const collections = catalogue.collections
    .filter((row) => row.niche === ranking.niche)
    .sort((a, b) => b.collection_volume - a.collection_volume || a.collection_keyword.localeCompare(b.collection_keyword, "fr"));
  for (const collection of collections) {
    architectureRows.push([
      "COLLECTION SEO",
      ranking.niche,
      `/collections/${slugify(collection.collection_keyword)}`,
      collection.collection_title,
      collection.collection_keyword,
      collection.collection_volume,
      volumeTier(collection.collection_volume),
      catalogue.clean_totals_by_niche[ranking.niche],
      collection.product_count,
      collection.collection_volume >= 1000
        ? "Collection cœur indexable"
        : (collection.collection_volume >= 500 ? "Collection secondaire indexable" : "Collection revue / repli mesuré"),
    ]);
  }
}
titleBand(
  architectureSheet,
  "Arborescence des cinq boutiques",
  "Chaque accueil et chaque collection possède une expression commerciale mesurée. Seuils Kraken : boutique ≥ 30k nettoyés (40k confort), collection cœur ≥ 1 000, secondaire ≥ 500, zone de revue 300–499.",
  "J",
);
const architectureTable = addTable(
  architectureSheet,
  4,
  ["Type", "Niche", "URL proposée", "Titre", "Mot-clé business", "Volume mensuel FR", "Niveau", "Volume boutique nettoyé", "Nb produits", "Décision"],
  architectureRows,
  "ArchitectureFinalTable",
);
architectureSheet.freezePanes.freezeRows(4);
architectureSheet.freezePanes.freezeColumns(2);
architectureSheet.getRange(`A4:J${architectureTable.endRow}`).format.wrapText = true;
architectureSheet.getRange(`F5:F${architectureTable.endRow}`).setNumberFormat("#,##0");
architectureSheet.getRange(`H5:I${architectureTable.endRow}`).setNumberFormat("#,##0");
architectureSheet.getRange(`F5:F${architectureTable.endRow}`).conditionalFormats.add("colorScale", {
  criteria: [
    { type: "lowestValue", color: COLORS.lightAmber },
    { type: "percentile", value: 50, color: COLORS.lightBlue },
    { type: "highestValue", color: COLORS.lightGreen },
  ],
});
[18, 38, 42, 50, 30, 17, 20, 21, 13, 38].forEach((width, index) => {
  architectureSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

const productRows = products.map((row, index) => [
  index + 1,
  row.niche,
  row.seo.product_title,
  row.seo.product_keyword,
  row.seo.product_volume,
  row.seo.collection_title,
  row.seo.collection_keyword,
  row.seo.collection_volume,
  row.root_keyword,
  row.root_volume,
  `/products/${slugify(row.seo.product_keyword)}-${row.aliexpress.product_id}`,
  row.concept_fr_normalized,
  row.competitor || "MANQUANT",
  row.competitor_product_url || "MANQUANT",
  row.aliexpress.listing_url,
  `ID-${row.aliexpress.product_id}`,
  row.aliexpress.title,
  row.competitor_evidence_status,
  row.candidate_origin,
  row.risk_flag,
  row.supplier_evidence_status,
  row.manual_review?.reason || "ACCEPTÉ SANS COMMENTAIRE",
]);
titleBand(
  productsSheet,
  `${products.length} produits SEO relus`,
  "Le mot-clé business et son volume se trouvent immédiatement à côté du titre. Toutes les lignes ont passé la revue humaine; l’objectif de référence et les déficits restent visibles dans la synthèse.",
  "V",
);
const productTable = addTable(
  productsSheet,
  4,
  ["#", "Niche", "Titre produit SEO", "Mot-clé produit FR", "Volume produit FR", "Collection", "Mot-clé collection FR", "Volume collection FR", "Mot-clé général", "Volume général FR", "URL produit proposée", "Concept normalisé", "Concurrent", "Lien concurrent", "Lien AliExpress", "Product ID", "Titre fournisseur", "Preuve concurrente", "Origine catalogue", "Risque / contrôle", "Statut fournisseur", "Motif revue humaine"],
  productRows,
  "ProductsFinalTable",
);
productsSheet.freezePanes.freezeRows(4);
productsSheet.freezePanes.freezeColumns(2);
productsSheet.getRange(`A4:V${productTable.endRow}`).format.wrapText = true;
productsSheet.getRange(`E5:E${productTable.endRow}`).setNumberFormat("#,##0");
productsSheet.getRange(`H5:H${productTable.endRow}`).setNumberFormat("#,##0");
productsSheet.getRange(`J5:J${productTable.endRow}`).setNumberFormat("#,##0");
productsSheet.getRange(`P5:P${productTable.endRow}`).setNumberFormat("@");
productsSheet.getRange(`E5:E${productTable.endRow}`).conditionalFormats.add("dataBar", { color: COLORS.blue, gradient: true });
productsSheet.getRange(`S5:S${productTable.endRow}`).conditionalFormats.addCustom('=$S5="EQUIVALENT_CONCURRENT_API"', { fill: COLORS.lightGreen, font: { color: COLORS.green } });
productsSheet.getRange(`S5:S${productTable.endRow}`).conditionalFormats.addCustom('=$S5="DECOUVERTE_FAMILLE_SEO_API"', { fill: COLORS.lightAmber, font: { color: "#7F6000" } });
[6, 38, 74, 30, 16, 32, 30, 18, 26, 16, 46, 42, 25, 54, 54, 22, 78, 26, 30, 52, 34, 64].forEach((width, index) => {
  productsSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

const sourcingRows = products.map((row, index) => [
  index + 1,
  row.niche,
  row.seo.product_keyword,
  row.seo.product_volume,
  row.aliexpress.product_id,
  row.aliexpress.title,
  numberValue(row.aliexpress.price),
  row.aliexpress.currency || "EUR",
  numberValue(row.aliexpress.rating),
  row.aliexpress.orders || "",
  row.aliexpress.listing_url,
  row.aliexpress.image || "",
  row.aliexpress.matched_query || "",
  numberValue(row.aliexpress.match?.score),
  row.aliexpress.match?.semantic_ok ? "OK" : "MANQUANT",
  row.aliexpress.match?.supplier_quality_ok ? "OK" : "MANQUANT",
  row.candidate_origin,
  row.risk_flag,
  row.supplier_evidence_status,
  row.manual_review?.reason || "ACCEPTÉ SANS COMMENTAIRE",
]);
titleBand(
  sourcingSheet,
  "Sourcing AliExpress — preuve read-only",
  "Pertinence produit et prix présents, ID unique, déduplication puis revue humaine exhaustive. Le statut distingue les listings déjà qualifiés par note/commandes de ceux qui restent à vérifier; fret, SKU, conformité et economics restent manquants.",
  "T",
);
const sourcingTable = addTable(
  sourcingSheet,
  4,
  ["#", "Niche", "Mot-clé produit", "Volume FR", "Product ID", "Titre AliExpress", "Prix API", "Devise", "Note", "Commandes", "Lien AliExpress", "Image", "Requête API", "Score sémantique", "Pertinence", "Qualité API", "Origine", "Risque / contrôle", "Statut fournisseur", "Motif revue humaine"],
  sourcingRows,
  "SourcingFinalTable",
);
sourcingSheet.freezePanes.freezeRows(4);
sourcingSheet.freezePanes.freezeColumns(2);
sourcingSheet.getRange(`A4:T${sourcingTable.endRow}`).format.wrapText = true;
sourcingSheet.getRange(`D5:D${sourcingTable.endRow}`).setNumberFormat("#,##0");
sourcingSheet.getRange(`E5:E${sourcingTable.endRow}`).setNumberFormat("@");
sourcingSheet.getRange(`G5:G${sourcingTable.endRow}`).setNumberFormat("0.00");
sourcingSheet.getRange(`I5:I${sourcingTable.endRow}`).setNumberFormat("0.0");
sourcingSheet.getRange(`N5:N${sourcingTable.endRow}`).setNumberFormat("0.0");
sourcingSheet.getRange(`O5:P${sourcingTable.endRow}`).conditionalFormats.addCustom('=O5="OK"', { fill: COLORS.lightGreen, font: { color: COLORS.green } });
[6, 38, 30, 14, 22, 80, 12, 9, 9, 13, 54, 48, 38, 17, 12, 15, 30, 52, 34, 64].forEach((width, index) => {
  sourcingSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

const selectedConceptKeys = new Set(products.filter((row) => row.candidate_origin === "EQUIVALENT_CONCURRENT_API").map((row) => `${row.niche}|||${row.concept_key}`));
const competitionRows = concepts.concepts.map((row, index) => [
  index + 1,
  row.niche,
  row.competitor,
  row.competitor_domain,
  row.competitor_collection,
  row.competitor_product_title,
  row.competitor_product_url || row.source_url,
  row.concept_fr_normalized,
  row.keyword_fr_candidate,
  row.aliexpress_query_en,
  row.evidence_status,
  selectedConceptKeys.has(`${row.niche}|||${row.concept_key}`) ? "OUI" : "NON / NON RETENU",
  row.distinctness_basis,
]);
titleBand(
  competitionSheet,
  `${competitionRows.length} concepts issus des catalogues concurrents`,
  "Les fiches concurrentes sont conservées comme preuve et inspiration catalogue. OBSERVE_CONCURRENT signifie PDP observée; EQUIVALENT_DERIVE signifie que la marque/le modèle ont été neutralisés pour produire une fonction sourceable.",
  "M",
);
const competitionTable = addTable(
  competitionSheet,
  4,
  ["#", "Niche", "Concurrent", "Domaine", "Collection concurrente", "Produit concurrent", "Lien concurrent", "Concept normalisé", "Mot-clé candidat", "Requête AliExpress EN", "Statut preuve", "Dans catalogue final", "Base de distinction"],
  competitionRows,
  "CompetitionEvidenceTable",
);
competitionSheet.freezePanes.freezeRows(4);
competitionSheet.freezePanes.freezeColumns(2);
competitionSheet.getRange(`A4:M${competitionTable.endRow}`).format.wrapText = true;
competitionSheet.getRange(`L5:L${competitionTable.endRow}`).conditionalFormats.addCustom('=$L5="OUI"', { fill: COLORS.lightGreen, font: { color: COLORS.green } });
[6, 38, 27, 28, 32, 66, 54, 46, 42, 46, 24, 20, 72].forEach((width, index) => {
  competitionSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

const volumeRows = volumes.keywords
  .sort((a, b) => (a.niches[0] || "").localeCompare(b.niches[0] || "", "fr") || b.volume - a.volume || a.keyword.localeCompare(b.keyword, "fr"))
  .map((row, index) => [
    index + 1,
    row.niches.join("; "),
    row.keyword,
    row.volume,
    row.volume > 0 ? "OUI" : "NON",
    volumeTier(row.volume),
    row.database,
    row.observed_at,
    row.status,
    row.source_run,
  ]);
titleBand(
  volumeSheet,
  "Banque de 100 mots-clés SEMrush France",
  "Valeurs observées le 8 août 2026 et réutilisées sans re-mesure le même jour. Les volumes de produits réutilisés sur plusieurs PDP ne sont jamais additionnés pour recalculer le potentiel de la boutique.",
  "J",
);
const volumeTable = addTable(
  volumeSheet,
  4,
  ["#", "Niche", "Mot-clé", "Volume mensuel FR", "Utilisable PDP", "Niveau collection", "Base", "Observé le", "Statut", "Run source"],
  volumeRows,
  "SemrushVolumesTable",
);
volumeSheet.freezePanes.freezeRows(4);
volumeSheet.freezePanes.freezeColumns(2);
volumeSheet.getRange(`A4:J${volumeTable.endRow}`).format.wrapText = true;
volumeSheet.getRange(`D5:D${volumeTable.endRow}`).setNumberFormat("#,##0");
volumeSheet.getRange(`D5:D${volumeTable.endRow}`).conditionalFormats.add("dataBar", { color: COLORS.blue, gradient: true });
[6, 38, 34, 18, 15, 21, 9, 14, 24, 36].forEach((width, index) => {
  volumeSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

const uniqueProductIds = new Set(products.map((row) => `${row.niche}|||${row.aliexpress.product_id}`)).size;
const uniqueTitles = new Set(products.map((row) => `${row.niche}|||${normalizeText(row.seo.product_title)}`)).size;
const referenceTargetTotal = Object.values(catalogue.reference_targets_by_niche).reduce((sum, value) => sum + Number(value || 0), 0);
const qualifiedListingCount = products.filter((row) => row.supplier_evidence_status === "LISTING_QUALIFIE_NOTE_COMMANDES").length;
const qaRows = [
  ["Catalogue", "PDP vs objectif de référence", referenceTargetTotal, products.length, products.length >= referenceTargetTotal ? "OK" : "PARTIEL", "Les déficits ne sont jamais remplis avec des lignes non relues"],
  ["Catalogue", "IDs AliExpress uniques par niche", products.length, uniqueProductIds, uniqueProductIds === products.length ? "OK" : "ÉCHEC", "Aucun listing compté deux fois dans une niche"],
  ["SEO", "Volumes produit strictement positifs", products.length, products.filter((row) => row.seo.product_volume > 0).length, products.every((row) => row.seo.product_volume > 0) ? "OK" : "ÉCHEC", "Chaque PDP possède un mot-clé mesuré"],
  ["SEO", "Volumes collection strictement positifs", products.length, products.filter((row) => row.seo.collection_volume > 0).length, products.every((row) => row.seo.collection_volume > 0) ? "OK" : "ÉCHEC", "Chaque collection possède un mot-clé mesuré"],
  ["SEO", "Titres produit uniques par niche", products.length, uniqueTitles, uniqueTitles === products.length ? "OK" : "ÉCHEC", "Titre SEO = mot-clé + descriptif fournisseur"],
  ["Revue", "Décision humaine ACCEPT", products.length, products.filter((row) => row.manual_review?.decision === "ACCEPT").length, products.every((row) => row.manual_review?.decision === "ACCEPT") ? "OK" : "ÉCHEC", "Chaque ligne livrée a été relue"],
  ["Concurrence", "Concepts concurrents acceptés", concepts.concepts.length, conceptValidation.accepted_after_dedup, conceptValidation.accepted_after_dedup === concepts.concepts.length ? "OK" : "REVUE", "Couleurs, tailles, conditionnements, marques et modèles neutralisés"],
  ["Sourcing", "Mot-clé directement prouvé", products.length, products.filter((row) => row.aliexpress.final_keyword_match?.semantic_ok).length, products.every((row) => row.aliexpress.final_keyword_match?.semantic_ok) ? "OK" : "ÉCHEC", "Le listing décrit le produit lui-même, pas une ancre transitive"],
  ["Sourcing", "Listings déjà qualifiés", products.length, qualifiedListingCount, "INFORMATION", "Les autres lignes restent explicitement à vérifier"],
];
titleBand(
  qaSheet,
  "Contrôles automatiques",
  "Ces contrôles valident la structure du classeur et le gate de recherche. Ils ne remplacent pas la vérification manuelle du SKU, du prix rendu, de la livraison, de la conformité, de la marge ou des droits de marque.",
  "F",
);
const qaTable = addTable(
  qaSheet,
  4,
  ["Domaine", "Contrôle", "Attendu", "Observé", "Résultat", "Note"],
  qaRows,
  "QAFinalTable",
);
qaSheet.freezePanes.freezeRows(4);
qaSheet.getRange(`A4:F${qaTable.endRow}`).format.wrapText = true;
qaSheet.getRange(`E5:E${qaTable.endRow}`).conditionalFormats.addCustom('=$E5="OK"', { fill: COLORS.lightGreen, font: { color: COLORS.green, bold: true } });
qaSheet.getRange(`E5:E${qaTable.endRow}`).conditionalFormats.addCustom('=$E5="ÉCHEC"', { fill: COLORS.lightRed, font: { color: COLORS.red, bold: true } });
qaSheet.getRange(`E5:E${qaTable.endRow}`).conditionalFormats.addCustom('=$E5="PARTIEL"', { fill: COLORS.lightAmber, font: { color: "#7F6000", bold: true } });
[16, 46, 14, 14, 14, 80].forEach((width, index) => {
  qaSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

const methodRows = [
  ["[OBSERVÉ]", "SEMrush France", "100 expressions mesurées le 08/08/2026; base fr", "Volume à côté de chaque mot-clé dans le classeur"],
  ["[OBSERVÉ]", "Concurrence", `${concepts.concepts.length} concepts issus de catalogues publics concurrents`, "PDP/collection source conservée avec statut de preuve"],
  ["[OBSERVÉ]", "AliExpress", "API officielle via VPS autorisé, destination FR, lecture seule", "ID, titre, prix, note, commandes et lien conservés"],
  ["[FAIT]", "Déduplication", "ID unique + signature sans couleur/taille/quantité + contrôle des quasi-variantes", "Les variantes simples ne comptent jamais comme nouveau produit"],
  ["[FAIT]", "Revue humaine", `${catalogue.manual_review.reviewed_count} candidats relus; ${catalogue.manual_review.accepted_count} acceptés`, "Un rejet n'est pas remplacé automatiquement pour remplir un quota"],
  ["[FAIT]", "Architecture", `Accueil + collections + ${products.length} PDP relues`, "Chaque niveau possède un mot-clé business mesuré"],
  ["[PARTIEL]", "Profondeur catalogue", `Objectif de référence ${referenceTargetTotal}; livré ${products.length}`, "Écart détaillé par niche dans la synthèse"],
  ["[RÈGLE]", "Seuil boutique", "30 000 recherches commerciales nettoyées; 40 000 confort", "Ne pas additionner les mêmes volumes répétés sur les PDP"],
  ["[RÈGLE]", "Seuil collection", "Cœur ≥ 1 000; secondaire ≥ 500; revue 300–499", "Les expressions plus faibles utilisent une collection de repli mesurée"],
  ["[RÈGLE]", "Prix", "Aucun plancher artificiel à 150 €", "Low-ticket autorisé si profondeur, panier, marge et CAC sont viables"],
  ["[MANQUANT]", "SKU exact", "Variante, stock et caractéristiques exactes", "À valider avant import Shopify/DSers"],
  ["[MANQUANT]", "Fret France", "Prix rendu, délai et méthode de livraison", "À valider SKU par SKU"],
  ["[MANQUANT]", "Conformité", "CE/GPSR, matériaux, sécurité, propriété intellectuelle", "Gate obligatoire selon la catégorie"],
  ["[MANQUANT]", "Economics", "Prix cible, marge de contribution, panier et CAC d'équilibre", "Aucune décision de lancement dans ce classeur"],
  ["[AUTORISATION]", "Mutations", "Aucune mutation Shopify, DSers, GMC ou Ads", "Classeur de recherche et d'architecture uniquement"],
];
titleBand(
  methodSheet,
  "Méthode, statuts et limites",
  "Observé, dérivé et manquant restent séparés. La présence d’un listing ou d’un concurrent ne prouve pas la demande rentable, la conformité ou la disponibilité durable.",
  "D",
);
const methodTable = addTable(
  methodSheet,
  4,
  ["Statut", "Sujet", "Règle / preuve", "Conséquence"],
  methodRows,
  "MethodFinalTable",
);
methodSheet.freezePanes.freezeRows(4);
methodSheet.getRange(`A4:D${methodTable.endRow}`).format.wrapText = true;
methodSheet.getRange(`A5:A${methodTable.endRow}`).conditionalFormats.addCustom('=LEFT($A5,9)="[OBSERVÉ]"', { fill: COLORS.lightGreen, font: { color: COLORS.green, bold: true } });
methodSheet.getRange(`A5:A${methodTable.endRow}`).conditionalFormats.addCustom('=LEFT($A5,10)="[MANQUANT]"', { fill: COLORS.lightAmber, font: { color: "#7F6000", bold: true } });
[18, 30, 88, 78].forEach((width, index) => {
  methodSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

titleBand(
  prioritiesSheet,
  "Priorités après étude concurrentielle",
  "Classement du meilleur premier test opérable, pas de la taille absolue du marché. Les cinq niches restent conditionnelles jusqu’à la validation du SKU exact, de la conformité et des economics.",
  "G",
);
const prioritiesTable = addTable(
  prioritiesSheet,
  4,
  ["Priorité", "Niche", "Volume FR nettoyé", "Lecture concurrence", "Right to win testable", "Gate", "Condition suivante"],
  PRIORITY_COMPETITION_ROWS,
  "PriorityCompetitionFinalTable",
);
prioritiesSheet.freezePanes.freezeRows(4);
prioritiesSheet.getRange(`A4:G${prioritiesTable.endRow}`).format.wrapText = true;
prioritiesSheet.getRange(`C5:C${prioritiesTable.endRow}`).setNumberFormat("#,##0");
prioritiesSheet.getRange(`F5:F${prioritiesTable.endRow}`).conditionalFormats.addCustom('=$F5="PRIORITÉ TEST"', { fill: COLORS.lightGreen, font: { color: COLORS.green, bold: true } });
[10, 38, 18, 50, 54, 22, 48].forEach((width, index) => {
  prioritiesSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

const profileRows = COMPETITOR_BASE_ROWS.map((row) => [
  row.niche,
  row.name,
  row.domain,
  row.url,
  row.classification,
  row.tech,
  row.visits,
  row.catalogue,
  row.meta,
  row.angle,
  row.merch,
  row.weakness,
  row.persona,
  "08/08/2026",
]);
titleBand(
  profilesSheet,
  `${profileRows.length} profils concurrents`,
  "BrandSearch et les catalogues publics fournissent des estimations tierces. Shopify reste un indice technique, jamais une preuve de dropshipping; aucune équivalence fournisseur exacte n’est déduite de la technologie seule.",
  "N",
);
const profilesTable = addTable(
  profilesSheet,
  4,
  ["Niche", "Concurrent", "Domaine", "URL", "Classification", "Technologie", "Visites estimées", "Catalogue", "Meta actives", "Angle", "Merchandising", "Faiblesse / whitespace", "Persona inféré", "Snapshot"],
  profileRows,
  "CompetitorProfilesFinalTable",
);
profilesSheet.freezePanes.freezeRows(4);
profilesSheet.freezePanes.freezeColumns(2);
profilesSheet.getRange(`A4:N${profilesTable.endRow}`).format.wrapText = true;
profilesSheet.getRange(`G5:G${profilesTable.endRow}`).setNumberFormat("#,##0");
profilesSheet.getRange(`I5:I${profilesTable.endRow}`).setNumberFormat("#,##0");
profilesSheet.getRange(`E5:E${profilesTable.endRow}`).conditionalFormats.addCustom('=ISNUMBER(SEARCH("PROBABLE_DROPSHIP",$E5))', { fill: COLORS.lightAmber, font: { color: "#7F6000", bold: true } });
[15, 27, 28, 44, 36, 18, 18, 36, 14, 44, 54, 54, 40, 14].forEach((width, index) => {
  profilesSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

titleBand(
  personasSheet,
  "Personas et voix du client",
  "Personas provisoires issus d’avis et communautés publiques. Ils sont étayés mais restent à confirmer par entretiens français et tests de concept de première main.",
  "I",
);
const personasTable = addTable(
  personasSheet,
  4,
  ["Niche", "Persona", "Confiance", "Job", "Déclencheurs", "Pains", "Objections", "Offre attendue", "Source VOC"],
  PERSONA_ROWS,
  "PersonasFinalTable",
);
personasSheet.freezePanes.freezeRows(4);
personasSheet.freezePanes.freezeColumns(2);
personasSheet.getRange(`A4:I${personasTable.endRow}`).format.wrapText = true;
[16, 36, 30, 50, 42, 54, 48, 54, 68].forEach((width, index) => {
  personasSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

titleBand(
  differentiationSheet,
  "Différenciation à tester",
  "Chaque promesse est une hypothèse de travail. La preuve, le sourcing exact, l’économie et la conformité doivent être construits avant publication.",
  "H",
);
const differentiationTable = addTable(
  differentiationSheet,
  4,
  ["Niche", "Pattern concurrentiel", "Promesse proposée", "Architecture", "Preuve nécessaire", "À ne pas copier", "Premier test", "Risque principal"],
  DIFFERENTIATION_ROWS,
  "DifferentiationFinalTable",
);
differentiationSheet.freezePanes.freezeRows(4);
differentiationSheet.getRange(`A4:H${differentiationTable.endRow}`).format.wrapText = true;
[36, 50, 54, 58, 60, 50, 50, 44].forEach((width, index) => {
  differentiationSheet.getRange(`${colLetter(index + 1)}:${colLetter(index + 1)}`).format.columnWidth = width;
});

const summaryInspection = await workbook.inspect({
  kind: "table",
  range: "Synthèse!A1:P10",
  include: "values,formulas",
  tableMaxRows: 10,
  tableMaxCols: 16,
  maxChars: 30000,
});
await fs.writeFile(path.join(outputDir, "inspection-synthese.ndjson"), summaryInspection.ndjson, "utf8");

const architectureInspection = await workbook.inspect({
  kind: "table",
  range: "Arborescence!A1:J35",
  include: "values,formulas",
  tableMaxRows: 35,
  tableMaxCols: 10,
  maxChars: 50000,
});
await fs.writeFile(path.join(outputDir, "inspection-arborescence.ndjson"), architectureInspection.ndjson, "utf8");

const productInspection = await workbook.inspect({
  kind: "table",
  range: "Produits SEO!A1:V25",
  include: "values,formulas",
  tableMaxRows: 25,
  tableMaxCols: 22,
  maxChars: 50000,
});
await fs.writeFile(path.join(outputDir, "inspection-produits.ndjson"), productInspection.ndjson, "utf8");

const formulaErrors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 300 },
  summary: "final formula error scan",
});
await fs.writeFile(path.join(outputDir, "formula-error-scan.ndjson"), formulaErrors.ndjson, "utf8");

const previewRanges = {
  "Synthèse": "A1:P10",
  "Arborescence": "A1:J32",
  "Produits SEO": "A1:V18",
  "Sourcing AliExpress": "A1:T18",
  "Preuves concurrence": "A1:M18",
  "Volumes SEMrush": "A1:J22",
  "Contrôles QA": "A1:F15",
  "Méthode & limites": "A1:D20",
  "Priorités concurrence": "A1:G10",
  "Profils concurrents": "A1:N18",
  "Personas": "A1:I13",
  "Différenciation": "A1:H10",
};
for (const [sheetName, range] of Object.entries(previewRanges)) {
  const preview = await workbook.render({ sheetName, range, scale: 0.8, format: "png" });
  const bytes = new Uint8Array(await preview.arrayBuffer());
  await fs.writeFile(path.join(previewDir, `${sheetName.replaceAll(/[^a-zA-Z0-9]+/g, "-")}.png`), bytes);
}

const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(outputPath);

console.log(JSON.stringify({
  outputPath,
  previewDir,
  products: products.length,
  productsByNiche: catalogue.counts_by_niche,
  collections: catalogue.collections.length,
  competitionRows: competitionRows.length,
  volumeRows: volumeRows.length,
  qaOk: qaRows.every((row) => row[4] !== "ÉCHEC"),
  validation,
}, null, 2));
