#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";

const repoRoot = process.cwd();
const mappingPath = path.join(
  repoRoot,
  "boutique-seiko-mod/MAPPING-92-REMPLACEMENTS-ALIEXPRESS-LIVE-2026-08-11.json",
);
const inboxDir = path.join(repoRoot, "ordres/pour-codex/inbox");
const mapping = JSON.parse(fs.readFileSync(mappingPath, "utf8"));

const batchPlan = [
  ["cadran-meteorite-28-5", "meteorite-9", 0, 9],
  ["cadran-pilote-29-mod-nh35", "pilote29-11", 0, 11],
  ["cadran-pilote-33-5-aiguilles-blanches", "pilote-blanches-5", 0, 5],
  ["cadran-pilote-33-5-aiguilles-lumineuses", "pilote-lumineuses-a-7", 0, 7],
  ["cadran-pilote-33-5-aiguilles-lumineuses", "pilote-lumineuses-b-6", 7, 13],
  ["cadran-pilote-noir-33-5-nh34", "pilote-nh34-6", 0, 6],
  ["cadran-sterile-couronne-3h-28-5", "sterile-couronne-7", 0, 7],
  ["cadran-sterile-lumineux-28-5", "sterile-lumineux-a-9", 0, 9],
  ["cadran-sterile-lumineux-28-5", "sterile-lumineux-b-8", 9, 17],
  ["cadran-sterile-sunburst-28-5", "sterile-sunburst-12", 0, 12],
  ["cadran-vierge-sterile-28-5", "vierge-sterile-12", 0, 12],
];

const productRules = {
  "cadran-meteorite-28-5": [
    "Cadran seul, vu de face, centré. Préserver exactement teinte, texture météorite, index, minuterie, chiffres, ouverture de date et couleur de lume propres à chaque source SKU.",
    "Les cartouches, vignettes de lume, mentions NH34, flèches et textes de démonstration appartiennent à la photographie fournisseur et ne doivent pas apparaître dans la nouvelle composition.",
  ],
  "cadran-pilote-29-mod-nh35": [
    "Respecter le type indiqué par le SKU : `dial` = cadran seul sans aiguilles ; `hands` = jeu d'aiguilles seul sans cadran ; `set` = cadran exact avec son jeu d'aiguilles exact. Aucun composant ne doit migrer d'une entrée à l'autre.",
    "Préserver l'ordre complet des chiffres 1-12 et 13-24, la minuterie, l'ouverture date à 3 h, le triangle à 12 h, la teinte et toute inscription physiquement imprimée sur le produit source exact. Ne jamais ajouter une inscription absente.",
  ],
  "cadran-pilote-33-5-aiguilles-blanches": [
    "Respecter le type indiqué par le SKU : cadran seul, aiguilles seules ou cadran avec aiguilles. Préserver les chiffres 1-12, la minuterie, les repères jaunes éventuels et le symbole constitutif du cadran exactement comme dans la source homologue.",
    "Le logo et le mot Tandorio situés hors produit sont un filigrane photographique fournisseur : ils doivent disparaître dans la nouvelle composition, sans altérer le cadran ni les aiguilles.",
  ],
  "cadran-pilote-33-5-aiguilles-lumineuses": [
    "Respecter le type indiqué par le SKU : cadran seul, aiguilles seules ou cadran avec aiguilles. Préserver chiffres 1-12 et 13-24, minuterie 5-60, teinte du cadran, points de lume, couleur et géométrie exactes des aiguilles.",
    "Le logo et le mot Tandorio situés hors produit sont un filigrane photographique fournisseur : ils doivent disparaître dans la nouvelle composition. Aucun jeu d'aiguilles ne doit être transféré vers une autre variante.",
  ],
  "cadran-pilote-noir-33-5-nh34": [
    "Respecter le type indiqué par le SKU : `Dial` = cadran seul ; `hand` = cadran exact avec son jeu d'aiguilles exact. Préserver chiffres, minuterie, triangles, points et couleurs de lume dans leur ordre et leur position source.",
    "Ne jamais confondre les trois géométries de cadran ni inventer un repère, une aiguille, une ouverture de date ou une inscription.",
  ],
  "cadran-sterile-couronne-3h-28-5": [
    "Cadran seul vu de face. Préserver exactement la teinte, la finition, le trou central, l'ouverture de date à 3 h et tous les index ou repères physiques de chaque source SKU.",
    "Le filigrane `Goutent Official Store` appartient à la photo fournisseur et doit disparaître uniquement grâce à une nouvelle composition complète, jamais par gommage ou inpainting.",
  ],
  "cadran-sterile-lumineux-28-5": [
    "Cadran seul vu de face. Préserver exactement teinte, finition, nombre et forme des index, trou central, ouverture date éventuelle et teinte de lume propres à chaque source SKU.",
    "Les mentions FIT, Size, NH35/8215/2836, les vignettes nocturnes et les encarts de démonstration appartiennent à la photographie fournisseur et ne doivent pas apparaître dans la nouvelle composition.",
  ],
  "cadran-sterile-sunburst-28-5": [
    "Disque de cadran intégralement vierge vu de face : conserver exactement la teinte soleillée et le seul trou central. Aucun index, chiffre, ouverture de date ou inscription ne doit être ajouté.",
    "Le filigrane `BellaTime` appartient à la photographie fournisseur et doit disparaître uniquement grâce à une nouvelle composition complète, jamais par gommage ou inpainting.",
  ],
  "cadran-vierge-sterile-28-5": [
    "Disque de cadran vierge vu de face : conserver exactement la teinte, la finition, le trou central et l'ouverture rectangulaire de date à 3 h. Aucun index, chiffre ou inscription ne doit être ajouté.",
    "Le filigrane `Jin Ming` appartient à la photographie fournisseur et doit disparaître uniquement grâce à une nouvelle composition complète, jamais par gommage ou inpainting. Distinguer fidèlement les deux bleus A1 et A2.",
  ],
};

const universalConstraints = [
  "VÉRITÉ PRODUIT PAR ENTRÉE : utiliser exclusivement le chemin `source` de l'entrée manifeste correspondante. Une source ne peut servir qu'à son fichier cible et à ses variantes explicitement mappées.",
  "La photographie fournisseur sert uniquement de référence produit. Produire une nouvelle composition Maison Noirmont complète : fond minéral clair pierre-vers-craie, lumière douce haute-gauche, ombre diffuse, produit centré et intégralement visible.",
  "Supprimer de la nouvelle composition uniquement les éléments photographiques extérieurs au produit : filigranes, logos de boutique, textes promotionnels, encarts, vignettes, outils, emballages et arrière-plan fournisseur. Aucun gommage, clonage ni inpainting de la source n'est admis.",
  "Préserver tout élément constitutif physiquement présent sur le produit source exact, y compris chiffres, repères, minuterie, texture, ouvertures, symboles et inscriptions génériques. Ne jamais inventer, corriger, déplacer, masquer ou transférer un élément physique.",
  "Aucun nom de marque, logo fournisseur, filigrane, texte promotionnel ou caractère parasite ajouté sur le produit ou le fond final. Les chiffres et symboles constitutifs prouvés par la source restent autorisés et obligatoires.",
  "Conserver un cadrage, une orientation, une échelle et une lumière identiques dans le lot. Les cadrans sont parfaitement de face et les jeux d'aiguilles seuls sont disposés proprement sans cadran ni composant inventé.",
  "Sortie 2048 × 2048 px, JPEG sRGB qualité environ 90, viser 400-900 Ko et respecter exactement le nom `fichier` du manifeste.",
];

const universalQa = [
  "Contrôle source↔rendu entrée par entrée, en résolution originale : type exact (cadran, aiguilles ou ensemble), teinte, texture, géométrie, chiffres, index, minuterie, ouvertures, symboles, inscriptions constitutives et composants.",
  "Contrôle bloquant : aucun filigrane, logo de boutique/fournisseur, texte promotionnel, vignette, encart, outil, emballage, trace de gommage ou caractère parasite.",
  "Contrôle bloquant : aucune permutation entre SKU ; aucun index, chiffre, trou, ouverture, aiguille, date, symbole ou inscription physique ajouté, retiré, déplacé ou masqué.",
  "Planche de contrôle du lot, au moins 740 px par vignette, avec noms de fichiers lisibles, afin de comparer fidélité et homogénéité de cadrage/échelle.",
  "Contrôle fichier : nom exact du manifeste, 2048 × 2048, 1:1 strict, JPEG sRGB et poids conforme. Tout candidat ambigu ou non prouvable est rejeté et n'entre pas dans le manifeste réalisé.",
];

function targetListFor(handle) {
  return mapping.targets.filter((target) => target.handle === handle);
}

const allSelected = [];
for (const [handle, slug, start, end] of batchPlan) {
  const full = targetListFor(handle);
  const selected = full.slice(start, end);
  if (selected.length !== end - start) {
    throw new Error(`${slug}: expected ${end - start}, got ${selected.length}`);
  }
  allSelected.push(...selected.map((target) => target.target_path));

  const manifest = selected.map((target) => ({
    handle: target.handle,
    sku: target.sku_keys.join(" | "),
    slot: target.slot,
    fichier: target.target_file,
    source: target.source_path,
  }));
  const order = {
    id: `codex-20260811-1227-remplacement92-${slug}`,
    type: "generate_images",
    created_at: "2026-08-11T12:27:00+02:00",
    requested_by: "codex",
    payload: {
      manifest,
      sources: manifest.map((entry) => entry.source),
      da: {
        reference: "docs/codex-handoff/15-CODEX-EXECUTANT-IMAGES.md §3",
        surcharges: [
          "Visuel de variante carré 1:1, source exacte par entrée, produit isolé sur le fond minéral clair Maison Noirmont, lumière douce haute-gauche et ombre diffuse.",
          "Toutes les images d'un même lot gardent cadrage, échelle, orientation, fond et lumière identiques ; seuls les attributs physiques prouvés par la source SKU varient.",
        ],
      },
      contraintes: {
        reference: "docs/codex-handoff/15-CODEX-EXECUTANT-IMAGES.md §4",
        specifiques: [...productRules[handle], ...universalConstraints],
      },
      qa_attendue: {
        reference: "docs/codex-handoff/15-CODEX-EXECUTANT-IMAGES.md §5",
        specifiques: universalQa,
      },
      sortie: {
        dossier: `boutique-seiko-mod/visuels-codex-2026-08/${handle}`,
        manifeste: `manifeste-remplacement92-${slug}.json`,
      },
    },
    notes: "Remplacement des 92 médias fournisseur retenus : génération locale uniquement. Ne toucher ni Shopify, ni DSers, ni prix, ni statut. Le rattachement Shopify sera réalisé séparément après QA indépendante.",
  };

  const fileName = `20260811-1227-generate_images-remplacement92-${slug}.json`;
  const outputPath = path.join(inboxDir, fileName);
  if (fs.existsSync(outputPath)) {
    throw new Error(`Order already exists: ${outputPath}`);
  }
  fs.writeFileSync(outputPath, `${JSON.stringify(order, null, 2)}\n`);
}

const expected = mapping.targets.map((target) => target.target_path).sort();
const actual = allSelected.sort();
if (JSON.stringify(expected) !== JSON.stringify(actual)) {
  throw new Error("Batch plan does not cover the 92 mapping exactly once");
}

console.log(`Wrote ${batchPlan.length} orders covering ${actual.length} targets exactly once.`);
