import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.dirname(fileURLToPath(import.meta.url));
const shopifyDir = path.join(root, "shopify");
const manifest = JSON.parse(
  fs.readFileSync(path.join(root, "visual-manifest-2026-07-25.json"), "utf8"),
);
const staged = JSON.parse(
  fs.readFileSync(path.join(shopifyDir, "staged-uploads.response.json"), "utf8"),
);
const targets = staged.stagedUploadsCreate?.stagedTargets ?? [];

if (targets.length !== manifest.images.length) {
  throw new Error(`Target/image mismatch: ${targets.length}/${manifest.images.length}`);
}

const resourceByKey = new Map(
  manifest.images.map((image, index) => [image.key, targets[index].resourceUrl]),
);
const outputFiles = [];

for (const product of manifest.products.filter((entry) => entry.assignments.length > 0)) {
  const images = manifest.images.filter((image) => image.productId === product.productId);
  const variables = {
    productId: product.productId,
    variants: product.assignments.map((assignment) => ({ id: assignment.variantId })),
    media: images.map((image) => ({
      originalSource: resourceByKey.get(image.key),
      alt: image.alt,
      mediaContentType: "IMAGE",
    })),
  };
  const numericId = product.productId.split("/").at(-1);
  const outputPath = path.join(shopifyDir, `product-media-add-${numericId}.variables.json`);
  fs.writeFileSync(outputPath, `${JSON.stringify(variables, null, 2)}\n`);
  outputFiles.push({
    productId: product.productId,
    product: product.product,
    images: images.length,
    variants: product.assignments.length,
    variables: outputPath,
  });
}

fs.writeFileSync(
  path.join(shopifyDir, "product-media-add-index.json"),
  `${JSON.stringify(outputFiles, null, 2)}\n`,
);
console.log(JSON.stringify(outputFiles, null, 2));
