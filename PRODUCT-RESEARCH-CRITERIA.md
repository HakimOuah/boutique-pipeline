# Critères canoniques de recherche produit

Dernière mise à jour : 23 août 2026 (décisions Hakim post-revues Fable 5 + ChatGPT Pro : émetteur du pass, vocabulaire `TECHNICAL_*`, plancher de sourçabilité UNIVERS, commande test, recherche continue — voir §0. Historique : 19/08 deux modes **PRODUIT PUR** / **UNIVERS**, Brand Search remplacé par TrendTrack, Search ≠ Shopping ; 18/08 plancher 50–400 €. Skills `ideation-produit` / `recherche-mots-cles` / `sourcing-aliexpress`.)

## 0. Décisions du 23/08/2026 (Hakim, après revue croisée Fable 5 + ChatGPT Pro)

1. **Émetteur des verdicts.** `PASS_PREQUALIFICATION` / `REVIEW` / `STOP` = conformité technique (volume, critères) → **émis par l'agent**. Les `REVIEW` et cas limites remontent à Hakim. La recommandation technique de phase 5 est également côté agent. La seule porte humaine de sélection produit est `GO_FINAL` / `WATCH_FINAL` / `NO_GO_FINAL`.
2. **Vocabulaire.** Les recommandations techniques s'écrivent `TECHNICAL_PASS`, `TECHNICAL_WATCH`, `TECHNICAL_FAIL`, `TECHNICAL_INCONCLUSIVE`. Le mot **GO** est réservé à la décision de Hakim. (Motif : la confusion s'est déjà produite — des lots de sourcing de la salve 30×30 ont été titrés « GO » alors qu'ils signifiaient « fiche trouvée, à tester ».)
3. **Sources de mesure.** SEMrush France (`db=fr`) reste **la loi**. DataForSEO et Ahrefs sont des replis documentés si SEMrush est indisponible ; tout chiffre rendu sur repli le signale, et un pass rendu sur repli le signale aussi. DataForSEO garde un rôle légitime de **filtre d'expansion peu coûteux** en amont (Product Factory), jamais de source de gate.
4. **Registre = référence.** `registre-candidats.md` (GitHub) est le système de référence des candidats. Tout état d'opportunité créé ailleurs (dont le state store de la Product Factory) doit référencer son entrée de registre ; l'anti-doublon se joue à l'entrée, systématiquement — d'autant plus que la recherche devient continue (point 7).
5. **Commande test.** Elle est passée par **Hakim lui-même**, immédiatement après `GO_FINAL` (latence livraison 1–3 semaines). Le build avance en parallèle sur les étapes gratuites et réversibles (persona, offre, DA) ; le contrôle de l'échantillon reçu (`SAMPLE_OK`) est **bloquant avant GMC/Ads**. `WATCH_FINAL` n'autorise rien : ni build, ni commande test automatique.
6. **UNIVERS.** Décision : construire le pipeline UNIVERS complet (option B) — consolidation par familles, économie de panier, sourcing par famille, boutique multi-collections. **Plancher de sourçabilité** : les 3–5 familles pesant ≥ 70 % du volume consolidé doivent avoir chacune ≥ 2 fournisseurs plausibles avant décision finale. Règle transitoire tant que ce pipeline n'existe pas : **aucun `GO_FINAL` sur un dossier UNIVERS** dont la consolidation par familles et la sourçabilité par famille ne sont pas documentées.
7. **Recherche continue.** La recherche produit fonctionne en veille de marché permanente, en parallèle de la production — avec anti-doublon systématique (point 4) et coût plafonné par candidat (pas de due diligence profonde sans pass).
8. **Autonomie des bots.** Les bots peuvent cliquer un CAPTCHA affiché, accepter CGU et cookies quand une page le demande. Jamais d'outil anti-détection, de proxy tournant ni de contournement technique ; blocage persistant = arrêt déclaré.

Ce document est le référentiel à appliquer à toutes les nouvelles recherches produit du pipeline.

## 1. Périmètre commercial

- Marché prioritaire : France. Royaume-Uni et Allemagne dans un second temps.
- Prix de vente cible : 50 à 400 € TTC. Un gadget drop 15–20 € n'est pas un candidat.
- **Deux modes, choisis en phase 0, jamais mélangés :**
  - **PRODUIT PUR** (ex. osmoseur) : un phare + complémentaires, Search pédagogique. Seuil : cluster adressable de l'ordre de **10 000**/mois ; un 9 900 passe (cas d'école Bonum Vitae). Shopping après validation.
  - **UNIVERS** (ex. gothique, montres, sacs) : dizaines de collections, Shopping visuel. Seuil : volume **consolidé par familles** qu'une même boutique servirait — plancher Kraken **30 000** boutique (confort 40 000). Une tête seule ne mesure pas un univers (leçon 08/08, ×2 à ×6).
- Ne jamais gonfler le volume avec des requêtes informationnelles hors produit, des prestations, des accessoires incompatibles, des marques concurrentes ou du low-ticket non comparable. En UNIVERS, additionner des collections d'un même catalogue n'est pas du gonflage.

## 2. Sources d'idées

**Source principale depuis le 19 août 2026 : TrendTrack seulement** (Google Ads Search ou Shopping selon le mode, shops, Meta/TikTok comme signal d'univers). Recette : skill `ideation-produit` et agent `mineur-brandsearch` (mineur TrendTrack, identifiant conservé). Mesure = `recherche-mots-cles` (y compris Google Trends). Fournisseur = `sourcing-aliexpress`, uniquement après `PASS_PREQUALIFICATION` écrit.

**Source secondaire :** Amazon, VEVOR, Flippa, Europages, balayage familles — sur demande.

**Brand Search n'est plus une source** (décision Hakim 19/08/2026 : TrendTrack fait le même travail). Les rapports historiques « vague Brand Search » restent de l'anti-doublon. Les visites Brand Search n'ont jamais fondé un verdict.

L'exploration s'élargit ensuite par **SEMrush lui-même** : les sous-groupes du Keyword Magic Tool révèlent les sous-niches autour de chaque idée mesurée, et les associations d'idées (une boutique d'étanchéité → béton ciré → rénovation décorative) alimentent des idées latérales qui suivent la même chaîne complète.

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
- Une matière comme le rotin ne suffit pas : forme, usage, modularité ou positionnement doivent être distinctifs.

Exclusions explicites : bureaux assis-debout, chaises gaming, tables basses génériques, canapés standards et meubles courants sans usage différencié.

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
- CPC compatible avec le CPA supportable.
- Poids, dimensions, casse, retours et SAV raisonnables.
- Stock et livraison France/UE satisfaisants.
- Caractéristiques techniques vérifiables sur échantillon.
- Conformité CE/RoHS et autres exigences applicables vérifiables.
- Vigilance renforcée pour les produits électriques, les produits enfants et les allégations liées à la santé.

## 7. Ordre obligatoire du pipeline

Deux chemins d'entrée (A idée / B balayage) et **deux modes** (PRODUIT PUR / UNIVERS). Les chemins disent d'où vient l'idée. Les **portes de volume et de canal dépendent du mode** (§1). On ne tue pas un univers avec le seuil d'un cluster, ni un osmoseur avec le plancher 30 000. Google Trends avant tout GO : platitude ~5 ans en PRODUIT PUR, socle ≥ 8 mois en UNIVERS.

### Chemin A — entrée par l'idée, avec mesure express (voie principale depuis le 20/07/2026)

Utilisé pour toute idée produit, qu'elle vienne de Hakim ou d'une salve d'idéation (`/qualifie-idees`, ou `/recherche-produit` pour une recherche cadrée).

1. Idée trouvée sur les sources d'inspiration ou apportée par Hakim.
2. **Mesure express, avant tout travail qualitatif.** PRODUIT PUR : volume du cluster (niveaux séparés) + sonde prix. UNIVERS : familles / collections à consolider, **pas une tête seule**, + sonde sur les catégories cœur. Une idée nettement sous le seuil **de son mode** meurt ici ; un ticket 15–20 € part en vivier. Google Trends dans la même passe ou juste après, avant le GO.
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

4. Analyse Google Search, Shopping, publicités, concurrents et prix — **le nettoyage SERP est obligatoire quel que soit le chemin.** Un volume mesuré à l'outil n'est jamais un volume adressable tant que la SERP n'a pas été lue.
5. Vérification du mode économique : capacité à défendre une offre entre 50 et
   400 EUR, ou panier/marge potentiels crédibles en
   `catalogue-volume`.
6. Porte intermédiaire : `PASS_PREQUALIFICATION`, `STOP_PREQUALIFICATION` ou `REVIEW_PREQUALIFICATION`. Le pass autorise uniquement la due diligence concurrence + sourcing ; aucun GO commercial n'est encore prononcé.
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

**Source de mesure du volume** : SEMrush France (`db=fr`). Ahrefs et DataForSEO ne sont que des replis documentés si SEMrush est indisponible, et un verdict rendu sur repli doit le signaler (décision Hakim 23/08/2026 — DataForSEO reste autorisé comme filtre d'expansion peu coûteux en amont, jamais comme source de gate).
