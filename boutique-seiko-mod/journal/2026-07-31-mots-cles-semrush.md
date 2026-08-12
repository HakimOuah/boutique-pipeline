# Mots-clés SEMrush — Maison Noirmont (`maisonnoirmont.fr`)

> **27/07/2026** — recherche seule. Aucune campagne créée, aucun projet payant lancé, aucun budget engagé.
> Base SEMrush : **France**, appareil **Ordinateur**, devise **EUR**, date de base 27 juil. 2026
> (rapport concurrent daté du 25 juil. 2026 — la date la plus récente que le compte gratuit expose).

---

## 0. ⚠️ À lire avant tout : le compte est en formule gratuite, le quota a sauté en cours de route

Le compte SEMrush de Hakim **n'a aucun abonnement actif**. `subscription-info` ne propose que
les forfaits Pro / Guru / Business — aucun n'est souscrit. Conséquences mesurées sur place :

| Limite constatée | Effet |
|---|---|
| **10 requêtes d'analyse par jour** | atteint après 10 appels ; message explicite : « Vous avez épuisé vos 10 requêtes gratuites » |
| **Analyse par lots plafonnée à 1 ligne** | j'ai bien saisi les 28 mots clés (compteur `28/100`), le tableau n'a rendu que la 1ʳᵉ ligne — « débloquez les résultats cachés » |
| **Keyword Magic Tool plafonné à 10 lignes** | les agrégats (nb de mots clés, volume total, KD moyen) sont visibles, mais seules les 10 lignes de plus fort volume sont détaillées |
| **Classements organiques plafonnés à 10 lignes** | idem pour `montre-avenue.com` |
| **KD affiché seulement sur 2 lignes / 10** | les autres lignes rendent `n/a` avec « Pour afficher les métriques, actualisez la page » — chaque actualisation coûte une requête |

**Le piège dans lequel je suis tombé, et qu'il faut connaître :** une fois le quota épuisé,
le Keyword Magic Tool **ne renvoie pas d'erreur** — il affiche `Tous les mots clés : 0`,
un tableau vide, et rien d'autre. Quatre requêtes se sont ainsi vidées silencieusement
avant que je ne détecte la panne :

- `montre sans logo` → **0 rendu — NON MESURÉ**
- `nh35` → **0 rendu — NON MESURÉ**
- `montre plongeuse` → **0 rendu — NON MESURÉ**
- `seiko mod` → **0 rendu — NON MESURÉ**

J'ai confirmé le diagnostic avec un témoin volontairement massif (`chaussures`, qui pèse
des centaines de milliers de recherches en France) : **il a rendu 0 lui aussi**, et la
modale de quota s'est affichée. **Ces quatre zéros ne sont donc pas des volumes nuls.
Ils ne veulent rien dire.** Ne les recopier nulle part comme des mesures.

Conformément à la consigne, je me suis **arrêté là** : aucun contournement, aucune saisie
d'identifiant, aucun autre compte.

### Ce qui a réellement été mesuré

| # | Requête | Ce qu'elle a rendu |
|---|---|---|
| 1 | Vue d'ensemble — `montre hommage` | fiche complète (volume, KD, CPC, densité concurrentielle, intention, répartition pays) |
| 2 | Keyword Magic — `montre hommage` (requête large) | agrégats + 10 lignes |
| 3 | Keyword Magic — `montre automatique` (requête large) | agrégats + 10 lignes |
| 4 | Classements organiques — `montre-avenue.com` | agrégats + 10 lignes |

**4 grappes sur 5 restent donc non mesurées.** Le détail grappe par grappe est en §2 à §6,
avec la mention explicite de ce qui manque.

---

## 1. Grappe 1 — Hommage sans logo

### 1.1 Vue d'ensemble : `montre hommage` (MESURÉ)

| Métrique | Valeur |
|---|---|
| **Volume France** | **90 / mois** |
| Volume total tous pays | 180 — FR 90, BE 20, CA 20, CH 20, LU 20, IT 10 |
| **Difficulté SEO (KD)** | **12 % — « Très facile »** |
| **CPC** | **0,39 €** |
| **Densité de la concurrence publicitaire** | **1,00** (maximum de l'échelle 0–1) |
| Intention | **Informationnelle** |
| PLA / Annonces | `n/a` (aucun historique d'annonce remonté) |
| Tendance 12 mois | irrégulière, pic net en fin de série |

Deux choses à ne pas confondre dans ce tableau. **La densité de concurrence est à 1,00**,
c'est-à-dire saturée — mais **le CPC est à 0,39 €**, c'est-à-dire dérisoire. Cette
combinaison décrit un mot clé sur lequel beaucoup d'annonceurs sont techniquement
présents (souvent en requête large ou en Performance Max, sans l'avoir choisi) alors que
personne ne se bat vraiment pour le clic. Ce n'est pas un mot clé cher. C'est un mot clé
petit.

Et l'intention est marquée **Informationnelle**, pas transactionnelle : le Français qui
tape « montre hommage » cherche d'abord à **comprendre ce que le mot veut dire**, ou à
trouver l'hommage d'un modèle précis. Il n'est pas encore en train d'acheter.

### 1.2 La famille `montre hommage` en requête large (MESURÉ)

**Agrégats de la famille : 130 mots clés · volume total 550 / mois · KD moyen 9 %.**

Un volume total de 550 pour 130 expressions, c'est une **famille miette**. À titre de
comparaison, la seule expression `montre automatique homme` pèse 9 900 (§3.1), soit
**dix-huit fois toute la grappe « hommage » réunie**.

| Mot clé | Intention | Volume FR | KD % | CPC (EUR) | Concurrence | Marque tierce |
|---|---|---|---|---|---|---|
| montre hommage | Info | 90 | 12 | 0,34 | 1,00 | — |
| montres hommage | Info | 90 | 6 | 0,24 | 1,00 | — |
| montre hommage rolex | n/a | 50 | n/a | 0,60 | 1,00 | ⚠️ Rolex |
| montre hommage panerai | n/a | 30 | n/a | 0,00 | 0,99 | ⚠️ Panerai |
| montre hommage audemars piguet | n/a | 20 | n/a | 0,00 | 1,00 | ⚠️ Audemars Piguet |
| montre hommage daytona | n/a | 20 | n/a | 0,00 | 1,00 | ⚠️ Rolex (Daytona) |
| montre hommage johnny hallyday | n/a | 20 | n/a | 0,00 | 1,00 | ⚠️ nom de personnalité |
| montre hommage nautilus | n/a | 20 | n/a | 0,00 | 1,00 | ⚠️ Patek Philippe (Nautilus) |
| montre hommage omega | n/a | 20 | n/a | 0,18 | 0,99 | ⚠️ Omega |
| montre hommage patek philippe | n/a | 20 | n/a | 0,00 | 1,00 | ⚠️ Patek Philippe |

`n/a` en KD et en intention = **non affiché par le plan gratuit**, pas « nul ».

**Le constat qui compte : 8 des 10 expressions de la grappe portent un nom de marque tierce.**
Retirer les marques de la grappe « hommage », c'est ne garder que `montre hommage` +
`montres hommage` = **180 recherches par mois en France**. La grappe « hommage sans
marque » n'existe quasiment pas en tant que demande spontanée.

### 1.3 Non mesuré dans cette grappe

`montre sans logo`, `montre cadran stérile`, `montre sans marque` — **aucune mesure
exploitable** (quota épuisé, cf. §0). À reprendre en priorité 1 demain.

### 1.4 Les mots que SEMrush associe à « hommage » (MESURÉ — non anticipé)

Le panneau latéral donne le nombre d'expressions de la famille contenant chaque mot :

| Mot | Nb d'expressions | Lecture |
|---|---|---|
| johnny | 10 | montres commémoratives Johnny Hallyday |
| gen | 7 | à élucider (« gen 1 / gen 2 » ? à vérifier) |
| hallyday | 7 | idem johnny |
| normal | 7 | à élucider |
| jh | 6 | initiales Johnny Hallyday |
| rolex | 6 | ⚠️ marque |
| zenith | 6 | ⚠️ marque |
| cartier | 5 | ⚠️ marque |
| el | 5 | Zenith **El** Primero |
| primero | 5 | Zenith El **Primero** |

**Découverte que nous n'avions pas anticipée, et qui est un piège :** le premier
pourvoyeur de trafic du mot « hommage » en France n'est pas l'horlogerie hommage — c'est
**Johnny Hallyday** (`johnny` 10 + `hallyday` 7 + `jh` 6 = 23 expressions sur 130,
soit ~18 % de la famille). Ces gens cherchent une montre-souvenir d'un chanteur mort. Ils
n'achèteront jamais une Noirmont. Si un jour on cible « montre hommage » en Search, il
faut **`johnny`, `hallyday` et `jh` en mots clés négatifs dès le premier jour.**

Second enseignement : `zenith` + `el` + `primero` (6/5/5) révèle une demande d'hommage au
**Zenith El Primero**, un chronographe. C'est le seul indice mesuré qui recoupe la famille
Chronographes du catalogue (cadran panda, VK63).

---

## 2. Grappe 2 — Intention technique (NON MESURÉE)

| Mot clé demandé | Statut |
|---|---|
| montre automatique NH35 | **non mesuré** |
| montre Miyota 8215 | **non mesuré** |
| montre mécanique automatique homme | **non mesuré** |
| montre automatique fond verre | **non mesuré** |
| calibre NH35 | **non mesuré** |

La requête `nh35` a été lancée mais elle est tombée après épuisement du quota : son
« 0 » est un artefact, pas une mesure (§0).

**Seul indice mesuré, indirect :** dans la famille `montre automatique` (§3), le mot
`squelette` apparaît dans **499 expressions**, et **aucun** nom de calibre (`nh35`,
`miyota`, `seiko` mis à part la marque) ne figure dans les 10 mots les plus fréquents.
C'est cohérent avec la doctrine notée en mémoire (« explicable-particulier, pas
technique-pro ») : **le particulier français ne cherche pas un calibre, il cherche un
effet visible.** Il tape `squelette`, pas `NH35`. Hypothèse à confirmer par la mesure,
mais elle va dans le sens de ce qu'on sait déjà.

---

## 3. Grappe 3 — Intention style (PARTIELLEMENT MESURÉE)

### 3.1 La famille `montre automatique` en requête large (MESURÉ)

**Agrégats : 22 185 mots clés · volume total 310 710 / mois · KD moyen 17 %.**

C'est **le** gisement. 310 710 recherches mensuelles contre 550 pour « hommage ».

| Mot clé | Intention | Volume FR | KD % | CPC (EUR) | Concurrence |
|---|---|---|---|---|---|
| montre automatique homme | Info | **9 900** | 29 | 0,38 | 1,00 |
| montre automatique | Info | **6 600** | 30 | 0,43 | 1,00 |
| montre homme automatique | Info | **5 400** | 26 | 0,38 | 1,00 |
| montre automatique femme | Info | 4 400 | 18 | 0,39 | 1,00 |
| montre automatique pour femmes | Info | 4 400 | 18 | 0,39 | 1,00 |
| montre pour femme automatique | Info | 4 400 | 21 | 0,39 | 1,00 |
| remontoir automatique pour montres | Info | **4 400** | 15 | 0,42 | 1,00 |
| **remontoir montre automatique** | Info | **4 400** | 19 | 0,42 | 1,00 |
| automatique montre homme | Info | 3 600 | 26 | 0,38 | 1,00 |
| montre remontoir automatique | Info | 3 600 | 18 | 0,42 | 1,00 |

Trois lectures :

1. **Le CPC de toute la famille tient dans une fourchette de 0,38 à 0,43 €.** C'est très
   bas pour un panier de 279–430 €. Même à 2 % de conversion, un CPC de 0,40 € donne un
   CPA d'environ 20 € — soit un rapport très favorable. **L'enchère n'est pas le
   problème sur ce marché ; la crédibilité de la marque l'est.**
2. **SEMrush classe tout en Informationnelle**, y compris `montre automatique homme` à
   9 900. Il faut le lire pour ce que c'est : sur ces requêtes le SERP est dominé par
   des guides et des comparatifs, pas par des fiches produit. **On n'achète pas la vente
   directe sur ces mots — on achète une audience à éduquer.** Cela recoupe exactement le
   levier « pédagogie au particulier » déjà identifié en mémoire.
3. **La demande « femme » est massive et symétrique de la demande « homme »** : 4 400 +
   4 400 + 4 400 = 13 200 sur les trois variantes féminines mesurées, contre 9 900 +
   5 400 + 3 600 = 18 900 pour les masculines. Le catalogue (53 montres, familles
   Classiques / Sport chic / Chronographes / Plongeuses / GMT) est décrit comme
   masculin. **Un tiers de la demande mesurée est féminine et le catalogue ne l'adresse
   pas.** C'est le plus gros écart offre/demande que cette mesure révèle.

### 3.2 Suggestions non anticipées, issues du panneau latéral (MESURÉ)

| Mot | Nb d'expressions dans la famille | Ce que ça ouvre |
|---|---|---|
| homme | 4 057 | segment principal |
| **seiko** | **1 378** | ⚠️ marque tierce, mais **1ᵉʳ modificateur non démographique** |
| femme | 1 230 | segment non couvert par le catalogue |
| **prix** | **748** | grappe 4 confirmée comme réelle |
| tissot | 701 | ⚠️ marque tierce |
| fossil | 668 | ⚠️ marque tierce |
| **cuir** | **609** | matière de bracelet — angle produit |
| **avis** | **560** | intention de réassurance / preuve sociale |
| **bracelet** | **505** | angle accessoire + variantes |
| **squelette** | **499** | **la trouvaille de cette mesure** |

Quatre entrées méritent une décision :

- **`squelette` (499 expressions)** — nous avions listé « montre automatique fond verre ».
  Le mot que les Français emploient réellement, en volume, c'est **squelette**. C'est le
  même produit vu de l'autre côté : le fond verre laisse voir le mouvement, la montre
  squelette montre le mouvement par le cadran. À vérifier contre le catalogue réel, mais
  si Noirmont a des cadrans ouverts, **c'est le mot à employer dans les titres, pas
  « fond verre »**.
- **`avis` (560 expressions)** — grappe entière que le brief n'avait pas prévue. Une
  marque inconnue qui vend à 279–430 € sans logo au cadran a un problème de confiance
  par construction. Il y a 560 expressions de gens qui cherchent des avis sur des
  montres automatiques. Angle éditorial évident, et cohérent avec la contrainte
  « promesses vérifiables » déjà en mémoire.
- **`cuir` (609)** et **`bracelet` (505)** — le bracelet est un modificateur plus
  fréquent que n'importe quel terme de style que nous avions listé. Le catalogue a
  jubilé, intégré, et 38 accessoires dont des bracelets. Sous-exploité.
- **`seiko` (1 378)** — ⚠️ voir §7. Signalé, non recommandé.

### 3.3 Non mesuré dans cette grappe

`montre plongeuse vintage`, `montre chronographe panda`, `montre bracelet intégré`,
`montre lunette cannelée`, `montre jubilé`, `montre GMT automatique` — **aucune mesure.**
(`montre plongeuse` a été tenté et est tombé dans le trou de quota.)

⚠️ **Intention ambiguë à surveiller quand on les mesurera :** `montre plongeuse` mélange
deux acheteurs qui n'ont rien en commun — celui qui veut le *style* plongeuse vintage à
300 €, et celui qui veut un vrai instrument de plongée certifié ISO 6425 à 2 000 €. Même
remarque, en plus net, pour `montre GMT` (voyageur / pilote) et `montre lunette cannelée`
(qui est un descripteur de Rolex Datejust avant d'être un descripteur générique — donc
requête crypto-marque).

---

## 4. Grappe 4 — Intention prix (NON MESURÉE)

| Mot clé demandé | Statut |
|---|---|
| montre automatique moins de 300 euros | **non mesuré** |
| belle montre automatique pas chère | **non mesuré** |
| montre automatique rapport qualité prix | **non mesuré** |

**Indice mesuré, solide :** `prix` apparaît dans **748 expressions** de la famille
`montre automatique` — 4ᵉ modificateur le plus fréquent, devant toutes les marques. La
grappe prix est donc **réelle et large**, il ne manque que la répartition fine.

Une réserve à garder en tête pour la mesure de demain : le catalogue démarre à **279 €**.
`montre automatique moins de 300 euros` cadre pile sur la borne basse du catalogue —
donc sur les seuls modèles d'entrée, et sur un chercheur qui optimise le prix. À
l'inverse `rapport qualité prix` attire quelqu'un qui accepte de payer s'il comprend
pourquoi. **La seconde intention vaut mieux que la première pour cette boutique**, même à
volume inférieur.

---

## 5. Grappe 5 — Accessoires (1 MOT CLÉ MESURÉ, ET C'EST LE MEILLEUR DU LOT)

### 5.1 MESURÉ, incidemment, via la famille `montre automatique`

| Mot clé | Intention | Volume FR | KD % | CPC (EUR) | Concurrence |
|---|---|---|---|---|---|
| **remontoir montre automatique** | Info | **4 400** | **19** | **0,42** | 1,00 |
| remontoir automatique pour montres | Info | **4 400** | **15** | **0,42** | 1,00 |
| montre remontoir automatique | Info | **3 600** | 18 | 0,42 | 1,00 |

**C'est le meilleur couple volume × difficulté × CPC de toute la mesure.**
4 400 recherches, KD 15–19 % (contre 29–30 % sur `montre automatique homme`), CPC 0,42 €.
Trois formulations qui cumulent 12 400 recherches mensuelles pour un seul produit
physique — un remontoir, déjà au catalogue parmi les 38 accessoires.

Et l'écart de difficulté est le point clé : **`remontoir` est 10 à 15 points de KD moins
cher à conquérir que `montre automatique homme`, pour la moitié du volume.** Pour une
marque neuve sans autorité de domaine, c'est là qu'on gagne d'abord.

### 5.2 Non mesuré dans cette grappe

`écrin montre`, `rouleau de voyage montre`, `bracelet jubilé 20mm`, `outil barrette montre`,
`coffret montre`, `boîte à montre` — **aucune mesure.** À faire demain : ce sont, avec le
remontoir, les mots les plus susceptibles de produire du chiffre à court terme.

---

## 6. « Seiko mod » — mesuré à part (NON MESURÉ)

`seiko mod`, `montre seiko mod`, `seiko mod france` — **aucune mesure exploitable.**
La requête `seiko mod` est tombée dans le trou de quota.

**Indice mesuré, et il est fort :** `seiko` apparaît dans **1 378 expressions** de la
famille `montre automatique` — premier modificateur après `homme`. La demande autour de
Seiko en France est donc massive. Mais l'indice ne dit **rien** sur la part de `mod`
là-dedans, et le brief a raison sur le fond : celui qui tape « seiko mod » veut un projet
de modification, pas une montre finie. Noirmont vend des montres finies.

**Ce que je retiens sans l'avoir mesuré :** l'intérêt de cette famille pour Noirmont n'est
pas son volume, c'est sa **qualification** — quelqu'un qui connaît le mot « mod » sait
déjà ce qu'est un cadran stérile et pourquoi une montre sans logo n'est pas un défaut.
C'est une audience à éduquer zéro. À mesurer, mais à ne jamais traiter comme le cœur.

---

## 7. ⚠️ Mots clés à nom de marque tierce — signalés, non recommandés

Mesurés dans cette recherche, par ordre de volume ou de fréquence :

| Terme | Où | Poids mesuré |
|---|---|---|
| seiko | famille `montre automatique` | 1 378 expressions |
| tissot | famille `montre automatique` | 701 expressions |
| fossil | famille `montre automatique` | 668 expressions |
| rolex | famille `montre hommage` | 6 expr. · `montre hommage rolex` = 50 vol., CPC 0,60 € |
| zenith (El Primero) | famille `montre hommage` | 6 expressions |
| cartier | famille `montre hommage` | 5 expressions |
| panerai | famille `montre hommage` | `montre hommage panerai` = 30 vol. |
| omega | famille `montre hommage` | `montre hommage omega` = 20 vol., CPC 0,18 € |
| audemars piguet | famille `montre hommage` | 20 vol. |
| patek philippe / nautilus | famille `montre hommage` | 20 + 20 vol. |
| daytona (Rolex) | famille `montre hommage` | 20 vol. |
| johnny hallyday / jh | famille `montre hommage` | 23 expressions |

Le cadre, rappelé sans ambiguïté : **enchérir sur une marque tierce comme mot clé est
licite dans l'UE ; l'écrire dans le texte d'annonce ne l'est pas**, et la jurisprudence
sanctionne l'annonce qui laisse croire à un lien commercial. À quoi s'ajoute la raison
qui devrait suffire : la doctrine Noirmont est de vendre une montre *sans* logo. Bâtir
l'acquisition sur le logo de quelqu'un d'autre la contredit frontalement.

**Recommandation : ne pas ouvrir cette porte.** Et surtout, mettre `johnny`, `hallyday`,
`jh` en **négatifs** — ce trafic est du bruit pur, pas une opportunité.

---

## 8. `montre-avenue.com` — le concurrent (MESURÉ)

### 8.1 Agrégats — Classements organiques France, 25 juil. 2026

| Métrique | Valeur |
|---|---|
| Mots clés organiques FR | **130** (**−18,24 %**) |
| Autres bases | US 5 · BE 3 |
| Trafic organique estimé | **380 / mois** (+0,53 %) |
| Coût du trafic équivalent | **252,30 €** |

### 8.2 Leurs 10 mots clés (les 10 seuls que le plan gratuit expose)

| Mot clé | Pos. | Trafic | Part | Volume FR | KD % | URL |
|---|---|---|---|---|---|---|
| montre avenue | 1 | 256 | 67,4 % | 320 | 16 | accueil |
| montres avenue | 1 | 88 | 23,2 % | 110 | 25 | accueil |
| montre rectangulaire femme vintage | n.l. | 5 | 1,3 % | 140 | 11 | `/products/montre-vintage-femme-rectangle-metal-doree` |
| montre homme design | n.l. | 5 | 1,3 % | 260 | 13 | `/products/montre-chronographe-quartz-design-homme-chic-finition-luxe` |
| montre snake | n.l. | 2 | 0,5 % | 70 | 15 | `/products/montre-luxe-femme-bracelet-serpent` |
| montre sport femme | 31 | 2 | 0,5 % | **3 600** | 22 | `/collections/montre-sport-femme` |
| avenue gousset | 5 | 2 | 0,5 % | 210 | 30 | `/collections/montre-a-gousset-homme` |
| montre homme chic | n.l. | 2 | 0,5 % | 320 | 19 | `/products/montre-chronographe-quartz-design-homme-chic-finition-luxe` |
| montre pédagogique 3 ans | 7 | 2 | 0,5 % | 110 | 12 | `/collections/montre-enfant-3-ans` |
| montre homme solaire | 23 | 1 | 0,3 % | 720 | 16 | `/collections/montre-solaire-homme` |

`n.l.` = position non lisible dans le rendu gratuit (badge de fonctionnalité SERP à la
place du rang).

### 8.3 ⚠️ Deux corrections au brief

**Correction 1 — ce n'est pas « le concurrent le plus proche ».**
Le brief le décrit comme « déjà installé sur les accessoires ». **La mesure dit le
contraire : zéro accessoire dans ses 10 premiers mots clés.** Ses pages qui classent
sont : montre vintage femme rectangulaire, montre homme design, montre serpent femme,
montre sport femme, montre à gousset, **montre enfant 3 ans**, montre solaire homme. Et
ses URL produit disent `quartz` en clair. C'est une boutique de **montres mode et cadeau,
majoritairement quartz, fortement féminine et enfant**. Noirmont vend de l'automatique
hommage à cadran stérile pour adulte. **Ce ne sont pas les mêmes clients.**
Il reste un voisin utile à observer (même thème FullStack 2.2, cf. `2026-07-25-mining-montre-avenue.md`),
mais **le traiter comme concurrent de référence sur les mots clés est une erreur de cadrage.**

**Correction 2 — ils ne sont pas « installés ».**
**90,5 % de leur trafic organique vient de leur propre nom de marque** (`montre avenue`
256 + `montres avenue` 88 = 344 sur 380). Hors marque, il leur reste **36 visites par
mois**, et leur stock de mots clés **recule de 18 % sur la période**. En référencement
non-marque, `montre-avenue.com` est à peu près à zéro. **Il n'y a pas de forteresse à
contourner ici** — ce qui est une bonne nouvelle, et qui devrait retirer toute urgence
défensive de la stratégie.

**Le seul enseignement vraiment transposable :** ils sont positionnés 31ᵉ sur
`montre sport femme` (**3 600 de volume, KD 22**) et 23ᵉ sur `montre homme solaire`
(720, KD 16). Ils ont trouvé des collections à fort volume et faible difficulté et ne
les ont pas converties en positions. La méthode est bonne, l'exécution non — et elle
confirme, indépendamment, le point de §3.1 : **la demande « femme » est là et personne
ne la sert bien.**

---

## 9. Recommandation de priorité — volume × intention × CPC

Le classement ci-dessous ne repose pas sur le volume seul. La règle appliquée : un mot clé
vaut d'être travaillé si **(a)** son volume est mesuré, **(b)** son KD est atteignable
pour un domaine neuf, **(c)** son CPC laisse une marge sur un panier de 279–430 €, et
**(d)** son intention correspond à ce que Noirmont vend réellement — une montre finie.

### Priorité 1 — attaquer maintenant, sur données mesurées

| Rang | Mot clé | Vol. | KD | CPC | Pourquoi celui-là |
|---|---|---|---|---|---|
| 1 | **remontoir automatique pour montres** | 4 400 | **15** | 0,42 € | meilleur KD de toute la mesure à ce volume ; produit au catalogue ; achat d'accessoire = ticket d'entrée sans risque de marque |
| 2 | **remontoir montre automatique** | 4 400 | 19 | 0,42 € | même produit, formulation la plus naturelle ; à traiter avec le n°1 sur une seule page |
| 3 | **montre remontoir automatique** | 3 600 | 18 | 0,42 € | 3ᵉ variante ; les trois ensemble = **12 400 / mois** sur une page unique |
| 4 | **montre automatique femme** | 4 400 | **18** | 0,39 € | KD 11 points sous l'équivalent homme, volume identique, et **le catalogue ne l'adresse pas** — décision produit avant décision SEA |

### Priorité 2 — le cœur, mais coûteux en autorité

| Rang | Mot clé | Vol. | KD | CPC | Réserve |
|---|---|---|---|---|---|
| 5 | **montre automatique homme** | 9 900 | 29 | 0,38 € | le plus gros volume mesuré, mais KD 29 et SERP éditorial : viser via contenu, pas via fiche produit |
| 6 | **montre homme automatique** | 5 400 | 26 | 0,38 € | même cible, KD légèrement plus tendre — meilleure porte d'entrée que le n°5 |
| 7 | **montre automatique** | 6 600 | 30 | 0,43 € | KD le plus élevé et intention la plus floue de la famille : à ne pas attaquer en premier |

### Priorité 3 — qualifié, minuscule, à traiter en contenu

| Rang | Mot clé | Vol. | KD | CPC | Rôle |
|---|---|---|---|---|---|
| 8 | **montre hommage** | 90 | **12** | 0,34 € | KD 12 : première position atteignable vite. Volume trop faible pour du SEA, mais c'est **la page qui explique le positionnement** — valeur de conversion, pas de trafic |
| 9 | **montres hommage** | 90 | **6** | 0,24 € | KD 6, le plus facile mesuré ; à couvrir par la même page que le n°8 |

### Priorité 4 — à mesurer avant de décider (donc non classé)

| Rang | Piste | Fondement |
|---|---|---|
| 10 | **montre automatique squelette** | `squelette` = 499 expressions mesurées dans la famille. **Volume propre non mesuré.** Meilleure piste nouvelle de la session : c'est le mot français de « fond verre », et il est déjà dans le catalogue |

### Ce qu'il faut faire mesurer demain, dans cet ordre

1. **Accessoires** — `écrin montre`, `coffret montre`, `boîte à montre`, `rouleau de voyage montre`, `outil barrette montre`, `bracelet jubilé 20mm`. Le remontoir a prouvé que cette grappe est la plus rentable ; il faut le reste.
2. **`montre automatique squelette`** et la famille `squelette` — la découverte de la session.
3. **Grappe 1 restante** — `montre sans logo`, `montre cadran stérile`, `montre sans marque`.
4. **Grappe 4 prix** — `rapport qualité prix` d'abord, `moins de 300 euros` ensuite.
5. **Grappe 3 style** — `chronographe panda`, `bracelet intégré`, `plongeuse vintage`, `GMT`, `jubilé`.
6. **`seiko mod`** et dérivés.
7. **La famille `femme`** — écart offre/demande le plus large qu'ait révélé la mesure.
8. **`avis`** — 560 expressions, grappe de réassurance non anticipée.

### Deux conclusions de méthode

**Le volume seul aurait fait choisir `montre automatique homme` (9 900). La mesure dit de
commencer par le remontoir** : moitié du volume, mais 10 à 14 points de KD en moins, un
produit déjà en stock, et un premier achat qui ne demande pas au client de faire
confiance à une marque inconnue pour 300 €.

**Et une contrainte à ne pas oublier : toute la famille `montre automatique` est classée
Informationnelle par SEMrush.** Sur ce marché, on ne récolte pas une intention d'achat
existante — on la fabrique en expliquant. Ce qui est exactement le levier déjà identifié
pour cette boutique, et confirmé ici par la donnée.

---

## 10. Traçabilité

| Ce qui est mesuré | Ce qui est supposé |
|---|---|
| Tous les chiffres des §1.1, §1.2, §1.4, §3.1, §3.2, §5.1, §8.1, §8.2 | Toutes les lectures d'intention client, les hypothèses de CPA, l'interprétation de `squelette` comme équivalent de « fond verre », le lien entre `zenith el primero` et la famille Chronographes |
| Les 4 rapports listés en §0 | La priorisation du §9, qui pondère des mots clés mesurés avec un jugement d'intention non mesurable |
| L'épuisement du quota et la nullité des 4 requêtes tombées | La projection selon laquelle les accessoires non mesurés se comporteront comme le remontoir |

**Aucun chiffre de ce document ne provient d'une estimation de ma part.** Les cases vides
sont annoncées comme vides. Les quatre `0` obtenus après épuisement du quota sont exclus
partout et ne figurent dans aucun tableau de mesure.
