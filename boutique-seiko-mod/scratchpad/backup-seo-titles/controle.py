# -*- coding: utf-8 -*-
"""Controle apres ecriture : diff seo.description, longueurs, chronos, diametres."""
import json, re, io, sys, contextlib, os
OUT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, OUT)
with contextlib.redirect_stdout(io.StringIO()):
    import build  # ROWS + regenere la sauvegarde

INTOUCHEES = json.load(open(os.path.join(OUT, "desc-intouchees.json")))

apres = {}
for f in ("apres-p1.json", "apres-p2.json"):
    for n in json.load(open(os.path.join(OUT, f)))["data"]["collection"]["products"]["nodes"]:
        apres[n["handle"]] = (n["status"], n["seo"]["title"], n["seo"]["description"])
actifs = {h: v for h, v in apres.items() if v[0] == "ACTIVE"}

ROWS = {r[0]: r for r in build.ROWS}
# baseline complete : description d'avant = celle du plan, ou celle relevee pour les intouchees
AVANT = {h: (r[4], r[5] if r[6] else INTOUCHEES.get(h)) for h, r in ROWS.items()}

# diametres reellement renseignes (metafield custom.diametre, releve 30/07)
DIAM = {
 "montre-squelette-automatique-octogone": None, "montre-acier-chiffres-3-6-9-explorateur": None,
 "montre-field-bronze-cadran-chiffres-1-12": "36", "montre-field-acier-cadran-chiffres-1-12": "39",
 "montre-squelette-automatique-carree": "42", "heritage-vert-plongeuse-vintage-42": "42",
 "heritage-bleu-nuit-plongeuse-vintage-42": "42", "heritage-bleu-plongeuse-vintage-42": "42",
 "montre-aviateur-bronze-cadran-chiffres-1-12": None, "montre-aviateur-acier-cadran-chiffres-1-12": None,
 "integrale-blanc-argente-sport-chic-acier": None, "integrale-bleu-ciel-sport-chic-acier": None,
 "integrale-bleu-nuit-sport-chic-acier": None, "integrale-noir-sport-chic-acier": None,
 "integrale-turquoise-sport-chic-acier": None, "integrale-brun-or-rose-sport-chic": None,
 "integrale-vert-sport-chic-acier": None,
}

ko = []
for h, (st, t, d) in actifs.items():
    if h not in AVANT:
        ko.append("FICHE HORS PLAN %s" % h); continue
    at, ad = AVANT[h]
    if d != ad:
        ko.append("DESCRIPTION ALTEREE %s\n  avant: %r\n  apres: %r" % (h, ad, d))
    if not t:
        ko.append("TITRE VIDE %s" % h)
    else:
        if len(t) > 65:
            ko.append("TITRE >65 (%d) %s" % (len(t), h))
        if "montre" not in t.lower():
            ko.append("SANS NOM COMMUN 'montre' %s" % h)
        if ROWS[h][3] == "chrono" and "automatique" in t.lower():
            ko.append("'automatique' SUR CHRONO %s" % h)
        if "plongée" in t.lower() or "plongee" in t.lower():
            ko.append("'montre de plongee' %s" % h)
        attendu = ROWS[h][6] or at
        if t != attendu:
            ko.append("TITRE INATTENDU %s: %r != %r" % (h, t, attendu))
    if h in DIAM:
        m = re.search(r"(\d+)(/\d+)? mm", t or "")
        if DIAM[h] is None and m:
            ko.append("DIAMETRE INVENTE %s: %s" % (h, t))
        if DIAM[h] and (not m or m.group(1) != DIAM[h]):
            ko.append("DIAMETRE ABSENT/FAUX %s: %s" % (h, t))

modifs = [h for h in actifs if ROWS[h][6]]
lens = [len(actifs[h][1]) for h in actifs]
print("ACTIVE relues            : %d" % len(actifs))
print("DRAFT ignorees           : %d" % (len(apres) - len(actifs)))
print("seo.title reecrits       : %d" % len(modifs))
print("seo.title inchanges      : %d" % (len(actifs) - len(modifs)))
print("seo.title renseignes     : %d / %d" % (sum(1 for h in actifs if actifs[h][1]), len(actifs)))
print("longueur max / moyenne   : %d / %.1f" % (max(lens), sum(lens) / len(lens)))
print("titres avec un mm chiffre: %d / %d" % (sum(1 for h in actifs if re.search(r"\d+(/\d+)? mm", actifs[h][1])), len(actifs)))
print("seo.description intactes : %d / %d" % (sum(1 for h in actifs if actifs[h][2] == AVANT[h][1]), len(actifs)))
print("seo.description nulles   : %d  %s" % (sum(1 for h in actifs if actifs[h][2] is None),
      [h for h in actifs if actifs[h][2] is None]))
print()
print("CONTROLE : " + ("TOUT OK, aucune anomalie" if not ko else "\n".join(ko)))
