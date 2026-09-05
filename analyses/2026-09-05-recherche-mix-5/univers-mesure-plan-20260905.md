# Plan de mesure — fléchettes et aquarelle — 2026-09-05

Périmètre préparatoire pour le mode **UNIVERS / Shopping France**. Ce fichier ne prononce aucun `PASS_PREQUALIFICATION`, aucun `TECHNICAL_*` et aucun sourcing. Il fournit des familles normalisées, des requêtes candidates et les exclusions à appliquer avant toute consolidation DataForSEO.

> Arbitrage Astra après collecte : D2 et D4 sont exclus du premier batch et du consolidé actif. Leur présence dans l’inventaire ci-dessous documente les contaminants et ne constitue pas une autorisation de reprise. Voir `mesure-preparee.json`.

## Contrôle anti-doublon

Recherche ciblée dans `registre-candidats.md` et dans les analyses datées du 01 au 05/09/2026 :

| Univers | Résultat anti-doublon | Proximités à ne pas réactiver |
|---|---|---|
| Fléchettes | Aucun univers `fléchettes` / `darts` trouvé. | Le registre contient un rejet de **cible de fléchettes électronique connectée** : cela ne doit pas être renommé en nouvel univers ; si la mesure continue, cette cible est seulement une famille isolée du catalogue complet. Exclure aussi poker, tir sportif et archery. |
| Aquarelle | Aucun univers `aquarelle` trouvé. Les analyses récentes ne contiennent que des graines génériques `coffret aquarelle` / `chevalet de peinture`. | Exclure `peinture au numéro` (déjà présente dans l’analyse Q4), gouache/acrylique/huile, beaux-arts génériques, papeterie générique, calligraphie et fournitures de tatouage. |

Les occurrences trouvées dans `analyses/2026-09-03-qualification-9-produits-pur/` (ex. `surround` audio, `pigment` de tatouage, `peinture` de lambris) sont des homonymes ou produits d’autres dossiers ; elles ne constituent pas une preuve de ces deux univers.

## Inventaire de requêtes — fléchettes

Les familles sont des ensembles de demande à dédupliquer par intention. Une formulation ne doit appartenir qu’à une famille. Les marques, joueurs et modèles servent éventuellement au nettoyage SERP, jamais au volume net de l’univers.

| ID / famille | Requêtes françaises candidates à mesurer | Inclus | À exclure / règle de déduplication |
|---|---|---|---|
| D1 — fléchettes de jeu acier | `fléchettes acier`; `fléchettes pointe acier`; `fléchettes tungstène`; `fléchettes 23g`; `jeu de fléchettes acier` | Jeu complet de fléchettes steel-tip pour particulier. | Une seule tête par série proche : `fléchettes acier` / `fléchettes pointe acier` à regrouper selon les résultats. Exclure `fléchettes chasse`, `fléchettes jouet`, `fléchettes nerf`, noms de joueurs et marques. |
| D2 — fléchettes soft-tip | `fléchettes plastique`; `fléchettes soft tip`; `fléchettes pointe plastique`; `fléchettes électroniques` | Accessoires de jeu soft-tip et consommables compatibles. | `cible électronique` ne doit pas être absorbée automatiquement dans D2. Exclure jouets enfants, pistolets à fléchettes, tir à l’arc et tir sportif. |
| D3 — cibles traditionnelles | `cible fléchettes`; `cible sisal`; `cible anglaise`; `cible steel tip` | Cibles de fléchettes en sisal/liège destinées au jeu domestique. | Exclure `cible tir`, `cible tir à l’arc`, `cible carabine`, `cible mousse` et les prestations de salle. `jeu de fléchettes` peut recouper D1/D3 : ne pas additionner sans adjudication SERP. |
| D4 — cibles électroniques et scoring | `cible fléchettes électronique`; `cible fléchettes connectée`; `jeu fléchettes électronique`; `compteur score fléchettes`; `scoreur fléchettes` | Cibles soft/electronic, tableaux de score et scoring destinés au domicile. | Famille conservée séparément à cause du rejet déjà inscrit sur la cible connectée. Exclure billard électronique, jeux d’arcade et applications seules. Aucun terme D4 ne doit porter seul le verdict univers. |
| D5 — installation / protection / setup | `éclairage cible fléchettes`; `lampe cible fléchettes`; `surround cible fléchettes`; `protection mur cible fléchettes`; `tapis fléchettes`; `oche fléchettes`; `armoire cible fléchettes`; `cabinet fléchettes` | Installation et environnement de jeu : lumière, tapis/oche, entourage, cabinet. | Exclure éclairage de tableau, tapis de tir/archery et mobilier de bar générique. `cible fléchettes` reste D3/D4 selon SERP et ne doit pas être comptée aussi en D5. |
| D6 — pièces et personnalisation | `ailettes fléchettes`; `plumes fléchettes`; `tiges fléchettes`; `shafts fléchettes`; `pointes fléchettes`; `étui fléchettes`; `accessoires fléchettes` | Pièces remplaçables, réglage et rangement. | Exclure accessoires de pêche, fléchettes de sarbacane et articles de joueur/licence. `accessoires fléchettes` est une requête de contrôle de couverture, pas une ligne additionnelle si ses sous-termes sont déjà mesurés. |

**Périmètre conseillé pour la première consolidation :** D1 à D5 ; D6 en contrôle de scalabilité et de panier. Garder D2 et D4 séparées, puis lire la SERP pour ne pas confondre soft-tip, cible électronique et jouet.

**Exclusions lexicales communes fléchettes :** `tir à l'arc`, `archerie`, `carabine`, `tir sportif`, `sarbacane`, `pistolet`, `nerf`, `jouet`, `casino`, `poker`, `billard`, `fléchettes apéro` si la page est un jeu de bar sans matériel comparable, `joueur`, `champion`, marques et modèles.

## Inventaire de requêtes — aquarelle

Le périmètre doit rester **matériel pour pratiquer l’aquarelle**. Le mot générique `aquarelle` peut désigner une œuvre, un cours, une technique ou une fourniture et ne doit pas être utilisé comme mesure isolée.

| ID / famille | Requêtes françaises candidates à mesurer | Inclus | À exclure / règle de déduplication |
|---|---|---|---|
| A1 — couleurs et pigments | `peinture aquarelle`; `aquarelle extra fine`; `aquarelle fine`; `godets aquarelle`; `tube aquarelle`; `pigment aquarelle`; `palette de couleurs aquarelle` | Couleurs prêtes à l’emploi et pigments pour artiste particulier. | `peinture` seul, `pigment` seul et `encre pigmentée` sont trop larges. Exclure gouache, acrylique, huile, peinture bâtiment, pigment tatouage/maquillage et aquarelle liquide scolaire si la SERP est non comparable. `palette de couleurs` est A1 ; `palette voyage` est A4. |
| A2 — papier et supports | `papier aquarelle`; `bloc aquarelle`; `papier coton aquarelle`; `papier 300g aquarelle`; `papier aquarelle grain fin`; `papier aquarelle grain torchon`; `carnet aquarelle` | Papier spécialisé, blocs et carnets pour aquarelle. | Exclure papier dessin générique, papier peint, papier photo, papier calligraphie et support d’œuvre fini. Regrouper `papier aquarelle` et `papier coton aquarelle` seulement après lecture des séries et de la SERP ; ne pas additionner des synonymes proches par défaut. |
| A3 — pinceaux et outils de geste | `pinceau aquarelle`; `pinceaux aquarelle`; `pinceau réservoir eau`; `pinceau lavis aquarelle`; `pinceau petit gris aquarelle`; `pinceau voyage aquarelle` | Pinceaux spécifiques, pinceaux à eau et outils directement associés au geste aquarelle. | Exclure pinceaux maquillage, pinceaux bâtiment, pinceau calligraphie sans intention aquarelle et `pinceau peinture` générique. Les coffrets de pinceaux restent A3 sauf s’ils sont explicitement un kit complet A4. |
| A4 — coffrets / palettes nomades | `coffret aquarelle`; `kit aquarelle`; `palette aquarelle voyage`; `aquarelle nomade`; `set aquarelle débutant`; `boîte aquarelle avec pinceau` | Kits prêts à démarrer, palettes portables et coffrets cohérents. | `coffret aquarelle` et `kit aquarelle` sont des variantes à grouper par série, pas deux familles. Exclure `peinture au numéro`, Aquarellum enfant si la mesure vise l’artiste adulte, kits loisirs créatifs non spécifiques et coffrets de peinture multi-techniques. |
| A5 — accessoires de pratique | `palette mélange aquarelle`; `godets vides aquarelle`; `masking fluid aquarelle`; `ruban papier aquarelle`; `pinceau réservoir` si non déjà attribué à A3; `trousse aquarelle`; `mallette aquarelle` | Accessoires et rangement utiles à la pratique, uniquement si la page est explicitement aquarelle. | Exclure chevalet/table de peinture générique, `mallette peinture` non spécialisée, matériel d’atelier pro, gravure, reliure et calligraphie. Les produits A5 ne doivent pas gonfler le volume cœur si leur prix et leur demande sont accessoires. |

**Périmètre conseillé pour la première consolidation :** A1 à A4 ; A5 comme test de profondeur. Le terme `chevalet de peinture` apparaît dans les fichiers locaux, mais il doit rester hors cœur tant que la SERP ne prouve pas une intention aquarelle particulière.

**Exclusions lexicales communes aquarelle :** `cours`, `tutoriel`, `apprendre`, `livre`, `peinture au numéro`, `tableau`, `œuvre`, `artiste`, `dessin aquarelle` lorsqu’il s’agit d’une image ou d’un résultat, `gouache`, `acrylique`, `huile`, `encre tatouage`, `maquillage`, `bâtiment`, `papier peint`, `calligraphie`, `professionnel` si la page bascule vers l’atelier pro, marques (Sennelier, Winsor & Newton, Schmincke, Arches, Raphaël, etc.) pour la mesure nette.

## Données locales déjà attestées — provenance

Les fichiers présents dans `/private/tmp` ont été lus sans nouvel appel DataForSEO. Ils contiennent des **listes de mots-clés envoyées ou préparées**, pas de lignes de résultats avec volumes exploitables dans cette passe.

| Fichier | Paramètres attestés | Termes pertinents présents | Ce que cela prouve / ne prouve pas |
|---|---|---|---|
| `/private/tmp/dfs5-loisirs-textile.json:1` | Endpoint `keywords_data/google_ads/search_volume/live`; `location_code: 2250`; `language_code: fr`; `search_partners` absent dans ce fichier. | `coffret aquarelle`, `chevalet de peinture`, `mallette peinture`. | Présence de ces graines dans un lot Q4 loisirs/textile ; aucun volume ni validation d’univers. `mallette peinture` reste ambiguë et n’est pas une requête cœur Aquarelle. |
| `/private/tmp/dfs-discovery1.json:1` | Endpoint `keywords_data/google_ads/search_volume/live`; `location_name: France`; `language_code: fr`; `search_partners: false`. | `chevalet peinture atelier`, `table dessin inclinable`, `projecteur dessin`, `presse gravure`, `presse fleurs professionnelle`. | Lot de découverte France ; seules les graines liées au chevalet sont potentiellement réutilisables après nettoyage. Aucun terme fléchette/darts/aquarelle spécifique. |
| `/private/tmp/dfs5-jobs.json:1` | Endpoint `keywords_data/google_ads/search_volume/live`; `location_name: France`; `language_code: fr`; `search_partners: false`. | `chevalet de peinture`, `chevalet atelier`, `table lumineuse dessin`, `mallette peinture` indirectement absente. | Graines multi-thèmes d’un lot jobs ; ne prouve ni demande adressable ni cohérence de catalogue. |
| `/private/tmp/dfs5-jobs2.json:1` | Endpoint `keywords_data/google_ads/search_volume/live`; `location_name: France`; `language_code: fr`; `search_partners: false`. | `chevalet peinture`, `chevalet peinture bois`, `chevalet atelier`, `table à dessin inclinable`. | Graines spécifiques d’équipement de peinture, mais trop génériques pour l’univers Aquarelle ; à nettoyer ou exclure. |

**Constat fléchettes dans les fichiers locaux :** aucune occurrence de `fléchette`, `flechette`, `darts`, `steel tip`, `soft tip`, `cible fléchettes`, `surround`, `oche`, `granboard` ou équivalent n’a été trouvée dans les `/private/tmp/dfs*.json` inspectés. Il n’existe donc pas de donnée locale attestée à reprendre pour cette famille.

**Constat aquarelle dans les fichiers locaux :** seule la graine exacte `coffret aquarelle` est présente dans `dfs5-loisirs-textile.json`; les autres lignes sont des graines de chevalets ou de peinture générique. Aucun chiffre de volume ne doit être associé à ces mots avant un appel DataForSEO documenté par Root.

## Séquence proposée à Root

1. Mesurer D1–D5 puis A1–A4 avec France/français et conserver les séries/cibles par requête.
2. Lire les SERP et Shopping pour attribuer les termes ambigus (`jeu de fléchettes`, `cible`, `aquarelle`, `chevalet`, `kit aquarelle`).
3. Regrouper par MAX les variantes proches ; ne pas additionner marques, joueurs, prestations, produits enfants ou accessoires d’un autre univers.
4. Seulement si un consolidé reste au-dessus du seuil UNIVERS, relever l’économie de panier et les prix 30–50 lignes pour Aquarelle et les familles low-ticket de fléchettes.

Limites : les données locales sont des payloads de mots-clés, pas des résultats de mesure ; le web public utilisé dans le scout précédent prouve l’existence de catalogues spécialisés mais ne remplace ni DataForSEO, ni le nettoyage SERP, ni la preuve fournisseur.
