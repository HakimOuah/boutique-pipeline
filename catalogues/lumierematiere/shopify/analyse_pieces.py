#!/usr/bin/env python3
"""Lecture du dump de sauvegarde : extrait pour chaque fiche le code LM, la collection matière,
les diamètres réellement proposés par les variantes et l'URL de la photo principale.

Les libellés de variantes sont humanisés ("Ø 40 cm"), donc le diamètre se lit sur le Ø.
Sortie : catalogue-pieces-2026-08-26.json + tableau texte pour relecture humaine.
Aucune écriture Shopify.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BACKUP = ROOT / "backups" / "2026-08-26-collections"

DIAM_O = re.compile(r"Ø\s*(\d{1,3})(?:[.,]\d+)?\s*cm", re.I)
DIAM_CM = re.compile(r"(?<![\dxX×])(\d{1,3})(?:[.,]\d+)?\s*cm", re.I)
LM_RE = re.compile(r"^LM-\d+$")
# axes dimensionnels seulement : jamais Température, Puissance, Ampoule…
AXES_TAILLE = {"Diamètre", "Taille", "Modèle", "Size", "Abat-jour", "Forme", "Lumières"}


def diametres(product: dict) -> tuple[list[int], list[str]]:
    """Diamètres lus sur les axes dimensionnels. Le Ø fait foi ; sinon repli sur « nn cm »."""
    vals: set[int] = set()
    libelles: list[str] = []
    for opt in product["options"]:
        if opt["name"] not in AXES_TAILLE:
            continue
        for value in opt["values"]:
            found = DIAM_O.findall(value) or DIAM_CM.findall(value)
            if found:
                libelles.append(value)
            for n in found:
                n = int(n)
                if 8 <= n <= 200:
                    vals.add(n)
    return sorted(vals), libelles


def charger() -> list[dict]:
    products = json.loads((BACKUP / "products-avant.json").read_text(encoding="utf-8"))
    rows = []
    for p in products:
        tags = p["tags"]
        lm = next((t for t in tags if LM_RE.match(t)), "")
        diam, libelles = diametres(p)
        media = p.get("featuredMedia") or {}
        rows.append(
            {
                "lm": lm,
                "id": p["id"],
                "handle": p["handle"],
                "title": p["title"],
                "status": p["status"],
                "type": p["productType"],
                "tags": tags,
                "collections": [c["handle"] for c in p["collections"]["nodes"]],
                "options": {o["name"]: o["values"] for o in p["options"]},
                "diametres": diam,
                "libelles_taille": libelles,
                "nb_variantes": len(p["variants"]["nodes"]),
                "prix": sorted({v["price"] for v in p["variants"]["nodes"]}, key=float),
                "photo": ((media.get("image") or {}).get("url") or ""),
            }
        )
    rows.sort(key=lambda r: (r["lm"] or "zz"))
    return rows


def main() -> None:
    rows = charger()
    (ROOT / "catalogue-pieces-2026-08-26.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    filtre = sys.argv[1] if len(sys.argv) > 1 else ""
    print(f"{len(rows)} fiches · {sum(1 for r in rows if r['status']=='ACTIVE')} actives\n")
    print(f"{'LM':7} {'ST':2} {'matière':21} {'Ø réels':22} titre")
    print("-" * 155)
    for r in rows:
        coll = ",".join(c for c in r["collections"] if c not in ("selection-199", "frontpage"))
        if filtre and filtre not in coll:
            continue
        d = r["diametres"]
        dtxt = f"{min(d)}>{max(d)} ({len(d)})" if len(d) > 1 else (f"{d[0]}" if d else "—")
        print(f"{r['lm']:7} {r['status'][:2]:2} {coll[:21]:21} {dtxt:22} {r['title'][:78]}")


if __name__ == "__main__":
    main()
