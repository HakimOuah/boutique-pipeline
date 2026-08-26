"""Overlay des 3 suspensions verre poussées par DSers (LM-128/129/130).

Reprend chaque brouillon DSers (titre usine, variantes, sku_attr) et applique
la copy maison. Les SKU DSers des variantes conservées ne sont jamais touchés.

Les prix ne sont écrits que si cout_dsers est renseigné. Sinon la fiche reste
DRAFT, coût et PV à caler après lecture DSers.

    python3 apply_verre.py --dry-run
    python3 apply_verre.py
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from client import gql  # noqa: E402
from import_catalogue import add_to_collection  # noqa: E402

COPY = json.loads((HERE / "verre-copy.json").read_text(encoding="utf-8"))
BACKUP_DIR = HERE / "backups" / f"{date.today().isoformat()}-verre"

PRODUCT_QUERY = """
query($handle: String!) {
  productByHandle(handle: $handle) {
    id handle title status
    options { id name optionValues { id name } }
    media(first: 50) { nodes { ... on MediaImage { id alt } } }
    variants(first: 100) { nodes { id sku title price } }
  }
}
"""

PRODUCT_ID_QUERY = """
query($id: ID!) {
  product(id: $id) {
    id handle title status
    options { id name optionValues { id name } }
    media(first: 50) { nodes { ... on MediaImage { id alt } } }
    variants(first: 100) { nodes { id sku title price } }
  }
}
"""


def check(payload: dict, key: str) -> dict:
    node = payload[key]
    errors = node.get("userErrors") or []
    if errors:
        raise RuntimeError(f"{key}: {json.dumps(errors, ensure_ascii=False)}")
    return node


def specs_html(rows: list[list[str]]) -> str:
    items = "".join(f"<li><strong>{label} :</strong> {value}</li>" for label, value in rows)
    return f"<ul>{items}</ul>"


def collection_id(handle: str) -> str | None:
    data = gql(
        "query($h: String!) { collectionByHandle(handle: $h) { id } }", {"h": handle}
    )
    node = data.get("collectionByHandle")
    return node["id"] if node else None


def find_product(spec: dict) -> dict:
    handles = [h for h in (spec.get("handle_dsers"), spec["handle"]) if h]
    for handle in handles:
        product = gql(PRODUCT_QUERY, {"handle": handle}).get("productByHandle")
        if product:
            return product
    sku = spec["variantes"][0]["sku"]
    data = gql(
        """
        query($q: String!) {
          products(first: 5, query: $q) {
            nodes { id handle }
          }
        }
        """,
        {"q": f"sku:{json.dumps(sku)[1:-1]}"},
    )
    nodes = data["products"]["nodes"]
    if len(nodes) == 1:
        return gql(PRODUCT_ID_QUERY, {"id": nodes[0]["id"]})["product"]
    tried = " / ".join(handles) or "(aucun handle)"
    raise RuntimeError(
        f"{spec['ref']} introuvable ({tried}, sku {sku!r}). "
        "Pousser d’abord la fiche depuis DSers."
    )


def apply_product(spec: dict, dry: bool) -> dict:
    print(f"\n== {spec['ref']} {spec['lm']} — {spec['title']}")
    live = find_product(spec)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    (BACKUP_DIR / f"{spec['ref']}-avant.json").write_text(
        json.dumps(live, ensure_ascii=False, indent=1), encoding="utf-8"
    )

    by_sku = {v["sku"]: v for v in live["variants"]["nodes"]}
    keep = []
    for var in spec["variantes"]:
        node = by_sku.get(var["sku"])
        if node is None:
            raise RuntimeError(f"SKU absent de la fiche live : {var['sku']}")
        keep.append((var, node))
    keep_ids = {node["id"] for _, node in keep}
    drop_ids = [v["id"] for v in live["variants"]["nodes"] if v["id"] not in keep_ids]

    print(f"  variantes : {len(keep)} gardées, {len(drop_ids)} supprimées")
    if drop_ids and not dry:
        check(
            gql(
                """
                mutation($productId: ID!, $ids: [ID!]!) {
                  productVariantsBulkDelete(productId: $productId, variantsIds: $ids) {
                    userErrors { field message }
                  }
                }
                """,
                {"productId": live["id"], "ids": drop_ids},
            ),
            "productVariantsBulkDelete",
        )

    dead = [o for o in live["options"] if o["name"] in spec["options_a_supprimer"]]
    if dead and not dry:
        check(
            gql(
                """
                mutation($productId: ID!, $options: [ID!]!) {
                  productOptionsDelete(
                    productId: $productId, options: $options,
                    strategy: NON_DESTRUCTIVE
                  ) { userErrors { field message } }
                }
                """,
                {"productId": live["id"], "options": [o["id"] for o in dead]},
            ),
            "productOptionsDelete",
        )
    if dead:
        print("  options retirées : " + ", ".join(o["name"] for o in dead))

    if spec["option_final"]:
        remaining = [o for o in live["options"] if o["name"] not in spec["options_a_supprimer"]]
        if len(remaining) != 1:
            raise RuntimeError(f"{spec['ref']} : {len(remaining)} options restantes, attendu 1")
        option = remaining[0]
        wanted = {}
        for var, node in keep:
            for value in option["optionValues"]:
                if value["name"] in node["title"].split(" / "):
                    wanted[value["id"]] = var["valeur"]
        updates = [{"id": vid, "name": name} for vid, name in wanted.items() if name]
        if len(updates) != len([k for k in keep if k[0]["valeur"]]):
            raise RuntimeError(
                f"{spec['ref']} : appariement valeurs incomplet ({len(updates)}/{len(keep)})"
            )
        print(f"  option « {option['name']} » → « {spec['option_final']} » : "
              + ", ".join(u["name"] for u in updates))
        if not dry:
            check(
                gql(
                    """
                    mutation($productId: ID!, $option: OptionUpdateInput!,
                             $values: [OptionValueUpdateInput!]) {
                      productOptionUpdate(
                        productId: $productId, option: $option,
                        optionValuesToUpdate: $values,
                        variantStrategy: LEAVE_AS_IS
                      ) { userErrors { field message } }
                    }
                    """,
                    {
                        "productId": live["id"],
                        "option": {"id": option["id"], "name": spec["option_final"]},
                        "values": updates,
                    },
                ),
                "productOptionUpdate",
            )

    priced = [(var, node) for var, node in keep if var.get("cout_dsers") is not None]
    if priced:
        price_input = [
            {"id": node["id"], "price": var["prix"], "compareAtPrice": None}
            for var, node in priced
        ]
        for var, node in priced:
            cost = var["cout_dsers"] + 2.0
            ht = float(var["prix"]) / 1.2
            marge = ht - cost
            print(f"    {var['valeur'] or 'unique'}: {var['prix']} € TTC — rendu {cost:.2f} € "
                  f"→ marge {marge:.2f} € HT ({marge / ht * 100:.0f} %)")
        if not dry:
            check(
                gql(
                    """
                    mutation($productId: ID!, $variants: [ProductVariantsBulkInput!]!) {
                      productVariantsBulkUpdate(productId: $productId, variants: $variants) {
                        userErrors { field message }
                      }
                    }
                    """,
                    {"productId": live["id"], "variants": price_input},
                ),
                "productVariantsBulkUpdate",
            )
    else:
        print(f"  prix non écrits (cout_dsers manquant), PV prévu {spec.get('prix_prevu')}")

    seo_title = f"{spec['title']} | Lumière Matière"
    if len(seo_title) > 70:
        seo_title = seo_title[:70].rstrip()
    product_input = {
        "id": live["id"],
        "title": spec["title"],
        "handle": spec["handle"],
        "descriptionHtml": spec["description_html"],
        "productType": spec["product_type"],
        "vendor": "Lumière Matière",
        "tags": [spec["lm"], spec["product_type"]],
        "seo": {"title": seo_title, "description": spec["seo_description"]},
        "status": "DRAFT",
    }
    if not dry:
        check(
            gql(
                """
                mutation($product: ProductUpdateInput!) {
                  productUpdate(product: $product) {
                    product { id handle title }
                    userErrors { field message }
                  }
                }
                """,
                {"product": product_input},
            ),
            "productUpdate",
        )
    print(f"  handle → {spec['handle']} | SEO {len(seo_title)}/70")

    faq = spec["faq"] + COPY["faq_commune"]
    metafields = [
        {"namespace": "custom", "key": "usps", "type": "list.single_line_text_field",
         "value": json.dumps(spec["usps"], ensure_ascii=False)},
        {"namespace": "custom", "key": "specs", "type": "multi_line_text_field",
         "value": specs_html(spec["specs"])},
        {"namespace": "custom", "key": "installation", "type": "multi_line_text_field",
         "value": spec["installation"]},
        {"namespace": "custom", "key": "benefits", "type": "json",
         "value": json.dumps(spec["benefits"], ensure_ascii=False)},
        {"namespace": "custom", "key": "faq", "type": "json",
         "value": json.dumps(faq, ensure_ascii=False)},
        {"namespace": "global", "key": "title_tag", "type": "string", "value": seo_title},
        {"namespace": "global", "key": "description_tag", "type": "string",
         "value": spec["seo_description"]},
    ]
    for m in metafields:
        m["ownerId"] = live["id"]
    if not dry:
        check(
            gql(
                """
                mutation($metafields: [MetafieldsSetInput!]!) {
                  metafieldsSet(metafields: $metafields) {
                    userErrors { field message }
                  }
                }
                """,
                {"metafields": metafields},
            ),
            "metafieldsSet",
        )
    print(f"  metafields : {len(metafields)} (faq {len(faq)} questions)")

    media = live["media"]["nodes"]
    files = [
        {"id": m["id"], "alt": f"{spec['title']}, vue {i}"}
        for i, m in enumerate(media, start=1)
    ]
    if files and not dry:
        check(
            gql(
                """
                mutation($files: [FileUpdateInput!]!) {
                  fileUpdate(files: $files) { userErrors { field message } }
                }
                """,
                {"files": files},
            ),
            "fileUpdate",
        )
    print(f"  alt réécrits : {len(files)}")

    if not dry:
        for handle in spec.get("collections") or []:
            cid = collection_id(handle)
            if not cid:
                print(f"  collection absente : {handle}")
                continue
            add_to_collection(cid, live["id"])
            print(f"  + {handle}")

    print(f"  statut : DRAFT" + (f" — {spec['bloque']}" if spec.get("bloque") else ""))
    return {"ref": spec["ref"], "id": live["id"], "handle": spec["handle"], "status": "DRAFT"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--only", help="refs séparées par des virgules (V1,V3)")
    args = parser.parse_args()

    todo = COPY["produits"]
    if args.only:
        wanted = {r.strip() for r in args.only.split(",")}
        todo = [p for p in todo if p["ref"] in wanted]

    print(f"{'[DRY RUN] ' if args.dry_run else ''}{len(todo)} fiches verre")
    results = [apply_product(spec, args.dry_run) for spec in todo]
    print("\n== bilan")
    for r in results:
        print(f"  {r['ref']:<3} {r['status']:<7} /products/{r['handle']}")


if __name__ == "__main__":
    main()
