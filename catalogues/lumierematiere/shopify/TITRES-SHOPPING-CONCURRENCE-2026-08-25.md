# Anatomie des titres Google Shopping — luminaires France (25/08/2026)

Relevé pour refondre les 120 titres de `lumierematiere.fr`.

**Corpus : 1 094 titres uniques**, carrousels Shopping France (`country_code: FR`), 9 requêtes :
`suspension bambou` · `suspension rotin` · `suspension bois` · `suspension verre` · `suspension céramique` ·
`suspension albâtre` · `lustre cristal` · `lustre anneau led` · `lustre salle à manger` · `plafonnier led salon`.

Source : Product Factory / DataForSEO, lecture du 25/08/2026. Carrousel Shopping ≠ annonces Search texte.
Données brutes : `shopping-titres-concurrence.json`.

---

## 1. Le titre est court

| Mesure | Valeur |
|---|---|
| Médiane | **51 caractères** |
| Moyenne | 61 |
| Quartiles | 34 (p25) · 76 (p75) |
| ≤ 70 caractères | **69 % des titres** |
| Maximum observé | 150 |

Le titre qui gagne la place tient en une ligne. Nos titres actuels sont dans la bonne longueur,
mais remplis de description au lieu de requêtes.

## 2. La dimension : verdict

**Question de Hakim : par quoi remplacer le `Ø` ?**

| Forme | Titres | Part |
|---|---|---|
| `40 cm` / `60cm` (nombre nu) | 133 | **12,2 %** |
| `Ø44 cm` / `Ø 44` | 67 | 6,1 % |
| `D44` / `D.40 cm` | 34 | 3,1 % |
| `diam. 30cm` / `diamètre` écrit | 33 | 3,0 % |
| `40 x 30` (L×H) | 16 | 1,5 % |
| **Au moins une dimension** | **223** | **20,4 %** |

**Deux enseignements :**

1. **80 % des titres n'annoncent aucune dimension.** La taille n'est pas un mot-clé de tête, c'est un
   attribut de variante. Google la lit dans `size` / les variantes, pas dans le titre.
2. Quand la dimension est écrite, la forme majoritaire est le **nombre nu suivi de `cm`** (12,2 %),
   deux fois plus fréquente que `Ø` (6,1 %). `Ø` est un usage de La Redoute, pas un usage de recherche.

Part de titres avec dimension, par requête :

| Requête | Avec dimension |
|---|---|
| suspension albâtre | 47 % |
| lustre anneau led | 32 % |
| suspension bambou | 26 % |
| plafonnier led salon | 21 % |
| lustre cristal | 20 % |
| suspension rotin | 17 % |
| suspension céramique | 15 % |
| lustre salle à manger | 12 % |
| suspension bois | 11 % |

**Conséquence pour nous :** nos titres portent des **plages** (`Ø 20 à 40 cm`), ce qui n'existe nulle part
dans le corpus. Une plage n'est pas un produit, c'est un axe de variante. À retirer du titre.

## 3. Ce que le titre contient vraiment

| Attribut | Titres | Part |
|---|---|---|
| **Matière** (bambou, rotin, verre, cristal, céramique…) | 679 | **62,1 %** |
| **Couleur / finition** (noir, doré, blanc, laiton, naturel…) | 402 | **36,7 %** |
| **Style** (moderne, scandinave, industriel, vintage…) | 321 | 29,3 % |
| **LED** | 302 | 27,6 % |
| **Pièce / usage** (salon, salle à manger, cuisine, chambre…) | 200 | 18,3 % |
| Dimmable / télécommande / réglable | 104 | 9,5 % |
| Douille E27 / E14 / G9 | 101 | 9,2 % |
| Nombre de lumières | 86 | 7,9 % |

La matière domine, la couleur suit. C'est exactement l'axe du catalogue Lumière Matière : bonne nouvelle.

## 4. Le premier mot est le type de produit

| Premier mot | Occurrences |
|---|---|
| suspension | 297 |
| lustre | 144 |
| plafonnier | 49 |
| lampe | 28 |
| *(marques : Atmosphera 24, Comely 24, Inspire 23, GOECO 18…)* | |

Seules les marques connues se mettent devant. Une marque que personne ne cherche perd la place
qu'elle occupe. **Lumière Matière ne doit pas apparaître dans le titre produit.**

## 5. Ponctuation

| Séparateur | Part |
|---|---|
| Virgule | **13,8 %** |
| Pipe `\|` | 6,5 % |
| Tiret ` - ` | 5,1 % |
| Slash ` / ` | 4,3 % |
| Cadratin `—` | **0,5 %** |

La virgule domine. Le cadratin est quasi absent : cohérent avec la consigne déjà appliquée au reste du site.

## 6. Deux écoles, et laquelle suivre

**École « bourrage » (3,2 % du corpus)** — pipe + répétition des mots-clés :

> `GEADI Lustre Salle à Manger Doré, 120cm Lustre Salon Moderne | 3000-6000K Dimmable LED Suspension Luminaire Cuisine Réglable, 12 Lustres Boule`
>
> `Lustre Industriel, 6 Lumières Suspension Luminaire Industrielle Noir Metal | Lustre Salon Chambre Cuisine Salle à Manger, Luminaire Plafonnier`

Ces titres viennent de vendeurs Amazon / dropshippers. Le **bourrage de mots-clés est contraire aux
règles Google Merchant Center** (« n'utilisez pas de texte promotionnel, de majuscules excessives ni de
mots-clés répétés dans l'attribut `title` »). Risque de refus, et illisible sur mobile. **À ne pas copier.**

**École « marque » (le reste)** — type + matière + attribut, court :

> `La Redoute Interieurs Suspension en bambou Ø45 cm`
> `Maisons du monde Suspension en bambou D44 style bord de mer`
> `Suspension éthnique bambou naturel LUSSIOL Doramu 1 lumière D.40 cm`
> `Inspire Suspension Palanga bambou beige`
> `Suspension bambou Margaux S naturel D60`
> `Lussiol Suspension Manille 40 cm`

C'est le registre à viser : lisible, une requête par bloc, pas de répétition.

## 7. Qui tient le carrousel

| Marchand | Cartes |
|---|---|
| Leroy Merlin | 204 |
| Amazon (vendeurs tiers) | ~98 |
| La Redoute | 48 |
| ManoMano | 45 |
| Maisons du Monde | 42 |
| Cdiscount | 38 |
| Lustria | 30 |
| luminaire.fr | 24 |

Grandes enseignes et marketplaces. Les indépendants qui passent (Lustria, luminaire.fr, Ma Suspension,
Nedgis) le font avec des titres **descriptifs et courts**, pas avec du bourrage.

---

## 8. Gabarit recommandé par famille

Règles communes : type de produit en tête · matière juste après · 50 à 70 caractères ·
virgules · pas de marque · pas de `Ø` · pas de plage de tailles · pas de cadratin ·
une seule dimension, et seulement si elle caractérise la pièce.

| Famille | Gabarit | Exemple |
|---|---|---|
| Suspensions bambou | `Suspension bambou {forme}, {couleur/finition}` | Suspension bambou tressé en vague, naturel |
| Suspensions rotin | `Suspension rotin {forme}, {usage ou couleur}` | Suspension rotin tressé, abat-jour tambour |
| Suspensions bois | `Suspension bois {forme}, {finition}` | Suspension bois tourné, ampoule apparente |
| Suspensions pierre | `Suspension pierre {forme}, {finition}` *(garder « effet pierre » si le corps n'est pas de la pierre)* | Suspension effet pierre, cylindre bois clair |
| Suspensions verre | `Suspension verre {type de verre}, {forme}` | Suspension verre fumé, globe |
| Suspensions métal | `Suspension métal {finition}, {forme}` | Suspension métal doré, dôme |
| Suspensions céramique | `Suspension céramique {motif/finition}, {détail}` | Suspension céramique blanche ajourée |
| Lustres cristal | `Lustre effet cristal {forme}, {finition}` | Lustre effet cristal LED, doré |
| Lustres anneau | `Lustre anneau LED {nb anneaux}, {finition}` | Lustre anneaux LED 3 cercles, noir |
| Lustres salon | `Lustre salon {style}, {matière/finition}` | Lustre salon moderne, globes verre doré |
| Plafonniers | `Plafonnier LED {forme}, {pièce si vraie requête}` | Plafonnier LED rond, chambre |
| Lustres statement | `Lustre {forme} {finition}, {nb lumières}` | Lustre sputnik noir et laiton, 8 globes |
| Suspensions modernes | `Suspension design LED, {forme}` | Suspension design LED, barres croisées |

**Le mot de pièce** (salon, salle à manger, cuisine, chambre) n'apparaît que dans 18 % des titres, mais
il porte du volume sur `lustre salle à manger` et `plafonnier chambre`. À réserver aux fiches dont
l'usage est réellement celui-là, jamais en liste (« salon chambre cuisine couloir » = bourrage).

Volumes SEMrush à croiser : voir `MOTS-CLES-TITRES-2026-08-25.md`.

## 9. Limites

- Carrousel Shopping page 1 seulement, une lecture datée du 25/08/2026.
- Les carrousels répètent les mêmes cartes : les 1 094 titres sont dédoublonnés à l'identique,
  une même fiche peut rester présente sous deux libellés.
- Le corpus ne dit pas quel titre **convertit**, seulement lequel obtient une place.
- Les parts d'attributs sont mesurées par expression régulière : un synonyme non prévu est compté zéro.
