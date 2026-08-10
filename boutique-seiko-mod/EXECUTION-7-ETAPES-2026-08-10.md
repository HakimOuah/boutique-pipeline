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
- État final de la boîte, après toutes les vagues : aucun exécuteur vivant, verrou absent, `inbox` et `en-cours` contiennent **0 fichier JSON**.
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

La relecture finale de la collection publiée `Cadrans à chiffres` (`gid://shopify/Collection/691208290642`) a révélé une dernière promesse globale fausse : « Tous les cadrans sont stériles ». Elle contredisait les six apparences Explorateur bloquées pour texte physique. La description a été réécrite sans cette affirmation ; elle précise désormais que détails et inscriptions varient selon l'apparence et que le visuel de variante fait foi. La relecture Shopify confirme cinq produits inchangés et la phrase fausse absente.

### Réconciliation de la campagne dite « 319 visuels »

Le chiffre historique de 319 mélangeait 304 besoins de fiches actives et 15 besoins de brouillons. La réconciliation ligne par ligne du brief, du manifeste local et du rattachement Shopify donnait l'instantané initial ci-dessous ; ce tableau est historique et ne constitue pas le compteur final :

| Priorité active | Cible initiale | Livré et rattaché initial | Reste initial |
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

Le premier audit des 33 P3 avait isolé **26 candidats productibles et 7 bloqués**. Ces 26 candidats couvraient 127 variantes enfant ; cinq ordres classe A totalisant 26 livrables avaient été déposés et pris dans la file. Les contrôles approfondis décrits ci-dessous ont ensuite reclassé `Black C sterile`, les deux squelettes noirs et enfin `Blue1`. Le mapping initial est dans `MAPPING-P3-33-VARIANTES-AGENT-2026-08-10.md`.

Sur P4, l'audit de 66 médias bracelets a qualifié **30/30** médias restants du bracelet caoutchouc gaufré à partir de l'article officiel AliExpress `1005008681374490`. Les **36/36** médias du bracelet FKM tropical restent bloqués faute d'item ID exact et de nuancier officiel traçable. Quatre ordres classe A totalisant 30 livrables gaufrés ont été déposés et pris dans la file. Le détail est dans `AUDIT-66-MEDIAS-BRACELETS-AGENT-2026-08-10.md`.

Les compteurs 96, 101, 111, 118, 124, 129, 131, 134, 138, 141 et 149 présentés ci-dessous sont des **jalons chronologiques**, pas l'état courant. Seul le bilan final **151 / 298** fait foi.

Les quatre lots gaufrés ont livré 30 fichiers. Les 29 premiers ont passé la QA de lot ; le blanc argenté, d'abord réservé pour son cadrage, a ensuite été régénéré depuis sa source exacte et validé contre les gabarits jaune et bleu clair. Les **30/30** médias sont désormais rattachés aux 60 variantes exactes : 3 argentés, 9 dorés, 9 à boucle noire et 9 or rose. Après relecture Shopify de chaque association, le compteur opérationnel atteint **96 / 298**. Les identifiants médias et le rollback sont consignés dans `RATTACHEMENT-VISUELS-ACTIFS-2026-08-10.md`.

Le premier lot P3 Explorateur a livré six produits visuellement vrais. Cinq passent aussi le gabarit et sont rattachés à 40 variantes exactes, après remplacement réversible de leur association au média générique ; ce dernier reste dans la galerie produit. À ce stade historique, `Blue1` est retenu hors Shopify pour un écart d'échelle mesuré à +8,1 % et envoyé en reprise ciblée. Le compteur atteint alors **101 / 298** ; le verdict définitif de cette reprise est consigné plus bas.

Le lot P3 Field acier passe ensuite 10/10 : chiffres, éventuelle couronne 13-24, échelle minutes, aiguilles et coloris ont été comparés source par source. Les dix médias remplacent réversiblement l'association générique sur 60 variantes, six par apparence, sans supprimer aucun média de la galerie. La relecture Shopify ne trouve aucun écart ; le compteur atteint **111 / 298**.

Le lot P3 Field bronze donne 7 PASS et 1 blocage. Les sept médias sûrs remplacent l'association générique sur 14 variantes. `Black C sterile` reste hors Shopify : sa seule source exacte est un crop du cadran, et l'audit API de 18 images SKU n'a trouvé aucune vue complète prouvant boîtier, couronne et bracelet. Ses deux variantes gardent le média générique. Le compteur atteint **118 / 298** et les blocages P3 passent de 7 à 8.

Les deux squelettes noirs sont ensuite exclus. Pour le carré, l'unique source exacte tronque le bracelet ; le rendu ajoute une commande latérale et redessine la construction du bracelet. Pour l'octogone, l'article officiel `1005009354912699` ne prouve que cinq vis visibles et un bracelet/fermoir incomplets ; l'ordre contradictoire à huit vis a été rejeté après quatre essais et n'a produit aucun livrable final. Aucun des deux n'est chargé dans Shopify. Les blocages P3 passent alors à **10**.

La reprise `Blue1` est finalement **REJECTED** après huit régénérations intégrales. La référence Green1 mesure 454 px au masque 512 avec une tolérance maximale de 2 px ; la meilleure tentative Blue1 mesure 457 px, soit 3 px d'écart. Aucun redimensionnement correctif, inpainting ou remplacement du fichier existant n'a été appliqué, et aucun média Blue1 n'a été rattaché à Shopify. Le bilan P3 final est donc **22 / 33 rattachés et 11 bloqués**.

Le premier audit des 130 autres P4 avait donné l'instantané suivant : **27 PRODUISIBLE, 99 BLOQUÉ et 4 ABANDON**. Les quatre abandons sont des médias `M120xx` dont les sources locales montrent des boîtes passives à un coussin, alors que les variantes vendent des remontoirs motorisés deux montres. Les 27 candidats initiaux couvraient six bracelets acier massif, cinq lots de dix coussins, trois Jubilé courbes, huit milanais, deux étuis vides, deux outils de mise à taille et un rouleau noir trois montres. Le détail est dans `AUDIT-130-MEDIAS-P4-RESTANTS-AGENT-2026-08-10.md`.

Le premier de ces sept ordres P4 livre les six finitions du bracelet acier massif. Les six passent la QA source → rendu et remplacent le vide média sur 60 variantes, dix largeurs par finition. La relecture Shopify confirme 60/60 associations exactes et la photo principale inchangée. Le compteur atteint **124 / 298**.

Le lot suivant livre cinq coloris de coussins de présentation. Chaque fichier montre exactement dix coussins, sans texte ni accessoire, et passe le contrôle source → rendu. Les cinq médias sont affectés aux cinq variantes exactes auparavant sans association. La relecture Shopify confirme 5/5 ; à ce jalon historique, le compteur atteint **129 / 298** et 16 médias de la première vague P4 restent en production.

Les deux étuis rigides six montres passent ensuite 2/2 : extérieur noir, intérieur prune/fuchsia ou vert olive, six coussins complets, étui vide et aucun texte. Ils sont affectés aux deux variantes exactes auparavant sans association ; la relecture Shopify confirme 2/2 et porte le compteur à **131 / 298**.

Les trois Jubilé à embouts courbes passent 3/3 : cinq rangées, embouts et micro-ajustement conformes, fermoirs vierges, finitions acier/or exactes. Les trois médias couvrent quinze variantes auparavant sans association ; la relecture Shopify confirme 15/15 et porte le compteur à **134 / 298**.

L'audit fournisseur avait ensuite qualifié **16/16** sources du bracelet cuir daim : le cartouche `GIFT` est hors silhouette, les surfaces produit et boucles sont vierges, et le motif `V4` est une surimpression photographique. Deux ordres classe A de huit médias avaient alors été préparés. La QA finale et le rollback décrits ci-dessous remplacent ce statut provisoire : seuls les huit médias à boucle noire restent rattachés.

Les quatre Milanais 0,6 mm sont d'abord approuvés et rattachés à leurs seize variantes exactes, portant le compteur à **138 / 298**. Les outils de mise à taille noir et argenté (`59905208713554`, `59905208746322`) puis le rouleau trois montres WB13 (`59905226637650`) ajoutent trois médias et portent le compteur à **141 / 298**. Pour WB13, l'ancien média `59691418714450` reste dans la galerie et associé aux variantes une et deux montres ; seule son association avec la variante trois montres est remplacée.

Le premier rattachement des huit daim à boucle argentée était une erreur de QA. Les **8 médias et 32 associations** ont été retirés intégralement ; la galerie est revenue à ses trois médias originaux, le featured media `59691949293906` est resté inchangé et les 64 variantes étaient de nouveau sans média avant le lot noir. Ce rollback ne laisse aucun média argenté compté. Les huit daim à boucle noire sont ensuite validés et rattachés à **32 variantes exactes**, avec statut et featured media préservés, portant le compteur à **149 / 298**.

La reprise des quatre Milanais 1,0 mm ne qualifie finalement que l'argenté (`59905696923986`) et l'or rose (`59905696956754`), rattachés à huit variantes exactes. Le noir et l'or montrent encore un rail cylindrique incompatible avec la source : **NE PAS RATTACHER** ; leurs huit variantes restent sans média. Le compteur final atteint ainsi **151 / 298**.

Le bilan P4 final est **69 / 198 rattachés et 129 ouverts**. Les 69 rattachés se composent du palier historique de 36 médias, puis de 6 acier massif, 5 coussins, 2 étuis, 3 Jubilé, 4 Milanais 0,6 mm, 2 outils, 1 WB13, 8 daim noir et 2 Milanais 1,0 mm. Les 129 ouverts sont tous bloqués : 8 daim argentés, 2 Milanais 1,0 mm noir/or, 36 FKM et 83 autres P4.

Tous les ordres possèdent leur résultat individuel. Le wrapper a terminé avec le code global **3** uniquement parce que le processus enfant du daim argenté a été interrompu après avoir écrit son résultat `done`, mais avant de rendre proprement la main ; le wrapper a ensuite archivé l'ordre et poursuivi la file. Le rollback est complet. La file finale est drainée, le verrou est absent et `inbox` comme `en-cours` contiennent zéro JSON.

### État des cinq portes d'activation

Contrôle live effectué le 10/08/2026. Les cinq conditions de la passation doivent être vraies simultanément ; aucune ne l'est encore.

| Condition obligatoire | État observé | Preuve / action restante |
|---|---|---|
| Plus aucune photo AliExpress brute sur les fiches concernées | **FAUX** | Les 26 nouveaux visuels ont été ajoutés en fin de galerie sans retirer les médias fournisseur. Le compteur final de la campagne active est **151 / 298** et **147 emplacements restent ouverts**, tous bloqués. |
| Trois politiques collées par Hakim et médiateur renseigné | **FAUX** | La politique `TERMS_OF_SALE` servie par Shopify contient encore `[À COMPLÉTER]` et l'ancien lien ODR européen. |
| Grille de prix arbitrée et appliquée | **FAUX** | Les documents locaux présentent deux stratégies ; ils indiquent qu'aucun prix n'a été écrit. L'arbitrage appartient à Hakim. |
| Mesure d'achat installée et testée | **FAUX** | L'écran Shopify « Événements clients » ne présente aucun pixel ; Google & YouTube n'apparaît pas dans les applications installées. Aucun test d'achat n'est donc prouvé. |
| P0/P1 de `AUDIT-GMC-FINAL-2026-08-08.md` soldés | **FAUX** | P1 visuel est soldé, mais les P0/P1 globaux ne le sont pas : sept galeries restent bloquées, les politiques/prix/mesure restent ouverts et le contrôle final n'a pas produit de clôture. |

Conséquence : aucune activation ni publication n'est effectuée dans cette exécution, le mot de passe reste en place et aucun compte CSS/Merchant Center n'est créé. Ces actions restent à Hakim après fermeture documentée des cinq portes.

## État des sept étapes

| Étape | Statut | Preuve ou blocage |
|---|---|---|
| 1. File visuelle stériles et pilote | FILE INITIALE TERMINÉE | File drainée, reprise g3 lumineuse terminée, 26 visuels approuvés ajoutés à 9 brouillons. Les 13 autres brouillons hors file ont été audités : 5 productibles, 5 bloqués et 3 archivés ; aucun blocage n'a été généré. |
| 2. Re-sourcing arabe | PARTIEL / BLOQUÉ | 2 produits distincts qualifiés au total ; 2 à 6 manquants malgré 811 IDs explorés. |
| 3. Cinq fiches arabes bloquées | TERMINÉE | 0/5 récupérable ; aucun des cinq handles n'existe dans Shopify. |
| 4. Import, rédaction et habillage | BLOQUÉ | La cible minimale de 4 produits distincts n'est pas atteinte ; aucun import partiel ou activation par défaut. |
| 5. Nettoyage catalogue | ASSAINI / ACTIVATION ENCORE BLOQUÉE | Contradiction corrigée ; cinq doublons perdants, deux cadrans à texte interdit, fiche arabe mixte et deux fiches techniquement incohérentes archivés ; 6 nuanciers affectés à 12 variantes ; trois fiches techniques réécrites. `cadran-squelette-29-noir-blanc` reste à libeller/remapper avant activation. |
| 6. Visuels des fiches actives | FILE DRAINÉE / 147 BLOQUÉS | Cible opérationnelle : 298 médias ; **151 sont livrés/rattachés**. Décomposition finale : galeries 60/67, P3 22/33, P4 69/198. Les 147 ouverts sont tous documentés comme bloqués : 7 galeries, 11 P3 et 129 P4. Aucun ordre JSON ne reste dans `inbox` ou `en-cours`. |
| 7. Activation | BLOQUÉE — 0/5 CONDITION VRAIE | Aucune activation ni publication ; le détail des cinq échecs et des actions appartenant à Hakim est consigné ci-dessus. |
