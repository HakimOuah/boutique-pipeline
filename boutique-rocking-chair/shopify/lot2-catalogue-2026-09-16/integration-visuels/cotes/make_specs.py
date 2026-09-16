import json,sys
def L(v,c="auto"): return {"type":"l","valeur":v,"cible":c}
def H(v,c="auto",cote="droite"): return {"type":"h","valeur":v,"cible":c,"cote":cote}
def D(v,c="auto"): return {"type":"d","valeur":v,"cible":c}
S={}
def s(h,lignes,encart=(),**kw):
    d={"lignes":lignes,"encart":list(encart),"fiche":f"fiches/{h}.md § Dimensions"}; d.update(kw); S[h]=d
F3="Vue de trois quarts : la ligne de largeur suit l'emprise visible, la profondeur est donnée en encart"
s("canape-enfant-2-places-gris",[L("77 cm"),H("48 cm")],["Profondeur 42 cm","Assise 69 × 31 cm"])
s("chaise-a-bascule-enfant-bois-blanc",[L("34,5 cm"),H("57 cm")],["Profondeur 46,5 cm","Hauteur d'assise 28 cm"])
s("fauteuil-a-bascule-allaitement-lin-poches",[L("68 cm"),H("96 cm")],["Profondeur 93 cm","Hauteur d'assise 54 cm","Accoudoirs à 70 cm du sol"],remarques="Largeur 68 cm ajoutée depuis le tableau (non citée dans le slot)")
s("fauteuil-a-bascule-chenille-soutien-lombaire",[L("63 cm"),H("89 cm")],["Profondeur 92 cm","Avancée du repose-pieds 30 cm"])
s("fauteuil-a-bascule-velours-cotele-repose-pieds-integre",[L("70 cm"),H("92 cm")],["Profondeur 80 cm (114 cm repose-pieds sorti)","Longueur en position allongée 134 cm"],remarques="Le slot prévoit un schéma en trois positions ; l'image n'en montre qu'une, les autres positions sont données en encart")
s("fauteuil-allaitement-bouclette-blanche-usb",[L("66,5 cm"),H("102 cm")],["Profondeur 72,5 cm (121,5 cm repose-pieds sorti)","Hauteur d'assise 50 cm","Accoudoirs à 67 cm du sol"])
s("fauteuil-allaitement-bouclette-pouf-appui-tete",[H("92,5 cm","gauche","gauche"),H("40,5 cm","droite")],["Fauteuil : largeur 75 cm, profondeur 75 cm","Hauteur d'assise 41,5 cm","Pouf 46,5 × 34 × 40,5 cm (l × P × H)"],remarques="Fauteuil et pouf se chevauchent : largeurs données en encart")
s("fauteuil-allaitement-capitonne-poches",[H("86 cm")],["Emprise au sol 66 × 65 cm","Hauteur d'assise 53 cm"],remarques="Emprise au sol en encart (pas de largeur hors tout dans le tableau)")
s("fauteuil-enfant-mousse-teddy-gris",[L("62 cm"),H("41 cm")],["Profondeur 41 cm","Assise 41 × 32 cm"],remarques="Hauteur 41 cm tracée sans la boucle de portage")
s("fauteuil-enfant-nuage-blanc",[L("46 cm"),H("55 cm")],["Profondeur 51 cm","Hauteur d'assise 23 cm"])
s("fauteuil-enfant-teddy-oreilles-ours",[L("47 cm"),H("53 cm")],["Profondeur 43 cm","Hauteur d'assise 27 cm"])
s("fauteuil-enfant-velours-rose-pouf",[H("50 cm","gauche","gauche"),H("25 cm","droite")],["Fauteuil 51 × 51 × 50 cm, assise à 27,5 cm","Pouf 35 × 30 × 25 cm"],remarques="Fauteuil et pouf se chevauchent : largeurs en encart")
s("fauteuil-pivotant-360-bouclette",[L("67 cm"),H("74 cm")],["Profondeur 55 cm","Hauteur d'assise 44 cm","Base Ø 48 cm"])
s("coussin-de-sol-carre-velours-cotele",[],["Existe en 45 × 45 cm et 50 × 50 cm"],remarques="Deux formats : encart texte, pas de ligne")
s("coussin-de-sol-rond-epais-dehoussable",[],["Existe en Ø 40 cm et Ø 50 cm","Épaisseur 10 cm"],remarques="Deux formats : encart ; épaisseur en encart (la vue de dessus fausserait une ligne de hauteur)")
s("coussin-de-sol-rond-raye-capitonne",[],["Existe en Ø 47 cm et Ø 55 cm"],remarques="Deux formats : encart texte")
s("galette-de-sol-en-paille-tressee",[D("Ø 40 cm")],["Épaisseur 6 cm"],remarques="Épaisseur en encart (vue plongeante)")
s("grand-coussin-de-sol-rond-velours-cotele",[D("Ø 55 cm")],[])
for h in ["jete-de-canape-a-glands","jete-de-canape-lignes-abstraites","jete-de-canape-motif-arches"]:
    s(h,[],["Existe en 130 × 180 cm et 180 × 230 cm"],remarques="Jeté drapé + deux formats : encart texte ; le slot prévoit un jeté déplié, l'image le montre drapé")
s("petit-pouf-carre-coton-gaufre",[L("30 cm"),H("20 cm")],["Dessus 30 × 30 cm"])
s("plaid-fausse-fourrure-effet-lapin",[],["Existe en 120 × 200 cm et 150 × 200 cm"],remarques="Deux formats : encart ; slot « déplié », image pliée")
s("plaid-gaufre-en-coton",[],["Dimensions déplié : 165 × 230 cm"],remarques="Slot « déplié à plat », image pliée : pas de ligne, cote en encart")
s("plaid-grosse-maille-tricote-main",[],["Existe en 100 × 120 cm et 100 × 150 cm"],remarques="Deux formats : encart ; slot « à plat », image pliée")
s("plaid-polaire-torsade-sherpa",[],["Existe en 120 × 200 cm et 150 × 200 cm"],remarques="Deux formats : encart ; slot « déplié », image pliée")
s("table-d-appoint-bambou-hauteur-reglable",[H("42 à 82 cm")],["Plateau 40 × 22 cm","Base 36 × 22 cm"],remarques="Plateau et base en encart (deux largeurs différentes)")
s("table-d-appoint-en-c-a-roulettes",[H("60 cm")],["Plateau Ø 40 cm","Base 40 × 30 cm"])
s("table-d-appoint-en-c-bois-rustique-metal",[L("40 cm"),H("50 cm")],["Profondeur 25 cm"])
s("table-d-appoint-ronde-3-plateaux-chene-fonce",[L("46 cm"),H("60 cm")],[],remarques="Tableau : 46 × 46 cm (pas de « Ø » explicite), ligne libellée 46 cm")
s("table-d-appoint-ronde-blanche-pieds-bois",[D("Ø 50 cm"),H("40 cm")],["Épaisseur du plateau 2 cm"])
s("tables-gigognes-blanches-pieds-bambou",[H("45 cm","gauche","gauche"),H("40 cm","droite")],["Grande table 55 × 55 × 45 cm","Petite table 40 × 40 × 40 cm"],remarques="Tables qui se chevauchent : largeurs en encart")
s("chaise-a-bascule-retro-similicuir-cognac",[L("62,5 cm"),H("88 cm")],["Profondeur 86 cm","Assise 55 × 55 cm à 47 cm du sol"])
s("fauteuil-a-bascule-effet-lin-avec-repose-pieds",[H("90 cm","gauche","gauche"),H("31 cm","droite")],["Fauteuil : largeur 64 cm, profondeur 89 cm","Hauteur d'assise 43 cm","Repose-pieds 45 × 37 × 31 cm (l × P × H)"],remarques="Fauteuil et repose-pieds se chevauchent : largeurs en encart")
s("fauteuil-a-bascule-inclinable-velours-cotele-terracotta",[L("78 cm"),H("89 cm")],["Emprise au sol 87 × 88 cm (P × l)","Dossier inclinable de 100° à 160°, 4 positions"],remarques="Les 4 angles du dossier (slot) ne sont pas dessinés : image en une seule position, plage donnée en encart")
s("fauteuil-a-bascule-oreilles-tissu-avec-tabouret",[H("98 cm","gauche","gauche"),H("37,5 cm","droite")],["Fauteuil : largeur 61 cm, profondeur 78 cm","Assise à 47,5 cm, accoudoirs à 60,5 cm","Tabouret 47 × 31 × 37,5 cm (l × P × H)"],remarques="Fauteuil et tabouret se chevauchent : largeurs en encart")
s("fauteuil-a-bascule-teddy-gris-poches-laterales",[L("63 cm"),H("104 cm")],["Profondeur 73 cm","Assise à 49 cm, accoudoirs à 68 cm"])
s("fauteuil-a-bascule-xxl-coussin-capitonne",[],["Coussin 97 × 70 cm (une fois regonflé)"],remarques="Seule la cote du coussin est connue : pas de ligne sur le fauteuil (la largeur hors tout n'est pas au tableau) ; le slot prévoit une vue de face, l'image est de trois quarts")
s("rocking-chair-acier-noir-coussin-cotele-ecru",[H("82 cm")],["Profondeur 116 cm","Hauteur d'assise 38 cm","Dossier 56 cm"],remarques="Pas de largeur hors tout au tableau (seulement assise 54 cm)")
s("rocking-chair-bois-blanc-dossier-a-lattes",[L("69 cm"),H("115 cm")],["Profondeur 86 cm","Assise à 47,5 cm, accoudoirs à 68,5 cm"])
s("rocking-chair-bouclette-blanche-cadre-bois-ouvert",[L("60 cm"),H("71 cm")],["Profondeur 81 cm","Assise à 46 cm, accoudoirs à 65 cm"],scene=True,remarques="Image en situation (fond non uni) : boîte produit posée à la main")
s("rocking-chair-bouclette-creme-avec-pouf",[H("100 cm","gauche","gauche"),H("41 cm","droite")],["Fauteuil : largeur 72 cm, profondeur 97 cm","Hauteur d'assise 52 cm","Pouf 56 × 43 × 41 cm (l × P × H)"],scene=True,remarques="Image en situation (fond non uni) : boîtes posées à la main ; largeurs en encart")
s("rocking-chair-effet-lin-creme-bois-clair",[L("64,5 cm"),H("81,5 cm")],["Profondeur 92 cm","Assise 58 × 56 cm à 44 cm du sol"])
s("rocking-chair-lin-creme-cadre-noyer-avec-pouf",[],["Épaisseur du coussin d'assise 20 cm","Épaisseur du coussin du pouf 14 cm"],remarques="Tableau sans largeur/hauteur/profondeur : seules les épaisseurs de coussin, en encart, aucune ligne")
s("rocking-chair-lounge-effet-lin-dossier-reglable",[L("62 cm")],["Profondeur 90,5 cm","Hauteur du dossier 61 cm","Hauteur d'assise 29 cm"],remarques="Pas de hauteur totale au tableau : pas de ligne de hauteur")
s("rocking-chair-mid-century-kaki-bois-fonce",[L("74 cm")],["Profondeur 88 cm","Assise à 50 cm, accoudoirs à 60 cm"],remarques="Pas de hauteur totale au tableau : pas de ligne de hauteur")
s("rocking-chair-teddy-creme-accoudoirs-bois",[L("65 cm"),H("98 cm")],["Profondeur 90 cm","Assise 60 × 57 cm","Dossier 59 × 65 cm (l × H)"])
s("rocking-chair-tissu-gris-cadre-bois-clair",[L("65 cm"),H("84 cm")],["Profondeur 87 cm","Assise 58,5 × 56 cm","Hauteur d'assise 39 à 43 cm"],remarques="Slot : assise à 43 cm ; tableau : 39 à 43 cm (affiché)")
s("fauteuil-pouf-bouclette-sherpa-matelasse",[L("86 cm"),H("75 cm")],["Hauteur d'assise 37,5 cm","Hauteur du dossier 51 cm"])
s("fauteuil-pouf-fausse-fourrure-gris-clair",[L("99 cm"),H("71 cm")],[])
s("fauteuil-pouf-fourrure-dossier-arrondi",[L("123 cm"),H("75 cm")],["Profondeur 111 cm","Hauteur d'assise 41 cm"])
s("pouf-coffre-chenille-beige",[L("38 cm","gauche"),H("45 cm","gauche","gauche")],["Profondeur 38 cm","Rangement Ø 35 cm, profondeur 37 cm"],remarques="Couvercle posé à côté : cotes tracées sur le corps du pouf")
s("pouf-coffre-rond-bouclette-blanc",[D("Ø 45 cm","gauche"),H("41 cm","gauche","gauche")],[],remarques="Couvercle posé à côté : cotes tracées sur le corps du pouf")
s("pouf-coffre-sherpa-creme",[L("38 cm","gauche"),H("45 cm","gauche","droite")],["Profondeur 38 cm","Profondeur intérieure 37 cm"],scene=True,remarques="Image en situation : boîte posée à la main")
s("pouf-geant-rond-velours-cotele",[D("Ø 109 à 122 cm"),H("58 à 66 cm")],[])
s("pouf-poire-geant-convertible-velours",[],["Position fauteuil 112 × 112 × 70 cm","Position lit 190 × 135 × 20 cm"],scene=True,remarques="Image composite de deux scènes avec personne : aucune ligne possible, cotes en encart ; slot « 112 × 70 cm », tableau « 112 × 112 × 70 cm »")
s("pouf-rond-velours-cotele-moelleux",[D("Ø 50 cm"),H("35 cm")],[],remarques="Diamètre tracé sans la poignée")
s("repose-pieds-carre-velours-cotele",[L("50 cm"),H("35 cm")],["Profondeur 50 cm"],remarques="Largeur tracée sans la poignée")
s("chaise-longue-a-bascule-acacia",[L("154 cm"),H("74 cm")],["Largeur 60 cm","Coussin de tête 45,5 × 26,5 cm"],remarques="Vue de profil : la ligne horizontale porte la longueur 154 cm")
s("fauteuil-lounge-cotele-avec-pouf",[H("95 cm","gauche","gauche"),H("46 cm","droite")],["Fauteuil : largeur 80 cm, profondeur 64 cm","Pouf 50 × 45 × 46 cm (L × P × H)"],remarques="Fauteuil et pouf se chevauchent : largeurs en encart")
s("fauteuil-oeuf-suspendu-rotin-gris",[L("105 cm"),H("195 cm")],["Nacelle 90 × 107 cm (l × H)","Pied 105 × 105 cm au sol"])
s("fauteuil-relax-large-chenille-creme",[L("95 cm"),H("104 cm")],["Profondeur 94 cm (162 cm incliné)","Hauteur d'assise 51 cm"])
s("fauteuil-relax-manuel-lin-gris-clair",[L("72 cm"),H("101 cm")],["Profondeur 65 cm","Longueur repose-pieds déplié 157 cm"])
s("fauteuil-relax-massant-chauffant-chenille-ecru",[L("73,5 cm"),H("108 cm")],["Profondeur 97 cm","Incliné : 163 cm de profondeur, 155°"])
s("fauteuil-relax-pivotant-beige-avec-pouf",[H("104 cm","gauche","gauche"),H("35 à 40 cm","droite")],["Fauteuil : largeur 69 cm, profondeur 71 cm","Pouf 42 × 43 cm, hauteur 35 à 40 cm"],remarques="Slot : pouf 42 × 43 × 35 cm ; tableau : hauteur 35 à 40 cm (affiché) ; largeurs en encart")
s("fauteuil-relax-push-back-cotele",[L("60 cm"),H("97 cm")],["Profondeur 73 cm","Longueur déplié 155 cm"])
s("fauteuil-suspendu-tissu-sur-pied",[L("94 cm"),H("197 cm")],["Emprise du pied 108 × 94 cm","Assise 71 × 52 cm"],remarques="Tableau incohérent : 196,5 cm (ligne L × P × H) et 197 cm (hauteur totale) ; 197 cm affiché comme le slot")
s("rocking-chair-acacia-coussins-beige",[L("60 cm"),H("107 cm")],["Profondeur 89 cm","Hauteur d'assise 42,5 à 44,5 cm"])
s("rocking-chair-adirondack-acacia",[L("75 cm"),H("90 cm")],["Profondeur 105 cm"])
s("rocking-chair-adirondack-noir-repose-pieds",[H("105 cm")],["Profondeur 84 cm","Repose-pieds 47 × 42 cm"],remarques="Pas de largeur hors tout au tableau")
s("rocking-chair-jardin-metal-noir",[L("59,5 cm"),H("92,5 cm")],["Profondeur 102 cm"])
s("transat-a-bascule-pliable-gris",[L("145 cm"),H("86 cm")],["Largeur 74 cm","Hauteur d'assise 36 cm"],remarques="Vue de profil : la ligne horizontale porte la longueur 145 cm")
old={}
try: old=json.load(open(sys.argv[1]))
except Exception: pass
for h,v in old.items():  # conserve les boîtes posées à la main
    for k in ("boite","cibles_manuelles"):
        if k in v and h in S: S[h][k]=v[k]
json.dump(S,open(sys.argv[1],"w"),ensure_ascii=False,indent=1)
print(len(S))
# ---- boîtes posées à la main (px source 2048), relevées sur grille
M={
 "fauteuil-a-bascule-effet-lin-avec-repose-pieds":{"gauche":[58,240,1360,1630],"droite":[1178,1104,2010,1830]},
 "fauteuil-a-bascule-oreilles-tissu-avec-tabouret":{"gauche":[80,102,1344,1658],"droite":[1024,1082,1968,1894]},
 "fauteuil-allaitement-bouclette-pouf-appui-tete":{"gauche":[128,256,1424,1664],"droite":[1024,1104,1958,1862]},
 "fauteuil-enfant-velours-rose-pouf":{"gauche":[122,458,1318,1520],"droite":[1062,1043,1952,1702]},
 "fauteuil-lounge-cotele-avec-pouf":{"gauche":[166,122,1498,1610],"droite":[922,998,1952,1936]},
 "fauteuil-relax-pivotant-beige-avec-pouf":{"gauche":[138,32,1386,1690],"droite":[1008,1158,1894,1990]},
 "rocking-chair-bouclette-creme-avec-pouf":{"gauche":[294,112,1446,1584],"droite":[918,1162,1872,1968],"boite":[294,112,1872,1968]},
 "pouf-coffre-chenille-beige":{"gauche":[208,266,1344,1712]},
 "pouf-coffre-rond-bouclette-blanc":{"gauche":[198,410,1328,1680]},
 "pouf-coffre-sherpa-creme":{"gauche":[336,432,1488,1840],"hgauche":[250,432,1488,1840],"boite":[208,432,1952,1840]},
 "rocking-chair-bouclette-blanche-cadre-bois-ouvert":{"boite":[336,410,1850,1744]},
 "pouf-rond-velours-cotele-moelleux":{"boite":[282,336,1664,1766]},
 "fauteuil-enfant-mousse-teddy-gris":{"boite":[102,304,1990,1808]},
 "table-d-appoint-ronde-blanche-pieds-bois":{"boite":[256,240,1792,1728]},
 "tables-gigognes-blanches-pieds-bambou":{"gauche":[96,336,1456,1674],"droite":[896,618,1946,1802],"boite":[96,336,1946,1802]},
}
for h,m in M.items():
    sp=S[h]
    if "boite" in m: sp["boite"]=m["boite"]
    for l in sp["lignes"]:
        c=l["cible"]
        if h=="pouf-coffre-sherpa-creme" and l["type"]=="h":
            l["cible"]=m["hgauche"]; l["cote"]="gauche"; continue
        if c in ("gauche","droite") and c in m: l["cible"]=m[c]
json.dump(S,open(sys.argv[1],"w"),ensure_ascii=False,indent=1)
S["pouf-coffre-sherpa-creme"]["encart_pos"]="haut-gauche"
b=S["rocking-chair-bouclette-blanche-cadre-bois-ouvert"]; b["boite"]=[336,410,1850,1750]
for l in b["lignes"]:
    if l["type"]=="h": l["cote"]="gauche"
json.dump(S,open(sys.argv[1],"w"),ensure_ascii=False,indent=1)
