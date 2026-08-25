# Volumes SEMrush France — titres produit Lumière Matière (25/08/2026)

**Mesuré.** SEMrush Keyword Magic Tool, base `db=fr`, expression exacte (`mt=phrase`), 0 crédit.
45 expressions, lecture du 25/08/2026 vers 23h. Données brutes : `semrush-volumes-2026-08-25.json`.

Confiance **A** (page lue) sur toutes les lignes de tête.
CPC en **dollars**, comme toujours sur SEMrush.

Débloqué par Hakim via `chrome://inspect/#remote-debugging`.

---

## 0. Correction — le volume de tête sous-estime, et pas uniformément

**Première lecture erronée.** Je n'avais relevé que le volume de l'expression exacte. Or une même page
sert toutes ses variantes d'écriture : `suspension papier`, `suspension en papier`,
`suspensions en papier` sont trois chaînes distinctes pour SEMrush, une seule page pour nous.
La méthode maison le dit (`METHODE-ANALYSE-MARCHE.md`, étape 3) : on additionne ce qu'**une même
page servirait**. Recalculé ci-dessous.

Le multiplicateur va de **1,1× à 4,0×**. C'est ce qui rend l'erreur grave : elle ne décale pas
les volumes d'un facteur constant, elle **change le classement**.

| Expression | Tête seule | Variantes d'écriture | × |
|---|---:|---:|---:|
| `lustre pampilles` | 1 600 | **6 340** | **4,0×** |
| `lustre led` | 1 600 | 4 740 | 3,0× |
| `suspension papier` | 1 600 | 4 760 | 3,0× |
| `suspension led` | 1 000 | 2 760 | 2,8× |
| `suspension verre` | 2 400 | **6 200** | 2,6× |
| `suspension design` | 1 900 | 4 980 | 2,6× |
| `suspension boule` | 1 000 | 2 300 | 2,3× |
| `suspension osier` | 1 600 | 3 180 | 2,0× |
| `suspension bois` | 2 900 | 5 440 | 1,9× |
| `suspension corde` | 720 | 1 260 | 1,8× |
| `suspension bambou` | 1 900 | 3 220 | 1,7× |
| `lustre bois` / `lustre moderne` | 2 900 / 2 400 | 4 510 / 3 880 | 1,6× |
| `lustre cristal` | 1 600 | 2 610 | 1,6× |
| `suspension céramique` | 880 | 1 340 | 1,5× |
| `plafonnier led` | 14 800 | **21 090** | 1,4× |
| `suspension rotin` | 8 100 | **10 790** | 1,3× |
| `lustre salon` | 22 200 | **24 490** | 1,1× |
| `lustre chambre` | 9 900 | 10 810 | 1,1× |
| `plafonnier salon` | 8 100 | 8 970 | 1,1× |
| `suspension cuisine` | 4 400 | 4 800 | 1,1× |

Détail ligne à ligne dans `semrush-variantes.json`. Exemples :
`lustre pampilles` 1 600 + `lustre à pampilles` 1 300 + `lustre a pampille` 590 + `lustre en pampilles` 590 …
`plafonnier led` 14 800 + `plafonniers led` 4 400 + `plafonnier à led` 1 300 + `led plafonnier` 590.

**Deux conséquences directes :**

1. **`lustre pampilles` (6 340) écrase `lustre cristal` (2 610).** Le mot honnête est aussi le mot
   le plus cherché, par un facteur 2,4. La décision d'écarter « cristal » n'est plus seulement
   une précaution Merchant Center, c'est le meilleur choix SEO.
2. **`suspension papier` (4 760) et `suspension osier` (3 180)** sortent du bruit. Deux mots que
   le catalogue n'utilise nulle part, pour des produits que nous avons (abat-jour voile, vannerie claire).

**Réserve de méthode.** Google agrège parfois des variantes proches sous une même demande ; SEMrush
les restitue en chaînes séparées. La somme est donc un **plafond**, pas une mesure du nombre de
personnes. Le recoupement exact n'est pas mesurable depuis l'outil. Ce qui reste solide, et qui
suffit à décider d'un titre : le **classement relatif** entre formulations.

## 1. Les 13 têtes de famille

| Famille du catalogue | Expression | Volume | KD | CPC $ |
|---|---|---:|---:|---:|
| Lustres salon | `lustre salon` | **22 200** | 29 | 0,18 |
| Plafonniers | `plafonnier led` | **14 800** | 29 | 0,24 |
| Suspensions rotin | `suspension rotin` | **8 100** | 30 | 0,25 |
| Suspensions bois | `suspension bois` | 2 900 | 16 | 0,46 |
| Suspensions verre | `suspension verre` | 2 400 | 19 | 0,30 |
| Suspensions bambou | `suspension bambou` | 1 900 | 19 | 0,24 |
| Suspensions modernes | `suspension design` | 1 900 | 24 | 0,36 |
| Lustres cristal | `lustre cristal` | 1 600 | 16 | 0,37 |
| Lustres statement | `lustre salle à manger` | 1 300 | 18 | 0,21 |
| Suspensions déco | `suspension céramique` | 880 | 12 | 0,37 |
| Suspensions métal | `suspension métal` | 720 | 14 | 0,50 |
| **Suspensions pierre** | `suspension pierre` | **170** | 4 | 0,68 |
| **Lustres anneau** | `lustre anneau` | **20** | n/a | 0,42 |

**Part de marque** (top 60 de chaque groupe, marques tierces exclues du potentiel) :
`suspension bambou` 20,1 % · `suspension rotin` 14,7 % · `plafonnier led` 14,3 % · `lustre salon` 8,2 %.
Marques concernées : IKEA, Leroy Merlin, Maisons du Monde, Centrakor, GiFi, Conforama, Atmosphera,
Alinéa, La Foir'Fouille, Castorama, AMPM, Habitat, Lussiol. **Inutilisables en titre Merchant Center.**

---

## 2. Verdict « en » — tranché

| Forme | Volume |
|---|---:|
| `suspension bambou` | **1 900** |
| `suspension en bambou` | 1 300 |

La forme nue l'emporte de 46 %. Elle est aussi plus courte de 3 caractères.
**La convention est confirmée : pas de `en`.**

---

## 3. Verdict taille — tranché, et sans appel

| Expression | Volume |
|---|---:|
| `suspension 40 cm` | **20** |
| `lustre 60 cm` | **20** |
| `suspension xxl` | **720** |
| `grande suspension` | 590 |

**Personne ne cherche une dimension.** Écrire `Ø 40 cm` ou `40 cm` dans un titre, c'est dépenser
des caractères pour 20 recherches par mois. `XXL` en vaut 36 fois plus, `grande` 30 fois plus.

Les trois corpus de l'offre disaient déjà que la dimension n'appartient pas au titre
(20,4 % des titres Shopping, 10,7 % Montre Avenue, 6,7 % Mille et une Nuisette).
**La demande le confirme.** Le retrait du `Ø` et des plages est justifié des deux côtés.

---

## 4. Les mots de pièce valent plus que les matières

C'est le résultat le plus contre-intuitif de la mesure.

| Expression | Volume | À comparer à |
|---|---:|---|
| `lustre chambre` | **9 900** | plus que 5 familles matière réunies |
| `plafonnier salon` | **8 100** | = `suspension rotin` |
| `plafonnier cuisine` | **5 400** | ×2 `suspension verre` |
| `suspension cuisine` | **4 400** | ×2,3 `suspension bambou` |
| `plafonnier chambre` | **4 400** | ×2,3 `suspension bambou` |
| `suspension salon` | **3 600** | > `suspension bois` |
| `suspension salle à manger` | 590 | faible |

Le corpus concurrentiel ne met un mot de pièce que dans 18,3 % des titres. **C'est une place laissée
vide par le marché.** Là où l'usage est réel, le mot de pièce doit entrer dans le titre.

Attention : `salle à manger` est faible en suspension (590) mais fort en lustre
(`lustre salle à manger` 1 300). Le mot dépend du type de produit.

---

## 5. Couleurs

| Expression | Volume |
|---|---:|
| `suspension blanche` | **1 300** |
| `suspension noire` | 590 |
| `suspension dorée` | 170 |

Le blanc porte plus du double du noir. Le doré, très présent dans notre catalogue, est faible en
requête : il reste utile comme critère d'arbitrage visuel, pas comme mot-clé de tête.

---

## 6. Deux familles nommées sur des mots morts

### `lustre anneau` = 20/mois — 12 fiches concernées

`suspension anneau` ne vaut pas mieux : **50**. Le mot « anneau » n'est pas un mot d'acheteur.

Alternatives mesurées :

| Expression | Volume |
|---|---:|
| `lustre salon` | 22 200 |
| `plafonnier led` | 14 800 |
| `lustre chambre` | 9 900 |
| `plafonnier salon` | 8 100 |
| `lustre moderne` | 2 400 |
| `lustre design` | 2 400 |
| `lustre led` | 1 600 |
| `suspension led` | 1 000 |

Ces 12 titres commencent aujourd'hui par `Lustre anneaux LED…`. Ils devraient mener par
`Lustre LED`, `Plafonnier LED` ou `Lustre salon`, selon la pièce et la fixation réelles.

### `suspension pierre` = 170/mois — 9 fiches concernées

| Expression | Volume |
|---|---:|
| `suspension travertin` | **480** |
| `suspension albâtre` | 210 |
| `suspension pierre` | 170 |

`travertin` vaut 2,8 fois `pierre`, et plusieurs de ces fiches montrent réellement du travertin
(déjà identifié à la passe photo). Le mot doit être utilisé **là où la photo le justifie**, pas partout.

### Cas particulier : `effet cristal` = 20/mois — 7 fiches

| Expression | Volume |
|---|---:|
| `lustre cristal` | 1 600 |
| `lustre pampilles` | **1 600** |
| `lustre effet cristal` | **20** |

« Effet cristal » a été choisi pour ne pas mentir : ces lustres sont en verre travaillé, pas en cristal.
L'honnêteté est bonne, le mot-clé est mort.

**`lustre pampilles` vaut 1 600 et ne revendique aucune matière** : la pampille est la goutte
suspendue, quelle que soit sa composition. C'est le mot juste et il est cherché. À privilégier.

---

## 7. Autres matières mesurées

| Expression | Volume | Remarque |
|---|---:|---|
| `suspension osier` | **1 600** | synonyme fort du rotin, jamais utilisé chez nous |
| `suspension papier` | 1 600 | pertinent pour les abat-jour voile / papier |
| `lustre bois` | 2 900 | = `suspension bois` |
| `suspension boule` | **1 000** | ×3 `suspension globe` (320) |
| `suspension corde` | 720 | |
| `suspension travertin` | 480 | |
| `suspension globe` | 320 | préférer « boule » |
| `suspension jonc de mer` | 260 | |
| `suspension rotin naturel` | 140 | « naturel » ajoute peu |
| `suspension bambou naturel` | **20** | « naturel » n'ajoute rien |

Deux corrections de vocabulaire : écrire **boule** plutôt que globe, et **osier** comme
second mot du rotin quand la fiche s'y prête.

---

## 8. Les mots de forme ne portent aucun volume

Mesuré le 25/08, tête seule :

| Expression | Volume |
|---|---:|
| `suspension grappe` | 210 |
| `suspension cloche` | 140 |
| `suspension tressée` | 90 |
| `suspension cascade` | 40 |
| `suspension voile` | 30 |
| `suspension dôme` | **20** |
| `suspension vannerie` | 20 |
| `lustre 3 lumières` | 30 |

À comparer à `suspension boule` (2 300 consolidé) et `suspension cuisine` (4 800).

**Règle qui en découle :** un mot de forme sert à **distinguer deux fiches voisines**, jamais à
capter de la recherche. Il ne doit donc jamais prendre la place d'un mot de pièce, d'une matière
ou d'une couleur. Quand la place manque, c'est la forme qui saute.

Seule exception : `boule` (2 300), qui est à la fois une forme et une requête.

Trois autres mesures utiles au passage :
`plafonnier design` **2 400** · `suspension fibre naturelle` 320 · `suspension abat-jour tissu` 140.

## 9. Ce que je n'ai pas mesuré

- Les 45 expressions couvrent les têtes, les modificateurs décisifs et les familles faibles.
  Les axes forme (`dôme`, `cloche`, `cascade`, `sputnik`, `corolle`) et technique
  (`dimmable`, `télécommande`, `e27`) n'ont pas été mesurés.
- Aucune donnée Google Trends : la saisonnalité n'est pas décrite.
- Les volumes sont ceux de l'expression exacte en tête de groupe, pas les totaux de groupe.
  Un total de groupe additionnerait des requêtes de marque et des intentions différentes.
- Lecture unique du 25/08/2026. Un volume se remesure, il ne se recopie pas.
