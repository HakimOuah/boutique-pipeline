---
type: journal
boutique: seiko-mod
date: 2026-08-10
nature: analyse
leviers: [sourcing, creative, technique]
titre: "Audit des 9 visuels de galerie actifs restants — API AliExpress"
---

# Audit des 9 visuels de galerie actifs restants — API AliExpress

Date de contrôle : 10 août 2026 (requêtes API observées le 9 août 2026 entre 22:41 et 22:46 UTC)

Périmètre : les 9 emplacements de galerie encore manquants, P0 = 8 et P2 = 1, recensés dans `2026-08-10-reconciliation-319-visuels-agent.md`.
Interdits respectés : aucun navigateur AliExpress, aucune génération d'image, aucune mutation Shopify ou DSers, aucune intervention dans la file d'ordres, aucun commit ni push.

## Verdict exécutable

| Verdict | Nombre d'emplacements |
|---|---:|
| **PRODUISIBLE** | **0** |
| **BLOQUÉ** | **7** |
| **ABANDON** | **2** |
| **Total audité** | **9** |

Aucune photo alternative ne satisfait simultanément les trois conditions obligatoires : correspondance exacte avec le produit ou ses variantes actives, absence de marque/verbatim, et preuve de provenance locale ou issue de l'API officielle AliExpress. Les sept blocages ne prouvent pas que la source n'existe plus ; ils indiquent qu'elle ne peut pas être rattachée honnêtement avec les identifiants conservés. Les deux abandons concernent uniquement les **deux ajouts de galerie** de la carte cadeau, pas la fiche ni son image actuelle.

## Décision emplacement par emplacement

| Priorité | Produit Shopify | Emplacement | Verdict | Preuve et motif |
|---|---|---:|---|---|
| P0 | `Trente-Neuf Rose — Classique cannelée` (`10978720317778`) | galerie-02 | **BLOQUÉ** | Les deux fichiers locaux trouvés montrent le même produit avec le verbatim interdit **« SWISS MADE » à 6 h**. Les recherches API par couleur, absence de logo, diamètres et mouvements ne retrouvent pas l'article exact. Aucun `product_id` AliExpress d'origine n'est conservé pour appeler `product.get`. |
| P0 | `Trente-Neuf Rose — Classique cannelée` (`10978720317778`) | galerie-03 | **BLOQUÉ** | Même source contaminée et même absence d'identifiant article exact ; aucune seconde vue propre et traçable. |
| P0 | `Trente-Neuf Rose — Classique cannelée` (`10978720317778`) | galerie-04 | **BLOQUÉ** | Même source contaminée et même absence d'identifiant article exact ; aucun résultat API ne prouve les variantes 36/39 mm et NH35/Miyota 8215. |
| P0 | `Trente-Neuf Rose — Classique cannelée` (`10978720317778`) | galerie-05 | **BLOQUÉ** | Même source contaminée et même absence d'identifiant article exact ; substituer une montre ou un boîtier proche créerait une fausse vérité produit. |
| P0 | `Bracelet FKM — tropical` (`10977445183826`) | galerie-02 | **BLOQUÉ** | L'unique source locale est un gros plan partiel ; une zone centrale est masquée/floutée et l'absence de marquage ne peut pas être confirmée. La recherche API renvoie des bracelets Apple/silicone/nylon ou d'autres objets, pas le bracelet FKM tropical exact. |
| P0 | `Bracelet FKM — tropical` (`10977445183826`) | galerie-03 | **BLOQUÉ** | Aucune vue complète propre. La fiche porte 108 combinaisons et 36 associations couleur/boucle : une image générique non rattachée à l'article d'origine ne permet pas de garantir la géométrie ni la vérité des coloris. |
| P0 | `Carte cadeau Maison Noirmont` (`10980393025874`) | galerie-02 | **ABANDON** | Produit numérique interne à la boutique, sans fournisseur AliExpress et sans SKU fournisseur pour ses quatre valeurs. Aucun fichier local alternatif n'a été trouvé. Une image fournisseur ne peut donc pas constituer une preuve produit exacte. Conserver l'image actuelle unique. |
| P0 | `Carte cadeau Maison Noirmont` (`10980393025874`) | galerie-03 | **ABANDON** | Même motif : l'objectif arbitraire de trois images ne justifie pas d'inventer deux vues d'un service numérique. Conserver l'image actuelle unique. |
| P2 | `Remontoir Solo` (`10977444626770`) | galerie-03 | **BLOQUÉ** | La seule source locale montre un remontoir sombre avec une gravure/inscription sur la façade. Les variantes actives conservées sont `14:193#Green` et `14:173#White`, ce que cette source ne permet pas de prouver. La recherche API n'a pas retrouvé l'article exact et son `product_id` AliExpress d'origine manque. |

## Preuves locales contrôlées visuellement

Les quatre JPEG ont été ouverts au niveau de détail original. Ils mesurent tous 2048 × 2048 px.

| Produit | Chemin de preuve | SHA-256 | Observation |
|---|---|---|---|
| Trente-Neuf Rose | `boutique-seiko-mod/livraisons/entrees-faces-REDONDANT-export-claude/trente-neuf-rose-classique-cannelee-face.jpg` | `374e705ddab182e4349f103543af3d8d7692fd299777cf879432c0cfcf318484` | Montre rose, lunette cannelée, cyclope ; « SWISS MADE » lisible à 6 h. Rejet. |
| Trente-Neuf Rose, sauvegarde | `boutique-seiko-mod/backups/backup-faces-swissmade-2026-07-26/trente-neuf-rose-classique-cannelee-ANCIENNE-FACE-swiss-made.jpg` | `9a9b9aee520933467817b5d916a98e1ac3b8675c3e680c0d8c1ff71bfcbfd968` | Même composition et même verbatim « SWISS MADE ». Rejet. |
| Bracelet FKM tropical | `boutique-seiko-mod/livraisons/entrees-faces-REDONDANT-export-claude/bracelet-fkm-tropical-face.jpg` | `c5d4499684402016f1ddcd9e593038585d8ec3a8a6e31c40f8eececa9c4d8158` | Macro partielle noire ; zone/lettrage central masqué ou flouté ; produit complet non observable. Rejet. |
| Remontoir Solo | `boutique-seiko-mod/livraisons/entrees-faces-REDONDANT-export-claude/remontoir-solo-face.jpg` | `2d7d703e422b45c9874a0cbafebd42deb2951b951136c89470b08ab4d79a0ff7` | Remontoir arqué sombre avec inscription gravée sur la façade ; teinte non probante pour Vert/Blanc. Rejet. |

La recherche locale ciblée sur `carte cadeau` / `gift card` ne trouve aucun fichier image alternatif sous `boutique-seiko-mod/`.

## Vérité produit conservée localement

- `boutique-seiko-mod/INVENTAIRE-VISUEL-2026-08-08.csv` confirme les quatre produits actifs et les comptes 1/5, 1/3, 1/3 et 2/3 ayant produit les neuf emplacements.
- `boutique-seiko-mod/backups/backup-avant-reduction-meres.json` conserve pour la Trente-Neuf Rose huit variantes `pink no logo`, avec 36/39 mm, fond plein/verre et mouvements Miyota 8215/NH35, mais aucun identifiant d'article AliExpress.
- `boutique-seiko-mod/backups/backup-variantes-avant-decoupage.json` conserve la matrice historique du bracelet FKM, dont des propriétés telles que `FKM-Orange Black`, tailles et boucles, mais aucun identifiant d'article permettant une requête exacte.
- `boutique-seiko-mod/backups/backup-sku-2026-08-08/table-correspondance.jsonl` confirme les deux variantes du Remontoir Solo, Vert (`14:193#Green`) et Blanc (`14:173#White`), ainsi que les quatre variantes de carte cadeau avec `sku_actuel: null`.
- `boutique-seiko-mod/journal/2026-08-08-fournee-visuels-1.md` et `boutique-seiko-mod/journal/2026-08-09-rattachement-visuels.md` documentaient déjà les mêmes ruptures de preuve : « SWISS MADE », SKU de galerie FKM indéterminable, carte cadeau sans SKU, et gravure du Remontoir Solo.

Ces propriétés sont des fragments de variante, pas des identifiants AliExpress `product_id`. Elles ne suffisent donc pas pour appeler honnêtement les routes API de détail ou de variante sur l'article d'origine.

## Contrôle via l'API officielle AliExpress

Route utilisée uniquement : client local en lecture seule `codex-chasse-clusters/tools/aliexpress_vps_gateway.py`, vers le VPS autorisé et l'API AliExpress Open Platform / AE-Dropshipper.

- `health` : succès à `2026-08-09T22:41:03Z`; jeton d'accès annoncé valide jusqu'au `2026-09-01T18:29:47Z` et jeton de rafraîchissement jusqu'au `2026-10-01T18:09:12Z`.
- Méthode de recherche officielle : `aliexpress.ds.text.search`; destination `FR`.
- La méthode de détail disponible est `aliexpress.ds.product.get`, mais elle exige un `product_id` exact qui n'est pas conservé pour ces trois produits physiques.
- Requêtes principales relues à `2026-08-09T22:46:00Z` et `22:46:16Z`, tri `orders`, limite 10 :
  - `pink dial no logo fluted bezel automatic watch 36mm 39mm NH35 8215` ;
  - `pink no logo Miyota 8215 NH35 36mm 39mm` ;
  - `FKM tropical rubber watch strap 18mm 20mm 22mm` ;
  - `single watch winder green white no logo`.
- Des recherches complémentaires ont aussi été tentées avec les propriétés locales et les tris prix. Le tri `latest` a renvoyé `IOPUpstreamError / EXCEPTION_TEXT_SEARCH_FOR_DS` et n'est pas retenu comme preuve de résultat.

Résultats disqualifiants représentatifs :

| Requête | Résultat API | Pourquoi il ne peut pas servir |
|---|---|---|
| Trente-Neuf Rose | `1005005597724853`, mouvement NH35 seul | Ce n'est pas une montre et ne prouve ni cadran rose, ni boîtier, ni bracelet. |
| Trente-Neuf Rose | `1005008518115553`, support d'assemblage NH34/NH35/8215 | Outil de réparation, pas produit fini. |
| Bracelet FKM | `1005006706836534`, bracelet silicone Apple Watch | Forme, matière/interface et tailles incompatibles avec la matrice FKM tropical. |
| Remontoir Solo | `1005008940491816`, boîte de rangement cinq montres | Boîte passive, pas remontoir motorisé Solo. |

Les autres premières pages sont tout aussi hors sujet (pieds à coulisse, protections Apple Watch, bracelets nylon, enrouleurs de câble, montres connectées). Aucune image CDN de ces résultats n'a été retenue ni téléchargée : leur titre et leur type produit suffisaient déjà à les disqualifier. Une recherche textuelle négative ne prouve pas l'inexistence du produit ; c'est pourquoi les sept emplacements physiques restent **BLOQUÉS**, et non abandonnés.

## Conséquence pour la réconciliation des 319 visuels

- Ne compter aucun des neuf emplacements comme livré.
- Retirer, après validation de l'arbitrage, les deux ajouts de galerie de la carte cadeau de la cible active : une image actuelle est cohérente pour ce service numérique.
- Les sept emplacements physiques restants ne peuvent être réouverts qu'avec au moins une de ces preuves : `product_id` AliExpress d'origine, export fournisseur complet contenant les URLs des médias, ou nouvelles photos locales exactes montrant le produit complet sans marque/verbatim.
- Ne pas fabriquer de galerie générique à partir d'un produit « proche » : cela contredirait les variantes actives et la séparation entre preuve fournisseur, vérité produit et image de vitrine.
