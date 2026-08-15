# U5 gothique / emo / démon — verdict terminal volume-first

**Date :** 2026-08-15

**Mode :** `catalogue-volume`, lecture seule ; mesures commerciales France transmises par l'orchestrateur, SERP Web publique sans Chrome ni SEMrush.

**Décision : `STOP_VOLUME_CATALOGUE`.** Aucun profilage concurrentiel lourd, aucune architecture et aucun sourcing ne sont ouverts.

Le périmètre terminal couvre aussi les extensions commerciales `emo` et `démon` : `vêtements emo` affiche 40 recherches/mois, `bijoux emo` 20, et `décoration démon` ne retourne aucune ligne mesurable dans la même base. Les têtes nues, polluées par musique, culture, fiction et licences, ne sont pas utilisées comme volume produit.

## 1. Pourquoi le gate ferme

### OBSERVÉ — mesures commerciales propres

| Requête | Volume France/mois | Lecture |
|---|---:|---|
| `robe gothique` | 1 000 | Transactionnel, textile à tailles |
| `chaussures gothiques` | 880 | Transactionnel, pointures/retours |
| `bijoux gothiques` | 720 | Transactionnel, matière et IP à vérifier |
| `vêtement gothique` | 720 | Transactionnel, mais recouvre potentiellement robes et chaussures |
| `boutique gothique` | 480 | Intention boutique, recouvre plusieurs catégories |
| `décoration gothique` | 210 | Transactionnel faible |
| `accessoire gothique` | 110 | Transactionnel très faible |
| **Somme brute maximale** | **4 120** | Avant toute déduplication |

La somme brute de 4 120 est volontairement généreuse. Elle additionne des ensembles qui se chevauchent : une recherche de robe peut relever de `vêtement gothique`, et l'intention `boutique gothique` recouvre vêtements, bijoux, chaussures et accessoires. Le volume net adressable est donc **inférieur ou égal à 4 120**, pas égal avec certitude.

La précédente extraction locale mentionnait aussi `bottine gothique` à 390. Même en l'ajoutant sans dédupliquer, le plafond atteindrait seulement **4 510**, sans modifier la décision.

Le protocole catalogue demande environ **30 000 recherches mensuelles France pertinentes et nettoyées** pour poursuivre. U5 atteint au mieux 13,7 % de ce seuil avec les sept lignes propres fournies, ou 15,0 % avec la bottine additionnelle. L'écart n'est pas une zone grise de nettoyage : il manque plus de 25 000 recherches pertinentes.

### OBSERVÉ — pollution des graines larges

- `gothique` nu renvoie architecture, histoire de l'art, littérature, typographie, tourisme et sous-culture ; ce volume ne peut pas être attribué à une boutique.
- `emo` nu mélange musique, définitions, médias, acronymes et culture ; les formulations produit mesurées restent à 40 et 20 recherches/mois.
- `démon` nu relève largement de la religion, de la mythologie, de la culture populaire et de licences ; `décoration démon` n'a retourné aucune ligne mesurable.
- Les permutations, pluriels et formulations proches ne doivent pas être additionnés sans éligibilité à une page distincte et déduplication.

### MANQUANT

- Aucun cluster commercial propre `emo + objet` ou `démon + objet` n'a été observé à une échelle susceptible de combler l'écart.
- Aucune preuve de 200 concepts produits non licenciés soutenus par une demande France suffisante.
- Part de marque et chevauchement exact entre robe/vêtement, chaussures/bottines et boutique/catégories.

### HYPOTHÈSE rejetée

Il serait possible d'imaginer que `dark academia`, `punk`, `witchy`, `occulte`, `crâne`, `chauve-souris` ou `fantasy` élargissent fortement l'univers. Ce serait toutefois **changer de marché** et importer des intentions adjacentes non mesurées, pas nettoyer U5. Elles ne sont donc pas utilisées pour sauver artificiellement le seuil.

## 2. SERP publique consolidée — seulement ce qui est nécessaire au verdict

La SERP publique est une lecture d'index, pas une capture certifiée et localisée des dix positions Google France. Elle suffit ici à constater que le faible volume n'est pas compensé par un vide concurrentiel.

### OBSERVÉ

| Sous-intention | Acteurs visibles | Lecture minimale |
|---|---|---|
| Mode / robe / chaussures | [Castle Gothic](https://castle-gothic.fr/), [L'Antre Gothique](https://antregothique.com/), [Vêtement Gothique](https://vetement-gothique.fr/), [EMP](https://www.emp-online.fr/topics/gothic/set/lifestyle/clothing/shoes/), [Darkland Paris](https://www.darklandparis.fr/) | Plusieurs spécialistes, marque/distributeur et acteur physique historique ; résultats déjà occupés |
| Bijoux | [EMP](https://www.emp-online.fr/themes/gothic/bijoux/), [Castle Gothic](https://castle-gothic.fr/collections/bijoux-gothiques), [Nocturne Atelier](https://nocturneatelier.fr/), [Nox Bunny](https://noxbunny.fr/), [Un Grand Marché](https://www.ungrandmarche.fr/boutiques/l/bijoux-gothique) | Spécialistes, artisans et marketplace créateurs ; concurrence sur prix, originalité et matière |
| Décoration | [Discobole](https://www.discobole.fr/boutique/accessoires/decoration-gothique/), [Les Arcanes d'Hel](https://www.lesarcanesdhel.fr/categorie-produit/decoration/), [L'Antre Gothique](https://antregothique.com/collections/accessoires-gothiques) | Discobole affiche 147 produits ; offre déjà profonde malgré seulement 210 recherches/mois mesurées sur la tête |
| Accessoires / catalogue | [GOTIQUE](https://gotique.fr/collections/accessoires-gothiques/), [Gothic Shop](https://www.gothic-shop.net/fr/cat%C3%A9gorie/accessoires-gothiques/), [Bat'Doll](https://batdoll.fr/), [Satan Shop](https://www.satan-shop.com/) | Catalogues spécialisés larges ; Gothic Shop affiche 1 080 résultats sur la catégorie indexée |

Les acteurs ne sont pas tous équivalents en qualité, ancienneté ou modèle économique ; aucun chiffre de trafic ou de ventes n'est inféré. Mais la présence de plusieurs spécialistes par sous-intention contredit une éventuelle thèse « micro-volume mais SERP vide ».

### OBSERVÉ — ticket, non bloquant

La sonde publique antérieure, conservée dans `reports/serp-prix-u5-u6-20260815.md`, avait relevé 50 prix avec une médiane consolidée de 59,45 €. Les accessoires seuls avaient une médiane de 12,40 €, tandis que textile, sacs, bijoux de marque/artisanaux et décoration pouvaient porter un ticket supérieur. Le gate prix n'est donc pas la cause du STOP.

### MANQUANT

- Positions exactes de Google.fr, annonces, Shopping et part de voix par acteur.
- Trafic, ventes, backlinks, historique publicitaire et rentabilité des acteurs.

Ces données ne sont pas recherchées davantage : le gate volume ferme déjà l'étude catalogue.

## 3. Risques qui renforcent le STOP sans le provoquer

### A. Tailles, pointures et retours

#### OBSERVÉ

- [Vêtement Gothique publie un guide des tailles](https://vetement-gothique.fr/pages/guide-des-tailles) distinct pour bagues, hauts, pantalons, shorts, jupes et robes, ce qui matérialise la complexité de correspondance.
- Sa [politique de retours](https://vetement-gothique.fr/pages/politique-retours) affiche des frais de renvoi à la charge du client et ne remplace explicitement que les articles défectueux ou endommagés dans la section échange visible.
- [Castle Gothic](https://castle-gothic.fr/products/baskets-a-plateforme-de-style-gothique-sur-une-plateforme-epaisse) affiche guide de pointures et retour 14 jours sur une chaussure à plateforme à 214,95 €.
- La DGCCRF rappelle qu'en vente à distance, sauf exception, le consommateur dispose de 14 jours pour notifier sa rétractation puis renvoyer le bien : [guide acheteur](https://www.economie.gouv.fr/files/files/directions_services/dgccrf/documentation/publications/depliants/guide-acheteur.pdf?v=1688387474).

#### HYPOTHÈSE prudente

Un catalogue dominé par robes et chaussures ajouterait variation de tailles, pointures, confort, qualité textile et coûts de retour. Aucun taux de retour propre à U5 n'est observé ; il ne faut pas en inventer un.

### B. Propriété intellectuelle et licences

#### OBSERVÉ

- Des résultats marchands mêlent esthétique générique et références à des groupes ou personnages. Satan Shop affiche par exemple des coques `My Chemical Romance`; d'autres catalogues alternatifs commercialisent couramment merch musique/films/séries.
- L'INPI rappelle que la détention, la vente ou l'importation de produits comportant une marque contrefaisante peut constituer une atteinte : [guide INPI sur la contrefaçon](https://www.inpi.fr/inpi-block/download-document?id=20585).

#### Règle de prudence

Tout nom de groupe, logo, album, personnage, franchise, œuvre graphique, mascotte ou motif reconnaissable doit être exclu sans preuve de licence. Une esthétique générique (chauve-souris, architecture, dentelle, lune, squelette stylisé) n'est pas automatiquement libre : chaque dessin/motif doit rester traçable et non copié.

### C. Contenu démoniaque, macabre ou choquant

#### OBSERVÉ

- La SERP bijoux/déco contient des objets décrits comme « guillotine sanglante », cœur anatomique, faucheuse, monstres ou créatures maléfiques.
- Google Ads interdit notamment les promotions comportant imagerie violente, graphique ou susceptible de choquer/effrayer : [Google Ads — Shocking content](https://support.google.com/adspolicy/answer/16490051?hl=en).

#### Règle de prudence

Le mot `démon` n'est pas en soi une preuve d'interdiction, mais chaque visuel, titre, landing page et flux produit devrait être évalué. Gore, sang réaliste, automutilation, haine, sexualisation et images effrayantes augmentent le risque publicitaire et de marque. Ce risque n'est pas quantifié et n'est pas la base du STOP volume.

## 4. Verdict final

### `STOP_VOLUME_CATALOGUE`

Le dossier ne franchit pas la première porte : **≤4 120 recherches/mois brutes** sur les sept requêtes commerciales propres, contre environ **30 000** exigées pour un univers catalogue. Le mot nu est trop pollué pour combler honnêtement l'écart, et la SERP transactionnelle montre déjà une offre spécialiste profonde.

Le ticket parfois élevé ne renverse pas la décision. Il répondrait au gate suivant, mais le protocole interdit de compenser un volume insuffisant par un panier hypothétique.

### Conséquences

- fin de l'analyse U5 comme boutique catalogue autonome ;
- aucun profilage lourd, aucune architecture, aucun sourcing ;
- aucune addition de graines voisines non mesurées pour « fabriquer » le seuil ;
- possibilité de requalifier plus tard **un produit ou micro-cluster autonome** uniquement avec une mesure France propre et une intention distincte. Ce serait un nouveau candidat, pas la réouverture automatique de l'univers U5.

## Sources locales de continuité

- `codex-chasse-clusters/reports/phase0-univers-u5-gothique-20260815-181328-a1.md`
- `codex-chasse-clusters/reports/serp-prix-u5-u6-20260815.md`
- `codex-chasse-clusters/reports/rapport-qualification-univers-20260815-181328.md`

## Limites

Pas de Chrome, SEMrush, tunnel marchand, analytics, sourcing ou données de commandes dans cette piste. Les prix, catalogues et politiques cités sont des observations publiques au 2026-08-15 et peuvent évoluer.
