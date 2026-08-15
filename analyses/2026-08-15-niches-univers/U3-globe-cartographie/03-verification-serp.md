# U3 — Globe terrestre et cartographie déco — vérification SERP (étape 5)

- **Date : 15/08/2026**, session ouverte à 22h40.
- **Outil unique : Google France en lecture texte**, `https://www.google.fr/search?q=…&hl=fr&gl=fr&num=20&pws=0`, onglet Chrome dédié `885844845`. Aucune capture, aucun clic, aucune saisie.
- Objet : exécuter l'**étape 5 de `METHODE-ANALYSE-MARCHE.md`** sur le consolidé de `02-volume-consolide.md` (80 960 nets), qui n'avait subi aucun filtre SERP.
- **Aucun verdict marché ici. C'est une vérification d'intention adossée à des pages 1 réelles.**

---

## État d'avancement

**TERMINÉ — 14 requêtes sur 14 lues, 15/08/2026 23h40.** Aucun CAPTCHA, aucun blocage. Onglet fermé en fin de tâche.

| # | Requête | Statut |
|---|---|---|
| 1 | `globe terrestre` | ✅ 22h42 — **retenu intégralement** |
| 2 | `mappemonde` | ✅ 22h47 — **retrait massif sur la tête** |
| 3 | `carte du monde à gratter` | ✅ 22h51 — **retenu, page 100 % marchande** |
| 4 | `carte du monde en bois` | ✅ 22h57 — **retenu intégralement** |
| 5 | `carte mappemonde` (tête mappemonde-mur) | ✅ 23h01 — **retrait sur les têtes nues** |
| 6 | `carte du monde liège` | ✅ 23h05 — **retenu, léger retrait enseigne** |
| 7 | `globe interactif` | ✅ 23h10 — **RETOURNEMENT : marché de jouet de marque** |
| 8 | `carte du monde murale` | ✅ 23h15 — **retenu intégralement** |
| 9 | `poster carte du monde` | ✅ 23h19 — **retenu, mais page 1 verrouillée par des marques** |
| 10 | `globe bar` | ✅ 23h24 — **retenu partiellement : pack local + marché de l'occasion** |
| 11 | `planisphère` (réserve) | ✅ 23h29 — **sort : page de dictionnaire, zéro annonce produit** |
| 12 | `planisphère du monde` (réserve) | ✅ 23h33 — **sort en majorité** |
| 13 | `planisphere` sans accent (réserve) | ✅ 23h37 — **même page 1 que n° 11** |
| 14 | `planisphère monde` (réserve) | ✅ 23h40 — **la moins scolaire des quatre** |

---

## 1. Méthode

- URL type : `https://www.google.fr/search?q=<requête>&hl=fr&gl=fr&num=20&pws=0`. Localisation détectée par Google : **France, 95390 Saint-Prix (d'après l'IP)**, mention « Les résultats ne sont pas personnalisés » confirmée en pied de page.
- Lecture par extraction JavaScript du DOM uniquement. Les positions organiques sont comptées sur les `h3` de résultats web (`#search a[href^=http] h3`), le comptage recoupé avec le compteur d'extension présent sur l'onglet (« Résultats organiques : N », « Annonces pour une offre de produit : N »).
- **Précaution de méthode n° 1 : je ne confonds jamais « carrousel Shopping / blocs produits visibles » et « annonces Search texte confirmées ».** Le compteur lit des *annonces pour offre de produit* (PLA / Shopping). **Je n'ai à aucun moment pu isoler des annonces Search texte** — je ne prétends donc rien à leur sujet.
- **Précaution n° 2 : page 1 seulement.** Cela interdit de juger la profondeur de la concurrence.
- **Précaution n° 3 : tous les pourcentages de retrait ci-dessous sont des estimations faites à la composition de la page 1, pas de nouvelles mesures.** Ils s'appliquent au volume consolidé de `02-volume-consolide.md` ; ils ne le remplacent pas.
- ≥ 4 s entre deux requêtes. Aucun CAPTCHA rencontré à ce stade.

### Journal des lectures

| # | Requête | Heure | Positions organiques | Annonces produit (PLA) | Ligne « Résultats, y compris pour… » |
|---|---|---|---:|---:|---|
| 1 | `globe terrestre` | 15/08 22h42 | 8 | **32** | **absente** |
| 2 | `mappemonde` | 15/08 22h47 | 9 | **0** | **absente** |
| 3 | `carte du monde à gratter` | 15/08 22h51 | 9 | **32** | **absente** |
| 4 | `carte du monde en bois` | 15/08 22h57 | 9 | **32** | **absente** |
| 5 | `carte mappemonde` | 15/08 23h01 | 10 | **16** | **absente** |
| 6 | `carte du monde liège` | 15/08 23h05 | 9 | **32** | **absente** |
| 7 | `globe interactif` | 15/08 23h10 | 8 | **24** | **absente** |
| 8 | `carte du monde murale` | 15/08 23h15 | 9 | **32** | **absente** |
| 9 | `poster carte du monde` | 15/08 23h19 | 9 | **32** | **absente** |
| 10 | `globe bar` | 15/08 23h24 | 8 | **24** | **absente** |
| 11 | `planisphère` | 15/08 23h29 | 8 | **0** | **absente** |
| 12 | `planisphère du monde` | 15/08 23h33 | 9 | **0** | **absente** |
| 13 | `planisphere` (sans accent) | 15/08 23h37 | 9 | **8** | **absente** |
| 14 | `planisphère monde` | 15/08 23h40 | 10 | **0** | **absente** |

### Contrôle du rabattement orthographique (piège n° 2)

**La ligne « Résultats, y compris pour X. Essayez avec l'orthographe Y uniquement » n'est apparue sur AUCUNE des quatorze pages.** Conséquences :

1. Google **ne rabat pas** `mappemonde` sur `globe terrestre`, ni `carte du monde à gratter` sur `carte à gratter`, ni `planisphère` sur `mappemonde`. Ce sont des racines distinctes servies par des pages 1 distinctes — **la réserve n° 6 de `02-volume-consolide.md` est levée**, l'arborescence à trois pôles tient.
2. **Mais il existe un rabattement de fait, sans bannière, entre `planisphère` et `planisphere`** (requêtes 11 et 13) : **7 des 9 hôtes organiques sont identiques** (fr.wikipedia.org, cartovia.com, geoconfluences.ens-lyon.fr, stock.adobe.com, fr.pinterest.com, pappus-editions.com, nuees.net) et les recherches associées se recouvrent à 6 sur 8. **Une seule page sert les deux écritures.** C'est cohérent avec la règle de consolidation (on additionne ce qu'une seule page servirait) : les deux volumes vont bien ensemble — ils partagent aussi le même sort.

---

## 2. Tableaux par tête

### Tête 1 — `globe terrestre` (famille 1, 31 150 consolidés)

| Colonne | Constat |
|---|---|
| **Ce que Google sert** | Page hybride. Un très gros étage marchand : **32 annonces pour offre de produit**, deux blocs produits distincts, filtres de marque en haut de page (**VTech, National Geographic, Clementoni, Lexibook**) et filtres `New` / `Used` / `Nearby`. Produits servis : globes lumineux, globes enfant, globes interactifs, globes déco design, un globe MOVA, un Zoffoli à 2 850 €. Étage organique mince : 8 positions seulement. |
| **Intention** | **Oui.** La requête désigne bien notre produit — le nom même de la niche. |
| **Commercial ou informationnel** | **Commercial en surface d'annonces, mixte en organique.** Sur 8 positions organiques : **3 sont non marchandes** (Google Earth, Wikipédia, Getty Images) et 1 est un fournisseur de matériel pédagogique B2B (Jeulin). Soit **4/8 non exploitables commercialement — exactement le seuil d'alerte de la méthode (« quatre sur dix »).** Une collection seule ne prendra pas cette page ; il faudra du contenu. |
| **Qui tient la page 1** | marketplace **1** (amazon.fr) · généraliste **1** (natureetdecouvertes.com) · marque **0** · spécialiste indépendant **2** (**barsglobes-et-mappemondes.com** « La Maison du Globe », depuis 1996 ; **univers-globe.com** « L'Univers du Globe ») · drop probable **0** · non marchand **3** (earth.google.fr, fr.wikipedia.org, gettyimages.fr) · B2B scolaire **1** (jeulin.com). **Un site de ma liste de veille apparaît : `univers-globe.com` est bien « Univers Globe ».** Aucun des huit autres (mon-globe-terrestre.com, globeterrestre.net, Afficheo, Eclyna, Gaia Map, La Carte du Monde, L'Afficherie, Woodleo). |
| **Volume** | **Retenu : 31 150 sur 31 150.** Aucun motif de retrait : la page vend, la requête désigne le produit, et les intentions parasites (dessin, 3D, coloriage) avaient déjà été retirées à l'étape 4. |

**Recherches associées :** Globe terrestre 3D · Globe terrestre interactif · Globe terrestre dessin · Planisphère globe terrestre · Globe terrestre en français · Globe terrestre Action.
→ **Contrôle marque cachée (piège n° 4) : négatif au niveau de la grappe organique**, mais la couche Shopping est explicitement segmentée par marque (VTech, National Geographic, Clementoni, Lexibook) et une seule enseigne apparaît en recherche associée (Action). Les lignes de marque correspondantes avaient déjà été retirées à l'étape 4 (2 550).
→ **Signal à retenir pour la suite : le sous-segment enfant / interactif est un marché de jouet éducatif tenu par des marques** (VTech, Clementoni, Buki, Lexibook) et distribué par King Jouet, Smyths Toys, Orchestra, Cultura. Il est vérifié en détail à la requête 7.

**Bande de prix relevée (33 prix) :** 13,99 · 18,99 · 19,99 · 23,99 · 25,99 · 27,97 · 27,98 · 29,90 · 34,99 · 37,90 · 38,08 · 42,99 · 44,95 · 46,90 · 49,95 · 62,00 · 69,95 · 72,95 · 89,00 · 94,50 · 95,03 · 95,88 · 99,95 · 149,00 · 237,60 · **2 850,00 €**.
→ **Médiane ≈ 46 €**, cœur de bande **25-100 €**, queue haute artisanale (Zoffoli 2 850 €). C'est la famille la mieux dotée en prix de tout l'univers.

---

### Tête 2 — `mappemonde` (famille 3a, tête de 12 100 dans un consolidé de 18 260)

**C'est le retournement de cette vérification.**

| Colonne | Constat |
|---|---|
| **Ce que Google sert** | **Une page d'encyclopédie.** Définitions (Larousse, Wikipédia, AquaPortail), listes de pays, cartes de référence, banques d'images (iStock, Adobe Stock), un blog voyage. **Aucun bloc Shopping. Aucune annonce produit. Aucun prix affiché nulle part sur la page 1 — zéro occurrence du symbole €.** À comparer aux 32 annonces produit de `globe terrestre` sur la même mécanique de requête. |
| **Intention** | **Partiellement, et minoritairement.** Le mot est d'abord un mot de vocabulaire géographique. La demande d'objet existe (elle porte la famille consolidée) mais elle ne s'exprime pas sur le mot nu. |
| **Commercial ou informationnel** | **Informationnel à 7 positions sur 9.** Non marchands : mappemonde.net, fr.mapsofworld.com, fr.wikipedia.org, istockphoto.com, larousse.fr, stock.adobe.com, globe-trotting.com. Marchands : amazon.fr, univers-globe.com. **Le seuil d'alerte de la méthode (4/10) est dépassé de très loin : 78 % de la page 1 est éditoriale.** Une collection seule ne prendra jamais cette page. |
| **Qui tient la page 1** | marketplace **1** (amazon.fr) · généraliste **0** · marque **0** · spécialiste indépendant **1** (univers-globe.com — le seul marchand spécialiste de la page) · drop probable **0** · non marchand **7** (dont 2 banques d'images et 2 dictionnaires/encyclopédies). |
| **Volume** | **Retiré : ~8 500 sur les 12 100 de la tête, estimation à ~70 %.** Le reste de la famille (`mappemonde globe`, `globe mappemonde`, `mappemonde interactive`, `bar mappemonde`, `mappemonde lumineuse`, `mappemonde ancienne`, `mappemonde enfant`, `mappemonde deco`, `lampe mappemonde`…) est qualifié par un modificateur d'objet et n'est pas touché. **Famille 3a : 18 260 → ~9 760.** |

**Questions posées par Google (PAA), toutes informationnelles :** « Quelle est la définition de "mappemonde" ? » · « Quelle est la différence entre une mappemonde et un planisphère ? » (deux fois) · **« Quel est le synonyme de "mappemonde" en mots fléchés ? »**
→ **C'est le piège n° 3 dans sa forme la plus pure**, celle-là même qui avait fait tomber `outil horloger` : la requête sert **des mots croisés**.

**Recherches associées :** Mappemonde carte · Mappemonde globe · **Mappemonde définition** · Mappemonde en français · **Mappemonde 3D** · **Mappemonde gratuite** · Mappemonde en anglais · Mappemonde enfant.
→ **Contrôle marque cachée (piège n° 4) : négatif.** Aucune grappe de marque dans la traîne de `mappemonde` — ni marque produit, ni enseigne. Le problème de ce mot n'est pas la marque, c'est l'intention.
→ 3 associées sur 8 sont explicitement non marchandes (`définition`, `gratuite`, `3D`).

**Bande de prix relevée : aucune.** Zéro prix sur la page 1. C'est en soi le constat.

**Note sur un acteur non listé :** le bloc images est occupé trois fois par **Original Map** (cartes du monde plexiglas / tableaux) — acteur français à noter pour l'étape concurrence, absent de l'organique.

---

### Tête 3 — `carte du monde à gratter` (famille 4b, 8 400 consolidés)

| Colonne | Constat |
|---|---|
| **Ce que Google sert** | **Une page de vente, sans ambiguïté.** Bloc « Produits Sponsorisés » explicitement libellé en tête, **32 annonces pour offre de produit**, filtres de format en haut de page (Europe, Voyage, Capitales, Affiche, Impression, Encadré, Tableaux, Art sur toile). Produits servis : cartes à gratter XXL, formats encadrés, coffrets cadeau. |
| **Intention** | **Oui, sans réserve.** Le produit est exactement celui de la famille. |
| **Commercial ou informationnel** | **Commercial à 8 positions sur 9.** Une seule position éditoriale (globe-trotting.com, blog voyage — probablement affilié). Très en dessous du seuil d'alerte. Une collection prendra cette page si elle est correctement faite. |
| **Qui tient la page 1** | marketplace **2** (amazon.fr, cdiscount.com) · généraliste **3** (fnac.com, gifi.fr, natureetdecouvertes.com) · marque **1** (lachaiselongue.fr — marque cadeau française) · spécialiste indépendant **2** (**lemondeagratter.com**, mono-produit, et **poledesetoiles.fr**) · drop probable **1 à 2** (lemondeagratter.com est un mono-produit au nom exact de la requête — profil de boutique drop ou d'affilié spécialisé ; à confirmer à l'étape concurrence, non tranché ici) · non marchand **1**. **Aucun site de ma liste de veille n'apparaît.** |
| **Volume** | **Retenu : ~7 560 sur 8 400, soit un retrait estimé de ~10 % (840)** au titre de l'intention « où l'acheter en magasin » (voir ci-dessous). Ce n'est pas un retrait d'intention produit — c'est un retrait de part adressable en ligne. |

**Recherches associées :** Carte du monde à gratter **Cultura** · Carte du monde à gratter **IKEA** · Carte du monde à gratter XXL · Carte du monde à gratter **GIFI** · Carte du monde à gratter petit format · Carte du monde à gratter **leclerc**.
→ **Contrôle marque cachée (piège n° 4) : positif, mais en enseignes, pas en marques produit.** **4 associées sur 6 sont des enseignes physiques** (Cultura, IKEA, Gifi, Leclerc), et Gifi tient une position organique. L'étape 4 n'avait retiré que `carte du monde à gratter cultura` (170) : la demande « je veux l'acheter en magasin près de chez moi » pèse manifestement plus que cette seule ligne. D'où le retrait estimé de ~10 %.

**Bande de prix relevée (54 prix) :** cœur très dense entre **14,99 et 29,95 €** (18,09 · 18,50 · 18,69 · 18,95 · 19,99 ×6 · 20,99 · 22,17 · 22,21 · 22,99 ×3 · 23,99 · 24,90 · 24,99 · 25,00 · 26,99 · 28,92 ×2 · 28,98 · 29,95 ×3), plancher à 13,99 et hauts isolés à 35,00 · 40,17 · 42,99 · 48,41 · 89,00 €. Les valeurs à 2,95 / 3,00 / 3,95 / 4,33 / 5,95 / 6,30 € sont des frais de livraison ou des accessoires, pas des produits.
→ **Médiane produit ≈ 22 €.** **Signal d'alerte prix à transmettre : cette famille est franchement low ticket** et devra passer la porte `STOP_PRIX_PANIER`. Ce n'est pas mon mandat de la franchir, je la signale.

---

### Tête 4 — `carte du monde en bois` (famille 4a, 5 490 consolidés)

| Colonne | Constat |
|---|---|
| **Ce que Google sert** | **Une page de vente haut de gamme.** Bloc « Produits Sponsorisés » en tête, **32 annonces pour offre de produit**, filtres de format déco (Impression, Affiche, Encadré, Œuvre d'art originale, Pancartes décoratives, Tableaux, Miroirs, Sculptures). Produits servis : cartes murales en bois découpé, panneaux chêne 200×120 cm, versions 3D et LED. |
| **Intention** | **Oui, sans réserve.** |
| **Commercial ou informationnel** | **Commercial à 8 positions sur 9.** Seule position non marchande : pinterest.com. Très loin sous le seuil d'alerte. |
| **Qui tient la page 1** | marketplace **1** (amazon.fr) · généraliste **1** (natureetdecouvertes.com) · marque **1** (fr.magicholz.de, marque allemande) · spécialiste indépendant **4** (**woodwork08.com** qui prend **deux** positions, **creatifwood.com**, **68travel.fr**, **atelierchezsoi.fr**) · drop probable **1 à 2** (creatifwood.com et 68travel.fr ont un profil de boutique mono-thème ; non tranché ici, à confirmer à l'étape concurrence) · non marchand **1**. **Aucun site de ma liste de veille n'apparaît** — ni Woodleo, ni Afficheo, ni La Carte du Monde. |
| **Volume** | **Retenu : 5 490 sur 5 490.** Aucun motif de retrait. **C'est la famille la plus proprement marchande de l'univers avec la plus haute bande de prix**, et son KD mesuré (3 à 17) confirme le piège n° 6 dans le bon sens : peu de densité, page 1 tenue par des indépendants de même nature que nous. |

**Questions posées par Google (PAA) :** « Quel est le meilleur type de carte du monde ? » · **« Comment faire sa propre map ? »** · « Comment accrocher une carte du monde au mur ? » · « Quels sont les différents types de cartes du monde ? »
→ Une adjacence DIY (« faire sa propre map ») existe, mais elle n'occupe **aucune** position organique. Pas de retrait.

**Recherches associées :** Carte du monde en bois 3D · en Français · mural · **maison du monde** · 3D LED · de luxe.
→ **Contrôle marque cachée (piège n° 4) : négatif.** Cinq associées sur six sont des modificateurs produit (3D, LED, luxe, mural, français). Une seule enseigne (Maison du Monde), aucune grappe de marque produit. Le seul retrait de marque de l'étape 4 (`carte du monde bois ikea` 110) reste le bon.

**Bande de prix relevée (58 prix, hors frais de port à 4,99 / 5,99 / 9,90 €) :** 26,95 · 26,99 · 29,90 · 31,00 · 33,98 · 38,00 · 39,00 ×2 · 39,99 · 48,00 · 48,99 · 53,00 · 55,00 · 68,85 · 69,00 ×5 · 74,90 · 79,00 ×2 · 89,00 ×2 · 91,27 · 94,00 · 97,00 ×2 · 101,90 · 106,99 ×2 · 109,00 ×4 · 119,90 · 129,00 ×2 · 159,00 ×2 · 184,56 · 209,00 · 210,00 · 220,00 · 288,00 · 289,00 · 325,00 · 365,00 · 429,00 · **526,00 €**.
→ **Médiane ≈ 97 €**, cœur de bande **69-159 €**. **C'est la bande de prix la plus haute de tout U3** et la seule sans zone low-ticket.

---

### Tête 5 — `carte mappemonde` (tête de la famille 3a-bis mappemonde-mur, 5 540 consolidés)

| Colonne | Constat |
|---|---|
| **Ce que Google sert** | **Une page mixte à dominante référence.** Google ouvre sur une carte de référence (mapsofworld), affiche un onglet **« Lieux »** et une localisation (95390 Saint-Prix), puis intercale des posters à petit prix. **16 annonces pour offre de produit — la moitié de ce que servent les requêtes franchement marchandes de cet univers.** |
| **Intention** | **Partiellement.** Le mot « carte » nu ramène la demande vers la carte-document, pas vers l'objet déco. |
| **Commercial ou informationnel** | **Informationnel à 5 positions sur 10 — au-dessus du seuil d'alerte de la méthode.** Non marchands : fr.mapsofworld.com, earth.google.fr, pinterest.com, 24timezones.com, fr.wikipedia.org. Une collection seule ne prendra pas cette page. |
| **Qui tient la page 1** | marketplace **0** · généraliste **1** (bimago.fr, déco murale) · marque **2** (**boutique.ign.fr** — l'IGN ; **antica-editions.com** — éditeur de cartes anciennes) · spécialiste indépendant **2** (**cartopolo.fr**, **originalmap.fr**) · drop probable **0 confirmé** (originalmap.fr est le profil le plus proche ; non tranché ici) · non marchand **5**. **Un site de ma liste apparaît indirectement : aucun des neuf noms surveillés, mais `originalmap.fr` est le même acteur « Original Map » déjà repéré au bloc images de `mappemonde`.** |
| **Volume** | **Retiré : ~1 150.** Estimation à **50 % sur les deux têtes nues de la famille** (`carte mappemonde` 1 300 + `mappemonde carte` 1 000 = 2 300), au prorata des 5 positions organiques non marchandes sur 10. Le reste de la famille (`mappemonde murale` 720, `mappemonde bois` / `en bois` / `sur bois` 1 170, `tableau mappemonde` 170, `poster mappemonde` 140, `affiche mappemonde` 110, `mappemonde a gratter` 110, `mappemonde liege` / `en liege` 200, stickers, cadres…) est qualifié par un modificateur d'objet et n'est pas touché. **Famille 3a-bis : 5 540 → 4 390.** |

**Questions posées par Google (PAA) :** « Quelle est la différence entre planisphère et mappemonde ? » · **« Où puis-je trouver un mappemonde en ligne ? »** · **« Où puis-je trouver une carte Google Maps satellite gratuite ? »** · « C'est quoi la carte Mercator ? » — **4 sur 4 informationnelles.**

**Recherches associées :** Carte du monde avec pays · **Carte du monde pays gratuit** · Carte du monde simple · **Carte du monde avec pays PDF** · Carte Europe · **Planisphère du monde détaillée** · Carte du monde continents et pays · **Google Earth**.
→ **8 associées sur 8 sont informationnelles**, dont deux explicitement gratuites/PDF. C'est le même bassin scolaire que `carte du monde` 301 000, déjà exclu à l'étape 4 — et la confirmation que l'exclusion était juste.
→ **Contrôle marque cachée : négatif.** Aucune marque dans la traîne.
→ **À noter pour la réserve : `Planisphère du monde détaillée` apparaît ici, dans un contexte 100 % informationnel.** Premier indice sur le sort des 46 000.

**Bande de prix relevée (29 prix) :** 6,80 · 8,39 · 8,50 · 8,90 · 11,92 · 12,00 · 12,95 · 16,90 · 16,95 · 18,49 · 19,00 · 19,50 · 20,00 · 24,41 · 25,90 · 29,95 · 34,50 · 44,99 · 49,00 · 55,00 · 70,80 · 71,20 · 117,56 · **369,00 €**.
→ **Médiane ≈ 20 €**, cœur **8-35 €** (posters, affiches). Bande basse — c'est la famille poster/affiche qui parle ici, pas la carte-objet.

---

### Tête 6 — `carte du monde liège` (famille 4e, 3 410 consolidés)

| Colonne | Constat |
|---|---|
| **Ce que Google sert** | **Une page de vente.** **32 annonces pour offre de produit**, filtres de format (Impression, Affiche, Océan, Photographie, Encadré) et filtres marchands (New / Used / Nearby). Produits servis : cartes du monde en liège à épingler, panneaux liège, coffrets avec punaises. |
| **Intention** | **Oui**, avec une réserve d'homonymie (voir plus bas). |
| **Commercial ou informationnel** | **Commercial à 8 positions sur 9.** Une seule position éditoriale (globe-trotting.com). |
| **Qui tient la page 1** | marketplace **1** (amazon.fr) · généraliste **1** (gifi.fr) · marque **2** (**misswood.eu**, la marque de référence de la carte en liège ; **boutique.ign.fr**) · spécialiste indépendant **4** (**liege24.fr** et **boutique-allboards.fr**, spécialistes du liège comme matériau ; **recollection.fr** et **tablodeco.fr**, déco murale) · drop probable **2** (recollection.fr et tablodeco.fr ont le profil ; non tranché ici) · non marchand **1**. **Aucun site de ma liste de veille n'apparaît.** |
| **Volume** | **Retiré : ~340, estimation à 10 %.** Motif : **intention d'achat en magasin physique**, lisible dans les recherches associées. Le reste est retenu : **3 410 → 3 070.** |

**Contrôle piège n° 3 (générique contaminé) — résultat mitigé mais à écrire :** Google affiche un onglet **« Lieux »** et deux questions PAA sur **la ville belge de Liège** (« Où se trouve Liège sur la carte ? », « Liège est située dans quel pays ? »). **L'homonymie liège-matériau / Liège-ville est réelle dans la tête de Google, mais elle ne contamine aucune position organique** : les 9 résultats sont tous des cartes en liège. Les formulations de la famille contiennent toutes « monde », ce qui les protège. **Aucun retrait à ce titre — mais c'est un risque de ciblage à transmettre pour les campagnes Search, où le mot nu ramènerait de la Belgique.**

**Recherches associées :** Carte du monde liège **cultura** · liège **leroy merlin** · en liège **GIFI** · Carte Monde Liège **Nature et decouverte** · en liège avec punaise · en liège **amazon**.
→ **Contrôle marque cachée (piège n° 4) : positif, en enseignes.** **5 associées sur 6 sont des enseignes** (Cultura, Leroy Merlin, Gifi, Nature & Découvertes, Amazon). L'étape 4 avait conclu « aucune marque dans la grappe » — c'est vrai au niveau du Keyword Magic Tool, **et faux au niveau de la SERP**. D'où le retrait de 10 %.

**Bande de prix relevée (37 prix) :** 12,10 · 14,39 · 19,79 · 20,39 · 20,99 ×2 · 21,09 · 24,90 · 24,95 ×2 · 24,99 · 27,29 · 28,99 · 32,59 · 34,79 · 39,95 · 41,95 · 45,99 · 46,13 · 49,59 · 56,49 · 56,99 ×3 · 69,90 · 69,99 ×4 · 70,74 · 71,95 · 84,08 · 89,00 · 98,08 €.
→ **Médiane ≈ 41 €**, cœur **20-70 €**. Bande saine, sans zone low-ticket dominante.

---

### Tête 7 — `globe interactif` (graine 3 600, + 3 600 de formulations « interactif » dans les familles 1 et 3a)

**C'est le retournement le plus lourd de cette vérification, et il était explicitement demandé au brief.**

| Colonne | Constat |
|---|---|
| **Ce que Google sert** | **Un rayon de jouet éducatif de marque.** Google segmente lui-même la requête par des **filtres de marque en haut de page : Vtech · Clementoni · Carrefour · Exploraglobe · 5 ans · Amazon · Tiptoi · King Jouet.** 24 annonces pour offre de produit, toutes sur des références de marque. |
| **Intention** | **Pas du tout celle qu'on croit.** La requête ne désigne pas un globe déco connecté : elle désigne **le Genius XL de VTech, l'Exploraglobe de Clementoni et le tiptoi de Ravensburger**. Ce sont trois références de jouets, pas une catégorie de produit ouverte. |
| **Commercial ou informationnel** | Commercial à 7 positions sur 8 (une seule éditoriale, bfmtv.com). **Mais la commercialité n'est ici d'aucun secours : la page est fermée par la marque, pas par l'intention.** |
| **Qui tient la page 1** | **marque 3** (**vtech-jouets.com**, **fr.clementoni.com**, **ravensburger.fr** — les trois sites officiels des trois fabricants, en tête de page) · marketplace **1** (amazon.fr) · généraliste **2** (lagranderecre.fr, oxybul.com — deux enseignes de jouets, revendeurs de ces mêmes marques) · comparateur **1** (idealo.fr) · spécialiste indépendant **0** · drop probable **0** · non marchand **1**. **Zéro position pour un indépendant. Zéro produit sans marque.** |
| **Volume** | **Retiré : ~80 %, estimation à la composition de la page 1.** Motif : **piège n° 4, marque cachée dans un mot générique — dans sa forme maximale.** `globe interactif` a l'air d'un descriptif de produit ; c'est en réalité le nom d'usage de trois références de marque, exactement comme `montre field` était Anna Field et Khaki Field. |

**Recherches associées :** Globe interactif **Vtech** · **Clementoni** · **carrefour** · **exploraglobe** · **5 ans** · **amazon** · **tiptoi** · **King Jouet** — **8 sur 8 sont des marques ou des enseignes.** Le contrôle marque cachée est aussi net qu'il peut l'être.

**Application chiffrée du retrait (estimations, pas de nouvelles mesures) :**

| Ligne concernée | Où elle est comptée | Volume | Retrait à 80 % |
|---|---|---:|---:|
| Graine `globe interactif` | hors total prudent, dans la variante haute 85 860 | 3 600 | **−3 600, retirée en totalité** |
| `globe terrestre interactif` + `globe terrestre intéractif` + `globe terrestre interactif 5 ans` | famille 1 | 3 120 | **−2 500** |
| `mappemonde interactive` | famille 3a | 480 | **−384** |
| **Total du retrait sur le total prudent de 80 960** | | | **−2 884** |

La graine `globe interactif` 3 600 ne figurait pas dans le total prudent de 80 960 : **elle sort définitivement de la variante haute**, qui perd donc 3 600 supplémentaires.

**Bande de prix relevée (30 prix) :** 13,16 · 18,99 · 27,99 · 29,99 ×2 · 33,97 · 34,99 · 36,99 · 39,99 ×2 · 45,99 · 47,38 · 49,90 · 57,99 · 59,99 ×2 · 65,00 · 78,00 · 84,99 · 85,00 · 95,88 · 99,90 · 109,99 ×2 · 111,54 · 120,99 · 158,80 · 170,35 · 194,26 €.
→ Médiane ≈ 59 €. Bande correcte — **mais c'est la bande de prix d'un jouet de marque, pas la nôtre.**

---

### Tête 8 — `carte du monde murale` (famille 4c, 3 020 additionnels consolidés)

| Colonne | Constat |
|---|---|
| **Ce que Google sert** | **Une page de vente déco.** **32 annonces pour offre de produit**, filtres de format (Impression, Affiche, Peinture, Photographie, Encadré, Sur toile, Tableaux, Papier peint). Produits servis : cartes murales grand format, toiles, panneaux bois, papiers peints. |
| **Intention** | **Oui.** |
| **Commercial ou informationnel** | **Commercial à 8 positions sur 9** (seule position non marchande : pinterest.com). Aucune question PAA affichée. |
| **Qui tient la page 1** | marketplace **1** (amazon.fr) · généraliste **2** (bimago.fr, cultura.com) · marque **2** (juniqe.com, izoa.fr) · spécialiste indépendant **3** (**originalmap.fr**, **creatifwood.com**, **cartovia.com**) · drop probable **2** (originalmap.fr et creatifwood.com, tous deux déjà croisés sur d'autres têtes de l'univers — profil de boutique mono-thème ; non tranché ici) · non marchand **1**. |
| **Volume** | **Retenu : 3 020 sur 3 020.** Aucun motif de retrait. |

**Recherches associées :** Carte du monde murale grand format · murale bois · murale avec photos · Belle carte du monde murale · murale français · Carte du monde déco **IKEA**.
→ **Contrôle marque cachée : négatif.** Cinq associées sur six sont des modificateurs produit, une seule enseigne.
→ Ces associées confirment ce que disait `02-volume-consolide.md` : les formulations déco que Codex avait déclarées introuvables **existent bien** (`belle carte du monde murale`, `carte du monde déco`), et elles sont marchandes.

**Bande de prix relevée (36 prix) :** 12,55 · 16,95 · 18,89 · 19,99 · 22,50 · 25,90 · 28,99 · 29,00 · 29,90 ×2 · 29,99 · 37,42 · 38,00 · 38,80 · 39,99 · 44,99 · 53,00 · 69,00 · 79,90 · 89,00 ×2 · 112,42 · 129,00 · 136,00 · 159,00 ×2 · 169,00 · 249,00 · 325,00 · **569,00 €**.
→ **Médiane ≈ 39 €**, cœur **29-159 €**. Bande large et saine.

---

### Tête 9 — `poster carte du monde` (famille 4d, 2 730 consolidés)

| Colonne | Constat |
|---|---|
| **Ce que Google sert** | **Une page de vente pure.** **32 annonces pour offre de produit**, filtres de format (Français, Photographie, Encadré, Œuvre d'art originale, Impression, Affiche, Art sur toile, **Cartes murales**). |
| **Intention** | **Oui.** |
| **Commercial ou informationnel** | **Commercial à 9 positions sur 9. C'est la seule page 1 de tout l'univers sans une seule position éditoriale.** |
| **Qui tient la page 1** | marketplace **1** (amazon.fr) · généraliste **0** · **marque 6** (**posterlounge.fr**, **desenio.fr**, **juniqe.com**, **scenolia.com**, **micasia.fr** — cinq plateformes/marques d'affiches installées, plus **boutique.ign.fr** et **pappus-editions.com**, deux éditeurs cartographiques) · spécialiste indépendant **1** (cartopolo.fr) · **drop probable 0** · non marchand **0**. |
| **Volume** | **Retiré : ~270, estimation à 10 %** au titre de la frange « affiches gratuites / imprimer soi-même » lisible dans les questions PAA, et de l'intention enseigne. **2 730 → 2 460.** |

**Le vrai constat de cette tête n'est pas un retrait de volume, c'est une porte fermée.** Neuf positions sur neuf appartiennent à des acteurs installés du poster ou de l'édition cartographique, et **aucun indépendant de notre nature n'y figure**. C'est l'inverse exact de `boite a montre` sur Noirmont (KD 35, six indépendants français en page 1 = porte difficile mais ouverte). Ici la page est commerciale **et** verrouillée.

**Questions posées par Google (PAA) :** « Où puis-je trouver une carte du monde avec la vraie échelle ? » · « Quel est le meilleur site pour créer des posters ? » · **« Où trouver des affiches gratuites ? »** · « Comment faire sa propre map ? »

**Recherches associées :** Poster carte du monde **IKEA** · pays · en français · voyage · **Cultura** · enfant. Deux enseignes sur six ; contrôle marque cachée : négatif au sens produit.

**Bande de prix relevée (37 prix) :** 5,49 · 5,95 · 5,99 ×2 · 6,80 · 7,50 · 7,90 · 8,00 · 10,80 · 10,90 ×3 · 12,00 · 12,55 · 12,87 · 12,99 · 14,99 · 16,90 · 16,95 · 17,90 · 18,49 · 19,47 · 19,50 · 19,99 ×3 · 22,91 · 24,23 ×2 · 28,00 · 31,99 · 35,99 · 43,45 · 47,92 · 144,00 · 156,99 · 249,00 €.
→ **Médiane ≈ 17 €**, et **onze prix relevés sont sous 12 €**. **C'est la bande la plus basse de l'univers, très en dessous du plancher de ratio prix/CPC.** Signal `STOP_PRIX_PANIER` à transmettre — je le signale, je ne le tranche pas.

---

### Tête 10 — `globe bar` (famille 2a, 1 730 additionnels consolidés — contrôle de retournement demandé)

| Colonne | Constat |
|---|---|
| **Ce que Google sert** | **Une page à trois étages.** (1) En tête, **un pack local** : « Résultats de recherche à proximité », adresses, carte, **Le Globe Café à Paris, 4,3(1,7 k), 10-20 €, Café** — Google interprète partiellement la requête comme la recherche d'un établissement. (2) 24 annonces pour offre de produit, sur des bars-globes réels. (3) Un organique marchand, avec un fort courant occasion. Filtres marchands : New / Used / **Nearby** / Price / Buy. |
| **Intention** | **Oui pour le produit, mais partagée.** Le produit existe et il est servi — le contrôle de retournement demandé au brief est **positif : le globe-bar est bien un meuble-bar en forme de globe**, pas autre chose. Mais deux intentions concurrentes occupent la page : l'établissement (pack local, PAA) et l'occasion. |
| **Commercial ou informationnel** | Commercial à 8 positions sur 8 en organique. **Mais 2 des 4 questions PAA portent sur des bars-établissements** (« Quel est un nom rigolo de bar ? », « Quels sont les bars les plus insolites au monde ? »), et le pack local occupe le haut de la page avant tout résultat produit. |
| **Qui tient la page 1** | **marque 2** (**zoffoliliving.com**, le fabricant italien de référence, qui prend **deux** positions) · marketplace **3** (amazon.fr, **leboncoin.fr** — occasion, idealo.fr — comparateur) · généraliste **1** (leroymerlin.fr) · spécialiste indépendant **2** (**univers-globe.com**, **barsglobes-et-mappemondes.com** — les deux mêmes qu'en tête 1) · drop probable **0**. |
| **Volume** | **Retiré : ~430, estimation à 25 %** — dont ~10 % d'intention établissement (pack local + PAA) et ~15 % d'intention occasion. **1 730 → 1 300.** |

**Recherches associées :** Globe bar **vintage** · Bar globe **ancien occasion** · Globe bar vintage **prix** · Bar globe terrestre **le bon coin** · Globe bar **paris** · Globe bar moderne.
→ **Quatre associées sur six relèvent du marché de l'occasion** (vintage, ancien occasion, prix, le bon coin), et leboncoin.fr tient une position organique. **C'est un marché de seconde main autant que de neuf** — constat structurel important, qui ne se voyait pas du tout dans le Keyword Magic Tool.
→ Une associée est navigationnelle (Globe bar paris). L'étape 4 avait déjà retiré 330 à ce titre ; la SERP montre que la part navigationnelle est plus large que ces trois lignes.

**Bande de prix relevée (28 prix) :** 92,99 · 114,99 · 117,48 · 124,27 · 126,70 · 127,99 · 129,99 · 130,49 · 144,99 · 174,43 · 199,00 · 200,00 · 214,99 · 219,00 · 221,00 · 317,23 · 385,00 · 389,00 · 415,00 · 420,00 · 517,50 ×2 · 590,00 · 599,23 · 605,85 · 730,00 · **820,00 €**.
→ **Médiane ≈ 214 €. C'est de loin la bande de prix la plus haute de tout U3**, et la seule sans aucun produit sous 90 €.

---

### Têtes 11 à 14 — la réserve indéterminée `planisphère` (46 000)

Ces quatre têtes n'entraient dans aucun total de `02-volume-consolide.md`. Elles étaient explicitement renvoyées à cette étape. Les voici, dans un tableau unique.

#### 11 — `planisphère` (27 100)

| Colonne | Constat |
|---|---|
| **Ce que Google sert** | **Une page de dictionnaire.** Google ouvre sur un **extrait optimisé Wikipédia** donnant la définition (« représentation plane de la surface du globe terrestre », projection de Hölzel). **Zéro annonce pour offre de produit — le compteur ne relève aucune ligne d'annonce sur toute la page.** Deux prix seulement sur l'ensemble de la page 1. |
| **Intention** | **Pas du tout.** C'est un mot de leçon de géographie. |
| **Commercial ou informationnel** | **Informationnel à 5 positions sur 8**, extrait optimisé encyclopédique en tête, et **4 questions PAA sur 4 informationnelles** — dont **« Pourquoi planisphère est-il masculin ? »**, une question de grammaire. |
| **Qui tient la page 1** | non marchand **5** (geoconfluences.ens-lyon.fr — ressource pédagogique de l'ENS Lyon, stock.adobe.com, fr.pinterest.com, **dictionnaire.lerobert.com**, nuees.net) · marketplace **1** (amazon.fr) · spécialiste indépendant **1** (cartovia.com) · marque/éditeur **1** (pappus-editions.com) · drop probable **0**. |
| **Volume** | **Sort à ~85 %.** |

**Recherches associées :** Planisphère du monde · **vierge** · **PDF** · **à imprimer** · **def** · Europe · **en ligne** · continent — **8 sur 8 informationnelles ou gratuites.**

#### 12 — `planisphère du monde` (5 400)

| Colonne | Constat |
|---|---|
| **Ce que Google sert** | Une page mixte, mais **Google segmente lui-même la requête par des filtres explicitement scolaires : Pays · 3D · En français · CM2 · Vierge · À imprimer · Gratuit · En ligne.** **Zéro annonce pour offre de produit.** Cinq prix seulement, dont deux frais de port. |
| **Intention** | **Partiellement.** Des tableaux et affiches apparaissent, mais tout l'espace de modificateurs est scolaire. |
| **Commercial ou informationnel** | Organique **marchand à 6 positions sur 9** — mais **aucun annonceur ne paie sur cette requête**, ce qui est le signal le plus dur de la page. |
| **Qui tient la page 1** | spécialiste indépendant **3** (**originalmap.fr**, **cartovia.com**, **linstantideal.fr**) · généraliste **1** (bimago.fr) · marque/éditeur **1** (pappus-editions.com) · marketplace **1** (amazon.fr) · non marchand **3** (fr.wikipedia.org, fr.pinterest.com, histoire-itinerante.fr). |
| **Volume** | **Sort à ~70 %.** |

**Recherches associées :** pays · 3D · en français · détaillée · **CM2** · **vierge** · **à imprimer** · **gratuit** — 4 sur 8 explicitement scolaires ou gratuites.

#### 13 — `planisphere` sans accent (8 100)

| Colonne | Constat |
|---|---|
| **Ce que Google sert** | **La même page que la requête 11**, à deux hôtes près. 8 annonces pour offre de produit (contre 0 sur la version accentuée) — une couche marchande marginale. |
| **Intention** | **Pas du tout**, pour les mêmes raisons que la requête 11. |
| **Commercial ou informationnel** | Informationnel à 5 positions sur 9, Wikipédia en position 1. |
| **Qui tient la page 1** | Identique à la requête 11 à 7 hôtes sur 9 ; entrent magequip.com et originalmap.fr, sort amazon.fr. |
| **Volume** | **Sort à ~85 %**, même sort que la requête 11 puisque c'est la même page. |

#### 14 — `planisphère monde` (5 400)

| Colonne | Constat |
|---|---|
| **Ce que Google sert** | **La moins scolaire des quatre.** En **position 1 organique : `originalmap.fr`**, avec sa page de collection « Cartes du Monde, Mappemondes et Planisphères » et son accroche « plus de 60 cartes du monde, mappemondes, planisphères et projections cartographiques **pour sublimer votre intérieur** ». **C'est exactement notre type de page, et elle est première.** Mais **zéro annonce pour offre de produit** là encore. |
| **Intention** | **Partiellement, et la part déco est ici réelle.** |
| **Commercial ou informationnel** | Informationnel à 5 positions sur 10 — au seuil d'alerte. |
| **Qui tient la page 1** | spécialiste indépendant **3** (originalmap.fr **en position 1**, cartovia.com, linstantideal.fr) · marque/éditeur **1** (pappus-editions.com) · marketplace **1** (amazon.fr) · non marchand **5** (fr.mapsofworld.com, fr.wikipedia.org, earth.google.fr, fr.pinterest.com, **prof.parlemonde.org** — ressource pour enseignants). |
| **Volume** | **Sort à ~60 %.** |

**Recherches associées :** grand format · **PDF** · **à imprimer** · détaillée · **vierge** · continents · **CE2** · pays.

**Bandes de prix des quatre têtes réunies :** 8,00 · 8,50 · 20,00 · 22,00 · 28,00 · 53,59 ×2 · 55,00 · 59,00 · 80,01 · 85,00 · 140,00 · 144,00 €. **Douze prix pour quatre pages 1 de 46 000 recherches cumulées.** À comparer aux 54 prix relevés sur la seule page `carte du monde à gratter` (8 400 recherches). **Le marché ne s'exprime pas là.**

---

## 3. Classement corrigé

Rappel : **tous les pourcentages ci-dessous sont des estimations faites à la composition de la page 1, pas de nouvelles mesures.** Le volume « avant » vient de `02-volume-consolide.md` (variante prudente, 80 960).

| Famille (= une page de collection) | Avant | Après | Retrait | Motif du retrait |
|---|---:|---:|---:|---|
| 1 — **Globe terrestre** | 31 150 | **28 650** | −2 500 | Sous-segment `interactif` (3 120) retiré à 80 % : marché de jouet tenu par VTech, Clementoni, Ravensburger — piège n° 4 |
| 3a — **Mappemonde-objet** | 18 260 | **9 380** | **−8 880** | Tête `mappemonde` 12 100 retirée à 70 % (page 1 éditoriale à 7/9, zéro annonce produit, zéro prix, PAA « mots fléchés ») ; `mappemonde interactive` 480 retirée à 80 % |
| 4b — **Carte du monde à gratter** | 8 400 | **7 560** | −840 | 10 % d'intention « acheter en magasin » : 4 recherches associées sur 6 sont des enseignes (Cultura, IKEA, Gifi, Leclerc) |
| 3a-bis — **Mappemonde-mur** | 5 540 | **4 390** | −1 150 | Têtes nues `carte mappemonde` + `mappemonde carte` (2 300) retirées à 50 % : 5 positions non marchandes sur 10, 8 recherches associées sur 8 informationnelles |
| 4a — **Carte du monde en bois** | 5 490 | **5 490** | **0** | Page 1 marchande à 8/9, 4 spécialistes indépendants, bande de prix la plus haute des cartes murales. **Rien à retirer.** |
| 4e — **Carte du monde en liège** | 3 410 | **3 070** | −340 | 10 % d'intention enseigne : 5 recherches associées sur 6 sont des enseignes. L'homonymie avec la ville de Liège existe dans les PAA mais ne touche aucune position organique |
| 4c — **Carte du monde murale** | 3 020 | **3 020** | **0** | Page 1 marchande à 8/9, 3 spécialistes indépendants. **Rien à retirer.** |
| 4d — **Carte du monde poster / affiche** | 2 730 | **2 460** | −270 | 10 % au titre de la frange « affiches gratuites / faire sa propre map ». Page commerciale à 9/9 **mais verrouillée par 6 marques installées** |
| 2a — **Globe-bar** (part additionnelle) | 1 730 | **1 300** | −430 | 25 % : pack local d'établissements en tête de page (Le Globe Café) + marché de l'occasion (4 associées sur 6 en vintage/occasion/leboncoin) |
| 2b — **Globe en lévitation** (part add.) | 430 | **430** | 0 | **Non vérifiée en SERP** — budget épuisé. Reportée telle quelle |
| 3b — **Planisphère déco** | 800 | **800** | 0 | **Non vérifiée directement** ; les 5 formulations sont qualifiées par un modificateur (`noir et blanc`, `grand format`, `enfant`) et se comportent comme les autres lignes qualifiées. Reportée telle quelle, avec réserve |
| **TOTAL** | **80 960** | **66 550** | **−14 410** | **soit −17,8 %** |

**Contrôle arithmétique :** 2 500 + 8 880 + 840 + 1 150 + 0 + 340 + 0 + 270 + 430 + 0 + 0 = **14 410**. 80 960 − 14 410 = **66 550**. ✅

**Deux familles sortent indemnes de l'étape 5** — `carte du monde en bois` et `carte du monde murale`. **Une seule famille porte 62 % du retrait total** : mappemonde-objet, dont la tête vaut deux tiers du volume et ne vend rien.

---

## 4. Total U3 vérifié — constat arithmétique

| | Volume |
|---|---:|
| Total consolidé avant SERP (variante prudente) | 80 960 |
| **Total retiré à l'étape 5** | **−14 410** |
| **TOTAL U3 VÉRIFIÉ** | **66 550** |
| Plancher `catalogue-volume` | 30 000 |
| **Écart au plancher** | **+36 550** — le plancher est franchi **2,2 fois** |
| Zone de confort | 40 000 |
| **Écart au confort** | **+26 550** — la zone de confort est franchie **1,7 fois** |

**C'est un constat, pas un verdict.** Trois choses le complètent :

1. **Le retrait réel (−17,8 %) est un peu plus doux que l'hypothèse posée en section 7 de `02-volume-consolide.md`** (« un retrait SERP de l'ordre de 20-30 % laisserait encore 57 000 à 65 000 »). Le résultat mesuré, 66 550, est **au-dessus** de la fourchette anticipée.
2. **Comparaison Noirmont :** l'étape 5 y avait retiré 24 500 et retourné 3 familles sur 20. Ici elle retire 14 410 et **retourne une seule famille sur onze** — `globe interactif`, qui n'était de toute façon qu'une graine hors total prudent. **U3 résiste mieux à l'étape 5 que Noirmont.**
3. **La variante haute tombe plus lourdement.** Les 85 860 de `02-volume-consolide.md` perdent en plus la graine `globe interactif` 3 600 **en totalité** (page 1 fermée par trois marques de jouet) : 85 860 − 14 410 − 3 600 = **67 850**, dont 1 300 de `globe armillaire` toujours non vérifié en SERP.

---

## 5. Sort des 46 000 en réserve

**Verdict : elles sortent à ~80 %. La part qui pourrait rentrer est estimée à 9 100 — et je recommande de la laisser hors du total tant qu'elle n'est pas mesurée autrement, parce que c'est le chiffre le plus fragile de ce rapport.**

| Tête | Volume | Annonces produit | Organique non marchand | Modificateurs de la traîne | Sort estimé | Ce qui pourrait rentrer |
|---|---:|---:|---|---|---:|---:|
| `planisphère` | 27 100 | **0** | 5/8 + extrait optimisé Wikipédia | 8/8 informationnels (vierge, PDF, à imprimer, def, en ligne) | **sort à 85 %** | 4 065 |
| `planisphere` (sans accent) | 8 100 | 8 | 5/9 | 6/8 identiques à la précédente | **sort à 85 %** | 1 215 |
| `planisphère du monde` | 5 400 | **0** | 3/9 mais filtres Google **CM2 / Vierge / À imprimer / Gratuit / En ligne** | 4/8 scolaires ou gratuits | **sort à 70 %** | 1 620 |
| `planisphère monde` | 5 400 | **0** | 5/10 dont une ressource pour enseignants | 4/8 scolaires ou gratuits | **sort à 60 %** | 2 160 |
| **Total** | **46 000** | | | | **−36 940** | **9 060** |

**Le fait qui tranche : sur 46 000 recherches mensuelles cumulées, trois pages 1 sur quatre ne portent aucune annonce produit, et les quatre pages réunies n'affichent que douze prix.** Un marché où personne n'achète d'espace publicitaire et où presque rien n'est tarifé n'est pas un marché adressable. Codex avait raison d'exclure `planisphère` ; `02-volume-consolide.md` avait raison de ne pas le compter ; **la SERP confirme les deux.**

**La nuance, et elle mérite d'être écrite :** sur `planisphère monde`, **`originalmap.fr` est en position 1 avec une page de collection déco**. Une part déco existe donc réellement dans cette réserve — mais elle est petite, et **elle est déjà servie par les familles 4a-4e et 3a-bis** que nous comptons par ailleurs. La compter en plus reviendrait à compter deux fois la même page de collection.

**Décision de mesure : la réserve de 46 000 reste hors du total. Le total U3 vérifié demeure 66 550.**

---

## 6. Qui tient réellement les pages 1

### Synthèse par type d'acteur, sur les 14 pages lues (123 positions organiques)

| Type | Ce qu'on observe |
|---|---|
| **Marketplace** | **Amazon apparaît sur 11 des 14 pages — et à chaque fois avec exactement UNE position organique, jamais deux.** Cdiscount une fois, Leboncoin une fois (occasion, sur `globe bar`), Idealo deux fois (comparateur). **C'est le piège n° 6 dans le bon sens, à l'identique de `boite a montre` sur Noirmont : la marketplace est présente partout et dominante nulle part.** |
| **Généralistes** | Nature & Découvertes (3 pages), Cultura (2), Gifi (2), Fnac, Leroy Merlin, Bimago, La Grande Récré, Oxybul, Maisons du Monde (bloc produits). **Ils tiennent la couche Shopping bien plus que l'organique.** |
| **Marques** | Fortes et bloquantes sur deux zones seulement : **le jouet éducatif** (VTech, Clementoni, Ravensburger, Lexibook, Buki — page `globe interactif` entièrement fermée) et **le poster** (Posterlounge, Desenio, Juniqe, Scenolia, MiCasia — page `poster carte du monde` entièrement fermée). Ailleurs : Zoffoli sur le globe-bar (2 positions), Misswood sur le liège, Magicholz sur le bois, IGN et Pappus Éditions comme éditeurs cartographiques. |
| **Spécialistes indépendants** | **C'est eux qui tiennent le cœur de l'univers**, et ils sont nombreux et petits : `originalmap.fr` (**5 pages** — le plus présent de tous, position 1 sur `planisphère monde`), `cartovia.com` (**5 pages**), `pappus-editions.com` (5), `univers-globe.com` (3), `barsglobes-et-mappemondes.com` (2), `creatifwood.com` (2), `linstantideal.fr` (2), `woodwork08.com` (2 positions sur une même page), `lemondeagratter.com`, `liege24.fr`, `boutique-allboards.fr`, `recollection.fr`, `tablodeco.fr`, `68travel.fr`, `atelierchezsoi.fr`, `izoa.fr`, `poledesetoiles.fr`. |
| **Drop probable** | **Aucun cas tranché** — ce n'est pas mon mandat. Profils les plus proches, à passer à l'étape concurrence : `originalmap.fr`, `creatifwood.com`, `lemondeagratter.com` (mono-produit au nom exact de la requête), `tablodeco.fr`, `recollection.fr`, `cartovia.com`. |
| **Non marchands** | Concentrés sur trois requêtes seulement — `mappemonde`, `carte mappemonde` et les quatre `planisphère`. **Sur les familles qualifiées par un modificateur de matière ou de format (bois, liège, à gratter, murale, poster), ils tombent à 0 ou 1 position sur 9.** C'est la ligne de partage de tout l'univers. |

### Les neuf sites de la liste de veille

**Un seul apparaît en page 1 : `univers-globe.com` (« Univers Globe »), sur 3 des 14 requêtes** — `globe terrestre`, `mappemonde`, `globe bar`. C'est le spécialiste le mieux placé de l'univers, et le seul marchand spécialiste présent sur la page `mappemonde`.

**Les huit autres sont absents de toutes les pages 1 lues** : mon-globe-terrestre.com, globeterrestre.net, Afficheo, Eclyna, Gaia Map, La Carte du Monde, L'Afficherie, Woodleo. *Page 1 uniquement — leur absence ici ne dit rien de leur existence ni de leur trafic.*

### Bandes de prix relevées, par famille

| Famille | Plancher | **Médiane** | Cœur de bande | Plafond |
|---|---:|---:|---|---:|
| **Globe-bar** | 92,99 € | **~214 €** | 115-420 € | 820 € |
| **Carte du monde en bois** | 26,95 € | **~97 €** | 69-159 € | 526 € |
| Globe interactif *(hors périmètre)* | 13,16 € | ~59 € | 30-120 € | 194 € |
| **Globe terrestre** | 13,99 € | **~46 €** | 25-100 € | 2 850 € (Zoffoli) |
| **Carte du monde en liège** | 12,10 € | **~41 €** | 20-70 € | 98 € |
| **Carte du monde murale** | 12,55 € | **~39 €** | 29-159 € | 569 € |
| **Carte du monde à gratter** | 13,99 € | **~22 €** | 18-30 € | 89 € |
| **Mappemonde-mur** (`carte mappemonde`) | 6,80 € | **~20 €** | 8-35 € | 369 € |
| **Poster carte du monde** | 5,49 € | **~17 €** | 10-24 € | 249 € |
| Planisphère *(réserve)* | 8,00 € | ~54 € | 12 prix seulement | 144 € |

**Deux observations à transmettre, sans les trancher :**
- **L'univers est bimodal.** Un pôle haut (globe-bar ~214 €, bois ~97 €, globe terrestre ~46 €) et un pôle bas (à gratter ~22 €, poster ~17 €). **C'est exactement la configuration du piège des bandes bimodales** signalé dans la méthode de pricing : une médiane globale calculée sur tout U3 serait un chiffre faux.
- **Deux familles sont franchement low-ticket** — `poster carte du monde` (médiane 17 €, onze prix relevés sous 12 €) et `carte du monde à gratter` (médiane 22 €). Elles pèsent 10 020 des 66 550 vérifiés. **La porte `STOP_PRIX_PANIER` les concerne ; je la signale, je ne la franchis pas.**

## 7. Ce qui n'a pas pu être mesuré

1. **Les annonces Search texte n'ont pas pu être isolées, sur aucune des 14 requêtes.** Le compteur disponible ne distingue que les *annonces pour offre de produit* (PLA / Shopping). **Toute mention d'annonces dans ce rapport porte sur le Shopping, jamais sur le Search texte** — je ne prétends rien sur la pression publicitaire Search de cet univers.
2. **Page 1 uniquement.** C'est le mandat, et cela interdit formellement de juger la profondeur de la concurrence. Un acteur absent des pages lues n'est pas un acteur absent du marché.
3. **Tous les pourcentages de retrait sont des estimations faites à la composition de la page 1**, pas de nouvelles mesures. Ils sont reproductibles (ils suivent le ratio de positions non marchandes, ou la part d'enseignes dans les recherches associées) mais ils restent des jugements. **Le plus fragile de tous est celui de la section 5**, sur les 46 000 en réserve : c'est pourquoi je les laisse hors du total.
4. **Deux familles n'ont pas été vérifiées en SERP, faute de budget de requêtes** : `globe en lévitation` (430 additionnels) et `planisphère déco` (800). Elles sont reportées telles quelles dans le total de 66 550. Ensemble elles pèsent 1 230, soit 1,8 % du total — même retirées intégralement, elles ne changeraient aucun constat.
5. **La graine `globe armillaire` (1 300) n'a pas été vérifiée.** Elle n'était pas dans le total prudent ; elle reste hors de mes chiffres.
6. **Le sous-segment `enfant` n'a pas eu sa requête propre.** `globe terrestre enfant` (1 600), `globe terrestre lumineux enfant` (110) et `mappemonde enfant` (720) restent comptés en totalité. **Or la page `globe interactif` montre que le voisinage enfant est un rayon de jouet de marque**, et la couche Shopping de `globe terrestre` est filtrée par VTech / National Geographic / Clementoni / Lexibook. **Il y a là un risque de retrait supplémentaire de l'ordre de 2 400, non mesuré. Le total de 66 550 doit être lu comme une borne haute à ce titre.**
7. **Aucun contrôle de l'intention d'achat en magasin n'a pu être chiffré autrement qu'à la louche.** Les retraits de 10 % appliqués à `à gratter` et `liège` reposent sur la part d'enseignes dans les recherches associées (4/6 et 5/6), pas sur une mesure de volume.
8. **Aucune donnée de saisonnalité.** Sur une niche à forte composante cadeau (globe-bar, carte à gratter, carte en liège), la question Q4 reste entièrement ouverte.
9. **Aucun jugement porté sur le statut « drop probable ».** Six domaines ont un profil compatible ; aucun n'a été ouvert. C'est le travail de l'étape 6-7 (agent `cartographie-concurrence`).

---

## Rappel de portée

Ce document est **une vérification d'intention, pas un verdict**. Il n'énonce ni GO marché, ni sourcing, ni architecture, ni prix. Il établit un seul fait :

> **Confronté aux pages 1 réelles de Google France, le consolidé de 80 960 perd 14 410 recherches (−17,8 %) et vaut 66 550 recherches mensuelles vérifiées. La réserve de 46 000 sur `planisphère` sort à ~80 % et reste hors total. Une seule famille est retournée par l'étape 5 — `globe interactif`, fermée par VTech, Clementoni et Ravensburger — et elle ne figurait pas dans le total prudent.**

La décision revient à Hakim.
