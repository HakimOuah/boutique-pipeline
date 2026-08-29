# Validation en aveugle sur 3 graines supplementaires

**Date : 2026-08-29** · Prealable a la resiliation de SEMrush. Complete le test `hamac` du meme jour.

Protocole : trois graines **jamais mesurees**, choisies parmi les candidats en attente de la shortlist UNIVERS, dont je ne connaissais aucun piege au lancement. Chaine DataForSEO seule (`scripts/kw_dfs.py`), puis controle de parite SEMrush sur la meme graine, meme jour, meme base France, meme expression exacte.

Cout DataForSEO : **0,396 USD** pour les trois.

## Resultat d'ensemble

| Graine | Idees apres dedup. | Parite des themes | Piege revele en aveugle |
|---|---:|---|---|
| `hamac` (28/08) | 468 | **33/35** | Hamac pour chat, de poussette, bebe — 3 produits sous un mot |
| `terrarium` | 534 | **excellente** | **Terrarium a plantes vs terrarium a reptiles** — 2 marches |
| `paddle` | 648 | **partielle — voir §3** | Location, padel-tennis, Decathlon, sports adjacents |
| `coffre de toit` | 615 | **excellente** | Marques et enseignes ecrasantes, location, occasion |

## 1. `terrarium` — le meilleur cas

| Theme DataForSEO | Volume cumule | Occurrences SEMrush |
|---|---:|---:|
| `plante` | 13 520 | 4 402 |
| `tortue` | 12 920 | 2 253 |
| `gecko` | 2 500 | 942 |
| `serpent` | 2 200 | 781 |
| `terrestre` | 3 480 | 370 |
| `kit` | 1 720 | 905 |
| `lampe` | 1 540 | 978 |
| `pogona` | 1 460 | 830 |
| `exo` (marque Exo Terra) | 2 090 | 1 012 |

Les deux outils designent les **memes deux poles**, dans le meme ordre. Et le piege est majeur : sous le mot `terrarium` cohabitent le **terrarium a plantes** (deco, DIY, bocal, verre, mousse — ticket bas) et le **terrarium a reptiles** (tortue, gecko, pogona, serpent, lampe chauffante, tapis chauffant — autre rayon, autre ticket, autre acheteur). Additionner les deux produirait un consolide qui ne correspond a aucune boutique reelle.

Tete : SEMrush 22 200 · DataForSEO 27 100 -> **x1,22**.

## 2. `coffre de toit` — parite quasi parfaite

| Theme | DataForSEO (volume) | SEMrush (occurrences) |
|---|---:|---:|
| `norauto` | 10 530 | 1 101 |
| `thule` | 6 740 | 1 679 |
| `bermude` | 5 490 | 1 135 |
| `location` | 4 580 | 512 |
| `feu vert` | 2 900 | 627 |
| `occasion` | 1 880 | 425 |
| `serrure` | 1 710 | 391 |
| `audi` / `renault` / `bmw` / `dacia` | ~4 700 | ~1 355 |

Meme liste, meme hierarchie. Le dossier est **presque entierement compose de marques, d'enseignes, de location et d'occasion** — un net de marque le viderait. C'est un verdict utile, obtenu pour 0,132 USD.

Tetes : `coffre de toit` 22 200 -> 27 100 (**x1,22**) · `coffre de toit norauto` 5 400 -> 6 600 (**x1,22**) · `coffre de toit thule` 3 600 -> 4 400 (**x1,22**) · `coffre de toit souple` 2 400 -> 2 400 (**x1,00**).

## 3. `paddle` — le cas qui limite la conclusion

C'est ici que DataForSEO decroche, et il faut le dire nettement.

**Ce que les deux voient** : `location` (11 680 / 3 056 occurrences), `decathlon` (30 530 / 1 344), `gonflable`, `surf`, `kayak`, `board`, `stand`.

**Ce que SEMrush voit et que DataForSEO manque :**

| Terme | SEMrush | DataForSEO | Consequence |
|---|---|---|---|
| `kid paddle` | **6 600** — la bande dessinee belge | **0 idee** | Contamination culturelle totalement invisible |
| `pickleball` | 4 550 occurrences | 1 idee, 320 | Sport adjacent sous-detecte |
| `tennis` | 1 738 occurrences | 3 idees, 8 570 | Partiellement vu |

`kid paddle` est un manque **franc** : 6 600 recherches par mois pour une bande dessinee, invisibles dans les 1 000 lignes DataForSEO. Sur un dossier ou l'on aurait retenu `paddle` a 135 000 (DataForSEO) ou 74 000 (SEMrush), c'est du volume qu'on aurait porte au credit du marche sans le savoir.

Tete : SEMrush 74 000 · DataForSEO **135 000** -> **x1,82**. C'est le plus gros ecart des quatre graines, et il va dans le mauvais sens : DataForSEO surestime la ou il detecte le moins bien la contamination.

## 4. Un bug de notre outil, trouve et corrige

Le test a revele un defaut de `scripts/kw_dfs.py` : le depluraliseur ecrasait les mots francais invariables se terminant par -s ou -x.

    tennis -> tenni    bois -> boi    prix -> pri    temps -> temp    souris -> souri

Le regroupement restait **coherent** (la transformation s'applique partout de la meme facon), donc les volumes n'etaient pas faux. Mais la table des themes devenait illisible : le rapport `hamac` du 28/08 affiche `boi` au lieu de `bois`. Corrige par une liste d'invariables (`INVARIABLES` dans le script). Les 3 graines ont ete recalculees depuis le cache, pour 0 USD.

## 5. Conclusion

**Trois graines sur quatre donnent une parite excellente.** La quatrieme, `paddle`, montre une limite reelle : DataForSEO detecte moins bien les contaminations **culturelles** (une bande dessinee, un nom propre) que les contaminations **produit** (chat, plante, tortue, marque, enseigne), qu'il trouve tres bien.

Lecture honnete de ce que ca implique :

- Sur un dossier **produit** — le cas de toutes nos boutiques — la chaine DataForSEO est fiable.
- Sur un mot **polysemique hors produit** (un titre d'oeuvre, un nom propre, un sigle), elle peut laisser passer du volume parasite.
- La parade ne coute rien : la **verification SERP**, deja obligatoire dans la methode, aurait montre la bande dessinee en page 1 de `paddle`. Aucun de nos verdicts ne repose sur le seul volume.

Mediane des tetes sur les quatre graines : **x1,22 a x1,25**, sauf `paddle` a x1,82. Le recalibrage propose (cluster 12 500, consolide UNIVERS 37 500, confort 50 000) tient.

## 6. Reserves

1. Quatre graines, c'est mieux qu'une, ce n'est pas une preuve statistique.
2. La comparaison de themes oppose des **volumes cumules** (DataForSEO) a des **comptages d'occurrences** (barre laterale SEMrush) : les deux grandeurs ne sont pas de meme nature. Elles servent a comparer des **classements**, pas des valeurs.
3. Seules les 1 000 premieres lignes DataForSEO sont lues, contre 100 chez SEMrush — mais SEMrush annonce des corpus plus larges sur `terrarium` (51 092) et `paddle` (117 073). L'exhaustivite reste a l'avantage de SEMrush.
4. `kid paddle` est le seul manque franc identifie. Il n'est pas exclu qu'il en existe d'autres sur des graines non testees.
5. Aucun controle de fraicheur des donnees entre les deux sources.
