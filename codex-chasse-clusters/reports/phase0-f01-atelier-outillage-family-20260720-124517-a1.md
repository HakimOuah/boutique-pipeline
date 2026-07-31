# Phase 0 Codex — Famille 1 · Atelier & outillage

- Run : `20260720-124517`
- Tentative : `a1`
- Date : 20 juillet 2026
- Base : SEMrush France (`db=fr`), devise EUR
- Graines traitées : `atelier`, `établi`, `outillage`, `servante atelier`
- Mode : mesure Codex indépendante, registre historique utilisé seulement après la mesure pour l'anti-doublon

## 1. Méthode

Lecture de Keyword Magic Tool en base France. Les accents, apostrophes et inversions manifestement équivalentes ne sont pas additionnés : le volume le plus élevé du même emplacement sémantique est conservé. Les marques, enseignes, occasion, prestations, lieux, établissements et requêtes informationnelles portant sur un autre objet sont exclus.

La phase 0 mesure des clusters ; elle ne prononce pas de verdict marché et ne consulte ni SERP Google, ni Shopping, ni AliExpress.

## 2. Clusters au-dessus du seuil brut prudent

### `f01-atelier-outillage-c01-servante-atelier`

| Emplacement sémantique | Mot-clé témoin retenu | Volume FR | CPC EUR | Notes |
|---|---|---:|---:|---|
| Générique | `servante d'atelier` | 22 200 | 0,32 | `servante d atelier` 9 900 et `servante atelier` 2 900 considérés comme variantes, non additionnés |
| Vide | `servante d'atelier vide` | 2 900 | 0,21 | Variantes orthographiques non additionnées |
| Complète | `servante d'atelier complete` | 2 400 | 0,33 | `pleine`, `avec outils` et variantes proches non additionnées |
| XXL | `servante d atelier xxl` | 320 | 0,37 | Segment distinct |
| Petite / mini | `mini servante d'atelier` | 170 | 0,28 | Variantes petite/mini non additionnées |
| Mécanicien | `servante d'atelier mecanicien` | 140 | 0,31 | Usage spécifique |

**Volume brut prudent : 28 130/mois.** Le cluster passe le seuil de 10 000 sans marques, enseignes ni occasion.

Pollution observée et exclue : Facom, KS Tools, Milwaukee, Stanley, Scheppach, Kraftmuller, Magnusson ; Leroy Merlin, Brico Dépôt, Castorama, Lidl et Amazon ; occasion ; mousse/accessoires.

### `f01-atelier-outillage-c02-etabli`

| Emplacement sémantique | Mot-clé témoin retenu | Volume FR | CPC EUR | Notes |
|---|---|---:|---:|---|
| Générique | `établi` | 5 400 | 0,43 | `un établi` et formes génériques proches non additionnés |
| Pliant / pliable | `établi pliante` | 4 400 | 0,14 | `établi pliant` 1 600 et `établi pliable` 720 non additionnés |
| Garage | `établi garage` | 1 900 | 0,28 | `établi pour garage` 1 900 non additionné |
| Bricolage | `établi bricolage` | 1 300 | 0,25 | `établi pour bricoler` 1 000 non additionné |
| Atelier | `établi atelier` | 1 000 | 0,67 | Usage commercial clair |
| Bois | `établi bois` | 1 000 | 0,39 | `établi en bois` 720 non additionné |

**Volume brut prudent : 15 000/mois.** Le cluster passe le seuil.

Pollution observée et exclue : `établissement`, scolaire, santé, Google Business, conjugaison, lieux, restaurants et `l'établi` ambigu ; marque Bosch.

## 3. Clusters sous le seuil ou non clusterables

| Cluster | Volume mesuré | Décision phase 0 |
|---|---:|---|
| Outillage carreleur / carrelage | 8 300 | Sous seuil : 2 400 + 2 400 + 1 900 + 1 600 ; assortiment métier, pas objet unique |
| Outillage électroportatif | 2 900 | Sous seuil : 1 600 + pack 1 300 |
| Outillage jardin | 3 160 environ | Sous seuil et relève de la famille jardin |
| Outillage générique | 9 900 sur la tête | Sous seuil et catégorie hétérogène ; vocabulaire dominé par marques, magasins et enseignes |
| Outillage frigoriste | 880 | Poche à re-mesurer dans un univers métier ; CPC 1,72 EUR, mais aucun cluster supérieur au seuil ici |

## 4. Anti-doublon appliqué après mesure

Le registre historique ferme les deux clusters survivants :

- servante d'atelier : déjà dérivée et rejetée en phase 2 le 20 juillet 2026 pour domination de Facom/KS Tools/Stanley et des enseignes généralistes ;
- établi : déjà dérivé et rejeté en phase 2 le 20 juillet 2026 pour domination de Wolfcraft et des enseignes généralistes.

Aucune reprise motivée n'a été demandée. Les clusters ne vont donc pas en sonde prix dans le run Codex.

## 5. Graines dérivées

- `outillage frigoriste` : poche déjà présente dans le vivier historique ; ne pas compter comme nouveau signal.
- Aucune autre graine dérivée autorisée : les segments visibles sont des variantes des deux clusters fermés ou relèvent d'autres familles déjà listées.

## 6. OBSERVÉ / MANQUANT / HYPOTHÈSE

### OBSERVÉ

- Session SEMrush active, base France, devise EUR.
- Volumes, CPC, intentions et densité concurrentielle visibles au 20 juillet 2026.
- Les deux clusters dépassent 10 000 avec une méthode prudente.
- Les deux usages sont déjà fermés dans le registre central.

### MANQUANT

- Aucun nettoyage SERP, prix Shopping ou fournisseur : volontairement non exécutés après l'anti-doublon.

### HYPOTHÈSE

- Aucune hypothèse utilisée pour franchir le seuil.

## 7. Gate

Phase 0 conforme. Deux clusters mesurés au-dessus du seuil, puis fermés par anti-doublon historique. Famille Codex `EXHAUSTED`, zéro candidat nouveau.

