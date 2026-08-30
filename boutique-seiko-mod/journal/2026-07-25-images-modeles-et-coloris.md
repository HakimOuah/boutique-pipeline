---
type: journal
boutique: seiko-mod
date: 2026-07-25
nature: intervention
leviers: [catalogue, creative]
titre: "Modèles d'image & production des coloris — 25/07/2026"
---

# Modèles d'image & production des coloris — 25/07/2026

> Complément au `2026-07-24-runbook-pdp-variantes-images.md`, devenu non inscriptible en fin de session (lecture OK, écriture refusée au niveau système alors que le dossier reste inscriptible — à débloquer côté macOS, aucune donnée perdue).

## 1. Leçon de fond : le mauvais modèle était la cause racine

Les faux logos qui ont coûté toute une boucle de détourage venaient de **`soul_2` (Higgsfield Soul 2.0)**, utilisé pour la première fournée de 35 images. C'est un modèle d'UGC et d'éditorial mode : il fabrique du branding parce que ses références en portent. **Proscrit pour tout packshot produit.**

## 2. Comparatif de 5 modèles (26,5 crédits) — modèle retenu : `nano_banana_pro` en 4K

Tâche de test = la tâche réelle des visuels de coloris : reprendre une face produit validée (Trente-Six, cadran argenté) et n'en changer que la couleur du cadran (bleu nuit), tout le reste identique.

| Rang | Modèle | Coût | Résolution réelle | Écart hors cadran¹ | Verdict |
|---|---|---:|---:|---:|---|
| 1 | **nano_banana_pro 4K** | **4 cr** | **4096 px** | 4,18 | **RETENU** — cadrage, fond, lumière et ombre conservés |
| 2 | gpt_image_2 4K/high | 12 cr | 2880 px | 3,42 | Excellent, mais 3× le prix, son « 4K » ne rend que 2880 px, et le fond vire plus chaud |
| 3 | seedream_v5_pro | 3 cr | 2048 px | 9,70 | Bon rapport qualité/prix, mais le cadrage dérive |
| 4 | flux_kontext | 1,5 cr | 1024 px | 16,98 | Bleu hors brief, 1024 px, et **réécrit le prompt tout seul** → ingérable en série |
| 5 | openai_hazel | 6 cr | 1024 px | 20,84 | **ÉLIMINÉ** — invente un « XII » typographié et une trotteuse centrale : ce n'est plus la montre vendue |

¹ écart moyen de pixels par rapport à la référence, mesuré **hors du disque du cadran** (le cadran doit changer, rien d'autre). Plus bas = plus fidèle.

Contre-vérification faite sur `scratchpad/noirmont-bakeoff/comparatif.jpg` : le « XII » d'openai_hazel est parfaitement lisible — défaut éliminatoire confirmé de visu. Les deux premiers sont **visuellement équivalents** : le choix se joue donc sur le coût (×3) et la résolution, pas sur la qualité. L'intuition initiale sur GPT Image 2 était juste sur la qualité du modèle, fausse sur le rapport qualité/prix pour cet usage.

**Coût projeté de la série complète de 67 coloris : ~268 crédits.**

## 3. Production des coloris — lot 1 (24 visuels) lancé

Découverte qui débloque la moitié du chantier : **5 montres ont déjà leurs coloris nommés en clair** dans leurs options Shopify — aucune identification AliExpress nécessaire.

| Montre | Coloris | Nature du changement |
|---|---:|---|
| Trente-Six — jubilé | 6 | couleur de cadran (+ « Or intégral » = montre entièrement dorée) |
| Trente-Neuf — cannelée | 7 | couleur de cadran |
| Quarante-et-Un — sport acier | 7 | cadran **et** bracelet (versions acier et cuir) |
| Noirmont Un — plongeuse | 2 | matière de boîtier (acier / bronze patiné) |
| Trente-Neuf Duo — bicolore | 2 | finition dorée (or rose / or jaune) |

Sortie : `scratchpad/noirmont-coloris/` + `manifest-coloris.json` portant les **libellés d'option Shopify exacts**, pour une assignation automatique aux variantes. Budget 130 crédits, modèle imposé `nano_banana_pro` 4K.

**Restent à identifier visuellement chez AliExpress avant production** (codes fournisseur opaques) : Voyageur GMT (réf. 1-9), Noirmont Deux (1-7), Contre-la-montre (M-1…M20), Intégrale (1-7), Héritage (S1-S3) — soit 43 coloris.

## 4. Rappel de la mécanique d'assignation

`productVariantsBulkUpdate` accepte un `mediaId` par variante. On assigne l'image du coloris à **toutes** les variantes qui le partagent (les 4 variantes « Doré » de la Trente-Six pointent sur le même média). Les options techniques — diamètre, fond verre/acier, mouvement — n'ont pas besoin de visuel propre : c'est ce qui fait tomber le besoin de 214 variantes à 67 images.

⚠️ QA à faire au premier branchement : vérifier que le thème FullStack bascule bien la galerie quand la variante sélectionnée porte un média.
