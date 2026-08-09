# Re-sourcing cadrans arabes orientaux — agent API — 10/08/2026

## Verdict

**PARTIEL — 1 produit distinct supplémentaire qualifié sur les 4 à 8 demandés. MANQUANT : 3 à 7 produits distincts.**

La passe respecte les frontières fixées :

- AliExpress Open Platform / AE-Dropshipper uniquement, via le gateway VPS officiel limité à la lecture ;
- aucun navigateur AliExpress ;
- aucune action Shopify, DSers, commande, paiement ou message fournisseur ;
- refus ferme sous 10 ventes réelles ;
- contrôle visuel des images de variantes, et non confiance accordée au seul titre fournisseur ;
- les coloris d'une même fiche comptent comme des variantes, jamais comme plusieurs produits.

Le gateway était sain au lancement. La découverte a produit 128 réponses sauvegardées : 116 recherches réussies et 12 erreurs amont sur le tri `latest`. Deux recherches Unicode directes supplémentaires ont réussi. Les résultats sauvegardés couvrent 811 `item_id` distincts, dont 20 seulement avaient un titre réunissant cadran et termes arabes. Après dédoublonnage, seuil de ventes et QA image, une seule nouvelle fiche passe.

Les produits déjà présents ou déjà traités n'ont pas été recomptés : `1005007976392353`, `1005012137091344`, `1005009056835202`, `1005011774911570`, le candidat du 09/08 `1005009751528666`, ainsi que les refus déjà motivés dans `RESOURCING-CADRAN-ARABE.md`.

## Produit qualifié

| Champ | Preuve observée via l'API officielle |
|---|---|
| Item | [1005007348127532](https://fr.aliexpress.com/item/1005007348127532.html) |
| Décision | **PASS — candidat distinct, sans import** |
| Produit | Cadran rayonné sans date, 28,5 mm |
| Compatibilité déclarée | NH35 / NH36 — observée dans le titre fournisseur, non testée physiquement |
| Ventes réelles | **58** |
| Note / évaluations | **5,0/5 · 13 évaluations** |
| Vendeur | **Watch DlY Factory Store** — article décrit 4,8 · communication 4,8 · expédition 4,8 |
| Variantes | **12** finitions, chacune résolue vers un SKU numérique unique |
| Prix TTC observé | **9,19 à 9,79 EUR** |
| Fret France exact | **1,99 EUR**, AliExpress Selection Standard, suivi, expédition de Chine |
| Coût rendu observé | **11,18 à 11,78 EUR** |
| Délai API | 8 à 13 jours pour le bleu ciel ; 10 à 13 jours pour les 11 autres variantes |
| Stock exact | **916 à 989 unités** selon variante |
| Relevé | 10/08/2026 entre 00:14:46 et 00:15:11, heure de Paris |

### Les deux contrôles éliminatoires

**1. Chiffres arabes orientaux : PASS.** La planche des douze variantes et deux zooms originaux montrent les douze chiffres orientaux en applique, notamment `١٢`, `٣`, `٦` et `٩`. Il ne s'agit pas des chiffres occidentaux 1–12.

**2. Logo / verbatim de marque : PASS.** Aucun nom, logo, sigle, mention d'origine, formule de certification, ni texte commercial n'est visible sur le cadran physique des douze variantes. Aucun filigrane n'est visible sur ces sources API.

Les images restent des **sources fournisseur** : même propres, elles ne doivent pas être publiées brutes sur Shopify. Elles servent à la vérité produit et à la future composition des visuels maison.

### Qualification exacte par variante

| SKU exact | Variante fournisseur | Prix TTC | Stock | Fret FR | Coût rendu | Délai FR API | Décision |
|---|---|---:|---:|---:|---:|---|---|
| `12000040364453605` | Silver sky blue | 9,19 € | 943 | 1,99 € | 11,18 € | 8–13 j | garder |
| `12000040364453604` | Silver Pink | 9,29 € | 972 | 1,99 € | 11,28 € | 10–13 j | garder |
| `12000040364453601` | Silver White | 9,39 € | 944 | 1,99 € | 11,38 € | 10–13 j | garder |
| `12000041650709974` | Rose black | 9,39 € | 975 | 1,99 € | 11,38 € | 10–13 j | garder |
| `12000040364453600` | Silver - Deep Blue | 9,19 € | 964 | 1,99 € | 11,18 € | 10–13 j | garder |
| `12000041650709975` | Gold black | 9,29 € | 967 | 1,99 € | 11,28 € | 10–13 j | garder |
| `12000040364453603` | Silver Green | 9,29 € | 943 | 1,99 € | 11,28 € | 10–13 j | garder |
| `12000041650709972` | Rose white | 9,39 € | 984 | 1,99 € | 11,38 € | 10–13 j | garder |
| `12000040364453602` | Silver Black | 9,39 € | 916 | 1,99 € | 11,38 € | 10–13 j | garder |
| `12000041650709973` | Gold white | 9,49 € | 973 | 1,99 € | 11,48 € | 10–13 j | garder |
| `12000041650709976` | Brown | 9,29 € | 989 | 1,99 € | 11,28 € | 10–13 j | garder |
| `12000041650709977` | Golden | 9,79 € | 981 | 1,99 € | 11,78 € | 10–13 j | garder |

Cette fiche apporte **un seul produit**. Ses douze finitions ne remplissent donc pas artificiellement l'objectif de quatre à huit produits distincts.

## Nouveaux refus et quasi-candidat

| Item | Ventes / note | Contrôle image | Décision |
|---|---:|---|---|
| [1005012130205925](https://fr.aliexpress.com/item/1005012130205925.html) | **9 ventes · 0 évaluation** | Les 5 variantes montrent de vrais chiffres orientaux, sans marque ni verbatim sur le cadran. | **REFUS** — sous le seuil non négociable de 10 ventes. À recontrôler plus tard, sans import aujourd'hui. |
| [1005010278946311](https://fr.aliexpress.com/item/1005010278946311.html) | **70 ventes · 4,7/5** | Chiffres orientaux confirmés, mais l'image API montre `660ft-200m PROFESSIONAL AUTOMATIC` et la fiche/SKU annonce `S Logo`. | **REFUS** — verbatim de type marque et signal `S Logo`. |

## Manquants honnêtes

- **3 à 7 produits distincts** restent à trouver pour satisfaire la demande initiale.
- Aucun autre cadran distinct en 29 mm ou 33,5 mm n'a passé simultanément ventes, compatibilité, chiffres orientaux et absence de verbatim dans cette passe.
- Les tris `orders`, `price_asc` et `price_desc` remontent principalement mouvements, boîtiers, aiguilles, montres finies et cadrans à chiffres occidentaux. Le tri `latest` a échoué douze fois avec une erreur amont ; ce manque de couverture est conservé comme limite, pas transformé en preuve négative absolue.
- Le quasi-candidat `1005012130205925` est à une vente du seuil, mais la règle impose son refus aujourd'hui.

## Décision opérationnelle

Le seul candidat prêt pour une éventuelle file DSers ultérieure est `1005007348127532`, **uniquement en DRAFT et après accord explicite de Hakim**. Avant tout mapping futur, refaire `variants` puis `exact` pour les douze SKU, car prix, stock et fret sont temporels.

Aucune file DSers n'est créée ici : l'objectif demandé à cet agent est la preuve de sourcing, et la cible de quatre produits n'est pas atteinte.

## Preuves

- `preuves-sourcing-api-2026-08-10-agent/1005007348127532.json` — inventaire API et douze qualifications SKU/fret exactes ;
- `preuves-sourcing-api-2026-08-10-agent/1005007348127532-variantes.jpg` — planche QA des douze variantes ;
- `preuves-sourcing-api-2026-08-10-agent/1005007348127532-sources/` — douze images de variantes renvoyées par l'API ;
- `preuves-sourcing-api-2026-08-10-agent/refus-et-near-miss.json` — preuves structurées des deux décisions négatives ;
- `preuves-sourcing-api-2026-08-10-agent/1005012130205925-near-miss.jpg` — planche du quasi-candidat à 9 ventes ;
- `preuves-sourcing-api-2026-08-10-agent/1005010278946311-refus.webp` — zoom du verbatim éliminatoire.
