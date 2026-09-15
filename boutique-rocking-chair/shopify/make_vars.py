import json, sys, pathlib
# usage: make_vars.py handle "opt1,opt2" "oldmedia1,..." "slot=fileid,..." "variantid=price,..."
BASE = pathlib.Path(__file__).resolve().parent
P = json.load(open(BASE/"products-payload.json"))
h, opts, rm, add, var = (sys.argv[1:] + [""]*5)[:5]
p = P[h]; pid = p["shopify_id"]
slots = dict(x.split("=") for x in add.split(",") if x)
files_add = []
for m in p["media"]:
    slot = m[len(h)+1:-4]
    files_add.append({"id": "gid://shopify/MediaImage/"+slots[slot], "alt": p["alts"][m], "referencesToAdd": [pid]})
v = {"id": pid,
 "product": {"id": pid, "title": p["title"], "handle": h, "descriptionHtml": p["descriptionHtml"].replace("\n",""), "seo": p["seo"], "productType": p["productType"], "vendor": "Bercelou", "tags": p["tags"]},
 "opts": ["gid://shopify/ProductOption/"+x for x in opts.split(",") if x],
 "filesRemove": [{"id": "gid://shopify/MediaImage/"+x, "referencesToRemove": [pid]} for x in rm.split(",") if x],
 "filesAdd": files_add,
 "variants": [{"id": "gid://shopify/ProductVariant/"+a, "price": b, "compareAtPrice": None} for a,b in (x.split("=") for x in var.split(",") if x)]}
print(json.dumps(v, ensure_ascii=False))
