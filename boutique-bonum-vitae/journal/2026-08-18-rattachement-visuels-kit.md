# 18/08/2026 — Rattachement des 6 visuels kit 600 GPD

Hakim a déposé le pack Codex
`livraisons/visuels-kit-entretien-600-gpd/`. Contrôle indépendant puis rattachement
sur le brouillon — même recette que le LPS.

## Contrôle (avant écriture)

| # | Brief | Constat |
|---|---|---|
| 1 | Packshot héros Shopping | 4 types nuls, membrane bleue en avant, lin/bois, 0 texte |
| 2 | Situation placard | plateau + sous-évier ouvert, aucune machine catalogue |
| 3 | Geste | mains + membrane, pas de boîtier 299 € |
| 4 | Macro | gaine bleue + joint noir, pas d'intérieur inventé |
| 5 | Contexte foyer | 4 pièces dans un bac, cuisine claire |
| 6 | Contenu carton | **2 PP + 2 PPC + 1 membrane + 2 inline** |

Format : 6 × JPEG 2048² sRGB, checksums = `manifeste.json`. Voie C tenue
(OSWNKW / PP / PPC / RTL / pH / 4000 L / 0,0001 µm absents).

## Périmètre

- Produit `11039467503954` / `kit-entretien-osmoseur-600-gpd`
- Statut **DRAFT** avant et après (pas d'activation)
- Boutique `kw7vak-g0` uniquement

## Écritures

1. Backup galerie DSers : `backups/2026-08-18-rattachement-kit/medias-avant.json`
2. `stagedUploadsCreate` + POST GCS : 6 × HTTP 201
3. `productCreateMedia` : 6 MediaImage, 0 `mediaUserErrors`
4. `productReorderMedia` : image 1 en position 0
5. `fileUpdate` + `referencesToRemove` sur les 6 brutes DSers — **0 `fileDelete`**,
   fichiers restés `READY`
6. `productVariantAppendMedia` : 4 variantes liées à l'image 1
   (`productVariantDetachMedia` inutile : le détachement produit avait déjà
   vidé les liaisons variante)

## Constaté API après coup

| Position | Fichier | Featured | 2048² |
|---|---|---|---|
| 1 | `kit-entretien-osmoseur-600-gpd-1.jpg` | **oui** | oui |
| 2 | `kit-entretien-osmoseur-600-gpd-2.jpg` | | oui |
| 3 | `kit-entretien-osmoseur-600-gpd-3.jpg` | | oui |
| 4 | `kit-entretien-osmoseur-600-gpd-4.jpg` | | oui |
| 5 | `kit-entretien-osmoseur-600-gpd-5.jpg` | | oui |
| 6 | `kit-entretien-osmoseur-600-gpd-6.jpg` | | oui |

Alts FR du manifeste posés. Aucune brute fournisseur (OSWNKW, claims, cotes)
n'est plus sur la fiche. Les fichiers DSers existent encore dans Files (réversibles).

IDs : `backups/2026-08-18-rattachement-kit/new-media-ids.json`.

## Non fait

Activation / publication. Commande test compat 299 € / 449 €. Reconfirm coût rendu.
Comptoir reporté.
