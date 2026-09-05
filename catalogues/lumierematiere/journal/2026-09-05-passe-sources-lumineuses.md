# 05/09/2026 — Passe « source lumineuse » sur les 51 fiches

Suite du balayage SKU × `specs` ouvert avec `147607`. Sept fiches restaient suspectes.
Méthode : la plaque cotée du fournisseur, en local, plutôt que l'étiquette de l'axe.

---

## Résultat : 6 fiches sur 7 mentaient, toutes dans le même sens

| Fiche | Ce qu'elle disait | La vérité | Preuve |
|---|---|---|---|
| `805304` | « LED intégrée » | **E27, LED 4 W fournie, max 60 W** | plaque : *« e27 4w led bulb max 60w (bulb included) »* |
| `952116` | « LED intégrée » | idem **+ interrupteur sur la douille** | plaque, même formule |
| `121862` | « LED intégrée » | idem | plaque : *« E27 4w(max 60w) LED Bulb Included »* |
| `832012` | « LED intégrée **ou** douille E27 selon la variante » | **3 ampoules fournies**, identique sur les 3 variantes | ampoules visibles sur 4 vues ; l'axe `136` n'a qu'une valeur |
| `934110` | « douille G9, ampoule **non** fournie » | **G9, ampoule fournie et remplaçable** | titre fournisseur : *« rétro moderne G9 remplaçable »* + axe température |
| `829449` | « douille G9, ampoule non fournie » | plaque : *« G9\*1 Warm white LED For Free »* | **non modifiée — voir plus bas** |
| `814554` | « douille E27, ampoule non fournie » | non concluant | l'axe `136:200003938` n'a pas d'étiquette |

---

## Ce que la ligne `4W(Max 60W)` voulait vraiment dire

Trois fiches portaient dans leur SKU DSers `249:200006305#4W(Max 60W)` et annonçaient
« LED intégrée ». La plaque du fournisseur dit l'inverse, mot pour mot :
**douille E27, ampoule LED 4 W fournie, remplaçable jusqu'à 60 W.**

Ce n'est pas un détail de rédaction. La FAQ des trois fiches répondait :

> « Non, il n'y en a pas besoin : la LED est intégrée au luminaire. Rien à visser à la pose,
> **rien à remplacer ensuite**. »

Elle transformait un **argument de vente** — une douille standard, une ampoule qu'on change,
jusqu'à 60 W si on veut plus de lumière — en une limitation définitive. Et elle aurait fait
jeter le luminaire à la première ampoule grillée.

Corrigé sur les quatre surfaces des trois fiches : description, `usps`, `specs`, `installation`,
FAQ. **Règle à retenir : `Max 60 W` désigne le calibre d'une douille. Une LED intégrée n'a pas
de maximum, elle a une puissance.**

## Bonus : les plaques donnaient les cotes

Ces trois fiches n'ont qu'une variante (`Default Title`) et n'affichaient **aucune dimension**.
Les plaques les portent, elles sont maintenant dans les specs :

- `805304` — abat-jour Ø 30 cm, H 21,5 cm, câble ajustable 200 cm
- `952116` — Ø 18 cm, H 11 cm, câble 200 cm, **interrupteur marche/arrêt sur la douille laiton**
- `121862` — Ø 18,5 cm, H totale 25,5 cm, câble 200 cm
- `814554` — Ø 25 cm, H 20 cm (seule correction sur cette fiche)

L'interrupteur de `952116` ne figurait nulle part sur la boutique. C'est pourtant ce qui permet
de la poser là où il n'y a pas d'interrupteur mural.

---

## `934110` — la réponse était dans le titre de la page fournisseur

`preuves-dom.json` porte le titre AliExpress : *« … lustre de chevet pour chambre à coucher,
rétro moderne **G9 remplaçable** »*. Et l'axe secondaire `5-361385` vaut *« 3000K warm light »* —
on ne vend pas une température de blanc sur un luminaire livré sans source.

Donc : **douille G9, ampoule LED fournie, remplaçable.** Corrigé.

**Ce qui reste ouvert sur cette fiche est inchangé** : l'axe principal mélange une matière
(`Yellow Travertine`) et deux températures (`3000k-warm white`, `6000k-cold white`) dont les
deux vignettes sont identiques au SHA-256 près, et l'axe secondaire n'a qu'une valeur 3000 K
qui contredit la variante 6000 K. Les libellés de variantes n'ont pas été touchés.

---

## `829449` — je n'ai pas corrigé, et c'est délibéré

La plaque `07.jpg` dit **« G9\*1 Warm white LED For Free »**, et c'est la même plaque qui donne
les cotes 40 / 10 / 17 cm que la fiche utilise déjà. Le SKU lui-même porte `40-10-17CM warm LED`.
Tout pointe vers une ampoule fournie.

Mais **l'attribut DSers dit non**, et la fiche porte déjà une décision explicite et assumée :

> « Une photo fournisseur annonce parfois une ampoule offerte : l'attribut dit non,
> on promet le moins. »

Promettre moins que ce qu'on livre ne lèse personne et n'est pas un risque Merchant Center —
c'est l'inverse qui l'est. Je ne renverse pas cette décision sur une plaque qui contredit
l'attribut de commande. **La commande test tranchera.**

---

## Contrôle

Lignes `Source` lues sur les pages publiques après écriture :

```
805304  douille E27, ampoule LED 4 W fournie, remplaçable jusqu'à 60 W
952116  douille E27, ampoule LED 4 W fournie, remplaçable jusqu'à 60 W
121862  douille E27, ampoule LED 4 W fournie, remplaçable jusqu'à 60 W
832012  3 ampoules LED fournies, une par goutte
934110  douille G9, ampoule LED fournie et remplaçable
147607  LED intégrée et fournie, blanc chaud 3000 K
623305  douille E27 ; ampoule LED fournie ou non selon la variante
```

51 produits publiés, 158 variantes, SKU DSers intacts.
