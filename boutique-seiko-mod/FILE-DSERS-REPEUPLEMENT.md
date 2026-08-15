# Maison Noirmont — file d'import DSers, repeuplement des collections sous-peuplées

**Établie le 15/08/2026** par sourcing API AliExpress. Registre complet, preuves et refus :
[`journal/2026-08-15-sourcing-repeuplement.md`](journal/2026-08-15-sourcing-repeuplement.md).

> ⛔ **Rien n'a été importé.** Ce document est une **file ordonnée prête à importer**, pas un compte rendu
> d'import. Aucun produit Shopify n'a été créé ni modifié, rien n'a été poussé dans DSers, aucune commande
> n'a été passée.
>
> ⛔ **Case « Set product status as Draft » de DSers** : elle se réarme à chaque lot malgré le cache.
> **Relire le DOM avant chaque validation** — sinon des fiches arrivent actives avec les photos brutes.
>
> ⛔ **Aucun `compareAtPrice`.** Les 931 prix barrés purgés le 08/08 ne se réintroduisent pas.
>
> ⛔ **Aucune fiche ne peut être activée tant qu'elle porte des photos AliExpress brutes** (`REGLES.md`).

---

## Ordre d'import, et pourquoi

L'ordre suit la **valeur du trou comblé × la solidité du dossier**, pas la priorité annoncée du brief :

1. **Coffrets d'abord** — trou n°1 (19 803 recherches par fiche existante), marges 51 à 75 %, délais
   7-14 jours, dossiers sans réserve. **Rien n'attend une décision.**
2. **Style plongeuse ensuite** — dossiers propres, cadrans stériles revendiqués par le fournisseur,
   marges 48 à 54 %.
3. **Squelette en dernier** — la plus grosse valeur SEO (17 120 recherches), mais **le lot 1 attend un
   arbitrage de prix — **tranché le 15/08 : 289 €**, marge 41,8 % (voir §8.1 du journal).

---

## Lot 1 — Coffrets et rangement · 7 fiches · collection `boite-a-montre` **(à créer)**

| # | URL AliExpress | Variante à sélectionner | Handle proposé | Prix | Coût rendu | Marge HT |
|---:|---|---|---|---:|---:|---:|
| 1 | `https://www.aliexpress.com/item/1005006704546094.html` | `12 Slots` — SKU `12000038055926449` | `coffret-douze-montres-aluminium-verre` | **89 €** | 17,28 € | 55,39 € (74,7 %) |
| 2 | `https://www.aliexpress.com/item/1005008635238967.html` | `Black 12 Grids` — SKU `12000046041901234` | `coffret-douze-montres-bois-laque-noir` | **129 €** | 40,78 € | 64,66 € (60,2 %) |
| 3 | `https://www.aliexpress.com/item/1005008635238967.html` | `Red 12 Grids` — SKU `12000046041901231` | `coffret-douze-montres-bois-laque-acajou` | **129 €** | 40,18 € | 65,26 € (60,7 %) |
| 4 | `https://www.aliexpress.com/item/1005008635238967.html` | `Red 10 Grids` — SKU `12000046041901230` | `coffret-dix-montres-bois-laque-acajou` | **109 €** | 36,38 € | 52,68 € (58,0 %) |
| 5 | `https://www.aliexpress.com/item/1005006704546094.html` | `24 Slots` — SKU `12000038055926447` ⚠️ stock 12 | `coffret-vingt-quatre-montres-aluminium-verre` | **149 €** | 32,98 € | 88,85 € (71,6 %) |
| 6 | `https://www.aliexpress.com/item/1005007696086141.html` | `15 Slots` — SKU `12000041930507635` | `malette-quinze-montres-etanche` | **139 €** | 38,58 € | 75,06 € (64,8 %) |
| 7 | `https://www.aliexpress.com/item/1005008635238967.html` | `Red 6 Grids` — SKU `12000046041901227` ⚠️ **stock 4** | `coffret-six-montres-bois-laque-acajou` | **79 €** | 30,58 € | 33,90 € (51,5 %) |

**Tous ≥ 79 €** : au-dessus du verrou Shopping SONGMICS (19-48 €), comme l'exige `NOTES-PRICING.md`.
Ratio prix ÷ CPC (0,38 €) : **208 à 392**, tous très au-dessus du seuil de 100.
Comparable : **Royaume de la Boîte, 55-99 €**.

---

## Lot 2 — Porte-montres · 1 fiche · collection `porte-montre` **(à créer)**

| # | URL AliExpress | Variante | Handle proposé | Prix | Coût rendu | Marge HT |
|---:|---|---|---|---:|---:|---:|
| 8 | `https://www.aliexpress.com/item/1005008659224282.html` | `A` — SKU `12000046130802653` | `porte-montre-bois-massif-cuir` | **39,90 €** | 6,58 € | 25,86 € (77,8 %) |

⚠️ La variante `B` est à **stock 0** : ne pas l'importer. ⛔ **Cible du brief non atteinte (1 sur 3-4)** —
voir §5.2 du journal, le trou se comble par le nom du magasin, pas par la description.

---

## Lot 3 — Style plongeuse · 6 fiches · collection existante

| # | URL AliExpress | Variante à sélectionner | Handle proposé | Prix | Coût rendu | Marge HT |
|---:|---|---|---|---:|---:|---:|
| 9 | `https://www.aliexpress.com/item/1005010218960866.html` | `black sterile dial 1` + `Miyota8215 movement` — SKU `12000051567315422` | `montre-style-plongeuse-36-cadran-noir` | **239 €** | 87,68 € | 107,89 € (54,2 %) |
| 10 | `https://www.aliexpress.com/item/1005010218960866.html` | `green sterile dial` + `Miyota8215 movement` — SKU `12000051567315428` | `montre-style-plongeuse-36-cadran-vert` | **239 €** | 87,68 € | 107,89 € (54,2 %) |
| 11 | `https://www.aliexpress.com/item/1005010218960866.html` | `red sterile dial` + `Miyota8215 movement` | `montre-style-plongeuse-36-cadran-bordeaux` | **239 €** | 87,68 € | 107,89 € (54,2 %) |
| 12 | `https://www.aliexpress.com/item/1005010218960866.html` | `blue sterile dial` + `Miyota8215 movement` | `montre-style-plongeuse-36-cadran-bleu` | **239 €** | 90,68 € | 104,89 € (52,7 %) |
| 13 | `https://www.aliexpress.com/item/1005009674157775.html` | `black sterile` + `Miyota 8215` — SKU `12000058520460496` ⚠️ délai 22 j | `montre-style-plongeuse-42-titane-noir` | **279 €** | 116,48 € | 111,86 € (48,1 %) |
| 14 | `https://www.aliexpress.com/item/1005009674157775.html` | `blue sterile` + `Miyota 8215` ⚠️ **SKU à choisir à la main** | `montre-style-plongeuse-42-titane-bleu` | **279 €** | 116,48 € | 111,86 € (48,1 %) |

⛔ **Interdit d'écriture sur tout ce lot : « montre de plongée ».** On écrit **« style plongeuse »**.
⚠️ Fiche 14 : `exact` a refusé la qualification, **deux SKU correspondent** (`blue sterile` et
`black-blue sterile`). Sélectionner le bon dans DSers, à l'œil, sur l'image de variante.

---

## Lot 4 — Montres squelette · 8 fiches · collection `montre-squelette` (existante, non publiée)

### 4a — Squelette de catalogue ✅ **prix arbitré par Hakim le 15/08 : 289 €**

| # | URL AliExpress | Variante à sélectionner | Handle proposé | Prix | Coût rendu | Marge HT |
|---:|---|---|---|---:|---:|---:|
| 15 | `https://www.aliexpress.com/item/1005006771109294.html` | `black chapter ring A` + `glass back` — SKU `12000038242398895` | `montre-squelette-automatique-40-anneau-noir` | **289 €** | 135,78 € | 100,75 € (41,8 %) |
| 16 | idem | `blue hand A` + `glass back` | `montre-squelette-automatique-40-aiguilles-bleues` | **289 €** | 135,78 € | 100,75 € (41,8 %) |
| 17 | idem | `red hand A` + `glass back` | `montre-squelette-automatique-40-aiguilles-rouges` | **289 €** | 135,78 € | 100,75 € (41,8 %) |
| 18 | idem | `Green Chapter Ring A` + `glass back` | `montre-squelette-automatique-40-anneau-vert` | **289 €** | 135,78 € | 100,75 € (41,8 %) |
| 19 | idem | `blue ring A` + `glass back` | `montre-squelette-automatique-40-lunette-bleue` | **289 €** | 135,78 € | 100,75 € (41,8 %) |
| 20 | idem | `white ring A` + `glass back` | `montre-squelette-automatique-40-anneau-blanc` | **289 €** | 135,78 € | 100,75 € (41,8 %) |

⚠️ **Fret 5,79 €, délai 10-22 jours** (25 août → 6 septembre) — **hors promesse J+21**.
⚠️ **`904L` imprimé en rouge sur le bracelet** : le cadran est nu, la source est valide, mais **aucun
visuel livré ne doit montrer cette inscription** et le mot ne doit apparaître nulle part.
⚠️ **Ne jamais employer de nom de modèle** dans le titre, le `alt` ou la description : les inserts de
lunette bicolores sont un hommage, pas une référence à citer.

### 4b — Squelette d'entrée de gamme

| # | URL AliExpress | Variante | Handle proposé | Prix | Coût rendu | Marge HT |
|---:|---|---|---|---:|---:|---:|
| 21 | `https://www.aliexpress.com/item/1005010362031259.html` | `1009-1` — SKU `12000052136800818` | `montre-squelette-automatique-pont-cuir` | **189 €** | 35,19 € | 119,41 € (75,8 %) |
| 22 | `https://www.aliexpress.com/item/1005010362031259.html` | `1009-2` — SKU `12000052136800819` | `montre-squelette-automatique-pont-cuir-noir` | **189 €** | 35,19 € | 119,41 € (75,8 %) |

⚠️ **Le fournisseur ne précise ni le mouvement, ni le verre, ni l'étanchéité.** Règle « aucune
spécification inventée » : **ne rien écrire là-dessus**, ni dans le titre, ni dans la fiche.

---

## Réserves — non versées à la file, à trancher

| Article | Pourquoi c'est en réserve |
|---|---|
| `1005006991847700` — squelette 42 mm, **20 coloris**, 344 ventes, note 4,7, **24,59-27,39 €** | Cadran nu et propre, marge **83,5 % à 199 €**. ⛔ **Alliage de zinc** : incohérent avec un catalogue en acier 316L. Ouvre une entrée de gamme, ou casse la promesse |
| `1005006994737069` — Tandorio 36 mm **field/pilote stérile**, saphir, 20 bar, 362 ventes, note 4,9, **75,39 €** (`silver sterile dial`, stock 91) | **Le seul article du sourcing qui tienne les cinq critères à la fois** : ≥ 10 ventes, cadran nu, saphir, 20 bar, coût rendu < 80 €. Hors cible du ticket — à rattacher à `Classiques` si Hakim ouvre |
| `1005006389834729` — Mod 013, 37 mm NH36 200 m, variantes `nologo`, 13 ventes, note 5,0, 110,99 € | Marge 40,0 % à 279 €, fret 5,79 € et délai 22 j, doublonne le 36 mm du lot 3 |

---

## Contrôles à passer avant d'activer une seule de ces fiches

1. **Photos maison** — chaque fiche doit porter des visuels composés depuis la photo fournisseur
   (`sources-fournisseur-2026-08/<handle>/`). **Une fiche qui porte encore des photos AliExpress brutes
   ne peut pas être activée.**
2. **Filigranes** — `Tandorio` et `BL Watches Parts` sont incrustés sur plusieurs sources : ils ne
   doivent jamais passer dans une composition.
3. **`904L`** — banni de tout livrable (lot 4a).
4. **Textes** — persona avant copywriting, aucune spécification inventée, aucun avis ni chiffre de
   satisfaction (la boutique est à 0 commande client), aucune promesse de délai contredisant les
   fenêtres relevées ici.
5. **Ratio prix ÷ CPC ≥ 100** — vérifié sur les 22 fiches : coffrets 208-392, porte-montre 111,
   montres très au-dessus du seuil.
6. **Collections** — `boite-a-montre` et `porte-montre` **n'existent pas encore**. Leur création et leur
   publication sont des décisions de Hakim.
