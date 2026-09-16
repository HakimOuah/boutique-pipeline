import json,re,glob,sys
TR="/Users/Hakim/.claude/projects/-Users-Hakim-Documents-Boutiques-drop/f13db31b-0454-40da-9b2d-d09781f8f692/tool-results/"
ROOT="/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/boutique-carport/"
QSN_HTML=("<h2>Ce qui fait la différence</h2>\n<ul>\n"
 "<li>Un abri complet au prix d'un kit : structure, toile ou toiture, ancrage et notice arrivent ensemble, sans chantier ni devis d'artisan.</li>\n"
 "<li>Des modèles choisis chez des fabricants partenaires et vérifiés un par un : cotes, kit d'ancrage et contenu des colis.</li>\n"
 "<li>Des démarches balisées : nos guides déclaration et montage donnent les seuils, les pièces à fournir et l'ordre de montage.</li>\n</ul>")
QSN_MD=("## Ce qui fait la différence\n\n"
 "- Un abri complet au prix d'un kit : structure, toile ou toiture, ancrage et notice arrivent ensemble, sans chantier ni devis d'artisan.\n"
 "- Des modèles choisis chez des fabricants partenaires et vérifiés un par un : cotes, kit d'ancrage et contenu des colis.\n"
 "- Des démarches balisées : nos guides déclaration et montage donnent les seuils, les pièces à fournir et l'ordre de montage.\n")
R=[
 # 1. qui sommes nous
 (r"<h2>Ce que nous ne promettons pas</h2>\s*<ul>.*?</ul>", QSN_HTML),
 (r"## Ce que nous ne promettons pas\n\n(?:- [^\n]*\n)+", QSN_MD),
 (r"Des visuels fidèles au produit livré, composés à partir des photos réelles du fabricant\.", "Des visuels fidèles au produit livré."),
 # 2. titres confessionnels (corps HTML + md)
 (r"<h3>Le montage, honnêtement</h3>", "<h3>Le montage</h3>"),
 (r"<h3>Ce qu'il ne fait pas</h3>", "<h3>Bon à savoir</h3>"),
 (r"### Le montage, honnêtement", "### Le montage"),
 (r"### Ce qu'il ne fait pas", "### Bon à savoir"),
 # 3. injonctions mairie
 (r"\s*Conseil pratique : passez au service urbanisme de votre mairie avec un plan coté de votre terrain avant de commander ; il vous confirmera la procédure et la distance à respecter par rapport aux limites de propriété, souvent 3 m selon le PLU(?:, un point à anticiper pour un abri de cette longueur)?\.", ""),
 (r"Notre guide déclaration offert vous accompagne pas à pas ; confirmez la procédure auprès du service urbanisme de votre mairie avant de commander\.", "Notre guide déclaration offert vous accompagne pas à pas, du formulaire aux pièces à joindre."),
 (r"Notre conseil : passez par le service urbanisme de votre mairie avant de commander, il confirme les règles propres à votre commune ; le guide déclaration offert", "Le guide déclaration offert"),
 (r"Le guide déclaration offert liste les pièces à joindre ; passez par le service urbanisme de votre mairie avant de commander pour confirmer les règles de distance\.", "Le guide déclaration offert liste les pièces à joindre et vous accompagne étape par étape."),
 (r"(Le guide déclaration offert(?:, disponible en ligne,)? vous accompagne étape par étape), et le service urbanisme de votre mairie confirme les règles propres à votre commune\.", r"\1."),
 (r"Expédié depuis la Pologne, il est livré en 5 à 12 jours ouvrés", "Livré en 5 à 12 jours ouvrés depuis un stock européen"),
 (r"expédiées depuis la France ou l'Allemagne en 5 à 12 jours ouvrés", "livrées en 5 à 12 jours ouvrés depuis nos stocks européens"),
 (r" et confirmez les règles de distance auprès du service urbanisme de votre mairie\.", "."),
 (r"\s*[Cc]onfirmez les règles de distance auprès du service urbanisme de votre mairie\.", ""),
 (r"Notre conseil : passez par le service urbanisme de votre mairie avant de valider la commande, le carport étant fabriqué à vos coloris, puis instruisez le dossier pendant les 4 à 8 semaines de fabrication\.", "Le carport étant fabriqué à vos coloris, instruisez le dossier pendant les 4 à 8 semaines de fabrication : il est prêt quand l'abri arrive."),
 (r"Notre conseil : faites confirmer les règles de votre commune par le service urbanisme de la mairie avant de valider la commande, puis montez le dossier pendant les 4 à 8 semaines de fabrication\.", "Montez le dossier pendant les 4 à 8 semaines de fabrication : il est prêt quand l'abri arrive."),
 (r"Confirmez le seuil applicable[^;]*auprès de votre mairie[^;]*; notre guide", "Notre guide"),
 (r"[Cc]onfirmez le seuil applicable auprès de votre mairie, notre guide", "Notre guide"),
 (r"Le service urbanisme de votre mairie vous indique en quelques minutes ce que prévoit le PLU pour votre parcelle : c'est le premier appel à passer, avant de commander\.", "Le PLU de votre commune se consulte en ligne ou en mairie en quelques minutes."),
 (r"Un doute sur vos cotes \? Écrivez-nous avant de commander, nous vérifions avec vous\.", "Les cotes intérieures et la hauteur de passage figurent sur chaque fiche."),
 (r"Si votre emplacement est mesuré au centimètre près, envoyez-nous un croquis avant de commander : nous vérifions avec vous que tout passe\.", "Les cotes extérieures et intérieures figurent sur cette fiche, débords compris."),
 (r" ; en cas de doute, envoyez-nous le modèle(?: de votre véhicule)?, nous vérifions avec vous\.", "."),
 # 4. coulisses
 (r"depuis nos stocks en France, en Allemagne ou en Pologne", "depuis nos stocks européens"),
 (r"\(stock France, Allemagne, Pologne\)", "(stock européen)"),
 (r"Le plus rapide du catalogue : expédié depuis l'Europe, livré en 5 colis sous 5 à 12 jours ouvrés", "Livré en 5 colis sous 5 à 12 jours ouvrés, depuis un stock européen"),
 (r"Ce modèle est expédié depuis un stock européen, en Pologne : c'est le plus rapide du catalogue, livré en 5 à 12 jours ouvrés\.", "Ce modèle part d'un stock européen et arrive sous 5 à 12 jours ouvrés."),
 (r"2\. Pourquoi la livraison est-elle plus rapide que les autres carports du catalogue \?(</strong>|\*\*|</summary>\s*<p>)\s*Il part d'un stock situé en Europe \(Pologne\), là où les carports aluminium sont fabriqués à la commande\. Comptez 5 à 12 jours ouvrés entre la commande et la livraison\.", r"2. Quel est le délai de livraison ?\1\nIl part d'un stock européen : comptez 5 à 12 jours ouvrés entre la commande et la livraison, offerte et sur rendez-vous."),
 (r"Délai 5 à 12 jours ouvrés, expédié depuis l'Europe", "Délai 5 à 12 jours ouvrés, stock européen"),
 (r"5 à 12 jours ouvrés, expédié depuis l'Europe", "5 à 12 jours ouvrés, stock européen"),
 (r"expédié depuis l'Europe en 5 à 12 jours ouvrés", "livré en 5 à 12 jours ouvrés depuis un stock européen"),
 (r"expédié depuis l'Europe, livré en 5 colis", "livré en 5 colis depuis un stock européen"),
 # 5. frais de retour sur fiche
 (r"Les frais de retour d'un colis volumineux restent à votre charge ; la marche à suivre est détaillée dans notre politique de retour\.", "La marche à suivre est détaillée dans notre politique de retour."),
]
PAT=re.compile(r"honnêtement|ne promettons|ne fait pas</h3>|ne fait pas\n|composés à partir|Pologne|France ou l'Allemagne|plus rapide du catalogue|plus rapide que les autres|service urbanisme de votre mairie (?:avant|confirme|vous le)|avant de commander|nous vérifions avec vous|restent à votre charge|expédié depuis l'Europe",re.I)
stats={}
def apply(t,label):
    for pat,rep in R:
        t,n=re.subn(pat,rep,t,flags=re.S)
        if n: stats[label]=stats.get(label,0)+n
    return t
def walk(o,fn):
    if isinstance(o,dict):
        for k in o: o[k]=walk(o[k],fn)
    elif isinstance(o,list): return [walk(x,fn) for x in o]
    elif isinstance(o,str): return fn(o)
    return o
resid=[]
def check(label,t):
    for m in PAT.finditer(t or ""):
        resid.append((label,re.sub(r"<[^>]+>"," ",t[max(0,m.start()-90):m.end()+70]).replace("\n"," ")))
mode=sys.argv[1] if len(sys.argv)>1 else "dry"
for f in glob.glob(ROOT+"shopify/theme-sousabri/work/templates/*.json")+glob.glob(ROOT+"shopify/theme-sousabri/work/sections/*.json"):
    if f.endswith(".min"): continue
    o=json.load(open(f,encoding="utf-8")); o2=walk(json.loads(json.dumps(o)),lambda s:apply(s,"theme:"+f.split("/")[-1]))
    check("theme:"+f.split("/")[-1],json.dumps(o2,ensure_ascii=False))
    if mode=="write" and o2!=o:
        open(f,"w",encoding="utf-8").write(json.dumps(o2,ensure_ascii=False,indent=2)+"\n"); open(f+".min","w",encoding="utf-8").write(json.dumps(o2,ensure_ascii=False,separators=(',',':')))
for f in glob.glob(ROOT+"content/pages/*.md")+glob.glob(ROOT+"content/collections/*.md")+glob.glob(ROOT+"content/produits/*.md"):
    t=open(f,encoding="utf-8").read(); t2=apply(t,"md:"+f.split("/")[-1]); check("md:"+f.split("/")[-1],t2)
    if mode=="write" and t2!=t: open(f,"w",encoding="utf-8").write(t2)
if mode=="write":
    b=ROOT+"shopify/build_metafields.py"; s=open(b,encoding="utf-8").read().replace('"Le montage, honnêtement"','"Le montage"').replace('"Ce qu\'il ne fait pas"','"Bon à savoir"'); open(b,"w",encoding="utf-8").write(s)
d=json.load(open(TR+"mcp-d36aaeec-0029-4c8b-86fc-f67976ed2f55-graphql_query-1789511635458.txt"))["data"]
_p=json.load(open(TR+"mcp-d36aaeec-0029-4c8b-86fc-f67976ed2f55-graphql_query-1789510689911.txt"))["data"]["pages"]["nodes"]
_c=json.load(open(TR+"mcp-d36aaeec-0029-4c8b-86fc-f67976ed2f55-graphql_query-1789510728170.txt"))["data"]
IDS={**{"page:"+x["handle"]:x["id"] for x in _p},**{"prod:"+x["handle"]:x["id"] for x in _c["products"]["nodes"]},**{"coll:"+x["handle"]:x["id"] for x in _c["collections"]["nodes"]}}
for x in d["pages"]["nodes"]: x["id"]=IDS["page:"+x["handle"]]
for x in d["products"]["nodes"]: x["id"]=IDS["prod:"+x["handle"]]
for x in d["collections"]["nodes"]: x["id"]=IDS["coll:"+x["handle"]]
TYPES={}
for x in _c["products"]["nodes"]:
    for m in x["metafields"]["nodes"]: TYPES[(x["handle"],m["key"])]=m["type"]
for x in _c["collections"]["nodes"]:
    if x["m"]: TYPES[(x["handle"],"texte_seo")]=x["m"]["type"]
for x in d["products"]["nodes"]:
    for m in x["metafields"]["nodes"]: m["type"]=TYPES[(x["handle"],m["key"])]
for x in d["collections"]["nodes"]:
    if x["m"]: x["m"]["type"]=TYPES[(x["handle"],"texte_seo")]
plan={"pages":[],"products":[],"metafields":[],"collections":[]}
for p in d["pages"]["nodes"]:
    b=p["body"] or ""; nb=apply(b,"page:"+p["handle"]); check("page:"+p["handle"],nb)
    if nb!=b: plan["pages"].append({"id":p["id"],"handle":p["handle"],"body":nb})
for pr in d["products"]["nodes"]:
    b=pr["descriptionHtml"] or ""; nb=apply(b,"prod:"+pr["handle"]); check("prod:"+pr["handle"],nb)
    if nb!=b: plan["products"].append({"id":pr["id"],"handle":pr["handle"],"descriptionHtml":nb})
    for m in pr["metafields"]["nodes"]:
        v=m["value"]; nv=apply(v,"mf:"+pr["handle"]+":"+m["key"]); check("mf:"+pr["handle"]+":"+m["key"],nv)
        if nv!=v: plan["metafields"].append({"ownerId":pr["id"],"handle":pr["handle"],"namespace":"custom","key":m["key"],"type":m["type"],"value":nv})
for c in d["collections"]["nodes"]:
    b=c["descriptionHtml"] or ""; nb=apply(b,"coll:"+c["handle"]); check("coll:"+c["handle"],nb)
    if nb!=b: plan["collections"].append({"id":c["id"],"handle":c["handle"],"descriptionHtml":nb})
    if c["m"]:
        v=c["m"]["value"]; nv=apply(v,"seo:"+c["handle"]); check("seo:"+c["handle"],nv)
        if nv!=v: plan["metafields"].append({"ownerId":c["id"],"handle":c["handle"],"namespace":"custom","key":"texte_seo","type":c["m"]["type"],"value":nv})
if mode=="write": json.dump(plan,open("plan-copy-transparence.json","w"),ensure_ascii=False,indent=1)
print(json.dumps(stats,ensure_ascii=False)); print("plan:",{k:len(v) for k,v in plan.items()})
print("\nRESIDUS",len(resid))
for l,s in resid: print(l,"::",s)
