#!/usr/bin/env python3
"""Contrôle de têtes search_volume/live France/French."""
from __future__ import annotations

import json
import os
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

API = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"
RAW = Path(__file__).resolve().parent / "raw"

MOTS = [
    # témoin déjà tiré à part
    "matelas",
    "sur-matelas",
    "sur matelas",
    "surmatelas",
    "protège-matelas",
    "protege matelas",
    "matelas gonflable",
    "matelas gonflables",
    "matelas 140x190",
    "matelas 160x200",
    "90x190 matelas",
    "140x200 matelas",
    "180x200 matelas",
    "90x200 matelas",
    "emma matelas",
    "matelas ikea",
    "matelas à langer",
    "alèse matelas",
    "matelas mémoire de forme",
    "futon",
    "matelas rafraichissant",
    "surconfort de matelas 160x200",
    "housse de matelas",
    "sommier",
    "matelas latex",
    "matelas de sol",
    "matelas pliable",
    "matelas bébé",
    "sommeil",
    "masque de sommeil",
    "masque sommeil",
    "masques sommeil",
    "boules quies sommeil",
    "bouchons oreilles sommeil",
    "casque anti-bruit sommeil",
    "oreiller",
    "oreiller mémoire de forme",
    "oreiller apnée du sommeil",
    "couverture lestée",
    "bruit blanc",
    "machine à bruit blanc",
    "machine bruit blanc",
    "apnée du sommeil",
    "gummies sommeil",
    "bruit chambre",
    "mousse anti-bruit chambre",
    "isolation bruit chambre",
    "bouchons d'oreille",
    "boules quies",
    "casque anti-bruit",
    "obscurité chambre",
    "obscurité",
    "rideau occultant",
    "rideaux occultants",
    "store occultant",
    "occultant",
    "rideau occultant chambre",
    "volet occultant",
]


def auth_header() -> str:
    import base64

    login, pwd = os.environ.get("DATAFORSEO_LOGIN"), os.environ.get("DATAFORSEO_PASSWORD")
    if not login or not pwd:
        raise SystemExit("IDENTIFIANTS ABSENTS")
    return "Basic " + base64.b64encode(f"{login}:{pwd}".encode()).decode()


def main() -> None:
    label = sys.argv[1] if len(sys.argv) > 1 else "tetes-1"
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
    print(f"{'keyword':<42}{'vol':>8}{'cpc':>8}  loc lang")
    for r in res:
        print(
            f"{(r.get('keyword') or ''):<42}{str(r.get('search_volume')):>8}"
            f"{str(r.get('cpc')):>8}  {r.get('location_code')} {r.get('language_code')}"
        )
    returned = {r.get("keyword") for r in res}
    missing = [m for m in MOTS if m not in returned]
    if missing:
        print("NON RENDUS (n/a, pas 0):", missing)


if __name__ == "__main__":
    main()
