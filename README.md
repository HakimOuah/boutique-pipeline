# Boutique Pipeline — Starter-kit Shopify mono-produit

Socle réutilisable pour lancer une boutique Shopify (Approche C : playbook + scripts).

## Démarrage
1. `python3 scripts/new_boutique.py <nom-projet>` — crée un dossier projet avec les livrables vierges.
2. Suivre `PLAYBOOK.md` phase par phase.
3. `python3 scripts/validate_tokens.py <projet>/brand-tokens.json`
4. `python3 scripts/tokens_to_theme.py <projet>/brand-tokens.json <theme>/config/settings_data.json`

## Tests
`python3 -m pytest`
