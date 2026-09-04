# Décisions en attente — Lumière Matière

Au 04/09/2026, fin de journée. Rien ici ne peut avancer sans un arbitrage de Hakim.
Le reste du travail est décrit dans `TABLEAU.md` et `shopify/ETAT.md`.

---

## D-1 · Trois titres qui décrivent un autre produit — **bloquant GMC**

Ce ne sont pas des libellés approximatifs. Un titre qui annonce un produit différent de celui
qui est vendu tombe dans la misrepresentation, au même titre que le montage en image principale.

| Fiche | Titre actuel | Ce qui est vendu | Proposition |
|---|---|---|---|
| `suspension-rotin-272937` | « Suspension cuisine, **3 boules** corde à **monture noire** » | **3 plafonniers simples** Ø 16 × H 17, montures noire / blanche / noire à jute brune | « **Plafonnier** corde tressée, Ø 16 cm » |
| `suspension-deco-blanc-560098` | « Suspension céramique cuisine, **double** à motif bleu » | 2 suspensions **simples** Ø 19,5, l'une à motif floral, l'autre à rayures | « Suspension céramique peinte main, Ø 19,5 cm » |
| `suspension-effet-pierre-led-147607` | « Suspension travertin cuisine, **cône ou galet** beige » | 3 formes : galet bas, cylindre haut, **bloc rectangulaire** | « Suspension travertin, trois formes » |

**Conséquence sur `272937` au-delà du titre** : ce sont des plafonniers, et la fiche est rangée
dans `suspensions-rotin` et `suspensions-cuisine`. À déplacer vers `plafonniers-led` /
`plafonniers-cuisine` — ce qui fait remonter `plafonniers-cuisine` de 1 à 2 produits.

**Ta décision** : valides-tu les trois titres proposés, et le déplacement de collection de 272937 ?

---

## D-2 · Renommage des libellés de `suspension-rotin-607504`

Cotes prouvées par Codex : `2550` = Ø 25 × H 50 · `4040` = Ø 40 × H 40 · `4019` = Ø 40 × H 19 ·
`4040BK` = Ø 40 × H 40 **noir**. Le doublon apparent « 40 × 40 cm » est donc naturel vs noir.

Proposition : `Ø 25 × H 50 cm · naturel` · `Ø 40 × H 40 cm · naturel` · `Ø 40 × H 19 cm · naturel` ·
`Ø 40 × H 40 cm · noir`.

Le schéma coté et le packshot « noir » attendent cette décision (lot 3, point G).

---

## D-3 · Doublons fournisseur de `suspension-rotin-897170`

Question fermée : les deux références « Ø 50 cm · rotin » sont **rigoureusement identiques**. Le
fournisseur a deux entrées de SKU pour un seul article. Idem probablement pour les « Ø 60 cm ».

Trois options, toutes tiennent :

1. **Supprimer les trois variantes « 2 »** — le client ne voit plus de choix identiques. Coût :
   on perd le stock rattaché (10 + 18 + 5 unités) et le mapping DSers de ces SKU.
2. **Les garder et renommer** en `Ø 50 cm · rotin (lot 2)` — honnête mais toujours incompréhensible
   pour un client.
3. **Ne rien faire** — statu quo, deux lignes identiques dans le sélecteur.

Ma recommandation : **option 1**, après vérification dans DSers que les SKU restants couvrent le
stock. C'est le seul choix où le client ne voit pas deux fois la même chose.

---

## D-4 · Sort des montages une fois les nouvelles vues livrées

Sur `147607` et `560098`, les montages ont été **relégués en fin de galerie**, pas supprimés.
Quand le lot 3 aura livré les vues de remplacement : les supprimer, ou les laisser en fin de
galerie ?

Ma recommandation : **les supprimer**. Ils restent dans `additional_image_link` du flux tant
qu'ils sont là, et ils montrent des produits non vendus.

---

## Ce qui n'attend personne

- Lot 3 Codex, points A à C : les références sont là, les faits sont établis, ça peut partir.
- Points D et E du lot 3 (scraping de `338324` modèle A et de `837156`) : questions ouvertes que
  Codex peut trancher seul.
