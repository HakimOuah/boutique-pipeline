#!/usr/bin/env python3
"""Témoin tufting DataForSEO — n'affiche jamais les identifiants."""
from __future__ import annotations

import json
import os
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

API = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"
HERE = Path(__file__).resolve().parent
RAW = HERE / "raw"


def auth_header() -> str:
    login, pwd = os.environ.get("DATAFORSEO_LOGIN"), os.environ.get("DATAFORSEO_PASSWORD")
    if not login or not pwd:
        raise SystemExit("IDENTIFIANTS ABSENTS: DATAFORSEO_LOGIN/PASSWORD")
    import base64

    return "Basic " + base64.b64encode(f"{login}:{pwd}".encode()).decode()


def main() -> None:
    label = sys.argv[1] if len(sys.argv) > 1 else "avant"
    corps = [{
        "keywords": ["tufting"],
        "location_name": "France",
        "language_name": "French",
        "search_partners": False,
    }]
    req = urllib.request.Request(
        API,
        data=json.dumps(corps).encode(),
        headers={"Authorization": auth_header(), "Content-Type": "application/json"},
    )
    raw = urllib.request.urlopen(req, timeout=120).read()
    rep = json.loads(raw)
    task = (rep.get("tasks") or [None])[0]
    if not task:
        raise SystemExit("FAIL-CLOSED: tache absente")
    status = task.get("status_code")
    msg = task.get("status_message")
    res = task.get("result")
    print("heure:", datetime.now().isoformat(timespec="seconds"))
    print("label:", label)
    print("status_code:", status, msg)
    print("cost:", rep.get("cost"))
    if status == 40200 or "Payment Required" in str(msg):
        raise SystemExit("FAIL-CLOSED: quota/paiement DataForSEO")
    if not res:
        raise SystemExit("FAIL-CLOSED: temoin reponse vide")
    row = res[0]
    vol = row.get("search_volume")
    print("keyword:", row.get("keyword"))
    print("volume:", vol)
    print("cpc:", row.get("cpc"))
    print("location_code:", row.get("location_code"))
    print("language_code:", row.get("language_code"))
    serie = row.get("monthly_searches") or []
    print("serie:", [(m.get("year"), m.get("month"), m.get("search_volume")) for m in serie[:12]])
    if vol is None:
        raise SystemExit("FAIL-CLOSED: temoin volume null")
    RAW.mkdir(parents=True, exist_ok=True)
    out = RAW / f"temoin-{label}.json"
    out.write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding="utf-8")
    print("saved:", out)


if __name__ == "__main__":
    main()
