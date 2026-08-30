#!/usr/bin/env python3
"""Purge les metafields d'avis qui peuvent alimenter le flux Shopping.

Cible uniquement les fiches dont le compteur n'est pas nul :
  - reviews.rating / reviews.rating_count  (lu par Google & YouTube)
  - vstar.product_rating                   (Trustoo, miroir du meme compteur)

Les 23 fiches deja a 0/0 ne sont pas touchees.
Dry-run par defaut ; --ecrire pour appliquer.
"""
import json, subprocess, sys

STORE = "et0hua-w1.myshopify.com"
DUMP = "/Users/Hakim/Documents/Boutiques drop/scratchpad/tufteo-mf-ids-3008.json"


def cli(query, muter=False):
    cmd = ["shopify", "store", "execute", "--store", STORE, "--json", "--query", query]
    if muter:
        cmd.append("--allow-mutations")
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = r.stdout
    i = out.find("{")
    if i < 0:
        sys.exit("Reponse CLI illisible :\n" + out + r.stderr)
    return json.loads(out[i:])


def cibles(dump):
    out = []
    for p in dump["products"]["nodes"]:
        for m in p["metafields"]["nodes"]:
            if m["namespace"] == "reviews" and m["key"] in ("rating", "rating_count"):
                out.append((p["title"], m))
            elif m["namespace"] == "vstar" and m["key"] == "product_rating":
                try:
                    n = int(json.loads(m["value"]).get("total_reviews") or 0)
                except Exception:
                    n = 0
                if n > 0:
                    out.append((p["title"], m))
    return out


dump = json.load(open(DUMP))
rows = cibles(dump)
print(f"{len(rows)} metafields a supprimer sur {len({t for t,_ in rows})} fiches\n")
for t, m in rows:
    extra = ""
    if m["key"] == "rating_count":
        extra = f"  count={m['value']}"
    elif m["namespace"] == "vstar":
        extra = f"  {m['value'][:80]}"
    print(f"  {t[:42]:42}  {m['namespace']}.{m['key']}{extra}")

if "--ecrire" not in sys.argv:
    print("\nDRY-RUN — relancer avec --ecrire")
    sys.exit(0)

# metafieldsDelete prend ownerId + namespace + key (pas l'id)
# on reconstruit ownerId depuis le dump
owners = {}
for p in dump["products"]["nodes"]:
    owners[p["title"]] = p["id"]

ok = ko = 0
for i in range(0, len(rows), 10):
    lot = rows[i:i + 10]
    items = []
    for t, m in lot:
        items.append(
            f'{{ownerId: "{owners[t]}", namespace: "{m["namespace"]}", key: "{m["key"]}"}}'
        )
    q = (
        "mutation { metafieldsDelete(metafields: ["
        + ", ".join(items)
        + "]) { deletedMetafields { ownerId namespace key } userErrors { field message } } }"
    )
    res = cli(q, muter=True)
    r = res.get("metafieldsDelete") or {}
    errs = r.get("userErrors") or []
    deleted = {(d["namespace"], d["key"], d["ownerId"]) for d in (r.get("deletedMetafields") or [])}
    if errs:
        print("  erreurs lot :", errs)
    for t, m in lot:
        if (m["namespace"], m["key"], owners[t]) in deleted:
            ok += 1
            print(f"  ok     {t[:40]}  {m['namespace']}.{m['key']}")
        else:
            ko += 1
            print(f"  ECHEC  {t[:40]}  {m['namespace']}.{m['key']}")

print(f"\n{ok} supprimes, {ko} en echec")
