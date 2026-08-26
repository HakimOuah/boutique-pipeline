"""Passe de cohérence 26/08/2026 — délais, marges, Lustria.

Lit Shopify (source des prix et coûts DSers facturés) et Lustria (catalogue
du 25/08). N'écrit rien sur la boutique.

    python3 audit_coherence.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from client import gql  # noqa: E402
from lustria_match import (  # noqa: E402
    FRET,
    apparie,
    charge_lustria,
    forme,
    ht,
    marge_ht,
    matiere,
    multiplicite,
    plancher_marge,
    prix_plancher,
    quantiles,
    tokens,
)

OUT = HERE / f"COHERENCE-{date.today().isoformat()}.json"
PROMESSE_MIN = 7
PROMESSE_MAX = 17
PREP_MAX = 2


PRODUCTS_Q = """
query($c: String) {
  products(first: 50, after: $c, query: "status:active") {
    pageInfo { hasNextPage endCursor }
    nodes {
      id handle title status productType tags
      variants(first: 50) {
        nodes {
          id sku title price compareAtPrice
          inventoryItem { unitCost { amount currencyCode } }
        }
      }
      metafields(first: 20, namespace: "custom") {
        nodes { key value }
      }
    }
  }
}
"""


def fetch_live() -> list[dict]:
    out, cursor = [], None
    while True:
        data = gql(PRODUCTS_Q, {"c": cursor})["products"]
        out.extend(data["nodes"])
        if not data["pageInfo"]["hasNextPage"]:
            break
        cursor = data["pageInfo"]["endCursor"]
    return out


def faq_delai(product: dict) -> str | None:
    for m in product.get("metafields", {}).get("nodes") or []:
        if m["key"] != "faq":
            continue
        try:
            items = json.loads(m["value"])
        except json.JSONDecodeError:
            return m["value"]
        for item in items:
            q = (item.get("q") or "").lower()
            if "délai" in q or "delai" in q or "livraison" in q:
                return item.get("a")
    return None


def parse_promesse(text: str | None) -> tuple[int | None, int | None]:
    if not text:
        return None, None
    pairs = re.findall(r"(\d+)\s*(?:à|-)\s*(\d+)\s*jours", text)
    if not pairs:
        return None, None
    # last pair is the total (7 à 17)
    lo, hi = (int(x) for x in pairs[-1])
    return lo, hi


def lm_code(product: dict) -> str | None:
    for tag in product.get("tags") or []:
        if re.fullmatch(r"LM-\d+", tag):
            return tag
    return None


def type_fiche(titre: str) -> str:
    first = titre.lower().split()[0] if titre else ""
    if first.startswith("plafonnier"):
        return "plafonnier"
    if first.startswith("applique"):
        return "applique"
    return "suspendu"


def main() -> None:
    dsers_csv = {
        r["handle"]: r
        for r in csv.DictReader((HERE.parent / "catalogue-dsers.csv").open(encoding="utf-8"))
    }
    mapping = {
        m["handle"]: m
        for m in json.loads((HERE / "overlay-mapping.json").read_text())["mapping"]
    }
    # appliques added after the overlay
    extra = {
        "applique-murale-pierre-588683": {
            "sku": "LM-122", "supplier_id": "1005010526588683",
        },
        "applique-liseuse-pierre-311650": {
            "sku": "LM-123", "supplier_id": "1005010525311650",
        },
        "applique-double-travertin-474088": {
            "sku": "LM-124", "supplier_id": "1005009931474088",
        },
        "applique-murale-pierre-metal-147598": {
            "sku": "LM-126", "supplier_id": "1005006852147598",
        },
        "applique-murale-verre-829449": {
            "sku": "LM-127", "supplier_id": "1005008903829449",
        },
    }

    live = fetch_live()
    lustria = charge_lustria()
    # add applique pool from the full Lustria dump
    src = json.loads((HERE / "lustria-catalogue-2026-08-25.json").read_text())["produits"]
    appliques_l = []
    for p in src:
        if (p.get("type") or "").lower().startswith("applique") and p.get("prix"):
            tk = tokens(p["h"], p["t"], *p.get("tags") or [])
            appliques_l.append({
                "h": p["h"], "prix": float(p["prix"]), "nvar": p["nvar"],
                "type": "applique", "matiere": matiere(tk), "forme": forme(tk),
                "multi": multiplicite(tk),
            })

    rows = []
    for p in live:
        handle = p["handle"]
        variants = p["variants"]["nodes"]
        costs = []
        for v in variants:
            unit = (v.get("inventoryItem") or {}).get("unitCost") or {}
            if unit.get("amount"):
                costs.append(float(unit["amount"]))
        prix = sorted(float(v["price"]) for v in variants)
        cout = min(costs) if costs else None
        csv_row = dsers_csv.get(handle) or {}
        map_row = mapping.get(handle) or extra.get(handle) or {}
        sku = lm_code(p) or map_row.get("sku") or csv_row.get("sku")
        ae_id = map_row.get("supplier_id") or csv_row.get("supplier_id")
        faq = faq_delai(p)
        promesse = parse_promesse(faq)
        typ = type_fiche(p["title"])
        tk = tokens(p["title"])
        nous = {
            "type": typ,
            "matiere": matiere(tk) or matiere(tokens(csv_row.get("supplier_title") or "")),
            "forme": forme(tk),
            "multi": multiplicite(tk),
        }
        pool = appliques_l if typ == "applique" else lustria
        match = apparie(nous, pool) if pool else {"qualite": "aucun", "pool": [], "critere": ""}
        lustria_pool = match.get("pool") or []
        median = None
        temoin = None
        if lustria_pool:
            _, median, _ = quantiles([x["prix"] for x in lustria_pool])
            temoin = min(lustria_pool, key=lambda x: (abs(x["prix"] - median), x["h"]))

        entree = prix[0] if prix else None
        marge = marge_ht(entree, cout) if entree and cout is not None else None
        plancher = plancher_marge(entree) if entree else None
        ok_marge = (
            marge is not None and plancher is not None and marge + 1e-9 >= plancher
        )
        vs_lustria = None
        if entree and median:
            vs_lustria = round(entree - median, 2)

        rows.append({
            "sku": sku,
            "handle": handle,
            "title": p["title"],
            "type": typ,
            "status": p["status"],
            "ae_id": ae_id,
            "n_var": len(variants),
            "prix_min": entree,
            "prix_max": prix[-1] if prix else None,
            "cout_dsers_min": cout,
            "cout_dsers_max": max(costs) if costs else None,
            "rendu": round(cout + FRET, 2) if cout is not None else None,
            "marge_ht": round(marge, 2) if marge is not None else None,
            "marge_pct": round(100 * marge / ht(entree), 1) if marge is not None else None,
            "plancher_ht": round(plancher, 2) if plancher is not None else None,
            "ok_marge": ok_marge,
            "prix_plancher": prix_plancher(cout) if cout is not None else None,
            "faq_delai": faq,
            "promesse_min": promesse[0],
            "promesse_max": promesse[1],
            "promesse_ok_texte": promesse == (PROMESSE_MIN, PROMESSE_MAX),
            "lustria_n": len(lustria_pool),
            "lustria_qualite": match.get("qualite"),
            "lustria_critere": match.get("critere"),
            "lustria_median": median,
            "lustria_handle": temoin["h"] if temoin else None,
            "vs_lustria": vs_lustria,
            "au_dessus_lustria": bool(vs_lustria is not None and vs_lustria > 0),
            "sku_entree": variants[0]["sku"] if variants else None,
            "sku_id_map": map_row.get("cheapest_sku_id"),
        })

    rows.sort(key=lambda r: (r["sku"] is None, r["sku"] or "", r["handle"]))
    payload = {
        "date": date.today().isoformat(),
        "n": len(rows),
        "promesse_boutique": f"{PROMESSE_MIN}–{PROMESSE_MAX} j ouvrés (prép. 1–2 + acheminement 6–15)",
        "regle_marge": "HT >= max(40 € ; 25 % du HT) après coût DSers + 2 €",
        "produits": rows,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")

    n = len(rows)
    sans_cout = sum(1 for r in rows if r["cout_dsers_min"] is None)
    sous_marge = [r for r in rows if r["ok_marge"] is False]
    sans_faq = [r for r in rows if not r["faq_delai"]]
    faq_autre = [r for r in rows if r["faq_delai"] and not r["promesse_ok_texte"]]
    dessus = [r for r in rows if r["au_dessus_lustria"]]
    print(f"{n} fiches ACTIVE")
    print(f"  sans coût DSers : {sans_cout}")
    print(f"  sous le plancher de marge : {len(sous_marge)}")
    print(f"  FAQ délai absente : {len(sans_faq)}")
    print(f"  FAQ délai ≠ 7–17 : {len(faq_autre)}")
    print(f"  prix d'entrée > médiane Lustria : {len(dessus)}")
    print(f"écrit {OUT.name}")


if __name__ == "__main__":
    main()
