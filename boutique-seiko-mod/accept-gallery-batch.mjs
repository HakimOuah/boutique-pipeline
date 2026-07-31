import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const projectRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const rawRoot = path.join(projectRoot, "scratchpad", "noirmont-galeries", "generated-raw");
fs.mkdirSync(rawRoot, { recursive: true });

const argument = process.argv[2];
const payload = JSON.parse(
  argument.startsWith("uri:")
    ? decodeURIComponent(argument.slice(4))
    : Buffer.from(argument, "base64url").toString("utf8"),
);
const accepted = [];
for (const item of payload) {
  const target = item.job.fichier;
  const rawTarget = path.join(rawRoot, `${path.basename(target, ".jpg")}.png`);
  fs.copyFileSync(item.generatedPath, rawTarget);
  execFileSync("sips", [
    "-s", "format", "jpeg",
    "-s", "formatOptions", "90",
    "-z", "2048", "2048",
    rawTarget,
    "--out", target,
  ], { stdio: "ignore" });
  accepted.push({ target, rawTarget, bytes: fs.statSync(target).size });
}
console.log(JSON.stringify({ accepted: accepted.length, files: accepted }, null, 2));
