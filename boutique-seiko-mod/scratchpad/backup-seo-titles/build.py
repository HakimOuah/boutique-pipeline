# -*- coding: utf-8 -*-
"""Sauvegarde de l'etat AVANT + calcul des nouveaux seo.title NOIRMONT."""
import json, os, unicodedata

OUT = os.path.dirname(os.path.abspath(__file__))

D_CHRONO = {
 "bleu-glacier": "Chronographe à cadran bleu glacier dégradé, compteurs assortis, boîtier 39 mm, bracelet acier. Méca-quartz Seiko VK63. Livraison offerte, garantie 12 mois.",
 "compteurs-bleus": "Chronographe à cadran blanc et compteurs bleus, boîtier 39 mm, bracelet caoutchouc bleu marine. Méca-quartz Seiko VK63. Livraison offerte, garantie 12 mois.",
 "argent": "Chronographe à cadran argenté et compteurs gris, boîtier 39 mm, bracelet caoutchouc noir. Méca-quartz Seiko VK63. Livraison offerte, garantie 12 mois.",
 "gris-anthracite": "Chronographe à cadran gris anthracite et compteurs noirs, boîtier 39 mm, bracelet acier. Méca-quartz Seiko VK63. Livraison offerte, garantie 12 mois.",
 "rose-poudre": "Chronographe à cadran rose poudré mat, compteurs assortis, boîtier 39 mm, bracelet acier. Méca-quartz Seiko VK63. Livraison offerte, garantie 12 mois.",
 "vert": "Chronographe à cadran vert et compteurs assortis, boîtier 39 mm, bracelet caoutchouc vert ou acier. Méca-quartz Seiko VK63. Livraison offerte, garantie 12 mois.",
 "turquoise": "Chronographe à cadran turquoise, boîtier 39 mm, bracelet acier, compteurs ton sur ton ou noirs. Méca-quartz Seiko VK63. Livraison offerte, garantie 12 mois.",
 "noir": "Chronographe tout noir, boîtier 39 mm, bracelet caoutchouc, lunette lisse ou tachymètre au choix. Méca-quartz Seiko VK63. Livraison offerte, garantie 12 mois.",
 "panda": "Chronographe à cadran clair et compteurs noirs, boîtier 39 mm, en blanc caoutchouc ou ivoire acier. Méca-quartz Seiko VK63. Livraison offerte, garantie 12 mois.",
 "champagne": "Chronographe à cadran champagne et compteurs noirs, boîtier 39 mm, bracelet acier ou caoutchouc. Méca-quartz Seiko VK63. Livraison offerte, garantie 12 mois.",
 "panda-inverse": "Chronographe à cadran noir et compteurs blancs, boîtier 39 mm, aiguille acier ou rouge. Méca-quartz Seiko VK63. Livraison offerte, garantie 12 mois.",
 "blanc": "Chronographe à cadran blanc, boîtier 39 mm, trois compteurs, bracelet acier ou caoutchouc. Méca-quartz Seiko VK63. Livraison offerte, garantie 12 mois.",
}

def tn(color, dial):
    return ("Montre automatique Miyota 8215 ou Seiko NH35, cadran %s, lunette cannelée, "
            "bracelet jubilé, 36 ou 39 mm. Livraison offerte, garantie 12 mois." % dial)

def ts(dial, extra="Livraison offerte, garantie 12 mois."):
    return ("Montre automatique Seiko NH35, cadran %s, bracelet jubilé acier, 36 ou 39 mm, "
            "étanche 10 bar. %s" % (dial, extra))

# handle, id, status, productType, old_title, old_desc, new_title (None = inchange), motif
ROWS = [
 # ---- 12 CHRONOGRAPHES (a corriger) ----
 ("contre-la-montre-bleu-glacier-chronographe", "10980083138898", "ACTIVE", "chrono",
  "Contre-la-montre Bleu glacier — Chronographe 39 mm", D_CHRONO["bleu-glacier"],
  "Contre-la-montre Bleu glacier — Montre chronographe 39 mm", "chrono"),
 ("contre-la-montre-compteurs-bleus-chronographe", "10980083007826", "ACTIVE", "chrono",
  "Contre-la-montre Compteurs bleus — Chronographe 39 mm", D_CHRONO["compteurs-bleus"],
  "Contre-la-montre Compteurs bleus — Montre chronographe 39 mm", "chrono"),
 ("contre-la-montre-argent-chronographe", "10980082778450", "ACTIVE", "chrono",
  "Contre-la-montre Argent — Chronographe 39 mm", D_CHRONO["argent"],
  "Contre-la-montre Argent — Montre chronographe 39 mm", "chrono"),
 ("contre-la-montre-gris-anthracite-chronographe", "10980081926482", "ACTIVE", "chrono",
  "Contre-la-montre Gris anthracite — Chronographe 39 mm", D_CHRONO["gris-anthracite"],
  "Contre-la-montre Gris anthracite — Montre chronographe 39 mm", "chrono"),
 ("contre-la-montre-rose-poudre-chronographe", "10980081762642", "ACTIVE", "chrono",
  "Contre-la-montre Rose poudré — Chronographe 39 mm", D_CHRONO["rose-poudre"],
  "Contre-la-montre Rose poudré — Montre chronographe 39 mm", "chrono"),
 ("contre-la-montre-vert-chronographe", "10980081631570", "ACTIVE", "chrono",
  "Contre-la-montre Vert — Chronographe 39 mm", D_CHRONO["vert"],
  "Contre-la-montre Vert — Montre chronographe 39 mm", "chrono"),
 ("contre-la-montre-turquoise-chronographe", "10980081533266", "ACTIVE", "chrono",
  "Contre-la-montre Turquoise — Chronographe 39 mm", D_CHRONO["turquoise"],
  "Contre-la-montre Turquoise — Montre chronographe 39 mm", "chrono"),
 ("contre-la-montre-noir-chronographe", "10980081041746", "ACTIVE", "chrono",
  "Contre-la-montre Noir — Chronographe 39 mm", D_CHRONO["noir"],
  "Contre-la-montre Noir — Montre chronographe 39 mm", "chrono"),
 ("contre-la-montre-panda-chronographe", "10980080976210", "ACTIVE", "chrono",
  "Contre-la-montre Panda — Chronographe 39 mm", D_CHRONO["panda"],
  "Contre-la-montre Panda — Montre chronographe 39 mm, cadran panda", "chrono"),
 ("contre-la-montre-champagne-chronographe", "10980080779602", "ACTIVE", "chrono",
  "Contre-la-montre Champagne — Chronographe 39 mm", D_CHRONO["champagne"],
  "Contre-la-montre Champagne — Montre chronographe 39 mm", "chrono"),
 ("contre-la-montre-panda-inverse-chronographe", "10980080419154", "ACTIVE", "chrono",
  "Contre-la-montre Panda inversé — Chronographe 39 mm", D_CHRONO["panda-inverse"],
  "Contre-la-montre Panda inversé — Montre chronographe 39 mm", "chrono"),
 ("contre-la-montre-blanc-chronographe", "10980078879058", "ACTIVE", "chrono",
  "Contre-la-montre Blanc — Chronographe méca-quartz 39 mm", D_CHRONO["blanc"],
  "Contre-la-montre Blanc — Montre chronographe méca-quartz 39 mm", "chrono"),

 # ---- 4 FICHES SANS seo.title ----
 ("trente-neuf-classique-cannelee", "10977444430162", "ACTIVE", "auto",
  None, None,
  "Trente-Neuf — Montre automatique homme 36/39 mm, lunette cannelée", "vide"),
 ("trente-six-classique-jubile", "10977448690002", "ACTIVE", "auto",
  None, None,
  "Trente-Six — Montre automatique homme 36/39 mm, bracelet jubilé", "vide"),
 ("trente-neuf-duo-classique-bicolore", "10977448722770", "ACTIVE", "auto",
  None, None,
  "Trente-Neuf Duo — Montre automatique homme 36/39 mm, acier et or", "vide"),
 ("quarante-et-un-sport-acier", "10977444495698", "ACTIVE", "auto",
  None, None,
  "Quarante-et-Un — Montre automatique homme 41 mm, sport acier", "vide"),

 # ---- RELECTURE DES 41 : CORRIGEES ----
 ("montre-squelette-automatique-octogone", "10988849365330", "ACTIVE", "auto",
  "Montre squelette automatique acier, calibre NH70 — Squelette Octogone",
  "Montre squelette homme : cadran ouvert sur le mouvement NH70, lunette octogonale vissée, bracelet acier. Verre saphir et étanchéité 100 m annoncés. Livraison offerte, garantie 12 mois.",
  "Montre squelette automatique acier, NH70 — Squelette Octogone", "longueur"),
 ("montre-squelette-automatique-carree", "10988849135954", "ACTIVE", "auto",
  "Montre squelette automatique carrée, calibre NH70 — Squelette Carré",
  "Montre squelette automatique : cadran ouvert, mouvement NH70 visible côté cadran. Boîtier acier carré 42 mm, verre saphir annoncé, squelette blanc ou noir. Livraison offerte, garantie 12 mois.",
  "Montre squelette automatique 42 mm, NH70 — Squelette Carré", "longueur+diametre"),
 ("montre-field-bronze-cadran-chiffres-1-12", "10988849267026", "ACTIVE", "auto",
  "Montre field militaire à chiffres 1-12, bronze — Éclaireur Bronze",
  "Montre automatique de terrain à cadran à chiffres 1-12, boîtier 36 mm en acier PVD bronze, calibre Seiko NH35. Verre saphir et étanchéité 200 m annoncés. Livraison offerte, garantie 12 mois.",
  "Montre field 36 mm à chiffres 1-12, bronze — Éclaireur Bronze", "diametre"),
 ("montre-field-acier-cadran-chiffres-1-12", "10988849234258", "ACTIVE", "auto",
  "Montre field à chiffres 1-12, acier — Éclaireur Acier",
  "Montre automatique field à cadran à chiffres 1-12, boîtier acier 39 mm, calibre Seiko NH35, Miyota 8215 ou PT5000. Verre saphir et étanchéité 200 m annoncés, bracelet cuir. Livraison offerte, garantie 12 mois.",
  "Montre field 39 mm à chiffres 1-12, acier — Éclaireur Acier", "diametre"),
 ("voyageur-bicolore-cadran-brun-gmt", "10980081664338", "ACTIVE", "auto",
  "Voyageur Bicolore cadran brun — Montre GMT automatique",
  "Montre GMT automatique bicolore à cadran brun, bracelet 5 maillons, boîtier 40 mm. Calibre DG3804 ou Seiko NH34. Livraison offerte, garantie 12 mois.",
  "Voyageur Bicolore cadran brun — Montre GMT automatique 40 mm", "diametre"),
 ("voyageur-or-rose-gmt-5-maillons", "10980081402194", "ACTIVE", "auto",
  "Voyageur Or rose — Montre GMT automatique, 5 maillons",
  "Montre GMT automatique or rose, bracelet 5 maillons, boîtier 40 mm, second fuseau. Calibre DG3804 ou Seiko NH34. Livraison offerte, garantie 12 mois.",
  "Voyageur Or rose — Montre GMT automatique 40 mm, 5 maillons", "diametre"),
 ("voyageur-bicolore-gmt-5-maillons", "10980081107282", "ACTIVE", "auto",
  "Voyageur Bicolore — Montre GMT automatique, 5 maillons",
  "Montre GMT automatique acier et or rose, bracelet 5 maillons, boîtier 40 mm. Calibre DG3804 ou Seiko NH34. Livraison offerte, garantie 12 mois.",
  "Voyageur Bicolore — Montre GMT automatique 40 mm, 5 maillons", "diametre"),
 ("voyageur-bicolore-gmt-3-maillons", "10980080845138", "ACTIVE", "auto",
  "Voyageur Bicolore — Montre GMT automatique, 3 maillons",
  "Montre GMT automatique bicolore acier et doré, bracelet 3 maillons, boîtier 40 mm. Calibre DG3804 ou Seiko NH34. Livraison offerte, garantie 12 mois.",
  "Voyageur Bicolore — Montre GMT automatique 40 mm, 3 maillons", "diametre"),
 ("voyageur-or-gmt-president", "10980079042898", "ACTIVE", "auto",
  "Voyageur Or — Montre GMT automatique, bracelet Président",
  "Montre GMT automatique dorée, bracelet Président à maillons arrondis, boîtier 40 mm. Calibre DG3804 ou Seiko NH34. Livraison offerte, garantie 12 mois.",
  "Voyageur Or — Montre GMT automatique 40 mm, bracelet Président", "diametre"),
 ("voyageur-or-gmt-3-maillons", "10980078780754", "ACTIVE", "auto",
  "Voyageur Or — Montre GMT automatique, bracelet 3 maillons",
  "Montre GMT automatique dorée, boîtier 40 mm, bracelet 3 maillons, lunette bicolore. Calibre DG3804 ou Seiko NH34. Livraison offerte, garantie 12 mois.",
  "Voyageur Or — Montre GMT automatique 40 mm, bracelet 3 maillons", "diametre"),
 ("integrale-blanc-argente-sport-chic-acier", "10980081336658", "ACTIVE", "auto",
  "Intégrale Blanc argenté — Montre automatique bracelet intégré acier",
  "Montre automatique à cadran blanc argenté texturé, boîtier et bracelet intégré en acier brossé. Seiko NH35, sans pile. Livraison offerte, garantie 12 mois.",
  "Intégrale Blanc argenté — Montre automatique bracelet intégré", "longueur"),
 ("trente-neuf-duo-dore-classique-bicolore", "10978722251090", "ACTIVE", "auto",
  "Trente-Neuf Duo Doré — Montre automatique bicolore acier et or",
  "Montre automatique bicolore acier et or, lunette cannelée, 36 ou 39 mm. Miyota 8215, Seiko NH35 ou Mingzhu 2813. Livraison offerte, garantie 12 mois.",
  "Trente-Neuf Duo Doré — Montre automatique 36/39 mm, acier et or", "diametre"),
 ("trente-neuf-noir-classique-cannelee", "10978720842066", "ACTIVE", "auto",
  "Trente-Neuf Noir — Montre automatique lunette cannelée", tn("noir", "noir brillant"),
  "Trente-Neuf Noir — Montre automatique 36/39 mm, lunette cannelée", "diametre"),
 ("trente-neuf-bleu-classique-cannelee", "10978720678226", "ACTIVE", "auto",
  "Trente-Neuf Bleu — Montre automatique lunette cannelée", tn("bleu", "bleu roi soleillé"),
  "Trente-Neuf Bleu — Montre automatique 36/39 mm, lunette cannelée", "diametre"),
 ("trente-neuf-vert-classique-cannelee", "10978720547154", "ACTIVE", "auto",
  "Trente-Neuf Vert — Montre automatique lunette cannelée", tn("vert", "vert sapin"),
  "Trente-Neuf Vert — Montre automatique 36/39 mm, lunette cannelée", "diametre"),
 ("trente-neuf-rose-classique-cannelee", "10978720317778", "ACTIVE", "auto",
  "Trente-Neuf Rose — Montre automatique lunette cannelée", tn("rose", "rose poudré"),
  "Trente-Neuf Rose — Montre automatique 36/39 mm, lunette cannelée", "diametre"),
 ("trente-neuf-bleu-mer-classique-cannelee", "10978720186706", "ACTIVE", "auto",
  "Trente-Neuf Bleu mer — Montre automatique lunette cannelée", tn("bleu mer", "bleu mer"),
  "Trente-Neuf Bleu mer — Montre automatique 36/39 mm, cannelée", "diametre"),
 ("trente-neuf-rouge-classique-cannelee", "10978720055634", "ACTIVE", "auto",
  "Trente-Neuf Rouge — Montre automatique lunette cannelée", tn("rouge", "rouge cramoisi"),
  "Trente-Neuf Rouge — Montre automatique 36/39 mm, lunette cannelée", "diametre"),
 ("trente-six-or-integral-classique-jubile", "10978719433042", "ACTIVE", "auto",
  "Trente-Six Or intégral — Montre automatique bracelet jubilé",
  "Montre automatique Seiko NH35 dorée, cadran et bracelet jubilé or jaune, 36 ou 39 mm, étanche 10 bar. Livraison offerte, garantie 12 mois.",
  "Trente-Six Or intégral — Montre automatique 36/39 mm, jubilé or", "diametre"),
 ("trente-six-dore-classique-jubile", "10978719367506", "ACTIVE", "auto",
  "Trente-Six Doré — Montre automatique bracelet jubilé acier", ts("doré champagne soleillé"),
  "Trente-Six Doré — Montre automatique 36/39 mm, jubilé acier", "diametre"),
 ("trente-six-rose-classique-jubile", "10978719236434", "ACTIVE", "auto",
  "Trente-Six Rose — Montre automatique bracelet jubilé acier", ts("rose poudré soleillé"),
  "Trente-Six Rose — Montre automatique 36/39 mm, jubilé acier", "diametre"),
 ("trente-six-bleu-classique-jubile", "10978719039826", "ACTIVE", "auto",
  "Trente-Six Bleu — Montre automatique bracelet jubilé acier",
  ts("bleu roi soleillé", "Livraison offerte en France, garantie 12 mois."),
  "Trente-Six Bleu — Montre automatique 36/39 mm, jubilé acier", "diametre"),
 ("trente-six-rouge-classique-jubile", "10978718744914", "ACTIVE", "auto",
  "Trente-Six Rouge — Montre automatique bracelet jubilé acier", ts("rouge cramoisi soleillé"),
  "Trente-Six Rouge — Montre automatique 36/39 mm, jubilé acier", "diametre"),

 # ---- RELECTURE DES 41 : LAISSEES INCHANGEES (18) ----
 ("montre-acier-chiffres-3-6-9-explorateur", "10988849299794", "ACTIVE", "auto",
  "Montre à chiffres 3-6-9, sport chic acier — Explorateur", None, None, "conforme"),
 ("heritage-vert-plongeuse-vintage-42", "10980084515154", "ACTIVE", "auto",
  "Héritage Vert — Montre automatique style plongeuse 42 mm", None, None, "conforme"),
 ("heritage-bleu-nuit-plongeuse-vintage-42", "10980084220242", "ACTIVE", "auto",
  "Héritage Bleu nuit — Montre automatique style plongeuse 42 mm", None, None, "conforme"),
 ("heritage-bleu-plongeuse-vintage-42", "10980082843986", "ACTIVE", "auto",
  "Héritage Bleu — Montre automatique style plongeuse 42 mm", None, None, "conforme"),
 ("integrale-bleu-ciel-sport-chic-acier", "10980081205586", "ACTIVE", "auto",
  "Intégrale Bleu ciel — Montre automatique bracelet intégré acier", None, None, "conforme"),
 ("integrale-bleu-nuit-sport-chic-acier", "10980081074514", "ACTIVE", "auto",
  "Intégrale Bleu nuit — Montre automatique bracelet intégré acier", None, None, "conforme"),
 ("integrale-noir-sport-chic-acier", "10980080877906", "ACTIVE", "auto",
  "Intégrale Noir — Montre automatique bracelet intégré acier", None, None, "conforme"),
 ("integrale-turquoise-sport-chic-acier", "10980080714066", "ACTIVE", "auto",
  "Intégrale Turquoise — Montre automatique bracelet intégré acier", None, None, "conforme"),
 ("integrale-brun-or-rose-sport-chic", "10980079075666", "ACTIVE", "auto",
  "Intégrale Brun or rose — Montre automatique bracelet intégré", None, None, "conforme"),
 ("integrale-vert-sport-chic-acier", "10980078911826", "ACTIVE", "auto",
  "Intégrale Vert — Montre automatique bracelet intégré acier", None, None, "conforme"),
 ("quarante-et-un-noir-cuir-sport-acier", "10978721988946", "ACTIVE", "auto",
  "Quarante-et-Un Noir — Montre automatique 41 mm bracelet cuir", None, None, "conforme"),
 ("quarante-et-un-bleu-cuir-sport-acier", "10978721857874", "ACTIVE", "auto",
  "Quarante-et-Un Bleu — Montre automatique 41 mm bracelet cuir", None, None, "conforme"),
 ("quarante-et-un-blanc-cuir-sport-acier", "10978721726802", "ACTIVE", "auto",
  "Quarante-et-Un Blanc — Montre automatique 41 mm bracelet cuir", None, None, "conforme"),
 ("quarante-et-un-noir-acier-sport-acier", "10978721530194", "ACTIVE", "auto",
  "Quarante-et-Un Noir — Montre automatique 41 mm bracelet acier", None, None, "conforme"),
 ("quarante-et-un-noir-jaune-acier-sport-acier", "10978721431890", "ACTIVE", "auto",
  "Quarante-et-Un Noir & Jaune — Montre automatique 41 mm acier", None, None, "conforme"),
 ("quarante-et-un-bleu-acier-sport-acier", "10978721235282", "ACTIVE", "auto",
  "Quarante-et-Un Bleu — Montre automatique 41 mm bracelet acier", None, None, "conforme"),
 ("montre-aviateur-bronze-cadran-chiffres-1-12", "10978722087250", "ACTIVE", "auto",
  "Montre aviateur à chiffres 1-12, bronze — Noirmont Un Bronze", None, None, "conforme"),
 ("montre-aviateur-acier-cadran-chiffres-1-12", "10977448558930", "ACTIVE", "auto",
  "Montre aviateur à chiffres 1-12, acier — Noirmont Un", None, None, "conforme"),
]

def main():
    backup, plan, errs = [], [], []
    for h, pid, st, pt, ot, od, nt, motif in ROWS:
        backup.append({"handle": h, "id": "gid://shopify/Product/" + pid,
                       "status": st, "seo_title_avant": ot, "seo_description_avant": od})
        if nt:
            n = len(nt)
            if n > 65:
                errs.append("TROP LONG %d %s" % (n, nt))
            if pt == "chrono" and "automatique" in nt.lower():
                errs.append("AUTOMATIQUE SUR CHRONO: " + nt)
            plan.append({"handle": h, "id": "gid://shopify/Product/" + pid,
                         "ancien": ot, "nouveau": nt, "len": n, "motif": motif,
                         "description_a_repasser": od})
    with open(os.path.join(OUT, "avant-seo-2026-07-30.json"), "w") as f:
        json.dump(backup, f, ensure_ascii=False, indent=1)
    with open(os.path.join(OUT, "plan-ecriture.json"), "w") as f:
        json.dump(plan, f, ensure_ascii=False, indent=1)
    print("fiches couvertes: %d | a ecrire: %d | inchangees: %d" %
          (len(ROWS), len(plan), len(ROWS) - len(plan)))
    for p in plan:
        print("%3d  %-46s %s" % (p["len"], p["motif"], p["nouveau"]))
    print("\nERREURS:", errs if errs else "aucune")

main()
