#!/usr/bin/env python3
import base64, json, os, pathlib, urllib.request

API = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"
ROOT = pathlib.Path(__file__).resolve().parent

def auth():
    login = os.environ.get("DATAFORSEO_LOGIN")
    password = os.environ.get("DATAFORSEO_PASSWORD")
    if not login or not password:
        raise SystemExit("Identifiants DataForSEO absents")
    return "Basic " + base64.b64encode(f"{login}:{password}".encode()).decode()

def call(keywords):
    payload = [{
        "keywords": keywords,
        "location_name": "France",
        "language_name": "French",
        "search_partners": False
    }]
    req = urllib.request.Request(API, data=json.dumps(payload).encode(), headers={
        "Authorization": auth(), "Content-Type": "application/json"
    })
    with urllib.request.urlopen(req, timeout=180) as response:
        body = json.load(response)
    task = body.get("tasks", [{}])[0]
    if task.get("status_code") != 20000 or not task.get("result"):
        raise SystemExit(f"Échec DataForSEO: {task.get('status_code')} {task.get('status_message')}")
    return body

keywords = json.loads((ROOT / "search-volume-keywords.json").read_text())
pre = call(["tufting"])
pre_value = pre["tasks"][0]["result"][0].get("search_volume")
if pre_value != 12100:
    raise SystemExit(f"Témoin avant non conforme: {pre_value}")
main = call(keywords)
post = call(["tufting"])
post_value = post["tasks"][0]["result"][0].get("search_volume")
if post_value != pre_value:
    raise SystemExit(f"Témoin après divergent: {post_value} vs {pre_value}")
proof = {
    "read_date": "2026-09-01",
    "endpoint": "keywords_data/google_ads/search_volume/live",
    "parameters": {"location_name": "France", "language_name": "French", "search_partners": False},
    "witness_before": pre,
    "grouped_control": main,
    "witness_after": post
}
(ROOT / "search-volume-raw.json").write_text(json.dumps(proof, ensure_ascii=False, indent=2))
rows = main["tasks"][0]["result"]
summary = {
    "read_date": "2026-09-01",
    "endpoint": "keywords_data/google_ads/search_volume/live",
    "parameters": proof["parameters"],
    "cost_usd": sum((x.get("cost") or 0) for x in (pre, main, post)),
    "witness_before": pre_value,
    "witness_after": post_value,
    "rows": rows
}
(ROOT / "search-volume-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2))
print(json.dumps({
    "witness_before": pre_value,
    "witness_after": post_value,
    "rows": len(rows),
    "cost_usd": summary["cost_usd"],
    "result_keys": sorted(set().union(*(r.keys() for r in rows)))
}, ensure_ascii=False))
