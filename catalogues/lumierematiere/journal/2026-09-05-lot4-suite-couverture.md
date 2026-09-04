# Lot 4 — solde A2, B et C

## Livré localement le 04/09/2026

**27 nouveaux visuels : 17 packshots A2 + 10 schémas B.** Avec les 13 A1 conservés à l’identique, le dossier contient **40 JPEG RGB 2048 × 2048**, 21 manifestes et la planche `qa-couverture.jpg`. Les deux questions C sont traitées sans produire d’image.

**La couverture réelle n’est pas totalement fermée : `183789` nécessite deux images supplémentaires.** Les deux anciens packshots montrent sept palets, et non six. L’autorisation de dépasser le plafond de 40 a été demandée à Hakim ; en l’absence de réponse, aucune production supplémentaire engagée.

Livraison : `../livraisons-visuels-codex/couverture-2026-09-05/`. Ne publier que les fichiers déclarés dans les manifestes, jamais les planches QA ni les références fournisseur. **Aucun import, aucune mutation Shopify/DSers, aucun changement de SKU.** L’import A1 consigné ailleurs reste une opération distincte.

## A2 — 17 packshots, sources par identifiant

| Fiche | Nouveaux | Existant vérifié / réserve |
|---|---|---|
| 717226 | 4 anneaux | 6 anneaux conservé |
| 625575 | 4 anneaux | 6 anneaux conservé |
| 134962 | blanc 6 anneaux, option `-2` | blanc 5 `-5`, noir 5 `-1`, doré 5 `-3` conservés |
| 183789 | gris 5 `173`, blanc 5 `691` | Anciens gris/blanc = **7 palets**, à écarter. Six gris `366` et six blanc `10` restent à produire |
| 950316 | 4 et 8 bras | 6 conservé |
| 361680 | noir/doré × 4/8 bras | noir/doré 6 conservés |
| 992600 | noir/blanc/doré × 4/8 boules | trois finitions à 6 conservées |

Les sept PDP A2 et les deux PDP C ont été interrogées. **35 références DOM**, avec identifiants, libellés, URL de l’image enfant du noeud `data-sku-col`, horodatage et empreinte. La forme n’a jamais été déduite d’un autre comptage.

Limite explicitement conservée : certains clics ne confirment pas une nouvelle sélection (`992600`, doré 8 de `361680`). Dans ce cas la preuve est **la vignette directement attachée au noeud d’option**, et non le hero ; le manifeste ne prétend pas que la sélection a été confirmée. Ces références ont une définition de 220² : comptage lisible, détails fins moins définis. Trois grandes images de `134962` renvoient 403 ; leur vignette observée a été récupérée en remplacement, avec son URL exacte.

Le doré 4 de `361680` a été repris une fois pour corriger le haut de chaîne coupé : bras exclusivement tirés de sa source DOM 4T ; rosace/chaîne/tige prises sur le packshot doré existant, rôle explicite au manifeste. Le rendu écarté n’est pas livré. Les SKU sans ampoule de `950316` et `361680` restent sans ampoule : l’ampoule illustrée ne prouve pas son inclusion.

## B — dix schémas, un seul luminaire par image

Une silhouette de référence en élévation, sa cote disponible et un tableau des tailles. Des traits comparent les largeurs à une échelle commune : **aucune juxtaposition de plusieurs luminaires**. Les hauteurs non documentées sont notées « — », jamais déduites du rendu.

- `330664` : **largeur L 100/120/150**, pas diamètre ; hauteur totale 100 cm connue, corps non coté.
- `761433` : silhouette du Ø30, H20 prouvée ; les grands diamètres restent non cotés en hauteur et ne sont pas présentés comme la même silhouette à une autre échelle.
- `795468` : **plafonnier sans câble**, profil Ø20/H4,5 ; tailles Ø20/30 et finitions blanc/noir au tableau. Le vieux hero en suspension n’est pas une référence pour le montage.
- `607504` : tableau des quatre tailles/formes/finitions, illustration goutte naturelle Ø25/H50.
- `837156` : hauteur de l’abat-jour 6,5/9 cm, Ø20, deux émaux ; pas la hauteur du luminaire complet.
- `630923` : plafond Ø50/H14, suspension Ø50/H13, plafond Ø60/H18 ; câbles suspension 100 cm.
- `246282`, `655008`, `377816`, `588683` : cotes connues du lot P6 reprises, limites inscrites.

Les SVG éditables accompagnent les JPEG. Construction vectorielle originale, rendu sharp directement en 2048² ; pas de retouche des photographies fournisseur. Les schémas restent indicatifs, pas des plans d’installation.

## C — réponses

### 934110 : une incohérence fournisseur, pas deux matières prouvées

`193#Yellow Travertine` montre **un tube** en pierre poreuse beige Ø4/H28. `173#3000k-warm white` et `175#6000k-cold white` montrent **deux tubes** sur une rosace commune. Les deux références 173/175 sont rigoureusement identiques, SHA-256 compris. Aucun objet blanc distinct n’est démontré.

Un second axe existe, mais il n’a qu’une valeur : `5:361385#3000K warm light`. Il contredit donc la variante annoncée 6000 K. Conclusion : options hétérogènes mélangeant matière, montage simple/double et température, **pas une grille matière × température fiable**. La température réellement livrée pour la combinaison 6000K/3000K reste inconnue. Confirmation fournisseur nécessaire avant normalisation. Aucune image produite.

### 092465 : correspondance confirmée

`200000531:200006153` = « jaune clair » / Pierre claire, tête bois clair. `200000531:365458` = Brun, tête bois foncé. Les deux packshots existants ont été comparés aux références DOM et correspondent ; aucune régénération.

## Contrôles et limites

- 40 JPEG uniques, tous RGB 2048² ; 27 ajouts, 13 A1 dont les SHA-256 sont inchangés.
- Mention « un seul luminaire dans le cadre » et SKU servis dans chaque entrée ; 21 manifestes dont deux sans images pour C.
- Revue agent de toutes les références utilisées, de chaque rendu, de chaque schéma puis des planches. Le nombre de luminaires/lumières n’est **pas** prétendu détecté automatiquement.
- Générateur intégré `image_gen` pour les packshots : natif 1254², agrandissement proportionnel sips vers 2048², JPEG qualité 95. Les schémas sont natifs 2048².
- Une livraison locale ne prouve ni import, ni affichage de variante en boutique, ni validation GMC. Ces étapes ne sont pas effectuées ici.

## Fichiers de relais

- `2026-09-05-lot4-a2-production.json` : requêtes/prompts initiaux ; `2026-09-05-lot4-a2-resultats.json` : sorties finales et correction de cadrage.
- `2026-09-05-lot4-suite-preuves-dom.json` : export public limité aux produits, sans navigation personnelle du compte.
- `2026-09-05-lot4-suite-registre.json` : copie versionnable des 21 manifestes ; `2026-09-05-lot4-suite-qa.json` : bilan.
- `../scripts/lot4-schema-jobs.json` et `generer-schemas-lot4.cjs` : données et construction des schémas.
- `../scripts/finaliser-lot4-suite.py --reviewed` : finalisation locale ; ne passer le flag qu’après revue visuelle.

Les médias et manifestes dans le dossier de livraison sont exclus de Git conformément au dépôt. Leur registre, les preuves textuelles, les prompts et les scripts sont versionnés ; aucun `git add -f`.
