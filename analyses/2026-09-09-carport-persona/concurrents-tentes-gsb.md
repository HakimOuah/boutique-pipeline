# Concurrents GSB + spécialistes — carports et tentes-garages (France)

Recherche menée le 09/09/2026. Aucun compte créé, aucun panier engagé, aucun message envoyé à un tiers. Règles de preuve du brief appliquées : `[O]` = observé directement sur la page citée, `[D]` = déduit/inféré. Captures brutes dans `raw/<slug>/`.

**Avertissement méthodologique majeur** : leroymerlin.fr, manomano.fr, oogarden.com et cdiscount.com bloquent systématiquement tous les accès outillés disponibles (WebFetch, curl avec en-têtes navigateur, monid/mrscraper avec rendu navigateur réel et mode stealth). Preuve : `raw/leroymerlin-carport-categorie/CONSTAT.txt`, `raw/manomano-carport-categorie/CONSTAT.txt`, `raw/oogarden-carport-categorie/CONSTAT.txt`, `raw/cdiscount-carport-tente-garage/CONSTAT.txt`. leroymerlin.fr et manomano.fr affichent un mur anti-bot (DataDome / Cloudflare "Just a moment...") sur le domaine entier, y compris les fiches produit individuelles (testé sur X-Metal). Ces trois cibles du brief (Leroy Merlin, ManoMano, OOGarden) n'ont donc **pas pu être documentées en verbatim** malgré plusieurs méthodes. J'ai substitué, quand le brief le permettait, des sources alternatives listées dans la même cible (Auchan/Outsunny.fr pour Outsunny, Brico Dépôt pour le 2e carport alu). `[D]` Ce mur systématique sur les 3 plus gros GSB généralistes est en soi une donnée utile pour la boutique : leurs fiches ne sont pas indexables/scrapables facilement, contrairement aux spécialistes (Dancover, VEVOR) qui restent ouverts.

---

## (a) Pages catégorie « carport » — GSB

### Leroy Merlin — INACCESSIBLE
URL cible : `https://www.leroymerlin.fr/produits/terrasse-jardin/abri-garage-rangement/carport/`
`[O]` 403 Forbidden systématique (DataDome). Aucune donnée exploitable. Voir `raw/leroymerlin-carport-categorie/CONSTAT.txt`.

### Castorama
URL : https://castorama.fr/jardin-et-terrasse/abri-de-jardin-garage-carport-et-rangement/garage-et-carport/cat_id_18.cat — capturé 09/09/2026 (extraction assistée WebFetch, voir `raw/castorama-carport-categorie/extraction.txt`)

`[O]` Titre H1 : « Carport »
`[O]` Intro citée : « Découvrez notre sélection de carports alliant robustesse, design et protection optimale pour votre véhicule. Que vous recherchiez un carport en aluminium, en bois ou en acier, nous proposons une gamme variée adaptée à tous les besoins et budgets. »

Filtres relevés (ce qu'ils jugent décisif) :
- **Type de produit** : bâche pour carport, carport autoporté, carport adossé, carport autoporté solaire, claustra pour carport, rideau pour carport, carport aluminium, carport bois
- **Marque** : Plastidis, CPBF, Skan Holz, Tecplast, Abri Français, Ombrazur, Ximax, Palmako, Vevor, +25 autres
- **Nombre maximal de voitures** : 1, 2, 3, 4, 0
- **Matière de la structure** : bois, aluminium, plastique
- **Type de couleur** : gris, vert, neutre, marron, beige, noir, crème, blanc, etc.
- **Prix** : 10€ → 2000€+
- **Options de retrait** : Drive 2h, en magasin, livraison à domicile, livraison express

Guide lié : « Choisir un garage ou un carport »
FAQ page : « Qu'est-ce qu'un carport ? », « Pourquoi utiliser un carport ? », « Comment installer un carport ? »

**Guide séparé fetché** : « Comment installer un carport en bois » (https://www.castorama.fr/idees-et-conseils/comment-installer-un-carport-en-bois/CF_CPRD_npcart_100568.art) — sommaire en 7 étapes (préparation du sol → poteaux → pannes → chevrons → renforts obliques → toiture), section « Règlementation selon l'emprise au sol » en préambule. `[O]` Voir `raw/castorama-guide-installation-carport-bois/extraction.txt`.

### Brico Dépôt
URL : https://www.bricodepot.fr/produits/terrasse-et-jardin/profiter-du-jardin/store-banne-pergola-barnum/carport — capturé 09/09/2026 (voir `raw/bricodepot-carport-categorie/extraction.txt`)

`[O]` Titre H1 : « Carport »
`[O]` Intro citée : « Protégez votre véhicule du soleil, de la pluie, de la neige ou du vent avec un carport en bois ou en aluminium. Fabriqués dans des matériaux résistants et durables, les carports sont prêts à monter. »

Filtres relevés : **Prix** (min/max), **arrivages par date de catalogue** (10 avril, 22 avril, 29 avril, 12 juin) — nettement plus pauvre que Castorama, pas de filtre matériau/nombre de voitures visible sur cette liste.

Titres des guides/conseils en bas de page (blocs éditoriaux, promesses) :
- « Un large choix de carports »
- « Carport en bois ou en aluminium »
- « Le carport pour protéger les voitures »
- « Optez pour un carport adossé »
- « Un carport design pour un extérieur élégant et fonctionnel »
- **« Faut-il un permis de construire pour un carport ? Les règles à connaître »** — exactement la question réglementaire attendue par le brief
- « Carport au meilleur prix chez Brico Dépôt »

### ManoMano — INACCESSIBLE
URL cible : `https://www.manomano.fr/carport-827` + guide `https://www.manomano.fr/conseil/comment-choisir-son-carport-2801`
`[O]` Challenge Cloudflare "Just a moment..." systématique. Voir `raw/manomano-carport-categorie/CONSTAT.txt`. `[D]` Le titre du guide identifié via recherche (non vérifié en page) suggère un contenu pédagogique similaire à Castorama/Brico Dépôt, mais ceci reste non confirmé.

### OOGarden — INACCESSIBLE
URL cible : `https://www.oogarden.com/cat-728-Carports.html`
`[O]` 403 systématique. Voir `raw/oogarden-carport-categorie/CONSTAT.txt`.

---

## (b) Fiches tentes-garages

### 1. Outsunny tente-garage 3x6m
Le brief demandait Leroy Merlin/ManoMano/Carrefour — les trois inaccessibles ou introuvables ; substitué par **Auchan.fr** (revendeur marketplace du même modèle exact) et **outsunny.fr** (marque elle-même), les deux consultés.

**Auchan** — https://www.auchan.fr/outsunny-carport-tente-de-garage-3-x-6-m-abri-voiture-exterieur-avec-2-portes-enroulables-pe-vert/pr-7c44a96e-cd51-4984-a5b5-b48ca06addb4 — capturé 09/09/2026
- `[O]` Titre exact : « Carport tente de garage 3 x 6 m abri voiture exterieur avec 2 portes enroulables PE vert »
- `[O]` Description citée : « Protégez vos véhicules ou bateaux avec notre carport de 3x6m, équipé d'un toit en PE de 200g et de côtés anti-UV. »
- `[O]` Specs : dimensions 594L x 300l x 280H cm ; portes 230l x 180H cm ; hauteur avant-toits 174H cm ; cadre tubes acier galvanisé Ø34/38mm ; bâche PE 200g anti-UV anti-déchirure ; 20 piquets + 4 cordes de tension
- `[O]` Prix 339,90 € — livraison offerte, estimée 13/09/2026 (4-5 jours)
- `[O]` Vendu par un tiers marketplace (Aosom)
- `[O]` **0 avis client affiché**

**Outsunny.fr** (marque directe) — https://outsunny.fr/products/carport-tente-de-garage-3-x-6-m-abri-voiture-exterieur-tente-de-stockage-avec-parois-laterales-amovibles-2-portes — capturé 09/09/2026 (variante gris foncé, avec fenêtres)
- `[O]` Titre exact : « Carport tente de garage 3 x 6 m avec parois latérales amovibles, 2 portes enroulables et 4 fenêtres, gris foncé »
- `[O]` Description citée : « Optimisez votre extérieur avec le carport de 3 x 6 m Outsunny, idéal pour motos, vélos et outils de jardin. Avec son tissu PE imperméable et anti-UV et ses parois amovibles, ce garage de voiture protège efficacement en tout temps. »
- `[O]` Specs : 596L x 300l x 281H cm ; hauteur avant-toits 195H cm ; porte 240l x 188H cm ; fenêtre 97l x 127H cm ; cadre acier ; bâche tissu PE imperméable anti-UV ; garantie 2 ans
- `[O]` Prix 269,90 € — statut **« Épuisé »** au moment de la capture ; livraison citée « Gratuite en France métropolitaine : 3 à 7 jours ouvrables après traitement »
- `[O]` Aucun avis détaillé visible

### 2. Tente-garage 4x6m à portes enroulables — NON DOCUMENTÉE EN VERBATIM
`[D]` Ciblé sur Conforama (fiche 3x6m identifiée, U20469400) : WebFetch n'a récupéré qu'une page listing catégorie (423 produits, pas de détail), monid mrscraper a échoué (HTTP 502 puis vide). Cdiscount et Leroy Merlin bloqués comme documenté ci-dessus. Voir `raw/conforama-tente-garage-3x6/extraction.txt`. Aucune fiche 4x6m à portes enroulables n'a donc pu être analysée en détail dans le temps imparti — à reprendre si besoin avec un accès dédié (ex. worker différent, ou visite manuelle).

### 3. VEVOR Abri de voiture 4x8m — vevor.fr
URL : https://www.vevor.fr/abris-d-auto-c_12018/vevor-abri-de-voiture-exterieur-en-metal-robuste-pour-pick-up-bateau-4-x-8-m-p_010702666070 — capturé 09/09/2026 (curl direct, 200 OK, raw HTML sauvegardé)

- `[O]` Titre exact : « VEVOR Abri de voiture en métal robuste, 4 x 8 m, abri de garage extérieur avec cadre et toit en acier galvanisé, auvent pour voiture multi-usage avec parois latérales amovibles, pour pick-up, bateau »
- `[O]` Prix : **1 242,90 €**
- `[O]` Description « Toit robuste » citée : « le toit est en acier galvanisé, offrant une protection durable. Il est équipé d'un ruban d'étanchéité haute densité amélioré pour éviter les fuites de pluie [...]. Avec une capacité de charge de toit de 35 lb/pi², cet abri d'auto avec toit en acier est idéal pour protéger vos véhicules et équipements des éléments »
- `[O]` Description « Structure solide » citée : « l'abri d'auto extérieur est doté d'un cadre renforcé avec des renforts en acier supplémentaires sur le toit et les côtés. Fabriqué à partir de tubes en acier haute résistance de 2 pouces/5 cm avec une finition en émail cuit, cet abri d'auto en acier offre une résistance à la rouille et une durabilité exceptionnelles, assurant une stabilité à long terme dans la neige et le vent - idéal pour les abris d'auto pour la neige ou d'autres conditions exigeantes »
- `[O]` Specs techniques tableau : matériau principal « Q195 + PE » ; 12 colonnes ; 40 barres transversales ; charge de toit 35 lb/pi² ; épaisseur paroi colonne 1,2 mm ; dimensions produit L x l x H = 4 x 8 x 3,15 m ; poids total réparti sur 4 boîtes (63 + 62,5 + 52,8 + 54,5 kg)
- `[O]` **Note et avis : 3,7/5 sur 78 avis**. Répartition : 5★ 53% / 4★ 10% / 3★ 14% / 2★ 5% / 1★ 18% — donc près d'1/4 des avis à 1-2 étoiles, malgré une moyenne correcte.
- `[O]` Verbatim négatif (1★, 32 personnes l'ont trouvé utile) : « BEWARE! !!! NOT GALVANIZED !!! [...] I received the 13' x 26' Vevor Carport, 4 packages. Had a crew assemble it while I was at work, came gome only to find that it was not a galvanized roof, not a galvanized frame. This us ckassic false advertising. ILLEGAL to false advertise in Canada. I have reached out to Vevor [...] they say "There is nothing wrong with the product". [...] I also had to give it a 5 star rating so that it wouldn't be pushed down to the bottom of the reviermw pile. » — Jason Taylor, achat vérifié
- `[O]` Verbatim positif (ES traduit) : « Todo perfecto, muy satisfecho con la compra. » — r.***
- `[O]` Verbatim positif (FR) : « Je suis trés contente de mon achat sa c est très bien monté rencontrer aucun problème reste a savoir si va etre solide pour la neige » — joseemorin522, titre « Belle qualite »
- `[O]` Verbatim mitigé/positif : « I didnt assemble the carport yet, but should look good when it is up, had some issues with delivery but vevors professional service sorted the issue 👌 » — pat mcneill, titre « Great service from Vevor. »
- `[O]` Q&A présente (1 question) : « comment sont fermés les côtés ? Peut-on cadenasser l'entrée ? » — réponse par le vendeur renvoyant vers un manuel PDF externe, pas de réponse d'un autre acheteur.
- `[D]` Signal fort : le système d'avis lui-même incite à mettre 5 étoiles pour ne pas être noyé (cf. verbatim Jason Taylor) — donne un doute sur la fiabilité de la note affichée à l'avantage du vendeur.

---

## (c) Carports aluminium GSB

Leroy Merlin (X-Metal / Preston) inaccessible (voir avertissement). Substitué par deux fiches Brico Dépôt.

### Brico Dépôt — Carport aluminium « Victoria »
URL : https://www.bricodepot.fr/catalogue/carport-en-aluminium-toit-plat/prod95584/ (URL trouvée sous le libellé « carport aluminium toit plat » en recherche, mais sert en réalité la fiche Victoria) — capturé 09/09/2026, curl direct 200 OK

- `[O]` Titre exact : « Carport aluminium "Victoria" - L. 5 x l. 2,90 x H. 2,10 m »
- `[O]` Prix : 999,00 € TTC/pièce
- `[O]` Bloc « Les plus produit » (texte intégral, 3 puces) : « Toit en polycarbonate Anti-UV » / « Avec gouttière » / « Toiture polycarbonate anti-UV résistante »
- `[O]` Référence 3601659519843 / Code 100825011
- `[O]` Garanties citées : « garantie légale de conformité (2 ans) et [...] garantie légale des vices cachés » + « garantie étendue du fabricant de 10 ans »
- `[O]` Mention : « À monter soi-même »
- `[O]` **Aucune fiche technique détaillée (pas d'épaisseur de polycarbonate, pas de charge de neige, pas de résistance au vent, pas de poids), aucun avis client visible dans le HTML statique** — la fiche produit est très pauvre en contenu par rapport aux specialistes.

### Brico Dépôt — Carport aluminium Almo
URL : https://www.bricodepot.fr/catalogue/carport-aluminium-almo/prod94858/ — capturé 09/09/2026, curl direct 200 OK

- `[O]` Titre exact : « Carport aluminium Almo »
- `[O]` Prix : 1 689,00 € TTC/pièce
- `[O]` Bloc « Les plus produit » (texte intégral) : « Laisse passer la lumière mais protège des UV » / « Protection hautes températures » / « Fournis prêt à monter rapidement »
- `[O]` Référence 5063022556417 / Code 101527086
- `[O]` **Même constat** : aucune caractéristique technique chiffrée (dimensions non listées dans le corps texte capturé, pas de charge neige/vent, pas de poids), aucun avis visible.

`[D]` Les deux fiches Brico Dépôt confirment un pattern : titre + prix + 2-3 « plus produit » en une ligne + garanties légales génériques, sans tableau de caractéristiques techniques complet ni avis clients dans le rendu capturé — soit ces données sont chargées par un widget JS non exécuté par curl, soit elles n'existent simplement pas sur ces fiches.

---

## (d) Spécialistes tentes-garages

### toolport.fr → en réalité toolportfr.com
URL accueil : https://toolportfr.com/ — capturé 09/09/2026 (WebFetch)

- `[O]` H1 : « L'EXPERT DES TENTES ET ABRIS EXTÉRIEURS »
- `[O]` Promesses citées : « Livraison Express Et Retours Gratuits Sous 30 Jours » ; « Nous concevons des solutions innovantes pour vos espaces extérieurs depuis plus de 15 ans » ; « Des produits de haute qualité » à prix accessible
- `[O]` Vocabulaire : tente, pavillon, tonnelle, barnum, chapiteau, abri, hangar de stockage, bâche imperméable PVC 700N, structure acier galvanisé/aluminium
- `[O]` Réassurance : « normes CE et TÜV », garantie « pièces détachées pendant 10 ans », avis 5 étoiles avec témoignages nommés, « 100% personnalisables », « fabriqués en Europe », « SAV réactif »
- **Constat structurel majeur `[O]`** : les 12 modèles vedettes affichés (3x6, 4x8, 5x10, 6x12, 3x3, 4x4, 4x6, 3x4, 4x5, 3,3x6, 5x8) ont tous un bouton « Acheter » qui **redirige vers une fiche Amazon.fr** (lien d'affiliation vérifié : https://www.amazon.fr/Abri-Tente-stockage-ECONOMY-impermeable/dp/B00TPZMVTE). `toolportfr.com` n'est donc **pas un site marchand direct** mais un site vitrine/comparateur qui capte le trafic SEO puis convertit sur Amazon. Confirmé sur la fiche de contenu « TOOLPORT Tente De Stockage » (https://toolportfr.com/toolport-tente-de-stockage/) : gamme ECONOMY 3x6m présentée comme « option économique adaptée à un usage occasionnel », toile PVC 700D certifiée M2, structure acier, durée de vie annoncée « pouvant dépasser 20 ans », résistance au vent « jusqu'à 100 km/h » — puis renvoi vers Amazon pour l'achat.

### dancovershop.com
Accueil (https://www.dancovershop.com/fr/) et fiche produit — capturés 09/09/2026 (curl direct, 200 OK, seul spécialiste + seul site du lot pleinement accessible en scraping direct)

**Accueil** :
- `[O]` Bandeau de réassurance : « 23+ ans d'expérience », « 55.000+ avis clients », « 4/5 étoiles », « Aide d'experts » avec numéro de téléphone direct (07 56 78 40 71) et email
- `[O]` Catégorie « Abris Voiture » affichée avec prix d'appel « A partir de 191 € »
- `[O]` Bloc contenu pergola : « CRÉEZ VOTRE NOUVEL ESPACE DE DÉTENTE EN PLEIN AIR [...] Son design moderne et architectural, associé à une structure robuste en aluminium thermolaqué, crée un espace extérieur élégant, durable et facile à entretenir »
- `[O]` Mécanique promo permanente : codes de réduction affichés en direct sur la home (« GREEN10 », « FLEX10 », « BIRTHDAY » -15%), compte à rebours « Dernière chance »
- `[O]` Moyens de paiement affichés : Visa, Mastercard, PayPal, Alma, Klarna

**Fiche « Tente abri garage PRO 3,6x8,4x2,7m PVC avec couvre-sol, Vert »** — https://www.dancovershop.com/fr/product/garage-portable-pro-36x84x27m-pvc-avec-couvre-sol-vert.aspx
- `[O]` Description citée : « Tente abri garage pour tout type de rangement. Parfait lorsque vous avez besoin d'une solution flexible, sécurisée et abordable pour être placée à peu près n'importe où. La structure en acier galvanisé et la toile imperméable ont une grande durabilité et garantissent un stockage optimal ! Sangles robustes pour fixer la toile au châssis au sol. Recouvrement de sol en PE avec velcro inclus ! »
- `[O]` Fiche technique complète et chiffrée (contraste fort avec les GSB) :
  - Matériau toit : « PVC Solides », poids 500g/m²
  - Matériau parois latérales : « Solides PVC », poids 500g/m²
  - Cadre : « Solide structure en acier galvanisé »
  - Construction selon norme **EN 1090-1:2009+A1:2011**
  - Hauteur latérale 2,2 m / hauteur du faîtage 2,68 m / largeur 3,6 m / longueur 8,4 m
  - Tubes/fixations : 32x45x1,2mm + Ø25x1,0mm + Ø25x0,8mm
  - Poids total 174 kg
  - Résistance UV et étanchéité « 100% Étanche » revendiquées
  - Taille de porte : 3,6/3,2 x 2,10 m
- `[O]` Prix : 1 335,61 € plein tarif / **1 135,26 € prix membre (-15%)**
- `[O]` Livraison : « Expédition le prochain jour ouvrable » si commande avant heure limite ; en stock, livraison estimée au 11 septembre
- `[O]` Garantie meilleur prix détaillée (remboursement de la différence sous conditions, 10 jours)
- `[O]` Notice et conseils de sécurité téléchargeables (PDF), incluant avertissements explicites : condensation normale, neige à retirer du toit sous peine d'effondrement, tente non testée pour une résistance neige/vent spécifique, ne pas monter sous 0°C
- `[O]` **Pièces détachées vendues séparément** à l'unité (23 références listées, ~15-70€/pièce, dont toile de toit de rechange à 510,56€ et paroi/porte à 70,19€) — signal de service après-vente structuré, contrairement aux GSB
- `[O]` Aucun verbatim d'avis individuel visible dans le HTML statique (seul le chiffre agrégé « 55.000+ avis / 4/5 étoiles » apparaît ; les avis détaillés semblent chargés par un widget tiers non présent dans le rendu capturé)

---

## Synthèse transversale

**Ce que les GSB font mieux que les spécialistes** : filtres de navigation plus riches côté Castorama (matériau, nombre de voitures, marque, couleur, prix) ; maillage de contenu réglementaire bien identifié (« Faut-il un permis de construire pour un carport ? », guide d'installation en 7 étapes) qui répond directement à l'objection juridique ; retrait en magasin/Drive 2h.

**Ce que les GSB font mal** : sur les deux fiches Brico Dépôt effectivement lues (Victoria 999€, Almo 1689€), aucune caractéristique technique chiffrée (pas d'épaisseur, pas de charge neige/vent, pas de poids) au-delà de 2-3 « plus produit » d'une ligne, et **zéro avis client visible** — écart énorme avec Dancover qui affiche fiche technique normée (EN 1090-1) + poids + notice de sécurité PDF + pièces détachées. `[D]` Sur Leroy Merlin/ManoMano, cohérent avec la mémoire de Hakim sur les photos fournisseur et descriptions minimalistes, mais non vérifiable ici faute d'accès — à confirmer par une autre méthode (visite manuelle ou worker dédié).

**10 attributs techniques mis en avant pour une tente-garage** (croisement Outsunny/VEVOR/Dancover/Toolport) : 1) dimensions L x l x H, 2) hauteur de passage/faîtage, 3) matériau du cadre (acier galvanisé quasi systématique), 4) grammage de la bâche (PE 150-200g chez Outsunny bas de gamme vs PVC 500-700g chez Dancover/Toolport haut de gamme), 5) traitement anti-UV, 6) étanchéité/imperméabilité revendiquée, 7) type et nombre de portes (enroulables), 8) parois amovibles/fenêtres, 9) piquets d'ancrage/cordes de tension fournis, 10) poids total du produit.

**10 attributs pour un carport aluminium** : 1) dimensions (L x l x H), 2) matériau toiture (polycarbonate épaisseur mm, souvent absente des fiches GSB), 3) traitement anti-UV du toit, 4) gouttière incluse ou non, 5) autoportant vs adossé, 6) nombre de voitures, 7) kit d'ancrage inclus, 8) garantie fabricant (10 ans revient souvent), 9) déclaration de travaux/permis (surface), 10) couleur/finition (anthracite, blanc, gris).

**Objections récurrentes identifiées dans les avis (VEVOR, seule source avec verbatims réels)** : matériau non conforme à l'annonce (« NOT GALVANIZED »), doute sur la tenue à la neige/au vent formulé par les acheteurs eux-mêmes au moment de l'achat (« reste à savoir si ça va être solide pour la neige »), système d'avis biaisé par le vendeur (incitation implicite à mettre 5 étoiles), problèmes de livraison résolus au cas par cas par le SAV. `[D]` Ces trois objections (matière réelle vs annoncée, tenue neige/vent, fiabilité du SAV) sont probablement transférables aux tentes-garages en général et méritent vérification croisée dans le fichier `voc-avis-clients.md`.
