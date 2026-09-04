# Revue de tous les libellés de variante

Date : **04/09/2026 (soir)** · Boutique : **Lumière Matière** · 52 fiches passées en revue.
Suite de `journal/2026-09-04-import-lot3-montages.md`.

**7 fiches renommées, 30 libellés réécrits, 3 titres corrigés.**
Contrôle : 52 produits / 158 variantes / SKU DSers intacts (toutes les mutations en
`variantStrategy: LEAVE_AS_IS`).

## La trouvaille : les lettres de la boutique ne sont pas celles du fournisseur

Sur `suspension-effet-pierre-led-338324`, les preuves DOM du lot 3 portent les **libellés
fournisseur** :

| SKU option | Libellé fournisseur | Lettre boutique |
|---|---|---|
| `200000531:173` | `A-Dark wood color` | **B** |
| `200000531:365458` | `B-Wood color` | **C** |
| `200000531:175` | `B-Dark wood color` | **D** |
| `200000531:193` | *(absent du sélecteur)* | **A** |

Le fournisseur décrit une **grille 2 × 2** — deux formes (A / B) × deux teintes de bois
(clair / noyer). Les lettres `A/B/C/D` de la boutique ont été attribuées à l'import et ne
recouvrent rien : un client qui choisit « Modèle B » croit prendre la deuxième forme, il prend
la première en noyer. Même famille de piège que l'inversion du mapping de `607504` ce matin.

Les libellés sont désormais : `Cylindre bas · tête bois clair` · `Cylindre bas · tête noyer` ·
`Cylindre haut · tête bois clair` · `Cylindre haut · tête noyer`.

**Le cas de `200000531:193`** — le modèle déclaré introuvable par Codex — est la seule cellule
reconstituée : la grille fournisseur en fait nécessairement `A-Wood color`, et la planche cotée
`05.jpg` (Ø 12 × H 10, tête bois **clair**) le montre. Ce n'est pas une déduction par
élimination entre objets sans rapport, c'est la lecture d'une grille dont trois cases sur quatre
sont observées. **À confirmer quand même** au prochain scraping.

## Les 7 fiches renommées

| Fiche | Avant | Après | Preuve |
|---|---|---|---|
| `suspension-rotin-272937` | `Modèle A / B / C` | `Monture noire · corde claire` · `Monture blanche · corde crème` · `Monture noire · jute brune` | packshots lot 3 |
| `suspension-effet-pierre-led-147607` | `Forme A / B / C` | `Galet bas` · `Cylindre haut` · `Bloc rectangulaire` | `alt` lot 2, vérifiés |
| `suspension-deco-blanc-560098` | `A / B` | `Motif floral bleu` · `Rayures bleues et dorées` | packshots lot 2 |
| `suspension-deco-253182` | `A / B / C` | `Motif géométrique bleu` · `Vert canard` · `Rouge` | packshots lot 2 |
| `suspension-metal-led-dore-975417` | `A / B / C / D` | `Cloche lisse · Ø 18 × H 12 cm` · `Corolle plissée · Ø 21 × H 21 cm` · `Cloche lisse · Ø 18 × H 8 cm` · `Corolle plissée · Ø 23 × H 10,5 cm` | **cotes portées sur les références fournisseur** |
| `suspension-effet-pierre-led-338324` | `A / B / C / D` | grille forme × teinte de bois (ci-dessus) | libellés fournisseur au DOM |
| `suspension-deco-led-837156` | `Céladon vert 2`, `Céladon bleu poudré 2` | `… · H 6,5 cm` / `… · H 9 cm` | mesure Codex lot 3 |

Noms d'options remis en cohérence quand ils ne décrivaient plus leur contenu :
`Modèle` → `Finition` (272937), `Motif` (560098), `Émail` (253182), `Forme et taille` (975417),
`Forme et finition` (338324) ; `Émail` → `Émail et hauteur` (837156).

## Trois titres tombés avec les libellés

Écrire les libellés a rendu visibles trois titres qui annonçaient une minorité des variantes —
même défaut que `607504` ce matin, même risque de misrepresentation.

| Fiche | Avant | Après | Pourquoi |
|---|---|---|---|
| `suspension-deco-253182` | Suspension céramique **émaillée rouge**, monture laiton | Suspension céramique émaillée, monture laiton | le rouge est **1 émail sur 3** |
| `suspension-effet-pierre-led-338324` | Suspension travertin, gros cylindre **à tête noyer** | Suspension travertin cylindre, tête bois ou noyer | le noyer est **2 finitions sur 4** |
| `suspension-deco-led-837156` | Suspension céramique festonnée, **vert céladon** | Suspension céramique festonnée, céladon vert ou bleu | le vert est **2 émaux sur 4** — et mes propres libellés le contredisaient |

## Ce qui reste, et pourquoi je n'y ai pas touché

- **`suspension-bois-193329`** — `Noyer · forme A` / `Bois clair · forme A` / `… forme B`.
  La teinte est prouvée par le SKU (`Walnut Base` / `Wood color`), **la forme ne l'est pas** :
  aucune référence par variante en local, aucune cote. À scraper.
- **`suspension-bois-led-934110`** — l'option « Modèle » mélange une matière et deux températures
  de couleur : `Blanc froid 6000 K` · `Travertin` · `Blanc chaud 3000 K`. Ce n'est pas un axe.
  Les libellés sont pourtant la traduction fidèle des SKU (`6000k-cold white`, `Yellow
  Travertine`, `3000k-warm white`) : **l'incohérence est celle du fournisseur**, et la trancher
  demande de retourner sur la PDP.
- **`suspension-effet-pierre-092465`** — `Pierre claire` / `Brun` : vague mais pas faux, et les
  deux packshots existent. Laissé tel quel.
- **9 fiches à variante unique** portent `Default Title` : c'est le défaut Shopify d'un produit
  sans option, invisible en boutique. Rien à faire.

## Suite

Brief `briefs/2026-09-05-codex-lot4-couverture-variantes.md` : ce qui reste sans visuel propre,
mesuré fiche par fiche sur le catalogue live.
