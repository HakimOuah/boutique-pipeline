# 17/08/2026 (nuit) — Rattachement des 6 visuels LPS

Hakim : « Garde tout et rattache tout » — image 5 incluse, malgré la réserve de topologie.

## Périmètre

- Produit `11036961964370` / `anti-tartre-galvanique-toute-la-maison`
- Statut **DRAFT** avant et après (pas d'activation)
- Boutique `kw7vak-g0` uniquement

## Écritures

1. Backup galerie DSers : `backups/2026-08-17-rattachement-lps/medias-avant.json`
2. `stagedUploadsCreate` + POST GCS : 6 × HTTP 201
3. `productCreateMedia` : 6 MediaImage, 0 `mediaUserErrors`
4. `productReorderMedia` : image 1 en position 0
5. `fileUpdate` + `referencesToRemove` sur les 6 brutes DSers — **0 `fileDelete`**,
   fichiers restés `READY`
6. `productVariantAppendMedia` : variante unique liée à l'image 1

## Constaté API après coup

| Position | Fichier | Featured | 2048² |
|---|---|---|---|
| 1 | `anti-tartre-galvanique-1.jpg` | **oui** | oui |
| 2 | `anti-tartre-galvanique-2.jpg` | | oui |
| 3 | `anti-tartre-galvanique-3.jpg` | | oui |
| 4 | `anti-tartre-galvanique-4.jpg` | | oui |
| 5 | `anti-tartre-galvanique-5.jpg` | | oui |
| 6 | `anti-tartre-galvanique-6.jpg` | | oui |

Alts FR du manifeste posés. Aucune brute fournisseur (drapeau / FDA / NSF / 86 %)
n'est plus sur la fiche. Les fichiers DSers existent encore dans Files (réversibles).

IDs nouveaux : `backups/2026-08-17-rattachement-lps/new-media-ids.json`.

## Non fait

Prix, publication Boutique en ligne, canal Google. Toujours T-H7 + feu vert Hakim.
