# `183789` refaite, et les puissances versées à la description

Date : **04/09/2026 (nuit)** · Boutique : **Lumière Matière** · Ticket **T-06 — clos**
Brief : `briefs/2026-09-05-codex-183789-refonte.md`. Livraison Codex : 7 visuels.

**7 images importées, 2 variantes rattachées, description réécrite.** La fiche passe de
**2 images** à **9**, toutes justes. Contrôle : 52 produits / 158 variantes / SKU DSers intacts.

## Le comptage, vérifié avant import

C'était le seul critère qui comptait. Recompté à pleine résolution :

| Image | Attendu | Compté |
|---|---|---|
| `g1`–`g5` | `4+1` = 5 points | **5** ✓ |
| `gris-6-lumieres-g1` | `5+1` = 6 points | **6** ✓ |
| `blanc-6-lumieres-g1` | `5+1` = 6 points | **6** ✓ |

Les versions à 6 sont visiblement plus étalées que celles à 5, ce qui colle aux 89 cm contre
79 cm annoncés. Aucune image à sept palets ne subsiste sur la fiche.

**Ce qui a fait la différence dans le brief** : avoir écrit les consignes dans la notation du
fournisseur, `4+1` et `5+1` — périphériques puis central — au lieu de « 5 lumières » et
« 6 lumières ». C'est cette notation qui rend l'erreur impossible à répéter : une image à sept
palets est un `6+1`, et on voit tout de suite que la fiche n'en vend pas.

## État final de la fiche

Galerie : `g1`–`g5` puis les quatre packshots de variante. Hero = `g1`, un gris `4+1` allumé,
donc l'image du flux Google Shopping montre enfin un produit réellement vendu. Les quatre
variantes portent chacune **sa** photo :

| Variante | SKU | Image |
|---|---|---|
| `5 lumières · Gris` | `…795:173` | gris `4+1` |
| `5 lumières · Blanc` | `…795:691` | blanc `4+1` |
| `6 lumières · Gris` | `…795:366` | gris `5+1` |
| `6 lumières · Blanc` | `…795:10` | blanc `5+1` |

## Les puissances et surfaces versées à la description

Les plaques fournisseur portaient des données d'achat que la fiche n'annonçait nulle part.
Ajoutées, en distinguant ce qui est documenté de ce qui ne l'est pas :

| Version | Largeur | Hauteur | Puissance | Flux | Surface conseillée |
|---|---|---|---|---|---|
| 5 lumières, gris et blanc | 79 cm | 14 cm | **40 W** | **3 600 lm** | **10 à 15 m²** |
| 6 lumières gris | 89 cm | 14 cm | **48 W** | **4 320 lm** | **15 à 20 m²** |
| 6 lumières blanc | 80 cm | **17 cm** | **72 W** | *non donné* | *non donné* |

**L'asymétrie est conservée telle quelle.** Le blanc à 6 lumières vient d'une autre plaque
fournisseur : ni flux ni surface n'y figurent, et la description le dit — « le fabricant n'en
donne ni le flux lumineux ni la surface conseillée, nous ne les inventons pas ». Harmoniser
aurait été plus élégant et faux.

La description mentionne aussi la structure en clair : « quatre palets en périphérie et un au
centre ». C'est ce qui manquait pour qu'un client comprenne l'écart entre les deux tailles.

`seo.description` reprise : « 40 à 72 W selon la version ».

## Les autres fiches : rien à verser

Recherche faite dans les preuves DOM des lots 3 et 4 : **aucune autre fiche ne porte de données
de puissance, de flux ou de surface**. Sur `183789` l'information était incrustée dans les
plaques, pas dans le DOM — c'est en les lisant pour cadrer le brief qu'elle est apparue.

Les verser ailleurs demanderait une passe de scraping dédiée sur les plaques des fiches LED.
Ça vaut probablement le coup — c'est de l'information d'achat vérifiable sur des produits à
199 € — mais c'est un chantier à part, pas un effet de bord de celui-ci.

## Reste ouvert

1. **`934110`** — confirmation fournisseur avant tout libellé ou visuel.
2. **`193329` / `338324`** — le même article à 199 € sur deux listings AliExpress.
3. **Puissances des autres fiches LED** — passe de scraping à décider.
