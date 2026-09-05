#!/usr/bin/env python3
"""Dump brut keyword_suggestions pour diagnostiquer une graine."""
from __future__ import annotations

import json
import os
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

API = "https://api.dataforseo.com/v3/dataforseo_labs/google/keyword_suggestions/live"


def auth_header() -> str:
    import base64

    login, pwd = os.environ.get("DATAFORSEO_LOGIN"), os.environ.get("DATAFORSEO_PASSWORD")
    if not login or not pwd:
        raise SystemExit("IDENTIFIANTS ABSENTS")
    return "Basic " + base64.b64encode(f"{login}:{pwd}".encode()).decode()


def main() -> None:
    graine = sys.argv[1]
    out = Path(sys.argv[2])
    corps = [{
        "keyword": graine,
        "location_name": "France",
        "language_name": "French",
        "include_serp_info": False,
        "limit": 1000,
        "offset": 0,
        "order_by": ["keyword_info.search_volume,desc"],
    }]
    req = urllib.request.Request(
        API,
        data=json.dumps(corps).encode(),
        headers={"Authorization": auth_header(), "Content-Type": "application/json"},
    )
    raw = urllib.request.urlopen(req, timeout=300).read()
    rep = json.loads(raw)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding="utf-8")
    task = (rep.get("tasks") or [{}])[0]
    res = task.get("result")
    print("heure:", datetime.now().isoformat(timespec="seconds"))
    print("graine:", graine)
    print("status:", task.get("status_code"), task.get("status_message"))
    print("cost:", rep.get("cost"))
    print("result_type:", type(res).__name__, "len:", 0 if res is None else len(res))
    if res:
        r0 = res[0]
        print("keys:", sorted(r0.keys()))
        print("total_count:", r0.get("total_count"))
        items = r0.get("items")
        print("items_type:", type(items).__name__, "len:", None if items is None else len(items))
        print("seed_keyword:", r0.get("seed_keyword") or r0.get("keyword"))
    print("saved:", out)


if __name__ == "__main__":
    main()
