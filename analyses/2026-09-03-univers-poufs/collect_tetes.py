#!/usr/bin/env python3
"""Contrôle de têtes — search_volume/live France/français. 2026-09-03 univers poufs."""
import base64, json, os, pathlib, urllib.request

API = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"
OUT = pathlib.Path(__file__).resolve().parent

KEYWORDS = [
    "tufting",
    "pouf",
    "poufs",
    "pouf salon",
    "pouf poire",
    "poire pouf",
    "pouf poire adulte",
    "pouf enfant",
    "pouf poire enfant",
    "pouf chambre enfant",
    "pouf géant",
    "pouf geant",
    "pouf xxl",
    "pouf géant xxl",
    "canapé pouf",
    "canape pouf",
    "fauteuil pouf",
    "pouf gamer",
    "pouf gaming",
    "pouf extérieur",
    "pouf exterieur",
    "pouf d'extérieur",
    "pouf jardin",
    "repose-pieds",
    "repose pieds",
    "pouf repose-pieds",
    "coussin de sol",
    "housse pouf",
    "housse pouf poire",
    "pouf à rangement",
    "coffre pouf",
    "pouf rond",
    "pouf carré",
    "bean bag",
    "pouf bean bag",
    "fauteuil poire",
    "pouf velours",
    "pouf velours côtelé",
    "fatboy pouf",
    "pouf fatboy",
    "yogibo",
    "big bertha pouf",
    "lounge pug",
    "pouf ikea",
    "ikea pouf",
    "pouf maisons du monde",
    "pouf action",
    "pouf chambre ado",
    "pouf ado",
    "adulte pouf poire",
    "pouf poire xxl",
    "remplissage pouf",
    "billes pouf",
    "bille polystyrène pouf",
]


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
        "search_partners": False,
    }]
    req = urllib.request.Request(API, data=json.dumps(payload).encode(), headers={
        "Authorization": auth(), "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req, timeout=180) as response:
        return json.load(response)


def main():
    body = call(KEYWORDS)
    dest = OUT / "tetes-live.json"
    dest.write_text(json.dumps(body, ensure_ascii=False, indent=2), encoding="utf-8")
    result = (body.get("tasks") or [{}])[0].get("result") or []
    print(f"wrote {dest} n={len(result)} cost={(body.get('tasks') or [{}])[0].get('cost')}")
    for row in result:
        kw = row.get("keyword")
        vol = row.get("search_volume")
        cpc = row.get("cpc")
        cur = row.get("monthly_searches") or []
        series = " ".join(str(m.get("search_volume")) for m in reversed(cur[-12:]))
        print(f"{vol!s:>8}  cpc={cpc}  {kw}  | {series}")


if __name__ == "__main__":
    main()
