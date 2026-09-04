# Arbitrages D-1 à D-4 — titres, libellés, doublons, montages

Date : **04/09/2026 (soir)** · Boutique : **Lumière Matière** · Décisions prises par Hakim sur
`DECISIONS-EN-ATTENTE.md`, D-1 délégué (« c'est l'occasion de revoir les titres et de les optimiser
pour le SEO / GMC donc je te laisse faire »).

Contrôle final : **52 produits ACTIVE / 158 variantes** (161 − 3 supprimées), **0 prix barré**,
**SKU DSers intacts** — toutes les mutations passées en `variantStrategy: LEAVE_AS_IS`.

## D-1 — trois titres faux, réécrits sur la convention

Grille de `CONVENTION-TITRES-2026-08-25.md`, avec la correction de volumes qui fait primer le
mot-pièce sur la matière (`plafonnier cuisine` 5 400/mois, `suspension cuisine` 4 400).

| Fiche | Avant | Après | c. |
|---|---|---|---:|
| `suspension-rotin-272937` | Suspension cuisine, 3 boules corde à monture noire | **Plafonnier cuisine, dôme en corde tressée** | 41 |
| `suspension-deco-blanc-560098` | Suspension céramique cuisine, double à motif bleu | **Suspension céramique cuisine, cloche laiton** | 43 |
| `suspension-effet-pierre-led-147607` | Suspension travertin cuisine, cône ou galet beige | **Suspension travertin cuisine, monture noyer** | 42 |

Aucune cote, aucun `Ø`, aucune énumération partielle de formes, aucun mot d'ambiance. Les
`seo.title` et `seo.description` ont été réécrits **en bloc** avec les titres (piège connu :
`ProductInput.seo` remplace, il n'ajoute pas).

**Deux corps de fiche étaient faux eux aussi et ont été repris** :

- `272937` annonçait « suspension en fibre tressée » posant « une lumière basse au-dessus d'une
  table » — faux pour un plafonnier à fixation directe, sans câble. Réécrit sur les cotes réelles
  (Ø 16, H 17, rosace 10, E27).
- `147607` dit « il vous faudra une ampoule E27 » alors que le SKU porte
  `136:200003939#Warm light 3000K`, c'est-à-dire une source intégrée. **Les deux ne peuvent pas
  être vrais.** Plutôt que d'arbitrer au jugé, j'ai **retiré `LED` du titre** et basculé sur un
  détail prouvé (la monture noyer, commune aux trois formes, lue dans les `alt` du lot 2).
  **Question ouverte pour Hakim / DSers : cette fiche est-elle vendue avec ou sans ampoule ?**

### Déplacement de collection

`272937` n'est pas une suspension : ce sont trois **plafonniers** Ø 16 × H 17 à montage direct.

- Retiré de `suspensions-rotin` (14 → 13) et `suspensions-cuisine` (33 → 32)
- Ajouté à `plafonniers-cuisine` (**4 → 5 produits** — la collection repasse au-dessus du seuil)
- `productType` `Suspensions rotin` → `Plafonniers`, tag idem
- **Pas** rattaché à `plafonniers-led` : la collection porte « LED » dans son intitulé et cette
  fiche est en E27. On ne range pas une fiche sous un attribut qu'elle n'a pas.

Les trois collections sont **manuelles** (`ruleSet: null`) : le déplacement ne pouvait pas se faire
en changeant seulement le `productType`.

## D-1 bis — une quatrième anomalie, trouvée en chemin

`suspension-rotin-607504` s'intitulait « Suspension rotin tressé **noir**, monture bois » alors que
le noir n'est **qu'une variante sur quatre** (25 %). La convention n'admet la couleur qu'au-dessus
de 60 %. Même défaut que les trois autres, sur une fiche déjà ouverte :
→ **« Suspension rotin tressé cuisine, monture bois »** (44 c.).

## D-2 — libellés de `607504`

**Le brief Codex du lot 3 donnait un mapping identifiant → code INVERSÉ** (`367 = 2550`,
`193 = 4040`). Les preuves DOM (`variantes-20260904/preuves-dom.json`, horodatées 04/09 15:22) et
les SKU Shopify concordent entre elles et disent l'inverse. Les quatre références l'ont confirmé
à l'œil.

| SKU | Identifiant | Code | Réel |
|---|---|---|---|
| `…795:193#2550` | 193 | 2550 | Ø 25 × H 50, **naturel**, goutte |
| `…795:10#4040` | 10 | 4040 | Ø 40 × H 40, **naturel**, bulbe |
| `…795:175#4019` | 175 | 4019 | Ø 40 × H 19, **naturel**, coupole plate |
| `…795:367#4040BK` | 367 | 4040BK | Ø 40 × H 40, **noir**, même silhouette que 4040 |

Les cotes des libellés étaient donc **déjà justes** ; ce qui manquait était la finition, d'où le
faux doublon « 40 × 40 cm » / « 40 × 40 cm · Noir ». Corrigé :
`25 × 50 cm · naturel` · `40 × 40 cm · naturel` · `40 × 19 cm · naturel` · `40 × 40 cm · noir`,
option `Taille` → **`Taille et finition`** (elle ne portait plus seulement une taille).

**Règle : le code d'une variante se lit dans le SKU et dans `preuves-dom.json`, jamais dans la
lecture d'une image ni dans un nom de fichier.** C'est la deuxième fois en une journée que la
lecture d'image induit en erreur (cf. `405368` le matin) — la règle est la même dans les deux sens.

## D-3 — doublons de `suspension-rotin-897170`

Les **trois paires** ont été vérifiées image par image avant toute suppression :

| Paire | Verdict |
|---|---|
| `193` / `29` — « Ø 50 cm · rotin » | identiques (même corolle, 50 cm, « 1.2m ~1.4m Adjustable », même avertissement jaunissement) |
| `175` / `350852` — « Ø 60 cm · plastique » | identiques (60 × 30, « Plastic material », « 1.2m Adjustable ») |
| `1052` / `173` — « Ø 60 cm · rotin » | identiques (60 × 30, « rattan », même avertissement) |

**Écart assumé avec ma recommandation initiale.** J'avais proposé de supprimer les variantes à
suffixe « 2 ». En les regardant, c'est **la « 2 » qui porte le plus de stock** dans deux paires sur
trois (rotin 50 : 3 vs 10 ; rotin 60 : 4 vs 5). Les deux membres d'une paire **partagent déjà la
même image** : le choix du survivant est libre côté visuel, et le seul critère qui reste est la
profondeur d'approvisionnement. J'ai donc gardé le SKU le mieux servi et renommé les libellés.

| Supprimée | Stock | Conservée | Stock |
|---|---:|---|---:|
| `…531:193#rattan 50cm` | 3 | `…531:29#rattan 50cm` → « Ø 50 cm · rotin » | 10 |
| `…531:350852#Plastic 60cm` | 18 | `…531:175#Plastic 60cm` | 19 |
| `…531:1052#rattan 60cm` | 4 | `…531:173#rattan 60cm` → « Ø 60 cm · rotin » | 5 |

La fiche passe de **7 à 4 variantes**, sans suffixe « 2 », sans perte de photo.

## D-4 — montages fournisseur supprimés

| Fiche | Supprimé | Reste |
|---|---|---|
| `suspension-effet-pierre-led-147607` | `g1`, `g2`, `g5` (10-12 lampes dans le cadre) | forme-a/b/c + `g3` + `g4` = **5** |
| `suspension-deco-blanc-560098` | `g1` à `g5` (suspension **double**, non vendue) | a-g1 + b-g1 = **2** |

Les cinq images retirées de `560098` portaient toutes l'`alt` « Suspension **double** en céramique »
— la misrepresentation est partie avec elles. Image de flux : `forme-a-g1` et `a-g1`, deux
packshots mono-produit.

**`suspension-rotin-272937` n'est pas touchée** : ses cinq médias sont tous des montages, les
supprimer la laisserait **sans aucune image**. Elle attend le lot 3 Codex (8 visuels).

## Suites

1. **Lot 3 Codex à envoyer** — brief corrigé ce soir : le point G (`607504`) est **débloqué**
   (2 visuels : schéma coté + packshot noir), le point F (`897170`) est **clos**. Total 18 images.
2. **`272937`** : supprimer ses 5 montages une fois les 5 nouvelles vues livrées.
3. **`147607`** : trancher avec / sans ampoule (SKU `Warm light 3000K` contre corps de fiche E27).
4. **`338324`** modèle A sans image, **`837156`** « 2 » non scrapées — deux questions Codex.
