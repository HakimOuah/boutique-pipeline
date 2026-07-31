# Boutique Pipeline — Starter-kit Shopify mono-produit

Socle réutilisable pour lancer une boutique Shopify (Approche C : playbook + scripts).

## Démarrage
### Recherche produit
1. Remplir `templates/product-research-request.template.md`.
2. Suivre `PRODUCT-RESEARCH-PLAYBOOK.md`.
3. Sortir une shortlist via `templates/product-research-scorecard.template.md`.

### Création boutique
1. Remplir `templates/new-boutique-intake.template.md` avec ce qui est connu.
2. `python3 scripts/new_boutique.py <nom-projet>` — crée un dossier projet avec les livrables vierges.
3. Tenir `project-state.md` à jour pendant le lancement.
4. Suivre `PLAYBOOK.md` phase par phase.
5. `python3 scripts/validate_tokens.py <projet>/brand-tokens.json`
6. `python3 scripts/tokens_to_theme.py <projet>/brand-tokens.json <theme>/config/settings_data.json`

## Tests
`python3 -m pytest`

## Pipeline automatisé Dropilot

La configuration opérationnelle unique se trouve dans `config/pipeline.yaml`. L’ancien broyeur sous
`recherche-prod-extracted/` est conservé comme archive et comme suite de régression historique.

Installation recommandée :

```bash
python3 -m venv .venv
.venv/bin/pip install -e '.[dev]'
.venv/bin/dropilot init-db
.venv/bin/python -m pytest
```

Traitement manuel d’un fichier :

```bash
.venv/bin/dropilot run --input candidats.json --source manual
```

Le pipeline normalise, déduplique, score, applique les portes finales, enregistre l’historique dans
SQLite et produit des rapports JSON, CSV et Markdown.

Documentation :

- `docs/ARCHITECTURE.md` ;
- `docs/OPERATIONS.md` ;
- `docs/ROUTINE-HEBDOMADAIRE.md` ;
- `docs/HERMES-VPS.md` ;
- `shopify-portable/README.md`.
