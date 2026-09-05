# AGENTS.md — boutique-pipeline

Fichier lu par Codex, Cursor et tout agent qui suit la convention `AGENTS.md`.
**Il ne duplique aucune règle** : il dit où elles sont.

## Les règles

Ce repo fait partie d'un ensemble de cinq, piloté depuis le hub
[boutiques-drop](https://github.com/HakimOuah/boutiques-drop) (`~/Documents/Boutiques drop/`).

1. Les règles propres à ce repo : `CLAUDE.md` ici même — valables pour tous les agents.
2. Les règles transverses (répartition des repos, GitHub source de vérité, ce qu'on ne commit
   jamais) : `../CLAUDE.md` dans le hub.

## Journal éditorial NOX — après chaque étape significative

**Après chaque étape significative, écrire un événement éditorial avant de rendre la main.**
Il s'écrit dans le hub, pas ici : NOX lit un seul répertoire pour les cinq repos.

Enregistrer : création d'un projet, d'une boutique, d'un agent, d'une automatisation,
d'une intégration, d'une API ; règle de méthode apprise ; premier chiffre réel.

Ne pas enregistrer : typo, refactor trivial, changement cosmétique, opération Git de confort,
changement technique sans conséquence. **En cas de doute, ne pas écrire.**

```bash
python3 "$HOME/Documents/Boutiques drop/scripts/nox-evenement.py" \
  --categorie <cat> --titre "..." --projet <slug> --repo boutique-pipeline --axes agents,ecommerce
```

L'événement créé est à committer **dans le hub**, pas dans ce repo.

Règle complète, test de significativité, schéma : `../nox/README.md`.
C'est la seule source ; ne pas la recopier.
