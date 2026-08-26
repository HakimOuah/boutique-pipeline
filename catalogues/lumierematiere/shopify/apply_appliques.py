"""Overlay des 5 appliques poussées par DSers le 26/08/2026.

Reprend chaque fiche brouillon telle que DSers l'a créée (titre anglais, variantes
d'usine, compareAtPrice = prix) et applique la copy maison : titre convention,
handle FR, description, metafields PDP, variantes réduites et renommées, prix,
collection, SEO, alt.

Les SKU DSers (`sku_attr`) ne sont jamais touchés sur les variantes conservées.

    python3 apply_appliques.py --dry-run
    python3 apply_appliques.py
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from apply_fullstack import theme_file, upsert_theme_file  # noqa: E402
from client import gql  # noqa: E402
from import_catalogue import publish  # noqa: E402

COPY = json.loads((HERE / "appliques-copy.json").read_text(encoding="utf-8"))
BACKUP_DIR = HERE / "backups" / f"{date.today().isoformat()}-appliques"

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


def fetch(*handles: str) -> dict:
    """Rejouable : la fiche répond d'abord sur son handle DSers, puis sur le handle FR."""
    for handle in handles:
        product = gql(PRODUCT_QUERY, {"handle": handle}).get("productByHandle")
        if product:
            return product
    raise RuntimeError(f"Fiche introuvable : {' / '.join(handles)}")


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


def ensure_collection(dry: bool) -> str | None:
    spec = COPY["collection"]
    existing = collection_id(spec["handle"])
    if existing:
        if not dry:
            publish(existing)
        print(f"  collection {spec['handle']} déjà là, publiée")
        return existing
    if dry:
        print(f"  [dry] créerait la collection {spec['handle']}")
        return None
    node = check(
        gql(
            """
            mutation($input: CollectionInput!) {
              collectionCreate(input: $input) {
                collection { id handle }
                userErrors { field message }
              }
            }
            """,
            {
                "input": {
                    "handle": spec["handle"],
                    "title": spec["title"],
                    "descriptionHtml": spec["description_html"],
                    "seo": {
                        "title": spec["seo_title"],
                        "description": spec["seo_description"],
                    },
                }
            },
        ),
        "collectionCreate",
    )
    cid = node["collection"]["id"]
    publish(cid)
    print(f"  collection créée et publiée : {spec['handle']}")
    return cid


def vitrine(coll_id: str | None, dry: bool) -> None:
    """Image de collection reprise de la première fiche, puis vignette sur /collections."""
    handle = COPY["collection"]["handle"]
    if coll_id:
        data = gql(
            "query($id: ID!) { collection(id: $id) { image { url } } }", {"id": coll_id}
        )["collection"]
        if data["image"]:
            print("  image de collection déjà posée")
        else:
            first = COPY["produits"][0]
            media = fetch(first["handle"])["media"]["nodes"]
            if media and not dry:
                url = gql(
                    "query($id: ID!) { node(id: $id) { ... on MediaImage { image { url } } } }",
                    {"id": media[0]["id"]},
                )["node"]["image"]["url"]
                check(
                    gql(
                        """
                        mutation($input: CollectionInput!) {
                          collectionUpdate(input: $input) {
                            userErrors { field message }
                          }
                        }
                        """,
                        {
                            "input": {
                                "id": coll_id,
                                "image": {"src": url, "altText": COPY["collection"]["title"]},
                            }
                        },
                    ),
                    "collectionUpdate",
                )
                print("  image de collection posée")

    path = "templates/list-collections.json"
    data = theme_file(path)
    settings = data["sections"]["main"]["settings"]
    listing = list(settings["collection_list"])
    if handle in listing:
        print(f"  {path} contient déjà {handle}")
        return
    listing.append(handle)
    print(f"  {path} : {len(settings['collection_list'])} -> {len(listing)} vignettes")
    if not dry:
        settings["collection_list"] = listing
        upsert_theme_file(path, data)


def apply_product(spec: dict, coll_id: str | None, dry: bool) -> dict:
    print(f"\n== {spec['ref']} {spec['lm']} — {spec['title']}")
    live = fetch(spec["handle_dsers"], spec["handle"])
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

    # 2. options mortes (une seule valeur restante)
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

    # 3. renommage de l'option restante et de ses valeurs
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
        updates = [{"id": vid, "name": name} for vid, name in wanted.items()]
        if len(updates) != len(keep):
            raise RuntimeError(f"{spec['ref']} : appariement valeurs incomplet ({len(updates)}/{len(keep)})")
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

    # 4. prix, compareAtPrice purgé
    price_input = [
        {"id": node["id"], "price": var["prix"], "compareAtPrice": None}
        for var, node in keep
    ]
    for var, node in keep:
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

    # 5. fiche : titre, handle, copy, SEO, rangement
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

    # 6. metafields PDP
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

    # 7. alt des visuels
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

    # 8. collection
    if coll_id and not dry:
        check(
            gql(
                """
                mutation($id: ID!, $productIds: [ID!]!) {
                  collectionAddProducts(id: $id, productIds: $productIds) {
                    userErrors { field message }
                  }
                }
                """,
                {"id": coll_id, "productIds": [live["id"]]},
            ),
            "collectionAddProducts",
        )

    # 9. statut, en dernier
    if spec["status"] == "ACTIVE" and not dry:
        check(
            gql(
                """
                mutation($product: ProductUpdateInput!) {
                  productUpdate(product: $product) {
                    product { id status }
                    userErrors { field message }
                  }
                }
                """,
                {"product": {"id": live["id"], "status": "ACTIVE"}},
            ),
            "productUpdate",
        )
    print(f"  statut : {spec['status']}" + (f" — {spec['bloque']}" if spec.get("bloque") else ""))
    return {"ref": spec["ref"], "id": live["id"], "handle": spec["handle"], "status": spec["status"]}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--only", help="refs séparées par des virgules (P1,P3)")
    args = parser.parse_args()

    todo = COPY["produits"]
    if args.only:
        wanted = {r.strip() for r in args.only.split(",")}
        todo = [p for p in todo if p["ref"] in wanted]

    print(f"{'[DRY RUN] ' if args.dry_run else ''}{len(todo)} fiches")
    coll_id = ensure_collection(args.dry_run)
    results = [apply_product(spec, coll_id, args.dry_run) for spec in todo]
    print("\n== vitrine")
    vitrine(coll_id, args.dry_run)

    print("\n== bilan")
    for r in results:
        print(f"  {r['ref']:<3} {r['status']:<7} /products/{r['handle']}")


if __name__ == "__main__":
    main()
