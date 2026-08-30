---
type: journal
boutique: seiko-mod
date: 2026-08-14
nature: intervention
leviers: [prix]
titre: "14/08/2026 — Application de la grille de prix sur Shopify (T-H3)"
---

# 14/08/2026 — Application de la grille de prix sur Shopify (T-H3)

**Périmètre : les 96 fiches actives de Maison Noirmont.** Source unique : [`GRILLE-PRIX.md`](../GRILLE-PRIX.md),
arbitrée par Hakim le 14/08/2026. **Aucun brouillon activé, aucun statut touché, aucun `compareAtPrice` écrit.**

## Résultat en une ligne

**585 variantes réécrites sur 65 fiches** ; **31 fiches laissées intactes** parce que la grille les
laisse à leur prix. **0 `userErrors`** sur les 12 appels de mutation. **0 écart** entre le prix attendu
et le prix lu en boutique après écriture, sur les 883 variantes actives.

---

## 1. La sauvegarde préalable

**Aucune écriture n'a eu lieu avant cette étape.** L'état complet des prix a été exporté par
`bulkOperationRunQuery` (l'export paginé côté Shopify, pas un `query:` filtré) :

| Fichier | Contenu |
|---|---|
| `backups/2026-08-14-prix/bulk-raw.jsonl` | export brut Shopify, 979 objets (96 produits + 883 variantes) |
| `backups/2026-08-14-prix/avant.jsonl` | **883 lignes** — produit (id, titre, handle, statut), variante (id, titre), `price`, `compareAtPrice`, `inventoryItem.unitCost` |
| `backups/2026-08-14-prix/apres.jsonl` | **883 lignes** — l'état relu après écriture, pour diff |

**Contrôle d'entrée : `compareAtPrice` était déjà nul sur les 883 variantes actives.** La purge du
08/08 n'a pas régressé.

---

## 2. La règle d'application, et la décision qu'elle a demandée

La grille donne, par fiche, soit **un prix unique** (`239 €`), soit **une échelle** (`279 € → 329 €`)
dont elle précise seulement les deux extrémités — alors que les fiches ont jusqu'à **six paliers**
(Explorateur : 104 variantes, Field acier : 66). Il a donc fallu répartir les paliers intermédiaires.

**Règle retenue, appliquée uniformément et mécaniquement :**

1. **Prix unique dans la grille** → ce prix sur **toutes** les variantes.
2. **Échelle `A → B`** → l'échelle actuelle est **additive** (prix de base + supplément par option).
   On rebase : **entrée = A**, **haut = B**, et les suppléments d'option sont réduits à des montants
   ronds qui **reproduisent exactement B** et **préservent l'ordre des paliers**.
3. **Échelle sous plafond** (remontoirs Collection, étui de voyage) → la grille ne déplace que le
   plafond. **Seuls les paliers qui dépassent le plafond sont redescendus** ; les paliers
   intermédiaires déjà dans la bande ne bougent pas. C'est la lecture minimale, et la bonne :
   la grille écrit « idem (plafond 270) ».

### Les suppléments d'option retenus, famille par famille

| Famille | Avant | Après | Suppléments |
|---|---|---|---|
| Classiques 39 cannelée | 329 / 358 / 368 / 397 | **279 / 299 / 309 / 329** | fond verre +20, NH35 +30 |
| Field & Aviateur acier | 289 / 318 / 328 / 357 / 378 / 407 | **279 / 289 / 299 / 309 / 319 / 329** | fond verre +10, NH35 +20, PT5000 +40 |
| Aviateur bronze | idem | **299 / 304 / 314 / 319 / 324 / 329** | fond verre +5, NH35 +15, PT5000 +25 |
| Explorateur 3-6-9 | 279 / 309 / 319 / 349 | **279 / 289 / 299 / 309** | fond verre +10, NH35 +20 |
| Trente-six jubilé | 299 / 328 | **239 / 259** | fond verre +20 |
| Sport chic 41 mm | 299 / 338 | **279 / 299** | NH35 +20 |

⚠️ **L'Aviateur bronze est le seul cas inconfortable** : la grille lui donne `299 → 329`, soit **30 €
d'amplitude pour six paliers**, ce qui force des suppléments de 5 à 25 € et des prix en 304/314/324.
Les autres familles tombent sur des prix ronds. **À trancher si Hakim veut un barème homogène** :
soit resserrer la fiche à deux ou trois paliers, soit lui laisser la même amplitude que l'Aviateur
acier (279 → 329).

---

## 3. Les cas particuliers demandés

### ✅ Les 7 Intégrale — appliquées à 329 €, non descendues

`integrale-noir` · `-bleu-nuit` · `-bleu-ciel` · `-blanc-argente` · `-vert` · `-turquoise` ·
`-brun-or-rose` : **379 € → 329 €**, une variante chacune.
**Elles n'ont pas été alignées sur leur comparable** : SILA Paris vit à 175-210 €, soit **sous notre
coût rendu de 147,76 €** (à 199 € la marge tomberait à 15,04 €, 9,1 %). À 329 € la marge est de
121,55 € (44,3 %). ⛔ **Rappel de la grille : ces 7 fiches sortent de toute campagne payante et sont
les premières candidates au dépeuplement.**

### ✅ Le GMT — strictement inchangé

Les 6 fiches `voyageur-*` sont **restées à 349 / 378 / 388 / 417 €**, vérifié en lecture directe
après écriture. Aucune mutation ne les a visées.

⚠️ **Écart relevé entre la grille et la boutique** : la grille écrit `349 € → 419 €` alors que le
haut de gamme réel en boutique est **417 €**. Comme la consigne est « prix inchangé » et que l'écart
est de 2 €, **je n'ai rien touché** — mais la grille devrait lire 417 €, pas 419 €.

### ⚠️ Les 4 remontoirs bois — prix appliqués (inchangés), marge invérifiable

`remontoir-bois-acajou` · `-ebene` · `-noir-laque` · `-noyer` : la grille leur donne
**79,90 € → 109,90 €**, soit exactement leur prix actuel. **Aucune écriture n'était donc nécessaire,
et aucune n'a eu lieu.**

⛔ **Leur marge reste invérifiable** : aucun `inventoryItem.unitCost` sur leurs 8 variantes, et le
registre de sourcing ne rattache aucun relevé à leur listing fournisseur (`1005012102224533`).
**Décision à prendre plus tard, après un relevé DSers.** Elles ne devraient recevoir ni publicité ni
mise en avant tant que le coût est inconnu.

### ⛔ Les 9 fiches qui cassent le ratio prix ÷ CPC — appliquées, mais exclues de toute campagne payante

Prix appliqués conformément à la grille. **Aucune ne peut recevoir de trafic payant** ; organique et
cross-sell seulement.

| Fiche | Prix appliqué | CPC de référence | Ratio |
|---|---|---|---|
| `bracelet-milanais-maille-italienne` | 19,90 € (entrée) | 0,27 € (cote mm) | 74 |
| `bracelet-caoutchouc-gaufre` | 24,90 € | 0,27 € | 92 |
| `bracelet-cuir-daim-degagement-rapide` | 24,90 € | 0,27 € | 92 |
| `loupe-d-horloger` | 12,90 € (entrée) | 0,20 € | 65 |
| `loupe-de-date-saphir` | 12,90 € | 0,20 € | 65 |
| `doigtiers-d-horloger-latex` | 12,90 € | 0,20 € | 65 |
| `barrettes-de-rechange-270` | 12,90 € | 0,20 € | 65 |
| `pince-a-barrettes` | 12,90 € (entrée) | 0,20 € | 65 |
| `coussins-de-presentation-lot-de-10` | 19,90 € | 0,38 € | 52 |

⛔ **Sur la tête générique `bracelet montre` (CPC 0,41 €), ce sont 6 fiches sur 10 qui tombent.**
La grille est explicite : **ne jamais acheter de clic sur la tête générique bracelet.**

---

## 4. Écarts entre la grille et ce qui a été appliqué

| Écart | Motif |
|---|---|
| **GMT : grille 419 €, boutique 417 €** | Consigne « prix inchangé ». Écart de 2 € non écrit. **La grille est à corriger, pas la boutique.** |
| **Aviateur bronze : paliers 304 / 314 / 319 / 324 €** | La grille donne 2 bornes pour 6 paliers sur 30 € d'amplitude. Prix non ronds, ordre préservé. À arbitrer. |
| **Remontoirs Collection bois beige / noir : seul le palier « 6 montres » redescend** | La grille pose un plafond (269,90 €), pas une échelle complète. Les paliers 2 et 4 montres sont déjà sous le plafond → non touchés. |
| **Étui de voyage : seul le palier « 6 slot » redescend** (189,90 → 149,90 €) | Même logique de plafond ; 69,90 / 89,90 / 109,90 € sont dans la bande. |
| **Remontoir Collection cuir PU : palier médian à 259,90 €** | La grille donne 249,90 → 269,90 pour 3 paliers ; le médian (274,90 €) dépassait le plafond, placé à mi-chemin. |
| **Bracelet présidentiel acier : « Président » passe de 39,90 à 49,90 €, les 3 autres à 54,90 €** | Mappage par rang de palier (entrée→49,90, haut→54,90). ⚠️ La grille chiffrait la marge d'entrée sur le coût du **Jubilé** (21,91 €), qui se retrouve au palier haut. Marge réelle d'entrée meilleure que la grille ne l'annonce. |
| **Les 4 rouleaux de voyage convergent sur 39,90 / 44,90 / 49,90 €** | Le bleu marine partait de 29,90 / 39,90 / 49,90 et le vert de 34,90 / 39,90 / 49,90 ; la grille impose 39,90 en entrée, ce qui aurait fait doublon avec le palier médian. Les 4 fiches sont désormais sur le même barème. |
| **Carte cadeau non touchée** | La grille la marque « sans objet ». |

---

## 5. Les preuves

### 5.1 Scan complet après écriture

`bulkOperationRunQuery` **sans filtre de statut** — énumération complète de la boutique, pas un
`query:` sur `productVariants` (qui serait ignoré silencieusement).

| Contrôle | Attendu | Lu |
|---|---|---|
| Produits total | 201 | **201** |
| Statuts | 96 actifs / 95 brouillons / 10 archivés | **96 / 95 / 10** ✅ |
| Variantes actives | 883 | **883** |
| Écart prix attendu vs prix lu (883 variantes actives) | 0 | **0** ✅ |
| Variantes réellement modifiées | 585 | **585** ✅ |
| `compareAtPrice` non nul sur les 96 fiches actives | 0 | **0** ✅ |

### 5.2 Contre-vérification indépendante par curseur

Scan `productVariants(first: 50, after: $cursor)` réellement paginé, page 1 : **44 variantes actives
contrôlées, 0 désaccord** avec `apres.jsonl`. Le chemin « bulk » et le chemin « curseur » disent la
même chose.

### 5.3 Lecture directe des cas particuliers

`productByHandle` sur 8 fiches sensibles, après écriture :

- GMT (`voyageur-or-gmt-president`, `voyageur-bicolore-gmt-5-maillons`) : **349 / 378 / 388 / 417 €**, inchangés ✅
- Intégrale (`integrale-noir`, `integrale-brun-or-rose`) : **329 €** ✅
- Remontoirs bois (`remontoir-bois-noyer`, `remontoir-bois-acajou`) : **79,90 / 109,90 €**, inchangés ✅
- Squelette octogone : **279 / 299 €** ✅ · Chronographe panda : **239 €** ✅
- `compareAtPrice` nul sur toutes ✅ · statut `ACTIVE` sur toutes ✅

---

## 6. ⛔ Anomalie trouvée, hors périmètre — 2 074 prix barrés sur les fiches non actives

Le scan complet a révélé que **la purge du 08/08 n'a jamais couvert les brouillons ni les archivées** :

| Statut | Variantes | `compareAtPrice` non nuls | Fiches |
|---|---:|---:|---:|
| **ACTIVE** | 883 | **0** ✅ | 0 |
| **DRAFT** | 1 978 | **1 926** ⛔ | 86 / 95 |
| **ARCHIVED** | 148 | **148** ⛔ | 10 / 10 |

**Je n'y ai pas touché** : le ticket dit explicitement que les 95 brouillons ne sont pas concernés
par cette grille et qu'il ne faut rien modifier d'autre.

⚠️ **Mais c'est une bombe à retardement pour Merchant Center** : le prix barré est le motif de refus
n°1 sur une boutique à 0 vente, et **la seconde où l'un de ces 86 brouillons est activé, il arrive
avec son prix barré**. → **ticket dédié à ouvrir : purger les 2 074 `compareAtPrice` des brouillons
et des archivées avant toute activation.**

---

## 7. Méthode d'écriture

- `productVariantsBulkUpdate` **aliasé** (`m0:`, `m1:`… jusqu'à 8 par document), **12 documents** au
  total, lots calibrés sur ≤ 110 variantes.
- `userErrors` contrôlé à chaque appel : **0 sur les 12**.
- **`compareAtPrice` n'apparaît dans aucune mutation** — le champ n'a jamais été envoyé, donc jamais
  écrit.
- Rien d'autre n'a été envoyé : ni `status`, ni titre, ni description, ni média, ni collection, ni
  option de variante.

## 8. Ce qui reste ouvert

1. ⛔ **Purger les 2 074 prix barrés** des 86 brouillons et 10 archivées (ticket à créer).
2. ⚠️ **Relever le coût DSers des 4 remontoirs bois** — leur marge est toujours invérifiable.
3. ⚠️ **Corriger la grille sur le GMT** : le haut de gamme est 417 €, pas 419 €.
4. ⚠️ **Arbitrer les paliers de l'Aviateur bronze** (304 / 314 / 319 / 324 €).
5. ⚠️ **Reconfirmer par l'API les coûts de classe B** (28 fiches : chronographes, GMT, Intégrale,
   Héritage) — les marges annoncées sont un plancher.
6. ⛔ **Exclure des campagnes payantes** : les 7 Intégrale, les 9 fiches à ratio cassé, et tout
   accessoire sous 70 €.
---

## Annexe — le détail fiche par fiche

### Les 65 fiches modifiées

| Fiche | variantes | Avant | Après |
|---|---:|---|---|
| `bracelet-cuir-daim-degagement-rapide` | 64 | 17.9 € | **24.9 €** |
| `bracelet-fkm-courbe` | 48 | 29.9 / 34.9 € | **39.9 €** |
| `bracelet-fkm-tropical` | 108 | 29.9 / 34.9 € | **39.9 €** |
| `bracelet-milanais-maille-italienne` | 32 | 14.9 / 24.9 € | **19.9 / 24.9 €** |
| `bracelet-presidentiel-acier-inoxydable` | 4 | 39.9 / 49.9 € | **49.9 / 54.9 €** |
| `bracelet-presidentiel-dore` | 8 | 54.9 / 59.9 € | **59.9 / 64.9 €** |
| `coffret-6-montres-couvercle-verre` | 1 | 54.9 € | **69.9 €** |
| `coffret-douze-aluminium` | 3 | 24.9 / 34.9 / 69.9 € | **69.9 / 84.9 / 99.9 €** |
| `contre-la-montre-argent-chronographe` | 1 | 299 € | **239 €** |
| `contre-la-montre-blanc-chronographe` | 3 | 299 € | **239 €** |
| `contre-la-montre-bleu-glacier-chronographe` | 1 | 299 € | **239 €** |
| `contre-la-montre-champagne-chronographe` | 2 | 299 € | **239 €** |
| `contre-la-montre-compteurs-bleus-chronographe` | 1 | 299 € | **239 €** |
| `contre-la-montre-gris-anthracite-chronographe` | 1 | 299 € | **239 €** |
| `contre-la-montre-noir-chronographe` | 2 | 299 € | **239 €** |
| `contre-la-montre-panda-chronographe` | 2 | 299 € | **239 €** |
| `contre-la-montre-panda-inverse-chronographe` | 2 | 299 € | **239 €** |
| `contre-la-montre-rose-poudre-chronographe` | 1 | 299 € | **239 €** |
| `contre-la-montre-turquoise-chronographe` | 2 | 299 € | **239 €** |
| `contre-la-montre-vert-chronographe` | 2 | 299 € | **239 €** |
| `etui-de-voyage-rigide` | 9 | 69.9 / 89.9 / 109.9 / 189.9 € | **69.9 / 89.9 / 109.9 / 149.9 €** |
| `integrale-blanc-argente-sport-chic-acier` | 1 | 379 € | **329 €** |
| `integrale-bleu-ciel-sport-chic-acier` | 1 | 379 € | **329 €** |
| `integrale-bleu-nuit-sport-chic-acier` | 1 | 379 € | **329 €** |
| `integrale-brun-or-rose-sport-chic` | 1 | 379 € | **329 €** |
| `integrale-noir-sport-chic-acier` | 1 | 379 € | **329 €** |
| `integrale-turquoise-sport-chic-acier` | 1 | 379 € | **329 €** |
| `integrale-vert-sport-chic-acier` | 1 | 379 € | **329 €** |
| `montre-acier-chiffres-3-6-9-explorateur` | 104 | 279 / 309 / 319 / 349 € | **279 / 289 / 299 / 309 €** |
| `montre-aviateur-acier-cadran-chiffres-1-12` | 6 | 289 / 318 / 328 / 357 / 378 / 407 € | **279 / 289 / 299 / 309 / 319 / 329 €** |
| `montre-aviateur-bronze-cadran-chiffres-1-12` | 6 | 289 / 318 / 328 / 357 / 378 / 407 € | **299 / 304 / 314 / 319 / 324 / 329 €** |
| `montre-field-acier-cadran-chiffres-1-12` | 66 | 289 / 318 / 328 / 357 / 378 / 407 € | **279 / 289 / 299 / 309 / 319 / 329 €** |
| `montre-field-bronze-cadran-chiffres-1-12` | 18 | 328 / 357 € | **299 / 329 €** |
| `montre-squelette-automatique-carree` | 2 | 399 € | **279 €** |
| `montre-squelette-automatique-octogone` | 4 | 399 / 429 € | **279 / 299 €** |
| `quarante-et-un-blanc-cuir-sport-acier` | 2 | 299 / 338 € | **279 / 299 €** |
| `quarante-et-un-bleu-acier-sport-acier` | 2 | 299 / 338 € | **279 / 299 €** |
| `quarante-et-un-bleu-cuir-sport-acier` | 2 | 299 / 338 € | **279 / 299 €** |
| `quarante-et-un-noir-acier-sport-acier` | 2 | 299 / 338 € | **279 / 299 €** |
| `quarante-et-un-noir-cuir-sport-acier` | 2 | 299 / 338 € | **279 / 299 €** |
| `quarante-et-un-noir-jaune-acier-sport-acier` | 2 | 299 / 338 € | **279 / 299 €** |
| `quarante-et-un-sport-acier` | 4 | 299 / 338 € | **279 / 299 €** |
| `remontoir-collection-bois-beige` | 4 | 104.9 / 219.9 / 249.9 / 299.9 € | **104.9 / 219.9 / 249.9 / 269.9 €** |
| `remontoir-collection-bois-noir` | 4 | 104.9 / 224.9 / 249.9 / 289.9 € | **104.9 / 224.9 / 249.9 / 269.9 €** |
| `remontoir-collection-cuir-pu` | 3 | 254.9 / 274.9 / 324.9 € | **249.9 / 259.9 / 269.9 €** |
| `remontoir-solo` | 2 | 59.9 / 64.9 € | **64.9 €** |
| `rouleau-de-voyage-bleu-marine-cuir` | 3 | 29.9 / 39.9 / 49.9 € | **39.9 / 44.9 / 49.9 €** |
| `rouleau-de-voyage-brun-cuir` | 3 | 34.9 / 44.9 / 49.9 € | **39.9 / 44.9 / 49.9 €** |
| `rouleau-de-voyage-noir-cuir` | 3 | 34.9 / 44.9 / 49.9 € | **39.9 / 44.9 / 49.9 €** |
| `rouleau-de-voyage-vert-cuir` | 3 | 34.9 / 39.9 / 49.9 € | **39.9 / 44.9 / 49.9 €** |
| `trente-neuf-bleu-classique-cannelee` | 8 | 329 / 358 / 368 / 397 € | **279 / 299 / 309 / 329 €** |
| `trente-neuf-bleu-mer-classique-cannelee` | 8 | 329 / 358 / 368 / 397 € | **279 / 299 / 309 / 329 €** |
| `trente-neuf-classique-cannelee` | 8 | 329 / 358 / 368 / 397 € | **279 / 299 / 309 / 329 €** |
| `trente-neuf-duo-classique-bicolore` | 6 | 319 / 358 € | **279 / 309 €** |
| `trente-neuf-duo-dore-classique-bicolore` | 6 | 348 / 387 € | **299 / 329 €** |
| `trente-neuf-noir-classique-cannelee` | 8 | 329 / 358 / 368 / 397 € | **279 / 299 / 309 / 329 €** |
| `trente-neuf-rose-classique-cannelee` | 8 | 329 / 358 / 368 / 397 € | **279 / 299 / 309 / 329 €** |
| `trente-neuf-rouge-classique-cannelee` | 8 | 329 / 358 / 368 / 397 € | **279 / 299 / 309 / 329 €** |
| `trente-neuf-vert-classique-cannelee` | 8 | 329 / 358 / 368 / 397 € | **279 / 299 / 309 / 329 €** |
| `trente-six-bleu-classique-jubile` | 4 | 299 / 328 € | **239 / 259 €** |
| `trente-six-classique-jubile` | 4 | 299 / 328 € | **239 / 259 €** |
| `trente-six-dore-classique-jubile` | 4 | 299 / 328 € | **239 / 259 €** |
| `trente-six-or-integral-classique-jubile` | 4 | 299 / 328 € | **239 / 259 €** |
| `trente-six-rose-classique-jubile` | 4 | 299 / 328 € | **239 / 259 €** |
| `trente-six-rouge-classique-jubile` | 4 | 299 / 328 € | **239 / 259 €** |

### Les 31 fiches laissées intactes

| Fiche | variantes | Prix (inchangé) |
|---|---:|---|
| `barrettes-de-rechange-270` | 4 | 12.9 € |
| `bracelet-acier-massif-12-22-mm` | 60 | 39.9 / 49.9 / 59.9 € |
| `bracelet-caoutchouc-gaufre` | 72 | 24.9 € |
| `bracelet-jubile-acier-20mm` | 1 | 49.9 € |
| `bracelet-jubile-embouts-courbes` | 15 | 29.9 / 34.9 / 39.9 € |
| `carte-cadeau-maison-noirmont` | 4 | 50 / 100 / 150 / 300 € |
| `coffret-douze-presentation` | 1 | 94.9 € |
| `coussins-de-presentation-lot-de-10` | 5 | 19.9 € |
| `doigtiers-d-horloger-latex` | 6 | 12.9 € |
| `heritage-bleu-nuit-plongeuse-vintage-42` | 1 | 279 € |
| `heritage-bleu-plongeuse-vintage-42` | 1 | 279 € |
| `heritage-vert-plongeuse-vintage-42` | 1 | 279 € |
| `kit-d-entretien-13-pieces` | 1 | 29.9 € |
| `loupe-d-horloger` | 13 | 12.9 / 21.9 € |
| `loupe-de-date-saphir` | 8 | 12.9 € |
| `outil-de-mise-a-taille-de-bracelet` | 2 | 19.9 € |
| `pince-a-barrettes` | 3 | 12.9 / 19.9 € |
| `remontoir-bois-acajou` | 2 | 79.9 / 109.9 € |
| `remontoir-bois-ebene` | 2 | 79.9 / 109.9 € |
| `remontoir-bois-noir-laque` | 2 | 79.9 / 109.9 € |
| `remontoir-bois-noyer` | 2 | 79.9 / 109.9 € |
| `remontoir-collection-bois-led-noir` | 2 | 184.9 / 219.9 € |
| `remontoir-collection-bois-led-rouge` | 2 | 184.9 / 219.9 € |
| `remontoir-vitrine` | 1 | 129.9 € |
| `set-tournevis-horloger` | 5 | 59.9 € |
| `voyageur-bicolore-cadran-brun-gmt` | 4 | 349 / 378 / 388 / 417 € |
| `voyageur-bicolore-gmt-3-maillons` | 4 | 349 / 378 / 388 / 417 € |
| `voyageur-bicolore-gmt-5-maillons` | 4 | 349 / 378 / 388 / 417 € |
| `voyageur-or-gmt-3-maillons` | 4 | 349 / 378 / 388 / 417 € |
| `voyageur-or-gmt-president` | 4 | 349 / 378 / 388 / 417 € |
| `voyageur-or-rose-gmt-5-maillons` | 4 | 349 / 378 / 388 / 417 € |
