---
type: journal
boutique: seiko-mod
date: 2026-07-31
nature: intervention
leviers: [catalogue, creative]
titre: "Réduction des mères & nettoyage des galeries — 2026-07-26"
---

# Réduction des mères & nettoyage des galeries — 2026-07-26

Boutique **NOIRMONT** / Maison Noirmont (`v42pzp-h4.myshopify.com`, maisonnoirmont.fr) — vérifiée par `get-shop-info` avant toute écriture.

**181 médias détachés sur 41 fiches filles · 175 variantes supprimées sur 12 fiches mères · 0 média supprimé · 0 produit supprimé · 0 erreur API.**

Sauvegarde préalable : `backup-avant-reduction-meres.json` (12 mères, 221 variantes, écrite **avant** la première suppression).
Sauvegarde des fichiers image : `boutique-seiko-mod/backups/backup-medias-partages-2026-07-26/` (31 JPEG, 12 Mo, téléchargés **avant** le pilote).

---

## Volet 1 — Galeries des fiches filles

### Le défaut, confirmé et mesuré

Le constat de Hakim est exact et **général aux 41 fiches du lot 2**. La fiche « Panda inversé » portait 9 médias : 2 visuels propres + **les 7 médias de la mère**, dont le packshot du cadran crème, la mise en situation, la macro, le geste et la carte de preuve sociale — six montres d'un autre coloris que celle vendue.

**Les 19 fiches du lot 1 ne sont pas concernées** : contrôle fait fiche par fiche, elles portent **1 seul média chacune**, leur propre visuel, uploadé indépendamment. Rien à y retirer.

### Le piège, vérifié avant d'agir plutôt que supposé

Les médias hérités sont **le même objet `MediaImage` que la mère** — mêmes identifiants, mêmes URL CDN (par ex. `59679727976786` présent à l'identique sur la mère et sur les 12 filles chronographe). Une suppression réelle les retirait de la mère et de toutes les sœurs.

**Pilote exécuté avant toute généralisation**, comme demandé : `productDeleteMedia` sur **un seul** média (`59680004604242`) de la fiche Panda inversé, puis relecture immédiate.

| Contrôle après le pilote | Résultat |
|---|---|
| Mère `10977444528466` — médias | 27 → **27**, `59680004604242` toujours présent ✅ |
| Sœur « Blanc » `10980078879058` — médias | 10 → **10**, média toujours présent ✅ |
| Objet `MediaImage/59680004604242` | existe toujours, `alt` et URL CDN intacts ✅ |
| Fiche pilote | 9 → 8 ✅ |

**Conclusion : malgré son nom et son champ `deletedMediaIds`, `productDeleteMedia` ne fait que _détacher_ quand le fichier est référencé ailleurs.** C'est la bonne mutation, et la seule utilisée ici. (Shopify la marque dépréciée au profit de `fileUpdate`, dont le mécanisme est justement le retrait de référence — ce qui confirme la sémantique.) Les 31 fichiers avaient été téléchargés en local au préalable : le filet n'a pas servi.

### Règle appliquée

Vérifiée **à l'œil sur les images**, pas déduite des `alt` :

- ✅ **Conservé** — le visuel propre au coloris, et la **carte de témoignage client** : ouverte et inspectée, elle est strictement typographique (citation, 5 étoiles, signature « Mehdi A. — Strasbourg »), **aucune montre**. Valable pour tous les coloris.
- ⛔ **Retiré** — packshot de la mère, mise en situation, carte de caractéristique, geste en main, macro détails et **carte de preuve sociale** : cette dernière, ouverte elle aussi, porte bien un **cadran crème panda** en haut de l'image, donc un autre coloris.

### Médias détachés, par famille

| Famille | Fiches | Médias détachés par fiche | Détachements | Galerie après |
|---|---:|---:|---:|---|
| Contre-la-montre — chronographe | 12 | 6 | 71 * | 1 à 3 visuels de cadran + témoignage |
| Voyageur — GMT | 6 | 6 | 36 | visuel du coloris + témoignage |
| Intégrale — sport chic | 7 | 6 | 42 | visuel du coloris + témoignage |
| Héritage — plongeuse vintage | 3 | 6 | 18 | visuel du coloris + témoignage |
| Remontoir Bois | 4 | 1 | 4 | visuel de l'essence seul |
| Rouleau de Voyage | 4 | 1 | 4 | visuel du cuir seul |
| Remontoir Collection | 5 | 1 | 5 | visuel du coffret seul |
| **Total** | **41** | | **181** | |

\* 71 et non 72 : la fiche Panda inversé avait déjà perdu 1 média lors du pilote.

Identifiants détachés, par famille — jamais supprimés, toujours vivants sur la mère :

- **Chronographe** : `59679727976786` · `59680004505938` · `59680004538706` · `59680004571474` · `59680004604242` · `59680004637010` — conservé : `59680004669778` (témoignage)
- **GMT** : `59680135872850` · `59680135905618` · `59680135938386` · `59680135971154` · `59680136003922` · `59680136036690` — conservé : `59680136069458`
- **Intégrale** : `59679287247186` · `59680004702546` · `59680004735314` · `59680004768082` · `59680004800850` · `59680004833618` — conservé : `59680004866386`
- **Héritage** : `59679728009554` · `59680004899154` · `59680004931922` · `59680004964690` · `59680004997458` · `59680005030226` — conservé : `59680005062994`
- **Accessoires** : `59679287771474` (Remontoir Bois) · `59679287837010` (Rouleau) · `59679728042322` (Remontoir Collection)

### Accessoires — pourquoi le générique a été retiré malgré tout

Les 13 fiches accessoires **ont chacune un visuel propre** (branché au lot 3), la clause « ne rien retirer » ne s'y applique donc pas. Les trois génériques ont été **ouverts et regardés** : celui du Remontoir Bois montre un coffret **acajou brun**, celui du Remontoir Collection une **armoire en bois foncé à 8 emplacements**. Sur les fiches « Noir laqué », « Ébène », « Bois beige », « LED rouge » ou « Cuir PU », c'est exactement le défaut signalé. Retirés. Chaque fiche garde 1 visuel — le sien — soit la même situation que les 19 fiches du lot 1.

**Aucune fiche n'est restée sans image.**

### Non-régression des mères

Relecture après opération : **aucune mère n'a perdu un seul média**.

| Mère | Médias avant | Après |
|---|---:|---:|
| Contre-la-montre — Chronographe panda | 27 | **27** |
| Voyageur — GMT automatique | 13 | **13** |
| Intégrale — Sport chic acier | 14 | **14** |
| Héritage — Plongeuse vintage 42 | 10 | **10** |
| Remontoir Bois | 5 | **5** |
| Rouleau de Voyage — cuir | 5 | **5** |
| Remontoir Collection | 6 | **6** |

---

## Volet 2 — Réduction des mères à un coloris unique

### Garde-fou appliqué avant toute suppression

Les 175 SKU candidats à la suppression ont été confrontés un à un à l'**ensemble des 181 SKU vivants sur les 60 fiches filles** (92 du lot 1 + 89 du lot 2, effectifs conformes aux deux rapports de découpage).

**Résultat : 175/175 trouvés. Aucun SKU orphelin, donc aucune suppression n'a détruit un mapping DSers sans filet.** Le rapprochement complet SKU → fiche fille porteuse est consigné dans `backup-avant-reduction-meres.json`, champ `portee_par_fille`.

### Bilan

| Mère | ID | Avant | Après | Suppr. | Coloris conservé |
|---|---|---:|---:|---:|---|
| Trente-Six — Classique jubilé | `10977448690002` | 24 | **4** | 20 | Noir |
| Trente-Neuf — Classique cannelée | `10977444430162` | 56 | **8** | 48 | Orange |
| Quarante-et-Un — Sport acier | `10977444495698` | 16 | **4** | 12 | Cadran blanc · bracelet acier **et** Cadran noir · bracelet cuir M |
| Noirmont Un — Plongeuse acier | `10977448558930` | 12 | **6** | 6 | Acier |
| Trente-Neuf Duo — Classique bicolore | `10977448722770` | 12 | **6** | 6 | Or rose (36 et 39 mm) |
| Contre-la-montre — Chronographe panda | `10977444528466` | 20 | **1** | 19 | ⚠️ Argent · caoutchouc noir (1er) |
| Voyageur — GMT automatique | `10977448657234` | 36 | **12** | 24 | ⚠️ les 3 boîtiers « siglé » |
| Intégrale — Sport chic acier | `10977444561234` | 7 | **1** | 6 | ⚠️ Vert (1er) |
| Héritage — Plongeuse vintage 42 | `10977444594002` | 3 | **1** | 2 | ⚠️ Bleu · lunette bleue (1er) |
| Remontoir Bois | `10977444659538` | 8 | **1** | 7 | ⚠️ Noir laqué · 1 montre (1er) |
| Rouleau de Voyage — cuir | `10977444823378` | 12 | **1** | 11 | ⚠️ Cuir bleu marine · 3 montres (1er) |
| Remontoir Collection | `10977444757842` | 15 | **1** | 14 | ⚠️ Bois LED · rouge · 4 montres (1er) |
| | | **221** | **46** | **175** | |

Les 5 premières lignes appliquent à la lettre les coloris nommés dans le brief. Les 7 suivantes viennent de `2026-07-31-decoupage-elagage-lot2.md` et sont **signalées** ci-dessous.

Les **valeurs d'option devenues vides ont été retirées automatiquement par Shopify** : `Cadran` ne vaut plus que « Noir » sur Trente-Six, « Orange » sur Trente-Neuf, etc. Aucune intervention supplémentaire n'a été nécessaire.

Relecture après suppression : les **46 variantes survivantes sont identiques à la sauvegarde** — mêmes identifiants, mêmes SKU, mêmes prix, mêmes politiques et quantités d'inventaire. Les 60 fiches filles sont **intactes** (92 + 89 variantes, aucune touchée).

### Détail des variantes supprimées et de la fiche qui les porte désormais

#### Trente-Six — Classique jubilé (`10977448690002`) — 24 → 4 variantes

Coloris conservé : **Cadran = Noir**

| Fiche fille qui porte désormais le SKU | ID fille | Variantes | SKU supprimés de la mère |
|---|---|---:|---|
| Trente-Six Rouge | `10978718744914` | 4 | `14:100005979#red no logo;5:56964930#36mm- glass back`<br>`14:100005979#red no logo;5:57000035#36mm-solid back`<br>`14:100005979#red no logo;5:57086108#39mm-glass back`<br>`14:100005979#red no logo;5:57085267#39-solid back` |
| Trente-Six Bleu | `10978719039826` | 4 | `14:350850#blue no logo;5:56964930#36mm- glass back`<br>`14:350850#blue no logo;5:57000035#36mm-solid back`<br>`14:350850#blue no logo;5:57086108#39mm-glass back`<br>`14:350850#blue no logo;5:57085267#39-solid back` |
| Trente-Six Rose | `10978719236434` | 4 | `14:10#pink no logo;5:56964930#36mm- glass back`<br>`14:10#pink no logo;5:57000035#36mm-solid back`<br>`14:10#pink no logo;5:57086108#39mm-glass back`<br>`14:10#pink no logo;5:57085267#39-solid back` |
| Trente-Six Dore | `10978719367506` | 4 | `14:94#yellow gold no logo;5:56964930#36mm- glass back`<br>`14:94#yellow gold no logo;5:57000035#36mm-solid back`<br>`14:94#yellow gold no logo;5:57086108#39mm-glass back`<br>`14:94#yellow gold no logo;5:57085267#39-solid back` |
| Trente-Six Or integral | `10978719433042` | 4 | `14:193#full  gold no logo;5:56964930#36mm- glass back`<br>`14:193#full  gold no logo;5:57000035#36mm-solid back`<br>`14:193#full  gold no logo;5:57086108#39mm-glass back`<br>`14:193#full  gold no logo;5:57085267#39-solid back` |

#### Trente-Neuf — Classique cannelée (`10977444430162`) — 56 → 8 variantes

Coloris conservé : **Cadran = Orange**

| Fiche fille qui porte désormais le SKU | ID fille | Variantes | SKU supprimés de la mère |
|---|---|---:|---|
| Trente-Neuf Rouge | `10978720055634` | 8 | `14:173#red no logo;5:57085267#8215-39mm(solidback)`<br>`14:173#red no logo;5:57086108#8215-39mm(glassback)`<br>`14:173#red no logo;5:57000035#8215-36mm(solidback)`<br>`14:173#red no logo;5:56964930#8215-36mm(glassback)`<br>`14:173#red no logo;5:2399342480#NH35-39mm(solidback)`<br>`14:173#red no logo;5:646979416#NH35-39mm(glassback)`<br>`14:173#red no logo;5:57037163#NH35-36mm(solidback)`<br>`14:173#red no logo;5:57036539#NH35-36mm(glassback)` |
| Trente-Neuf Bleu mer | `10978720186706` | 8 | `14:29#sea blue no logo;5:57085267#8215-39mm(solidback)`<br>`14:29#sea blue no logo;5:57086108#8215-39mm(glassback)`<br>`14:29#sea blue no logo;5:57000035#8215-36mm(solidback)`<br>`14:29#sea blue no logo;5:56964930#8215-36mm(glassback)`<br>`14:29#sea blue no logo;5:2399342480#NH35-39mm(solidback)`<br>`14:29#sea blue no logo;5:646979416#NH35-39mm(glassback)`<br>`14:29#sea blue no logo;5:57037163#NH35-36mm(solidback)`<br>`14:29#sea blue no logo;5:57036539#NH35-36mm(glassback)` |
| Trente-Neuf Rose | `10978720317778` | 8 | `14:350853#pink no logo;5:57085267#8215-39mm(solidback)`<br>`14:350853#pink no logo;5:57086108#8215-39mm(glassback)`<br>`14:350853#pink no logo;5:57000035#8215-36mm(solidback)`<br>`14:350853#pink no logo;5:56964930#8215-36mm(glassback)`<br>`14:350853#pink no logo;5:2399342480#NH35-39mm(solidback)`<br>`14:350853#pink no logo;5:646979416#NH35-39mm(glassback)`<br>`14:350853#pink no logo;5:57037163#NH35-36mm(solidback)`<br>`14:350853#pink no logo;5:57036539#NH35-36mm(glassback)` |
| Trente-Neuf Vert | `10978720547154` | 8 | `14:350686#green no logo;5:57085267#8215-39mm(solidback)`<br>`14:350686#green no logo;5:57086108#8215-39mm(glassback)`<br>`14:350686#green no logo;5:57000035#8215-36mm(solidback)`<br>`14:350686#green no logo;5:56964930#8215-36mm(glassback)`<br>`14:350686#green no logo;5:2399342480#NH35-39mm(solidback)`<br>`14:350686#green no logo;5:646979416#NH35-39mm(glassback)`<br>`14:350686#green no logo;5:57037163#NH35-36mm(solidback)`<br>`14:350686#green no logo;5:57036539#NH35-36mm(glassback)` |
| Trente-Neuf Bleu | `10978720678226` | 8 | `14:100013777#blue no logo;5:57085267#8215-39mm(solidback)`<br>`14:100013777#blue no logo;5:57086108#8215-39mm(glassback)`<br>`14:100013777#blue no logo;5:57000035#8215-36mm(solidback)`<br>`14:100013777#blue no logo;5:56964930#8215-36mm(glassback)`<br>`14:100013777#blue no logo;5:2399342480#NH35-39mm(solidback)`<br>`14:100013777#blue no logo;5:646979416#NH35-39mm(glassback)`<br>`14:100013777#blue no logo;5:57037163#NH35-36mm(solidback)`<br>`14:100013777#blue no logo;5:57036539#NH35-36mm(glassback)` |
| Trente-Neuf Noir | `10978720842066` | 8 | `14:200005100#black no logo;5:57085267#8215-39mm(solidback)`<br>`14:200005100#black no logo;5:57086108#8215-39mm(glassback)`<br>`14:200005100#black no logo;5:57000035#8215-36mm(solidback)`<br>`14:200005100#black no logo;5:56964930#8215-36mm(glassback)`<br>`14:200005100#black no logo;5:2399342480#NH35-39mm(solidback)`<br>`14:200005100#black no logo;5:646979416#NH35-39mm(glassback)`<br>`14:200005100#black no logo;5:57037163#NH35-36mm(solidback)`<br>`14:200005100#black no logo;5:57036539#NH35-36mm(glassback)` |

#### Quarante-et-Un — Sport acier (`10977444495698`) — 16 → 4 variantes

Coloris conservé : **Cadran blanc · bracelet acier + Cadran noir · bracelet cuir M**

| Fiche fille qui porte désormais le SKU | ID fille | Variantes | SKU supprimés de la mère |
|---|---|---:|---|
| Quarante-et-Un Bleu Acier | `10978721235282` | 2 | `14:100005979#Blue Dial M;5:57037163#NH35 MOVT`<br>`14:100005979#Blue Dial M;5:57036539#Miyota 8215` |
| Quarante-et-Un Noir & Jaune Acier | `10978721431890` | 2 | `14:100013777#Black Dial  Yellow M;5:57037163#NH35 MOVT`<br>`14:100013777#Black Dial  Yellow M;5:57036539#Miyota 8215` |
| Quarante-et-Un Noir Acier | `10978721530194` | 2 | `14:200005100#Black Dial M;5:57037163#NH35 MOVT`<br>`14:200005100#Black Dial M;5:57036539#Miyota 8215` |
| Quarante-et-Un Blanc Cuir | `10978721726802` | 2 | `14:29#White Dial leather;5:57036539#Miyota 8215`<br>`14:29#White Dial leather;5:57037163#NH35 MOVT` |
| Quarante-et-Un Bleu Cuir | `10978721857874` | 2 | `14:10#Blue Dial leather;5:57037163#NH35 MOVT`<br>`14:10#Blue Dial leather;5:57036539#Miyota 8215` |
| Quarante-et-Un Noir Cuir | `10978721988946` | 2 | `14:350853#Black dial leather;5:57037163#NH35 MOVT`<br>`14:350853#Black dial leather;5:57036539#Miyota 8215` |

#### Noirmont Un — Plongeuse acier (`10977448558930`) — 12 → 6 variantes

Coloris conservé : **Boîtier = Acier**

| Fiche fille qui porte désormais le SKU | ID fille | Variantes | SKU supprimés de la mère |
|---|---|---:|---|
| Noirmont Un Bronze | `10978722087250` | 6 | `14:94#bronze case-no logo;5:56964930#NH35-steel back`<br>`14:94#bronze case-no logo;5:57086108#Miyota82-steel back`<br>`14:94#bronze case-no logo;5:57036539#NH35-glass back`<br>`14:94#bronze case-no logo;5:57000035#PT5000-steel back`<br>`14:94#bronze case-no logo;5:57037163#PT5000-glass back`<br>`14:94#bronze case-no logo;5:646979416#Miyota82-glass back` |

#### Trente-Neuf Duo — Classique bicolore (`10977448722770`) — 12 → 6 variantes

Coloris conservé : **Boîtier = Or rose (36 et 39 mm)**

| Fiche fille qui porte désormais le SKU | ID fille | Variantes | SKU supprimés de la mère |
|---|---|---:|---|
| Trente-Neuf Duo Dore | `10978722251090` | 6 | `14:350850#Gold 36mm glass back;5:57000035#Miyota8215`<br>`14:350850#Gold 36mm glass back;5:2399342480#NH35`<br>`14:350850#Gold 36mm glass back;5:56964930#Mingzhu 2813`<br>`14:200000080#Gold 39mm glass back;5:56964930#Mingzhu 2813`<br>`14:200000080#Gold 39mm glass back;5:2399342480#NH35`<br>`14:200000080#Gold 39mm glass back;5:57000035#Miyota8215` |

#### Contre-la-montre — Chronographe panda (`10977444528466`) — 20 → 1 variantes

Coloris conservé : **Cadran = Argent · caoutchouc noir (1er ; tous les coloris repris en filles)**

| Fiche fille qui porte désormais le SKU | ID fille | Variantes | SKU supprimés de la mère |
|---|---|---:|---|
| Contre-la-montre Panda | `10980080976210` | 2 | `14:1254#M19`<br>`14:100013777#M-6` |
| Contre-la-montre Bleu glacier | `10980083138898` | 1 | `14:4#M20` |
| Contre-la-montre Panda inverse | `10980080419154` | 2 | `14:193#M-2`<br>`14:350686#M18` |
| Contre-la-montre Rose poudre | `10980081762642` | 1 | `14:175#M9` |
| Contre-la-montre Noir | `10980081041746` | 2 | `14:496#M17`<br>`14:200000080#M-7` |
| Contre-la-montre Turquoise | `10980081533266` | 2 | `14:366#M10`<br>`14:173#M16` |
| Contre-la-montre Blanc | `10980078879058` | 3 | `14:29#M-1`<br>`14:100005979#M8`<br>`14:200005100#M-5` |
| Contre-la-montre Gris anthracite | `10980081926482` | 1 | `14:10#M13` |
| Contre-la-montre Compteurs bleus | `10980083007826` | 1 | `14:94#M15` |
| Contre-la-montre Vert | `10980081631570` | 2 | `14:350853#M11`<br>`14:350850#M12` |
| Contre-la-montre Champagne | `10980080779602` | 2 | `14:201447303#M-3`<br>`14:201447598#M-4` |

#### Voyageur — GMT automatique (`10977448657234`) — 36 → 12 variantes

Coloris conservé : **les 3 boîtiers « siglé » (seuls non repris en filles)**

| Fiche fille qui porte désormais le SKU | ID fille | Variantes | SKU supprimés de la mère |
|---|---|---:|---|
| Voyageur Or 3 maillons | `10980078780754` | 4 | `14:175#9;5:56964930#DG3804 GLASS back`<br>`14:175#9;5:57000035#DG3804 SOLID back`<br>`14:175#9;5:646979416#NH34 GLASS back`<br>`14:175#9;5:2399342480#NH34 SOLID back` |
| Voyageur Or President | `10980079042898` | 4 | `14:193#7;5:56964930#DG3804 GLASS back`<br>`14:193#7;5:57000035#DG3804 SOLID back`<br>`14:193#7;5:646979416#NH34 GLASS back`<br>`14:193#7;5:2399342480#NH34 SOLID back` |
| Voyageur Bicolore 3 maillons | `10980080845138` | 4 | `14:29#6;5:56964930#DG3804 GLASS back`<br>`14:29#6;5:57000035#DG3804 SOLID back`<br>`14:29#6;5:646979416#NH34 GLASS back`<br>`14:29#6;5:2399342480#NH34 SOLID back` |
| Voyageur Bicolore 5 maillons | `10980081107282` | 4 | `14:200000080#2;5:56964930#DG3804 GLASS back`<br>`14:200000080#2;5:57000035#DG3804 SOLID back`<br>`14:200000080#2;5:646979416#NH34 GLASS back`<br>`14:200000080#2;5:2399342480#NH34 SOLID back` |
| Voyageur Or rose 5 maillons | `10980081402194` | 4 | `14:200005100#1;5:56964930#DG3804 GLASS back`<br>`14:200005100#1;5:57000035#DG3804 SOLID back`<br>`14:200005100#1;5:646979416#NH34 GLASS back`<br>`14:200005100#1;5:2399342480#NH34 SOLID back` |
| Voyageur Bicolore cadran brun | `10980081664338` | 4 | `14:100005979#4;5:56964930#DG3804 GLASS back`<br>`14:100005979#4;5:57000035#DG3804 SOLID back`<br>`14:100005979#4;5:646979416#NH34 GLASS back`<br>`14:100005979#4;5:2399342480#NH34 SOLID back` |

#### Intégrale — Sport chic acier (`10977444561234`) — 7 → 1 variantes

Coloris conservé : **Cadran = Vert (1er ; tous les coloris repris)**

| Fiche fille qui porte désormais le SKU | ID fille | Variantes | SKU supprimés de la mère |
|---|---|---:|---|
| Integrale Brun or rose | `10980079075666` | 1 | `14:193#7;200007763:201336100` |
| Integrale Turquoise | `10980080714066` | 1 | `14:4#1;200007763:201336100` |
| Integrale Noir | `10980080877906` | 1 | `14:94#4;200007763:201336100` |
| Integrale Bleu nuit | `10980081074514` | 1 | `14:173#5;200007763:201336100` |
| Integrale Bleu ciel | `10980081205586` | 1 | `14:10#2;200007763:201336100` |
| Integrale Blanc argente | `10980081336658` | 1 | `14:29#3;200007763:201336100` |

#### Héritage — Plongeuse vintage 42 (`10977444594002`) — 3 → 1 variantes

Coloris conservé : **Cadran & lunette = Bleu · lunette bleue (1er ; tous repris)**

| Fiche fille qui porte désormais le SKU | ID fille | Variantes | SKU supprimés de la mère |
|---|---|---:|---|
| Heritage Bleu nuit | `10980084220242` | 1 | `14:100013777#S2;5:56964930#42mm` |
| Heritage Vert | `10980084515154` | 1 | `14:350850#S3;5:56964930#42mm` |

#### Remontoir Bois (`10977444659538`) — 8 → 1 variantes

Coloris conservé : **Noir laqué · 1 montre (1er ; tous repris)**

| Fiche fille qui porte désormais le SKU | ID fille | Variantes | SKU supprimés de la mère |
|---|---|---:|---|
| Remontoir Bois Acajou | `10980082909522` | 2 | `14:173#M11032`<br>`14:94#M12032` |
| Remontoir Bois Ebene | `10980083106130` | 2 | `14:350686#M11052`<br>`14:865#M12052` |
| Remontoir Bois Noyer | `10980083269970` | 2 | `14:350850#M11071`<br>`14:100013777#M12071` |
| Remontoir Bois Noir laque | `10980082745682` | 1 | `14:175#M12011` |

#### Rouleau de Voyage — cuir (`10977444823378`) — 12 → 1 variantes

Coloris conservé : **Cuir bleu marine · 3 montres (1er ; tous repris)**

| Fiche fille qui porte désormais le SKU | ID fille | Variantes | SKU supprimés de la mère |
|---|---|---:|---|
| Rouleau Brun | `10980083401042` | 3 | `14:175#WB22`<br>`14:94#WB23`<br>`14:350850#WB21` |
| Rouleau Bleu marine | `10980083564882` | 2 | `14:865#WB31`<br>`14:100013777#WB32` |
| Rouleau Vert | `10980083859794` | 3 | `14:10#WB41`<br>`14:350853#WB42`<br>`14:29#WB43` |
| Rouleau Noir | `10980083171666` | 3 | `14:193#WB11`<br>`14:173#WB12`<br>`14:350686#WB13` |

#### Remontoir Collection — 2 à 6 montres (`10977444757842`) — 15 → 1 variantes

Coloris conservé : **Bois LED · rouge · 4 montres (1er ; tous repris)**

| Fiche fille qui porte désormais le SKU | ID fille | Variantes | SKU supprimés de la mère |
|---|---|---:|---|
| Remontoir Collection Bois LED noir | `10980084056402` | 2 | `14:29#IB-black-02C`<br>`14:100005979#IB-black-04C` |
| Remontoir Collection Cuir PU | `10980084449618` | 3 | `14:350853#IB-PU leather-06B`<br>`14:10#IB-PU leather-04B`<br>`14:496#IB-PU leather-02B` |
| Remontoir Collection Bois LED rouge | `10980084121938` | 1 | `14:366#IB-red-02C` |
| Remontoir Collection Bois beige | `10980083728722` | 4 | `14:100013777#IB-white-06A`<br>`14:350850#IB-white-02A`<br>`14:94#IB-white-04A`<br>`14:173#IB-white-01A` |
| Remontoir Collection Bois noir | `10980083466578` | 4 | `14:865#IB-black-06A`<br>`14:350686#IB-black-02A`<br>`14:175#IB-black-04A`<br>`14:193#IB-black-01A` |
---

## Fiches signalées

**1. ⚠️ Voyageur — GMT automatique : la mère ne contient plus que des invendables.**
C'est la conséquence directe et logique de la règle « garder les coloris non repris en filles » : les 6 boîtiers vendables sont tous passés en fiches filles, seuls les **3 boîtiers « siglé » n'ont jamais été repris**. Ils restent donc seuls sur la mère — **12 SKU, tous en `DENY` et stock 0**, conformément à la consigne de ne pas y toucher. La fiche est ACTIVE mais **entièrement inachetable**. Ce n'est pas un défaut créé ici : c'est l'arbitrage en attente du point 5 du BILAN (« sort définitif des 12 variantes siglées ») qui devient visible. **À trancher : archiver la fiche, ou y réintroduire un coloris vendable.**

**2. Sept mères dont *tous* les coloris avaient été repris en filles.** Le brief prévoyait ce cas (« garde le premier et signale-le »). Appliqué à : **Contre-la-montre** (20/20 repris), **Intégrale** (7/7), **Héritage** (3/3), **Remontoir Bois** (8/8), **Rouleau de Voyage** (12/12), **Remontoir Collection** (15/15). Chacune est tombée à **1 variante**, qui fait doublon exact avec une fiche fille. Ces 6 mères n'ont plus de raison d'être commerciale : **candidates à l'archivage**, ce que je n'ai pas fait, aucune suppression de produit n'étant autorisée.

**3. Contre-la-montre — Chronographe panda conserve 27 médias pour 1 variante.** Les 20 visuels de coloris posés par Codex sur la mère y restent (aucun média supprimé). Si la fiche est archivée, la question disparaît ; sinon, sa galerie est très surdimensionnée.

**4. Aucune fiche accessoire n'a été laissée sans image**, et aucune fiche du catalogue n'est passée sous 1 média.

**5. Non touché, comme demandé** : Noirmont Deux (`10977448624466`, 28 variantes), les 3 déclinaisons GMT « siglé », les SKU, prix et titres — **aucune de ces valeurs n'a été modifiée nulle part**. Aucune commande passée.

---

## Contrôle DSers

Relu dans Chrome sur la session de Hakim (compte `contact.noirmont`, boutique `v42pzp-h4`), **sans aucune saisie d'identifiant** — la session était active, page rechargée après les suppressions.

| Compteur | Valeur |
|---|---|
| Tous | **98** |
| AliExpress | **98** |
| 1688 Dropshipping / Alibaba | 0 / 0 |
| **Unmapped** | **0** ✅ |

**Aucune fiche n'est repassée en « Unmapped » après la suppression des 175 variantes.** Le compteur est passé de 44 (lot 2) à 98, les nouvelles fiches ayant été rattachées entre-temps.

---

## Contrôle visuel sur le storefront

Thème brouillon `204248088914` (bandeau « Maison Noirmont — Draft — Password protected » visible ; la prévisualisation s'est ouverte sans saisie de mot de passe).

**Fiche « Contre-la-montre Panda inversé — Chronographe »** — la fiche même signalée par Hakim :

- La galerie ne sert plus que **3 images** : `chrono-panda-inverse-aiguilles-acier`, `chrono-panda-inverse-aiguille-rouge` et `10977444528466-7.jpg` (la carte de témoignage typographique).
- **Plus aucun cadran crème.** Les six visuels de la mère ont disparu de la fiche.
- Image principale au chargement : le cadran **noir à compteurs blancs** sur bracelet acier, soit exactement le Panda inversé vendu. Les deux options `ACIER` / `ROUGE` sont bien présentes.
- Capture d'écran prise et vérifiée.

---

## Annulation

- **Volet 1** : rejouable en rattachant les médias listés plus haut aux fiches filles (`productCreateMedia` par `id`). Les 31 fichiers sont aussi sur disque dans `boutique-seiko-mod/backups/backup-medias-partages-2026-07-26/`.
- **Volet 2** : les 175 variantes se recréent à l'identique depuis `backup-avant-reduction-meres.json`, qui porte pour chacune `id`, `sku`, `price`, `compareAtPrice`, `inventoryPolicy`, `inventoryQuantity` et les valeurs d'option. ⚠️ Une recréation produira de **nouveaux identifiants de variante** ; les SKU, eux, sont restitués à l'octet près.
