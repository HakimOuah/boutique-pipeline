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

## Reste ouvert (hors descriptions)

**Bloc « Ce que contient » du kit** : Liquid personnalisé en dur dans la section produit du thème
(`templates/product.json`, variant 55953035297153). Contient encore « Contenu annoncé par le
fournisseur. » et « Petit outillage (sans malette) ». Modification de thème : copie de travail puis
publication par Hakim (REGLES.md). Proposition : supprimer la note et remplacer la ligne par
« Outillage de réglage ».

## Tracking (contexte)

Commande test #1005 du 10/09 : l'action Purchase est passée de « Mauvaise configuration » à « En attente
de conversions » (constaté le 14/09). Détails : mémoire `tracking-purchase-google-youtube-tufteo`.
