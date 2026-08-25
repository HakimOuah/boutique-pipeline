# Convention de titre produit — Lumière Matière (25/08/2026)

Règle unique pour les 120 fiches. Vaut pour le titre Shopify, donc pour le flux Google Shopping.

**Trois relevés indépendants la fondent :**

| Source | Volume | Fichier |
|---|---|---|
| Titres Shopping concurrents France | 1 094 titres, 9 requêtes | `TITRES-SHOPPING-CONCURRENCE-2026-08-25.md` |
| Montre Avenue + Mille et une Nuisette (catalogues complets) | 364 + 777 titres | `GABARITS-BOUTIQUES-REFERENCE-2026-08-25.md` |
| Recherches associées et questions Google | 4 requêtes de tête | `serp-recherches-associees.json` |
| Volumes SEMrush France | *(en cours)* | `MOTS-CLES-TITRES-2026-08-25.md` |

---

## La grille

```
{Type} {forme} {couleur|finition} en {matière} à {détail}
```

Chaque emplacement n'accepte qu'une valeur **d'une liste finie et vérifiable sur la photo**.
Les emplacements sont facultatifs, **leur ordre ne varie jamais**.

| Emplacement | Valeurs autorisées |
|---|---|
| **Type** | `Suspension` · `Lustre` · `Plafonnier` |
| **Forme** | `globe` · `dôme` · `cloche` · `cylindre` · `anneau` · `anneaux` · `grappe` · `cascade` · `tube` · `sputnik` · `corolle` · `coupole` · `galet` · `disque` · `tressé` · `tressée` |
| **Couleur / finition** | `noir` · `blanc` · `doré` · `laiton` · `chrome` · `naturel` · `beige` · `noyer` · `fumé` · `opalin` · `ambre` · `céladon` |
| **Matière** | `bambou` · `rotin` · `bois` · `verre` · `verre fumé` · `céramique` · `métal` · `pierre` / `effet pierre` · `travertin` · `corde` · `paille` · `fibre` |
| **Détail** | `3 lumières` · `6 anneaux` · `abat-jour tambour` · `ampoule apparente` · `LED` · `télécommande` |

Un mot qui n'est dans aucune liste n'entre pas dans un titre.

---

## Les dix règles

1. **Le type de produit est le premier mot.** Sans exception.
   Montre Avenue 100 %, Mille et une Nuisette 99,6 %, corpus Shopping : `suspension` (297), `lustre` (144), `plafonnier` (49) en tête.

2. **Le premier mot est celui de la collection qui porte la fiche.** Une fiche de « Suspensions bambou » commence par `Suspension bambou`. Titre, page collection et flux Shopping portent alors la même requête. (71,7 % des titres Montre Avenue reprennent tous les mots de leur `product_type`.)

3. **Jamais la marque.** `Lumière Matière` n'apparaît dans aucun titre. Les deux boutiques de référence sont à 0 %, malgré un domaine à leur nom. Seules les enseignes réellement cherchées (Leroy Merlin, Atmosphera) se permettent la position 1.

4. **40 à 60 caractères. Plafond dur à 65.**
   Mille et une Nuisette : 777 titres, **aucun au-dessus de 60**. Montre Avenue : max 77. Corpus Shopping : médiane 51.
   Les titres à 150 caractères du corpus sont ceux des marketplaces en bourrage : école à ne pas suivre.

5. **Un seul bloc.** La virgule est autorisée mais rare, et seulement pour détacher un attribut secondaire court (une quinzaine de caractères). Jamais pour empiler un second titre.
   93,3 % / 81,6 % des titres de référence sont en un seul bloc.
   **Aucun pipe `|`. Aucun cadratin `—`. Aucun deux-points.**

6. **La matière est obligatoire quand elle existe.** Cible ≥ 70 %.
   62 % du corpus Shopping, 70,4 % chez Mille et une Nuisette. C'est l'axe du catalogue : c'est notre avantage naturel.

7. **La couleur ou la finition dès qu'elle discrimine.** Cible ≥ 60 %.
   Le corpus Shopping n'est qu'à 36,7 %, Mille et une Nuisette à 73,5 %. C'est là qu'on passe devant le marché, et c'est le critère d'arbitrage d'un acheteur à 149–499 €.

8. **Pas de dimension, sauf si elle caractérise la pièce.**
   Corpus Shopping 20,4 %, Montre Avenue 10,7 %, Mille et une Nuisette 6,7 %. Trois relevés, même verdict : la taille est un attribut de variante, pas un mot de titre. Google la lit dans les variantes.
   - **Le symbole `Ø` est interdit** : 6,1 % du corpus, contre 12,2 % pour le nombre nu. C'est un usage de La Redoute, pas un usage de recherche.
   - **Les plages sont interdites** (`Ø 20 à 40 cm`) : elles n'existent dans aucun des trois corpus. Une plage n'est pas un produit.
   - Si une dimension est vraiment nécessaire (pièce hors norme, XXL) : `120 cm`, nombre nu suivi de `cm`.

9. **Aucun mot d'ambiance.** Interdits : `élégance`, `raffiné`, `chic`, `charme`, `esprit`, `style luxe`, `design épuré`, `intemporel`, `unique`, `sublime`.
   Le défaut de Montre Avenue : 27,5 % de mots d'ambiance, et **onze titres où l'ambiance a remplacé l'attribut** (`Montre Quartz Homme Style Luxe`). Transposé, cela donnerait « Suspension Élégance Naturelle » : indistinguable de ses voisines de collection, rien à indexer.
   Un mot d'ambiance ne doit jamais **occuper** un emplacement de la grille. S'il reste de la place après, il ne sert toujours à rien.

10. **Casse : première lettre du titre seulement**, comme le reste du site (`Suspension bambou tressé, naturel`). Les deux boutiques de référence sont incohérentes sur ce point (37,3 % et 7,6 % de casse mixte) — c'est un défaut d'exécution, visible en page de collection. Le choix importe peu, l'appliquer aux 120 fiches importe.

---

## Ce qui est légitime et ne doit pas être confondu avec du remplissage

**Les mots de style qui sont de vraies requêtes** — 29,3 % du corpus Shopping :
`moderne` · `scandinave` · `industriel` · `vintage` · `bohème` · `japandi` · `design`.
Confirmés par les recherches associées : `lustre cristal moderne`, `lustre cristal ancien`, `suspension en verre vintage`.

**Le mot de pièce, quand l'usage est réellement celui-là** — 18,3 % du corpus :
`salon` · `salle à manger` · `cuisine` · `chambre` · `entrée`.
Confirmés : `suspension verre cuisine`, `suspension verre salon`, `lustre salle à manger bois`, `lustre pour salle à manger et salon`.
**Jamais en liste** (« salon chambre cuisine couloir » = bourrage, contraire aux règles Merchant Center sur l'attribut `title`).

**Le nombre de lumières, quand c'est l'axe de choix** : `suspension bambou 3 lampes` est une recherche associée réelle.

---

## Ce qu'on ne peut pas aller chercher

Les recherches associées des quatre têtes mesurées sont saturées de marques tierces :
`Leroy Merlin` · `IKEA` · `Maisons du Monde` · `Centrakor` · `GiFi` · `Conforama` · `Baccarat` · `Swarovski`.

Volume réel, mais **interdit en titre Merchant Center** (usurpation de marque). C'est du volume qui n'est pas à nous. À retirer de tout calcul de potentiel.

---

## Avant / après, sur nos fiches

| Aujourd'hui | Le problème | Cible |
|---|---|---|
| `Suspension effet pierre, galet plat sur tige de bois clair` (57 c.) | « galet plat sur tige de bois clair » n'est pas une requête | `Suspension galet effet pierre, tige bois clair` |
| `Suspension nuages en verre soufflé LED, Ø 20 à 40 cm` (52 c.) | plage + `Ø` ; « nuages » est un nom de modèle | `Suspension verre soufflé LED, blanc opalin` |
| `Suspension bambou tissée, Ø 40 à 100 cm` (39 c.) | la plage occupe la moitié du titre, aucune couleur, aucune forme | `Suspension bambou tressé en vague, naturel` |
| `Lustre anneau LED, Ø 20 à 91 cm` (31 c.) | plage aberrante (20 à 91), rien d'autre | `Lustre anneaux LED, blanc, télécommande` |
| `Suspension travertin à capot noyer, bois clair ou foncé` (55 c.) | « capot » n'est pas un mot d'acheteur | `Suspension cylindre travertin, bois clair ou noyer` |
| `Suspension boule d'épines dorées, Ø 65 cm` (41 c.) | nom d'invention, dans la collection Plafonniers | `Suspension boule dorée en métal, 65 cm` |

---

## Contrôle automatique avant publication

Un titre est refusé s'il :

- ne commence pas par `Suspension`, `Lustre` ou `Plafonnier` ;
- dépasse **65 caractères** ;
- contient `Ø`, `—`, `–`, `|`, ` : ` ;
- contient une plage de tailles (`\d+ à \d+ cm`) ;
- contient `Lumière Matière` ;
- contient un mot de la liste d'ambiance ;
- est identique à un autre titre du catalogue (les 120 doivent rester uniques) ;
- ne contient ni matière, ni couleur, ni forme (titre vide au sens du § 9).

`seo_title` = titre + ` | Lumière Matière`, coupé à 70 caractères.
