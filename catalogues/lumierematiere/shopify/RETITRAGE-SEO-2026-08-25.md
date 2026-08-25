# Retitrage SEO des 120 fiches — Lumière Matière

Store `nzefxg-gg.myshopify.com` · 25/08/2026 · application de `CONVENTION-TITRES-2026-08-25.md`.

Les titres éditoriaux (« Suspension nuages en verre soufflé LED, Ø 20 à 40 cm ») sont remplacés
par des titres composés de requêtes, lisibles par Google Shopping. Aucune convention nouvelle
n'a été inventée : la grille, les listes de valeurs et le contrôle automatique viennent de la
convention. Le travail photo de la passe précédente (`HUMANISATION-PDP-2026-08-25.md`) est
conservé, y compris ses 13 requalifications de type de luminaire.

## Résultat

| Mesure | Avant | Après | Cible |
|---|---|---|---|
| Titres uniques | 120 / 120 | **120 / 120** | 120 |
| Longueur moyenne | 50,0 c. | **46,2 c.** | 40–60 |
| Longueur médiane | 52 c. | **46 c.** | ~51 (médiane du marché) |
| Minimum / maximum | 30 / 67 | **40 / 55** | plafond dur 65 |
| Hors fourchette 40–60 | 32 | **0** | 0 |
| Titres portant `Ø` | 53 | **0** | 0 |
| Titres portant une plage `\d+ à \d+ cm` | 50 | **0** | 0 |
| Titres au-dessus de 65 c. | 1 | **0** | 0 |
| **Matière présente** | 89 (74 %) | **100 (83 %)** | ≥ 70 % |
| **Couleur ou finition présente** | 63 (53 %) | **120 (100 %)** | ≥ 60 % |
| Mots d'ambiance | 0 | **0** | 0 |
| Marque dans le titre | 0 | **0** | 0 |
| Cadratin, demi-cadratin, pipe, deux-points | 0 | **0** | 0 |

Le taux de couleur passe de 53 % à 100 %, soit très au-dessus des 36,7 % du corpus Shopping
concurrentiel et des 73,5 % de Mille et une Nuisette. C'est le critère d'arbitrage d'un acheteur
à 149–499 €, et c'est là que le catalogue prend l'avantage.

## Ce qui a été poussé

117 fiches modifiées, 3 déjà conformes (`suspension-rotin-dore-865596`,
`suspension-bois-193329`, `suspension-effet-pierre-led-073999` — leur titre cible était déjà
celui donné en exemple par la convention). Champs envoyés : `title`, `seo.title` et
`seo.description` — cette dernière renvoyée à l'identique, pas modifiée.

`seo_title` = titre + ` | Lumière Matière`, coupé à 70 caractères. Un seul titre (55 c.) déborde
le budget : la coupe reprend la règle segment par segment de `humanise_pdp.seo_title_of`, qui
tronque sur la dernière virgule plutôt qu'au milieu du nom de marque.

**Piège rencontré, à retenir pour les prochaines passes.** `ProductInput.seo` est un objet
remplacé en bloc, pas fusionné champ par champ : envoyer `seo: {title}` seul **efface**
`seo.description`. Le premier push a ainsi vidé les 117 meta descriptions concernées. Le script
renvoie désormais toujours les deux champs, la description reprise telle quelle depuis
`pdp-copy.json`. Restauration vérifiée en live : **120 / 120 identiques au caractère** à l'état
pré-push relevé dans `titles-media-dump.json`. Les 3 fiches non poussées n'avaient jamais été
touchées.

Le script `retitle_seo.py` est idempotent : la seconde exécution a rapporté
`0 modifiés, 120 déjà à jour`. Relecture live après push : 0 écart de titre, 0 écart de
`seo_title`, 0 caractère interdit, 0 dépassement de 65 caractères, 120 / 120 uniques.

## Les trois défauts systématiques, corrigés

**Le symbole `Ø` et les plages de tailles.** 53 titres portaient `Ø`, 50 une plage. Aucune plage
ne subsiste. Aucune dimension n'a été remplacée par une autre dimension : une seule fiche garde
un chiffre, `Suspension boule sputnik métal doré, 65 cm`, parce que la pièce n'a qu'un diamètre.
Les très grandes pièces (Ø 60 à 150 cm) portent `XXL`, la formulation que Google propose
lui-même en recherche associée sur `suspension rotin XXL` :
`Suspension bambou XXL tressé, pétales naturels`, `Suspension rotin XXL tressé, pétales naturels`,
`Suspension barres LED croisées, métal noir XXL`.

**Les noms d'invention.** « nuages » devient `cascade` ou `grappe`, « boule d'épines » devient
`boule sputnik`, « capot noyer » devient `tête noyer`, « galet plat sur tige de bois clair »
devient `galet effet pierre, tige bois clair`. Tous les mots retenus viennent des listes de la
convention (formes, couleurs, matières) ou des recherches associées relevées le 25/08
(`3 lampes`, `XXL`, `naturel`, `moderne`, `vintage`, `cuisine`, `salon`).

**L'absence de couleur.** 57 titres n'en portaient aucune. Les 120 en portent une désormais,
lue sur la photo ou sur l'axe de variante correspondant, jamais devinée.

## Où j'ai tranché — photo contre classification

### Les 13 requalifications de type de luminaire, conservées

La règle 2 de la convention veut que le premier mot soit celui de la collection. Treize fiches y
dérogent, et c'est volontaire : ce sont exactement les fiches que la passe photo précédente avait
requalifiées, parce que l'image montre autre chose que la collection ne dit. Les défaire aurait
réintroduit un type de luminaire faux, ce qui est un risque `misrepresentation` plus grave qu'un
désalignement de mot-clé.

| Handle | Collection | Premier mot retenu | Ce que montre la photo |
|---|---|---|---|
| `lustre-anneau-led-led-625575` | Lustres anneau | `Plafonnier` | anneaux plaqués au plafond sur platine chromée |
| `lustre-anneau-led-007557` | Lustres anneau | `Plafonnier` | diffuseur rond plaqué au plafond, lumière RVB |
| `lustre-salon-led-366435` | Lustres salon | `Suspension` | ruban doré suspendu sur câbles |
| `lustre-salon-957153` | Lustres salon | `Suspension` | profilé doré replié en trèfle, suspendu |
| `lustre-salon-blanc-246282` | Lustres salon | `Suspension` | soucoupe de soie tendue sur un seul câble |
| `lustre-salon-led-630766` | Lustres salon | `Suspension` | anneau sur trois câbles fins |
| `lustre-salon-blanc-575463` | Lustres salon | `Suspension` | corolle de pétales acryliques sur câble |
| `lustre-salon-led-784326` | Lustres salon | `Plafonnier` | palets plaqués sur bras au plafond |
| `lustre-salon-led-341706` | Lustres salon | `Suspension` | coupole organique sur câbles |
| `suspension-metal-led-dore-843772` | Suspensions métal | `Plafonnier` | trois anneaux plaqués au plafond |
| `suspension-metal-noir-dore-361680` | Suspensions métal | `Lustre` | lustre à bras et douilles bougie |
| `plafonnier-led-led-442025` | Plafonniers | `Suspension` | sphère de tiges suspendue à une tige |
| `plafonnier-led-led-922186` | Plafonniers | `Suspension` | guirlande de globes tendue sur câbles |

### Les matières où la photo contredit le libellé de collection

Ces fiches vivent dans une collection dont elles ne portent pas la matière. Le titre nomme la
matière de la photo, pas celle de la collection — refuser de le faire aurait été un gain de
mot-clé payé par une affirmation fausse.

| Handle | Collection | Matière écrite | Vérification photo |
|---|---|---|---|
| `suspension-rotin-489600` | Suspensions rotin | `paille` | couronne de brins de paille libres, aucun rotin tressé |
| `suspension-rotin-272937` | Suspensions rotin | `corde` | petits globes de corde tressée fine, monture noire |
| `suspension-rotin-477244` | Suspensions rotin | `corde` | corolle ondulée de corde, beige ou chanvre |
| `suspension-rotin-443915` | Suspensions rotin | `corde` | cloche de corde, kaki ou noir |
| `suspension-rotin-led-761433` | Suspensions rotin | `fibre` | corolle de pétales en fibre tressée |
| `suspension-rotin-dore-865596` | Suspensions rotin | `bois` | deux pétales de bois sur monture dorée |
| `suspension-bois-193329` | Suspensions bois | `travertin` | cylindre de travertin, seul le capuchon est en bois |
| `suspension-bois-led-245113` | Suspensions bois | `travertin` | cylindre de travertin cerclé d'un anneau de noyer |
| `suspension-bois-led-934110` | Suspensions bois | `travertin` | tube vertical de travertin, rosace bois foncé |
| `suspension-bois-led-30cm-886635` | Suspensions bois | `céramique` | abat-jour de céramique plissée, tête bois |
| `suspension-bois-led-121862` | Suspensions bois | `céramique` | abat-jour de céramique festonné, tête bois |
| `suspension-metal-led-dore-952116` | Suspensions métal | `céramique` | dôme de céramique bleu et blanc, monture laiton |
| `suspension-metal-dore-037279` | Suspensions métal | `céramique` | dôme de céramique gaufrée, le laiton n'est que la monture |
| `suspension-metal-led-dore-975417` | Suspensions métal | `céramique` | corolle de céramique plissée blanche, cordon doré |
| `suspension-metal-dore-502141` | Suspensions métal | `tissu` | abat-jour de tissu sur armature laiton |
| `suspension-metal-led-dore-701414` | Suspensions métal | `papier` / `soie` | voile blanc, deux matières selon l'axe de variante |
| `plafonnier-led-led-dore-blanc-354637` | Plafonniers | `acrylique` | coupole plissée blanche, aucune variante dorée |
| `lustre-salon-blanc-575463` | Lustres salon | `acrylique` | pétales acryliques blancs |

### Les paires quasi identiques, séparées par un attribut vérifiable

Six paires de fiches montrent des produits très proches. Chaque paire est départagée par un
attribut lisible sur la photo, jamais par un mot ajouté pour faire nombre.

| Paire | Départage |
|---|---|
| `lustre-anneau-led-led-717226` / `…-625575` | `tige de suspension` contre `platine chromée` — la première pend, la seconde est plaquée |
| `lustre-salon-led-240560` / `…-630766` | `effet cristal` contre `verre facetté`, et lustre contre suspension |
| `suspension-verre-led-489156` / `suspension-verre-091815` | `cascade` verticale contre `grappe` étalée ; la première est en LED intégrée, la seconde en G9 |
| `lustre-cristal-led-led-dore-841671` / `lustre-cristal-led-dore-202521` | couronne de `perles` dressées contre `cascade` de pampilles tombantes |
| `lustre-salon-led-254609` / `lustre-statement-led-noir-950316` | `noir et doré, 12 globes` contre `laiton et noir, 6 globes` |
| `lustre-salon-led-784326` / `plafonnier-led-led-183789` | `blanc, noir ou doré` contre `gris ou blanc` — les deux axes de finition réels |

### Les trois mots de pièce utilisés

Jamais en liste, et seulement quand la photo confirme l'usage.

| Handle | Mot | Justification |
|---|---|---|
| `plafonnier-led-led-728204` | `cuisine` | la photo produit montre la réglette au-dessus d'un îlot de cuisine ; `plafonnier LED cuisine` est une recherche associée relevée |
| `lustre-salon-blanc-246282` | `salon` | soucoupe de 30 à 60 cm, pièce de plafond de salon ; `plafonnier LED salon` et `suspension verre salon` sont attestés |
| `lustre-salon-blanc-575463` | `salon` | corolle acrylique de la collection Lustres salon, même usage |

## Écarts assumés par rapport à la convention

**Un seul bloc : 10 titres sur 120, contre 93,3 % chez Mille et une Nuisette.** C'est l'écart le
plus visible et il est délibéré. Mille et une Nuisette tient un seul bloc parce qu'elle articule
par les prépositions (`en Satin`, `à Dentelle`) — 51,5 % et 25,7 % de ses titres. La convention
nous interdit précisément cette articulation : § « Suspension bambou ou Suspension en bambou »,
forme nue, sans `en`. Sans préposition et sans ponctuation, il ne reste qu'une file de mots
(« Suspension bambou dôme tressé tige bois clair »), qui est de la juxtaposition de mots-clés.
La virgule reste donc utilisée dans son emploi autorisé par la règle 5 : détacher **un** attribut
secondaire court. Longueur moyenne du bloc de queue : 15 caractères, exactement le gabarit des
deux boutiques de référence (16 et 16,5). Aucun titre ne dépasse deux blocs sauf lorsque le
second est une liste de finitions (`noir, café ou doré`), qui est la façon dont le corpus Shopping
écrit un axe de couleur. Les six exemples cible de la convention elle-même portent tous une
virgule.

**Matière à 83 %, pas 100 %.** Les 20 titres sans matière sont les luminaires LED en métal peint
— anneaux, spirales, sputnik, palets, tiges. Leur matière réelle est l'aluminium laqué, que
personne ne tape et qui ne discrimine rien entre deux lustres à anneaux. L'emplacement est occupé
par la forme et la finition, qui sont les deux critères de choix réels. La cible de la convention
est ≥ 70 % ; 83 % la dépasse.

## Ce que je n'ai pas pu vérifier

**Les volumes SEMrush restent non mesurés.** La convention le signalait déjà
(`MOTS-CLES-TITRES-2026-08-25.md`) : Chrome bloque le pilotage, une autorisation manuelle est
requise. Aucun titre n'est donc classé par volume. Les arbitrages entre deux formulations
plausibles (`cascade` contre `grappe`, `coupole` contre `dôme`, `tambour` contre `ovale`) reposent
sur la photo, sur les listes de la convention et sur les recherches associées, pas sur une mesure.
À revalider quand SEMrush sera accessible.

**Les `seo_description` gardent l'ancien titre en tête de phrase.** La description meta de chaque
fiche commence par l'ancien titre, donc 53 d'entre elles contiennent encore un `Ø` et une plage
(`Suspension nuages en verre soufflé LED, Ø 20 à 40 cm. LED intégrée, …`). Le périmètre demandé
était `title` et `seo_title` : la description a été conservée à l'identique, pas réécrite, ni dans
`pdp-copy.json`, ni en live. Ce n'est pas l'attribut `title` du flux Shopping, donc pas un risque
Merchant Center, mais c'est une incohérence visible en SERP. À traiter dans une passe dédiée —
la régénérer proprement demande de repasser par `humanise_pdp.seo_description_of`, qui compose la
phrase à partir du titre, de la famille et de la source lumineuse.

**Les descriptions produit reprennent aussi les anciennes formulations.** `descriptionHtml` et les
métafields `custom.*` n'ont pas été relus : le corps des fiches peut encore parler de « nuages »
ou de « boule d'épines ». Hors périmètre.

**Les valeurs d'option restent brutes.** La réserve notée dans `HUMANISATION-PDP-2026-08-25.md`
tient toujours : le sélecteur de variante affiche encore `Ø 92 cm`, `3 head Transparent glass`,
`Dimmable by Remote`. Les axes de variante n'ont pas été touchés, conformément à la consigne.

**Les textes alternatifs des médias n'ont pas été mis à jour.** Ils portent encore l'ancien
libellé (`Suspension céramique émaillée, autre vue`), et certains un cadratin.

## Les cinq titres dont je suis le moins sûr

| Handle | Titre | Le doute |
|---|---|---|
| `suspension-deco-253182` | Suspension céramique émaillée rouge, monture laiton | Les cinq visuels montrent tous l'abat-jour rouge, mais l'axe propose trois modèles. Si B et C sont d'une autre couleur, `rouge` ne décrit que A. |
| `suspension-rotin-897170` | Suspension rotin corolle tressée, naturel | L'axe de variante mêle des valeurs `rotin` et des valeurs `plastique`. Le titre retient `rotin`, ce que montre la photo, mais une variante pourrait être en plastique — le seul cas du catalogue où une variante pourrait démentir la matière du titre. |
| `suspension-rotin-607504` | Suspension rotin tressé noir, monture bois | L'image principale et les deux vues secondaires sont noires, mais l'axe `Taille` ne mentionne « Noir » que sur une valeur sur quatre : il existe peut-être une version naturelle. |
| `lustre-salon-233314` | Lustre grappe globes opalins, 7 ou 13 lumières | Les globes ont une texture de lune, plausiblement de la résine et non du verre. J'ai écrit `opalins` comme finition et n'ai revendiqué aucune matière, mais un lecteur peut y lire du verre. |
| `suspension-bois-led-453740` | Suspension bois brun vintage, 6 lanternes verre | La pièce est un corps de guitare en bois patiné. `vintage` est une requête réelle et décrit juste, mais renonce au descripteur distinctif ; `brun` est lu sur la photo seule, aucun axe de finition ne le confirme. |

Un sixième cas mérite d'être noté : `suspension-bambou-dore-60cm-805884`, dont le handle annonce
`dore` alors qu'aucun axe de variante ne propose de doré — les axes sont `Diamètre` et
`Température`. Le titre dit `naturel`, la teinte miel du bambou sur la photo. Le mot `doré` du
handle vient probablement du câble ou d'une ancienne fiche fournisseur.

## Contrôles de non-régression

Relus en live après le push, comparés au jeu de référence :

| Contrôle | Résultat |
|---|---|
| Variantes | 629, identique à `variants-work.json` |
| SKU distincts | 602, identique |
| Prix distincts | 149, 199, 249, 299, 349, 399, 499 € — inchangés |
| Axes et valeurs d'option | non touchés, aucune mutation émise |
| Thème | aucune mutation, `templates/product.json` non réécrit |
| `apply_pdp.py` | jamais exécuté ; `main()` jamais appelé, `build_pdp_copy.py` non relancé |
| `descriptionHtml` et métafields `custom.*` | non envoyés dans la mutation |
| `seo.description` | renvoyée à l'identique, 120 / 120 vérifiées au caractère |

La mutation utilisée est `productUpdate` avec pour seule charge
`{id, title, seo: {title, description}}` — écrite dans `retitle_seo.py`, pas importée de
`apply_pdp.py`, pour qu'aucun autre champ ne puisse partir par inadvertance.

## Le contrôle automatique

`retitle_seo.py` refuse un titre qui ne commence pas par `Suspension`, `Lustre` ou `Plafonnier`,
dépasse 65 caractères, contient `Ø`, `—`, `–`, `|` ou ` : `, contient une plage `\d+ à \d+ cm`,
contient `Lumière Matière`, contient un mot d'ambiance, porte une majuscule interne hors sigle
(`LED`, `RVB`, `XXL`, `E27`, `E14`, `G9`), est vide au sens du § 9 (ni matière, ni couleur, ni
forme), ou double un autre titre du catalogue. Le script sort en erreur avant tout appel réseau
si un seul titre échoue.

```
Table : 120 handles
Contrôle automatique : 120/120 acceptés
  120 titres · 120 uniques · longueur moy 46.2 (min 40, max 55, médiane 46) · hors 40-60 : 0
  matière 100/120 (83 %) · couleur 120/120 (100 %) · un seul bloc 10/120
```

## Fichiers

| Fichier | Nature |
|---|---|
| `retitle_seo.py` | table des 120 titres, contrôle automatique, backup, mise à jour `pdp-copy.json`, push, relecture |
| `dump_media_titles.py` | dump lecture seule des 120 fiches avec `featuredMedia` et `media`, pour l'audit photo |
| `pdp-copy.json` | `title` et `seo_title` mis à jour sur 120 fiches, aucun autre champ modifié |
| `titles-media-dump.json` | état pré-push, titres et médias |
| `RETITRAGE-SEO-2026-08-25.md` | ce rapport |
| `backups/2026-08-25-titres-seo/titles-live.avant.json` | 120 titres et `seo_title` live avant le push |
| `backups/2026-08-25-titres-seo/pdp-copy.avant.json` | `pdp-copy.json` avant le push |

Les deux fichiers de backup ont été recoupés avec `titles-seo-audit.json` : 0 écart sur `title`,
0 écart sur `seo.title`. Le script ne réécrit plus un backup existant, pour qu'une seconde
exécution ne puisse pas y enregistrer l'état déjà retitré.

---

# Les 120 titres, avant et après

### Suspensions bambou — 16 fiches

Longueur moyenne 44.4 c. · matière 16/16 · couleur ou finition 16/16

| Handle | Avant | Après | c. |
|---|---|---|---|
| `suspension-bambou-45cm-962644` | Suspension bambou tissée, Ø 38 à 45 cm | **Suspension bambou dôme tressé, tige bois clair** | 46 |
| `suspension-bambou-067987` | Suspension bambou tissée, Ø 40 à 100 cm | **Suspension bambou ovale tressé, câble noir** | 42 |
| `suspension-bambou-led-136557` | Suspension bambou tissée, LED, Ø 40 à 100 cm | **Suspension bambou vague tressée LED, naturel** | 44 |
| `suspension-bambou-led-80-cm-236157` | Suspension bambou tressé en vague, tige rigide, Ø 40 à 80 cm | **Suspension bambou vague naturelle, tige rigide** | 46 |
| `suspension-bambou-280004` | Suspension bambou tissée, Ø 20 à 60 cm, câble blanc ou noir | **Suspension bambou tressé 3 lampes, câble noir** | 45 |
| `suspension-bambou-led-583180` | Suspension bambou tressé, une vague, Ø 40 à 100 cm | **Suspension bambou vague tressée, câble doré** | 43 |
| `suspension-bambou-942503` | Suspension bambou tissée, Ø 60 à 150 cm | **Suspension bambou XXL tressé, pétales naturels** | 46 |
| `suspension-bambou-led-033589` | Suspension bambou tressé, 3 vagues en cascade, Ø 40 à 100 cm | **Suspension bambou cascade 3 vagues, naturel** | 43 |
| `suspension-bambou-655008` | Suspension dôme en bambou tressé serré, tige de bois | **Suspension bambou dôme tressé serré naturel** | 43 |
| `suspension-bambou-led-80-cm-191307` | Suspension bambou tressé en vague, câble souple, Ø 40 à 80 cm | **Suspension bambou vague naturelle, câble souple** | 47 |
| `suspension-bambou-655463` | Suspension coupole en bambou tressé, câble noir | **Suspension bambou coupole tressée, câble noir** | 45 |
| `suspension-bambou-led-630923` | Suspension bambou tissée, Ø 50 à 60 cm | **Suspension bambou disque plat tressé naturel** | 44 |
| `suspension-bambou-led-50cm-377816` | Suspension bambou tissée, Ø 30 à 50 cm | **Suspension bambou tressé double étage naturel** | 45 |
| `suspension-bambou-104055` | Suspension bambou tissée, Ø 40 à 50 cm | **Suspension bambou tambour tressé, naturel** | 41 |
| `suspension-bambou-317565` | Suspension bambou tissée, Ø 40 à 80 cm | **Suspension bambou soucoupe tressée, tige dorée** | 46 |
| `suspension-bambou-dore-60cm-805884` | Suspension bambou tissée, Ø 40 à 60 cm, doré | **Suspension bambou ovale tressé serré naturel** | 44 |

### Suspensions rotin — 14 fiches

Longueur moyenne 44.9 c. · matière 14/14 · couleur ou finition 14/14

| Handle | Avant | Après | c. |
|---|---|---|---|
| `suspension-rotin-897170` | Suspension rotin tressée, Ø 50 à 60 cm | **Suspension rotin corolle tressée, naturel** | 41 |
| `suspension-rotin-dore-435189` | Suspension rotin tressée, doré | **Suspension rotin cloche haute tressée, naturel** | 46 |
| `suspension-rotin-469688` | Suspension rotin tressé, 3 lanternes sur platine noire | **Suspension rotin tressé 3 lampes, platine noire** | 47 |
| `suspension-rotin-623305` | Suspension rotin tressé, abat-jour tambour, une lumière | **Suspension rotin tressé, abat-jour tambour naturel** | 50 |
| `suspension-rotin-489600` | Suspension paille brute, Ø 40 à 80 cm | **Suspension paille brute tressée, naturel doré** | 45 |
| `suspension-rotin-607504` | Suspension rotin tressée, Ø 19 à 50 cm | **Suspension rotin tressé noir, monture bois** | 42 |
| `suspension-rotin-272937` | Suspension corde de chanvre tressée, 1 ou 3 lumières | **Suspension globes corde tressée, monture noire** | 46 |
| `suspension-rotin-led-535545` | Suspension rotin tressée, LED, Ø 60 à 150 cm | **Suspension rotin XXL tressé, pétales naturels** | 45 |
| `suspension-rotin-477244` | Suspension corolle en corde tressée, Ø 40 à 60 cm | **Suspension corolle corde tressée, beige ou chanvre** | 50 |
| `suspension-rotin-443915` | Suspension corde tressée en cloche, Ø 30 à 60 cm | **Suspension cloche corde tressée, kaki ou noir** | 45 |
| `suspension-rotin-led-420069` | Suspension rotin tressée, LED, Ø 35 à 65 cm | **Suspension rotin cloche large tressée, naturel** | 46 |
| `suspension-rotin-dore-865596` | Suspension bois deux pétales, Ø 39 à 85 cm, monture dorée | **Suspension bois deux pétales, monture dorée** | 43 |
| `suspension-rotin-605780` | Suspension rotin tressée, Ø 35 à 65 cm | **Suspension rotin dôme tressé naturel clair** | 42 |
| `suspension-rotin-led-761433` | Suspension corolle en fibre tressée, Ø 30 à 60 cm | **Suspension corolle fibre tressée, naturel** | 41 |

### Lustres anneau — 12 fiches

Longueur moyenne 47.6 c. · matière 0/12 · couleur ou finition 12/12

| Handle | Avant | Après | c. |
|---|---|---|---|
| `lustre-anneau-led-led-noir-dore-024410` | Lustre anneaux LED en cascade, 1 à 4 anneaux, noir, café ou doré | **Lustre anneaux LED cascade, noir, café ou doré** | 46 |
| `lustre-anneau-led-led-597704` | Lustre anneau LED, Ø 40 à 100 cm | **Lustre anneaux LED superposés, doré, blanc ou noir** | 50 |
| `lustre-anneau-led-led-717226` | Lustre anneaux LED blancs, 4 ou 6 lumières, tige de suspension | **Lustre anneaux LED blancs, tige de suspension** | 45 |
| `lustre-anneau-led-led-625575` | Plafonnier anneaux LED blancs, 4 ou 6 lumières, platine chromée | **Plafonnier anneaux LED blancs, platine chromée** | 46 |
| `lustre-anneau-led-led-dore-418494` | Lustre 6 anneaux LED superposés, noir, café ou doré | **Lustre 6 anneaux LED superposés, noir, café ou doré** | 51 |
| `lustre-anneau-led-led-784897` | Lustre anneau LED, Ø 40 à 100 cm, doré, blanc ou noir | **Lustre anneau LED double, doré, blanc ou noir** | 45 |
| `lustre-anneau-led-007557` | Plafonnier LED connecté, lumière RVB, blanc ou noir | **Plafonnier LED rond connecté RVB, blanc ou noir** | 47 |
| `lustre-anneau-led-led-795468` | Lustre anneau LED, Ø 20 à 30 cm | **Lustre anneau LED simple, finition blanche ou noire** | 51 |
| `lustre-anneau-led-led-dore-641905` | Lustre anneau LED, Ø 40 à 80 cm, noir, doré ou blanc | **Lustre anneaux LED 5 cercles, noir, doré ou blanc** | 49 |
| `lustre-anneau-led-led-892612` | Lustre anneau LED, Ø 20 à 91 cm | **Lustre anneau LED opalin blanc, télécommande** | 44 |
| `lustre-anneau-led-led-799451` | Lustre anneau LED, Ø 40 à 80 cm, blanc, doré ou noir | **Lustre anneaux LED spirale, blanc, doré ou noir** | 47 |
| `lustre-anneau-led-led-134962` | Lustre anneau LED, 5 ou 6 lumières | **Lustre anneaux LED 6 lumières, blanc, doré ou noir** | 50 |

### Lustres salon — 12 fiches

Longueur moyenne 46.7 c. · matière 7/12 · couleur ou finition 12/12

| Handle | Avant | Après | c. |
|---|---|---|---|
| `lustre-salon-led-366435` | Suspension ruban LED double boucle, 70 à 92 cm, doré | **Suspension ruban LED double boucle, doré ou blanc** | 49 |
| `lustre-salon-957153` | Suspension ruban LED en trèfle, Ø 50 cm, doré | **Suspension ruban LED trèfle, doré ou noir** | 41 |
| `lustre-salon-led-147017` | Lustre anneaux LED concentriques, Ø 40 à 80 cm | **Lustre anneaux LED concentriques, doré ou blanc** | 47 |
| `lustre-salon-blanc-246282` | Suspension soucoupe en soie tendue, Ø 30 à 60 cm, blanc | **Suspension soucoupe soie plissée blanche, salon** | 47 |
| `lustre-salon-led-240560` | Lustre anneau LED à couronne effet cristal, noir, blanc ou doré | **Lustre anneau LED effet cristal, blanc, noir ou doré** | 52 |
| `lustre-salon-led-630766` | Suspension anneau LED à verre facetté, doré, blanc ou noir | **Suspension anneau LED verre facetté, doré ou noir** | 49 |
| `lustre-salon-233314` | Lustre grappe de globes effet lune, 7 ou 13 lumières | **Lustre grappe globes opalins, 7 ou 13 lumières** | 46 |
| `lustre-salon-blanc-575463` | Suspension rose en pétales acryliques, Ø 33 à 43 cm | **Suspension corolle acrylique blanche, salon** | 43 |
| `lustre-salon-907106` | Lustre grappe de globes en verre coloré, 1 à 8 lumières | **Lustre grappe globes verre coloré, doré ou noir** | 47 |
| `lustre-salon-led-254609` | Lustre sputnik, 4, 8 ou 12 globes, doré, noir ou bicolore | **Lustre sputnik noir et doré, 12 globes verre** | 44 |
| `lustre-salon-led-784326` | Plafonnier palets LED et bois, 4 à 7 lumières | **Plafonnier LED palets bois, blanc, noir ou doré** | 47 |
| `lustre-salon-led-341706` | Suspension coupole galet LED, Ø 40 à 60 cm, cinq modèles | **Suspension coupole galet LED, finition blanc mat** | 48 |

### Suspensions bois — 12 fiches

Longueur moyenne 47.4 c. · matière 12/12 · couleur ou finition 12/12

| Handle | Avant | Après | c. |
|---|---|---|---|
| `suspension-bois-led-830581` | Suspension bois tourné, ampoule globe apparente | **Suspension bois clair tourné, ampoule apparente** | 47 |
| `suspension-bois-193329` | Suspension travertin à capot noyer, bois clair ou foncé | **Suspension cylindre travertin, bois clair ou noyer** | 50 |
| `suspension-bois-led-453740` | Suspension bois en forme de guitare, 6 lanternes de verre | **Suspension bois brun vintage, 6 lanternes verre** | 47 |
| `suspension-bois-led-245113` | Suspension cylindre travertin et bois foncé, Ø 17 cm | **Suspension cylindre travertin, anneau noyer** | 43 |
| `suspension-bois-led-934110` | Suspension tube vertical effet travertin, rosace bois foncé | **Suspension tube travertin, rosace bois noyer** | 44 |
| `suspension-bois-led-334133` | Suspension perles de pierre et bois, globe opalin | **Suspension perles pierre et bois, globe opalin** | 46 |
| `suspension-bois-059364` | Suspension tonneau en bois, chaîne et rosace métal | **Suspension tonneau bois, chaîne métal noire** | 43 |
| `suspension-bois-led-30cm-886635` | Suspension abat-jour plissé en céramique, Ø 30 cm | **Suspension céramique plissée blanche, tête bois** | 47 |
| `suspension-bois-led-989306` | Suspension double coquille en bois tressé, platine linéaire blanche | **Suspension double coquille bois tressé, platine blanche** | 55 |
| `suspension-bois-led-582321` | Suspension double coquille en bois tressé, rosace ronde dorée | **Suspension double coquille bois tressé, rosace dorée** | 52 |
| `suspension-bois-832012` | Suspension 3 gouttes de verre, tête bois, fumé, ambre ou clair | **Suspension bois 3 gouttes verre, fumé ou ambre** | 46 |
| `suspension-bois-led-121862` | Suspension abat-jour festonné en céramique, tête bois | **Suspension céramique festonnée blanche, tête bois** | 49 |

### Plafonniers — 10 fiches

Longueur moyenne 46.6 c. · matière 7/10 · couleur ou finition 10/10

| Handle | Avant | Après | c. |
|---|---|---|---|
| `plafonnier-led-led-637673` | Plafonnier LED rond, lumière colorée et enceinte intégrée | **Plafonnier LED rond blanc, RVB et enceinte intégrée** | 51 |
| `plafonnier-led-565566` | Plafonnier tiges croisées, 6 globes, cuivre ou chrome | **Plafonnier tiges croisées chrome, 6 globes verre** | 48 |
| `plafonnier-led-led-442025` | Suspension boule d’épines dorées, Ø 65 cm | **Suspension boule sputnik métal doré, 65 cm** | 42 |
| `plafonnier-led-led-183789` | Plafonnier palets LED et bois, 5 ou 6 lumières, gris ou blanc | **Plafonnier LED palets bois, gris ou blanc** | 41 |
| `plafonnier-led-led-698635` | Plafonnier anneaux LED, 1 à 6 anneaux, blanc, noir ou doré | **Plafonnier anneaux LED, blanc, noir ou doré** | 43 |
| `plafonnier-led-led-922186` | Suspension guirlande de globes opalins, 5 à 20 globes | **Suspension guirlande globes opalins, monture laiton** | 51 |
| `plafonnier-led-led-728204` | Réglette LED au plafond, 60 à 200 cm, blanc ou noyer | **Plafonnier LED linéaire cuisine, blanc ou noyer** | 47 |
| `plafonnier-led-led-465027` | Plafonnier boucles LED entrelacées, blanc ou noir | **Plafonnier LED boucles entrelacées, blanc ou noir** | 49 |
| `plafonnier-led-992600` | Plafonnier tiges courbes, 4, 6 ou 8 globes, noir, blanc ou doré | **Plafonnier tiges courbes noires, 8 globes verre** | 47 |
| `plafonnier-led-led-dore-blanc-354637` | Plafonnier coupole plissée en acrylique, Ø 30 à 55 cm | **Plafonnier coupole acrylique plissée, blanc mat** | 47 |

### Suspensions verre — 10 fiches

Longueur moyenne 45.8 c. · matière 10/10 · couleur ou finition 10/10

| Handle | Avant | Après | c. |
|---|---|---|---|
| `suspension-verre-led-489156` | Suspension nuages en verre soufflé LED, Ø 20 à 40 cm | **Suspension cascade verre soufflé LED transparent** | 48 |
| `suspension-verre-led-dore-436718` | Suspension arceau laiton et globes opale, doré ou noir | **Suspension arceau laiton et globes opalins, doré** | 48 |
| `suspension-verre-394147` | Suspension globe en verre double paroi, 1 ou 3 lumières | **Suspension globe verre fumé, 1 ou 3 lumières** | 44 |
| `suspension-verre-091815` | Suspension nuages en verre soufflé, Ø 20 à 40 cm | **Suspension grappe verre soufflé, ambre ou fumé** | 46 |
| `suspension-verre-446435` | Suspension globe en verre fumé sur tige rigide, Ø 20 cm | **Suspension globe verre fumé, tige rigide noire** | 46 |
| `suspension-verre-noir-201424` | Suspension grappe de verres fumés miroir, rosace noire | **Suspension grappe verre fumé miroir, rosace noire** | 49 |
| `suspension-verre-led-blanc-554061` | Suspension globes opale sur câbles laiton, quatre modèles | **Suspension globes opalins, câbles laiton doré** | 45 |
| `suspension-verre-651675` | Suspension boule en verre fumé miroir, Ø 20 à 30 cm | **Suspension boule verre fumé miroir argenté** | 42 |
| `suspension-verre-928640` | Suspension galet en verre fumé à micro-LED, monture laiton | **Suspension galet verre fumé LED, monture laiton** | 47 |
| `suspension-verre-814554` | Suspension disque plat en verre coloré, ampoule apparente | **Suspension disque verre vert, brun ou blanc** | 43 |

### Suspensions pierre — 9 fiches

Longueur moyenne 47.0 c. · matière 9/9 · couleur ou finition 9/9

| Handle | Avant | Après | c. |
|---|---|---|---|
| `suspension-effet-pierre-led-073999` | Suspension effet pierre, galet plat sur tige de bois clair | **Suspension galet effet pierre, tige bois clair** | 46 |
| `suspension-effet-pierre-led-434888` | Suspension effet pierre, LED, Ø 18 à 22 cm | **Suspension effet pierre, galet et tube opalin** | 45 |
| `suspension-effet-pierre-092465` | Suspension pierre translucide, pierre claire ou brun | **Suspension cylindre pierre claire, tête bois brun** | 49 |
| `suspension-effet-pierre-led-dore-960013` | Suspension galet effet pierre, Ø 40 à 70 cm | **Suspension galet effet pierre, blanc cassé ou gris** | 50 |
| `suspension-effet-pierre-led-709819` | Suspension effet pierre, LED, Ø 28 à 40 cm | **Suspension tube travertin beige, LED intégrée** | 45 |
| `suspension-effet-pierre-led-338324` | Suspension effet pierre, large cylindre à capot noyer | **Suspension gros cylindre travertin, tête noyer** | 46 |
| `suspension-effet-pierre-led-445794` | Suspension effet pierre, cylindre étroit, bois clair ou foncé | **Suspension cylindre travertin étroit, bois clair** | 48 |
| `suspension-effet-pierre-led-147607` | Suspension effet pierre, trois formes au choix | **Suspension travertin beige et bois, cône ou galet** | 49 |
| `suspension-effet-pierre-343987` | Suspension effet pierre, tube court ou long | **Suspension tube travertin court ou long beige** | 45 |

### Suspensions déco — 8 fiches

Longueur moyenne 48.0 c. · matière 8/8 · couleur ou finition 8/8

| Handle | Avant | Après | c. |
|---|---|---|---|
| `suspension-deco-led-837156` | Suspension céramique festonnée, vert céladon ou bleu poudré | **Suspension céramique festonnée, vert céladon** | 44 |
| `suspension-deco-led-blanc-805304` | Suspension coupelle en céramique à motifs, cordon laiton | **Suspension coupelle céramique blanche, cordon laiton** | 52 |
| `suspension-deco-348096` | Suspension dôme en céramique blanche ajourée | **Suspension dôme céramique blanche ajourée** | 41 |
| `suspension-deco-led-077631` | Suspension céramique à fleurs bleues, douille laiton | **Suspension céramique à fleurs bleues, douille laiton** | 52 |
| `suspension-deco-led-889929` | Suspension grappe de cônes en céramique, deux modèles | **Suspension grappe cônes céramique blanche, bois** | 47 |
| `suspension-deco-blanc-560098` | Suspension double en céramique à motifs bleus, laiton | **Suspension double céramique à motifs bleus, laiton** | 50 |
| `suspension-deco-253182` | Suspension céramique émaillée, trois modèles, monture laiton | **Suspension céramique émaillée rouge, monture laiton** | 51 |
| `suspension-deco-led-689455` | Suspension 3 lumières, céramique nervurée et laiton | **Suspension céramique nervurée blanche, 3 lampes** | 47 |

### Suspensions métal — 8 fiches

Longueur moyenne 47.1 c. · matière 8/8 · couleur ou finition 8/8

| Handle | Avant | Après | c. |
|---|---|---|---|
| `suspension-metal-dore-502141` | Suspension abat-jour tissu sur armature laiton, Ø 35 à 55 cm | **Suspension abat-jour tissu, armature laiton dorée** | 49 |
| `suspension-metal-led-dore-081498` | Suspension anneau LED et oiseau doré | **Suspension anneau LED métal doré, oiseau posé** | 45 |
| `suspension-metal-led-dore-701414` | Suspension voile LED, Ø 40 à 100 cm, papier ou soie | **Suspension voile LED blanc, papier ou soie** | 42 |
| `suspension-metal-led-dore-952116` | Suspension céramique bleu et blanc, monture laiton | **Suspension céramique bleu et blanc, monture laiton** | 50 |
| `suspension-metal-led-dore-843772` | Plafonnier 3 anneaux LED dorés, Ø 40 à 80 cm | **Plafonnier 3 anneaux LED entrelacés, métal doré** | 47 |
| `suspension-metal-noir-dore-361680` | Lustre laiton à bougies, 4, 6 ou 8 bras | **Lustre laiton à bougies, 6 bras dorés ou noirs** | 46 |
| `suspension-metal-dore-037279` | Suspension dôme en céramique gaufrée, monture laiton | **Suspension dôme céramique gaufrée, monture laiton** | 49 |
| `suspension-metal-led-dore-975417` | Suspension corolle plissée blanche, cordon doré | **Suspension corolle céramique blanche, cordon doré** | 49 |

### Lustres cristal — 7 fiches

Longueur moyenne 44.6 c. · matière 7/7 · couleur ou finition 7/7

| Handle | Avant | Après | c. |
|---|---|---|---|
| `lustre-cristal-led-led-141724` | Lustre effet cristal, LED, Ø 20 cm | **Lustre effet cristal 3 anneaux LED dorés** | 40 |
| `lustre-cristal-led-677865` | Lustre effet cristal, LED, Ø 40 à 100 cm, doré ou chrome | **Lustre effet cristal LED, anneaux doré ou chrome** | 48 |
| `lustre-cristal-led-led-dore-264869` | Lustre effet cristal, LED, 2 lumières | **Lustre effet cristal doré, 1 ou 2 lumières** | 42 |
| `lustre-cristal-led-led-560904` | Lustre effet cristal, LED, 10, 12 ou 14 lumières | **Lustre effet cristal doré, couronne de pampilles** | 48 |
| `lustre-cristal-led-led-dore-841671` | Lustre effet cristal, LED, Ø 45 à 160 cm, argenté ou doré | **Lustre branches dorées, perles effet cristal** | 44 |
| `lustre-cristal-led-dore-202521` | Lustre effet cristal, LED, Ø 46 à 180 cm, doré ou argenté | **Lustre cascade effet cristal, branches dorées** | 45 |
| `lustre-cristal-led-noir-347688` | Lustre effet cristal, LED, 5 lumières | **Lustre tambour effet cristal noir, 5 lumières** | 45 |

### Lustres statement — 1 fiche

Longueur moyenne 45.0 c. · matière 1/1 · couleur ou finition 1/1

| Handle | Avant | Après | c. |
|---|---|---|---|
| `lustre-statement-led-noir-950316` | Lustre sputnik noir et laiton, 4, 6 ou 8 globes | **Lustre sputnik laiton et noir, 6 globes verre** | 45 |

### Suspensions modernes — 1 fiche

Longueur moyenne 46.0 c. · matière 1/1 · couleur ou finition 1/1

| Handle | Avant | Après | c. |
|---|---|---|---|
| `suspension-moderne-led-noir-330664` | Suspension deux barres LED croisées, 100 à 150 cm, noir | **Suspension barres LED croisées, métal noir XXL** | 46 |
