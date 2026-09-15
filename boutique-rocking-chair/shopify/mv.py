import json, sys, pathlib
# mv.py handle 'spec-json'   spec: {"opts":[..], "rm":[..], "add":{"slot":id}, "price":{"vid":"199.00"}, "del":[..], "ren":{"id":optid,"name":"Couleur","vals":{"valid":"Rose"}}}
BASE = pathlib.Path(__file__).resolve().parent
P = json.load(open(BASE/"products-payload.json"))
h = sys.argv[1]; s = json.loads(sys.argv[2]); p = P[h]; pid = p["shopify_id"]
G = lambda kind, x: f"gid://shopify/{kind}/{x}"
fa = [{"id": G("MediaImage", s["add"][m[len(h)+1:-4]]), "alt": p["alts"][m], "referencesToAdd": [pid]} for m in p["media"]]
ren = s.get("ren")
v = {"id": pid,
 "product": {"id": pid, "title": p["title"], "handle": h, "descriptionHtml": p["descriptionHtml"].replace("\n",""), "seo": p["seo"], "productType": p["productType"], "vendor": "Bercelou", "tags": p["tags"]},
 "opts": [G("ProductOption", x) for x in s.get("opts", [])], "hasOpts": bool(s.get("opts")),
 "del": [G("ProductVariant", x) for x in s.get("del", [])], "hasDel": bool(s.get("del")),
 "rename": {"id": G("ProductOption", ren["id"]), "name": ren["name"]} if ren else {"id": G("ProductOption", "0")},
 "vals": [{"id": G("ProductOptionValue", k), "name": n} for k, n in (ren or {}).get("vals", {}).items()], "hasRename": bool(ren),
 "filesRemove": [{"id": G("MediaImage", x), "referencesToRemove": [pid]} for x in s["rm"]],
 "filesAdd": fa,
 "variants": [{"id": G("ProductVariant", k), "price": pr, "compareAtPrice": None} for k, pr in s["price"].items()]}
print(json.dumps(v, ensure_ascii=False))
