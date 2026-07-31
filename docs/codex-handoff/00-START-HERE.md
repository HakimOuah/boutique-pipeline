# 00 — START HERE (point d'entrée de la passation Codex)

> Dossier de passation Codex — assemblé et vérifié le **2026-07-30** (soir).
> Racine projet : `/Users/Hakim/Documents/Boutiques drop` · Dépôt git : `boutique-pipeline/` · Ce dossier : `boutique-pipeline/docs/codex-handoff/`.
> Étiquettes de source utilisées dans tout le dossier : **[FAIT — repo:chemin]** (vérifié dans un fichier), **[FAIT — Shopify API]**, **[MÉMOIRE]** (fiches mémoire Claude), **[NOTION]**, **[INFO HAKIM — brief de passation]** (transmis, non vérifié), **[HYPOTHÈSE]**, **[MANQUANT]**, **[CONTRADICTOIRE]**, **[OBSOLÈTE POSSIBLE]**.
> Règle de lecture : ce qui n'a pas d'étiquette de fait vérifié ne doit jamais être traité comme un fait.

---

> ## ⚡ Décision du 31/07/2026 — le partage des rôles est inversé (D-0731-A, `05-DECISION-LOG.md`)
>
> **Claude Code conserve l'orchestration du projet.** Codex est **exécutant de génération d'images,
> uniquement** (GPT Image 2 natif, sans compteur de crédits), servi par la boîte `ordres/pour-codex/`
> (`14-PROTOCOLE-ORDRES.md` §9 ; instructions permanentes : `15-CODEX-EXECUTANT-IMAGES.md`).
> **L'exécution navigateur (AliExpress, DSers) reste à Claude Code, définitif** — Codex n'utilisera pas
> DSers. Le sens historique Codex → Claude de `14` est conservé mais dormant. Les passages de ce dossier qui
> décrivent une reprise d'orchestration par Codex (§1 point 9 ci-dessous, `01`, `05` Partie 3) se lisent à
> travers cette décision : **le dossier reste la référence projet pour tout collaborateur.**
> Le mode opératoire d'orchestration multi-agents que Claude Code conserve est documenté dans
> **`16-MULTI-AGENT-ORCHESTRATION.md`** (numéroté 16, les numéros 14 et 15 étant pris par le protocole d'ordres).

---

## 1. Le projet en 10 lignes

1. **Hakim (SASU OH Ventures) lance des boutiques Shopify de dropshipping FR** en mid-ticket (150–400 € TTC), acquisition **Google Ads Search/Shopping France**, fournisseurs **AliExpress uniquement**, fulfillment **DSers**. [FAIT — repo:PRODUCT-RESEARCH-CRITERIA.md]
2. Le système actuel est **piloté par Claude Code** : des documents markdown font office de base de données, des agents exécutent les phases, les MCP (Shopify, Notion, Brand Search, Chrome, Higgsfield) sont les bras. **Rien ne tourne en continu.** [FAIT — voir `02`]
3. La recherche produit est un **pipeline volume-first** : le volume SEMrush est mesuré avant tout travail créatif ; verdicts fail-closed ; registre central anti-doublon (`registre-candidats.md`, compteur **2/20**). [FAIT — repo:registre-candidats.md]
4. La source d'idées principale est le **minage Brand Search** de boutiques prouvées en Google Ads FR ; la voie principale est `/qualifie-idees` (mesure express ~6 min par idée). [MÉMOIRE + FAIT — voir `03`]
5. Le lancement d'une boutique suit le **Campement type Notion** (20 tickets-briefs) + `PLAYBOOK.md` (6 phases / 3 portes de validation humaine). [NOTION + FAIT]
6. **Six marques existent** (voir §2) ; la plus avancée, **Maison Noirmont** (montres à cadran stérile), est construite mais **sous mot de passe, 0 commande**. [FAIT — Shopify API]
7. Garde-fous transversaux hérités des échecs : **jamais de fausse preuve sociale** (suspension GMC Bien Brûlé vécue), **promesses vérifiables uniquement**, persona validé **bloquant** avant tout copywriting, mobile-first. [FAIT + MÉMOIRE]
8. **Fichiers locaux = source de vérité, Notion = tableau de bord** — invariant du système. [MÉMOIRE — notion-pipeline-boutiques]
9. La vision cible de Hakim ([INFO HAKIM]) : migrer l'orchestration vers **Codex** (avec Browser Use / Apify / n8n en briques d'exécution) — architecture **non actée** à ce jour, voir `01` et `05` Partie 3.
10. Deux précédents Codex réussis existent déjà : la boucle `codex-chasse-clusters` (20/07) et les galeries Noirmont (26/07). [FAIT — voir `03` §8]

## 2. État actuel (30/07/2026)

| Boutique | État | Détail |
|---|---|---|
| **Maison Noirmont** (montres, `v42pzp-h4.myshopify.com` / maisonnoirmont.fr) | **La plus avancée — en construction, sous mot de passe, 0 commande, 0 client** [FAIT — Shopify API] | 105 fiches, DSers 103/103 mappé, configurateur-guide livré, SEO fait ; le thème de travail `204248088914` est **UNPUBLISHED** — rien du travail n'est visible |
| **Tuftéo** (kits tufting, `et0hua-w1.myshopify.com` / tufteo.com) | Publiée le 23/07 [FAIT — repo] ; statut Notion « Ads lancées » **[CONTRADICTOIRE — aucune trace de campagne dans le dépôt]** | Store et thème live `188623847809` confirmés par HTTP public ; **les 6 avis démo fictifs sont publics avec « Vérifié », plus un compteur 789 non étayé** [FAIT — navigateur/HTTP public 30/07 23:35] |
| **Bonum Vitae** (osmoseurs, bonumvitae.fr) | En ligne, Google Ads actives 30 €/j (pointage 24/07) [OBSOLÈTE POSSIBLE] | **Gel : ne rien modifier sans autorisation explicite de Hakim** ; sert de référence Horizon (PDP/panier/home) |
| **Lihyl** (reformer Pilates, lihyl.fr) | Test clos non concluant (juin) | Détail du kill [MANQUANT] |
| **Bien Brûlé** (café nomade, bienbrule.com) | Test clos non concluant (juin) | Origine de la règle anti-fausse-preuve (GMC suspendu → réintégré) |
| **Petit Astre** (canapé enfant) | Jamais créée — abandonnée (STOP SEMrush 17/07) | — |

Pipeline : 2 candidats qualifiés en attente de décision Hakim (fontaine à gravité, surpresseur), boucle en pause depuis le 24/07. **Aucune boutique du pipeline n'est en campagne. Aucun chiffre d'affaires documenté nulle part** [MANQUANT — voir `04` §8].

### Ce qui fonctionne / incomplet / expérimental
- **Fonctionne (éprouvé)** : le pipeline de recherche produit (skills + 9 agents), le registre, le build de boutique par API sur thème brouillon, l'import/mapping DSers documenté, l'import d'avis Trustoo, le pipeline visuel « Codex génère → agent branche », la culture du piège documenté (`10`).
- **Incomplet** : Noirmont non publiée (P0 en attente de Hakim) ; Tuftéo sans plan de test Ads rempli ; `boutique-tufting/project-state.md` bloc « Accès & Shopify » vide ; compteur candidats 2/20 ; QA mobile réelle jamais faite.
- **Expérimental / non exploité** : **dropilot** (package Python de scoring batch : jamais installé, inbox vide, VPS jamais déployé), n8n/Apify/Browser Use (vision cible, zéro existant ici), skills post-lancement (ads, emails, SAV — installés, jamais servis en production).

## 3. Blocages majeurs

1. ⚠️ **Git sans remote et travail non suivi — le blocage n°1** [FAIT — repo:.git] : branche `feat/boucle-chasse-clusters`, dernier commit **21/07** ; la quasi-totalité du travail de production (`boutique-seiko-mod/`, `boutique-tufting/`, `docs/`, `reports/`…) est **untracked** ; **aucun remote**. Le projet n'existe que sur ce Mac. Première action recommandée : faire committer/pousser par Hakim **après purge des secrets** (voir `07` §4 : le mot de passe storefront est en clair dans 3 fichiers du dépôt/mémoire — il a aussi été retiré de ce dossier de passation).
2. **Médiateur de la consommation** (obligation légale, adhésion **par site**, jamais recopiée d'une autre boutique) — P0 Noirmont, marqueur `[À COMPLÉTER…]` en CGV art. 17. [FAIT — voir `11` BIZ-1]
3. **Mot de passe storefront + thème UNPUBLISHED** : tant que Hakim n'a pas republié le thème `204248088914` et levé le mot de passe, tout le travail Noirmont est invisible. [FAIT — voir `11` BIZ-2]
4. **Avis et compteurs de démonstration** : Noirmont affiche « 1340 avis », « 2 000 clients satisfaits » pour 0 commande (= motif de suspension GMC, précédent Bien Brûlé) — chasse gardée de Hakim, à purger avant exposition. **Cas aggravé Tuftéo : le site public sert les 6 avis explicitement fictifs avec « Vérifié » et un compteur « 789 avis » non étayé** — confirmé par rendu Browser Use et HTTP public le 30/07 à 23:35. [FAIT — voir `boutique-tufting/audit-avis-demo-publics-2026-07-30.md`, `11` BUG-0]
5. **Accès** : tout passe par les MCP Claude et les sessions Chrome de Hakim (SEMrush, DSers, AliExpress) ; aucun accès API propre n'existe pour un repreneur ; AliExpress a déjà bloqué le navigateur Codex le 20/07. [FAIT — voir `07`, `08`]

## 4. Priorités (P0 du backlog `11`)

| # | Tâche | Qui |
|---|---|---|
| P0 | **BIZ-1** — Adhésion médiateur de la consommation pour maisonnoirmont.fr | Hakim |
| P0 | **BIZ-2** — Republier le thème « Maison Noirmont », retirer le mot de passe, supprimer le fork obsolète `204329288018` | Hakim |
| P0 | **BIZ-4** — Trancher/retirer les avis et compteurs de démonstration avant toute exposition publique | Hakim (exclusif) |
| P0 | **BUG-0 — retirer les 6 avis fictifs publics et le compteur 789 de Tuftéo** | Hakim (exclusif) |
| P0 de passation (hors backlog `11`) | Committer + créer un remote privé **après purge des secrets** | Hakim + Codex |

Ordre conseillé pour Noirmont (Phase 0 de `plan-nommage-seo.md` §5) : médiateur → republication → paiement/commande test → mot de passe → purge des affirmations invérifiables. Ensuite, P1 : voir la vue d'ensemble en fin de `11`.

## 5. Ordre de lecture recommandé des autres fichiers

Lire dans cet ordre (une ligne par fichier) :

1. **`01-PROJECT-VISION.md`** — ce que le projet cherche à faire : vision confirmée par les sources vs vision cible du brief, et la définition écrite de la charte NOIRMONT.
2. **`02-CURRENT-ARCHITECTURE.md`** — l'existant réel : composants, flux, MCP, stockage, et l'écart vision/existant (n8n, VPS, Apify, Browser Use).
3. **`03-AGENTS-AND-WORKFLOWS.md`** — les 3 skills + 9 agents, le campement Notion 20 tickets, le pipeline étape par étape avec marquage migrabilité, les précédents Codex.
4. **`04-BOUTIQUES-ET-PRODUITS.md`** — les 6 boutiques une à une, le registre des candidats, contradictions C1–C5 et manquants.
5. **`05-DECISION-LOG.md`** — le journal des décisions reconstitué (pipeline + Noirmont), 13 contradictions documentées, points à réévaluer avec Hakim.
6. **`10-FAILURES-AND-LESSONS.md`** — **le fichier le plus riche** : chaque piège payé en production (AliExpress, DSers, API Shopify, images IA, véracité) au format symptôme→prévention.
7. **`11-OPEN-TASKS.md`** — le backlog priorisé P0→P3 (bugs, dette, évolutions, tâches business de Hakim, migration Codex/Browser Use).
8. **`12-CODEX-INSTRUCTIONS.md`** — comment travailler ici : conventions, règles métier, validations obligatoires, la liste « Codex ne doit jamais ».
9. **`07-SETUP-AND-SECRETS.md`** — installation, connexions service par service, état des secrets (aucune valeur recopiée), checklist repreneur.
10. **`.env.example`** — gabarit des variables d'environnement à créer (aucune valeur réelle).
11. **`08-BROWSER-AUTOMATION.md`** — tout ce qui passe par le navigateur (AliExpress, DSers, SEMrush) : recettes existantes puis contrats JSON de l'architecture cible.
11 bis. **`14-PROTOCOLE-ORDRES.md`** — la mise en œuvre opérationnelle des contrats de `08` : boîte aux lettres `ordres/` entre Codex (dépose) et Claude Code (valide + exécute), classes d'autonomie A/B/C — sens désormais **dormant** ; le §9 porte le sens actif inverse (Claude Code → Codex, images), détaillé dans **`15-CODEX-EXECUTANT-IMAGES.md`**.
11 ter. **`16-MULTI-AGENT-ORCHESTRATION.md`** — le mode opératoire réel de Claude Code en chef d'équipe multi-agents : anatomie des briefs, vagues de parallélisation, gates humains, détection des résultats faibles, protocole de reprise état-d'abord (numéroté 16 car 14 et 15 étaient déjà pris).
12. **`09-DATA-MODELS.md`** — les 18 modèles de données (registre, fiches, variantes/SKU, médias, erreurs fail-closed) ancrés dans les structures réelles.
13. **`06-NOTION-INDEX.md`** — cartographie du workspace Notion, ce qui n'existe **que** dans Notion (campement type !), divergences Notion↔dépôt.
14. **`13-HANDOFF-SUMMARY.json`** — synthèse machine-lisible de l'ensemble.
15. En annexe : **`_analyse-repo.md`** — notes d'assemblage : état git détaillé, obsolètes/doublons, refactorisations recommandées avant migration.

## 6. Commandes essentielles

Il y en a **très peu** : **pas de build, pas de CI, aucun service** ; le « système » est documentaire et s'exécute en session. Les seules commandes du dépôt :

```bash
# Tests du starter-kit (exécutés le 30/07 : 14 passed en 0.08s) — TESTÉ
/usr/bin/python3 -m pytest tests/ -q

# Tests du prototype dropilot (exécutés le 30/07 : 16 passed) — TESTÉ
/usr/bin/python3 -m pytest tests_dropilot/ -q

# Scaffolder un projet boutique — ⚠️ TESTÉ PARTIELLEMENT le 30/07 : pas d'argparse,
# le script crée un dossier du nom EXACT du 1er argument (un `--help` a créé un dossier `--help`, supprimé depuis).
/usr/bin/python3 scripts/new_boutique.py <nom-boutique>

# Valider des brand-tokens contre le schéma (prend un chemin de fichier, pas de --help) — NON TESTÉ sur un vrai fichier
/usr/bin/python3 scripts/validate_tokens.py <chemin/brand-tokens.json>

# Charte → settings_data.json de thème — NON TESTÉ
/usr/bin/python3 scripts/tokens_to_theme.py …

# Installation dropilot (prototype jamais installé ; voir docs/OPERATIONS.md) — NON TESTÉ
python3 -m venv .venv && .venv/bin/pip install -e '.[dev]' && .venv/bin/dropilot init-db
```

⚠️ Utiliser `/usr/bin/python3` (PyYAML + pytest déjà présents) — pas le Python Homebrew 3.14 sans installer les dépendances [FAIT — repo:docs/OPERATIONS.md]. Les scripts ad hoc `boutique-seiko-mod/*.mjs|*.py` sont des one-shots de session (Node natif, aucun `package.json`) — **tous NON TESTÉS ici**, à lire avant tout réemploi. Le reste du travail passe par les MCP/API en session, pas par des commandes.
