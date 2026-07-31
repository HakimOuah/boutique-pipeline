# Phase 0 Codex — Famille 4 · Auto / moto atelier & diagnostic

- Run : `20260720-124517`
- Tentative : `a1`
- Date : 20 juillet 2026
- Base : SEMrush France (`db=fr`), EUR
- Graines : `diagnostic auto`, `atelier moto`, `outil garage`, `valise diagnostic`
- Graine dérivée traitée : `bequille atelier moto` (profondeur 1)

## 1. Méthode

Lecture du Keyword Magic Tool en base France. Les accents, pluriels, inversions et formulations quasi équivalentes ne sont pas additionnés lorsqu'ils occupent le même emplacement sémantique. Les services de garage, recherches locales, marques, enseignes, logiciels, accessoires et intentions portant sur un autre objet sont exclus. Le registre historique est consulté après la mesure pour empêcher la réouverture d'un dossier déjà tranché sans nouvelle condition de reprise.

## 2. Cluster au-dessus du seuil

### `f04-auto-moto-diagnostic-c01-valise-diagnostic`

Cluster : valise, boîtier ou tablette de diagnostic automobile multimarque.

| Requête distincte | Volume FR | CPC EUR | Statut de comptage |
|---|---:|---:|---|
| `valise diagnostic` | 8 100 | 0,47 | Retenue comme tête générique ; les têtes `auto`, `voiture`, `automobile`, accents et inversions ne sont pas ajoutées |
| `valise diagnostic auto multimarque professionnelle` | 2 400 | 0,41 | Retenue comme besoin professionnel/multimarque distinct |
| `meilleur valise diagnostic auto multimarque professionnelle` | 1 300 | 0,28 | Retenue comme intention comparative commerciale distincte |
| `boitier diagnostic auto` | 720 | 0,26 | Retenue comme forme produit distincte |
| `appareil diagnostic auto` | 590 | 0,37 | Retenue comme formulation produit distincte |
| `tablette diagnostic auto` | 320 | 0,50 | Retenue comme segment tablette distinct |

**Volume brut prudent : 13 430 recherches/mois.** Les formulations proches non ajoutées incluent notamment `valise diagnostic auto` (5 400), `valise diagnostic voiture` (3 600), `valise diagnostique auto` (2 400), `valise de diagnostic` (1 900), `diagnostic auto valise` (1 600) et les variantes de marque.

### Fermeture par anti-doublon historique

Ce cluster correspond au dossier canonique `Valise OBD2 bidirectionnelle`, déjà rejeté dans `../../registre-candidats.md`. Le dernier verdict de référence indique un KINGBOLEN S6 à 175 EUR rendu France, trop proche du prix public européen du même modèle. Le rapport historique `../../reports/validation-microscope-obd2-2026-07-16.md` précise que le coût devait descendre durablement sous environ 110–120 EUR, ou qu'un bundle/dispositif de distribution réellement non comparable devait être obtenu avant reprise.

Le volume est donc confirmé indépendamment par Codex, mais aucune nouvelle condition de reprise n'est observée. Le cluster est fermé sans nouvelle sonde fournisseur et ne devient pas un nouveau candidat.

## 3. Clusters sous le seuil ou hors périmètre

### Béquille d'atelier moto

La tête `bequille atelier moto` atteint 3 600/mois. `bequille moto atelier` (2 400), les variantes accentuées et `béquille d'atelier moto` occupent le même emplacement sémantique et ne sont pas additionnées. Les sous-besoins réellement distincts visibles — avant (210), monobras (90), avant/arrière et supports — maintiennent le plancher prudent très loin de 10 000/mois.

**Décision : sous seuil.** La forte concurrence publicitaire (`Con.` 1,00 sur la tête) ne compense pas le manque de demande adressable.

### Rangement et outils de garage

Les premières têtes observées sont `rangement outils garage` (590), `ranger outil garage` (590), `garage rangement outils` (480), puis `outil garage` (140). Le reste mélange idées de rangement, services, logiciels et accessoires low-ticket.

**Décision : sous seuil et intention trop diffuse.**

### Atelier moto générique

La tête `atelier moto` (1 300 ; CPC 1,75 EUR) désigne principalement des ateliers, réparateurs et recherches locales. Le vocabulaire produit significatif remonte presque exclusivement vers la béquille d'atelier, déjà traitée sous le seuil.

**Décision : hors cluster produit adressable.**

## 4. Graines dérivées

- `bequille atelier moto` : traitée à profondeur 1 ; sous seuil prudent.
- Les variantes de valise diagnostic ne sont pas réexpansées, car elles appartiennent au dossier historique fermé.

## 5. OBSERVÉ / MANQUANT / HYPOTHÈSE

### OBSERVÉ

- Base SEMrush France et devise EUR actives.
- Cluster valise diagnostic à 13 430/mois bruts prudents.
- CPC de 0,28 à 0,50 EUR sur les requêtes comptées et densité publicitaire généralement maximale.
- Dossier économique OBD2 déjà fermé dans la source de vérité historique.
- Béquille moto et rangement garage sous le seuil de 10 000/mois après déduplication.

### MANQUANT

- Aucun nouveau coût fournisseur, prix livré ou délai n'est mesuré : l'anti-doublon ferme la valise avant sourcing.
- Aucune preuve de baisse durable du coût OBD2 sous 110–120 EUR ni de bundle non comparable n'est disponible.

### HYPOTHÈSE

- Aucune hypothèse utilisée pour franchir un seuil ou changer un verdict.

## 6. Gate

Famille épuisée. Un cluster franchit le seuil de volume mais est fermé par anti-doublon économique historique ; aucun nouveau candidat Codex ne continue vers le sourcing.
