#!/usr/bin/env python3
"""Fusionne les JSON sourcing lots 1-4 + reste → sourcing-complet-30x30.json + MAJ verdicts."""
import json
import os
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "analyses" / "2026-08-22-recherche-30x30"

SOURCES = [
    "sourcing-lot1-local.json",
    "sourcing-lot2-local.json",
    "sourcing-lot3-local.json",
    "sourcing-lot4-local.json",
    "sourcing-reste-local.json",
    "sourcing-manual-local.json",
]

def load_all():
    merged = {}
    for name in SOURCES:
        p = BASE / name
        if not p.exists():
            continue
        try:
            data = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        for row in data:
            cid = row.get("id")
            if not cid:
                continue
            prev = merged.get(cid)
            # prefer entry with best status / price
            rank = {"FOURNISSEUR À TESTER": 3, "OFFRE TROUVÉE": 2, "AUCUNE OFFRE EXPLOITABLE": 1}
            if prev is None or rank.get(row.get("status"), 0) > rank.get(prev.get("status"), 0):
                merged[cid] = row
            elif row.get("status") == prev.get("status") and row.get("best") and not prev.get("best"):
                merged[cid] = row
    return merged


def price_label(row):
    if not row or not row.get("best"):
        return None
    p = row["best"].get("price_n") or row["best"].get("list", {}).get("price")
    if p is None:
        return None
    if isinstance(p, (int, float)):
        return f"~{p:.0f} €"
    return f"~{p}"


def sourcing_cell(row):
    if not row:
        return "—"
    st = row.get("status", "—")
    pl = price_label(row)
    if st == "FOURNISSEUR À TESTER" and pl:
        return f"**FOURNISSEUR À TESTER** {pl}"
    if st == "OFFRE TROUVÉE" and pl:
        return f"**OFFRE TROUVÉE** {pl}"
    if st == "AUCUNE OFFRE EXPLOITABLE":
        return "**AUCUNE OFFRE**"
    return st


def main():
    merged = load_all()
    out = BASE / "sourcing-complet-30x30.json"
    json.dump(list(merged.values()), open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    # stats
    stats = {}
    for v in merged.values():
        stats[v.get("status", "?")] = stats.get(v.get("status", 0), 0) + 1
    print("Merged", len(merged), "candidats", stats)
    print("Wrote", out)
    return merged


if __name__ == "__main__":
    main()
