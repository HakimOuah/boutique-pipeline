import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const projectRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const noirmontRoot = path.join(projectRoot, "boutique-seiko-mod");
const outputRoot = path.join(projectRoot, "scratchpad", "noirmont-galeries");
const inputRoot = path.join(outputRoot, "entrees-faces");
const rawRoot = path.join(outputRoot, "entrees-brutes");
const generatedRoot = path.join(outputRoot, "generated");
const qaRoot = path.join(outputRoot, "qa");

for (const directory of [outputRoot, inputRoot, rawRoot, generatedRoot, qaRoot]) {
  fs.mkdirSync(directory, { recursive: true });
}

const oldPrompt = fs.readFileSync(
  path.join(noirmontRoot, "OBSOLETE-NE-PAS-UTILISER-prompt-galeries-v1.md.bak"),
  "utf8",
);
const skuByHandle = new Map();
for (const match of oldPrompt.matchAll(/^\| `([^`]+)` \| `([^`]+)`/gm)) {
  skuByHandle.set(match[1], match[2]);
}

Object.entries({
  "trente-six-classique-jubile": "14:200000080#black no logo;5:57085267#39-solid back",
  "trente-neuf-classique-cannelee": "14:193#orange no logo;5:57085267#8215-39mm(solidback)",
  "quarante-et-un-sport-acier": "14:350686#White Dia M;5:57036539#Miyota 8215",
  "trente-neuf-duo-classique-bicolore": "14:201447303#Rose 36mm solid back;5:57000035#Miyota8215",
  "noirmont-un-plongeuse-acier": "14:350686#steel case-no logo;5:646979416#Miyota82-glass back",
  "noirmont-deux-plongeuse-ceramique": "14:29#color 3;5:646979416#Miyota 8215",
}).forEach(([handle, sku]) => skuByHandle.set(handle, sku));

const watchHandles = [
  "contre-la-montre-argent-chronographe",
  "contre-la-montre-blanc-chronographe",
  "contre-la-montre-bleu-glacier-chronographe",
  "contre-la-montre-champagne-chronographe",
  "contre-la-montre-compteurs-bleus-chronographe",
  "contre-la-montre-gris-anthracite-chronographe",
  "contre-la-montre-noir-chronographe",
  "contre-la-montre-panda-inverse-chronographe",
  "contre-la-montre-panda-chronographe",
  "contre-la-montre-rose-poudre-chronographe",
  "contre-la-montre-turquoise-chronographe",
  "contre-la-montre-vert-chronographe",
  "heritage-bleu-nuit-plongeuse-vintage-42",
  "heritage-bleu-plongeuse-vintage-42",
  "heritage-vert-plongeuse-vintage-42",
  "integrale-blanc-argente-sport-chic-acier",
  "integrale-bleu-ciel-sport-chic-acier",
  "integrale-bleu-nuit-sport-chic-acier",
  "integrale-brun-or-rose-sport-chic",
  "integrale-noir-sport-chic-acier",
  "integrale-turquoise-sport-chic-acier",
  "integrale-vert-sport-chic-acier",
  "voyageur-bicolore-cadran-brun-gmt",
  "voyageur-bicolore-gmt-3-maillons",
  "voyageur-bicolore-gmt-5-maillons",
  "voyageur-or-rose-gmt-5-maillons",
  "voyageur-or-gmt-3-maillons",
  "voyageur-or-gmt-president",
  "trente-six-bleu-classique-jubile",
  "trente-six-dore-classique-jubile",
  "trente-six-or-integral-classique-jubile",
  "trente-six-rose-classique-jubile",
  "trente-six-rouge-classique-jubile",
  "trente-six-classique-jubile",
  "trente-neuf-bleu-mer-classique-cannelee",
  "trente-neuf-bleu-classique-cannelee",
  "trente-neuf-noir-classique-cannelee",
  "trente-neuf-rose-classique-cannelee",
  "trente-neuf-rouge-classique-cannelee",
  "trente-neuf-vert-classique-cannelee",
  "trente-neuf-classique-cannelee",
  "quarante-et-un-blanc-cuir-sport-acier",
  "quarante-et-un-bleu-acier-sport-acier",
  "quarante-et-un-bleu-cuir-sport-acier",
  "quarante-et-un-noir-jaune-acier-sport-acier",
  "quarante-et-un-noir-acier-sport-acier",
  "quarante-et-un-noir-cuir-sport-acier",
  "quarante-et-un-sport-acier",
  "trente-neuf-duo-dore-classique-bicolore",
  "trente-neuf-duo-classique-bicolore",
  "noirmont-un-bronze-plongeuse",
  "noirmont-un-plongeuse-acier",
  "noirmont-deux-plongeuse-ceramique",
];

const accessoryHandles = [
  "barrettes-de-rechange-270",
  "bracelet-acier-massif-12-22-mm",
  "bracelet-caoutchouc-gaufre",
  "bracelet-cuir-daim-degagement-rapide",
  "bracelet-fkm-courbe",
  "bracelet-fkm-tropical",
  "bracelet-jubile-acier-904l-20mm",
  "bracelet-jubile-embouts-courbes",
  "bracelet-milanais-maille-italienne",
  "bracelet-presidentiel-904l",
  "bracelet-presidentiel-dore",
  "coffret-douze-aluminium",
  "coffret-douze-presentation",
  "coussins-de-presentation-lot-de-10",
  "doigtiers-d-horloger-latex",
  "kit-d-entretien-13-pieces",
  "loupe-d-horloger",
  "loupe-de-date-saphir",
  "outil-de-mise-a-taille-de-bracelet",
  "pince-a-barrettes",
  "remontoir-bois-acajou",
  "remontoir-bois-ebene",
  "remontoir-bois-noir-laque",
  "remontoir-bois-noyer",
  "remontoir-collection-bois-beige",
  "remontoir-collection-bois-led-noir",
  "remontoir-collection-bois-led-rouge",
  "remontoir-collection-bois-noir",
  "remontoir-collection-cuir-pu",
  "remontoir-solo",
  "remontoir-vitrine",
  "rouleau-de-voyage-bleu-marine-cuir",
  "rouleau-de-voyage-brun-cuir",
  "rouleau-de-voyage-noir-cuir",
  "rouleau-de-voyage-vert-cuir",
  "set-tournevis-horloger",
  "coffret-6-montres-couvercle-verre",
  "etui-de-voyage-rigide",
];

const cdnPrefix = "https://cdn.shopify.com/s/files/1/1094/1893/8706/files/";
const cdnFiles = {
  "trente-six-bleu-classique-jubile": "10977448690002-var-bleu.jpg",
  "trente-six-dore-classique-jubile": "10977448690002-var-dore.jpg",
  "trente-six-or-integral-classique-jubile": "10977448690002-var-or-integral.jpg",
  "trente-six-rose-classique-jubile": "10977448690002-var-rose.jpg",
  "trente-six-rouge-classique-jubile": "10977448690002-var-rouge.jpg",
  "trente-neuf-bleu-mer-classique-cannelee": "10977444430162-var-bleu-mer.jpg",
  "trente-neuf-bleu-classique-cannelee": "10977444430162-var-bleu.jpg",
  "trente-neuf-noir-classique-cannelee": "10977444430162-var-noir.jpg",
  "trente-neuf-rose-classique-cannelee": "10977444430162-var-rose.jpg",
  "trente-neuf-rouge-classique-cannelee": "10977444430162-var-rouge.jpg",
  "trente-neuf-vert-classique-cannelee": "10977444430162-var-vert.jpg",
  "quarante-et-un-blanc-cuir-sport-acier": "10977444495698-var-blanc-cuir.jpg",
  "quarante-et-un-bleu-acier-sport-acier": "10977444495698-var-bleu-acier.jpg",
  "quarante-et-un-bleu-cuir-sport-acier": "10977444495698-var-bleu-cuir.jpg",
  "quarante-et-un-noir-jaune-acier-sport-acier": "10977444495698-var-noir-jaune-acier.jpg",
  "quarante-et-un-noir-acier-sport-acier": "10977444495698-var-noir-acier.jpg",
  "quarante-et-un-noir-cuir-sport-acier": "10977444495698-var-noir-cuir.jpg",
  "trente-neuf-duo-dore-classique-bicolore": "10977448722770-var-dore.jpg",
  "noirmont-un-bronze-plongeuse": "10977448558930-var-bronze.jpg",
  "trente-six-classique-jubile": "10977448690002-1.jpg",
  "trente-neuf-classique-cannelee": "10977444430162-1.jpg",
  "quarante-et-un-sport-acier": "10977444495698-1.jpg",
  "trente-neuf-duo-classique-bicolore": "10977448722770-1.jpg",
  "noirmont-un-plongeuse-acier": "10977448558930-1.jpg",
  "noirmont-deux-plongeuse-ceramique": "10977448624466-1.jpg",
  "barrettes-de-rechange-270": "10977444954450-1.jpg",
  "bracelet-fkm-courbe": "10977445151058-1.jpg",
  "bracelet-fkm-tropical": "10977445183826-1.jpg",
  "bracelet-presidentiel-904l": "10977445052754-1.jpg",
  "bracelet-presidentiel-dore": "10977445085522-1.jpg",
  "coffret-douze-aluminium": "10977444856146-1.jpg",
  "coffret-douze-presentation": "10977444888914-1.jpg",
  "loupe-de-date-saphir": "10977445216594-1.jpg",
  "pince-a-barrettes": "10977444921682-1.jpg",
  "remontoir-solo": "10977444626770-1.jpg",
  "remontoir-vitrine": "10977444790610-1.jpg",
  "set-tournevis-horloger": "10977444987218-1.jpg",
};

const localFiles = {
  "bracelet-acier-massif-12-22-mm": "jubile-plat-1.jpg",
  "bracelet-caoutchouc-gaufre": "waffle-1.jpg",
  "bracelet-cuir-daim-degagement-rapide": "noirmont-cuir-daim-1.jpg",
  "bracelet-jubile-acier-904l-20mm": "noirmont-jubile-904l-1.jpg",
  "bracelet-jubile-embouts-courbes": "jubile-courbe-1.jpg",
  "bracelet-milanais-maille-italienne": "noirmont-milanais-1.jpg",
  "coussins-de-presentation-lot-de-10": "coussin-1.jpg",
  "doigtiers-d-horloger-latex": "noirmont-doigtiers-1.jpg",
  "kit-d-entretien-13-pieces": "kit-entretien-1.jpg",
  "loupe-d-horloger": "noirmont-loupe-1.jpg",
  "outil-de-mise-a-taille-de-bracelet": "outil-bracelet-1.jpg",
  "coffret-6-montres-couvercle-verre": "coffret-six-1.jpg",
  "etui-de-voyage-rigide": "etui-voyage-1.jpg",
};

if (watchHandles.length !== 53 || accessoryHandles.length !== 38) {
  throw new Error(`Unexpected scope: ${watchHandles.length} watches, ${accessoryHandles.length} accessories`);
}

const visualManifest = JSON.parse(
  fs.readFileSync(path.join(noirmontRoot, "visual-manifest-2026-07-25.json"), "utf8"),
);
const priorBySku = new Map();
for (const product of visualManifest.products) {
  for (const assignment of product.assignments) {
    priorBySku.set(assignment.sku, assignment.file);
  }
}

const entries = [];
for (const [family, handles] of [["montre", watchHandles], ["accessoire", accessoryHandles]]) {
  for (const handle of handles) {
    const sku = skuByHandle.get(handle);
    if (!sku) throw new Error(`Missing SKU for ${handle}`);

    let source;
    let sourceKind;
    if (cdnFiles[handle]) {
      source = `${cdnPrefix}${cdnFiles[handle]}`;
      sourceKind = "cdn";
    } else if (localFiles[handle]) {
      source = path.join(projectRoot, "scratchpad", "noirmont-accessoires-img", localFiles[handle]);
      sourceKind = "local-accessoire";
    } else {
      source = priorBySku.get(sku);
      sourceKind = "visuel-valide-2026-07-25";
    }
    if (!source) throw new Error(`Missing face source mapping for ${handle}`);

    const slots = family === "montre"
      ? ["02-situation", "03-macro", "04-poignet"]
      : (["coffret-6-montres-couvercle-verre", "etui-de-voyage-rigide"].includes(handle)
        ? ["03-macro"]
        : ["02-situation", "03-macro"]);

    entries.push({
      handle,
      sku,
      famille: family,
      source,
      sourceKind,
      entreeFace: path.join(inputRoot, `${handle}-01-face.jpg`),
      slots,
    });
  }
}

const jobs = entries.flatMap((entry) =>
  entry.slots.map((slot) => ({
    handle: entry.handle,
    sku: entry.sku,
    famille: entry.famille,
    slot,
    source: entry.entreeFace,
    fichier: path.join(generatedRoot, `${entry.handle}-${slot}.jpg`),
    modeleUtilise: "GPT Image 2 natif",
    nombreRegenerations: 0,
    statut: "a_generer",
  })),
);

if (entries.length !== 91 || jobs.length !== 233 || Object.keys(cdnFiles).length !== 37) {
  throw new Error(`Unexpected totals: ${entries.length} entries, ${jobs.length} jobs, ${Object.keys(cdnFiles).length} CDN`);
}

fs.writeFileSync(
  path.join(outputRoot, "sources.json"),
  `${JSON.stringify({ generatedAt: new Date().toISOString(), entries }, null, 2)}\n`,
);
fs.writeFileSync(
  path.join(outputRoot, "worklist.json"),
  `${JSON.stringify({ generatedAt: new Date().toISOString(), counts: {
    fiches: entries.length,
    montres: watchHandles.length,
    accessoires: accessoryHandles.length,
    generations: jobs.length,
    sourcesCdn: Object.keys(cdnFiles).length,
  }, jobs }, null, 2)}\n`,
);

console.log(JSON.stringify({
  fiches: entries.length,
  montres: watchHandles.length,
  accessoires: accessoryHandles.length,
  generations: jobs.length,
  sources: Object.fromEntries(
    Object.entries(Object.groupBy(entries, (entry) => entry.sourceKind))
      .map(([key, value]) => [key, value.length]),
  ),
  outputRoot,
}, null, 2));
