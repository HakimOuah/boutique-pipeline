# Exécution des 7 étapes — Maison Noirmont — 10/08/2026

## Cadre

- État cible : `GMC_READY`.
- Mode économique : boutique spécialisée à catalogue étendu, déjà validée et en construction ; cette passe reste aux portes 4 et 5.
- Aucun achat ni paiement.
- Aucune activation de produit, publication de collection, suppression du mot de passe ou création Merchant Center avant la preuve des cinq conditions de la passation.

## Journal des actions

### Correction de la collection active « Cadrans à chiffres »

- Collection : `gid://shopify/Collection/691208290642`
- Handle : `montre-cadran-a-chiffres`
- État initial observé par le MCP Shopify le 10/08/2026 : 5 produits actifs ; description contenant « et non des chiffres orientaux de l'écriture arabe : nous n'en proposons pas ».
- Cible autorisée : supprimer uniquement la contradiction future, sans changer le titre, le handle, les produits, l'image, l'ordre de tri ni le statut de publication.
- Nouvelle phrase : « Il s'agit bien des chiffres 1 à 12 que vous lisez ici, et non des chiffres orientaux de l'écriture arabe, qui constituent une famille distincte. »
- Rollback : remettre la phrase initiale dans `descriptionHtml` via la mise à jour de collection Shopify.
- Résultat : modification appliquée via le MCP Shopify le 10/08/2026.
- Vérification après écriture : nouvelle lecture MCP conforme ; titre, handle, image, tri, type manuel, 5 produits actifs et leurs prix sont inchangés. Seule la phrase ciblée diffère.

### Nettoyage réversible des doublons et du cadran à risque de marque

Décision : archiver les fiches perdantes plutôt que les supprimer. Cela retire les fiches du catalogue exploitable tout en conservant un rollback et les correspondances DSers.

| Fiche archivée | Motif | Fiche conservée / preuve de choix |
|---|---|---|
| `cadran-pilote-29-aiguilles-nh35` — `gid://shopify/Product/11013081563474` — AliExpress `1005006012512581` | Même produit, mêmes 21 variantes et mêmes photos que l'autre fiche. | `cadran-pilote-29-classique-nh36` / `1005007635155982` : prix source inférieur et signal fournisseur plus fort dans le relevé du 09/08. |
| `cadran-pilote-noir-33-5-nh35` — `gid://shopify/Product/11013081629010` — AliExpress `1005003002119259` | Même produit et mêmes photos ; fiche plus complexe avec variantes de compatibilité supplémentaires et signal fournisseur plus faible. | `cadran-pilote-noir-33-5-nh34` / `1005008660462030` : 324 ventes relevées contre 130, 96 avis contre 16, catalogue de variantes plus lisible. |
| `mouvement-nh35-japon` — `gid://shopify/Product/11013057478994` — AliExpress `1005005597724853` | Même mouvement NH35, date blanche à 3 h ; stock Shopify observé 158. | `mouvement-nh35-date-blanche` / `1005008494235697` : stock observé 9 667, prix légèrement inférieur et signal fournisseur restant élevé (+5 000 ventes, 740 avis au relevé du 09/08). |
| `cadran-lumineux-28-5-nh35` — `gid://shopify/Product/11013078909266` | Le cadran porte « SUPERLATIVE CHRONOMETER / OFFICIALLY CERTIFIED », verbatim Rolex incompatible avec la ligne sans marque. | Aucun remplacement automatique ; un produit propre devra être qualifié séparément. |

État initial relu via le MCP Shopify le 10/08/2026 : les quatre fiches sont `DRAFT`. Aucune fiche active n'est visée. Rollback : repasser individuellement une fiche de `ARCHIVED` à `DRAFT` après nouvelle preuve.

Résultat : les quatre passages à `ARCHIVED` ont réussi. Une seconde lecture MCP confirme `ARCHIVED` pour chaque GID, avec le nombre de variantes et l'inventaire inchangés.

Un cinquième brouillon a ensuite été archivé séparément : `montre-cadran-arabe-oriental-36-39` (`gid://shopify/Product/11013081366866`, AliExpress `1005010249362754`). La fiche mélangeait 40 variantes `blue/black/white/green` et `… sterile`, alors que la description promettait de ne commander que les variantes sans logo ; ses 15 médias étaient des images fournisseur sans alt et la photo principale montrait la famille Tandorio. État initial `DRAFT`, état final relu `ARCHIVED`, 40 variantes, stock total 11 995 et 15 médias inchangés. Rollback : revenir à `DRAFT` uniquement après élagage aux variantes stériles et remplacement complet des visuels.

L'audit complémentaire des treize brouillons stériles/pilote sans manifeste a ensuite prouvé trois autres retraits réversibles. Ils ont été relus `DRAFT`, archivés ensemble via Shopify, puis relus `ARCHIVED` sans changement de variantes, stock ou médias :

| Fiche archivée | Motif | État relu après écriture |
|---|---|---|
| `cadran-sterile-bleu-lumineux-28-5` — `gid://shopify/Product/11013078810962` | Les 18/18 variantes portent physiquement `AUTOMATIC / WATER RESISTANT / 100m:330ft` ; aucune variante ne tient la promesse stérile. | 18 variantes, stock 508, 12 médias inchangés. |
| `cadran-plongee-33-5-aiguilles` — `gid://shopify/Product/11013078581586` | Doublon trompeusement nommé : ses cinq médias API sont octet-identiques à ceux de la meilleure fiche rétro conservée. | 10 variantes, stock 1 533, 10 médias inchangés. |
| `cadran-retro-33-5-aiguilles-nh35` — `gid://shopify/Product/11013078286674` | Même produit et mêmes compositions que la fiche rétro conservée, mais recompressés et filigranés ; similarité SSIM 0,9525 à 0,9765. | 10 variantes, stock 426, 8 médias inchangés. |

La fiche canonique conservée est `cadran-retro-blanc-rose-nh35` / AliExpress `1005008468061052`, dont les sources sont les plus propres et le signal fournisseur le plus fort du trio. Rollback : remettre individuellement une fiche archivée à `DRAFT` seulement après une nouvelle preuve produit distincte et conforme.

### Décision sur les cinq dossiers arabes bloqués

- Correction de périmètre : ce sont cinq dossiers source excédentaires, pas cinq fiches Shopify ; la recherche par handle exact renvoie zéro produit.
- Quatre abandons visuels nets : verbatim associé à Rolex, variantes uniquement `S Dial`, ou chiffres occidentaux au lieu des glyphes arabes orientaux.
- `1005006492769759` possède des variantes stériles visuellement propres, mais est abandonné comme nouveau candidat : 4 ventes, 1 avis et doublon du brouillon Shopify `gid://shopify/Product/11013081366866` / AliExpress `1005010249362754`.
- Bilan : `0/5` récupérable pour un nouvel import. Le rapport détaillé et les limites de la surface API sont consignés dans `DECISION-5-FICHES-ARABES-AGENT-2026-08-10.md`.

### Re-sourcing API des cadrans arabes orientaux

- Surface explorée : 118 recherches AliExpress Open Platform réussies, 811 item IDs distincts ; 12 erreurs amont conservées sur le tri `latest`.
- Résultat supplémentaire qualifié : `1005007348127532`, cadran 28,5 mm NH35/NH36, 58 ventes, 13 évaluations, 12 variantes visuellement propres, coût rendu France observé 11,18 à 11,78 EUR.
- Les deux contrôles éliminatoires passent sur les 12 variantes : glyphes arabes orientaux visibles et aucun logo/verbatim sur le cadran physique. Les images restent des sources fournisseur non publiables brutes.
- Refus maintenus : `1005012130205925` est propre mais sous le plancher de 10 ventes (9 ventes, 0 évaluation) ; `1005010278946311` porte `S Logo` et `660ft-200m PROFESSIONAL AUTOMATIC`.
- Avec le candidat déjà qualifié le 09/08 (`1005009751528666`), le lot honnête ne compte que 2 produits distincts. L'objectif de 4 à 8 n'est pas atteint ; aucun import partiel n'est lancé.

### Clôture et rattachement de la file visuelle prioritaire

- Les cinq derniers lots stériles/pilotes de la file existante sont `done` : stérile lumineux, sunburst, météorite, vierge stérile et pilote noir NH34.
- Le pilote NH34 a livré 3/3 JPEG 2048 × 2048 après cinq rejets internes correctement isolés ; le contrôle source/planche confirme chiffres 1–24, index, piste, aiguilles et absence de marque.
- L'ancien lot `cadran-pilote-33-5-aiguilles-lumineuses` déclarait à tort son g3 terminé alors que la QA l'avait reclassé en rejet. Une reprise de ce seul slot a été validée classe A, exécutée, puis relue : `done`, 1/1, zéro rejet ; g1 et g2 n'ont pas été écrasés.
- État final de la boîte : aucun exécuteur vivant, verrou absent, `inbox` vide et `en-cours` vide hors `.gitkeep`.
- Les 26 livrables finaux de neuf fiches cadran en brouillon ont été téléversés et ajoutés via Shopify. Aucune image fournisseur n'a été retirée, aucun statut/stock/prix/SKU/variante n'a changé. Le contrôle indépendant donne 160 médias après ajout contre 134 avant.
- Le détail par fiche, les réserves QA et les 26 identifiants de rollback sont dans `RATTACHEMENT-VISUELS-BROUILLONS-2026-08-10.md`.

Le rapprochement live par tags a aussi retrouvé treize autres brouillons stériles/pilote qui n'appartenaient pas à la file initiale. Leur audit API complet donne **5 PRODUISIBLE, 5 BLOQUÉ et 3 ARCHIVER**. Les cinq blocages restent hors génération : variantes mixtes avec texte physique, lettres `N/E/S/W` sur le cadran ou filigrane traversant le produit. Les trois archivages ont été appliqués comme décrit plus haut. Les cinq sources propres restantes sont des opportunités de lot futur, pas une extension implicite de la file déjà demandée. Le détail est dans `AUDIT-13-BROUILLONS-SANS-MANIFESTE-API-ALIEXPRESS-2026-08-10.md`.

### Affectation des six nuanciers du bracelet caoutchouc gaufré

- Produit : `gid://shopify/Product/10980388536658`, handle `bracelet-caoutchouc-gaufre`, statut `ACTIVE`.
- État initial relu via Shopify : 9 médias produit, 72 variantes, aucune association média-variante.
- Périmètre : réutiliser les six médias déjà présents ; aucune création ou suppression de média, aucun changement de prix, stock, SKU, option, texte ou statut.
- Chaque nuancier « boucle argentée » doit être affecté aux deux largeurs vendues du SKU fournisseur correspondant :

| Nuancier | Média Shopify | Variantes 20 / 22 mm |
|---|---|---|
| Vert kaki | `gid://shopify/MediaImage/59894129033554` | `54098042618194`, `54098042749266` |
| Rouge | `gid://shopify/MediaImage/59894129066322` | `54098043666770`, `54098043896146` |
| Bleu profond | `gid://shopify/MediaImage/59894129099090` | `54098042880338`, `54098043109714` |
| Brun | `gid://shopify/MediaImage/59894129131858` | `54098043142482`, `54098043371858` |
| Noir | `gid://shopify/MediaImage/59894129164626` | `54098043404626`, `54098043634002` |
| Orange | `gid://shopify/MediaImage/59894129197394` | `54098044191058`, `54098044420434` |

Rollback : détacher ces six médias des douze variantes par `productVariantDetachMedia`, sans retirer les médias de la galerie.

Résultat : mutation validée contre le schéma Shopify puis appliquée sans `userErrors`. Une requête indépendante après écriture confirme 6 médias distincts associés aux 12 variantes attendues, 9 médias produit et 72 variantes au total ; le produit reste `ACTIVE`.

### Clôture des cinq doutes techniques du §4.2

Le détail des preuves AliExpress et des limites est conservé dans `DECISION-DOUTES-TECHNIQUES-AGENT-2026-08-10.md`. Les décisions ont ensuite été appliquées uniquement à des fiches `DRAFT`, puis relues par le MCP Shopify.

| Fiche | Action appliquée | Vérification après écriture |
|---|---|---|
| `cadran-squelette-nh70-3-coloris` — `gid://shopify/Product/11013068915026` | Titre et description resserrés sur l'anneau NH70/NH72 et la seule promesse prouvée : points et petits repères lumineux. Intensité et durée explicitement non mesurées. | `DRAFT`, 7 variantes, stock total 1 145, 13 médias inchangés. |
| `cadran-squelette-29-noir-blanc` — `gid://shopify/Product/11013068816722` | Promesse lumineuse retirée. Le titre et le texte distinguent anneau seul, anneau avec aiguilles et aiguilles seules. | `DRAFT`, 5 variantes, stock total 1 573, 10 médias inchangés. Les cinq libellés d'option restent en anglais et le remapping fournisseur reste obligatoire avant activation. |
| `cadran-transparent-lume-28-5` — `gid://shopify/Product/11013068849490` | Fiche archivée : les disques et anneaux sont des SKU séparés alors que deux pièces sont nécessaires. | `ARCHIVED`, 11 variantes, stock total 1 078, 17 médias inchangés. |
| `support-mouvement-acrylique` — `gid://shopify/Product/11013057118546` | Titre et description clarifiés : vingt références au choix, un seul support livré, mouvement non inclus, jamais universel. | `DRAFT`, 20 variantes, stock total 748, 4 médias inchangés. |
| `cadran-sterile-index-35` — `gid://shopify/Product/11013068620114` | Fiche archivée : seules A1–A4 sont des cadrans ; B1–B8 sont des aiguilles et C1–C2 des boîtiers. | `ARCHIVED`, 14 variantes, stock total 1 354, 16 médias inchangés. |

Rollback : remettre individuellement un produit archivé à `DRAFT`, ou restaurer les anciens titres/descriptions consignés dans l'historique Shopify. Aucun prix, SKU, stock, variante, média ou mapping DSers n'a été modifié. Les deux brouillons maintenus et le brouillon prudent restent non activables sans les libellés français, le contrôle de mapping et les autres portes globales.

### Réconciliation de la campagne dite « 319 visuels »

Le chiffre historique de 319 mélangeait 304 besoins de fiches actives et 15 besoins de brouillons. La réconciliation ligne par ligne du brief, du manifeste local et du rattachement Shopify donne :

| Priorité active | Cible | Livré et rattaché | Reste à produire |
|---|---:|---:|---:|
| P0 — galeries bloquantes | 14 | 6 | 8 |
| P1 — galeries prioritaires | 41 | 41 | 0 |
| P2 — galeries secondaires | 14 | 13 | 1 |
| P3 — médias de variantes montres | 33 | 0 | 33 |
| P4 — médias de variantes accessoires | 202 | 6 | 196 |
| **Total actif** | **304** | **66** | **238** |

Les six médias P4 existants du bracelet caoutchouc gaufré sont bien rattachés au produit et, depuis cette passe, affectés aux douze variantes exactes. Les 15 besoins hors dénominateur actif sont cinq médias de galerie Aviateur et dix médias de variantes Noirmont Deux/Voyageur sur des brouillons historiques. Le rapport détaillé est `RECONCILIATION-319-VISUELS-AGENT-2026-08-10.md`.

L'audit fournisseur des neuf emplacements de galerie encore ouverts a ensuite établi qu'aucun n'était productible honnêtement avec les preuves actuelles : sept restent bloqués faute d'article exact propre et traçable (Trente-Neuf Rose 4, bracelet FKM tropical 2, Remontoir Solo 1) ; les deux ajouts prévus pour la carte cadeau sont abandonnés, car une fiche numérique interne n'a pas à recevoir deux fausses vues fournisseur. Aucun de ces neuf emplacements n'est compté comme livré. Le détail est dans `AUDIT-9-GALERIES-RESTANTES-API-ALIEXPRESS-2026-08-10.md`.

L'abandon motivé des deux fausses vues de carte cadeau et de quatre faux médias de remontoirs ramène la cible opérationnelle active de **304 à 298 fichiers**. Avant la nouvelle production, 66 sont livrés et 232 restent donc ouverts : 7 galeries bloquées, 33 P3 et 192 P4.

L'audit exact des 33 P3 a ensuite isolé **26 médias productibles et 7 bloqués**. Les 26 sources autorisées couvrent 127 variantes enfant qui partagent ces apparences ; les blocages sont six cadrans Explorateur avec texte physique et le Trente-Neuf Duo, dont le cadran porte du texte et dont la dimension 36/39 mm manquante n'est pas attribuable. Cinq ordres classe A totalisant 26 livrables ont été déposés et pris dans la file. Le mapping est dans `MAPPING-P3-33-VARIANTES-AGENT-2026-08-10.md`.

Sur P4, l'audit de 66 médias bracelets a qualifié **30/30** médias restants du bracelet caoutchouc gaufré à partir de l'article officiel AliExpress `1005008681374490`. Les **36/36** médias du bracelet FKM tropical restent bloqués faute d'item ID exact et de nuancier officiel traçable. Quatre ordres classe A totalisant 30 livrables gaufrés ont été déposés et pris dans la file. Le détail est dans `AUDIT-66-MEDIAS-BRACELETS-AGENT-2026-08-10.md`.

Les quatre lots gaufrés ont depuis livré 30 fichiers, dont 29 ont passé la QA de lot et ont été rattachés aux 58 variantes exactes : 2 argentés, 9 dorés, 9 à boucle noire et 9 or rose. Le blanc argenté initial, conforme au produit mais réservé pour son cadrage, reste volontairement non rattaché ; sa reprise ciblée est dans la file et remplace le même slot. Les trois lots de neuf passent sans réserve. Après relecture Shopify de chaque association, le compteur opérationnel atteint **95 / 298**. Les identifiants médias et le rollback sont consignés dans `RATTACHEMENT-VISUELS-ACTIFS-2026-08-10.md`.

Les 130 autres P4 ont ensuite été réconciliés ligne par ligne : **27 PRODUISIBLE, 99 BLOQUÉ et 4 ABANDON**. Les quatre abandons sont des médias `M120xx` dont les sources locales montrent des boîtes passives à un coussin, alors que les variantes vendent des remontoirs motorisés deux montres. Les 27 sources autorisées couvrent six bracelets acier massif, cinq lots de dix coussins, trois Jubilé courbes, huit milanais, deux étuis vides, deux outils de mise à taille et un rouleau noir trois montres. Les 99 blocages restent hors génération. Le détail est dans `AUDIT-130-MEDIAS-P4-RESTANTS-AGENT-2026-08-10.md`.

### État des cinq portes d'activation

Contrôle live effectué le 10/08/2026. Les cinq conditions de la passation doivent être vraies simultanément ; aucune ne l'est encore.

| Condition obligatoire | État observé | Preuve / action restante |
|---|---|---|
| Plus aucune photo AliExpress brute sur les fiches concernées | **FAUX** | Les 26 nouveaux visuels ont été ajoutés en fin de galerie sans retirer les médias fournisseur. Après abandon motivé de six emplacements trompeurs, la campagne active conserve 232 emplacements ouverts avant imputation du lot en cours. |
| Trois politiques collées par Hakim et médiateur renseigné | **FAUX** | La politique `TERMS_OF_SALE` servie par Shopify contient encore `[À COMPLÉTER]` et l'ancien lien ODR européen. |
| Grille de prix arbitrée et appliquée | **FAUX** | Les documents locaux présentent deux stratégies ; ils indiquent qu'aucun prix n'a été écrit. L'arbitrage appartient à Hakim. |
| Mesure d'achat installée et testée | **FAUX** | L'écran Shopify « Événements clients » ne présente aucun pixel ; Google & YouTube n'apparaît pas dans les applications installées. Aucun test d'achat n'est donc prouvé. |
| P0/P1 de `AUDIT-GMC-FINAL-2026-08-08.md` soldés | **FAUX** | P1 visuel est soldé, mais les P0/P1 globaux ne le sont pas : sept galeries restent bloquées, les politiques/prix/mesure restent ouverts et le contrôle final n'a pas produit de clôture. |

Conséquence : aucun produit n'est activé, aucune collection n'est publiée, le mot de passe reste en place et aucun compte CSS/Merchant Center n'est créé. Ces actions restent à Hakim après fermeture documentée des cinq portes.

## État des sept étapes

| Étape | Statut | Preuve ou blocage |
|---|---|---|
| 1. File visuelle stériles et pilote | FILE INITIALE TERMINÉE | File drainée, reprise g3 lumineuse terminée, 26 visuels approuvés ajoutés à 9 brouillons. Les 13 autres brouillons hors file ont été audités : 5 productibles, 5 bloqués et 3 archivés ; aucun blocage n'a été généré. |
| 2. Re-sourcing arabe | PARTIEL / BLOQUÉ | 2 produits distincts qualifiés au total ; 2 à 6 manquants malgré 811 IDs explorés. |
| 3. Cinq fiches arabes bloquées | TERMINÉE | 0/5 récupérable ; aucun des cinq handles n'existe dans Shopify. |
| 4. Import, rédaction et habillage | BLOQUÉ | La cible minimale de 4 produits distincts n'est pas atteinte ; aucun import partiel ou activation par défaut. |
| 5. Nettoyage catalogue | ASSAINI / ACTIVATION ENCORE BLOQUÉE | Contradiction corrigée ; cinq doublons perdants, deux cadrans à texte interdit, fiche arabe mixte et deux fiches techniquement incohérentes archivés ; 6 nuanciers affectés à 12 variantes ; trois fiches techniques réécrites. `cadran-squelette-29-noir-blanc` reste à libeller/remapper avant activation. |
| 6. Visuels des fiches actives | EN PRODUCTION / 203 OUVERTS | Cible opérationnelle révisée : 298 actifs après abandon motivé de six emplacements trompeurs ; 95 sont maintenant livrés/rattachés. Produisibles encore dans la file : 26 P3 + la reprise du blanc gaufré + 27 autres P4. Restent bloqués : 7 galeries, 7 P3, 36 FKM et 99 autres P4. |
| 7. Activation | BLOQUÉE — 0/5 CONDITION VRAIE | Aucune activation ni publication ; le détail des cinq échecs et des actions appartenant à Hakim est consigné ci-dessus. |
