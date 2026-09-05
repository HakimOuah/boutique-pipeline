# PLAYBOOK — Recherche produit Google-first

Objectif : trouver des produits testables en dropshipping via Google Ads, en distinguant
**Shopping-first**, **Search-first** et **Both**, puis sortir une shortlist priorisée avec verdict
GO / MAYBE / NO-GO.

Ce playbook s'utilise avant `PLAYBOOK.md`. Il sert à décider quel produit mérite une boutique.

## Posture obligatoire

- Agir comme chef de projet dropshipping senior orienté testing Google Ads.
- Chercher la marge, l'intention, la différenciation et la faisabilité opérationnelle avant l'effet
  "wow".
- Ne pas confondre produit viral social et produit testable sur Google.
- Ne pas chercher "un produit" mais une **thèse produit** : problème réel + client identifiable +
  solution utile + angle différenciant + marge + faisabilité fournisseur + landing page capable de
  créer plus de valeur que les concurrents.
- Challenger les idées faibles : marge trop basse, fournisseur risqué, demande floue, claims
  dangereux, concurrence trop forte, angle trop fragile.
- Être hyper sélectif : mieux vaut sortir 3 produits solides que 20 idées moyennes.
- Filtrer les produits mainstream/rincés dès la recherche, pas seulement au scoring. Ne pas remplir
  la shortlist avec des produits connus d'avance comme faibles.
- Écarter Amazon, Darty, Decathlon, Fnac, marketplaces et grandes enseignes du benchmark
  concurrentiel direct. Les utiliser seulement comme repères prix/SERP.
- Prioriser les boutiques DTC, mono-produit, DNVB, dropshipping ou e-commerce spécialisés pour
  comprendre les vraies mécaniques de conversion.
- DataForSEO API est l'unique source de volume et de gate. TrendTrack, Minea, Similarweb et les autres
  outils payants ne servent qu'à leurs usages propres si Hakim confirme un accès actif ; aucun ne
  remplace DataForSEO pour mesurer la demande.
- Pour la France, toujours vérifier que les outils de keyword research sont réglés sur **France**
  avant d'interpréter volumes, CPC, intent ou difficulté. Ne pas utiliser les données United States
  par défaut pour décider d'un lancement France.

## Entrée minimale

Demander ou remplir `templates/product-research-request.template.md`.

Les champs peuvent rester vides. Si aucune niche n'est donnée, chercher des produits compatibles
avec le profil OH Ventures : dropshipping Shopify, Google Ads, France, marge suffisante, conformité
GMC, produits non dangereux.

## Définition d'un bon produit

Un bon produit pour ce pipeline n'est pas seulement un produit qui se vend déjà. C'est un produit
qui permet de construire une offre utile, désirable, différenciée et crédible.

Il existe deux grandes voies acceptables :

1. **Problème / solution** : le produit atténue une douleur, une frustration ou une contrainte.
2. **Désir / univers / high-ticket** : le produit n'a pas besoin de résoudre une douleur forte s'il
   crée un désir clair, améliore un intérieur, apporte une valeur esthétique, statutaire, pratique
   ou émotionnelle, et laisse une marge suffisante pour Google Ads.

Il doit idéalement cocher plusieurs de ces points :

- il résout une douleur concrète, fréquente ou émotionnellement forte ;
- ou il répond à un désir clair : maison plus belle, espace mieux organisé, objet plus premium,
  ambiance, confort, cadeau, statut, praticité ou cohérence décorative ;
- il améliore une situation déjà existante, pas un besoin artificiel ;
- il est compréhensible rapidement, mais assez riche pour justifier une page persuasive ;
- il laisse une marge de manoeuvre pour créer une marque, une offre, un bundle, un angle ou une
  meilleure expérience d'achat ;
- il permet de faire mieux que les concurrents sur au moins un axe : bénéfice, pédagogie, design,
  confort, usage, qualité perçue, livraison, garantie, bundle, spécialisation ou persona ;
- il a une demande Google vérifiable ou une douleur recherchée ;
- il atteint au minimum le seuil DataForSEO du mode défini dans `PRODUCT-RESEARCH-CRITERIA.md` :
  **12 500/mois en PRODUIT PUR** ou **37 500 consolidés en UNIVERS**, sur une demande directement pertinente. Sous ce seuil, le
  produit ne doit pas entrer en shortlist, sauf demande explicite d'Hakim ;
- pour les marchés maison, mobilier, cuisine, salle de bain ou déco high-ticket : il a une demande
  mensuelle suffisante, une recherche Shopping visible, des concurrents imparfaits, et une
  différenciation possible par style, sélection, qualité perçue, dimensions, usage, bundle,
  livraison ou réassurance ;
- il n'a pas besoin de fausses promesses pour être désirable ;
- il supporte un prix qui laisse respirer Google Ads.

Exemple de logique attendue :

- Mauvaise recherche : "des t-shirts se vendent, donc vendre des t-shirts".
- Bonne recherche : "des hommes cherchent un t-shirt qui flatte la silhouette sans faire
  compression médicale ; angle : coupe ventre discret + bras/pectoraux mieux dessinés + basique
  premium de tous les jours".

La valeur peut venir du produit lui-même, mais aussi de l'angle, du persona, du bundle, du contenu,
de la pédagogie, des images, de la réassurance ou de l'offre.

## Exclusion amont — produits à ne pas sourcer

Ces produits ne doivent pas seulement être pénalisés au scoring : ils doivent être évités dès la
phase de sourcing. Ne pas remplir la shortlist avec eux, sauf demande explicite d'Hakim ou variation
réellement nouvelle et défendable.

Éviter les produits dropshipping rincés ou trop mainstream :

- correcteur de posture générique ;
- ceinture sudation / minceur ;
- pistolet de massage générique ;
- humidificateur LED générique ;
- brosse anti-poils générique ;
- lampe galaxie / projecteur étoilé générique ;
- gadget de cuisine vu partout ;
- produit "miracle" beauté/santé ;
- accessoire téléphone commoditisé ;
- mini imprimante, mini caméra, gadgets électroniques sans vraie promesse ;
- tout produit dont la page pourrait être copiée-collée depuis 2019.

Éviter aussi les produits bizarres ou trop éloignés d'une marque DTC grand public, sauf demande
explicite :

- ferme, poulailler, élevage, matériel agricole ;
- outillage industriel très niche ;
- pièces mécaniques obscures ;
- produits B2B sans émotion d'achat ;
- produits qui demandent une expertise technique ou SAV disproportionné.

Un produit mainstream peut redevenir intéressant uniquement si l'angle change réellement le marché
perçu, comme un t-shirt repositionné sur la silhouette masculine plutôt que sur "un t-shirt basique".
Dans ce cas, il doit être présenté comme une nouvelle thèse produit, pas comme un produit générique.

## Sortie obligatoire

Produire un tableau shortlist avec :

- produit ;
- source ;
- prix fournisseur livré si disponible ;
- fournisseur AliExpress identifié ;
- URL fournisseur AliExpress ;
- commandes AliExpress ;
- note produit AliExpress ;
- notation vendeur AliExpress ;
- délai de livraison AliExpress ;
- expédié depuis Europe : oui/non ;
- prix de vente probable ;
- marge estimée ;
- Shopping Score ;
- Search Score ;
- Business Score ;
- canal recommandé : Shopping / Search / Both ;
- concurrents DTC comparables ;
- angle marketing ;
- thèse de différenciation ;
- problème résolu ;
- désir ou univers adressé si ce n'est pas un produit douleur ;
- valeur ajoutée possible ;
- raison pour laquelle ce n'est pas juste une copie ;
- risques ;
- verdict : GO / MAYBE / NO-GO.

Puis proposer les 1 à 3 meilleurs produits à creuser, avec ordre de priorité.

### Livraison obligatoire dans Google Sheet

À chaque recherche produit, créer une nouvelle feuille dans ce Google Sheet :

`https://docs.google.com/spreadsheets/d/1L-SLQrpzEIK07eBUqS1Q9C6sbl398TU8e5Xm4DK7JAU/edit?gid=0#gid=0`

Nommer la feuille :

`recherche YYYY-MM-DD`

Exemple : `recherche 2026-06-25`.

Si plusieurs recherches sont faites le même jour, ajouter un suffixe court :

`recherche YYYY-MM-DD 2`

La feuille doit contenir au minimum toutes les colonnes de la sortie obligatoire :

- produit ;
- source ;
- prix fournisseur livré si disponible ;
- fournisseur AliExpress identifié ;
- URL fournisseur AliExpress ;
- commandes AliExpress ;
- note produit AliExpress ;
- notation vendeur AliExpress ;
- délai de livraison AliExpress ;
- expédié depuis Europe : oui/non ;
- prix de vente probable ;
- marge estimée ;
- Shopping Score ;
- Search Score ;
- Business Score ;
- score total ;
- canal recommandé : Shopping / Search / Both ;
- concurrents DTC comparables ;
- concurrents marketplaces / grandes enseignes utilisés seulement comme repères ;
- angle marketing ;
- thèse de différenciation ;
- problème résolu ;
- désir ou univers adressé si ce n'est pas un produit douleur ;
- valeur ajoutée possible ;
- raison pour laquelle ce n'est pas juste une copie ;
- Google Trends : pays, période, indice moyen, tendance récente, saisonnalité ;
- DataForSEO : endpoint, France/français, volume, CPC + devise, intention disponible, variations ;
- Google Shopping / SERP : présence commerciale, prix observés, qualité des offres ;
- fournisseurs : prix livré si disponible, prix non livré sinon, MOQ, délai, risque fournisseur ;
- AliExpress : prix fournisseur, prix livré, commandes, étoiles/note produit, notation vendeur,
  délai, pays d'expédition, expédié depuis Europe oui/non, URL fournisseur ;
- risques ;
- condition de GO ;
- verdict : GO / MAYBE / NO-GO.

La réponse finale dans Codex doit indiquer clairement que la feuille a été créée/remplie, avec son
nom exact. Si l'accès au Google Sheet est bloqué ou si aucun outil Google Sheets n'est disponible,
ne pas faire semblant : livrer le tableau dans la conversation et signaler explicitement que la mise
à jour du Google Sheet reste à faire.

### Anti-doublon obligatoire avant recherche

Avant de noter une nouvelle idée produit, vérifier l'historique des recherches déjà livrées :

1. Ouvrir le Google Sheet obligatoire.
2. Parcourir les feuilles `recherche YYYY-MM-DD` existantes et relever les produits déjà analysés.
3. Comparer les nouvelles idées aux anciens produits avec une logique de synonymes et variantes :
   singulier/pluriel, accents, nom anglais/français, variante couleur/taille, produit très proche ou
   même usage client.
4. Exclure tout produit déjà recherché, même si le nom est légèrement différent.
5. Ne réintégrer un produit déjà analysé que si Hakim demande explicitement une mise à jour ou si la
   thèse est réellement nouvelle. Dans ce cas, marquer clairement `déjà recherché - reprise motivée`.

Si l'accès au Google Sheet est bloqué, utiliser les livrables locaux et l'historique disponible dans
la conversation. Si l'historique ne peut pas être vérifié, le signaler dans les limites avant de
présenter la shortlist.

## Étape 1 — Cadrage

Clarifier :

- pays cible ;
- budget test approximatif ;
- gamme de prix souhaitée ;
- niches interdites ;
- contraintes légales ;
- outils disponibles ;
- objectif de sortie : nombre d'idées, profondeur d'analyse, délai.

Par défaut :

- Pays : France.
- Langue : français.
- Business : SASU/OH Ventures, HT, TVA au réel, IS.
- Canal : Google Shopping + Google Search.
- Recherche : DataForSEO API pour les volumes/CPC, web public pour SERP, Shopping et concurrents ;
  autres outils payants seulement si accès confirmé et jamais comme source de gate.

## Étape 2 — Sourcing large d'idées

Objectif : collecter 20 à 50 idées brutes en appliquant déjà le filtre d'exclusion amont, puis
rechercher la thèse cachée derrière chaque idée prometteuse.

Sources gratuites :

- Google Trends : tendances, saisonnalité, comparaison de formulations.
- Google Search + onglet Shopping : présence commerciale réelle, prix, formats d'annonces.
- Amazon Best Sellers : repérer demande massive, formats produits, avis et objections.
- AliExpress / DSers : produits disponibles, prix, variantes, expédition, volume de commandes.
- Alibaba : sourcing B2B, tendances fournisseur, prix grossiste, variantes.
- TikTok Creative Center : signaux créatifs, bénéfices visuels, angles viraux.
- Meta Ad Library : boutiques qui poussent encore des pubs.
- Google Ads Transparency Center : ads Google de concurrents vérifiés.
- Reddit / forums / commentaires avis : douleurs client et langage naturel.
- Avis Amazon/AliExpress/concurrents : frustrations répétées, attentes non satisfaites, défauts
  produit, objections et opportunités de repositionnement.

### Protocole AliExpress obligatoire via Computer Use

Chaque fois qu'une idée produit est notée dans la recherche, utiliser Computer Use pour ouvrir
AliExpress et tenter d'identifier au moins un fournisseur crédible. Cette vérification doit être
faite dès le sourcing, pas seulement à la fin du scoring.

Pour chaque idée, relever si disponible :

- URL du produit/fournisseur AliExpress ;
- prix produit ;
- prix livré ou frais de livraison estimés ;
- nombre de commandes ;
- note produit / étoiles ;
- notation vendeur ou score boutique ;
- pays d'expédition ;
- délai de livraison estimé vers la France ;
- mention `expédié depuis Europe : oui/non` ;
- variantes pertinentes ;
- signaux de risque : peu de ventes, avis faibles, délais longs, images watermarquées, specs floues.

Critères minimums pour considérer le fournisseur comme exploitable :

- note produit minimum : **4,5/5** ;
- vendeur/boutique avec notation crédible, idéalement **4,5/5 ou équivalent** ;
- nombre de commandes suffisant pour réduire le risque, à interpréter selon le prix et la niche ;
- livraison assez rapide pour une promesse e-commerce France ;
- priorité aux produits expédiés depuis l'Europe ;
- pour les produits volumineux ou gros mobilier, accepter un délai non-EU seulement s'il reste court
  pour la catégorie, clairement annoncé et défendable dans l'offre.

Si aucun fournisseur AliExpress ne respecte ces critères, ne pas masquer le problème :

- marquer le fournisseur comme `non confirmé` ;
- pénaliser le score fournisseur ;
- ne pas donner un verdict GO sans fournisseur alternatif crédible ou condition de GO explicite ;
- préciser si AliExpress a été bloqué, vide, incohérent ou inutilisable.

Sources complémentaires utiles si accès actif :

- DataForSEO API : source unique des volumes et CPC de gate.
- TrendTrack : stores performants, best-sellers, ads, apps, thèmes, signaux e-commerce.
- Minea : ads spy multi-plateforme, produits poussés, angles créatifs.
- PipiAds : TikTok/TikTok Shop, utile pour repérer des produits qui migrent ensuite vers Google.
- Similarweb : trafic concurrent, canaux d'acquisition, poids Search/Paid/Referral.
- Ahrefs / KeywordTool.io : signaux SEO complémentaires, jamais sources de volume de gate.
- Copyfy / services copy : inspiration ou délégation, mais Codex doit garder le contrôle stratégique
  du persona, des douleurs et de la conformité.

Utilisation recommandée des outils complémentaires :

- **Ahrefs** : pages concurrentes et contenus qui captent la demande, sans alimenter la gate de volume.
- **TrendTrack** : repérer stores, best-sellers, ads, apps utilisées, produits poussés récemment.
- **Similarweb** : estimer mix de trafic concurrent, poids Search/Paid/Social/Referral.
- **Minea / PipiAds** : détecter angles créatifs, durée des ads, produits social qui peuvent être
  revalidés sur Google.

Les données des outils complémentaires ne remplacent jamais DataForSEO ni le jugement stratégique : un volume élevé ou
une pub active ne suffit pas. Le produit doit toujours passer les filtres : utilité ou désir,
différenciation, marge, fournisseur, conformité, opportunité CRO.

### Protocole DataForSEO France

1. Charger les identifiants depuis `ecommerce-dropshipping/.env` sans les afficher.
2. Tirer le témoin `tufting` via DataForSEO avant la première mesure et après la dernière ; les deux
   réponses doivent être non nulles et cohérentes entre elles. Sinon, arrêter sans publier de chiffres.
3. Découvrir le corpus avec `boutique-pipeline/scripts/kw_dfs.py`, endpoint
   `dataforseo_labs/google/keyword_suggestions`, correspondance plein texte.
4. Contrôler les têtes et mots décisifs avec `keywords_data/google_ads/search_volume/live`.
5. Imposer `location_name: France` et `language_name: French` dans chaque payload.
6. Comparer 3 à 5 formulations et plusieurs niveaux : produit, variante, singulier/pluriel, catégorie
   parente, requête achat/prix ou douleur/usage.
7. Dédupliquer les buckets proches : une idée normalisée par groupe, `MAX` du groupe ; ne jamais sommer
   deux séries mensuelles identiques.
8. Appliquer les seuils DataForSEO de `PRODUCT-RESEARCH-CRITERIA.md`, puis croiser obligatoirement avec
   Google Trends, SERP et Shopping. Archiver le JSON, l'endpoint, les paramètres, la date et le coût.

### Quand utiliser les autres outils Kloow

- Utiliser **TrendTrack / SellTheTrend / Minea / PipiAds** si le produit vient d'un signal social,
  si l'on veut vérifier que le produit est déjà massivement poussé, ou si l'on cherche des angles
  créatifs et boutiques DTC actives.
- Utiliser **Similarweb** si un concurrent DTC semble sérieux et qu'il faut estimer ses canaux :
  Search, Paid, Social, Referral, trafic direct.
- Utiliser **Ahrefs** pour vérifier contenus SEO, pages concurrentes ou potentiel organique, jamais
  pour remplacer une mesure DataForSEO manquante.
- Ne pas ouvrir tous les outils par réflexe. Les utiliser quand ils répondent à une question précise
  du scoring : demande, concurrence, trafic, angles, canaux ou opportunité CRO.

Méthodes de sourcing à privilégier :

- **Douleur -> solution** : partir d'un problème recherché, puis trouver le produit qui l'atténue.
- **Désir -> objet high-ticket** : partir d'un univers de désir (maison, déco, rangement premium,
  salle de bain, cuisine, chambre enfant, espace sport maison), puis chercher un produit avec
  demande, belle valeur perçue, panier élevé et concurrents améliorables.
- **Produit banal -> angle spécialisé** : chercher un usage, persona ou bénéfice qui transforme un
  produit commun en offre différenciée.
- **Concurrent faible -> meilleure expérience** : trouver un produit vendu par des pages pauvres et
  construire une meilleure pédagogie/offre/réassurance.
- **Avis négatifs -> opportunité** : identifier ce que les clients reprochent aux produits existants
  et chercher une variante ou une offre qui répond mieux.
- **Accessoire -> système** : transformer un simple accessoire en routine, kit, pack ou solution
  complète.

## Étape 3 — Filtre anti-perte de temps

Éliminer rapidement :

- produit déjà ultra connu en dropshipping sans angle neuf, idéalement avant même la shortlist ;
- prix de vente trop bas pour Google Ads ;
- marge insuffisante après TVA/IS/CAC ;
- produit fragile, dangereux ou très réglementé ;
- promesses médicales, minceur, santé ou sécurité difficiles à prouver ;
- fournisseur sans stock, délais longs ou avis inquiétants ;
- produit trop générique sans différenciation possible ;
- produit impossible à expliquer visuellement ou verbalement ;
- marché verrouillé uniquement par grosses enseignes sans angle DTC ;
- produit qui n'apporte aucune valeur utile au client au-delà de "c'est pas cher" ;
- produit dont la seule preuve de potentiel est "je l'ai vu chez un concurrent".

Garder en priorité :

- produit visuel ;
- douleur ou désir clair ;
- prix psychologique exploitable ;
- fournisseur EU ou délai acceptable ;
- marge brute confortable ;
- différenciation visible ou angle éditorial fort ;
- potentiel de plus-value : bundle, guide, meilleure promesse, meilleur usage, meilleure sélection,
  meilleure présentation, meilleure réassurance ;
- persona précis et solvable ;
- concurrents DTC présents mais faibles ;
- page produit améliorable par CRO, copy, images ou offre.

Questions éliminatoires :

1. Quel problème précis ce produit résout-il, ou quel désir clair nourrit-il ?
2. Pourquoi quelqu'un paierait-il plus cher chez nous qu'une alternative marketplace ?
3. Quelle amélioration pouvons-nous apporter par rapport à ce qui existe ?
4. Si un concurrent vend déjà ce produit, que faisons-nous différemment et mieux ?
5. Est-ce que l'angle peut tenir sans mensonge, fausse preuve ou claim dangereux ?
6. Le produit a-t-il encore l'air intéressant après calcul marge/CAC ?

Si les réponses sont faibles, le produit est NO-GO.

Exception high-ticket / désir :

Un produit maison, mobilier, cuisine, salle de bain, déco ou lifestyle peut passer sans douleur
forte si :

- le panier est suffisant ;
- la demande Google est claire ;
- l'image et la valeur perçue jouent un rôle majeur ;
- les concurrents sont faibles sur design, réassurance, livraison, photos, dimensions, usage ou
  offre ;
- la boutique peut créer un univers désirable et rassurant ;
- le fournisseur permet une qualité visuelle et opérationnelle crédible.

## Étape 4 — Validation Google Demand

Pour chaque idée survivante :

1. Rechercher les termes produit dans Google.
2. Rechercher les termes douleur/problème.
3. Vérifier Google Shopping.
4. Vérifier Google Trends.
5. Mesurer via DataForSEO API avec `location_name: France` et `language_name: French`.

À noter :

- volume ou indice relatif ;
- CPC approximatif ;
- intention d'achat ;
- variantes longue traîne ;
- saisonnalité ;
- pays/régions intéressants ;
- requêtes à exclure ;
- niveau de pédagogie nécessaire.

### Protocole Google Trends

Google Trends est obligatoire pour les meilleurs produits et recommandé pour toute idée survivante.
Pour la France :

1. Régler le pays sur **France**.
2. Régler la période sur **cinq dernières années** par défaut.
3. Utiliser **Recherche sur le Web**, sauf raison explicite de choisir Shopping ou YouTube.
4. Comparer jusqu'à 5 formulations proches, puis isoler les finalistes si l'échelle écrase un terme.
5. Relever : indice moyen, évolution 52 dernières semaines vs 52 précédentes si possible,
   évolution 13 dernières semaines vs 13 précédentes si possible, saisonnalité, régions et requêtes
   associées.
6. Télécharger le CSV quand l'interface le permet et utiliser ce fichier pour calculer les moyennes
   plutôt qu'une lecture approximative du graphique.
7. Si l'API, une librairie ou l'automatisation bloque avec un rate limit, un CAPTCHA, un timeout ou
   une erreur technique, ouvrir l'interface Google Trends dans un navigateur réel et récupérer au
   minimum les indices moyens et la tendance visuelle.
8. Si Trends reste inaccessible, le signaler dans le livrable et ne pas présenter le produit comme
   pleinement validé Google Demand.

Google Trends ne remplace jamais DataForSEO : Trends mesure un intérêt relatif ; DataForSEO donne les
volumes, CPC et séries disponibles. Les deux doivent être croisés avant une recommandation technique.

Signaux Shopping :

- requête produit claire ;
- résultats Shopping déjà actifs ;
- image/prix déterminants ;
- produit compréhensible en 2 secondes ;
- titre produit optimisable ;
- concurrence visible mais pas parfaitement optimisée.

Signaux Search :

- requêtes problème/solution ;
- besoin de comparaison ;
- produit cher ou impliquant ;
- objections nombreuses ;
- nécessité de storytelling, preuve, FAQ et pédagogie.

## Étape 5 — Audit SERP et benchmark concurrentiel

Pour chaque produit intéressant :

- ouvrir les pages DTC, mono-produit, DNVB ou e-commerce spécialisés comparables ;
- ignorer les marketplaces comme concurrents directs ;
- analyser la home et la fiche produit ;
- identifier le canal probable : Shopping, Search, Meta, TikTok, SEO ;
- vérifier les ads via Google Ads Transparency Center, Meta Ad Library, TikTok Creative Center ou
  outils payants.

Séparer explicitement deux listes :

- **Concurrents DTC/spécialisés comparables** : boutiques, spécialistes, marques, sites mono-produit
  ou e-commerce de niche qui aident à comprendre l'offre, la conversion et le positionnement.
- **Repères marketplaces / grandes enseignes** : Amazon, Cdiscount, ManoMano, Leroy Merlin, Darty,
  Fnac, Decathlon, BUT, Conforama, etc. Ils servent seulement à borner les prix, identifier les
  standards de marché et repérer les offres trop commoditisées.

Un produit ne peut pas être GO sans au moins 2 à 4 concurrents ou spécialistes comparables analysés.
Si aucun concurrent DTC/spécialisé comparable n'existe, formuler le risque clairement : soit le
marché est trop marketplace, soit l'angle DTC reste à prouver.

Analyse CRO par concurrent :

- promesse hero ;
- structure de page ;
- ordre des arguments ;
- bénéfices ;
- prix et prix barrés ;
- bundles ;
- garanties ;
- livraison ;
- retours ;
- FAQ ;
- images ;
- preuves ;
- CTA ;
- friction panier ;
- conformité ;
- points forts à reprendre ;
- points faibles à éviter ;
- opportunités pour faire mieux.

Ne jamais copier un concurrent faible. Le benchmark sert à trouver des opportunités, pas à imiter.

Pour chaque concurrent, formuler une conclusion stratégique :

- "Il gagne probablement grâce à..." ;
- "Il est faible sur..." ;
- "Nous pouvons faire mieux en..." ;
- "À ne surtout pas reprendre..." ;
- "Notre angle serait différent parce que...".

Le but n'est pas d'être un clone plus joli, mais de trouver un terrain de jeu où la future marque a
une raison d'exister.

## Étape 5b — Thèse de différenciation

Avant de scorer un produit, écrire une thèse en une phrase :

> Pour [persona précis] qui souffre de [problème], vendre [produit/offre] comme [angle] afin de
> produire [bénéfice émotionnel/concret], contrairement aux concurrents qui [faiblesse].

Variante high-ticket / désir :

> Pour [persona précis] qui veut [désir/univers], vendre [produit/offre] comme [angle esthétique,
> pratique ou premium] afin de créer [bénéfice émotionnel/concret], contrairement aux concurrents
> qui [faiblesse].

Exemples de types de différenciation acceptables :

- persona spécifique : hommes 30-45, jeunes parents en appartement, femmes sport maison, etc. ;
- usage spécifique : voyage, télétravail, petit espace, post-partum, sommeil, enfant, senior ;
- bénéfice concret : gain de place, confort, confiance, simplicité, sécurité, autonomie ;
- désir esthétique : intérieur plus harmonieux, cuisine plus premium, salle de bain mieux rangée,
  chambre enfant plus douce, objet qui donne envie d'être montré ;
- design/premiumisation : produit banal mais perception haut de gamme et usage quotidien valorisé ;
- bundle/système : kit complet plutôt qu'objet isolé ;
- pédagogie : expliquer mieux un produit mal compris ;
- sélection : choisir une variante meilleure que les alternatives génériques ;
- service/réassurance : livraison, guide, garantie, support, installation, entretien.

Différenciations faibles :

- "moins cher" seulement ;
- "meilleure qualité" sans preuve ;
- "premium" sans traduction visible ;
- "vu sur TikTok" ;
- "les concurrents le vendent donc nous aussi" ;
- changement de couleur ou nom de marque sans bénéfice client.

Sans thèse claire, le produit ne peut pas être GO.

## Étape 6 — Validation fournisseur

Pour chaque produit en shortlist :

- fournisseur AliExpress vérifié via Computer Use ;
- URL AliExpress ;
- prix produit ;
- prix livré ;
- nombre de commandes AliExpress ;
- note produit / étoiles AliExpress ;
- notation vendeur AliExpress ;
- pays d'expédition ;
- délai ;
- expédié depuis Europe : oui/non ;
- MOQ si Alibaba ;
- variantes ;
- stock ;
- qualité images ;
- avis ;
- historique vendeur ;
- présence de fournisseur backup ;
- risque de marque tierce / watermark ;
- possibilité de facture HT / TVA intracom.

Classer le risque fournisseur :

- Faible : fournisseur crédible, note >= 4,5, commandes suffisantes, expédition Europe ou délai
  France court, stock, backup, images exploitables.
- Moyen : fournisseur correct mais délai/stock/images/commandes à surveiller.
- Fort : fournisseur fragile, note < 4,5, peu de ventes, délais longs, specs floues, pas de backup
  ou fournisseur AliExpress non confirmé.

## Étape 7 — Calcul business

Raisonner en SASU/OH Ventures :

- prix fournisseur livré ;
- TVA récupérable ou non ;
- prix TTC cible ;
- chiffre d'affaires HT ;
- coût produit HT ou coût TTC non récupérable ;
- marge brute HT ;
- marge après IS estimée ;
- CAC break-even ;
- panier moyen potentiel ;
- cross-sell/accessoires ;
- seuil de livraison offerte ;
- budget test recommandé.

Règle : si le CAC max est trop bas pour Google Ads, le produit est NO-GO ou doit être repositionné.

## Étape 8 — Scoring

Attribuer une note sur 100 :

| Critère | Points |
|---|---:|
| Google Demand | 20 |
| Shopping Potential | 15 |
| Search Potential | 15 |
| Marge & CAC | 15 |
| Fournisseur | 10 |
| Différenciation & valeur ajoutée | 15 |
| CRO Opportunity | 10 |

Interprétation :

- 80+ : GO deep research.
- 65-79 : MAYBE, creuser ou attendre meilleur fournisseur/angle.
- <65 : NO-GO.

Shopping Score :

- produit visuel ;
- requête produit claire ;
- image/prix compétitifs ;
- feed optimisable ;
- faible besoin d'éducation.

Search Score :

- douleur explicite ;
- requêtes problème/solution ;
- besoin de comparaison ;
- panier suffisant ;
- landing page persuasive utile.

Business Score :

- marge ;
- fournisseur ;
- différenciation réelle ;
- valeur ajoutée possible ;
- conformité ;
- faisabilité Shopify ;
- potentiel de panier moyen.

Pénalités automatiques :

- Produit ou cluster France sous **10 000 recherches mensuelles pertinentes** : hors shortlist ou
  NO-GO. Ne pas compenser ce manque par un bon fournisseur, une belle marge ou un bon angle.
- Produit dropshipping rincé sans angle neuf : ne devrait pas entrer en shortlist ; si détecté
  après coup, NO-GO.
- Produit sans problème clair ni désir high-ticket défendable : -15 à -30.
- Produit uniquement copié d'un concurrent : -20.
- Produit bizarre / agricole / poulailler / trop éloigné DTC grand public : NO-GO sauf demande
  explicite d'Hakim.
- Produit avec claims santé/minceur non prouvables : NO-GO ou MAYBE uniquement avec angle conforme.
- Produit sans marge Google Ads : NO-GO.
- Produit déjà présent dans une recherche précédente : NO-GO, sauf demande explicite de reprise ou
  thèse réellement nouvelle documentée.
- Produit sans fournisseur AliExpress exploitable ou alternative fournisseur crédible : pas de GO.

## Étape 9 — Verdict et recommandation

Pour chaque produit :

- verdict ;
- canal recommandé ;
- pourquoi maintenant ;
- problème résolu ;
- désir/univers adressé si applicable ;
- thèse de différenciation ;
- valeur ajoutée que la boutique peut apporter ;
- pourquoi ce n'est pas un produit dropshipping rincé ;
- risque principal ;
- condition de GO ;
- angle de test ;
- prochain livrable si sélectionné.

Pour les meilleurs produits :

- proposer ordre de priorité ;
- dire quel produit lancer en premier ;
- dire quel produit garder en réserve ;
- dire quels produits couper sans regret.

## Étape 10 — Passage au playbook boutique

Quand Hakim valide un produit :

1. Créer ou remplir le brief `templates/new-boutique-intake.template.md`.
2. Démarrer `PLAYBOOK.md`.
3. Lancer `python3 scripts/new_boutique.py <nom-projet>`.
4. Reporter les hypothèses clés dans `research-brief.md` et `project-state.md`.

## Format de réponse recommandé

Répondre en 4 blocs :

1. **Synthèse** : nombre de produits analysés, top 3, canal recommandé.
2. **Shortlist scorée** : tableau compact.
3. **Deep dive top produits** : pourquoi ça peut marcher, risques, fournisseurs, concurrents.
4. **Décision** : produit recommandé, prochaines actions, questions bloquantes.

Ajouter aussi :

- le nom de la feuille Google Sheet créée/remplie ;
- les limites éventuelles : Trends bloqué, prix fournisseur non livré, DataForSEO indisponible,
  concurrent audit incomplet, etc. ;
- les sources principales utilisées, en distinguant DataForSEO, Google Trends, SERP/Shopping,
  concurrents DTC/spécialisés et fournisseurs.

### Checklist avant livraison

Avant de répondre, vérifier explicitement :

- l'historique des feuilles précédentes a été consulté pour éviter les doublons, ou le blocage est
  déclaré ;
- chaque appel DataForSEO utilise **France / français**, avec endpoint et date documentés ;
- chaque produit retenu atteint le seuil DataForSEO de son mode dans `PRODUCT-RESEARCH-CRITERIA.md` ;
- Google Trends a été vérifié ou l'échec est déclaré ;
- AliExpress a été vérifié via Computer Use pour chaque idée notée, ou l'échec est déclaré ;
- les colonnes AliExpress obligatoires sont remplies : prix, commandes, note, notation vendeur,
  délai, expédié depuis Europe oui/non, URL ;
- les concurrents DTC/spécialisés sont séparés des marketplaces et grandes enseignes ;
- chaque GO a une thèse de différenciation en une phrase ;
- les produits faibles ne sont pas gardés pour faire du volume ;
- la shortlist contient toutes les colonnes obligatoires ;
- le Google Sheet a été créé/rempli, ou le blocage est signalé ;
- aucune donnée United States n'est utilisée pour valider un produit France.

## Garde-fous

- Ne pas recommander un produit seulement parce qu'il est viral.
- Ne pas retenir en shortlist un candidat sous le seuil DataForSEO de son mode.
- Ne pas sourcer volontairement des produits mainstream/rincés sans angle neuf et crédible.
- Ne pas reproposer un produit déjà recherché dans une feuille précédente, sauf demande explicite ou
  nouvelle thèse documentée.
- Ne pas recommander un produit juste parce qu'un concurrent le vend.
- Ne pas recommander un produit qui ne résout aucun problème, ne nourrit aucun désir clair et
  n'améliore aucune situation.
- Ne pas recommander un produit si la seule différenciation possible est une couleur, un logo ou une
  baisse de prix.
- Ne pas recommander un produit si la marge ne laisse pas respirer Google Ads.
- Ne pas recommander un produit si les claims nécessaires sont trop risqués.
- Ne pas recommander un produit si le fournisseur est l'unique point de rupture et qu'aucun backup
  n'est identifié.
- Ne pas recommander en GO un produit dont le fournisseur AliExpress vérifié a une note inférieure à
  4,5, une notation vendeur faible, des commandes insuffisantes ou une livraison trop longue.
- Ne pas confondre forte demande marketplace et opportunité DTC.
- Ne pas sortir une shortlist sans verdict clair.
- Ne pas remplir le tableau pour remplir le tableau : chaque GO doit avoir une raison stratégique
  d'exister.
- Ne pas prétendre avoir vérifié Google Trends, Google Shopping, DataForSEO, fournisseurs ou
  concurrents si l'étape n'a pas été réellement faite.
- Ne pas donner une réponse finale conforme au playbook si le Google Sheet obligatoire n'a pas été
  rempli ou si le blocage n'a pas été clairement signalé.
