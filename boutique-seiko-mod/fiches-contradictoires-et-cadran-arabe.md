# Fiches contradictoires et ouverture du cadran arabe — Maison Noirmont

> **27/07/2026** — boutique `v42pzp-h4` / maisonnoirmont.fr.
> Traite le §5 de `verification-catalogue-strategie.md` (3 fiches actives dont les visuels contredisent le
> fournisseur mappé) puis ouvre la grappe « cadran chiffres arabes ».
> **Écritures : 3 passages en `DRAFT` + 1 fiche créée en `DRAFT`.** Aucun SKU, prix, variante, option, titre,
> description, média, métachamp existant ni mapping DSers modifié. Aucune suppression. Aucun thème, aucune
> publication, aucune commande, aucun achat.
> Sauvegarde d'état : `backup-avant-draft-noirmont-2026-07-27.json`.
> Preuves visuelles fournisseur : `preuves-fournisseur-2026-07-27/`.

---

## 1. Le diagnostic — d'un seul côté, et ce n'est pas celui du mapping

**Verdict : le mapping DSers est juste sur les trois fiches. Ce sont les fiches qui sont mal conçues.**

Deux preuves indépendantes concordent, listing par listing.

### Preuve 1 — la chaîne d'attributs SKU correspond au listing, valeur par valeur

Les SKU Shopify portent la concaténation DSers `propId:valueId#libellé`. Ces libellés ne peuvent venir que du
listing d'import. J'ai relevé les axes d'option **en direct sur AliExpress** et les ai confrontés aux SKU :

| Listing | Axes relevés sur AliExpress (27/07) | Correspondance avec nos SKU |
|---|---|---|
| `1005004626900765` (Tandorio) | `Couleur` : **steel case-no logo · bronze case-no logo · steel case-logo · bronze case-logo** — `Taille` : **Miyota82-steel back · Miyota82-glass back · NH35-steel back · NH35-glass back · PT5000-steel back · PT5000-glass back** | **8 / 8 libellés identiques.** `noirmont-un-plongeuse-acier` utilise les 6 « Taille » × `steel case-no logo` ; `noirmont-un-bronze-plongeuse` les 6 × `bronze case-no logo` |
| `1005005629655849` (BLIGER) | `Couleur` : **color 1 … color 7** — `Taille` : **Mingzhu 2813 · Miyota 8215 · NH35 · PT5000** | **11 / 11 libellés identiques.** Les 20 variantes de `noirmont-deux` sont des couples de ces deux axes |

Un mauvais rattachement ne produit pas 8 puis 11 libellés exacts. **Les fiches ont été construites sur ces
listings ; le mapping enregistre fidèlement leur origine.**

### Preuve 2 — les visuels de la boutique ne sont pas des photos fournisseur

Ce point ferme l'hypothèse « mapping faux » définitivement. Les visuels de ces fiches sont des **images
produites par la boutique** (`audit-visuel-catalogue.md`, `branchement-galeries-codex.md`,
`backup-medias-partages-2026-07-26/` où les fichiers sont nommés par **famille** — `gmt-1-face.jpg`,
`chrono-1-face.jpg` — et non par référence fournisseur). Ils ont été générés d'après ce que la **fiche**
prétendait vendre. Ils ne constituent donc à aucun moment une preuve de ce que le fournisseur livre : ils sont
la conséquence de l'erreur, pas sa source.

### Ce que vend réellement chaque listing

**`1005004626900765` — Tandorio** → `noirmont-un-plongeuse-acier`, `noirmont-un-bronze-plongeuse`

Attributs **structurés du vendeur** (pas l'« Aperçu IA », écarté comme dans `veracite-produit-cloture.md`) :

| Attribut vendeur | Valeur |
|---|---|
| **Type d'affichage** | **Marqueurs de chiffres arabes** |
| **Type de matériau du bracelet** | **Cuir** |
| Largeur de bande | 20 à 24 mm *(tranche — inexploitable)* |
| Forme du boîtier | rond |
| Origine du mouvement | JP |
| Profondeur de résistance à l'eau | 20 bars *(relevé du 26/07, inchangé)* |

Photos de variante du vendeur (`preuves-fournisseur-2026-07-27/TANDORIO-…jpg`) : **montre type flieger**,
cadran noir, **chiffres arabes 1-12 en couronne intérieure et 5-55 en couronne extérieure**, **lunette lisse
non tournante**, **bracelet cuir brun surpiqué**. Les deux références `-no logo` ont un cadran **stérile** ; les
`-logo` portent la marque à 12 h. Un avis acheteur vérifié parle spontanément de « montres de **pilote** ».

**Contradiction avec nos fiches :** elles annoncent une **plongeuse à lunette tournante et bracelet acier**
(`noirmont-un-bronze` écrit mot pour mot « le cadran noir et le **bracelet acier** », « **lunette tournante** »)
et montrent des visuels de plongeuse acier. **Ni la lunette tournante, ni le bracelet acier, ni le type
plongeuse ne sont ce que le fournisseur expédie.** Le cadran noir, lui, est juste dans les deux lectures.

**`1005005629655849` — BLIGER** → `noirmont-deux-plongeuse-ceramique`

Les 7 vignettes de variante téléchargées et mises en planche
(`preuves-fournisseur-2026-07-27/BLIGER-…jpg`) : **les 7 références partagent le même cadran bleu ciel semé de
pastilles multicolores** (rouge, jaune, rose, vert foncé, blanc), sur **bracelet acier jubilé**, avec un **insert
de lunette bleu ciel**. Elles ne diffèrent que par le marquage de l'insert : plongée graduée (réf. 1, 3, 4),
marquages noirs (réf. 5), **chiffres arabes orientaux** (réf. 2), **GMT 24 h** (réf. 6), **12 h occidental**
(réf. 7). Le H1 vendeur confirme la teinte : « …Insert Noir Bleu Vert, 40mm, **Bleu Ciel** ».

**L'hypothèse « photo de lume » est écartée.** `renommage-variantes-2026-07-25.md` §3 lisait ces pastilles comme
une démonstration de matière luminescente. Ce sont bien les **photos de jour**, en lumière naturelle sur fond
clair ; chacune porte **en incrustation séparée** un petit disque noir qui est, lui, la vraie photo de lume
(aiguilles et index verts). Les pastilles sont donc le **motif du cadran**, pas un artefact d'éclairage.

**Contradiction avec notre fiche :** elle montre une plongeuse **noire à cadran stérile, insert céramique noir**
et parle d'« insert céramique ». Aucune des 7 références n'est noire.

> **Conclusion.** Un client recevrait une autre montre que celle vue, sur les trois fiches. La contradiction est
> confirmée, et **elle est du côté de la fiche** — donc l'étape 2 s'applique, pas la correction de mapping.
> Corollaire heureux : il n'y a **rien à refaire dans DSers**.

---

## 2. Protection appliquée — les 3 fiches passées en `DRAFT`

| Fiche | ID | Avant | Après | Variantes | SKU / prix |
|---|---|---|---|---:|---|
| `noirmont-deux-plongeuse-ceramique` | `10977448624466` | ACTIVE | **DRAFT** | 20 | **intacts** |
| `noirmont-un-plongeuse-acier` | `10977448558930` | ACTIVE | **DRAFT** | 6 | **intacts** |
| `noirmont-un-bronze-plongeuse` | `10978722087250` | ACTIVE | **DRAFT** | 6 | **intacts** |

Trois `productUpdate { status: DRAFT }`, rien d'autre dans la charge utile. Les visuels trompeurs sortent de la
vitrine et plus aucune commande ne peut partir sur la mauvaise montre. **Réversible d'un clic** : repasser en
`ACTIVE`. Les trois publications d'origine (Boutique en ligne · Point de vente · Shop) sont relevées dans
`backup-avant-draft-noirmont-2026-07-27.json` au cas où elles ne se restaureraient pas d'elles-mêmes.

Aucun média retiré, aucune variante supprimée, aucun mapping touché : les fiches sont exactement dans l'état où
elles étaient, moins leur visibilité. `noirmont-un-bronze` était déjà à stock 0.

**Effet de bord à connaître :** la collection `Plongeuses` passe de 7 à **4 fiches visibles** (les 3 `Héritage`
et… c'est tout côté vraies plongeuses). Le guide de choix « Famille → Couleur » perd donc une famille en
vitrine. C'est le prix de l'honnêteté, mais il faut le savoir avant de brancher les facettes Search & Discovery.

---

## 3. La fiche cadran arabe — créée en `DRAFT`

`gid://shopify/Product/10981883150674` · handle **`aviateur-acier-cadran-chiffres-arabes`**

Le produit est celui du listing Tandorio déjà mappé, en version **stérile acier** (`steel case-no logo`) : le
cadran à chiffres arabes que la grappe SEMrush réclame (**≈ 15 500 recherches/mois, personne au-dessus de la
4ᵉ position**) était **déjà dans la chaîne d'approvisionnement**, caché derrière une fiche qui le décrivait en
plongeuse.

| Champ | Valeur |
|---|---|
| **Titre** | Aviateur Acier — Cadran à chiffres arabes |
| **Statut** | **DRAFT** |
| Type · vendeur | Montre automatique · Maison Noirmont |
| Collections | `classiques`, `montres` |
| Étiquette | `classiques` |
| `seo.title` | Montre à cadran chiffres arabes, automatique — Aviateur Acier |
| `seo.description` | Montre automatique à cadran noir et chiffres arabes, boîtier acier, bracelet cuir. Calibre Seiko NH35, Miyota 8215 ou PT5000. Livraison offerte, garantie 12 mois. |
| `custom.couleur_cadran` | `["Noir"]` |
| `custom.calibre` | `["Miyota 8215","NH35","PT5000"]` |
| `custom.bracelet` | `["Cuir"]` |
| `custom.famille` | `["Classiques"]` |
| `custom.diametre` | **laissé vide** |

### Les 6 variantes — SKU porteurs de la chaîne AliExpress

Option unique **`Mouvement & fond`**, exactement comme `noirmont-un-bronze-plongeuse` (motif maison issu du
découpage des mères).

| Variante | SKU | Prix | Barré |
|---|---|---:|---:|
| Miyota 8215 · fond acier | `14:350686#steel case-no logo;5:57086108#Miyota82-steel back` | 289 € | 379 € |
| Miyota 8215 · fond verre | `14:350686#steel case-no logo;5:646979416#Miyota82-glass back` | 318 € | 419 € |
| NH35 · fond acier | `14:350686#steel case-no logo;5:56964930#NH35-steel back` | 328 € | 429 € |
| NH35 · fond verre | `14:350686#steel case-no logo;5:57036539#NH35-glass back` | 357 € | 469 € |
| PT5000 · fond acier | `14:350686#steel case-no logo;5:57000035#PT5000-steel back` | 378 € | 499 € |
| PT5000 · fond verre | `14:350686#steel case-no logo;5:57037163#PT5000-glass back` | 407 € | 539 € |

`inventoryPolicy: CONTINUE`, suivi actif à 300, poids 0,18 kg, taxable — réglages copiés sur les fiches montres
existantes.

**Règle de prix maison vérifiée sur les six lignes** (prix × 1,3, arrondi à l'entier supérieur finissant par 9) :
289→375,7→**379** · 318→413,4→**419** · 328→426,4→**429** · 357→464,1→**469** · 378→491,4→**499** ·
407→529,1→**539**. Les prix de vente sont ceux déjà pratiqués sur ces SKU exacts : même fournisseur, même coût,
aucune nouvelle position tarifaire inventée.

### Ce que la fiche affirme, et sur quoi

| Affirmation | Source |
|---|---|
| Cadran noir à chiffres arabes 1-12, minutes 5-55 | attribut vendeur « Type d'affichage : Marqueurs de chiffres arabes » + les 4 photos de variante |
| Sans logo ni mention de marque | valeur d'option `steel case-**no logo**` + photos comparées aux versions `-logo` |
| Boîtier acier | titre vendeur « acier inoxydable » |
| Lunette lisse, sans graduation | photos de variante |
| Bracelet cuir | attribut vendeur « Type de matériau du bracelet : Cuir » |
| Fond acier ou fond verre | valeurs d'option `-steel back` / `-glass back` |
| Miyota 8215 · Seiko NH35 · PT5000 | valeurs d'option ; **fabricants de calibre, seule marque tierce autorisée** |
| « Verre saphir **annoncé** » | titre vendeur « verre saphir AR », avec le hedge maison |
| « Étanchéité **annoncée** 200 m ; la plongée en bouteille reste déconseillée » | attribut structuré 20 bars ; **formulation reprise mot pour mot** de `veracite-produit-cloture.md` pour ce listing |

**Aucune marque de design n'apparaît** — le mot « Tandorio » n'est nulle part dans la fiche.
**Aucun diamètre n'est écrit** : le listing ne donne qu'un « diamètre du cadran 30 à 34 mm », qui est une
tranche et n'est pas le boîtier (piège déjà documenté le 26/07). Même raison pour la largeur de bracelet
« 20 à 24 mm », non reportée.

**Une phrase ajoutée qui n'existait sur aucune autre fiche** : « le bracelet cuir, lui, n'aime pas l'eau —
prévoyez un bracelet de rechange si vous nagez avec ». Les 200 m sont réels mais le bracelet livré est en cuir :
promettre la nage sans le dire aurait été exact et trompeur à la fois.

### ⚠️ Aucun visuel — c'est volontaire

**La fiche a 0 média.** Aucun visuel de la boutique ne montre un cadran arabe : lui attribuer une image
existante aurait reproduit exactement le défaut qu'on vient de neutraliser. Et aucune photo fournisseur n'a été
posée, la boutique en ayant été entièrement purgée. **Un visuel reste à produire** — c'est le seul obstacle à la
publication.

---

## 4. Ce qui reste à faire

1. **Produire les visuels de `aviateur-acier-cadran-chiffres-arabes`** — face, situation, macro, poignet, au
   format des autres fiches. Le brief est précis et vérifiable : cadran noir stérile, **chiffres arabes 1-12 en
   couronne intérieure, 5-55 en couronne extérieure**, boîtier acier, **lunette lisse non tournante**, bracelet
   cuir brun surpiqué clair. Les photos de référence sont dans `preuves-fournisseur-2026-07-27/`. **Puis
   publier** — la fiche est prête par ailleurs.
2. **Trancher le sort des 3 fiches en brouillon.** Le mapping étant bon, la voie la moins coûteuse n'est pas de
   les jeter mais de les **réécrire sur le produit réel** : `noirmont-un-plongeuse-acier` et
   `noirmont-un-bronze-plongeuse` sont, en vérité, l'aviateur acier et l'aviateur bronze. `noirmont-deux`
   devient une plongeuse à cadran bleu ciel à pastilles — un produit atypique qui mérite sa propre décision
   (assumer le motif, ou re-sourcer).
3. **SKU en double, à surveiller.** `aviateur-acier-cadran-chiffres-arabes` porte les **mêmes 6 SKU** que
   `noirmont-un-plongeuse-acier` — inévitable, puisque c'est le même produit fournisseur et qu'il était interdit
   de supprimer ou modifier l'existant. Sans effet tant que `noirmont-un-plongeuse-acier` reste en brouillon.
   **Si tu la republies telle quelle, deux fiches partageront ces SKU.** Le plus propre est de la réécrire
   (point 2) ou de la laisser en brouillon définitivement.
4. **Rattacher la nouvelle fiche dans DSers.** Les SKU portent la chaîne d'attributs exacte, donc le mapping
   variante par variante sera automatique — mais **le fournisseur doit être lié à la fiche**, ce qui est une
   opération dans l'interface DSers. Listing : `https://fr.aliexpress.com/item/1005004626900765.html`,
   couleur `steel case-no logo`.
5. **L'aviateur bronze est disponible** sur le même listing (`14:94#bronze case-no logo`, mêmes 6 calibres/fonds,
   mêmes prix). Une seconde fiche est possible sans aucun sourcing — après le point 2, pour ne pas multiplier les
   doublons de SKU.
6. **`custom.bracelet` de `noirmont-un-bronze-plongeuse` est faux** : il dit « Acier maille non précisée », le
   fournisseur dit **Cuir**. Signalé le 27/07 comme douteux, il est maintenant **tranché**. Non modifié ici —
   la fiche est en brouillon et son avenir dépend du point 2.
7. **La collection `Plongeuses` n'a plus que 4 fiches visibles.** À reconsidérer avant de brancher les facettes.

---

## 5. Ce que ce document n'établit pas

- **Le diamètre du boîtier Tandorio reste inconnu.** Rien n'a été inventé ; `custom.diametre` est vide sur la
  nouvelle fiche. Seule issue : demander au vendeur, ou mesurer à réception.
- **« Chiffres arabes » désigne ici les chiffres 1-12 occidentaux**, au sens de l'attribut vendeur et de la
  requête française « montre cadran chiffres arabes ». Le **chiffre arabe oriental** (١ ٢ ٣) n'existe dans la
  chaîne d'approvisionnement que sur **l'insert de lunette** de la référence 2 de `noirmont-deux` — pas sur un
  cadran. Si la grappe SEMrush visait ce second sens, **elle n'est toujours pas servie** et demande un sourcing
  dédié.
- **Aucun rendu n'a été vu.** La fiche est en brouillon, sans visuel : il n'y avait pas de page à contrôler.
- **Je n'ai pas jugé la pertinence commerciale du cadran bleu ciel à pastilles** de `noirmont-deux`. Ce n'est
  pas un défaut, c'est un produit — mais ce n'est pas celui que la fiche vendait.

---

*27/07/2026. Écritures : 3 statuts `ACTIVE → DRAFT`, 1 fiche créée en `DRAFT` (6 variantes, 4 métachamps, 2
balises SEO, 2 collections, 0 média). Aucun SKU, prix, variante, option, titre, description, métachamp existant,
média, mapping DSers, thème, publication ni commande touché. Aucune suppression. Aucun achat.*
