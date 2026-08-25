# Humanisation des 120 fiches produit — Lumière Matière

Store `nzefxg-gg.myshopify.com` · 25/08/2026 · reprise après plantage de l'agent précédent.

## Résultat

| Mesure | Valeur |
|---|---|
| Fiches poussées | `copy OK 120/120` |
| FAIL | 0 |
| Titres uniques en live | 120 / 120 |
| Doublons restants | 0 |
| Tirets cadratins et demi-cadratins en live | 0 |
| Métafields absents | 0 |
| Écarts entre `pdp-copy.json` et le live | 0 |

Champs envoyés par fiche : `title`, `descriptionHtml`, `seo.title` (≤ 70), `seo.description` (≤ 320), et les métafields `custom.usps`, `custom.specs`, `custom.installation`, `custom.benefits`, `custom.faq`.

## État avant reprise

L'agent précédent avait bien réécrit `pdp-copy.json`, mais n'avait rien poussé : le dump live du 25/08 à 16 h montrait encore les 13 groupes de doublons intacts, soit 32 fiches partageant un titre avec au moins une autre. Aucun push partiel à rattraper.

## Les 13 groupes de doublons

### « Suspension déco en céramique, LED » (4 fiches)

- `suspension-deco-led-077631` → **Suspension céramique à fleurs bleues, douille laiton**
- `suspension-deco-led-689455` → **Suspension 3 lumières, céramique nervurée et laiton**
- `suspension-deco-led-837156` → **Suspension céramique festonnée, vert céladon ou bleu poudré**
- `suspension-deco-led-889929` → **Suspension grappe de cônes en céramique, deux modèles**

### « Suspension effet pierre, LED » (4 fiches)

- `suspension-effet-pierre-led-073999` → **Suspension effet pierre, galet plat sur tige de bois clair**
- `suspension-effet-pierre-led-147607` → **Suspension effet pierre, trois formes au choix**
- `suspension-effet-pierre-led-338324` → **Suspension effet pierre, large cylindre à capot noyer**
- `suspension-effet-pierre-led-445794` → **Suspension effet pierre, cylindre étroit, bois clair ou foncé**

### « Suspension bois, LED » (3 fiches)

- `suspension-bois-led-453740` → **Suspension bois en forme de guitare, 6 lanternes de verre**
- `suspension-bois-led-830581` → **Suspension bois tourné, ampoule globe apparente**
- `suspension-bois-led-934110` → **Suspension tube vertical effet travertin, rosace bois foncé**

### « Suspension rotin tressée » (3 fiches)

- `suspension-rotin-272937` → **Suspension corde de chanvre tressée, 1 ou 3 lumières**
- `suspension-rotin-469688` → **Suspension rotin tressé, 3 lanternes sur platine noire**
- `suspension-rotin-623305` → **Suspension rotin tressé, abat-jour tambour, une lumière**

### « Lustre anneau LED, 4 lumières et 6 lumières » (2 fiches)

- `lustre-anneau-led-led-625575` → **Plafonnier anneaux LED blancs, 4 ou 6 lumières, platine chromée**
- `lustre-anneau-led-led-717226` → **Lustre anneaux LED blancs, 4 ou 6 lumières, tige de suspension**

### « Lustre anneau LED, Ø 40–100 cm, noir, café ou doré » (2 fiches)

- `lustre-anneau-led-led-dore-418494` → **Lustre 6 anneaux LED superposés, noir, café ou doré**
- `lustre-anneau-led-led-noir-dore-024410` → **Lustre anneaux LED en cascade, 1 à 4 anneaux, noir, café ou doré**

### « Plafonnier LED, intérieur » (2 fiches)

- `plafonnier-led-led-637673` → **Plafonnier LED rond, lumière colorée et enceinte intégrée**
- `plafonnier-led-led-922186` → **Suspension guirlande de globes opalins, 5 à 20 globes**

### « Suspension bambou tissée, LED, Ø 40–100 cm, câble blanc, noir ou doré » (2 fiches)

- `suspension-bambou-led-033589` → **Suspension bambou tressé, 3 vagues en cascade, Ø 40 à 100 cm**
- `suspension-bambou-led-583180` → **Suspension bambou tressé, une vague, Ø 40 à 100 cm**

### « Suspension bambou tissée, LED, Ø 40–80 cm » (2 fiches)

- `suspension-bambou-led-80-cm-191307` → **Suspension bambou tressé en vague, câble souple, Ø 40 à 80 cm**
- `suspension-bambou-led-80-cm-236157` → **Suspension bambou tressé en vague, tige rigide, Ø 40 à 80 cm**

### « Suspension bambou tissée, Ø 30–45 cm » (2 fiches)

- `suspension-bambou-655008` → **Suspension dôme en bambou tressé serré, tige de bois**
- `suspension-bambou-655463` → **Suspension coupole en bambou tressé, câble noir**

### « Suspension bois, LED, Ø 40–80 cm » (2 fiches)

- `suspension-bois-led-582321` → **Suspension double coquille en bois tressé, rosace ronde dorée**
- `suspension-bois-led-989306` → **Suspension double coquille en bois tressé, platine linéaire blanche**

### « Suspension déco en céramique, blanc » (2 fiches)

- `suspension-deco-348096` → **Suspension dôme en céramique blanche ajourée**
- `suspension-deco-blanc-560098` → **Suspension double en céramique à motifs bleus, laiton**

### « Suspension métal, LED, doré » (2 fiches)

- `suspension-metal-led-dore-952116` → **Suspension céramique bleu et blanc, monture laiton**
- `suspension-metal-led-dore-975417` → **Suspension corolle plissée blanche, cordon doré**

## Titres corrigés hors doublons

84 fiches non concernées par les doublons ont quand même changé de titre. Deux mécanismes :

**28 titres par simple normalisation.** `Ø 40–100 cm` devient `Ø 40 à 100 cm`, parce que le demi-cadratin est interdit dans les chaînes client et que Shopping le lit mal ; « 4 lumières, 6 lumières et 8 lumières » devient « 4, 6 ou 8 lumières ».

**56 titres réécrits parce que la photo contredisait le titre.** Ces fiches annonçaient une matière ou un type de luminaire que l'image ne montre pas. `TITLE_OVERRIDES` compte donc 88 entrées : 32 pour les doublons, 56 pour ces corrections. Exemples relevés à l'audit :

| Handle | Ancien titre | Nouveau titre | Ce que montre la photo |
|---|---|---|---|
| `suspension-bois-193329` | Suspension bois | Suspension travertin à capot noyer, bois clair ou foncé | cylindre de travertin, seul le capot est en bois |
| `suspension-metal-dore-037279` | Suspension métal, doré ou blanc | Suspension dôme en céramique gaufrée, monture laiton | dôme céramique, le laiton n'est que la monture |
| `plafonnier-led-led-442025` | Plafonnier LED, Ø 65 cm, intérieur | Suspension boule d'épines dorées, Ø 65 cm | sphère de tiges suspendue, pas un plafonnier |
| `plafonnier-led-led-922186` | Plafonnier LED, intérieur | Suspension guirlande de globes opalins, 5 à 20 globes | guirlande tendue de globes acryliques |
| `lustre-anneau-led-007557` | Lustre anneau LED, blanc ou noir | Plafonnier LED connecté, lumière RVB, blanc ou noir | diffuseur plaqué au plafond, lumière couleur |
| `suspension-metal-led-dore-843772` | Suspension métal, LED, Ø 40–80 cm, doré | Plafonnier 3 anneaux LED dorés, Ø 40 à 80 cm | trois anneaux plaqués au plafond |
| `suspension-metal-noir-dore-361680` | Suspension métal, 4 lumières… | Lustre laiton à bougies, 4, 6 ou 8 bras | lustre à bras et douilles bougie |
| `suspension-rotin-dore-865596` | Suspension rotin tressée, Ø 39–85 cm, doré | Suspension bois deux pétales, Ø 39 à 85 cm, monture dorée | deux pétales de bois, pas de rotin |
| `suspension-rotin-489600` | Suspension rotin tressée, Ø 40–80 cm | Suspension paille brute, Ø 40 à 80 cm | paille en couronne, brins libres |
| `suspension-verre-928640` | Suspension verre | Suspension galet en verre fumé à micro-LED, monture laiton | galet aplati, micro-LED sur fils cuivre |
| `suspension-verre-led-dore-436718` | Suspension verre, LED, doré | Suspension arceau laiton et globes opale, doré ou noir | arceau en U, deux globes opale |
| `lustre-salon-blanc-246282` | Lustre salon, Ø 30–60 cm, blanc | Suspension soucoupe en soie tendue, Ø 30 à 60 cm, blanc | soie tendue sur armature, forme soucoupe |
| `lustre-salon-blanc-575463` | Lustre salon, Ø 33–43 cm, blanc | Suspension rose en pétales acryliques, Ø 33 à 43 cm | corolle de pétales acryliques |
| `lustre-salon-957153` | Lustre salon, LED, Ø 50 cm | Suspension ruban LED en trèfle, Ø 50 cm, doré | profilé doré replié en trèfle |
| `plafonnier-led-led-dore-blanc-354637` | Plafonnier LED, Ø 30–55 cm, blanc ou doré, intérieur | Plafonnier coupole plissée en acrylique, Ø 30 à 55 cm | coupole plissée blanche, aucune variante dorée |

Quatre fiches gardent leur titre d'origine : il était déjà descriptif et sans tiret.

## Corrections de fond au-delà des titres

L'audit photo a fait apparaître trois familles d'erreurs dans la copy, corrigées dans `humanise_pdp.py` :

**Famille de produit.** `FAMILY_OVERRIDES` reclasse 18 fiches dont la famille du catalogue contredisait l'image (un « plafonnier » qui est une suspension, une « suspension métal » qui est en céramique). La copy suit désormais la photo, pas la classification.

**Matière.** `MATTER_OVERRIDES` décrit la matière réelle pour 53 fiches, avec au besoin une intro et des angles dédiés quand le texte de famille aurait produit une affirmation fausse. Exemple : la famille « Suspensions verre » ouvrait sur « un globe, une cloche, une grappe », ce qui ne décrit ni un galet à micro-LED ni un arceau à deux globes.

**Source lumineuse.** `detect_source` retombait sur « mixte » (« LED intégrée ou douille E27 selon la variante ») pour 34 fiches. La plupart n'offraient aucun axe de variante permettant ce choix : la fiche promettait une option inexistante. 31 sont désormais typées d'après la photo et les données fournisseur, dont 27 en douille E27 (ampoule visible sur l'image ou axe `Ampoule` à valeur unique « ampoule non fournie »), une en G9 (`suspension-verre-091815`, dont les nuggets de verre sont trop petits pour un E27), une en E14 et deux en LED intégrée. Il reste 3 fiches en « mixte » : `suspension-verre-394147`, `suspension-rotin-dore-435189` et `suspension-bois-832012`, les seules où l'axe propose réellement « ampoule non fournie » face à une température de blanc.

Après overrides, la répartition des 120 fiches est de 70 en LED intégrée, 44 en douille E27, 2 en G9, 1 en E14 et 3 en mixte. `SOURCE_OVERRIDES` compte 41 entrées, dont 10 posées lors de l'audit précédent sur des fiches que `detect_source` classait déjà à tort en LED.

Deux nettoyages transverses complètent ça : un post-traitement retire des textes de famille les gestes réservés aux fiches à douille quand la LED est intégrée (« même avec une ampoule assez forte » devient « même à pleine puissance »), et les specs ne répètent plus le nom de l'axe dans ses valeurs (« Modèle : Modèle A, Modèle B » se lit « Modèle : A, B »).

## Chiffres ops FROZEN

Présents à l'identique sur 120/120 fiches, vérifiés champ par champ : 16h00 heure de Paris, 1 à 2 jours de préparation, 6 à 15 jours d'acheminement, 7 à 17 jours au total, livraison offerte en France métropolitaine Corse incluse, retours 30 jours plus 14 jours de rétractation, service client du lundi au vendredi de 10h00 à 18h00, réponse sous 24 h ouvrées.

## Contrôle live, 0 cadratin

Échantillon GraphQL sur `title`, `descriptionHtml`, `seo` et le métafield `custom.faq` :

```
handle : suspension-verre-led-489156
title  : Suspension nuages en verre soufflé LED, Ø 20 à 40 cm
seo    : Suspension nuages en verre soufflé LED, Ø 20 à 40 cm | Lumière Matière
desc   : <p>Le verre est la seule matière qui laisse la lumière traverser entièrement. […]
faq[3] : Livraison offerte en France métropolitaine, Corse incluse. On prépare le colis
         en 1 à 2 jours ouvrés, l'acheminement prend 6 à 15 jours ouvrés, soit 7 à 17 […]

cadratins U+2014 : 0 | demi-cadratins U+2013 : 0
```

Le balayage complet des 120 fiches (titre, description, SEO, cinq métafields) donne également 0 cadratin et 0 demi-cadratin.

**Réserve à traiter ailleurs :** les *valeurs d'option* live contiennent encore des cadratins et du texte fournisseur brut (`Ø 92 cm — — Blanc`, `3 head Transparent glass`, `Dimmable by Remote`, `one 8.Ø 5 cm glass`). Elles ne passent pas par `push_copy` et sortaient du périmètre de cette mission. La copy les nettoie pour l'affichage dans `specs`, mais le sélecteur de variante les montre telles quelles. Les textes alternatifs des médias contiennent aussi des cadratins (`Suspension effet pierre — vue 1`).

## Option `suspension-effet-pierre-092465` : renommée

« Blanc chaud » est devenu **« Pierre claire »**, sur l'axe `Couleur`, sans toucher au SKU.

La justification ne vient pas seulement de la photo. Le dump d'import montre l'axe fournisseur d'origine : `Body Color` avec les valeurs `Light Yellow` et `Brown`, SKU `200000531:200006153` et `200000531:365458`. « Blanc chaud » était donc une mauvaise traduction d'une couleur de corps, sur un axe où l'autre valeur est « Brun ». Laissée telle quelle, elle se lisait comme une température de 2700 K et laissait croire à un choix d'éclairage qui n'existe pas.

Les cinq visuels confirment la lecture : cylindre de pierre translucide crème sous une tige brune. « Pierre claire » nomme la teinte minérale du corps et lève l'ambiguïté.

Mutation utilisée : `productOptionUpdate` avec `variantStrategy: LEAVE_AS_IS` et `optionValuesToUpdate` sur le seul libellé. Vérification avant/après :

```
SKU avant : ['200000531:200006153', '200000531:365458']
SKU apres : ['200000531:200006153', '200000531:365458']
userErrors: []
```

## Confirmations

**SKU DSers intouchés.** Les 602 SKU distincts répartis sur 629 variantes sont identiques au jeu de référence `variants-work.json` : 0 disparu, 0 apparu, ensembles égaux. `clean_variants` n'a pas été lancé, aucune variante n'a été recréée, aucune fiche n'a été splittée.

**Thème non écrit.** Aucune mutation de thème n'a été émise, ni sur le Full Stack de travail `gid://shopify/OnlineStoreTheme/186708001104`, ni sur Helio MAIN `186709180752`, ni sur UNIVERS. Aucun fichier de thème ni page markdown n'a été modifié : la copy est passée uniquement par `productUpdate` et les métafields `custom.*`.

**`apply_pdp.py` non lancé en entier.** `main()` n'a jamais été appelé, donc `build_pdp_copy.py` n'a pas régénéré la copy et `templates/product.json` n'a pas été réécrit. Seuls `fetch_products` et `push_copy` ont été importés depuis le module, appelés sur le `pdp-copy.json` humanisé.

## Fichiers modifiés

| Fichier | Nature |
|---|---|
| `humanise_pdp.py` | titres, familles, matières, source lumineuse, nettoyage des valeurs d'option, post-traitements LED et longueur |
| `pdp-copy.json` | régénéré, 120 fiches |
| `HUMANISATION-PDP-2026-08-25.md` | ce rapport |

Backup de l'état antérieur : `backups/2026-08-25-humanisation/pdp-copy.avant.json`.
