# Import des visuels de variantes — 04/09/2026

Livraison Codex (`livraisons-visuels-codex/variantes-forme/`, 34 fichiers) contrôlée et importée
dans Shopify. Go Hakim : « Codex a terminé, tu peux check, ajouter les images et après je publie ».

## Contrôle avant import

Planches `qa-packshots.jpg` (26) et `qa-schemas.jpg` (8) relues à l'œil, 20 manifestes lus.
DA conforme au lot d'août : fond papier, lumière chaude, packshot cadré comme le `g1`, 2048².
Les schémas cotés annoncent explicitement leurs trous (« Hauteurs et rosace : cotes non
documentées », « Échelle comparative des largeurs uniquement ») — c'est la bonne honnêteté.

**Correction du 405368 bien appliquée** : `beige-et-blanc` est repartie de `A2.jpg` (Beige+White),
disque **blanc** et câble **blanc**. L'erreur de référence de mon brief est effacée.

Le rapprochement variante → image se fait par **identifiant d'option fournisseur**
(`200000531:193` …), pas par libellé — la règle tirée de l'incident A2/D1.

## Import

Chaîne : `stagedUploadsCreate` → POST GCS (34/34 en 201) → `productCreateMedia` (18 produits) →
`productVariantsBulkUpdate` (10 produits, **41 variantes**).

| Fiche | Variantes servies | Images |
|---|---|---|
| `suspension-deco-253182` | A · B · C | 3 |
| `suspension-deco-blanc-560098` | A · B | 2 |
| `suspension-effet-pierre-092465` | Pierre claire · Brun | 2 |
| `suspension-effet-pierre-led-147607` | Forme A · B · C | 3 |
| `suspension-effet-pierre-led-338324` | B · C · D (9 variantes) | 3 |
| `suspension-metal-led-dore-975417` | A · B · C · D | 4 |
| `suspension-rotin-623305` | Pans coupés · Dôme arrondi (6 variantes) | 2 |
| `suspension-rotin-897170` | rotin (4) · plastique (3) | 2 |
| `suspension-verre-405368` | 3 coloris | 3 |
| `suspension-verre-538307` | Vert · Blanc | 2 |

Huit schémas cotés ajoutés en fin de galerie (pas de variante associée) : `applique-murale-pierre-588683`,
`lustre-anneau-led-led-795468`, `lustre-salon-blanc-246282`, `suspension-bambou-655008`,
`suspension-bambou-led-50cm-377816`, `suspension-bambou-led-630923`,
`suspension-moderne-led-noir-330664`, `suspension-rotin-led-761433`.

Chaque média porte un `alt` descriptif rédigé à l'import (forme, matière, cotes quand elles sont
prouvées) — plus aucun artefact de génération.

## Contrôle après import

52 produits publics · 161 variantes · **161/161 SKU DSers intacts** · 0 `compare_at_price`.
Les 10 fiches traitées montrent bien une image par valeur d'option distincte. Vérifié en vitrine
sur `suspension-metal-led-dore-975417` (choisir A/B/C/D change la photo principale) et
`suspension-bambou-655008` (schéma en galerie, alt correct).

Le compteur brut « variantes partageant une photo » passe de 125/161 à 105/161, mais **ce chiffre
n'est plus le bon indicateur** : sur 338324, 623305 et 897170, le partage restant est légitime —
trois températures d'ampoule ou deux diamètres du même objet partagent forcément la même photo.
Ce qui compte : plus aucune variante ne montre un objet qui n'est pas le sien.

## Effet de bord assumé sur l'allumage au survol

Le réglage `lm_hover_light` se désactive quand la variante par défaut a sa propre image — c'est le
garde-fou écrit hier, et il joue. Mesuré en prévisualisation : `suspensions-bambou` 3 cartes sur 3
gardent l'effet ; `suspensions-deco` 2 sur 5, les trois autres montrent leur packshot de variante.

C'est le bon arbitrage : là où on sait montrer la bonne couleur ou la bonne forme, on la montre ;
là où on n'a qu'un objet, on montre la lumière.

## Reste ouvert

- **`suspension-effet-pierre-led-338324`, modèle A** : pas d'image. Codex n'a pas trouvé
  l'identifiant `200000531:193` dans le sélecteur fournisseur du 04/09 et **a refusé de le déduire
  par élimination**. Les 3 variantes A gardent le `g1`. Bonne décision.
- **`suspension-rotin-272937` — mon diagnostic était faux.** J'avais lu dans la planche fournisseur
  une suspension simple, une applique murale et deux trios, et alerté sur « une applique dans une
  fiche de suspension ». Codex a vérifié les SKU réellement vendus : **A1/B1/C1 sont trois
  plafonniers Ø 16 × H 17** (abat-jour H 12), qui diffèrent par la monture et le cordon — noire /
  corde dorée, blanche / corde claire, noire / fibre brune. La planche montrait le catalogue du
  fournisseur, pas les trois SKU de la fiche. **Il n'y a pas d'applique murale à sortir.** Reste à
  décider les libellés (le titre « 3 boules corde à monture noire » ne décrit qu'une des trois).
- **`suspension-rotin-607504`** : dimensions prouvées — `2550` = Ø 25 × H 50, `4040` = Ø 40 × H 40,
  `4019` = Ø 40 × H 19, `4040BK` = Ø 40 × H 40 **noir**. Le doublon apparent « 40 × 40 cm » est donc
  naturel vs noir. Renommage évident à valider, puis schéma à produire.
- **Variantes « 2 » (P3)** de `suspension-rotin-897170` et `suspension-deco-led-837156` : toujours
  sans distinction lisible. Elles partagent désormais correctement la photo de leur matière/émail.

## Périmètre

Aucun SKU touché, aucun média d'origine supprimé, aucun brouillon publié, aucun délai modifié.
Les nouvelles images sont **en ligne** (les médias produit ne dépendent pas du thème) ; la copie
`LM UX 2026-09-04` reste à publier par Hakim.
