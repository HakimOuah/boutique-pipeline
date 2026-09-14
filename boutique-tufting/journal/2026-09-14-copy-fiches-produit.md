# Copy des 5 fiches principales — 14/09/2026

Validé par Hakim le 14/09 (ton « vendeur, expert, rassurant », tutoiement conservé, neutre en genre).
Écrit dans l'admin Shopify (éditeur HTML de la description), puis contrôlé sur la boutique publique :
`/products/<handle>.json` identique au fichier `.apres.html` pour les cinq.

| Fiche | ID | Avant | Après |
|---|---|---|---|
| Kit Tufting Complet | 15466411688321 | 2067 | 1610 |
| Tufting gun 2-en-1 | 15466410213761 | 726 | 960 |
| Ciseaux électriques | 15466411458945 | 941 | 697 |
| Toile premium polyester | 15466411590017 | 393 | 552 |
| Miroir acrylique | 15466414408065 | 398 | 459 |

Sauvegardes avant/après : [`shopify/backups/2026-09-14-copy-fiches/`](../shopify/backups/2026-09-14-copy-fiches/).

## Pourquoi

Diagnostic du 10/09 (Ads 11/08–09/09) : Kit 44 visites / 0 ajout panier, ciseaux 28 / 0, toile 22 / 0.
Accroche confessionnelle, texte genré au féminin, rétractation Makita en plein argumentaire.

## Ce qui a changé

- Kit : accroche bénéfice (« trois gestes »), neutre en genre, clôture = formule de délai de REGLES.md
  (« Livraison offerte en France en 6 à 10 jours ouvrés, suivi par e-mail »).
- Gun : répond à « pourquoi pas le kit ? » ; renvoi vers le kit. « Même pistolet que le kit » :
  source = `shopify/dsers-switch-gun-2026-07-21.md` (fiche Urban Corners, base du kit).
- Ciseaux : compatibilité Makita **retirée** (plutôt que prudencée) ; specs gardées avec attribution
  (« Caractéristiques annoncées »), conformément à l'audit du 16/08 ; « Expédiés depuis un entrepôt en
  Allemagne » maintenu (origine documentée, REGLES.md).
- Toile, miroir : structure conservée (deux puces courtes en tête), texte étoffé sans nouvelle allégation.

Affirmations ajoutées par erreur dans la première proposition puis retirées avant écriture :
« sans rien démonter » (cut/loop), « au bout de deux heures », « sans laisser de trace ni fragiliser la
trame », « sans gabarit », « ne casse pas si tu le fais tomber », « pas d'attente longue, pas de frais
de douane », « attaquer les poils longs sans forcer ».

## Bloc « Ce que contient » du kit — copie de thème préparée

| | |
|---|---|
| Source | MAIN `190113350017` « Tuftéo 2 » |
| Copie | **`190353080705`** « Tuftéo 2 — bloc kit 14-09 » (UNPUBLISHED, `themeDuplicate`) |
| Preview | https://tufteo.com/products/kit-tufting-complet?preview_theme_id=190353080705 |

- `templates/product.json` : ligne `<p class="tuf-compo-note">Contenu annoncé par le fournisseur.</p>`
  retirée du `custom_liquid` du bloc `composition` (seul chemin JSON modifié, contrôlé par diff
  sémantique). Écrit par staged upload + `themeFilesUpsert` (retour `upsertedThemeFiles: []`, faux
  négatif) ; empreinte copie = fichier envoyé `8f1e94783d1137c5055d5bce880cdcf1` ; MAIN inchangé
  `679ef7c78663459ccc31510b6a85f9c6`. Preview : note 0 (live 1), bloc toujours rendu.
- Fichiers : [`shopify/backups/2026-09-14-bloc-kit/`](../shopify/backups/2026-09-14-bloc-kit/)
  (l'API renvoie le template indenté ; Shopify le stocke minifié, d'où 66 565 vs 109 757 octets).
- **« Petit outillage (sans malette) » ne vient pas du thème** : métachamp de variante
  `custom.composition` (variante 55953035297153, `gid://shopify/Metafield/200808784232833`).
  Correction = donnée produit, visible en ligne dès l'écriture, indépendamment de la publication.
  Proposition : « Petit outillage de réglage » (SET C : clés Allen, clé plate, enfile-aiguille,
  crochet — `journal/2026-07-22-kit-compositions-variantes.md`). Non écrite, en attente de Hakim.
- Publication de la copie : Hakim.

## Constat hors périmètre — thème en ligne

Le MAIN `190113350017` « Tuftéo 2 » est la copie « preview branding » du 03/09 marquée « ne pas
publier » (ETAT.md et TABLEAU.md la disent encore UNPUBLISHED). Constaté le 14/09 sur la fiche kit
servie sans cookie : « 789 avis », 3 badges « Vérifié », avis démo Manon/Julie/Chloé, barré 350 €
(`compare_at_price` catalogue). Aucune trace de décision de publication dans les dépôts. Bandeau
« Brouillon » retiré. Arbitrage conformité : Hakim. La copie `190353080705` hérite de ces éléments.

## Tracking (contexte)

Commande test #1005 du 10/09 : l'action Purchase est passée de « Mauvaise configuration » à « En attente
de conversions » (constaté le 14/09). Détails : mémoire `tracking-purchase-google-youtube-tufteo`.
