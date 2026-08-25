# Remplacement de « Autour de 199 € » — lumierematiere.fr (26/08/2026)

Hakim n’aime pas l’approche prix. La collection mentait déjà après l’alignement
Lustria : 12 fiches sous 179 € (3 à 129, 1 à 149, 8 à 169).

## Remplacement

**« Pour le salon »**, branché sur la collection existante `suspensions-salon`
(29 fiches, mot-clé 4 080/mois, déjà dans le menu « Par pièce »).

Pourquoi celle-là, et pas une autre sélection prix ou un « coups de cœur » :

- même axe que Lustria (la pièce porte 2,8× le trafic de la matière) ;
- déjà SEO-complète, déjà peuplée, déjà dans le menu ;
- la grille sous le panier propose une pièce à vivre, pas un palier.

## Écrit

| Surface | Avant | Après |
|---|---|---|
| Home, grille featured | Autour de 199 € / `selection-199` | Pour le salon / `suspensions-salon` |
| Home, CTA final | La sélection autour de 199 € | Voir les suspensions salon |
| `/cart`, reco 4 fiches | Autour de 199 € | Pour le salon |
| Collection `selection-199` | publiée | **dépubliée** |
| `/collections/selection-199` | 200 | **301** → `/collections/suspensions-salon` |

Vérifié en ligne : accueil sans « Autour de 199 » ni `selection-199` (1 « Pour le
salon », 2 CTA, 4 liens `suspensions-salon`). Ancienne URL en 301. Nouvelle
page en 200.

Sous-titre de la grille : « Les suspensions qui tiennent une pièce à vivre.
Bambou, rotin, verre, pierre ou métal, choisis pour le salon. »

## Scripts alignés

`apply_fullstack.py`, `patch_home.py`, `patch_cart.py`, `humanise_theme.py`,
`import_catalogue.py` (plus de création ni de rattachement auto),
`collections-seo.json` (entrée `selection-199` retirée pour qu’un rerun SEO
ne réécrive pas l’ancien texte). Script de passe : `replace_selection_199.py`.
Backup `backups/2026-08-26-selection-salon/`.

La collection reste dans Shopify et dans `state.json`, hors vitrine. Rien
n’a été supprimé.
