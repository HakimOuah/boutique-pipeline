#!/usr/bin/env python3
"""Pages + policies + duplication thème Horizon (non publié). Lumière Matière."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from client import gql  # noqa: E402
from md_html import md_to_html  # noqa: E402

PAGES_DIR = ROOT.parent / "pages"
STATE = ROOT / "state.json"

PAGES = [
    ("notre-histoire", "Notre histoire", "notre-histoire.md"),
    ("faq", "FAQ", "faq.md"),
    ("contact", "Contact", "contact.md"),
    ("conditions-paiement", "Paiement", "conditions-paiement.md"),
]

POLICIES = [
    ("TERMS_OF_SERVICE", "cgv.md"),
    ("PRIVACY_POLICY", "politique-confidentialite.md"),
    ("REFUND_POLICY", "politique-retours.md"),
    ("SHIPPING_POLICY", "politique-livraison.md"),
]

LEGAL_NOTICE_HTML = """
<p><strong>Lumière Matière</strong> est le nom commercial sous lequel <strong>OH Ventures</strong>, SASU au capital de 1&nbsp;000&nbsp;€, édite ce site.</p>
<ul>
<li>Siège : 47 rue Vivienne, 75002 Paris, France</li>
<li>SIRET 10315725100010 · TVA FR55103157251</li>
<li>E-mail : <a href="mailto:contact@lumierematiere.fr">contact@lumierematiere.fr</a> · Tél. +33 7 56 91 60 84</li>
<li>Directeur de la publication : le président d'OH Ventures</li>
<li>Hébergement de la boutique : Shopify Inc.</li>
<li>Médiateur de la consommation : CM2C, 14 rue Saint Jean, 75017 Paris. Téléphone 01 89 47 00 14, <a href="https://www.cm2c.net/">https://www.cm2c.net/</a></li>
</ul>
<p>Les conditions générales et les politiques (livraison, retours, confidentialité, paiement) complètent ces mentions.</p>
"""


def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {}


def save_state(state: dict) -> None:
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")


def existing_pages() -> dict[str, str]:
    data = gql(
        """query { pages(first: 50) { nodes { id handle title } } }"""
    )
    return {n["handle"]: n["id"] for n in data["pages"]["nodes"]}


def upsert_page(handle: str, title: str, body: str, known: dict[str, str]) -> str:
    if handle in known:
        data = gql(
            """
            mutation PageUpdate($id: ID!, $page: PageUpdateInput!) {
              pageUpdate(id: $id, page: $page) {
                page { id handle }
                userErrors { field message }
              }
            }
            """,
            {"id": known[handle], "page": {"title": title, "handle": handle, "body": body, "isPublished": True}},
        )
        errs = data["pageUpdate"]["userErrors"]
        if errs:
            raise RuntimeError(errs)
        return data["pageUpdate"]["page"]["id"]
    data = gql(
        """
        mutation PageCreate($page: PageCreateInput!) {
          pageCreate(page: $page) {
            page { id handle }
            userErrors { field message }
          }
        }
        """,
        {"page": {"title": title, "handle": handle, "body": body, "isPublished": True}},
    )
    errs = data["pageCreate"]["userErrors"]
    if errs:
        raise RuntimeError(errs)
    return data["pageCreate"]["page"]["id"]


def upsert_policy(policy_type: str, body: str) -> None:
    data = gql(
        """
        mutation ShopPolicyUpdate($shopPolicy: ShopPolicyInput!) {
          shopPolicyUpdate(shopPolicy: $shopPolicy) {
            shopPolicy { type url }
            userErrors { field message }
          }
        }
        """,
        {"shopPolicy": {"type": policy_type, "body": body}},
    )
    errs = data["shopPolicyUpdate"]["userErrors"]
    if errs:
        msg = " ".join(e.get("message", "") for e in errs)
        if "gestion automatique" in msg.lower() or "automatically" in msg.lower():
            print(f"  SKIP {policy_type} (gestion auto Shopify — à désactiver dans Réglages → Politiques) : {msg}")
            return
        raise RuntimeError(errs)
    print(f"  policy {policy_type} -> {data['shopPolicyUpdate']['shopPolicy']['url']}")


def duplicate_theme() -> str:
    data = gql(
        """
        query {
          themes(first: 20) { nodes { id name role } }
        }
        """
    )
    nodes = data["themes"]["nodes"]
    for n in nodes:
        if n["name"] == "Lumière Matière — UNIVERS" and n["role"] != "MAIN":
            print(f"  theme déjà là {n['id']}")
            return n["id"]
    main = next(n for n in nodes if n["role"] == "MAIN")
    data = gql(
        """
        mutation ThemeDuplicate($id: ID!, $name: String!) {
          themeDuplicate(id: $id, name: $name) {
            newTheme { id name role }
            userErrors { field message }
          }
        }
        """,
        {"id": main["id"], "name": "Lumière Matière — UNIVERS"},
    )
    errs = data["themeDuplicate"]["userErrors"]
    if errs:
        raise RuntimeError(errs)
    theme = data["themeDuplicate"]["newTheme"]
    print(f"  duplicated {main['name']} -> {theme['id']} role={theme['role']}")
    return theme["id"]


def main() -> None:
    state = load_state()
    known = existing_pages()
    print("=== pages ===")
    page_ids = state.get("pages", {})
    for handle, title, filename in PAGES:
        body = md_to_html((PAGES_DIR / filename).read_text(encoding="utf-8"))
        pid = upsert_page(handle, title, body, known)
        page_ids[handle] = pid
        print(f"  {handle} {pid}")
        known[handle] = pid
    state["pages"] = page_ids

    print("=== policies ===")
    for ptype, filename in POLICIES:
        body = md_to_html((PAGES_DIR / filename).read_text(encoding="utf-8"))
        upsert_policy(ptype, body)
    upsert_policy("LEGAL_NOTICE", LEGAL_NOTICE_HTML.strip())

    print("=== theme duplicate ===")
    state["theme_id"] = duplicate_theme()
    save_state(state)
    print("OK", STATE)


if __name__ == "__main__":
    main()
