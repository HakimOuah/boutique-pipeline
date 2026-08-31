"""Client GraphQL Admin — token env / .env, sinon auth CLI Shopify (jamais stocké ici)."""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path

STORE = "nzefxg-gg.myshopify.com"
API_VERSION = "2025-07"
CLI_STORE_CONFIG = Path.home() / "Library/Preferences/shopify-cli-store-nodejs/config.json"
PIPELINE_ENV = Path(__file__).resolve().parents[3] / ".env"


def _token_from_dotenv() -> str | None:
    if not PIPELINE_ENV.exists():
        return None
    for line in PIPELINE_ENV.read_text().splitlines():
        if line.startswith("SHOPIFY_LUMIERE_MATIERE_TOKEN="):
            value = line.split("=", 1)[1].strip()
            return value or None
    return None


def access_token() -> str:
    token = os.environ.get("SHOPIFY_LUMIERE_MATIERE_TOKEN") or _token_from_dotenv()
    if token:
        return token
    data = json.loads(CLI_STORE_CONFIG.read_text())
    for key, value in data.items():
        if STORE in key and isinstance(value, dict):
            uid = str(value["currentUserId"])
            return value["sessionsByUserId"][uid]["accessToken"]
    raise RuntimeError(f"Pas de token pour {STORE} — poser SHOPIFY_LUMIERE_MATIERE_TOKEN ou relancer shopify store auth")


def gql(query: str, variables: dict | None = None, *, retries: int = 6) -> dict:
    payload = json.dumps({"query": query, "variables": variables or {}}).encode()
    url = f"https://{STORE}/admin/api/{API_VERSION}/graphql.json"
    last_err = None
    for attempt in range(retries):
        req = urllib.request.Request(
            url,
            data=payload,
            method="POST",
            headers={
                "X-Shopify-Access-Token": access_token(),
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                body = json.loads(resp.read().decode())
        except urllib.error.HTTPError as err:
            last_err = err
            if err.code in (429, 500, 502, 503, 504):
                time.sleep(min(2 ** attempt, 20))
                continue
            raise RuntimeError(f"HTTP {err.code}: {err.read().decode()[:800]}") from err
        if body.get("errors"):
            msg = json.dumps(body["errors"], ensure_ascii=False)
            if "Throttled" in msg or "THROTTLED" in msg:
                time.sleep(min(2 ** attempt, 20))
                continue
            raise RuntimeError(msg)
        return body.get("data") or {}
    raise RuntimeError(f"GraphQL failed after retries: {last_err}")
