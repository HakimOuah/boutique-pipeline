# Brief pour Codex (app) — visuels Sous Abri, 09/09/2026

À coller tel quel dans Codex, ouvert sur le dépôt `boutique-pipeline` (racine du dépôt).

---

Tu es l'exécutant d'images du parc (instructions permanentes : `docs/codex-handoff/15-CODEX-EXECUTANT-IMAGES.md`, à lire en entier avant tout). Tu n'as aucun accès à la boutique. Tu lis les ordres, tu génères des images sur le disque, tu livres selon la spec §6.

Mission : traiter les trois ordres `generate_images` présents dans `ordres/pour-codex/inbox/` pour la boutique Sous Abri, dans cet ordre :
1. `20260909-2345-generate_images-sousabri-lot1c-hero.json` (1 image : le hero de l'accueil)
2. `20260909-2310-generate_images-sousabri-lot3-devis-guides.json` (9 images : 3 pages sur devis × face + situation, 3 visuels de guides)
3. `20260909-2305-generate_images-sousabri-lot2-galeries.json` (50 images : 10 produits × face, situation, detail-structure, montage, ancrage)

Avant de générer : lis `boutique-carport/BRIEF-VISUELS-CODEX-2026-09-09.md` en entier (vérité produit par source §1, direction artistique validée par Hakim §2, bloc d'orientation à copier dans chaque prompt §2 bis, formats §3, QA §4, livraison §5) et `boutique-carport/shot-list.md` (un prompt rédigé par image, à reprendre comme base). Les sources sont dans `boutique-carport/assets/source/<id AliExpress>/` (index : `assets/source/index.json`). Le lot 1 déjà livré dans `boutique-carport/livraisons/visuels-lot1-2026-09-09/` (6 images validées par Hakim) montre le rendu attendu : `sousabri-famille-devis.jpg` et `sousabri-douleur-grele.jpg` sont les références de style.

Règles qui ont fait échouer les essais précédents, à respecter absolument :
- Même nombre de poteaux que la source, disposés comme sur la source (le carport cintré 2 pieds ONE ALU a trois poteaux alignés d'un seul côté ; le carport alu autoportant 1005009961706626 a quatre poteaux : compter avant de livrer).
- Aucun emblème, logo, plaque ou lettrage sur les voitures, les structures, les bâches ; aucun texte dans l'image.
- Les tentes montrées par le fournisseur en tente de réception se livrent en garage (voiture ou utilitaire dessous).
- Pas de neige portée par une bâche, pas de grêle qui rebondit sur une toile.
- Image rejetée = dans `rejected/` avec motif ; jamais une image douteuse livrée en silence.

Livraison : dossiers `payload.sortie.dossier` de chaque ordre, manifeste `manifeste.json` (ou `manifeste-1c.json` pour le hero) indexé handle + sku + slot, enveloppe de résultat dans `ordres/pour-codex/resultats/<nom de l'ordre>.json` (statut, manifeste réalisé, rejets, sujets difficiles). Un ordre déjà présent dans `resultats/` ne se retraite pas. Quand tu as fini un lot, écris son enveloppe avant de passer au suivant.

## Reprise du 10/09 (après les lots 2 et 3)

Bilan Codex : lot 2 = 43/50 livrés, lot 3 = 4/9. Rejets légitimes (plaques ou emblèmes sur les voitures, ossatures au mauvais nombre de montants, géométrie non sourcée). Les visuels des pages devis toit plat et adossé sont impossibles avec les sources actuelles (rendus Star Alu à toit cintré) : il faut des photos fournisseur des vrais modèles (voir `QUESTIONS-FOURNISSEUR.md`), pas de génération.

Ordre de reprise à faire tourner dans l'app Codex : `ordres/pour-codex/inbox/20260910-0040-generate_images-sousabri-lot2b-reprises.json` (8 visuels : 7 slots du lot 2 + guide-comparatif, contraintes renforcées : plus aucun véhicule dans les slots concernés, compte des portiques écrit dans la QA). Sortie attendue : `boutique-carport/livraisons/visuels-lot2b-2026-09-10/`.

## Lot 4 — réalisme (10/09, après retour de Hakim)

Décision : plus aucune image sur fond studio ; tout doit ressembler à une vraie photo prise sur place (DA §2 mise à jour, prompts de la shot-list réécrits). Ordre : `ordres/pour-codex/inbox/20260910-0210-generate_images-sousabri-lot4-realisme.json` (17 visuels : 10 faces produit, 2 cartes famille, face du devis cintré, 4 montages de tentes 4x6 avec des scènes imposées différentes). Les fichiers gardent les mêmes noms et remplacent les précédents. Sortie : `boutique-carport/livraisons/visuels-lot4-2026-09-10/`. Après livraison : remplacement des médias correspondants dans Shopify (première image de chaque fiche, cartes famille de l'accueil, page devis cintré).
