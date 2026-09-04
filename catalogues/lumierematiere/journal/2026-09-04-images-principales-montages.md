# Images principales : des montages fournisseur en tête de fiche — 04/09/2026

Signalement Hakim, après publication du thème : « J'ai encore ce souci de photo de variante
notamment sur `suspension-rotin-272937` où les photos sont les mêmes à chaque variante. »

Le symptôme est réel. La cause est plus profonde, et elle touche le flux Merchant Center.

## Ce qui a été trouvé

Planche contact des **52 images principales** du catalogue live, puis agrandissement des cas
suspects. Trois fiches ont pour image principale un **montage catalogue du fournisseur** — la
passe visuelle d'août a composé `g1` à partir d'une planche multi-produits au lieu d'isoler la
référence vendue.

| Fiche | Image principale | Ce qui est réellement vendu |
|---|---|---|
| `suspension-effet-pierre-led-147607` | **10 à 12 suspensions** travertin dans une seule image (`g1`, `g2`, `g5`) | 3 formes : galet bas, cylindre haut, bloc rectangulaire |
| `suspension-rotin-272937` | **5 configurations** : suspension simple, applique murale, trio à rosace ronde, trio sur barre linéaire | 3 **plafonniers** Ø 16 × H 17 (abat-jour H 12), montures et cordons différents |
| `suspension-deco-blanc-560098` | une suspension **double** (deux abat-jour sur une rosace) sur `g1` à `g5` | 2 suspensions **simples** Ø 19,5 × H 16, E27 × 1 |

`applique-murale-pierre-metal-147598` montre deux exemplaires du même modèle : risque moindre,
pas classé avec les trois précédentes.

**Pourquoi c'est sérieux.** L'image principale est celle qui part dans le flux Google Shopping.
Le collage est explicitement proscrit par la checklist GMC (« pas de collage, variante = image »),
et ici le montage ne se contente pas d'être un collage : il montre des produits qui **ne sont pas
vendus dans la fiche**. C'est le registre exact de la misrepresentation Noirmont.

## Corrigé tout de suite

Sur les deux fiches où Codex avait livré des packshots propres, les visuels de variante sont
**remontés en tête de galerie** (`productReorderMedia`), les montages relégués derrière :

- `suspension-effet-pierre-led-147607` → `forme-a`, `forme-b`, `forme-c`, puis `g3`, `g4`
  (les deux seules vues d'origine mono-produit), puis les montages `g1`, `g2`, `g5`
- `suspension-deco-blanc-560098` → `a-g1`, `b-g1`, puis les vues de la double

L'image du flux est donc désormais un packshot mono-produit sur ces deux fiches. Vérifié en
vitrine. Rien n'a été supprimé.

## Reste à faire — arbitrage Hakim

**1. `suspension-rotin-272937` — nouvelle passe Codex nécessaire.** Aucun packshot propre
n'existe : Codex l'avait mise en `BLOQUE_ARBITRAGE` et n'a rien produit. Les références par
variante sont maintenant scrapées (`sources-par-handle/suspension-rotin-272937/variantes-20260904/`,
avec `preuves-dom.json`), cotées et sans ambiguïté :

| Variante | SKU | Ce que montre la référence |
|---|---|---|
| Modèle A | `200000531:193#A1` | plafonnier, monture **noire**, corde papier beige clair, Ø 16 × H 17 |
| Modèle B | `200000531:1052#B1` | plafonnier, monture **blanche**, corde crème, Ø 16 × H 17 |
| Modèle C | `200000531:100018786#C1` | plafonnier, monture **noire**, **corde de jute brune** plus grossière, Ø 16 × H 17 |

Les références portent des cotes incrustées : elles ne peuvent pas être publiées telles quelles,
il faut les repasser en packshot maison. Il faut aussi **cinq nouvelles vues g1–g5 mono-produit**
pour remplacer le montage.

**2. Trois titres faux.** Ce ne sont pas des libellés approximatifs, ce sont des descriptions
d'un autre produit :

- `suspension-rotin-272937` : « Suspension cuisine, **3 boules** corde à **monture noire** » →
  ce sont trois **plafonniers simples**, et une seule des trois montures est noire. La fiche est
  en plus rangée dans `suspensions-rotin` et `suspensions-cuisine`, alors qu'il s'agit de
  plafonniers.
- `suspension-deco-blanc-560098` : « Suspension céramique cuisine, **double** à motif bleu » →
  ce sont deux suspensions **simples**, et la variante B est à rayures brunes et bleues, pas à
  motif.
- `suspension-effet-pierre-led-147607` : « cône ou galet beige » ne décrit que deux des trois
  formes (il manque le bloc rectangulaire).

Le renommage touche le titre, la catégorie et le rangement en collection : c'est ta décision.

**3. Rappels des points déjà ouverts** : modèle A de `suspension-effet-pierre-led-338324` sans
image ; libellés de `suspension-rotin-607504` (cotes prouvées, « 40 × 40 » = naturel vs noir) ;
variantes « 2 » de `suspension-rotin-897170` et `suspension-deco-led-837156`.

## Ce qu'on retient pour la méthode

**Un packshot maison n'est pas une garantie de conformité si sa source est une planche
fournisseur.** La passe d'août a produit 121 `g1` au slot `g1-hero-allume` sans contrôler que la
source `01.jpg` montrait un seul produit. Le contrôle manquant : ouvrir l'image principale de
chaque fiche live et compter les luminaires. Une planche contact de 52 vignettes suffit — c'est
ce qui a permis de trouver les trois cas en une lecture.
