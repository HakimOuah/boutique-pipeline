#!/usr/bin/env python3
"""SEO collections Lumière Matière + branchement Full Stack (description Liquid)."""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from apply_fullstack import theme_file, upsert_theme_file  # noqa: E402
from client import gql  # noqa: E402
from import_catalogue import COLLECTIONS  # noqa: E402

SEO = json.loads((ROOT / "collections-seo.json").read_text(encoding="utf-8"))
STATE = json.loads((ROOT / "state.json").read_text(encoding="utf-8"))

HANDLE_TO_GID = {}
for csv_name, gid in STATE["collections"].items():
    if csv_name == "selection-199":
        HANDLE_TO_GID["selection-199"] = gid
        continue
    meta = COLLECTIONS.get(csv_name)
    if not meta:
        raise RuntimeError(f"collection state sans mapping: {csv_name}")
    HANDLE_TO_GID[meta[1]] = gid


def patch_collection_template() -> None:
    data = theme_file("templates/collection.json")
    blob = json.dumps(data, ensure_ascii=False)
    if "Lorem ipsum" not in blob and "{{ closest.collection.description }}" in blob:
        print("  collection.json déjà branché (pas de Lorem)")
        return
    try:
        block = data["sections"]["custom_section_NyAmKB"]["blocks"]["group_Y8NX6K"]["blocks"]["text_GMnLLj"]
    except KeyError as err:
        raise RuntimeError(f"chemin Liquid collection.json introuvable: {err}") from err
    current = block["settings"].get("text", "")
    if "Lorem ipsum" not in current and "{{ closest.collection.description }}" in current:
        print("  text_GMnLLj déjà branché")
        return
    if "Lorem ipsum" not in current:
        raise RuntimeError(f"texte inattendu dans text_GMnLLj: {current[:180]!r}")
    block["settings"]["text"] = "{{ closest.collection.description }}"
    upsert_theme_file("templates/collection.json", data)
    print("  collection.json : Lorem → {{ closest.collection.description }}")


def update_collections() -> None:
    missing = set(SEO) - set(HANDLE_TO_GID)
    extra = set(HANDLE_TO_GID) - set(SEO)
    if missing:
        raise RuntimeError(f"SEO sans GID: {sorted(missing)}")
    if extra:
        print(f"  skip handles sans SEO: {sorted(extra)}")
    ok = 0
    for handle, copy in SEO.items():
        gid = HANDLE_TO_GID[handle]
        payload = gql(
            """
            mutation U($input: CollectionInput!) {
              collectionUpdate(input: $input) {
                collection { id handle seo { title description } }
                userErrors { field message }
              }
            }
            """,
            {
                "input": {
                    "id": gid,
                    "descriptionHtml": copy["description_html"],
                    "seo": {
                        "title": copy["seo_title"],
                        "description": copy["seo_description"],
                    },
                }
            },
        )
        errs = payload["collectionUpdate"]["userErrors"]
        if errs:
            raise RuntimeError((handle, errs))
        coll = payload["collectionUpdate"]["collection"]
        print(f"  {coll['handle']} · {len(copy['seo_title'])}c / {len(copy['seo_description'])}c")
        ok += 1
        time.sleep(0.15)
    print(f"OK {ok} collections")


def verify() -> None:
    handles = list(SEO)
    data = gql(
        """
        query {
          collections(first: 50) {
            nodes {
              handle
              description
              seo { title description }
            }
          }
        }
        """
    )
    by_handle = {n["handle"]: n for n in data["collections"]["nodes"]}
    for handle in handles:
        node = by_handle.get(handle)
        if not node:
            raise RuntimeError(f"collection absente: {handle}")
        if not (node.get("description") or "").strip():
            raise RuntimeError(f"description vide: {handle}")
        if "Lorem" in (node.get("description") or ""):
            raise RuntimeError(f"Lorem restant: {handle}")
        seo = node.get("seo") or {}
        if not seo.get("title") or not seo.get("description"):
            raise RuntimeError(f"SEO vide: {handle}")
    tmpl = theme_file("templates/collection.json")
    blob = json.dumps(tmpl, ensure_ascii=False)
    if "Lorem ipsum" in blob:
        raise RuntimeError("Lorem encore dans templates/collection.json Full Stack")
    if "{{ closest.collection.description }}" not in blob:
        raise RuntimeError("Liquid description absent du template Full Stack")
    print("vérif GraphQL + template OK")


def main() -> None:
    print("— collections SEO")
    update_collections()
    print("— Full Stack collection.json")
    patch_collection_template()
    verify()


if __name__ == "__main__":
    main()
