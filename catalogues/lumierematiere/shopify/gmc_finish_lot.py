#!/usr/bin/env python3
"""Fin de lot GMC LM — téléphone boutique + restage filenames AE.

Ne publie pas de thème, ne publie pas de brouillon, ne touche pas aux SKU,
ne fait jamais fileDelete.
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from attach_applique_codex import delete_media, reorder, set_variant_media  # noqa: E402
from attach_variant_packshots import wait_media  # noqa: E402
import importlib

import bootstrap_pages  # noqa: E402
from bootstrap_pages import existing_pages, upsert_page, upsert_policy  # noqa: E402
from client import gql  # noqa: E402
from md_html import md_to_html  # noqa: E402

PAGES = ROOT.parent / "pages"
TMP = Path("/tmp/lm-gmc-ae")
HANDLE = "applique-murale-pierre-metal-147598"
MAIN = "gid://shopify/OnlineStoreTheme/186708001104"
COPY = "gid://shopify/OnlineStoreTheme/186897498448"

OLD_DISPLAY = "+33 7 56 82 80 94"
OLD_TEL = "+33756828094"
NEW_DISPLAY = "+33 7 56 91 60 84"
NEW_TEL = "+33756916084"


def staged_upload_named(path: Path, filename: str) -> str:
    size = path.stat().st_size
    mime = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }.get(path.suffix.lower(), "image/jpeg")
    data = gql(
        """
        mutation($input: [StagedUploadInput!]!) {
          stagedUploadsCreate(input: $input) {
            stagedTargets { url resourceUrl parameters { name value } }
            userErrors { field message }
          }
        }
        """,
        {
            "input": [
                {
                    "resource": "IMAGE",
                    "filename": filename,
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
            raise RuntimeError(f"upload {filename} HTTP {resp.status}")
    return target["resourceUrl"]


def theme_raw(theme_id: str, filename: str) -> str:
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
    return (nodes[0]["body"]["content"] or "") if nodes else ""


def upsert_theme(theme_id: str, filename: str, body: str) -> None:
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


def align_phone_sources() -> int:
    n = 0
    for path in PAGES.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        new = text.replace(OLD_DISPLAY, NEW_DISPLAY).replace(OLD_TEL, NEW_TEL)
        if new != text:
            path.write_text(new, encoding="utf-8")
            n += 1
            print(f"  source {path.name}")
    boot = ROOT / "bootstrap_pages.py"
    text = boot.read_text(encoding="utf-8")
    new = text.replace(OLD_DISPLAY, NEW_DISPLAY).replace(OLD_TEL, NEW_TEL)
    if new != text:
        boot.write_text(new, encoding="utf-8")
        n += 1
        print("  source bootstrap_pages.py")
    for script in (ROOT / "patch_footer.py", ROOT / "humanise_theme.py"):
        text = script.read_text(encoding="utf-8")
        new = text.replace(OLD_DISPLAY, NEW_DISPLAY).replace(OLD_TEL, NEW_TEL)
        if new != text:
            script.write_text(new, encoding="utf-8")
            n += 1
            print(f"  source {script.name}")
    return n


def push_phone_pages() -> None:
    pages = existing_pages()
    mapping = {
        "faq": "faq.md",
        "contact": "contact.md",
        "conditions-paiement": "conditions-paiement.md",
        "notre-histoire": "notre-histoire.md",
    }
    titles = {
        "faq": "FAQ",
        "contact": "Contact",
        "conditions-paiement": "Paiement",
        "notre-histoire": "Notre histoire",
    }
    for handle, name in mapping.items():
        body = md_to_html((PAGES / name).read_text(encoding="utf-8"))
        upsert_page(handle, titles[handle], body, pages)
        print(f"  page {handle}")
    for ptype, name in (
        ("TERMS_OF_SERVICE", "cgv.md"),
        ("PRIVACY_POLICY", "politique-confidentialite.md"),
        ("REFUND_POLICY", "politique-retours.md"),
        ("SHIPPING_POLICY", "politique-livraison.md"),
    ):
        upsert_policy(ptype, md_to_html((PAGES / name).read_text(encoding="utf-8")))
    importlib.reload(bootstrap_pages)
    upsert_policy("LEGAL_NOTICE", bootstrap_pages.LEGAL_NOTICE_HTML.strip())


def align_phone_themes() -> None:
    for label, tid in (("MAIN", MAIN), ("COPY", COPY)):
        raw = theme_raw(tid, "sections/footer-group.json")
        if not raw:
            print(f"  footer {label} introuvable")
            continue
        new = raw.replace(OLD_DISPLAY, NEW_DISPLAY).replace(OLD_TEL, NEW_TEL)
        if new == raw:
            print(f"  footer {label} déjà aligné ou autre graphie")
            if OLD_DISPLAY not in raw and NEW_DISPLAY not in raw:
                print(f"    (aucun des deux numéros dans footer {label})")
            continue
        upsert_theme(tid, "sections/footer-group.json", new)
        print(f"  footer {label} → {NEW_DISPLAY}")


def fetch_product() -> dict:
    data = gql(
        """
        query($h: String!) {
          productByHandle(handle: $h) {
            id handle status
            media(first: 50) {
              nodes {
                id alt
                ... on MediaImage { image { url } }
              }
            }
            variants(first: 20) {
              nodes {
                id title
                media(first: 5) { nodes { id ... on MediaImage { image { url } } } }
              }
            }
          }
        }
        """,
        {"h": HANDLE},
    )["productByHandle"]
    if not data:
        raise RuntimeError(HANDLE)
    return data


def fname(url: str) -> str:
    return url.split("?")[0].rsplit("/", 1)[-1]


def try_rename(nodes: list[dict]) -> bool:
    files = []
    for i, node in enumerate(nodes, start=1):
        url = (node.get("image") or {}).get("url") or ""
        if not re.match(r"S[A-Za-z0-9]+\.webp$", fname(url)):
            continue
        files.append({"id": node["id"], "filename": f"{HANDLE}-g{i}.webp"})
    if not files:
        print("  rien à renommer")
        return True
    data = gql(
        """
        mutation($files: [FileUpdateInput!]!) {
          fileUpdate(files: $files) {
            files { id ... on MediaImage { image { url } } }
            userErrors { field message }
          }
        }
        """,
        {"files": files},
    )
    payload = data["fileUpdate"]
    if payload["userErrors"]:
        print("  fileUpdate filename:", payload["userErrors"])
        return False
    still = 0
    for f in payload["files"]:
        url = ((f or {}).get("image") or {}).get("url") or ""
        if re.match(r"S[A-Za-z0-9]+\.webp$", fname(url)):
            still += 1
            print("  CDN inchangé", fname(url))
    return still == 0


def restage(product: dict) -> None:
    TMP.mkdir(parents=True, exist_ok=True)
    nodes = product["media"]["nodes"]
    old_ids = [n["id"] for n in nodes]
    variant_old = {}
    for v in product["variants"]["nodes"]:
        urls = [fname((m.get("image") or {}).get("url") or "") for m in v["media"]["nodes"]]
        variant_old[v["id"]] = (v["title"], urls[0] if urls else "")

    new_ids = []
    old_file_to_new = {}
    for i, node in enumerate(nodes, start=1):
        url = (node.get("image") or {}).get("url") or ""
        old_name = fname(url)
        dest = TMP / f"{HANDLE}-g{i}.webp"
        print(f"  dl {old_name} → {dest.name}")
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        dest.write_bytes(urllib.request.urlopen(req, timeout=60).read())
        src = staged_upload_named(dest, dest.name)
        payload = gql(
            """
            mutation($productId: ID!, $media: [CreateMediaInput!]!) {
              productCreateMedia(productId: $productId, media: $media) {
                media { ... on MediaImage { id } }
                mediaUserErrors { field message }
              }
            }
            """,
            {
                "productId": product["id"],
                "media": [
                    {
                        "originalSource": src,
                        "alt": node.get("alt") or f"vue {i}",
                        "mediaContentType": "IMAGE",
                    }
                ],
            },
        )["productCreateMedia"]
        if payload["mediaUserErrors"]:
            raise RuntimeError(payload["mediaUserErrors"])
        mid = payload["media"][0]["id"]
        wait_media(product["id"], [mid])
        new_ids.append(mid)
        old_file_to_new[old_name] = mid
        print(f"  upload {dest.name}")
        time.sleep(0.15)

    pairs = []
    for vid, (title, old) in variant_old.items():
        mid = old_file_to_new.get(old)
        if mid:
            pairs.append((vid, mid))
            print(f"  variante {title} → nouveau média")
        else:
            print(f"  variante {title} sans mapping, skip")
    if pairs:
        try:
            set_variant_media(product["id"], pairs)
            print(f"  {len(pairs)} variantes rattachées")
        except Exception as err:
            print("  variant rebind skip (write_products ?) :", err)

    delete_media(product["id"], old_ids)
    print(f"  {len(old_ids)} anciens médias détachés (pas fileDelete)")
    reorder(product["id"], new_ids)
    print("  ordre g1–g9")


def verify_ae() -> None:
    product = fetch_product()
    ae = 0
    for i, node in enumerate(product["media"]["nodes"], start=1):
        name = fname((node.get("image") or {}).get("url") or "")
        print(f"  {i:02d} {name} | {node.get('alt')}")
        if re.match(r"S[A-Za-z0-9]+\.webp$", name):
            ae += 1
    print(f"  restants S…webp : {ae}")


def main() -> None:
    print("== téléphone")
    align_phone_sources()
    push_phone_pages()
    align_phone_themes()

    print("== AE filenames")
    product = fetch_product()
    print(f"  {product['handle']} {product['status']} {len(product['media']['nodes'])} médias")
    if try_rename(product["media"]["nodes"]):
        print("  rename in-place OK")
    else:
        print("  rename in-place insuffisant → restage")
        restage(product)
    verify_ae()


if __name__ == "__main__":
    main()
