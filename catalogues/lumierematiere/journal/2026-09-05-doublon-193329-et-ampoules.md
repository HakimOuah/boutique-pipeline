# 05/09/2026 — Doublon travertin arbitré, question de l'ampoule tranchée

Instruction de Hakim : « Pour le doublon, supprimes-en un. Et c'est quoi le souci de l'ampoule ? »
Plus une capture du réglage de devise et le numéro de téléphone.

---

## 1. Doublon `193329` / `338324` — `338324` archivée

Les deux fiches vendent la même grille : cylindre travertin, **deux formes × deux bois**,
à **199 €** toutes les deux, dans `selection-199` toutes les deux.

| | `193329` gardée | `338324` archivée |
|---|---|---|
| Variantes | 4 | 12 (2 formes × 2 bois × 3 températures) |
| Stock total | 51 | 22 |
| Variantes en stock | **4 / 4** | **4 / 12** |
| Source | douille E27, ampoule non fournie | LED intégrée, 3 températures |
| Historique | — | grille `A/B/C/D` qui ne recouvrait pas la grille fournisseur (revue du 04/09) |

`338324` offre mieux sur le papier — LED intégrée, choix de température — mais **huit
combinaisons sur douze sont à zéro** : le sélecteur est mort aux deux tiers. `193329` est
complète et lisible. C'est elle qui reste.

**Archivée, pas détruite.** `status: ARCHIVED` sort la fiche de la boutique, du sitemap et
du futur flux (contrôlé : `/products/suspension-effet-pierre-led-338324` répond **404**,
`products.json` passe de 52 à **51**), tout en gardant SKU DSers, médias et rattachements
si la décision devait s'inverser. Une suppression définitive reste possible sur ta parole.

**Effet de bord réparé dans le même passage** : `338324` était l'une des 4 fiches publiques de
`suspensions-pierre`. `193329` — un travertin, rangé jusqu'ici en `suspensions-bois` seulement —
y a été ajoutée. La collection **reste à 4 en vue visiteur** (comptée sur `products.json`,
pas sur l'admin).

---

## 2. `147607` — l'ampoule : la fiche mentait, quatre fois

Question ouverte depuis le 04/09 (`O-1`) : le SKU porte `136:200003939#Warm light 3000K`
(source fournie) et le corps de fiche disait « il vous faudra une ampoule E27 ».

**Tranché par les plaques fournisseur**, `sources-fournisseur/1005009207147607/` :

- `03.jpg` cote le bloc rectangulaire à **6,5 × 6,5 × H 16 cm**, avec un émetteur rond
  encastré d'environ 2 cm au culot. Une douille E27 fait ~4 cm de diamètre et demande une
  ampoule de ~6 cm : **elle ne rentre pas** dans un bloc de 6,5 cm de côté.
- `06.jpg` montre le faisceau : un cône serré de spot encastré, pas la nappe diffuse d'un globe E27.
- Le même fournisseur écrit explicitement `No Bulb(E27)` quand il le pense (`607504`).
  Ici il écrit `Warm light 3000K`, et **n'offre aucune alternative sans ampoule**.

Conclusion : **LED intégrée, blanc chaud 3000 K, fournie.** La fiche envoyait le client
acheter une ampoule inutile, sur quatre surfaces : description, `usps`, `specs` (« Source :
douille E27, ampoule non fournie »), `installation` (« Vissez l'ampoule E27 après la pose »)
et la FAQ (« L'ampoule est-elle fournie ? Non »).

**Corrigé sur les cinq.** Contrôle : `0` occurrence de « E27 » sur la page live,
« LED intégrée et fournie, blanc chaud 3000 K » présente. Le titre reste
« Suspension travertin cuisine, monture noyer » — vrai, et plus discriminant qu'un `LED`.

**O-1 est close.**

---

## 3. La même erreur ailleurs : balayage des 51 fiches

Croisement systématique « ce que le SKU fournisseur dit de la source » × « ce que le bloc
`specs` annonce ». Une deuxième contradiction prouvable sans image :

### `623305` — corrigée

Neuf variantes : `5:100014066#Cold white`, `5:100014065#Warm white`, `5:100014064#No Bulb`.
**Six variantes sur neuf sont livrées avec leur ampoule.** Les libellés le disaient déjà
(« Avec ampoule LED · blanc chaud 3000 K »), mais la description, les `usps`, la ligne
`Source`, l'`installation` et la FAQ disaient tous « ampoule non fournie », sans nuance.
Passées au modèle de `435189` : « douille E27 ; ampoule LED fournie ou non selon la variante ».

### Restent suspectes, non touchées faute de preuve

| Fiche | Le SKU dit | La fiche dit |
|---|---|---|
| `934110` | `5:361385#3000K warm light` + variantes 3000 K / 6000 K | « douille G9, ampoule non fournie » |
| `805304`, `952116`, `121862` | `249:200006305#4W(Max 60W)` | « LED intégrée » — or « Max 60 W » se lit comme une **douille**, avec une LED 4 W fournie |
| `832012` | les 3 variantes partagent `136:200006153#3 Lights bulb` | « LED intégrée **ou** douille E27 selon la variante » — l'axe n'a qu'une valeur |
| `829449` | `40-10-17CM warm LED` | « douille G9, ampoule non fournie » (aucune source fournisseur en local) |

Ce sont des lectures d'étiquette, pas des preuves. Elles demandent la plaque fournisseur ou
la PDP. `934110` était déjà en attente de confirmation fournisseur depuis le 04/09.

---

## 4. Devise et téléphone

**Devise** — le réglage est passé de `€{{amount_with_comma_separator}}` à
`{{amount_with_comma_separator}}€` sur les quatre champs. Le symbole est du bon côté ;
il manque **l'espace insécable** que veut la typographie française : `199,00 €`, pas `199,00€`.

**Téléphone** — le site affiche partout `+33 7 56 91 60 84` / `tel:+33756916084`, et le
JSON-LD sort `0756916084` depuis le champ Téléphone des réglages. Hakim donne
`+33 7 56 82 80 94`. **Cela renverse la décision du 31/08** (`nox/evenements/2026-08-31-…`),
où il avait montré l'écran Réglages et dit que le numéro y était le bon. Rien touché en
attendant confirmation : basculer 8 surfaces publiques vers un numéro qui ne décroche pas
serait pire que l'écart actuel.

---

## Contrôle final

- **51 produits publiés** (52 − 1 archivé), 158 variantes, **SKU DSers intacts**.
- `suspensions-pierre` : **4 fiches en vue visiteur**, inchangé.
- `147607` : 0 mention E27, source déclarée intégrée.
- `623305` : source déclarée « selon la variante ».
