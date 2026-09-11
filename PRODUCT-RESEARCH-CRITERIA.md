# Critères canoniques de recherche produit

Dernière mise à jour : 11 septembre 2026 (décisions Hakim, chemin SMP : UNIVERS ≥ 30 000 net de marque + ≥ 800 par collection, sans plafond SKU, prix visé ≥ 50 € avec 30–40 € possibles, CPC par bande de prix, passe Ads = repère, animalerie exclue, volume OneClickBrand/Semrush valide — voir §0 bis. Historique : 01/09 DataForSEO seule source de mesure et de gate ; 29/08 seuils DataForSEO recalibrés ; 23/08 émetteur du pass, vocabulaire `TECHNICAL_*`, plancher de sourçabilité UNIVERS, commande test, recherche continue ; 19/08 deux modes **PRODUIT PUR** / **UNIVERS**, Brand Search remplacé par TrendTrack, Search ≠ Shopping ; 18/08 plancher 50–400 €.)

## 0 bis. Décisions du 11/09/2026 (Hakim, chemin SMP)

Ces décisions priment sur les sections plus anciennes du document là où elles divergent. Le canon des skills est dans le hub `boutiques-drop` (`METHODE-ANALYSE-MARCHE.md`, skills `recherche-mots-cles`, `ideation-produit`, `qualifie-idees`, agent `phase3-demande`).

1. **Mode par défaut : UNIVERS.** Le chemin SMP (mini-marque, muse) est un chemin UNIVERS. PRODUIT PUR (seuil 12 500) seulement sur demande explicite de Hakim, hors SMP.
2. **Gate volume (dur).** Deux conditions **ensemble** :
   - niche **≥ 30 000 recherches/mois net de marque**. On retire les requêtes « marque + produit ». Les fautes d'orthographe et les graphies sans accent **comptent** : tout bucket distinct s'ajoute. Une paire que Google fusionne (même série mensuelle) ne compte qu'une fois, au MAX du bucket, jamais en somme (garde-fou n° 3 de `METHODE-ANALYSE-MARCHE.md`) ;
   - **≥ 800 recherches/mois sur le mot-clé courte traîne de chaque collection.** Sous 800, la page ne se crée pas.

   Une SERP dominée par des généralistes (Amazon, Vevor, GSB, marketplaces) **ne retranche pas** de volume. La lecture SERP garde son rôle contre les contaminations (autre sens, service, informationnel hors produit), qui restent des retraits motivés.
3. **Pas de plafond SKU.** Le catalogue grandit tant que le sourcing reste facile et que la marge s'applique.
4. **Prix.** Viser **≥ 50 €**. Un produit à **30–40 €** reste acceptable si la marge tient. Les prix à décimales sont admis (39,90 €, 54,90 €). Le 50 € n'est plus un plancher dur.
5. **Gate CPC (dur, avec le volume)**, lu dans la bande de prix du produit :
   - **Low ticket** (prix jusqu'à 50 €) : CPC **0 à 0,40 €** ;
   - **Mid ticket** (prix de 50 à 500 €) : CPC **0,40 à 0,60 €** ;
   - **High ticket** (prix au-dessus de 500 €) : CPC **0,60 à 1 €**.

   CPC hors de sa bande = pas de `PASS_PREQUALIFICATION`, sauf cas limite motivé quand la lecture est incomplète. La devise du CPC est lue dans la réponse, jamais présumée.
6. **Passe Ads concurrents : recommandée, pas un veto.** TrendTrack en priorité, sinon Google Ads Transparency (`https://adstransparency.google.com`, qui donne un *Last shown*, pas un *First Seen*). Une ligne par concurrent : domaine · First Seen / Time Running · Search ou Shopping · source. **6 mois sert de repère** de preuve solide, pas de couperet : un concurrent actif depuis 3 à 5 mois reste intéressant et s'écrit « 4 mois, encore court ». Une passe non faite est un **gap** noté ; elle ne bloque pas le PASS. Le minage 60–90 jours de l'idéation n'est pas cette passe, et on ne mélange jamais les deux fenêtres dans une même requête.
7. **Animalerie exclue.** Destination animal : accessoires chiens et chats, aquariophilie, terrariophilie, apiculture, petit élevage. Le **thème animal** reste autorisé (chaussons koala, bouillottes peluche).
8. **Sources d'idées.** TrendTrack, OneClickBrand et les généralistes (Amazon, Vevor, best-sellers de marketplaces, trends réseaux) sont au même rang pour inspirer. Les généralistes sont conservés comme source d'idées ; ils ne sont ni des fournisseurs ni des concurrents à copier.
9. **Volume OneClickBrand = Semrush : il compte.** Hakim fait confiance à ce chiffre. Il se note avec la source `OCB/Semrush`, la date et le pays. DataForSEO reste le gate de l'étude rapide. Les deux se recoupent : un écart se documente, on ne jette pas le chiffre OCB, et OCB ne devient jamais le seul gate par repli silencieux.
10. **OneClickBrand Trend Niche : deux passes.** Une passe filtrée **Facile (difficulté 0–40)** et une passe **sans filtre de difficulté**, sinon on rate des niches. Le filtre High Ticket sert à trier, pas à couper.

## 0. Décisions du 23/08/2026 (Hakim, après revue croisée Fable 5 + ChatGPT Pro)

1. **Émetteur des verdicts.** `PASS_PREQUALIFICATION` / `REVIEW` / `STOP` = conformité technique (volume, critères) → **émis par l'agent**. Les `REVIEW` et cas limites remontent à Hakim. La recommandation technique de phase 5 est également côté agent. La seule porte humaine de sélection produit est `GO_FINAL` / `WATCH_FINAL` / `NO_GO_FINAL`.
2. **Vocabulaire.** Les recommandations techniques s'écrivent `TECHNICAL_PASS`, `TECHNICAL_WATCH`, `TECHNICAL_FAIL`, `TECHNICAL_INCONCLUSIVE`. Le mot **GO** est réservé à la décision de Hakim. (Motif : la confusion s'est déjà produite — des lots de sourcing de la salve 30×30 ont été titrés « GO » alors qu'ils signifiaient « fiche trouvée, à tester ».)
3. **Source de mesure.** **DataForSEO API est le gate de l'étude rapide.** Toute requête utilise `location_name: France` et `language_name: French`. `dataforseo_labs/google/keyword_suggestions` sert à découvrir et nettoyer les clusters ; `keywords_data/google_ads/search_volume/live` sert à contrôler précisément les têtes et les mots décisifs. *Amendé le 11/09/2026 (§0 bis.9) :* le volume OneClickBrand (données Semrush) compte et se recoupe avec DataForSEO. Aucun verdict ne dépend d'Ahrefs ou d'un volume lu dans une interface tierce sans source nommée.
4. **Registre = référence.** `registre-candidats.md` (GitHub) est le système de référence des candidats. Tout état d'opportunité créé ailleurs (dont le state store de la Product Factory) doit référencer son entrée de registre ; l'anti-doublon se joue à l'entrée, systématiquement — d'autant plus que la recherche devient continue (point 7).
5. **Commande test.** Elle est passée par **Hakim lui-même**, immédiatement après `GO_FINAL` (latence livraison 1–3 semaines). Le build avance en parallèle sur les étapes gratuites et réversibles (persona, offre, DA) ; le contrôle de l'échantillon reçu (`SAMPLE_OK`) est **bloquant avant GMC/Ads**. `WATCH_FINAL` n'autorise rien : ni build, ni commande test automatique.
6. **UNIVERS.** Décision : construire le pipeline UNIVERS complet (option B) — consolidation par familles, économie de panier, sourcing par famille, boutique multi-collections. **Plancher de sourçabilité** : les 3–5 familles pesant ≥ 70 % du volume consolidé doivent avoir chacune ≥ 2 fournisseurs plausibles avant décision finale. Règle transitoire tant que ce pipeline n'existe pas : **aucun `GO_FINAL` sur un dossier UNIVERS** dont la consolidation par familles et la sourçabilité par famille ne sont pas documentées.
7. **Recherche continue.** La recherche produit fonctionne en veille de marché permanente, en parallèle de la production — avec anti-doublon systématique (point 4) et coût plafonné par candidat (pas de due diligence profonde sans pass).
8. **Autonomie des bots.** Les bots peuvent cliquer un CAPTCHA affiché, accepter CGU et cookies quand une page le demande. Jamais d'outil anti-détection, de proxy tournant ni de contournement technique ; blocage persistant = arrêt déclaré.

Ce document est le référentiel à appliquer à toutes les nouvelles recherches produit du pipeline.

## 1. Périmètre commercial

- Marché prioritaire : France. Royaume-Uni et Allemagne dans un second temps.
- Prix de vente cible : viser **≥ 50 € TTC** ; **30–40 €** acceptable si la marge tient ; décimales admises (§0 bis.4). Au-dessus de 500 €, la bande CPC High ticket s'applique. Un gadget drop 15–20 € n'est pas un candidat.
- **Deux modes, choisis en phase 0, jamais mélangés :**
  - **PRODUIT PUR** (ex. osmoseur) : un phare + complémentaires, Search pédagogique. Seuil DataForSEO : cluster adressable de l'ordre de **12 500**/mois. Shopping après validation. **Hors chemin SMP**, sur demande explicite de Hakim.
  - **UNIVERS** (ex. gothique, montres, sacs) : dizaines de collections, Shopping visuel, **sans plafond SKU**. Mode par défaut du chemin SMP. Gate volume : niche **≥ 30 000/mois net de marque** consolidée par familles qu'une même boutique servirait, **et ≥ 800/mois** sur le mot-clé courte traîne de chaque collection (sous 800, la page ne se crée pas). Fautes et graphies sans accent incluses, sans retrait pour SERP généraliste (§0 bis.2). Une tête seule ne mesure pas un univers (leçon 08/08, ×2 à ×6). *L'ancien plancher de 37 500 (confort 50 000) est abandonné le 11/09/2026.*
- **Gate CPC (dur, avec le volume)** : Low ticket ≤ 50 € → CPC 0–0,40 € ; Mid ticket 50–500 € → 0,40–0,60 € ; High ticket ≥ 500 € → 0,60–1 € (§0 bis.5).

**Base de mesure — décisions Hakim des 29/08, 01/09 et 11/09/2026.** Le gate de l'étude rapide se lit dans **DataForSEO** ; chaque chiffre porte la date, les paramètres France/français, l'endpoint et la chaîne exacte qui le produit. Depuis le 11/09, un volume **OneClickBrand/Semrush** compte aussi : il s'écrit à côté, avec sa source, sa date et son pays, et se recoupe avec DataForSEO sans être jeté (§0 bis.9). Le gate 12 500 a été recalibré sur DataForSEO à partir de comparaisons historiques. Deux nuances vérifiées le 29/08 :

  - la **dispersion tête à tête est forte** (écart-type 2,65, étendue ×0,03 à ×31) : le facteur ajuste un seuil, il ne convertit jamais un mot-clé isolé ;
  - **le consolidé est plus stable que ses composants.** Rejeu du dossier rideaux : +25 % sur les têtes mais **−4,8 % sur le consolidé** (614 130 contre 645 340), verdict identique, familles de tête identiques. Les deux biais se compensent — la méthode SEMrush additionnait des formulations que Google sert dans un seul bucket. Détail : `analyses/2026-08-29-rejeu-rideaux-dataforseo.md`.

**Ce que le rejeu n'a PAS testé** : la zone de décision. Le dossier rideaux est à ×16 du seuil, c'est le test le moins exigeant possible. Les écarts par famille vont de ×0,62 à ×1,27 — sur un dossier à ±20 % du seuil, cela suffirait à faire basculer un verdict. **Un rejeu sur un dossier proche du seuil, ou conclu STOP, reste à faire.**
- Ne jamais gonfler le volume avec des requêtes informationnelles hors produit, des prestations, des accessoires incompatibles, des marques concurrentes ou du low-ticket non comparable. En UNIVERS, additionner des collections d'un même catalogue n'est pas du gonflage. Compter une faute d'orthographe ou une graphie sans accent qui forme un bucket distinct n'en est pas non plus ; retirer du volume parce que la page 1 est tenue par des généralistes est en revanche interdit sur le chemin SMP.

## 2. Sources d'idées

> **Orientation Q4 du 03/09/2026, avant implémentation :** Hakim demande de coupler la découverte par requêtes à TrendTrack et d'élargir le scouting au-delà des deux vues sauvegardées. [Constats du test et méthode proposée](analyses/2026-09-03-test-decouverte-search-12/orientation-decouverte-couplee.md). Cette orientation est documentée ; la recette active ci-dessous, les seuils et les gates ne sont pas modifiés à ce stade.

**Sources d'idées depuis le 11/09/2026 : TrendTrack, OneClickBrand et généralistes, au même rang** (§0 bis.8).

- **TrendTrack** : Google Ads Search ou Shopping selon le mode, shops, Meta/TikTok comme signal d'univers. Recette : skill `ideation-produit` et agent `mineur-brandsearch` (mineur TrendTrack, identifiant conservé).
- **OneClickBrand (Trend Niche)** : niches France, données Semrush. Deux passes, une filtrée Facile (difficulté 0–40) et une sans filtre de difficulté (§0 bis.10). Le volume lu compte, noté `OCB/Semrush`.
- **Généralistes** : Amazon, Vevor, best-sellers de marketplaces, Flippa, Europages, trends Meta / TikTok / Pinterest. Conservés comme source d'idées ; un hit Amazon ou Vevor est une piste à mesurer, pas un STOP.

Mesure = `recherche-mots-cles` (y compris Google Trends). Fournisseur = `sourcing-aliexpress`, uniquement après `PASS_PREQUALIFICATION` écrit.

**Modalité d'accès TrendTrack (décision Hakim 23/08/2026)** : les bots Grok utilisent TrendTrack **dans leur navigateur** (app web, mêmes modules et filtres via l'interface) — jamais l'API, dont la clé ne doit pas vivre sur la machine cloud partagée. Les recettes API `/v1/...` restent réservées à Claude Code en local.

**Veille continue (23/08/2026)** : les généralistes et le balayage familles tournent **en rotation autonome** dans la veille, sans demande explicite, avec la même discipline : anti-doublon registre d'abord, mesure avant filtre qualitatif.

**Brand Search n'est plus une source** (décision Hakim 19/08/2026 : TrendTrack fait le même travail). Les rapports historiques « vague Brand Search » restent de l'anti-doublon. Les visites Brand Search n'ont jamais fondé un verdict.

L'exploration s'élargit ensuite par **DataForSEO Labs** : la table des thèmes co-occurrents produite par `kw_dfs.py` et les suggestions plein texte révèlent les sous-niches autour de chaque idée mesurée. Les associations d'idées (une boutique d'étanchéité → béton ciré → rénovation décorative) alimentent des idées latérales qui suivent la même chaîne complète.

Ces sources servent uniquement à trouver et préqualifier des idées. **Le fournisseur doit exclusivement être trouvé sur AliExpress, uniquement après `PASS_PREQUALIFICATION` écrit.** Ce pass autorise la due diligence ; il ne constitue jamais le `GO_FINAL`.

## 3. Profils de produits recherchés

**Cible : le particulier, toujours.** Le levier n'est pas « anti-technique » : un produit **technique-particulier** (osmoseur) se vend en Search. Le STOP, c'est le **technique-pro** (poste à souder, plieuse, presse) — acheteur expert, devis, facture pro. Cas d'école : plieuse zinc.

**Signal d'exclusion — persona professionnel** : un vocabulaire de métier dans le cluster (nom de profession, chantier, devis, location, occasion massive, formation) indique un acheteur pro. C'est un motif d'exclusion ou de vivier, pas de poursuite. Cas d'école documenté : la plieuse zinc (vocabulaire de couvreur — chantier, location, « parisienne ») a coûté une chaîne complète avant que ce signal soit lu.

Un candidat peut appartenir à une ou plusieurs familles :

- produit **explicable** nécessitant pédagogie et aide au choix, destiné au particulier ;
- produit qui résout un problème précis, fréquent et suffisamment gênant ;
- produit à forte valeur perçue ;
- produit offrable ou visuellement désirable pour le Q4 ;
- ameublement niché, transformable, modulaire ou destiné à un usage/public précis ;
- produit fondé sur une matière ou un savoir-faire distinctif, notamment le rotin ;
- produit permettant l'achat en quantité, des bundles, accessoires ou extensions de gamme.

Exemples de problèmes intéressants : sommeil et environnement nocturne, bruit, lumière, chaleur, humidité, posture, qualité de l'eau ou de l'air, sécurité, entretien, diagnostic et réparation.

Pour le sommeil et le bien-être, parler de confort et d'environnement. Écarter les promesses médicales non justifiées et les produits impliquant des allégations thérapeutiques risquées.

## 4. Différenciation obligatoire

- Le produit ne doit pas être un produit banal que le client peut acheter facilement en grande surface.
- Rejeter les produits dominés par IKEA, BUT, Conforama, JYSK, Maisons du Monde, Leroy Merlin, Darty, Decathlon, Lidl ou des équivalents généralistes.
- Rejeter les marchés où l'offre est immédiatement comparable uniquement sur le prix.
- **PRODUIT PUR :** rejeter les catégories dominées par quelques marques si une offre générique n'est pas défendable. **UNIVERS :** s'inspirer d'une marque / d'un spécialiste déjà en place est une preuve, pas un STOP. Occupation = densité + GSB + absence d'espace, pas le premier concurrent.
- **Chemin SMP :** des dropshippers en page 1 prouvent le marché. Une page 1 à 100 % généralistes (Amazon, Vevor, GSB, marketplaces) ne ferme pas le dossier et ne retire pas de volume : on note la faisabilité du sourcing et de la marge, et on continue.
- Une matière comme le rotin ne suffit pas : forme, usage, modularité ou positionnement doivent être distinctifs.

Exclusions explicites : bureaux assis-debout, chaises gaming, tables basses génériques, canapés standards et meubles courants sans usage différencié. **Animalerie** (décision Hakim 11/09/2026) : tout produit dont l'animal est le destinataire — accessoires chiens et chats, aquariophilie, terrariophilie, apiculture, petit élevage. Le **thème animal** reste autorisé : chaussons koala, bouillottes peluche.

Exemple d'ameublement valide : canapé en mousse pour enfant transformable en plateforme ou parcours de motricité.

## 5. Scalabilité

La scalabilité horizontale est un bonus important, mais pas un critère éliminatoire.

Favoriser :

- plusieurs tailles, couleurs, styles ou niveaux de gamme ;
- achat en quantité ou au mètre carré, comme le papier peint ;
- accessoires et consommables ;
- bundles cohérents ;
- achats répétés ;
- extension naturelle du catalogue sans changer de clientèle.

Un produit isolé peut rester candidat s'il surperforme clairement sur tous les autres critères.

## 6. Faisabilité

- Coût rendu et marge permettant de financer Google Ads.
- CPC compatible avec le CPA supportable, et dans la bande de prix du produit (§0 bis.5). Illustration, pas un seuil : CPC moyen 0,60 € → 60 € pour 100 visites ; à 1 % de conversion, 1 achat ; panier 250 €, marge ×2 → 125 € de marge − 60 € = 65 € par article ; CPA = CPC ÷ taux de conversion = 60 €.
- Poids, dimensions, casse, retours et SAV raisonnables.
- Stock et livraison France/UE satisfaisants.
- Caractéristiques techniques vérifiables sur échantillon.
- Conformité CE/RoHS et autres exigences applicables vérifiables.
- Vigilance renforcée pour les produits électriques, les produits enfants et les allégations liées à la santé.

## 7. Ordre obligatoire du pipeline

Deux chemins d'entrée (A idée / B balayage) et **deux modes** (PRODUIT PUR / UNIVERS). Les chemins disent d'où vient l'idée. Les **portes de volume et de canal dépendent du mode** (§1). On ne tue pas un univers avec le seuil d'un cluster, ni un osmoseur avec le plancher UNIVERS. Google Trends avant tout GO : platitude ~5 ans en PRODUIT PUR, socle ≥ 8 mois en UNIVERS.

### Chemin A — entrée par l'idée, avec mesure express (voie principale depuis le 20/07/2026)

Utilisé pour toute idée produit, qu'elle vienne de Hakim ou d'une salve d'idéation (`/qualifie-idees`, ou `/recherche-produit` pour une recherche cadrée).

1. Idée trouvée sur les sources d'inspiration ou apportée par Hakim.
2. **Mesure express, avant tout travail qualitatif.** PRODUIT PUR : volume du cluster (niveaux séparés) + sonde prix. UNIVERS : familles / collections à consolider, **pas une tête seule**, + sonde sur les catégories cœur ; les deux gates durs SMP se lisent ici (30 000 net de marque + 800 par collection, CPC dans la bande de prix). Une idée nettement sous le seuil **de son mode** meurt ici ; un ticket 15–20 € part en vivier. Google Trends dans la même passe ou juste après, avant le GO.
3. Filtre qualitatif : banalité, valeur perçue, problème/usage, avec la fourchette de la sonde comme donnée de prix.

#### Extension obligatoire en mode `catalogue-volume`

Le low ticket est autorisé, mais il ne dispense pas du filtre économique
immédiat. Avant l'étude concurrentielle profonde :

1. relever un échantillon de 30–50 prix visibles sur les catégories cœur ;
2. calculer médiane, part sous 10/15 EUR et nombre d'articles nécessaire pour
   atteindre le seuil de livraison ou le panier cible ;
3. chercher un mécanisme **observé** de panier : lots, kits, quantités,
   réachat, accessoires ou commandes multi-lignes ;
4. si le cœur est autour de 5–10 EUR et qu'aucun panier/marge de commande
   crédible n'est observé, classer `STOP_PRIX_PANIER` immédiatement.

Les 200 produits, le SEO ou un volume Search élevé ne sauvent pas une faible
contribution par commande. Ne jamais inventer un bundle pour faire passer le
gate. Un ticket légèrement supérieur reste conditionné au couple prix/CPC et à
l'économie de commande.

La mesure express existe parce que l'ancien ordre (idée → filtre → validation volume en phase 3) faisait porter tout le travail créatif avant le critère le plus éliminatoire : sur les recherches de juillet 2026, environ 30 candidats sur 50 sont morts sur le volume en phase 3, après filtrage qualitatif complet.

### Chemin B — entrée par le volume (balayage, voie secondaire)

Balayage de familles de marché sans idée préalable (`/chasse-clusters`). Voir `specs/2026-07-20-boucle-chasse-clusters-design.md`.

1. Balayage d'une famille : clusters mesurés en France, sans qu'aucun produit ne soit encore nommé.
2. Sélection des clusters atteignant le seuil, sonde prix.
3. Filtre qualitatif sur les produits attestés par le vocabulaire mesuré.

Bilan du 20/07/2026 (7 familles balayées) : le chemin B élimine bien les morts tardives sur le volume, mais il balaie sans jugement de potentiel (3 familles « machines » verrouillées au §4 traitées en pure perte) et ne peut pas nommer ce que le vocabulaire du marché ne nomme pas encore. Il reste disponible pour de la couverture systématique, en choisissant les familles ; la voie principale est le chemin A avec mesure express.

### Étapes communes aux deux chemins

4. Analyse Google Search, Shopping, publicités, concurrents et prix — **le nettoyage SERP est obligatoire quel que soit le chemin.** Un volume mesuré à l'outil n'est jamais un volume adressable tant que la SERP n'a pas été lue pour les contaminations (autre sens, service, informationnel). Sur le chemin SMP, une page 1 de généralistes ne retire rien. **Passe Ads concurrents** : TrendTrack en priorité, sinon Google Ads Transparency ; 6 mois = repère, 3–5 mois reste intéressant ; recommandée, jamais un veto du PASS (§0 bis.6).
5. Vérification du mode économique : capacité à défendre une offre visée à
   50 € ou plus (30–40 € si la marge tient, §0 bis.4), avec un CPC dans sa bande,
   ou panier/marge potentiels crédibles en `catalogue-volume`.
6. Porte intermédiaire : `PASS_PREQUALIFICATION`, `STOP_PREQUALIFICATION` ou `REVIEW_PREQUALIFICATION`. Sur le chemin SMP, le PASS exige les deux gates durs, volume et CPC ; la ligne Ads est recommandée, son absence est un gap. Le pass autorise uniquement la due diligence concurrence + sourcing ; aucun GO commercial n'est encore prononcé.
7. En parallèle lorsque possible : sourcing exclusivement sur AliExpress et analyse concurrentielle approfondie après vérification SERP.
8. Contrôle exact : SKU, coût rendu, logistique, conformité documentée, marge contributive, densité concurrentielle et droit de gagner. Sortie : recommandation `TECHNICAL_PASS` / `TECHNICAL_WATCH` / `TECHNICAL_FAIL` / `TECHNICAL_INCONCLUSIVE`.
9. Décision humaine finale : `GO_FINAL`, `WATCH_FINAL` ou `NO_GO_FINAL`. Aucun bot ne prononce cette décision à la place de Hakim.
10. Après `GO_FINAL` : commande test passée par Hakim immédiatement ; build en parallèle sur les étapes réversibles ; contrôle échantillon (`SAMPLE_OK`) bloquant avant GMC/Ads (§0.5).

### Ce qui ne change pas

- Les filtres de différenciation GSB / banalité (§4) et le persona pro (§3).
- L'étanchéité : préqualification → concurrence + fiche AliExpress → décision finale → commande test → lancement.
- L'anti-doublon par le registre.
- En PRODUIT PUR : ne pas additionner des familles distinctes (anti-exemple catio).
- En UNIVERS : additionner les collections d'un même catalogue ; ne pas additionner un autre univers.

### Règle de lecture de la concurrence

- **PRODUIT PUR :** un concurrent qui tient le cluster = occupation. **UNIVERS :** un concurrent qui exécute = validation de demande.
- Un concurrent comparable isolé n'impose pas une différenciation radicale :
  une meilleure exécution, une offre plus claire ou une faiblesse exploitable
  peuvent suffire si l'économie passe.
- La concurrence devient éliminatoire par sa densité, ses actifs défensifs ou
  l'absence d'espace exécutable, jamais à la découverte du premier acteur.
- Trafic estimé faible ou absence d'Ads ne prouve ni échec ni rentabilité ; ne
  pas transformer une estimation tierce en verdict commercial.

**Gate de l'étude rapide** : DataForSEO API, `location_name: France`, `language_name: French`. L'indisponibilité de l'API, des identifiants ou du quota arrête ce gate ; aucun autre outil ne remplace silencieusement DataForSEO. **Volume OneClickBrand/Semrush** : il compte, s'écrit avec sa source et se recoupe avec DataForSEO (§0 bis.9) ; il ne devient pas le seul gate par repli.
