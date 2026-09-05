#!/usr/bin/env python3
"""DataForSEO Labs ranked_keywords + relevant_pages + domain_rank_overview — France/fr."""
import base64
import json
import os
import time
import urllib.request
from collections import defaultdict
from pathlib import Path

LOGIN = os.environ["DATAFORSEO_LOGIN"]
PASSWORD = os.environ["DATAFORSEO_PASSWORD"]
TOKEN = base64.b64encode(f"{LOGIN}:{PASSWORD}".encode()).decode()
BASE = "https://api.dataforseo.com/v3"
OUT = Path(
    "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/"
    "analyses/2026-09-03-univers-poufs/raw"
)
DATE = "2026-09-03"

TARGETS = {
    "big-bertha-original": "bigberthaoriginal.fr",
    "bananair": "bananair.fr",
    "iconpouf": "iconpouf.fr",
    "happers": "happers.fr",
    "casabiloba": "casabiloba.fr",
}


def post(endpoint, payload):
    req = urllib.request.Request(
        BASE + endpoint,
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Basic {TOKEN}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode())


def save(slug, name, data):
    dest = OUT / slug / DATE / "seo"
    dest.mkdir(parents=True, exist_ok=True)
    path = dest / name
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    return path


def ranked_keywords(target):
    # paginate up to 3 pages of 1000
    all_items = []
    cost = 0
    status = None
    for offset in (0, 1000, 2000):
        payload = [{
            "target": target,
            "location_name": "France",
            "language_name": "French",
            "item_types": ["organic"],
            "limit": 1000,
            "offset": offset,
            "order_by": ["keyword_data.keyword_info.search_volume,desc"],
        }]
        data = post("/dataforseo_labs/google/ranked_keywords/live", payload)
        status = data.get("status_code")
        cost += data.get("cost") or 0
        tasks = data.get("tasks") or []
        if not tasks or tasks[0].get("status_code") != 20000:
            if offset == 0:
                return data, []
            break
        result = (tasks[0].get("result") or [None])[0] or {}
        items = result.get("items") or []
        all_items.extend(items)
        total = result.get("total_count") or 0
        print(f"    ranked offset {offset}: {len(items)} items, total_count={total}, cost so far {cost}")
        if len(items) < 1000 or offset + 1000 >= total:
            break
        time.sleep(0.4)
    # wrap last response + aggregated items
    return {"status_code": status, "cost": cost, "n_items": len(all_items), "raw_last": data}, all_items


def relevant_pages(target):
    payload = [{
        "target": target,
        "location_name": "France",
        "language_name": "French",
        "limit": 100,
        "order_by": ["metrics.organic.etv,desc"],
    }]
    return post("/dataforseo_labs/google/relevant_pages/live", payload)


def domain_overview(target):
    payload = [{
        "target": target,
        "location_name": "France",
        "language_name": "French",
    }]
    return post("/dataforseo_labs/google/domain_rank_overview/live", payload)


def agg_by_url(items):
    by = defaultdict(lambda: {
        "etv": 0.0,
        "n_kw": 0,
        "top3": 0,
        "top10": 0,
        "examples": [],
    })
    for it in items:
        kd = it.get("keyword_data") or {}
        ri = it.get("ranked_serp_element") or {}
        serp = ri.get("serp_item") or {}
        url = serp.get("url") or "(sans url)"
        etv = float(serp.get("etv") or 0)
        rank = serp.get("rank_absolute") or serp.get("rank_group")
        kw = kd.get("keyword")
        vol = (kd.get("keyword_info") or {}).get("search_volume")
        rec = by[url]
        rec["etv"] += etv
        rec["n_kw"] += 1
        if isinstance(rank, (int, float)):
            if rank <= 3:
                rec["top3"] += 1
            if rank <= 10:
                rec["top10"] += 1
        if len(rec["examples"]) < 5:
            rec["examples"].append({"kw": kw, "vol": vol, "rank": rank, "etv": etv})
    rows = []
    for url, rec in by.items():
        rec["url"] = url
        rec["etv"] = round(rec["etv"], 2)
        rows.append(rec)
    rows.sort(key=lambda x: -x["etv"])
    return rows


def main():
    report = {}
    for slug, target in TARGETS.items():
        print(f"\n=== DFS {target} ===")
        try:
            ov = domain_overview(target)
            save(slug, "domain-rank-overview.json", ov)
            ov_res = ((ov.get("tasks") or [{}])[0].get("result") or [None])[0]
            print(f"  overview status {ov.get('status_code')} cost {ov.get('cost')} result={bool(ov_res)}")
        except Exception as e:
            ov = {"error": str(e)}
            save(slug, "domain-rank-overview.json", ov)
            print(f"  overview FAIL {e}")

        try:
            rp = relevant_pages(target)
            save(slug, "relevant-pages.json", rp)
            items = (((rp.get("tasks") or [{}])[0].get("result") or [{}])[0].get("items") or [])
            print(f"  relevant_pages {len(items)} cost {rp.get('cost')}")
        except Exception as e:
            rp = {"error": str(e)}
            save(slug, "relevant-pages.json", rp)
            print(f"  relevant_pages FAIL {e}")

        try:
            meta, items = ranked_keywords(target)
            save(slug, "ranked-keywords-meta.json", {
                "status_code": meta.get("status_code"),
                "cost": meta.get("cost"),
                "n_items": meta.get("n_items"),
            })
            # don't dump 3000 raw items if huge — save a compact extract
            compact = []
            for it in items:
                kd = it.get("keyword_data") or {}
                ri = it.get("ranked_serp_element") or {}
                serp = ri.get("serp_item") or {}
                compact.append({
                    "keyword": kd.get("keyword"),
                    "search_volume": (kd.get("keyword_info") or {}).get("search_volume"),
                    "cpc": (kd.get("keyword_info") or {}).get("cpc"),
                    "url": serp.get("url"),
                    "rank_absolute": serp.get("rank_absolute"),
                    "etv": serp.get("etv"),
                    "type": serp.get("type"),
                })
            save(slug, "ranked-keywords-compact.json", compact)
            by_url = agg_by_url(items)
            save(slug, "ranked-keywords-by-url.json", by_url)
            print(f"  ranked {len(items)} items, {len(by_url)} urls, cost {meta.get('cost')}")
        except Exception as e:
            print(f"  ranked FAIL {e}")
            save(slug, "ranked-keywords-error.json", {"error": str(e)})
            by_url = []
            items = []

        report[slug] = {
            "target": target,
            "n_ranked": len(items) if isinstance(items, list) else 0,
            "n_urls": len(by_url) if isinstance(by_url, list) else 0,
        }
        time.sleep(0.5)

    (OUT / "_scratch" / "dfs-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2)
    )
    print("done", report)


if __name__ == "__main__":
    main()
