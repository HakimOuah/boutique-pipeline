# Exploitation locale

## Installation

```bash
python3 -m venv .venv
.venv/bin/pip install -e '.[dev]'
.venv/bin/python -m pytest
```

Sur le Mac actuel, `/usr/bin/python3` possède déjà PyYAML et pytest. Le Python Homebrew 3.14 ne doit
pas être utilisé avant installation des dépendances du projet.

## Premier test local

```bash
.venv/bin/dropilot init-db
.venv/bin/dropilot run --input exemple.json --source manual
```

Chaque exécution écrit trois rapports dans `reports/` et met à jour la base sans dupliquer le même
produit, la même URL fournisseur ou la même thèse.

Les fichiers `reports/latest.csv`, `reports/latest.json` et `reports/latest.md` pointent toujours
vers la dernière exécution. Ils constituent les cibles stables à utiliser dans n8n ou Google Sheets.

## BigBuy

L’API officielle utilise un Bearer token. Le connecteur cible le sandbox par défaut :

```bash
export BIGBUY_API_KEY='...'
.venv/bin/dropilot bigbuy-fetch --taxonomy 123 --out data/inbox/bigbuy-123.json
automation/manual-trigger.sh
```

Passer explicitement `--base-url https://api.bigbuy.eu` pour la production. Le connecteur collecte
le catalogue et les informations localisées, mais ne transforme pas automatiquement une suggestion
de prix BigBuy en validation marché.

## Autres sources

Dupliquer `config/source-mapping.template.yaml`, renseigner les colonnes réelles du premier export,
puis exécuter :

```bash
dropilot map-source --input export.csv --mapping config/vevor.yaml --out data/inbox/vevor.json
```

Cette méthode évite d’inventer les noms de colonnes des fournisseurs.

## Google Ads

Compléter `templates/google-ads-tests.template.csv`, puis :

```bash
dropilot ads-import --input export-tests.csv
```

Le rapport calcule CTR, CPC, taux de conversion, coût par conversion et ROAS. Les experts restent
responsables des règles de coupure et de scaling.
