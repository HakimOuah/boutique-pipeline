#!/usr/bin/env python3
"""Download AliExpress gallery images for Orysbain / Lumière Matière catalogues.

Layout:
  catalogues/<brand>/sources-fournisseur/<supplier_id>/01.jpg …
  catalogues/<brand>/sources-par-handle/<handle> → symlink to supplier_id
  catalogues/<brand>/sources-fournisseur/MANIFESTE.json
"""
from __future__ import annotations

import csv
import json
import re
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
MAX_PER_PRODUCT = 12
WORKERS = 6


def fetch_html(product_id: str) -> str:
    url = f"https://fr.aliexpress.com/item/{product_id}.html"
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "fr-FR,fr;q=0.9"})
    with urllib.request.urlopen(req, timeout=40) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def extract_gallery(html: str) -> list[str]:
    m = re.search(r'"imagePathList"\s*:\s*(\[[^\]]+\])', html)
    if not m:
        # escaped form
        m = re.search(r'imagePathList\\?":\s*(\[[^\]]+\])', html)
    urls: list[str] = []
    if m:
        raw = m.group(1)
        raw = raw.replace('\\/', '/').replace('\\u002F', '/')
        try:
            urls = json.loads(raw)
        except json.JSONDecodeError:
            urls = re.findall(r'https://[^"\\]+\.(?:jpg|jpeg|png|webp)', raw)
    # dedupe preserve order, normalize
    out: list[str] = []
    seen: set[str] = set()
    for u in urls:
        u = u.strip().split("?")[0]
        # prefer full-size: strip common size suffixes in path if present
        u = re.sub(r"_\d+x\d+\.", ".", u)
        if u not in seen and "alicdn" in u or "aliexpress-media" in u:
            seen.add(u)
            out.append(u)
    return out[:MAX_PER_PRODUCT]


def download_one(url: str, dest: Path) -> tuple[bool, str]:
    if dest.exists() and dest.stat().st_size > 2000:
        return True, "exists"
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Referer": "https://fr.aliexpress.com/"})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = resp.read()
        if len(data) < 1500:
            return False, f"too_small:{len(data)}"
        dest.write_bytes(data)
        return True, f"ok:{len(data)}"
    except Exception as exc:  # noqa: BLE001
        return False, str(exc)[:120]


def process_product(brand_dir: Path, row: dict) -> dict:
    sid = row["supplier_id"].strip()
    handle = row["handle"].strip()
    gal_dir = brand_dir / "sources-fournisseur" / sid
    gal_dir.mkdir(parents=True, exist_ok=True)
    entry: dict = {
        "sku": row.get("sku"),
        "handle": handle,
        "supplier_id": sid,
        "supplier_url": row.get("supplier_url"),
        "images": [],
        "status": "pending",
        "error": None,
    }
    try:
        html = fetch_html(sid)
        urls = extract_gallery(html)
        if not urls:
            entry["status"] = "no_gallery"
            entry["error"] = "imagePathList empty"
            return entry
        for i, url in enumerate(urls, start=1):
            ext = ".jpg"
            if url.lower().endswith(".png"):
                ext = ".png"
            elif url.lower().endswith(".webp"):
                ext = ".webp"
            dest = gal_dir / f"{i:02d}{ext}"
            ok, msg = download_one(url, dest)
            entry["images"].append(
                {"n": i, "file": dest.name, "url": url, "ok": ok, "msg": msg, "bytes": dest.stat().st_size if dest.exists() else 0}
            )
            time.sleep(0.15)
        # symlink by handle
        link_root = brand_dir / "sources-par-handle"
        link_root.mkdir(parents=True, exist_ok=True)
        link = link_root / handle
        if link.is_symlink() or link.exists():
            link.unlink()
        link.symlink_to(Path("..") / "sources-fournisseur" / sid)
        ok_n = sum(1 for im in entry["images"] if im["ok"])
        entry["status"] = "ok" if ok_n else "download_failed"
        entry["count_ok"] = ok_n
    except Exception as exc:  # noqa: BLE001
        entry["status"] = "error"
        entry["error"] = str(exc)[:200]
    return entry


def run_brand(brand: str) -> None:
    brand_dir = ROOT / brand
    csv_path = brand_dir / "catalogue-dsers.csv"
    rows = list(csv.DictReader(csv_path.open(encoding="utf-8")))
    print(f"=== {brand}: {len(rows)} products ===", flush=True)
    results: list[dict] = []
    # sequential HTML fetch is more polite / less blocked; parallelize downloads inside product
    for i, row in enumerate(rows, 1):
        print(f"[{i}/{len(rows)}] {row['supplier_id']} {row['handle'][:40]}...", flush=True)
        entry = process_product(brand_dir, row)
        results.append(entry)
        print(f"  → {entry['status']} ({entry.get('count_ok', 0)} imgs)", flush=True)
        time.sleep(0.4)
    man = {
        "brand": brand,
        "downloaded_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "max_per_product": MAX_PER_PRODUCT,
        "products": results,
        "summary": {
            "total": len(results),
            "ok": sum(1 for r in results if r["status"] == "ok"),
            "no_gallery": sum(1 for r in results if r["status"] == "no_gallery"),
            "error": sum(1 for r in results if r["status"] not in ("ok", "no_gallery")),
            "images_ok": sum(r.get("count_ok", 0) for r in results),
        },
    }
    out = brand_dir / "sources-fournisseur" / "MANIFESTE.json"
    out.write_text(json.dumps(man, ensure_ascii=False, indent=2), encoding="utf-8")
    print("MANIFESTE", out, man["summary"], flush=True)


def main() -> None:
    import sys

    brands = sys.argv[1:] or ["orysbain", "lumierematiere"]
    for b in brands:
        run_brand(b)


if __name__ == "__main__":
    main()
