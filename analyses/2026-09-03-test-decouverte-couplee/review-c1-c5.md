# Contrelecture indépendante — périmètres et consolidation C1–C5

**3 septembre 2026.** Lecture de `selection.json`, du protocole, des réponses DataForSEO archivées, des cinq SERP et des sondes concurrentes. Aucun nouvel appel API ni recherche externe effectué pendant cette contrelecture. Les propositions ci-dessous restent techniques ; aucun GO humain ni sourcing autorisé.

## Conclusion pour la décision de cette passe

| Candidat figé | Proposition de préqualification | Ce que cette décision signifie |
|---|---|---|
| C1 — Sèche-chaussures soufflant domestique | `STOP_PREQUALIFICATION` **sur le périmètre de demande mesuré** | Union des deux seeds produit et du seed problème, variantes singulier/pluriel et bottes contrôlées : 10 720 avant exclusions, puis **8 460 après seules marques/enseignes**, sous la bande de clarification 10–15k ; 7 530 après retrait des méthodes DIY explicites. Ce n'est pas une absence de marché ni un rejet du signal concurrent. |
| C2 — Kit casque TV sans fil | `REVIEW_PREQUALIFICATION` | Les requêtes sont nombreuses mais fortement redondantes. L'offre commerciale existe ; le cluster net suffisant n'est pas démontré. Le complément « casque télévision » a été relu : voir l'estimation prudente et les scénarios en fin de document. |
| C3 — Rallonge déportée de cliquet | `STOP_PREQUALIFICATION` **sur l'offre et le vocabulaire sondés** | La demande observée de rallonges reste insuffisante, même avec de nombreux termes plus larges. Ne pas créditer le marché des clés complètes à cet accessoire. Les valeurs nulles du qualificatif ne valent pas zéro marché. |
| C4 — Coussin gel amovible de selle moto | `STOP_PREQUALIFICATION` **sur le périmètre mesuré** | Volume faible malgré plusieurs formulations et des contrôles plus larges. Ne pas élargir silencieusement à la selle complète, au garnissage ou à tout équipement moto. |
| C5 — Bracelet réveil vibrant personnel | `STOP_PREQUALIFICATION` **sur le périmètre mesuré** | La demande sondée reste faible ; le duo commercial existe, donc ne pas ajouter un kill économique fondé sur « aucun bundle ». Le chiffre du shop et une croissance récente éventuelle ne remplacent pas la demande Search française actuelle. |

Ces libellés doivent être publiés avec la portée de l'étude. `STOP_PREQUALIFICATION` arrête le budget de cette passe ; il ne prétend pas que toutes les formulations possibles ont été recensées. Ne pas créer un nouveau statut technique pour exprimer cette réserve : utiliser un champ/motif de périmètre. Le témoin final et le bilan d'accès ont été contrôlés par l'orchestrateur ; voir [manifest.json](manifest.json) et [obstacles.md](obstacles.md).

## Vérifications chiffrées et limites des quatre STOP de périmètre

Les montants ci-dessous sont des **sommes de volumes mensuels**, pas des dépenses. Les additions généreuses servent uniquement à tester si des corrections favorables pourraient raisonnablement renverser le gate. Elles ne sont pas des clusters nets publiables.

| Piste | Réponse Labs inspectée | Addition de sensibilité sur les données observées | Interprétation |
|---|---|---|---|
| C1 | Union `05-demand-product.json.gz` : 79/79 lignes, brut **8 870** ; `27-c1-spelling.json.gz` : 118/118, brut **8 360** ; `03-demand-seed.json.gz` : 42/42, brut **520** | `MAX` par `core_keyword` normalisé sur 05+27 = **8 920** ; union du corpus problème 03 = **9 230** ; contrôles live22 : seuls chauffe-chaussures 480, sèche-bottes 1 000 et sèche-bottes électrique 10 ajoutent du volume connu, soit **10 720**. Retirer marques/enseignes 2 260 donne **8 460** ; retirer méthodes DIY explicites 930 donne **7 530**, encore avec formats non servis et doublons résiduels. | Les exclusions de marques/enseignes seules ramènent le périmètre sous 10 000 ; le STOP ne repose donc pas sur un résultat net dans la bande REVIEW 10–15k. **L'ancien calcul 9 120 est remplacé**, car il omettait les nouvelles formulations du complément 27. Ce n'est pas une borne exhaustive du marché ni une demande nette adressable. |
| C3 | `15-c3-labs.json.gz` : 92/92 lignes, brut **7 100** | Ajouter tous les contrôles C3 sauf `clé à cliquet` 6 600 ajoute **1 500** : total excessif **8 600**, avec doublons, marques et rallonges non déportées. | Le parent clé complète n'est pas la même offre. Le vocabulaire exact déporté est pauvre/non renseigné ; le STOP n'est pas fondé sur l'interprétation de `null` comme zéro. |
| C4 | `16-c4-labs.json.gz` : 115/115 lignes, brut **4 660** | Ajouter **tous** les contrôles C4, y compris doublons et `selle confort moto` 1 000, ajoute 2 570 : **7 230**. | Même en créditant provisoirement trop de demande, le périmètre observé reste très inférieur au seuil. Cette somme ne doit pas être présentée comme adressable. |
| C5 | `20-c5-labs.json.gz` : 44/44 lignes, brut **3 560** | Ajouter **tous** les contrôles C5, y compris doublons, bracelet générique et réveils silencieux ambigus, ajoute 2 540 : **6 100**. | L'offre peut être intéressante commercialement, mais cette passe ne démontre pas la taille Search attendue. |

**Reproductibilité C1, corrigée après lecture du complément 27.** Unir les trois réponses 05, 27 et 03. Pour chaque item Labs, prendre `keyword_properties.core_keyword`, ou à défaut `keyword`, puis retirer les accents, remplacer la ponctuation par des espaces et normaliser les espaces. Garder le maximum connu du groupe, en intégrant les onze premiers contrôles C1 de live22 au groupe du mot normalisé ou de son core observé. Les valeurs `null` restent inconnues et ne contribuent pas à cette somme de volumes connus ; elles ne sont pas interprétées comme absence de demande. La tête `seche chaussure` 2 900 est déjà présente dans 27, et `appareil pour sécher les chaussures` 70 aussi : aucun deuxième crédit. Les deux groupes ski à 1 000 chacun restent distincts à ce stade, ainsi que les marques/enseignes (Action 1 000 notamment), l'aide sèche-linge et plusieurs formats non servis. **10 720 représente 96 groupes au volume connu après MAX**, avant nettoyage sémantique final ; l'algorithme de core n'est pas supposé prouver à lui seul une indépendance ou une compatibilité produit. Une simple union des mots normalisés sans cores donnerait 13 050 avant contrôles, illustrant le risque de franchir artificiellement le seuil avec les synonymes. Le résultat ne change pas le STOP limité au périmètre, mais la correction relève l'estimation de sensibilité de 1 600 par rapport au calcul initial incomplet.

**Exclusions minimales C1, contrôlables.** Les **2 260** de marques/enseignes sont : Action 1 000 + avis 40 ; Decathlon 320 + 110 + ski 70 ; Lidl 210 + électrique 10 ; Amazon 90 + ski 10 ; puis Sidas, Therm-ic, Silvercrest, Intersport, Quadralp, Koralp et autres marques/enseignes explicites pour 400. Les groupes Decathlon sont laissés séparés avant exclusion : cela ne gonfle pas le volume restant puisqu'ils sont entièrement retirés. Les **930** de méthodes explicites regroupent sèche-linge 840, sèche-cheveux 60, soleil 20 et four 10. Ce deuxième retrait classe l'intention observée ; aucune impossibilité de convertir un tel lecteur n'est affirmée. Il n'est pas nécessaire au STOP, déjà obtenu après les seules marques/enseignes. Même les **7 530** restants conservent deux groupes ski à 1 000, chauffe-chaussures, mural, occasion, ozone et des formats non prouvés compatibles : c'est une enveloppe de sensibilité, pas un cluster admissible définitif.

**Artefact reproductible :** `c1-consolidation-review.json` contient les 151 groupes, chaque mot/core/volume, les `null`, les exclusions, les index JSON exacts des quatre sources brutes et leurs empreintes SHA-256. Aucun appel supplémentaire n'a été réalisé.

**Portée de “79/79”, “92/92”, etc.** Cela veut dire totalité des lignes retournables par ce seed dans cette réponse Labs, pas totalité de la demande française de la catégorie. Les autres racines non testées restent hors périmètre. Pour rouvrir un STOP, documenter un nouveau vocabulaire attesté, une offre réellement différente ou une nouvelle preuve ; ne pas prolonger indéfiniment les requêtes pour obtenir un PASS.

## C2 — ce que le corpus permet réellement de dire

`raw/10-c2-labs.json.gz` contient **500 lignes sur 2 405**, triées par volume décroissant, pour le seed `casque tv`. La somme brute est **97 220**. Une première réduction mécanique par `core_keyword` normalisé et `MAX` produit **254 groupes / 33 280** avant nettoyage sémantique. Ces deux nombres incluent marques, enseignes, branchement, aide, filaire, duo et variantes de format. **Ni l'un ni l'autre ne mesure la demande nette de notre kit.**

Le fichier `c2-keyword-review.json` aide à la lecture, mais le contrôle des séries et cores se fait dans les réponses brutes. La première passe live est `raw/22-first-controls.json.gz`.

### Groupes de consolidation proposés

| Groupe | Preuve relevée | Traitement conservateur proposé |
|---|---|---|
| Produit sans fil TV/télévision | `casque tv sans fil`, `casque télévision sans fil`, `casque television sans fil` : **5 400 chacun, séries mensuelles exactement identiques**. `casque sans fil tv` : 1 600 mais core Labs `casque tv sans fil`. | **MAX 5 400**, jamais 17 800. Les autres inversions et fautes de pluriel rejoignent le groupe. |
| Variante “audio sans fil” | `casque audio tv sans fil` et variantes : 1 300, même offre générique décrite avec “audio”. | Rattacher provisoirement au groupe produit, sans +1 300 automatique. Une série différente ne suffit pas à prouver des recherches indépendantes. |
| Parents TV/audio/écouter | `casque tv` 2 900 ; `casque audio tv` 1 300 ; `casque pour écouter la tv` 480. | Garder séparés de la contrainte sans fil. `MAX` provisoire **2 900** au sein de ce parent sémantique ; ne pas l'ajouter automatiquement à 5 400. Contrôler si le parent révèle un besoin supplémentaire accessible ou surtout les mêmes kits. |
| Bluetooth TV | `casque bluetooth tv` 880 ; core séparé pour `casque sans fil tv bluetooth` 480 et variante audio 210 ; d'autres lignes ressemblantes. | `MAX` provisoire **880**, distinct pour l'analyse. Une partie cherche à connecter un casque existant directement à la TV ; pas de transfert intégral à un kit émetteur. Ne pas cumuler ces sous-formulations ni tout le groupe avec le produit sans fil sans arbitrage. |
| Comparaison commerciale | `meilleur casque tv sans fil` 1 300 ; `meilleur casque tv` 140 ; comparatif 90 ; variantes audio/test/avis. | Groupe commercial distinct, `MAX` de départ **1 300** ; pas une addition de toutes les années/pluriels. Potentiel Search pédagogique, mais clic comparatif ≠ achat assuré. |
| Contraintes de kit | Émetteur Bluetooth 170 ; recharge sur socle 70 ; prise optique 50 ; sans Bluetooth 20 ; autres petites formulations. | Préciser la connectique de l'offre, contrôler les séries et l'objet recherché. Ne pas transformer chacune en ajout indépendant sur le volume parent. |
| Duo | Pour 2 personnes 320 ; double 260 ; duo 170 et autres variantes. | Un seul groupe `MAX` de départ **320**. Hors offre unitaire figée tant que le kit double et son économie ne sont pas documentés ; un second casque possible n'est pas un panier déjà validé. |
| Aide et problème | Brancher/connecter, prise manquante, pas de son, son TV et casque simultanés. | Annexe de pédagogie et de besoins. Exclure du gate de base ; une réintégration demanderait une preuve de recherche de solution à acheter, pas simplement de dépannage d'un appareil possédé. |

**Test de sensibilité utile :** additionner les six têtes live distinctes 5 400 + 2 900 + 1 300 + 880 + 1 300 + 480 donne **12 260**, avant recouvrement et avant allocation aux bons formats. Ce n'est pas un cluster admissible ; c'est précisément pourquoi le candidat voisin du seuil mérite une clarification. Une somme qui franchirait 12 500 seulement en ajoutant l'inversion à 1 600 ou “audio sans fil” à 1 300 serait artificielle.

### Marques et exclusions

- Marques explicites de casque : Sennheiser, Sony, Philips, Bose, JBL, Thomson, CGV, Meliconi, Avantree, Linkster, Simolio, Muse et références RS/WH/Prelude, selon la ligne. Les requêtes navigationnelles de ces offres ne sont pas la demande générique.
- Enseignes : Darty, Boulanger, Fnac, Amazon, Leclerc, Carrefour, Electro Dépôt, Action, Lidl, etc. À conserver pour la lecture de concurrence, hors gate générique prudent.
- **Samsung/LG/TCL/Hisense ne sont pas automatiquement des marques du casque recherché.** Elles peuvent désigner le téléviseur à équiper. Classer ces lignes comme compatibilité à arbitrer, pas comme preuve mécanique de dépendance à une marque de casque. Un dépannage d'une TV existante peut néanmoins rester hors gate.
- Exclure de l'offre unitaire : filaire, stéthoscopique/intra-auriculaire si notre format ne les sert pas, réalité virtuelle, conduction osseuse, consommables, adaptateurs ou émetteur seuls. Les requêtes explicitement liées à une déficience auditive restent hors thèse B2C non médicale figée.
- Un ratio générique/marque calculé sur ces 500 lignes triées et déjà sélectionnées ne serait pas un ratio exhaustif de catégorie. Ne pas produire de pourcentage de dépendance précis sur cette base.

### Un raffinement borné qui peut changer la décision

Avant une nouvelle collecte, écrire la question : **une offre de kit TV non médical peut-elle franchir le seuil après déduplication, sans créditer du dépannage, des marques ou un autre format ?**

1. Contrôler les variantes commerciales encore non contrôlées : `casque audio tv sans fil`, `casque sans fil pour télévision`, `casque télé sans fil`, `casque audio télévision`, `casque sans fil pour téléviseur`. Ces requêtes vérifient des alias et une racine alternative ; elles ne sont pas des volumes à ajouter d'avance.
2. Contrôler les contraintes du kit : `casque tv sans fil avec émetteur`, `casque tv sans fil rechargeable sur socle`, `casque tv sans fil prise optique`, `casque tv sans fil avec base`, `casque tv sans fil qui ne coupe pas le son`. Déjà présentes ou voisines dans le corpus, elles vérifient l'adéquation offre/demande plutôt qu'une expansion opportuniste.
3. Si un second seed Labs est retenu, utiliser une racine attestée telle que `casque télévision`, puis fusionner avec le corpus existant par cores/séries. `écouteur tv` peut servir de contrôle de couverture, mais son volume reste hors offre si la SERP appelle un autre format. Ne pas paginer mécaniquement 1 905 lignes de plus pour atteindre le seuil.
4. Lire les SERP des parents décisifs `casque tv`, `casque bluetooth tv` et de la meilleure contrainte réellement servie. La SERP actuelle sur `casque tv sans fil` ne tranche pas seule l'attribution de ces parents.
5. Après cette unique clarification : maintenir REVIEW si la somme dépend de recouvrements incertains ou si le prix/connectique de notre offre reste indéfini. Aucun PASS parce que le temps ou le budget est épuisé ; aucun STOP global parce que le corpus est incomplet.

## Lecture concurrentielle à préserver dans les conclusions

- **C1 :** la SERP contient G-Heat, Action, Amazon, Silvergear, Ducatillon, spécialistes ski et Therm-ic. L'offre à 79,95–129 € sur nos PDP existe, mais les petits formats à faible prix aussi. Conserver les distinctions soufflerie/radiateur/gabarit et les risques de comparabilité ; la présence d'Action seule ne prouve pas un verrou global.
- **C2 :** CGV est premier résultat organique, puis Darty et La Boutique d'Éric ; EasyLounge est également visible. Les guides Que Choisir, actu.fr et Soundcore sont présents. C'est une SERP commerciale avec spécialistes et enseignes, pas une démonstration de gagnabilité ni un désert concurrentiel. Les promesses et l'assistance déjà relevées dans `competitors-c1-c2.md` évitent de déclarer la pédagogie vierge.
- **C3 :** même la requête déportée mélange extensions droites, outillage de marque et véritables accessoires déportés. Ne pas prendre la plage de catégorie Leroy Merlin 0,44–924 € comme prix du produit. Les prix des cartes ne remplacent pas une PDP comparable.
- **C4 :** coussin amovible et plaque de gel à intégrer dans la selle coexistent. **9,99 € chez Motea est explicitement un prix de livraison dans le snippet**, pas le prix du coussin. Ne pas l'utiliser pour un kill prix.
- **C5 :** le cœur B2C “sans déranger” est déjà servi par plusieurs petites boutiques ; la SERP mêle aussi des produits d'assistance auditive. Le duo observé sur PulseOn empêche de conclure “panier impossible” sans instruction, mais ne résout pas le gate de volume.

Les blocs `popular_products` des réponses SERP ne sont pas automatiquement des annonces payantes. Aucun item `paid` n'a été utilisé pour déduire une absence de budget ou une densité publicitaire nulle. Les observations de traction TrendTrack doivent rester datées et attribuées au bon niveau, shop ou produit.

## Complément C2 — estimation après le raffinement « casque télévision »

Réponse relue : `raw/29-c2-refinement.json.gz`, collectée le **03/09/2026 à 13:51:04 UTC**. Seed `casque télévision`, France/français, **73/73 items**, somme brute **24 470**. Ce complément ne s'ajoute pas au premier corpus : il retrouve principalement les mêmes formulations avec « télévision » à la place de « TV ».

### Équivalences vérifiées, et erreur du regroupement automatique

Les paires suivantes ont **exactement la même série de 12 mois**, en plus du même volume moyen, entre les deux réponses Labs :

| Première formulation | Alias du complément | Volume commun, compté une seule fois |
|---|---|---:|
| casque tv sans fil | casque télévision sans fil | 5 400 |
| casque audio tv sans fil | casque audio télévision sans fil | 1 300 |
| meilleur casque tv sans fil | meilleur casque télévision sans fil | 1 300 |
| casque tv | casque télévision | 2 900 |
| casque bluetooth tv | casque bluetooth télévision | 880 |

**Anomalie observée :** le core de `casque pour télévision avec fil` (140) est `casque télévision sans fil`. Le core de `casque d'écoute avec fil pour télévision` (10) comporte lui aussi « sans fil ». Ces deux lignes restent **exclues** de notre offre sans fil, quelle que soit l'association automatique. Le nettoyage sémantique doit précéder le regroupement des cores ; le code fournisseur n'est pas une preuve absolue de compatibilité produit.

### Estimation opérationnelle à retenir

**Estimation prudente de travail : 6 700 recherches/mois sur la portion contrôlée**, composée du groupe produit sans fil 5 400 et du groupe comparatif commercial 1 300. Elle conserve les formulations audio/inversées dans le groupe produit et les variantes meilleur/comparatif dans un seul groupe commercial. Ce regroupement sémantique prudent ne prétend pas que Google fusionne tous ces mots dans un bucket unique. C'est un choix de consolidation explicite en l'absence de preuve de demande incrémentale.

Cette estimation n'est ni un comptage d'acheteurs uniques, ni une borne basse statistique, ni un recensement exhaustif du marché. Elle est utilisable pour la décision du test parce qu'elle évite de valider avec des extensions encore incertaines.

| Groupe exact de travail | Base prudente | Crédit supplémentaire maximal dans un scénario permissif | Pourquoi le supplément est conditionnel |
|---|---:|---:|---|
| Produit sans fil : TV/télévision, inversions `sans fil TV`, formulations écoute/audio sans fil non différenciées | 5 400 | 1 300 pour la sous-tête `casque audio tv sans fil` | Série différente de la tête, mais même intention/produit ; différence de série ≠ indépendance démontrée. |
| Comparaison commerciale : meilleur/comparatif/test/avis, variantes TV/télévision | 1 300 | 0 | MAX du groupe ; pas d'addition des années, pluriels et alias. |
| Parent `casque tv` / `casque télévision` | 0 | 2 900 | Inclut potentiellement filaire et utilisateurs n'ayant pas besoin d'un kit ; recouvrement avec sans fil non arbitré. |
| Parent audio `casque audio tv` / `casque audio télévision` | 0 | 1 300 | À absorber dans le parent à 2 900 dans le scénario groupé ; crédit distinct non démontré. |
| Parent usage `casque pour écouter la tv/télévision` et formulations proches | 0 | 480 | Même problème d'alias et de format ; pas une nouvelle demande prouvée. |
| Bluetooth : `casque bluetooth tv/télévision`, variantes sans fil Bluetooth | 0 | 880 | Le kit peut être pertinent, mais un casque seul directement connecté peut suffire ; doublonnage avec sans fil possible. |
| Émetteur : `casque tv sans fil avec émetteur bluetooth` | 0 | 170 | Kit exact pertinent ; incrément par rapport à la tête non établi. |
| Recharge : `casque tv sans fil rechargeable sur socle`, station/base de recharge | 0 | 70 | MAX du groupe ; la base de charge seule n'est pas un kit. |
| Optique : `casque tv sans fil prise optique`, `casque tv optique`, variantes | 0 | 50 | Crédit seulement à un kit ayant cette entrée, pas au RS 120-W analogique seul. |
| Sans Bluetooth : `casque tv sans fil sans bluetooth` | 0 | 20 | Entrée sans fil à préciser : technologie radio alternative ou TV dépourvue de Bluetooth ; pas de crédit automatique au même SKU. |
| Son simultané : `casque tv sans fil qui ne coupe pas le son` et variantes produit | 0 | 40 | Fonction à prouver pour le modèle TV/kit ; les requêtes de dépannage générales restent exclues. |
| **Total** | **6 700** | **7 210** | **13 910** seulement si tous ces crédits sont indépendants et entièrement accessibles, hypothèse non démontrée. |

Trois lectures, avec des hypothèses visibles :

- **Prudente : 6 700** — les deux groupes cœur retenus ci-dessus.
- **Parents groupés : 10 830** — ajouter un seul MAX parent de 2 900, Bluetooth 880 et les cinq contraintes totalisant 350. Ce scénario accorde encore 100 % de ces volumes au kit ; leur incrément n'est pas validé.
- **Très permissive : 13 910** — ajouter en plus audio sans fil 1 300, audio parent 1 300 et écouter TV 480 comme trois groupes indépendants. **Seule cette hypothèse très permissive dépasse 12 500. Elle ne justifie pas un PASS.**

Cette plage de scénarios **6 700–13 910** n'est pas un intervalle statistique et son extrémité haute n'est pas un plafond exhaustif de marché : des lignes non retenues et les 1 905 lignes non ramenées du premier seed restent hors périmètre. Son utilité est de montrer que le passage du seuil repose actuellement sur le traitement de quelques têtes, pas sur une nouvelle poche de demande découverte par le raffinement.

### Exclusions conservées et portée du résultat

Sont exclus de ces totaux : requêtes de marques de casque et enseignes ; aides/dépannages ; filaire ; casque/émetteur/accessoire seul lorsque le kit n'est pas l'objet ; duo ; formats alternatifs non servis ; demandes médicales explicites ; Wi-Fi ou USB ambigus sans preuve de compatibilité ; recherche avec plafond de prix incompatible avec l'offre de référence. **“Senior” seul n'est pas synonyme de médical** : les formulations non médicales restent dans leur groupe produit/comparatif, sans ajout séparé. Les marques du téléviseur restent un sujet de compatibilité, pas une dépendance de marque automatiquement attribuée au casque.

Le CPC du cœur produit est **0,25 USD**, celui du groupe comparatif **0,34 USD**, selon les données archivées. Ne pas appliquer le plus bas à une extension complète du cluster. Le Q4 2025 des deux groupes réunis montre octobre 7 000, novembre 12 300, décembre 12 300 : une hausse saisonnière observée, **pas une modification du gate moyen annuel** ni une prévision de Q4 2026.

**Recommandation maintenue après cette passe : `REVIEW_PREQUALIFICATION`, dépriorisé tant que l'incrément de demande et une offre précise restent non établis.** Le raffinement n'a pas créé une raison d'engager automatiquement d'autres appels ou le sourcing. Les contrôles/lectures de parents décrits dans le plan précédent n'ont pas été exécutés par cette contrelecture ; ils restent des conditions explicites d'une éventuelle poursuite, pas des preuves acquises.
