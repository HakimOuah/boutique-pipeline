import json,re,glob,sys
TR="/Users/Hakim/.claude/projects/-Users-Hakim-Documents-Boutiques-drop/f13db31b-0454-40da-9b2d-d09781f8f692/tool-results/"
ROOT="/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/boutique-carport/"
R=[
 # réassurance standard
 (r"Garantie légale de conformité 2 ans, service client français, réponse sous 1 jour ouvré, conseil avant et après l'achat\.", "Garantie légale de conformité 2 ans, guides déclaration et montage offerts."),
 (r"Garantie légale de conformité 2 ans, service client français, réponse sous 1 jour ouvré, guide de montage et d'ancrage offert\.", "Garantie légale de conformité 2 ans, guide de montage et d'ancrage offert."),
 (r"Garantie légale de conformité 2 ans, garantie fabricant 1 an, service client français, réponse sous 1 jour ouvré\.", "Garantie légale de conformité 2 ans, garantie fabricant 1 an, guides déclaration et montage offerts."),
 (r"Garantie légale de conformité 2 ans, service client français, réponse sous 1 jour ouvré\.", "Garantie légale de conformité 2 ans, guides déclaration et montage offerts."),
 (r"Garantie légale de conformité 2 ans, service client français, réponse sous 1 jour ouvré", "Garantie légale de conformité 2 ans, rétractation 14 jours"),
 (r"Guides déclaration et montage offerts, conseil avant et après l'achat", "Guides déclaration et montage offerts, kit d'ancrage compris"),
 (r"Guides déclaration mairie et montage offerts, conseil par une vraie personne avant et après l'achat", "Guides déclaration mairie et montage offerts, kit d'ancrage compris"),
 # accueil / thème
 (r"Livraison offerte en France métropolitaine, guides déclaration et montage offerts, conseil par une vraie personne avant et après l'achat\.", "Livraison offerte en France métropolitaine, kits complets avec ancrage, guides déclaration et montage offerts."),
 (r"Nos guides déclaration et montage sont offerts, et une vraie personne vous conseille avant comme après l'achat\.", "Nos guides déclaration et montage sont offerts, et chaque kit arrive complet, ancrage compris."),
 (r"la livraison est offerte sur rendez-vous, et une vraie personne vous conseille avant comme après l'achat\.", "la livraison est offerte sur rendez-vous, et chaque kit arrive complet, ancrage compris."),
 (r"<li><strong>Le conseil d'une vraie personne</strong> : avant l'achat pour choisir, après pour monter, réponse sous 1 jour ouvré\.</li>", "<li><strong>Un kit complet</strong> : structure, toile ou toiture, kit d'ancrage et notice, rien à racheter.</li>"),
 (r"\*\*Carte 4 — Le conseil d'une vraie personne\*\* Avant l'achat pour choisir le bon modèle, après pour le monter\. Service client français, réponse sous 1 jour ouvré\.", "**Carte 4 — Un kit complet** Structure, toile ou toiture, kit d'ancrage et notice : rien à racheter."),
 (r"Conseil par une vraie personne avant et après l'achat", "Cotes et hauteur de passage vérifiées pour votre véhicule"),
 (r"Sélection vérifiée, livraison offerte sur rendez-vous, conseil par une vraie personne", "Sélection vérifiée, livraison offerte sur rendez-vous, kit d'ancrage compris"),
 (r"Montage et ancrage expliqués, conseil par une vraie personne", "Montage et ancrage expliqués, guide offert"),
 (r"Une question \? Conseil par une vraie personne, réponse sous 1 jour ouvré", "Guides déclaration en mairie et montage offerts"),
 (r"Réponse sous 1 jour ouvré : service client français, du lundi au vendredi, par une personne qui connaît ces abris", "Kit complet, prêt à monter : structure, toile ou toiture, kit d'ancrage et notice dans les colis"),
 (r"<p>Service client français, du lundi au vendredi, par une personne qui connaît ces abris\.</p>", "<p>Structure, toile ou toiture, kit d'ancrage et notice dans les colis. Guides déclaration et montage offerts.</p>"),
 (r"<p>Service client français, du lundi au vendredi\.</p>", "<p>Structure, toile ou toiture, kit d'ancrage et notice dans les colis. Guides déclaration et montage offerts.</p>"),
 (r"Livraison offerte, guides déclaration et montage offerts, et une vraie personne pour vous conseiller avant comme après l'achat\.", "Livraison offerte, guides déclaration et montage offerts, kit d'ancrage compris."),
 (r"La différence se joue dans la sélection des modèles et dans l'accompagnement autour de l'abri\.", "La différence se joue dans la sélection des modèles et dans ce qui arrive avec l'abri : kit d'ancrage, guides, livraison sur rendez-vous."),
 (r"Le spécialiste qui vous accompagne, du choix au montage", "Le spécialiste qui pense à tout, du choix au montage"),
 # fiches produit
 (r"les guides déclaration et montage sont offerts, et une vraie personne vous répond sous 1 jour ouvré, avant comme après l'achat\.", "les guides déclaration et montage sont offerts, et le kit d'ancrage est compris."),
 (r"les guides déclaration et montage sont offerts, et une vraie personne vous aide à vérifier la compatibilité de votre véhicule, avant comme après l'achat\.", "les guides déclaration et montage sont offerts, et la fiche donne la hauteur de passage pour vérifier la compatibilité de votre véhicule."),
 (r"vous recevez les guides déclaration et montage, et une vraie personne vous répond sous 1 jour ouvré, avant comme après l'achat\.", "vous recevez les guides déclaration et montage, et le kit d'ancrage est compris."),
 (r"La sélection et l'accompagnement : chaque modèle", "La sélection et le kit : chaque modèle"),
 (r"Notre guide de montage offert complète la notice, et notre service client répond à vos questions avant comme après l'achat\.", "Notre guide de montage offert complète la notice avec l'ordre des étapes et les points de contrôle avant de tendre la toile."),
 (r"Le guide de montage offert complète la notice avec l'ordre des étapes que nous conseillons, et notre équipe répond à vos questions avant et pendant le montage\.", "Le guide de montage offert complète la notice avec l'ordre des étapes que nous conseillons et les points de contrôle avant de poser la toiture."),
 (r"Le guide de montage offert complète la notice, et notre équipe répond à vos questions pendant le montage\.", "Le guide de montage offert complète la notice avec l'ordre des étapes et les points de contrôle."),
 (r"Le guide de montage offert détaille l'ordre des étapes,? et notre équipe vous répond pendant le montage\.", "Le guide de montage offert détaille l'ordre des étapes et les points de contrôle avant la fixation définitive."),
 (r"La notice du fabricant guide chaque étape, et notre conseiller reste joignable par e-mail avant, pendant et après le montage\.", "La notice du fabricant guide chaque étape, et notre guide de montage offert ajoute l'ordre conseillé et les points de contrôle."),
 (r"notre service client vous indique la marche à suivre sous 1 jour ouvré", "la marche à suivre est détaillée dans notre politique de retour"),
 (r"\s*Notre service client français vous répond sous 1 jour ouvré\.", ""),
 (r"avant de commander, notre équipe vous répond sous 1 jour ouvré\.", "avant de commander : toutes les cotes utiles figurent sur cette fiche."),
 (r"avant de commander, notre équipe vous aide à le faire\.", "avant de commander : toutes les cotes utiles figurent sur cette fiche."),
 # pages
 (r"La garantie légale de conformité de 2 ans couvre tout le catalogue, et notre service client français vous répond sous 1 jour ouvré\.", "La garantie légale de conformité de 2 ans couvre tout le catalogue."),
 (r"pièce manquante renvoyée à nos frais, garantie légale de conformité de 2 ans et un service client français qui vous répond sous 1 jour ouvré\.", "pièce manquante renvoyée à nos frais et garantie légale de conformité de 2 ans."),
 (r"Une question sur les cotes d'un modèle avant de déposer votre dossier \? Notre conseiller vous répond sous 1 jour ouvré\.", "Les cotes exactes de chaque modèle figurent sur sa fiche, pour remplir votre dossier sans erreur."),
 (r"Pour tout ce qui concerne votre modèle, ses cotes ou son kit d'ancrage, notre conseiller vous répond sous 1 jour ouvré, avant et après l'achat\.", "Pour votre modèle, les cotes et le contenu du kit d'ancrage figurent sur sa fiche."),
 (r"Un service client français qui vous répond sous 1 jour ouvré, du lundi au vendredi, par e-mail ou téléphone, avant et après l'achat\.", "Un service client joignable par e-mail et par téléphone, du lundi au vendredi."),
 (r"un guide de montage détaillé et un conseiller joignable avant comme après l'achat : c'est ce qui distingue", "un guide de montage détaillé et une hauteur de passage vérifiée : c'est ce qui distingue"),
 (r"Nos guides déclaration et montage vous donnent les réponses, et notre conseiller vérifie vos cotes avec vous avant la commande\.", "Nos guides déclaration et montage vous donnent les réponses, et chaque fiche indique les cotes à vérifier avant la commande."),
 # contact (on garde le délai, sans « nous-mêmes » ni « conseiller qui connaît »)
 (r"Nous répondons nous-mêmes, sous 1 jour ouvré, du lundi au vendredi\.", "Réponse sous 1 jour ouvré, du lundi au vendredi."),
 (r"Un conseiller qui connaît chaque modèle du catalogue vous répond sous 1 jour ouvré, du lundi au vendredi, avant comme après l'achat\.", "Réponse sous 1 jour ouvré, du lundi au vendredi."),
 (r"un conseiller vous répond sous 1 jour ouvré, du lundi au vendredi\.", "réponse sous 1 jour ouvré, du lundi au vendredi."),
 (r"Conseil avant et après l'achat, guides déclaration et montage offerts", "Guides déclaration et montage offerts"),
 (r"^Réponse sous 1 jour ouvré$", "Kit complet, prêt à monter"),
 (r"\*\*Carte 4 — Le conseil d'une vraie personne\*\*\s+Avant l'achat pour choisir le bon modèle, après pour le monter\. Service client français, réponse sous 1 jour ouvré\.", "**Carte 4 — Un kit complet**\nStructure, toile ou toiture, kit d'ancrage et notice : rien à racheter."),
 (r"dans l'accompagnement autour de votre abri\.", "dans ce qui arrive avec votre abri : kit d'ancrage, guides, livraison sur rendez-vous."),
 (r"La sélection et l'accompagnement\. Nous avons vérifié", "La sélection et le kit. Nous avons vérifié"),
 (r"avec la notice du fabricant et notre accompagnement par e-mail", "avec la notice du fabricant et notre guide de montage offert"),
 (r"Notre service client français vous répond sous (<strong>|\*\*)1 jour ouvré(</strong>|\*\*), du lundi au vendredi, par e-mail et par téléphone, avant comme après l'achat\.", r"Réponse sous \g<1>1 jour ouvré\g<2>, du lundi au vendredi, par e-mail et par téléphone."),
 (r"est prévu pour cela, et notre service client vous répond sous 1 jour ouvré\.", "est prévu pour cela."),
 (r"3\. Réponse sous 1 jour ouvré, du lundi au vendredi", "3. Guides déclaration en mairie et montage offerts"),
]
PAT=re.compile(r"vraie personne|une personne qui|personne qui conna|répond(?:ons|re)? sous 1 jour|réponse sous 1 jour|sous 1 jour ouvré|service client|conseil(?:lé|ler|s)? par|un conseiller|notre conseiller|vous répond|nous vous répondons|avant et après l'achat|avant comme après l'achat|notre équipe|pendant le montage|accompagnement|nous-mêmes",re.I)
stats={}
def apply(t,label):
    for pat,rep in R:
        t,n=re.subn(pat,rep,t)
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
    for m in PAT.finditer(t):
        resid.append((label,re.sub(r"<[^>]+>"," ",t[max(0,m.start()-100):m.end()+80]).replace("\n"," ")))
mode=sys.argv[1] if len(sys.argv)>1 else "dry"
# 1. thème local
for f in glob.glob(ROOT+"shopify/theme-sousabri/work/templates/*.json")+glob.glob(ROOT+"shopify/theme-sousabri/work/sections/*.json"):
    if f.endswith(".min"): continue
    o=json.load(open(f,encoding="utf-8")); o2=walk(json.loads(json.dumps(o)),lambda s:apply(s,"theme:"+f.split("/")[-1]))
    s=json.dumps(o2,ensure_ascii=False); check("theme:"+f.split("/")[-1],s)
    if mode=="write" and o2!=o:
        open(f,"w",encoding="utf-8").write(json.dumps(o2,ensure_ascii=False,indent=2)+"\n"); open(f+".min","w",encoding="utf-8").write(json.dumps(o2,ensure_ascii=False,separators=(',',':')))
# 2. md locaux
for f in glob.glob(ROOT+"content/pages/*.md")+glob.glob(ROOT+"content/collections/*.md")+glob.glob(ROOT+"content/produits/*.md"):
    t=open(f,encoding="utf-8").read(); t2=apply(t,"md:"+f.split("/")[-1]); check("md:"+f.split("/")[-1],t2)
    if mode=="write" and t2!=t: open(f,"w",encoding="utf-8").write(t2)
# 3. live
pages=json.load(open(TR+"mcp-d36aaeec-0029-4c8b-86fc-f67976ed2f55-graphql_query-1789510689911.txt"))["data"]["pages"]["nodes"]
cp=json.load(open(TR+"mcp-d36aaeec-0029-4c8b-86fc-f67976ed2f55-graphql_query-1789510728170.txt"))["data"]
plan={"pages":[],"products":[],"metafields":[],"collections":[]}
for p in pages:
    b=p["body"] or ""; nb=apply(b,"page:"+p["handle"]); check("page:"+p["handle"],nb)
    if nb!=b: plan["pages"].append({"id":p["id"],"handle":p["handle"],"body":nb})
for pr in cp["products"]["nodes"]:
    b=pr["descriptionHtml"] or ""; nb=apply(b,"prod:"+pr["handle"]); check("prod:"+pr["handle"],nb)
    if nb!=b: plan["products"].append({"id":pr["id"],"handle":pr["handle"],"descriptionHtml":nb})
    for m in pr["metafields"]["nodes"]:
        v=m["value"]; nv=apply(v,"mf:"+pr["handle"]+":"+m["key"]); check("mf:"+pr["handle"]+":"+m["key"],nv)
        if nv!=v: plan["metafields"].append({"ownerId":pr["id"],"handle":pr["handle"],"namespace":"custom","key":m["key"],"type":m["type"],"value":nv})
for c in cp["collections"]["nodes"]:
    b=c["descriptionHtml"] or ""; nb=apply(b,"coll:"+c["handle"]); check("coll:"+c["handle"],nb)
    e={"id":c["id"],"handle":c["handle"]}
    if nb!=b: e["descriptionHtml"]=nb
    if c["m"]:
        v=c["m"]["value"]; nv=apply(v,"seo:"+c["handle"]); check("seo:"+c["handle"],nv)
        if nv!=v: plan["metafields"].append({"ownerId":c["id"],"handle":c["handle"],"namespace":"custom","key":"texte_seo","type":c["m"]["type"],"value":nv})
    if "descriptionHtml" in e: plan["collections"].append(e)
if mode=="write": json.dump(plan,open("plan-copy-personne.json","w"),ensure_ascii=False,indent=1)
print(json.dumps(stats,ensure_ascii=False,indent=0)); print("plan:",{k:len(v) for k,v in plan.items()})
print("\nRESIDUS",len(resid)); 
for l,s in resid: print(l,"::",s)
