#!/usr/bin/env python3
"""Rattache les packshots Codex de teinte aux variantes Lumière Matière.

SKU / sku_attr DSers inchangés. Les g1–g5 existants restent dans la galerie.
Idempotent : skip si le média du slug est déjà sur le produit.
"""
from __future__ import annotations

import re
import sys
import time
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from apply_pdp import fetch_products  # noqa: E402
from client import gql  # noqa: E402
from import_catalogue import staged_upload  # noqa: E402

DELIVERY = ROOT.parent / "livraisons-visuels-codex" / "variantes-couleur"
THROTTLE = 0.18
COLOR_WORDS = [
    ("blanc cassé", "Blanc cassé"),
    ("noir mat", "Noir mat"),
    ("noir et doré", "Noir et doré"),
    ("gris fumé", "Gris fumé"),
    ("bois brut", "Bois brut"),
    ("bois foncé", "Bois foncé"),
    ("papier dupont", "Papier DuPont"),
    ("soie unie", "Soie unie"),
    ("transparent", "Transparent"),
    ("argenté", "Argenté"),
    ("cognac", "Cognac"),
    ("ambre", "Ambre"),
    ("noyer", "Noyer"),
    ("chanvre", "Chanvre"),
    ("cuivre", "Cuivre"),
    ("chrome", "Chrome"),
    ("beige", "Beige"),
    ("kaki", "Kaki"),
    ("café", "Café"),
    ("doré", "Doré"),
    ("noir", "Noir"),
    ("blanc", "Blanc"),
    ("vert", "Vert"),
    ("brun", "Brun"),
    ("gris", "Gris"),
    ("bois", "Bois"),
]


def slugify(text: str) -> str:
    folded = unicodedata.normalize("NFD", (text or "").lower())
    folded = "".join(c for c in folded if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", folded).strip("-")


def value_slug(val: str) -> str:
    cleaned = re.sub(r"\s+\d+$", "", (val or "").strip())
    return slugify(cleaned)


def colors_in(text: str) -> list[str]:
    low = (text or "").lower()
    found: list[str] = []
    for needle, label in sorted(COLOR_WORDS, key=lambda x: -len(x[0])):
        if needle in low:
            found.append(label)
            low = low.replace(needle, " ")
    return found


def variant_slugs(selected: list[dict]) -> set[str]:
    out: set[str] = set()
    for so in selected:
        val = so.get("value") or ""
        out.add(value_slug(val))
        for label in colors_in(val):
            out.add(slugify(label))
    out.discard("")
    return out


def parse_file(path: Path) -> tuple[str, str] | None:
    name = path.name
    if not name.endswith("-g1.jpg"):
        return None
    handle = path.parent.name
    prefix = f"{handle}-"
    if not name.startswith(prefix):
        return None
    slug = name[len(prefix) : -len("-g1.jpg")]
    return handle, slug


def pick_slug(vslugs: set[str], available: list[str]) -> str | None:
    ranked = sorted(available, key=len, reverse=True)
    for slug in ranked:
        if slug in vslugs:
            return slug
    return None


def list_delivery() -> dict[str, dict[str, Path]]:
    by_handle: dict[str, dict[str, Path]] = {}
    for path in sorted(DELIVERY.glob("*/*.jpg")):
        parsed = parse_file(path)
        if not parsed:
            print("  warn nom", path.name)
            continue
        handle, slug = parsed
        by_handle.setdefault(handle, {})[slug] = path
    return by_handle


def wait_media(product_id: str, media_ids: list[str], timeout: int = 90) -> None:
    deadline = time.time() + timeout
    pending = set(media_ids)
    while time.time() < deadline and pending:
        info = gql(
            """
            query M($id: ID!) {
              product(id: $id) {
                media(first: 50) {
                  nodes { ... on MediaImage { id status } }
                }
              }
            }
            """,
            {"id": product_id},
        )
        nodes = (info.get("product") or {}).get("media", {}).get("nodes") or []
        statuses = {n["id"]: n.get("status") for n in nodes if n.get("id") in pending}
        failed = [i for i, s in statuses.items() if s == "FAILED"]
        if failed:
            raise RuntimeError(f"media FAILED {failed}")
        pending = {i for i in pending if statuses.get(i) not in {"READY"}}
        if pending:
            time.sleep(1.2)


def existing_slug_media(product: dict) -> dict[str, str]:
    found: dict[str, str] = {}
    handle = product["handle"]
    nodes = (product.get("media") or {}).get("nodes") or []
    for n in nodes:
        alt = (n.get("alt") or "").lower()
        url = ""
        img = n.get("image") or {}
        if isinstance(img, dict):
            url = (img.get("url") or "").lower()
        blob = f"{alt} {url}"
        prefix = f"{handle}-"
        for token in re.findall(r"[a-z0-9-]+-g1", blob):
            if token.startswith(prefix):
                slug = token[len(prefix) : -len("-g1")]
                if slug:
                    found[slug] = n["id"]
    return found


def create_media(product_id: str, title: str, items: list[tuple[str, Path]]) -> dict[str, str]:
    media = []
    for slug, path in items:
        src = staged_upload(path, resource="IMAGE")
        media.append(
            {
                "originalSource": src,
                "alt": f"{title} — {slug.replace('-', ' ')}",
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
        {"productId": product_id, "media": media},
    )
    payload = data["productCreateMedia"]
    if payload["mediaUserErrors"]:
        raise RuntimeError(payload["mediaUserErrors"])
    ids = [m["id"] for m in payload["media"] if m and m.get("id")]
    if len(ids) != len(items):
        raise RuntimeError(f"media count {len(ids)} != {len(items)}")
    wait_media(product_id, ids)
    return {slug: mid for (slug, _path), mid in zip(items, ids)}


def set_variant_media(product_id: str, pairs: list[tuple[str, str]]) -> None:
    for i in range(0, len(pairs), 25):
        chunk = pairs[i : i + 25]
        data = gql(
            """
            mutation V($productId: ID!, $variants: [ProductVariantsBulkInput!]!) {
              productVariantsBulkUpdate(productId: $productId, variants: $variants) {
                userErrors { field message }
              }
            }
            """,
            {
                "productId": product_id,
                "variants": [{"id": vid, "mediaId": mid} for vid, mid in chunk],
            },
        )
        errs = data["productVariantsBulkUpdate"]["userErrors"]
        if errs:
            raise RuntimeError(errs)
        time.sleep(THROTTLE)


def plan(products: list[dict], delivery: dict[str, dict[str, Path]]) -> list[dict]:
    by_handle = {p["handle"]: p for p in products}
    rows = []
    missing_handles = sorted(set(delivery) - set(by_handle))
    for handle in missing_handles:
        rows.append({"handle": handle, "error": "produit introuvable"})
    for handle, files in sorted(delivery.items()):
        product = by_handle.get(handle)
        if not product:
            continue
        variants = product["variants"]["nodes"]
        available = list(files)
        assigned: dict[str, str] = {}
        unmatched = []
        for v in variants:
            slug = pick_slug(variant_slugs(v.get("selectedOptions") or []), available)
            if slug:
                assigned[v["id"]] = slug
            else:
                unmatched.append(v.get("title") or v["id"])
        unused = [s for s in available if s not in set(assigned.values())]
        rows.append(
            {
                "handle": handle,
                "id": product["id"],
                "title": product["title"],
                "files": files,
                "assigned": assigned,
                "unmatched": unmatched,
                "unused": unused,
                "existing": existing_slug_media(product),
            }
        )
    return rows


def main() -> None:
    apply = "--apply" in sys.argv
    delivery = list_delivery()
    n_files = sum(len(v) for v in delivery.values())
    print(f"livraison {len(delivery)} handles / {n_files} JPEG")
    print("— fetch produits")
    products = fetch_products()
    rows = plan(products, delivery)
    errors = [r for r in rows if r.get("error")]
    bad = [r for r in rows if r.get("unmatched") or r.get("unused")]
    ok = [r for r in rows if not r.get("error") and not r.get("unmatched") and not r.get("unused")]
    print(f"mapping OK {len(ok)} / problèmes {len(bad)} / handles manquants {len(errors)}")
    for r in errors:
        print(f"  MISSING {r['handle']}")
    for r in bad:
        print(
            f"  WARN {r['handle']}: unmatched={r.get('unmatched')} unused={r.get('unused')} "
            f"assigned={len(r.get('assigned') or {})}/{len((r.get('files') or {}))}"
        )
    if not apply:
        for r in ok[:5]:
            slugs = sorted(set((r["assigned"] or {}).values()))
            print(f"  {r['handle']}: {slugs} → {len(r['assigned'])} variantes")
        print("dry-run (relancer avec --apply)")
        return
    done = 0
    for r in rows:
        if r.get("error"):
            print("  SKIP", r["handle"], r["error"])
            continue
        handle = r["handle"]
        files: dict[str, Path] = r["files"]
        existing: dict[str, str] = dict(r["existing"] or {})
        need = [(slug, path) for slug, path in files.items() if slug not in existing]
        try:
            if need:
                created = create_media(r["id"], r["title"], need)
                existing.update(created)
                print(f"  upload {handle}: {len(created)}")
            pairs = []
            for vid, slug in r["assigned"].items():
                mid = existing.get(slug)
                if mid:
                    pairs.append((vid, mid))
            if not pairs:
                print(f"  SKIP {handle}: aucun média")
                continue
            set_variant_media(r["id"], pairs)
            done += 1
            print(f"  OK {handle}: {len(pairs)} variantes")
        except Exception as exc:  # noqa: BLE001
            print(f"  FAIL {handle}: {exc}")
        time.sleep(THROTTLE)
    print(f"rattachement OK {done}/{len(rows) - len(errors)}")


if __name__ == "__main__":
    main()
