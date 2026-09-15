import re, json, pathlib, markdown
# build_collections.py -> collections-payload.json (one collectionCreate input per collection)
ROOT = pathlib.Path(__file__).resolve().parent.parent
CDN = "https://cdn.shopify.com/s/files/1/1082/4564/7705/files/"
NAMES = {
    "fauteuils à bascule": "fauteuil-a-bascule",
    "fauteuils d'allaitement": "fauteuil-allaitement",
    "rocking chair design & scandinave": "rocking-chair-design-scandinave",
    "rocking chair bois & rotin": "rocking-chair-bois-rotin",
    "chaises à bascule": "chaise-a-bascule",
    "fauteuils cocon": "fauteuil-cocon",
    "rocking chair extérieur": "rocking-chair-exterieur",
    "fauteuils relax": "fauteuil-relax",
    "fauteuils relax de jardin": "fauteuil-relax-jardin",
    "rocking chair relax & repose-pieds": "rocking-chair-repose-pieds",
    "rocking chair enfant": "rocking-chair-enfant",
    "accessoires rocking chair": "accessoires-rocking-chair",
}
ids = {h: pid for pid, h in json.load(open(ROOT / "shopify/mapping-shopify-handles.json")).items()}
members = {h: [] for h in NAMES.values()}
for f in json.load(open(ROOT / "catalogue-source-2026-09-14.json")):
    for c in f["collections"]:
        members[NAMES[c]].append(f"gid://shopify/Product/{ids[f['handle']]}")

def section(md, name):
    m = re.search(rf"^## {re.escape(name)}\s*\n(.*?)(?=^## |\Z)", md, re.S | re.M)
    return m.group(1).strip() if m else ""

def meta(md, label):
    m = re.search(rf"\*\*{re.escape(label)}[^*]*:\*\*\s*(.+)", md)
    return m.group(1).strip() if m else ""

out = {}
for handle in NAMES.values():
    md = (ROOT / f"content/collections/{handle}.md").read_text()
    title = section(md, "H1")
    faq = section(md, "FAQ")
    faq = re.sub(r"\*\*(.+?)\*\*\s*\n", r"**\1**  \n", faq)  # question + answer on two lines
    body = section(md, "Intro") + "\n\n## Bien choisir\n\n" + section(md, "Aide au choix") + "\n\n## Questions fréquentes\n\n" + faq
    html = markdown.markdown(body)
    out[handle] = {
        "input": {
            "title": title,
            "handle": handle,
            "descriptionHtml": html,
            "seo": {"title": meta(md, "Meta title"), "description": meta(md, "Meta description")},
            "image": {"src": f"{CDN}collection-{handle}-carte.jpg", "altText": title},
            "products": members[handle],
        }
    }
    assert len(out[handle]["input"]["seo"]["title"]) <= 60, handle
    assert len(out[handle]["input"]["seo"]["description"]) <= 155, handle
json.dump(out, open(ROOT / "shopify/collections-payload.json", "w"), ensure_ascii=False, indent=1)
for h, v in out.items():
    print(h, len(v["input"]["products"]), v["input"]["title"], "|", v["input"]["seo"]["title"])
