# Phase 0 Codex — Famille 5 · Impression 3D, découpe & gravure

- Run : `20260720-124517`
- Tentative : `a1`
- Date : 20 juillet 2026
- Base : SEMrush France (`db=fr`), EUR
- Graines : `imprimante 3d`, `graveur laser`, `découpe vinyle`, `cnc`
- Graine dérivée : `machine gravure laser` (profondeur 1)

## 1. Clusters au-dessus du seuil

### `f05-impression-decoupe-gravure-c01-imprimante-3d`

La requête cœur `imprimante 3d` porte à elle seule **74 000 recherches/mois**, intention commerciale, CPC 0,16 EUR et concurrence publicitaire 1,00. Le seuil est franchi sans additionner fichiers, logiciels, filaments, maisons imprimées ni marques.

Sous-besoins observés, non nécessaires au franchissement : `imprimante 3d prix` 4 400 ; `imprimante 3d résine` 3 600 ; `imprimante 3d débutant` 1 600 ; `imprimante 3d professionnelle` 1 600 ; `meilleur imprimante 3d` 1 600 ; `imprimante 3d grand format` 1 000 ; `comparatif imprimante 3d` 720 ; `imprimante 3d multi couleur` 720.

**Plancher prudent retenu : 74 000/mois.**

### `f05-impression-decoupe-gravure-c02-graveur-laser`

Le contrôle courant retrouve les valeurs du dossier SEMrush canonique du 17 juillet : `graveur laser` 4 400 ; `graveur laser bois` 1 900 ; `laser graveur` 1 900 ; `graveur laser pour bois` 720 ; `machine gravure laser` 880 ; `graveur découpeur laser` 260 ; `graveur laser 20w` 210 ; `graveur découpe laser` 170 ; `graveur laser 10w` 140.

Le nettoyage détaillé déjà inscrit dans `../../reports/validation-semrush-2026-07-17.md` fixe le cluster générique bois/diode hors métal, fibre, CO2 pro, marques et mini/portable à **12 000–14 100 recherches/mois**. Les valeurs principales sont reconfirmées dans cette reprise ; l'intervalle canonique est conservé sans reconstruire artificiellement la longue traîne. Le littéral `graveur laser fermé` reste historiquement à 20/mois.

## 2. Clusters sous le seuil

### Découpe vinyle

`découpe vinyle` 260 ; `découpeuse vinyle` 260 ; `découpe de vinyle` 170 ; `plotter de découpe vinyle` 140 ; `machine découpe vinyle adhésif` 90. Même avant déduplication et après exclusion des sols, disques vinyles et prestations, le cluster machine reste très loin de 10 000.

### CNC de bureau / bois

La tête `cnc` (22 200) est inexploitable : acronyme massivement pollué par organismes, contenus adultes, emplois, usinage et requêtes anglophones. Le vocabulaire machine observé — `cnc machine` 2 900, `fraiseuse cnc` 1 300, `cnc bois` 880, `cnc routeur bois pro` 590, `cnc pour bois` 480, `gravure cnc` 480 et `cnc 3018` 390 — reste sous 10 000 même avec des termes de procédé discutables. Les inversions `machine cnc` et `3018 cnc` ne sont pas ajoutées.

## 3. Graines dérivées

- `machine gravure laser` : traitée, confirme le cluster graveur.
- Aucune expansion vinyle ou CNC : têtes produit trop éloignées du seuil.

## 4. OBSERVÉ / MANQUANT / HYPOTHÈSE

### OBSERVÉ

- Deux clusters au-dessus de 10 000 : imprimante 3D et graveur laser.
- Découpe vinyle et CNC de bureau sous seuil après nettoyage.
- Base France et EUR actives.

### MANQUANT

- Prix, comparabilité et sécurité à traiter dans les portes suivantes.

### HYPOTHÈSE

- Aucune hypothèse n'est utilisée pour faire passer l'imprimante 3D.
- Le graveur reprend l'intervalle SEMrush canonique du 17 juillet, explicitement signalé, après reconfirmation des principales lignes actuelles.

## 5. Gate

Deux clusters continuent vers la sonde prix et le filtre qualitatif : imprimante 3D et graveur laser.
