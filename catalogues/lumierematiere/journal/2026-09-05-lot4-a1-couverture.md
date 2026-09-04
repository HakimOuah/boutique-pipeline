# Lot 4 A1 — couverture des formes et finitions

## Livraison locale

**13/13 packshots, 5 manifestes et `qa-couverture.jpg`.** Périmètre A1 seul, conformément à l'option de fractionnement du brief. A2 (17 images), B (10 schémas) et C (2 questions) ne sont pas traités dans cette passe.

Le dossier porte la date du brief, 05/09 ; génération et captures réalisées le 04/09/2026 au soir. Chaque preuve conserve son horodatage réel.

Livraison : `../livraisons-visuels-codex/couverture-2026-09-05/`. Ne rattacher que les JPEG déclarés dans les manifestes ; la planche QA n'est pas une image produit à publier. **Aucune action Shopify ou DSers, aucun SKU modifié, aucun ancien fichier remplacé.**

| Fiche | Visuels | Correspondance |
|---|---:|---|
| 607504 | 4 | `193#2550` goutte naturelle ; `10#4040` bulbe naturel ; `175#4019` coupole plate ; `367#4040BK` bulbe noir |
| 837156 | 4 | `365458` vert H6,5 ; `193` vert H9 ; `175` bleu H6,5 ; `173` bleu H9 |
| 630923 | 2 | `173` et `365458` plafonnier ; `193` suspension |
| 193329 | 2 | `193#Walnut Base A` bas noyer ; `173#Wood color A` bas bois clair |
| 338324 | 1 | `193` bas bois clair, reconstitué selon le brief — pas observé au DOM |

## 193329 — identification préalable résolue

La nouvelle passe DOM a sélectionné les quatre identifiants et confirmé l'image correspondante. Les planches cotées établissent :

| Identifiant | Libellé fournisseur | Forme | Dimensions |
|---|---|---|---|
| `200000531:193` | Walnut Base A | cylindre bas, tête noyer | Ø12 × H10 cm |
| `200000531:173` | Wood color A | cylindre bas, tête bois clair | Ø12 × H10 cm |
| `200000531:365458` | Walnut Base B | cylindre haut, tête noyer | Ø11 × H16,5 cm |
| `200000531:175` | Wood color B | cylindre haut, tête bois clair | Ø11 × H16,5 cm |

Le suffixe des SKU A est également vérifié dans l'export local `shopify/variants-work.json` ; ses anciens titres ne sont pas utilisés comme état actuel de la boutique. Après comparaison des quatre sources avec les deux anciens packshots, les images `variantes-couleur/...-bois-g1.jpg` et `...-noyer-g1.jpg` sont conservées pour la forme **B haute**. Le manifeste en donne les chemins, empreintes et SKU servis. Les deux nouvelles images couvrent A basse. Aucun renommage en boutique effectué.

## 338324 — exception de provenance, explicite

Le sélecteur expose toujours seulement `173`, `365458`, `175`. **193 reste absent** au contrôle du 04/09 à 18 h (horodatage exact dans l'export de preuves). Le lot3 avait donc bien laissé ce visuel non produit.

Le brief lot4 autorise désormais sa reconstitution à partir de la grille fournisseur et de `05.jpg`, qui montre le cylindre bas Ø12/H10 à tête bois clair. Le nouveau rendu reprend la composition du packshot B validé au lot2, avec la tête de bois éclaircie selon `05.jpg`, en conservant le cordon et la rosace bruns. Statut : `RECONSTITUEE_VALIDEE_PAR_BRIEF_NON_OBSERVEE_DOM`. Il ne faut pas le transformer en « référence 193 récupérée chez le fournisseur ».

## 630923 — mutualisation choisie

Le plafonnier Ø50/H14 et le plafonnier Ø60/H18 montrent la même silhouette de disque tressé, sans câble. Ils partagent un packshot canonique Ø50, qui **prouve le type de montage, pas l'échelle**. Le manifeste porte les deux SKU dans `sku_options_servis`. La suspension Ø50 dispose de sa propre image avec rosace et fils. Le comparatif coté relève du lot B, non livré ici.

## Vérifications et limites

- 13 générations intégrées, 13 retenues ; références par option inspectées avant chaque génération. Aucun montage fournisseur employé comme référence.
- JPEG RGB 2048 × 2048, qualité95 ; générations natives **1254 × 1254**, agrandies proportionnellement, sans étirement ni prétention de détail natif2048.
- 13 empreintes distinctes ; existence et empreinte des sources ; rattachements DOM validés par identifiant et état sélectionné, avec l'exception338324 déclarée.
- Revue agent individuelle et de la planche : **un seul luminaire dans le cadre**, silhouettes et teintes distinctes, pas de texte/cotes/logo/personne/décor de pièce sur les JPEG produit. Le contrôle visuel n'est pas présenté comme une détection automatique.
- Fond papier chaud, cible artistique `#F6F3EC` ; l'éclairage photographique induit de légères variations de tonalité, les cadrages ne constituent pas un comparatif métrique.
- Aucun contrôle d'import, de page live ou de flux GMC dans cette intervention. Aucun indice sur la présence d'une ampoule dans le colis ne doit être déduit du packshot allumé.

Les skills imagegen et navigateur ont encadré la production et l'identification ; storefront a orienté le contrôle sur la correspondance sélection/photo. Il s'agit d'une livraison locale, pas d'une publication.

[Prompts et sorties](2026-09-05-lot4-a1-production.json) · [Preuves DOM nettoyées](2026-09-05-lot4-a1-preuves-dom.json) · [Registre des manifestes](2026-09-05-lot4-a1-registre.json) · [QA](2026-09-05-lot4-a1-qa.json).

Rejouer : `python3 catalogues/lumierematiere/scripts/finaliser-lot4-a1.py`, puis examiner la planche et repasser avec `--reviewed`. Le script n'écrase pas les JPEG existants. Médias et DOM bruts restent locaux et ignorés par Git ; seuls les rapports, scripts, prompts, empreintes et preuves publiques nettoyées sont versionnés.

Arrêt après A1 comme permis par le brief. Les lots A2/B/C restent explicitement à faire. Pas de nouvel événement NOX : application de la méthode SKU/DOM déjà consignée, sans nouvelle règle générale ni premier résultat commercial.
