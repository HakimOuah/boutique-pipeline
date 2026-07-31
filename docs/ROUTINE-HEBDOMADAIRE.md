# Routine hebdomadaire de testing

Objectif de production : trois dossiers qualifiés, deux pages prêtes et un à deux lancements payants
par semaine. Un troisième lancement n’est autorisé que si son budget de collecte est suffisant.

## Lundi — collecte et préfiltre

- 06:30 : traitement automatique de la boîte d’entrée ;
- contrôle des erreurs et doublons ;
- collecte BigBuy et imports des autres sources disponibles ;
- sortie attendue : cinq à huit candidats à analyser.

## Mardi — validation Google

- volumes transactionnels par pays ;
- CPC et intention ;
- Google Shopping et SERP ;
- saisonnalité ;
- sortie attendue : trois à cinq dossiers encore plausibles.

## Mercredi — fournisseur et économie

- fournisseur principal et backup ;
- coût livré, stock, délai, notes et expédition européenne ;
- marge nette et CAC break-even ;
- thèse de différenciation ;
- sortie attendue : trois décisions documentées et un ordre de priorité.

## Jeudi — page produit numéro 1

- création du projet avec `scripts/new_boutique.py` ;
- rédaction du brief produit ;
- intégration du kit Liquid dans le thème retenu ;
- contrôle mobile, preuves et conformité.

## Vendredi — QA et lancement numéro 1

- tracking, Merchant Center, prix, stock et livraison ;
- lancement après validation humaine ;
- démarrage de la page numéro 2.

## Samedi — produit numéro 2

- finalisation et contrôle ;
- lancement si le budget est exploitable ;
- sinon, conservation au statut `ready`.

## Dimanche — revue

- import des performances avec `dropilot ads-import` ;
- rapport destiné aux experts ;
- aucune décision automatique couper/scaler ;
- préparation des sources de la semaine suivante.

## Commandes courantes

```bash
dropilot init-db
dropilot run --input data/inbox/candidats.json --source manual
dropilot list
dropilot status EMPREINTE to_analyze
dropilot ads-import --input export-google-ads.csv
automation/manual-trigger.sh
```

