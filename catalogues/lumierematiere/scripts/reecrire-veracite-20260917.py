import json,re,html
mf=json.load(open('/tmp/lmfix/metafields.json',encoding='utf-8'))
live={p['handle']:p for p in json.load(open('/tmp/lmaudit/products.json'))['products']}
A="’"  # apostrophe typographique du catalogue

# --- phrases entières à remplacer ou retirer (ordre = priorité) ---
PH=[
 # jargon / confessionnel
 (r" ?Le fournisseur écrit parfois « waterproof » sur une photo : aucun indice de protection n’est lisible, on ne reprend pas cette mention\.", " Aucun indice de protection contre l’eau : intérieur et pièces sèches uniquement."),
 (r"Non\. Certaines photos fournisseur portent le mot waterproof : aucun indice de protection n’est lisible dans les attributs\. Intérieur et pièces sèches uniquement\.", "Non. Cette applique ne porte aucun indice de protection contre l’eau. Intérieur et pièces sèches uniquement."),
 (r" ?Le fournisseur la montre au-dessus d’un lavabo, nous ne reprenons pas cette promesse\.", ""),
 (r" ?Une photo fournisseur annonce parfois une ampoule offerte : l’attribut dit non, on promet le moins\.", ""),
 (r"Non\. L’attribut fournisseur dit ampoule non incluse\. Une photo de variante annonce parfois 1 LED offerte : nous ne reprenons pas cette mention\. ", "Non. "),
 (r"Du verre\. L’attribut fournisseur dit parfois « pierre de verre » : les photos montrent un verre laqué et une boule dépolie, pas un bloc de pierre\.", "Du verre : un disque laqué et une boule dépolie."),
 # garanties de matière
 (r"\{\"q\":\"C’est de la vraie pierre \?\",\"a\":\"[^\"]*\"\},?", ""),
 (r"\"title\":\"Du travertin, pas un placage\",\"body\":\"Les deux disques sont taillés dans la pierre\. ", "\"title\":\"Un aspect travertin\",\"body\":\"Les deux têtes reprennent le grain du travertin. "),
 (r"Les nuances et les petits creux propres au travertin se voient de près", "Les nuances et les petits creux se voient de près"),
 (r"Les creux du travertin sont ceux de la pierre, ils diffèrent d’une pièce à l’autre", "Les creux et les nuances diffèrent d’une pièce à l’autre"),
 # fabrication
 (r"L’émail est appliqué à la main, le liseré n’est jamais parfaitement régulier", "Le liseré n’est jamais parfaitement régulier d’une pièce à l’autre"),
 (r"De la corde de chanvre tressée à la main", "De la corde tressée"),
 (r"c’est le propre du tressage à la main", "c’est le propre du tressage"),
 (r"Le soufflage laisse des irrégularités dans l’épaisseur", "Le verre présente de légères irrégularités d’épaisseur"),
 # délai : qui prépare, d'où ça part
 (r"On prépare le colis en 1 à 2 jours ouvrés, l’acheminement prend 6 à 16 jours ouvrés", "La commande est préparée en 1 à 2 jours ouvrés puis expédiée depuis l’entrepôt de notre fabricant partenaire, en Chine ; l’acheminement prend 6 à 16 jours ouvrés"),
 # retours : vers où
 (r"S’il s’agit d’un simple changement d’avis, les frais de retour sont à votre charge", "S’il s’agit d’un simple changement d’avis, le retour se fait vers une adresse en France et ses frais sont à votre charge"),
]
# --- expressions de matière (après les phrases) ---
EX=[
 # pierre / travertin
 (r"Bloc de pierre 16 cm","Bloc effet pierre 16 cm"),(r"Travertin plein","Aspect travertin"),(r"Pierre pleine","Aspect pierre"),
 (r"Pierre translucide","Effet pierre translucide"),(r"\"Travertin et bois\"","\"Effet travertin et bois\""),(r"\"Pierre et bois\"","\"Effet pierre et bois\""),
 (r"Applique murale cubique en pierre","Applique murale cubique effet pierre"),(r"Applique murale double en travertin","Applique murale double effet travertin"),
 (r"Applique murale en pierre","Applique murale effet pierre"),(r"Applique liseuse en pierre sur bras de bois","Applique liseuse effet pierre sur bras de bois"),
 (r"Suspension pierre translucide","Suspension effet pierre translucide"),
 (r"pierre beige à ocre, platine métal ou bois","aspect pierre beige à ocre, platine métal ou bois"),
 (r"travertin beige, platine bois","aspect travertin beige, platine bois"),
 (r"pierre beige à ocre, corps plein","aspect pierre beige à ocre"),
 (r"pierre beige et bras en bois","aspect pierre beige, bras en bois"),
 (r"pierre claire translucide et tige brune","aspect pierre claire translucide, tige brune"),
 (r"Matière :</strong> travertin et bois foncé","Matière :</strong> composite effet travertin et bois foncé"),
 (r"Matière :</strong> travertin et bois","Matière :</strong> composite effet travertin et bois"),
 (r"perles de pierre et bois","perles effet pierre et bois"),
 (r"Un bloc de pierre taillé droit","Un bloc à l’aspect de pierre, taillé droit"),
 (r"le bloc de pierre vient par-dessus","le bloc vient par-dessus"),
 (r"C’est la platine qui change, pas la pierre","C’est la platine qui change, pas le bloc"),
 (r"C’est la platine qui change, la pierre reste la même","C’est la platine qui change, les têtes restent les mêmes"),
 (r"Deux têtes rondes en travertin","Deux têtes rondes effet travertin"),
 (r"La pierre est creusée en galet et posée","Le corps effet pierre est creusé en galet et posé"),(r"La pierre est creusée en galet","Le corps effet pierre est creusé en galet"),
 (r"Les veines de la pierre changent","Les nuances changent"),
 (r"La lumière sort de la pierre","La lumière sort du galet"),(r"la tranche de pierre s’allumer","la tranche du galet s’allumer"),
 (r"Chaque pierre est différente","Chaque pièce est différente"),
 (r"Le disque de pierre est monté","Le disque effet pierre est monté"),(r"le disque de pierre dirige","le disque dirige"),
 (r"La pierre, elle, ne change pas","Le disque, lui, ne change pas"),(r"C’est le bras qui change, pas la pierre","C’est le bras qui change, pas le disque"),
 (r"Un cylindre en travertin","Un cylindre effet travertin"),
 (r"un chiffon doux sur la pierre","un chiffon doux sur le corps"),
 (r"Deux perles de pierre claire","Deux perles effet pierre claire"),
 (r"Le veinage de la pierre change","Le veinage change"),
 (r"Ce que la pierre fait à la lumière","Ce que la matière fait à la lumière"),
 (r"La pierre porte ses creux et ses veines","Le corps porte des creux et des veines"),
 (r"La pierre est taillée assez fine","Le cylindre est assez fin"),
 (r"Un cylindre de pierre claire assez fine","Un cylindre effet pierre claire, assez fin"),
 (r"Allumée, la pierre devient laiteuse","Allumée, la matière devient laiteuse"),
 (r"La lumière passe dans la pierre","La lumière passe dans la matière"),
 (r"Les nuances de la pierre ne se répètent pas","Les nuances ne se répètent pas"),
 # laiton
 (r"Matière :</strong> laiton","Matière :</strong> métal, finition dorée ou noire"),
 (r"Lustre laiton à bougies","Lustre à bras bougies"),(r"\"Laiton\"","\"Doré ou noir\""),
 (r"céramique plissée et laiton","céramique plissée et métal doré"),(r"céramique gaufrée et laiton","céramique gaufrée et métal doré"),
 (r"céramique peinte et laiton","céramique peinte et métal doré"),(r"métal noir et laiton","métal noir et doré"),
 (r"Des bras de laiton courbés","Des bras de métal courbés"),(r"un chiffon doux sur le laiton","un chiffon doux sur le métal"),
 (r"Du laiton, sur des bras courbés","Du métal doré ou noir, sur des bras courbés"),
 (r"des douilles en laiton","des douilles dorées"),(r"sur une douille en laiton","sur une douille dorée"),
 (r"sur une monture en laiton","sur une monture dorée"),(r"La douille en laiton porte","La douille dorée porte"),
 (r"une douille et une rosace en laiton","une douille et une rosace dorées"),
 # cuivre
 (r"céramique émaillée, cuivre et bois","céramique émaillée, métal cuivré et bois"),(r"monture cuivre et bois","monture cuivrée et bois"),
 (r"finition cuivre ou chrome","finition cuivrée ou chromée"),(r"cuivre ou chrome","cuivré ou chromé"),(r"Cuivre et Chromé","Cuivré et Chromé"),
 # soie
 (r"\"Soie tendue\"","\"Tissu plissé\""),(r"soie tendue sur armature","tissu plissé tendu sur armature"),
 (r"jamais d’eau sur la soie","jamais d’eau sur le tissu"),(r"De la soie tendue sur une armature","Un tissu plissé tendu sur une armature"),
 (r"La lumière traverse la soie","La lumière traverse le tissu"),(r"Suspension soucoupe en soie","Suspension soucoupe en tissu plissé"),
 # verre soufflé, chanvre
 (r"verre soufflé","verre"),(r"\"Corde de chanvre\"","\"Corde tressée\""),
 (r"Finitions au choix : pierre claire ou brun","Finitions au choix : clair ou brun"),
 (r"Teinte :</strong> Pierre claire et Brun","Teinte :</strong> Clair et Brun"),
 (r"Noyer · Ø","Teinte noyer · Ø"),
 (r"Ce <strong>plafonnier LED</strong> est fait pour les endroits où la hauteur manque","Ce <strong>plafonnier</strong> est fait pour les endroits où la hauteur manque"),
 (r"Ce <strong>plafonnier LED</strong> se plaque au plafond","Ce <strong>plafonnier</strong> se plaque au plafond"),
 # essence de bois employée comme teinte
 (r"\bou noyer\b","ou teinte noyer"),(r"Bois clair ou Noyer","Bois clair ou teinte noyer"),(r"Bois brut et Noyer","Bois brut et teinte noyer"),
 (r"clair ou noyer","clair ou teinte noyer"),(r"le noyer souligne","la teinte noyer souligne"),(r"le noyer tranche","la teinte noyer tranche"),
 (r"le noyer marque","la teinte noyer marque"),(r"\"Bois clair ou noyer \?\"","\"Bois clair ou teinte noyer ?\""),
]
def fix(s):
    for a,b in PH+EX: s=re.sub(a,b,s)
    s=s.replace("teinte teinte","teinte")
    s=re.sub(r",\]","]",s)
    return s

TITLES={
 "applique-double-travertin-474088":"Applique murale double effet travertin, 2 lumières",
 "applique-liseuse-pierre-311650":"Applique murale liseuse effet pierre et bois, chambre",
 "applique-murale-pierre-588683":"Applique murale galet beige effet pierre, chambre",
 "applique-murale-pierre-metal-147598":"Applique murale cubique beige effet pierre, chambre",
 "suspension-bois-193329":"Suspension cylindre effet travertin, tête bois clair ou foncé",
 "suspension-bois-led-245113":"Suspension cylindre effet travertin, anneau bois foncé",
 "suspension-bois-led-334133":"Suspension cuisine, perles effet pierre et boule opaline",
 "suspension-bois-led-934110":"Suspension effet travertin cuisine, un ou deux tubes",
 "suspension-effet-pierre-092465":"Suspension effet pierre claire, cylindre à tête bois brun",
 "suspension-effet-pierre-led-073999":"Suspension effet pierre cuisine, galet sur tige bois clair",
 "suspension-effet-pierre-led-147607":"Suspension effet travertin cuisine, monture bois foncé",
 "lustre-statement-led-noir-950316":"Lustre salon sputnik doré et noir, boules en verre",
 "suspension-deco-253182":"Suspension céramique émaillée, monture dorée",
 "suspension-deco-blanc-560098":"Suspension céramique cuisine, monture dorée",
 "suspension-deco-led-blanc-805304":"Suspension coupelle céramique blanche, câble torsadé",
 "suspension-metal-dore-037279":"Suspension dôme céramique gaufrée, monture dorée",
 "suspension-metal-led-dore-952116":"Suspension céramique bleu et blanc, douille à interrupteur",
 "suspension-metal-noir-dore-361680":"Lustre salle à manger à bras bougies, doré ou noir",
 "lustre-salon-blanc-246282":"Suspension soucoupe tissu plissé blanc, salon",
 "plafonnier-led-565566":"Plafonnier salon 6 boules verre sur tiges, chromé ou cuivré",
 "plafonnier-led-992600":"Plafonnier salon boules de verre sur tiges courbes",
 "lustre-anneau-led-led-134962":"Plafonnier LED anneaux entrelacés, blanc, noir ou doré",
 "suspension-verre-446435":"Suspension boule en verre, tige rigide noire",
 "suspension-bois-832012":"Suspension bois 3 gouttes de verre, fumé, ambre ou clair",
 "suspension-rotin-897170":"Suspension corolle de pétales, rotin ou fibre synthétique",
 "suspension-rotin-led-761433":"Suspension salon corolle de pétales tressés",
 "suspension-rotin-dore-435189":"Suspension en rotin tressé, forme cloche haute",
 "suspension-rotin-623305":"Suspension rotin tressé cuisine, trois formes d’abat-jour",
 "suspension-metal-led-dore-975417":"Suspension céramique blanche, cloche ou corolle, cordon doré",
}
plan={}
for h,p in live.items():
    new={}
    if h in TITLES and TITLES[h]!=p['title']: new['title']=TITLES[h]
    d=fix(p['body_html'] or '')
    if d!=(p['body_html'] or ''): new['descriptionHtml']=d
    for k,v in mf.get(h,{}).items():
        nv=fix(v)
        if nv!=v:
            if k in ('faq','benefits'): json.loads(nv)   # doit rester du JSON valide
            if k=='usps': json.loads(nv)
            new['mf.'+k]=nv
    if new: plan[h]=new
json.dump(plan,open('/tmp/lmfix/plan.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
from collections import Counter
c=Counter(k.split('.')[0] if k.startswith('mf.') else k for v in plan.values() for k in v)
print(len(plan),'fiches modifiées ;',dict(Counter(k for v in plan.values() for k in v)))
