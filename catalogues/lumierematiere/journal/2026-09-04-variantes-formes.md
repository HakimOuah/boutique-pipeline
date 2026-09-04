# Variantes formes — production locale du 04/09/2026

État : LIVRAISON PARTIELLE VÉRIFIÉE ; reste bloqué sur preuves/arbitrages. Aucun changement Shopify/DSers, aucune réattribution de SKU.

## Contrôle préalable des sources

Au précontrôle initial, les trois lots JSON et le brief du dépôt étaient identiques aux quatre pièces jointes fournies par Hakim. Le commit concurrent **52a9f80**, détecté avant livraison finale, a ensuite corrigé la référence A2 de 405368 : cette correction est intégrée. 20 fiches distinctes : P1=4, P2=7, P6=9 (le texte « dix fiches » de P6 est une coquille).

Lecture visuelle des fichiers locaux, sans extrapolation des codes :

| Fiche | Observation / décision |
|---|---|
| 538307 | Vert=green2.jpg, Blanc=white1.jpg ; Orange déjà couvert. |
| 405368 | Bordeaux/blanc=A1, jaune/orange=B1, beige/blanc=A2 (SKU `200000531:173#A2`) après correction 52a9f80. Câble blanc sur A2, noir sur A1/B1. D1 beige/vert est non vendu ; premier rendu écarté puis A2 régénéré. Le g1 est bien A2 beige/blanc. |
| 092465 | Les six vues montrent le même assemblage pierre claire + bois brun ; aucune seconde finition identifiable. Ne pas inventer une version brune. |
| 897170 | 06.jpg porte explicitement « Plastic material » et montre un pétale tressé synthétique ; 04.jpg porte « cloth », pas « rotin ». Plastique documenté, rotin non prouvé. |
| 623305 | 01=A7 tambour ; 02=A8 pans coupés ; 03=A9 volume arrondi. A8 est large au milieu et resserré aux extrémités : la formule « diabolo pincé à mi-hauteur » du brief ne correspond pas à la source. Suivre 02.jpg. |
| 975417 | Quatre dessins visibles (ombrelle plissée, cloche, petite cloche à calotte, corolle ondulée), aucun badge A/B/C/D dans 01–06. Correspondances bloquées. Titre trop restrictif. |
| 338324 | Cylindres bas/hauts, bois clair/foncé ; 05/06 montrent Ø12 H10, sans code. Correspondances A/B/C/D bloquées. |
| 147607 | Nombreux volumes dans 01, galet dans 05, cônes dans 06 ; aucun code Forme A/B/C. Correspondances bloquées. |
| 253182 | 03 porte A et montre une céramique blanche à motifs géométriques bleu sombre ; g1 rouge. A prouvé, B/C non attribuables aux couleurs par déduction. Le titre rouge ne décrit pas A. |
| 560098 | Fleurs=03/04, rayures=02/05, aucun badge A/B. Correspondances bloquées. |
| 272937 | Blocage explicite du brief, aucun visuel à produire sans arbitrage des configurations. |

## Cotes P6

| Fiche | Preuves disponibles / limites |
|---|---|
| 588683 | 06.jpg : Ø20/25/30 cm, épaisseur 45 mm = 4,5 cm. 02.jpg montre séparément Ø23 cm non demandé : ne pas le reprendre. Applique sans câble pendant. |
| 330664 | Tailles 100/120/150 dans JSON ; aucune cote dans les six sources. Barres linéaires, pas un disque : ne pas utiliser le symbole diamètre pour leur largeur. |
| 246282 | Diamètres 30/40/50/60 dans JSON ; aucune cote de hauteur/câble/rosace dans les cinq vues. |
| 795468 | Les six vues montrent un plafonnier collé au plafond, pas une suspension à câble. Montage à arbitrer avant schéma. |
| 607504 | Blocage explicite du JSON jusqu’au renommage des tailles/matières. |
| 761433 | 06.jpg : Ø40/50/60, câble réglable 120 ; Ø30 demandé seulement dans JSON. Hauteur/rosace non cotées. |
| 377816 | 05.jpg : Ø40, câble 150 ; Ø30/50 demandés dans JSON. Hauteur/rosace non cotées. |
| 630923 | Toutes les vues montrent la suspension, aucune le plafonnier. 06 cote Ø80 H20, câble100 : ne pas transposer H20 aux Ø50/60 demandés. Montage plafonnier non prouvé. |
| 655008 | 02.jpg : Ø38 H20, câble120, rosaceØ10. Ø30/45 dans JSON ; hauteurs de ces tailles non documentées, ne pas les extrapoler. |

## Production et QA

Skill imagegen, outil intégré, un appel par visuel. Cadrage g1 comme référence ; matière/forme depuis source fournisseur. Conversion JPEG RGB 2048² par sips, sans modifier les sources. Les schémas incomplets seront explicitement distingués des schémas complets.

### Bilan livré

15 JPEG RGB 2048 × 2048 dans `../livraisons-visuels-codex/variantes-forme/` :

- P1 : **6 packshots** — 538307 Vert/Blanc ; 405368 Bordeaux et blanc / Jaune et orange / Beige et blanc (A2, câble blanc, corrigé avant livraison finale) ; 897170 Plastique.
- P2 : **3 packshots** — 623305 A8 et A9 ; 253182 A.
- P6 : **6 schémas** — 588683 complet ; 330664, 246282, 761433, 377816, 655008 partiels, avec les cotes manquantes écrites sur le visuel. Les diamètres seulement présents dans le JSON sont identifiés dans la table de preuves ci-dessus, ils ne sont pas présentés comme vérifiés sur une image fournisseur.

**Neuf fiches sans nouveau visuel** : 092465, 975417, 338324, 147607, 560098, 272937, 795468, 607504, 630923. Manquent également le rotin de 897170 et B/C de 253182. Voir les observations ci-dessus et les `ecartes` des 20 manifestes. Aucun rattachement automatique. L’ancienne anomalie de nommage 405368 est levée par le brief corrigé : A2 est la bonne référence, le rendu D1 n’est plus dans les livrables.

### Échelle des schémas : correction après QA

Trois premiers essais imagegen de schémas ont été écartés. Les nombres étaient corrects, mais les largeurs des barres 100/120/150 n’étaient pas dans le rapport demandé ; le même risque existait sur les diamètres. Les six livrables P6 ont donc été créés comme **dessins techniques SVG originaux calculés**, exportés en JPEG par Sharp. Aucune photo fournisseur n’a été retouchée par code. Les SVG sont conservés à côté des JPEG pour révision.

L’échelle des largeurs est exacte dans les géométries (18, 9, 11 ou 10 pixels/cm selon planche), avec rasterisation à 2048². Les hauteurs non documentées ne sont pas cotées ; le dessin ne constitue pas un plan d’installation. Seul le Ø38 de 655008 porte H20. Les longueurs de câble sont données en légende, câbles raccourcis par un signe de rupture. Sur le schéma partiel 655008, la rosace connue est décrite en légende, sans dessin d’une fixation non documentée.

### Vérifications

- **20/20 manifestes** lisibles au schéma demandé ; 15 fichiers déclarés, 9 manifestes sans image et avec exclusion explicite.
- **15/15 JPEG RGB 2048²**, sources existantes, **15 SHA-256 distincts**, aucune erreur technique.
- **6/6 comparatifs** : rapport pixels/cm constant dans chaque SVG.
- QA visuelle des 9 packshots : états allumés, teintes/matières, profils A8/A9, cadrages cohérents avec les g1, absence de texte/décor. Il s’agit de dérivés générés, pas d’une comparaison pixel à pixel ni d’une preuve physique du produit.
- QA des 6 schémas : silhouette, libellés, absence de chevauchement et échelle des largeurs. Les cotes manquantes restent MANQUANT.
- Les essais non retenus sont isolés dans `essais-non-retenus/` et absents des manifestes ; ne pas importer les JPEG par recherche récursive aveugle.
- `git diff --check` et validation de syntaxe des scripts effectués avant commit.

### Fichiers de relais

- [Registre durable : manifestes, correspondances, sources et prompts](2026-09-04-variantes-formes-registre.json).
- [QA technique et empreintes](2026-09-04-variantes-formes-qa.json).
- [Générateur des schémas](../scripts/generer-schemas-variantes-20260904.cjs) ; [vérificateur](../scripts/verifier-variantes-20260904.py).
- Dossier local : `../livraisons-visuels-codex/variantes-forme/`, avec `README.md`, `prompts-production.json`, `qa-geometrie.json`, `qa-packshots.jpg`, `qa-schemas.jpg` et un manifeste par fiche.

Les images, SVG, sources et manifestes locaux sont exclus par `.gitignore` ; aucun forçage Git. Le registre, la QA, le journal, le tableau et les scripts sont versionnés. Aucune vérification live Shopify n’a été effectuée : les chiffres du brief restent ceux de son audit daté.
