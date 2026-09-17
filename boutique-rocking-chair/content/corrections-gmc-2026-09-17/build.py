#!/usr/bin/env python3
"""Corrections GMC 4.7 (« vérifié »), 4.8 (« se relever ») et 2.13 (délais par catégorie).

Lit dump.json (thème de travail + fiches actives) et pages.json, écrit out/*.
Chaque remplacement doit trouver exactement le nombre d'occurrences attendu.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out"
OUT.mkdir(exist_ok=True)
dump = json.loads((ROOT / "dump.json").read_text())["data"]
pages = json.loads((ROOT / "pages.json").read_text())


def rep(text, pairs, label):
    for old, new, n in pairs:
        got = text.count(old)
        if got != n:
            raise SystemExit(f"{label}: « {old[:60]} » trouvé {got} fois, attendu {n}")
        text = text.replace(old, new)
    return text


RULE_MEUBLES = "fauteuils, poufs, repose-pieds et tables d'appoint"
RULE_TEXTILES = "plaids, coussins et housses de protection"

# ---------------------------------------------------------------- fiches
products = {p["handle"]: p["descriptionHtml"] for p in dump["products"]["nodes"]}
prod_fix = {
    "fauteuil-a-bascule-allaitement-teddy": [
        ("dos soutenu, bras posés, vous vous relevez sans réveiller bébé.",
         "dos soutenu, bras posés, bébé bercé en douceur.", 1),
    ],
    "fauteuil-pivotant-360-bouclette": [
        ("Se relever en douceur", "Une assise à hauteur de chaise", 1),
        ("Il reste stable pour s'asseoir et se relever.", "Il reste stable quand vous vous asseyez.", 1),
    ],
    "fauteuil-pouf-fourrure-dossier-arrondi": [
        ("1. Est-il facile de se relever ?", "1. Quelle est la hauteur d'assise ?", 1),
        ("<h3>Une assise à bonne hauteur</h3>\n<p>L'assise se trouve à 41 cm du sol : on s'y assoit et on s'en relève plus facilement que d'un pouf posé au ras du sol.</p>",
         "<h3>Une assise surélevée</h3>\n<p>L'assise se trouve à 41 cm du sol, plus haut qu'un pouf posé au ras du sol : on s'y installe comme dans un fauteuil.</p>", 1),
        ("L'assise est à 41 cm du sol, plus haute qu'un pouf classique, ce qui aide à se relever.",
         "L'assise est à 41 cm du sol, plus haute qu'un pouf classique. Pour vous lever, avancez-vous d'abord au bord de l'assise.", 1),
    ],
}
out_products = {h: rep(products[h], pairs, h) for h, pairs in prod_fix.items()}

# ---------------------------------------------------------------- pages
out_pages = {}
out_pages["qui-sommes-nous"] = rep(pages["qui-sommes-nous"], [
    ("Avant de retenir un fauteuil, notre équipe vérifie sa hauteur d'assise, la largeur de ses accoudoirs, la hauteur de son dossier et la matière annoncée, pour s'assurer qu'il répond aux critères que vous nous avez rapportés : se relever facilement, être bien soutenu, garder un style qui reste au salon.",
     "Nous sélectionnons chaque fauteuil d'après ses dimensions et sa matière : hauteur d'assise, largeur des accoudoirs, hauteur du dossier, tissu annoncé. Ces cotes figurent sur chaque fiche, pour que vous choisissiez selon ce qui compte pour vous : une assise à la bonne hauteur, un dos bien soutenu, un style qui reste au salon.", 1),
    ("Notre catalogue couvre les fauteuils d'allaitement, les rocking chairs design et scandinaves, les modèles en bois et en rotin, les fauteuils cocon et d'extérieur, et les fauteuils relax.",
     "Notre catalogue couvre les fauteuils d'allaitement, les rocking chairs design et scandinaves, les modèles en bois et en rotin, les fauteuils cocon et d'extérieur, les fauteuils relax, le mobilier enfant et un coin cocooning : poufs, repose-pieds, coussins de sol, plaids et tables d'appoint.", 1),
], "qui-sommes-nous")

out_pages["guide-bien-choisir-fauteuil-allaitement"] = rep(pages["guide-bien-choisir-fauteuil-allaitement"], [
    ("Ce guide reprend les sept points que nous vérifions sur chaque fiche avant de retenir un modèle.",
     "Ce guide reprend les sept critères sur lesquels nous sélectionnons nos modèles, et vous montre où les lire sur chaque fiche.", 1),
    ("<h2>1. Pouvoir se relever facilement, même avec bébé dans les bras</h2>",
     "<h2>1. Une hauteur d'assise adaptée à votre façon de vous lever</h2>", 1),
    ("Un fauteuil pensé pour l'allaitement doit vous laisser sortir sans acrobatie, bébé dans les bras.",
     "Plus l'assise est haute, plus le passage assis-debout demande peu d'effort ; une assise basse et enveloppante invite au contraire à se lover.", 1),
    ("un profil plus droit facilite le lever, un profil très enveloppant demande plus d'effort.",
     "comparez-la à la hauteur standard d'une chaise, autour de 45 cm. Pour vous lever, avancez-vous au bord de l'assise, arrêtez la bascule avec les pieds et prenez appui sur les accoudoirs.", 1),
], "guide")

out_pages["faq"] = rep(pages["faq"], [
    ("<strong>2. Comment savoir si je pourrai me relever facilement avec bébé dans les bras ?</strong><br>\nConsultez la hauteur d'assise dans le tableau des dimensions de chaque fiche, et la forme du dossier et de l'assise sur les photos. Un profil plus droit facilite le lever.",
     "<strong>2. Comment choisir la bonne hauteur d'assise ?</strong><br>\nConsultez la hauteur d'assise dans le tableau des dimensions de chaque fiche et comparez-la à celle d'une chaise, autour de 45 cm. Pour vous lever avec bébé dans les bras, avancez-vous au bord de l'assise, arrêtez la bascule et prenez appui sur les accoudoirs.", 1),
    ("Les fauteuils sont livrés en 3 à 10 jours ouvrés, sauf mention d'un autre délai sur la fiche produit. Les accessoires (plaid, coussin, repose-pieds, housse de protection) sont livrés en 7 à 15 jours ouvrés.",
     f"Les meubles ({RULE_MEUBLES}) sont livrés en 3 à 10 jours ouvrés. Les textiles ({RULE_TEXTILES}) sont livrés en 7 à 15 jours ouvrés. Le délai de chaque article figure sur sa fiche produit et prime en cas de différence.", 1),
], "faq")

out_pages["livraison-retours"] = rep(pages["livraison-retours"], [
    ("<p>Vos fauteuils sont livrés en 3 à 10 jours ouvrés, sauf mention d'un autre délai sur la fiche produit. Les accessoires (plaid, coussin, repose-pieds, housse de protection) sont livrés en 7 à 15 jours ouvrés.</p>",
     f"<p>Les meubles ({RULE_MEUBLES}) sont livrés en 3 à 10 jours ouvrés. Les textiles ({RULE_TEXTILES}) sont livrés en 7 à 15 jours ouvrés. Le délai de chaque article figure sur sa fiche produit et prime en cas de différence.</p>", 1),
], "livraison-retours")

out_pages["suivre-ma-commande"] = rep(pages["suivre-ma-commande"], [
    ("<th>Fauteuils et chaises à bascule, relax, enfant</th>",
     "<th>Meubles : fauteuils, poufs, repose-pieds, tables d'appoint</th>", 1),
    ("<th>Accessoires (coussins, plaids, repose-pieds, housses)</th>",
     "<th>Textiles : plaids, coussins, housses de protection</th>", 1),
    ("Si votre commande réunit un fauteuil et un accessoire,", "Si votre commande réunit un meuble et un textile,", 1),
], "suivre-ma-commande")

# ---------------------------------------------------------------- thème
theme = {f["filename"]: f["body"]["content"] for f in dump["theme"]["files"]["nodes"]}


def strip_header(c):
    return c[c.index("{"):] if c.lstrip().startswith("/*") else c


index = rep(strip_header(theme["templates/index.json"]), [
    ("Vous vous installez, vous bercez bébé en douceur, vous vous relevez sans le réveiller.",
     "Vous vous installez, vous bercez bébé en douceur, le dos bien soutenu.", 1),
    ("Chaque fauteuil est vérifié avant d'être retenu", "Chaque fauteuil est sélectionné sur ses cotes", 1),
    ("Hauteur d'assise, largeur des accoudoirs, hauteur du dossier, matière : nous contrôlons ces points sur chaque modèle, pour qu'il réponde à ce que vous cherchez vraiment. Se relever facilement, avoir le dos soutenu, garder un fauteuil qui reste beau au salon.",
     "Hauteur d'assise, largeur des accoudoirs, hauteur du dossier, matière : nous choisissons chaque modèle sur ces critères, et vous les retrouvez sur chaque fiche. Une assise à la bonne hauteur, un dos soutenu, un fauteuil qui reste beau au salon.", 1),
    ("Se relever facilement, même avec bébé dans les bras", "Des accoudoirs pour prendre appui en vous relevant", 1),
    ("Cinq points que nous vérifions avant de retenir un modèle.", "Cinq critères sur lesquels nous choisissons nos modèles.", 1),
], "index.json")
json.loads(index)

cart = (ROOT.parent / "panier/apres/cart.json").read_text()
cart = rep(cart, [
    ("Le délai de chaque article figure sur sa fiche produit : 3 à 10 jours ouvrés pour les fauteuils, 7 à 15 jours ouvrés pour les accessoires.",
     f"Meubles ({RULE_MEUBLES}) : 3 à 10 jours ouvrés. Textiles ({RULE_TEXTILES}) : 7 à 15 jours ouvrés. Le délai de chaque article figure sur sa fiche produit.", 1),
    ("Un fauteuil et un accessoire commandés ensemble", "Un meuble et un textile commandés ensemble", 1),
], "cart.json")
json.loads(cart)

(OUT / "index.json").write_text(index)
(OUT / "cart.json").write_text(cart)
json.dump(out_pages, open(OUT / "pages.json", "w"), ensure_ascii=False, indent=1)
json.dump(out_products, open(OUT / "products.json", "w"), ensure_ascii=False, indent=1)

bad = re.compile(r"relev(ez|er) (facilement|sans)|vérifi(é|ons) (avant|sur chaque)|contrôlons|[—–]")
for label, blob in [("index", index), ("cart", cart)] + list(out_pages.items()) + list(out_products.items()):
    for m in bad.finditer(blob):
        ctx = blob[max(0, m.start() - 40):m.end() + 20]
        if "—" in m.group(0) and label in ("index", "cart"):
            continue
        print("RESTE", label, repr(ctx))
print("ok")
