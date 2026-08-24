#!/usr/bin/env python3
"""Génère les titres SEO, USP, specs, 3 bénéfices et FAQ — une fiche, un texte."""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent

CM_RE = re.compile(r"(?:Ø\s*)?(\d+)\s*cm", re.I)
COLOR_WORDS = [
    ("gris fumé", "Gris fumé"),
    ("transparent", "Transparent"),
    ("argenté", "Argenté"),
    ("cognac", "Cognac"),
    ("ambre", "Ambre"),
    ("doré", "Doré"),
    ("dore", "Doré"),
    ("gold", "Doré"),
    ("golden", "Doré"),
    ("gloden", "Doré"),
    ("noir", "Noir"),
    ("black", "Noir"),
    ("blanc", "Blanc"),
    ("white", "Blanc"),
    ("café", "Café"),
    ("cafe", "Café"),
    ("chrome", "Chrome"),
    ("beige", "Beige"),
    ("kaki", "Kaki"),
    ("khaki", "Kaki"),
    ("noyer", "Noyer"),
    ("walnut", "Noyer"),
    ("chanvre", "Chanvre"),
    ("hemp", "Chanvre"),
    ("laiton", "Laiton"),
    ("naturel", "Naturel"),
]

FAMILIES = {
    "Suspensions bambou": {
        "kind": "suspension",
        "matter": "bambou tissé",
        "title_base": "Suspension bambou tissée",
        "kw": "suspension bambou",
        "usp_matter": "Bambou tissé",
        "usage": "au-dessus d’une table, d’un îlot ou dans une entrée",
        "entretien": "un chiffon sec, sans eau ni produit abrasif : les fibres n’aiment pas l’humidité stagnante",
        "material_faq": "Du bambou tissé, celui que montrent les photos. Les fibres varient légèrement de teinte d’une pièce à l’autre.",
        "b1_title": "La lumière passe à travers le tressage",
        "b2_title": "Le diamètre décide de la table",
        "b3_title": "Une présence végétale, même éteinte",
    },
    "Suspensions rotin": {
        "kind": "suspension",
        "matter": "rotin tressé",
        "title_base": "Suspension rotin tressée",
        "kw": "suspension rotin",
        "usp_matter": "Rotin tressé",
        "usage": "au-dessus d’un coin repas, d’un salon ou d’une chambre",
        "entretien": "un chiffon sec ; le rotin ne se lave pas à l’eau",
        "material_faq": "Du rotin tressé, plus souple et plus miel que le bambou. La teinte varie un peu d’une pièce à l’autre.",
        "b1_title": "Le tressage strie la lumière",
        "b2_title": "Un volume léger au-dessus de la pièce",
        "b3_title": "Le miel du rotin, allumé ou éteint",
    },
    "Suspensions bois": {
        "kind": "suspension",
        "matter": "bois",
        "title_base": "Suspension bois",
        "kw": "suspension bois",
        "usp_matter": "Bois",
        "usage": "au-dessus d’une table de salle à manger ou en chambre",
        "entretien": "un chiffon sec, sans cire ni détergent",
        "material_faq": "Du bois (lamelles, placage ou abat-jour tourné selon le modèle). Le veinage diffère d’une pièce à l’autre.",
        "b1_title": "Une lumière que le bois absorbe",
        "b2_title": "Chaude au-dessus de la table",
        "b3_title": "Le veinage fait l’objet",
    },
    "Suspensions pierre": {
        "kind": "suspension",
        "matter": "composite à grain minéral",
        "title_base": "Suspension effet pierre",
        "kw": "suspension pierre",
        "usp_matter": "Effet pierre",
        "usage": "au-dessus d’une table ou d’un lit",
        "entretien": "un chiffon doux, sans abrasif qui rayerait le grain",
        "material_faq": "Un composite à grain minéral, plus léger qu’un bloc de pierre. L’effet albâtre ou travertin vient de cette surface, pas d’une pierre massive.",
        "b1_title": "Une clarté laiteuse, comme l’albâtre",
        "b2_title": "Le grain se lit une fois allumé",
        "b3_title": "Plus simple à suspendre qu’un bloc",
    },
    "Suspensions verre": {
        "kind": "suspension",
        "matter": "verre",
        "title_base": "Suspension verre",
        "kw": "suspension verre",
        "usp_matter": "Verre",
        "usage": "au-dessus d’un îlot, d’une table ou en ligne de globes",
        "entretien": "un chiffon microfibre ; la poussière se voit vite sur le verre",
        "material_faq": "Du verre — fumé, opalin, ambre ou transparent selon la variante. Ce n’est pas du cristal de marque.",
        "b1_title": "La lumière traverse et se teinte",
        "b2_title": "Globes, cloches, grappes",
        "b3_title": "Un verre qui se tient propre",
    },
    "Lustres cristal": {
        "kind": "lustre",
        "matter": "verre travaillé",
        "title_base": "Lustre effet cristal",
        "kw": "lustre cristal",
        "usp_matter": "Effet cristal",
        "usage": "au-dessus d’une table, dans un salon ou une cage d’escalier",
        "entretien": "un plumeau ou un chiffon microfibre, sans produit agressif sur les facettes",
        "material_faq": "Du verre travaillé — facetté, strié ou taillé en gouttes. « Effet cristal » décrit ce jeu d’arêtes, pas un cristal de marque ni un lustre ancien.",
        "b1_title": "Le verre fragmente la lumière",
        "b2_title": "Un dessin contemporain, pas un lustre d’époque",
        "b3_title": "Baissée, la lumière scintille",
    },
    "Lustres anneau": {
        "kind": "lustre",
        "matter": "anneau LED",
        "title_base": "Lustre anneau LED",
        "kw": "lustre anneau",
        "usp_matter": "Anneau LED",
        "usage": "au-dessus d’une table ronde ou au centre d’un salon",
        "entretien": "un chiffon sec sur le profilé ; pas d’ampoule à changer",
        "material_faq": "Un ou plusieurs cercles avec LED logée dans le profilé. Pas d’ampoule visible, pas d’ampoule à ajouter.",
        "b1_title": "Un cercle de lumière, sans ampoule visible",
        "b2_title": "Un, deux ou plusieurs anneaux",
        "b3_title": "L’envergure compte plus que le nombre",
    },
    "Lustres salon": {
        "kind": "lustre",
        "matter": "métal et lumière",
        "title_base": "Lustre salon",
        "kw": "lustre salon",
        "usp_matter": "Lustre de salon",
        "usage": "au centre du séjour, assez haut pour traverser sans baisser la tête",
        "entretien": "un chiffon doux sur la structure ; LED intégrée ou douille selon la variante",
        "material_faq": "Un lustre pensé pour une pièce à vivre — anneaux, branches ou verre, selon le modèle. Les photos font foi.",
        "b1_title": "Le point haut de la pièce à vivre",
        "b2_title": "Dimensionnez-le à la pièce",
        "b3_title": "La lumière du soir part de là",
    },
    "Plafonniers": {
        "kind": "plafonnier",
        "matter": "plafonnier LED",
        "title_base": "Plafonnier LED",
        "kw": "plafonnier",
        "usp_matter": "Plafonnier LED",
        "usage": "en chambre, couloir ou pièce basse, là où une suspension gênerait",
        "entretien": "un chiffon sec sur le diffuseur",
        "material_faq": "Un plafonnier d’intérieur, plaqué au plafond, hors volumes d’eau. Ce n’est pas un modèle salle de bain ni un ventilateur.",
        "b1_title": "Collé au plafond, rien ne descend",
        "b2_title": "La pièce basse trouve sa lumière",
        "b3_title": "Une nappe régulière, pas un spot",
    },
    "Suspensions métal": {
        "kind": "suspension",
        "matter": "métal",
        "title_base": "Suspension métal",
        "kw": "suspension métal",
        "usp_matter": "Métal",
        "usage": "au-dessus d’un îlot de cuisine ou d’une table",
        "entretien": "un chiffon sec, sans abrasif qui marquerait la finition",
        "material_faq": "Un abat-jour en métal — noir, doré ou aspect laiton selon la variante. Le faisceau part vers le bas.",
        "b1_title": "Un faisceau net, dirigé vers le bas",
        "b2_title": "Noir graphique ou doré chaud",
        "b3_title": "Deux ou trois dômes sur un îlot",
    },
    "Suspensions déco": {
        "kind": "suspension",
        "matter": "céramique émaillée",
        "title_base": "Suspension déco en céramique",
        "kw": "suspension déco",
        "usp_matter": "Céramique émaillée",
        "usage": "en accent : comptoir, couloir, chevet",
        "entretien": "un chiffon doux sur l’émail",
        "material_faq": "De la céramique émaillée. L’émail peut présenter de légères variations de teinte, liées à la cuisson.",
        "b1_title": "La forme d’abord, la lumière ensuite",
        "b2_title": "Un accent plutôt qu’un lustre",
        "b3_title": "L’émail renvoie un satiné",
    },
    "Lustres statement": {
        "kind": "lustre",
        "matter": "structure rayonnante",
        "title_base": "Lustre statement",
        "kw": "lustre statement",
        "usp_matter": "Grand lustre",
        "usage": "dans un séjour ou une cage d’escalier qui offre de la hauteur",
        "entretien": "un chiffon sec sur les branches ; LED intégrée",
        "material_faq": "Une seule pièce, choisie pour son envergure. Mesurez la hauteur libre avant de commander.",
        "b1_title": "Un geste qui occupe le vide",
        "b2_title": "Toute la lumière du soir part de là",
        "b3_title": "Mesurez avant de l’accrocher",
    },
    "Suspensions modernes": {
        "kind": "suspension",
        "matter": "structure épurée",
        "title_base": "Suspension design",
        "kw": "suspension design",
        "usp_matter": "Dessin épuré",
        "usage": "au-dessus d’une table ou au centre d’un séjour contemporain",
        "entretien": "un chiffon sec ; LED intégrée, pas d’ampoule à ajouter",
        "material_faq": "Une structure noire, LED intégrée, peu d’éléments autour. Une seule pièce dans cette collection.",
        "b1_title": "Peu de choses, bien tenues",
        "b2_title": "La source ne se voit pas",
        "b3_title": "Calme au-dessus de la table",
    },
}


def et_join(items: list[str]) -> str:
    items = [x for x in items if x]
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    return f"{', '.join(items[:-1])} et {items[-1]}"


def option_map(options: list[dict]) -> dict[str, list[str]]:
    return {o["name"]: list(o["values"]) for o in options}


def diameters_cm(options: list[dict]) -> list[int]:
    found: list[int] = []
    for opt in options:
        for val in opt["values"]:
            for n in CM_RE.findall(val):
                num = int(n)
                if 8 <= num <= 250:
                    found.append(num)
    return sorted(set(found))


def colors_of(options: list[dict]) -> list[str]:
    out: list[str] = []
    for opt in options:
        if opt["name"] not in {"Couleur", "Finition"} and not (
            opt["name"] == "Taille" and any(any(w in v.lower() for w, _ in COLOR_WORDS) for v in opt["values"])
        ):
            if opt["name"] not in {"Couleur", "Finition"}:
                continue
        for val in opt["values"]:
            low = val.lower()
            matched = None
            for needle, label in COLOR_WORDS:
                if needle in low:
                    matched = label
                    break
            if matched and matched not in out:
                out.append(matched)
    return out


def detect_source(handle: str, title: str, options: list[dict]) -> str:
    blob = " ".join(
        [handle, title] + [v for o in options for v in o["values"]] + [o["name"] for o in options]
    ).lower()
    e27 = "e27" in blob or "ampoule non fournie" in blob or "sans ampoule" in blob
    led = "led" in blob or "intégrée" in blob or "integree" in blob
    remote = "télécommande" in blob or "telecommande" in blob or "variable" in blob
    teintes = "3 teintes" in blob or "tri color" in blob
    if e27 and led:
        return "mixte"
    if e27:
        return "e27"
    if led or remote or teintes:
        return "led"
    if "plafonnier" in handle:
        return "led"
    return "mixte"


def source_label(source: str) -> str:
    return {
        "led": "LED intégrée",
        "e27": "Douille E27",
        "mixte": "LED ou douille E27",
    }[source]


def diam_phrase(cms: list[int]) -> str:
    if not cms:
        return ""
    if len(cms) == 1:
        return f"Ø {cms[0]} cm"
    return f"Ø {cms[0]}–{cms[-1]} cm"


def build_title(family: dict, source: str, cms: list[int], colors: list[str], handle: str, options: list[dict]) -> str:
    base = family["title_base"]
    bits: list[str] = []
    if source == "led" and "LED" not in base:
        bits.append("LED")
    lights: list[int] = []
    for opt in options:
        for val in opt["values"]:
            for n in re.findall(r"(\d+)\s*lumières", val, re.I):
                lights.append(int(n))
    if lights:
        bits.append(et_join([f"{n} lumières" for n in sorted(set(lights))]))
    dp = diam_phrase(cms)
    if dp:
        bits.append(dp)
    elif "60cm" in handle or "60-cm" in handle:
        bits.append("Ø 60 cm")
    elif "80-cm" in handle or "80cm" in handle:
        bits.append("Ø 80 cm")
    elif "50cm" in handle:
        bits.append("Ø 50 cm")
    elif "45cm" in handle:
        bits.append("Ø 45 cm")
    elif "30cm" in handle:
        bits.append("Ø 30 cm")
    if "dore" in handle and "Doré" not in colors:
        colors = ["Doré"] + colors
    if "noir" in handle and "Noir" not in colors:
        colors = ["Noir"] + colors
    if "blanc" in handle and "Blanc" not in colors:
        colors = ["Blanc"] + colors
    if len(colors) == 1:
        bits.append(colors[0].lower())
    elif 1 < len(colors) <= 3 and not lights:
        bits.append(et_join([c.lower() for c in colors]))
    if family["kind"] == "plafonnier" and "intérieur" not in base.lower():
        bits.append("intérieur")
    if not bits:
        return base
    title = f"{base}, {', '.join(bits)}"
    if len(title) > 78 and len(bits) > 2:
        title = f"{base}, {', '.join(bits[:2])}"
    return title


def seo_title(title: str) -> str:
    suffix = " | Lumière Matière"
    max_len = 70
    if len(title) + len(suffix) <= max_len:
        return title + suffix
    cut = max_len - len(suffix)
    chunk = title[:cut].rsplit(" ", 1)[0].rstrip(" ,")
    return chunk + suffix


def seo_description(family: dict, title: str, source: str, cms: list[int], colors: list[str]) -> str:
    dp = diam_phrase(cms)
    col = f" Finitions {et_join([c.lower() for c in colors])}." if colors else ""
    src = source_label(source)
    size = f" {dp}." if dp else ""
    text = (
        f"{title} — {family['matter']}, {src.lower()}.{size}{col} "
        f"Livraison offerte en France. Diamètre et source indiqués sur la fiche."
    )
    return text[:320]


def usps(family: dict, source: str, cms: list[int], colors: list[str], options: list[dict]) -> list[str]:
    pills = [family["usp_matter"], source_label(source)]
    dp = diam_phrase(cms)
    if dp:
        pills.append(dp)
    blob = " ".join(v for o in options for v in o["values"]).lower()
    if "télécommande" in blob or "variable" in blob:
        pills.append("Variable (télécommande)")
    elif "3 teintes" in blob:
        pills.append("3 teintes")
    if family["kind"] == "plafonnier":
        pills.append("Plafond bas")
    elif len(pills) < 4 and colors:
        pills.append(colors[0])
    # max 4, unique
    seen = []
    for p in pills:
        if p not in seen:
            seen.append(p)
    return seen[:4]


def description_html(family: dict, title: str, source: str, cms: list[int], colors: list[str]) -> str:
    dp = diam_phrase(cms)
    size = f" Les diamètres proposés vont de {cms[0]} à {cms[-1]} cm." if len(cms) > 1 else (f" Diamètre {dp}." if dp else "")
    col = f" Finitions : {et_join([c.lower() for c in colors])}." if colors else ""
    src = {
        "led": "La LED est intégrée : pas d’ampoule à ajouter.",
        "e27": "Douille E27 : prévoyez une LED blanc chaud, l’ampoule n’est pas fournie.",
        "mixte": "Selon la variante : LED intégrée, ou douille E27 sans ampoule.",
    }[source]
    det = "Cette" if family["kind"] == "suspension" else "Ce"
    pron = "Elle" if family["kind"] == "suspension" else "Il"
    p1 = (
        f"<p>{det} <strong>{family['kw']}</strong> travaille d’abord la matière : {family['matter']}. "
        f"{pron} se place {family['usage']}.</p>"
    )
    p2 = f"<p>{src}{size}{col} Les photos du modèle font foi : mesurez votre pièce avant de choisir le diamètre.</p>"
    return p1 + p2


def specs_html(family: dict, source: str, cms: list[int], colors: list[str], options: list[dict], price: str | None) -> str:
    rows = [
        f"<li><strong>Type :</strong> {family['title_base']}</li>",
        f"<li><strong>Matière :</strong> {family['matter']}</li>",
        f"<li><strong>Usage :</strong> intérieur, hors volumes d’eau</li>",
        f"<li><strong>Source :</strong> {source_label(source).lower()}</li>",
    ]
    if cms:
        rows.append(f"<li><strong>Diamètre :</strong> {et_join([str(c) + ' cm' for c in cms])}</li>")
    if colors:
        rows.append(f"<li><strong>Finitions :</strong> {et_join(colors)}</li>")
    temps = []
    for opt in options:
        if "empérature" in opt["name"] or opt["name"] == "Éclairage":
            temps = [v for v in opt["values"] if "entrepôt" not in v.lower() and "chine" not in v.lower()]
    if temps:
        rows.append(f"<li><strong>Lumière :</strong> {et_join(temps[:6])}</li>")
    if price:
        rows.append(f"<li><strong>Prix :</strong> à partir de {price.replace('.00', '')} € TTC selon variante</li>")
    rows.append("<li><strong>Installation :</strong> plafond — courant coupé, hors salle de bain</li>")
    return "<ul>" + "".join(rows) + "</ul>"


def installation_html(family: dict, source: str) -> str:
    if family["kind"] == "plafonnier":
        pose = (
            "Le plafonnier se plaque au plafond : pas de câble apparent. "
            "Convient aux pièces dont la hauteur descend sous 2,50 m, aux chambres et aux couloirs."
        )
    else:
        pose = (
            "Fixation au plafond, hors volumes d’eau. Le câble se coupe ou s’enroule à la rosace pour régler la hauteur. "
            "On doit pouvoir circuler sans heurter le luminaire."
        )
    src = {
        "led": "LED intégrée : raccordez phase / neutre / terre, sans douille à équiper.",
        "e27": "Vissez une LED E27 après la pose. Ampoule non fournie.",
        "mixte": "Selon la variante : raccordement LED, ou douille E27 à équiper.",
    }[source]
    sav = (
        "Coupez le courant. Si le raccordement n’est pas une opération que vous maîtrisez, "
        "faites appel à un électricien. Notice jointe au colis."
    )
    return f"<p>{pose}</p><p>{src}</p><p>{sav}</p>"


def benefits(family: dict, source: str, cms: list[int], colors: list[str], title: str) -> list[dict]:
    dp = diam_phrase(cms)
    size_txt = (
        f"Les diamètres {et_join([str(c) + ' cm' for c in cms])} sont ceux de cette fiche : "
        f"au-dessus d’une table, visez un diamètre nettement plus étroit que le plateau."
        if cms
        else "Mesurez la table ou la pièce avant de commander : les photos compressent souvent l’échelle."
    )
    col_txt = (
        f"Les finitions {et_join([c.lower() for c in colors])} changent le dialogue avec le mur et le meuble."
        if colors
        else "La finition que vous voyez sur les photos est celle que vous recevez."
    )
    src_txt = {
        "led": "La LED est déjà dans la pièce : température selon la variante, parfois réglable.",
        "e27": "Vous choisissez l’ampoule : une LED blanc chaud suffit pour une pièce à vivre.",
        "mixte": "Regardez la variante : LED intégrée, ou douille E27 à équiper.",
    }[source]
    bodies = {
        "Suspensions bambou": [
            f"Le tressage ne laisse pas passer un faisceau cru : il le découpe. Allumée, la vannerie apparaît nervure par nervure. {src_txt}",
            size_txt + " Un dôme trop large écrase une petite table ; trop étroit, il disparaît.",
            f"Éteinte, le bambou reste un volume chaud. {family['entretien'].capitalize()}. {col_txt}",
        ],
        "Suspensions rotin": [
            f"Le rotin filtre la lumière en raies fines. Plus miel que le bambou, plus souple dans la courbe. {src_txt}",
            size_txt,
            f"Même éteint, le panier tient comme un objet de vannerie. {col_txt}",
        ],
        "Suspensions bois": [
            f"Le bois absorbe au lieu de renvoyer. La pièce se réchauffe sans éclat. {src_txt}",
            size_txt + " Au-dessus d’une table, la chaleur de la matière compte plus que les watts.",
            f"Le veinage diffère d’une pièce à l’autre. {col_txt}",
        ],
        "Suspensions pierre": [
            f"Le grain minéral retient le faisceau et le rend laiteux. Ce n’est pas un bloc de pierre : un composite plus léger, même effet à l’œil. {src_txt}",
            size_txt,
            f"Allumée, la surface se réveille de l’intérieur. {col_txt}",
        ],
        "Suspensions verre": [
            f"La lumière traverse, se teinte, et dépose des reflets. Verre fumé pour le soir, opalin pour élargir. {src_txt}",
            size_txt + " Une ligne de globes tient un îlot ; une grappe tient une table.",
            f"{family['entretien'].capitalize()}. {col_txt}",
        ],
        "Lustres cristal": [
            f"Le verre travaillé éclate le faisceau en points brillants. Effet cristal de facettes, pas un lustre Baccarat. {src_txt}",
            size_txt + " Il lui faut un peu de hauteur sous plafond.",
            "Sur un variateur, baissée, cette lumière devient scintillante plutôt qu’éclatante.",
        ],
        "Lustres anneau": [
            f"La LED est dans le profilé : un cercle, pas une masse, pas d’ampoule visible. {src_txt}",
            size_txt + " Un anneau pour une table ronde ; plusieurs cercles pour une pièce haute.",
            "L’envergure totale, indiquée sur chaque variante, décide de l’effet — plus que le nombre d’anneaux.",
        ],
        "Lustres salon": [
            f"C’est le point haut du séjour : trop petit, il disparaît. {src_txt}",
            "Repère : longueur + largeur de la pièce en mètres, le chiffre en centimètres donne un diamètre de départ. " + size_txt,
            "On doit traverser le salon sans baisser la tête. " + col_txt,
        ],
        "Plafonniers": [
            f"Rien ne descend : la lumière reste au-dessus des têtes. {src_txt}",
            "Dès que la hauteur passe sous 2,50 m, au-dessus d’un lit ou dans un couloir, le plafonnier gagne. " + size_txt,
            "Hors volumes d’eau. Ce n’est ni un modèle salle de bain, ni un ventilateur. " + col_txt,
        ],
        "Suspensions métal": [
            f"Le métal dirige : abat-jour vers le bas, halo net sur le plan de travail. {src_txt}",
            size_txt + " En cuisine, deux ou trois dômes alignés tiennent un îlot.",
            col_txt + " Chiffon sec uniquement.",
        ],
        "Suspensions déco": [
            f"On la choisit pour sa forme : céramique émaillée, volume bombé, objet autant qu’éclairage. {src_txt}",
            "Comptoir, couloir, chevet : un accent, pas un lustre de salon. " + size_txt,
            col_txt + " L’émail varie un peu à la cuisson.",
        ],
        "Lustres statement": [
            f"Une seule pièce, pour un séjour ou un escalier qui offre du vide. {src_txt}",
            "Mesurez la hauteur libre sous le luminaire et comparez-la à l’envergure. " + size_txt,
            "Pour un plafond bas, un anneau ou un plafonnier convient mieux.",
        ],
        "Suspensions modernes": [
            f"Géométrie lisible, source invisible, rien autour. {src_txt}",
            size_txt + " Elle tient au-dessus d’une table comme au centre d’un séjour.",
            "Matières mates — béton, bois brut, lin — autour. " + col_txt,
        ],
    }
    key = next(k for k, v in FAMILIES.items() if v is family)
    texts = bodies[key]
    return [
        {"title": family["b1_title"], "body": texts[0]},
        {"title": family["b2_title"], "body": texts[1]},
        {"title": family["b3_title"], "body": texts[2]},
    ]


def faq(family: dict, source: str, cms: list[int]) -> list[dict]:
    if cms:
        q1 = f"Le diamètre ({diam_phrase(cms)}) conviendra-t-il à ma table ?"
        a1 = (
            f"Les tailles de cette fiche : {et_join([str(c) + ' cm' for c in cms])}. "
            "Au-dessus d’une table, visez un diamètre nettement inférieur à la largeur du plateau, "
            "et une hauteur qui laisse passer sans heurter les têtes."
        )
    else:
        q1 = "Comment choisir la taille ?"
        a1 = "Reportez-vous aux dimensions indiquées sur les variantes. Les photos compressent souvent l’échelle : mesurez avant d’acheter."
    if family["kind"] == "plafonnier":
        q1 = "Plafonnier ou suspension ?"
        a1 = (
            "Le plafonnier se plaque au plafond : pièces basses, chambres, couloirs. "
            "La suspension garde l’avantage au-dessus d’une table, où la descente crée l’intimité. "
            + (f"Diamètres proposés : {et_join([str(c) + ' cm' for c in cms])}." if cms else "")
        )
    a2 = {
        "led": "Non : la LED est intégrée. Pas d’ampoule à ajouter, pas d’ampoule à changer au quotidien.",
        "e27": "Non : douille E27, ampoule non fournie. Prévoyez une LED blanc chaud (environ 2700–3000 K) pour une pièce à vivre.",
        "mixte": "Selon la variante. LED intégrée : rien à ajouter. Douille E27 : ampoule non fournie.",
    }[source]
    q4 = "Quel délai de livraison ?"
    a4 = (
        "Livraison offerte en France métropolitaine. Préparation 1 à 2 jours ouvrés, "
        "acheminement 6 à 15 jours ouvrés, total 7 à 17 jours ouvrés. Heure limite 16h00, heure de Paris."
    )
    return [
        {"q": q1, "a": a1},
        {"q": "L’ampoule est-elle fournie ?", "a": a2},
        {"q": "Quelle est la matière exactement ?", "a": family["material_faq"]},
        {"q": q4, "a": a4},
    ]


def handle_hint(handle: str) -> str:
    skip = {
        "suspension",
        "lustre",
        "led",
        "plafonnier",
        "effet",
        "pierre",
        "bambou",
        "rotin",
        "bois",
        "verre",
        "metal",
        "anneau",
        "salon",
        "cristal",
        "deco",
        "moderne",
        "statement",
    }
    parts = [p for p in handle.split("-") if p not in skip and not p.isdigit() and len(p) > 1]
    labels = {"dore": "doré", "noir": "noir", "blanc": "blanc", "cm": None}
    out = []
    for p in parts:
        if p in labels:
            if labels[p]:
                out.append(labels[p])
        elif not p.isnumeric():
            out.append(p)
    return " ".join(out[:3])


def uniquify_titles(copies: dict[str, dict]) -> None:
    for c in copies.values():
        c.pop("_cms", None)
        c.pop("_hint", None)


def build_one(row: dict) -> dict:
    ptype = row.get("type") or row.get("productType") or ""
    family = FAMILIES.get(ptype) or FAMILIES["Suspensions bambou"]
    options = row["options"]
    cms = diameters_cm(options)
    colors = colors_of(options)
    source = detect_source(row["handle"], row.get("title") or "", options)
    title = build_title(family, source, cms, colors, row["handle"], options)
    # strip leftover reference numbers from becoming titles
    title = re.sub(r"\s*·\s*\d{4,}$", "", title)
    return {
        "title": title,
        "seo_title": seo_title(title),
        "seo_description": seo_description(family, title, source, cms, colors),
        "usps": usps(family, source, cms, colors, options),
        "description_html": description_html(family, title, source, cms, colors),
        "specs_html": specs_html(family, source, cms, colors, options, row.get("price")),
        "installation_html": installation_html(family, source),
        "benefits": benefits(family, source, cms, colors, title),
        "faq": faq(family, source, cms),
        "_cms": cms,
        "_hint": handle_hint(row["handle"]),
    }


def build_all(rows: list[dict]) -> dict[str, dict]:
    copies = {row["handle"]: build_one(row) for row in rows}
    uniquify_titles(copies)
    return copies


if __name__ == "__main__":
    rows = json.loads((ROOT / "pdp-options-live.json").read_text(encoding="utf-8"))
    copies = build_all(rows)
    out = ROOT / "pdp-copy.json"
    out.write_text(json.dumps(copies, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    titles = [c["title"] for c in copies.values()]
    print(f"{len(copies)} fiches, titres uniques {len(set(titles))}/{len(titles)}")
    for h in list(copies)[:5]:
        c = copies[h]
        print(h, "→", c["title"], "|", " · ".join(c["usps"]))
