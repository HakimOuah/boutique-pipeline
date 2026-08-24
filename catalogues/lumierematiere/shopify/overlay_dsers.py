#!/usr/bin/env python3
"""Overlay DSers → Lumière Matière : titres FR, HTML VOC, prix, images Codex, collections.

Ne touche pas aux SKU DSers (sku_attr). Reprise via overlay-state.json.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from client import gql  # noqa: E402
from import_catalogue import (  # noqa: E402
    COLLECTIONS,
    EXTRA_COLLECTIONS,
    ONLINE,
    SELECTION_199,
    SKIP_IMAGES_SKU,
    add_to_collection,
    load_state,
    publish,
    staged_upload,
)

CATALOGUE = ROOT.parent / "catalogue-dsers.csv"
PRODUITS = ROOT.parent / "livraisons-visuels-codex" / "produits"
DUMP = ROOT / "shopify-products-dump.jsonl"
AE_FILES = sorted(ROOT.glob("ae-details-batch*.jsonl"))
STATE = ROOT / "overlay-state.json"
REPORT = ROOT / "overlay-prix-rapport.json"
FREIGHT_EUR = 2.0  # quotes FR 24/08 : 1,99 € / 0 €
JUNK_COST = 12.0  # pièces détachées / faux 2 €
GRID = [149, 199, 249, 299, 349, 399, 449, 499]
# leftovers DSers non mappés par hash — titres EN = traduction du supplier_title
MANUAL = {
    "LM-059": "gid://shopify/Product/10591495455056",
    "LM-110": "gid://shopify/Product/10591496175952",
}


def load_overlay_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {"products": {}, "drafted_duplicates": []}


def save_overlay_state(state: dict) -> None:
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")


def ht_margin(ttc: float, landed: float) -> float:
    return ttc / 1.2 - landed - (ttc * 0.014 + 0.25)


def snap_up(amount: float) -> int:
    for g in GRID:
        if g >= amount - 0.01:
            return g
    return GRID[-1]


def compare_at(price: int) -> int:
    n = int(price * 1.3)
    while n % 10 != 9:
        n += 1
    if n <= price:
        n += 10
    return n


def price_for(landed: float, competitor: int) -> int:
    """Concurrent d'abord ; on remonte la grille si la marge HT est insuffisante."""
    start = snap_up(max(competitor, GRID[0]))
    idx = GRID.index(start) if start in GRID else 0
    chosen = GRID[-1]
    for ttc in GRID[idx:]:
        ht = ttc / 1.2
        m = ht_margin(ttc, landed)
        if m >= 40 and (m >= 0.25 * ht or ttc >= 399):
            chosen = ttc
            break
        chosen = ttc
    return chosen


def patch_description(html: str, price: int) -> str:
    html = re.sub(r"Environ \d+\s*€", f"Environ {price} €", html)
    html = re.sub(r"(Prix :</strong> )\d+\s*€", rf"\g<1>{price} €", html)
    html = re.sub(r"(Prix :</strong>)\s*\d+\s*€", rf"\g<1> {price} €", html)
    return html


def hashes_of(blob: str) -> set[str]:
    return set(re.findall(r"(S[A-Za-z0-9]{10,})", blob or ""))


def build_mapping() -> tuple[list[dict], list[str]]:
    rows = list(csv.DictReader(CATALOGUE.open(encoding="utf-8")))
    dump = [json.loads(l) for l in DUMP.read_text().splitlines() if l.strip()]
    ae: dict[str, dict] = {}
    for path in AE_FILES:
        for line in path.read_text().splitlines():
            rec = json.loads(line)
            ae[str(rec["product_id"])] = rec
    shop = []
    for p in dump:
        skus = {v["sku"] for v in p["variants"]["nodes"] if v.get("sku")}
        blob = (p.get("descriptionHtml") or "") + " " + ((p.get("featuredImage") or {}).get("url") or "")
        shop.append({"id": p["id"], "skus": skus, "hashes": hashes_of(blob), "raw": p})
    used: set[str] = set()
    mapping = []
    for row in rows:
        pid = row["supplier_id"]
        gid = MANUAL.get(row["sku"])
        a = ae.get(pid) or {}
        if not gid:
            ae_skus = {s["sku_attr"] for s in (a.get("skus") or []) if s.get("sku_attr")}
            ae_hashes = set(a.get("image_hashes") or [])
            best = None
            for s in shop:
                if s["id"] in used:
                    continue
                score = len(ae_skus & s["skus"]) * 10 + len(ae_hashes & s["hashes"])
                if score and (best is None or score > best[0]):
                    best = (score, s)
            if best:
                gid = best[1]["id"]
        if not gid:
            continue
        used.add(gid)
        s = next(x for x in shop if x["id"] == gid)
        mapping.append(
            {
                "sku": row["sku"],
                "handle": row["handle"],
                "title": row["title"],
                "seo_title": row["seo_title"],
                "seo_description": row["seo_description"],
                "collection": row["collection"],
                "price_csv": int(float(row["price_ttc"])),
                "description_file": row["description_file"],
                "supplier_id": pid,
                "shopify_id": gid,
                "shopify_handle": s["raw"]["handle"],
            }
        )
    leftovers = [s["id"] for s in shop if s["id"] not in used]
    return mapping, leftovers


def product_live(gid: str) -> dict:
    data = gql(
        """
        query P($id: ID!) {
          product(id: $id) {
            id
            handle
            media(first: 50) {
              nodes { id alt mediaContentType }
            }
            variants(first: 100) {
              nodes {
                id
                sku
                title
                price
                compareAtPrice
                inventoryItem { unitCost { amount currencyCode } }
              }
            }
          }
        }
        """,
        {"id": gid},
    )
    return data["product"]


def overlay_meta(row: dict, min_price: int) -> None:
    desc_path = ROOT.parent / row["description_file"]
    html = desc_path.read_text(encoding="utf-8") if desc_path.exists() else ""
    html = patch_description(html, min_price)
    seo_desc = row["seo_description"]
    seo_desc = re.sub(r"Environ \d+\s*€", f"Environ {min_price} €", seo_desc)
    tags = [row["collection"], row["sku"]]
    variables = {
        "input": {
            "id": row["shopify_id"],
            "title": row["title"],
            "handle": row["handle"],
            "descriptionHtml": html,
            "vendor": "Lumière Matière",
            "productType": row["collection"],
            "tags": tags,
            "status": "ACTIVE",
            "seo": {"title": row["seo_title"][:70], "description": seo_desc[:320]},
        }
    }
    data = gql(
        """
        mutation U($input: ProductInput!) {
          productUpdate(input: $input) {
            product { id handle }
            userErrors { field message }
          }
        }
        """,
        variables,
    )
    errs = data["productUpdate"]["userErrors"]
    if errs:
        # handle already taken → keep DSers handle
        msg = json.dumps(errs, ensure_ascii=False)
        if "handle" in msg.lower():
            variables["input"].pop("handle", None)
            data = gql(
                """
                mutation U($input: ProductInput!) {
                  productUpdate(input: $input) {
                    product { id handle }
                    userErrors { field message }
                  }
                }
                """,
                variables,
            )
            errs = data["productUpdate"]["userErrors"]
        if errs:
            raise RuntimeError((row["sku"], errs))


def overlay_prices(live: dict, competitor: int) -> dict:
    variants = live["variants"]["nodes"]
    real_costs = []
    for v in variants:
        cost = float((v["inventoryItem"].get("unitCost") or {}).get("amount") or v["price"] or 0)
        if cost >= JUNK_COST:
            real_costs.append(cost)
    fallback = min(real_costs) if real_costs else competitor / 2.5
    updates = []
    priced = []
    for v in variants:
        cost = float((v["inventoryItem"].get("unitCost") or {}).get("amount") or v["price"] or 0)
        if cost < JUNK_COST:
            cost = fallback
        landed = cost + FREIGHT_EUR
        ttc = price_for(landed, competitor)
        cap = compare_at(ttc)
        updates.append({"id": v["id"], "price": f"{ttc}.00", "compareAtPrice": f"{cap}.00"})
        priced.append(
            {
                "variant_id": v["id"],
                "sku_attr": v.get("sku"),
                "title": v.get("title"),
                "cost": round(cost, 2),
                "landed": round(landed, 2),
                "price": ttc,
                "compareAt": cap,
                "margin_ht": round(ht_margin(ttc, landed), 2),
            }
        )
    # batches of 50
    for i in range(0, len(updates), 50):
        chunk = updates[i : i + 50]
        data = gql(
            """
            mutation V($productId: ID!, $variants: [ProductVariantsBulkInput!]!) {
              productVariantsBulkUpdate(productId: $productId, variants: $variants) {
                userErrors { field message }
              }
            }
            """,
            {"productId": live["id"], "variants": chunk},
        )
        errs = data["productVariantsBulkUpdate"]["userErrors"]
        if errs:
            raise RuntimeError(errs)
        time.sleep(0.2)
    prices = sorted({p["price"] for p in priced})
    return {"min_price": min(prices), "prices": prices, "variants": priced}


def overlay_images(row: dict, live: dict) -> None:
    if row["sku"] in SKIP_IMAGES_SKU:
        return
    vue = [n for n in live["media"]["nodes"] if "vue" in (n.get("alt") or "")]
    others = [n for n in live["media"]["nodes"] if n.get("id") not in {x["id"] for x in vue}]
    if len(vue) >= 5:
        if others:
            gql(
                """
                mutation D($productId: ID!, $mediaIds: [ID!]!) {
                  productDeleteMedia(productId: $productId, mediaIds: $mediaIds) {
                    mediaUserErrors { field message }
                  }
                }
                """,
                {"productId": row["shopify_id"], "mediaIds": [n["id"] for n in others if n.get("id")]},
            )
        return
    pdir = PRODUITS / row["handle"]
    files = []
    for n in range(1, 6):
        img = pdir / f"{row['handle']}-g{n}.jpg"
        if not img.exists():
            raise FileNotFoundError(img)
        resource_url = staged_upload(img, resource="IMAGE")
        files.append(
            {
                "originalSource": resource_url,
                "alt": f"{row['title']} — vue {n}",
                "mediaContentType": "IMAGE",
            }
        )
        time.sleep(0.12)
    data = gql(
        """
        mutation M($productId: ID!, $media: [CreateMediaInput!]!) {
          productCreateMedia(productId: $productId, media: $media) {
            media { ... on MediaImage { id status } }
            mediaUserErrors { field message }
          }
        }
        """,
        {"productId": row["shopify_id"], "media": files},
    )
    payload = data["productCreateMedia"]
    if payload["mediaUserErrors"]:
        raise RuntimeError((row["sku"], payload["mediaUserErrors"]))
    new_ids = [m["id"] for m in payload["media"] if m and m.get("id")]
    deadline = time.time() + 90
    while time.time() < deadline and new_ids:
        info = gql(
            """
            query M($id: ID!) {
              product(id: $id) {
                media(first: 30) {
                  nodes { ... on MediaImage { id status } }
                }
              }
            }
            """,
            {"id": row["shopify_id"]},
        )
        statuses = {
            n["id"]: n.get("status")
            for n in info["product"]["media"]["nodes"]
            if n.get("id") in new_ids
        }
        if statuses and all(s in {"READY", "FAILED"} for s in statuses.values()):
            failed = [i for i, s in statuses.items() if s == "FAILED"]
            if failed:
                raise RuntimeError((row["sku"], "media FAILED", failed))
            break
        time.sleep(1.5)
    old_ids = [n["id"] for n in live["media"]["nodes"] if n.get("id")]
    if old_ids:
        data = gql(
            """
            mutation D($productId: ID!, $mediaIds: [ID!]!) {
              productDeleteMedia(productId: $productId, mediaIds: $mediaIds) {
                mediaUserErrors { field message }
              }
            }
            """,
            {"productId": row["shopify_id"], "mediaIds": old_ids},
        )
        errs = data["productDeleteMedia"]["mediaUserErrors"]
        if errs:
            print("  warn delete media", row["sku"], errs)
    if new_ids:
        moves = [{"id": mid, "newPosition": str(i)} for i, mid in enumerate(new_ids)]
        try:
            gql(
                """
                mutation R($id: ID!, $moves: [MoveInput!]!) {
                  productReorderMedia(id: $id, moves: $moves) {
                    userErrors { field message }
                  }
                }
                """,
                {"id": row["shopify_id"], "moves": moves},
            )
        except Exception as err:
            print("  warn reorder", row["sku"], err)


def overlay_collections(row: dict, coll: dict[str, str], min_price: int) -> None:
    ids = [coll[row["collection"]]]
    extra = EXTRA_COLLECTIONS.get(row["sku"])
    if extra:
        ids.append(coll[extra])
    if min_price in (149, 199) or row["sku"] in SELECTION_199:
        ids.append(coll["selection-199"])
    for cid in ids:
        add_to_collection(cid, row["shopify_id"])
        time.sleep(0.15)


def draft_product(gid: str) -> None:
    gql(
        """
        mutation U($input: ProductInput!) {
          productUpdate(input: $input) {
            userErrors { field message }
          }
        }
        """,
        {"input": {"id": gid, "status": "DRAFT"}},
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-images", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    mapping, leftovers = build_mapping()
    print(f"mapping {len(mapping)} leftovers {len(leftovers)}")
    shop_state = load_state()
    coll = shop_state.get("collections") or {}
    if not coll and not args.dry_run:
        raise SystemExit("state.json sans collections — relancer import collections")

    overlay_state = load_overlay_state()
    done = overlay_state.setdefault("products", {})
    report = []

    rows = mapping[: args.limit] if args.limit else mapping
    for i, row in enumerate(rows, 1):
        sku = row["sku"]
        rec = done.get(sku, {})
        live = product_live(row["shopify_id"]) if not args.dry_run else None
        if args.dry_run:
            # approximate from dump via a second live-less path
            dump = [json.loads(l) for l in DUMP.read_text().splitlines() if l.strip()]
            p = next(x for x in dump if x["id"] == row["shopify_id"])
            variants = p["variants"]["nodes"]
            priced = []
            real = []
            for v in variants:
                cost = float((v["inventoryItem"].get("unitCost") or {}).get("amount") or v["price"])
                if cost >= JUNK_COST:
                    real.append(cost)
            fallback = min(real) if real else row["price_csv"] / 2.5
            for v in variants:
                cost = float((v["inventoryItem"].get("unitCost") or {}).get("amount") or v["price"])
                if cost < JUNK_COST:
                    cost = fallback
                landed = cost + FREIGHT_EUR
                ttc = price_for(landed, row["price_csv"])
                priced.append(ttc)
            min_price = min(priced)
            report.append(
                {
                    "sku": sku,
                    "title": row["title"],
                    "collection": row["collection"],
                    "csv": row["price_csv"],
                    "n_var": len(priced),
                    "price_min": min_price,
                    "price_max": max(priced),
                    "price_set": sorted(set(priced)),
                }
            )
            continue

        try:
            if not rec.get("prices"):
                priced = overlay_prices(live, row["price_csv"])
                rec["prices"] = {"min": priced["min_price"], "set": priced["prices"]}
                rec["variant_count"] = len(priced["variants"])
                rec["thin"] = [
                    v
                    for v in priced["variants"]
                    if v["margin_ht"] < 40 or v["margin_ht"] < 0.25 * (v["price"] / 1.2)
                ]
                done[sku] = rec
                save_overlay_state(overlay_state)
            min_price = rec["prices"]["min"]
            if not rec.get("meta"):
                overlay_meta(row, min_price)
                rec["meta"] = True
                done[sku] = rec
                save_overlay_state(overlay_state)
            if not rec.get("images") and not args.skip_images:
                live = product_live(row["shopify_id"])
                overlay_images(row, live)
                rec["images"] = True if sku not in SKIP_IMAGES_SKU else "skipped"
                done[sku] = rec
                save_overlay_state(overlay_state)
            if not rec.get("collections"):
                overlay_collections(row, coll, min_price)
                rec["collections"] = True
                done[sku] = rec
                save_overlay_state(overlay_state)
            if not rec.get("published"):
                publish(row["shopify_id"])
                rec["published"] = True
                done[sku] = rec
                save_overlay_state(overlay_state)
            print(
                f"  {sku} {row['handle']} {min_price}€ set={rec['prices']['set']} "
                f"thin={len(rec.get('thin') or [])}"
            )
        except Exception as err:
            print(f"FAIL {sku} {err}")
            save_overlay_state(overlay_state)
            raise
        if i % 10 == 0:
            print(f"  … {i}/{len(rows)}")

    if args.dry_run:
        print(Counter((r["price_min"], r["csv"]) for r in report).most_common(20))
        print("price_min dist", Counter(r["price_min"] for r in report))
        REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
        print("wrote", REPORT)
        return

    if leftovers and not overlay_state.get("drafted_duplicates"):
        for gid in leftovers:
            try:
                draft_product(gid)
                print("draft duplicate", gid)
            except Exception as err:
                print("warn draft", gid, err)
        overlay_state["drafted_duplicates"] = leftovers
        save_overlay_state(overlay_state)

    shop_state.setdefault("products", {})
    for row in mapping:
        rec = done.get(row["sku"]) or {}
        shop_state["products"][row["handle"]] = {
            "id": row["shopify_id"],
            "sku": row["sku"],
            "overlay": True,
        }
    from import_catalogue import save_state as save_shop_state

    save_shop_state(shop_state)
    print("OK overlay", len(done), "drafted", len(overlay_state.get("drafted_duplicates") or []))


if __name__ == "__main__":
    main()
