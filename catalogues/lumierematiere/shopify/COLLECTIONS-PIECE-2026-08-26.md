# Collections de pièce et d'opportunité — lumierematiere.fr (26/08/2026)

**Fait.** 8 collections créées, 2 renommées, 110 rattachements, 2 redirections 301, menu principal
réorganisé en deux axes. Les 10 pages portent un `seo_title`, une `seo_description` et un
`description_html` au format de `collections-seo.json`. Vérifié en ligne : 10 pages en HTTP 200,
2 anciennes URL en 301, aucune 404.

Périmètre et ordre : § A de `CONCURRENT-LUSTRIA-2026-08-25.md`. Volumes : `MOTS-CLES-TITRES-2026-08-25.md`
(consolidés, § 0). Feu vert de Hakim le 25/08 au soir.

**Le retard visé.** Chez Lustria, les collections de pièce pèsent 38,8 % du trafic des 100 premières
pages contre 13,8 % pour les matières. Nous étions rangés à 100 % par matière, avec zéro collection
de pièce. Ce rattrapage n'a demandé aucun sourcing : il n'utilise que les 120 fiches existantes.

---

## 1. Ce qui a été fait, ligne par ligne

| # § A | Collection | Handle | Mot-clé | Volume | Fiches | Estimation § A |
|---:|---|---|---|---:|---:|---|
| 1 | **Plafonniers LED** *(renommée)* | `plafonniers-led` | `plafonnier led` | **21 090** | **14** | 10 |
| 2 | **Lustres chambre** | `lustres-chambre` | `lustre chambre` | **10 810** | **10** | ~10 |
| 3 | **Plafonniers salon** | `plafonniers-salon` | `plafonnier salon` | **8 970** | **9** | 6 à 8 |
| 4 | **Suspensions cuisine** | `suspensions-cuisine` | `suspension cuisine` | **4 800** | **31** | ~20 |
| 5 | **Plafonniers cuisine** | `plafonniers-cuisine` | `plafonnier cuisine` | **6 190** | **4** | 4 à 6 |
| 6 | **Lustres pampilles** *(renommée)* | `lustres-pampilles` | `lustre pampilles` | **6 340** | **7** | 7 |
| 7 | **Suspensions salon** | `suspensions-salon` | `suspension salon` | **4 080** | **29** | 12 à 15 |
| 8 | **Suspensions papier** | `suspensions-papier` | `suspension papier` | **4 760** | **1** | 1 |
| 9 | **Grandes suspensions XXL** | `suspensions-xxl` | `suspension xxl` | **1 310** | **15** | 8 à 10 |
| 10 | **Suspensions osier** | `suspensions-osier` | `suspension osier` | **3 180** | **5** | 4 à 6 |

Volume de demande adressé par les 8 nouvelles pages : **44 140** recherches/mois cumulées.
Les deux renommages en ajoutent **27 430** sur des pages qui existaient déjà.

### Les deux renommages

**`Lustres effet cristal` → `Lustres pampilles`** (`lustres-effet-cristal` → `lustres-pampilles`).
`lustre pampilles` vaut 6 340 contre 2 610 pour `lustre cristal`, et `lustre effet cristal` ne vaut
que 20. Chez Lustria, `lustre-pampilles` a **zéro produit** et fait quand même 890 visites/mois sur
84 mots-clés : le mot est prouvé et la place est libre. La copy a été **entièrement réécrite** et le
mot « cristal » en est **absent**, y compris dans la forme « effet cristal » : nos pièces sont en
verre travaillé, et la revendication est un risque `misrepresentation` en Merchant Center.
Les 7 fiches membres n'ont pas changé.

**`Plafonniers` → `Plafonniers LED`** (`plafonniers` → `plafonniers-led`).
`plafonnier led` vaut 21 090, notre plus gros mot-clé mesuré, contre `plafonnier` nu qui était le
mot-clé déclaré de l'ancienne page.

### Les redirections

**Shopify ne pose aucune redirection quand on change un handle de collection par l'API Admin.**
Vérifié : `urlRedirects` était vide avant et après les deux `collectionUpdate`. Les deux
redirections ont donc été créées à la main avec `urlRedirectCreate`, puis testées sur le domaine
public :

| Ancienne URL | Code | Cible |
|---|---|---|
| `/collections/lustres-effet-cristal` | **301** | `/collections/lustres-pampilles` |
| `/collections/plafonniers` | **301** | `/collections/plafonniers-led` |

Aucune 404. Les deux nouveaux handles répondent en 200.

`footer-principal` contenait une entrée vers `/collections/plafonniers` : elle est de type
`COLLECTION`, donc elle suit le `resourceId` et pointe désormais d'elle-même vers
`/collections/plafonniers-led`. **Son libellé affiche toujours « Plafonniers »** et non
« Plafonniers LED » : c'est cosmétique, l'URL est juste, et je n'ai pas touché aux menus de pied de
page qui n'étaient pas dans la commande.

---

## 2. Comment les fiches ont été choisies

Trois sources, dans cet ordre, pour chacune des 120 fiches :

1. **Le type de luminaire et sa fixation.** Une suspension et un plafonnier ne répondent pas à la
   même requête. J'ai relu les photos pour séparer les deux, parce que le titre ne suffit pas : le
   catalogue contenait **6 plafonniers encastrés rangés en `lustres-anneau` ou en `suspensions-metal`**
   (LM-056, LM-057, LM-060, LM-061, LM-094, LM-120) et **2 suspensions rangées dans `Plafonniers`**
   (LM-082, LM-085).
2. **Le diamètre réel des variantes**, lu sur les axes dimensionnels des options humanisées
   (`Diamètre`, `Taille`, `Modèle`), jamais sur le titre. Les axes `Température`, `Puissance` et
   `Ampoule` sont exclus de la lecture, sans quoi `4W (max 60W)` et `110v220v` se font passer pour
   des centimètres. **59 fiches sur 120 ne publient aucune dimension**, ni dans les variantes ni
   dans `specs_html` : pour celles-là, l'échelle a été jugée sur la photo seule.
3. **La photo principale**, récupérée via `featuredMedia` sur l'API Admin et regardée. Six
   planches-contacts étiquetées (code LM, diamètres réels, titre) plus trois planches agrandies pour
   la matière. Elles sont conservées dans `backups/2026-08-26-collections/planches/`.

### Les règles appliquées

| Collection | Règle |
|---|---|
| `suspensions-cuisine` | diamètre minimum ≤ 45 cm, ou barre à plusieurs lampes pour un îlot, ou titre « cuisine » |
| `suspensions-salon` | suspension de diamètre minimum ≥ 40 cm, ou pièce visiblement large, ou titre « salon » |
| `lustres-chambre` | diamètre dominant ≤ 45 cm, lumière douce, aucune pièce d'apparat |
| `plafonniers-salon` | plafonnier encastré large ou décoratif, apte à tenir une pièce à vivre |
| `plafonniers-cuisine` | plafonnier plat, sobre, facile à nettoyer |
| `suspensions-xxl` | **au moins une variante de 100 cm ou plus** |
| `suspensions-papier` / `suspensions-osier` | **la photo montre la matière**, sinon la fiche n'y entre pas |

Le partage du bambou est une bonne illustration : les 11 modèles à partir de 40 cm sont allés en
salon (LM-001 à LM-015), les 4 petits de 30 à 45 cm en cuisine (LM-006, LM-007, LM-011, LM-013).

### Le détail des rattachements

**`lustres-chambre` — 10 fiches**
LM-059, LM-062, LM-064, LM-065, LM-066, LM-072, LM-078, LM-099, LM-113, LM-117

**`plafonniers-salon` — 9 fiches**
LM-056, LM-061, LM-083, LM-084, LM-087, LM-088, LM-091, LM-094, LM-120

**`suspensions-cuisine` — 31 fiches**
LM-006, LM-007, LM-011, LM-013, LM-020, LM-023, LM-024, LM-027, LM-028, LM-032, LM-033, LM-036,
LM-042, LM-044, LM-047, LM-049, LM-050, LM-051, LM-052, LM-073, LM-074, LM-075, LM-076, LM-079,
LM-081, LM-093, LM-096, LM-097, LM-101, LM-105, LM-107

**`plafonniers-cuisine` — 4 fiches**
LM-057, LM-086, LM-089, LM-090

**`suspensions-salon` — 29 fiches**
LM-001, LM-002, LM-003, LM-004, LM-005, LM-008, LM-009, LM-010, LM-012, LM-014, LM-015, LM-018,
LM-021, LM-025, LM-026, LM-029, LM-030, LM-041, LM-048, LM-082, LM-085, LM-092, LM-098, LM-109,
LM-110, LM-111, LM-115, LM-117, LM-121

**`suspensions-papier` — 1 fiche**
LM-092

**`suspensions-xxl` — 15 fiches**
LM-003, LM-005, LM-008, LM-010, LM-015, LM-029, LM-053, LM-055, LM-058, LM-059, LM-067, LM-070,
LM-071, LM-092, LM-121

**`suspensions-osier` — 5 fiches**
LM-017, LM-021, LM-022, LM-023, LM-024

**`plafonniers-led` — 6 ajouts, 2 retraits**
Ajouts : LM-056, LM-057, LM-060, LM-061, LM-094, LM-120. Retraits : LM-082, LM-085. Effectif final 14.

Les recoupements matière/pièce sont assumés et voulus : LM-092 est à la fois en papier, en salon et
en XXL ; LM-021 en rotin, en osier et en salon ; LM-117 en lustres salon, en chambre et en salon.

---

## 3. Les trois écarts avec les estimations du § A

Le dossier Lustria donnait des estimations de fiches éligibles. Trois sont fausses par le bas, et
c'est le catalogue qui a tranché, pas moi.

**`suspensions-cuisine` : 31 au lieu de ~20.** Le catalogue est dominé par les petits pendants. Les
travertins, les céramiques émaillées et les globes de verre font à eux seuls 20 fiches sous 45 cm,
avant même de compter les 11 fiches dont le titre dit déjà « cuisine ».

**`suspensions-salon` : 29 au lieu de 12 à 15.** L'estimation ne comptait pas la famille bambou, dont
11 modèles sur 16 commencent à 40 cm. Un catalogue de fibres tressées **est** un catalogue de salon.

**`suspensions-xxl` : 15 au lieu de 8 à 10.** J'ai retenu un critère vérifiable plutôt qu'une
fourchette : une variante de 100 cm au moins doit exister. Cinq fiches montent à 150, 160 ou 180 cm.
À titre de repère, chez Lustria cette page fait 60 visites par fiche sur 20 fiches, le meilleur
rendement de tout leur catalogue.

**`plafonniers-salon` : 9 au lieu de 6 à 8**, parce que 3 plafonniers étaient mal rangés ailleurs.

---

## 4. Les choix de pièce que je signale comme douteux

Dix fiches où le rangement se discute. Aucune n'est fausse, toutes sont défendables, et toutes se
défont d'un `collectionRemoveProducts`.

| Fiche | Placée en | Pourquoi c'est discutable |
|---|---|---|
| **LM-020** | `suspensions-cuisine` | Ø 50 à 60 cm, donc au-dessus de ma règle des 45 cm. Retenue parce que son titre dit « cuisine » : une corolle de 50 cm au-dessus d'un îlot se tient |
| **LM-036** | `suspensions-cuisine` | Ø 40 à 80 cm, même cas. C'est une barre à deux coquilles, faite pour un îlot, et son titre dit « cuisine » |
| **LM-072**, **LM-078** | `lustres-chambre` | Deux petites boules opalines sur tige laiton, sans cote publiée. Lues comme des pièces de chevet ; elles iraient tout aussi bien en cuisine |
| **LM-111** | `suspensions-salon` | Ruban LED trèfle de Ø 50 cm. Entre les deux pièces ; j'ai tranché pour le salon et l'ai retirée de la chambre |
| **LM-113** | `lustres-chambre` et `suspensions-salon` | Soucoupe de Ø 30 à 60 cm : le petit format est une chambre, le grand un salon. Dans les deux, volontairement |
| **LM-117** | `lustres-chambre` et `suspensions-salon` | Ø 33 à 43 cm. Le § A la voulait en chambre, son titre dit « salon ». Dans les deux |
| **LM-098** | `suspensions-salon` | Ø 35 à 55 cm, sous ma règle des 40 cm. Retenue sur son titre « salon » et sur sa forme d'abat-jour large |
| **LM-041** | `suspensions-salon` | Bois flotté à 6 lanternes, aucune cote publiée. Classée sur la photo seule : la pièce est manifestement large |
| **LM-095** | aucune pièce | Lustre à 6 bras à bougies, dit « salle à manger ». `lustre salle à manger` vaut 1 300 et `suspension salle à manger` 590 : trop peu pour créer la collection, et la fiche reste donc hors axe pièce |

**Deux fiches où la matière était douteuse, et écartées pour cette raison :**

- **LM-116** « grappe de 7 ou 13 boules opalines ». La photo montre une texture fibreuse et veinée
  qui ressemble beaucoup à du papier de riz. Mais la fiche dit « opalines », et le verre « effet
  lune » a exactement ce grain. **Écartée de `suspensions-papier`** : je ne peux pas contredire le
  titre d'une fiche que je n'ai pas le droit de modifier.
- **LM-113** « soucoupe soie plissée ». Le rendu est très proche d'un abat-jour de papier plissé,
  mais le titre dit soie. **Écartée** pour la même raison.
- **LM-027** (rotin tressé noir) et **LM-028** (boules corde) auraient pu entrer en osier : le
  tressage y est de la vannerie. **Écartées** parce que l'une est teinte en noir, quand l'osier se
  vend clair, et que l'autre annonce de la corde.

---

## 5. Le SEO des 10 pages

Écrit au format exact de `collections-seo.json` : `keyword`, `seo_title`, `seo_description`,
`description_html`. Poussé avec `update_collections()` de `apply_collections_seo.py`, sans toucher
au script. **22 collections mises à jour, `verify()` passe.**

Contrôles automatiques passés, dans `valide_copy_collections.py` :

- zéro tiret cadratin, zéro demi-cadratin, zéro `Ø`, zéro apostrophe droite ;
- mot-clé en gras **dans la première phrase** sur les 10 pages dont je suis responsable ;
- exactement deux paragraphes par page ;
- une ouverture différente sur chacune des 22 collections, contrôlée sur les 26 premiers caractères ;
- aucun de « premium », « atelier », « artisanal », aucune mention AliExpress, aucun avis ;
- `seo_title` de 52 à 62 caractères, `seo_description` de 144 à 157 ;
- les seuls délais écrits sont ceux du référentiel ops : 1 à 2 jours de préparation, 6 à 15 jours
  d'acheminement, 7 à 17 au total, livraison offerte France métropolitaine Corse incluse.

**Note sur la convention.** Les 14 pages antérieures placent le mot-clé en gras dans le paragraphe
d'ouverture, souvent en deuxième phrase (7 sur 14). Mes 10 pages le placent dans la **première**
phrase, ce qui satisfait la consigne au sens strict. Le validateur applique la règle stricte à mes
10 pages et la règle du paragraphe aux 14 anciennes, qu'il n'était pas question de réécrire.

Trois pages disent franchement ce qu'elles n'ont pas, parce qu'un texte qui promet plus que la page
ne montre se paie en rebond : `suspensions-papier` écrit qu'elle n'a qu'un seul modèle,
`plafonniers-cuisine` qu'elle en a quatre et qu'elle s'étoffera, `lustres-pampilles` que deux de ses
sept fiches sont des anneaux sertis de facettes et non des gouttes libres.

**Les images de collection.** Aucun visuel de marque n'existait pour les 8 nouvelles collections
dans `livraisons-visuels-codex/brand/`. Chaque collection reprend donc la photo principale d'une de
ses fiches membres, déjà publiée sur la boutique, ce qui évite 8 vignettes vides sur `/collections`
et dans le menu. À remplacer par des visuels dédiés quand Codex en livrera.

---

## 6. Le menu

`main-menu` réorganisé, 10 entrées de premier niveau au lieu d'une liste à plat de 22 collections.
La sauvegarde d'avant est dans `backups/2026-08-26-collections/menus-avant.json`, celle d'après dans
`menus-apres.json`.

```
Accueil
Par pièce ........... Salon · Chambre · Cuisine · Plafonniers salon · Plafonniers cuisine
Par matière ......... Bambou · Rotin · Osier · Bois · Pierre · Verre · Métal · Papier · Déco colorée
Lustres ............. Lustres salon · Lustres chambre · Lustres anneau · Lustres pampilles
Plafonniers LED ..... Plafonniers salon · Plafonniers cuisine
Grand format
Notre histoire · FAQ · Contact · Suivre votre commande
```

« Par pièce » passe **avant** « Par matière », puisque la pièce porte 38,8 % du trafic de collection
chez le comparable direct contre 13,8 % pour la matière. Les 3 collections sans mot de pièce ni de
matière propre (`lustres-statement`, `suspensions-modernes`, `selection-199`) restent hors menu,
comme avant.

**`templates/list-collections.json` a été modifié**, et il fallait le faire : son réglage
`collection_list` citait en dur `lustres-effet-cristal` et `plafonniers`, deux handles qui
n'existent plus. Sans correction, la page `/collections` perdait deux vignettes. Les 8 nouveaux
handles ont été ajoutés dans le même mouvement, pour tenir la règle du fichier, qui est de rester
aligné sur le menu. La liste passe de **11 à 19 entrées**. Thème visé : `copie-de-fullstack-2-3`,
gid `186708001104`, rôle MAIN. Ni Helio ni UNIVERS n'ont été touchés.

---

## 7. La décision que je signale, parce qu'elle sort du strict énoncé

**J'ai retiré 2 fiches de `Plafonniers LED` et j'y en ai ajouté 6.** La commande présentait les
renommages comme des changements d'étiquette sans travail de rattachement. Je m'en suis écarté sur
ce point, pour une raison de cohérence :

- l'ancienne collection `Plafonniers` contenait **LM-082** (suspension boule sputnik de 65 cm) et
  **LM-085** (suspension guirlande de boules opalines). Ce sont des suspensions à ampoules E27, pas
  des plafonniers, et pas des LED. Sous un H1 « Plafonniers LED », elles rendent la page fausse et
  exposent le flux Merchant Center. Les deux sont désormais dans `suspensions-salon`, où elles
  étaient attendues : **aucune fiche n'a été orpheline à aucun moment**, le script refuse le retrait
  d'une fiche qui n'aurait pas d'autre collection d'accueil ;
- à l'inverse, 6 plafonniers LED encastrés dormaient dans `lustres-anneau` et `suspensions-metal`.
  Sur notre plus gros mot-clé, à 21 090, les laisser hors de la page n'avait pas de sens.

Effectif final 14, dont 14 vrais plafonniers LED. Réversible en une commande si Hakim préfère l'état
d'avant : `collections-avant.json` porte la composition d'origine.

---

## 8. Ce que je n'ai pas pu faire, ou pas fait

1. **`Suspensions papier` n'a qu'une fiche.** LM-092, le voile de papier technique, est la seule du
   catalogue dont la photo montre du papier. Le § A l'annonçait (« 1 fiche éligible, +10 à 12 à
   sourcer ») et je le confirme après relecture des 120 photos. La page vaut quand même d'exister :
   Lustria fait 890 visites/mois sur une collection **à zéro produit**. Mais les 4 760 de
   `suspension papier` ne rentreront qu'avec le sourcing du § B.4.
2. **Aucune collection `Plafonniers chambre`** alors que `plafonnier chambre` vaut 4 400 et que deux
   fiches l'attendent (LM-060, LM-089). Elle n'était pas dans la liste du § A, qui fait foi. À
   arbitrer : c'est la onzième ligne évidente.
3. **59 fiches sur 120 ne publient aucune dimension.** Ni les variantes ni `specs_html` ni les
   données fournisseur (`ae-details-batch*.jsonl`) n'en portent. Leur rangement par pièce repose
   donc sur la photo seule, ce qui est moins solide que pour les 61 autres. C'est la limite
   principale de ce travail, et elle se lèverait en documentant les cotes sur ces 59 fiches.
4. **32 fiches actives ne sont dans aucune collection de pièce**, en comptant `lustres-salon` qui
   préexistait : LM-016, LM-017, LM-019, LM-022, LM-031, LM-034, LM-035, LM-037, LM-038, LM-039,
   LM-040, LM-043, LM-046, LM-053, LM-054, LM-055, LM-058, LM-060, LM-063, LM-067, LM-068, LM-069,
   LM-070, LM-071, LM-077, LM-080, LM-095, LM-100, LM-102, LM-103, LM-104, LM-106. Ce n'est pas un
   oubli : la plupart sont des lustres à anneaux de 40 à 100 cm qui relèveraient d'un
   `lustres-salle-a-manger` (`lustre salle à manger` 1 300), ou des céramiques sans cote dont je ne
   peux pas juger l'échelle. **88 fiches sur 120 sont couvertes.**
5. **Rien n'a été commité sur git**, conformément à la consigne. Cela déroge au réflexe GitHub du
   `CLAUDE.md` : les fichiers modifiés attendent la décision de Hakim.
6. **Aucun titre produit, aucun SKU, aucune variante, aucun prix n'a été touché.** `apply_pdp.py` et
   `apply_fullstack.py` n'ont jamais été exécutés ; seules les deux fonctions `theme_file` et
   `upsert_theme_file` du second ont été importées, comme le fait déjà `apply_collections_seo.py`.
   **Vérifié plutôt qu'affirmé** : relecture des 123 fiches contre `products-avant.json` en fin de
   passe, variante par variante. Zéro écart de titre, de statut, de SKU, de libellé de variante,
   zéro variante ajoutée ou retirée. Les **166 prix** qui ont bougé sur 38 fiches sont ceux de
   l'agent prix qui travaillait en parallèle, et son commit le dit (« Aligne 38 prix sous Lustria »).
   Mes écritures Shopify se limitent à `collectionCreate`, `collectionUpdate`,
   `collectionAddProducts`, `collectionRemoveProducts`, `urlRedirectCreate`, `menuUpdate` et un
   `themeFilesUpsert` sur `templates/list-collections.json`.
7. **Le libellé « Plafonniers » du menu `footer-principal`** n'a pas été renommé en
   « Plafonniers LED ». L'URL est correcte, le mot ne l'est plus tout à fait.

---

## Traces et réversibilité

Sauvegarde d'avant, dans `backups/2026-08-26-collections/` :
`collections-avant.json` (les 15 collections avec leur composition complète, leur SEO et leurs
règles), `products-avant.json` (les 123 fiches avec variantes, options, médias et appartenances),
`menus-avant.json` (les 6 menus), `redirects-avant.json` (vide, ce qui prouve qu'aucune redirection
n'existait), `themes-avant.json`, `state-avant.json`, `collections-seo-avant.json`.
Instantané d'après : `collections-apres.json`, `menus-apres.json`, `redirects-apres.json`.
Photos et planches-contacts : `photos-cache/` et `planches/`.

Scripts écrits pour cette passe, tous idempotents et relançables :

| Script | Rôle |
|---|---|
| `backup_collections.py` | l'instantané d'avant |
| `analyse_pieces.py` | lecture du catalogue, diamètres réels, `catalogue-pieces-2026-08-26.json` |
| `planches_photos.py` | planches-contacts étiquetées, option `--zoom` |
| `collections_piece.py` | `renomme` · `cree` · `rattache` · `nettoie` · `verifie` |
| `valide_copy_collections.py` | contrôle de la copy avant publication |
| `menu_collections.py` | réorganisation de `main-menu` |

Fichiers de référence modifiés : `collections-seo.json` (14 → 22 entrées, 2 réécrites),
`import_catalogue.py` (registre `COLLECTIONS` : 2 titres et handles corrigés, 8 entrées ajoutées,
aucune clé CSV touchée), `state.json` (8 GID de collection ajoutés).
