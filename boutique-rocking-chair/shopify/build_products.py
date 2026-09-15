import re, json, pathlib, markdown
BASE = pathlib.Path(__file__).resolve().parent.parent
cat = {f["handle"]: f for f in json.load(open(BASE/"catalogue-source-2026-09-14.json"))}
mapping = json.load(open(BASE/"shopify/mapping-shopify-handles.json"))
FAMILY = {"rocking chair extérieur@housse":"Accessoire","fauteuils relax":"Fauteuil relax","fauteuils relax de jardin":"Fauteuil relax","rocking chair enfant":"Fauteuil enfant","accessoires rocking chair":"Accessoire"}
SLOT = {"face":"vue d'ensemble","nuit":"au calme le soir","salon":"au salon","matiere":"détail de la matière","detail":"détail","soir":"en fin de journée","usage":"en situation","reglages":"position inclinée","situation":"en situation"}
ORDER = ["face","salon","nuit","soir","usage","reglages","situation","matiere","detail"]
imgs = sorted(p.name for p in pathlib.Path("/private/tmp/claude-502/-Users-Hakim-Documents-Boutiques-drop/3e7e2b1c-6159-4d50-8344-3a7c42b52fca/scratchpad/upload-shopify").glob("*.jpg"))
out = {}
for h, f in cat.items():
    s = (BASE/f"content/produits/{h}.md").read_text()
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    seo_t = re.search(r"\*\*Meta title \(≤60\) :\*\* (.+)", s).group(1).strip()
    seo_d = re.search(r"\*\*Meta description \(≤155\) :\*\* (.+)", s).group(1).strip()
    body = re.sub(r"^\*\*[^\n]*:\*\*[^\n]*\n", "", s, flags=re.M).strip()
    secs = re.split(r"^## ", body, flags=re.M)
    secs = [x for x in secs if x.strip()]
    if secs[0].startswith("H1"):
        h1 = secs[0].split("\n",1)[1].strip(); sub = secs[1].split("\n",1)[1].strip(); rest = secs[2:]
    else:
        h1 = secs[0].strip().split("\n")[0]; sub = secs[1].strip().split("\n")[0]; rest = secs[2:]
    html = [f"<p><strong>{sub}</strong></p>"]
    for sec in rest:
        name, _, content = sec.partition("\n")
        name = name.strip(); content = content.strip()
        if name.startswith("Images"): continue
        if name == "Bloc d'achat":
            lines = [l for l in content.split("\n") if l.startswith("- ")]
            html.append(markdown.markdown("\n".join(lines)))
            continue
        if name == "Description":
            html.append(markdown.markdown(re.sub(r"^### ", "### ", content, flags=re.M)).replace("<h3>","<h3>"))
            continue
        html.append(f"<h2>{name}</h2>")
        if name == "FAQ":
            content = re.sub(r"\*\*\n", "**<br>\n", content)
        html.append(markdown.markdown(content, extensions=["tables"]))
    desc = "\n".join(html)
    fam = "Accessoire" if h.startswith("housse") else FAMILY.get(f["collections"][0], "Fauteuil à bascule")
    media = [i for i in imgs if re.fullmatch(re.escape(h)+r"-([a-z]+)\.jpg", i)]
    media.sort(key=lambda i: ORDER.index(re.fullmatch(re.escape(h)+r"-([a-z]+)\.jpg", i).group(1)))
    alts = {i: f"{h1} – {SLOT[re.fullmatch(re.escape(h)+r'-([a-z]+)\.jpg', i).group(1)]}" for i in media}
    pid = [k for k,v in mapping.items() if v==h][0]
    out[h] = {"shopify_id": f"gid://shopify/Product/{pid}", "title": h1, "handle": h, "descriptionHtml": desc, "seo": {"title": seo_t, "description": seo_d}, "productType": fam, "tags": f["collections"], "media": media, "alts": alts}
json.dump(out, open(BASE/"shopify/products-payload.json","w"), ensure_ascii=False, indent=1)
for h,v in out.items(): print(h, len(v["descriptionHtml"]), len(v["media"]), v["productType"], "|", v["title"][:60])
