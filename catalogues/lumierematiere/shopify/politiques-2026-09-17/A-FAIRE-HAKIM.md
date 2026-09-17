# À faire par Hakim — Lumière Matière, 17/09/2026

Le connecteur Shopify refuse ces trois opérations. Tout le reste est déjà en ligne.

## 1. Coller les 5 politiques (≈ 5 min)

**Paramètres → Politiques.** Pour chacune : ouvrir, cliquer sur l'icône `<>` (afficher le HTML),
tout sélectionner, coller le fichier, enregistrer.

| Politique Shopify | Fichier |
|---|---|
| Politique d'expédition | `1-expedition.html` |
| Politique de remboursement | `2-remboursement.html` |
| Conditions d'utilisation (CGV) | `3-cgv.html` |
| Politique de confidentialité | `4-confidentialite.html` |
| Coordonnées | `5-coordonnees.html` |

Ce qui change : l'origine Chine dite en clair, l'adresse de retour en France et son coût, plus de
« contrôle / emballage », plus de Colissimo / DPD, plus de « l'équipe répond de Paris », les
fabricants partenaires hors UE dans la confidentialité, Maestro retiré, les visuels déclarés comme
mises en scène, 10 h au lieu de 9 h et le `mailto:contact@ohventures.fr` caché supprimé.

## 2. Publier le thème `LM Véracité 2026-09-17` (≈ 1 min)

**Boutique en ligne → Thèmes → `LM Véracité 2026-09-17` → Publier.**
Aperçu avant : `https://lumierematiere.fr/?preview_theme_id=187309752656`

C'est une copie du thème en ligne du 17/09, avec seulement ces changements :
- home : bloc « Ce qu'on regarde avant de mettre une pièce en ligne » → « Ce que chaque fiche vous
  donne », 3 icônes `verified` remplacées, phrase « la texture que vous voyez en photo » supprimée,
  « pierre » → « effet pierre », « osier » retiré ;
- panier : origine Chine, retour vers la France, plus de « contrôle du colis » ;
- footer : origine Chine dans le bloc livraison, « OH Ventures » devant l'adresse ;
- fiches (accordéon Livraison) : origine Chine, retour vers la France.

## 3. Dépublier 2 collections (≈ 1 min) — 4 sur 6 sont déjà faites

**Dépublier une collection ne sort aucun produit du catalogue.** Les fiches restent publiées et
restent dans leurs autres collections ; c'est la page de collection qui disparaît. Le nombre
affiché dans la colonne de l'admin compte aussi les brouillons — d'où l'écart avec ce qu'un
visiteur voit.

| Collection | Admin | Visible en visiteur | État |
|---|---|---|---|
| Lustres pampilles | 7 | **0** | ✅ déjà dépubliée |
| Lustres statement | 1 | **0** | ✅ déjà dépubliée |
| Suspensions modernes | 1 | **0** | ✅ déjà dépubliée |
| Suspensions papier | 1 | **0** | ✅ déjà dépubliée |
| Grandes suspensions XXL | 15 | **1** | à dépublier — 14 des 15 sont en brouillon |
| Suspensions osier | 5 | **2** | à dépublier — les 2 fiches visibles sont du rotin |

**Produits → Collections → [collection] → Disponibilité des ventes → décocher Boutique en ligne
et Google & YouTube.**

À décider : **Plafonniers cuisine** (2 fiches visibles, hors menu, description corrigée). Elle ne
mentait plus après la passe du 17/09 — on peut la laisser.

## 4. Ensuite

- **Pas de campagne**, pas de demande de réexamen avant d'avoir fait 1 à 3.
- Relancer le scan : `python3 .claude/skills/gmc-acceptance/scripts/scan_veracite.py https://lumierematiere.fr --email contact@lumierematiere.fr` → viser **0 bloquant**.
- **Commande test** : seule preuve de la matière des appliques (pierre ou résine ?), de l'ampoule de
  `829449` et du délai réel.
- **DEEE** : OH Ventures doit être enregistrée auprès d'un éco-organisme (Ecosystem) pour vendre des
  luminaires ; l'éco-participation s'affiche ensuite. Non écrit sur le site tant que ce n'est pas fait.
- **Directeur de la publication** : les mentions légales doivent nommer une personne.
- Réexamen : une seule demande, dans la fenêtre indiquée par Google.
