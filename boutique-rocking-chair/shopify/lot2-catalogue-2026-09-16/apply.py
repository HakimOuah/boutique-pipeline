"""Construit, pour chaque fiche du lot 2, la mutation GraphQL Shopify à partir de <handle>.md et <handle>.plan.json.

Usage : python3 apply.py            -> écrit gql/<handle>.gql + gql/INDEX.json et affiche les contrôles
"""
import json, re, pathlib, sys
import markdown

L = pathlib.Path(__file__).resolve().parent
F = L / "fiches"
OUT = L / "gql"
OUT.mkdir(exist_ok=True)

COLL = json.load(open(L / "collections_ids.json")) if (L / "collections_ids.json").exists() else {}
RAW = {p["id"]: p for p in json.load(open(L / "shopify_raw.json"))["data"]["products"]["nodes"]}


def value_id(gid, option_id, old):
    for o in RAW[gid]["options"]:
        if o["id"] == option_id:
            for v in o["optionValues"]:
                if v["name"] == old:
                    return v["id"]
    return None


def md_to_payload(path):
    s = path.read_text()
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    seo_t = re.search(r"\*\*Meta title \(≤60\) :\*\*\s*(.+)", s).group(1).strip()
    seo_d = re.search(r"\*\*Meta description \(≤155\) :\*\*\s*(.+)", s).group(1).strip()
    body = re.sub(r"^\*\*[^\n]*:\*\*[^\n]*\n", "", s, flags=re.M).strip()
    secs = [x for x in re.split(r"^## ", body, flags=re.M) if x.strip()]
    if secs[0].startswith("H1"):
        h1 = secs[0].split("\n", 1)[1].strip()
        sub = secs[1].split("\n", 1)[1].strip()
    else:
        h1 = secs[0].strip().split("\n")[0]
        sub = secs[1].strip().split("\n")[0]
    rest = secs[2:]
    html = [f"<p><strong>{sub}</strong></p>"]
    alts = []
    for sec in rest:
        name, _, content = sec.partition("\n")
        name, content = name.strip(), content.strip()
        if name.startswith("Images"):
            alts = [re.sub(r"^\s*[-*\d.]+\s*", "", l).strip() for l in content.split("\n") if l.strip()]
            continue
        if name == "Bloc d'achat":
            lines = [l for l in content.split("\n") if l.startswith("- ")]
            html.append(markdown.markdown("\n".join(lines)))
            continue
        if name == "Description":
            html.append(markdown.markdown(content))
            continue
        html.append(f"<h2>{name}</h2>")
        if name == "FAQ":
            content = re.sub(r"\*\*\n", "**<br>\n", content)
        html.append(markdown.markdown(content, extensions=["tables"]))
    return {"title": h1, "descriptionHtml": "\n".join(html), "seo": {"title": seo_t, "description": seo_d}, "alts": alts}


def q(v):
    return json.dumps(v, ensure_ascii=False)


def build(plan, pay):
    gid = plan["gid"]
    parts, checks = [], []
    keep = [v for v in plan["variants"] if v["keep"]]
    drop = [v["id"] for v in plan["variants"] if not v["keep"]]
    if not keep:
        checks.append("AUCUNE VARIANTE GARDÉE")
    if drop:
        parts.append(f'd: productVariantsBulkDelete(productId:{q(gid)}, variantsIds:{q(drop)}) {{ userErrors {{ field message }} }}')
    i = 0
    for o in plan["options"]:
        if o.get("delete"):
            parts.append(f'od{i}: productOptionsDelete(productId:{q(gid)}, options:[{q(o["id"])}], strategy:DEFAULT) {{ userErrors {{ field message code }} }}')
        else:
            # valeurs : on ne renomme que celles encore portées par une variante gardée (les autres disparaissent avec la suppression)
            kept_vals = {vr["options"].get(o["name_old"]) for vr in plan["_shop_variants"] if vr["id"] in {k["id"] for k in keep}}
            ren = [v for v in o.get("values", []) if v.get("old") in kept_vals and v.get("new") and v["old"] != v["new"]]
            for v in ren:
                v["value_id"] = value_id(gid, o["id"], v["old"])
                if not v["value_id"]:
                    checks.append(f"valeur introuvable {o['name_old']}={v['old']}")
            vals = ", ".join("{" + f'id:{q(v["value_id"])}, name:{q(v["new"])}' + "}" for v in ren if v.get("value_id"))
            parts.append(
                f'ou{i}: productOptionUpdate(productId:{q(gid)}, option:{{id:{q(o["id"])}, name:{q(o["name_new"])}}}'
                + (f', optionValuesToUpdate:[{vals}]' if vals else "")
                + ') { userErrors { field message code } }')
        i += 1
    prod = {"id": gid, "title": pay["title"], "handle": plan["handle"], "descriptionHtml": pay["descriptionHtml"],
            "seo": pay["seo"], "productType": plan["productType"], "vendor": "Bercelou",
            "tags": plan["collections"]}
    parts.append(
        "p: productUpdate(product:{" + ", ".join(f"{k}:{q(v) if not isinstance(v, dict) else '{' + ', '.join(f'{kk}:{q(vv)}' for kk, vv in v.items()) + '}'}" for k, v in prod.items()) + "}) { product { id handle } userErrors { field message } }")
    vv = ", ".join("{" + f'id:{q(v["id"])}, price:{q(f"{float(v["price"]):.2f}")}, inventoryPolicy:DENY' + "}" for v in keep)
    if vv:
        parts.append(f'u: productVariantsBulkUpdate(productId:{q(gid)}, variants:[{vv}]) {{ userErrors {{ field message }} }}')
    # pastilles : hex sur la première variante gardée de chaque couleur
    copt = next((o for o in plan["options"] if not o.get("delete") and o["name_new"].lower() == "couleur"), None)
    if copt:
        hexes = {v["old"]: v.get("hex") for v in copt.get("values", [])}
        done, mf = set(), []
        for vr in plan["_shop_variants"]:
            if vr["id"] not in {k["id"] for k in keep}:
                continue
            old = vr["options"].get(copt["name_old"])
            if old in done:
                continue
            done.add(old)
            if hexes.get(old):
                mf.append("{" + f'ownerId:{q(vr["id"])}, namespace:"color", key:"hexcode", type:"color", value:{q(hexes[old].upper())}' + "}")
            else:
                checks.append(f"hex manquant {old}")
        if mf:
            parts.append(f'm: metafieldsSet(metafields:[{", ".join(mf)}]) {{ userErrors {{ field message }} }}')
    for c in plan["collections"]:
        if c not in COLL:
            checks.append(f"collection inconnue {c}")
    if len(pay["title"]) > 60:
        checks.append(f"H1 {len(pay['title'])} car.")
    if len(pay["seo"]["title"]) > 60:
        checks.append(f"meta title {len(pay['seo']['title'])} car.")
    if len(pay["seo"]["description"]) > 155:
        checks.append(f"meta desc {len(pay['seo']['description'])} car.")
    cost = {vr["id"]: float(vr["cout_eur_pousse_par_dsers"]) for vr in plan["_shop_variants"]}
    for v in keep:
        if float(v["price"]) < 1.6 * cost[v["id"]] - 0.01:
            checks.append(f"prix {v['price']} < 1,6 × coût {cost[v['id']]}")
    return "mutation {\n  " + "\n  ".join(parts) + "\n}\n", checks


def main():
    index, seen = {}, {}
    for pf in sorted(F.glob("*.plan.json")):
        plan = json.load(open(pf))
        plan["_shop_variants"] = json.load(open(L / "bundles" / f"{plan['pid']}.json"))["shopify_variants"]
        h = plan["handle"]
        md = F / f"{h}.md"
        if not md.exists():
            print("MANQUE md", h); continue
        if h in seen:
            print("HANDLE EN DOUBLE", h, seen[h], plan["pid"])
        seen[h] = plan["pid"]
        pay = md_to_payload(md)
        gql, checks = build(plan, pay)
        (OUT / f"{h}.gql").write_text(gql)
        index[h] = {"pid": plan["pid"], "gid": plan["gid"], "len": len(gql), "checks": checks,
                    "collections": plan["collections"], "alts": pay["alts"]}
        if checks:
            print(h, checks)
    json.dump(index, open(OUT / "INDEX.json", "w"), ensure_ascii=False, indent=1)
    print(len(index), "mutations prêtes")


if __name__ == "__main__":
    main()
