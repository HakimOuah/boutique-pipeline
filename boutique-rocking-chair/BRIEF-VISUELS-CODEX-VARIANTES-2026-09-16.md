# Visuels par coloris — Bercelou (16/09/2026)

**Document de mission autoportant.** À lire après `BRIEF-VISUELS-CODEX-2026-09-14.md` (§2 direction « Veille douce », §4 QA, §5 livraison) et `BRIEF-VISUELS-CODEX-LOTS-2-5-2026-09-15.md` (§1 vérité produit, §2 scènes et formats). Tout y reste valable.

## 0. Pourquoi ce lot
Sur la boutique, quand un client clique sur une couleur, la photo ne change pas : les galeries actuelles ne montrent qu'un seul coloris par fiche. Il faut **une image par coloris vendu**. Shopify associera ensuite chaque image à sa variante.

Deux ordres :

1. **Lot V1, coloris** : 46 images, une par coloris en stock qui n'est pas déjà montré.
   `ordres/pour-codex/inbox/20260916-1000-generate_images-bercelou-variantes-couleurs.json`
2. **Lot V2, refonte de galerie** : 6 fiches dont la galerie actuelle montre une couleur que la boutique ne peut pas vendre (en rupture, ou absente de la fiche), soit 30 images.
   `ordres/pour-codex/inbox/20260916-1010-generate_images-bercelou-refonte-galeries.json`

## 1. Slot `couleur` (lot V1)

- **Ce que montre l'image** : le produit seul, dans le coloris demandé.
  - Mêmes cadrage, angle (trois quarts avant), pièce, lumière et accessoires de décor que l'image `face` déjà livrée pour la fiche : `livraisons/visuels-final-2026-09-15/<handle>-face.jpg`.
  - Seule la couleur du revêtement change. Le client doit voir la même photo, déclinée.
- **Référence de couleur** : `assets/source/<pid>/couleurs/<couleur>.jpg`, la photo du fournisseur pour ce coloris. Reprends exactement sa teinte, ainsi que la matière et les éléments qui changent avec le coloris (couleur des patins, du cadre ou des coussins).
  - Ne reprends ni les textes, ni les logos (« otautau », « VEVOR »), ni les cotes, ni les pictogrammes de ces photos.
- **Vérité produit** : la silhouette reste celle des sources `01.jpg` à `08.jpg` et de l'image `face` existante. Si la photo du coloris montre un autre modèle que la fiche, **ne génère pas** : rejette avec motif.
- **Format** : JPEG 2048 × 2048, qualité ~90. Nom : `<handle>-couleur-<slug>.jpg` (voir le manifeste).
- **Aucune personne** sur ce slot.

### Points connus, fiche par fiche

- **plaid-pour-fauteuil, « Caramel »** : teinte caramel ou camel de la photo fournisseur (coloris renommé le 16/09, ancien nom « Kaki foncé »).
- **fauteuil-cocon-suspendu, « Noir »** : coussin gris anthracite et panier noir, comme la photo fournisseur. L'image `face` existante montre le coloris vendu sous le nom « Gris foncé » (coussin beige, cadre noir).
- **repose-pieds-assorti** : pouf rond au pied d'un rocking chair, comme l'image `face`. Onze teintes vives ou sombres : garde la même scène douce, seul le pouf change de couleur.
- **housse-de-protection-rocking-chair, « Argent »** : housse rectangulaire argentée posée sur un mobilier de terrasse, comme l'image `face` noire.
- **rocking-chair-papasan-avec-pouf, « Blanc »** : fauteuil et pouf en tissu épais blanc cassé, même cadre noir.
- **fauteuil-relax-electrique** : aucune télécommande, aucun pictogramme ni aucune tête de massage visibles.
- **chaise-a-bascule-enfant et rocking-chair-bebe, « Gris »** : la coque et l'assise deviennent grises, la structure reste claire. Aucun bébé.

## 2. Refonte de galerie (lot V2)

Pour les 6 fiches du tableau, l'actuelle couleur des slots `face`, `nuit`/`salon`/`soir`/`reglages`, `matiere` et `detail` est à remplacer par le **coloris cible**. Les images produites **remplacent** celles de même nom dans `livraisons/visuels-final-2026-09-15/`. Écris-les dans le dossier du lot V2 ; Claude Code fera l'assemblage.

| Handle | Pid | Couleur actuelle (non vendable) | Coloris cible | Référence couleur | Slots (même famille qu'au lot d'origine) |
|---|---|---|---|---|---|
| fauteuil-relax-manuel | 1005008598267746 | noir (rupture) | Blanc cassé | `couleurs/blanc-casse.jpg` | face · salon · reglages · matiere · detail |
| rocking-chair-moderne-inclinable | 1005012105192978 | beige (rupture) | Bleu | `couleurs/bleu.jpg` | face · soir · usage · matiere · detail |
| fauteuil-a-bascule-allaitement-teddy | 1005010201578018 | beige (rupture) | Gris clair | `couleurs/gris-clair.jpg` | face · nuit · salon · matiere · detail |
| fauteuil-a-bascule-bois-massif | 1005012803890256 | beige (rupture) | Gris | `couleurs/gris.jpg` | face · nuit · salon · matiere · detail |
| chaise-rocking-chair | 1005010240771968 | teddy blanc (non vendu) | Lin beige | `couleurs/lin-beige.jpg` | face · nuit · salon · matiere · detail |
| chaise-qui-se-balance | 1005012653961063 | beige (non vendu) | Gris clair | `couleurs/gris-clair.jpg` | face · nuit · salon · matiere · detail |

Scènes et règles de chaque slot : `BRIEF-VISUELS-CODEX-LOTS-2-5-2026-09-15.md` §2. Reprends la composition de l'image actuelle du même slot, en changeant la couleur.

Si le lot V2 est traité, les images `couleur` du lot V1 pour ces mêmes coloris (`fauteuil-relax-manuel-couleur-blanc-casse`, `rocking-chair-moderne-inclinable-couleur-bleu`, `fauteuil-a-bascule-allaitement-teddy-couleur-gris-clair`, `fauteuil-a-bascule-bois-massif-couleur-gris`, `chaise-rocking-chair-couleur-lin-beige`, `chaise-qui-se-balance-couleur-gris-clair`) doivent être cohérentes avec le nouveau `face` : même pièce et même lumière.

## 3. QA et livraison
- **Planche par fiche** : `qa/controle-<handle>.jpg`, avec l'image `face` existante, la photo fournisseur du coloris et l'image livrée côte à côte.
  - **Contrôle obligatoire** : la teinte livrée correspond à la photo du coloris, pas à celle de la face.
- **Zoom** sur les zones où un logo ou un texte peut réapparaître (étiquette, poche, emballage de la housse).
- **Rejet propre** dans `rejected/` avec motif. Au-delà de 3 régénérations, déclare le sujet dans `sujets_difficiles`.
- **Livraison** :
  - dossier `payload.sortie.dossier` de chaque ordre ;
  - `manifeste-realise.json` ;
  - enveloppe de résultat dans `ordres/pour-codex/resultats/<nom de l'ordre>.json`.

## 4. Règle pour les prochains produits (lot 2 du catalogue)
À partir de maintenant, toute fiche à plusieurs coloris reçoit, en plus des slots de sa famille, **un slot `couleur` par coloris en stock** (hors coloris déjà montré par `face`). Le coloris de la galerie (`01.jpg`) doit être **un coloris en stock et vendu dans la fiche**. Sinon, la galerie se génère dans le premier coloris en stock.
