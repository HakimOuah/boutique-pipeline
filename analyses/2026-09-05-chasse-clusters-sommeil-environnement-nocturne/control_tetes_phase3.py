#!/usr/bin/env python3
"""Contrôle de têtes search_volume/live France/French — phase 3 surmatelas."""
from __future__ import annotations

import json
import os
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

API = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"
RAW = Path(__file__).resolve().parent / "raw-phase3"

MOTS = [
    "surmatelas",
    "sur-matelas",
    "sur matelas",
    "surmatelas à mémoire de forme",
    "surmatelas memoire de forme",
    "surmatelas mémoire de forme",
    "memoire de forme surmatelas",
    "sur-matelas à mémoire de forme",
    "surmatelas 140x190",
    "surmatelas 160x200",
    "surmatelas 180x200",
    "surmatelas 90x190",
    "surmatelas 140x200",
    "surmatelas 120x190",
    "surmatelas 90x200",
    "surmatelas 80x200",
    "surconfort de matelas 160x200",
    "surconfort",
    "topper",
    "topper matelas",
    "matelas",
    "matelas mémoire de forme",
    "surmatelas lit parapluie",
    "ikea surmatelas",
    "ikéa surmatelas",
    "surmatelas decathlon",
    "surmatelas rafraîchissant",
    "surmatelas rafraichissant",
    "surmatelas chauffante",
    "surmatelas chauffant",
    "emma surmatelas",
    "sofitel surmatelas",
    "surmatelas tempur",
    "bultex surmatelas",
    "but surmatelas",
    "conforama surmatelas",
    "dodo surmatelas",
    "surmatelas canapé",
    "housse sur-matelas",
    "surmatelas ferme",
    "surmatelas à quoi ça sert",
    "meilleurs surmatelas",
    "mello surmatelas",
    "surmatelas viscoelastique",
    "surmatelas viscoélastique",
    "surmatelas mousse à mémoire de forme",
    "surmatelas latex",
    "surmatelas 140x190 à mémoire de forme",
    "surmatelas à mémoire de forme 160x200",
    "simmonssur-matelas",
    "sur-matelas simmons",
]


def auth_header() -> str:
    import base64

    login, pwd = os.environ.get("DATAFORSEO_LOGIN"), os.environ.get("DATAFORSEO_PASSWORD")
    if not login or not pwd:
        raise SystemExit("IDENTIFIANTS ABSENTS")
    return "Basic " + base64.b64encode(f"{login}:{pwd}".encode()).decode()


def main() -> None:
    label = sys.argv[1] if len(sys.argv) > 1 else "tetes-phase3"
    corps = [{
        "keywords": MOTS,
        "location_name": "France",
        "language_name": "French",
        "search_partners": False,
    }]
    req = urllib.request.Request(
        API,
        data=json.dumps(corps).encode(),
        headers={"Authorization": auth_header(), "Content-Type": "application/json"},
    )
    raw = urllib.request.urlopen(req, timeout=180).read()
    rep = json.loads(raw)
    task = (rep.get("tasks") or [{}])[0]
    status = task.get("status_code")
    msg = task.get("status_message")
    print("heure:", datetime.now().isoformat(timespec="seconds"))
    print("status:", status, msg)
    print("cost:", rep.get("cost"))
    if status == 40200 or "Payment Required" in str(msg):
        raise SystemExit("FAIL-CLOSED: quota/paiement")
    if status != 20000:
        raise SystemExit(f"FAIL-CLOSED: status {status} {msg}")
    res = task.get("result")
    if not res:
        raise SystemExit("FAIL-CLOSED: result vide")
    RAW.mkdir(parents=True, exist_ok=True)
    out = RAW / f"{label}.json"
    out.write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding="utf-8")
    print("saved:", out)
    series_path = RAW / f"{label}-series.txt"
    lines = []
    print(f"{'keyword':<46}{'vol':>8}{'cpc':>8}  loc lang")
    for r in res:
        serie = [m.get("search_volume") for m in (r.get("monthly_searches") or [])]
        kw = r.get("keyword") or ""
        print(
            f"{kw:<46}{str(r.get('search_volume')):>8}"
            f"{str(r.get('cpc')):>8}  {r.get('location_code')} {r.get('language_code')}"
        )
        lines.append(f"{kw!r}\t{r.get('search_volume')}\t{r.get('cpc')}\t{serie}")
    series_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("series:", series_path)
    returned = {r.get("keyword") for r in res}
    missing = [m for m in MOTS if m not in returned]
    if missing:
        print("NON RENDUS (n/a, pas 0):", missing)


if __name__ == "__main__":
    main()
