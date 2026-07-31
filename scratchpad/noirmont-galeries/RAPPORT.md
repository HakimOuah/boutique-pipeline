# Rapport de livraison — galeries Maison Noirmont

Date : 26 juillet 2026  
Feuille de route : `audit-visuel-catalogue.md`, version 3.

## Produit

- **90 fiches traitées** : 52 montres et 38 accessoires.
- **230 JPEG livrables**, tous en **2048 × 2048**, mode RGB, qualité cible 90.
- **156 images de montres** : 52 situations, 52 macros, 52 portés-poignet.
- **74 images d'accessoires** : 36 situations et 38 macros.
- **90 planches par fiche** et **15 vues d'ensemble** pour le contrôle visuel.
- Modèle : **GPT Image 2 natif**, en image-to-image depuis chaque face validée.

## Sources

- 41 faces déjà validées dans `visuels-2026-07-25/generated/`.
- 36 faces exportées depuis les URLs CDN publiques listées dans l'audit.
- 13 faces d'accessoires déjà disponibles localement.

## Régénérations

Trois fichiers ont demandé **une régénération chacun** :

- `doigtiers-d-horloger-latex-situation.jpg` — suppression de micro-gravures sur la pièce manipulée.
- `pince-a-barrettes-situation.jpg` — outil complet rendu visible et identifiable.
- `pince-a-barrettes-macro.jpg` — macro recentrée sur la charnière, le ressort et les mâchoires.

**Aucun fichier n'a demandé plus de trois régénérations.**

Les versions refusées sont conservées dans `rejected/`.

## Écarté

- `noirmont-deux-plongeuse-ceramique` — exclue par le prompt et l'audit v3 : ses 7 références ne sont pas identifiables avec fiabilité. Trois images avaient été générées avant la mise à jour concurrente de l'audit ; elles ont été retirées du livrable et conservées dans `excluded/`.
- `carte-cadeau-maison-noirmont` — visuel unique déjà conforme.
- Les 3 déclinaisons GMT « siglé » — marque tierce, variantes invendables, aucune fiche active à traiter.
- Les 7 fiches mères en brouillon — hors périmètre.
- Les cartes typographiques et médias hérités — aucune production, aucune modification.

## Sécurité et branchement

**Aucune connexion à Shopify et aucune écriture sur la boutique.**  
Le futur branchement doit suivre l'ordre `face` → `situation` → `macro` → `poignet` à partir du champ `slot` du manifeste, et faire la correspondance exclusivement par `handle` + `sku`.
