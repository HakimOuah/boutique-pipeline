#!/usr/bin/env python3
"""Contrôle de têtes — search_volume/live France/français. 2026-09-02."""
import base64, json, os, pathlib, urllib.request

API = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"
ROOT = pathlib.Path(__file__).resolve().parent

KEYWORDS = [
    "tufting",
    "portefeuille",
    "portefeuilles",
    "portefeuille homme",
    "portefeuille hommes",
    "portefeuille femme",
    "porte-cartes",
    "porte cartes",
    "porte-cartes homme",
    "porte-cartes femme",
    "portefeuille carte",
    "portefeuille carte homme",
    "portefeuille carte femme",
    "porte-monnaie",
    "porte monnaie",
    "porte-monnaie femme",
    "porte-monnaie homme",
    "compagnon portefeuille",
    "compagnon portefeuille femme",
    "protège-passeport",
    "protege passeport",
    "portefeuille chaîne",
    "portefeuille chaine",
    "portefeuille à chaîne",
    "portefeuille rfid",
    "portefeuille cuir",
    "portefeuille homme cuir",
    "portefeuille femme cuir",
    "robe portefeuille",
    "jupe portefeuille",
    "pantalon portefeuille",
    "portefeuille louis vuitton",
    "louis vuitton portefeuille",
    "portefeuille goyard",
    "portefeuille chanel",
    "portefeuille lacoste",
    "portefeuille cabaia",
    "petit portefeuille femme",
    "grand portefeuille femme",
    "portefeuille personnalisé",
    "etui carte",
    "étui cartes",
    "card holder",
    "portefeuille slim",
    "portefeuille minimaliste",
    "portefeuille aluminium",
    "portefeuille bitcoin",
    "portefeuille crypto",
    "coque portefeuille",
    "portefeuille samsung",
    "portefeuille iphone",
    "portefeuille english",
    "portefeuille anglais",
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


def volume(body):
    result = body["tasks"][0]["result"]
    if not result:
        return None
    return result[0].get("search_volume")


pre = call(["tufting"])
pre_value = volume(pre)
if pre_value != 12100:
    raise SystemExit(f"Témoin avant non conforme: {pre_value}")
main = call(KEYWORDS)
post = call(["tufting"])
post_value = volume(post)
if post_value != pre_value:
    raise SystemExit(f"Témoin après divergent: {post_value} vs {pre_value}")

rows = main["tasks"][0]["result"] or []
proof = {
    "read_date": "2026-09-02",
    "endpoint": "keywords_data/google_ads/search_volume/live",
    "parameters": {
        "location_name": "France",
        "language_name": "French",
        "search_partners": False,
    },
    "witness_before": pre_value,
    "witness_after": post_value,
    "cost_usd": sum((x.get("cost") or 0) for x in (pre, main, post)),
    "rows": rows,
}
(ROOT / "2026-09-02-tetes-live.json").write_text(
    json.dumps(proof, ensure_ascii=False, indent=2)
)

def serie(row):
    monthly = row.get("monthly_searches") or []
    return tuple((m.get("year"), m.get("month"), m.get("search_volume")) for m in monthly)

print(f"temoin {pre_value} / {post_value}  cost={proof['cost_usd']}")
print(f"{'keyword':42} {'vol':>8} {'cpc':>7} {'cur':>4}  serie_fingerprint")
by_kw = {r.get("keyword"): r for r in rows}
for r in rows:
    kw = r.get("keyword") or ""
    vol = r.get("search_volume")
    cpc = r.get("cpc")
    cur = r.get("currency") or r.get("money_currency") or "?"
    s = serie(r)
    fp = hash(s) % 10000 if s else "-"
    print(f"{kw:42} {str(vol):>8} {str(cpc):>7} {cur:>4}  {fp}")

# Paires à tester pour fusion de bucket
paires = [
    ("portefeuille", "portefeuilles"),
    ("portefeuille", "portefeuille homme"),
    ("portefeuille", "portefeuille femme"),
    ("portefeuille homme", "portefeuille hommes"),
    ("portefeuille", "porte-monnaie"),
    ("portefeuille femme", "porte-monnaie femme"),
    ("portefeuille homme", "porte-cartes homme"),
    ("portefeuille carte", "porte-cartes"),
    ("portefeuille carte homme", "porte-cartes homme"),
    ("portefeuille carte femme", "porte-cartes femme"),
    ("portefeuille homme", "portefeuille homme cuir"),
    ("protège-passeport", "protege passeport"),
    ("portefeuille chaîne", "portefeuille chaine"),
    ("portefeuille louis vuitton", "louis vuitton portefeuille"),
]
print("\n=== Comparaison de séries (identique = un seul bucket) ===")
for a, b in paires:
    ra, rb = by_kw.get(a), by_kw.get(b)
    if not ra or not rb:
        print(f"{a} / {b} : ligne manquante")
        continue
    sa, sb = serie(ra), serie(rb)
    same = sa == sb and sa
    print(
        f"{a} ({ra.get('search_volume')}) / {b} ({rb.get('search_volume')}) "
        f"→ {'MÊME BUCKET' if same else 'distinct'}"
    )
