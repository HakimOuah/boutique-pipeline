# Re-sourcing cadrans arabes orientaux — API officielle — 09/08/2026

## Statut

**PARTIEL — 1 nouvelle fiche fournisseur qualifiée sur les 4 à 8 recherchées.**

Hakim a demandé d'utiliser le MCP connecté pour Shopify et l'API pour AliExpress. Cette passe a donc utilisé :

- le MCP Shopify, en lecture seule, sur **Maison Noirmont** ;
- l'AliExpress Open Platform / AE-Dropshipper, via la passerelle VPS autorisée et limitée à la lecture ;
- les images de variantes renvoyées par l'API pour la QA visuelle.

Aucun import DSers, aucune création ou modification Shopify, aucune commande et aucun paiement n'ont été effectués.

## État réel vérifié

Contrôle Shopify du 09/08/2026 :

- 199 produits au total ;
- 96 actifs ;
- 103 brouillons ;
- 0 archivé.

La passe de cohérence existante laisse **5 fiches réellement arabes** dans la collection cible : 4 cadrans pièces et 1 montre finie. Le candidat ci-dessous n'existe pas encore dans Shopify.

## Candidat qualifié par l'API officielle

| Champ | Preuve observée |
|---|---|
| Fiche | [1005009751528666](https://fr.aliexpress.com/item/1005009751528666.html) |
| Handle proposé | `cadran-arabe-oriental-soleille-28-5` |
| Produit fournisseur | Cadran arabe soleillé 28,5 mm, avec variantes cadran seul et ensembles cadran + aiguilles |
| Compatibilité déclarée | NH35, NH36 et famille 4R — information observée dans le titre fournisseur, non testée physiquement |
| Ventes / note / évaluations | **200 ventes · 4,6/5 · 56 évaluations** |
| Vendeur | XinXin Watch Parts Store — article décrit 4,8 · communication 4,8 · expédition 4,9 |
| Variantes retenues | **11 variantes cadran seul**, chacune résolue vers un SKU numérique unique |
| Prix exact des cadrans | **5,49 à 5,69 EUR TTC** |
| Fret France | **1,99 EUR**, suivi, expédié de Chine |
| Coût livré observé | **7,48 à 7,68 EUR** selon la variante |
| Délai API | 10 à 13 jours pour 10 variantes ; 5 à 12 jours pour le bleu ciel |
| Stock exact | 3 à 499 unités selon variante ; **bleu ciel fragile à 3 unités** |
| Source | AliExpress Open Platform / AE-Dropshipper via VPS à IP autorisée |
| Relevé | 09/08/2026, entre 21:52:16 et 21:52:20 UTC |

### QA visuelle des variantes

Les 11 images de variantes cadran seul montrent :

- des chiffres arabo-indiens orientaux visibles, notamment `٣`, `٦`, `٩` et `١٢` ;
- aucun logo, sigle, nom de marque ni formule déposée imprimé sur le cadran physique ;
- un filigrane **« XinXin Store »** superposé à la photo fournisseur, et non imprimé sur le produit ;
- un guichet de date à 3 h sur chacune des 11 variantes cadran seul retenues ; le mapping doit malgré tout rester image par image et SKU par SKU.

Le filigrane rend les photos brutes impropres à la publication. Elles peuvent servir de sources de composition, conformément au protocole Maison Noirmont, mais ne doivent jamais être placées telles quelles dans une galerie Shopify.

Preuves locales :

- planche versionnée : `preuves-sourcing-api-2026-08-09/1005009751528666-variantes-cadran.jpg` ;
- relevé machine : `preuves-sourcing-api-2026-08-09/1005009751528666.json` ;
- sources ignorées par Git : `sources-fournisseur-2026-08/cadran-arabe-oriental-soleille-28-5/`.

### Lecture commerciale

Cette fiche apporte **un produit supplémentaire**, pas onze produits : les coloris sont des variantes d'une même page fournisseur. Après un éventuel import, la collection passerait donc de 5 à **6 produits réels**, encore sous la cible de 9 à 13 résultant du besoin de 4 à 8 ajouts.

Le design est proche du `cadran-arabe-oriental-sunburst-29` déjà présent, mais la cote 28,5 mm et le choix de onze finitions créent une différence produit réelle. Le titre et le contenu SEO devront éviter de cannibaliser la fiche 29 mm.

## Refus motivés

| Item ID | Décision | Motif observé |
|---|---|---|
| `1005012132349173` | REFUS | 6 ventes, sous le plancher ; titre et image annoncent en plus un logo S. |
| `1005012072864621` | REFUS | 7 ventes, sous le plancher ; logo S annoncé. |
| `1005010135248171` | REFUS | 11 ventes mais logo S annoncé sur le cadran. |
| `1005009469054356` | REFUS | 205 ventes, mais toutes les variantes API sont `S Dial` ; les images déjà documentées portent aussi une formule de type Rolex. |
| `1005007138348184` | REFUS | 1 vente ; produit fini à logo personnalisé, pas une pièce qualifiable pour la collection. |
| `1005009954277951` | REFUS | Faux positif de recherche : 54 variantes de cadrans plongeuse/jeux d'aiguilles, aucun chiffre oriental sur la planche API ; plusieurs cadrans portent des formules de type Rolex. |
| `1005008379676708` | REFUS | Faux positif : 29 cadrans plongeuse à index, aucun chiffre oriental ; texte imprimé sur plusieurs faces. |
| `1005008875165003` | REFUS | Faux positif : 38 visuels uniques de cadrans plongeuse/jeux d'aiguilles, aucun chiffre oriental ; textes imprimés sur les cadrans. |

## Couverture de recherche et limite constatée

Les formulations testées incluent notamment `arabic dial no logo`, `arabic dial NH35 28.5`, `eastern arabic numeral dial NH35`, `arabic numbers dial 28.5mm`, `sky blue arabic dial NH35`, les recherches par couleur, ainsi que les glyphes `٣ ٦ ٩ ١٢`.

Le tri AliExpress par ventes remonte massivement des mouvements, boîtiers, aiguilles et montres à chiffres occidentaux. Une requête triée par nouveautés a aussi renvoyé une erreur amont `EXCEPTION_TEXT_SEARCH_FOR_DS`. La couverture est donc sérieuse mais ne justifie pas d'inventer les 3 à 7 fiches manquantes.

## Suite sûre

1. Conserver la ligne qualifiée dans `FILE-DSERS-CADRAN-ARABE.md`, sans l'importer tant que Hakim n'a pas donné son accord.
2. Continuer la recherche API sur de nouvelles fiches et vendeurs alternatifs ; garder le seuil de 10 ventes et la QA image stricte.
3. Au moment d'un éventuel import, recontrôler stock, prix et fret de chaque SKU retenu, puis pousser uniquement en DRAFT.
4. Produire les visuels maison avant toute activation ; ne jamais publier les images fournisseur filigranées.
