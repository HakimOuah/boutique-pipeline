#!/usr/bin/env python3
"""Outils GraphQL thème Tuftéo via `shopify store execute` — jamais le MAIN."""
from __future__ import annotations

import json
import subprocess
import sys
import time

STORE = "et0hua-w1.myshopify.com"
MAIN = "gid://shopify/OnlineStoreTheme/189437772161"
COPY = "gid://shopify/OnlineStoreTheme/190113350017"
OLD = "gid://shopify/OnlineStoreTheme/188623847809"


def gql(query: str, muter: bool = False) -> dict:
    cmd = ["shopify", "store", "execute", "--store", STORE, "--json", "--query", query]
    if muter:
        cmd.append("--allow-mutations")
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = r.stdout
    i = out.find("{")
    if i < 0:
        raise SystemExit("Réponse CLI illisible:\n" + out + r.stderr)
    data = json.loads(out[i:])
    if data.get("errors"):
        raise SystemExit(json.dumps(data["errors"], indent=2, ensure_ascii=False))
    return data


def theme_meta(theme_id: str) -> dict:
    q = (
        '{ theme(id: "%s") { id name role processing updatedAt } }' % theme_id
    )
    return gql(q)["theme"]


def wait_ready(theme_id: str, timeout: int = 180) -> dict:
    t0 = time.time()
    while time.time() - t0 < timeout:
        meta = theme_meta(theme_id)
        if meta.get("role") == "MAIN":
            raise SystemExit("ABORT: la copie est MAIN")
        if not meta.get("processing"):
            return meta
        time.sleep(3)
    raise SystemExit("timeout processing")


def theme_file(theme_id: str, filename: str) -> str:
    q = """
    { theme(id: "%s") { files(filenames: ["%s"]) {
        nodes { filename checksumMd5 size
          body { ... on OnlineStoreThemeFileBodyText { content } }
        } } } }
    """ % (theme_id, filename)
    nodes = gql(q)["theme"]["files"]["nodes"]
    if not nodes:
        raise SystemExit(f"fichier absent: {filename}")
    body = nodes[0].get("body") or {}
    return body.get("content") or ""


def upsert_text(theme_id: str, filename: str, content: str) -> None:
    if theme_id == MAIN:
        raise SystemExit("refus: écriture MAIN")
    # Shopify store execute --query is a string; escape via JSON in a mutation
    # with variables is cleaner but CLI may not take variables. Use TEXT body.
    payload = {
        "filename": filename,
        "body": {"type": "TEXT", "value": content},
    }
    q = (
        "mutation { themeFilesUpsert(themeId: \"%s\", files: [%s]) "
        "{ upsertedThemeFiles { filename } userErrors { field message } } }"
        % (theme_id, _file_input(payload))
    )
    data = gql(q, muter=True)
    errs = data["themeFilesUpsert"]["userErrors"]
    if errs:
        raise SystemExit(json.dumps(errs, ensure_ascii=False, indent=2))


def _file_input(payload: dict) -> str:
    fn = payload["filename"].replace("\\", "\\\\").replace('"', '\\"')
    val = payload["body"]["value"]
    # GraphQL string: escape \ and "
    val = val.replace("\\", "\\\\").replace('"', '\\"')
    return '{ filename: "%s", body: { type: TEXT, value: """%s""" } }' % (fn, payload["body"]["value"])


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "status":
        print(json.dumps(theme_meta(COPY), indent=2, ensure_ascii=False))
    elif cmd == "wait":
        print(json.dumps(wait_ready(COPY), indent=2, ensure_ascii=False))
    elif cmd == "get":
        print(theme_file(sys.argv[2], sys.argv[3]))
    else:
        raise SystemExit("usage: status|wait|get <theme_id> <filename>")
