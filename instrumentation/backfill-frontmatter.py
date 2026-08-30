#!/usr/bin/env python3
"""Ajoute un frontmatter YAML aux entrées de journal des boutiques.

Le contenu des journaux n'est jamais modifié : le bloc est inséré en tête.
Un fichier qui a déjà un frontmatter est laissé intact. Idempotent —
relançable après chaque nouvelle entrée.

    python3 instrumentation/backfill-frontmatter.py --dry-run
    python3 instrumentation/backfill-frontmatter.py --ecrire
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
JOURNAUX = sorted(RACINE.glob("boutique-*/journal/*.md"))
DATE_EN_TETE = re.compile(r"^(\d{4}-\d{2}-\d{2})-")

# Un levier = un endroit où l'on a agi. L'ordre compte : le premier motif qui
# correspond gagne pour les cas ambigus, mais tous les leviers trouvés sont gardés.
LEVIERS = {
    "prix": ["prix", "grille-prix", "tarif"],
    "sourcing": ["sourcing", "resourcing", "fournisseur", "dsers", "aliexpress",
                 "repeuplement", "import-", "push-", "file-dsers"],
    "catalogue": ["catalogue", "collections", "variantes", "decoupage", "coloris",
                  "fiches", "metachamps", "brouillons", "mapping", "renommage",
                  "elagage", "familles", "swatches", "grappes", "meres", "sku",
                  "compositions", "kit"],
    "creative": ["visuel", "image", "galerie", "photo", "shot", "badge", "fournee",
                 "illustre", "media"],
    "conformite": ["gmc", "conformite", "policies", "legales", "consentement",
                   "cookies", "avis", "veracite", "promesses", "misrepresentation",
                   "json-ld", "tracking", "crible", "marquage"],
    "seo": ["seo", "mots-cles", "serp", "titles", "nommage", "redirects", "article",
            "volumes", "semrush", "recherche-mots"],
    "page": ["uiux", "home", "panier", "collection-refonte", "copy", "textes",
             "editoriale", "usp", "gabarit", "configurateur", "arborescence",
             "charte", "design", "footer", "megamenu", "lps", "theme", "objections",
             "positionnement", "axes", "guide-de-choix", "storefront", "hero"],
    "vitesse": ["performance", "vitals", "pagespeed"],
    "technique": ["fix", "correctif", "correction", "regression", "cli", "api",
                  "reparation", "technique", "build", "preflight", "reconciliation"],
    "ads": ["ads", "campagne", "pmax"],
    "offre": ["offre", "bundle", "coffret", "kit-"],
    "concurrence": ["concurrent", "concurrence", "etude-", "mining", "marche"],
}

# Une entrée qui mesure ou audite sans rien changer.
MOTS_ANALYSE = ["audit", "analyse", "etude", "verification", "mining", "bilan",
                "mots-cles", "serp", "volumes", "concurrent", "recherche", "plan-",
                "spec-", "brief", "dossier", "decision", "consignes", "prompt"]


def leviers_de(nom: str, titre: str) -> list[str]:
    base = f"{nom} {titre}".lower()
    trouves = [levier for levier, motifs in LEVIERS.items()
               if any(m in base for m in motifs)]
    return trouves or ["autre"]


def nature_de(nom: str) -> str:
    return "analyse" if any(m in nom.lower() for m in MOTS_ANALYSE) else "intervention"


def titre_de(texte: str) -> str:
    for ligne in texte.splitlines():
        if ligne.startswith("# "):
            return ligne[2:].strip().replace('"', "'")
    return ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ecrire", action="store_true", help="écrit vraiment (sinon dry-run)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    traites = deja = ignores = 0
    apercu: list[str] = []

    for chemin in JOURNAUX:
        m = DATE_EN_TETE.match(chemin.name)
        if not m:
            ignores += 1
            continue

        texte = chemin.read_text(encoding="utf-8")
        if texte.startswith("---\n"):
            deja += 1
            continue

        boutique = chemin.parent.parent.name.removeprefix("boutique-")
        titre = titre_de(texte)
        leviers = leviers_de(chemin.stem, titre)
        bloc = (
            "---\n"
            "type: journal\n"
            f"boutique: {boutique}\n"
            f"date: {m.group(1)}\n"
            f"nature: {nature_de(chemin.stem)}\n"
            f"leviers: [{', '.join(leviers)}]\n"
            f'titre: "{titre}"\n'
            "---\n\n"
        )
        if args.ecrire:
            chemin.write_text(bloc + texte, encoding="utf-8")
        else:
            apercu.append(f"{boutique:12} {m.group(1)}  {nature_de(chemin.stem):12} "
                          f"{','.join(leviers):40} {chemin.name}")
        traites += 1

    if apercu:
        print("\n".join(apercu))
    print(f"\n{traites} à traiter · {deja} déjà pourvus · {ignores} ignorés (pas une entrée datée)")
    if not args.ecrire:
        print("DRY-RUN — relancer avec --ecrire pour appliquer")
    return 0


if __name__ == "__main__":
    sys.exit(main())
