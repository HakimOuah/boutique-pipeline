#!/usr/bin/env python3
"""Réimporte les policies LM (pack FR reformulé) + pages CMS. Ne duplique pas de thème."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from bootstrap_pages import (  # noqa: E402
    LEGAL_NOTICE_HTML,
    PAGES,
    POLICIES,
    existing_pages,
    load_state,
    save_state,
    upsert_page,
    upsert_policy,
)
from client import gql  # noqa: E402
from md_html import md_to_html  # noqa: E402

PAGES_DIR = ROOT.parent / "pages"
THEME_FS = "gid://shopify/OnlineStoreTheme/186708001104"
THEME_UNIV = "gid://shopify/OnlineStoreTheme/186708066640"
HEADER = (
    "/*\n * ------------------------------------------------------------\n"
    " * IMPORTANT: The contents of this file are auto-generated.\n *\n"
    " * This file may be updated by the Shopify admin theme editor\n"
    " * or related systems. Please exercise caution as any changes\n"
    " * made to this file may be overwritten.\n"
    " * ------------------------------------------------------------\n */\n"
)


def theme_file_raw(theme_id: str, filename: str) -> str:
    data = gql(
        """
        query ($id: ID!, $names: [String!]) {
          theme(id: $id) {
            files(filenames: $names) {
              nodes { filename body { ... on OnlineStoreThemeFileBodyText { content } } }
            }
          }
        }
        """,
        {"id": theme_id, "names": [filename]},
    )
    nodes = data["theme"]["files"]["nodes"]
    if not nodes:
        raise RuntimeError(f"missing {filename} on {theme_id}")
    return nodes[0]["body"]["content"]


def upsert_theme_file(theme_id: str, filename: str, body: str) -> None:
    payload = gql(
        """
        mutation Upsert($themeId: ID!, $files: [OnlineStoreThemeFilesUpsertFileInput!]!) {
          themeFilesUpsert(themeId: $themeId, files: $files) {
            upsertedThemeFiles { filename }
            userErrors { field message }
          }
        }
        """,
        {
            "themeId": theme_id,
            "files": [{"filename": filename, "body": {"type": "TEXT", "value": body}}],
        },
    )
    errs = payload["themeFilesUpsert"]["userErrors"]
    if errs:
        raise RuntimeError((filename, errs))
    print(f"  template {filename} -> {theme_id.split('/')[-1]}")


def clone_page_faq(theme_id: str) -> None:
    raw = theme_file_raw(theme_id, "templates/page.json")
    stripped = re.sub(r"/\*.*?\*/", "", raw, flags=re.S).strip()
    data = json.loads(stripped)
    body = HEADER + json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    upsert_theme_file(theme_id, "templates/page.faq.json", body)


def set_template_suffix(page_id: str, suffix: str | None) -> None:
    data = gql(
        """
        mutation PageUpdate($id: ID!, $page: PageUpdateInput!) {
          pageUpdate(id: $id, page: $page) {
            page { id handle templateSuffix }
            userErrors { field message }
          }
        }
        """,
        {"id": page_id, "page": {"templateSuffix": suffix}},
    )
    errs = data["pageUpdate"]["userErrors"]
    if errs:
        raise RuntimeError(errs)
    print(f"  suffix {data['pageUpdate']['page']['handle']} = {suffix}")


def main() -> None:
    state = load_state()
    known = existing_pages()
    print("=== pages CMS ===")
    page_ids = state.get("pages", {})
    for handle, title, filename in PAGES:
        body = md_to_html((PAGES_DIR / filename).read_text(encoding="utf-8"))
        pid = upsert_page(handle, title, body, known)
        page_ids[handle] = pid
        known[handle] = pid
        print(f"  {handle} {pid}")
    state["pages"] = page_ids
    save_state(state)

    print("=== shop policies ===")
    for ptype, filename in POLICIES:
        body = md_to_html((PAGES_DIR / filename).read_text(encoding="utf-8"))
        upsert_policy(ptype, body)
    upsert_policy("LEGAL_NOTICE", LEGAL_NOTICE_HTML.strip())

    print("=== templates page.faq (thèmes non publiés) ===")
    for tid in (THEME_FS, THEME_UNIV):
        clone_page_faq(tid)

    # Helio est MAIN : un suffixe faq casserait la page live si page.faq.json n'existe pas.
    # On laisse FAQ sur le gabarit page.json par défaut.
    print("OK policies + pages")


if __name__ == "__main__":
    main()
