# _analyse-repo — notes de travail pour l'assemblage final

> Dossier de passation Codex — généré le 2026-07-30. **Analyse seulement : rien n'a été supprimé, déplacé ni modifié.**
> Étiquettes de source. Chaque recommandation est à arbitrer par Hakim.

---

## 1. État git — le problème n°1

> **[CORRIGÉ 31/07 : remote créé et dépôt poussé — l'affirmation ci-dessous décrivait l'état au moment de l'audit initial (30/07).]** État réel au 31/07 : branche `main`, arbre propre, remote privé `origin` = `HakimOuah/boutique-pipeline`, HEAD local = HEAD distant. Restent d'actualité dans cette section : la purge du mot de passe storefront (07-SETUP §4) et le tri archives/binaires (§2-3).

- Branche courante `feat/boucle-chasse-clusters`, dernier commit **21/07/2026** ; `main` en retard ; **aucun remote**. **[FAIT — repo:.git]**
- **La quasi-totalité du travail de production est untracked** : `boutique-seiko-mod/` (toute la boutique Noirmont), `boutique-tufting/`, `dropilot/`, `docs/`, `reports/`, `scratchpad/`, `personas/`, `specs/`… **[FAIT — `git status`]**
- Modifs non commitées sur des fichiers suivis : `PLAYBOOK.md`, `registre-candidats.md`, `README.md`, `scripts/new_boutique.py`, 4 templates, `.gitignore`, `pytest.ini`. **[FAIT]**
- **Reco** : (1) trier ce qui doit entrer dans git (voir §2-3 : exclure images/backups lourds), (2) committer, (3) merger ou renommer la branche, (4) créer un remote privé, (5) purger le mot de passe storefront des fichiers **avant** le premier push (voir 07-SETUP §4).

## 2. Fichiers obsolètes / archives à trancher

| Élément | Constat | Reco |
|---|---|---|
| `recherche-prod-extracted/` | Ancien « broyeur » ; le README le déclare archive/suite de régression historique ; contient un doublon interne complet (`broyeur_package/broyeur_package/`) **[FAIT — repo + README.md]** | Archiver hors dépôt ou dossier `archive/` |
| `Recherche prod.zip` | Zip source de l'archive ci-dessus, déjà extraite **[FAIT]** | Supprimer du dépôt |
| `broyeur/` + `tmp/*.json` + `tmp/pdfs/` | Anciennes niches (scanner, thermique, microscope… juillet 15-16) supplantées par le registre **[FAIT]** | Archiver |
| `tmp/venv/` | Un venv Python **dans le dépôt** (non ignoré par `.gitignore` qui ne couvre que `.venv/`) **[FAIT]** | Supprimer + ajouter `tmp/` au .gitignore |
| `../CONTEXTE-MEMOIRE-pour-Codex.md` | Précédent handoff Codex du **23/06** : chemins périmés (`/Users/Hakim/boutique-pipeline`), règle SEMrush contredite par juillet **[FAIT — repo parent]** [OBSOLÈTE POSSIBLE] | Marquer obsolète ; le remplacer par ce dossier `codex-handoff/` |
| `../drop/boutique-pipeline/boutique-seiko-mod/backup-faces-swissmade-2026-07-26/` | Arborescence **vide** créée le 26/07 — vraisemblablement un `mkdir -p` lancé depuis un mauvais cwd **[FAIT — repo parent:drop/]** | Supprimer `../drop/` |
| `boutique-seiko-mod/ARCHIVE-prompt-reprise-visuels-2026-07-25.md.bak`, `OBSOLETE-NE-PAS-UTILISER-prompt-galeries-v1.md.bak` | Prompts Codex archivés en `.bak`, déjà auto-étiquetés obsolètes **[FAIT]** | Déplacer dans un dossier `archive/` de la boutique ; ne pas committer |
| `boutique-seiko-mod/entrees-faces-REDONDANT-export-claude/` | Auto-étiqueté redondant (doublon d'images) **[FAIT]** | Supprimer après vérification |
| Thème Shopify `204329288018` (BROUILLON fix-uiux) | Fork obsolète **côté Shopify**, marqué « à supprimer » **[FAIT — repo:REPRISE-SESSION.md]** | Action Shopify réservée à Hakim |

## 3. Doublons et masse binaire

- **Kit Liquid portable en double** : `shopify-portable/` et `boutique-tufting/shopify/portable-kit/` (copie d'intégration). **[FAIT]** Reco : garder `shopify-portable/` comme canonique, noter la copie comme instanciée.
- **Playbooks qui se recouvrent** : `PRODUCT-RESEARCH-PLAYBOOK.md` (36 Ko, méthode) vs `PRODUCT-RESEARCH-CRITERIA.md` (seuils canoniques, MAJ 20/07). Les agents citent les deux ; le risque de divergence est documenté comme la raison d'être de CRITERIA. **[FAIT]** Reco : garder les deux mais faire de CRITERIA l'unique porteur de chiffres (déjà la règle), et purger les seuils chiffrés résiduels du PLAYBOOK.
- **Masse d'images et de backups** dans le dépôt : `boutique-seiko-mod/` (~110 fichiers dont dizaines de JPG/PNG de backup), `boutique-tufting/assets/source/aliexpress/` (des centaines de webp), `scratchpad/`, `swatches-2026-07-25/`, `visuels-2026-07-25/`. **[FAIT]** Reco : ne **pas** committer les binaires ; stockage à part (Drive/S3) + manifestes markdown (les MANIFESTE.json/urls.txt existent déjà).
- `PLAYBOOK.md` (racine, boutique) vs `../New project/PLAYBOOK.md` et `../New project/PRODUCT-RESEARCH-PLAYBOOK.md` — anciens exemplaires hors dépôt. **[FAIT — repo parent]** [OBSOLÈTE POSSIBLE] Reco : marquer `New project/` comme archive.

## 4. Prompts et documents dispersés

- Les livrables de sessions Noirmont sont ~80 markdown à plat dans `boutique-seiko-mod/` (audits, plans, journaux de nuit, prompts Codex `PROMPT-CODEX-galeries.md`, bilans datés). La convention « lire `REPRISE-SESSION.md` d'abord » compense, mais rien n'indique quels fichiers sont encore faisant-foi. **[FAIT]**
- Reco : sous-dossiers `sessions/` (journaux datés), `prompts/`, `audits/`, et un index dans `REPRISE-SESSION.md`. À faire **après** le premier commit (pour garder l'historique lisible).
- Prompts Codex historiques : `recherche-prod-extracted/PROMPT_CLAUDE_CODE.md` (x2 via doublon interne), `.bak` de `boutique-seiko-mod/`, `boutique-tufting/prompt-codex-images-2026-07-21.md`, espace `codex-chasse-clusters/`. Aucun n'est le « prompt d'entrée » actuel — c'est précisément ce que ce dossier de passation doit remplacer. **[FAIT]**

## 5. Configurations incohérentes / périmées

1. **README.md ment par omission** : il décrit le starter-kit + dropilot, pas le vrai centre de gravité (agents Claude, registre, boutiques). **[FAIT]** Reco : réécrire le README comme carte du dépôt.
2. **PLAYBOOK phase 1b « Semrush désactivé par défaut »** vs compte payant utilisé partout en juillet. [CONTRADICTOIRE — PLAYBOOK.md vs REPRISE-SESSION.md/marche-complet-semrush.md] Résolution probable : la règle date de l'ère « essais ponctuels » (juin) ; à réécrire. **À valider par Hakim.**
3. **`.env.example` racine vs réalité** : il pointe des chemins VPS `/opt/dropilot/...` jamais déployés. **[FAIT]** Reco : le garder comme doc dropilot mais renvoyer vers `docs/codex-handoff/.env.example` pour l'installation réelle.
4. **`.gitignore` incomplet** : n'exclut ni `tmp/`, ni les dossiers de backups images, ni `*.bak`, ni `.DS_Store` partout (règle présente mais des .DS_Store sont déjà suivis ailleurs). **[FAIT]**
5. **`boutique-tufting/project-state.md` bloc « Accès & Shopify » vide** (store, domaine, thème live, IDs) alors que le build est fait sur le thème `188623847809`. [MANQUANT] Reco : remplir — c'est l'équivalent Tuftéo du REPRISE-SESSION Noirmont, indispensable à une reprise.
6. **Registre vs Notion** : le registre local (24/07) est plus frais que l'import Notion documenté (19/07). Cohérent avec la règle « local d'abord », mais la synchro n'est pas systématique (`notion-sync-pending.md` a existé pour ça). **[FAIT + MÉMOIRE]** Reco : décider si Codex maintient la synchro ou si Notion est gelé pendant la migration.

## 6. Parties fortement dépendantes de Claude Code (points durs de la migration)

| Dépendance | Où | Impact pour Codex |
|---|---|---|
| **Skills + agents** (`SKILL.md`, `agents/*.md` avec orchestration `subagent_type`, exécution synchrone, règles fail-closed) | `../.claude/` — **hors dépôt git** | Le cœur méthodologique du pipeline n'est ni versionné ni portable tel quel. La *logique* est heureusement dupliquée dans `specs/*.md` (validés par Hakim) → réécrire en prompts/outils Codex à partir des specs, pas des fichiers d'agents |
| **Mémoire persistante** (14 fiches, index MEMORY.md) | `~/.claude/projects/-Users-Hakim-Documents-Boutiques-drop/memory/` | Décisions et pièges critiques invisibles depuis le dépôt. Reco : exporter les fiches dans `docs/decisions/` du dépôt (versionnées), la mémoire Claude devenant un miroir |
| **MCP connecteurs** : Shopify (connecteur Claude, OAuth), Notion, Brand Search, Higgsfield, claude-in-chrome | config Claude de Hakim | Aucun n'existe côté Codex. Équivalents : app custom Shopify Admin API, Notion API, API/UI Brand Search, API Higgsfield, et un navigateur pilotable pour SEMrush/DSers/AliExpress (le run Codex du 20/07 a déjà montré que **Browser Use bloquait AliExpress** — `codex-chasse-clusters/run-state.json`) **[FAIT]** |
| **Sessions Chrome de Hakim** (SEMrush, DSers, AliExpress, Trustoo, Brand Search web) | Chrome local | Le « trousseau » réel du système. Non transférable ; tout repreneur doit soit partager la machine, soit obtenir des identifiants via gestionnaire de mots de passe |
| **Skills globaux skills.sh** (cro, copywriting, ads, higgsfield-*, ui-ux-pro-max…) | `~/.claude/skills/` | Simples dossiers markdown : copiables dans le dépôt si utile, mais leur déclenchement automatique est propre à Claude |
| **Scratchpad de session Claude** (`/private/tmp/claude-502/...`) | hors dépôt | Éphémère par design — rien à migrer, mais vérifier qu'aucun backup unique n'y traîne avant une purge machine |

## 7. Ce qui empêche Codex de reprendre aujourd'hui

1. **Pas de remote git** + travail untracked → aucun moyen d'accéder au code hors du Mac. **[FAIT]** [CORRIGÉ 31/07 : résolu — remote privé `HakimOuah/boutique-pipeline` créé et dépôt poussé, `main` alignée sur le distant.]
2. **Aucun accès API propre** : tout passe par des connecteurs MCP Claude et des sessions Chrome. [MANQUANT — tokens à créer]
3. **La méthode vit hors du dépôt** (`.claude/` parent + mémoire `~/.claude/`) — un clone du dépôt seul est incomplet.
4. **Identifiants boutique Tuftéo partiellement documentés** : `et0hua-w1.myshopify.com`, `tufteo.com` et thème live `188623847809` confirmés publiquement le 30/07 ; compte DSers et accès CLI/API toujours [MANQUANT].
5. **Accès AliExpress automatisé non résolu côté Codex** (échec Browser Use du 20/07 ; le pipeline Claude s'appuie sur la session Chrome). **[FAIT — codex-chasse-clusters]**
6. Secret storefront en clair dans 3 fichiers → à purger avant tout partage du dépôt. **[FAIT]**

## 8. Refactorisations recommandées AVANT migration (liste, rien d'exécuté)

1. Purger le mot de passe storefront des 3 fichiers identifiés (07-SETUP §4) puis le faire tourner dans l'admin.
2. Committer l'existant sur une branche propre ; exclure binaires/backups via `.gitignore` renforcé (`tmp/`, `*.bak`, dossiers backup-*, assets sources) ; créer un remote privé. [CORRIGÉ 31/07 : commits sur `main` + remote privé poussé — fait ; le renforcement du `.gitignore` reste à vérifier.]
3. Rapatrier dans le dépôt les éléments hors-git faisant foi : `../.claude/skills` + `agents` (ou leur réécriture agnostique), export des 14 fiches mémoire → `docs/decisions/`.
4. Compléter `boutique-tufting/project-state.md` (bloc Accès & Shopify) et créer l'équivalent pour Noirmont si `REPRISE-SESSION.md` ne suffit pas.
5. Réécrire `README.md` en carte du dépôt réelle (starter-kit + agents + boutiques + dropilot-prototype + handoff).
6. Trancher le sort de dropilot : l'activer (installer, alimenter l'inbox) ou le déclasser explicitement en « prototype conservé » — aujourd'hui il occupe le README sans servir. **[FAIT — aucune trace d'exécution]**
7. Archiver : `recherche-prod-extracted/`, `Recherche prod.zip`, `broyeur/`, `tmp/`, `../drop/`, `.bak`, `entrees-faces-REDONDANT-…`.
8. Mettre à jour PLAYBOOK (règle SEMrush, mention du campement Notion et des skills à invoquer) pour qu'il redevienne l'unique procédure de lancement.
9. Documenter en un tableau unique les boutiques (URL myshopify, domaine, thème live/brouillon, compte DSers, e-mail, apps installées) — Tuftéo est désormais partiellement renseignée dans `project-state.md`, mais les autres données restent dispersées entre REPRISE-SESSION, mémoire et… la tête de Hakim.
