# Lot 3 — remplacement local des montages fournisseur

## Livraison

**16/16 images livrées et vérifiées : un seul luminaire dans le cadre.** Sept manifestes couvrent A à G : trois avec images, deux avec conclusion de recherche et deux sans action. Aucun import Shopify, aucune suppression d'ancien média, aucune modification DSers, de SKU, titre ou collection par cette intervention.

Dossier : `../livraisons-visuels-codex/montages-2026-09-04/`. Planche : `qa-montages.jpg`. Importer uniquement les fichiers du champ `images` des manifestes ; exclure la planche et `essais-non-retenus/`.

| Fiche | Livraison | Option représentée |
|---|---|---|
| 272937 | g1–g5 + modele-a/b/c-g1 = 8 | Vues sur A `200000531:193#A1` ; B `200000531:1052#B1` ; C `200000531:100018786#C1`. Plafonniers directs sans câble. |
| 560098 | g1–g5 = 5 | A floral bleu `200000531:193`, suspension simple, une rosace et un cordon. Packshots A/B du lot 2 non modifiés. |
| 147607 | g1, g2, g5 = 3 | Forme A `200000531:193`, cylindre bas en pierre et tête noyer. g3/g4 et packshots de formes conservés, non recopiés. |

Slugs modele-a/b/c : aucun renommage supposé. Le slot g4-lifestyle garde son nom conventionnel mais reste un packshot éditorial sur papier uni, sans pièce. Les proportions de272937 suivent la photo : total17, cage12, Ø16, rosace10 ; la formulation contradictoire « abat-jour17 » n'a pas servi à allonger la cage.

## D — 338324 : recherche close

Dernière ouverture de la PDP, lecture DOM et clics sur ses options. Le sélecteur expose seulement `200000531:173`, `200000531:365458`, `200000531:175`. **`200000531:193` reste absent.** Manifeste : INTROUVABLE_DEFINITIF_POUR_CE_LOT. Zéro génération, aucune déduction par élimination ; vue générique conservée pour les trois variantes A, sans mutation. « Définitif » clôture cette recherche, pas toute éventuelle réintroduction future par le fournisseur.

## E — 837156 : les « 2 » sont-elles le même objet ?

**Non. Ce sont deux formes d'abat-jour différentes dans deux couleurs.** Les « 2 » ont une cloche plus haute au bord ondulé ; les autres une corolle plus basse et évasée. Toutes sont Ø20, avec câble annoncé200 et rosace12 cm.

| Identifiant | Variante selon brief | Cote de la référence |
|---|---|---|
| `200000531:365458` | Céladon vert | Ø20 × H6,5 cm |
| `200000531:193` | Céladon vert 2 | Ø20 × H9 cm |
| `200000531:175` | Céladon bleu poudré | Ø20 × H6,5 cm |
| `200000531:173` | Céladon bleu poudré 2 | Ø20 × H9 cm |

Les libellés fournisseur sont identiques par couleur, mais les images et hauteurs diffèrent. Chaque clic a confirmé la sélection et son image. Ne pas fusionner sur le seul nom de couleur. Aucune génération ni modification boutique : E demandait uniquement cette identification.

## F / G et changements parallèles

F/897170 : aucune action. G/607504 : non produit dans ce lot limité par le message utilisateur à16 images et demandant d'attendre le renommage. Pendant la production, le [compte rendu d'arbitrage](2026-09-04-arbitrages-titres-variantes.md) a été ajouté : il consigne le renommage et ouvre deux visuels supplémentaires (schéma + noir), soit un périmètre18 distinct du présent lot16. Le manifeste G signale cette évolution sans prétendre que le renommage manque encore. La correspondance correcte y est documentée :193=2550,10=4040,175=4019,367=4040BK.

Ce travail parallèle consigne aussi les nouveaux titres et le retrait des montages de560098/147607. Ces modifications ont été préservées, pas réexécutées. Leur état live n'a pas été revalidé par cette intervention. Les nouveaux médias restent à importer ; les montages de272937 restent à remplacer lors de cet import.

## QA et provenance

- Références exactes sources-par-handle/variantes-20260904, identifiant vérifié dans preuves-dom.json. Les canoniques propres du lot2 servent à la cohérence ; aucun ancien montage utilisé comme entrée.
- Imagegen intégré :17 appels,16 rendus retenus. Premier g2 travertin rectangulaire écarté puis régénéré carré. Les sources natives carrées sont agrandies proportionnellement en JPEG RGB2048² qualité95 ; aucune prétention de résolution native2048.
- Revue individuelle puis planche complète : un seul luminaire, ou détail de celui-ci pour les macros ; pas de texte/cotes/logos/personnes/décor, formes et matériaux associés aux options.
- QA technique :16 empreintes SHA256 distinctes, sources existantes, ratios natifs carrés. Chaque image déclare sku_option, controle et nombre_luminaires_observe=1. Le comptage visuel est une revue agent, pas une détection PIL automatisée.
- Les preuves D/E horodatées sont dans variantes-lot3-20260904, sans écraser le lot2. L'export versionné exclut compte et navigation. La QA ne vaut ni import ni validation du flux GMC, ni preuve de contenu du colis (ampoule incluse ou non).

[Plan](2026-09-04-lot3-plan.json) · [Prompts et tentatives](2026-09-04-lot3-production.json) · [Preuves D/E](2026-09-04-lot3-preuves-dom.json) · [Registre](2026-09-04-lot3-registre.json) · [QA](2026-09-04-lot3-qa.json).

Contrôle rejouable : `python3 catalogues/lumierematiere/scripts/finaliser-lot3-montages.py`. Il reconstruit les manifestes et la planche sans toucher aux canaux de vente. Collecte : collecter-preuves-lot3-20260904.py via navigateur. Les skills imagegen/storefront ont guidé la fidélité au SKU et la séparation référence/rendu/import ; le skill navigateur a servi à D/E. Médias locaux ignorés par Git ; scripts, preuves nettoyées et rapports versionnés.
