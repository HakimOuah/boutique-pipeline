import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.dirname(fileURLToPath(import.meta.url));
const snapshot = JSON.parse(
  fs.readFileSync(path.join(root, "shopify-target-products-2026-07-25.json"), "utf8"),
);
const imageDir = path.join(root, "visuels-2026-07-25", "generated");

const explicit = {
  "Contre-la-montre — Chronographe panda": {
    "Argent · caoutchouc noir": "chrono-argent-caoutchouc-noir",
    "Panda ivoire · aiguille rouge": "chrono-panda-ivoire-aiguille-rouge",
    "Bleu glacier": "chrono-bleu-glacier",
    "Panda inversé · aiguilles acier": "chrono-panda-inverse-aiguilles-acier",
    "Rose poudré": "chrono-rose-poudre",
    "Noir tachymètre · caoutchouc": "chrono-noir-tachymetre-caoutchouc",
    "Turquoise ton sur ton": "chrono-turquoise-ton-sur-ton",
    "Blanc · compteurs cerclés": "chrono-blanc-compteurs-cercles",
    "Gris anthracite": "chrono-gris-anthracite",
    "Turquoise · compteurs noirs": "chrono-turquoise-compteurs-noirs",
    "Compteurs bleus · bracelet bleu": "chrono-compteurs-bleus-bracelet-bleu",
    "Panda inversé · aiguille rouge": "chrono-panda-inverse-aiguille-rouge",
    "Blanc · compteurs gris": "chrono-blanc-compteurs-gris",
    "Vert · caoutchouc vert": "chrono-vert-caoutchouc-vert",
    "Vert · bracelet acier": "chrono-vert-bracelet-acier",
    "Blanc ton sur ton · caoutchouc": "chrono-blanc-ton-sur-ton-caoutchouc",
    "Champagne · bracelet acier": "chrono-champagne-bracelet-acier",
    "Panda · bracelet caoutchouc": "chrono-panda-bracelet-caoutchouc",
    "Noir intégral · caoutchouc": "chrono-noir-integral-caoutchouc",
    "Champagne · bracelet caoutchouc": "chrono-champagne-caoutchouc",
  },
  "Voyageur — GMT automatique": {
    "Or rose · bracelet 5 maillons": "gmt-or-rose-bracelet-5-maillons",
    "Bicolore · bracelet 5 maillons": "gmt-bicolore-bracelet-5-maillons",
    "Bicolore · cadran brun": "gmt-bicolore-cadran-brun",
    "Bicolore · bracelet 3 maillons": "gmt-bicolore-bracelet-3-maillons",
    "Or · bracelet Président": "gmt-or-bracelet-president",
    "Or · bracelet 3 maillons": "gmt-or-bracelet-3-maillons",
  },
  "Intégrale — Sport chic acier": {
    "Turquoise": "integrale-turquoise",
    "Bleu ciel": "integrale-bleu-ciel",
    "Blanc argenté": "integrale-blanc-argente",
    "Noir": "integrale-noir",
    "Bleu nuit": "integrale-bleu-nuit",
    "Vert": "integrale-vert",
    "Brun · boîtier or rose": "integrale-brun-boitier-or-rose",
  },
  "Héritage — Plongeuse vintage 42": {
    "Bleu · lunette bleue": "heritage-bleu-lunette-bleue",
    "Bleu nuit · lunette noire": "heritage-bleu-nuit-lunette-noire",
    "Vert · lunette verte": "heritage-vert-lunette-verte",
  },
  "Bracelet Présidentiel — doré": {
    "Maille fixe · acier": "bracelet-maille-fixe-acier",
    "Maille fixe · acier & or rose": "bracelet-maille-fixe-acier-or-rose",
    "Maille fixe · acier & or": "bracelet-maille-fixe-acier-or",
    "Maille fixe · or jaune": "bracelet-maille-fixe-or-jaune",
    "Maille fixe · or rose": "bracelet-maille-fixe-or-rose",
    "Président · acier": "bracelet-president-acier",
    "Président · noir": "bracelet-president-noir",
    "Président · or rose": "bracelet-president-or-rose",
    "Président · or jaune": "bracelet-president-or-jaune",
    "Président · acier & or rose": "bracelet-president-acier-or-rose",
    "Président · acier & or": "bracelet-president-acier-or",
    "Jubilé · or rose (réf. 12)": "bracelet-jubile-or-rose",
    "Jubilé · acier & or rose": "bracelet-jubile-acier-or-rose",
    "Jubilé · acier & or": "bracelet-jubile-acier-or",
    "Jubilé · or rose (réf. 15)": "bracelet-jubile-or-rose",
    "Jubilé · noir": "bracelet-jubile-noir",
    "Jubilé · acier": "bracelet-jubile-acier",
    "3 rangs · or rose": "bracelet-3-rangs-or-rose",
    "3 rangs · or jaune": "bracelet-3-rangs-or-jaune",
    "3 rangs · acier & or rose": "bracelet-3-rangs-acier-or-rose",
    "3 rangs · noir": "bracelet-3-rangs-noir",
    "3 rangs · acier & or": "bracelet-3-rangs-acier-or",
    "3 rangs · acier": "bracelet-3-rangs-acier",
    "Maille sablée · acier": "bracelet-maille-sablee-acier",
  },
  "Set de tournevis d'horloger — 10 pièces": {
    "Manche moleté · repère couleur": "tournevis-manche-molete-repere-couleur",
    "Manche moleté · tête colorée": "tournevis-manche-molete-tete-coloree",
    "Manche annelé · repère couleur": "tournevis-manche-annele-repere-couleur",
    "Manche annelé · tête colorée": "tournevis-manche-annele-tete-coloree",
    "Manche noir · tête colorée": "tournevis-manche-noir-tete-coloree",
  },
};

function appearance(title, value) {
  if (explicit[title]?.[value]) return explicit[title][value];
  if (title === "Remontoir Bois") {
    const finish = value.replace(/ · [12] montres?$/, "");
    return {
      "Noir laqué": "remontoir-bois-noir-laque",
      Acajou: "remontoir-bois-acajou",
      Ébène: "remontoir-bois-ebene",
      Noyer: "remontoir-bois-noyer",
    }[finish];
  }
  if (title === "Rouleau de Voyage — cuir") {
    const color = value.replace(/ · [123] montres?$/, "");
    return {
      "Cuir noir": "rouleau-cuir-noir",
      "Cuir brun": "rouleau-cuir-brun",
      "Cuir bleu marine": "rouleau-cuir-bleu-marine",
      "Cuir vert": "rouleau-cuir-vert",
    }[color];
  }
  if (title === "Remontoir Collection — 2 à 6 montres") {
    const kind = value.replace(/ · [1246] montres?$/, "");
    return {
      "Bois · noir": "remontoir-collection-bois-noir",
      "Bois · beige": "remontoir-collection-bois-beige",
      "Cuir PU · fermeture à clé": "remontoir-collection-cuir-pu-cle",
      "Bois LED · noir": "remontoir-collection-bois-led-noir",
      "Bois LED · rouge": "remontoir-collection-bois-led-rouge",
    }[kind];
  }
  return undefined;
}

const products = [];
const skipped = [];
const imageByKey = new Map();

for (const product of snapshot.nodes) {
  const optionName = product.options[0]?.name;
  const assignments = [];
  for (const variant of product.variants.nodes) {
    const value = variant.selectedOptions.find((o) => o.name === optionName)?.value;
    const key = appearance(product.title, value);
    if (!key) {
      skipped.push({
        productId: product.id,
        product: product.title,
        variantId: variant.id,
        value,
        sku: variant.sku,
      });
      continue;
    }
    const file = path.join(imageDir, `${key}.jpg`);
    if (!fs.existsSync(file)) throw new Error(`Missing image ${file}`);
    const alt = `${product.title} — ${value} — Maison Noirmont`;
    assignments.push({ variantId: variant.id, value, key, file, alt, sku: variant.sku });
    if (!imageByKey.has(`${product.id}|${key}`)) {
      imageByKey.set(`${product.id}|${key}`, {
        productId: product.id,
        product: product.title,
        key,
        file,
        alt,
      });
    }
  }
  if (assignments.length) {
    products.push({
      productId: product.id,
      product: product.title,
      handle: product.handle,
      assignments,
    });
  }
}

const output = {
  generatedAt: new Date().toISOString(),
  images: [...imageByKey.values()],
  products,
  skipped,
  counts: {
    uniqueImages: imageByKey.size,
    assignedVariants: products.reduce((n, p) => n + p.assignments.length, 0),
    skippedVariants: skipped.length,
  },
};

fs.writeFileSync(
  path.join(root, "visual-manifest-2026-07-25.json"),
  JSON.stringify(output, null, 2) + "\n",
);
console.log(JSON.stringify(output.counts));
