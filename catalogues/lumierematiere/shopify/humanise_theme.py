#!/usr/bin/env python3
"""Humanisation du texte client — thème Full Stack « copie-de-fullstack-2-3 » (25/08/2026).

Patch chirurgical de templates/index.json, sections/header-group.json et
sections/footer-group.json : chaque remplacement cible un chemin de bloc précis
et vérifie le texte attendu avant d'écrire, donc le script échoue au lieu de
diverger si la structure du thème bouge.

Objectif : plus aucun tiret cadratin ni demi-cadratin dans le texte affiché,
phrases écrites comme on parle, chiffres d'exploitation inchangés.

Deux passes cumulées, rejouables depuis l'un ou l'autre état :
1. suppression des tirets et des tournures de rédaction machine ;
2. cassure de la cadence — chaîne de titres « matière / lumière », « pièce par
   pièce », ouvertures de cartes identiques, tricolon du guide.
Chaque entrée accepte donc plusieurs textes de départ.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from apply_fullstack import theme_file, upsert_theme_file  # noqa: E402

BACKUP = ROOT / "backups" / "2026-08-25-humanisation"

EMAIL = "contact@lumierematiere.fr"
PHONE_DISPLAY = "+33 7 56 82 80 94"
PHONE_TEL = "+33756828094"
CONTACT_PATH = "/pages/contact"

HERO = "sections.image_banner_VXNP89.blocks.image_banner_dBEabG.blocks.group_nypGzr"
FEAT = "sections.collection_featured_JXRpw3.blocks.group_9NwHBp"
EDITO = "sections.custom_section_k9aPjP.blocks.group_XyMggk"
BENEF = "sections.lm_benefices_piece.blocks.group_principal"
GUIDE = "sections.lm_guide_choix.blocks.group_principal"
CTA = "sections.lm_cta_final.blocks.group_principal"
TRUST = "sections.custom_section_k6mNHc"
FOOTER = "sections.footer"

BRAND_HTML = (
    "<p>Lumière Matière rassemble des suspensions, des lustres et des plafonniers "
    "choisis pour la lumière qu’ils posent dans une pièce.</p>"
    f'<p><a href="mailto:{EMAIL}">{EMAIL}</a><br>'
    f'<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br>'
    f'<a href="{CONTACT_PATH}">Contact</a></p>'
    "<p>47 rue Vivienne, 75002 Paris<br>"
    "SAV ouvert du lundi au vendredi, de 10h à 18h (heure de Paris)</p>"
)

SAV_TRUST_HTML = (
    f'<p>Écrivez-nous à <a href="mailto:{EMAIL}">{EMAIL}</a> ou appelez le '
    f'<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.<br>'
    f'Vous pouvez aussi passer par la page <a href="{CONTACT_PATH}">Contact</a>. '
    "On répond du lundi au vendredi, de 10h à 18h (heure de Paris), "
    "sous 24 h ouvrées.</p>"
)

# (chemin du bloc, clé de setting, texte(s) accepté(s) avant, texte humanisé)
EDITS: dict[str, list[tuple[str, str, str | tuple[str, ...], str]]] = {
    "templates/index.json": [
        (
            f"{HERO}.blocks.text_8GW6GA",
            "text",
            "<p>Lumière Matière — galerie de matières. Suspensions et lustres choisis "
            "pour le bambou, le rotin, le bois, la pierre ou le verre. Le matériau "
            "change la lumière : commencez par l’ambiance.</p>",
            "<p>Chez Lumière Matière, on choisit les suspensions et les lustres pour "
            "ce dont ils sont faits. Bambou, rotin, bois, pierre ou verre, c’est la "
            "matière qui décide de l’ambiance. Alors commencez par là.</p>",
        ),
        (
            f"{HERO}.blocks.group_rFrEU8.blocks.button_JteLrC",
            "label",
            "Explorer les matières",
            "Voir les matières",
        ),
        (
            f"{HERO}.blocks.group_3Pie6V.blocks.icon_with_text_AdYCCm",
            "text",
            "<p>SAV lun–ven 10h–18h</p>",
            "<p>SAV en semaine, de 10h à 18h</p>",
        ),
        (
            f"{FEAT}.blocks.group_TwitGb.blocks.text_6LANC3",
            "text",
            (
                "<p>Une sélection de suspensions et de lustres autour de 199 € — le prix "
                "le plus courant du catalogue.</p>",
                "<p>C’est le prix qui revient le plus souvent dans le catalogue. Vous y "
                "trouverez autant de suspensions que de lustres.</p>",
                "<p>C’est le prix qui revient le plus souvent dans le catalogue. Vous y "
                "trouverez des suspensions comme des lustres.</p>",
            ),
            "<p>Les suspensions qui tiennent une pièce à vivre. Bambou, rotin, verre, "
            "pierre ou métal, choisis pour le salon.</p>",
        ),
        (
            f"{FEAT}.blocks.button_DFrQyK",
            "label",
            "Voir tous",
            "Voir les suspensions salon",
        ),
        (
            f"{EDITO}.blocks.text_34dYXd",
            "text",
            "<h2>La matière fait la lumière</h2>",
            "<h2>Ce qu’on regarde avant de mettre une pièce en ligne</h2>",
        ),
        (
            f"{EDITO}.blocks.group_6DLfAU.blocks.group_BhcLrP.blocks.icon_with_text_DCkFpJ",
            "text",
            "<p><strong>Matière visible</strong><br/>Bambou tissé, rotin, bois, pierre "
            "ou verre : la texture de la photo est celle qui joue avec la lumière "
            "chez vous.</p>",
            "<p><strong>La matière se voit</strong><br/>Bambou tissé, rotin, bois, "
            "pierre ou verre. La texture que vous voyez en photo est celle qui jouera "
            "avec la lumière chez vous.</p>",
        ),
        (
            f"{EDITO}.blocks.group_6DLfAU.blocks.group_BhcLrP.blocks.icon_with_text_bFDMHJ",
            "text",
            "<p><strong>L’échelle d’abord</strong><br/>Diamètre et hauteur de câble : "
            "les deux chiffres qui font tenir la pièce.</p>",
            "<p><strong>Les bonnes dimensions</strong><br/>Le diamètre et la hauteur "
            "de câble sont les deux chiffres qui font qu’une pièce tombe juste. On les "
            "donne sur chaque fiche.</p>",
        ),
        (
            f"{EDITO}.blocks.group_6DLfAU.blocks.group_BhcLrP.blocks.icon_with_text_D4CKhV",
            "text",
            "<p><strong>Pose et SAV</strong><br/>Un humain au bout de l’e-mail, "
            "lun–ven 10h–18h (Paris).</p>",
            "<p><strong>Une vraie personne au SAV</strong><br/>Vous écrivez, quelqu’un "
            "vous répond. Du lundi au vendredi, de 10h à 18h, heure de Paris.</p>",
        ),
        (
            "sections.custom_section_qetdex.blocks.text_PkpXrD",
            "text",
            "<p>Nouvelles pièces, conseils de diamètre et d’ampoule. Pas de remise "
            "tant qu’aucun code n’existe.</p>",
            "<p>On écrit quand une nouvelle pièce arrive, ou pour un conseil utile sur "
            "le diamètre et l’ampoule à choisir. Rien de plus.</p>",
        ),
        (
            "sections.custom_section_qetdex.blocks.group_cpEwfM.blocks.newsletter_signup_98MQp8",
            "newsletter_label",
            "Adresse email",
            "Votre adresse e-mail",
        ),
        (
            "sections.collections_matieres.blocks.title",
            "text",
            "<h2>Choisissez la matière, vous choisissez la lumière</h2>",
            "<h2>Par matière</h2>",
        ),
        (
            "sections.collections_matieres.blocks.subtitle",
            "text",
            (
                "<p>Bambou, rotin, bois, pierre, verre ou effet cristal : six matières, "
                "six manières d’habiter la même pièce.</p>",
                "<p>Bambou, rotin, bois, pierre, verre ou effet cristal. Six matières, et "
                "six façons d’éclairer la même pièce.</p>",
            ),
            "<p>Six matières au catalogue : bambou, rotin, bois, pierre, verre et effet "
            "cristal. Ouvrez celle qui vous attire, les modèles sont derrière.</p>",
        ),
        (
            f"{BENEF}.blocks.titre",
            "text",
            "<h2>Ce que la matière change, pièce par pièce</h2>",
            "<h2>Où voulez-vous de la lumière ?</h2>",
        ),
        (
            f"{BENEF}.blocks.intro",
            "text",
            (
                "<p>Le même salon change du tout au tout selon ce qui diffuse la lumière. "
                "Partez de l’endroit à éclairer : la matière suit.</p>",
                "<p>Un même salon n’a rien à voir selon ce qui diffuse la lumière. Partez "
                "de l’endroit que vous voulez éclairer, la matière viendra ensuite.</p>",
            ),
            "<p>Un même salon n’a rien à voir selon ce qui diffuse la lumière. Répondez "
            "à ça d’abord, la matière viendra ensuite.</p>",
        ),
        (
            f"{BENEF}.blocks.cartes.blocks.carte_table.blocks.contenu",
            "text",
            (
                "<p><strong>Au-dessus de la table</strong><br/>Le bambou et le rotin "
                "tamisent la lumière et la posent sur le plateau : le reste de la pièce "
                "s’adoucit, les dîners s’attardent.</p>",
                "<p><strong>Au-dessus de la table</strong><br/>Le bambou et le rotin "
                "tamisent la lumière et la posent sur le plateau. Le reste de la pièce "
                "s’adoucit et les dîners s’étirent.</p>",
            ),
            "<p><strong>Au-dessus de la table</strong><br/>Le bambou et le rotin "
            "tamisent la lumière et la posent sur le plateau. Autour, la pièce "
            "s’adoucit, et on reste plus longtemps à table.</p>",
        ),
        (
            f"{BENEF}.blocks.cartes.blocks.carte_salon.blocks.contenu",
            "text",
            (
                "<p><strong>Dans le salon</strong><br/>Un lustre anneau ou une pièce en "
                "bois donne un centre à la pièce : la lumière porte loin sans éblouir le "
                "canapé.</p>",
                "<p><strong>Dans le salon</strong><br/>Un lustre anneau ou une pièce en "
                "bois donne un centre à la pièce. La lumière porte loin sans éblouir ceux "
                "qui sont assis dans le canapé.</p>",
            ),
            "<p><strong>Dans le salon</strong><br/>Là, on cherche un point de repère au "
            "milieu de la pièce. Un lustre anneau ou du bois fait l’affaire, et la "
            "lumière porte loin sans éblouir ceux qui sont dans le canapé.</p>",
        ),
        (
            f"{BENEF}.blocks.cartes.blocks.carte_plafond.blocks.contenu",
            "text",
            (
                "<p><strong>Sous un plafond bas</strong><br/>Un plafonnier ou du verre "
                "clair garde les volumes : de la clarté partout, sans rien qui pende trop "
                "bas.</p>",
                "<p><strong>Sous un plafond bas</strong><br/>Un plafonnier ou du verre "
                "clair laisse les volumes respirer. Vous avez de la clarté partout et rien "
                "qui pende trop bas.</p>",
            ),
            "<p><strong>Sous un plafond bas</strong><br/>Pas envie de se cogner la "
            "tête. Un plafonnier ou du verre clair éclaire large, et rien ne pend au "
            "milieu du passage.</p>",
        ),
        (
            f"{GUIDE}.blocks.titre",
            "text",
            "<h2>Bien choisir, en trois étapes</h2>",
            "<h2>Bien choisir en trois étapes</h2>",
        ),
        (
            f"{GUIDE}.blocks.intro",
            "text",
            "<p>Pas besoin d’être du métier : trois décisions suffisent, et la fiche "
            "produit donne les chiffres.</p>",
            "<p>Pas besoin de s’y connaître. Trois décisions suffisent, et les chiffres "
            "sont sur chaque fiche produit.</p>",
        ),
        (
            f"{GUIDE}.blocks.etapes.blocks.etape_matiere",
            "text",
            (
                "<p><strong>1 · La matière</strong><br/>C’est elle qui fait l’ambiance : "
                "fibres tissées pour une lumière chaude striée d’ombres, verre pour une "
                "clarté nette, pierre pour un halo dense et calme.</p>",
                "<p><strong>1. La matière</strong><br/>C’est elle qui fait l’ambiance. Les "
                "fibres tissées donnent une lumière chaude striée d’ombres, le verre une "
                "clarté nette, la pierre un halo dense et calme.</p>",
            ),
            "<p><strong>1. La matière</strong><br/>C’est elle qui fait l’ambiance. Le "
            "bambou et le rotin donnent une lumière chaude, striée d’ombres. Le verre "
            "éclaire plus franchement, et la pierre pose un halo dense et calme.</p>",
        ),
        (
            f"{GUIDE}.blocks.etapes.blocks.etape_diametre",
            "text",
            (
                "<p><strong>2 · Le diamètre</strong><br/>Mesurez la table ou la zone à "
                "éclairer, puis choisissez nettement plus étroit que le plateau. Chaque "
                "fiche donne les dimensions exactes, pour acheter sans se tromper.</p>",
                "<p><strong>2. Le diamètre</strong><br/>Mesurez la table ou la zone à "
                "éclairer, puis prenez nettement plus étroit que le plateau. Les dimensions "
                "exactes sont sur chaque fiche, vous ne vous tromperez pas.</p>",
            ),
            "<p><strong>2. Le diamètre</strong><br/>Mesurez la table ou la zone à "
            "éclairer, puis prenez nettement plus étroit que le plateau. C’est le "
            "chiffre à vérifier en premier, avant même la forme.</p>",
        ),
        (
            f"{GUIDE}.blocks.etapes.blocks.etape_ampoule",
            "text",
            "<p><strong>3 · L’ampoule</strong><br/>LED intégrée ou douille (E27, "
            "parfois E14) : chaque fiche le précise. S’il faut une ampoule, une LED "
            "blanc chaud donne la lumière la plus accueillante.</p>",
            "<p><strong>3. L’ampoule</strong><br/>LED intégrée ou douille E27, parfois "
            "E14. Chaque fiche le précise. Et s’il faut une ampoule, une LED blanc "
            "chaud reste la plus accueillante.</p>",
        ),
        (
            f"{GUIDE}.blocks.cta",
            "label",
            "Toutes les réponses dans la FAQ",
            "Lire la FAQ",
        ),
        (
            f"{CTA}.blocks.titre",
            "text",
            "<h2>Commencez par la matière</h2>",
            "<h2>À vous de voir</h2>",
        ),
        (
            f"{CTA}.blocks.texte",
            "text",
            "<p>Livraison offerte en France métropolitaine, retours sous 30 jours : "
            "vous jugez la pièce chez vous, dans votre lumière.</p>",
            "<p>Livraison offerte en France métropolitaine et retours sous 30 jours. "
            "Vous jugez la pièce chez vous, dans votre lumière.</p>",
        ),
    ],
    "sections/header-group.json": [
        (
            "sections.announcement_bar_r8QCCw.blocks.announcement_y7tnxm.blocks.text_Lk3QUw",
            "text",
            "<p>Livraison offerte en France métropolitaine — sans minimum</p>",
            "<p>Livraison offerte partout en France métropolitaine, sans minimum "
            "d’achat</p>",
        ),
        (
            "sections.announcement_bar_r8QCCw.blocks.announcement_VprFGF.blocks.text_ndz4fN",
            "text",
            "<p>Retours sous 30 jours · Paiement sécurisé</p>",
            "<p>Retours sous 30 jours et paiement sécurisé</p>",
        ),
    ],
    "sections/footer-group.json": [
        (
            f"{TRUST}.blocks.group_Xb8cmj.blocks.text_QCNw3n",
            "text",
            "<p>France métropolitaine, sans minimum. Préparation 1 à 2 jours, "
            "acheminement 6 à 15 jours.</p>",
            "<p>Partout en France métropolitaine, sans minimum. Comptez 1 à 2 jours de "
            "préparation, puis 6 à 15 jours d’acheminement.</p>",
        ),
        (
            f"{TRUST}.blocks.group_r6xr7P.blocks.text_GxU484",
            "text",
            "<p>Connexion chiffrée SSL. Aucune donnée de carte n’est stockée chez "
            "nous.</p>",
            "<p>La connexion est chiffrée en SSL et aucune donnée de carte n’est "
            "conservée chez nous.</p>",
        ),
        (
            f"{TRUST}.blocks.group_wMEVzi.blocks.text_ew3NP8",
            "text",
            "<p>14 jours légaux, étendus à 30 jours. Aucun frais de "
            "réapprovisionnement.</p>",
            "<p>La loi prévoit 14 jours, nous allons jusqu’à 30. Et aucun frais de "
            "réapprovisionnement.</p>",
        ),
        (
            f"{TRUST}.blocks.group_x7TjnR.blocks.text_wDwwwK",
            "text",
            f'<p><a href="mailto:{EMAIL}">{EMAIL}</a> · '
            f'<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br>'
            f'<a href="{CONTACT_PATH}">Contact</a> · lun–ven 10h–18h (Paris) · '
            "réponse sous 24 h ouvrées.</p>",
            SAV_TRUST_HTML,
        ),
        (
            f"{FOOTER}.blocks.group_y4aNMX.blocks.text_hzJHEn",
            "text",
            "<p>Lumière Matière, c’est une galerie de matières : suspensions, lustres "
            "et plafonniers choisis pour la lumière qu’ils posent dans une pièce.</p>"
            f'<p><a href="mailto:{EMAIL}">{EMAIL}</a><br>'
            f'<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><br>'
            f'<a href="{CONTACT_PATH}">Contact</a></p>'
            "<p>47 rue Vivienne, 75002 Paris<br>"
            "SAV lun–ven 10h–18h (heure de Paris)</p>",
            BRAND_HTML,
        ),
        (
            f"{FOOTER}.blocks.menu_K3tacq",
            "title",
            "<p>Menu principal</p>",
            "<p>La boutique</p>",
        ),
        (
            f"{FOOTER}.blocks.menu_rnCAbX",
            "title",
            "<p>Informations</p>",
            "<p>Informations pratiques</p>",
        ),
        (
            f"{FOOTER}.blocks.group_BxVQwU.blocks.text_RtFCiT",
            "text",
            "<p>S'abonner à nos e-mails</p>",
            "<p>Recevoir nos e-mails</p>",
        ),
        (
            f"{FOOTER}.blocks.group_BxVQwU.blocks.newsletter_signup_tUYiRB",
            "newsletter_label",
            "Adresse email",
            "Votre adresse e-mail",
        ),
    ],
}

# Chiffres d'exploitation qui doivent rester visibles après réécriture.
OPS_TOKENS = {
    "templates/index.json": ["10h à 18h", "30 jours", "Pour le salon"],
    "sections/header-group.json": ["30 jours"],
    "sections/footer-group.json": [
        "1 à 2 jours",
        "6 à 15 jours",
        "30 jours",
        "10h à 18h",
        "24 h ouvrées",
        f"mailto:{EMAIL}",
        f"tel:{PHONE_TEL}",
        f'href="{CONTACT_PATH}"',
        "47 rue Vivienne",
    ],
}

TEXT_KEYS = {"text", "label", "title", "newsletter_label"}

# Tournures de rédaction machine à ne plus jamais voir côté client.
CADENCE_INTERDITE = (
    "galerie de matières",
    "pièce par pièce",
    "vous choisissez la lumière",
    "La matière fait la lumière",
    "six façons",
)


def settings_at(data: dict, path: str) -> dict:
    node: object = data
    for part in path.split("."):
        if not isinstance(node, dict) or part not in node:
            raise RuntimeError(f"chemin introuvable: {path} (bloque sur {part!r})")
        node = node[part]
    if not isinstance(node, dict) or "settings" not in node:
        raise RuntimeError(f"pas de settings à {path}")
    return node["settings"]


def displayed_texts(data: dict) -> list[str]:
    found: list[str] = []

    def walk(node: object) -> None:
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "settings" and isinstance(value, dict):
                    for skey, svalue in value.items():
                        if skey in TEXT_KEYS and isinstance(svalue, str):
                            found.append(svalue)
                walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(data)
    return found


def main() -> None:
    BACKUP.mkdir(parents=True, exist_ok=True)
    journal: list[tuple[str, str, str, str]] = []

    for filename, edits in EDITS.items():
        data = theme_file(filename)
        avant = BACKUP / f"{filename.replace('/', '__')}.avant-{date.today().isoformat()}"
        # L'état « avant » n'est capturé qu'une fois : une relecture du script ne doit
        # pas écraser l'original par du texte déjà humanisé.
        if not avant.exists():
            avant.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

        for path, key, expected, new in edits:
            settings = settings_at(data, path)
            current = settings.get(key)
            if current == new:
                print(f"  déjà humanisé · {path}.{key}")
                continue
            acceptes = expected if isinstance(expected, tuple) else (expected,)
            if current not in acceptes:
                raise RuntimeError(
                    f"texte inattendu à {path}.{key}\n  live: {current!r}\n  attendu: {acceptes!r}"
                )
            settings[key] = new
            journal.append((filename, f"{path}.{key}", current, new))

        affiches = displayed_texts(data)
        blob = "\n".join(affiches)
        for token in OPS_TOKENS[filename]:
            if token not in blob:
                raise RuntimeError(f"{filename}: repère perdu « {token} »")

        restants = [t for t in affiches if re.search(r"[—–]", t)]
        if restants:
            raise RuntimeError(f"{filename}: tirets restants {restants}")

        for tournure in CADENCE_INTERDITE:
            if tournure in blob:
                raise RuntimeError(f"{filename}: cadence machine « {tournure} »")

        upsert_theme_file(filename, data)
        apres = BACKUP / f"{filename.replace('/', '__')}.apres-{date.today().isoformat()}"
        apres.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

    print(f"\n{len(journal)} textes réécrits")
    if not journal:
        return
    # Journal cumulatif : une relecture sans changement ne doit pas effacer l'historique.
    piste = BACKUP / f"journal-{date.today().isoformat()}.json"
    passe = json.loads(piste.read_text()) if piste.exists() else []
    passe += [
        {"fichier": f, "chemin": p, "avant": a, "apres": n} for f, p, a, n in journal
    ]
    piste.write_text(json.dumps(passe, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
