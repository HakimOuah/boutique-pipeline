# Sourcing configurateur NOIRMONT — pièces, compatibilités, combinaisons ouvrables

Relevés du **27/07/2026** (AliExpress FR/EUR via navigateur intégré, sans session — aucun CAPTCHA rencontré ;
goteia.fr et watchmodcustom.com lus en direct ; catalogues de mod spécialisés lus en web). Chrome était occupé
par l'agent SEMrush : rien n'y a été touché. **Étude seulement** : aucune commande, aucun message vendeur,
aucune modification de la boutique. Les prix et délais AliExpress sont dynamiques et à reconfirmer au panier.

---

## 1. Qui assemble ? — la réponse

**Un fournisseur qui monte à la commande existe, mais il n'est *déclaré* que par un seul vendeur et n'est
prouvé par aucune commande. Ce n'est pas encore un chemin, c'est une piste avec un nom.**

Ce qui est établi, dans l'ordre de solidité décroissante :

1. **BL Watches Parts Store (AliExpress) l'a écrit à Hakim** les 24-25/07 (verbatim archivé dans
   `fournisseurs-reponses-2026-07-24.md`) : « can assemble watch according to your combination », « no seiko,
   no Rolex, no any famous brand logo », « we can assemble more than 100 watches everyday », « bulk order or
   drop shipping all ok ». C'est **la voie 1 du brief, déclarée par écrit** : assemblage libre + stérile garanti
   + dropship à l'unité. Manquent les trois chiffres qui la rendraient exploitable : **prix d'un build
   configuré, délai réel d'un build configuré, catalogue des pièces réellement en stock.**
2. **Aucune fiche AliExpress ne vend un « service d'assemblage »**. Recherche dédiée ce jour
   (`custom assembled nh35 mod watch build service`) : elle ne renvoie que des pièces, des mouvements et des
   **supports de mouvement** (outils de montage). L'assemblage à la config n'est pas un SKU achetable : il
   n'existe qu'en négociation par messagerie vendeur.
3. **Le seul « assemblé à la commande » structuré du marché ne recombine rien** : le bouton « Personnaliser »
   de Corgeut Factory Store (fiches à 361-387 ventes) ajoute **un logo ou un texte** sur un cadran stérile —
   il ne permet pas de choisir cadran × lunette × aiguilles × bracelet. Production 30 j, total 38-51 j.
4. **La montre finie, elle, est un vrai produit dropshippable aujourd'hui** : Corgeut DJ 36/39 cannelée jubilé
   variante **« black no logo »** à **106,99 €** (−6 € dès 55 € ⇒ ≈ 101 €), livrée 4-10 août soit **8-14 j**,
   vendeur 94,5 %, 5,0/5 sur 2 avis, 9 ventes ([1005009697365359](https://fr.aliexpress.com/item/1005009697365359.html)).
   C'est le socle économique — mais c'est un catalogue de variantes, pas un configurateur.

### La contrainte structurelle que personne ne contourne

**Un configurateur dont les options viennent de six vendeurs différents ne peut être assemblé par aucun
d'eux.** Les pièces relevées ci-dessous sont réparties entre Timefront, PORSTIER, Manbushijie, Corgeut,
BL Watches et « NH35 NH36 NH38 VK63 Parts Watch Factory ». Si l'assemblage se fait en Chine, **les options du
configurateur doivent être le stock de l'assembleur, pas notre sélection**. Le sourcing ci-dessous établit
donc ce qui *existe et s'emboîte* ; le catalogue final devra être **celui de BL Watches**, à demander.

### Les trois voies, tranchées

| Voie | Statut | Ce qui la bloque ou la conditionne |
|---|---|---|
| **1. Fournisseur qui monte à la commande** (BL Watches) | **La seule compatible avec notre métier — à instruire en priorité** | Déclarée par écrit, jamais éprouvée. Il faut : catalogue de pièces en stock, prix par build, délai, packaging, traitement d'un défaut. Une commande test d'un build configuré est le seul moyen de la valider. |
| **2. Achat de pièces + assemblage par Hakim** | **Techniquement faisable, économiquement sans intérêt à ce stade** | Les pièces au détail coûtent **108-145 €** (§6) — soit **plus cher que la montre déjà montée à 101-107 €**. On paierait plus cher pour ajouter du travail, de l'outillage (support de mouvement, potence à aiguilles, presse de boîtier), la pose des aiguilles — le geste le plus difficile du modding — et **aucun test d'étanchéité**, donc aucune promesse d'étanchéité possible. À réserver au cas où la voie 1 échoue et où la personnalisation reste l'argument central. |
| **3. Expédition de pièces non montées** | **À écarter** | Le client devrait poser lui-même des aiguilles au centième de millimètre. Ce n'est plus vendre une montre, c'est vendre un kit — le métier de DIY Watch Club, un autre marché, une autre promesse, et un taux de retour qui tuerait la marge. Écarté, comme le brief le supposait. |

### Correction factuelle sur les prix concurrents

Le brief cite « 289 € configurable contre 259 € fixe, prime de 30 € ». **Ce n'est pas ce que les deux sites
affichent aujourd'hui** :

- **goteia.fr** : configurateur **349,00 €** pour les 5 modèles configurables (`basePrice: 34900` dans le
  payload) ; montres fixes **249,00 €** (SeikoJust, SeikoS, SeikoRiner, SeikoNa) et **259,00 €** (SeikoAk,
  SeikoLus), 34 produits. **La prime de personnalisation est de +90 à +100 €, pas de +30 €.** Délai annoncé
  14-20 jours ouvrés en configuré, 2-4 jours en stock. Preuve sociale mince : **9 avis Trustpilot**.
- **watchmodcustom.com** : le **289 €** du brief est leur prix barré sur la « Rose Gold Dayto » (soldée 269 €).
  Leur configurateur démarre lui aussi à **349,00 €**, **plus des suppléments par option** (voir §2).

**Conséquence directe** : la fourchette de prix disponible pour une NOIRMONT configurée est plus large que le
brief ne le supposait. À 299 € on est sous les deux concurrents ; à 349 € on est à leur niveau.

---

## 2. Comment les concurrents résolvent la compatibilité — le modèle à copier

### Goteia : plateforme d'abord, règles purement esthétiques

Le moteur de règles de Goteia est **exposé en clair** dans le payload de la page. Il compte
**8 groupes d'options sur 7 étapes** et **19 règles**, toutes de la forme
`quand groupe A = valeur X, alors groupe B est limité à [valeurs]` :

| Groupe | Options | Règles qui le pilotent |
|---|---:|---|
| `boitier` (cannelé/lisse × 6 finitions) | 12 | — (c'est le déclencheur) |
| `bracelet` (jubilé/oyster/présidentiel × finitions, 9 caoutchoucs, cuir) | 25 | **12 règles** : chaque boîtier n'autorise que 12 à 17 bracelets sur 25 |
| `cadran` | 34 | — |
| `aiguilles` | 9 | — |
| `trotteuse` | 13 | — |
| `date` (loupe cyclope) | 2 | **7 règles** : 7 cadrans (Automatic ×3, Casino, Skeleton ×2, Who Cares) forcent une seule valeur |
| `size` | 2 (36/39 mm) | — |
| `fond-de-boitier` | 2 | — |

**Les deux enseignements sont majeurs :**

1. **Les 12 règles boîtier → bracelet sont des règles de *couleur*, pas de dimension** (« Boîtier Cannelé Or
   Jaune » n'autorise que les bracelets or jaune ou bicolores). Aucune règle dimensionnelle n'existe dans leur
   configurateur.
2. **Les 7 règles cadran → date sont les seules règles techniques** : un cadran sans guichet de date interdit
   la loupe cyclope. C'est exactement le type de règle fonctionnelle qu'il faut encoder.

**Toute la compatibilité dimensionnelle est absorbée en amont par le choix du modèle** (SeikoAk, SeikoJust,
SeikoLus, SeikoNa, SeikoRiner — 5 configurateurs séparés). Le client choisit une plateforme, et la plateforme
fixe le boîtier, le diamètre de cadran, l'entrecorne et le calibre. **C'est le patron d'architecture à
reprendre.**

Combinatoire Goteia SeikoJust : **9,55 M** brut, **≈ 5,08 M** après application des 19 règles
(178 couples boîtier×bracelet × 61 couples cadran×date × 468 pour le reste), **au prix unique de 349 €**.

### WatchModCustom : un seul flux, mais des groupes de bracelets par plateforme

Leur configurateur (`/en/configurator/32-basic-watch.html`) met **32 boîtiers de 10 plateformes différentes
dans un seul flux** (Sub 40, Nautilus, DJ 36, DJ 39, Explorer 36/39, Pilot 38, Engineer 40, Oak 40, PR 40,
Sharp 40, KX), ~80 cadrans, puis inserts, lunette, rehaut (15 finitions), aiguilles, trotteuses, aiguilles GMT,
loupe date, couronne (4), fond, gravure, upload de logo — soit **~14 groupes**.

**Leur solution au problème dimensionnel est structurelle et élégante : il n'y a pas un groupe « bracelet »,
il y a cinq groupes distincts** — `Bracelet 22mm`, `Bracelet Nautilus`, `Bracelet DJ & Explorer`,
`Bracelet Pilot`, **`Bracelet DJ 36`** (2 options seulement). L'entrecorne et le profil de cornes ne sont
jamais laissés au hasard : chaque plateforme porte sa propre liste. **À reprendre tel quel.**

Tarification inverse de Goteia : **349 € de base + suppléments par option** (+29 € carbone forgé, +49/59 €
squelette, +119 € cadran OEM, **+199 € météorite**, +60 € cadran personnalisé, +10 € fond transparent, 9 €
les aiguilles). Assemblage annoncé **1 à 3 semaines**. Leur catalogue de cadrans assume les logos tiers
(« Black Sub SEIKO », « Arabic Ice Blue S Logo », « Rainbow Seiko Day/Date ») — **chasse gardée que NOIRMONT
ne suit pas.**

### « Mod Catalog » : le site n'existe pas sous ce nom

Vérifié : `modcatalog.com` est un catalogue d'applications Android piratées, sans rapport ;
`modcatalog.co`, `themodcatalog.com`, `watchmodcatalog.com`, `modcatalog.net`, `mod-catalog.com` et
`modcatalogue.com` **ne résolvent pas** (aucun DNS). La référence de Hakim renvoie très probablement à l'un
des catalogues de pièces de mod établis, dont voici la taxonomie — **c'est elle qui vaut d'être copiée** :

| Catalogue | Taxonomie | Comment il exprime la compatibilité |
|---|---|---|
| [Crystaltimes USA](https://usa.crystaltimes.net/) | **« Shop By Parts » × « Shop By Model »** (20 plateformes : SKX007/SRPD, SKX013, Turtle, Samurai, Sumo, Monster, SARB033…) | Une page **« Case Dimensions »** : 25 boîtiers × 4 mesures (entrecorne, corne-à-corne, diamètre hors couronne, épaisseur hors fond et lunette). **Ni le diamètre de cadran ni le calibre n'y figurent.** |
| [DLW MODS](https://www.dlwwatches.com/) | Bezel Inserts, Bezels, Cases, Chapter Rings, Crowns, Crystals, Dials, Hands + bracelets **classés par taille (18-22 mm), modèle et matière** | Inserts vendus **par modèle de base** (SKX007/SRPD *Slope* vs *Flat*, SNZF, Turtle, Sumo, Samurai) et renvoi vers un « Case Size Chart ». Aucune cote publiée sur les fiches. |
| [namokiMODS](https://www.namokimods.com/) | Cases/Casebacks, Bezels, Bezel Inserts, Crystals, Dials & Hands, Crowns, Chapter Rings, Bracelets, Tools, Movements | Filtre **par famille de calibre** : « NH35/36 » (53 cadrans, 133 jeux d'aiguilles) vs « NH34 GMT » (3) vs « NH70 Skeleton » (6). **Aucun diamètre d'alésage publié.** |
| [Mod Mode Watches](https://modmodewatches.com/) | **« Shop by Parts » × « Shop by Type » × « Shop by Build »** | « Shop by Type » = catégories de calibre (NH34/4R34, NH35/4R35, NH36/4R36, SKX007/009 Compatible). « Shop by Build » est un **parcours guidé** mouvement → cadrans → aiguilles → verres → lunettes → inserts → bracelets → couronnes → boîtiers. Cadran « 28.5mm Minute Track » vendu tel quel. |

**Le constat qui gouverne tout le reste** : aucun catalogue professionnel du mod ne publie les cotes fines
(alésages d'aiguilles, position des pieds de cadran). **Tous expriment la compatibilité par étiquette de
plateforme et par famille de calibre.** Notre matrice doit faire pareil — pas par déduction dimensionnelle,
mais par **couple (plateforme, calibre) déclaré par le fournisseur**.

---

## 3. Matrice de compatibilité, par calibre et par boîtier

### 3.1 Les six règles, avec leur statut de preuve

| Règle du brief | Ce que les données fournisseur établissent | Statut |
|---|---|---|
| **cadran ↔ mouvement** (diamètre + pieds de cadran) | Le **diamètre est fixé par la plateforme de boîtier**, pas par le calibre : **28,5 mm** (DJ 36/39 et SKX007 42), **31,8 mm** (Oak 41), **29,5 mm** (chrono VK63/64). Sur les **12 cadrans 28,5 mm** relevés, la compatibilité est annoncée « NH35 / NH36 » (parfois + NH34, + 4R, + 7S26) — **aucun ne mentionne le Miyota 8215.** Les pieds de cadran ne sont **jamais** cotés ; ils sont implicites dans l'étiquette de calibre. | ✅ **Établi par étiquette.** ⛔ **Miyota 8215 fermé** : les boîtiers l'acceptent, les cadrans 28,5 mm relevés ne le déclarent pas. Ne pas ouvrir l'axe mouvement au-delà de NH35/NH36. |
| **couronne ↔ position du guichet** *(règle non demandée mais découverte, et c'est le vrai piège)* | Le cadran stérile Manbushijie 28,5 mm est vendu **en deux variantes explicites : « compatible avec une couronne à 3 heures » et « une couronne à 3,8 heures »**. Le boîtier DJ est à 3 h ; le boîtier SKX007 est à ≈ 4 h. Un cadran 3 h dans un boîtier SKX = guichet décalé. | ✅ **Établi, et c'est une règle bloquante** : la variante de cadran dépend de la plateforme de boîtier. |
| **aiguilles ↔ mouvement** (alésages heure/minute/seconde) | **Aucun alésage publié, chez aucun fournisseur** (AliExpress, namoki, DLW, Mod Mode). Les fiches donnent des **longueurs** (`10*14*15 mm`, `8*12*13 mm`, `8*12*12,5 mm`) et une **liste de calibres** — parfois large (« NH35 NH36 PT5000 ETA2836 2824 DG2813 3804 Miyota8215 8205 821A »), parfois étroite (« NH34 GMT »). **Quelle longueur convient à un cadran de 28,5 mm n'est indiqué nulle part.** | ⛔ **Non établi. L'axe aiguilles ne s'ouvre pas.** Soit les aiguilles arrivent **appariées au cadran** (plusieurs fiches vendent le couple), soit **l'assembleur les choisit dans son stock**. C'est l'arbitrage n°1 à obtenir de BL Watches. |
| **insert ↔ lunette** (ø ext. / ø int.) | Coté en clair dans les titres : **38 × 31,5 mm** (inserts *plats*) et **38 × 30,6 mm** (inserts *inclinés / incurvés*) pour boîtiers SKX007/SKX009/SRPD/SUB. Un boîtier relevé annonce « lunette **38 mm × 31,5 mm** ». | ✅ **Établi.** Règle : **le profil de lunette impose le ø intérieur** — plat ⇒ 31,5 ; incliné ⇒ 30,6. **Les deux ne sont pas interchangeables.** ⛔ Sur la plateforme DJ, la lunette (cannelée/lisse) est usinée dans le boîtier : **aucun axe insert**. |
| **cadran + rehaut ↔ boîtier** (ø d'ouverture) | Rehauts SKX007/SKX009/SRPD cotés **30,5 × 27,5 mm** (le plus courant), également **30,3 × 27,4 mm**, et **31,4 / 31,5 mm** annoncés pour « SKX009 / nouveau SRPD ». Un boîtier SKX007 42 mm relevé est vendu **rehaut inclus**, avec « cadran 28,5 mm » et « lunette 38 × 31,5 mm » — la chaîne dimensionnelle complète chez un seul vendeur. | ✅ **Établi pour SKX007** (30,5 × 27,5). ⛔ **Indécidable pour la plateforme DJ** : aucune référence de rehaut DJ trouvée dans cette passe. Pas d'axe rehaut sur DJ. |
| **bracelet ↔ boîtier** (entrecorne) | **20 mm** pour les boîtiers DJ 36/39 et les bracelets « pour DATEJUST / SUB / GMT NH34 NH35 » ; **22 mm** pour SKX007/009. Second critère explicite dans les titres : **extrémité droite vs extrémité incurvée** (« extrémité incurvée », « à extrémités courbes »). | ✅ **Établi.** Règle : entrecorne = plateforme (20 ou 22) **et** les extrémités incurvées ne sont valides que sur le profil de cornes pour lequel elles sont vendues ⇒ **n'ouvrir que les extrémités droites**, sauf paire boîtier+bracelet vendue ensemble. |
| **verre ↔ boîtier** (ø et hauteur) | Verres saphir SKX007/009/SRPD : **ø 31,5 mm, épaisseur 3,5 mm** (plat) ; **31,5 × 5,2 × 2,9 mm** (double dôme). Sur les plateformes DJ **et** SKX relevées, **le verre est fourni avec le boîtier** (« verre saphir » au titre). | ✅ ø établi (31,5 pour SKX). ⛔ **La hauteur acceptée par un boîtier donné n'est jamais publiée** : plat 3,5 vs double dôme 5,2 ne sont pas substituables à l'aveugle. **Pas d'axe verre** — on prend celui du boîtier. |
| **couronne ↔ boîtier** | Exprimée uniquement par modèle (« convient au SKX007 / SKX009 / mouvement NH35 NH36 7S26 »). **Aucun diamètre de tube, aucun filetage de tige publié.** ⚠️ La majorité des couronnes du marché sont **gravées d'un « S »** = logo Seiko non licencié. | ⛔ **Pas d'axe couronne** : dimension non établie **et** risque de marque. Le boîtier arrive avec sa couronne. |

### 3.2 La matrice, plateforme par plateforme

**Plateforme A — DJ 36/39 mm** (cannelée ou lisse, la famille de Goteia SeikoJust)

| Organe | Valeur imposée | Axe ouvrable ? |
|---|---|---|
| Calibre | **NH35** (date à 3 h) — NH36 possible mais exige un cadran jour+date : **1 seule référence relevée** | NH35 seul au lancement |
| Cadran | **ø 28,5 mm**, pieds NH3x, **variante couronne 3 h** | ✅ 11 faces stériles relevées |
| Aiguilles | longueur non publiée | ⛔ appariées au cadran ou choisies par l'assembleur |
| Lunette / insert | usinée dans le boîtier (cannelée / lisse) | ⛔ = choix du boîtier |
| Rehaut | aucune référence DJ trouvée | ⛔ fermé |
| Verre | saphir fourni avec le boîtier | ⛔ fermé |
| Couronne | fournie avec le boîtier | ⛔ fermé |
| Bracelet | **entrecorne 20 mm**, extrémités droites | ✅ 6 modèles |
| Diamètre | 36 / 39 mm | ✅ 2 |
| Fond | verre / plein | ✅ 2 |
| Loupe cyclope | à coller, sans contrainte de cote relevée | ✅ 2 — **valide seulement si le cadran a un guichet date** (règle Goteia à reprendre) |

**Plateforme B — SKX007 42 mm** (plongée)

| Organe | Valeur imposée | Axe ouvrable ? |
|---|---|---|
| Calibre | **NH35** (le boîtier annonce aussi NH36/NH38/4R35/7S26) | NH35 seul au lancement |
| Cadran | **ø 28,5 mm**, **variante couronne 3,8 h** (≈ 4 h) — pas la variante 3 h | ✅ 5 coloris stériles relevés |
| Insert de lunette | **38 × 31,5 mm** si lunette plate, **38 × 30,6 mm** si lunette inclinée — **un seul des deux selon le boîtier** | ✅ ~6 finitions dans le profil retenu |
| Rehaut | **30,5 × 27,5 mm** | ✅ ~5 finitions |
| Verre | saphir ø 31,5 mm fourni avec le boîtier | ⛔ fermé |
| Aiguilles | longueur non publiée | ⛔ appariées / assembleur |
| Bracelet | **entrecorne 22 mm** | ✅ 3 modèles |
| Fond | verre / plein | ✅ 2 |

**Plateforme C — Oak 41 mm** : boîtier **et bracelet intégrés** (donc aucun axe bracelet), NH35/NH36/NH70,
**cadran ø 31,8 mm**, aiguilles incluses, « sans logo », 53,99 €. ⛔ **Aucun cadran 31,8 mm sourcé séparément
dans cette passe ⇒ plateforme non ouvrable** (elle ne servirait qu'un modèle fixe).

**Plateforme D — Chrono VK63/64** : **cadran ø 29,5 mm**, boîtier 12,89 €. ⛔ **Aucun cadran 29,5 mm sourcé
⇒ non ouvrable.** De plus le VK63 est un quartz-méca : la promesse « automatique » tombe.

---

## 4. Les pièces sourcées

Relevés du 27/07/2026 sauf mention « (24/07) » reprise du rapport phase 4c. « Délai » = fenêtre de livraison
affichée pour la France depuis le 27/07.

### Boîtiers

| Pièce | Fiche / vendeur | Prix rendu FR | Délai | Preuve sociale | Cotes annoncées |
|---|---|---:|---|---|---|
| Boîtier DJ or rose 36/39 + bracelet jubilé/huître 316L | [1005009672647007](https://fr.aliexpress.com/item/1005009672647007.html) — Timefront, **95,7 %**, retour gratuit 90 j | **30,39 €** liv. gratuite | 4-10 août (**8-14 j**) | **4,8/5 · 66 avis · 329 vendus** | « pour NH35 NH36 », **cadran 28,5 mm**, 36/39. ⚠️ stock 6 |
| Boîtier DJ cannelé incurvé 36/39 + bracelet + saphir | carte SERP (non ouverte) | 26,59 € | n.c. | 4,8 · **+500 vendus** | « NH35 Datejust **NH36 NH34 Miyota8215** », cadran 28,5 mm |
| Boîtier + bracelet 36/39 saphir | carte SERP | 22,59 € | n.c. | 4,8 · 182 vendus | « NH35 NH36 NH34 **NH70 8215** », cadran 28,5 mm |
| Boîtier DJ lunette cannelée 36/39 saphir | carte SERP | 20,19 € | n.c. | 4,7 · **+5 000 vendus** | « compatible NH35 NH36 » seulement |
| Boîtier SKX007 42 mm saphir **+ rehaut** | [1005012713852445](https://fr.aliexpress.com/item/1005012713852445.html) | non relevé | n.c. | n.c. | « NH35 NH36 NH38 4R35 7S26, **cadran 28,5 mm, lunette 38 mm × 31,5 mm** » |
| Boîtier + bracelet **Oak 41 mm** intégré, sans logo | store [1103720007](https://fr.aliexpress.com/store/1103720007) — NH35/36/38/VK63 Parts Watch Factory, **91,9 %** | 53,99 € | n.c. | 49 vendus | NH35/NH36/NH70, **cadran 31,8 mm**, aiguilles incluses |
| Boîtier chrono style Daytona | même store | 12,89 € | n.c. | 24 vendus | VK63/64, **cadran 29,5 mm** |

### Cadrans

| Pièce | Fiche / vendeur | Prix | Délai | Preuve sociale | Cotes |
|---|---|---:|---|---|---|
| **Cadran stérile 28,5 mm** noir/bleu/rouge/gris/beige, luminescent | [1005010804667820](https://fr.aliexpress.com/item/1005010804667820.html) — Manbushijie | **6,29 €** (liv. gratuite dès 10 €) | 1-5 août (**5-9 j**) | **5,0/5 · 27 avis · 87 vendus** | « NH34 NH35 », **variantes couronne 3 h ET 3,8 h** |
| Cadran stérile 28,5 mm texture Ocean, BW9/C3, calendrier simple | [1005012697064876](https://fr.aliexpress.com/item/1005012697064876.html) | non relevé | n.c. | n.c. | NH35/NH36 |
| Cadran stérile arabe 28,5 mm | [1005012130205925](https://fr.aliexpress.com/item/1005012130205925.html) | ~8-13 € (24/07) | n.c. | récent | « for NH36 movement » |
| Cadran vierge brossé 28,5 mm, sans lume | [1005012416011726](https://fr.aliexpress.com/item/1005012416011726.html) | non relevé | n.c. | n.c. | NH35 |
| **Cadran + aiguilles** appariés 28,5 mm (« who cares ») | [1005010285476501](https://fr.aliexpress.com/item/1005010285476501.html) | non relevé | n.c. | n.c. | « aiguilles NH34 NH35 NH36 » — **couple garanti** |
| **Cadran texturé + aiguilles** 28,5 mm | [1005011916523734](https://fr.aliexpress.com/item/1005011916523734.html) | non relevé | n.c. | n.c. | NH35/NH36 — **couple garanti** |
| Cadran arabe bleu ciel sunburst **+ aiguilles** 28,5 mm | [1005009751528666](https://fr.aliexpress.com/item/1005009751528666.html) | non relevé | n.c. | n.c. | NH35/NH36/4R — **couple garanti** |
| Cadran jour+date 28,5 mm (pour NH36) | [1005012203820696](https://fr.aliexpress.com/item/1005012203820696.html) | non relevé | n.c. | n.c. | NH35/NH36 — **la seule référence jour+date relevée** |
| ⚠️ Cadrans arabes **siglés « Logo S »** | 1005009469054356 (313 vendus, 4,79 €), 1005010096442147, 1005012549490372, 1005012213245310 | 2,21-15,19 € (24/07) | — | jusqu'à 313 vendus | **Contrefaçon probable — documentés, jamais vendus** |

### Aiguilles

| Pièce | Fiche | Cotes annoncées | Compatibilité déclarée |
|---|---|---|---|
| Aiguilles polies Dauphine | [1005007896534058](https://fr.aliexpress.com/item/1005007896534058.html) | **10 × 14 × 15 mm** (longueurs) | NH35 / NH38 |
| Aiguilles argent/or/vintage | [1005009426116839](https://fr.aliexpress.com/item/1005009426116839.html) | **8 × 12 × 13 mm** | NH35 NH36 4R 7S |
| Aiguilles bâton style Datejust, C3 | [1005007884473587](https://fr.aliexpress.com/item/1005007884473587.html) | **8 × 12 × 12,5 mm** | NH35 / NH36 |
| Aiguilles argent/bleu multi-calibres | [1005012517007454](https://fr.aliexpress.com/item/1005012517007454.html) | — | NH35 NH36 PT5000 ETA2836/2824 DG2813 3804 **Miyota8215/8205/821A** |
| Jeu style Datejust + trotteuses couleur (24/07) | SERP `royal oak nh35` | — | 3,69-4,39 €, 110-122 vendus, 4,8-4,9 |

**Aucune de ces fiches ne publie d'alésage.** Les longueurs varient de 8×12×12,5 à 10×14×15 mm sans que le
diamètre de cadran cible soit précisé.

### Inserts, rehauts, verres, couronnes, bracelets, loupes

| Famille | Références | Prix | Cotes annoncées |
|---|---|---:|---|
| **Insert céramique plat** | [1005010035549860](https://fr.aliexpress.com/item/1005010035549860.html), [1005007018344494](https://fr.aliexpress.com/item/1005007018344494.html) | non relevé | **38 × 31,5 mm** — SKX007/009/SRPD, NH35/NH36 |
| **Insert céramique incliné/incurvé** | [1005009604722736](https://fr.aliexpress.com/item/1005009604722736.html), [1005007492125284](https://fr.aliexpress.com/item/1005007492125284.html), [1005012330784890](https://fr.aliexpress.com/item/1005012330784890.html) | non relevé | **38 × 30,6 mm** |
| Insert céramique incurvé (meilleure preuve sociale, 24/07) | [1005007293732155](https://fr.aliexpress.com/item/1005007293732155.html) | **6,99 €** | **4,9/5 · 373 vendus** — SKX007/009 GMT SUB, NH35/NH36 |
| **Rehaut (chapter ring)** | [1005008698824504](https://fr.aliexpress.com/item/1005008698824504.html), [1005010153601813](https://fr.aliexpress.com/item/1005010153601813.html), [1005008279845538](https://fr.aliexpress.com/item/1005008279845538.html) | non relevé | **30,5 × 27,5 mm** (aussi 30,3 × 27,4) — SKX007/009/SRPD |
| Rehaut « SKX009 / nouveau SRPD » | [1005007089052320](https://fr.aliexpress.com/item/1005007089052320.html), [1005009745748682](https://fr.aliexpress.com/item/1005009745748682.html) | non relevé | **31,4 / 31,5 mm** — ⚠️ **pas interchangeable avec 30,5** |
| **Verre saphir plat** | [1005007670953344](https://fr.aliexpress.com/item/1005007670953344.html) | non relevé | **ø 31,5 mm, ép. 3,5 mm** — SKX007/009/SRPD |
| **Verre saphir double dôme** | [1005005396411799](https://fr.aliexpress.com/item/1005005396411799.html) | non relevé | **31,5 × 5,2 × 2,9 mm**, AR bleu/rouge |
| **Couronnes** | [1005004267376427](https://fr.aliexpress.com/item/1005004267376427.html), [1005010267854902](https://fr.aliexpress.com/item/1005010267854902.html) | non relevé | « SKX007/009, NH34/35/36/4R/7S26 » — **aucune cote**. ⚠️ nombreuses variantes gravées « S » |
| **Bracelet jubilé 20 mm** 316L fermoir coulissant | [1005008728294161](https://fr.aliexpress.com/item/1005008728294161.html) — vendeur 95,3 %, **4,6/5 · 7 avis · 53 vendus**, livré 4-10 août | **27,59 €** | 20 mm, « datejust Sub gmt NH34 NH35 » |
| Bracelet jubilé extrémité incurvée (24/07) | [1005008857791659](https://fr.aliexpress.com/item/1005008857791659.html) — 4,7 · **+800 vendus** | 6,79 € | 20 mm — ⚠️ **extrémité incurvée** |
| Bracelet massif 18-24 mm (24/07) | [1005008811155500](https://fr.aliexpress.com/item/1005008811155500.html) — 4,5 · **+3 000 vendus** | 6,99 € | 18-24 mm, « Seiko SKX / jubilé » |
| Bracelet jubilé 904L (24/07) | [1005008516568536](https://fr.aliexpress.com/item/1005008516568536.html) — 4,8 · 122 vendus | 12,59 € | 20 mm |
| Bracelet 20 mm présidentiel 904L glide lock | [1005010566768951](https://fr.aliexpress.com/item/1005010566768951.html) | non relevé | 20 mm, « Sub Log NH34 NH35 » |
| Bracelet acier SKX007/009 | [1005012768764252](https://fr.aliexpress.com/item/1005012768764252.html) | non relevé | **20 et 22 mm**, oyster ou jubilé incurvé |
| **Loupe cyclope** à coller (24/07) | [1005011940440567](https://fr.aliexpress.com/item/1005011940440567.html) (4,9 · 124 vendus) · [1005007361555028](https://fr.aliexpress.com/item/1005007361555028.html) (4,9 · 135 vendus) | 2,47 € · 4,29 € | bulle saphir 10 × 5 mm |

### Mouvements

| Pièce | Fiche | Prix | Délai | Preuve sociale |
|---|---|---:|---|---|
| **NH35A** original Japon, 24 rubis, date à 3:00 | [1005008494235697](https://fr.aliexpress.com/item/1005008494235697.html) — vendeur **98,4 %** | **62,69 €** (−2 % dès 3 pièces) | 4-10 août (**8-14 j**) | **4,9/5 · 719 avis · +5 000 vendus** |
| NH35 « authentique », haute précision | [1005005597724853](https://fr.aliexpress.com/item/1005005597724853.html) | 69,39 € | n.c. | 4,9 · **+10 000 vendus** |

### Montre finie (repère voie 1)

| Pièce | Fiche | Prix | Délai | Preuve sociale |
|---|---|---:|---|---|
| DJ 36/39 cannelée jubilé saphir 10 bar, variante **« black no logo »** | [1005009697365359](https://fr.aliexpress.com/item/1005009697365359.html) — Corgeut, 94,5 %, 8 231 abonnés | **106,99 €** (−6 € dès 55 € ⇒ ≈ **101 €**) | 4-10 août (**8-14 j**) | 5,0/5 · 2 avis · 9 vendus. Variantes : 36/39 × fond verre/plein |

---

## 5. Combien de combinaisons sont réellement ouvrables

Calcul sur les seules cotes établies au §3, **aiguilles comptées pour 1** (elles sont appariées au cadran ou
choisies par l'assembleur) :

**Plateforme A — DJ 36/39, calibre NH35**
`2 diamètres × 2 fonds × 11 faces de cadran stériles 28,5 mm/couronne 3 h × 6 bracelets 20 mm à extrémités droites × 2 (avec/sans loupe) × 1 jeu d'aiguilles`
= **528 combinaisons**

**Plateforme B — SKX007 42 mm, calibre NH35**
`2 fonds × 5 faces de cadran 28,5 mm/couronne 3,8 h × 6 inserts (dans le profil de lunette du boîtier) × 5 rehauts 30,5 × 27,5 × 3 bracelets 22 mm × 1 jeu d'aiguilles`
= **900 combinaisons**

**Total ≈ 1 428 combinaisons réellement ouvrables**, dont **528 immédiatement**, la plateforme B supposant de
confirmer le profil de lunette du boîtier retenu.

Ordre de grandeur, pas chiffre gravé : il est dérivé des références vues **ce jour** et **devra être refait
sur le catalogue de l'assembleur** (§1). À comparer aux **≈ 5,08 M** combinaisons que Goteia affiche — dont
la quasi-totalité ne repose sur aucune règle dimensionnelle. **Notre 1 428 est petit et montable ; leur 5 M
est grand et non vérifié.** C'est exactement le renversement d'argument à tenir : *« chaque combinaison que
nous proposons a été montée »*, pas *« nous avons plus de choix »*.

Et 1 428 reste **hors de portée du client** : à 8 secondes par option, personne n'explore 1 428 montres. Le
vrai sujet de conception n'est pas d'ouvrir plus, c'est de **guider** — comme Mod Mode Watches avec son
parcours « Shop by Build ».

---

## 6. Prix de revient d'une montre configurée

| Voie | Détail | Coût rendu | Face à Goteia 349 € |
|---|---|---:|---:|
| **1. Assembleur (BL Watches), estimation** | La montre finie comparable est à **101-107 €**. Un build à combinaison libre coûtera au moins autant, plus les pièces non standard. **Prix non obtenu du fournisseur** ⇒ estimation prudente **100-135 €** | **100-135 €** *(estimé)* | marge brute **214-249 €** |
| **2. Pièces au détail + assemblage Hakim** | boîtier 26,59-30,39 € (verre + couronne + parfois bracelet inclus) + cadran 6,29-13 € + aiguilles 3,69-6,69 € + bracelet 6,79-27,59 € + **NH35 62,69 €** + loupe 2,47-4,29 € | **108,52-144,65 €** | marge brute **204-240 €** **avant** outillage, temps de montage, absence de test d'étanchéité, garantie et SAV |
| **Repère marché** | Goteia : **349 €** configuré / **249-259 €** fixe · WatchModCustom : **349 € + suppléments** (jusqu'à +199 €) / **269-399 €** fixe | — | — |

**Trois lectures :**

1. **Acheter les pièces coûte plus cher que la montre montée** (108-145 € contre 101-107 €). L'assemblage
   chinois est moins cher que la somme des pièces au détail — ce qui confirme la logique économique de la
   voie 1 et retire tout intérêt de court terme à la voie 2.
2. **Le mouvement pèse à lui seul 43 à 58 % du coût des pièces** (62,69 € sur 108-145 €). C'est là que se
   joue la marge de la voie 2, pas sur les cadrans à 6 €.
3. **À 349 €, la marge brute reste de ~215-250 €**, soit ~62-71 %. Le brief craignait une prime de
   personnalisation de 30 € ; la réalité du marché est de **+90 à +100 €** sur le prix fixe. Un positionnement
   à **299 €** placerait NOIRMONT sous les deux concurrents en configuré tout en conservant ~165-200 € de
   marge brute.

---

## 7. Ce qui est indécidable, et pourquoi

Chacun de ces points est **une combinaison qu'on n'ouvre pas** tant qu'il n'est pas levé.

| Indécidable | Pourquoi | Ce qui le lèverait |
|---|---|---|
| **Alésages des aiguilles** (canons heure/minute/seconde) | **Aucun fournisseur ne les publie** — ni AliExpress, ni namokiMODS, ni DLW, ni Mod Mode Watches. La compatibilité n'est donnée que comme liste de calibres. | Rien sur le web. **Il faut le catalogue d'aiguilles de l'assembleur** ou une mesure sur échantillon. En attendant : aiguilles appariées au cadran. |
| **Longueur d'aiguilles adaptée à un cadran de 28,5 mm** | Les fiches annoncent 8×12×12,5, 8×12×13 et 10×14×15 mm **sans jamais dire pour quel diamètre de cadran**. Une trotteuse trop longue dépasse la piste des minutes. | Achat des couples cadran+aiguilles déjà appariés, ou arbitrage de l'assembleur. |
| **Pieds de cadran, position exacte** | Jamais cotés. L'étiquette « NH35/NH36 » en tient lieu. Les sources communautaires indiquent que **NH35 et Miyota 8215 ont des positions de pieds différentes** et un guichet de date à une distance différente du centre — mais **ce n'est pas une donnée fournisseur** et je ne l'utilise pas comme règle. | La règle opérationnelle suffit : **n'ouvrir que les calibres explicitement listés par le vendeur du cadran** ⇒ NH35/NH36 seulement, jamais 8215. |
| **Hauteur de verre acceptée par un boîtier** | Le même ø 31,5 mm existe en 2,9 / 3,5 / 5,2 mm de hauteur. Aucun boîtier n'annonce la hauteur qu'il accepte. | Non nécessaire : le verre vient avec le boîtier. **Pas d'axe verre.** |
| **Couronne ↔ tube de boîtier** (ø, filetage de tige) | Aucune cote publiée, uniquement « convient au SKX007 ». S'ajoute le risque de marque : la plupart sont gravées « S ». | **Pas d'axe couronne.** |
| **Rehaut pour la plateforme DJ** | Tous les rehauts trouvés sont SKX007/009/SRPD. Aucun rehaut DJ dans cette passe. | Recherche dédiée, ou le catalogue de l'assembleur. |
| **Cadrans ø 31,8 mm (Oak) et ø 29,5 mm (chrono)** | Les boîtiers existent et annoncent la cote ; **aucun cadran de ces diamètres n'a été sourcé séparément**. | Ces deux plateformes restent **non configurables** — modèles fixes seulement. |
| **Prix, délai et catalogue d'un build configuré chez BL Watches** | Déclaration écrite d'assemblage, **sans aucun chiffre**. | Message vendeur (Hakim) puis **une commande test d'un build configuré**. C'est le prochain jalon décisif du projet. |
| **Distinction plat / incliné du boîtier SKX retenu** | Le ø intérieur d'insert (31,5 vs 30,6) en dépend entièrement. | Lire la cote de lunette sur la fiche du boîtier exact retenu (l'une la publie : « 38 mm × 31,5 mm »). |
| **Ce que reçoit réellement le client** (stérile vs logoté) | Photos d'avis non extraites ; les vendeurs euphémisent (« Logo S »). Reste vrai depuis la phase 4b. | Contrôle visuel Hakim + commande test. |

---

## 8. Recommandation de conception, si le configurateur se fait

1. **Plateforme d'abord** — un configurateur par famille de boîtier, comme les 5 configurateurs de Goteia.
   La plateforme fixe le diamètre de cadran, la position de couronne, l'entrecorne et le calibre. C'est ce qui
   rend inutile toute règle dimensionnelle côté client.
2. **Un groupe de bracelets par plateforme et par diamètre**, à la manière de WatchModCustom
   (`Bracelet DJ & Explorer`, `Bracelet DJ 36`, `Bracelet 22mm`) — jamais une liste globale.
3. **Deux règles fonctionnelles à encoder**, les seules qui soient techniques :
   `cadran sans guichet date ⇒ loupe cyclope indisponible` (la règle de Goteia) et
   `plateforme ⇒ variante de cadran couronne 3 h ou 3,8 h`.
4. **N'ouvrir aucun axe aiguilles** avant d'avoir le catalogue de l'assembleur. Le vendre comme un parti pris :
   *« les aiguilles sont choisies pour le cadran »*.
5. **Zéro pièce siglée** — ni cadran « Logo S », ni couronne gravée « S ». C'est la ligne NOIRMONT, et c'est
   aussi le seul point où les deux concurrents sont attaquables : Goteia affiche des cadrans siglés dans sa
   preview, WatchModCustom vend explicitement des cadrans « SEIKO » et « S Logo ».
6. **Ne rien promettre sur l'étanchéité** : aucune montre configurée ne sera testée. Les boîtiers annoncent
   « 10 bar » / « étanche » — c'est une **spec fournisseur**, pas une mesure, et l'ouverture du boîtier pour
   changer un cadran invalide de fait le joint d'origine.

---

*Rapport du 27/07/2026. Aucun GO. Aucune commande. La faisabilité du configurateur repose entièrement sur une
information encore manquante : le catalogue, le prix et le délai d'un build configuré chez BL Watches Parts
Store.*
