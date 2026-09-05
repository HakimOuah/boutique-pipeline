# Consolidation nette bijoux pierres naturelles / symboles

Date : 05/09/2026. Corpus de mots-clés déjà collectés, France/français. Aucun appel API ni sourcing supplémentaire dans cette passe. Les familles arbres décoratifs, luxe/or/diamant et santé/lithothérapie sont exclues du total bijoux.

## Méthode et déduplication

Corpus brut : **2039 lignes** : `groupes-bijoux.json`, `raw/screen-univers-reprises.json`, `raw/labs-bracelet-amethyste.json` (78), `raw/labs-bracelet-lapis.json` (281), `raw/labs-collier-lapis.json` (73). Après déduplication lexicale : **1881 lignes**.

La clé normalisée retire accents, prépositions et pluriels, conserve le type et les qualificatifs du bijou, et unifie seulement l’alias clair `lapis`/`lapis-lazuli`. Pour une clé, le volume mensuel maximum est conservé ; les séries mensuelles et tous les alias source restent dans le JSON. Une série mensuelle identique entre deux requêtes commerciales différentes ne suffit pas à les fusionner : les sous-types peuvent contribuer séparément. Les volumes seuls servent au total ; CPC et autres signaux ne sont pas additionnés.

Statuts après déduplication : **eligible 633**, **ambigu 546**, **exclu 702**. Les lignes éligibles sans volume numérique restent dans le JSON mais ne contribuent pas au total net.

## Total net des familles éligibles

| Famille | Groupes | Volume mensuel net |
|---|---:|---:|
| bracelets pierres naturelles | 229 | 19 870 |
| bagues pierres naturelles | 126 | 13 350 |
| colliers/pendentifs pierres naturelles | 110 | 7 320 |
| symboles | 60 | 3 600 |
| boucles d'oreilles pierres naturelles | 1 | 590 |
| **Total pierres naturelles + symboles** | **526** | **44 730** |

Le total est une somme de requêtes commerciales distinctes après déduplication lexicale. Il ne représente ni personnes, ni commandes, ni prévision de ventes, et ne doit pas être recyclé comme gate PRODUIT PUR/Search. Il reste une consolidation UNIVERS.

Statut proposé : `eligible` signifie candidat à adjudication pour la suite, jamais PASS ni GO ; `ambigu` reste en revue sans réinstruction ; `exclu` est hors périmètre. La famille bagues (13 350) agrège des requêtes améthyste et pierres naturelles dont la SERP montre aussi luxe, métaux précieux et occasion ; ce chiffre ne vaut donc pas validation commerciale. Les prix observés (médiane 39 € sur 33 bijoux) attestent une offre, sans prouver marge, qualité, conformité ou sourcing.

## Extension Labs et lecture SERP

Les trois corpus additionnels ont été unis avant total. Les variantes inversées/accents et `lapis`/`lapis-lazuli` sont dédupliquées ; les sous-types réellement différents (`bracelet`/`collier`, homme/femme, pierre différente) restent séparés quand la requête est commerciale.

La SERP fraîche `raw/serp-bijoux.json` pour `bracelet pierre naturelle` comporte **9 résultats organiques** : Annavelezia Litho, Arbre des Chakras, Garaulion, La Boîte à Cailloux, Bijou Brigitte, Mayana, Histoire d’Or, Pinterest et Cristal Forest. L’intention est mixte : esthétique/achat de bijoux, pierres naturelles et lithothérapie. Les claims de santé, énergie ou protection ne sont pas repris comme faits.

Deux contrôles SERP supplémentaires ont été versés au contexte sans modifier le volume net : `bague améthyste` (9 offres visibles, dont Histoire d’Or, Maty, Elliade, Juwelo, Marc Orian, Glamira, Carador ; 58 Facettes luxe et Castafiore occasion sont des cas à adjudication) et `collier pierre naturelle` (10 offres visibles, dont Nature.fr, Miracles Minéraux, Atelier Amaya, Histoire d’Or, Bohm, Ysie, Maison DiGiorgio, Mayana, Gas et Zosha). Les enseignes, métaux précieux, luxe et occasion restent des signaux d’incertitude, pas des sommes.

Le fichier `raw/trends-bijoux.json` compare les trois têtes en web France sur 2021-09–2026-08. Les indices Trends sont des séries normalisées et ne sont pas convertis en volumes ni additionnés au net.

## Échantillon éligible

| Volume | Famille | Expression retenue | Sources regroupées |
|---:|---|---|---:|
| 4 400 | bracelets pierres naturelles | `bracelet pierre naturelle` | 2 |
| 3 600 | bagues pierres naturelles | `bague améthyste` | 2 |
| 1 900 | bracelets pierres naturelles | `bracelet pierre lune` | 1 |
| 1 900 | bagues pierres naturelles | `bague pierre lune` | 1 |
| 1 900 | bracelets pierres naturelles | `bracelet œil de tigre` | 1 |
| 1 900 | symboles | `bijoux arbre de vie` | 2 |
| 1 600 | bracelets pierres naturelles | `bracelet améthyste` | 3 |
| 1 600 | colliers/pendentifs pierres naturelles | `collier pierre naturelle` | 2 |
| 1 000 | colliers/pendentifs pierres naturelles | `collier pierre de lune` | 2 |
| 720 | bagues pierres naturelles | `bague pierre naturelle` | 2 |
| 720 | bracelets pierres naturelles | `bracelet lapis lazuli` | 7 |
| 720 | colliers/pendentifs pierres naturelles | `collier lapis` | 8 |
| 590 | bracelets pierres naturelles | `bracelet pierre lave` | 1 |
| 590 | bagues pierres naturelles | `améthyste bague argent` | 1 |
| 590 | boucles d'oreilles pierres naturelles | `boucles d oreilles pierre naturelle` | 2 |
| 480 | bracelets pierres naturelles | `bracelet femme pierre naturelle` | 1 |
| 390 | bracelets pierres naturelles | `bracelet homme pierre naturelle` | 1 |
| 390 | bagues pierres naturelles | `bague argent pierre de lune` | 1 |
| 390 | bagues pierres naturelles | `bague améthyste ancienne` | 1 |
| 390 | symboles | `collier main de Fatma` | 1 |
| 390 | bracelets pierres naturelles | `bracelet homme lapis lazuli` | 6 |
| 320 | bracelets pierres naturelles | `bracelet pierre jade` | 1 |
| 320 | bagues pierres naturelles | `bague pierre semi-précieuse` | 1 |
| 320 | bracelets pierres naturelles | `bracelet amethyste homme` | 2 |
| 260 | colliers/pendentifs pierres naturelles | `collier pierre jade` | 1 |
| 260 | bracelets pierres naturelles | `bracelet lapis lazuli femme` | 3 |
| 210 | bracelets pierres naturelles | `bracelet pierre soleil` | 1 |
| 210 | colliers/pendentifs pierres naturelles | `collier pierre semi-précieuse` | 1 |
| 210 | bagues pierres naturelles | `bague pierre turquoise` | 1 |
| 210 | bagues pierres naturelles | `bague grosse pierre naturelle` | 1 |
| 210 | bagues pierres naturelles | `améthyste bague homme` | 1 |
| 210 | symboles | `bijoux symboliques` | 1 |
| 210 | bracelets pierres naturelles | `bracelet amethyste femme` | 2 |
| 170 | bracelets pierres naturelles | `bracelet pierre de lune véritable` | 1 |
| 170 | bracelets pierres naturelles | `bracelet pierre améthyste` | 4 |

## Ambiguïtés et exclusions

Les lignes `ambigu` restent consultables dans le JSON, mais ne contribuent pas aux totaux : pierre générique/couleur sans identité naturelle, type de bijou incomplet ou intention non tranchée. Les lignes `exclu` sont écartées pour arbre ou porte-bijoux décoratif, accessoires/DIY, information/service/enseigne, luxe/or/diamant, ou santé/lithothérapie (recharge, vertus, chakra/mala, symptômes/pathologies). Aucun de ces ensembles n’est réactivé.

Exemples ambigus :
- 2900 — `bracelet pierre` : bijou porté mais pierre seulement générique/couleur : naturel non démontré
- 2900 — `bague pierre` : bijou porté mais pierre seulement générique/couleur : naturel non démontré
- 1600 — `bracelet homme pierre` : bijou porté mais pierre seulement générique/couleur : naturel non démontré
- 1600 — `collier à pierre` : bijou porté mais pierre seulement générique/couleur : naturel non démontré
- 1300 — `bague pierre bleue` : bijou porté mais pierre seulement générique/couleur : naturel non démontré
- 1300 — `bague pierre verte` : bijou porté mais pierre seulement générique/couleur : naturel non démontré
- 880 — `bracelet pierre naissance` : bijou porté mais pierre seulement générique/couleur : naturel non démontré
- 880 — `collier pierre naissance` : bijou porté mais pierre seulement générique/couleur : naturel non démontré
- 720 — `bague pierre noire` : bijou porté mais pierre seulement générique/couleur : naturel non démontré
- 590 — `bracelet pierre bleue` : bijou porté mais pierre seulement générique/couleur : naturel non démontré

Exemples exclus :
- 880 — `bague pierre précieuse` : luxe, or/diamant, marque ou requête enseigne hors périmètre pierres naturelles/symboles génériques
- 720 — `améthyste bague or` : luxe, or/diamant, marque ou requête enseigne hors périmètre pierres naturelles/symboles génériques
- 480 — `collier pierre précieuse` : luxe, or/diamant, marque ou requête enseigne hors périmètre pierres naturelles/symboles génériques
- 480 — `lapis stone bracelet` : requête détectée en langue étrangère ou formulation anglaise ; hors corpus France/français
- 390 — `bracelet pierre précieuse` : luxe, or/diamant, marque ou requête enseigne hors périmètre pierres naturelles/symboles génériques
- 390 — `bracelet pierre naturelle signification` : information, service, DIY, comparateur, achat/retailer ou accessoire ; pas une offre produit cœur
- 260 — `bague or pierre` : luxe, or/diamant, marque ou requête enseigne hors périmètre pierres naturelles/symboles génériques
- 260 — `bague améthyste or blanc` : luxe, or/diamant, marque ou requête enseigne hors périmètre pierres naturelles/symboles génériques
- 260 — `pendentif arbre de vie manège à bijoux` : luxe, or/diamant, marque ou requête enseigne hors périmètre pierres naturelles/symboles génériques
- 210 — `bracelet montre pierre lannier` : luxe, or/diamant, marque ou requête enseigne hors périmètre pierres naturelles/symboles génériques

## Contrôle du catalogue de prix

Le fichier `prix-bijoux-20260905.md` contient **35 fiches distinctes : 33 bijoux portés et 2 arbres de vie décoratifs**. Seuls les 33 bijoux entrent dans les statistiques : prix **24–119 €**, médiane **39 €**, moyenne **45,88 €** ; **26** fiches à 24–49 €, **3** à 50–89 € et **4** à 90–119 €. Les deux arbres décoratifs restent hors stats et hors volume bijoux. Prix normal et prix soldé d’une même fiche ne sont pas doublés.

Ces prix attestent une offre publique observée ; ils ne donnent ni coût rendu, ni marge, ni panier moyen. Les matières, origines, certifications, claims lithothérapie et délais restent à vérifier séparément.
