#!/usr/bin/env python3
"""Purge + rewrite client-facing product HTML for Orysbain & Lumière Matière.

Grounded in catalogues/2026-08-20-voc-personas-objections-orysbain-lm.md
Removes ops leaks (AliExpress cost, DSers, GMC validation notes).
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

FINISH_FR = {
    "chrome": "chrome",
    "noir": "noir mat",
    "or": "doré",
    "blanc": "blanc",
    "standard": "métal soigné",
}

TECH_HOOK = {
    "classique": (
        "Serviettes sèches et chaudes, sans usine à boutons.",
        "Commande simple : vous allumez pour les plages utiles (avant / après la douche), "
        "pas pour chauffer la maison 24 h/24.",
        "L’échelle murale libère le sol — utile en petite salle de bain.",
    ),
    "tactile": (
        "Un réglage au doigt, pour le confort d’après-douche.",
        "L’interface tactile évite les positions approximatives : allumez, ajustez, éteignez.",
        "Pensé pour le geste du quotidien — sans télécommande à perdre.",
    ),
    "smart": (
        "Programmez la chaleur au moment où vous en avez besoin.",
        "Les modes intelligents aident à éviter le piège du « tout allumé en continu » "
        "qui alourdit la facture sans mieux sécher les serviettes.",
        "Idéal si vous voulez du confort le matin sans surveiller l’interrupteur.",
    ),
}

COLOR_LINE = {
    "noir": "Ligne Noire",
    "chrome": "Ligne Chrome",
    "or": "Ligne Dorée",
    "blanc": "Ligne Blanche",
    "standard": "Ligne Minérale",
}

LM_COLLECTION_ANGLE = {
    "Lustres cristal": (
        "effet cristal",
        "Le verre découpe la lumière en reflets sur la table — présence sans look showroom inaccessible.",
        "Parlez d’effet cristal / verre travaillé : la magie vient du jeu de lumière, pas d’une promesse minérale.",
    ),
    "Lustres anneau": (
        "anneau",
        "Une silhouette anneau qui cadre la pièce : lumière diffuse, lecture claire du volume.",
        "Le cercle structure l’espace au-dessus d’une table ou d’un salon ouvert.",
    ),
    "Lustres salon": (
        "salon",
        "Un lustre pensé pour le salon : lumière d’ambiance d’abord, déclaration de style ensuite.",
        "Choisissez la taille en fonction de la hauteur sous plafond et de la largeur du canapé / table basse.",
    ),
    "Lustres statement": (
        "statement",
        "Une pièce forte : la lumière devient le point focal de la pièce.",
        "Vérifiez le diamètre avant commande — les photos compressent souvent l’échelle.",
    ),
    "Suspensions rotin": (
        "rotin",
        "Le rotin filtre la LED en motifs chauds — matière d’abord, ambiance ensuite.",
        "Attendez-vous à une armature interne : c’est normal ; le rendu dépend de l’ampoule (blanc chaud recommandé).",
    ),
    "Suspensions bambou": (
        "bambou",
        "Fibres naturelles, lumière tamisée : une présence végétale au-dessus de la table.",
        "Matière sensible : réception = contrôlez l’abat-jour ; entretien à sec, sans produits abrasifs.",
    ),
    "Suspensions bois": (
        "bois",
        "Le bois réchauffe le faisceau : idéal pour une salle à manger ou un îlot.",
        "Le grain et la teinte varient légèrement d’une pièce à l’autre — signe de matière, pas défaut.",
    ),
    "Suspensions pierre": (
        "pierre / effet pierre",
        "Une matière minérale qui ancre la lumière — contraste avec les murs clairs.",
        "Sauf preuve contraire, on parle d’effet pierre / composite : honnêteté sur la matière.",
    ),
    "Suspensions verre": (
        "verre",
        "Le verre laisse passer une lumière nette ou fumée selon la finition — clarté sur la table.",
        "Nettoyage doux ; évitez les chocs à l’installation.",
    ),
    "Suspensions métal": (
        "métal",
        "Laiton, noir ou doré : le métal donne une lecture graphique à la pièce.",
        "La finition se lit de près — regardez les photos détail avant de choisir la couleur.",
    ),
    "Suspensions déco": (
        "décorative",
        "Une suspension choisie pour le caractère de la pièce, pas pour un catalogue anonyme.",
        "Matière + silhouette : vérifiez diamètre et hauteur de câble sur la variante.",
    ),
    "Plafonniers": (
        "plafonnier",
        "Lumière plus rasante, plafond dégagé — utile en hauteur limitée.",
        "Idéal couloir, chambre ou pièce où une suspension basse gênerait.",
    ),
}


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def orys_title(row: dict) -> str:
    tech = row["tech"]
    color = row["color"]
    size = row.get("size") or "standard"
    line = COLOR_LINE.get(color, "Ligne Orysbain")
    tech_label = {"classique": "classique", "tactile": "tactile", "smart": "programmable"}.get(tech, tech)
    finish = FINISH_FR.get(color, color)
    slim = " slim" if size == "slim" else ""
    return f"Orysbain {line} — sèche-serviettes électrique {tech_label}{slim}, finition {finish}"


def orys_seo_title(row: dict) -> str:
    finish = FINISH_FR.get(row["color"], row["color"])
    tech = {"classique": "mural", "tactile": "tactile", "smart": "programmable"}[row["tech"]]
    return f"Sèche-serviettes électrique {tech} {finish} | Orysbain"


def orys_seo_desc(row: dict) -> str:
    finish = FINISH_FR.get(row["color"], row["color"])
    return (
        f"Sèche-serviettes électrique finition {finish} : serviettes chaudes après la douche, "
        f"pose murale, usage par plages. Livraison suivie en France — Orysbain."
    )[:320]


def orys_html(row: dict) -> str:
    tech = row["tech"]
    color = row["color"]
    size = row.get("size") or "standard"
    price = row["price_ttc"]
    finish = FINISH_FR.get(color, color)
    hook, p1, p2 = TECH_HOOK[tech]
    format_label = "slim (petit espace)" if size == "slim" else "standard"
    return f"""<div class="product-desc">
<p><strong>{esc(hook)}</strong></p>
<p>Orysbain conçoit le sèche-serviettes pour ce qu’il fait vraiment bien : <strong>sécher et réchauffer les serviettes</strong>,
avec un apport de confort dans la salle de bain — pas remplacer un radiateur principal dans une pièce mal isolée.</p>
<h3>Au quotidien</h3>
<p>{esc(p1)} Finition <strong>{esc(finish)}</strong>.</p>
<p>{esc(p2)}</p>
<h3>Caractéristiques</h3>
<ul>
<li><strong>Type :</strong> sèche-serviettes électrique — {esc(tech)}</li>
<li><strong>Finition :</strong> {esc(finish)}</li>
<li><strong>Format :</strong> {esc(format_label)}</li>
<li><strong>Alimentation :</strong> 220–240 V (usage résidentiel)</li>
<li><strong>Prix :</strong> {esc(price)} € TTC</li>
<li><strong>Pose :</strong> murale (kit) ; raccordement fixe = professionnel recommandé</li>
</ul>
<h3>Questions fréquentes</h3>
<details><summary>Est-ce un chauffage pour toute la salle de bain ?</summary>
<p>C’est d’abord un sèche-serviettes. Il apporte de la chaleur locale ; pour une grande pièce froide,
comptez un appoint ou un appareil dimensionné chauffage — sinon la déception vient de l’attente, pas de l’appareil.</p></details>
<details><summary>Ça consomme beaucoup ?</summary>
<p>La facture dépend surtout du temps d’allumage. Privilégiez des plages avant/après la douche plutôt que le 24 h/24.
Un mode minuterie ou programmable (selon modèle) aide à garder le confort sans laisser tourner inutilement.</p></details>
<details><summary>Faut-il un électricien ?</summary>
<p>Si le modèle se raccorde au réseau (pas simple prise hors zone), oui : respectez la notice et les règles des locaux humides.
Vérifiez l’indice IP indiqué sur la notice avant pose près d’un point d’eau.</p></details>
<details><summary>Odeur à la première mise sous tension ?</summary>
<p>Une légère odeur de « neuf » peut apparaître les premières heures ; aérez la pièce. Elle disparaît à l’usage.</p></details>
<p><strong>Livraison suivie en France métropolitaine. Droit de rétractation légal. SAV joignable.</strong></p>
</div>
"""


def lm_matter_key(collection: str) -> tuple[str, str, str]:
    return LM_COLLECTION_ANGLE.get(
        collection,
        (
            "matière",
            "Une suspension choisie pour sa matière et la qualité de lumière qu’elle donne à la pièce.",
            "Vérifiez diamètre, finition et type de source (LED intégrée ou douille) sur la variante.",
        ),
    )


def clean_lm_title(title: str, collection: str) -> str:
    """Keep existing title if decent; strip duplicate LED noise."""
    t = re.sub(r"\s+", " ", title).strip()
    t = re.sub(r"\bLED\s*[—\-]\s*LED\b", "LED", t, flags=re.I)
    t = re.sub(r"\bmodèle\s*0*\d+\b", "", t, flags=re.I)
    t = re.sub(r"\s{2,}", " ", t).strip(" —-")
    if len(t) < 12:
        matter, _, _ = lm_matter_key(collection)
        t = f"Suspension {matter} — Lumière Matière"
    return t


def lm_seo_title(title: str) -> str:
    base = re.sub(r"\s*\|\s*Lumière Matière\s*$", "", title, flags=re.I)
    out = f"{base} | Lumière Matière"
    return out[:70]


def lm_seo_desc(collection: str, price: str) -> str:
    matter, angle, _ = lm_matter_key(collection)
    return (
        f"{angle} Collection {collection}. Environ {price} €. "
        f"Ø et ampoule selon variante. Livraison France — Lumière Matière."
    )[:320]


def lm_html(row: dict) -> str:
    collection = row["collection"]
    price = row["price_ttc"]
    title = clean_lm_title(row["title"], collection)
    matter, angle, matter_note = lm_matter_key(collection)
    is_plafonnier = "plafonnier" in collection.lower()
    install = "plafonnier (proche plafond)" if is_plafonnier else "suspension plafond (câble / tige selon modèle)"
    return f"""<div class="product-desc">
<p><strong>{esc(angle)}</strong></p>
<p>Chez Lumière Matière, on choisit d’abord une <strong>matière</strong> — ici : <strong>{esc(matter)}</strong>.
C’est elle qui change la qualité de lumière dans la pièce — pas un catalogue de styles anonymes.</p>
<h3>Ce modèle</h3>
<p><strong>{esc(title)}</strong> — collection <strong>{esc(collection)}</strong>.</p>
<p>{esc(matter_note)}</p>
<h3>Avant de commander</h3>
<ul>
<li><strong>Échelle :</strong> notez le diamètre / l’envergure (les photos compressent souvent la taille réelle).</li>
<li><strong>Source :</strong> LED intégrée ou douille (E27/E14 selon variante) — ampoule parfois non fournie.</li>
<li><strong>Câble :</strong> longueur souvent réglable à la rosace ; trop long = à ajuster, pas un défaut.</li>
<li><strong>Pose :</strong> {esc(install)} ; faites appel à un professionnel si vous n’êtes pas à l’aise avec le raccordement.</li>
</ul>
<h3>Caractéristiques</h3>
<ul>
<li><strong>Collection :</strong> {esc(collection)}</li>
<li><strong>Usage :</strong> intérieur</li>
<li><strong>Prix :</strong> {esc(price)} € TTC</li>
<li><strong>Installation :</strong> plafond — hors volumes d’eau</li>
</ul>
<h3>Questions fréquentes</h3>
<details><summary>Le diamètre conviendra-t-il à ma table ?</summary>
<p>Repère simple : au-dessus d’une table, visez un diamètre nettement inférieur à la largeur du plateau,
et une hauteur qui laisse circuler sans heurter les têtes. En doute, mesurez avant d’acheter.</p></details>
<details><summary>Ampoule incluse ?</summary>
<p>Selon variante. Si douille : prévoyez une LED blanc chaud pour une ambiance accueillante.
Si LED intégrée : pas d’ampoule à ajouter.</p></details>
<details><summary>Est-ce du cristal / rotin « artisanal » ?</summary>
<p>Nous décrivons la matière visible sans sur-promettre. « Effet cristal », rotin, bambou, métal :
ce que vous voyez sur les photos produit — pas une usine artisanale fictive.</p></details>
<details><summary>Fragile au transport ?</summary>
<p>Ouvrez le colis dès réception et contrôlez l’abat-jour / le verre. En cas de casse, contactez le SAV avec photos.</p></details>
<p><strong>Livraison suivie en France métropolitaine. Droit de rétractation légal. SAV joignable.</strong></p>
</div>
"""


def rewrite_brand(brand: str) -> None:
    csv_path = ROOT / brand / "catalogue-dsers.csv"
    rows = list(csv.DictReader(csv_path.open(encoding="utf-8")))
    fieldnames = list(rows[0].keys())
    desc_dir = ROOT / brand / "descriptions"
    desc_dir.mkdir(exist_ok=True)

    for row in rows:
        rel = row["description_file"]
        path = ROOT / brand / rel
        if brand == "orysbain":
            row["title"] = orys_title(row)
            row["seo_title"] = orys_seo_title(row)
            row["seo_description"] = orys_seo_desc(row)
            html = orys_html(row)
        else:
            row["title"] = clean_lm_title(row["title"], row["collection"])
            row["seo_title"] = lm_seo_title(row["title"])
            row["seo_description"] = lm_seo_desc(row["collection"], row["price_ttc"])
            html = lm_html(row)
        path.write_text(html, encoding="utf-8")

    with csv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    # Refresh markdown catalogue titles for Orysbain
    if brand == "orysbain":
        md = ROOT / brand / "CATALOGUE-DSERS.md"
        lines = [
            "# Catalogue Orysbain — DSers — 2026-08-21 (copy VOC + recette)",
            "",
            f"**{len(rows)} produits.** Descriptions purgées (plus de fuites ops) + arguments VOC.",
            "",
            "Recette couleurs : `RECETTE-FINITIONS-2026-08-21.md`. Quatre SKU UV/tapis remplacés (005, 007, 008, 009).",
            "",
            "| SKU | Titre | Prix | Techno | Couleur | Lien |",
            "|---|---|---:|---|---|---|",
        ]
        for r in rows:
            sid = r["supplier_id"]
            url = r["supplier_url"]
            lines.append(
                f"| `{r['sku']}` | {r['title']} | {r['price_ttc']} € | {r['tech']} | {r['color']} | [{sid}]({url}) |"
            )
        lines.append("")
        lines.append("Descriptions dans `descriptions/`. Coûts AE = colonne interne CSV uniquement.")
        md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    else:
        md = ROOT / brand / "CATALOGUE-DSERS.md"
        lines = [
            "# Catalogue Lumière Matière — DSers — 2026-08-20 (copy VOC)",
            "",
            f"**{len(rows)} produits.** Descriptions purgées + angles matière / objections Amazon.",
            "",
            "| SKU | Collection | Titre | Prix | Lien |",
            "|---|---|---|---:|---|",
        ]
        for r in rows:
            sid = r["supplier_id"]
            url = r["supplier_url"]
            lines.append(
                f"| `{r['sku']}` | {r['collection']} | {r['title']} | {r['price_ttc']} € | [{sid}]({url}) |"
            )
        lines.append("")
        lines.append("Descriptions dans `descriptions/`. Coûts AE = colonne interne CSV uniquement.")
        md.write_text("\n".join(lines) + "\n", encoding="utf-8")


def assert_no_leaks(brand: str) -> None:
    banned = [
        "aliexpress",
        "ali express",
        "dser",
        "proxy coût",
        "proxy cout",
        "coût ae",
        "cout ae",
        "avant gmc",
        "à valider avant",
        "mappez",
        "mappez",
        "fournisseur ; mappez",
    ]
    bad = []
    for path in (ROOT / brand / "descriptions").glob("*.html"):
        text = path.read_text(encoding="utf-8").lower()
        for b in banned:
            if b in text:
                bad.append((path.name, b))
    if bad:
        raise SystemExit(f"Leaks remaining in {brand}: {bad[:10]}")


def main() -> None:
    for brand in ("orysbain", "lumierematiere"):
        rewrite_brand(brand)
        assert_no_leaks(brand)
        n = len(list((ROOT / brand / "descriptions").glob("*.html")))
        print(f"{brand}: {n} HTML rewritten, CSV+MD updated, leaks check OK")


if __name__ == "__main__":
    main()
