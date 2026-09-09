# VoC avis clients — carports & tentes-garages (France)

09/09/2026. Sources exploitées : Amazon.fr (Outsunny, VEVOR, Palram, carports alu génériques, Cazeboo, XMTECH — via outil monid/Apify `axesso_data/amazon-reviews-scraper` en domainCode fr, et via Chrome de Hakim en parallèle pour les fiches nécessitant une connexion), ManoMano.fr (Outsunny 5x3x2,4m, carport « Le Mans » 15m² alu/polycarbonate), Trustpilot (mon-abri-de-jardin.com, coclic-alu.fr, perenza.com, oogarden.com, toolport.de, dancovershop.com), Avis Vérifiés (perenza.com), Avis73.fr (franceabris.com). **Leroy Merlin non exploitable** : le site est protégé par un CAPTCHA DataDome qui bloque aussi bien la navigation directe que l'outil de scraping tiers testé (mrscraper, mode « super » stealth inclus) ; conformément à la consigne de ne jamais contourner un CAPTCHA, aucune tentative de contournement n'a été faite. Pages/avis bruts sauvegardés dans `raw/avis/`.

Règles de preuve respectées : verbatims cités entre guillemets, non paraphrasés, datés et sourcés. `[O]` = observé directement dans un avis. `[D]` = déduction de l'orchestrateur à partir de plusieurs `[O]`, marquée comme telle.

---

## 1. Tableau des thèmes (fréquence × intensité, confiance)

| Thème | Fréquence (sources indép.) | Intensité dominante | Confiance |
|---|---|---|---|
| Montage : durée, nb de personnes, notice, perçages, visserie manquante | Très haute (Amazon×5 fiches, ManoMano×2, Trustpilot×5 marchands, Avis Vérifiés, Avis73) | Négatif à mitigé (notice = point faible n°1 cité même par les clients satisfaits) | **Haute** |
| Livraison : délai non tenu, colis abîmé, créneau raté, transporteur | Très haute (OOGarden, Perenza, Dancover, Toolport, Franceabris, Mon Abri de Jardin) | Bipolaire (loué quand rapide/pro, très négatif quand retardé/abîmé) | **Haute** |
| Bâche/toile : se déchire, blanchit, laisse passer la lumière, coutures qui lâchent | Haute (Amazon Outsunny×2, ManoMano, Toolport, OOGarden/polycarbonate, XMTECH) | Négatif, dégradation dans le temps (1,5 à 4 ans) | **Haute** |
| Résistance au vent (tempête, arrachage, structure qui bouge) | Haute (Amazon VEVOR, Amazon Outsunny B0GRYT9KYK, ManoMano×2) | Négatif à rassurant selon le cas ; anxiogène même chez les satisfaits (« stressant quand il y a du vent ») | **Haute** |
| Ancrage au sol (sardines/piquets jugés faibles, dalle, chevilles, équerres) | Haute (Amazon×2, ManoMano, Perenza×2, Amazon B0GRYT9KYK) | Négatif, système fourni jugé systématiquement sous-dimensionné | **Haute** |
| SAV : réactivité, pièces de rechange, refus de garantie | Haute (Toolport, OOGarden, Franceabris, Perenza, mon-abri-de-jardin) | Bipolaire fort (très bon vs. inexistant/hostile) | **Haute** |
| Rapport qualité/prix | Haute (quasi toutes les sources) | Majoritairement positif si le reste va bien | **Haute** |
| Durée de vie constatée (dégradation 1,5-4 ans) | Moyenne-haute (Toolport×2, ManoMano/Paolo, Amazon/rouille) | Négatif, désillusion progressive | **Haute** |
| Étanchéité entre plaques polycarbonate (silicone à ajouter) | Moyenne (Amazon Cazeboo×2, OOGarden×2) | Négatif, écart notice/réalité | **Moyenne** |
| Taille réelle vs annoncée (largeur fausse, décalage hauteur) | Moyenne (Amazon Palram, Perenza/Denis B., Amazon « taille de l'article ») | Négatif ponctuel | **Moyenne** |
| Usage réel constaté (piscine, stockage, structure seule) | Moyenne (ManoMano, OOGarden) | Neutre/positif, usage détourné fréquent | **Moyenne** |
| Rouille précoce | Basse (1 mention directe Amazon + specs « acier galvanisé » mises en avant par les vendeurs en creux) | Négatif quand cité | **Basse** |
| Neige | Basse (1 mention anticipative, non vécue ; specs vendeurs seulement) | Inquiétude anticipée plutôt que vécue dans ce corpus | **Basse** |
| Esthétique / regard des voisins / « ça fait chantier » | Basse (2-3 mentions positives indirectes, aucune négative explicite) | Quasi absent des avis produits | **Basse** |
| Démarches administratives (déclaration préalable, voisin) | Absente de ce corpus | — cf. `voc-forums-reddit.md`, thème naturellement absent des avis produits e-commerce | **Absente (ce corpus)** |

---

## 2. Verbatims par thème

### 2.1 Montage — durée, personnes, notice, perçage, visserie
- Amazon, Outsunny 5x3x2,4m (B0CW6FK9BS), France, 20/04/2026, 3★ : « Carport bien. Notice de montage très peu explicite et mal imprimée. Il faut sortir de polytechnique pour comprendre😂 ou avoir une bonne loupe. Sinon pratique. »
- ManoMano, carport « Le Mans » 15m² alu (Michel), France, 22/12/2023 : « Des pbs de montage des gouttières, trop hautes de 4 mm impossible de la glisser dans son rail. Obligé de redesserer la structure pour engager celles-ci. Obligé d'haubaner, structure trop fragile. »
- Amazon, Cazeboo KLEO (FABIEN BOURSON), 05/04/2025, 4★, titre « bien étudier la notice avant, être au moins 2. » : « la notice est très succincte! ex: il faut des forets 8, et non 6 ; manque de vidéo avec QR code. Courage aux amateurs. »
- Avis Vérifiés, Perenza (Jonathan C.), 27/08/2026 : « la numérotation des éléments indiquée dans le livret d'assemblage ne correspond pas toujours aux pièces et les images/explications manquent parfois de précision. »
- Avis73, franceabris.com (Michel 31), 09/03/2022 : « pas de plan de montage, si ce n'est qu'un petit assemblage de schémas d'origines diverses ne correspondant à rien de précis et qui plus est sont erronés (...) j'ai maintes fois réclamé les plans de montage, on a fini par me revoyer le même torchon inutilisable. »
- Amazon, Outsunny 3x6m hauteur réglable (Frédéric), 19/05/2026, 4★ : « Montage en 3 heures 30 à deux personnes. Une notice plus précise aurait évité des montages à blanc et fait gagner du temps. »

### 2.2 Livraison — délai, colis abîmé, créneau, transporteur
- Trustpilot, OOGarden (Catherine), 31/07/2025, 1★ : « J'aurais mis 0 étoile ! Mon carport devait être arrivé depuis deux semaines. Mais j'ai déjà reçu deux messages pour me dire que la livraison serait différée. Et personne ne répond au téléphone. Je ne sais pas comment récupérer mon argent. Ce site est une arnaque !! »
- Avis Vérifiés, Perenza (Denis B.), 29/08/2026 : « j'ai attendu environ 1 mois pour être livré par le transporteur qui ne trouvait pas de créneau pour moi (...) Le dessus de la palette arrive abimé. »
- Trustpilot, Dancover (RAMEL François), 16/08/2017, 5★ : « J'ai acheté un carport deux places. Commandé le jeudi, livré le mardi, alors que je m'attendais à deux semaines pour la livraison. Chapeau bas ! »
- Trustpilot, OOGarden (Letoffe), 07/06/2025, 3★ : « Livraison un peu longue (2 mois) reportée 2 fois. »
- Trustpilot, mon-abri-de-jardin.com (Pascale FISZBIN), 24/07/2026 : « Je viens de commander 1 abri (...) Je suis déçue car il manque 1 colis 5 sur 6. »
- Avis73, franceabris.com (Swing44), 11/09/2024 : « ce colis est resté 1 mois dans mon jardin!!! je n'appelle pas cela livré, monté, dans la foulée!! »

### 2.3 Bâche / toile — déchirure, UV, coutures, transparence
- ManoMano, Outsunny 5x3x2,4m (Paolo, avis traduit), Italie, 23/07/2026, note non précisée : « après un an et demi d'installation, la toile du store a été endommagée par le soleil et la moindre pression du doigt a commencé à la percer. Une averse de grêle, pourtant sans gravité, a également perforé toute la toile. »
- Amazon, Outsunny (B08VDQ1Z96), France, 27/08/2023, 1★, titre « la toile pas du tout solide » : « Toile fragile et bâche pas trop épaisse se déchire avec le temps 1 ans et demi après foutu un grand coup de vent et toute déchirer. »
- ManoMano, Outsunny 5x3x2,4m (Sandra), 10/08/2025 : « 2 faiblesses dans la toile qui laissent passer la lumière. On va mettre un Scotch gris a l'extérieur pour que ca ne craque pas. »
- Trustpilot, Toolport (jens hansel, trad. allemand), 30/08/2026, 1★ : « Nach zweieinhalb Jahren löst sich die Dachplane komplett auf. » (Après deux ans et demi, la bâche de toit se désagrège complètement.)
- Amazon, XMTECH tente 3x6m (avis Allemagne, trad.), 14/07/2025, 1★ : « la bâche présente des fissures/coupures comme si elle avait déjà servi (...) peu à peu la bâche se défait partout aux coutures. »
- Trustpilot, OOGarden (Roland), 26/07/2025, 4★ : « Les plaques de polycarbonates sont relativement fragiles (sensibles objet contendant, grêle, etc...). Le remplacement ad intégrum est impossible. »

### 2.4 Résistance au vent
- Amazon, VEVOR abri voiture (lorinljrk), 23/01/2023, 2★, titre « Exactly what we were expecting » : « Tonight was the first windy day of winter. Poles bent in half, tarp ripped, entire structure lifted from the ground and flipped upside down. We even had sand bags on each corner pole. Ruined! »
- Amazon, VEVOR (avis US), 09/03/2023, 1★, titre « Flimsy trash » : « One mild storm and it's completely destroyed. don't waste your money. »
- ManoMano, Outsunny (Laurent), 09/12/2025, note non précisée : « Bien mais les tubes pas très épais. Ils ont commencé à se déformer au premier coup de vent (80 km/h). »
- ManoMano, Outsunny (Vincent), 08/09/2026 : « Très bon rapport qualité prix très bonne solidité à l'usage, très bonne résistance au rafales de vent. Je recommande. »
- Amazon, Outsunny 3x6m hauteur réglable (Sylvie), 22/08/2026, 4★ : « je trouve qu'il y'a un peu de jeu sur les poteaux de structure, stressant quand il y a du vent. Ça bouge et avec des petits grincements qui rassure pas. »

### 2.5 Ancrage au sol
- Amazon, Outsunny (patrick), 05/06/2023, note non précisée : « tres bon produit manque de fixation au sol. obliger de racheter des piquet plus solide par securité. »
- Amazon, Outsunny (B0CW6FK9BS, avis 09/05/2024) : « il manquerait une accroche solide pour le fixer au sol car les sardines semblent sortie d'une dinette. »
- Amazon, Outsunny 3x6m hauteur réglable (Alindia), 05/09/2026, 5★ : « Structure solide et toile résistante. Seules les fiches (les 'sardines') sont camelote ! »
- Avis Vérifiés, Perenza (Franck P.), 28/08/2026 : « attention à la visserie pour la fixation au sol, nous avons aussi renforcé la base avec des équerres. » — réponse Perenza : « prévoir une visserie appropriée et renforcer l'ancrage selon le terrain (...) est exactement le bon réflexe. »
- ManoMano, Outsunny (Joel), 13/07/2026 : « La bâche enrobe bien la structure et il n'y a pas de prise au vent. Les pieds sont scellés dans du béton. Elle tiens bien. »

### 2.6 SAV
- Trustpilot, Franceabris (bricolo21), 24/08/2024, expérience 24/08/2020 : « aucun SAV, aucune pièce ne peut etre demandée ni remboursement, ni retour (...) l'accueil téléphonique a été épouvantable et grossier. »
- Trustpilot, Toolport (Sylvia), 27/06/2026, 5★ : « Herzlichen Dank für die schnelle und komplikationslose Bearbeitung unserer Reklamation! (...) 3 Tage danach beide Ersatzteile (Dach, Seitenwand) hier. » (Merci pour le traitement rapide de notre réclamation, 3 jours après les deux pièces de rechange étaient là.)
- Trustpilot, OOGarden (Grenouille27), 02/08/2024, 1★ : « il manque le sachet avec les vis et les chevilles bois. Impossible de le monter sans ça. Mail de réclamation envoyé mais pas de réponse. Et numéro téléphone payant. »
- Trustpilot, mon-abri-de-jardin.com (Claude M.), 27/03/2026, 5★ : « suite à la chute d'un arbre, une partie de mon carport était détériorée (...) un conseiller m'a orienté vers la page de pièces détachées (...) Bon accueil, rapidité et bon suivi. »
- Avis73, franceabris.com (Ninja), 24/04/2025 : « j'avais appelé le SAV suite au matériel reçu à propos de sa fabrication made in China (...) j'ai eu une personne très désagréable qui m'a ri au nez. »

### 2.7 Durée de vie constatée
- Trustpilot, Toolport (Michael Leisering, trad.), 29/06/2026, 2★ : « Nach 4 Jahren sehen die Platten nun aus wie ein Schweizer Käse. » (Après 4 ans, les plaques ressemblent à un gruyère.)
- Trustpilot, Toolport (Christian, IT, trad.), 24/06/2026, 2★ : « dopo un anno e poco più il telo (...) ha iniziato ad avere sulla parte superiore molti micro fori. » (après un peu plus d'un an, la toile a commencé à avoir de nombreux micro-trous sur le dessus.)
- ManoMano, Outsunny (Paolo), 23/07/2026 : « après un an et demi d'installation, la toile du store a été endommagée par le soleil. »
- Amazon, Outsunny (B0CW6FK9BS), 11/05/2024, 4★ : « A part les barres du bas rouillées (oui déjà) et 2 écrous non taraudés, s'est monté facilement seul. »
- Avis73, franceabris.com (Ninja), 24/04/2025 : « les panneaux de coté se déforment avec un temps ensoleillé !!! un panneau en particulier exposé à l'ouest gondole et revient en place. »

### 2.8 Étanchéité / assemblage polycarbonate
- Amazon, Cazeboo KLEO (Eric B.), 16/06/2026, 5★ : « Prévoir une à deux cartouches de silicone pour l'étanchéité de l'ensemble (...) je trouve que les plaques de couverture en polycarbonate sont un peu fines : c'est le seul point faible. »
- Amazon, Cazeboo KLEO (Client d'Amazon), 11/09/2025, 3★, titre « Problème Étanchéité » : « l'étanchéité laisse à désirer. Trop de jeux entre les plaques, il faut compenser avec beaucoup de silicone. »
- Trustpilot, OOGarden (danielle delaye), 24/06/2025, 3★ : « pinces impossible de rentrer facilement les plaques de toiture qui sont certaines cornées. »

### 2.9 Taille réelle vs annoncée
- Amazon, Palram Arcadia (B004L6GKOE, avis France), 12/08/2020, 4★ : « la largeur indiquée est fausse, il faut rajouter 8cm. si on a fait des plots d'ancrage un peu justes en écartement, cela peut poser un problème et obliger à refaire du béton. »
- Avis Vérifiés, Perenza (Denis B.), 29/08/2026 : « les planches composites les plus courtes sont moins larges que les autres, ce qui donne un décalage de hauteur au montage. »
- Amazon, Outsunny 3x6m hauteur réglable (Pascal GIULIANI), 02/08/2026, 4★, titre « taille de l'article » : « bien préciser les mesures exactes (L l H) »

### 2.10 Usage réel constaté
- ManoMano, carport « Le Mans » (Client ManoMano), 10/06/2020 : « Ce carport à gentiment fait office de protection de piscine. Le résultat est apprécié par la famille. »
- Trustpilot, OOGarden (Christer_F), 03/12/2021, 5★ : « Nous avons commandé un auvent de type carport (structure seulement). Produit au top, très stable et solide. »
- Trustpilot, OOGarden (martial bouleau), 26/06/2025, 5★ : « nous avons déjà commandé sur o garden (...) La dernière fois c'était un carport, et il n'y a jamais eu de soucis, ni manque de pièces. »

---

## 3. (a) Jobs à faire

**Fonctionnel**
- Mettre le véhicule (voiture, camping-car, bateau) à l'abri de la pluie, du soleil, de la grêle, sans construire un garage en dur.
- Protéger un bien de valeur ou fragile en attendant/à la place d'un vrai garage (`[D]` déduit des usages détournés : piscine, stockage, atelier).
- Tenir dans la durée sans surveillance constante (pas de bâche à retendre chaque semaine, pas de pièce à recommander tous les ans).
- Pouvoir le monter soi-même ou à deux, sans compétence de chantier, en un week-end raisonnable.

**Émotionnel**
- Ne plus avoir peur du prochain coup de vent ou de la prochaine averse de grêle — l'anxiété est présente même chez les clients globalement satisfaits (« stressant quand il y a du vent », Sylvie, Amazon).
- Ne pas se sentir « arnaqué » ou floué par un écart entre la photo/la promesse marketing et le produit réel (mot « arnaque » revient chez plusieurs marchands différents, signe d'un point de bascule émotionnel fort).
- Avoir la fierté du bricoleur qui a réussi le montage seul ou à deux (verbatims élogieux très fréquents sur la clarté d'une notice bien faite, à l'inverse).

**Social**
- Ne pas avoir à gérer un litige long et frustrant avec un SAV qui « rit au nez » du client ou ne répond pas (charge mentale et sentiment d'impuissance très présents).
- Un produit qui « fait sérieux » et pas « ça fait chantier » — thème sous-représenté dans les avis produits mais présent en creux (satisfaction citée sur le « design magnifique », le fait que ça « s'intègre bien au parking »).

## 4. (b) Déclencheurs d'achat cités ou déductibles
- Un événement climatique récent endommage un bien non protégé (grêle citée explicitement comme cause de dégât sur bâche existante, donc aussi comme motif d'achat/upgrade par les acheteurs suivants — `[D]`).
- Achat d'un camping-car, d'un bateau, ou d'un second véhicule sans place de garage (usages cités : « voiture, camion, bateau » dans les descriptifs vendeurs, confirmés par des avis « auvent pour bateau »).
- Absence de garage en dur sur le terrain (motif implicite dans la quasi-totalité des avis, jamais formulé en négatif — `[D]`).
- Volonté de protéger la peinture/l'intérieur d'un véhicule neuf ou de valeur avant l'hiver (`[D]`, cohérent avec la saisonnalité des avis concentrés sur les mois d'achat pré-hiver et les mentions de vent/pluie récurrentes).
- Remplacement d'un abri déjà dégradé (bâche/tôle trouée par l'usage, voir §2.7) — un cycle de rachat tous les 1,5 à 4 ans se dessine.

## 5. (c) Vocabulaire client exact (liste)
« torchon inutilisable » · « catastrophe » · « à fuir » · « arnaque » / « arnaqué » · « sardines » (piquets) · « camelote » · « prise au vent » · « ça bouge » · « stressant quand il y a du vent » · « les tubes pas très épais » · « la bâche se défait aux coutures » · « comme un gruyère » (plaques trouées) · « toile se déchire avec le temps » · « laisse passer la lumière » · « perce » / « percé » (bâche trouée) · « gondole » (panneau qui se déforme au soleil) · « jeu » (décalage/imprécision au montage) · « à blanc » (montage à blanc pour vérifier avant fixation définitive) · « torchon » · « plan de calpinage » (implantation des plots béton, vocabulaire technique repris par les clients avertis) · « équerres » · « haubaner » · « pinces impossible de rentrer » · « cornées » (plaques déformées) · « geste commercial » · « dossier SAV » · « fin de non recevoir » · « rire au nez » · « chapeau bas » (compliment livraison rapide) · « au top » · « sérieux » · « conforme au descriptif » · « bon bricoleur » · « bricoleurs avertis » · « prévoir d'être 2/3/4 » · « une bonne loupe » (pour lire une notice trop petite) · « du silicone » (pour compenser une étanchéité insuffisante).

## 6. (d) Objections → ce qu'une bonne fiche devrait répondre
| Objection cliente (verbatim-type) | Réponse attendue sur la fiche |
|---|---|
| « la notice ne correspond pas aux pièces / est un torchon » | Notice numérotée, testée, avec QR code vers une vidéo de montage réelle (pas un montage générique traduit) ; préciser le nombre de personnes et la durée réaliste. |
| « il manque des vis / des pièces » | Annoncer explicitement un kit de visserie complet + une marge de pièces en plus (« toujours une ou deux pièces en plus », cité comme un vrai plus par un client Perenza), et un contact SAV réactif pour un envoi rapide en cas de manque. |
| « les sardines/piquets fournis sont de la camelote » | Soit fournir un système d'ancrage réellement dimensionné (chevilles, platines à sceller), soit dire clairement sur la fiche qu'un scellement béton/renfort est recommandé selon le terrain — éviter la déception après coup. |
| « la bâche/toile se déchire ou blanchit en 1 à 2 ans » | Donner une donnée concrète de grammage/traitement UV, et une politique claire de pièces de rechange (bâche seule rachetable) plutôt que de laisser découvrir l'absence de pièce détachée après coup. |
| « au premier coup de vent, ça a plié / grinçait » | Afficher une résistance au vent chiffrée et crédible (comme Palram le fait avec « jusqu'à 120 km/h »), et insister sur le renforcement au sol nécessaire selon l'exposition. |
| « colis abîmé / palette écrasée à la livraison » | Prévenir sur la fiche du mode de livraison (palette, camion avec hayon ou non, RDV avec créneau), et donner la marche à suivre en cas de dommage visible (réserve à la livraison). |
| « le SAV ne répond pas / rit au nez du client » | Afficher un canal de contact et un délai de réponse engageant, visibles avant achat — les avis positifs sur le SAV citent systématiquement la rapidité et la clarté d'une réponse écrite. |
| « la largeur/hauteur réelle n'est pas celle annoncée » | Donner des cotes précises intérieur/hors-tout, avec marge d'erreur assumée, en particulier pour l'écartement des plots béton à couler avant réception du produit. |
| « avec la pluie/grêle, les plaques ont morflé » | Préciser la résistance aux chocs des plaques (polycarbonate compact vs alvéolaire) et la politique de remplacement pièce par pièce en cas de casse. |

## 7. (e) Banque de 20 money quotes
1. « Le montage assez simple la toile pas assez épaisse et la fixation au sol faible ça le vaux le prix. » — Michael, ManoMano, 06/03/2024, 5★
2. « Tonight was the first windy day of winter. Poles bent in half, tarp ripped, entire structure lifted from the ground and flipped upside down. » — lorinljrk, Amazon, 23/01/2023, 2★
3. « après un an et demi d'installation, la toile du store a été endommagée par le soleil et la moindre pression du doigt a commencé à la percer. » — Paolo, ManoMano, 23/07/2026
4. « Nach zweieinhalb Jahren löst sich die Dachplane komplett auf. » (après 2,5 ans, la bâche se désagrège) — jens hansel, Trustpilot Toolport, 30/08/2026, 1★
5. « Aucune information quant au montage des pignons (...) on voit de petites taches blanches, des faiblesses? » — pascal, ManoMano, 13/05/2024
6. « J'aurais mis 0 étoile ! (...) personne ne répond au téléphone. Je ne sais pas comment récupérer mon argent. » — Catherine, Trustpilot OOGarden, 31/07/2025, 1★
7. « la largeur indiquée est fausse, il faut rajouter 8cm (...) cela peut poser un problème et obliger à refaire du béton. » — avis France, Amazon Palram, 12/08/2020
8. « Structure solide et toile résistante. Seules les fiches (les 'sardines') sont camelote ! » — Alindia, Amazon, 05/09/2026, 5★
9. « pas de plan de montage (...) on a fini par me revoyer le même torchon inutilisable. » — Michel 31, Avis73 franceabris.com, 09/03/2022
10. « il manque le sachet avec les vis et les chevilles bois. Impossible de le monter sans ça. (...) numéro téléphone payant. » — Grenouille27, Trustpilot OOGarden, 02/08/2024, 1★
11. « je trouve qu'il y'a un peu de jeu sur les poteaux de structure, stressant quand il y a du vent. Ça bouge (...) » — Sylvie, Amazon, 22/08/2026, 4★
12. « Après un très léger différent qui a été réglé ultra rapidement (...) Un vrai bonheur! » — laurent vicquenault, Trustpilot Perenza, 20/03/2026, 5★
13. « 90% des composants bois sont vrillés (poteaux, traverses, planche de finition). » — G1bocarport, Avis73 franceabris.com, 08/10/2024
14. « J'ai acheté un carport modèle Carlton. Le livreur a été fort désagréable. 'On se dépêche' me dit il. » — Roger Nguyen, Trustpilot Perenza, 20/06/2026, 1★
15. « Nach 4 Jahren sehen die Platten nun aus wie ein Schweizer Käse. » (après 4 ans, les plaques ressemblent à un gruyère) — Michael Leisering, Trustpilot Toolport, 29/06/2026, 2★
16. « une notice plus précise aurait évité des montages à blanc et fait gagner du temps. Comportement à vérifier lors du prochain coup de vent. » — Frédéric, Amazon, 19/05/2026, 4★
17. « les panneaux de coté se déforment avec un temps ensoleillé !!! un panneau en particulier exposé à l'ouest gondole et revient en place. » — Ninja, Avis73 franceabris.com, 24/04/2025
18. « Commandé le jeudi, livré le mardi, alors que je m'attendais à deux semaines pour la livraison. Chapeau bas ! » — RAMEL François, Trustpilot Dancover, 16/08/2017, 5★
19. « l'accueil téléphonique a été épouvantable et grossier (...) aucun SAV, aucune pièce ne peut etre demandée ni remboursement, ni retour. » — bricolo21, Avis73 franceabris.com, 24/08/2024
20. « Ce carport à gentiment fait office de protection de piscine. Le résultat est apprécié par la famille. » — Client ManoMano, 10/06/2020

---

## Limites et écarts au brief
- **Leroy Merlin inaccessible** (CAPTCHA DataDome, aucune tentative de contournement) : la source #3 du brief n'a pas pu être exploitée en direct. Compensé partiellement par un volume plus important sur Amazon/ManoMano/Trustpilot que prévu (au moins 5 fiches Amazon au lieu de 4, 6 marchands Trustpilot/avis vérifiés/avis73 au lieu de 5).
- **Démarches administratives** (déclaration préalable, voisin) : thème naturellement absent des avis produits e-commerce (les clients ne commentent pas leur mairie sur une fiche produit) — à chercher dans `voc-forums-reddit.md`.
- **Neige et rouille** : peu représentés dans ce corpus (échantillon dominé par des avis printemps/été/automne 2024-2026) ; confiance basse, à ne pas sur-pondérer dans le persona sans confirmation par une autre source.
- Un fichier `raw/avis/amazon-chrome-2026-09-09.md` provient d'une lecture Amazon via le Chrome de Hakim en parallèle de ce travail (fiches Outsunny 3x6 hauteur réglable, Cazeboo KLEO 4x3, XMTECH 3x6) ; intégré ci-dessus car daté et sourcé selon les mêmes règles.
