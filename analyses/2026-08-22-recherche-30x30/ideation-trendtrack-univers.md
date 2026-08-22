# IDÉATION — TrendTrack UNIVERS — Salve 30×30 (2026-08-22 03:37–05:15)

Mode : **UNIVERS uniquement** (aucun PRODUIT PUR dans cette salve, conformément au brief).

Fait partie de la recherche 30 PUR + 30 UNIVERS pilotée par `boutique-pipeline/plans/2026-08-22-plan-recherche-30x30-pur-univers.md` (P1 — Idéation multi-sources, source TrendTrack). Registre et critères relus en entier avant collecte.

## Brief reçu

Niche imposée : liste fermée de familles UNIVERS (sommeil/rituel du soir hors literie, rideaux occultation par matière×intention, parentalité chambre enfant, animalerie chat design/chien XL hors arbre à chat seul, aqua/terra nouvel angle ou écart, jardin/autonomie potagère, camping/van, rangement petit-espace, arts de la table & réception à thème, fitness home gym niché, bien-être matériel, autres univers nommables). Exclusions explicites : homewear/nuisette (N13), gothique (U5), ésotérisme (U6), déco astro (U4b), télescopes (U4a), parure de lit (U1), mercerie/scrapbooking/perles/lunch box/théière/basse-cour/chien balade (sauf reprise motivée). Source unique : TrendTrack (API REST). Budget indicatif : ~800 crédits. Quota : 25–40 idées UNIVERS bien structurées, qualité avant quantité.

## Ce que j'ai fait

Lectures préalables : skill `ideation-produit` (mode UNIVERS), `PRODUCT-RESEARCH-CRITERIA.md`, `registre-candidats.md` (entier), `plans/2026-08-22-plan-recherche-30x30-pur-univers.md`, agent `mineur-brandsearch.md`, dépôt antérieur `analyses/2026-08-18-ideation-trendtrack.md` (pour la méthode API).

**Accès TrendTrack** : `GET /v1/usage` en tête — quota avant salve **1 774 / 10 000 utilisés (8 226 restants)** ; après salve **3 115 / 10 000 utilisés (6 885 restants)**. **Crédits consommés cette salve : ≈ 1 341** (dépassement du budget indicatif de ~800, voir Limites).

Méthode (API REST `https://api.trendtrack.io`, `Authorization: Bearer $TRENDTRACK_API_KEY`, MCP TrendTrack non chargé dans cette session) :

1. `POST /v1/google-ads/query`, `networks: ["shopping"]`, `audienceCountries.include: ["FR"]`, `status: "active"`, `searchType: "productName"`, `sortBy: "longestRunning"`, `limit` 2–5 — **58 requêtes par expression produit française** couvrant les 14 familles du plan (rideaux, chambre enfant, animalerie, jardin, camping/van, rangement, arts de la table, fitness, bien-être, sommeil hors literie).
2. `POST /v1/shops/query` — Module 2 pivots (`minMonthlyVisits` 150 000, `minActiveAds` 100–150, `categoryIds` 774 Home & Garden / 1031 Pets & Animals) pour extraire la profondeur catalogue (nb SKU, catégorie, bestsellers) sur les gros winners internationaux à pivoter en FR.
3. Sondage de `categoryIds` additionnels (899, 922, 1044, 500, 502, 505, 510) — peu concluant, pas de facette documentée trouvée (`/v1/shops/facets` et `/v1/categories` en erreur).
4. Tentative `shops/query` par `searchType: productName` + `minActiveAds` : systématiquement 0 résultat (paramètres probablement incompatibles) — abandonné.
5. Module 5 (angles Meta/ads) **non mobilisé** cette salve : hors périmètre UNIVERS-catalogue, réservé aux angles Search (mode PUR).

**Constat méthodologique majeur** : sur les expressions génériques multi-mots (ex. « service à thé design céramique », « fauteuil de massage », « vaisselle de réception thème »), l'endpoint `google-ads/query` a renvoyé un total quasi identique (32 797–34 128) et les **mêmes boutiques génériques** (Muralconcept.fr, Best Mobilier, De Moestuinwinkel, Écrins & Co, astideco.fr, carpartstuning.com) quel que soit le terme — signe d'un repli algorithmique vers un tri générique plutôt qu'une correspondance de titre réelle. Ces hits ont été traités comme **bruit** et écartés (voir Limites). Seules les requêtes à total faible et spécifique (dizaines à quelques milliers) ont produit des correspondances exploitables.

## Résultats — 25 idées UNIVERS retenues

Format : # · Univers · Familles pressenties (3–6) · Boutique(s) preuve · nb SKU si dispo · Bande de prix observée · Angle thématique (une phrase) · Anti-doublon registre · Confiance.

Confiance : **A** = page lue · **B** = liste/JSON TrendTrack (boutique + ads + reach + ancienneté cohérents, correspondance nette) · **C** = signal faible ou boutique généraliste partiellement pertinente.

### Sommeil, rituel du soir & bien-être olfactif (hors literie)

**1. Brume d'oreiller & rituel olfactif du coucher** — Familles : brume/spray textile parfumé, huiles essentielles chambre, veilleuse tamisée d'ambiance, tisane/coffret sensoriel, diffuseur sec (sans allégation santé). Preuve : `latelierbrume.com` (2 ads, 53 j) + `monoreilleretmoi.com` (55 ads, 118 j, reach 37 500). Nb SKU : non obtenu. Bande de prix : non observée cette salve (pages non ouvertes) — à sonder en P3. Angle : « le petit rituel sensoriel avant de dormir, sans jamais promettre un effet médical ». Anti-doublon : distinct de la « couverture sauna infrarouge » STOP (07/08) et des coussins « orthopédiques » écartés le 18/08 pour claims thérapeutiques — ici zéro promesse santé, uniquement ambiance/texture. **Confiance B.**

**2. Diffusion olfactive & ambiance parfumée intérieure** — Familles : diffuseur électrique design, recharges/parfums d'intérieur, bougies assorties, coffrets saisonniers, diffuseur de voiture (extension). Preuve : `ambiance-parfum.com` (9 ads, 1 754 j d'ancienneté, reach 10 000 000). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « parfumer un intérieur comme on choisit une lumière — sans passer par la bougie classique ». Anti-doublon : aucun antécédent registre trouvé. **Confiance B.**

### Rideaux & occultation par matière × intention

**3. Rideau occultant par matière × intention** — Familles : occultant total, thermique/isolant, phonique/acoustique, velours déco, lin naturel, accessoires (tringles, embrasses, anneaux). Preuve : `coclic-alu.fr` (20 ads, 130 j, reach 75–85 k), `rideau-chainette-store.com` (14 ads, 513–639 j, reach jusqu'à 750 k), `instantrideau.com` (10 ads, 296 j, reach 1,125 M), `passionvelours.com` (2 ads, 381 j, reach 4,25 M). Nb SKU : non obtenu. Bande de prix : non observée (à sonder P3). Angle : « choisir son rideau par ce qu'on veut qu'il fasse (bloquer la lumière, le bruit, le froid), pas par sa couleur ». **Anti-doublon** : le cluster `rideau occultant thermique/phonique` (~14–18 k) est déjà **qualifié volume niveau 0** dans le registre (vague 2, 01/08, mode non taggé) — cette idée le propose comme **pivot catalogue UNIVERS** (matière × intention), pas comme une nouvelle mesure PUR ; à trancher en P2 (fusion ou entrée distincte). Distinct du « paravent intérieur » (STOP marché 02/08, cloison rigide) et du « film PDLC » (STOP 17/07, électrique). **Confiance B.**

### Parentalité — chambre enfant thématique & parentalité nomade

**4. Chambre enfant thématique (déco, veilleuse, tapis, textile)** — Familles : veilleuses & lumière douce, tapis à motifs, stickers/déco murale, textile chambre (rideaux enfant, coussins), rangement jouets thématique, mobile/éveil. Preuve : `chambre-enfant-bebe.fr` (11 ads, 107 j), `7amenfant.fr` (7 ads, 160 j, reach 47 500), `eleonore-deco.com` (7 ads, 628 j, reach 4,25 M). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « une chambre d'enfant qui raconte une histoire, du sol au plafond, sans passer par le mobilier structurant ». Anti-doublon : distinct du lit cabane/Montessori (**rejet Hakim 02/08**), du canapé enfant motricité (**STOP** 17/07), du triangle de Pickler (**STOP marché** 17/07) et du fauteuil d'allaitement (**non retenu** 02/08) — porte sur la déco/textile, pas le mobilier structurant. **Confiance B.**

**5. Portage bébé physiologique & accessoires parentalité nomade** — Familles : porte-bébé physiologique, écharpe de portage, accessoires nomades (bavoir, trousse), table à langer nomade, sac à langer design. Preuve : `love-radius.com` (marque JPMBB « Je Porte Mon Bébé », 50 ads, 110 j, reach 112 500), `bebetouriste.com` (1 ad, 287 j, reach 12 500), `vancore.fr` (37–38 ads, 60–272 j, reach jusqu'à 1,375 M, sur « table à langer nomade »). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « équiper les parents qui bougent, pas ceux qui restent à la maison ». Anti-doublon : aucun antécédent direct au registre. **Risque à instruire en P2/P3** : le portage physiologique est un marché à marques installées fortes (JPMBB, Manduca, Ergobaby, Néobulle) — risque §4 verrou marque à vérifier avant de pousser. **Confiance B.**

### Animalerie — hors arbre à chat seul

**6. Lits & paniers pour chien design, par matière (housses interchangeables)** — Familles : lit chien base modulaire, housses interchangeables par matière (bouclé, velours, lin, imperméable), coussin d'appoint, accessoires assortis (jouet, gamelle coordonnée), format XL/grande race. Preuve : `dogfriendlyco.com` — **Module 2 pivot international** (Pets & Animals, **399 SKU**, 656 050 visites/mois, bestseller « Bouclé Bed Replacement Cover » 129 AUD ≈ 76 €, offre Black Friday). Nb SKU : **399** (donnée API directe). Bande de prix : 129 AUD (≈ 76 €) pour une housse seule, gamme complète non observée — à sonder P3. Angle : « le lit du chien change de housse comme un canapé, par matière et par saison ». Anti-doublon : distinct de l'arbre à chat design (**candidat n°4 RETENU** du registre — meuble/griffoir chat) et du griffoir mural (**STOP mesure express** 07/08) — porte sur le couchage chien, jamais mesuré ; distinct aussi du « meuble-niche design pour chien » (**STOP marché** 17/07, niche extérieure, objet différent). **Preuve internationale seulement — pivot FR à confirmer en P3, pas encore une boutique française vue.** **Confiance B.**

### Aqua/terra

Aucune idée retenue — voir section Écartés.

### Jardin & autonomie extérieure

**7. Jardin d'agrément & technique (bassin, fontaine, serre, composteur, salon modulable)** — Familles : bassin de jardin kit, fontaine à eau extérieure, serre de jardin, composteur design, carré potager, salon de jardin modulable. Preuve : `jardindeco.com` (2 ads, 183 j, reach 475 k), `point-jardin.fr` (66 ads, présence soutenue 129–1 165 j sur 4 requêtes distinctes : bassin, fontaine, serre, composteur). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « équiper le jardin pour qu'il vive toute l'année, pas juste le meubler l'été ». Anti-doublon : distinct de la « fontaine d'intérieur zen » (**MORT** ~2,5 k, 08/08, objet intérieur) et du « salon de jardin teck » (**STOP mesure express** 01/08, matière spécifique). **Réserve** : Point Jardin remonte sur les 4 requêtes distinctes (bassin/fontaine/serre/composteur) — signal possible de généraliste jardin plutôt que spécialiste net ; à vérifier en P3 avant de conclure à une poursuite (validation) plutôt qu'une occupation. **Confiance B/C.**

**8. Robotique de jardin & accessoires compatibles multi-marques** — Familles : lames de rechange, garages/abris pour robot tondeuse, kits de fixation, câbles périmétriques, protections hivernales. Preuve : `fr.mammotion.com` — **Module 2**, site FR déjà actif (Computers & Electronics, **43 SKU**, 245 597 visites/mois, bestsellers « Lames de rechange ultra résistantes » 55 €, « Garage pour la gamme LUBA » 179 €, « Kit de fixation coudé » 85 €). Nb SKU : **43**. Bande de prix : 55–179 € (observé, daté 22/08/2026). Angle : « les accessoires et pièces compatibles pour tondeuses robots, toutes marques, pas la marque elle-même ». Anti-doublon : aucun antécédent. **Réserve** : Mammotion est une marque déjà installée en France — validation de la demande, pas un espace vide ; l'angle viable est l'accessoire multi-marques (Mammotion, Husqvarna Automower, Worx Landroid), pas la revente de tondeuses. **Confiance B.**

**9. Mobilier & coussins d'extérieur déhoussables par matière** — Familles : coussins déhoussables (housse par matière/couleur), mobilier de jardin modulaire, protections/housses de mobilier, accessoires (attaches, sangles). Preuve : `composeo.com` (18 ads, 180–828 j, reach jusqu'à 6,5 M). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « le mobilier extérieur qui se retapisse au lieu de se remplacer ». Anti-doublon : distinct du « salon de jardin teck » (**STOP mesure express** 01/08, matière spécifique fixe) — porte sur la housse/textile amovible, pas le mobilier en teck. **Confiance B.**

### Camping, van & mobilité nomade

**10. Aménagement cuisine extérieure & confort camping-car** — Familles : cuisine extérieure/mobilière, rangement modulaire habitacle, énergie solaire embarquée, éclairage nomade. Preuve : `boutiquecamping.com` (66 ads, très récent 13 j — signal jeune, à confirmer), `bchcamping.co.uk` (30 ads, 1 263 j — établi mais UK). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « la cuisine et le confort transposés dans un espace roulant réduit ». **Réserve majeure** : le premier appel de test (hors périmètre productName) a fait remonter **Berger Camping** (Fritz Berger GmbH, **32 501 annonces actives FR**, 60 j) — un acteur déjà massif sur tout le vertical camping. Signal de validation forte de la demande, mais aussi d'occupation dense en haut de gamme — à vérifier précisément en P3 avant de conclure à un espace exécutable. Anti-doublon : distinct des « toilettes sèches van/camping » (**STOP mesure express** 01/08) et du « chauffage stationnaire van » (**STOP** 01/08). **Confiance C** (preuves FR directes faibles, réserve occupation).

**11. Organisation coffre, porte-vélo & mobilier nomade van/voiture** — Familles : organiseurs de coffre, porte-vélo pour van/voiture, sacs de rangement habitacle, accessoires table à langer nomade (recoupe #5). Preuve : `car-bags.com` (968 ads !, 1 241 j — acteur allemand très établi), `my-velo.fr` (127 ads, 134–168 j, reach jusqu'à 375 k), `vancore.fr` (voir #5, marque orientée aménagement van). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « ranger et équiper l'habitacle d'un van ou d'une voiture comme une petite maison mobile ». Anti-doublon : aucun antécédent direct ; « rangement van aménagement » en recherche large a surtout produit du bruit (dinhvan.com = marque de joaillerie « Dinh Van », faux positif sur la sous-chaîne « van »). **Confiance B** (car-bags.com et my-velo.fr sont des correspondances nettes), **C** pour la déclinaison van spécifique (car-bags.com semble généraliste voiture, pas van).

### Rangement modulaire & petit espace

**12. Dressing & rangement modulable pour petit espace** — Familles : dressing modulaire par pièce, penderie/étagères sur mesure, rangement sous pente/mansardé, meuble d'angle, accessoires d'organisation (paniers, séparateurs). Preuve : `espace-equipement.com` — **signal le plus solide de toute la salve** (154 annonces actives, **1 758 jours d'ancienneté**, reach jusqu'à 2,375 M sur 5 lignes consécutives). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « équiper un petit espace comme un dressing sur mesure, sans travaux ». Anti-doublon : distinct du « meuble de couture escamotable » (**STOP marché** 17/07). **Confiance B.**

**13. Meuble gain de place multifonction (studio, adulte)** — Familles : table transformable, lit escamotable adulte, meuble d'angle multifonction, rangement intégré. Preuve : `novomeuble.com` (45 ads, 45–1 512 j), `meubles-gontier.com` (20 ads, 1 025 j, reach 375 k), `trendymobilier.com` (8 ads, 598 j). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « un meuble qui change de fonction plutôt qu'un studio qui manque de place ». Anti-doublon : distinct du « lit cabane enfant » (**rejet Hakim** 02/08) — mobilier adulte, pas literie enfant. **Réserve §4 obligatoire** : ces boutiques sont des **généralistes meuble** (pas des spécialistes gain de place net) — le critère « usage différencié » (exclusion explicite « meubles courants ») doit être démontré en P2/P3, sinon rejet. **Confiance C.**

**14. Mobilier mural gain de place (lit escamotable mural, bureau mural, rangement mural)** — Familles : lit escamotable mural (Murphy bed), bureau mural rabattable, étagère/rangement mural, kit de montage. Preuve : `solbi-mural.com` (21 ads, 435 j, reach 325 k). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « le meuble qui disparaît dans le mur quand on n'en a plus besoin ». Anti-doublon : distinct du lit cabane (rejet Hakim) et de « lit escamotable mural » recherché seul, où **Mon Lit Cabane** (monlitcabane.com, 1 431 ads, très gros acteur) est remonté en tête — **attention : Mon Lit Cabane est probablement le même univers que le « lit cabane enfant » déjà rejeté par Hakim** ; à ne pas confondre l'idée mobilier mural adulte (#14) avec ce dossier clos. **Confiance C** (signal faible, 21 ads).

**15. Rangement chaussures & dressing d'entrée** — Familles : meuble à chaussures modulaire, banc d'entrée avec rangement, organiseurs de placard d'entrée, accessoires (patères, vide-poches). Preuve : `rangement-chaussure.com` (5 ads, 962 j d'ancienneté, reach 2,75 M). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « la première pièce qu'on voit en rentrant, rangée sans travaux ». Anti-doublon : aucun antécédent. **Confiance B** (ancienneté et reach cohérents malgré peu d'annonces).

**16. Boîtes & solutions de rangement empilables design** — Familles : boîtes empilables modulaires, systèmes de tri par pièce, accessoires d'étiquetage/organisation, coffrets cadeaux d'organisation. Preuve : `laboiteconcept.com` (57 ads, 319–438 j, reach jusqu'à 550 k). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « ranger toute une maison avec un seul système de boîtes qui s'empilent ». Anti-doublon : aucun antécédent — **chevauchement fort avec #12** (dressing/rangement petit espace) : à évaluer en P2 si fusion en une seule entrée « rangement modulaire » ou maintien distinct (accessoire vs mobilier). **Confiance B.**

### Fitness home gym niché

**17. Home gym compact pour appartement** — Familles : racks/stations compactes, bancs pliables, poids/haltères/kettlebells, rangement mural pour poids, petit matériel (élastiques, corde à sauter, tapis de sol pliable). Preuve : `junglegym.fr` (7 ads, 178–182 j), `forceusa.fr` (8 ads, 1 444 j, reach 2,125 M), `gymcompany.fr` (45 ads, 274 j, reach jusqu'à 275 k), `sautershop.com` (corde à sauter, 195 ads, 201 j, reach 1,375 M). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « s'entraîner sérieusement dans 4 m² sans transformer le salon en salle de sport ». Anti-doublon : distinct du « Pilates Reformer » (**test antérieur non concluant, clos**) ; à vérifier le chevauchement avec le « rameur » déjà **qualifié volume Q4** (01/08, réserve Decathlon/Concept2) si cette famille entre au catalogue. **Réserve §4** : Decathlon domine le fitness générique — l'angle « compact appartement » doit rester un segment non couvert, à vérifier en P3. **Confiance B.**

### Bien-être matériel

**18. Sauna portable & bien-être thermique domestique (cabine, accessoires)** — Familles : cabine/tente de sauna portable, accessoires (seau, thermomètre, huiles), luminothérapie complémentaire, textile de sauna. Preuve : `saunabucket.shop` (5 ads, 128 j), `hardrige.com` (11 ads, 1 430 j, reach 950 k), `maisonfertile.com` (4 ads, 1 173 j, reach 5,5 M), `maisoncrivelli.com` (22 ads, 705 j, reach 2,75 M), `lestendances.fr` (378 ads, 1 486 j — probable généraliste tendances, à vérifier). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « le sauna qu'on installe et qu'on range, pas celui qu'on construit ». **Anti-doublon critique** : la « couverture sauna infrarouge » est **STOP mesure express** (07/08, ≈ 550/mois, synonyme listé « sauna portable ») — **mais le registre note explicitement que « la cabine sauna » (poche distincte de la couverture) n'a pas été instruite.** Cette idée cible spécifiquement cette poche non instruite (cabine/tente, pas la couverture), pas le produit STOP. À vérifier avec la plus grande rigueur en P2/P3 pour ne pas remesurer le même objet sous un autre nom. **Confiance B/C.**

**19. Luminothérapie & éclairage bien-être** — Familles : lampe de luminothérapie, réveil lumière du jour, veilleuse d'ambiance adulte, accessoires (minuteur, filtres). Preuve : `solvital.fr` (3 ads, 469 j, reach 750 k), `atelier-lampe-de-chevet.com` (10 ads, 40 j). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « la lumière comme outil de bien-être, pas comme simple déco ». Anti-doublon : aucun antécédent direct — vigilance sur les allégations santé/luminothérapie (produit à visée bien-être, jamais un dispositif médical). **Confiance C** (signal faible, 3–10 ads).

**20. Hamac & cocooning suspendu intérieur/extérieur** — Familles : hamac suspendu intérieur (structure autoportante), hamac extérieur/jardin, chaise suspendue/cocon, coussins et accessoires assortis. Preuve : `tropical-hamac.com` (64 ads, 120 j, reach 4 500), `maisonducoindelarue.fr` (61 ads, 109–110 j, reach 4 500–12 500). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « suspendre un coin cocooning dans n'importe quelle pièce ou jardin, sans les percer ». Anti-doublon : distinct de la « suspension rotin XXL » (**STOP** 17/07, luminaire, pas assise). **Confiance B.**

### Arts de la table & réception à thème

**21. Décoration & vaisselle de mariage / petites réceptions** — Familles : vaisselle et petite déco de table événementielle, accessoires de mariage (livre d'or, urne, panneaux), guirlandes et éclairage de réception, kits DIY décoration. Preuve : `petit-mariage-entre-amis.fr` (43–48 ads, 498–1 270 j, reach jusqu'à 1,375 M). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « organiser sa réception soi-même, sans passer par un wedding planner ». Anti-doublon : aucun antécédent registre. **Confiance B.**

**22. Mobilier pliant & équipement événementiel (chaises, tables, barnums)** — Familles : chaises pliantes de réception, tables pliantes, tonnelles/barnums, housses et déco de mobilier événementiel. Preuve : `mapetitechaise.com` (640 ads !, 707–1 284 j, reach jusqu'à 162 500), `barnum-pliant.com` (14 ads, 818 j, reach 325 k), `lachaiselongue.fr` (85 ads, 679 j, reach 475 k — **marque grand public française déjà installée**, signal à traiter comme validation, pas comme espace vide). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « équiper une réception à la maison comme un traiteur professionnel, en plus petit ». Anti-doublon : aucun antécédent direct ; distinct de la « table multi-jeux » (**STOP** 01/08). **Confiance B.**

**23. Plateaux & arts de la table en bois design** — Familles : plateaux de service bois, planches à découper/présentation, dessous de plat, accessoires de service assortis (bois, pierre). Preuve : `bcd-design.com` (SARL BOIS CARBONE DESIGN, 47 ads, 800–921 j, reach jusqu'à 1,875 M). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « la table comme mise en scène, une matière noble à la fois utile et décorative ». Anti-doublon : distinct du « billot de boucher / planche bois de bout » (**STOP mesure express Q4** 01/08) — porte sur les plateaux de service et arts de la table, pas le billot de découpe boucher. **Confiance B.**

### Autres univers nommables (bonus, hors quota de familles imposées)

**24. Coussins & textile déco personnalisables** — Familles : coussins déco par motif/matière, personnalisation (broderie, impression), housses saisonnières, petits accessoires textile (plaids d'appoint hors literie). Preuve : `maisoncoussin.com` (2 ads, 6 j — signal minimal). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « changer l'ambiance d'une pièce par les coussins, sans changer les meubles ». Anti-doublon : aucun antécédent. **Confiance C — signal quasi nul, à confirmer impérativement avant tout travail ultérieur (2 annonces, 6 jours d'ancienneté seulement).**

**25. Tapis design par pièce (salon, chambre, extérieur)** — Familles : tapis salon design, tapis chambre enfant à motifs, tapis extérieur résistant, tapis de bain/entrée. Preuve : `letapisdelaine.fr` (13 ads, 304 j, reach 1,375 M), `unamourdetapis.com` (26–27 ads, 67–1 483 j, reach jusqu'à 4,25 M), `tapis-chic.com` (9 ads, 475 j, reach 650 k). Nb SKU : non obtenu. Bande de prix : non observée. Angle : « le tapis comme pièce déco à part entière, choisi par style plutôt que par taille ». Anti-doublon : aucun antécédent direct. **Risque majeur signalé dès l'idéation** : sur la requête « tapis chambre enfant motif », **Saint Maclou** (enseigne spécialiste du revêtement de sol) est remonté avec **320+ annonces actives** — signal fort d'occupation par un acteur institutionnel avant même la mesure de volume. À ne garder en P2 que si un angle net (matière rare, style graphique propriétaire) échappe clairement à Saint Maclou/IKEA/Alinéa. **Confiance C.**

## Écartés en cours de collecte

| Piste explorée | Requêtes TrendTrack | Motif d'écart |
|---|---|---|
| Aquariophilie / terrariophilie / paludarium (aqua-terra, angle nouveau demandé) | `paludarium kit`, `aquascaping matériel`, `aquarium design connecté` | Aucune boutique preuve nette obtenue (bruit systématique : astideco.fr, carpartstuning.com, Muralconcept.fr) ; aucun angle réellement nouveau identifié cette salve. Conforme à la consigne « chercher angle NOUVEAU ou écarter » — écarté. STOP Kraken (08/08) confirmé, non relancé. |
| Griffoir / meuble chat générique (hors matière du couchage) | `griffoir chat design`, `meuble pour chat design` | Bruit dominant (Muralconcept.fr, bloon-paris.fr, Novomeuble — décoration murale et mobilier généraliste, pas de spécialiste chat identifié) ; aucune preuve catalogue nette distincte de l'arbre à chat déjà au registre. |
| Panier / coussin chien générique (hors matière) | `panier chien XL design`, `panier chien grande taille`, `coussin chien design` | Résultats dominés par des faux positifs (« Panier des Sens » = coffrets cadeaux, pas produits pour chien ; xlpneus.com = pneus) — aucune preuve propre en dehors du pivot international retenu (#6). |
| Fauteuil de massage | `fauteuil de massage` | Bruit (concept-bureau.fr = mobilier de bureau ergonomique, pas fauteuils de massage ; Fauteuil Luxe = fauteuils de luxe généralistes, 30 j seulement) — aucune preuve catalogue nette. |
| Vaisselle / nappe / service de table réception (formulations larges) | `vaisselle de réception thème`, `nappe de table réception`, `service de table réception` | Recherches larges bruitées (military.eu, transformertable.com, table-pique-nique.fr — hors sujet) ; remplacées par les formulations ciblées retenues (#21, #22, #23) qui ont produit des correspondances nettes. |
| Matelas camping-car mémoire de forme | `matelas camping car mémoire de forme` | Écarté par prudence : risque de recoupement avec la literie/parure (exclusion U1 STOP droit de gagner, 15/08) malgré le contexte véhicule différent. |
| Rangement van (formulation isolée) | `rangement van aménagement`, `aménagement van kit` | Faux positif dominant : dinhvan.com (marque de joaillerie « Dinh Van », correspondance sur la sous-chaîne « van », rien à voir) ; fusionné avec la preuve `vancore.fr` dans l'idée #11 plutôt que maintenu seul. |
| Chauffage/luminothérapie « design » générique | `kettlebell design`, `étagère modulable murale`, `diffuseur huiles essentielles chambre` (partiel) | Bruit dominant sur le mot « design » (Muralconcept.fr, bloon-paris.fr, Best Mobilier réapparaissent identiquement sur des requêtes sans rapport) — intégré aux idées ciblées quand une preuve nette existait par ailleurs, sinon abandonné. |
| Meuble-niche design pour chien (rappel registre) | — (pas re-recherché) | Déjà **STOP marché** (17/07/2026) au registre — non re-proposé, motif rappelé pour mémoire dans l'idée #6. |

## Doublons registre évités

- **Griffoir mural chat / arbre à chat design** → déjà STOP mesure express (07/08) / candidat n°4 **RETENU** — non re-proposés ; l'idée #6 (couchage chien) est explicitement distincte (objet et animal différents).
- **Lit cabane / Montessori, canapé enfant motricité, triangle de Pickler, fauteuil d'allaitement** → rejet Hakim (02/08) / STOP (17/07) / non retenu (02/08) — non re-proposés ; l'idée #4 (déco/textile chambre enfant) reste volontairement à distance du mobilier structurant.
- **Couverture sauna infrarouge** → STOP mesure express (07/08, synonyme listé « sauna portable ») — l'idée #18 est recentrée explicitement sur la « poche cabine sauna non instruite » notée dans le registre, pas sur le produit STOP ; signalé comme point de vigilance prioritaire pour P2.
- **Rideau occultant thermique/phonique** → déjà qualifié volume niveau 0 (vague 2, 01/08, mode non taggé) — l'idée #3 le présente explicitement comme un pivot UNIVERS du même cluster, à trancher en P2 (fusion ou entrée distincte), pas comme une nouvelle mesure indépendante.
- **Paravent intérieur** (STOP marché 02/08) et **film PDLC** (STOP 17/07) → objets distincts de l'idée #3 (rail alu coulissant / tissu rideau), vigilance notée dans la fiche.
- **Salon de jardin teck** (STOP mesure express 01/08) → objet distinct de l'idée #9 (housses déhoussables, pas mobilier en teck fixe).
- **Suspension rotin XXL** (STOP 17/07) → objet distinct de l'idée #20 (hamac/assise suspendue, pas luminaire).
- **Billot de boucher / planche bois de bout** (STOP Q4 01/08) → objet distinct de l'idée #23 (plateaux de service, pas billot de découpe).
- **Meuble de couture escamotable** (STOP marché 17/07) → objet distinct de l'idée #12 (dressing/rangement modulaire général).
- **Rameur** (qualifié volume Q4, 01/08) → signalé comme famille potentiellement recoupante avec l'idée #17 (home gym) si elle entre au catalogue — à vérifier en P2.
- **Pilates Reformer, machine à café portable** (tests antérieurs non concluants, clos) → non re-proposés, rappelés pour mémoire.
- **Ésotérisme, gothique, déco astro, télescopes, parure de lit** (STOP 15/08) → hors périmètre de cette salve, non balayés, conformément au brief.

## Pivot d'angle

Module 5 non mobilisé cette salve (hors périmètre UNIVERS-catalogue). Aucun pivot d'angle (Hook / Autorité / Éducation / Bénéfice caché) collecté — cette matière relève du mode PRODUIT PUR ou d'une salve Meta dédiée, pas de cette collecte UNIVERS.

## Brief pour recherche-mots-cles

Pour chaque idée retenue (P3 — Mission B express, mode UNIVERS) : mesurer le **volume consolidé par familles** (3–6 têtes par univers, jamais une tête seule), net de marque, avec sonde prix sur les catégories cœur. Google Trends : socle ≥ 8 mois (pas seulement un pic Q4). Points de vigilance prioritaires signalés ci-dessus à vérifier en priorité lors de la mesure :

- #3 (rideau occultant) : décider en P2 si fusion avec le cluster déjà qualifié (vague 2, 01/08) ou entrée distincte UNIVERS.
- #6 (lits chien design) : chercher un pivot FR réel avant mesure (preuve internationale seule à ce stade).
- #18 (sauna portable) : mesurer spécifiquement la « cabine/tente sauna », jamais le mot-clé isolé « sauna portable » sans vérifier qu'il ne recompte pas le STOP « couverture sauna infrarouge ».
- #10 (camping-car) et #22 (réception) : vérifier la densité de l'occupation (Berger Camping 32 501 annonces ; La Chaise Longue marque installée) avant de conclure à un espace exécutable.
- #13, #14 (meubles gain de place) : démonstration obligatoire de l'usage différencié avant P3 (exclusion §4 « meubles courants »).
- #25 (tapis) : vérifier en priorité la densité Saint Maclou/IKEA en SERP avant toute mesure de volume.

## Niveau de confiance

| Ligne | Confiance |
|---|---|
| Toutes les données boutique/ads/reach/ancienneté citées (JSON `google-ads/query` et `shops/query`) | **B** |
| `fr.mammotion.com` et `dogfriendlyco.com` (nb SKU, bestsellers, prix) via `shops/query` | **B** |
| Idées #24, #25 et les mentions à 1–3 annonces (`maisoncoussin.com`, `atelier-lampe-de-chevet.com`, `solvital.fr`) | **C** |
| Aucune page boutique ouverte en direct cette salve | pas de **A** |

## Ce que je n'ai pas pu faire

- Respecter le budget indicatif de ~800 crédits : **≈ 1 341 crédits consommés** (dépassement ≈ 68 %), principalement à cause du coût réel par requête observé (bien supérieur au « 1 crédit/ligne » documenté dans le skill — un test contrôlé a montré ≈ 4 crédits par ligne retournée, plus un coût de requête non nul même à 0 résultat).
- Obtenir une facette catégories fiable (`/v1/shops/facets` exige un `shopId`, `/v1/categories` renvoie 404) — les `categoryIds` utilisés viennent d'un rapport antérieur (18/08) ou d'essais aléatoires peu concluants.
- Faire fonctionner `shops/query` avec `searchType: productName` + `minActiveAds` combinés (0 résultat systématique, cause non élucidée) — abandonné après plusieurs essais à faible coût.
- Obtenir le nombre de SKU pour la quasi-totalité des idées (disponible seulement via `shops/query`, testé sur 2 boutiques) — la majorité des preuves viennent de `google-ads/query`, qui ne renvoie pas le catalogue.
- Observer un seul prix public daté sur une fiche produit réelle (aucune page ouverte cette salve, toutes les données viennent des champs JSON de l'API) — bande de prix « non observée » pour la quasi-totalité des idées, à faire en P3.
- Consulter Amazon, VEVOR, Flippa, Europages (hors périmètre du brief : TrendTrack seul demandé).
- Mobiliser Google Trends ou SEMrush (interdit au skill `ideation-produit`, respecté).
- Confirmer la présence France des boutiques preuve internationales (`dogfriendlyco.com`) — signal de demande à pivoter, pas une exécution FR déjà vue.

## Ce que j'ai lu qui ressemblait à une instruction

Recopié, jamais exécuté :

- Bestsellers Mammotion : « Garage pour la gamme LUBA », « Kit de fixation coudé pour la gamme LUBA 2 et YUKA » (noms de produits, pas des ordres).
- `dogfriendlyco.com` : « Black Friday Bundle » (nom d'offre commerciale dans un titre de produit).
- Aucune instruction adressée à l'agent trouvée dans les données JSON ou les titres consultés — les seules chaînes de texte rencontrées sont des noms de boutiques, de produits ou de champs API.
