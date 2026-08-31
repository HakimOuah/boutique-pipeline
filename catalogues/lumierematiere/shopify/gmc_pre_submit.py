#!/usr/bin/env python3
"""Corrections GMC Lumière Matière — lots 2 à 6 du brief 31/08/2026.

Ne touche jamais aux SKU variantes, ne publie jamais un thème, ne publie jamais un brouillon.
Lot 1.1 (adresse boutique) reste manuel dans l'admin.

Usage :
  python3 gmc_pre_submit.py --audit
  python3 gmc_pre_submit.py --apply-texts
  python3 gmc_pre_submit.py --apply-media
  python3 gmc_pre_submit.py --apply-theme
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from client import gql  # noqa: E402
from md_html import md_to_html  # noqa: E402

PAGES = ROOT.parent / "pages"
OUT = ROOT / "GMC-PRE-SOUMISSION-2026-08-31.md"
THIN = [
    "suspensions-xxl",
    "plafonniers-cuisine",
    "suspensions-osier",
    "lustres-chambre",
    "suspensions-bambou",
    "suspensions-pierre",
    "suspensions-salon",
]
CODEX_HANDLES = {
    "suspension-verre-538307",
    "suspension-verre-bois-910933",
    "suspension-verre-405368",
    "applique-murale-verre-829449",
    "applique-double-travertin-474088",
    "applique-liseuse-pierre-311650",
    "applique-murale-pierre-588683",
}
AE_HANDLE = "applique-murale-pierre-metal-147598"
SOCIAL_KEYS = (
    "instagram_url",
    "facebook_url",
    "youtube_url",
    "linkedin_url",
    "twitter_url",
    "tiktok_url",
    "pinterest_url",
    "snapchat_url",
)
LD_CANDIDATES = [
    "snippets/structured-data.liquid",
    "snippets/seo-settings.liquid",
    "snippets/meta-tags.liquid",
    "snippets/schema.liquid",
    "layout/theme.liquid",
]


def fetch_products() -> list[dict]:
    q = """
    query($c: String) {
      products(first: 80, after: $c) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id handle status tags
          variants(first: 50) {
            nodes { sku price compareAtPrice }
          }
          media(first: 20) {
            nodes {
              id alt
              ... on MediaImage { image { url } }
            }
          }
          collections(first: 30) { nodes { handle title } }
        }
      }
    }
    """
    out, cursor = [], None
    while True:
        data = gql(q, {"c": cursor})["products"]
        out.extend(data["nodes"])
        if not data["pageInfo"]["hasNextPage"]:
            break
        cursor = data["pageInfo"]["endCursor"]
    return out


def lm_code(product: dict) -> str:
    for tag in product.get("tags") or []:
        if re.fullmatch(r"LM-\d+", tag):
            return tag
    return ""


def audit(products: list[dict]) -> dict:
    barred = []
    for p in products:
        for v in p["variants"]["nodes"]:
            if v.get("compareAtPrice"):
                barred.append(
                    {
                        "handle": p["handle"],
                        "status": p["status"],
                        "sku": v.get("sku"),
                        "price": v.get("price"),
                        "compareAtPrice": v.get("compareAtPrice"),
                    }
                )
    thin = {}
    for handle in THIN:
        drafts = []
        for p in products:
            if p["status"] != "DRAFT":
                continue
            if any(c["handle"] == handle for c in p["collections"]["nodes"]):
                caps = [v.get("compareAtPrice") for v in p["variants"]["nodes"]]
                drafts.append(
                    {
                        "handle": p["handle"],
                        "lm": lm_code(p),
                        "compareAtPrice": [c for c in caps if c],
                    }
                )
        thin[handle] = drafts
    return {"compare_at": barred, "thin_drafts": thin}


def write_audit_md(report: dict) -> None:
    lines = [
        "# Audit catalogue GMC — 31/08/2026",
        "",
        "Lecture seule. Aucune publication.",
        "",
        "## 6.1 Prix barrés dormants",
        "",
    ]
    barred = report["compare_at"]
    if not barred:
        lines.append("Aucun `compareAtPrice` non nul (ACTIVE, DRAFT, ARCHIVED).")
    else:
        lines += [
            "| handle | statut | sku | price | compareAtPrice |",
            "|---|---|---|---:|---:|",
        ]
        for row in barred:
            lines.append(
                f"| `{row['handle']}` | {row['status']} | `{row['sku']}` | {row['price']} | {row['compareAtPrice']} |"
            )
    lines += ["", "## 6.2 Brouillons des collections maigres", ""]
    for handle, drafts in report["thin_drafts"].items():
        lines.append(f"### `{handle}` — {len(drafts)} brouillon(s) rattaché(s)")
        if not drafts:
            lines.append("Aucun brouillon déjà dans cette collection.")
        else:
            lines += ["| handle | LM | compareAtPrice |", "|---|---|---|"]
            for d in drafts:
                caps = ", ".join(d["compareAtPrice"]) or "—"
                lines.append(f"| `{d['handle']}` | {d['lm'] or '—'} | {caps} |")
        lines.append("")
    path = ROOT / "GMC-AUDIT-CATALOGUE-2026-08-31.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("écrit", path)


def apply_alts(products: list[dict]) -> int:
    n = 0
    for p in products:
        if p["handle"] not in CODEX_HANDLES:
            continue
        files = []
        for m in p["media"]["nodes"]:
            alt = m.get("alt") or ""
            if "vue Codex " not in alt:
                continue
            files.append({"id": m["id"], "alt": alt.replace("vue Codex ", "vue ")})
        if not files:
            continue
        data = gql(
            """
            mutation($files: [FileUpdateInput!]!) {
              fileUpdate(files: $files) {
                userErrors { field message }
              }
            }
            """,
            {"files": files},
        )
        errs = data["fileUpdate"]["userErrors"]
        if errs:
            raise RuntimeError(errs)
        print(f"  alt {p['handle']} {len(files)}")
        n += len(files)
    return n


def apply_ae_rename(products: list[dict]) -> None:
    target = next((p for p in products if p["handle"] == AE_HANDLE), None)
    if not target:
        raise RuntimeError(f"fiche {AE_HANDLE} introuvable")
    print(f"  AE rename : {len(target['media']['nodes'])} médias — téléchargement + restage")
    print("  STOP : le renommage CDN exige write_files + staged upload.")
    print("  Les alts sont déjà au format « vue N ». À relancer avec --apply-ae une fois les scopes ouverts.")


def apply_texts() -> None:
    faq_html = md_to_html((PAGES / "faq.md").read_text(encoding="utf-8"))
    pages = gql("""query { pages(first: 50) { nodes { id handle } } }""")["pages"]["nodes"]
    faq = next(p for p in pages if p["handle"] == "faq")
    data = gql(
        """
        mutation($id: ID!, $page: PageUpdateInput!) {
          pageUpdate(id: $id, page: $page) {
            userErrors { field message }
          }
        }
        """,
        {"id": faq["id"], "page": {"body": faq_html}},
    )
    if data["pageUpdate"]["userErrors"]:
        raise RuntimeError(data["pageUpdate"]["userErrors"])
    print("  FAQ mise à jour")

    pay = next((p for p in pages if p["handle"] == "conditions-paiement"), None)
    if pay:
        body = md_to_html((PAGES / "conditions-paiement.md").read_text(encoding="utf-8"))
        data = gql(
            """
            mutation($id: ID!, $page: PageUpdateInput!) {
              pageUpdate(id: $id, page: $page) {
                userErrors { field message }
              }
            }
            """,
            {"id": pay["id"], "page": {"body": body}},
        )
        if data["pageUpdate"]["userErrors"]:
            raise RuntimeError(data["pageUpdate"]["userErrors"])
        print("  page Paiement mise à jour")

    cgv = md_to_html((PAGES / "cgv.md").read_text(encoding="utf-8"))
    data = gql(
        """
        mutation($shopPolicy: ShopPolicyInput!) {
          shopPolicyUpdate(shopPolicy: $shopPolicy) {
            userErrors { field message }
          }
        }
        """,
        {"shopPolicy": {"type": "TERMS_OF_SERVICE", "body": cgv}},
    )
    errs = data["shopPolicyUpdate"]["userErrors"]
    if errs:
        raise RuntimeError(errs)
    print("  CGV mises à jour")


def theme_file(theme_id: str, filename: str) -> str:
    data = gql(
        """
        query($id: ID!, $names: [String!]) {
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
        return ""
    return nodes[0]["body"]["content"] or ""


def upsert_text(theme_id: str, filename: str, body: str) -> None:
    data = gql(
        """
        mutation($themeId: ID!, $files: [OnlineStoreThemeFilesUpsertFileInput!]!) {
          themeFilesUpsert(themeId: $themeId, files: $files) {
            userErrors { field message }
          }
        }
        """,
        {
            "themeId": theme_id,
            "files": [{"filename": filename, "body": {"type": "TEXT", "value": body}}],
        },
    )
    errs = data["themeFilesUpsert"]["userErrors"]
    if errs:
        raise RuntimeError(errs)


def apply_theme() -> str:
    themes = gql("""query { themes(first: 30) { nodes { id name role } } }""")["themes"]["nodes"]
    main = next(t for t in themes if t["role"] == "MAIN")
    name = "LM GMC 2026-08-31"
    existing = next((t for t in themes if t["name"] == name and t["role"] != "MAIN"), None)
    if existing:
        copy_id = existing["id"]
        print("  copie déjà là", copy_id)
    else:
        data = gql(
            """
            mutation($id: ID!, $name: String!) {
              themeDuplicate(id: $id, name: $name) {
                newTheme { id name role }
                userErrors { field message }
              }
            }
            """,
            {"id": main["id"], "name": name},
        )
        errs = data["themeDuplicate"]["userErrors"]
        if errs:
            raise RuntimeError(errs)
        copy_id = data["themeDuplicate"]["newTheme"]["id"]
        role = data["themeDuplicate"]["newTheme"]["role"]
        if role == "MAIN":
            raise RuntimeError("la copie a pris le rôle MAIN — abandon")
        print("  copie créée", copy_id, "role", role)

    raw = theme_file(copy_id, "config/settings_data.json")
    if not raw:
        raise RuntimeError("settings_data.json introuvable sur la copie")
    cleaned = re.sub(r"/\*.*?\*/", "", raw, flags=re.S).strip()
    settings = json.loads(cleaned)
    current = settings.get("current") or {}
    changed = False
    for key in SOCIAL_KEYS:
        val = current.get(key) or ""
        if "themefullstack" in str(val).lower():
            current[key] = ""
            changed = True
            print(f"  social vidé {key}")
    if changed:
        settings["current"] = current
        header = (
            "/*\n * ------------------------------------------------------------\n"
            " * IMPORTANT: The contents of this file are auto-generated.\n *\n"
            " * This file may be updated by the Shopify admin theme editor\n"
            " * or related systems. Please exercise caution as any changes\n"
            " * made to this file may be overwritten.\n"
            " * ------------------------------------------------------------\n */\n"
        )
        upsert_text(copy_id, "config/settings_data.json", header + json.dumps(settings, ensure_ascii=False, indent=2) + "\n")

    for filename in LD_CANDIDATES:
        body = theme_file(copy_id, filename)
        if not body or "sku" not in body.lower():
            continue
        if "ld+json" not in body and "schema.org" not in body:
            continue
        new = re.sub(
            r'([,{{])\s*"sku"\s*:\s*\{\{\s*[^}]+\.sku[^}]*\}\}\s*,?',
            r"\1",
            body,
        )
        new = re.sub(r",\s*}", "}", new)
        if new != body:
            upsert_text(copy_id, filename, new)
            print(f"  sku retiré du JSON-LD dans {filename}")
        else:
            print(f"  sku présent dans {filename} — à relire à la main")
    return copy_id


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit", action="store_true")
    parser.add_argument("--apply-texts", action="store_true")
    parser.add_argument("--apply-media", action="store_true")
    parser.add_argument("--apply-theme", action="store_true")
    args = parser.parse_args()
    if not any([args.audit, args.apply_texts, args.apply_media, args.apply_theme]):
        parser.print_help()
        sys.exit(2)
    products = None
    if args.audit or args.apply_media:
        products = fetch_products()
    if args.audit:
        write_audit_md(audit(products))
    if args.apply_texts:
        apply_texts()
    if args.apply_media:
        n = apply_alts(products)
        print(f"  {n} alts Codex corrigés")
        apply_ae_rename(products)
    if args.apply_theme:
        apply_theme()


if __name__ == "__main__":
    main()
