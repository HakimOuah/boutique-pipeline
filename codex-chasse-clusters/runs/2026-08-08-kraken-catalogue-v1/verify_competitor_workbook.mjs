import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile } from "/Users/Hakim/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs";

const inputPath = "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/codex-chasse-clusters/outputs/2026-08-08-kraken-concurrence-v1/5-niches-kraken-etude-concurrentielle-2026-08-08.xlsx";
const outputDir = "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/codex-chasse-clusters/outputs/2026-08-08-kraken-concurrence-v1/verification-import";

await fs.mkdir(outputDir, { recursive: true });
const input = await FileBlob.load(inputPath);
const workbook = await SpreadsheetFile.importXlsx(input);

const overview = await workbook.inspect({
  kind: "workbook,sheet,table",
  maxChars: 12000,
  tableMaxRows: 8,
  tableMaxCols: 12,
  tableMaxCellChars: 120,
});
await fs.writeFile(`${outputDir}/overview.ndjson`, overview.ndjson, "utf8");

const sheetInfo = await workbook.inspect({ kind: "sheet", include: "id,name", maxChars: 8000 });
await fs.writeFile(`${outputDir}/sheets.ndjson`, sheetInfo.ndjson, "utf8");

const renderRanges = {
  "Synthèse": "A1:P9",
  "Arborescence": "A1:L34",
  "Produits SEO": "A1:V24",
  "Fournisseurs candidats": "A1:S22",
  "Sourcing QA": "A1:N9",
  "SERP & Trends": "A1:H22",
  "Méthode & limites": "A1:D17",
  "Priorités concurrence": "A1:G18",
  "Concurrents": "A1:P29",
  "SEMrush concurrence": "A1:K32",
  "Personas & VOC": "A1:I12",
  "Différenciation": "A1:H9",
};
const sheetNames = workbook.worksheets.items.map((sheet) => sheet.name);
const expectedSheetNames = Object.keys(renderRanges);
if (JSON.stringify(sheetNames) !== JSON.stringify(expectedSheetNames)) {
  throw new Error(`Onglets inattendus: ${JSON.stringify(sheetNames)}`);
}
for (const sheetName of sheetNames) {
  const preview = await workbook.render({ sheetName, range: renderRanges[sheetName], scale: 0.55, format: "png" });
  const safeName = sheetName.replace(/[^a-z0-9]+/gi, "-").replace(/^-|-$/g, "").toLowerCase();
  await fs.writeFile(`${outputDir}/${safeName}.png`, new Uint8Array(await preview.arrayBuffer()));
}

const formulaErrors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 300 },
  summary: "post-import formula error scan",
});
await fs.writeFile(`${outputDir}/formula-error-scan.ndjson`, formulaErrors.ndjson, "utf8");
if (!formulaErrors.ndjson.includes("matched 0 entries")) {
  throw new Error("Le scan post-import contient au moins une erreur de formule");
}

console.log(JSON.stringify({ sheetNames, outputDir }, null, 2));
