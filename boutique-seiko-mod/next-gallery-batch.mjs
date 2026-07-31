import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const projectRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const outputRoot = path.join(projectRoot, "scratchpad", "noirmont-galeries");
const worklist = JSON.parse(fs.readFileSync(path.join(outputRoot, "worklist.json"), "utf8"));
const batchSize = Number(process.argv[2] ?? 6);

const watchBase = [
  "Use the supplied validated product face as the sole identity reference.",
  "Reproduce exactly the same watch geometry, case, bracelet or strap, hands, indices, subdials, date window, bezel, crown, pushers, colors, finishes and materials.",
  "Do not add, remove or redesign any product feature.",
  "The dial must remain sterile: absolutely no logo, no letters, no words, no Roman numerals, no invented symbols or pseudo-text.",
  "Functional Arabic numerals are allowed only if they already exist on the supplied bezel or date window and must remain coherent.",
  "No text anywhere else in the image.",
  "Square premium editorial product photography, light mineral stone #E7E4DE to chalk #FAFAF7, soft lateral upper-left light, diffuse shadow, restrained luxury French mechanical-watch collection aesthetic.",
].join(" ");

const accessoryBase = [
  "Use the supplied validated product face as the sole identity reference.",
  "Reproduce exactly the same accessory geometry, dimensions, construction, colors, finishes, materials and number of components.",
  "Do not add, remove or redesign any feature of the product.",
  "Absolutely no brand, logo, letters, words, numbers, label, watermark or pseudo-text anywhere.",
  "Square premium editorial product photography, light mineral stone #E7E4DE to chalk #FAFAF7, soft lateral upper-left light, diffuse shadow, restrained luxury French horology-boutique aesthetic.",
].join(" ");

function accessorySituation(handle) {
  if (handle.startsWith("bracelet-")) {
    return "Show the exact bracelet mounted naturally on one simple unbranded sterile watch case, with the bracelet remaining the dominant subject. The dial is plain, out of focus and carries no logo, text, Roman numeral or symbol. No other jewelry.";
  }
  if (handle.startsWith("remontoir-")) {
    return "Show the exact watch winder open and in plausible use, holding the correct capacity suggested by the source where visible. Any watch dial is secondary, softly out of focus, completely sterile and unbranded. The winder remains the dominant subject.";
  }
  if (handle.startsWith("rouleau-") || handle.startsWith("etui-")) {
    return "Show the exact travel case open in plausible use with sterile unbranded watches placed naturally inside. The case and its material remain dominant; watch dials are secondary and out of focus.";
  }
  if (handle.startsWith("coffret-")) {
    return "Show the exact presentation case open in plausible use with a restrained selection of sterile unbranded watches. Preserve the exact case geometry and capacity visible in the source. The case remains dominant.";
  }
  if (handle.startsWith("coussins-")) {
    return "Show the exact presentation cushions in a restrained horology display, with one cushion supporting a sterile unbranded watch. The cushions remain the dominant subject.";
  }
  if (handle.includes("doigtiers")) {
    return "Show the exact finger cots worn correctly on two anatomically normal fingertips while handling one small neutral watch component. Natural hand anatomy, normal nails, no extra fingers, no jewelry.";
  }
  if (handle.includes("loupe")) {
    return "Show the exact loupe in plausible inspection use beside a plain unbranded mechanical movement, with the loupe dominant and no readable markings.";
  }
  if (
    handle.includes("tournevis") ||
    handle.includes("outil-") ||
    handle.includes("pince-") ||
    handle.includes("barrettes") ||
    handle.includes("kit-")
  ) {
    return "Show the exact tool or set in plausible watchmaking use on a pale neutral work mat beside an unbranded bracelet or watch component. If a hand is visible, it is anatomically normal, relaxed, and free of jewelry. The accessory remains dominant.";
  }
  return "Show the exact accessory in a restrained, plausible horology-use scene with no decorative prop and no branding. The product remains dominant.";
}

function buildPrompt(job) {
  if (job.famille === "montre") {
    if (job.slot === "02-situation") {
      return `${watchBase} SLOT SITUATION: show the complete watch resting naturally on one pale limestone slab, with at most one subtle folded unbranded chalk-linen edge far in the background. The product dominates the frame. No other object, no jewelry, no packaging.`;
    }
    if (job.slot === "03-macro") {
      return `${watchBase} SLOT MACRO: create a tight true photographic macro of this exact watch, focusing on its real case finishing, crown or pushers if present, bezel edge if present, dial texture, indices and bracelet or strap texture. Keep enough of the product visible to prove identity. No overlay or annotation.`;
    }
    return `${watchBase} SLOT WRIST: show this exact watch worn on one anatomically correct adult wrist and forearm only, never a face. Neutral solid charcoal or chalk sleeve, no pattern and no brand, no other jewelry and no second watch. Hand relaxed and slightly closed; fingers together and mostly outside the crop. Exactly one hand, five normal fingers if visible, natural nails and wrist joint. Watch face clearly visible and dominant.`;
  }
  if (job.slot === "02-situation") {
    return `${accessoryBase} SLOT SITUATION: ${accessorySituation(job.handle)} No packaging and no gift decoration.`;
  }
  return `${accessoryBase} SLOT MACRO: create a tight true photographic macro of the most distinctive real material and construction detail visible in the source: grain, brushing, polished edge, weave, stitching, hinge, clasp, knurling or tooling as appropriate. Keep enough context to prove the exact product identity. No overlay or annotation.`;
}

const pending = worklist.jobs
  .filter((job) => !fs.existsSync(job.fichier))
  .slice(0, batchSize)
  .map((job) => ({ ...job, prompt: buildPrompt(job) }));

process.stdout.write(JSON.stringify({
  pendingTotal: worklist.jobs.filter((job) => !fs.existsSync(job.fichier)).length,
  batch: pending,
}));
