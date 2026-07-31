# Vérification du catalogue contre la stratégie — Maison Noirmont

> **27/07/2026** — boutique `v42pzp-h4`. Périmètre : les **53 fiches montres actives**.
> Écritures effectuées : **métachamps `custom.couleur_cadran` et `custom.bracelet`** + **une description**
> (`quarante-et-un-sport-acier`, sauvegardée). Aucun SKU, prix, variante, titre, statut, média ni mapping DSers
> touché. Aucun thème modifié, aucune publication, aucune commande.
> Sources : API Admin Shopify, les 53 visuels de fiche, et les fiches fournisseur AliExpress d'origine.

---

## 0. Les deux comptes, en une ligne chacun

| Grappe SEMrush | Volume | Fiches réellement servies | Verdict |
|---|---:|---:|---|
| **montre squelette** | ≈ 8 400/mois | **0 sur 53** | ⛔ **Mirage.** Chantier de sourcing intégral. |
| **arabic dial / cadran chiffres arabes** | ≈ 15 500/mois | **0 sur 53** *(en vitrine)* | ⛔ **Pas une opportunité immédiate** — mais le fournisseur déjà mappé en vend. Chantier de sourcing **court**. |

---

## 1. « Montre squelette » — la grappe est un mirage

**Compte exact : 0 fiche sur 53.** Aucun handle à citer, et c'est le résultat.

Le piège annoncé dans le brief est confirmé, et il est encore plus net que prévu : **« fond verre » est une valeur
d'option de *fond de boîtier*, jamais un cadran.** Trois preuves indépendantes :

1. **La structure des options.** « fond verre » n'apparaît jamais seul : il est toujours accolé à un calibre dans une
   option nommée **« Mouvement & fond »** — `NH35 · fond verre`, `Miyota 8215 · 36 mm · fond acier`. C'est un choix
   de fond, pas de cadran.
2. **Le texte de la boutique le dit lui-même.** `noirmont-un-bronze-plongeuse` écrit :
   « **le fond verre laisse voir le mouvement tourner** ». Le mouvement se voit **par l'arrière**. C'est exactement la
   définition du fond transparent, et l'inverse d'un squelette.
3. **Les 53 visuels.** J'ai téléchargé et inspecté la face des 53 montres (planches de contact, 3 × 18). **Les 53 ont
   un cadran plein.** Aucun cadran ajouré, aucun cœur ouvert, aucun mouvement visible par l'avant.

Recherche plein texte sur tout le catalogue (titres, descriptions, balises SEO, valeurs d'options) —
`squelette`, `ajouré`, `skeleton`, `cadran ouvert`, `cœur ouvert`, `open heart`, `mouvement visible` :
**0 occurrence.** Contrôle de validité de la recherche fait avec un mot témoin présent dans une description
(`cramoisi` → 2 fiches), donc l'absence de résultat est une absence réelle, pas un moteur muet.

> **Conclusion.** 23 fiches proposent un **fond verre** ; **aucune** n'est une montre squelette. Écrire « squelette »
> sur une fiche à fond verre serait une affirmation fausse sur un attribut visible en photo — le client le verrait au
> déballage. Les 8 400 recherches/mois ne sont pas adressables avec le catalogue actuel. **Il faut sourcer, ou
> renoncer.**

---

## 2. « Arabic dial » — 0 en vitrine, mais le fournisseur en vend déjà

**Compte exact : 0 fiche sur 53 avec un cadran à chiffres arabes.**

- `arabe` / `arabes` : **0 occurrence** dans tout le catalogue.
- `chiffres` : **1 seule** occurrence — `trente-neuf-duo-classique-bicolore`, et elle dit
  « **chiffres romains** ». Le piège du brief est confirmé : c'est bien la fiche à « Index Romain » du fournisseur.
  *(À noter : le visuel de cette fiche montre des index **bâtons**, pas des chiffres romains. Sa description se
  contredit avec sa propre photo — signalé, non corrigé, hors périmètre.)*
- Les 53 visuels : **index bâtons, points et triangles** partout. Aucun chiffre, ni arabe ni romain.

### Le fait nouveau, trouvé en remontant chez le fournisseur

En vérifiant les fiches fournisseur, deux découvertes changent la nature du chantier :

| Source | Ce qu'elle porte |
|---|---|
| `1005005629655849` (BLIGER) — mappé sur **Noirmont Deux** | **Référence 2** a une lunette à **chiffres arabes orientaux** (١٢ ١١ ٩ ٨ ٧ ٣ ٢ ١) — sur la **lunette**, pas le cadran |
| `1005004626900765` (Tandorio) — mappé sur **Noirmont Un** et **Noirmont Un Bronze** | Montre **type pilote (flieger)** : **cadran noir à chiffres arabes 1-12** + couronne des minutes 5-55 |

**La deuxième est décisive.** Le fournisseur d'un produit **déjà mappé, déjà en ligne, déjà tarifé** vend un
cadran à chiffres arabes. Le chantier n'est donc pas « trouver un fournisseur » — il est « ouvrir une fiche sur
une référence dont le mapping DSers existe déjà ».

> **Conclusion.** Opportunité **non immédiate** — on ne peut pas se positionner aujourd'hui sur 15 500
> recherches/mois avec 0 cadran arabe en vitrine. Mais **le chantier de sourcing est court et le fournisseur est
> identifié**. Compte tenu du fait que personne ne tient mieux que la 4ᵉ position sur cette grappe, c'est la piste
> la plus rentable du lot — et elle passe par la résolution du point 5 ci-dessous.

---

## 3. Métachamps comblés

### `custom.couleur_cadran` — 45 → **52 / 53**

Sept fiches renseignées. **Aucune n'était dérivable du titre** : « Or », « Or rose », « Bicolore » y désignent le
**boîtier**, jamais le cadran — le piège du brief. J'ai donc mesuré la couleur **au pixel** sur les visuels, en
calibrant contre des fiches dont la valeur canonique est déjà connue.

| Handle | Valeur écrite | Preuve |
|---|---|---|
| `noirmont-un-plongeuse-acier` | **Noir** | luminance 15,3 % (réf. `integrale-noir` = Noir à 25,5 %) · 4 visuels concordants |
| `voyageur-or-gmt-3-maillons` | **Noir** | luminance 5,9 % |
| `voyageur-or-gmt-president` | **Noir** | luminance 11,0 % |
| `voyageur-bicolore-gmt-3-maillons` | **Noir** | luminance 13,3 % |
| `voyageur-bicolore-gmt-5-maillons` | **Noir** | luminance 7,8 % |
| `voyageur-or-rose-gmt-5-maillons` | **Blanc** | voir ci-dessous |
| `trente-neuf-duo-classique-bicolore` | **Or** | rgb(197,176,142) — écart < 6/canal avec son jumeau `trente-neuf-duo-dore`, déjà canoniquement **Or** |

**Le raccourci que j'ai failli prendre, et pourquoi il était faux.** Quatre Voyageur sur cinq ont un cadran noir ;
il était tentant de conclure « les Voyageur sont noirs ». **Le cinquième ne l'est pas.** `voyageur-or-rose-5-maillons`
a un cadran **blanc**. Sur la photo principale il mesure une chaleur trompeuse (saturation 9,3 %, teinte 30°) parce
que le boîtier or rose lui renvoie sa lumière — ce qui aurait pu le faire classer « Ivoire » ou « Rose ». Mesuré sur
la **photo au poignet**, sur fond neutre et sans réverbération, il donne rgb(232,229,222), **saturation 4,3 %**,
soit la signature de la référence `quarante-et-un-blanc-cuir` = **Blanc** (5,7 %). C'est le reflet qui était coloré,
pas le cadran.

**Forme canonique respectée** : aucune valeur nouvelle créée. Les 7 écritures réutilisent `Noir`, `Blanc` et `Or`,
déjà en place. La palette reste à 14 valeurs — aucune entrée en double dans la facette.

### `custom.bracelet` — créé, **48 / 53**

Définition créée à l'identique des quatre autres : `list.single_line_text_field`, accès vitrine `PUBLIC_READ`,
filtrable en admin. ID `gid://shopify/MetafieldDefinition/507132772690`.

Les valeurs viennent de `axes-guide-de-choix.md`, **non redérivées**. Le report est validé par réconciliation :
mes 53 affectations sur 48 fiches retombent **exactement** sur les sept comptes du livrable.

| Valeur canonique | Attendu | Écrit |
|---|---:|---:|
| Jubilé | 18 | **18** ✅ |
| Acier maille non précisée | 14 | **14** ✅ |
| Intégré | 7 | **7** ✅ |
| Caoutchouc | 7 | **7** ✅ |
| Cuir | 4 | **4** ✅ |
| Acier 3 maillons | 2 | **2** ✅ |
| Président | 1 | **1** ✅ |
| **Total affectations** | **53** | **53** sur **48 fiches** |

Cinq fiches portent deux bracelets (`quarante-et-un-sport-acier` acier + cuir ; quatre Chronos acier + caoutchouc) —
c'est pourquoi une liste, et non un texte simple. Forme longue « Acier maille non précisée » retenue plutôt que
l'abréviation « Acier maille n.p. » du livrable : c'est un libellé de facette, il s'affiche au client.

### Ce qui reste vide, et pourquoi

| Champ | Vides | Raison |
|---|---:|---|
| **`diametre`** | **9** — les 7 `Intégrale`, `noirmont-un-plongeuse-acier`, `noirmont-un-bronze` | **Constat confirmé, valeurs non inventées.** J'ai relu les 9 descriptions et les 9 balises SEO : **aucune mention de millimètre**, nulle part. Reste à 44/53. |
| **`couleur_cadran`** | **1** — `noirmont-deux-plongeuse-ceramique` | **Valeur retirée après vérification fournisseur** — voir §5. |
| **`bracelet`** | **5** — `noirmont-un-plongeuse-acier`, `noirmont-deux`, les 3 `Héritage` | Indéterminables : leurs titres qualifient le **boîtier**. Non devinées. |

**Le piège du diamètre a été re-tenu à l'écart.** La phrase « si vous portez d'habitude du 38 ou 39 mm » des six
`Quarante-et-Un` parle du **poignet du client**. Elle n'a produit aucune valeur ; ces montres restent à 41 mm,
d'après leur propre mention « Boîtier acier de 41 mm ». Aucune entrecorne de bracelet (18/20/22 mm) convertie en
diamètre de boîtier.

---

## 4. Une affirmation fausse corrigée — `quarante-et-un-sport-acier`

La fiche annonçait « **un bracelet intégré au poignet** » alors que ses options vendent
« Cadran blanc · **bracelet acier** » et « Cadran noir · **bracelet cuir M** ». Un bracelet intégré n'est ni l'un ni
l'autre : c'est un bracelet indémontable qui prolonge le boîtier — ce que sont les `Intégrale`, pas celle-ci.

Corrigé, et corrigé aussi sur le mouvement : la fiche annonçait « Seiko NH35 » seul alors qu'elle vend **NH35 ou
Miyota 8215**. La description dit maintenant les deux versions réellement vendues.

- Sauvegarde : `backup-description-quarante-et-un-2026-07-27.json`
- **Aucun titre SEO perdu** : `seo.title` et `seo.description` de cette fiche étaient **déjà `null`** avant
  intervention (vérifié avant écriture), et le sont restés. Le piège des 47 titres perdus ne s'est pas rejoué.
- Titre, options, prix, variantes : **non touchés**.

---

## 5. Noirmont Deux — débloqué, et le blocage n'était pas celui qu'on croyait

**Les 7 références sont identifiées.** Le mapping n'a pas eu besoin de DSers : l'URL fournisseur était déjà relevée
dans `renommage-variantes-2026-07-25.md` → `1005005629655849` (BLIGER).

**Mapping vérifié en direct, et il est exact.** Les 7 identifiants de propriété de la fiche AliExpress correspondent
un pour un aux SKU Shopify (`color 1` → `14-200005100` = `14:200005100#color 1`, etc.), et les 4 identifiants de
calibre correspondent aussi (`5-646979416` Miyota 8215, `5-2399342480` NH35, `5-5507616738` PT5000,
`5-57086108` Mingzhu 2813). Aucune ambiguïté sur l'identité du produit.

### Ce que sont réellement les 7 références

**Le fournisseur ne les nomme pas non plus.** Sur AliExpress elles s'appellent littéralement « color 1 » à
« color 7 ». L'opacité vient de l'amont — DSers l'a fidèlement recopiée, ce n'est pas un défaut de notre mapping.

Mais les visuels les distinguent sans équivoque. **Les 7 partagent un cadran identique — bleu ciel à motif de
bulles multicolores** (pastilles rouges, jaunes, roses, vert foncé, bleu clair massées dans la moitié basse). Elles
ne diffèrent que par **l'insert de lunette** :

| Référence | Ce qu'elle est |
|---|---|
| **Référence 1** | Lunette plongée bleu ciel, graduation 10-50, pastille de lume à 12 |
| **Référence 2** | Lunette **à chiffres arabes orientaux** (١٢ ١١ ٩ ٨ ٧ ٣ ٢ ١), disposition 12 h |
| **Référence 3** | Lunette plongée bleu ciel, graduation 10-50, piste des minutes complète |
| **Référence 4** | Lunette plongée bleu ciel, graduation 10-50, index plus fins que la 3 |
| **Référence 5** | Lunette bleu ciel à marquages **noirs** contrastés, graduation plongée |
| **Référence 6** | Lunette **GMT 24 heures** (2·4·6…22) |
| **Référence 7** | Lunette **12 heures à chiffres occidentaux** (1·2·3…11) |

### ⚠️ Le vrai blocage : la fiche ne montre pas le produit qu'elle vend

C'est le constat qui compte, et il dépasse la question des 7 références.

- **La fiche** montre, sur ses 5 visuels produit, une plongeuse **noire à cadran stérile**, lunette céramique noire,
  bracelet acier — et sa description parle d'« insert céramique ».
- **Le fournisseur** livrera, pour les 7 références sans exception, une montre à **cadran bleu ciel à bulles
  multicolores**.

Ce ne sont pas deux variantes du même produit : ce sont **deux montres différentes**. C'est pour cette raison que
j'ai **retiré** la valeur `couleur_cadran = Noir` que j'avais d'abord écrite d'après les visuels : ni « Noir » (ce
que la fiche montre) ni « Bleu » (ce qui serait expédié) n'est établi tant que la contradiction n'est pas tranchée.
Une facette fausse est pire qu'une facette incomplète.

**Le lettrage de la face** : le cadran est bien **stérile**, sans inscription de marque — la promesse est tenue. Le
lettrage visible est celui de la **lunette** (graduation de plongée 10-50), plus deux mentions marketing
**incrustées dans les images** (« CÉRAMIQUE INRAYABLE », « Insert céramique · Index lumineux »).

### Et le même défaut sur deux autres fiches, trouvé au passage

En re-vérifiant `noirmont-un-plongeuse-acier` — parce qu'après Noirmont Deux je ne pouvais plus faire confiance aux
visuels seuls — le même écart apparaît, mappage vérifié label par label et identifiant par identifiant :

| Fiche | Mappée sur | Ce que la fiche montre | Ce que le fournisseur livre |
|---|---|---|---|
| `noirmont-un-plongeuse-acier` | `1005004626900765` (Tandorio) `14:350686#steel case-no logo` | Plongeuse acier, lunette tournante, bracelet acier | **Montre type pilote**, cadran noir **à chiffres arabes**, **bracelet cuir** |
| `noirmont-un-bronze-plongeuse` | idem, `14:94#bronze case-no logo` | idem en bronze, « bracelet acier » | idem en bronze, **bracelet cuir** |

`couleur_cadran = Noir` reste juste sur ces deux fiches : le cadran est noir dans les deux lectures. En revanche
`bracelet = Acier maille non précisée` sur `noirmont-un-bronze` — valeur reprise du livrable, qui l'avait lue dans
la description — est **contredite par le fournisseur (cuir)**. Je l'ai laissée telle quelle, conformément à la
consigne de ne pas redériver les 48, mais **elle est à retrancher si l'arbitrage donne raison au fournisseur**.

> **Ce que ça change pour la décision.** Hakim n'a plus à trancher « brouillon ou pas » sur une inconnue : les 7
> références sont établies. La question est devenue **« quelle est la bonne source de vérité, nos visuels ou le
> fournisseur ? »**, et elle porte sur **3 fiches actives** (Noirmont Deux, Noirmont Un, Noirmont Un Bronze), soit
> 279-407 €. Je n'ai touché ni statut, ni titre, ni variante, ni média : **le constat est posé, l'arbitrage reste
> à Hakim.**

---

## 6. Montres devenues atteignables dans le guide de choix

| Axe | Avant | Après | Gain |
|---|---:|---:|---:|
| **Couleur de cadran** | 45/53 | **52/53** | **+7** |
| **Bracelet** | *axe inexistant* | **48/53** | **+48** |
| **Diamètre** | 44/53 | 44/53 | 0 (constat confirmé) |
| **Mouvement · Famille** | 53 · 53 | 53 · 53 | — |

**Montres qui gagnent au moins un axe de filtrage : 49 sur 53.** (Les 48 du bracelet, plus
`noirmont-un-plongeuse-acier` qui ne gagne que la couleur.)

### Effet sur le parcours retenu (Famille → Couleur)

| Indicateur | Avant | Après |
|---|---|---|
| Montres cachées, Q2 sur 3 familles | **1** (`trente-neuf-duo-classique-bicolore`) | **0** — 53/53 atteignables |
| Q2 posable aux **5** familles ? | Non : GMT 1 couleur (5 ∅), Plongeuses 3 (2 ∅) | **Oui** — GMT **3 couleurs, 0 ∅** · Plongeuses **3 couleurs, 1 ∅** |
| Montres atteignables, Q2 sur 5 familles | 45/53 | **52/53** |

**C'est l'objectif structurel atteint** : GMT (Noir 4 · Blanc 1 · Brun 1) et Plongeuses (Noir 2 · Bleu 2 · Vert 1)
ont maintenant assez de couleurs pour porter une deuxième question. **Tous les chemins peuvent avoir le même
nombre d'écrans**, au lieu de deux familles qui sautaient aux résultats.

**La seule montre encore hors d'atteinte est `noirmont-deux-plongeuse-ceramique`** — et ce n'est plus un trou de
donnée : c'est le blocage produit du §5. Elle sortira de l'ombre par une décision, pas par une écriture.

⚠️ **Rappel** : ces facettes ne s'afficheront en vitrine que lorsque les filtres seront ajoutés à la main dans
**Search & Discovery** (cf. `metachamps-montres.md` §1 — l'application est dans une iframe d'une autre origine et
n'est pas pilotable par l'outillage). Un filtre **Bracelet** est désormais à ajouter, en plus des quatre prévus.

---

## 7. Ce que ce document n'établit pas

- **Le diamètre des 9 fiches reste inconnu.** Rien n'a été inventé ; aucune cote de boîtier n'est publiée.
- **Le bracelet des 5 Plongeuses reste inconnu**, et celui de `noirmont-un-bronze` est désormais **douteux** (§5).
- **Je n'ai pas tranché la contradiction fiche/fournisseur** des 3 Noirmont. Ce n'est pas mon rôle.
- **La couleur de cadran de `trente-neuf-duo-classique-bicolore` est établie par mesure et par jumeau**, pas par une
  mention textuelle. Sa description dit « chiffres romains » quand sa photo montre des bâtons : cette fiche mérite
  une relecture éditoriale indépendante.
- **Aucun rendu mobile ni aucune facette en vitrine n'a été vu** — les écritures sont vérifiées côté données
  (compteurs de définition relus après écriture : 52 · 48 · 44 · 53 · 91).

---

*27/07/2026. Écritures : 2 métachamps (56 valeurs, 1 retirée), 1 définition créée, 1 description corrigée avec
sauvegarde. Aucun SKU, prix, variante, titre, statut, média, mapping DSers, thème, publication ni commande touché.*
