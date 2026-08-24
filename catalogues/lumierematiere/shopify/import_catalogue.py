#!/usr/bin/env python3
"""Import catalogue LM : collections + 121 SKU + images Codex (hors LM-086). Reprise possible."""
from __future__ import annotations

import csv
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from client import gql  # noqa: E402

CATALOGUE = ROOT.parent / "catalogue-dsers.csv"
DESC_DIR = ROOT.parent / "descriptions"
VISUELS = ROOT.parent / "livraisons-visuels-codex"
BRAND = VISUELS / "brand"
PRODUITS = VISUELS / "produits"
STATE = ROOT / "state.json"
ONLINE = "gid://shopify/Publication/287538413904"
SKIP_IMAGES_SKU = {"LM-086"}
SELECTION_199 = {
    "LM-003",
    "LM-017",
    "LM-037",
    "LM-043",
    "LM-076",
    "LM-053",
}

# titre UI, handle, fichier cover (échange salon ↔ plafonniers déjà tranché)
COLLECTIONS = {
    "Suspensions bambou": ("Suspensions bambou", "suspensions-bambou", "lumierematiere-collection-suspensions-bambou.jpg"),
    "Suspensions rotin": ("Suspensions rotin", "suspensions-rotin", "lumierematiere-collection-suspensions-rotin.jpg"),
    "Suspensions bois": ("Suspensions bois", "suspensions-bois", "lumierematiere-collection-suspensions-bois.jpg"),
    "Suspensions pierre": ("Suspensions pierre", "suspensions-pierre", "lumierematiere-collection-suspensions-pierre.jpg"),
    "Suspensions verre": ("Suspensions verre", "suspensions-verre", "lumierematiere-collection-suspensions-verre.jpg"),
    "Lustres cristal": ("Lustres effet cristal", "lustres-effet-cristal", "lumierematiere-collection-lustres-cristal.jpg"),
    "Lustres anneau": ("Lustres anneau", "lustres-anneau", "lumierematiere-collection-lustres-anneau.jpg"),
    "Lustres salon": ("Lustres salon", "lustres-salon", "lumierematiere-collection-plafonniers.jpg"),
    "Plafonniers": ("Plafonniers", "plafonniers", "lumierematiere-collection-lustres-salon.jpg"),
    "Suspensions métal": ("Suspensions métal", "suspensions-metal", "lumierematiere-collection-suspensions-metal.jpg"),
    "Suspensions déco": ("Suspensions déco", "suspensions-deco", "lumierematiere-collection-suspensions-deco.jpg"),
    "Lustres statement": ("Lustres statement", "lustres-statement", "lumierematiere-collection-lustres-statement.jpg"),
    "Suspensions modernes": ("Suspensions modernes", "suspensions-modernes", "lumierematiere-collection-suspensions-modernes.jpg"),
}

EXTRA_COLLECTIONS = {
    "LM-108": "Lustres salon",
    "LM-121": "Suspensions métal",
}


def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {}


def save_state(state: dict) -> None:
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")


def staged_upload(path: Path, resource: str = "IMAGE") -> str:
    size = path.stat().st_size
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    data = gql(
        """
        mutation Staged($input: [StagedUploadInput!]!) {
          stagedUploadsCreate(input: $input) {
            stagedTargets { url resourceUrl parameters { name value } }
            userErrors { field message }
          }
        }
        """,
        {
            "input": [
                {
                    "resource": resource,
                    "filename": path.name,
                    "mimeType": mime,
                    "httpMethod": "PUT",
                    "fileSize": str(size),
                }
            ]
        },
    )
    payload = data["stagedUploadsCreate"]
    if payload["userErrors"]:
        raise RuntimeError(payload["userErrors"])
    target = payload["stagedTargets"][0]
    headers = {p["name"]: p["value"] for p in target["parameters"]}
    headers.setdefault("Content-Type", mime)
    req = urllib.request.Request(target["url"], data=path.read_bytes(), method="PUT", headers=headers)
    with urllib.request.urlopen(req, timeout=180) as resp:
        if resp.status >= 300:
            raise RuntimeError(f"upload {path.name} HTTP {resp.status}")
    return target["resourceUrl"]


def publish(gid: str) -> None:
    data = gql(
        """
        mutation Pub($id: ID!, $input: [PublicationInput!]!) {
          publishablePublish(id: $id, input: $input) {
            userErrors { field message }
          }
        }
        """,
        {"id": gid, "input": [{"publicationId": ONLINE}]},
    )
    errs = data["publishablePublish"]["userErrors"]
    if errs:
        msg = json.dumps(errs, ensure_ascii=False)
        if "already" not in msg.lower() and "déjà" not in msg.lower():
            raise RuntimeError(errs)


def ensure_collections(state: dict) -> dict[str, str]:
    coll = state.setdefault("collections", {})
    existing = gql("query { collections(first: 50) { nodes { id handle title } } }")
    by_handle = {n["handle"]: n["id"] for n in existing["collections"]["nodes"]}
    wanted = list(COLLECTIONS.items()) + [
        ("selection-199", ("Autour de 199 €", "selection-199", None))
    ]
    # normalize the extra tuple
    for csv_name, meta in list(COLLECTIONS.items()):
        title, handle, cover = meta
        if handle in by_handle:
            coll[csv_name] = by_handle[handle]
            continue
        image_input = None
        if cover:
            src = staged_upload(BRAND / cover, resource="COLLECTION_IMAGE")
            image_input = {"src": src, "altText": title}
        variables = {"input": {"title": title, "handle": handle, "sortOrder": "BEST_SELLING"}}
        if image_input:
            variables["input"]["image"] = image_input
        data = gql(
            """
            mutation Coll($input: CollectionInput!) {
              collectionCreate(input: $input) {
                collection { id handle }
                userErrors { field message }
              }
            }
            """,
            variables,
        )
        errs = data["collectionCreate"]["userErrors"]
        if errs:
            raise RuntimeError((csv_name, errs))
        cid = data["collectionCreate"]["collection"]["id"]
        coll[csv_name] = cid
        publish(cid)
        print(f"  collection {handle} {cid}")
        save_state(state)
        time.sleep(0.3)

    if "selection-199" not in by_handle and "selection-199" not in coll:
        data = gql(
            """
            mutation Coll($input: CollectionInput!) {
              collectionCreate(input: $input) {
                collection { id handle }
                userErrors { field message }
              }
            }
            """,
            {"input": {"title": "Autour de 199 €", "handle": "selection-199", "sortOrder": "MANUAL"}},
        )
        errs = data["collectionCreate"]["userErrors"]
        if errs:
            raise RuntimeError(errs)
        cid = data["collectionCreate"]["collection"]["id"]
        coll["selection-199"] = cid
        publish(cid)
        print(f"  collection selection-199 {cid}")
    elif "selection-199" in by_handle:
        coll["selection-199"] = by_handle["selection-199"]
    save_state(state)
    return coll


def add_to_collection(collection_id: str, product_id: str) -> None:
    data = gql(
        """
        mutation Add($id: ID!, $productIds: [ID!]!) {
          collectionAddProducts(id: $id, productIds: $productIds) {
            userErrors { field message }
          }
        }
        """,
        {"id": collection_id, "productIds": [product_id]},
    )
    errs = data["collectionAddProducts"]["userErrors"]
    if errs:
        print("  warn add collection", errs)


def import_product(row: dict, coll: dict[str, str], state: dict) -> None:
    handle = row["handle"]
    sku = row["sku"]
    done = state.setdefault("products", {})
    if handle in done:
        return
    title = row["title"]
    price = f"{int(row['price_ttc'])}.00"
    desc_path = ROOT.parent / row["description_file"]
    description = desc_path.read_text(encoding="utf-8") if desc_path.exists() else ""
    csv_coll = row["collection"]
    collection_ids = [coll[csv_coll]]
    if sku in SELECTION_199:
        collection_ids.append(coll["selection-199"])
    extra = EXTRA_COLLECTIONS.get(sku)
    if extra:
        collection_ids.append(coll[extra])

    files = []
    if sku not in SKIP_IMAGES_SKU:
        pdir = PRODUITS / handle
        for n in range(1, 6):
            img = pdir / f"{handle}-g{n}.jpg"
            if not img.exists():
                raise FileNotFoundError(img)
            resource_url = staged_upload(img, resource="IMAGE")
            files.append(
                {
                    "originalSource": resource_url,
                    "contentType": "IMAGE",
                    "filename": img.name,
                    "alt": f"{title} — vue {n}",
                    "duplicateResolutionMode": "REPLACE",
                }
            )
            time.sleep(0.15)

    product_input = {
        "title": title,
        "handle": handle,
        "descriptionHtml": description,
        "vendor": "Lumière Matière",
        "productType": csv_coll,
        "status": "DRAFT" if sku in SKIP_IMAGES_SKU else "ACTIVE",
        "tags": [csv_coll, sku],
        "seo": {"title": row["seo_title"], "description": row["seo_description"][:320]},
        "collections": collection_ids,
        "productOptions": [{"name": "Title", "values": [{"name": "Default Title"}]}],
        "variants": [
            {
                "optionValues": [{"optionName": "Title", "name": "Default Title"}],
                "price": price,
                "sku": sku,
                "inventoryPolicy": "CONTINUE",
                "taxable": True,
            }
        ],
    }
    if files:
        product_input["files"] = files

    data = gql(
        """
        mutation Set($input: ProductSetInput!, $synchronous: Boolean!) {
          productSet(synchronous: $synchronous, input: $input) {
            product { id handle }
            userErrors { field message code }
          }
        }
        """,
        {"input": product_input, "synchronous": True},
    )
    payload = data["productSet"]
    if payload["userErrors"]:
        raise RuntimeError((sku, payload["userErrors"]))
    pid = payload["product"]["id"]
    if sku not in SKIP_IMAGES_SKU:
        publish(pid)
    done[handle] = {"id": pid, "sku": sku}
    save_state(state)
    print(f"  {sku} {handle} {pid}")


def main() -> None:
    state = load_state()
    print("=== collections ===")
    coll = ensure_collections(state)
    rows = list(csv.DictReader(CATALOGUE.open(encoding="utf-8")))
    print(f"=== products {len(rows)} ===")
    for i, row in enumerate(rows, 1):
        try:
            import_product(row, coll, state)
        except Exception as err:
            print(f"FAIL {row['sku']} {err}")
            save_state(state)
            raise
        if i % 10 == 0:
            print(f"  … {i}/{len(rows)}")
    print("OK", len(state.get("products", {})), "products")


if __name__ == "__main__":
    main()
