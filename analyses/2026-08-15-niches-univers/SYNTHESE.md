# Synthèse — analyse des 6 niches univers

**15/08/2026.** Six univers apportés par Hakim, analysés en mode Kraken `catalogue-volume`
(plancher 30 000 recherches commerciales nettoyées France, confort 40 000, 200 concepts produits,
ratio prix/CPC ≥ 100). Deux moteurs ont travaillé : **Codex** (lot complet, run `20260815-181328`)
puis **Claude** (reprise ciblée sur ce que la mesure Codex n'avait pas couvert). Ce document est le
verdict consolidé des deux.

---

## Le tableau de décision

| | Univers | Volume net vérifié | Concurrence | Sourcing | Statut |
|---|---|---|---|---|---|
| **U1** | Parure de lit | ✅ passe largement (`housse de couette` 60 500 seule) | ❌ 10 acteurs couvrent les angles génériques | non instruit | **STOP droit de gagner** |
| **U2** | Bouillottes | ~42 600 provisoire | à instruire | ⚠️ **bloqué par l'outil, pas par le marché** | **En suspens** |
| **U3** | Globe & cartographie | ✅ **66 550 vérifiés en SERP** (2,2× le plancher) | ✅ **favorable** — Amazon 1 position par page, indépendants au cœur | ❌ **59 concepts sur 200** | **GO marché, sourcing insuffisant** |
| **U4a** | Télescopes | — | ❌ marques, confiance technique, SAV | — | **STOP** |
| **U4b** | Déco astro | ❌ 24 830 (− 5 170) | non instruit | non instruit | **STOP volume** |
| **U5** | Gothique / emo | ❌ 26 453 après SERP (− 3 547) | ✅ **ouverte** — spécialistes absents des pages 1 | non instruit | **STOP volume, dossier vivant** |
| **U6** | Ésotérisme | ✅ 31 600 prudents | ❌ 10 acteurs couvrent catalogue, édition, curation | non instruit | **STOP droit de gagner** |

**Aucun univers ne ressort en GO lancement.** U3 est le seul à franchir toutes les portes marché, et
il échoue sur la profondeur fournisseur.

---

## U3 — le dossier qui va le plus loin, et pourquoi il s'arrête

**Ce qui est acquis :**
- **66 550 recherches nettes vérifiées en SERP** (80 960 consolidés − 14 410 retirés, soit −17,8 %).
- Une **structure concurrentielle favorable** : Amazon présent sur 11 pages 1 sur 14 mais **toujours
  avec une seule position** ; le cœur appartient à de petits indépendants (`originalmap.fr`,
  `cartovia.com`, `pappus-editions.com`). Un seul des neuf sites de veille apparaît.
- Une **économie saine sur le globe** : 44,90 € → marge contributive **26,35 € (58,7 %)**, ROAS
  break-even **1,70**, ratio prix/CPC **249** (cible 150-200), taux de conversion de rupture 0,70 %.

**Ce qui le bloque — et c'est un retournement :**

> **Les familles les mieux notées par Google sont les moins fournies par AliExpress.**

- **59 concepts produits observés contre 200 exigés.**
- **Globe-bar** (la plus haute bande, ~214 €) : 2 références, **0 vente, 0 note**.
- **Carte du monde en bois** (meilleure marge du dossier, 48,9 %) : une seule référence à prix de
  dropship, **3 ventes** ; tout le reste à 320-955 € sans aucune vente.
- **Carte à gratter** : avec le seul fournisseur qui vend réellement (17,19 €), la marge passe à
  **− 1,14 €**. Le palier haut ne tient pas non plus : globe-bar à 199 € rend 9,9 % et un ROAS
  break-even de 10,10.

Trois familles tiennent en `FOURNISSEUR À TESTER` : globe terrestre (24 concepts, 4 vendeurs pivots
≥ 96 %), carte murale (60/60 pertinents), liège (sous réserve : 5 références sur 7 sont la même
marque).

**Deux risques à ne pas perdre de vue :**
- **Aucun globe en français observé sur 58 cartes fournisseur**, alors que la demande mesurée est
  française. C'est un problème d'offre, pas de traduction de fiche.
- Des **cartes « terre plate » sont présentes et vendues** au catalogue fournisseur (une à 114
  ventes) — risque Merchant Center direct si elles entrent au feed.

**Verdict : `GO_CONDITIONNEL` économique, à quatre conditions** — recentrer sur le globe seul (43 %
du volume, seul dossier sain de bout en bout), mesurer le fret via DSers, résoudre la langue,
mesurer la saisonnalité.

---

## Ce que la reprise a corrigé chez Codex

Codex avait mesuré **4 à 11 requêtes par univers** et additionné les têtes. La consolidation par
famille (étape 3 de `METHODE-ANALYSE-MARCHE.md`) change les ordres de grandeur :

| Univers | Codex | Après consolidation | |
|---|---|---|---|
| U3 | 22 870 → STOP | **80 960**, puis 66 550 vérifiés | **×2,9** |
| U5 | 4 120 → STOP | **22 120**, puis 26 453 avec SERP | **×6,4** |
| U4b | 12 000 → STOP | **24 830** | ×2,1 |

Sur U3, **les 7 130 manquants sont comblés 11 fois sans une seule graine nouvelle** : il a suffi de
consolider les cinq formulations que Codex avait lui-même retenues (`carte du monde à gratter`
1 900 → 8 400 ; `en bois` 1 600 → 5 490 ; `murale` 590 → 3 370 ; `poster` 590 → 2 730 ; `mappemonde`
12 100 → 23 800). C'est le phénomène Noirmont à l'identique.

**Deux erreurs de comptage corrigées dans l'autre sens**, à porter au crédit de la reprise :
- U4b : les 12 000 de Codex contenaient `planétarium` 6 600, dont **38 400 lignes sont des villes,
  horaires et tarifs**. Sa base réelle valait **6 090**. Le produit « planétarium de bureau » pèse
  690.
- U3 : la somme des six chiffres publiés par Codex fait **16 870, pas 22 870**, et son « noyau
  prudent de 21 600 » n'est explicité nulle part. Ces nombres ne sont pas reproductibles — c'est le
  piège n° 8 de la méthode.

**Et une conclusion de Codex invalidée** : son U2 fermé sur « 30 résultats AliExpress, 0 pertinent »
utilisait des requêtes en **mots fréquents**, mode d'échec documenté de l'API. Retesté ce soir :
6 requêtes, 33 résultats, 0 pertinent, uniquement des pulvérisateurs d'huile et des gourdes de vélo.
**Ce 0/30 mesure une limite d'outil, pas une absence de fournisseur.** U2 n'a pas de verdict sourcing.

---

## Ce que Codex avait raison de dire, et qui tient

- **U1 et U6 sont des STOP de droit de gagner, pas de volume.** Remesurer ne les rouvre pas : il
  faudrait une sous-intention mal servie ou un avantage propriétaire.
- **`carte du monde` 301 000 et `planisphère` 27 100 sont bien à exclure.** La SERP le confirme :
  74 formulations sur 100 de `planisphère` sont scolaires, et `mappemonde` sert une page
  d'encyclopédie (7 positions non marchandes sur 9, une question suggérée sur les **mots fléchés**).
- **Un grand sitemap n'est pas de la demande.** Vérifié contre son propre exemple : les familles
  jamais mesurées du Petit Astronaute (1 769 URL) pèsent 390 en décoration murale, 190 en textile,
  650 en figurines. Sa mise en garde était juste.
- **Sa discipline de preuve** (observé / manquant / hypothèse, audit aveugle contre ses propres
  conclusions) est la bonne manière de travailler.

---

## Les trouvailles de méthode de la session

1. **Les variantes sans accent sont des lignes SEMrush distinctes.** `ciel etoile projecteur` 1 300
   est invisible depuis `ciel étoilé`. Deux requêtes ont rapporté 9 650 bruts et expliquent
   l'essentiel d'un ×8,4. **Tous nos totaux consolidés sont des planchers tant que la forme sans
   accent n'a pas été interrogée.** → versé en mémoire (`variantes-sans-accent-kmt`).
2. **`poster` est rabattu sur `poste`** par SEMrush, qui rend « La Poste espace client » sur 57 290
   de volume. Racine inutilisable telle quelle.
3. **`lampe demi lune`** n'est pas une lampe décorative mais une **lampe UV de manucure**.
4. **`gothiqua`** n'est pas une faute rabattue : c'est une jument de course et une police.
5. **Les compteurs de ventes des SERP AliExpress dépassent systématiquement l'API** (52 vs 14,
   434 vs 254) — confirmation du piège n° 7, l'API fait foi.

---

## Ce que je recommande

**U3 est le seul dossier à instruire davantage**, en le redimensionnant : pas une boutique catalogue
de 200 concepts, mais **une boutique globe** — 43 % du volume, économie saine, concurrence
d'indépendants. Les quatre conditions du `GO_CONDITIONNEL` sont à lever avant toute décision, et la
première est le fret : **tout le chiffrage est fret à 0 €**, aucune fiche n'a rendu poids ni
dimensions, sur des produits fragiles et volumineux.

**U5 mérite une décision de Hakim plutôt qu'un classement.** 26 453 contre un plancher de 30 000,
mais des pages 1 où `antregothique.com`, `castle-gothic.fr` et `vetement-gothique.fr` sont
**absents**, où Shein et Temu font 0/10 et Amazon 3/10 jamais en tête. Le format Kraken ne passe pas ;
une boutique plus petite n'a pas été évaluée. Deux ouvertures produit repérées : lingerie gothique,
costume de mariage gothique homme.

**U2 doit être rouvert par le bon canal** : le sourcing bouillotte se fait par noms de magasins ou à
l'étape DSers, pas par l'API `search`.

**Un candidat neuf est né de l'analyse** : « bijoux pierres naturelles et symboles », révélé par
Moment Ici (2 344 produits, médiane 39 €, 0,4 % sous 15 €). Il ne s'ajoute pas à U6 et n'a jamais été
mesuré.

---

## Ce qui n'a pas pu être mesuré

- **La saisonnalité, sur deux rapports d'affilée** : le widget Tendance SEMrush ne rend aucune
  donnée. L'hypothèse Q4 du globe reste une hypothèse, et elle conditionne la fenêtre de lancement.
- **Le fret, le poids et les dimensions** : aucun produit U3 n'en a rendu. Aucune fiche en confiance A.
- **Les annonces Search texte** : jamais isolables (le compteur ne voit que le Shopping). Aucune
  conclusion n'en est tirée.
- **U5** : les 22 120 des familles déjà mesurées n'ont pas été vérifiés en SERP. Le retrait sur
  Noirmont était de 24 500 sur 65 570 — le vrai adressable d'U5 peut encore baisser.
- **U3** : le sous-segment `enfant` (2 430) n'a pas eu sa requête propre alors que son voisinage est
  un rayon de jouet de marque. **66 550 est une borne haute.**
- **U4b** : trois planchers non percés, variantes sans accent explorées sur deux familles seulement.
- **U2 et U4b** : aucune vérification SERP.
