# Brief Codex — visuels de variantes, lot 2 (formes + couleurs restantes)

Date : **04/09/2026** · Boutique : **Lumière Matière** (`lumierematiere.fr`) · Catalogue live : 52 ACTIVE / 161 variantes.
Suite de `2026-08-24-codex-variantes-couleur.md` (livré 124/124 le 25/08).
Audit source : `shopify/AUDIT-VARIANTES-2026-09-04.md`.

## Pourquoi ce lot existe

Le brief du 24/08 avait **volontairement écarté** les fiches à codes aveugles :

> « **13 fiches à codes aveugles** (A/B/C, A7…) : Codex ne peut pas inventer la forme.
> À traiter plus tard avec le listing AliExpress, pas comme un brief couleur. »

**Ce blocage est levé.** Les sources fournisseur locales documentent elles-mêmes les codes : sur
`suspension-rotin-623305`, les fichiers `01/02/03.jpg` portent le badge `A7`, `A8`, `A9` avec les
cotes. Pas besoin de retourner sur AliExpress.

État actuel : **125 variantes sur 161 (78 %) affichent la photo d'une autre variante.** Le
sélecteur ne change rien à l'écran.

## Direction artistique — inchangée depuis le 24/08

Ne rien réinventer. Les nouveaux visuels doivent être indiscernables des 124 déjà livrés.

| | |
|---|---|
| Fond | papier `#F6F3EC`, uni |
| Lumière | chaude |
| Type | packshot objet, **cadrage identique au `g1` du handle** |
| Format | JPEG RGB, **2048 × 2048**, sans compression visible |
| État allumé | allumé si le `g1` du handle l'est, éteint s'il l'est |
| Interdits | texte, logo, badge, cote, filigrane, main, visage, décor de pièce, table, plante, personne |

**Référence de cadrage** : `catalogues/lumierematiere/livraisons-visuels-codex/produits/{handle}/{handle}-g1.jpg`
**Référence matière/forme** : chemin donné variante par variante dans les JSON.

### Nommage

```
{handle}-{slug}-g1.jpg
```

`slug` = valeur de variante en minuscules, sans accent, espaces → tirets.
Exemple : `suspension-rotin-623305-dome-arrondi-g1.jpg`

### Livraison

```
catalogues/lumierematiere/livraisons-visuels-codex/variantes-forme/{handle}/
```

Un sous-dossier par handle, plus un `manifeste.json` au schéma existant (voir
`livraisons-visuels-codex/produits/suspension-verre-538307/manifeste.json`) : champs `brand`,
`sku`, `handle`, `supplier_id`, `images[{fichier, slot, source}]`, `ecartes`, `collection`.

**Aucune action Shopify ni DSers.** Le rattachement aux variantes se fait après QA, par script.
Les SKU (`sku_attr` DSers) sont **intouchables**.

## La règle qui change par rapport au lot 1

Le lot 1 ne faisait varier qu'une **teinte** sur une silhouette figée. Ici la **forme change**.

- **Ne pas** garder la silhouette du `g1` quand la variante est une autre forme : c'est tout
  l'objet du lot. Reproduire la forme de la référence fournisseur.
- **Garder** en revanche le cadrage, la distance, l'angle, le fond, la lumière et l'état
  allumé/éteint du `g1`.
- **Ne pas inventer** une matière, une finition ou un nombre de lumières absent de la référence.
- Une variante = une image, même si la fiche a plusieurs tailles derrière : le rattachement
  groupera ensuite toutes les variantes de cette forme.

## Trois lots, trois JSON

| Lot | Fichier | Fiches | Visuels |
|---|---|---:|---:|
| P1 — couleurs restantes | `2026-09-04-lot-p1-couleurs.json` | 4 | 7 à 9 |
| P2 — formes sous code | `2026-09-04-lot-p2-formes.json` | 7 | ~22 |
| P6 — schémas cotés | `2026-09-04-lot-p6-schemas.json` | 9 | 9 |

Chaque entrée porte `statut` :

- `"confirme"` — la référence par variante est identifiée, le rendu est décrit. **Générer.**
- `"a_identifier"` — la référence existe en local mais le lien code → forme n'est pas encore
  établi. **Lire d'abord les images fournisseur du dossier, établir le lien, le reporter dans le
  manifeste, puis générer.** Ne rien deviner : si la référence ne permet pas de trancher, livrer
  le reste et signaler la fiche.

## Ce qui a déjà été résolu, à titre d'exemple

`suspension-rotin-623305` — les trois abat-jour en corde de chanvre, E27 × 1, câble ajustable
jusqu'à 120 cm, monture et rosace noires :

| Code | Forme | Cotes |
|---|---|---|
| `A7` | tambour droit, paroi verticale | Ø 31 × H 18 cm |
| `A8` | pans coupés, profil diabolo | Ø 30 × H 16 cm |
| `A9` | dôme arrondi, profil citrouille | Ø 32 × H 16 cm |

Le `g1` existant a été composé depuis `01.jpg`, donc **il montre déjà A7**. Seuls `A8` et `A9`
sont à produire.

## Le lot P6 — schémas cotés, pas des packshots

Dix fiches où les variantes ne diffèrent **que par la dimension**. Partager une photo y est
légitime : c'est le même luminaire. Ce qui manque est l'échelle.

**Un seul visuel par fiche**, différent des packshots :

- Silhouette du luminaire en élévation, de face, sur le fond papier `#F6F3EC`
- Cotes portées : diamètre et hauteur de l'abat-jour, hauteur de câble ajustable, diamètre de rosace
- Trait fin, chiffres en gris charbon `#24211B`, unités en cm
- **C'est la seule exception à l'interdit « aucune cote, aucun texte »** — et elle ne vaut que pour
  ce lot
- Nom : `{handle}-schema-g6.jpg` · livraison dans `variantes-forme/{handle}/`

Cohérent avec la FAQ, qui prévient déjà : « le piège, c'est la photo : elle écrase toujours les
proportions ».

## Deux anomalies relevées, à trancher par Hakim — ne pas corriger seul

**`suspension-verre-405368`** — ~~anomalie de nommage~~ **CORRIGÉ le 04/09 : il n'y a pas
d'anomalie.** La première version de ce brief pointait la référence `D1.jpg` (« Beige + Green »)
et concluait à une variante mal nommée. Erreur d'analyse de ma part : le SKU de la variante est
`200000531:173#A2`, donc la référence est **`A2.jpg`**, étiquetée « Beige+White » — douille beige,
disque de verre blanc, **câble blanc**. La variante « Beige et blanc » est correctement nommée.
`D1.jpg` et `C1.jpg` sont des coloris fournisseur non vendus en boutique.

**Le visuel `suspension-verre-405368-beige-et-blanc-g1.jpg` livré le 04/09 est à REGÉNÉRER**
depuis `A2.jpg` : celui qui a été produit montre un disque vert.

**`suspension-rotin-272937`** — les codes `Modèle A / B / C` ne désignent **pas** une forme
d'abat-jour mais une **configuration** : la référence montre une suspension simple, une applique
murale, un trio à rosace ronde et un trio sur barre linéaire. Le titre actuel — « Suspension
cuisine, 3 boules corde à monture noire » — ne décrit qu'une de ces configurations. Le lien
lettre → configuration n'est pas établi par les images seules. **Ne pas générer avant arbitrage.**
