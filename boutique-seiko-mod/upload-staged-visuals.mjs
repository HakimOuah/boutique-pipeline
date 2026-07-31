import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.dirname(fileURLToPath(import.meta.url));
const manifest = JSON.parse(
  fs.readFileSync(path.join(root, "visual-manifest-2026-07-25.json"), "utf8"),
);
const response = JSON.parse(
  fs.readFileSync(path.join(root, "shopify", "staged-uploads.response.json"), "utf8"),
);
const targets = response.stagedUploadsCreate?.stagedTargets ?? [];

if (targets.length !== manifest.images.length) {
  throw new Error(`Target/image mismatch: ${targets.length}/${manifest.images.length}`);
}

const results = new Array(targets.length);
let cursor = 0;

async function worker() {
  while (cursor < targets.length) {
    const index = cursor++;
    const target = targets[index];
    const image = manifest.images[index];
    const upload = await fetch(target.url, {
      method: "PUT",
      headers: { "Content-Type": "image/jpeg" },
      body: fs.readFileSync(image.file),
    });
    const body = await upload.text();
    results[index] = {
      index,
      key: image.key,
      file: image.file,
      resourceUrl: target.resourceUrl,
      status: upload.status,
      ok: upload.ok,
      responseBody: body,
    };
    if (!upload.ok) {
      throw new Error(`Upload failed for ${image.key}: ${upload.status} ${body}`);
    }
  }
}

await Promise.all(Array.from({ length: 8 }, () => worker()));
fs.writeFileSync(
  path.join(root, "shopify", "staged-uploads.put-results.json"),
  `${JSON.stringify(results, null, 2)}\n`,
);
console.log(JSON.stringify({
  uploaded: results.filter((result) => result.ok).length,
  failed: results.filter((result) => !result.ok).length,
}, null, 2));
