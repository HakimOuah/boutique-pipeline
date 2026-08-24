#!/usr/bin/env python3
"""Exporte les 121 URLs AliExpress du catalogue pour import DSers."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "catalogue-dsers.csv"
OUT_TXT = ROOT / "shopify" / "dsers-urls.txt"
OUT_JSONL = ROOT / "shopify" / "dsers-mapping.jsonl"


def main() -> None:
    urls: list[str] = []
    rows: list[dict] = []
    with CSV_PATH.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            url = (row.get("supplier_url") or "").strip()
            if not url:
                continue
            urls.append(url)
            rows.append(
                {
                    "sku": row["sku"],
                    "handle": row["handle"],
                    "title": row["title"],
                    "price_ttc": row["price_ttc"],
                    "supplier_url": url,
                    "supplier_id": row.get("supplier_id", ""),
                }
            )
    OUT_TXT.write_text("\n".join(urls) + "\n", encoding="utf-8")
    OUT_JSONL.write_text(
        "\n".join(__import__("json").dumps(r, ensure_ascii=False) for r in rows) + "\n",
        encoding="utf-8",
    )
    print(f"{len(urls)} URLs -> {OUT_TXT}")
    print(f"{len(rows)} lignes mapping -> {OUT_JSONL}")
    dupes = len(urls) - len(set(urls))
    if dupes:
        print(f"ATTENTION {dupes} URL(s) en double")


if __name__ == "__main__":
    main()
