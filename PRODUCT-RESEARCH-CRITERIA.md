# Critères canoniques de recherche produit

Dernière mise à jour : 18 août 2026 (§2 : TrendTrack 5 modules = source principale 1 ; Amazon/VEVOR/Flippa/Europages/balayage = source principale 2 ; Brand Search reste une méthode valide, plus la source unique. Skill `recherche-produit-dossier`. 8 août 2026 : §3 « explicable-particulier », §7 chemin A mesure express.)

Ce document est le référentiel à appliquer à toutes les nouvelles recherches produit du pipeline.

## 1. Périmètre commercial

- Marché prioritaire : France. Royaume-Uni et Allemagne dans un second temps.
- Prix de vente cible : 150 à 400 € TTC.
- Acquisition initiale : Google Ads Search. Shopping/Merchant Center seulement après validation.
- Boutique de niche avec un produit phare et des produits complémentaires.
- Seuil éliminatoire : au moins 10 000 recherches mensuelles pertinentes en France pour le cluster réellement adressable.
- Ne jamais gonfler le volume avec des requêtes informationnelles hors produit, des prestations, des accessoires incompatibles, des marques concurrentes ou du low-ticket non comparable.

## 2. Sources d'idées

**Source principale 1 depuis le 18 août 2026 : TrendTrack**, 5 modules d'idéation et d'arbitrage (Early Market, Marketproof & Pivot, Temps Réel / Pages, Saisonnalité, Rétro-ingénierie des Angles). Recette et filtres : skill `recherche-produit-dossier`. Objectif : capter une intention déjà payée ailleurs et l'importer sur le marché FR en Google Ads Search.

**Source principale 2 :** Amazon, VEVOR, Flippa, Europages, balayage familles.

**Brand Search reste une méthode valide** (connecté en MCP) : boutiques d'origine France, 0 publicité Meta active, au moins 1 publicité Google, prix moyen ≥ ~130 $, triées par volume d'annonces Google. Chaque idée extraite est adossée à une boutique preuve. L'agent `mineur-brandsearch` applique cette recette et le §3 dès l'extraction. Ce n'est plus la source unique. Les visites Brand Search ne sont pas fiables et ne fondent jamais un verdict.

L'exploration s'élargit ensuite par **SEMrush lui-même** : les sous-groupes du Keyword Magic Tool révèlent les sous-niches autour de chaque idée mesurée, et les associations d'idées (une boutique d'étanchéité → béton ciré → rénovation décorative) alimentent des idées latérales qui suivent la même chaîne complète.

Ces sources servent uniquement à trouver et valider des idées. **Le fournisseur doit exclusivement être trouvé sur AliExpress, uniquement après verdict marché écrit.**

## 3. Profils de produits recherchés

**Cible : le particulier, toujours.** Précision du 20 juillet 2026, tirée du bilan des balayages 1-4 : le levier gagnant n'est pas « produit technique » mais **« produit explicable au particulier »** — un particulier face à un choix qu'il ne maîtrise pas (osmoseur, fontaine à gravité, tufting), ce qui justifie une boutique spécialisée pédagogique. Ne pas confondre avec le technique-pro (poste à souder, plieuse, presse), où l'acheteur est expert, fidèle aux marques prescriptrices, et où le parcours d'achat (comparaison, devis, facture pro) ne correspond pas au modèle Search → fiche produit.

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
- Rejeter les catégories dominées par quelques marques incontournables si une offre générique ne peut pas être défendue.
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

Deux chemins d'entrée sont légitimes. Ils diffèrent uniquement par **ce qui déclenche l'étude** ; les portes à franchir sont les mêmes et aucune n'est jamais sautée.

### Chemin A — entrée par l'idée, avec mesure express (voie principale depuis le 20/07/2026)

Utilisé pour toute idée produit, qu'elle vienne de Hakim ou d'une salve d'idéation (`/qualifie-idees`, ou `/recherche-produit` pour une recherche cadrée).

1. Idée trouvée sur les sources d'inspiration ou apportée par Hakim.
2. **Mesure express, avant tout travail qualitatif** : volume du cluster de l'idée (SEMrush France, niveaux hiérarchiques séparés) + sonde prix (Google Shopping). Une idée nettement sous le seuil meurt ici, en quelques minutes ; un ticket manifestement low-ticket part en vivier.
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
5. Vérification du mode économique : capacité à défendre une offre entre 150 et
   400 EUR en high-ticket, ou panier/marge potentiels crédibles en
   `catalogue-volume`.
6. Sourcing exclusivement sur AliExpress.
7. Contrôle fournisseur, coût rendu, logistique, conformité et marge.
8. Classement : GO, à approfondir ou rejet documenté.

### Ce qui ne change pas selon le chemin

- Le seuil de volume pertinent (§1) et tous les filtres de différenciation (§4).
- L'interdiction de gonfler un cluster en additionnant des familles de mots-clés distinctes.
- L'étanchéité des quatre niveaux de validation : marché → fiche AliExpress → commande test → lancement.
- L'anti-doublon par le registre central.

### Règle de lecture de la concurrence

- Un concurrent qui exécute déjà le modèle visé est une validation de demande
  et de faisabilité apparente, pas un motif d'arrêt automatique.
- Un concurrent comparable isolé n'impose pas une différenciation radicale :
  une meilleure exécution, une offre plus claire ou une faiblesse exploitable
  peuvent suffire si l'économie passe.
- La concurrence devient éliminatoire par sa densité, ses actifs défensifs ou
  l'absence d'espace exécutable, jamais à la découverte du premier acteur.
- Trafic estimé faible ou absence d'Ads ne prouve ni échec ni rentabilité ; ne
  pas transformer une estimation tierce en verdict commercial.

**Source de mesure du volume** : SEMrush France (`db=fr`). Ahrefs n'est qu'un repli documenté si SEMrush est indisponible, et un verdict rendu sur repli doit le signaler.
