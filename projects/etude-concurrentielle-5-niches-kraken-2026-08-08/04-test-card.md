# Carte de test concept — TC-CONCEPT-01

- Date/ID : 2026-08-08 / TC-CONCEPT-01
- Statut : suspendu ; aucune diffusion ou dépense autorisée avant passage du
  filtre prix/panier de la niche retenue.
- Hypothèse : une entrée par projet/scénario avec kit compatible convertit mieux qu’une entrée par grille de produits.
- Porte/goulot : Gate 1 — prix/panier d'abord, puis compréhension de l'offre.
- Marché : France.
- Variante A : landing catalogue par catégories produits.
- Variante B : landing projet-first, diagnostic court et kit personnalisable.
- Conversion primaire : démarrer/completer le configurateur ou demander la liste du kit.
- Variable principale : architecture de décision, contenu produit identique.
- Métrique primaire : taux d’avancement vers le panier simulé.
- Secondaires : AOV simulé, abandons par étape, questions/objections, préférence déclarée.
- Garde-fous : aucune fausse preuve, aucun achat réel, aucune promesse de conformité non vérifiée.
- Budget : `NON_AUTORISE`.
- Stop rules : compréhension faible, panier irréaliste, sourcing/conformité bloqués.
- Fenêtre de revue : après 5 entretiens ou un échantillon de test défini avec Hakim.

## Résultat

- Données : `MANQUANT`.
- Décision : ne pas exécuter pour le scrap (`STOP_PRIX_PANIER`) ; réutiliser
  seulement après choix d'une niche ayant passé la sonde prix/AOV.
- Prochain test : kit figé versus kit modulable, puis preuve générique versus preuve niche.
