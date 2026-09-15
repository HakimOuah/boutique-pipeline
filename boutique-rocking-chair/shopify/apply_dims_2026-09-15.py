"""Bercelou : ajoute les cotes montées lues sur les fiches AliExpress (texte ou schéma coté) aux descriptions."""
import json, re

def rows(pairs):
    return "".join(f"<tr>\n<td>{a}</td>\n<td>{b}</td>\n</tr>\n" for a, b in pairs)

def load(h):
    return json.load(open(f"live_{h}.json"))["product"]

def add_rows(html, pairs):
    m = re.search(r"(<h2>Dimensions</h2>\s*<table>.*?<tbody>\s*)", html, re.S)
    assert m, "table Dimensions introuvable"
    return html[:m.end()] + rows(pairs) + html[m.end():]

def sub1(html, old, new):
    assert html.count(old) >= 1, old[:80]
    return html.replace(old, new)

SRC = {}
out = {}

# 1. Teddy dossier haut — schéma coté galerie (pouces), 1005012886082802
h = "fauteuil-rocking-chair-teddy-dossier-haut"; x = load(h)["body_html"]
x = add_rows(x, [("Hauteur totale", "91 cm"), ("Largeur hors tout", "64 cm"), ("Profondeur au sol (patins)", "92 cm"),
                 ("Hauteur d'assise (sol)", "42 cm"), ("Hauteur de l'accoudoir (sol)", "57 cm"),
                 ("Hauteur du dossier (depuis l'assise)", "59 cm"), ("Largeur de l'assise", "43 cm"), ("Profondeur de l'assise", "46 cm")])
x = sub1(x, "<p>Conseil de place : laissez environ 50 cm derrière le fauteuil pour une bascule libre.</p>",
         "<p>Conseil de place : comptez environ 92 cm de profondeur au sol pour les patins, et 50 cm de dégagement derrière le fauteuil pour une bascule libre.</p>")
x = sub1(x, "Le colis mesure 65 × 65 × 33 cm. Comptez environ 50 cm de dégagement derrière le fauteuil pour une bascule libre.",
         "Le fauteuil mesure 64 cm de large et ses patins occupent environ 92 cm de profondeur au sol. Comptez environ 50 cm de dégagement derrière pour une bascule libre.")
x = sub1(x, "Les accoudoirs larges offrent un appui stable pour vous redresser,",
         "L'assise est à 42 cm du sol et les accoudoirs à 57 cm : ils offrent un appui stable pour vous redresser,")
out[h] = x; SRC[h] = "galerie AliExpress 1005012886082802, image « Product Dimension » (pouces convertis)"

# 2. Siège à bascule rembourré — schéma « Produktinformation » du détail, 1005011557882819
h = "siege-a-bascule-rembourre"; x = load(h)["body_html"]
x = add_rows(x, [("Hauteur totale", "98,5 cm"), ("Largeur hors tout", "70 cm"), ("Profondeur au sol (patins)", "98 cm"),
                 ("Profondeur repose-pieds déplié", "123 cm"), ("Hauteur d'assise (sol)", "50 cm"), ("Hauteur de l'accoudoir (sol)", "65 cm"),
                 ("Hauteur du dossier (depuis l'assise)", "56 cm"), ("Largeur de l'assise", "43 cm"), ("Profondeur de l'assise", "50,5 cm")])
x = sub1(x, "<p>Conseil de place : prévoyez de la place devant le siège pour déplier le repose-pieds, et un dégagement derrière pour la bascule.</p>",
         "<p>Conseil de place : comptez 98 cm de profondeur au sol, 123 cm repose-pieds déplié, et un dégagement derrière le siège pour la bascule.</p>")
x = sub1(x, "Prévoyez la place devant le siège pour déplier le repose-pieds, et un dégagement derrière pour la bascule.",
         "Le siège mesure 70 cm de large et 98 cm de profondeur au sol, 123 cm repose-pieds déplié. Prévoyez aussi un dégagement derrière pour la bascule.")
out[h] = x; SRC[h] = "détail AliExpress 1005011557882819, image « Produktinformation » (cm)"

# 3. Chaise qui se balance — spécifications du détail (pouces), 1005012653961063 ; charge 250 lb = 113 kg
h = "chaise-qui-se-balance"; x = load(h)["body_html"]
x = add_rows(x, [("Hauteur totale", "91 cm"), ("Encombrement au sol", "75 × 53 cm"), ("Hauteur d'assise (sol)", "40 cm"),
                 ("Hauteur du dossier (depuis l'assise)", "61 cm"), ("Largeur de l'assise", "60 cm"),
                 ("Hauteur de l'accoudoir (depuis l'assise)", "22 cm"), ("Poids du fauteuil", "11,3 kg")])
x = x.replace("120 kg", "113 kg")
x = sub1(x, "<p>Conseil de place : prévoyez un dégagement derrière la chaise pour une bascule libre.</p>",
         "<p>Conseil de place : la chaise occupe environ 75 × 53 cm au sol ; prévoyez un dégagement derrière pour une bascule libre.</p>")
out[h] = x; SRC[h] = "détail AliExpress 1005012653961063, spécifications texte (pouces convertis) ; charge 250 lb"

# 4. Relax électrique — schéma « Dimensions » galerie (pouces), 1005012054721103
h = "fauteuil-relax-electrique"; x = load(h)["body_html"]
x = add_rows(x, [("Hauteur totale", "108 cm"), ("Largeur hors tout", "74 cm"), ("Profondeur (position assise)", "67 cm"),
                 ("Longueur en position sieste", "157 cm"), ("Largeur du dossier", "57 cm"), ("Charge maximale", "136 kg")])
x = sub1(x, "<p>Comptez de l'espace à l'avant du fauteuil pour déplier complètement le repose-pieds jusqu'à la position 150°.</p>",
         "<p>Conseil de place : le fauteuil mesure 67 cm de profondeur en position assise et 157 cm en position sieste ; prévoyez cet espace à l'avant pour déplier complètement le repose-pieds.</p>")
x = sub1(x, "Comptez de l'espace à l'avant du fauteuil pour déplier complètement le repose-pieds.",
         "Le fauteuil mesure 74 cm de large et 67 cm de profondeur, 157 cm en position sieste : prévoyez cet espace à l'avant.")
out[h] = x; SRC[h] = "galerie AliExpress 1005012054721103, image « Dimensions » (pouces convertis ; 300 lb)"

# 5. Relax moderne — schéma « Size details » galerie (cm), 1005012454786223
h = "fauteuil-relax-moderne"; x = load(h)["body_html"]
x = add_rows(x, [("Hauteur totale", "105 cm"), ("Largeur hors tout", "74 cm"), ("Longueur en position allongée", "160 cm"),
                 ("Hauteur des accoudoirs (sol)", "60 cm"), ("Largeur de l'assise", "40 cm"), ("Largeur du dossier", "57 cm")])
x = sub1(x, "<p>Comptez de l'espace à l'avant du fauteuil pour profiter de l'inclinaison jusqu'à 165°.</p>",
         "<p>Conseil de place : le fauteuil atteint 160 cm de long en position allongée ; prévoyez cet espace pour profiter de l'inclinaison jusqu'à 165°.</p>")
x = sub1(x, "Comptez de l'espace à l'avant du fauteuil pour profiter de l'inclinaison complète.",
         "Le fauteuil mesure 74 cm de large et atteint 160 cm de long en position allongée.")
out[h] = x; SRC[h] = "galerie AliExpress 1005012454786223, image « Size details » (cm)"

# 6. Relax cuir — texte du détail, 1005012780948146
h = "fauteuil-relax-cuir"; x = load(h)["body_html"]
x = add_rows(x, [("Fauteuil en position assise (L × P × H)", "71 × 84 × 102 cm"), ("Fauteuil incliné (L × P × H)", "75 × 111 × 85 cm"),
                 ("Repose-pieds (L × P × H)", "48 × 40 × 41 cm")])
x = sub1(x, "Comptez l'espace du repose-pieds devant le fauteuil.",
         "Le fauteuil mesure 71 × 84 cm au sol, 111 cm de profondeur une fois incliné ; ajoutez le repose-pieds (48 × 40 cm) devant.")
out[h] = x; SRC[h] = "détail AliExpress 1005012780948146, texte « Dimensions officielles »"

# 7. Relax de salon — texte du détail, 1005012809448823
h = "fauteuil-relax-de-salon"; x = load(h)["body_html"]
x = add_rows(x, [("Fauteuil (L × l × H)", "69 × 71 × 104 cm"), ("Pouf (L × l × H)", "42 × 43 × 35 à 40 cm"), ("Charge maximale du pouf", "50 kg")])
x = sub1(x, "Comptez l'espace du pouf devant le fauteuil.",
         "Le fauteuil occupe 69 × 71 cm au sol ; ajoutez le pouf (42 × 43 cm) devant pour la position détente.")
out[h] = x; SRC[h] = "détail AliExpress 1005012809448823, texte « Spécifications du produit »"

json.dump(out, open("dims_out.json", "w"), ensure_ascii=False)
json.dump(SRC, open("dims_sources.json", "w"), ensure_ascii=False, indent=1)
for h, v in out.items():
    print(h, len(v), v.count("<tr>"), "120 kg" in v)
