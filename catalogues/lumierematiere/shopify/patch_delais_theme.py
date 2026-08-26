#!/usr/bin/env python3
"""Aligne footer + panier sur 7–18 j et retire pampilles/papier de /collections."""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from apply_fullstack import theme_file, upsert_theme_file  # noqa: E402

BACKUP = HERE / "backups" / f"{date.today().isoformat()}-delais-theme"
UNPUB_FROM_LIST = {"lustres-pampilles", "suspensions-papier"}

REPLACES = (
    ("6 à 15 jours d’acheminement", "6 à 16 jours d’acheminement"),
    ("6 à 15 jours ouvrés", "6 à 16 jours ouvrés"),
    ("7 à 17 jours ouvrés", "7 à 18 jours ouvrés"),
    ("7 à 17 jours ", "7 à 18 jours "),
)


def replace_blob(blob: str) -> tuple[str, int]:
    n = 0
    for old, new in REPLACES:
        c = blob.count(old)
        if c:
            blob = blob.replace(old, new)
            n += c
    return blob, n


def patch_json(filename: str) -> int:
    data = theme_file(filename)
    BACKUP.mkdir(parents=True, exist_ok=True)
    stamp = filename.replace("/", "__")
    (BACKUP / f"{stamp}.avant.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    raw = json.dumps(data, ensure_ascii=False)
    patched, n = replace_blob(raw)
    if n:
        data = json.loads(patched)
    if filename == "templates/list-collections.json":
        listing = data["sections"]["main"]["settings"]["collection_list"]
        cleaned = [h for h in listing if h not in UNPUB_FROM_LIST]
        if cleaned != listing:
            print(f"  list-collections {listing} -> {cleaned}")
            data["sections"]["main"]["settings"]["collection_list"] = cleaned
            n += 1
    if n:
        upsert_theme_file(filename, data)
    print(f"  {filename}: {n} remplacement(s)")
    return n


def main() -> None:
    total = 0
    for name in (
        "sections/footer-group.json",
        "templates/cart.json",
        "sections/cart-drawer-group.json",
        "templates/list-collections.json",
    ):
        total += patch_json(name)
    print(f"OK thème délais · {total} changements")


if __name__ == "__main__":
    main()
