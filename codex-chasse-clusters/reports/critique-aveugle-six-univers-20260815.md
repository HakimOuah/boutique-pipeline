# Critique aveugle et hostile — décisions U1 à U5 et sourcing U2

- Date : **15/08/2026**
- Mode : revue contradictoire des preuves disponibles, lecture seule, **sans Chrome**
- Contrainte : aucun compteur d'avancement ni objectif final consulté
- Périmètre décisionnel : U1 à U5 et gate sourcing U2
- U6 : aucune décision ; checklist générique seulement, car l'analyse est encore en cours

## Conclusion hostile

Les décisions opérationnelles sont globalement conservatrices et défendables, mais plusieurs formulations doivent être resserrées pour ne pas transformer une absence de preuve en vérité universelle.

| Univers | Décision attaquée | Verdict contradictoire recommandé |
|---|---|---|
| U1 literie | STOP droit de gagner | **Maintenir `STOP_PHASE_2_DROIT_DE_GAGNER`**, mais limiter la portée à la boutique générique et aux angles étudiés. |
| U2 bouillottes — marché | Marché conditionnel | **Maintenir conditionnel, pas PASS marché définitif** : volume/page eligibility, AOV et sécurité restent à fermer. |
| U2 bouillottes — sourcing | 4 requêtes, 30 résultats, zéro exact | **`REPARER_AVANT_SOURCE_EXACTE`** ; zéro exact invalide la tentative, pas le marché fournisseur. |
| U3 cartographie | STOP à 22,87 k | **Maintenir `STOP_VOLUME_CATALOGUE_AU_PERIMETRE_MESURE`** ; ne pas appeler 22,87 k un plafond de toute cartographie. |
| U4a télescopes | STOP historique | **Maintenir `STOP_REPRISE_SANS_THESE_NOUVELLE`** ; ne pas le requalifier en STOP volume. |
| U4b déco astro | STOP à ≤12 k brut | **Maintenir `STOP_VOLUME_CATALOGUE_AU_PERIMETRE_MESURE`**, avec correction : 12 k est le maximum des quatre têtes mesurées, pas de tout l'univers déco astro. |
| U5 gothique/emo/démon | STOP à ≤4,12 k | **Maintenir `STOP_VOLUME_CATALOGUE_PERIMETRE_GOTHIQUE_MESURE`** ; emo et démon restent non qualifiés, pas négativement prouvés. |

La recommandation commune reste : **aucune architecture ni aucun sourcing supplémentaire**, sauf réparation strictement bornée de la méthode de découverte U2 si le pilote autorise la poursuite conditionnelle.

## 1. Méthode de contradiction

Pour chaque décision, la revue cherche cinq erreurs possibles :

1. **Faux positif :** un `GO` obtenu par addition de variantes, panier théorique ou concurrence insuffisamment étudiée.
2. **Faux négatif :** un `STOP` présenté comme universel alors que seul un sous-périmètre a été mesuré.
3. **Double comptage :** synonymes, parents/enfants de collection ou requêtes servies par la même page.
4. **Droit de gagner fictif :** friction concurrente ou amélioration UX confondue avec avantage défendable.
5. **Gate sourcing mal nommé :** accès API fonctionnel confondu avec preuve d'un SKU exact, livré France et conforme.

La charge de preuve est asymétrique : il faut des preuves positives pour engager architecture et sourcing ; il suffit qu'un gate indispensable reste non démontré pour ne pas poursuivre. En revanche, un STOP doit annoncer clairement son périmètre et ses conditions de réouverture.

## 2. U1 literie — attaque du `STOP_PHASE_2_DROIT_DE_GAGNER`

### OBSERVÉ

- `housse de couette` : **60 500 recherches/mois**, CPC **0,53 USD**.
- `parure de lit` : **33 100 recherches/mois**, CPC **0,49 USD**.
- Les collections matière mesurées vont de **1 000 à 3 600 recherches/mois**.
- La sonde de 40 offres affiche une médiane de **70,91 €** ; les bundles et parures complètes sont structurels.
- Dix acteurs documentés couvrent prix/volume, design accessible, promotion catalogue, profondeur, matières premium, fabrication française, personnalisation, expertise sommeil et omnicanal.

### Attaque : risques de faux négatif

- Dix acteurs ne prouvent pas littéralement que **tous** les positionnements possibles sont occupés.
- L'absence de DR, trafic, part de voix Ads ou AOV empêche de dire que chaque concurrent est fort sur chaque canal.
- Une niche de taille, de fermeture, d'usage ou de matière pourrait exister en dehors des angles génériques étudiés.
- Les têtes `housse de couette` et `parure de lit` ne doivent pas être interprétées comme 93 600 acheteurs uniques. Elles peuvent être servies par des pages proches et une même personne peut effectuer plusieurs recherches.

### Réponse hostile à l'attaque

Ces réserves ne créent aucun droit de gagner. Le dossier n'a pas besoin de prouver que toute innovation future est impossible ; il doit décider si **la thèse actuelle** autorise l'étape suivante. Elle ne l'autorise pas.

- Même en ignorant totalement `parure de lit`, la seule tête `housse de couette` franchit le seuil catalogue : le volume n'est pas le point fragile.
- Un DR faible ou un AOV élevé chez un concurrent quantifierait l'accès ou l'économie ; il ne fournirait pas un produit, une distribution ou une promesse exclusive.
- Les frictions visibles — prix « dès », choix de taille, composition pièce par pièce — sont copiables et déjà partiellement résolues par d'autres acteurs.

### Correction requise

Remplacer toute formulation absolue « les concurrents couvrent tous les angles » par : **« les concurrents couvrent tous les angles génériques documentés dans la thèse actuelle »**.

### Verdict recommandé

**Maintenir `STOP_PHASE_2_DROIT_DE_GAGNER`.** Réouverture seulement sur preuve préalable d'une sous-intention solvable et mal servie, d'un avantage fournisseur exclusif, d'une performance matière vérifiable ou d'une distribution autorisée. Ne pas collecter DR/AOV par réflexe avant cette thèse.

## 3. U2 bouillottes — attaque du marché conditionnel

### OBSERVÉ

- Le minimum prudent publié atteint **42 600 recherches/mois** avec `bouillotte`, `électrique`, `peluche`, `sèche`, `cervicale` et `chausson` ; les graines micro-ondes/noyaux/lin les plus recouvrantes ne sont pas ajoutées.
- Sonde de 40 offres : médiane **17,63 €**, **40 % sous 15 €**, seulement **45 % à 20 € ou plus**.
- Huit acteurs montrent des seuils de franco et des fonctions complémentaires ; un seul coffret précomposé clair est observé à **58,50 €**.
- La sécurité est un gate indépendant : eau chaude, micro-ondable, électrique, peluche/enfant et claims santé ne partagent pas les mêmes risques.

### Attaque : faux positif volume

Le total 42,6 k n'est valide que si les requêtes correspondent à des pages/collections distinctes qu'une même boutique peut légitimement servir. `bouillotte` est une page parent probable ; `bouillotte sèche`, `peluche`, `électrique`, `cervicale` et `chausson` sont des enfants ou usages. Additionner les volumes exacts de requêtes n'est pas automatiquement interdit, mais l'éligibilité de pages distinctes et la convergence de boutique doivent être démontrées.

Le dossier ne doit donc pas présenter 42,6 k comme un volume « nettoyé définitif ». Le bon statut reste **marché conditionnel**.

### Attaque : faux positif panier

- Calculer « deux produits franchissent le franco » ne prouve pas que deux produits sont achetés ensemble.
- Un seuil de livraison peut pousser l'AOV, mais il peut aussi augmenter l'abandon ou conduire le marchand à subventionner la livraison.
- Les duos cervicale+lombaire ou deux peluches sont **paniers arithmétiquement possibles**, pas paniers observés en commande.
- Le seul coffret précomposé à 58,50 € prouve une offre, pas sa conversion ni sa marge.

La médiane à 17,63 € rend l'économie single-unit fragile. Le gate prix/panier n'est pas passé ; il est seulement assez plausible pour éviter un STOP immédiat.

### Attaque : faux droit de gagner

« Chaleur par zone et moment » est déjà couvert par Douce Bouillotte, Soframar/Warmies, Coussin Zenitude et les spécialistes artisanaux. Ce n'est pas encore un wedge. L'origine française, le bio, le cadeau, la peluche, la profondeur et le ciblage anatomique ont tous des incumbents visibles.

### Verdict marché recommandé

**`MARCHE_CONDITIONNEL_NON_VALIDE`**, et non `GO marché` :

- nettoyer volume et page eligibility par eau / sèche / peluche / électrique / anatomique ;
- obtenir un proxy crédible d'AOV ou une économie prudente sur panier single-unit ;
- choisir un régime de sécurité principal au lieu de sourcer simultanément quatre familles hétérogènes ;
- démontrer un droit de gagner qui n'est pas seulement un assemblage des offres existantes.

## 4. U2 sourcing — attaque du `REPARER`

### OBSERVÉ

Quatre requêtes ont retourné 30 résultats via l'API AliExpress officielle :

- `microwave flaxseed heating pad neck` : 0/5 exact ;
- `rubber hot water bottle knitted cover 2 liter` : 0/5 exact ;
- `hot water bag plush cover winter warmer` : 0/10 exact ;
- `bouillotte eau chaude housse peluche 2L` : 0/10 exact.

L'accès et la destination France ont répondu correctement, mais aucun `product_id` pertinent n'a été retenu. Il n'existe donc aucune preuve de variante, composition, capacité, stock, prix ou fret France.

### Attaque : mauvaise inférence possible

Trente résultats sur quatre formulations constituent un test de requête, pas un balayage fournisseur. Zéro exact peut signifier :

- mauvais vocabulaire ou mauvaise segmentation de recherche ;
- ranking API médiocre ;
- catégorie ou locale inadéquate ;
- résultats limités trop tôt ;
- absence d'identifiants exacts provenant d'une découverte publique autorisée.

Il serait donc faux de conclure « aucune offre fournisseur existe ». Il serait tout aussi faux de conclure que le sourcing est en cours de validation simplement parce que l'API répond `ok: true`.

### Gate exact à respecter

La réparation doit produire, pour une seule famille prioritaire :

1. un identifiant produit exact obtenu par une voie autorisée ;
2. les variantes exactes et leurs propriétés ;
3. stock et expédition vers la France pour la variante retenue ;
4. coût rendu prudent ;
5. cohérence des photos et de la composition ;
6. notices, avertissements, traçabilité et responsable UE ;
7. preuves de sécurité adaptées au type de bouillotte.

L'API fournisseur ne suffit pas à prouver la conformité. Les certificats génériques, mentions `CE` ou assertions de fiche ne sont pas des rapports exacts du SKU.

### Verdict sourcing recommandé

**Maintenir `REPARER_AVANT_SOURCE_EXACTE`.** Le statut ne doit être ni `AUCUN_FOURNISSEUR`, ni `RETENU_MARCHE_A_SOURCER`, ni `GO lancement`.

Si la méthode réparée trouve un SKU, le produit doit encore passer séparément économie et sécurité. Si elle échoue de nouveau après recherche mieux ciblée, le bon résultat pourra devenir `AUCUNE_OFFRE_EXPLOITABLE_OBSERVEE_DANS_LE_CANAL`, toujours sans généraliser à toute l'offre mondiale.

## 5. U3 globe/cartographie — attaque du STOP 22,87 k

### OBSERVÉ

- Noyau produit : globe terrestre 18,1 k + carte monde bois 1,6 k + carte à gratter 1,9 k = **21,6 k**.
- Complément mural : carte du monde murale 590 + planisphère mural 90 + poster 590 = **1,27 k**.
- Total prudent : **22,87 k**, déficit **7,13 k** face au seuil de 30 k.
- Les têtes `carte du monde`, `planisphère` et `mappemonde` sont polluées et synonymiques ; elles ne sont pas ajoutées.

### Attaque : faux négatif possible

Le déficit de 7,13 k est assez faible pour qu'une expansion commerciale propre puisse théoriquement le combler. Le dossier ne démontre pas que tous les objets légitimes — cartes relief, magnétiques, enfant, liège, métal, affiches ville, globes lumineux — ont été mesurés et dédupliqués.

Par conséquent, **22,87 k n'est pas un plafond de tout l'univers cartographie**, seulement le total propre actuellement prouvé.

### Réponse hostile à l'attaque

Le protocole n'autorise pas à sauver un candidat avec une liste d'adjacences imaginées. Aucun lot commercial net de 7,13 k n'est actuellement démontré. Les grosses têtes génériques ne peuvent pas être ajoutées sans relecture de SERP et déduplication.

### Verdict recommandé

**Maintenir `STOP_VOLUME_CATALOGUE_AU_PERIMETRE_MESURE`.** Réouverture seulement si un export propre apporte au moins 7,13 k de requêtes servies par des pages distinctes et cohérentes avec la même boutique. Ce serait une nouvelle preuve, pas une correction arithmétique.

## 6. U4 astronomie — attaque séparée des deux modes

### U4a télescopes

#### OBSERVÉ

- Mesure historique : `telescope` à **27 100 recherches/mois France**.
- Cœur prix historique **239–369 €**, occupé par Bresser, Sky-Watcher, Celestron et Mizar.
- La lecture publique actuelle montre spécialistes techniques, grandes enseignes, marques établies, profondeur d'accessoires et comparaison sur diamètre, focale, monture, stabilité et collimation.

#### Attaque

Le volume historique n'est pas une mesure fraîche et 27,1 k serait sous le plancher catalogue. Mais U4a est explicitement un mode high-ticket : appliquer mécaniquement le seuil catalogue de 30 k serait une erreur de protocole. Inversement, le ticket élevé ne compense pas le besoin de confiance et le SAV technique.

#### Verdict recommandé

**Maintenir `STOP_REPRISE_SANS_THESE_NOUVELLE`.** La cause est marques/confiance/SAV, pas un faux STOP volume. Réouverture uniquement avec distribution autorisée, avantage technique prouvé ou capacité SAV réelle.

### U4b décoration astro

#### OBSERVÉ

- `projecteur galaxie` 1,6 k ; `lampe lune` 1,9 k ; `projecteur ciel étoilé` 1,9 k ; `planétarium` 6,6 k.
- Somme des quatre mesures : **12 k**.
- `projecteur galaxie` et `projecteur ciel étoilé` se recouvrent fortement ; les marchands utilisent également `planétarium projecteur` pour les mêmes appareils.
- `planétarium` est pollué par lieux, horaires, séances et billetterie.
- Un rappel officiel 2026 matérialise le risque de faisceau laser trop puissant et mal étiqueté.

#### Attaque : portée du plafond

Dire « U4b ≤12 k » est trop fort si cela signifie tout l'univers décoratif. **12 k est la somme brute maximale de ces quatre têtes**, non une borne mathématique de `veilleuse galaxie`, `lampe astronaute`, `déco espace`, `néon planète` et autres familles non mesurées.

#### Réponse hostile

Les quatre têtes échouent même avant nettoyage, avec un déficit de 18 k. Aucune famille additionnelle propre et suffisamment large n'est apportée. Les synonymes et la pollution réduisent le total prouvé. La sécurité laser rend en outre une expansion opportuniste vers des projecteurs génériques moins désirable, sans être la cause du STOP.

#### Verdict recommandé

**Maintenir `STOP_VOLUME_CATALOGUE_AU_PERIMETRE_MESURE`.** Ne rouvrir qu'avec de nouvelles collections commerciales, non synonymes, totalisant le déficit après nettoyage et partageant réellement une même proposition de boutique.

## 7. U5 gothique / emo / démon — attaque du STOP ≤4,12 k

### OBSERVÉ

- Les sept requêtes gothiques commerciales totalisent au maximum **4,12 k** avant déduplication.
- `vêtement gothique` recouvre robes et potentiellement chaussures ; `boutique gothique` recouvre toutes les catégories. Le net est donc inférieur.
- Même avec `bottine gothique` à 390, le plafond du lot mesuré serait 4,51 k.
- Les têtes nues `gothique`, `emo` et `démon` sont polluées ; aucun cluster produit propre emo/démon assez large n'est fourni.
- La SERP produit contient déjà spécialistes, artisans et catalogues profonds ; tailles, retours, licences et contenu choquant ajoutent des risques.

### Attaque : faux négatif de périmètre

Le titre « gothique / emo / démon » dépasse la preuve disponible : le calcul terminal porte principalement sur le gothique commercial. L'absence de mesure emo/démon ne prouve pas que ces deux sous-univers valent zéro.

### Réponse hostile

Le déficit est supérieur à 25 k. Aucun cluster adjacent mesuré n'approche l'ordre de grandeur nécessaire. Ajouter `dark academia`, `punk`, `witchy`, `occulte` ou fantasy changerait de marché et augmenterait les risques de licence/positionnement. Le STOP de la thèse actuelle est donc robuste.

### Verdict recommandé

**Maintenir `STOP_VOLUME_CATALOGUE_PERIMETRE_GOTHIQUE_MESURE`.** Marquer emo et démon `NON_QUALIFIES`, pas `STOP_VOLUME_PROUVE`. Toute analyse future serait un nouveau candidat autonome, sans addition rétroactive au lot gothique.

## 8. Corrections transverses requises

1. **Qualifier les totaux.** Employer `total propre prouvé`, `somme brute des graines mesurées` ou `borne du lot mesuré`, pas `plafond de l'univers`, sauf expansion réellement exhaustive.
2. **Séparer recherche et audience.** Les volumes de requêtes ne sont pas des acheteurs uniques ; l'addition exige page eligibility et convergence de boutique.
3. **Séparer panier possible et panier observé.** Deux prix qui franchissent un franco ne prouvent ni AOV, ni taux d'attachement, ni marge.
4. **Borner les STOP droit de gagner.** Le STOP porte sur la thèse actuelle, pas sur toute innovation future imaginable.
5. **Ne pas confondre API saine et sourcing réussi.** `ok: true` prouve le transport API ; seule une fiche exacte avec variante et fret France permet l'économie, et la conformité reste un gate séparé.
6. **Ne pas utiliser les risques comme substitut au gate principal.** Laser, brûlure, retours, IP ou contenu Ads renforcent une prudence ; ils ne doivent pas masquer un calcul volume ou concurrence faible.
7. **Uniformiser les statuts.** Ajouter `_AU_PERIMETRE_MESURE` aux STOP volume lorsque l'expansion n'est pas exhaustive, et des critères de réouverture chiffrés.

## 9. Verdicts recommandés finaux

| Univers / étape | Statut recommandé | Prochaine action autorisée |
|---|---|---|
| U1 | `STOP_PHASE_2_DROIT_DE_GAGNER` | Aucune ; réouverture seulement sur thèse propriétaire prouvée. |
| U2 marché | `MARCHE_CONDITIONNEL_NON_VALIDE` | Nettoyage volume/page eligibility, économie single-unit/AOV et choix d'un régime de sécurité. |
| U2 sourcing | `REPARER_AVANT_SOURCE_EXACTE` | Réparer la découverte API pour une seule famille, sans import ni engagement. |
| U3 | `STOP_VOLUME_CATALOGUE_AU_PERIMETRE_MESURE` | Aucune ; rouvrir seulement avec ≥7,13 k nets additionnels cohérents. |
| U4a | `STOP_REPRISE_SANS_THESE_NOUVELLE` | Aucune ; thèse marque/technique/SAV obligatoire. |
| U4b | `STOP_VOLUME_CATALOGUE_AU_PERIMETRE_MESURE` | Aucune ; nouvelles familles non synonymes nécessaires. |
| U5 gothique mesuré | `STOP_VOLUME_CATALOGUE_PERIMETRE_GOTHIQUE_MESURE` | Aucune. Emo/démon restent candidats non qualifiés séparés. |

## 10. U6 — checklist générique uniquement

Sans intégrer ni préjuger le travail en cours, le verdict U6 devra vérifier :

- intentions commerciales France nettoyées, marques et informationnel retirés ;
- synonymes dédupliqués et page eligibility explicite ;
- cohérence réelle des collections dans une même boutique ;
- gate prix avant profilage lourd : 30–50 prix comparables, médiane et part low-ticket ;
- panier réellement marchandisé distingué d'un panier arithmétique ;
- acteurs généralistes, spécialistes, artisans et marketplaces ;
- droit de gagner formulé comme capacité défendable, pas simple esthétique ou meilleure UX ;
- risques de claims, sécurité, propriété intellectuelle et politiques Ads ;
- aucun sourcing tant que marché, panier, concurrence et droit de gagner ne sont pas validés ;
- au sourcing : produit, variante, stock, fret France, coût rendu, vérité visuelle et conformité traités comme preuves séparées.

## Sources internes relues

- `reports/niches-univers-terminal-u1-literie-20260815.md`
- `reports/phase0-univers-u2-bouillottes-20260815-181328-a1.md`
- `reports/u2-bouillottes-competiteurs-panier-20260815.md`
- `reports/phase4-sourcing-u2-bouillottes-20260815.md`
- `reports/niches-univers-terminal-u3-cartographie-20260815.md`
- `reports/niches-univers-terminal-u4-astronomie-20260815.md`
- `reports/niches-univers-terminal-u5-gothique-20260815.md`

**Aucun registre, run-state, sourcing additionnel ou architecture n'a été modifié.**
