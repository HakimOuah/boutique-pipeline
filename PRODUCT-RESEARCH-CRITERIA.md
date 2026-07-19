# Critères canoniques de recherche produit

Dernière mise à jour : 20 juillet 2026 (§7 : reconnaissance de deux chemins d'entrée, par l'idée ou par le volume)

Ce document est le référentiel à appliquer à toutes les nouvelles recherches produit du pipeline.

## 1. Périmètre commercial

- Marché prioritaire : France. Royaume-Uni et Allemagne dans un second temps.
- Prix de vente cible : 150 à 400 € TTC.
- Acquisition initiale : Google Ads Search. Shopping/Merchant Center seulement après validation.
- Boutique de niche avec un produit phare et des produits complémentaires.
- Seuil éliminatoire : au moins 10 000 recherches mensuelles pertinentes en France pour le cluster réellement adressable.
- Ne jamais gonfler le volume avec des requêtes informationnelles hors produit, des prestations, des accessoires incompatibles, des marques concurrentes ou du low-ticket non comparable.

## 2. Sources d'idées

Explorer largement, sans se limiter aux produits techniques :

- Amazon : catégories, meilleures ventes, nouveautés, tendances, avis et achats complémentaires ;
- VEVOR : catégories et usages techniques ;
- Flippa et DotMarket : concepts de boutiques et catégories monétisées ;
- Europages : usages, équipements et marchés professionnels pouvant être adaptés au particulier ;
- Google : tendances, SERP, concurrents, prix et annonceurs.

Ces sites servent uniquement à trouver et valider des idées. **Le fournisseur doit exclusivement être trouvé sur AliExpress.**

## 3. Profils de produits recherchés

Un candidat peut appartenir à une ou plusieurs familles :

- produit technique nécessitant une explication ;
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

### Chemin A — entrée par l'idée

Utilisé pour une recherche cadrée sur une niche précise (orchestrateur `/recherche-produit`).

1. Idée trouvée sur les sources d'inspiration.
2. Filtre immédiat : banalité, valeur perçue, problème/usage et prix cible.
3. Validation du volume : cluster pertinent supérieur ou égal au seuil, en France.

### Chemin B — entrée par le volume

Utilisé pour l'accumulation de candidats en autonomie (boucle `/chasse-clusters`). Voir `specs/2026-07-20-boucle-chasse-clusters-design.md`.

1. Balayage d'une famille de marché : clusters mesurés en France, sans qu'aucun produit ne soit encore nommé.
2. Sélection des clusters atteignant le seuil.
3. Filtre qualitatif sur les produits qui servent ces clusters : banalité, valeur perçue, problème/usage et prix cible.

Ce chemin existe parce que l'entrée par l'idée fait porter tout le travail créatif avant le critère le plus éliminatoire : sur les recherches de juillet 2026, environ 30 candidats sur 50 sont morts sur le volume en phase 3, après filtrage qualitatif complet.

### Étapes communes aux deux chemins

4. Analyse Google Search, Shopping, publicités, concurrents et prix — **le nettoyage SERP est obligatoire quel que soit le chemin.** Un volume mesuré à l'outil n'est jamais un volume adressable tant que la SERP n'a pas été lue.
5. Vérification de la capacité à défendre une offre entre 150 et 400 €.
6. Sourcing exclusivement sur AliExpress.
7. Contrôle fournisseur, coût rendu, logistique, conformité et marge.
8. Classement : GO, à approfondir ou rejet documenté.

### Ce qui ne change pas selon le chemin

- Le seuil de volume pertinent (§1) et tous les filtres de différenciation (§4).
- L'interdiction de gonfler un cluster en additionnant des familles de mots-clés distinctes.
- L'étanchéité des quatre niveaux de validation : marché → fiche AliExpress → commande test → lancement.
- L'anti-doublon par le registre central.

**Source de mesure du volume** : SEMrush France (`db=fr`). Ahrefs n'est qu'un repli documenté si SEMrush est indisponible, et un verdict rendu sur repli doit le signaler.

