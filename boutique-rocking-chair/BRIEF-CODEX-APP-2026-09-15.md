# Brief pour Codex (app) — visuels Bercelou, production complète — 15/09/2026

À coller tel quel dans Codex, ouvert sur le dépôt `boutique-pipeline` (racine du dépôt).

---

Tu es l'exécutant d'images du parc. Tes instructions permanentes sont dans `docs/codex-handoff/15-CODEX-EXECUTANT-IMAGES.md` : lis-les en entier avant tout. Tu n'as aucun accès à la boutique. Tu lis les ordres, tu génères des images sur le disque et tu livres selon la spec §6.

**Mission** : produire tous les visuels de **Bercelou**, la boutique française de rocking chairs et de fauteuils à bascule. Hakim a validé le style « Veille douce » sur le lot test déjà livré dans `boutique-rocking-chair/livraisons/visuels-lot1-test-2026-09-14/`.

Traite les quatre ordres `generate_images` de `ordres/pour-codex/inbox/`, **dans cet ordre** :
1. `20260915-0200-generate_images-bercelou-lot2-allaitement-bascule.json` : 50 images, 10 fauteuils × face, nuit, salon, matière, détail.
2. `20260915-0300-generate_images-bercelou-lot3-design-exterieur-rotin.json` : 55 images, 11 fauteuils × face, soir, usage, matière, détail.
3. `20260915-0400-generate_images-bercelou-lot4-relax.json` : 55 images, 11 fauteuils × face, salon, réglages, matière, détail.
4. `20260915-0500-generate_images-bercelou-lot5-enfant-accessoires-pages.json` : 38 images. 2 produits enfant × 3, 4 accessoires × 3, 12 cartes de collection, 4 cartes « moment de vie » de l'accueil, 1 bandeau d'accueil et 3 bandeaux de guides.

**Avant de générer, lis en entier** :
- `boutique-rocking-chair/BRIEF-VISUELS-CODEX-2026-09-14.md` : direction artistique validée §2, bloc d'orientation §2 bis à copier dans chaque prompt, QA §4 ;
- `boutique-rocking-chair/BRIEF-VISUELS-CODEX-LOTS-2-5-2026-09-15.md` : vérité produit fiche par fiche §1, scènes par famille et formats §2, H1 et sources §3, visuels de pages §4, QA et livraison §5.

**Références de rendu à regarder** (lot test validé) : `fauteuil-a-bascule-allaitement-teddy-face.jpg`, `-nuit.jpg`, `-salon.jpg`, `fauteuil-allaitement-chambre-bebe-avec-repose-pieds-detail.jpg`, `fauteuil-a-bascule-scandinave-velours-cotele-matiere.jpg`.

Les photos fournisseur sont dans `boutique-rocking-chair/assets/source/<id AliExpress>/`.

**Règles à respecter absolument** :
- **Le fauteuil n'est jamais réinventé.** Même silhouette, même capitonnage, même base (patins bois ou métal, pied pivotant, trépied), même matière, même couleur que `01.jpg`. Seule la mise en scène change.
- **Avant chaque fiche**, écris `qa/verite-<handle>.md` d'après toutes les photos sources, puis compare avec le H1 du brief. Si les photos contredisent le H1, ne génère pas : rejette la fiche avec son motif.
- **Aucun texte, logo, étiquette, pictogramme, cote, badge ni tableau de personnage de dessin animé.** Les sources en contiennent beaucoup.
- **Lumière** de lampe ou de fin de journée, intérieurs et terrasses français ordinaires, réalisme photo : pas de rendu 3D lisse, pas de pièce de catalogue.
- **Personnes** de profil ou de dos, jamais de visage en gros plan, mains à 5 doigts.
- **Bébé** emmailloté uniquement sur les slots `nuit` du lot 2, allaitement pudique. Aucun bébé ni enfant sur les produits enfant.
- **Pièges connus** :
  - le rocking chair « avec repose-pieds » n'est pas pivotant ;
  - pour le coussin, seul le coussin est vendu (slot `face` sans panier) ;
  - relax : aucun élément médical, et position inclinée seulement si les sources la montrent.
- **Image douteuse** : dans `rejected/` avec son motif, jamais livrée en silence. Au-delà de 3 régénérations, déclare le sujet dans `sujets_difficiles`.

**Livraison** :
- dossier `payload.sortie.dossier` de chaque ordre ;
- manifeste `manifeste-realise.json` indexé `handle` + `sku` + `slot` ;
- planches `qa/controle-<handle>.jpg`, avec la source et les images livrées, vignettes ≥ 740 px ;
- enveloppe de résultat dans `ordres/pour-codex/resultats/<nom de l'ordre>.json` : statut, manifeste réalisé, rejets, sujets difficiles.

**Écris l'enveloppe d'un lot avant de passer au suivant.** Un ordre déjà présent dans `resultats/` ne se retraite pas.
