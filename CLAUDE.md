# Règles du repo boutique-pipeline

## Point d'entrée d'une boutique (décision Hakim, 11/08/2026)

**Avant toute intervention sur une boutique, lire son `TABLEAU.md`** — c'est le Kanban de tickets, la seule source de ce qu'il reste à faire et de comment le faire. Ne jamais fouiller `journal/` pour savoir quoi faire : c'est une archive.

**En fin d'intervention, mettre `TABLEAU.md` à jour avant de rendre la main** (tickets passés en EN COURS / FAIT, nouveaux tickets créés si le travail en a révélé). Écrire le compte rendu dans `<boutique>/journal/AAAA-MM-JJ-sujet.md`, jamais à la racine du dossier boutique.

Convention complète et format des tickets : [`METHODE-TABLEAU.md`](METHODE-TABLEAU.md). Elle vaut pour Claude comme pour Codex.

## Réflexe GitHub (décision Hakim, 07/08/2026)

GitHub est la source de vérité unique du projet. **En fin de toute tâche qui modifie des fichiers durables (registres, rapports, specs, code, docs), committer et pousser sur `origin main` sans que Hakim ait à le demander.** Message de commit en français, une ligne de résumé claire. Jamais de secrets ni de `venv/` dans git — le `.gitignore` fait foi.

Ce repo fait partie d'un ensemble de 3, cartographié dans le hub [boutiques-drop](https://github.com/HakimOuah/boutiques-drop) (racine locale `~/Documents/Boutiques drop/`, voir son README et son CLAUDE.md pour les règles complètes).
