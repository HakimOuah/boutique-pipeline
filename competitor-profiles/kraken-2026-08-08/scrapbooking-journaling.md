# Étude concurrentielle profonde — Scrapbooking & journaling France (Kraken phase 2)

**Date** : 8 août 2026

**Marché** : France / français

**Périmètre** : demande, SERP, concurrence, modèle, persona, différenciation et
right to win ; aucun sourcing, import, site ou dépense.

**Verdict** : `STOP_PHASE_2` pour une boutique catalogue dropshipping France.

## Verdict exécutif

Le premier filtre aurait dû être le prix, avant l'analyse concurrentielle
profonde. Sur 48 produits visibles des trois catégories principales de
Scraperie, la médiane est de 10,99 EUR et 33 produits sur 48 sont à 13,99 EUR ou
moins. Les papiers ont une médiane de 4,99 EUR et les autocollants de 8,99 EUR.
Sans preuve d'un panier multi-produits élevé, d'une marge contributive par
commande et d'un CAC de rupture compatible, cette structure n'est pas
intéressante pour le portefeuille d'Hakim.

Le `STOP` vient donc d'abord de la **structure prix/panier**, puis des autres
incertitudes : volume propre non reproductible, pression Shopping et
fulfillment multi-fournisseurs. L'existence d'un seul concurrent qui exécute
déjà le même modèle est au contraire un signal de validation. Elle ne devient
un frein que si les comparables se multiplient ou si leurs actifs rendent
l'offre impossible à défendre.

## 1. Filtre prix et panier — éliminatoire en premier

### Échantillon public Scraperie

| Catégorie, première page | Produits | Médiane | Lecture |
|---|---:|---:|---|
| Papiers | 16 | 4,99 EUR | 12/16 à 6,99 EUR ou moins |
| Autocollants | 16 | 8,99 EUR | 6/16 à 5,99 EUR |
| Matériel | 16 | 24,49 EUR | albums et outils remontent le ticket |
| **Ensemble** | **48** | **10,99 EUR** | **33/48 à 13,99 EUR ou moins** |

Le scrap favorise naturellement les paniers multi-lignes, mais aucune donnée
publique ne prouve ici le nombre d'articles par commande, l'AOV, la marge ou le
réachat. La livraison gratuite à 40 EUR demanderait, à prix médian, environ
quatre articles ; avec des produits à 5,99 EUR, environ sept. On ne doit pas
supposer que les clientes composent systématiquement ce panier.

**Décision projet** : `STOP_PRIX_PANIER`. Une niche dont le cœur est ancré
autour de 5–14 EUR ne poursuit pas l'étude coûteuse sans mécanisme de panier
observé et économie plausible. Les 200 produits ou le volume Search ne
compensent pas une faible contribution par commande.

## 2. Audit de la demande

Le total historique de **64 740 recherches mensuelles** ne peut pas être
reproduit à partir du fichier de mesure conservé :

| Élément conservé | Volume FR |
|---|---:|
| Mot-clé racine `scrapbooking` | 27 100 |
| Union des ancres mesurées du cluster | 11 360 |
| Champ `clean_totals_by_niche` historique | 64 740 |

La dérivation entre ces objets n'est pas conservée. En outre, la SERP
`scrapbooking` mélange Shopping, boutiques, questions et guides : les 27 100
recherches racine ne peuvent pas être comptées automatiquement comme 100 %
commerciales.

Quelques ancres réellement mesurées restent utiles :

| Mot-clé | Volume FR | Lecture |
|---|---:|---|
| `album scrapbooking` | 1 600 | collection commerciale plausible |
| `papier scrapbooking` | 1 300 | collection commerciale |
| `kit scrapbooking` | 880 | bande de revue cœur |
| `perforatrice scrapbooking` | 480 | collection secondaire à justifier |
| `stickers scrapbooking` | 590 | commercial, vigilance licences |
| `tampon scrapbooking` | 320 | secondaire à justifier |
| `washi tape` | 2 400 | intention à nettoyer, usage plus large |
| `massicot papier` | 2 900 | intention produit large, non exclusivement scrap |

**Décision demande** : `MANQUANT_RENETTOYAGE`. L'existence du marché est
observée, mais le seuil projet de 30 000 recherches commerciales dédupliquées
n'est plus considéré comme prouvé pour ce cluster tant que le calcul n'est pas
reconstruit requête par requête.

## 3. SERP et pression prix

### `matériel scrapbooking`

Fée du Scrap, Kerglaz et La Fourmi Créative apparaissent en tête, suivis par
des spécialistes, un bloc local, puis Cultura, Canson, Clairefontaine et
Craftelier. Il n'y a pas de vide de spécialiste.

### `kit scrapbooking`

Le bloc Shopping observé affichait notamment :

- Amazon, 351 pièces à 31,49 EUR ;
- Alibaba, 346 pièces à 20,33 EUR HT avec environ 30,40 EUR de livraison ;
- AliExpress, 125 pièces à 12,59 EUR + 1,73 EUR de livraison ;
- Rosemood, album à 34,90 EUR + 7,50 EUR de livraison.

Fée du Scrap, Studio-Scrap, Kerglaz, La Fourmi et Cultura occupent ensuite les
résultats organiques. Sur `scrapbooking`, Shopping expose également AliExpress
à 12,59 EUR et Craftelier à 18,22 EUR. La différenciation ne peut donc pas être
un simple kit générique revendu avec une marge marketing.

## 4. Comparables déterminants

| Acteur | Modèle observé | Preuve de force | Limite / signal |
|---|---|---|---|
| Scrapmalin | Stockiste/groupe établi | 80 000+ références revendiquées ; AS 33 ; 19,5 k trafic organique estimé | Spécialité diluée, mais profondeur et logistique hors de portée d'une V1 drop |
| La Fourmi Créative | Stockiste PrestaShop | 40 775 visites Brand Search directionnelles ; AS 33 ; 30,9 k trafic organique estimé | Largeur multi-loisirs, incidents de stock/SAV dans la VOC |
| Fée du Scrap | Stockiste + boutique physique | 11 000 produits ; kits/tutoriels ; AS 23 ; 13,5 k trafic organique estimé | L'angle projet-first et souvenir est déjà occupé |
| Florilèges Design | Fabricant/créateur français | Collections coordonnées, muses et contenu ; AS 21 ; 3 216 trafic organique estimé | Le moat est la propriété intellectuelle esthétique |
| Variations Créatives | Stockiste + boutique physique | 12 000 références, 150 marques, créée en 2007 ; AS 22 ; 6 686 trafic organique estimé | Preuve d'ancienneté, stock et conseil |
| Scraperie | `PROBABLE_DROPSHIP`, confiance élevée | 214 PDP publiques, promesse souvenir-first, expédition directe déclarée | AS 8 ; 58 trafic organique estimé ; 32 mots-clés ; 0 paid ; aucune vente prouvée |

Les estimations SEMrush et Brand Search ne sont pas des analytics internes.
Elles servent à comparer la visibilité, jamais à inférer un chiffre d'affaires.

## 5. Scraperie : validation, pas motif d'arrêt

Scraperie est un comparable important parce que sa FAQ décrit une
expédition directe par des fournisseurs européens, américains ou chinois,
avec colis séparés possibles. Le site reprend précisément le territoire
souvenir-first : émotion, matière, composition et « atelier des beaux
souvenirs ».

Pourtant, le snapshot SEMrush n'estime que 58 visites organiques et 32 mots-clés
sur 214 PDP publiques. Le nombre de PDP surestime en plus les concepts : des
couleurs de massicot disposent d'URL distinctes. Aucun paid, revenu, AOV,
conversion ou réachat n'est observé.

**Conclusion corrigée** : Scraperie valide qu'un acteur peut construire ce
positionnement en dropshipping. Sa présence isolée n'est pas un signal négatif
et sa faible estimation SEMrush ne prouve pas un échec. Ce comparable sert à
lire les prix, le catalogue et l'opération ; c'est la structure économique
observée, pas son existence, qui déclenche le `STOP`.

## 6. Personas et critères de décision

### Persona A — gardienne d'un souvenir

Elle veut transformer photos et moments en album ou cadeau cohérent. Elle
craint les couleurs trompeuses, un kit générique, les éléments incompatibles
et le résultat amateur. Elle achète une méthode, une palette et une preuve du
résultat, pas seulement des stickers.

### Persona B — scrappeuse collectionneuse

Elle connaît les marques, attend les nouveautés, veut compléter une collection
et exige un stock exact. Sa fidélité va naturellement aux stockistes capables
de fournir rapidement la référence et ses compléments.

### Conséquence

- La débutante est déjà servie par les kits, tutoriels et projets de Fée du
  Scrap, ainsi que par l'inspiration de Florilèges.
- L'experte exige des marques, du stock et des références exactes qu'un
  catalogue AliExpress générique ne peut pas promettre honnêtement.

## 7. Différenciation et contradiction opératoire

Une différenciation radicale n'est pas exigée par principe. Un meilleur choix,
une exécution plus propre, une navigation claire ou une offre mieux construite
peuvent suffire lorsque l'économie est bonne. Un concurrent similaire isolé ne
ferme donc pas le marché.

L'offre la plus séduisante serait :

> événement → ambiance → format → niveau → kit personnalisable, avec rendu
> couleur/matière réel, liste exacte, compatibilité et résultat fini.

Mais cette promesse impose :

1. un kitting cohérent et contrôlé ;
2. une expédition groupée et prévisible ;
3. une vérité matière/couleur vérifiée ;
4. des designs originaux ou licenciés ;
5. des substitutions maîtrisées en cas de rupture ;
6. un contenu original reliant chaque projet à sa nomenclature.

Le dropshipping multi-fournisseurs produit l'inverse : colis séparés, couleurs
ou matières hétérogènes, délais divergents et faible maîtrise du kit. Construire
la promesse correctement reviendrait à stocker, assembler ou sous-traiter le
kitting en Europe.

## 8. Score Kraken indicatif

| Dimension | Score /3 | Motif |
|---|---:|---|
| Demande commerciale propre | 1 | marché réel, total propre non reproductible |
| Intensité du problème | 2 | désir émotionnel réel, urgence faible |
| Valeur du résultat | 0 | cœur catalogue autour de 5–14 EUR ; panier élevé non prouvé |
| Concurrence accessible | 2 | marché validé ; un seul comparable drop n'est pas bloquant |
| Différenciation défendable | 2 | amélioration d'exécution possible ; pas besoin d'être totalement inédit |
| Marge / CAC | 0 | contribution par commande, CPC et AOV non prouvés sur un ticket très bas |
| Logistique | 1 | panier multi-SKU et cohérence de kit défavorables au drop |
| Conformité / IP | 2 | gérable avec exclusions, mais licences et chimie à contrôler |
| Potentiel contenu | 2 | tutoriels et projets riches, déjà bien exploités |
| Exécution Kraken | 1 | contradiction entre promesse et fulfillment |
| **Total** | **13/30** | score indicatif ; le STOP vient d'abord du prix/panier, pas du concurrent isolé |

## 9. Décision et conditions de réouverture

### Décision active

`STOP_PHASE_2` pour une boutique France catalogue dropshipping générique, avec
motif principal `STOP_PRIX_PANIER`. Le sourcing, l'arborescence et la
construction de site sont interdits sur ce dossier. Réouverture uniquement par
`/qualifie-idees`.

### Réouverture possible sous un autre modèle

Le marché pourrait être réétudié si les quatre conditions suivantes sont
réunies :

1. mix catalogue recentré sur des produits ou bundles à ticket supérieur, sans
   fabriquer artificiellement un pack ;
2. panier moyen réel ou testable, coûts livrés, marge contributive et CAC de
   rupture compatibles ;
3. CPC et demande commerciale propre remesurés avant toute phase profonde ;
4. fulfillment capable de livrer honnêtement un panier multi-produits.

Un modèle marque + stock/kitting pourrait résoudre certains points, mais il
n'est pas la seule réouverture possible et ne constitue pas un GO actuel.

## 10. Preuves et limites

- SERP : `competitor-profiles/raw/serp-scrapbooking/2026-08-08/`.
- Scraperie : `competitor-profiles/raw/scraperie/2026-08-08/`.
- Variations Créatives :
  `competitor-profiles/raw/variations-creatives/2026-08-08/`.
- Florilèges Design :
  `competitor-profiles/raw/florileges-design/2026-08-08/seo/`.
- Panel historique et VOC :
  `competitor-profiles/workstreams/mercerie-scrapbooking.md` et profils
  concurrents associés.
- Volumes :
  `codex-chasse-clusters/runs/2026-08-08-kraken-catalogue-expansion-v2/keyword-volumes-fr.json`.

**[MANQUANT]** CPC actualisé, économie unitaire, analytics internes, ventes du
panel, fournisseurs exacts et mesure propre reconstruite du cluster. Aucun de
ces manques n'est comblé par extrapolation.
