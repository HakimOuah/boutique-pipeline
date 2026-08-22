#!/usr/bin/env python3
"""Sourcing AliExpress batch pour salve 30×30 — exécuté via browser-use (Chrome local)."""
import json, re, sys, time, os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "analyses", "2026-08-22-recherche-30x30")

# id, name, queries EN techniques, min €, max €
CANDIDATES = {
    "PUR-01": ("Déshumidificateur", ["dehumidifier 12l", "home dehumidifier compressor"], 45, 120),
    "PUR-02": ("Couverture lestée", ["weighted blanket 7kg", "gravity blanket adult"], 35, 90),
    "PUR-03": ("Ventilateur colonne", ["tower fan remote", "column fan oscillating"], 40, 100),
    "PUR-04": ("Shampouineuse", ["carpet cleaner machine", "upholstery shampooer"], 50, 150),
    "PUR-05": ("Tapis de marche", ["walking pad treadmill", "under desk treadmill"], 80, 250),
    "PUR-09": ("Parc bébé", ["playpen baby large", "baby play yard fence"], 45, 120),
    "PUR-10": ("Tarière", ["earth auger petrol", "post hole digger auger"], 55, 200),
    "PUR-13": ("Cave à vin", ["wine cooler cabinet", "wine refrigerator 28 bottle"], 80, 250),
    "PUR-17": ("Coffre-fort", ["digital safe box", "electronic safe cabinet"], 55, 160),
    "PUR-18": ("Ponceuse girafe", ["drywall sander giraffe", "ceiling sander machine"], 50, 150),
    "PUR-19": ("Nettoyeur haute pression", ["pressure washer electric", "high pressure cleaner 2000w"], 50, 130),
    "PUR-20": ("Robot piscine", ["pool cleaner robot cordless", "automatic pool vacuum"], 80, 250),
    "PUR-22": ("Intercom moto", ["motorcycle bluetooth intercom 2 pack", "helmet intercom duo"], 35, 90),
    "PUR-23": ("Baby-foot", ["foosball table", "table football game"], 80, 200),
    "PUR-24": ("Douche solaire", ["solar shower camping", "portable solar heated shower"], 20, 85),
    "PUR-25": ("Hamac sur pied", ["hammock stand steel", "hammock with stand"], 45, 120),
    "PUR-27": ("Porte placard coulissante", ["sliding wardrobe door", "closet sliding door system"], 50, 150),
    "PUR-28": ("PAC piscine", ["pool heat pump", "swimming pool heater pump"], 200, 600),
    "PUR-29": ("Billard", ["pool table 7ft", "billiard table home"], 200, 500),
    "UNIV-01": ("Dressing rangement", ["wardrobe closet organizer system", "portable closet rack"], 35, 100),
    "UNIV-02": ("Mobilier outdoor coussins", ["outdoor cushion cover waterproof", "patio sofa cushion set"], 30, 80),
    "UNIV-03": ("Padel pickleball", ["padel racket carbon", "pickleball paddle set"], 35, 90),
    "UNIV-04": ("Entretien textiles", ["fabric shaver rechargeable", "upholstery cleaner machine"], 25, 70),
    "UNIV-05": ("Mobilier événementiel", ["folding banquet table", "wedding chair covers set"], 35, 90),
    "UNIV-06": ("Meuble gain de place", ["murphy bed mechanism", "sofa bed convertible"], 80, 250),
    "UNIV-07": ("Lounging outdoor", ["outdoor daybed", "patio lounge chair set"], 50, 150),
    "UNIV-08": ("Cuisine extérieure", ["portable gas griddle", "camping kitchen stove"], 40, 120),
    "UNIV-09": ("Traitement jardin", ["brush cutter machine", "electric cultivator tiller"], 45, 150),
    "UNIV-10": ("Tapis design", ["area rug living room", "washable rug large"], 40, 120),
    "UNIV-13": ("Sports nautiques paddle", ["inflatable paddle board", "sup board paddle"], 80, 200),
    "UNIV-16": ("Vin cave accessoires", ["wine aerator electric", "wine decanter set gift"], 28, 75),
    "UNIV-18": ("Vinyle audio salon", ["turntable record player", "vinyl player bluetooth"], 50, 150),
    "UNIV-20": ("Irrigation potager", ["drip irrigation kit timer", "garden watering system automatic"], 22, 65),
    "UNIV-21": ("Rangement chaussures", ["shoe rack cabinet", "rotating shoe organizer"], 35, 100),
    "UNIV-24": ("Sauna bien-être", ["portable steam sauna tent", "infrared sauna blanket"], 80, 250),
    "UNIV-25": ("Aire jeux jardin", ["outdoor playset swing slide", "backyard playground set"], 150, 400),
    "UNIV-26": ("Jeux plein air premium", ["giant yard games set", "premium outdoor game set"], 45, 120),
    "UNIV-29": ("Bagagerie 2-roues", ["motorcycle tail bag", "motorcycle tank bag magnetic"], 30, 80),
    "UNIV-30": ("Hamac cocooning", ["hanging egg chair outdoor", "cocoon hammock chair"], 60, 180),
}


def parse_price(s):
    if not s:
        return 0.0
    s = str(s).replace("€", "").strip()
    if re.search(r",\d{2}$", s):
        s = s.replace(".", "").replace(",", ".")
    else:
        s = s.replace(",", "")
    m = re.search(r"\d+\.?\d*", s)
    try:
        return float(m.group()) if m else 0.0
    except ValueError:
        return 0.0


def parse_sold(s):
    if not s:
        return 0
    s = str(s).lower().replace(" ", "").replace("+", "")
    if "k" in s:
        m = re.search(r"([\d.]+)k", s)
        return int(float(m.group(1)) * 1000) if m else 0
    m = re.search(r"(\d+)", s)
    return int(m.group(1)) if m else 0


def get_price(obj):
    if not obj:
        return ""
    if isinstance(obj, str):
        return obj
    if isinstance(obj, dict):
        if "formattedPrice" in obj:
            return obj["formattedPrice"]
        if "salePrice" in obj:
            return get_price(obj["salePrice"])
    return ""


def get_title(obj):
    if not obj:
        return ""
    if isinstance(obj, str):
        return obj
    if isinstance(obj, dict):
        for k in ("displayTitle", "title", "name"):
            if k in obj:
                return get_title(obj[k])
    return ""


def walk_items(node, out, seen):
    if isinstance(node, dict):
        pid = node.get("productId")
        if pid and str(pid) not in seen:
            price_raw = get_price(node.get("salePrice") or node.get("prices"))
            title = get_title(node.get("title") or node.get("name"))
            if price_raw or title:
                seen.add(str(pid))
                out.append(
                    {
                        "productId": str(pid),
                        "title": title,
                        "salePrice": price_raw,
                        "tradeDesc": node.get("tradeDesc") or "",
                        "starRating": node.get("starRating") or "",
                    }
                )
        for v in node.values():
            walk_items(v, out, seen)
    elif isinstance(node, list):
        for v in node:
            walk_items(v, out, seen)


EXTRACT_PDP = r"""(function(){
  const body = document.body ? document.body.innerText : '';
  const priceMatch = body.match(/([\d]+[,.][\d]{2})\s*€/);
  const soldMatch = body.match(/([\d+ ]+)\s*(?:vendus|ventes)/i);
  const starMatch = body.match(/([\d.]+)\s*(?:Avis|étoiles)/i);
  return {title: document.title, href: location.href, price: priceMatch?priceMatch[1]:null,
    sold: soldMatch?soldMatch[1].trim():null, star: starMatch?starMatch[1]:null, sample: body.slice(0,1200)};
})()"""


def source_one(cand_id, name, queries, min_p, max_p, pdp=False):
    # browser-use globals injected at runtime
    best = None
    tried = []
    for q in queries:
        url = "https://fr.aliexpress.com/w/wholesale-" + q.replace(" ", "-") + ".html?SortType=total_tranpro_desc"
        try:
            new_tab(url)
            wait_for_load()
            time.sleep(2.0)
            raw = js(
                "(function(){ try { return JSON.stringify(window._dida_config_._init_data_); } catch(e){ return null; } })()"
            )
        except Exception as e:
            tried.append({"query": q, "url": url, "serp_count": 0, "error": str(e)})
            continue
        items = []
        if raw:
            try:
                data = json.loads(raw)
                seen = set()
                walk_items(data, items, seen)
            except Exception:
                pass
        tried.append({"query": q, "url": url, "serp_count": len(items)})
        for it in items:
            price = parse_price(it.get("salePrice"))
            if min_p <= price <= max_p:
                sold = parse_sold(it.get("tradeDesc"))
                score = sold * 10 + price
                if best is None or score > best["score"]:
                    best = {
                        "query": q,
                        "productId": it["productId"],
                        "title": it.get("title", ""),
                        "price": it.get("salePrice"),
                        "price_n": price,
                        "sold": it.get("tradeDesc"),
                        "star": it.get("starRating"),
                        "href": "https://fr.aliexpress.com/item/" + it["productId"] + ".html",
                        "score": score,
                    }
        if best:
            break

    entry = {
        "id": cand_id,
        "name": name,
        "queries": queries,
        "min": min_p,
        "max": max_p,
        "tried": tried,
        "confiance": "B",
    }
    if best:
        pdp = None
        if pdp:
            try:
                new_tab(best["href"])
                wait_for_load()
                time.sleep(1.8)
                pdp = js(EXTRACT_PDP)
                entry["confiance"] = "A"
            except Exception as e:
                pdp = {"error": str(e)}
        pdp_price = parse_price(pdp.get("price")) if isinstance(pdp, dict) and pdp.get("price") else 0
        final_price = pdp_price if pdp_price >= min_p else best["price_n"]
        entry["best"] = {
            "query": best["query"],
            "list": {k: best[k] for k in ["href", "title", "price", "sold", "star"]},
            "pdp": pdp,
            "price_n": final_price,
        }
        if final_price >= min_p:
            entry["status"] = "FOURNISSEUR À TESTER"
        elif final_price > 0:
            entry["status"] = "OFFRE TROUVÉE"
        else:
            entry["status"] = "AUCUNE OFFRE EXPLOITABLE"
    else:
        entry["status"] = "AUCUNE OFFRE EXPLOITABLE"
        entry["best"] = None
    return entry


def should_skip(entry, force=False):
    if not entry or force:
        return False
    if entry.get("status") == "FOURNISSEUR À TESTER" and entry.get("best"):
        return True
    # retry timeout failures
    for t in entry.get("tried", []):
        if t.get("error"):
            return False
    return entry.get("status") in ("FOURNISSEUR À TESTER", "OFFRE TROUVÉE", "AUCUNE OFFRE EXPLOITABLE")


def run_batch(batch_ids, outfile, force=False):
    ensure_real_tab()
    results = []
    existing = {}
    if os.path.exists(outfile):
        try:
            results = json.load(open(outfile, encoding="utf-8"))
            existing = {r["id"]: r for r in results}
        except Exception:
            results = []
    for cid in batch_ids:
        if should_skip(existing.get(cid), force=force):
            print("SKIP", cid)
            continue
        if cid not in CANDIDATES:
            print("UNKNOWN", cid)
            continue
        name, queries, min_p, max_p = CANDIDATES[cid]
        print("SOURCING", cid, name, "...")
        entry = source_one(cid, name, queries, min_p, max_p)
        results = [r for r in results if r["id"] != cid] + [entry]
        with open(outfile, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(cid, "=>", entry["status"], entry.get("best", {}).get("price_n") if entry.get("best") else "-")
    return results


if __name__ == "__main__":
    # Usage: browser-use <<'PY'
    # import runpy; runpy.run_path('scripts/ae_sourcing_30x30.py')
    # PY
    # Or pass batch via env BATCH_IDS comma-separated
    batch = os.environ.get("BATCH_IDS", "").split(",")
    batch = [b.strip() for b in batch if b.strip()]
    lot = os.environ.get("LOT", "4")
    outfile = os.path.join(OUT_DIR, f"sourcing-lot{lot}-local.json")
    if not batch:
        print("Set BATCH_IDS env")
        sys.exit(1)
    run_batch(batch, outfile)
