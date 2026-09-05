#!/usr/bin/env python3
import json
from pathlib import Path

RAW = Path(
    "/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/"
    "analyses/2026-09-03-univers-poufs/raw"
)
DATE = "2026-09-03"
SLUGS = ["big-bertha-original", "bananair", "iconpouf", "happers", "casabiloba"]


def pick(d, *keys, default=None):
    cur = d
    for k in keys:
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur


for slug in SLUGS:
    seo = RAW / slug / DATE / "seo"
    print(f"\n========== {slug} ==========")
    ov = json.loads((seo / "domain-rank-overview.json").read_text())
    tasks = ov.get("tasks") or []
    result = (tasks[0].get("result") or [None])[0] if tasks else None
    if result:
        metrics = (result.get("metrics") or {}).get("organic") or {}
        print("overview organic:", {k: metrics.get(k) for k in [
            "etv", "count", "estimated_paid_traffic_cost", "is_new", "is_up", "is_down",
            "is_lost", "pos_1", "pos_2_3", "pos_4_10", "pos_11_20", "pos_21_50", "pos_51_100",
        ]})
        print("target", result.get("target"), "location", result.get("location_code"))
    else:
        print("overview empty", ov.get("status_message"), (tasks[0] if tasks else None))

    by = json.loads((seo / "ranked-keywords-by-url.json").read_text())
    total_etv = sum(x["etv"] for x in by)
    print(f"ranked by url: {len(by)} urls, sum etv {round(total_etv,1)}")
    print("TOP 20 URL:")
    for row in by[:20]:
        ex = ", ".join(
            f"{e['kw']} r{e['rank']} v{e['vol']}"
            for e in (row.get("examples") or [])[:3]
        )
        print(f"  {row['etv']:8.1f} | {row['n_kw']:3} kw | t3={row['top3']:2} t10={row['top10']:2} | {row['url']}")
        print(f"           {ex}")

    rp = json.loads((seo / "relevant-pages.json").read_text())
    ritems = (((rp.get("tasks") or [{}])[0].get("result") or [{}])[0].get("items") or [])
    print("relevant_pages top 10:")
    for it in ritems[:10]:
        m = (it.get("metrics") or {}).get("organic") or {}
        print(f"  etv={m.get('etv')} count={m.get('count')} pos1={m.get('pos_1')} | {it.get('page_address')}")
