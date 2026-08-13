# Maison Noirmont — grille de prix et marges réelles

**Établie le 14/08/2026.** Document de référence du pricing. Périmètre : **les 96 fiches actives**
(57 montres, 39 accessoires dont la carte cadeau).

> ⛔ **Aucun prix n'a été écrit sur Shopify.** Ce document est une proposition ; l'application
> attend l'arbitrage de Hakim (T-H3).
> ⛔ **Aucun `compareAtPrice`.** Les 931 prix barrés purgés le 08/08 ne sont pas réintroduits :
> aucune ligne de ce document ne prévoit de prix de référence.

Sources : `NOTES-PRICING.md` §1 et §2 bis · `journal/2026-08-14-verification-serp-montres.md` (16 SERP
du 14/08) · `journal/2026-08-14-verification-serp.md` (accessoires) · `journal/2026-08-14-etude-maisondutemps.md` ·
coûts `inventoryItem.unitCost` lus sur Shopify en lecture seule le 14/08 · registre de sourcing
`boutique-pipeline/reports/phase4*-2026-07-24.md` pour les coûts absents de Shopify.

---

## 1. La règle appliquée

**Se placer juste en dessous du concurrent qui vend le même produit que nous** — même type de
mouvement, même gamme, **même absence de récit de marque**.

**Sont écartés du choix du comparable**, parce qu'ils vendent autre chose que nous :

| Écarté | Pourquoi |
|---|---|
| **Marques officielles** — Seiko, Tissot, Citizen, Orient, Pierre Lannier, Fossil, Lotus, Tudor, Rolex | On ne vend pas leur nom. Leur prix est un prix de marque. |
| **Marques à récit national** — Charlie Paris (445 €, « Assemblée en France » dans ses dix titres), Herbelin | **À 445 € on vend un pays, pas une montre.** Nous n'avons pas cet argument. |
| **Bas de gamme marketplace** — Amazon, AliExpress, Songmics, Steampunk Store, HelloIce, faussesmontres.com | Ni le produit, ni la promesse, ni la marge. |
| **Grandes surfaces de bricolage** — Leroy Merlin, Conrad | Ils occupent l'outillage et une partie du rangement. Pas notre acheteur. |

### Le piège que cette règle évite

Sur le **squelette**, la bande est **bimodale** : un socle 25-300 €, puis **un palier unique à 445 €
tenu par Charlie Paris seul**, et **rien entre 300 et 440 €**. Se placer « juste sous le plus cher »
nous mettrait à **429 €, dans le vide où personne n'achète** — c'est exactement où nous sommes
aujourd'hui. Le comparable est l'indépendant sans récit de fabrication : **`maisondutemps.com`,
285-295 €**. D'où la cible : **279 €, pas 429 €**.

### Les ancrages retenus, famille par famille

| Famille | Concurrent comparable | Prix relevé | Ancrage cible | Pourquoi lui |
|---|---|---|---|---|
| Montres squelette | `maisondutemps.com` — MTBeta Skeleton | **285-295 €** | **279 €** | Indépendant, sans marque, **1ᵉʳ organique sur `montre squelette automatique`** |
| Chronographes | **GT Watches — GT1 Chrono** | **249 €** | **239 €** | 40 mm, acier 316L, verre saphir, **méca-quartz VK63** : notre produit trait pour trait |
| GMT | Time2Seiko 360 € · Watchmodcustom 432,90 € | **319-599 €** | **349 → 419 €** | Sept ateliers français de mod tiennent la bande. **La seule famille où notre prix est déjà le bon.** |
| Classiques 39-42 mm | Montignac 289-339 € · `maisondutemps` 295 € | **190-340 €** | **279 → 329 €** | Les deux seuls indépendants sans récit de la page 1 de `montre automatique homme` |
| Classiques 36 mm | **Gustave & Cie** (`montre 36mm homme`) | **245 €** | **239 → 259 €** | Indépendant français, même cote, sans marque |
| Sport chic bracelet intégré | SILA Paris | **175-210 €** | ⛔ **sous notre coût** — voir §4 | Le comparable existe, il est simplement inatteignable |
| Boîtes et coffrets | Royaume de la Boîte | **55-99 €** | **69,90 → 99,90 €** | Indépendant qui **gagne l'organique** ; Songmics à 19-27 € est écarté |
| Étuis et rouleaux | `etui montre` — maisondutemps/watchroll, Le Tanneur, Lucrin | **11-150 €** | **39,90 → 149,90 €** | Le Français dit « étui », pas « rouleau de voyage » |
| Remontoirs | Indépendants qui gagnent l'organique | **68-270 €** | **64,90 → 269,90 €** | Bande complète 21,99-840 €, mais l'organique vit entre 68 et 270 € |
| Bracelets | Spécialistes (bracelet-montre.eu, Maison Fèvre, Montre.com…) | **4,99-120 €** | inchangé pour l'essentiel | ⚠️ **Aucun relevé par type de bracelet** — seule la bande globale est connue |
| Outillage | `outil montre` / `kit horlogerie` | **4-30 €** | inchangé | ⛔ **AliExpress se classe en organique** : aucune marge défendable |

---

## 2. Étape 1 — le prix cible, fiche par fiche

Lecture des colonnes : **Prix cible** = prix d'entrée, et le haut de gamme quand la fiche a plusieurs
paliers. **Écart** = variation du prix d'entrée. **Coût rendu** = coût produit + fret France.
**Marge HT** et **Marge %** sont calculées **au prix d'entrée** (le cas le plus défavorable).
La formule est au §3.

#### Squelette

| Fiche | Comparable | Prix relevé | Prix actuel | **Prix cible** | Écart | Coût rendu | Marge HT | Marge % | Coef. |
|---|---|---|---|---|---|---|---|---|---|
| `montre-squelette-automatique-carree` | maisondutemps MTBeta Skeleton | 285-295 € | 399 € | **279 €** | -120 € | 111,86 € | 116,48 € | 50,1 % | 2,49 |
| `montre-squelette-automatique-octogone` | maisondutemps MTBeta Skeleton | 285-295 € | 399-429 € | **279 € → 299 €** | -120 € | 120,76 € | 107,58 € | 46,3 % | 2,31 |

#### Chronographe VK63

| Fiche | Comparable | Prix relevé | Prix actuel | **Prix cible** | Écart | Coût rendu | Marge HT | Marge % | Coef. |
|---|---|---|---|---|---|---|---|---|---|
| `contre-la-montre-argent-chronographe` | GT Watches GT1 Chrono VK63 | 249 € | 299 € | **239 €** | -60 € | 60,68 € | 134,89 € | 67,7 % | 3,94 |
| `contre-la-montre-blanc-chronographe` | GT Watches GT1 Chrono VK63 | 249 € | 299 € | **239 €** | -60 € | 60,68 € | 134,89 € | 67,7 % | 3,94 |
| `contre-la-montre-bleu-glacier-chronographe` | GT Watches GT1 Chrono VK63 | 249 € | 299 € | **239 €** | -60 € | 60,68 € | 134,89 € | 67,7 % | 3,94 |
| `contre-la-montre-champagne-chronographe` | GT Watches GT1 Chrono VK63 | 249 € | 299 € | **239 €** | -60 € | 60,68 € | 134,89 € | 67,7 % | 3,94 |
| `contre-la-montre-compteurs-bleus-chronographe` | GT Watches GT1 Chrono VK63 | 249 € | 299 € | **239 €** | -60 € | 60,68 € | 134,89 € | 67,7 % | 3,94 |
| `contre-la-montre-gris-anthracite-chronographe` | GT Watches GT1 Chrono VK63 | 249 € | 299 € | **239 €** | -60 € | 60,68 € | 134,89 € | 67,7 % | 3,94 |
| `contre-la-montre-noir-chronographe` | GT Watches GT1 Chrono VK63 | 249 € | 299 € | **239 €** | -60 € | 60,68 € | 134,89 € | 67,7 % | 3,94 |
| `contre-la-montre-panda-chronographe` | GT Watches GT1 Chrono VK63 | 249 € | 299 € | **239 €** | -60 € | 60,68 € | 134,89 € | 67,7 % | 3,94 |
| `contre-la-montre-panda-inverse-chronographe` | GT Watches GT1 Chrono VK63 | 249 € | 299 € | **239 €** | -60 € | 60,68 € | 134,89 € | 67,7 % | 3,94 |
| `contre-la-montre-rose-poudre-chronographe` | GT Watches GT1 Chrono VK63 | 249 € | 299 € | **239 €** | -60 € | 60,68 € | 134,89 € | 67,7 % | 3,94 |
| `contre-la-montre-turquoise-chronographe` | GT Watches GT1 Chrono VK63 | 249 € | 299 € | **239 €** | -60 € | 60,68 € | 134,89 € | 67,7 % | 3,94 |
| `contre-la-montre-vert-chronographe` | GT Watches GT1 Chrono VK63 | 249 € | 299 € | **239 €** | -60 € | 60,68 € | 134,89 € | 67,7 % | 3,94 |

#### GMT

| Fiche | Comparable | Prix relevé | Prix actuel | **Prix cible** | Écart | Coût rendu | Marge HT | Marge % | Coef. |
|---|---|---|---|---|---|---|---|---|---|
| `voyageur-bicolore-cadran-brun-gmt` | Time2Seiko 360 / Watchmodcustom 432,90 | 319-599 € | 349-417 € | **349 € → 419 €** | = | 111,95 € | 173,75 € | 59,7 % | 3,12 |
| `voyageur-bicolore-gmt-3-maillons` | Time2Seiko 360 / Watchmodcustom 432,90 | 319-599 € | 349-417 € | **349 € → 419 €** | = | 111,95 € | 173,75 € | 59,7 % | 3,12 |
| `voyageur-bicolore-gmt-5-maillons` | Time2Seiko 360 / Watchmodcustom 432,90 | 319-599 € | 349-417 € | **349 € → 419 €** | = | 111,95 € | 173,75 € | 59,7 % | 3,12 |
| `voyageur-or-gmt-3-maillons` | Time2Seiko 360 / Watchmodcustom 432,90 | 319-599 € | 349-417 € | **349 € → 419 €** | = | 111,95 € | 173,75 € | 59,7 % | 3,12 |
| `voyageur-or-gmt-president` | Time2Seiko 360 / Watchmodcustom 432,90 | 319-599 € | 349-417 € | **349 € → 419 €** | = | 111,95 € | 173,75 € | 59,7 % | 3,12 |
| `voyageur-or-rose-gmt-5-maillons` | Time2Seiko 360 / Watchmodcustom 432,90 | 319-599 € | 349-417 € | **349 € → 419 €** | = | 111,95 € | 173,75 € | 59,7 % | 3,12 |

#### Plongeuse Heritage

| Fiche | Comparable | Prix relevé | Prix actuel | **Prix cible** | Écart | Coût rendu | Marge HT | Marge % | Coef. |
|---|---|---|---|---|---|---|---|---|---|
| `heritage-bleu-plongeuse-vintage-42` | chapeau : maisondutemps 295 | 190-340 € | 279 € | **279 €** | = | 77,68 € | 150,66 € | 64,8 % | 3,59 |
| `heritage-bleu-nuit-plongeuse-vintage-42` | chapeau : maisondutemps 295 | 190-340 € | 279 € | **279 €** | = | 77,68 € | 150,66 € | 64,8 % | 3,59 |
| `heritage-vert-plongeuse-vintage-42` | chapeau : maisondutemps 295 | 190-340 € | 279 € | **279 €** | = | 77,68 € | 150,66 € | 64,8 % | 3,59 |

#### Classiques 39 cannelee

| Fiche | Comparable | Prix relevé | Prix actuel | **Prix cible** | Écart | Coût rendu | Marge HT | Marge % | Coef. |
|---|---|---|---|---|---|---|---|---|---|
| `trente-neuf-classique-cannelee` | Montignac 289 / maisondutemps 295 | 190-340 € | 329-397 € | **279 € → 329 €** | -50 € | 77,44 € | 150,90 € | 64,9 % | 3,60 |
| `trente-neuf-bleu-classique-cannelee` | Montignac 289 / maisondutemps 295 | 190-340 € | 329-397 € | **279 € → 329 €** | -50 € | 79,38 € | 148,96 € | 64,1 % | 3,51 |
| `trente-neuf-bleu-mer-classique-cannelee` | Montignac 289 / maisondutemps 295 | 190-340 € | 329-397 € | **279 € → 329 €** | -50 € | 79,38 € | 148,96 € | 64,1 % | 3,51 |
| `trente-neuf-noir-classique-cannelee` | Montignac 289 / maisondutemps 295 | 190-340 € | 329-397 € | **279 € → 329 €** | -50 € | 79,38 € | 148,96 € | 64,1 % | 3,51 |
| `trente-neuf-rose-classique-cannelee` | Montignac 289 / maisondutemps 295 | 190-340 € | 329-397 € | **279 € → 329 €** | -50 € | 79,38 € | 148,96 € | 64,1 % | 3,51 |
| `trente-neuf-rouge-classique-cannelee` | Montignac 289 / maisondutemps 295 | 190-340 € | 329-397 € | **279 € → 329 €** | -50 € | 79,38 € | 148,96 € | 64,1 % | 3,51 |
| `trente-neuf-vert-classique-cannelee` | Montignac 289 / maisondutemps 295 | 190-340 € | 329-397 € | **279 € → 329 €** | -50 € | 79,38 € | 148,96 € | 64,1 % | 3,51 |

#### Classiques 39 duo

| Fiche | Comparable | Prix relevé | Prix actuel | **Prix cible** | Écart | Coût rendu | Marge HT | Marge % | Coef. |
|---|---|---|---|---|---|---|---|---|---|
| `trente-neuf-duo-classique-bicolore` | Montignac 289 | 190-340 € | 319-358 € | **279 € → 309 €** | -40 € | 86,16 € | 142,18 € | 61,2 % | 3,24 |
| `trente-neuf-duo-dore-classique-bicolore` | Montignac 299 | 190-340 € | 348-387 € | **299 € → 329 €** | -49 € | 95,75 € | 148,98 € | 59,8 % | 3,12 |

#### Classiques 36 jubile

| Fiche | Comparable | Prix relevé | Prix actuel | **Prix cible** | Écart | Coût rendu | Marge HT | Marge % | Coef. |
|---|---|---|---|---|---|---|---|---|---|
| `trente-six-classique-jubile` | Gustave & Cie (montre 36mm homme) | 245 € | 299-328 € | **239 € → 259 €** | -60 € | 103,23 € | 92,34 € | 46,4 % | 2,32 |
| `trente-six-bleu-classique-jubile` | Gustave & Cie (montre 36mm homme) | 245 € | 299-328 € | **239 € → 259 €** | -60 € | 108,98 € | 86,59 € | 43,5 % | 2,19 |
| `trente-six-dore-classique-jubile` | Gustave & Cie (montre 36mm homme) | 245 € | 299-328 € | **239 € → 259 €** | -60 € | 108,98 € | 86,59 € | 43,5 % | 2,19 |
| `trente-six-or-integral-classique-jubile` | Gustave & Cie (montre 36mm homme) | 245 € | 299-328 € | **239 € → 259 €** | -60 € | 108,98 € | 86,59 € | 43,5 % | 2,19 |
| `trente-six-rose-classique-jubile` | Gustave & Cie (montre 36mm homme) | 245 € | 299-328 € | **239 € → 259 €** | -60 € | 108,98 € | 86,59 € | 43,5 % | 2,19 |
| `trente-six-rouge-classique-jubile` | Gustave & Cie (montre 36mm homme) | 245 € | 299-328 € | **239 € → 259 €** | -60 € | 108,98 € | 86,59 € | 43,5 % | 2,19 |

#### Field / Aviateur

| Fiche | Comparable | Prix relevé | Prix actuel | **Prix cible** | Écart | Coût rendu | Marge HT | Marge % | Coef. |
|---|---|---|---|---|---|---|---|---|---|
| `montre-field-acier-cadran-chiffres-1-12` | maisondutemps 295 | 190-340 € | 289-407 € | **279 € → 329 €** | -10 € | 73,52 € | 154,82 € | 66,6 % | 3,79 |
| `montre-field-bronze-cadran-chiffres-1-12` | Montignac 299 | 190-340 € | 328-357 € | **299 € → 329 €** | -29 € | 109,40 € | 135,33 € | 54,3 % | 2,73 |
| `montre-aviateur-acier-cadran-chiffres-1-12` | maisondutemps 295 | 190-340 € | 289-407 € | **279 € → 329 €** | -10 € | 70,65 € | 157,69 € | 67,8 % | 3,95 |
| `montre-aviateur-bronze-cadran-chiffres-1-12` | Montignac 299 | 190-340 € | 289-407 € | **299 € → 329 €** | +10 € | 109,40 € | 135,33 € | 54,3 % | 2,73 |

#### Explorateur 3-6-9

| Fiche | Comparable | Prix relevé | Prix actuel | **Prix cible** | Écart | Coût rendu | Marge HT | Marge % | Coef. |
|---|---|---|---|---|---|---|---|---|---|
| `montre-acier-chiffres-3-6-9-explorateur` | maisondutemps 295 | 190-340 € | 279-349 € | **279 € → 309 €** | = | 72,38 € | 155,96 € | 67,1 % | 3,85 |

#### Sport chic 41 mm

| Fiche | Comparable | Prix relevé | Prix actuel | **Prix cible** | Écart | Coût rendu | Marge HT | Marge % | Coef. |
|---|---|---|---|---|---|---|---|---|---|
| `quarante-et-un-sport-acier` | maisondutemps 295 | 190-340 € | 299-338 € | **279 € → 299 €** | -20 € | 71,75 € | 156,59 € | 67,4 % | 3,89 |
| `quarante-et-un-blanc-cuir-sport-acier` | maisondutemps 295 | 190-340 € | 299-338 € | **279 € → 299 €** | -20 € | 75,68 € | 152,66 € | 65,7 % | 3,69 |
| `quarante-et-un-bleu-acier-sport-acier` | maisondutemps 295 | 190-340 € | 299-338 € | **279 € → 299 €** | -20 € | 75,68 € | 152,66 € | 65,7 % | 3,69 |
| `quarante-et-un-bleu-cuir-sport-acier` | maisondutemps 295 | 190-340 € | 299-338 € | **279 € → 299 €** | -20 € | 75,68 € | 152,66 € | 65,7 % | 3,69 |
| `quarante-et-un-noir-acier-sport-acier` | maisondutemps 295 | 190-340 € | 299-338 € | **279 € → 299 €** | -20 € | 75,68 € | 152,66 € | 65,7 % | 3,69 |
| `quarante-et-un-noir-cuir-sport-acier` | maisondutemps 295 | 190-340 € | 299-338 € | **279 € → 299 €** | -20 € | 75,68 € | 152,66 € | 65,7 % | 3,69 |
| `quarante-et-un-noir-jaune-acier-sport-acier` | maisondutemps 295 | 190-340 € | 299-338 € | **279 € → 299 €** | -20 € | 75,68 € | 152,66 € | 65,7 % | 3,69 |

#### Sport chic Integrale

| Fiche | Comparable | Prix relevé | Prix actuel | **Prix cible** | Écart | Coût rendu | Marge HT | Marge % | Coef. |
|---|---|---|---|---|---|---|---|---|---|
| `integrale-noir-sport-chic-acier` | SILA Paris 175-210 (SOUS notre cout) | 175-210 € | 379 € | **329 €** | -50 € | 147,76 € | 121,55 € | 44,3 % | 2,23 |
| `integrale-bleu-nuit-sport-chic-acier` | SILA Paris 175-210 (SOUS notre cout) | 175-210 € | 379 € | **329 €** | -50 € | 147,76 € | 121,55 € | 44,3 % | 2,23 |
| `integrale-bleu-ciel-sport-chic-acier` | SILA Paris 175-210 (SOUS notre cout) | 175-210 € | 379 € | **329 €** | -50 € | 147,76 € | 121,55 € | 44,3 % | 2,23 |
| `integrale-blanc-argente-sport-chic-acier` | SILA Paris 175-210 (SOUS notre cout) | 175-210 € | 379 € | **329 €** | -50 € | 147,76 € | 121,55 € | 44,3 % | 2,23 |
| `integrale-vert-sport-chic-acier` | SILA Paris 175-210 (SOUS notre cout) | 175-210 € | 379 € | **329 €** | -50 € | 147,76 € | 121,55 € | 44,3 % | 2,23 |
| `integrale-turquoise-sport-chic-acier` | SILA Paris 175-210 (SOUS notre cout) | 175-210 € | 379 € | **329 €** | -50 € | 147,76 € | 121,55 € | 44,3 % | 2,23 |
| `integrale-brun-or-rose-sport-chic` | SILA Paris 175-210 (SOUS notre cout) | 175-210 € | 379 € | **329 €** | -50 € | 147,76 € | 121,55 € | 44,3 % | 2,23 |

#### Bracelets

| Fiche | Comparable | Prix relevé | Prix actuel | **Prix cible** | Écart | Coût rendu | Marge HT | Marge % | Coef. |
|---|---|---|---|---|---|---|---|---|---|
| `bracelet-acier-massif-12-22-mm` | bracelet montre 4,99-120 | 4,99-120 € | 39,90-59,90 € | **39,90 € → 59,90 €** | = | 12,39 € | 20,05 € | 60,3 % | 3,22 |
| `bracelet-caoutchouc-gaufre` | idem | 4,99-120 € | 24,90 € | **24,90 €** | = | 7,26 € | 12,89 € | 62,1 % | 3,43 |
| `bracelet-cuir-daim-degagement-rapide` | idem | 4,99-120 € | 17,90 € | **24,90 €** | +7 € | 6,73 € | 13,42 € | 64,7 % | 3,70 |
| `bracelet-milanais-maille-italienne` | idem | 4,99-120 € | 14,90-24,90 € | **19,90 € → 24,90 €** | +5 € | 6,43 € | 9,62 € | 58,0 % | 3,09 |
| `bracelet-jubile-embouts-courbes` | idem | 4,99-120 € | 29,90-39,90 € | **29,90 € → 39,90 €** | = | 9,69 € | 14,56 € | 58,4 % | 3,09 |
| `bracelet-jubile-acier-20mm` | bracelet montre 20mm (5 marchands) | 4,99-120 € | 49,90 € | **49,90 €** | = | 17,34 € | 23,29 € | 56,0 % | 2,88 |
| `bracelet-fkm-courbe` | idem | 4,99-120 € | 29,90-34,90 € | **39,90 €** | +10 € | 16,83 € | 15,61 € | 47,0 % | 2,37 |
| `bracelet-fkm-tropical` | idem | 4,99-120 € | 29,90-34,90 € | **39,90 €** | +10 € | 16,25 € | 16,19 € | 48,7 % | 2,46 |
| `bracelet-presidentiel-acier-inoxydable` | idem | 4,99-120 € | 39,90-49,90 € | **49,90 € → 54,90 €** | +10 € | 23,90 € | 16,73 € | 40,2 % | 2,09 |
| `bracelet-presidentiel-dore` | idem | 4,99-120 € | 54,90-59,90 € | **59,90 € → 64,90 €** | +5 € | 28,69 € | 20,14 € | 40,3 % | 2,09 |

#### Remontoirs

| Fiche | Comparable | Prix relevé | Prix actuel | **Prix cible** | Écart | Coût rendu | Marge HT | Marge % | Coef. |
|---|---|---|---|---|---|---|---|---|---|
| `remontoir-solo` | independants organiques 68-270 | 68-270 € | 59,90-64,90 € | **64,90 €** | +5 € | 29,41 € | 23,51 € | 43,5 % | 2,21 |
| `remontoir-vitrine` | idem | 68-270 € | 129,90 € | **129,90 €** | = | 58,99 € | 47,19 € | 43,6 % | 2,20 |
| `remontoir-bois-acajou` | idem | 68-270 | 79,90-109,90 € | **79,90 € → 109,90 €** | = | ⛔ COUT INTROUVABLE | — | — | — |
| `remontoir-bois-ebene` | idem | 68-270 | 79,90-109,90 € | **79,90 € → 109,90 €** | = | ⛔ COUT INTROUVABLE | — | — | — |
| `remontoir-bois-noir-laque` | idem | 68-270 | 79,90-109,90 € | **79,90 € → 109,90 €** | = | ⛔ COUT INTROUVABLE | — | — | — |
| `remontoir-bois-noyer` | idem | 68-270 | 79,90-109,90 € | **79,90 € → 109,90 €** | = | ⛔ COUT INTROUVABLE | — | — | — |
| `remontoir-collection-bois-beige` | idem (plafond 270) | 68-270 € | 104,90-299,90 € | **104,90 € → 269,90 €** | = | 48,78 € | 36,92 € | 42,2 % | 2,15 |
| `remontoir-collection-bois-noir` | idem (plafond 270) | 68-270 € | 104,90-289,90 € | **104,90 € → 269,90 €** | = | 48,78 € | 36,92 € | 42,2 % | 2,15 |
| `remontoir-collection-bois-led-noir` | idem | 68-270 € | 184,90-219,90 € | **184,90 € → 219,90 €** | = | 48,78 € | 102,46 € | 66,5 % | 3,79 |
| `remontoir-collection-bois-led-rouge` | idem | 68-270 € | 184,90-219,90 € | **184,90 € → 219,90 €** | = | 48,78 € | 102,46 € | 66,5 % | 3,79 |
| `remontoir-collection-cuir-pu` | idem (plafond 270) | 68-270 € | 254,90-324,90 € | **249,90 € → 269,90 €** | -5 € | 48,78 € | 155,72 € | 74,8 % | 5,12 |

#### Rangement

| Fiche | Comparable | Prix relevé | Prix actuel | **Prix cible** | Écart | Coût rendu | Marge HT | Marge % | Coef. |
|---|---|---|---|---|---|---|---|---|---|
| `coffret-6-montres-couvercle-verre` | Royaume de la Boite 55-99 | 55-99 € | 54,90 € | **69,90 €** | +15 € | 16,34 € | 40,68 € | 69,8 % | 4,28 |
| `coffret-douze-aluminium` | Royaume de la Boite 55-99 | 55-99 € | 24,90-69,90 € | **69,90 € → 99,90 €** | +45 € | 13,14 € | 43,88 € | 75,3 % | 5,32 |
| `coffret-douze-presentation` | Royaume de la Boite 99 | 55-99 € | 94,90 € | **94,90 €** | = | 44,38 € | 33,12 € | 41,9 % | 2,14 |
| `etui-de-voyage-rigide` | etui montre 11-150 | 11-150 € | 69,90-189,90 € | **69,90 € → 149,90 €** | = | 19,78 € | 37,24 € | 63,9 % | 3,53 |
| `coussins-de-presentation-lot-de-10` | aucun comparable releve | - € | 19,90 € | **19,90 €** | = | 5,70 € | 10,35 € | 62,4 % | 3,49 |
| `rouleau-de-voyage-noir-cuir` | etui montre 11-150 (maisondutemps watchroll) | 11-150 € | 29,90-49,90 € | **39,90 € → 49,90 €** | +10 € | 15,48 € | 16,96 € | 51,0 % | 2,58 |
| `rouleau-de-voyage-brun-cuir` | etui montre 11-150 (maisondutemps watchroll) | 11-150 € | 29,90-49,90 € | **39,90 € → 49,90 €** | +10 € | 15,48 € | 16,96 € | 51,0 % | 2,58 |
| `rouleau-de-voyage-bleu-marine-cuir` | etui montre 11-150 (maisondutemps watchroll) | 11-150 € | 29,90-49,90 € | **39,90 € → 49,90 €** | +10 € | 15,48 € | 16,96 € | 51,0 % | 2,58 |
| `rouleau-de-voyage-vert-cuir` | etui montre 11-150 (maisondutemps watchroll) | 11-150 € | 29,90-49,90 € | **39,90 € → 49,90 €** | +10 € | 15,48 € | 16,96 € | 51,0 % | 2,58 |

#### Outillage

| Fiche | Comparable | Prix relevé | Prix actuel | **Prix cible** | Écart | Coût rendu | Marge HT | Marge % | Coef. |
|---|---|---|---|---|---|---|---|---|---|
| `loupe-d-horloger` | outil montre 4-30 | 4-30 € | 12,90-21,90 € | **12,90 € → 21,90 €** | = | 4,80 € | 5,52 € | 51,3 % | 2,69 |
| `loupe-de-date-saphir` | idem | 4-30 € | 12,90 € | **12,90 €** | = | 4,61 € | 5,71 € | 53,1 % | 2,80 |
| `doigtiers-d-horloger-latex` | idem | 4-30 € | 12,90 € | **12,90 €** | = | 3,75 € | 6,57 € | 61,1 % | 3,44 |
| `barrettes-de-rechange-270` | idem | 4-30 € | 12,90 € | **12,90 €** | = | 5,45 € | 4,87 € | 45,3 % | 2,37 |
| `pince-a-barrettes` | idem | 4-30 € | 12,90-19,90 € | **12,90 € → 19,90 €** | = | 6,32 € | 4,00 € | 37,2 % | 2,04 |
| `outil-de-mise-a-taille-de-bracelet` | idem | 4-30 € | 19,90 € | **19,90 €** | = | 5,96 € | 10,09 € | 60,9 % | 3,34 |
| `kit-d-entretien-13-pieces` | kit horlogerie 9,88-299 | 9,88-299 € | 29,90 € | **29,90 €** | = | 11,26 € | 12,99 € | 52,1 % | 2,66 |
| `set-tournevis-horloger` | kit horlogerie 9,88-299 | 9,88-299 € | 59,90 € | **59,90 €** | = | 28,35 € | 20,48 € | 41,0 % | 2,11 |

#### Carte cadeau

| Fiche | Comparable | Prix relevé | Prix actuel | **Prix cible** | Écart | Coût rendu | Marge HT | Marge % | Coef. |
|---|---|---|---|---|---|---|---|---|---|
| `carte-cadeau-maison-noirmont` | - | - | 50-300 € | **—** | — | ⛔ sans objet | — | — | — |
---

## 3. Étape 2 — la marge réelle : la formule

Les prix affichés sont **TTC en France**. Le calcul, dans l'ordre :

```
base HT        = prix TTC ÷ 1,2
coût rendu     = coût produit + fret France (1,99 €, suivi)
frais paiement = 1,4 % × prix TTC + 0,25 €   (Shopify Payments)
marge          = base HT − coût rendu − frais paiement
marge %        = marge ÷ base HT
coefficient    = prix TTC ÷ coût rendu
```

**Exemple lisible — le squelette carré à 279 €**
`279 ÷ 1,2 = 232,50 € HT` · coût rendu `109,87 + 1,99 = 111,86 €` ·
frais `1,4 % × 279 + 0,25 = 4,16 €` · **marge `232,50 − 111,86 − 4,16 = 116,48 €`, soit 50,1 % HT**,
coefficient **2,49**.

Deux remarques de méthode :
- Le **fret est déjà inclus** dans les coûts marqués « rendu » (Intégrale, GMT, Trente-neuf duo doré) :
  il n'y est pas ajouté une deuxième fois.
- Les frais de paiement sont calculés **sur le montant encaissé**, donc TTC. C'est le montant réel
  prélevé par Shopify Payments, pas une part du HT.

### La qualité des coûts, dite franchement

| Classe | Ce que c'est | Fiches concernées |
|---|---|---|
| **A** | `inventoryItem.unitCost` **lu sur Shopify**, renseigné par DSers, par variante | 10 fiches mères de montres + **tous les accessoires sauf les remontoirs bois et les rouleaux** |
| **B** | **Registre de sourcing du 24/07/2026** — prix relevés sur `fr.aliexpress.com` en session France/EUR. Datés, non estimés, mais **antérieurs de deux semaines** à la découverte que les coûts réels DSers sont **souvent inférieurs** au relevé SERP | Chronographes ×12, GMT ×6, Héritage ×3, Intégrale ×7, rouleaux ×4, Remontoir Collection ×5, coloris frères des Classiques |
| **C** | **Proxy assumé** | `montre-aviateur-bronze` : le seul coût relevé sur son listing porte sur la variante **acier**, pas bronze. J'ai repris le coût du Field bronze. **Chiffre à reconfirmer.** |
| **X** | **Introuvable — non chiffré** | `remontoir-bois-acajou`, `-ebene`, `-noir-laque`, `-noyer` |

⚠️ **Les coûts de classe B sont prudents** : le push DSers du 09/08 a montré des écarts dans notre
sens (9,19 € réels contre 18,49 € attendus). **Les marges ci-dessous sont donc plutôt un plancher.**

---

## 4. Synthèse par famille

| Famille | Fiches | Marge moyenne € | Marge moyenne % | Marge minimale | Fiche la plus basse |
|---|---:|---:|---:|---:|---|
| **Chronographe VK63** | 12 | **134,89 €** | **67,7 %** | 67,7 % | — (prix unique) |
| Explorateur 3-6-9 | 1 | 155,96 € | 67,1 % | 67,1 % | — |
| **Sport chic 41 mm** | 7 | 153,23 € | 65,9 % | 65,7 % | `quarante-et-un-blanc-cuir-sport-acier` |
| Plongeuse Héritage | 3 | 150,66 € | 64,8 % | 64,8 % | — |
| Classiques 39 cannelée | 7 | 149,24 € | 64,2 % | 64,1 % | `trente-neuf-bleu-classique-cannelee` |
| Field / Aviateur | 4 | 145,79 € | 60,8 % | **54,3 %** | `montre-field-bronze-cadran-chiffres-1-12` |
| Classiques 39 duo | 2 | 145,58 € | 60,5 % | 59,8 % | `trente-neuf-duo-dore-classique-bicolore` |
| **GMT** | 6 | **173,75 €** | 59,7 % | 59,7 % | — (la meilleure marge en euros) |
| Rangement | 9 | 25,90 € | 57,5 % | **41,9 %** | `coffret-douze-presentation` |
| Remontoirs | 7 chiffrés / 11 | 72,17 € | 54,2 % | **42,2 %** | `remontoir-collection-bois-beige` |
| Bracelets | 10 | 16,25 € | 53,6 % | **40,2 %** | `bracelet-presidentiel-acier-inoxydable` |
| Outillage | 8 | 8,78 € | 50,3 % | **37,2 %** | `pince-a-barrettes` |
| Squelette | 2 | 112,03 € | 48,2 % | **46,3 %** | `montre-squelette-automatique-octogone` |
| **Sport chic Intégrale** | 7 | 121,55 € | **44,3 %** | 44,3 % | ⛔ voir §5 |
| **Classiques 36 jubilé** | 6 | 87,55 € | **44,0 %** | **43,5 %** | `trente-six-bleu-classique-jubile` |

**Seuil retenu pour « acceptable » : 45 % de marge HT.** En dessous, la fiche ne finance plus un CPA
publicitaire et un retour éventuel. **Deux familles de montres passent sous ce seuil** (Intégrale
44,3 %, Trente-six 44,0 %) et **quatre fiches d'accessoires** (`pince-a-barrettes` 37,2 %,
`bracelet-presidentiel-acier` 40,2 %, `coffret-douze-presentation` 41,9 %, `remontoir-collection`
en entrée 42,2 %).

---

## 5. Le contrôle prix ÷ CPC ≥ 100

CPC mesurés. Pour les montres, ils n'étaient pas dans `NOTES-PRICING.md` §1 : je les ai repris de
`journal/2026-07-31-marche-complet-semrush.md` — `montre squelette homme` **0,38 €**,
`montre squelette` 0,39 €, `montre automatique homme` **0,38 €**, `chronographe` **0,32 €**,
`montre gmt automatique` **0,23 €**, `montre plongeuse vintage` **0,71 €** (le plus cher).

| Famille | CPC retenu | Plancher (×100) | Prix cible le plus bas | Ratio | Verdict |
|---|---:|---:|---:|---:|---|
| **Toutes les montres** | 0,71 € (le pire cas) | 71 € | **239 €** | **337** | ✅ **Aucune montre ne casse le ratio, même au prix cible.** La cible 150-200 est dépassée partout. |
| Remontoirs | 0,55 € | 55 € | 64,90 € | 118 | ✅ tenu (et 59,90 € donnait déjà 109) |
| Boîtes et coffrets | 0,38-0,46 € | 46 € | 69,90 € | 152-184 | ✅ **réparé** — le 24,90 € actuel donnait 54 |
| Écrins et rouleaux | 0,36 € | 36 € | 39,90 € | 111 | ✅ **réparé** — le 29,90 € actuel donnait 83 |
| Bracelets (cote mm) | 0,27 € | 27 € | 19,90 € | 74 | ⚠️ **3 fiches tombent encore** : milanais 19,90 €, caoutchouc et cuir-daim 24,90 € |
| Bracelets (tête générique) | 0,41 € | 41 € | 19,90 € | 49 | ⛔ **6 fiches sur 10 tombent.** À ne jamais cibler sur la tête générique. |
| Outillage | 0,20 € | 20 € | 12,90 € | 65 | ⛔ **5 fiches sur 8 tombent, et je ne propose pas de les remonter** : le marché vit à 4-30 € et AliExpress s'y classe en organique. |
| Coussins de présentation | 0,38 € | 38 € | 19,90 € | 52 | ⛔ consommable de cross-sell, jamais de publicité |

⚠️ **Un prix cible qui casse le ratio est signalé** : ce sont les **9 fiches** ci-dessus
(3 bracelets, 5 outils, 1 lot de coussins). Aucune ne peut recevoir de trafic payant ; toutes
restent vendables en organique et en cross-sell, où le ratio n'a pas de sens.

---

## 6. Étape 3 — ce qu'il faut décider

### 6.1 Ce qui devient non rentable au prix du marché : l'Intégrale

**C'est le seul vrai problème du dossier, et il est net.**

Le coût rendu de l'`integrale-*-sport-chic-acier` est de **147,76 €** (143,18 € + 4,58 € de port).
Le comparable de marché est **SILA Paris, 175-210 €**. Appliquer la règle « juste en dessous » donne
**199 €** — et à 199 € :

`199 ÷ 1,2 = 165,83 € HT` − `147,76 €` − `3,04 €` = **15,04 €, soit 9,1 % de marge.**

⛔ **Le comparable de cette famille est sous notre prix de revient.** Ce n'est pas un problème de
positionnement : nous ne savons pas fabriquer ce produit à ce prix.

**Recommandation : ne pas descendre.** Ramener les 7 fiches de **379 € à 329 €** (44,3 % de marge),
**les sortir de toute campagne payante**, et les traiter comme les premières candidates au
dépeuplement. La demande le confirme : `montre bracelet intégré` pèse **≈ 100 recherches nettes pour
14 fiches**, et sa page 1 est un magazine qui répond entre 960 et 2 000 €.

### 6.2 Les autres cas à trancher

| Cas | Constat | Recommandation |
|---|---|---|
| **Trente-six jubilé** (6 fiches) | 43,5-46,4 % — la marge la plus serrée des montres, coût 101-107 € contre un comparable à 245 € | **Garder à 239 €.** Rentable, mais **ne jamais descendre en dessous** : à 219 € la marge passe sous 38 %. |
| **Squelette octogone** | 46,3 % à 279 € — coût 118,77 € | **Garder.** C'est le prix qui ouvre la famille la plus saine du dossier (17 120 recherches, 2 fiches). La marge paie l'entrée. |
| **Remontoirs bois** (4 fiches) | **Coût introuvable** | ⛔ **Ne pas publier de prix dessus avant un relevé DSers.** Prix laissés inchangés dans la grille, marge non chiffrée. |
| **Outillage** (8 fiches) | Marges en % correctes (50 %) mais **8,78 € en moyenne en euros** | **Garder les prix, sortir de la publicité.** Cross-sell sur les fiches montres uniquement. |
| **Bracelets** (10 fiches) | Aucun relevé concurrentiel **par type** — seule la bande 4,99-120 € est connue | **Remonter les 4 fiches à marge faible** (FKM à 39,90 €, présidentiel acier à 49,90 €, présidentiel doré à 59,90 €) et **laisser le reste**. Ne pas acheter de clic sur la tête générique. |
| **Coffrets** (3 fiches) | Le premier prix à 24,90 € est **le pire endroit du marché** (bande Songmics verrouillée à 19-27 €) | **Passer le premier prix à 69,90 €.** La marge passe de 33,8 % à 75,3 %, et on quitte une bande qu'on ne peut pas gagner. |
| **GMT** (6 fiches) | 59,7 % à 349 €, **173,75 € de marge — la meilleure du catalogue en euros** | ⛔ **Ne rien toucher.** Seule famille où notre prix est déjà le prix du marché. |

### 6.3 Le panier moyen attendu, et ce qu'il implique à 30 €/jour

Prix cibles moyens et marges moyennes, calculés sur les 95 fiches chiffrables :

| Mix de commandes | Panier moyen TTC | Marge contributive |
|---|---:|---:|
| 100 % montres | **280,93 €** | **137,91 €** |
| 50 % montres / 50 % accessoires | 171,80 € | 83,24 € |
| **30 % montres / 70 % accessoires** *(le mix que la demande annonce : 142 640 recherches sur les accessoires contre 37 710 sur les montres)* | **128,14 €** | **61,37 €** |

**Le budget de 30 €/jour = 900 €/mois.** Ce qu'il achète, aux CPC mesurés :

| Tête achetée | CPC | Clics/mois | TC 0,5 % | TC 1,0 % | TC 1,5 % |
|---|---:|---:|---:|---:|---:|
| `montre gmt automatique` | 0,23 € | 3 913 | 19,6 cdes — **CPA 46 €** | 39,1 cdes — CPA 23 € | 58,7 cdes — CPA 15 € |
| `chronographe` | 0,32 € | 2 812 | 14,1 cdes — **CPA 64 €** | 28,1 cdes — CPA 32 € | 42,2 cdes — CPA 21 € |
| `montre squelette homme` / chapeau | 0,38 € | 2 368 | 11,8 cdes — **CPA 76 €** | 23,7 cdes — CPA 38 € | 35,5 cdes — CPA 25 € |

**Ce que ça dit.**

1. ✅ **Sur les montres, le budget tient largement.** Une marge de 137,91 € couvre un CPA de 76 €
   même dans l'hypothèse noire (taux de conversion à 0,5 %). **L'objectif de 15 conversions est
   atteint en ~19 jours à 1 % de conversion**, en ~38 jours à 0,5 %.
2. ⛔ **Sur les accessoires, le budget ne tient pas.** Marge moyenne **28,56 €** contre un CPA de
   38 à 76 € : **chaque commande d'accessoire achetée en publicité perd de l'argent.** Les seules
   exceptions sont les fiches au-dessus de 70 € — remontoirs (36,92 à 102,46 € de marge), étui de
   voyage (37,24 €), coffrets à 69,90 € (40,68 à 43,88 €).
3. ⚠️ **Le mix réaliste 30/70 donne 61,37 € de marge par commande.** Il ne survit qu'à un taux de
   conversion **≥ 1 %**. C'est l'arbitrage réel : **la demande est sur les accessoires, la marge est
   sur les montres.** Le budget doit aller aux montres et aux accessoires > 70 €, en laissant le
   reste du catalogue à l'organique et au cross-sell.

### 6.4 Ce que je n'ai pas pu chiffrer

- ⛔ **Les 4 remontoirs bois** (`acajou`, `ebene`, `noir-laque`, `noyer`) : **aucun coût dans le
  dépôt.** Leur listing fournisseur est identifié (`1005012102224533`) mais **aucun relevé de prix
  ne lui est attribué**. Le seul chiffre proche (32,99 €) appartient à **un autre listing** — je ne
  l'ai pas repris.
- ⚠️ **Le coût par variante n'existe nulle part** pour les familles de classe B. Les coloris frères
  partagent le listing de leur fiche mère ; j'ai donc appliqué **un coût unique par famille**. Les
  échelles hautes (Remontoir Collection à 269,90 €, étui de voyage à 149,90 €) sont chiffrées avec
  **le coût d'entrée du listing** : leur marge réelle est donc **surestimée**, et à reconfirmer.
- ⚠️ **`montre-aviateur-bronze`** : coût emprunté au Field bronze (classe C).
- ⚠️ **Aucun prix concurrent relevé par type de bracelet.** Les cibles bracelets reposent sur la
  bande globale 4,99-120 € et sur la contrainte de marge, **pas sur un comparable identifié**.
  C'est le seul endroit de cette grille où la règle « juste en dessous » n'a pas pu être appliquée.
- ⚠️ **Le taux de conversion est une hypothèse**, pas une mesure : la boutique est à 0 vente. Les
  CPA du §6.3 sont des scénarios.
- ⚠️ **Les frais de retour ne sont pas dans le calcul.** Avec un « 14 jours même portée », un taux
  de retour de 5 % sur une montre à 279 € coûte ≈ 14 € par commande — soit **10 % de la marge**.
  À intégrer quand le premier chiffre réel existera.

---

## 7. Ce qui reste à faire

1. **Arbitrage de Hakim sur cette grille** (T-H3) — puis application des prix sur Shopify, jamais avant.
2. **Relever le coût DSers des 4 remontoirs bois** avant de leur toucher un prix.
3. **Reconfirmer par l'API les coûts de classe B** — chronographes, GMT, Intégrale, Héritage : ce
   sont 28 fiches chiffrées sur un relevé SERP du 24/07, et le précédent du 09/08 dit que le coût
   réel est souvent plus bas.
4. **Trancher le sort des 7 Intégrale** : baisse à 329 € et sortie de la publicité, ou dépeuplement.
