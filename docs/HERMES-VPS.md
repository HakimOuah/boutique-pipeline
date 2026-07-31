# Déploiement VPS et raccordement Hermes

## Installation

```bash
sudo useradd --system --create-home --home-dir /opt/dropilot dropilot
sudo rsync -a --delete ./ /opt/dropilot/
sudo chown -R dropilot:dropilot /opt/dropilot
sudo -u dropilot python3 -m venv /opt/dropilot/.venv
sudo -u dropilot /opt/dropilot/.venv/bin/pip install -e /opt/dropilot
sudo -u dropilot cp /opt/dropilot/.env.example /opt/dropilot/.env
```

Renseigner ensuite `BIGBUY_API_KEY` si l’API BigBuy est utilisée et générer un secret long pour
`DROPILOT_WEBHOOK_TOKEN`. Ne jamais transmettre ces valeurs dans un prompt ou un rapport.

## Services

```bash
sudo cp deploy/systemd/dropilot-* /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now dropilot-webhook.service
sudo systemctl enable --now dropilot-research.timer
```

Le timer traite la boîte d’entrée du lundi au vendredi à 06:30. Le lancement manuel reste disponible :

```bash
/opt/dropilot/automation/manual-trigger.sh
```

## Hermes

Adapter `automation/hermes-tool.example.json` au format exact attendu par l’installation Hermes.
Hermes ne reçoit qu’un nom de fichier, jamais un chemin arbitraire. Le fichier doit avoir été déposé
dans `DROPILOT_INBOX`. Le service refuse les chemins sortant de cette boîte.

## n8n

Créer un appel HTTP `POST http://127.0.0.1:8787/run` avec le header Bearer et un corps comme :

```json
{"input":"bigbuy-2026-07-14.json","source":"bigbuy","format":"json"}
```

Conserver également un déclencheur manuel n8n à côté de toute planification.

## Sécurité

- exposer le service uniquement sur `127.0.0.1` ou derrière un proxy authentifié ;
- ne jamais placer une clé fournisseur dans Git ;
- sauvegarder `data/dropilot.sqlite3` ;
- surveiller les journaux systemd ;
- laisser les métriques non disponibles à `null` plutôt que les inventer.

