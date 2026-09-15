import json, sys
# sv.py specs.json -> prints mutation doc and variables for N products
P = json.load(open("products-payload.json"))
specs = json.load(open(sys.argv[1]))
G = lambda k, x: f"gid://shopify/{k}/{x}"
doc_vars, body, V = [], [], {}
for i, (h, s) in enumerate(specs.items()):
    p = P[h]; pid = p["shopify_id"]; a = f"x{i}"
    V[a+"id"] = pid
    if s.get("del"):
        doc_vars.append(f"${a}del: [ID!]!"); V[a+"del"] = [G("ProductVariant", x) for x in s["del"]]
        body.append(f"{a}d: productVariantsBulkDelete(productId: ${a}id, variantsIds: ${a}del) {{ userErrors {{ field message }} }}")
    if s.get("opts"):
        doc_vars.append(f"${a}opts: [ID!]!"); V[a+"opts"] = [G("ProductOption", x) for x in s["opts"]]
        body.append(f"{a}o: productOptionsDelete(productId: ${a}id, options: ${a}opts, strategy: NON_DESTRUCTIVE) {{ userErrors {{ field message }} }}")
    for j, r in enumerate(s.get("ren", [])):
        doc_vars += [f"${a}r{j}: OptionUpdateInput!", f"${a}v{j}: [OptionValueUpdateInput!]!"]
        V[f"{a}r{j}"] = {"id": G("ProductOption", r["id"]), "name": r["name"]}
        V[f"{a}v{j}"] = [{"id": G("ProductOptionValue", k), "name": n} for k, n in r.get("vals", {}).items()]
        body.append(f"{a}r{j}: productOptionUpdate(productId: ${a}id, option: ${a}r{j}, optionValuesToUpdate: ${a}v{j}) {{ userErrors {{ field message }} }}")
    doc_vars.append(f"${a}p: [ProductVariantsBulkInput!]!")
    V[a+"p"] = [{"id": G("ProductVariant", k), "price": pr, "compareAtPrice": None} for k, pr in s["price"].items()]
    body.append(f"{a}u: productVariantsBulkUpdate(productId: ${a}id, variants: ${a}p) {{ productVariants {{ title price }} userErrors {{ field message }} }}")
    doc_vars += [f"${a}rm: [FileUpdateInput!]!", f"${a}add: [FileUpdateInput!]!"]
    V[a+"rm"] = [{"id": G("MediaImage", x), "referencesToRemove": [pid]} for x in s["rm"]]
    V[a+"add"] = [{"id": G("MediaImage", s["add"][m[len(h)+1:-4]]), "alt": p["alts"][m], "referencesToAdd": [pid]} for m in p["media"]]
    body.append(f"{a}m: fileUpdate(files: ${a}rm) {{ userErrors {{ field message }} }}")
    body.append(f"{a}a: fileUpdate(files: ${a}add) {{ userErrors {{ field message }} }}")
    doc_vars.insert(0, f"${a}id: ID!")
doc = "mutation S(" + ", ".join(doc_vars) + ") { " + " ".join(body) + " }"
print(doc); print("=====")
print(json.dumps(V, ensure_ascii=False))
