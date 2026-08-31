#!/usr/bin/env python3
"""Réorganisation de main-menu autour des deux axes de navigation (26/08/2026).

Trois entrées de parcours (Par pièce, Par matière, puis les deux familles de luminaire)
au lieu d'une liste à plat, et les pages de service inchangées.
menuUpdate remplace la totalité des items.
31/08 : `plafonniers-cuisine` et `suspensions-xxl` sortis du menu (1 produit public).
Sauvegarde : backups/2026-08-31-gmc-menu/.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from client import gql  # noqa: E402

HANDLE = "main-menu"

# (titre affiché, type, cible) ; cible = handle de collection, ou URL pour les autres types
ARBRE = [
    ("Accueil", "FRONTPAGE", "/"),
    ("Par pièce", "COLLECTIONS", "/collections", [
        ("Salon", "COLLECTION", "suspensions-salon"),
        ("Chambre", "COLLECTION", "lustres-chambre"),
        ("Cuisine", "COLLECTION", "suspensions-cuisine"),
        ("Plafonniers salon", "COLLECTION", "plafonniers-salon"),
    ]),
    ("Par matière", "COLLECTIONS", "/collections", [
        ("Bambou", "COLLECTION", "suspensions-bambou"),
        ("Rotin", "COLLECTION", "suspensions-rotin"),
        ("Osier", "COLLECTION", "suspensions-osier"),
        ("Bois", "COLLECTION", "suspensions-bois"),
        ("Pierre", "COLLECTION", "suspensions-pierre"),
        ("Verre", "COLLECTION", "suspensions-verre"),
        ("Métal", "COLLECTION", "suspensions-metal"),
        ("Déco colorée", "COLLECTION", "suspensions-deco"),
    ]),
    ("Lustres", "COLLECTION", "lustres-salon", [
        ("Lustres salon", "COLLECTION", "lustres-salon"),
        ("Lustres chambre", "COLLECTION", "lustres-chambre"),
        ("Lustres anneau", "COLLECTION", "lustres-anneau"),
    ]),
    ("Plafonniers LED", "COLLECTION", "plafonniers-led", [
        ("Plafonniers salon", "COLLECTION", "plafonniers-salon"),
    ]),
    ("Appliques murales", "COLLECTION", "appliques-murales"),
    ("Notre histoire", "PAGE", "/pages/notre-histoire"),
    ("FAQ", "PAGE", "/pages/faq"),
    ("Contact", "PAGE", "/pages/contact"),
    ("Suivre votre commande", "HTTP", "/apps/parcelpanel"),
]


def collections() -> dict[str, str]:
    out: dict[str, str] = {}
    cursor = None
    while True:
        data = gql(
            """
            query C($cursor: String) {
              collections(first: 50, after: $cursor) {
                pageInfo { hasNextPage endCursor }
                nodes { id handle }
              }
            }
            """,
            {"cursor": cursor},
        )["collections"]
        out.update({n["handle"]: n["id"] for n in data["nodes"]})
        if not data["pageInfo"]["hasNextPage"]:
            return out
        cursor = data["pageInfo"]["endCursor"]


def pages() -> dict[str, str]:
    data = gql("query { pages(first: 50) { nodes { id handle } } }")
    return {f"/pages/{n['handle']}": n["id"] for n in data["pages"]["nodes"]}


def item(noeud, colls: dict[str, str], pgs: dict[str, str]) -> dict:
    titre, kind, cible = noeud[0], noeud[1], noeud[2]
    enfants = noeud[3] if len(noeud) > 3 else []
    out: dict = {"title": titre, "type": kind}
    if kind == "COLLECTION":
        if cible not in colls:
            raise RuntimeError(f"collection absente du menu : {cible}")
        out["resourceId"] = colls[cible]
    elif kind == "PAGE":
        if cible not in pgs:
            raise RuntimeError(f"page absente : {cible}")
        out["resourceId"] = pgs[cible]
    else:
        out["url"] = cible
    if enfants:
        out["items"] = [item(e, colls, pgs) for e in enfants]
    return out


def main() -> None:
    colls, pgs = collections(), pages()
    menus = gql("query { menus(first: 20) { nodes { id handle title } } }")["menus"]["nodes"]
    menu = next((m for m in menus if m["handle"] == HANDLE), None)
    if not menu:
        raise RuntimeError(f"menu {HANDLE} introuvable")

    items = [item(n, colls, pgs) for n in ARBRE]
    payload = gql(
        """
        mutation M($id: ID!, $title: String!, $handle: String!, $items: [MenuItemUpdateInput!]!) {
          menuUpdate(id: $id, title: $title, handle: $handle, items: $items) {
            menu { id handle items { title items { title } } }
            userErrors { field message }
          }
        }
        """,
        {"id": menu["id"], "title": menu["title"], "handle": HANDLE, "items": items},
    )["menuUpdate"]
    if payload["userErrors"]:
        raise RuntimeError(payload["userErrors"])

    print(f"=== {HANDLE} · {len(items)} entrées de premier niveau ===")
    for entree in payload["menu"]["items"]:
        print(f"  {entree['title']}")
        for enfant in entree["items"]:
            print(f"    - {enfant['title']}")


if __name__ == "__main__":
    main()
