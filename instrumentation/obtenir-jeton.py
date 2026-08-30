#!/usr/bin/env python3
"""Obtient un jeton Admin API durable pour une boutique, une fois pour toutes.

Pourquoi ce script existe (constat du 30/08/2026) : le *client credentials
grant* ne fonctionne qu'entre une app et des boutiques de la **même
organisation** du dev dashboard. Les boutiques du parc sont des boutiques de
production autonomes, hors organisation — le grant ne les atteint pas. La
route qui reste est l'**authorization code grant** : une autorisation dans le
navigateur, une seule fois par boutique, contre un jeton hors ligne durable.

Le jeton est écrit directement dans le `.env` par le script. Il ne s'affiche
jamais à l'écran et ne transite par aucune conversation.

    export SHOPIFY_CLIENT_ID=...      # ou renseignés dans .env
    export SHOPIFY_CLIENT_SECRET=...
    python3 instrumentation/obtenir-jeton.py --boutique bonum-vitae \\
                                             --domaine kw7vak-g0.myshopify.com
"""
from __future__ import annotations

import argparse
import http.server
import json
import os
import secrets
import sys
import threading
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from pathlib import Path

PORT = 8123
RAPPEL = f"http://localhost:{PORT}/callback"
SCOPES = "read_reports"
ENV = Path(__file__).resolve().parent.parent / ".env"

_recu: dict[str, str] = {}


class Rappel(http.server.BaseHTTPRequestHandler):
    def do_GET(self):  # noqa: N802
        params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        _recu.update({k: v[0] for k, v in params.items()})
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        ok = "code" in _recu
        self.wfile.write(
            ("<h2>" + ("Autorisation reçue. Tu peux fermer cet onglet."
                       if ok else "Aucun code reçu — voir le terminal.")
             + "</h2>").encode()
        )

    def log_message(self, *_):  # silence
        pass


def ecrire_env(cle: str, valeur: str) -> None:
    """Écrit ou remplace une variable dans .env, en préservant le reste."""
    lignes = ENV.read_text(encoding="utf-8").splitlines() if ENV.exists() else []
    sortie, remplace = [], False
    for l in lignes:
        if l.startswith(f"{cle}="):
            sortie.append(f"{cle}={valeur}"); remplace = True
        else:
            sortie.append(l)
    if not remplace:
        sortie.append(f"{cle}={valeur}")
    ENV.write_text("\n".join(sortie) + "\n", encoding="utf-8")
    ENV.chmod(0o600)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--boutique", required=True, help="slug, ex. bonum-vitae")
    ap.add_argument("--domaine", required=True, help="xxx.myshopify.com")
    a = ap.parse_args()

    cid = os.environ.get("SHOPIFY_CLIENT_ID")
    secret = os.environ.get("SHOPIFY_CLIENT_SECRET")
    if not cid or not secret:
        raise SystemExit("SHOPIFY_CLIENT_ID et SHOPIFY_CLIENT_SECRET doivent être "
                         "définis dans l'environnement (ou dans .env, puis `set -a; . ./.env`).")

    etat = secrets.token_urlsafe(24)
    url = f"https://{a.domaine}/admin/oauth/authorize?" + urllib.parse.urlencode({
        "client_id": cid, "scope": SCOPES, "redirect_uri": RAPPEL, "state": etat,
    })

    serveur = http.server.HTTPServer(("localhost", PORT), Rappel)
    threading.Thread(target=serveur.handle_request, daemon=True).start()

    print(f"\nOuvre cette page et approuve l'installation sur {a.domaine} :\n\n  {url}\n")
    try:
        webbrowser.open(url)
    except Exception:
        pass
    print("En attente de l'autorisation…")

    for _ in range(600):
        if _recu:
            break
        __import__("time").sleep(0.5)
    serveur.server_close()

    if _recu.get("state") != etat:
        raise SystemExit(f"État inattendu — autorisation abandonnée. Reçu : {_recu}")
    code = _recu.get("code")
    if not code:
        raise SystemExit(f"Aucun code d'autorisation reçu. Reçu : {_recu}")

    corps = urllib.parse.urlencode({
        "client_id": cid, "client_secret": secret, "code": code,
    }).encode()
    req = urllib.request.Request(
        f"https://{a.domaine}/admin/oauth/access_token", data=corps,
        headers={"Content-Type": "application/x-www-form-urlencoded"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            rep = json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise SystemExit(f"Échange refusé (HTTP {e.code}) — {e.read().decode()[:300]}")

    jeton, portee = rep.get("access_token"), rep.get("scope", "")
    if not jeton:
        raise SystemExit(f"Réponse sans access_token : {rep}")
    if "read_reports" not in portee:
        raise SystemExit(f"Jeton obtenu sans read_reports (scopes : {portee or 'aucun'}).")

    cle = "SHOPIFY_" + a.boutique.upper().replace("-", "_") + "_TOKEN"
    ecrire_env(cle, jeton)
    print(f"\n✓ {cle} écrit dans {ENV} (permissions 600). Scopes : {portee}")
    print("  Le jeton n'a jamais été affiché ici.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
