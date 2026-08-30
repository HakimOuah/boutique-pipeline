---
type: journal
boutique: seiko-mod
date: 2026-08-10
nature: analyse
leviers: [catalogue]
titre: "Décision — cinq dossiers « cadran arabe » bloqués — 10/08/2026"
---

# Décision — cinq dossiers « cadran arabe » bloqués — 10/08/2026

## Verdict

**Aucune des cinq entrées ne doit être ajoutée à Shopify ou rouverte dans DSers.**

- **Quatre abandons nets** : deux cadrans portent un verbatim associé à Rolex, un troisième est vendu uniquement en `S Dial` et porte le même type de verbatim, et une montre n'a que des chiffres occidentaux `1-12`.
- **Un produit est sauvé visuellement mais pas commercialement** : `1005006492769759` possède de vraies variantes `sterile`, à chiffres arabes orientaux et sans marque au cadran. Il n'a toutefois plus que **4 ventes**, et la même famille existe déjà en brouillon Shopify sous `1005010249362754`. Ajouter le listing NH35 créerait un doublon faible.

Aucune modification Shopify ou DSers, aucun achat et aucun message fournisseur n'ont été effectués.

## Correction de périmètre

L'expression « cinq fiches bloquées » de la passation ne désigne pas cinq produits Shopify. Le journal `2026-08-09-fournee-visuels-nouveaux.md` établit qu'il y avait **99 dossiers source pour 94 fiches importées** ; les cinq dossiers excédentaires sont précisément les deux refus du push, le candidat conditionnel jamais mis en file et deux cadrans non importés.

Recherche Shopify MCP du 10/08/2026, par handle exact : **0 résultat pour les cinq handles**. Ils n'ont donc ni Shopify ID, ni statut, ni publication à nettoyer.

| Handle local | Item ID AliExpress | Shopify ID | Source locale existante |
|---|---:|---|---|
| `cadran-arabe-oriental-rose-28-5` | `1005007922653909` | absent de Shopify | `sources-fournisseur-2026-08/cadran-arabe-oriental-rose-28-5/face-fournisseur-1005007922653909.jpg` |
| `cadran-arabe-oriental-sunburst-relief-28-5` | `1005010654686163` | absent de Shopify | `sources-fournisseur-2026-08/cadran-arabe-oriental-sunburst-relief-28-5/face-fournisseur-1005010654686163.jpg` |
| `cadran-nh35-chiffres-arabes-orientaux-28-5` | `1005009469054356` | absent de Shopify | `sources-fournisseur-2026-08/cadran-nh35-chiffres-arabes-orientaux-28-5/face-fournisseur-1005009469054356.jpg` |
| `montre-cadran-arabe-oriental-nh35` | `1005006492769759` | absent de Shopify | `sources-fournisseur-2026-08/montre-cadran-arabe-oriental-nh35/face-fournisseur-1005006492769759.jpg` |
| `montre-field-titane-39-chiffres-arabes` | `1005012493670989` | absent de Shopify | `sources-fournisseur-2026-08/montre-field-titane-39-chiffres-arabes/face-fournisseur-1005012493670989.png` |

## Méthode et niveau de preuve

- AliExpress : passerelle officielle Open Platform / AE-Dropshipper, lecture seule, santé `ok`.
- Relevés produit et variantes : entre `2026-08-09T22:06:29Z` et `2026-08-09T22:10:06Z`, soit le 10/08 entre 00:06 et 00:10 à Paris.
- QA : inspection visuelle des **62 images de variantes uniques** renvoyées par l'API pour les cinq item IDs.
- Recherche d'alternatives : requêtes par dimensions, calibre, famille de cadran, Tandorio, `sterile`, `Arabic`, `Eastern Arabic`, `Urdu` et glyphes orientaux ; tris `orders`, `latest` et `price_desc`.
- Limite : l'action `variants` expose les images de SKU, pas nécessairement chaque photo longue de la galerie. Plusieurs recherches ciblées en tri `latest` ont échoué avec `EXCEPTION_TEXT_SEARCH_FOR_DS`. La conclusion exacte est donc : **aucune alternative propre et fiable trouvée dans la surface officielle disponible**, pas « aucune alternative n'existe au monde ».

## Décisions fiche par fiche

### 1. `cadran-arabe-oriental-rose-28-5` — abandon

- **Item** : [1005007922653909](https://fr.aliexpress.com/item/1005007922653909.html)
- **Données actuelles API** : 7 ventes, note 4,3/5, 6 évaluations ; `Shop1104206650 Store`, note « conforme à la description » 4,5/5.
- **Chiffres** : oui, les cadrans montrent bien les glyphes orientaux, notamment `٣`, `٦`, `٩`, `١٢`.
- **Marque/verbatim** : échec. Les **12 variantes de cadran** visibles portent `SUPERLATIVE CHRONOMETER / OFFICIALLY CERTIFIED`. La treizième image propre n'est pas un cadran : c'est uniquement un jeu d'aiguilles à 4,59 EUR.
- **Autre photo/vendeur** : aucune variante de cadran muette dans la fiche ; aucun jumeau pertinent et propre trouvé par l'API.
- **Décision** : **ABANDON**. Ne pas prendre la photo des aiguilles pour une variante stérile et ne jamais effacer le verbatim du produit.

### 2. `cadran-arabe-oriental-sunburst-relief-28-5` — abandon

- **Item** : [1005010654686163](https://fr.aliexpress.com/item/1005010654686163.html)
- **Données actuelles API** : 13 ventes, note 5,0/5, 3 évaluations ; `NH35 Watch Parts Store`, notes vendeur 4,7/5.
- **Chiffres** : échec. Malgré le titre fournisseur « Arabic », les trois images montrent respectivement des chiffres **occidentaux 1-12**, des index bâtons et des index bâtons. Aucun `٣ ٦ ٩ ١٢`.
- **Marque/verbatim** : échec. Les trois cadrans portent `SUPERLATIVE CHRONOMETER / OFFICIALLY CERTIFIED`; les variantes affichent en plus `JAPAN MOV'T`. Le libellé `NO LOGO` ne rend pas le produit stérile.
- **Autre photo/vendeur** : trois SKU sur trois contrôlés ; aucun jumeau oriental propre trouvé.
- **Décision** : **ABANDON** de la collection arabe et abandon produit Maison Noirmont à cause du verbatim. Ce produit ne doit pas être simplement renommé.

### 3. `cadran-nh35-chiffres-arabes-orientaux-28-5` — abandon

- **Item** : [1005009469054356](https://fr.aliexpress.com/item/1005009469054356.html)
- **Données actuelles API** : 205 ventes, note 4,9/5, 35 évaluations ; `Shop1104389318 Store`, notes vendeur 4,7 à 4,8/5.
- **Chiffres** : certaines variantes montrent bien des chiffres arabes orientaux.
- **Marque/verbatim** : échec bloquant. Les **15 SKU sont explicitement `S Dial`**. Les variantes orientales visibles portent aussi le texte tronqué `RLATIVE CHRONO / OFFICIALLY CERTIFIED`, cohérent avec le signalement local de type Rolex.
- **Autre photo/vendeur** : aucune variante `NO LOGO` ou `sterile` dans l'API ; aucune offre jumelle propre identifiée.
- **Décision** : **ABANDON**. La traction élevée ne compense ni `S Dial` ni le verbatim de certification.

### 4. `montre-cadran-arabe-oriental-nh35` — débloquée visuellement, abandon commercial du candidat

- **Item** : [1005006492769759](https://fr.aliexpress.com/item/1005006492769759.html)
- **Données actuelles API** : **4 ventes** et 1 évaluation, note 5,0/5 ; vendeur `tandorio Timepieces Store`, notes 4,8/5. Le dossier du 09/08 indiquait 8 ventes : la réponse actuelle de l'API est plus basse et doit primer pour cette décision.
- **Chiffres** : oui. Les variantes `blue/green/white/black sterile` montrent bien les glyphes orientaux `٣ ٦ ٩ ١٢`.
- **Marque/verbatim** : les variantes sans suffixe portent logo et nom Tandorio ; les variantes `sterile` n'en portent aucun. Le seul mot restant est `Automatic`, descriptif générique et non verbatim de marque. Les photos fournisseur restent brutes et ne sont pas publiables telles quelles.
- **Preuve SKU exacte** : `black sterile` + `39mm-glass back`, SKU `12000037405238308`, stock 494, 112,39 EUR, fret France 5,79 EUR, délai API 10-15 jours. Image exacte : [variante stérile noire](https://ae01.alicdn.com/kf/S046fc20acffe4e888cf9b7e43cd9e940S.jpg).
- **Jumeaux retrouvés** :
  - `1005006492848846`, même vendeur et mêmes images stériles, mais **0 vente / 0 avis** ; SKU noir stérile 39 mm vérifié à 120,39 EUR + 1,99 EUR de fret, stock 99.
  - `1005010249362754`, même vendeur et mêmes images stériles, mouvement Miyota 8215 ; **8 ventes / 3 avis** actuellement. Ce jumeau existe déjà dans Shopify en **DRAFT**, ID `11013081366866`, handle `montre-cadran-arabe-oriental-36-39`.
- **Risque sur le brouillon existant** : Shopify expose 40 variantes mêlant `blue` et `blue sterile`, donc logotées et stériles. Sa photo principale brute porte Tandorio. Il ne doit pas être activé sans élagage strict aux variantes stériles et remplacement des visuels.
- **Décision** : la preuve visuelle de variante propre est **ACQUISE**, mais **ABANDONNER CE NOUVEAU CANDIDAT NH35** : 4 ventes, 1 avis et doublon d'une fiche déjà en brouillon. Conserver le brouillon 8215 comme dossier séparé à arbitrer, pas comme produit validé.

### 5. `montre-field-titane-39-chiffres-arabes` — abandon de la collection arabe

- **Item** : [1005012493670989](https://fr.aliexpress.com/item/1005012493670989.html)
- **Données actuelles API** : 3 ventes, note 5,0/5, 1 évaluation ; `watchery Store`, notes vendeur 4,8/5.
- **Chiffres** : échec total pour la grappe visée. Les **21 images de variantes uniques** montrent exclusivement les chiffres occidentaux `1-12`, des cadrans pilote ou des index. Aucun chiffre arabe oriental.
- **Marque/verbatim** : les variantes `logo` portent Tandorio. Les variantes `sterile` retirent le logo mais conservent, selon le cadran, des mentions génériques de profondeur et `Automatic`; cela ne corrige pas l'absence de glyphes orientaux.
- **Autre vendeur** : `1005010214933750` propose des variantes `sterile` de la même famille titane 39 mm, mais n'a qu'1 vente / 0 avis et porte toujours des chiffres occidentaux. Les autres familles Tandorio déjà documentées (`1005005323678492`, `1005010107913039`) sont également occidentales.
- **Décision** : **ABANDON** de la collection `cadran-arabe`. Ne pas utiliser ce produit pour servir `seiko arabic dial` au sens oriental ; sa preuve sociale est en outre insuffisante.

## Conséquence opérationnelle

| Entrée | Décision finale | Action autorisée maintenant |
|---|---|---|
| `1005007922653909` | abandon | aucune |
| `1005010654686163` | abandon | aucune |
| `1005009469054356` | abandon | aucune |
| `1005006492769759` | variante propre prouvée, candidat à abandonner | aucune création ; ne pas dupliquer le brouillon 8215 |
| `1005012493670989` | abandon de la grappe arabe | aucune |

**Bilan : 0 nouvelle fiche récupérable sur 5 pour le catalogue.** Les quatre dossiers locaux clairement abandonnés peuvent être traités comme preuves historiques ; leur suppression physique n'est pas autorisée par cette mission. Le brouillon Shopify `11013081366866` reste bloqué et doit être arbitré dans le nettoyage catalogue, sans activation automatique.
