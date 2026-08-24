# Chasse aux clusters — espace Codex indépendant

Cet espace contient l'adaptation Codex de la boucle volume-first. Il est volontairement séparé du dispositif Claude afin de permettre une comparaison honnête des résultats.

## Dernière requalification ciblée

Le run `20260824-232503`, révisé le 2026-08-25 après un nouvel apport fournisseur de Hakim, a repris les quatre pistes Q4 : **deux `TECHNICAL_WATCH`, deux `TECHNICAL_FAIL`, zéro décision humaine attribuée**. La couverture lestée devient la priorité de requalification : un 8 kg rendu à 59,75 EUR depuis l'Allemagne rend l'économie plausible, sans encore prouver conformité, qualité, retours ni backup. Le déshumidificateur reste la seconde piste.

- [Évaluation finale Q4](runs/20260824-232503-q4-validation/final-20260824-232503.md)
- [État isolé du run](runs/20260824-232503-q4-validation/run-state.json)
- [Dossiers et preuves](runs/20260824-232503-q4-validation/)
- [Amendement couverture lestée](runs/20260824-232503-q4-validation/amendment-couverture-lestee-20260825.md)

Le `run-state.json` racine conserve volontairement l'état terminal détaillé du run catalogue-volume précédent ; la requalification Q4 possède son état isolé afin de ne pas écraser cet historique.

## Run catalogue-volume précédent

Le run `20260815-181328` a déroulé six univers catalogue-volume apportés par Hakim jusqu'à leur gate terminal : **cinq STOP, un `REPARER_AVANT_SOURCE_EXACTE`, zéro candidat retenu**. Les seuils n'ont pas été abaissés.

- [Livrable final](final-20260815-181328.md)
- [Audit de consolidation](reports/audit-consolidation-six-univers-20260815.md)
- [Registre des candidats](registre-candidats.codex.md)
- [État terminal](run-state.json)

## Périmètre

- Objectif expérimental : jusqu'à 20 dossiers marché qualifiés, complets ou à sourcer manuellement.
- Marché : France.
- Acquisition : Google Ads Search.
- Prix cible : 150–400 EUR TTC.
- Volume : au moins 10 000 recherches mensuelles réellement adressables après nettoyage SERP.
- Fournisseur retenu : AliExpress uniquement, fiche exacte et ouverte lorsque l'accès fonctionne.
- Repli autorisé : si AliExpress est techniquement inaccessible, fournir les mots-clés de sourcing manuel sans inventer de fournisseur.
- Économie : marge contributive et CPA maximal compatibles avec le CPC observé pour les dossiers complets ; économie à compléter pour les dossiers sans coût rendu.

Deux statuts peuvent entrer dans le livrable : `RETENU_NIVEAU_2_ECO` lorsque toutes les preuves documentaires passent, et `RETENU_MARCHE_A_SOURCER` lorsque le marché passe mais qu'un blocage technique AliExpress empêche le sourcing. Le second statut ne valide ni fournisseur ni économie. Aucun statut ne signifie que le produit a été commandé, testé ou autorisé au lancement.

## Isolation

Codex peut lire les fichiers suivants comme sources de vérité ou d'anti-doublon :

- `../PRODUCT-RESEARCH-CRITERIA.md`
- `../PRODUCT-RESEARCH-PLAYBOOK.md`
- `../registre-candidats.md`
- `../familles-exploration.md`
- `/Users/Hakim/Documents/Boutiques drop/.claude/agents/`
- `/Users/Hakim/Documents/Boutiques drop/.claude/skills/chasse-clusters/`

Codex n'écrit jamais dans ces fichiers. Toutes les écritures de la boucle restent dans ce dossier.

## Fichiers

- `families.json` : liste indépendante des 40 univers ; leurs statuts Codex démarrent tous à `PENDING` pour permettre une mesure indépendante.
- `run-state.json` : checkpoint de reprise au niveau famille, graine, cluster et phase.
- `registre-candidats.codex.md` : source de vérité des résultats Codex.
- `reports/` : rapports immuables par phase, run et tentative.
- `checkpoints/` : explications des pauses, fenêtres stériles et blocages.
- `source-integrity.sha256` : empreintes de référence des principaux originaux au moment de la création.

## Mode de comparaison

Les familles déjà explorées par Claude ne sont pas marquées terminées ici. Codex peut donc les remesurer indépendamment, mais il doit appliquer l'anti-doublon au registre historique. Un candidat déjà rejeté ou déjà retenu par Claude ne compte pas comme nouveau candidat Codex, sauf reprise explicitement autorisée par Hakim avec une thèse nouvelle.

## Lancement ultérieur

La création de cet espace ne lance aucune navigation ni recherche. Pour démarrer, demander explicitement à Codex :

> Lance la compétence `chasse-clusters-codex` et poursuis la boucle indépendante jusqu'à 20 candidats qualifiés ou épuisement des familles. Utilise Chrome, reprends depuis `codex-chasse-clusters/run-state.json` et ne touche jamais aux fichiers Claude.

La recherche Web est séquentielle afin de ne pas faire piloter une même session Chrome par plusieurs agents en parallèle.
