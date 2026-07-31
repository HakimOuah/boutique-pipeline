import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.dirname(fileURLToPath(import.meta.url));
const manifestPath = path.join(root, "visual-manifest-2026-07-25.json");
const shopifyDir = path.join(root, "shopify");
const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf8"));

if (manifest.counts.uniqueImages !== 77 || manifest.counts.assignedVariants !== 118) {
  throw new Error(`Unexpected manifest counts: ${JSON.stringify(manifest.counts)}`);
}

for (const image of manifest.images) {
  const stats = fs.statSync(image.file);
  if (!stats.isFile() || stats.size === 0) {
    throw new Error(`Missing or empty image: ${image.file}`);
  }
}

const stageVariables = {
  input: manifest.images.map((image) => ({
    resource: "IMAGE",
    filename: path.basename(image.file),
    mimeType: "image/jpeg",
    httpMethod: "PUT",
    fileSize: String(fs.statSync(image.file).size),
  })),
};

fs.writeFileSync(
  path.join(shopifyDir, "staged-uploads.variables.json"),
  `${JSON.stringify(stageVariables, null, 2)}\n`,
);

fs.writeFileSync(
  path.join(shopifyDir, "verify-products.variables.json"),
  `${JSON.stringify({ ids: manifest.products.map((product) => product.productId) }, null, 2)}\n`,
);

console.log(JSON.stringify({
  images: manifest.images.length,
  assignedVariants: manifest.counts.assignedVariants,
  stagedVariables: path.join(shopifyDir, "staged-uploads.variables.json"),
}, null, 2));
