import json,sys
P=json.load(open("products-payload.json")); G=json.load(open("desc-groups.json"))
g=G[int(sys.argv[1])]
print(json.dumps({f"p{i}":{"id":P[h]["shopify_id"],"title":P[h]["title"],"handle":h,"descriptionHtml":P[h]["descriptionHtml"].replace("\n",""),"seo":P[h]["seo"],"productType":P[h]["productType"],"vendor":"Bercelou","tags":P[h]["tags"]} for i,h in enumerate(g)},ensure_ascii=False))
