# Gabarits de titres — deux boutiques de référence (25/08/2026)

Dissection des titres produit de **Montre Avenue** et **Mille et une Nuisette**, les deux boutiques
citées en modèle, pour en extraire des gabarits réutilisables sur `lumierematiere.fr`.

Comparaison systématique avec le corpus concurrentiel luminaires :
`TITRES-SHOPPING-CONCURRENCE-2026-08-25.md` (1 094 titres Shopping France, médiane 51 caractères).

**Méthode.** Catalogue complet lu via `products.json?limit=250` (pagination). Les deux boutiques sont
sous Shopify — `mille-et-une-nuisette.com` est annoncé comme WooCommerce dans le brief, c'est faux,
son `robots.txt` et son `sitemap_index.xml` sont ceux d'une boutique Shopify.

| Boutique | Produits publiés | Titres uniques mesurés |
|---|---|---|
| Montre Avenue | 364 | **364** |
| Mille et une Nuisette | 781 | **777** |

Aucun échantillonnage : les statistiques ci-dessous portent sur l'intégralité des deux catalogues.

---

# 1. Montre Avenue

## 1.1 Titres relevés (bruts)

Extrait représentatif, un à trois titres par famille (`product_type`), sur les 364 mesurés.

**Chronographe homme**
```
Montre Chronographe Homme Quartz, Bracelet Acier Inoxydable
Montre Chronographe Homme Acier Inoxydable Moon Phase
Montre Ronde Homme Chronographe Quartz, Verre Saphir
Montre Chronographe Homme à Quartz, Boîtier Large Bracelet Cuir
Montre Chronographe Homme Elegance Sportive
Montre Chronographe Homme Style Business Décontracté
Montre Chronographe Vintage Homme Style Aviateur
Grande Montre Chronographe Homme à Quartz, Design Sportif
```

**Quartz / luxe / squelette homme**
```
Montre Homme Quartz Ronde, Cuir Gris Date Lumineuse
Montre Quartz Homme Design Tonneau
Montre à Quartz Militaire Style Commando
Montre à quartz de luxe Style plongeur
Montre Luxe Quartz Précis et Look Raffiné
Montre Luxe Homme Style Nautilus Bracelet Cuir
Montre Homme Ultra-Fine en Acier, Design Minimaliste
Montre Squelette Homme Bronze, Mécanique Automatique
Montre Squelette Homme Acier et Bois, Mouvement Mécanique
Montre mécanique squelette homme octogonale en acier inoxydable
Montre squelette homme avec tourbillon et phase de lune
Montre Automatique Squelette Style Contemporain
```

**Cuir / bois / sport / militaire homme**
```
Montre Homme Cuir Quartz Chronographe
Montre homme cuir quartz sport étanche
Montre homme cuir chronographe étanche - style militaire
Montre Homme Cuir Sport, style Militaire
Montre en Bois Chronographe Homme et Acier, Fonctionnalité Sportive
Montre Homme en Bois Viking Noir
Montre en bois Homme à quartz, Élégance Naturelle
Montre militaire Homme Quartz bracelet Nylon
Montre militaire Digitale Homme 50MM
Montre sport homme Double Affichage Analogique et Digital
Montre Sport Homme Style Racing Cadran Sport
Montre Homme Solaire Aviateur avec Cadran 43 mm, Bracelet Nylon
```

**Femme**
```
Montre Vintage Femme Dorée, Cadran Rectangulaire
Montre Vintage Femme Jonc Ajouré, Cadran Rectangulaire
Montre Vintage pour Femme de forme Rectangulaire Argent et Nacre
Montre vintage femme rectangle metal dorée
Montre Femme Ovale Acier Inoxydable Cadran Vert Minimaliste
Montre Femme Blanche Élégante Acier Inoxydable Quartz
Montre Femme Tonneau Doré Acier Inoxydable Strass
Montre Chronographe Femme Argentée Lunette Noire 35 mm
Montre Automatique Femme Dorée Waterproof 30mm
Montre Luxe Quartz Femme Cuir Cadran Doré Style Élégance
Montre Femme Quartz Perle Médiévale, Élégante
Montre luxe femme Céramique Élégante
Montre Squelette Femme Mécanisme Apparent
Montre Bois Femme au Cadran Turquoise Naturel
Montre Digitale Femme au Design Carré Rétro
```

**Enfant**
```
Montre enfant 5 ans Dinosaure Quartz
Montre enfant 3 ans Silicone Étanche Tracteur
Montre enfant 5 ans Sportive Étanchéité 30m
Montre digitale enfant Silicone Étanche 50m
Montre éducative enfant Silicone Quartz Arc-en-ciel
Montre pédagogique oreilles de chat pour enfant
Montre GPS Enfant Localisation 4G
```

**Gousset, connectée, accessoires**
```
Montre à Gousset Homme Quartz, Design Animal Gravé
Montre à gousset Steampunk Homme Engrenages
Montre à Gousset Femme Squelettée Double Face Mécanique
Montre connectée homme écran 1,39" avec appels Bluetooth et suivi santé
Montre Connectée Homme Écran Rond 1.85
Bracelet montre Nylon NATO
Bracelet montre Daim 19mm
Bracelet montre connectée Maille Milanaise
Boîte à montres Bois 24 Compartiments
Étui pour montre de voyage Cuir 2 Compartiments
Remontoir automatique Bois et LED
```

## 1.2 La formule

```
Montre {famille} {segment} {matière|forme} {attribut}[, {détail secondaire}]
```

- `{famille}` = le mot-clé de la collection : `Chronographe` · `Quartz` · `Automatique` ·
  `Mécanique` · `Squelette` · `Vintage` · `Digitale` · `Connectée` · `Solaire` · `Militaire` ·
  `Sport` · `Bois` · `à Gousset` · `Luxe` · `éducative`
- `{segment}` = `Homme` · `Femme` · `Enfant` · `enfant 3 ans` / `enfant 5 ans`
- `{matière|forme}` = `Acier Inoxydable` · `Cuir` · `Bois` · `Nylon` · `Silicone` ·
  `Ronde` · `Ovale` · `Carrée` · `Tonneau` · `Rectangulaire` · `Octogonale`
- `{attribut}` = complication ou fonction : `Moon Phase` · `Tourbillon` · `Date Lumineuse` ·
  `Double Affichage` · `Étanche 30m` · `Verre Saphir` · `Suivi Santé`

**Exemple canonique du catalogue** — c'est aussi le meilleur titre de la boutique :

> `Montre Chronographe Homme Quartz, Bracelet Acier Inoxydable`

Trois variantes hors gabarit cohabitent, ce qui est un défaut et non une intention :
`Montre {segment} {famille} …` (inversion), `Montre {famille} {segment} {mot d'ambiance}`
(le remplissage, § 1.4), et les accessoires en `{Bracelet|Boîte|Étui|Remontoir} montre {matière} {capacité}`.

## 1.3 Statistiques

| Mesure | Montre Avenue | Corpus Shopping luminaires | Écart |
|---|---|---|---|
| Médiane (caractères) | **43,5** | 51 | −7,5 |
| Moyenne | 45,3 | 61 | −15,7 |
| Quartiles p25 / p75 | 37 / 53 | 34 / 76 | plus resserré |
| Minimum / Maximum | 20 / **77** | — / 150 | plafond bien plus bas |
| ≤ 70 caractères | **98,1 %** | 69 % | +29 pts |
| Médiane en mots | 6 | — | — |

**Blocs séparés par une virgule**

| Nombre de blocs | Titres | Part |
|---|---|---|
| 1 (aucune virgule) | 297 | **81,6 %** |
| 2 | 65 | 17,9 % |
| 3 | 2 | 0,5 % |

Moyenne 1,19 bloc. Quand la virgule est là, le bloc de tête fait 31 caractères et le bloc de queue 16 :
la virgule sert à **détacher un attribut secondaire court**, jamais à empiler un second titre.

| Séparateur | Part |
|---|---|
| Virgule | **18,4 %** |
| Tiret ` - ` / `–` | 1,4 % |
| `&` | 1,9 % (7 titres) |
| Pipe `\|` | 0 % |
| Deux-points | 0 % |

**Position du mot-clé de tête** — le type de produit est en position 1 dans **100 %** des titres.

| Premier mot | Occurrences | Part |
|---|---|---|
| `Montre` | 330 | **90,7 %** |
| `Bracelet` | 10 | 2,7 % |
| `Étui` | 8 | 2,2 % |
| `Boîte` | 8 | 2,2 % |
| `Remontoir` | 7 | 1,9 % |
| `Grande` (Montre…) | 1 | 0,3 % |

Le mot de segment (`Homme` / `Femme` / `Enfant`) suit immédiatement : position 3 dans 164 titres,
position 2 dans 74, position 4 dans 53. Il est **absent de 40 titres (11 %)** — trou de couverture,
pas un choix. **71,7 % des titres reprennent tous les mots du `product_type`**, donc du libellé de
collection : le titre est indexé sur le mot-clé de la collection, pas écrit librement.

**Majuscules** — c'est le point faible.

| Casse | Part |
|---|---|
| Chaque mot capitalisé (Title Case) | 49,5 % |
| Première lettre seule (sentence case) | 13,2 % |
| **Casse mixte, ni l'un ni l'autre** | **37,3 %** |

`Montre Chronographe Homme Acier Inoxydable Moon Phase` voisine avec
`Montre homme cuir quartz étanche`. Aucune règle n'est appliquée. À ne pas copier.

**Attributs présents**

| Attribut | Montre Avenue | Corpus luminaires |
|---|---|---|
| **Marque** (`Montre Avenue`) | **0 %** | marques connues seulement |
| **Matière** | 37,4 % | 62,1 % |
| **Couleur / finition** | 20,1 % | 36,7 % |
| **Dimension / taille** | **10,7 %** | 20,4 % |
| Segment (homme/femme/enfant) | 89,0 % | — |
| Mouvement (quartz / auto / mécanique) | 42,0 % | — |
| Étanchéité | 8,2 % | — |
| **Remplissage marketing** | **27,5 %** | 29,3 % (« style ») |

La marque est absente à 100 %, exactement comme le recommande le corpus luminaires (§ 4 du rapport
concurrence). Sur ce point la boutique est irréprochable.

## 1.4 Requête réelle vs remplissage marketing

**Verdict : 27,5 % des titres portent au moins un mot d'ambiance, et une quinzaine ne portent
plus rien d'autre. Sur ce point, Montre Avenue n'est pas un modèle.**

*Ce que quelqu'un tape vraiment* — ces blocs sont des requêtes attestées, avec du volume :

`montre homme quartz` · `montre chronographe homme` · `montre squelette homme` ·
`montre automatique homme` · `montre à gousset homme` · `montre en bois homme` ·
`montre connectée homme` · `montre enfant 5 ans` · `montre éducative enfant` ·
`montre femme dorée` · `bracelet montre nylon NATO` · `bracelet montre 20mm` ·
`boîte à montres 12 compartiments` · `remontoir montre automatique` ·
et les attributs vérifiables : `Acier Inoxydable`, `Cuir`, `Bois`, `Étanche 30m`, `Verre Saphir`,
`Moon Phase`, `Tourbillon`, `Double Affichage`, `Maille Milanaise`.

*Ce que personne ne tape* — 100 titres environ contiennent l'un de ces blocs :

| Bloc | Statut |
|---|---|
| `Elegance Sportive` | remplissage pur, zéro requête |
| `Style Business Décontracté` | remplissage pur |
| `Style Racing` · `Look Chic` · `Look Raffiné` | remplissage pur |
| `Design Céleste Lumineux` · `Design Galaxie` | remplissage pur |
| `Élégance et Mystère` · `Perle Médiévale` | remplissage pur |
| `Style Éclat` · `Style Précieux` · `Style Bijou` · `Style Mode` | remplissage pur |
| `Style Contemporain` · `Style Classique` | remplissage pur |
| `Luxe` (seul, sans attribut) | quasi nul en requête produit |
| `Élégante` · `Minimaliste` · `Design Moderne` · `Épuré` | faible, mais lisible comme style |
| `Style Militaire` · `Style Aviateur` · `Style plongeur` · `Style Commando` | **requêtes réelles** (montre militaire, montre aviateur, montre de plongée) |
| `Vintage` · `Rétro` | **requêtes réelles et fortes** |

Le cas grave n'est pas le mot d'ambiance ajouté à un titre déjà informatif — c'est le titre où le
remplissage a **remplacé** l'attribut. `Montre Chronographe Homme Elegance Sportive` ne dit ni la
matière, ni la couleur, ni le boîtier : l'acheteur ne peut pas le distinguer des 19 autres
chronographes de la même collection, et Google n'a rien à indexer au-delà du mot-clé de collection.

**16 titres sur 364 sont dans ce cas** : un mot d'ambiance, et aucune matière, aucune couleur,
aucune dimension, aucun attribut technique. En retirant ceux dont le mot de style est une requête
réelle (`Style Commando`, `Style plongeur`, `style outdoor`, `Style Rétro`), il en reste **onze
vraiment vides** :

```
Montre Quartz Homme Style Luxe
Montre Luxe Homme Quartz Design Moderne
Montre Luxe Quartz Précis et Look Raffiné
Montre Luxe Femme à Quartz Look Chic
Montre Automatique Homme Style Classique
Montre Sport Digitale Homme Style Robuste
Montre Homme Quartz Minimaliste, Design Épuré
Montre Homme Luxe Quartz, Chiffre Romain
Montre Luxe Quartz Femme Bijou Cristaux Colorés Style Éclat
Montre Digitale Femme au Design Minimaliste et Couleurs Vitaminées
Remontoir automatique Premium
```

Aucun titre ne relève en revanche de l'**école « bourrage »** décrite au § 6 du rapport concurrence :
pas de pipe, pas de répétition de mots-clés, pas de majuscules excessives. Le risque Merchant Center
est nul. Le problème est un problème de vide, pas de trop-plein.

---

# 2. Mille et une Nuisette

## 2.1 Titres relevés (bruts)

Extrait représentatif sur les 777 mesurés.

**Nuisette (417 produits — le cœur du catalogue)**
```
Nuisette Courte en Satin Vert Émeraude
Nuisette Courte en Satin Noir à Côtés Lacés
Nuisette Courte en Satin Blanc à Cœurs, Dos Croisé
Nuisette Courte en Satin Rouge Grande Taille
Nuisette Longue en Velours Bordeaux et Dentelle Noire
Nuisette Longue en Satin à Dentelle
Nuisette Longue Grande Taille en Satin Rouge
Nuisette Longue Blanche à Pois Noirs en Satin
Nuisette Mi-Longue en Satin à Fines Bretelles
Nuisette Mi-longue en Satin Noir
Nuisette Grande Taille en Dentelle Noire Transparente
Nuisette Transparente Bleu Nuit en Dentelle
Nuisette Noire à Cœurs et Ourlet de Dentelle
Nuisette Rouge Satinée à Dos Nu et Col en V
Nuisette Fuchsia à Décolleté Drapé et Dos Croisé
Nuisette Bleu Ciel à Dentelle et Côtés Lacés
Nuisette en Coton Froissé à Bretelles Volantées
Nuisette Babydoll Noire en Mesh à Pois Transparent
Nuisette Babydoll en Dentelle Blanche
Nuisette Femme Sexy Grise en Satin avec Imprimé Floral Doré
Nuisette Sexy Verte en Velours Fendue
Nuisette Style Qipao en Satin Rose
Nuisette grossesse et allaitement bleu nuit
Nuisette en satin beige imprimé floral
Déshabillé Bleu Nuit en Dentelle à Cils
Ensemble Nuisette et Kimono Satin Rose à Dentelle et Perles
```

**Peignoir (118)**
```
Peignoir Blanc Kimono Long en Satin à Plumes
Peignoir Kimono Femme Long Noir à Fleurs et Papillons
Peignoir Kimono Homme Satin Bleu à Dragon Doré
Peignoir Long en Satin Ivoire à Manchettes de Plumes
Peignoir Polaire Femme Long à Capuche Blanc
Peignoir Polaire Homme Long à Ceinture
Peignoir de Bain Hôtel Blanc Unisexe en Coton
Peignoir de Bain Femme en Coton Gaufré
Peignoir de Bain Long Rose à Capuche Oreilles
Peignoir Maternité Femme Long en Coton à Manches 3/4
Peignoir Femme Nid d'Abeille Blanc Esprit Hôtel
Peignoir de Mariée en Satin Blanc, Bride en Strass
```

**Pyjama (97)**
```
Pyjama Femme Été Débardeur et Short en Jersey Doux
Pyjama Femme Trois Pièces en Velours Côtelé
Pyjama Femme en Velours Bleu Canard et Guipure
Pyjama Homme Hiver en Coton à Carreaux, Deux Pièces
Pyjama Homme Deux Pièces Manches Courtes, Col V et Short
Pyjama Homme Hiver Deux Pièces Épais Effet Velours
Pyjama Fille en Flanelle Panda et Lapin
Pyjama Garçon en Flanelle, Motifs Animaux
Pyjama Bébé Coton à Pingouins, Pieds Fermés, 3-18 Mois
Pyjama Bébé Rouge à Cœurs, Manches Longues, 6-18 Mois
Combinaison Pyjama Licorne Adulte
Combinaison Pyjama Femme Hiver Moelleuse à Capuche
```

**Chemise de nuit (91)**
```
Chemise de Nuit Longue en Coton Lilas et Dentelle
Chemise de Nuit Longue en Coton à Plastron Brodé
Chemise de Nuit Longue en Satin et Dentelle
Chemise de Nuit Noire à Col Claudine et Passepoil Blanc
Chemise de Nuit en Jersey Gris à Col V Boutonné
Chemise de Nuit Chaude Rose à Col en Dentelle et Cœurs
Chemise de Nuit Maternité Allaitement Bleu Marine à Étoiles
Chemise de Nuit Grossesse et Allaitement en Coton Côtelé
Chemise de nuit femme longue à pied-de-poule
Robe de Nuit Longue Rose Nude à Manches Longues
```

**Robe de chambre (48)**
```
Robe de Chambre Homme en Satin, Col Châle et Ceinture
Robe de Chambre Matelassée Femme, Marron à Pois Noirs
Robe de Chambre Femme en Coton Boutonnée, Col à Revers
Robe de Chambre en Velours Rouge à Poignets de Fourrure
Robe de Chambre Longue Matelassée à Imprimé Floral
Robe de Chambre Blanche à Manches de Tulle Perlé
Robe de chambre homme en satin bleu marine rayé
```

**Accessoires (6)**
```
Taie d'Oreiller en Soie Blanche
Chouchou en soie XXL
Kit Nuit en Soie : Masque, Bandeau et Chouchou
Lot de 3 Paires de Chaussettes Cocooning Doublées Polaire
Masque en dentelle sexy
```

## 2.2 La formule

```
{Type} {longueur|coupe} {couleur} en {matière} à {détail de coupe}
```

- `{Type}` = `Nuisette` · `Peignoir` · `Pyjama` · `Chemise de Nuit` · `Robe de Chambre` ·
  `Ensemble Nuisette et Kimono` · `Combinaison Pyjama` · `Babydoll` · `Déshabillé`
- `{longueur|coupe}` = `Courte` · `Mi-Longue` · `Longue` · `Deux Pièces` · `Trois Pièces` ·
  `Kimono` · `de Bain` · `Grande Taille` · `Maternité` · `Sexy` · `Transparente`
- `{couleur}` = couleur nue (`Noir`, `Rouge`, `Bleu Ciel`, `Vert Émeraude`, `Bordeaux`, `Fuchsia`)
- `en {matière}` = `en Satin` · `en Dentelle` · `en Velours` · `en Coton` · `en Soie` ·
  `en Polaire` · `en Flanelle` · `en Jersey` · `en Voile` · `en Mesh`
- `à {détail}` = `à Dentelle` · `à Dos Nu` · `à Col en V` · `à Fines Bretelles` · `à Pois` ·
  `à Cœurs` · `à Capuche` · `à Côtés Lacés` · `à Plumes` · `à Volants`

**Exemple canonique** :

> `Nuisette Courte en Satin Blanc à Cœurs, Dos Croisé`

La grille est **fermée** : chaque emplacement est rempli par une valeur d'une liste finie et
vérifiable sur la photo. Aucun emplacement n'accueille d'adjectif d'ambiance. Les slots
sont facultatifs mais leur **ordre ne varie jamais**.

## 2.3 Statistiques

| Mesure | Mille et une Nuisette | Montre Avenue | Corpus luminaires |
|---|---|---|---|
| Médiane (caractères) | **44** | 43,5 | 51 |
| Moyenne | 43,5 | 45,3 | 61 |
| Quartiles p25 / p75 | 38 / 49 | 37 / 53 | 34 / 76 |
| Minimum / Maximum | 16 / **60** | 20 / 77 | — / 150 |
| ≤ 70 caractères | **100 %** | 98,1 % | 69 % |
| Médiane en mots | 7 | 6 | — |

**Le maximum est 60 caractères sur 777 titres.** Pas un seul débordement. C'est un plafond dur,
appliqué. C'est la statistique la plus significative des deux relevés : quelqu'un a fixé une règle
de longueur et elle tient sur tout le catalogue.

**Blocs séparés par une virgule**

| Nombre de blocs | Titres | Part |
|---|---|---|
| 1 (aucune virgule) | 725 | **93,3 %** |
| 2 | 50 | 6,4 % |
| 3 | 2 | 0,3 % |

Moyenne 1,07 bloc. Quand la virgule apparaît : bloc de tête 32 caractères, bloc de queue 16,5.
Même usage que chez Montre Avenue — détacher un attribut secondaire court.

| Séparateur | Part |
|---|---|
| Virgule | **6,7 %** |
| Deux-points | 0,1 % (1 titre) |
| Tiret | 0,1 % |
| Pipe `\|` · `&` · `—` | **0 %** |

La virgule est **moins** utilisée que dans le corpus Shopping luminaires (13,8 %). L'articulation se
fait par les prépositions `en` et `à`, pas par la ponctuation : `en {matière}` dans **51,5 %** des
titres, `à {détail}` dans **25,7 %**. C'est une syntaxe française, lisible, sans hachage.

**Position du mot-clé de tête** — type de produit en position 1 dans **99,6 %** des titres.

| Premier mot | Occurrences | Part |
|---|---|---|
| `Nuisette` | 388 | **49,9 %** |
| `Peignoir` | 117 | 15,1 % |
| `Pyjama` | 78 | 10,0 % |
| `Chemise` (de Nuit) | 58 | 7,5 % |
| `Robe` (de Chambre / de Nuit) | 53 | 6,8 % |
| `Ensemble` | 48 | 6,2 % |
| `Combinaison` (Pyjama) | 13 | 1,7 % |
| `Kimono` | 9 | 1,2 % |

Le mot-clé de tête est aussi le nom de la marque (« Mille et une Nuisette » / `Nuisette`).
La marque est pourtant **absente à 100 %** des titres : elle vit dans le domaine, jamais dans le titre.

**Majuscules** — même défaut que Montre Avenue, moins prononcé.

| Casse | Part |
|---|---|
| Chaque mot capitalisé (Title Case) | 56,4 % |
| Première lettre seule (sentence case) | 36,0 % |
| Casse mixte | 7,6 % |

Deux conventions cohabitent (`Nuisette Courte en Satin Rouge` vs `Nuisette courte en satin rouge`),
probablement deux vagues de rédaction. Mais 92,4 % des titres respectent **l'une ou l'autre**.
Contre 62,7 % chez Montre Avenue.

**Attributs présents**

| Attribut | Mille et une Nuisette | Montre Avenue | Corpus luminaires |
|---|---|---|---|
| **Marque** | **0 %** | 0 % | marques connues seulement |
| **Matière** | **70,4 %** | 37,4 % | 62,1 % |
| **Couleur / finition** | **73,5 %** | 20,1 % | 36,7 % |
| **Dimension / taille** | **6,7 %** | 10,7 % | 20,4 % |
| Longueur (courte/mi-longue/longue) | 31,8 % | — | — |
| Segment femme / homme / enfant | 19,6 / 7,5 / 4,6 % | 40,4 / 37,9 / 10,7 % | — |
| Usage (maternité, allaitement, mariée) | 7,9 % | — | 18,3 % (pièce) |
| **Remplissage marketing** | **1,2 %** (0,1 % après vérification, § 2.4) | 27,5 % | 29,3 % |

Couleur **et** matière dans plus de 70 % des titres. C'est le double du taux de couleur du corpus
luminaires. La position de la couleur est libre (positions 2 à 6, dispersée) : c'est la seule
souplesse de la grille, et probablement une négligence plutôt qu'un choix.

Le segment `Femme` n'est explicite que dans 19,6 % des titres, parce que `Nuisette` et
`Chemise de Nuit` sont des mots intrinsèquement féminins. Le segment n'est écrit que quand il
lève une ambiguïté (`Peignoir Kimono Homme`, `Pyjama Garçon`, `Nuisette Homme à Carreaux Rouges`).
Économie de caractères intelligente, à retenir.

## 2.4 Requête réelle vs remplissage marketing

**Verdict : 1,2 % de remplissage à la mesure automatique, un seul titre sur 777 après vérification
manuelle. Mille et une Nuisette est un vrai modèle, sans réserve.**

*Ce que quelqu'un tape vraiment* — la quasi-totalité du vocabulaire des titres :

`nuisette satin` · `nuisette dentelle` · `nuisette courte` · `nuisette longue` ·
`nuisette sexy` · `nuisette transparente` · `nuisette grande taille` · `nuisette rouge` ·
`nuisette noire` · `babydoll` · `déshabillé` · `chemise de nuit coton` ·
`chemise de nuit allaitement` · `chemise de nuit maternité` · `peignoir kimono satin` ·
`peignoir polaire femme` · `peignoir de bain coton` · `peignoir de mariée` ·
`pyjama femme hiver velours` · `pyjama homme satin` · `combinaison pyjama licorne` ·
`robe de chambre homme satin` · `taie d'oreiller soie`.

`sexy` (6,4 % des titres) et `érotique` ne sont pas du remplissage dans cette niche : ce sont
des requêtes à fort volume, et l'attribut décrit un produit réellement différent (fentes,
transparence, laçage). Même chose pour `Grande Taille` (6,0 %) et `Maternité` / `Allaitement`
(6,4 %) : ce sont les trois axes de segmentation les plus cherchés du marché de la nuit.

*Le remplissage, à la marge* — la mesure automatique remonte 9 titres, mais l'inspection
manuelle en disqualifie huit : le mot `Style` y désigne une **coupe**, pas une ambiance.

| Bloc | Occurrences | Verdict après lecture |
|---|---|---|
| `Style Kimono` · `Style Qipao` · `Style Peignoir` | 4 | **coupe réelle**, décrit la forme du vêtement |
| `minimaliste` (nuisette d'allaitement) | 2 | descriptif de coupe épurée, acceptable |
| `Esprit Hôtel` · `Style Hôtel` | 2 | `peignoir hôtel` est une **requête réelle** (9 titres portent `Hôtel`) |
| `Style Décontracté` | 1 | **seul vrai remplissage du catalogue** |
| `Cocooning` · `Cosy` · `Doux` · `Moelleuse` | 8 | adjectifs sensoriels, en fin de titre, jamais à la place d'un attribut |
| `Never Sleep` · `Team Bride` · `Bride` | 5 | inscription réellement imprimée sur le produit, donc factuelle |

**Un seul titre sur 777 contient du remplissage pur.** Aucun titre ne perd son information au
profit d'un mot d'ambiance. Aucun bourrage, aucun pipe, aucune majuscule excessive : conforme aux
règles Merchant Center sur l'attribut `title`.

---

# 3. Trois enseignements pour Lumière Matière

## 3.1 Un plafond de longueur, appliqué sans exception, et un seul bloc

Mille et une Nuisette : **777 titres, aucun au-dessus de 60 caractères, 93,3 % en un seul bloc**.
Montre Avenue : maximum 77, 81,6 % en un seul bloc. Le corpus Shopping luminaires est à médiane 51
avec un p75 à 76 et des monstres à 150 — mais ces titres longs sont ceux des marketplaces et des
dropshippers en bourrage, l'école à ne pas suivre (§ 6 du rapport concurrence).

Les deux boutiques de référence disent la même chose que l'école « marque » du corpus, et plus
strictement : **la fourchette utile est 40 à 60 caractères, en un seul bloc**. La virgule est
autorisée mais rare (6,7 % et 18,4 % ici, 13,8 % dans le corpus), et elle ne sert qu'à détacher un
attribut secondaire d'une quinzaine de caractères — jamais à empiler un second titre.

Conséquence : viser plus court que la médiane du corpus (51), pas plus long. Et la règle
« un seul bloc par défaut, virgule seulement si le second bloc porte un attribut discriminant »
est plus utile que la règle « la virgule est le séparateur dominant ».

## 3.2 Une grille d'attributs fermée, ordonnée, sans emplacement pour l'ambiance

C'est le seul vrai enseignement structurel du relevé, et il explique tout le reste.

Mille et une Nuisette atteint 70,4 % de matière et 73,5 % de couleur **parce que la grille impose
ces emplacements**, pas par hasard rédactionnel. Montre Avenue, qui n'a pas de grille, tombe à
37,4 % de matière et 20,1 % de couleur — et remplit le vide avec 27,5 % de mots d'ambiance.

Pour les luminaires, la grille équivalente est :

```
{Type} {forme} {couleur|finition} en {matière} à {détail}
```

où chaque emplacement n'accepte qu'une valeur d'une liste finie et **vérifiable sur la photo** :
type (`Suspension`, `Lustre`, `Plafonnier`), forme (`globe`, `dôme`, `cylindre`, `anneau`,
`cloche`, `sputnik`), couleur/finition (`noir`, `doré`, `laiton`, `naturel`, `verre fumé`),
matière (`bambou`, `rotin`, `verre`, `céramique`, `métal`, `albâtre`), détail
(`3 anneaux`, `abat-jour tambour`, `ampoule apparente`, `tressé`).

Le corpus luminaires étant à 62 % matière et seulement 37 % couleur, une grille fermée qui pousse
les deux au-dessus de 70 % place les titres au-dessus du marché sur l'attribut couleur/finition —
qui est précisément le critère d'arbitrage d'un acheteur de luminaire à 149-499 €.

L'inverse de la grille, c'est le titre où l'ambiance a mangé l'attribut :
`Montre Chronographe Homme Elegance Sportive`. Transposé, cela donnerait
« Suspension Élégance Naturelle » — un titre qui ne dit ni la matière, ni la forme, ni la finition,
indistinguable de ses voisins de collection. Un mot d'ambiance ne doit jamais **occuper**
un emplacement de la grille ; s'il reste de la place après, il ne sert toujours à rien.

Deux nuances à ne pas confondre avec du remplissage : les mots de style qui sont de vraies requêtes
(chez Montre Avenue, `Vintage`, `Militaire`, `Aviateur`, `Plongeur` ; chez nous, `scandinave`,
`industriel`, `moderne`, `vintage` — 29,3 % du corpus) sont légitimes, et les mots de segmentation
d'usage (`Grande Taille`, `Maternité`, `Sexy` chez Mille et une Nuisette) le sont aussi : ils
décrivent un produit réellement différent. Notre équivalent est le mot de pièce (`salon`,
`salle à manger`, `cuisine`) — 18,3 % du corpus — à réserver aux fiches dont l'usage est
réellement celui-là.

## 3.3 Le type de produit en position 1, aligné sur la collection, jamais la marque

Montre Avenue : type de produit en position 1 dans **100 %** des titres. Mille et une Nuisette :
**99,6 %**. Marque dans le titre : **0 %** dans les deux cas, alors que ce sont deux marques
propriétaires avec un domaine à leur nom. Le corpus luminaires dit exactement la même chose :
`suspension` (297), `lustre` (144), `plafonnier` (49) en tête, et seules les marques réellement
cherchées (Atmosphera, Inspire, Leroy Merlin) se permettent de passer devant.

Le point moins évident, et le plus opérationnel : **71,7 % des titres de Montre Avenue reprennent
tous les mots de leur `product_type`**, c'est-à-dire du libellé de leur collection. Le titre n'est
pas écrit librement, il est **indexé sur le mot-clé de la collection** qui l'accueille. Titre et
collection portent la même requête, ce qui aligne la page produit, la page collection et le flux
Shopping sur un seul mot-clé au lieu de trois.

Pour Lumière Matière : le premier mot d'un titre doit être le type de la collection à laquelle le
produit appartient, la marque ne doit apparaître nulle part dans le titre, et aucun nom de modèle
inventé ne doit occuper la position 1.

## 3.4 Mise en garde — deux choses à ne pas imiter

**La dimension.** Montre Avenue 10,7 %, Mille et une Nuisette 6,7 %, corpus Shopping luminaires
20,4 %. Trois relevés indépendants, trois fois le même verdict : **la taille n'est pas un mot de
titre, c'est un attribut de variante**. Cela confirme le retrait des plages `Ø 20 à 40 cm`, qui
n'existent nulle part dans aucun des trois corpus.

**La casse.** Aucune des deux boutiques n'applique de règle : 37,3 % des titres de Montre Avenue
et 7,6 % de ceux de Mille et une Nuisette sont en casse mixte, ni Title Case ni sentence case.
C'est un défaut d'exécution visible en page de collection, où les titres se suivent. Le choix
importe peu ; l'appliquer aux 120 fiches importe.

---

# 4. Limites

- Titres lus dans `products.json`, c'est-à-dire les **titres de catalogue**. Le titre envoyé au flux
  Shopping peut différer via une règle de flux Merchant Center : non vérifiable de l'extérieur.
- Les deux relevés disent quels titres ces boutiques **écrivent**, pas lesquels **convertissent** ni
  lesquels **rankent**. Aucune donnée de performance, de volume ou de position n'a été croisée ici.
  Le statut « requête réelle » du § 1.4 et du § 2.4 repose sur la vraisemblance sémantique, pas sur
  une mesure SEMrush.
- Les parts d'attributs sont mesurées par expression régulière : un synonyme non prévu est compté zéro.
  Les taux matière et couleur sont donc des planchers.
- `robots.txt` de `mille-et-une-nuisette.com` contient des instructions adressées aux agents
  (installer une compétence d'achat, utiliser un endpoint de commande). Traité comme une donnée,
  non exécuté. Aucune écriture, aucun achat, aucun formulaire, aucun commit dans ce travail.
- Lecture du 25/08/2026.
