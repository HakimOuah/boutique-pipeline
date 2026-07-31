import fs from "node:fs/promises";
import path from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const ROOT = "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/codex-chasse-clusters";
const RUN_ID = "20260720-124517";
const SOURCE_REGISTER = path.join(ROOT, "registre-candidats.codex.md");
const SOURCE_FINAL = path.join(ROOT, `final-${RUN_ID}.md`);
const SOURCE_FAMILIES = path.join(ROOT, "families.json");
const OUTPUT_DIR = path.join(ROOT, "outputs", RUN_ID);
const PREVIEW_DIR = path.join(ROOT, `tmp-excel-build-${RUN_ID}`);
const OUTPUT_PATH = path.join(OUTPUT_DIR, `tableau-produits-codex-${RUN_ID}.xlsx`);

function splitMarkdownRow(line) {
  return line
    .trim()
    .replace(/^\|/, "")
    .replace(/\|$/, "")
    .split("|")
    .map((cell) => cell.trim());
}

function tableUnder(markdown, headingPrefix) {
  const lines = markdown.split(/\r?\n/);
  const headingIndex = lines.findIndex((line) => line.startsWith(headingPrefix));
  if (headingIndex < 0) throw new Error(`Section introuvable: ${headingPrefix}`);
  let index = headingIndex + 1;
  while (index < lines.length && !lines[index].trim().startsWith("|")) index += 1;
  if (index >= lines.length) return { headers: [], rows: [] };
  const headers = splitMarkdownRow(lines[index]);
  index += 2;
  const rows = [];
  while (index < lines.length && lines[index].trim().startsWith("|")) {
    rows.push(splitMarkdownRow(lines[index]));
    index += 1;
  }
  return { headers, rows };
}

function plain(text = "") {
  return text
    .replace(/\*\*/g, "")
    .replace(/`/g, "")
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, "$1")
    .replace(/<br\s*\/?\s*>/gi, " — ")
    .trim();
}

function markdownLinkTarget(text = "") {
  return text.match(/\]\(([^)]+)\)/)?.[1] ?? "";
}

function stopStatus(gate) {
  const pureExclusions = new Set([
    "Anti-doublon historique",
    "Preuve volume",
    "Volume",
    "Volume adressable",
    "Volume du sous-segment",
  ]);
  return pureExclusions.has(plain(gate)) ? "EXCLU" : "CREUSÉ";
}

function volumeSummary(motif) {
  const firstClause = plain(motif).split(/,\s+/)[0].trim();
  return /(mois|\bK\b|\bk\b|cluster|tête commerciale|total large)/i.test(firstClause)
    ? firstClause
    : "";
}

function findFamilyName(id, families) {
  return families.find((family) => id.startsWith(family.id))?.name ?? "Non renseignée";
}

async function extractQueries(dossierRelativePath) {
  if (!dossierRelativePath) return ["", ""];
  const dossierPath = path.join(ROOT, dossierRelativePath);
  try {
    const content = await fs.readFile(dossierPath, "utf8");
    const section = content.match(
      /## Requêtes manuelles à copier dans AliExpress([\s\S]*?)(?=\n## |$)/,
    )?.[1] ?? "";
    const queries = [...section.matchAll(/`([^`]+)`/g)].map((match) => match[1]);
    return [queries[0] ?? "", queries[1] ?? ""];
  } catch {
    return ["", ""];
  }
}

function setColumnWidth(sheet, column, width) {
  sheet.getRange(`${column}:${column}`).format.columnWidth = width;
}

function applyBaseRangeFormat(range) {
  range.format = {
    font: { color: "#203040" },
    verticalAlignment: "center",
    wrapText: true,
  };
}

async function main() {
  await fs.mkdir(OUTPUT_DIR, { recursive: true });
  await fs.mkdir(PREVIEW_DIR, { recursive: true });

  const [registerMarkdown, finalMarkdown, familiesJson] = await Promise.all([
    fs.readFile(SOURCE_REGISTER, "utf8"),
    fs.readFile(SOURCE_FINAL, "utf8"),
    fs.readFile(SOURCE_FAMILIES, "utf8").then(JSON.parse),
  ]);

  const retainedTable = tableUnder(registerMarkdown, "## Candidats retenus");
  const stopTable = tableUnder(registerMarkdown, "## STOP documentés");
  const priorityTable = tableUnder(finalMarkdown, "## Tableau des 17 thématiques");

  const priorityByDossier = new Map();
  for (const row of priorityTable.rows) {
    const dossier = markdownLinkTarget(row[6]);
    priorityByDossier.set(dossier, {
      priority: Number.parseInt(plain(row[0]), 10),
      costCeiling: plain(row[5]),
    });
  }

  const retainedRows = [];
  for (const row of retainedTable.rows) {
    const dossier = markdownLinkTarget(row[12]);
    const [queryFr, queryEn] = await extractQueries(dossier);
    const sourcing = priorityByDossier.get(dossier) ?? {};
    retainedRows.push({
      status: "VALIDÉ",
      priority: sourcing.priority ?? "",
      id: plain(row[0]),
      product: plain(row[1]),
      family: plain(row[2]),
      sourceVerdict: plain(row[11]),
      gate: "Marché qualifié — fournisseur et économie à valider",
      volume: plain(row[3]),
      marketPrice: plain(row[4]),
      cpc: plain(row[5]),
      deliveredCost: sourcing.costCeiling ?? plain(row[8]),
      evidence: plain(row[6]),
      queryFr,
      queryEn,
      supplierLink: "",
      report: dossier,
      reserves: plain(row[13]),
      source: SOURCE_REGISTER,
    });
  }

  retainedRows.sort((a, b) => (a.priority || 99) - (b.priority || 99) || a.id.localeCompare(b.id));

  const stopRows = stopTable.rows.map((row) => ({
    status: stopStatus(row[2]),
    priority: "",
    id: plain(row[0]),
    product: plain(row[1]),
    family: findFamilyName(plain(row[0]), familiesJson.families ?? []),
    sourceVerdict: "STOP",
    gate: plain(row[2]),
    volume: volumeSummary(row[3]),
    marketPrice: "",
    cpc: "",
    deliveredCost: "",
    evidence: plain(row[3]),
    queryFr: "",
    queryEn: "",
    supplierLink: "",
    report: markdownLinkTarget(row[4]),
    reserves: "",
    source: SOURCE_REGISTER,
  }));

  // Quatre clusters de phase 0 figurent dans run-state.json (110 traités),
  // mais pas dans le tableau STOP du registre. Les faits ci-dessous viennent
  // directement de leurs deux rapports de famille afin de ne perdre aucune ligne.
  stopRows.push(
    {
      status: "EXCLU",
      priority: "",
      id: "f18-bijouterie-lapidaire-c01-laminoir-bijoutier",
      product: "Laminoir de bijoutier",
      family: "Bijouterie & lapidaire",
      sourceVerdict: "STOP",
      gate: "Volume",
      volume: "1 050 recherches/mois",
      marketPrice: "",
      cpc: "",
      deliveredCost: "",
      evidence: "Total large de 1 050 recherches/mois ; principales formulations appareil à 260, 210 et 140 recherches/mois. Sous le seuil.",
      queryFr: "",
      queryEn: "",
      supplierLink: "",
      report: `reports/phase0-f18-bijouterie-lapidaire-family-${RUN_ID}-a1.md`,
      reserves: "",
      source: path.join(ROOT, `reports/phase0-f18-bijouterie-lapidaire-family-${RUN_ID}-a1.md`),
    },
    {
      status: "EXCLU",
      priority: "",
      id: "f18-bijouterie-lapidaire-c02-tonneau-polir",
      product: "Tonneau à polir les pierres",
      family: "Bijouterie & lapidaire",
      sourceVerdict: "STOP",
      gate: "Volume",
      volume: "40 recherches/mois",
      marketPrice: "",
      cpc: "",
      deliveredCost: "",
      evidence: "Total SEMrush de 40 recherches/mois : deux formulations à 20, le reste à zéro. Sous le seuil.",
      queryFr: "",
      queryEn: "",
      supplierLink: "",
      report: `reports/phase0-f18-bijouterie-lapidaire-family-${RUN_ID}-a1.md`,
      reserves: "",
      source: path.join(ROOT, `reports/phase0-f18-bijouterie-lapidaire-family-${RUN_ID}-a1.md`),
    },
    {
      status: "EXCLU",
      priority: "",
      id: "f20-cuir-maroquinerie-c01-machine-coudre-cuir",
      product: "Machine à coudre le cuir",
      family: "Cuir & maroquinerie",
      sourceVerdict: "STOP",
      gate: "Volume",
      volume: "4 350 recherches/mois",
      marketPrice: "",
      cpc: "",
      deliveredCost: "",
      evidence: "Total large SEMrush de 4 350 recherches/mois ; plusieurs formulations sont orientées tutoriel. Très inférieur au seuil.",
      queryFr: "",
      queryEn: "",
      supplierLink: "",
      report: `reports/phase0-f20-cuir-maroquinerie-family-${RUN_ID}-a1.md`,
      reserves: "",
      source: path.join(ROOT, `reports/phase0-f20-cuir-maroquinerie-family-${RUN_ID}-a1.md`),
    },
    {
      status: "EXCLU",
      priority: "",
      id: "f20-cuir-maroquinerie-c02-pareuse-cuir",
      product: "Pareuse cuir",
      family: "Cuir & maroquinerie",
      sourceVerdict: "STOP",
      gate: "Volume",
      volume: "570 recherches/mois",
      marketPrice: "",
      cpc: "",
      deliveredCost: "",
      evidence: "Total large de 570 recherches/mois ; deux formulations principales à 210 et 170, le reste à 20–30 ou orienté occasion.",
      queryFr: "",
      queryEn: "",
      supplierLink: "",
      report: `reports/phase0-f20-cuir-maroquinerie-family-${RUN_ID}-a1.md`,
      reserves: "",
      source: path.join(ROOT, `reports/phase0-f20-cuir-maroquinerie-family-${RUN_ID}-a1.md`),
    },
  );

  stopRows.sort((a, b) => {
    const order = { "CREUSÉ": 1, "EXCLU": 2 };
    return order[a.status] - order[b.status] || a.id.localeCompare(b.id);
  });

  const allRows = [...retainedRows, ...stopRows];
  const counts = {
    total: allRows.length,
    valid: allRows.filter((row) => row.status === "VALIDÉ").length,
    investigated: allRows.filter((row) => row.status === "CREUSÉ").length,
    excluded: allRows.filter((row) => row.status === "EXCLU").length,
  };

  if (counts.total !== 110 || counts.valid !== 17) {
    throw new Error(`Comptage inattendu: ${JSON.stringify(counts)}`);
  }

  const headers = [
    "Statut",
    "Priorité sourcing",
    "ID",
    "Produit / thématique",
    "Famille",
    "Verdict source",
    "Porte / motif",
    "Volume FR",
    "Prix marché TTC",
    "CPC",
    "Coût livré maximal",
    "Concurrence / motif factuel",
    "Requête AliExpress FR",
    "Requête AliExpress EN",
    "Lien fournisseur AliExpress",
    "Rapport / dossier",
    "Réserves / conditions",
    "Source de vérité",
  ];

  const dataMatrix = allRows.map((row) => [
    row.status,
    row.priority,
    row.id,
    row.product,
    row.family,
    row.sourceVerdict,
    row.gate,
    row.volume,
    row.marketPrice,
    row.cpc,
    row.deliveredCost,
    row.evidence,
    row.queryFr,
    row.queryEn,
    row.supplierLink,
    row.report,
    row.reserves,
    row.source,
  ]);

  const workbook = Workbook.create();
  const summary = workbook.worksheets.add("Synthèse");
  const products = workbook.worksheets.add("Produits");
  summary.showGridLines = false;
  products.showGridLines = false;

  // Synthèse
  summary.mergeCells("A1:H1");
  summary.getRange("A1").values = [["TABLEAU DE RECHERCHE PRODUITS — FRANCE"]];
  summary.getRange("A1:H1").format = {
    fill: "#17324D",
    font: { bold: true, color: "#FFFFFF" },
    horizontalAlignment: "center",
    verticalAlignment: "center",
  };
  summary.getRange("A1:H1").format.rowHeight = 34;

  summary.mergeCells("A2:H2");
  summary.getRange("A2").values = [[
    "Run Codex 20260720-124517 · 40 familles épuisées · statut fournisseur encore à compléter pour les marchés retenus",
  ]];
  summary.getRange("A2:H2").format = {
    fill: "#EAF2F8",
    font: { color: "#36536B" },
    horizontalAlignment: "center",
    verticalAlignment: "center",
    wrapText: true,
  };
  summary.getRange("A2:H2").format.rowHeight = 32;

  const lastDataRow = 5 + allRows.length;
  const cards = [
    { top: "A4:B4", body: "A5:B6", label: "TOTAL PRODUITS", formula: `=COUNTA(Produits!$C$6:$C$${lastDataRow})`, fill: "#D9EAF7", color: "#17324D" },
    { top: "C4:D4", body: "C5:D6", label: "VALIDÉS", formula: `=COUNTIF(Produits!$A$6:$A$${lastDataRow},\"VALIDÉ\")`, fill: "#E2F0D9", color: "#1B5E20" },
    { top: "E4:F4", body: "E5:F6", label: "CREUSÉS", formula: `=COUNTIF(Produits!$A$6:$A$${lastDataRow},\"CREUSÉ\")`, fill: "#FFF2CC", color: "#9A5B00" },
    { top: "G4:H4", body: "G5:H6", label: "EXCLUS", formula: `=COUNTIF(Produits!$A$6:$A$${lastDataRow},\"EXCLU\")`, fill: "#F4CCCC", color: "#9C1C1C" },
  ];
  for (const card of cards) {
    summary.mergeCells(card.top);
    summary.mergeCells(card.body);
    summary.getRange(card.top.split(":")[0]).values = [[card.label]];
    summary.getRange(card.body.split(":")[0]).formulas = [[card.formula]];
    summary.getRange(card.top).format = {
      fill: "#17324D",
      font: { bold: true, color: "#FFFFFF" },
      horizontalAlignment: "center",
      verticalAlignment: "center",
      borders: { preset: "all", style: "thin", color: "#FFFFFF" },
    };
    summary.getRange(card.body).format = {
      fill: card.fill,
      font: { bold: true, color: card.color },
      horizontalAlignment: "center",
      verticalAlignment: "center",
      borders: { preset: "all", style: "thin", color: "#D0D8E0" },
    };
  }
  summary.getRange("A5:H6").format.rowHeight = 28;

  summary.mergeCells("A9:H9");
  summary.getRange("A9").values = [["LÉGENDE ET RÈGLE DE CLASSEMENT"]];
  summary.getRange("A9:H9").format = {
    fill: "#2D5B70",
    font: { bold: true, color: "#FFFFFF" },
    horizontalAlignment: "left",
    verticalAlignment: "center",
  };

  const legend = [
    ["VALIDÉ", "Marché retenu : demande, SERP et prix ont passé les portes. Le fournisseur et l'économie restent à confirmer."],
    ["CREUSÉ", "Piste analysée au-delà du seul volume, puis arrêtée sur prix, concurrence, sécurité, logistique, SAV ou risque comparable."],
    ["EXCLU", "Exclusion ferme dans ce run : volume/adressabilité insuffisants, preuve volume absente ou doublon historique sans reprise motivée."],
  ];
  const legendStyles = [
    { fill: "#E2F0D9", color: "#1B5E20" },
    { fill: "#FFF2CC", color: "#9A5B00" },
    { fill: "#F4CCCC", color: "#9C1C1C" },
  ];
  legend.forEach((entry, index) => {
    const row = 10 + index;
    summary.mergeCells(`A${row}:B${row}`);
    summary.mergeCells(`C${row}:H${row}`);
    summary.getRange(`A${row}`).values = [[entry[0]]];
    summary.getRange(`C${row}`).values = [[entry[1]]];
    summary.getRange(`A${row}:B${row}`).format = {
      fill: legendStyles[index].fill,
      font: { bold: true, color: legendStyles[index].color },
      horizontalAlignment: "center",
      verticalAlignment: "center",
      borders: { preset: "all", style: "thin", color: "#D0D8E0" },
    };
    summary.getRange(`C${row}:H${row}`).format = {
      fill: "#F7F9FB",
      font: { color: "#30475A" },
      horizontalAlignment: "left",
      verticalAlignment: "center",
      wrapText: true,
      borders: { preset: "all", style: "thin", color: "#D0D8E0" },
    };
    summary.getRange(`A${row}:H${row}`).format.rowHeight = 36;
  });

  summary.mergeCells("A14:H14");
  summary.getRange("A14").values = [[
    "Utilisation : ouvre l'onglet Produits, filtre la colonne Statut, Priorité, Famille ou Porte / motif. La liste déroulante de Statut recolore automatiquement toute la ligne.",
  ]];
  summary.getRange("A14:H14").format = {
    fill: "#EAF2F8",
    font: { bold: true, color: "#36536B" },
    verticalAlignment: "center",
    wrapText: true,
    borders: { preset: "outside", style: "thin", color: "#B7C9D6" },
  };
  summary.getRange("A14:H14").format.rowHeight = 38;

  summary.mergeCells("A16:H16");
  summary.getRange("A16").values = [[
    `Source : ${SOURCE_REGISTER} · Généré le 20/07/2026`,
  ]];
  summary.getRange("A16:H16").format = {
    font: { color: "#6B7C8A" },
    wrapText: true,
    verticalAlignment: "center",
  };

  for (const column of ["A", "B", "C", "D", "E", "F", "G", "H"]) setColumnWidth(summary, column, 17);
  summary.freezePanes.freezeRows(2);

  // Produits
  products.mergeCells("A1:R1");
  products.getRange("A1").values = [["PRODUITS ET THÉMATIQUES — REGISTRE FILTRABLE"]];
  products.getRange("A1:R1").format = {
    fill: "#17324D",
    font: { bold: true, color: "#FFFFFF" },
    horizontalAlignment: "left",
    verticalAlignment: "center",
  };
  products.getRange("A1:R1").format.rowHeight = 32;

  products.mergeCells("A2:R2");
  products.getRange("A2").values = [[
    "Vert = marché retenu · Orange = piste approfondie puis arrêtée · Rouge = exclusion ferme dans ce run",
  ]];
  products.getRange("A2:R2").format = {
    fill: "#EAF2F8",
    font: { color: "#36536B" },
    horizontalAlignment: "left",
    verticalAlignment: "center",
  };

  products.mergeCells("A3:R3");
  products.getRange("A3").values = [[
    "Les 17 lignes VALIDÉES correspondent à des marchés à sourcer : aucun fournisseur AliExpress ni lancement n'est encore validé.",
  ]];
  products.getRange("A3:R3").format = {
    fill: "#FFF4E5",
    font: { bold: true, color: "#8A4B08" },
    horizontalAlignment: "left",
    verticalAlignment: "center",
  };

  products.getRange("A5:R5").values = [headers];
  products.getRange(`A6:R${lastDataRow}`).values = dataMatrix;
  applyBaseRangeFormat(products.getRange(`A5:R${lastDataRow}`));

  const table = products.tables.add(`A5:R${lastDataRow}`, true, "ProduitsTable");
  table.style = "TableStyleMedium2";
  table.showHeaders = true;
  table.showFilterButton = true;
  table.showBandedRows = false;

  products.getRange("A5:R5").format = {
    fill: "#2D5B70",
    font: { bold: true, color: "#FFFFFF" },
    horizontalAlignment: "center",
    verticalAlignment: "center",
    wrapText: true,
    borders: { preset: "all", style: "thin", color: "#D8E2E8" },
  };
  products.getRange("A5:R5").format.rowHeight = 42;
  products.getRange(`A6:R${lastDataRow}`).format.rowHeight = 48;
  products.getRange(`A6:R${lastDataRow}`).format.borders = {
    preset: "all",
    style: "thin",
    color: "#D9E1E7",
  };

  products.getRange(`A6:A${lastDataRow}`).format.horizontalAlignment = "center";
  products.getRange(`B6:B${lastDataRow}`).format.horizontalAlignment = "center";
  products.getRange(`F6:F${lastDataRow}`).format.horizontalAlignment = "center";
  products.getRange(`A6:A${lastDataRow}`).format.font = { bold: true, color: "#203040" };

  const dataRange = products.getRange(`A6:R${lastDataRow}`);
  dataRange.conditionalFormats.addCustom('=$A6="VALIDÉ"', {
    fill: "#E2F0D9",
    font: { color: "#1B5E20" },
  });
  dataRange.conditionalFormats.addCustom('=$A6="CREUSÉ"', {
    fill: "#FFF2CC",
    font: { color: "#7A4A00" },
  });
  dataRange.conditionalFormats.addCustom('=$A6="EXCLU"', {
    fill: "#F4CCCC",
    font: { color: "#8B1E1E" },
  });

  products.getRange(`A6:A${lastDataRow}`).dataValidation = {
    rule: { type: "list", values: ["VALIDÉ", "CREUSÉ", "EXCLU"] },
  };

  const widths = {
    A: 13,
    B: 11,
    C: 34,
    D: 32,
    E: 25,
    F: 25,
    G: 27,
    H: 24,
    I: 18,
    J: 12,
    K: 19,
    L: 58,
    M: 47,
    N: 47,
    O: 32,
    P: 48,
    Q: 50,
    R: 58,
  };
  Object.entries(widths).forEach(([column, width]) => setColumnWidth(products, column, width));

  products.freezePanes.freezeRows(5);
  products.freezePanes.freezeColumns(4);

  const summaryInspect = await workbook.inspect({
    kind: "table",
    range: "Synthèse!A1:H16",
    include: "values,formulas",
    tableMaxRows: 20,
    tableMaxCols: 10,
  });
  const productsInspect = await workbook.inspect({
    kind: "table",
    range: "Produits!A1:R16",
    include: "values,formulas",
    tableMaxRows: 20,
    tableMaxCols: 18,
  });
  const errorsInspect = await workbook.inspect({
    kind: "match",
    searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
    options: { useRegex: true, maxResults: 300 },
    summary: "Recherche finale des erreurs de formule",
  });

  console.log("COUNTS", JSON.stringify(counts));
  console.log("SUMMARY_INSPECT", summaryInspect.ndjson);
  console.log("PRODUCTS_INSPECT", productsInspect.ndjson);
  console.log("ERROR_INSPECT", errorsInspect.ndjson);

  const previewSummary = await workbook.render({
    sheetName: "Synthèse",
    range: "A1:H16",
    scale: 1.4,
    format: "png",
  });
  await fs.writeFile(
    path.join(PREVIEW_DIR, "preview-synthese.png"),
    new Uint8Array(await previewSummary.arrayBuffer()),
  );

  const previewProducts = await workbook.render({
    sheetName: "Produits",
    range: "A1:R24",
    scale: 0.9,
    format: "png",
  });
  await fs.writeFile(
    path.join(PREVIEW_DIR, "preview-produits.png"),
    new Uint8Array(await previewProducts.arrayBuffer()),
  );

  const previewTail = await workbook.render({
    sheetName: "Produits",
    range: `A${Math.max(6, lastDataRow - 15)}:R${lastDataRow}`,
    scale: 0.9,
    format: "png",
  });
  await fs.writeFile(
    path.join(PREVIEW_DIR, "preview-exclus.png"),
    new Uint8Array(await previewTail.arrayBuffer()),
  );

  const xlsx = await SpreadsheetFile.exportXlsx(workbook);
  await xlsx.save(OUTPUT_PATH);
  console.log("OUTPUT", OUTPUT_PATH);
}

await main();
