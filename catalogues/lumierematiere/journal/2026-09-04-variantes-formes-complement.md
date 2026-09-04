# Variantes formes — complément vérifié du 04/09/2026

## Résultat et périmètre

**34 JPEG RGB 2048 × 2048 déclarés dans 20 manifestes : 26 packshots et 8 schémas, dont 3 complets et 5 partiels.** Livraison locale, aucune écriture Shopify/DSers, aucun changement de SKU, titre, collection, prix ou publication. Les fichiers d'essais et planches QA ne font pas partie des 34 images.

Ce complément ajoute 17 packshots (14 générations intégrées et 3 réutilisations de canoniques vérifiés), ajoute 2 schémas et enrichit 3 schémas existants. Il remplace les blocages historiques du [premier compte rendu](2026-09-04-variantes-formes.md) lorsqu'une preuve nouvelle est disponible. Le lot global reste partiel : deux décisions métier, une référence A et des cotes restent manquantes.

Livraison : `../livraisons-visuels-codex/variantes-forme/`. Lire son README et les manifestes ; importer uniquement leurs champs `images`, jamais tous les JPEG récursivement. Les médias restent locaux et ignorés par Git. Les preuves nettoyées, prompts, contrôles et scripts sont versionnés.

## Recherche et correspondances résolues

Les six vues de galerie ne suffisaient pas. Lecture des sélecteurs publics de 16 pages fournisseur, clics sur les variantes et sauvegarde de l'image sélectionnée : identifiant `data-sku-col`, libellé affiché, URL exacte observée et empreinte de la référence JPEG. Les lettres fournisseur actuelles peuvent différer des lettres Shopify historiques : c'est l'identifiant de propriété qui fait la jointure.

[Preuves SKU nettoyées](2026-09-04-variantes-formes-preuves-sku.json), [plan avant génération](2026-09-04-variantes-formes-complement-plan.json), [production et prompts](2026-09-04-variantes-formes-complement-production.json), [registre actuel](2026-09-04-variantes-formes-registre.json).

| Fiche | Correspondance établie et livraison |
|---|---|
| 975417 / LM097 | Propriété 200000531 : 193=A cloche festonnée Ø18 H12 ; 173=B ombrelle plissée avec ampoule apparente (canonique réutilisé) ; 365458=C petite cloche Ø18 H8, chapeau laiton hémisphérique ; 175=D corolle large à quatre ondulations Ø23. A/B/C/D livrés. |
| 338324 / LM043 | 173=B cylindre bas Ø12 H10, bois foncé (canonique réutilisé), malgré le libellé fournisseur actuel « A-Darkwoodcolor ». 365458=C cylindre haut Ø11 H16,5, bois clair ; 175=D même forme haute, bois foncé. B/C/D livrés. 193=A absent du sélecteur actuel, recontrôlé ; aucune déduction par élimination. |
| 147607 / LM051 | 193=A Stone : cylindre bas large, long capuchon bois ; 173=B Stone : cylindre étroit ; 365458=C Stone : bloc carré. Trois lampes isolées livrées. Le canonique est un assortiment : il ne prouve pas une variante unique et n'a pas été réutilisé comme telle. |
| 560098 / LM105 | 193=A fleurs bleues ; 173=B rayures bleues/brunes. Deux packshots d'une seule suspension Ø19,5 H16, et non le double luminaire du canonique. |
| 253182 / LM106 | 193=A géométrique blanc/bleu conservé ; 173=B bande inférieure bleu-vert ; 365458=C bande rouge (canonique réutilisé). A/B/C livrés. |
| 092465 / LM046 | 200006153=Pierre claire : capuchon bois clair ; 365458=Brun : capuchon bois foncé. La pierre reste claire dans les deux cas. Deux packshots livrés, aucun renommage. |
| 897170 / LM020 | 193 « rattan50cm » prouve le rotin naturel ; 365458 « Plastic50 » prouve le plastique. Rotin ajouté, plastique de première passe conservé. Pas de duplication par diamètre. |

Ces preuves établissent l'identité photographique, pas la disponibilité commerciale, la livraison ou le mapping DSers courant. Les captures DOM complètes restent locales ; l'export durable exclut les informations de compte et de navigation.

## Schémas : cotes vérifiées et manquantes

| Fiche | État actuel | Preuves / limites |
|---|---|---|
| 588683 / LM122 | COMPLET | Ø20/25/30, épaisseur 4,5 cm ; applique sans câble pendant. Première passe conservée. |
| 795468 / LM062 | COMPLET — ajouté | Ø20/30, épaisseur 4,5 cm, montage plafonnier sans câble. Vues de dessous et profil ; le titre historique n'a pas été modifié. |
| 655008 / LM007 | COMPLET — enrichi | Ø30 H18 ; Ø38 H20 ; Ø45 H22 ; câble120 et rosaceØ10. Hauteurs additionnelles prouvées dans les sélecteurs. |
| 330664 / LM121 | PARTIEL — enrichi | Largeurs100/120/150 ; hauteur totale100 réglable ; fixation25×6×3,5 ; barre2 cm. La hauteur du corps lumineux et la longueur nue des suspentes ne sont pas isolées : ne pas appeler « câble100 » la hauteur totale. |
| 246282 / LM113 | PARTIEL | Ø30/40/50/60 du brief ; hauteurs, câble et rosace manquants. PDP fournisseur indisponible dans la région observée ; pas de contournement ni de cote ajoutée. |
| 761433 / LM018 | PARTIEL — enrichi | Ø30 H20 : cloche fermée bordée sombre, distincte des grands pétales Ø40/50/60. Câble120. Hauteurs des trois grandes tailles et rosace manquantes. |
| 377816 / LM016 | PARTIEL | Ø30/40/50 et câble150 confirmés ; hauteurs des abat-jour et rosace manquantes. |
| 630923 / LM014 | PARTIEL — ajouté | PlafonnierØ50 H14 ; suspensionØ50 H13, câbles réglables100 ; plafonnierØ60 H18. Diamètre de rosace de la suspension manquant. Aucun transfert de la hauteur du Ø80. |

Les largeurs, et les hauteurs lorsqu'elles sont prouvées, sont calculées à la même échelle dans chaque schéma. Les câbles raccourcis sont signalés. Les parties sans cote ne doivent pas être mesurées à partir du dessin. La version finale de 630923 déplace la mention des câbles au pied de l'image pour éviter le chevauchement avec les suspentes.

## Décisions indispensables avant le solde

### 272937 / LM028 — correction du brief à arbitrer

SKU A=193#A1, B=1052#B1, C=100018786#C1 : **trois plafonniers Ø16, H17 totale, abat-jour H12, fixationØ10**, et non suspension simple/applique/trio. A1 = monture noire et corde dorée ; B1 = monture blanche et corde claire ; C1 = monture noire et fibre brune.

Proposition : valider ces trois configurations de plafonniers et décider du traitement du titre/collection avant production. Aucun visuel généré, conformément au verrou explicite du brief ; aucune correction live effectuée.

### 607504 / LM027 — libellés à valider avant schéma

Propriété 200000795 : 193#2550 = Ø25×H50 naturel ; 10#4040 = Ø40×H40 naturel ; 175#4019 = Ø40×H19 naturel ; 367#4040BK = Ø40×H40 noir.

Proposition de libellés : **« Ø25 × H50 cm — Naturel », « Ø40 × H40 cm — Naturel », « Ø40 × H19 cm — Naturel », « Ø40 × H40 cm — Noir »**. Les quatre photos confirment dimensions, formes et finition. Le brief exige l'arbitrage du renommage avant de figer le schéma ; aucun schéma ni renommage live effectué.

### 338324 / LM043 — preuve manquante

Fournir une photo fournisseur associée explicitement à `200000531:193` (modèle A historique). L'identifiant est absent du sélecteur actuel ; B/C/D ne permettent pas d'inventer A. A reste hors livraison.

## QA et traçabilité

- [QA technique](2026-09-04-variantes-formes-qa.json) : PASS, 34/34 JPEG RGB 2048², 34 empreintes distinctes, sources existantes, 20 manifestes, 8 schémas à géométrie calculée. Deux fiches verrouillées restent sans image.
- Relecture des références et des images finales ; planches actuelles `qa-packshots.jpg` (26) et `qa-schemas.jpg` (8). Corrections du motif B de 560098, du cadrage C de 975417, de la rosace puis du cadrage C/D de 338324 ; cinq essais du complément conservés hors livraison. Les photos restent des packshots, pas des comparatifs métriques : le cadrage C/D est harmonisé, mais l'échelle apparente avec le canonique B n'est pas strictement identique.
- Le skill imagegen a guidé l'édition à partir de références exactes et la conservation des tentatives ; la génération intégrée a été utilisée pour les photographies. Le référentiel storefront a guidé le contrôle identité produit/variante. Schémas dessinés par le générateur SVG existant puis exportés en JPEG, sans cotes inventées.
- Les anciens états du registre sont historiques. `manifests`, `schemas_derniere_revision` et `complement_production` décrivent la livraison actuelle. Seules les images déclarées sont retenues.

Scripts : `collecter-preuves-variantes-20260904.py` (navigateur, lecture/clics), `generer-schemas-variantes-20260904.cjs` (SVG déterministe, refuse d'écraser un JPEG existant), `finaliser-complement-variantes-20260904.py` (jointure locale), `verifier-variantes-20260904.py` (format, provenance, géométrie, verrous). Les deux derniers se relancent avec Python3 depuis la racine du dépôt. Aucun de ces contrôles ne vaut validation du rattachement Shopify ou de l'état public.
