#!/usr/bin/env python3
"""Positionnement des variantes Lumière Matière : delete junk, traduire, réduire.

Règles (25/08/2026) :
- jamais toucher aux sku / sku_attr DSers des variantes conservées ;
- « Damaged replacement » et consorts = pièce détachée AliExpress → suppression ;
- libellés FR compréhensibles (line → couleur seule, heads → lumières, codes usine → finitions) ;
- cible ≤ 12 variantes par fiche (température unique si le prix ne bouge pas,
  paliers de tailles commerciaux, 3 couleurs max) ;
- pas de productDuplicate : un split créerait une fiche orpheline côté DSers
  (mapping AE au niveau produit) → réduction sur place, décision notée dans ETAT.md.
"""
from __future__ import annotations

import json
import re
import sys
import time
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from client import gql  # noqa: E402

WORK = ROOT / "variants-work.json"
JUNK_RE = re.compile(r"damaged|replacement|\bspare\b|pi[eè]ce cass[ée]e|broken", re.I)
THROTTLE = 0.15

PRODUCT_QUERY = """
query ($id: ID!) {
  product(id: $id) {
    id handle title status
    featuredMedia { id }
    media(first: 10) { nodes { id ... on MediaImage { image { url } } } }
    options { id name position optionValues { id name } }
    variants(first: 100) {
      pageInfo { hasNextPage endCursor }
      nodes { id title sku price selectedOptions { name value } image { url } }
    }
  }
}
"""


def fetch_variants(pid: str, cursor: str | None) -> list[dict]:
    nodes: list[dict] = []
    while True:
        data = gql(
            """
            query ($id: ID!, $c: String) {
              product(id: $id) {
                variants(first: 100, after: $c) {
                  pageInfo { hasNextPage endCursor }
                  nodes { id title sku price selectedOptions { name value } image { url } }
                }
              }
            }
            """,
            {"id": pid, "c": cursor},
        )
        conn = data["product"]["variants"]
        nodes.extend(conn["nodes"])
        if not conn["pageInfo"]["hasNextPage"]:
            return nodes
        cursor = conn["pageInfo"]["endCursor"]


def fetch_product(pid: str) -> dict:
    data = gql(PRODUCT_QUERY, {"id": pid})
    p = data["product"]
    conn = p["variants"]
    variants = list(conn["nodes"])
    if conn["pageInfo"]["hasNextPage"]:
        variants.extend(fetch_variants(pid, conn["pageInfo"]["endCursor"]))
    p["variants"] = variants
    return p


def fetch_all_products() -> list[dict]:
    out: list[dict] = []
    cursor = None
    while True:
        data = gql(
            """
            query ($c: String) {
              products(first: 20, after: $c, query: "status:active") {
                pageInfo { hasNextPage endCursor }
                nodes { id handle }
              }
            }
            """,
            {"c": cursor},
        )
        page = data["products"]
        for n in page["nodes"]:
            out.append(fetch_product(n["id"]))
            time.sleep(0.05)
        if not page["pageInfo"]["hasNextPage"]:
            return out
        cursor = page["pageInfo"]["endCursor"]


def delete_variants(pid: str, ids: list[str]) -> None:
    for i in range(0, len(ids), 50):
        chunk = ids[i : i + 50]
        data = gql(
            """
            mutation D($productId: ID!, $variantsIds: [ID!]!) {
              productVariantsBulkDelete(productId: $productId, variantsIds: $variantsIds) {
                userErrors { field message }
              }
            }
            """,
            {"productId": pid, "variantsIds": chunk},
        )
        errs = data["productVariantsBulkDelete"]["userErrors"]
        if errs:
            print("  warn delete variants", errs)
        time.sleep(THROTTLE)


def update_option_values(pid: str, option_id: str, renames: list[tuple[str, str]],
                         deletes: list[str] | None = None, new_name: str | None = None) -> None:
    if not renames and not deletes and not new_name:
        return
    option: dict = {"id": option_id}
    if new_name:
        option["name"] = new_name
    variables: dict = {"productId": pid, "option": option}
    parts = ["$productId: ID!", "$option: OptionUpdateInput!"]
    args = ["productId: $productId", "option: $option"]
    if renames:
        variables["optionValuesToUpdate"] = [{"id": vid, "name": name} for vid, name in renames]
        parts.append("$optionValuesToUpdate: [OptionValueUpdateInput!]")
        args.append("optionValuesToUpdate: $optionValuesToUpdate")
    if deletes:
        variables["optionValuesToDelete"] = deletes
        parts.append("$optionValuesToDelete: [ID!]")
        args.append("optionValuesToDelete: $optionValuesToDelete")
    query = (
        "mutation U(" + ", ".join(parts) + ") {\n"
        "  productOptionUpdate(" + ", ".join(args) + ") {\n"
        "    userErrors { field message }\n  }\n}"
    )
    data = gql(query, variables)
    errs = data["productOptionUpdate"]["userErrors"]
    if errs:
        print("  warn option update", errs)
    time.sleep(THROTTLE)


def delete_option(pid: str, oid: str) -> None:
    data = gql(
        """
        mutation D($productId: ID!, $options: [ID!]!, $strategy: ProductOptionDeleteStrategy) {
          productOptionsDelete(productId: $productId, options: $options, strategy: $strategy) {
            userErrors { field message }
          }
        }
        """,
        {"productId": pid, "options": [oid], "strategy": "POSITION"},
    )
    errs = data["productOptionsDelete"]["userErrors"]
    if errs:
        print("  warn delete option", errs)
    time.sleep(THROTTLE)


def attach_variant_images(pid: str, variant_ids: list[str], media_id: str) -> None:
    for i in range(0, len(variant_ids), 25):
        chunk = variant_ids[i : i + 25]
        data = gql(
            """
            mutation A($productId: ID!, $variantMedia: [ProductVariantAppendMediaInput!]!) {
              productVariantAppendMedia(productId: $productId, variantMedia: $variantMedia) {
                userErrors { field message }
              }
            }
            """,
            {
                "productId": pid,
                "variantMedia": [{"variantId": vid, "mediaIds": [media_id]} for vid in chunk],
            },
        )
        errs = data["productVariantAppendMedia"]["userErrors"]
        if errs:
            print("  warn media", errs[:2])
        time.sleep(THROTTLE)


def _fold(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def opt_value(variant: dict, option_name: str) -> str | None:
    for so in variant["selectedOptions"]:
        if so["name"] == option_name:
            return so["value"]
    return None


def purge_unused_values(pid: str) -> None:
    """Retire les valeurs d'option qui n'ont plus aucune variante (après delete)."""
    p = fetch_product(pid)
    used: dict[str, set[str]] = {}
    for v in p["variants"]:
        for so in v["selectedOptions"]:
            used.setdefault(so["name"], set()).add(so["value"])
    for opt in p["options"]:
        dead = [ov["id"] for ov in opt["optionValues"] if ov["name"] not in used.get(opt["name"], set())]
        if dead:
            update_option_values(pid, opt["id"], [], deletes=dead)


# ---------------------------------------------------------------------------
# Phase bambou : les 2 fiches de la capture d'Hakim
# ---------------------------------------------------------------------------

BAMBOU_HANDLES = ["suspension-bambou-led-583180", "suspension-bambou-led-033589"]
LINE_COLORS = {
    "blanc line": "Blanc", "white line": "Blanc",
    "noir line": "Noir", "black line": "Noir",
    "doré line": "Doré", "dore line": "Doré", "gold line": "Doré", "golden line": "Doré",
}


def product_by_handle(handle: str) -> dict:
    data = gql(
        'query ($q: String) { products(first: 1, query: $q) { nodes { id } } }',
        {"q": f"handle:{handle}"},
    )
    nodes = data["products"]["nodes"]
    if not nodes:
        raise RuntimeError(f"produit introuvable: {handle}")
    return fetch_product(nodes[0]["id"])


def run_bambou() -> None:
    for handle in BAMBOU_HANDLES:
        p = product_by_handle(handle)
        pid = p["id"]
        before = len(p["variants"])
        junk_ids = [
            v["id"] for v in p["variants"]
            if any(JUNK_RE.search(so["value"]) for so in v["selectedOptions"])
        ]
        print(f"{handle}: {before} variantes, {len(junk_ids)} junk à supprimer")
        if junk_ids:
            delete_variants(pid, junk_ids)
        purge_unused_values(pid)
        p = fetch_product(pid)
        for opt in p["options"]:
            renames = []
            for ov in opt["optionValues"]:
                new = LINE_COLORS.get(_fold(ov["name"]))
                if new and new != ov["name"]:
                    renames.append((ov["id"], new))
            if renames:
                update_option_values(pid, opt["id"], renames)
        # vérif
        p = fetch_product(pid)
        print(f"  après: {len(p['variants'])} variantes")
        for opt in p["options"]:
            print(f"  {opt['name']}: {[ov['name'] for ov in opt['optionValues']]}")
        missing = [v["id"] for v in p["variants"] if not (v.get("image") or {}).get("url")]
        media = p.get("media", {}).get("nodes") or []
        if missing and media:
            attach_variant_images(pid, missing, media[0]["id"])
            print(f"  image g1 rattachée sur {len(missing)} variantes")


def run_dump() -> None:
    products = fetch_all_products()
    WORK.write_text(json.dumps(products, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"dump {len(products)} produits → {WORK.name}")


# ---------------------------------------------------------------------------
# Plans fiche par fiche (décisions Fable 25/08/2026)
# ---------------------------------------------------------------------------

GRID = {"149.00", "199.00", "249.00", "299.00", "349.00", "399.00", "449.00", "499.00"}
TEMP_PRIORITY = [
    "3 teintes", "3 lumières — 3 teintes", "3 teintes change",
    "Variable (télécommande)", "Variation continue (télécommande)(RC)",
    "Variation continue (télécommande)", "Variable",
    "Blanc chaud", "Blanc chaud 3000 K", "Blanc neutre", "Blanc froid",
]

# Règles génériques appliquées à toutes les valeurs restantes (après les plans).
GENERIC_RULES: list[tuple[str, str]] = [
    (r"(\d+)\s*heads?\b", r"\1 lumières"),
    (r"\s*\bglass\b", ""),
    (r"\bGloden\b", "Doré"),
    (r"Café frame", "Café"),
    (r"Light Jaune", "Blanc chaud"),
    (r"^(Blanc|Noir|Doré) line$", r"\1"),
    (r"Ampoule non fournies", "Ampoule non fournie"),
    (r"—\s*—", "·"),
    (r"\s{2,}", " "),
]

PLANS: dict[str, dict] = {
    # --- lustres anneau (candidats split 1-2 vs 3-5 anneaux → réduction sur place, DSers) ---
    "lustre-anneau-led-led-dore-418494": {
        "keep": {"Taille": ["Ø 40 cm", "Ø 60 cm", "Ø 80 cm (3 anneaux 80 cm)", "Ø 100 cm"],
                 "Couleur": ["Noir", "Café", "Doré"]},
        "temp_auto": "Température", "drop_nongrid": True,
        "rename": {"Taille": {"Ø 80 cm (3 anneaux 80 cm)": "Ø 80 cm"}},
        "drop_option": ["Température"],
        "note": "réduction 108→12 : paliers Ø 40/60/80/100, 3 couleurs, une température ; split 1-2/3-5 anneaux écarté (mapping DSers)",
    },
    "lustre-anneau-led-led-784897": {
        "keep": {"Taille": ["Ø 40 cm", "Ø 60 cm", "Ø 80 cm", "Ø 100 cm"],
                 "Couleur": ["Doré", "Blanc", "Noir"]},
        "temp_auto": "Température", "drop_nongrid": True,
        "drop_option": ["Température"],
        "note": "réduction 132→≤12 : libellés DIA jumeaux supprimés, prix hors grille purgés",
    },
    "lustre-anneau-led-led-noir-dore-024410": {
        "keep": {"Taille": ["Ø 40 cm (1 anneau 40 cm)", "Ø 60 cm (2 anneaux 60 cm)",
                             "Ø 80 cm (3 anneaux 80 cm)", "Ø 100 cm (4 anneaux 100 cm)"],
                 "Température": ["Variable (télécommande)"]},
        "rename": {"Taille": {"Ø 40 cm (1 anneau 40 cm)": "Ø 40 cm · 1 anneau",
                               "Ø 60 cm (2 anneaux 60 cm)": "Ø 60 cm · 2 anneaux",
                               "Ø 80 cm (3 anneaux 80 cm)": "Ø 80 cm · 3 anneaux",
                               "Ø 100 cm (4 anneaux 100 cm)": "Ø 100 cm · 4 anneaux"}},
        "drop_option": ["Température"],
        "note": "réduction 99→12 : échelle honnête 1→4 anneaux avec paliers 199→399",
    },
    "lustre-anneau-led-led-dore-641905": {
        "keep": {"Taille": ["Ø 40 cm", "Ø 60 cm", "Ø 80 cm", "Ø 80 cm (5 anneaux 80 cm)"],
                 "Température": ["Blanc chaud"]},
        "rename": {"Taille": {"Ø 80 cm (5 anneaux 80 cm)": "Ø 80 cm · 5 anneaux"}},
        "drop_option": ["Température"],
        "note": "réduction 81→12 : Blanc chaud = prix uniforme 299 (Variable portait un 499 incohérent sur Ø 40)",
    },
    "lustre-anneau-led-led-799451": {
        "keep": {"Taille": ["Ø 40 cm", "Ø 60 cm", "Ø 80 cm"],
                 "Température": ["Variable (télécommande)"]},
        "drop_option": ["Température"],
        "note": "réduction 81→9 : prix unique 199, doublons (N anneaux) supprimés",
    },
    "lustre-anneau-led-led-597704": {
        "keep": {"Couleur": ["Ø 40 cm", "Ø 80 cm (80 cm Dor 40 60)", "Ø 100 cm (100 cm Dor 40 60 80)",
                              "Ø 40 cm · Blanc", "Ø 80 cm · Blanc 40 60", "Ø 100 cm · Blanc 40 60 80",
                              "Ø 40 cm (40 cm Noir)", "Ø 80 cm (80 cm Noir 40 60)", "Ø 100 cm (100 cm Noir 60 80)"],
                 "Température": ["Variable (télécommande)"]},
        "rename": {"Couleur": {"Ø 40 cm": "Doré · Ø 40 cm",
                                "Ø 80 cm (80 cm Dor 40 60)": "Doré · Ø 80 cm",
                                "Ø 100 cm (100 cm Dor 40 60 80)": "Doré · Ø 100 cm",
                                "Ø 40 cm · Blanc": "Blanc · Ø 40 cm",
                                "Ø 80 cm · Blanc 40 60": "Blanc · Ø 80 cm",
                                "Ø 100 cm · Blanc 40 60 80": "Blanc · Ø 100 cm",
                                "Ø 40 cm (40 cm Noir)": "Noir · Ø 40 cm",
                                "Ø 80 cm (80 cm Noir 40 60)": "Noir · Ø 80 cm",
                                "Ø 100 cm (100 cm Noir 60 80)": "Noir · Ø 100 cm"}},
        "rename_option": {"Couleur": "Modèle"},
        "drop_option": ["Température"],
        "note": "réduction 54→9 : 3 couleurs × 3 diamètres, codes usine dépliés en libellés FR",
    },
    "lustre-anneau-led-led-795468": {
        "keep": {"Taille": ["Ø 20 cm · Blanc", "Ø 20 cm (20 cm Noir)", "Ø 30 cm · Blanc", "Ø 30 cm (30 cm Noir)"],
                 "Température": ["3 teintes"]},
        "rename": {"Taille": {"Ø 20 cm (20 cm Noir)": "Ø 20 cm · Noir", "Ø 30 cm (30 cm Noir)": "Ø 30 cm · Noir"}},
        "drop_option": ["Température"],
        "note": "réduction 18→4 : valeurs ambiguës (couleur inconnue) supprimées",
    },
    # --- lustres cristal (rond vs allongé : réduction sur place) ---
    "lustre-cristal-led-677865": {
        "keep": {"Taille": ["Ø 40 cm", "Ø 60 cm", "Ø 80 cm", "Ø 100 cm"],
                 "Couleur": ["Doré", "Chrome"],
                 "Température": ["3 lumières — 3 teintes"]},
        "drop_option": ["Température"],
        "note": "réduction 220→8 : 22 tailles-combos → 4 paliers propres (249/299/399/399)",
    },
    "lustre-cristal-led-dore-202521": {
        "keep": {"Taille": ["Ø 46 cm · rond", "Ø 60 cm · rond", "Ø 76 cm · rond", "Ø 100 cm · rond",
                             "Ø 120 cm · allongé", "Ø 180 cm · allongé"],
                 "Température": ["3 teintes change"]},
        "drop_option": ["Température"],
        "note": "réduction 102→12 : 4 ronds + 2 allongés, split écarté (mapping DSers)",
    },
    "lustre-cristal-led-led-dore-841671": {
        "keep": {"Taille": ["Ø 45 cm · rond", "Ø 60 cm · rond", "Ø 80 cm · rond", "Ø 100 cm · rond",
                             "Ø 120 cm · allongé", "Ø 160 cm · allongé"],
                 "Température": ["3 lumières — 3 teintes"]},
        "drop_option": ["Température"],
        "note": "réduction 80→12 : Applique (autre objet) supprimée, 4 ronds + 2 allongés",
    },
    "lustre-cristal-led-led-560904": {
        "rename": {"Couleur": {"10 heads": "10 lumières", "12 heads": "12 lumières", "14 heads": "14 lumières"}},
        "rename_option": {"Couleur": "Lumières"},
        "note": "traduction heads → lumières",
    },
    "lustre-cristal-led-led-141724": {
        "keep": {"Température": ["Variable"]},
        "rename": {"Taille": {"Ø 20 cm · Chrome D40xD30xD20cm": "3 anneaux · Ø 40/30/20 cm"}},
        "drop_option": ["Température"],
        "note": "doublon Variable/Télécommande réduit, libellé D40xD30xD20 déplié",
    },
    "lustre-cristal-led-led-dore-264869": {
        "keep": {"Température": ["3 teintes"]},
        "rename": {"Couleur": {"1 lumières": "1 lumière"}},
        "rename_option": {"Couleur": "Lumières"},
        "drop_option": ["Température"],
        "note": "réduction 8→2 : une température",
    },
    # --- lustres salon ---
    "lustre-salon-led-147017": {
        "keep": {"Taille": ["Ø 40 cm", "Ø 60 cm", "Ø 80 cm"],
                 "Température": ["Variable (télécommande)"]},
        "rename_option": {"Éclairage": "Couleur"},
        "drop_option": ["Température"],
        "note": "réduction 108→9 : doublons (N anneaux) supprimés, Éclairage=couleurs renommé Couleur",
    },
    "lustre-salon-led-341706": {
        "keep": {"Taille": ["Ø 40 cm · Type A", "Ø 50 cm · Type A", "Ø 60 cm · Type A"],
                 "Température": ["3 teintes"]},
        "rename": {"Taille": {"Ø 40 cm · Type A": "Ø 40 cm", "Ø 50 cm · Type A": "Ø 50 cm",
                               "Ø 60 cm · Type A": "Ø 60 cm"}},
        "drop_option": ["Température"],
        "note": "réduction 75→3 : Type A–E = codes usine au même prix, un seul conservé",
    },
    "lustre-salon-907106": {
        "keep": {"Couleur": ["A", "P-3heads", "W-5heads", "X-8heads"]},
        "rename": {"Couleur": {"A": "1 lumière", "P-3heads": "3 lumières",
                                "W-5heads": "5 lumières", "X-8heads": "8 lumières"},
                   "Finition": {"Doré plat": "Doré", "Noir plat": "Noir"}},
        "rename_option": {"Couleur": "Lumières"},
        "drop_option": ["Température"],
        "note": "réduction 48→8 : 24 formes codées → échelle 1/3/5/8 lumières (199→499)",
    },
    "lustre-salon-led-784326": {
        "keep": {"Couleur": ["Noir 4 lumières", "Noir 6 lumières", "Doré 4 lumières",
                              "Doré 6 lumières", "Blanc 4 lumières", "Blanc 6 lumières"],
                 "Température": ["3 teintes"]},
        "rename": {"Couleur": {"Noir 4 lumières": "Noir · 4 lumières", "Noir 6 lumières": "Noir · 6 lumières",
                                "Doré 4 lumières": "Doré · 4 lumières", "Doré 6 lumières": "Doré · 6 lumières",
                                "Blanc 4 lumières": "Blanc · 4 lumières", "Blanc 6 lumières": "Blanc · 6 lumières"}},
        "rename_option": {"Couleur": "Modèle"},
        "drop_option": ["Température"],
        "note": "réduction 38→6 : 3 couleurs × 4/6 lumières, valeurs sans couleur supprimées",
    },
    "lustre-salon-led-254609": {
        "keep": {"Couleur": ["4 heads sans ampoule E27 bulb", "8 heads sans ampoule E27 bulb",
                              "12 heads ampoule E27 non fournie"]},
        "rename": {"Couleur": {"4 heads sans ampoule E27 bulb": "4 lumières",
                                "8 heads sans ampoule E27 bulb": "8 lumières",
                                "12 heads ampoule E27 non fournie": "12 lumières"},
                   "Finition": {"Doré sans ampoule E27 bulb": "Doré", "Noir sans ampoule E27 bulb": "Noir",
                                 "Noir and Doré sans ampoule E27": "Noir et doré"}},
        "rename_option": {"Couleur": "Lumières"},
        "note": "réduction 15→9 : 4/8/12 lumières × 3 finitions (ampoule E27 non fournie → specs)",
    },
    "lustre-salon-233314": {
        "keep": {"Taille": ["7 lumières · Ø 12 cm · A Noir", "7 lumières · Ø 12 cm · A Doré",
                             "13 lumières · Ø 12 cm · A Noir", "13 lumières · Ø 12 cm · A Doré"]},
        "rename": {"Taille": {"7 lumières · Ø 12 cm · A Noir": "7 lumières · Noir",
                               "7 lumières · Ø 12 cm · A Doré": "7 lumières · Doré",
                               "13 lumières · Ø 12 cm · A Noir": "13 lumières · Noir",
                               "13 lumières · Ø 12 cm · A Doré": "13 lumières · Doré"}},
        "rename_option": {"Taille": "Modèle"},
        "drop_option": ["Température"],
        "note": "réduction 19→4 : formes A/B/C au même prix, forme A conservée",
    },
    "lustre-salon-led-366435": {
        "keep": {"Format": ["Ø 92 cm · Blanc", "Ø 92 cm (92 cm Noir)", "Ø 75 cm · Blanc", "Ø 75 cm (75 cm Dor)"],
                 "Température": ["3 teintes"]},
        "rename": {"Format": {"Ø 92 cm (92 cm Noir)": "Ø 92 cm · Noir", "Ø 75 cm (75 cm Dor)": "Ø 75 cm · Doré"}},
        "rename_option": {"Format": "Modèle"},
        "drop_option": ["Température", "Taille"],
        "note": "réduction 14→4 : valeur 110–220 V retirée, couleurs explicites seulement",
    },
    "lustre-statement-led-noir-950316": {
        "rename": {"Couleur": {"4 heads": "4 lumières", "6 heads": "6 lumières", "8 heads": "8 lumières"}},
        "rename_option": {"Couleur": "Lumières"},
        "drop_option": ["Taille"],
        "note": "heads → lumières, option Taille=Ampoule non fournie retirée (info en specs)",
    },
    # --- suspensions rotin / bambou / bois ---
    "suspension-rotin-led-535545": {
        "keep": {"Taille": ["Ø 60 cm", "Ø 80 cm", "Ø 100 cm", "Ø 120 cm", "Ø 150 cm"],
                 "Température": ["Blanc chaud"], "Éclairage": ["3 teintes"]},
        "drop_option": ["Température", "Éclairage"],
        "note": "réduction 152→5 : Lampadaire + versions Tissu (autres objets) et doublons supprimés",
    },
    "suspension-bambou-942503": {
        "keep": {"Taille": ["Ø 60 cm", "Ø 80 cm", "Ø 100 cm", "Ø 120 cm", "Ø 150 cm"],
                 "Température": ["Blanc chaud"]},
        "drop_option": ["Température"],
        "note": "réduction 38→5 : Lampadaire + Tissu supprimés, paliers 199→399",
    },
    "suspension-rotin-605780": {
        "keep": {"Taille": ["Ø 35 cm", "Ø 40 cm", "Ø 50 cm", "Ø 60 cm", "Ø 65 cm"],
                 "Température": ["Blanc chaud 3000 K"]},
        "drop_option": ["Température"],
        "note": "réduction 46→5 : 23 combos forme/couleur → 5 diamètres propres",
    },
    "suspension-rotin-led-761433": {
        "keep": {"Taille": ["Ø 30 cm", "Ø 40 cm", "Ø 50 cm", "Ø 60 cm"],
                 "Température": ["3 teintes"]},
        "drop_option": ["Température"],
        "note": "réduction 28→4 : doublons (NN CM 1) supprimés",
    },
    "suspension-rotin-477244": {
        "keep": {"Température": ["3 teintes"]},
        "rename": {"Taille": {"Ø 40 cm · Beige D": "Ø 40 cm · Beige", "Ø 50 cm · Beige D": "Ø 50 cm · Beige",
                               "Ø 60 cm · Beige D": "Ø 60 cm · Beige",
                               "Ø 40 cm · Chanvre D40cm": "Ø 40 cm · Chanvre",
                               "Ø 50 cm · Chanvre D50cm": "Ø 50 cm · Chanvre",
                               "Ø 60 cm · Chanvre D60cm": "Ø 60 cm · Chanvre"}},
        "drop_option": ["Température"],
        "note": "réduction 24→6 : une température, suffixes D/DXXcm nettoyés",
    },
    "suspension-rotin-led-420069": {
        "keep": {"Taille": ["Ø 35 cm", "Ø 40 cm", "Ø 50 cm", "Ø 65 cm"]},
        "note": "réduction 21→4 : paliers de prix réels 199/249/299/399",
    },
    "suspension-rotin-469688": {
        "keep": {"Couleur": ["A1", "B1", "C1"], "Température": ["Blanc chaud"]},
        "rename": {"Couleur": {"A1": "Modèle A", "B1": "Modèle B", "C1": "Modèle C"}},
        "rename_option": {"Couleur": "Modèle"},
        "drop_option": ["Température"],
        "note": "réduction 18→3 : codes A1–C2 → 3 modèles",
    },
    "suspension-rotin-272937": {
        "keep": {"Couleur": ["A1", "B1", "C1"]},
        "rename": {"Couleur": {"A1": "Modèle A", "B1": "Modèle B", "C1": "Modèle C"}},
        "rename_option": {"Couleur": "Modèle"},
        "note": "réduction 15→3 : codes A1–C5 → 3 modèles",
    },
    "suspension-rotin-443915": {
        "keep": {"Taille": ["Ø 30 cm · Kaki A", "Ø 40 cm · Kaki A", "Ø 50 cm · Kaki B", "Ø 60 cm · Kaki B",
                             "Ø 40 cm (40 cm Noir A)", "Ø 50 cm (50 cm Noir B)", "Ø 60 cm (60 cm Noir B)"]},
        "rename": {"Taille": {"Ø 30 cm · Kaki A": "Ø 30 cm · Kaki", "Ø 40 cm · Kaki A": "Ø 40 cm · Kaki",
                               "Ø 50 cm · Kaki B": "Ø 50 cm · Kaki", "Ø 60 cm · Kaki B": "Ø 60 cm · Kaki",
                               "Ø 40 cm (40 cm Noir A)": "Ø 40 cm · Noir",
                               "Ø 50 cm (50 cm Noir B)": "Ø 50 cm · Noir",
                               "Ø 60 cm (60 cm Noir B)": "Ø 60 cm · Noir"}},
        "drop_option": ["Température"],
        "note": "réduction 14→7 : deux couleurs réelles, formes codées dépliées",
    },
    "suspension-rotin-607504": {
        "rename": {"Couleur": {"4040": "40 × 40 cm", "4019": "40 × 19 cm", "2550": "25 × 50 cm",
                                "4040BK": "40 × 40 cm · Noir"}},
        "rename_option": {"Couleur": "Taille"},
        "drop_option": ["Température"],
        "note": "codes 4040/4040BK → dimensions FR (BK = noir), ampoule E27 → specs",
    },
    "suspension-rotin-dore-435189": {
        "rename": {"Température": {"3000 K": "LED 3000 K (blanc chaud)",
                                    "Ampoule non fournie": "Ampoule non fournie (E27)"}},
        "rename_option": {"Température": "Éclairage"},
        "note": "deux versions réelles (LED intégrée vs E27) clarifiées",
    },
    "suspension-bambou-280004": {
        "keep": {"Taille": ["Ø 20 cm", "Ø 30 cm", "Ø 38 cm", "Ø 50 cm", "Ø 60 cm"]},
        "rename": {"Éclairage": {"Blanc line": "Blanc", "Noir line": "Noir"}},
        "rename_option": {"Éclairage": "Couleur"},
        "drop_option": ["Température"],
        "note": "réduction 18→10 : line → couleur du câble, doublons (20 cm A/D) supprimés",
    },
    "suspension-bambou-led-136557": {
        "keep": {"Couleur": ["suspension"]},
        "drop_option": ["Couleur", "Température"],
        "note": "réduction 14→7 : version plafonnier retirée (la fiche vend une suspension)",
    },
    "suspension-bois-832012": {
        "keep": {"Taille": ["220V"],
                 "Couleur": ["L Transparent", "L Ambre", "L Gris fumé"],
                 "Température et entrepôt": ["3 lumières — 3 teintes"]},
        "rename": {"Couleur": {"L Transparent": "Transparent", "L Ambre": "Ambre", "L Gris fumé": "Gris fumé"}},
        "drop_option": ["Taille", "Température et entrepôt"],
        "note": "réduction 64→3 : 110V supprimé (France = 220V), bases nues retirées, 3 teintes conservé",
    },
    "suspension-bois-led-453740": {
        "keep": {"Couleur": ["sku3"]},
        "drop_option": ["Couleur"],
        "note": "réduction 22→1 : 22 codes sku aveugles sans photo — à re-vérifier face au listing AE",
    },
    "suspension-bois-832012-": {},  # sentinelle inutilisée
    "suspension-bois-led-30cm-886635": {
        "keep": {"Couleur": ["Blanc"]},
        "drop_option": ["Couleur", "Taille"],
        "note": "réduction 23→1 : Blanc1–21 = jumeaux aveugles",
    },
    "suspension-bois-led-989306": {
        "keep": {"Température": ["3 teintes"]},
        "drop_option": ["Température"],
        "note": "réduction 15→3 : une température",
    },
    "suspension-bois-led-582321": {
        "keep": {"Température": ["3 teintes"]},
        "drop_option": ["Température"],
        "note": "réduction 15→3 : une température",
    },
    "suspension-bois-led-934110": {
        "rename": {"Couleur": {"6000 K-Blanc froid": "Blanc froid 6000 K",
                                "3000 K-Blanc chaud": "Blanc chaud 3000 K",
                                "Jaune Travertine": "Travertin"}},
        "rename_option": {"Couleur": "Modèle"},
        "drop_option": ["Température"],
        "note": "libellés FR, option Température single retirée",
    },
    "suspension-bois-led-334133": {
        "rename": {"Éclairage": {"log Bois": "Bois brut"}},
        "rename_option": {"Éclairage": "Finition"},
        "drop_option": ["Température"],
        "note": "log Bois → Bois brut",
    },
    "suspension-bois-led-121862": {
        "keep": {"Couleur": ["Blanc"]},
        "drop_option": ["Taille", "Couleur"],
        "note": "doublon Blanc/Blanc 1 réduit, option 4w(max60w) retirée",
    },
    # --- suspensions pierre / métal / verre / céramique / plafonniers ---
    "suspension-effet-pierre-led-dore-960013": {
        "keep": {"Taille": ["Ø 40 cm", "Ø 50 cm", "Ø 60 cm", "Ø 70 cm"],
                 "Couleur": ["Off Blanc", "Matte Noir", "Gris A"]},
        "temp_auto": "Température", "drop_nongrid": True,
        "rename": {"Couleur": {"Off Blanc": "Blanc cassé", "Matte Noir": "Noir mat", "Gris A": "Gris"}},
        "drop_option": ["Température"],
        "note": "réduction 192→≤12 : 8 couleurs → 3, Ø 30/80 (prix cassés) supprimés",
    },
    "suspension-effet-pierre-led-147607": {
        "keep": {"Couleur": ["A Stone", "B Stone", "C Stone"],
                 "Température": ["Blanc chaud 3000 K"]},
        "rename": {"Couleur": {"A Stone": "Forme A", "B Stone": "Forme B", "C Stone": "Forme C"}},
        "rename_option": {"Couleur": "Forme"},
        "drop_option": ["Température"],
        "note": "réduction 40→3 : 20 formes codées → 3",
    },
    "suspension-effet-pierre-led-445794": {
        "keep": {"Température": ["Blanc chaud 3000 K"]},
        "rename": {"Couleur": {"A-Bois": "Bois · forme A", "A-Dark Bois": "Bois foncé · forme A",
                                "B-Bois": "Bois · forme B", "B-Dark Bois": "Bois foncé · forme B"}},
        "drop_option": ["Température"],
        "note": "réduction 12→4 : une température, libellés FR",
    },
    "suspension-metal-led-dore-701414": {
        "keep": {"Température": ["Variable (télécommande)"]},
        "rename": {"Couleur": {"DuPont paper": "Papier DuPont", "Silk without patter": "Soie unie"}},
        "drop_option": ["Température"],
        "note": "réduction 40→10 : une température, matières traduites",
    },
    "suspension-metal-led-dore-081498": {
        "keep": {"Couleur": ["A Argenté", "A Doré", "A Noir Doré"],
                 "Température": ["3 teintes"]},
        "rename": {"Couleur": {"A Argenté": "Argenté", "A Doré": "Doré", "A Noir Doré": "Noir et doré"}},
        "drop_option": ["Température"],
        "note": "réduction 36→3 : formes A/B/C au même prix, forme A conservée",
    },
    "suspension-metal-led-dore-843772": {
        "keep": {"Taille": ["Ø 40 cm", "Ø 50 cm", "Ø 60 cm", "Ø 80 cm"],
                 "Température": ["Variable (télécommande)"]},
        "drop_option": ["Température", "Couleur"],
        "note": "réduction 33→4 : doublons anneaux supprimés, Couleur=Doré unique retirée",
    },
    "suspension-metal-led-dore-952116": {
        "keep": {"Couleur": ["Ceramic"]},
        "drop_option": ["Couleur", "Taille"],
        "note": "réduction 24→1 : Ceramic 1–20 + canopy = jumeaux aveugles",
    },
    "suspension-metal-dore-502141": {
        "keep": {"Température": ["Blanc chaud"]},
        "drop_option": ["Température"],
        "note": "réduction 18→6 : une température",
    },
    "suspension-metal-noir-dore-361680": {
        "rename": {"Couleur": {"Doré 4T": "Doré · 4 lumières", "Doré 6T": "Doré · 6 lumières",
                                "Doré 8T": "Doré · 8 lumières", "Noir 4T": "Noir · 4 lumières",
                                "Noir 6T": "Noir · 6 lumières", "Noir 8T": "Noir · 8 lumières"}},
        "rename_option": {"Couleur": "Modèle"},
        "drop_option": ["Température"],
        "note": "codes 4T/6T/8T → lumières, option Not with Bulb retirée (info specs)",
    },
    "suspension-verre-led-489156": {
        "keep": {"Température": ["3 teintes"]},
        "drop_option": ["Température"],
        "note": "réduction 45→15 : reste 5 tailles × 3 couleurs réelles, assumé >12",
    },
    "suspension-verre-091815": {
        "rename": {"Couleur": {"Transparent glass": "Transparent", "Ambre glass": "Ambre",
                                "Gris fumé glass": "Gris fumé"}},
        "note": "15 var conservées : 5 tailles × 3 couleurs réelles, assumé >12",
    },
    "suspension-verre-394147": {
        "keep": {"Couleur": ["1 lumières Transparent glass", "1 lumières Ambre glass", "1 lumières Gris Glass",
                              "3 lumières Transparent glass", "3 lumières Ambre glass", "3 heads Gris Glass"],
                 "Température": ["Blanc chaud"]},
        "rename": {"Couleur": {"1 lumières Transparent glass": "1 lumière · Transparent",
                                "1 lumières Ambre glass": "1 lumière · Ambre",
                                "1 lumières Gris Glass": "1 lumière · Gris fumé",
                                "3 lumières Transparent glass": "3 lumières · Transparent",
                                "3 lumières Ambre glass": "3 lumières · Ambre",
                                "3 heads Gris Glass": "3 lumières · Gris fumé"}},
        "rename_option": {"Couleur": "Modèle"},
        "drop_option": ["Température"],
        "note": "réduction 24→6 : doublons supprimés, 1/3 lumières × 3 verres",
    },
    "suspension-verre-651675": {
        "keep": {"Couleur": ["Ø 20 cm · Argenté", "Ø 25 cm · Argenté", "Ø 30 cm · Argenté",
                              "Ø 20 cm · Gris fumé", "Ø 25 cm · Gris fumé", "Ø 30 cm · Gris fumé",
                              "Ø 20 cm · Cognac", "Ø 25 cm · Cognac", "Ø 30 cm · Cognac"]},
        "rename_option": {"Couleur": "Modèle"},
        "note": "réduction 20→9 : paires A/B (249) et plains ambigus supprimés",
    },
    "suspension-verre-led-dore-436718": {
        "keep": {"Couleur": ["A Doré small", "A Doré large", "A Noir small", "A Noir large"],
                 "Température": ["Blanc chaud"]},
        "rename": {"Couleur": {"A Doré small": "Doré · petit", "A Doré large": "Doré · grand",
                                "A Noir small": "Noir · petit", "A Noir large": "Noir · grand"}},
        "rename_option": {"Couleur": "Modèle"},
        "drop_option": ["Température"],
        "note": "réduction 18→4 : forme A conservée, small/large traduits",
    },
    "suspension-verre-814554": {
        "keep": {"Couleur": ["Blanc 1", "Brun 1", "Vert 1"]},
        "rename": {"Couleur": {"Blanc 1": "Blanc", "Brun 1": "Brun", "Vert 1": "Vert"}},
        "drop_option": ["Température"],
        "note": "réduction 15→3 : jumeaux numérotés supprimés",
    },
    "suspension-verre-noir-201424": {
        "keep": {"Couleur": ["Sogon Margherita"]},
        "drop_option": ["Couleur", "Température"],
        "note": "réduction 13→1 : 13 noms fantaisie sans photo — à re-vérifier face au listing AE",
    },
    "suspension-verre-446435": {
        "keep": {"Format": ["220V"]},
        "drop_option": ["Format"],
        "note": "110V supprimé (France = 220V)",
    },
    "suspension-moderne-led-noir-330664": {
        "keep": {"Taille": ["Ø 100 cm (100 cm Noir)", "Ø 120 cm", "Ø 150 cm (150 cm Noir150cm)"],
                 "Température": ["Variation continue (télécommande)(RC)"]},
        "rename": {"Taille": {"Ø 100 cm (100 cm Noir)": "Ø 100 cm", "Ø 150 cm (150 cm Noir150cm)": "Ø 150 cm"}},
        "drop_option": ["Température"],
        "note": "réduction 24→3 : versions noires explicites conservées (fiche = noir)",
    },
    "suspension-deco-led-blanc-805304": {
        "keep": {"Couleur": ["Ceramic"]},
        "drop_option": ["Couleur", "Taille"],
        "note": "réduction 24→1 : Ceramic 1–23 = jumeaux aveugles",
    },
    "suspension-deco-led-077631": {
        "keep": {"Taille": ["No plug"], "Couleur": ["A", "B", "C"]},
        "rename": {"Couleur": {"A": "Modèle A", "B": "Modèle B", "C": "Modèle C"}},
        "rename_option": {"Couleur": "Modèle"},
        "drop_option": ["Taille"],
        "note": "réduction 12→3 : branchement plafond standard, formes A–F → 3 modèles",
    },
    "suspension-deco-led-689455": {
        "keep": {"Couleur": ["Style A", "Style B", "Style C"]},
        "rename": {"Couleur": {"Style A": "Modèle A", "Style B": "Modèle B", "Style C": "Modèle C"}},
        "rename_option": {"Couleur": "Modèle"},
        "note": "réduction 6→3 : combinations 1–3 supprimées",
    },
    "plafonnier-led-led-728204": {
        "keep": {"Taille": ["Ø 60 cm · Blanc L60cm", "Ø 100 cm · Blanc L100cm", "Ø 150 cm · Blanc L150cm",
                             "Ø 200 cm · Blanc L200cm", "Ø 60 cm · Noyer L60cm", "Ø 100 cm · Noyer L100cm",
                             "Ø 150 cm · Noyer L150cm", "Ø 200 cm · Noyer L200cm"],
                 "Température": ["Variable (télécommande)"]},
        "rename": {"Taille": {"Ø 60 cm · Blanc L60cm": "Ø 60 cm · Blanc", "Ø 100 cm · Blanc L100cm": "Ø 100 cm · Blanc",
                               "Ø 150 cm · Blanc L150cm": "Ø 150 cm · Blanc", "Ø 200 cm · Blanc L200cm": "Ø 200 cm · Blanc",
                               "Ø 60 cm · Noyer L60cm": "Ø 60 cm · Noyer", "Ø 100 cm · Noyer L100cm": "Ø 100 cm · Noyer",
                               "Ø 150 cm · Noyer L150cm": "Ø 150 cm · Noyer", "Ø 200 cm · Noyer L200cm": "Ø 200 cm · Noyer"}},
        "drop_option": ["Température"],
        "note": "réduction 96→8 : Blanc + Noyer × 4 longueurs, valeurs ambiguës supprimées",
    },
    "plafonnier-led-992600": {
        "rename": {"Couleur": {"Noir 4 heads": "Noir · 4 lumières", "Noir 6 heads": "Noir · 6 lumières",
                                "Noir 8 heads": "Noir · 8 lumières", "Doré 4 heads": "Doré · 4 lumières",
                                "Doré 6 heads": "Doré · 6 lumières", "Doré 8 heads": "Doré · 8 lumières",
                                "Blanc 4 heads": "Blanc · 4 lumières", "Blanc 6 heads": "Blanc · 6 lumières",
                                "Blanc 8 heads": "Blanc · 8 lumières"}},
        "rename_option": {"Couleur": "Modèle"},
        "note": "heads → lumières (9 var conservées)",
    },
    "plafonnier-led-led-922186": {
        "keep": {"Couleur": ["5 Balls", "10 Balls", "15 Balls", "20 Balls"],
                 "Température": ["Blanc chaud 3000 K"]},
        "rename": {"Couleur": {"5 Balls": "5 globes", "10 Balls": "10 globes",
                                "15 Balls": "15 globes", "20 Balls": "20 globes"}},
        "rename_option": {"Couleur": "Modèle"},
        "drop_option": ["Température"],
        "note": "réduction 15→4 : valeur inquiry supprimée, Balls → globes",
    },
    "plafonnier-led-led-442025": {
        "keep": {"Couleur": ["Ø 65 cm"]},
        "drop_option": ["Couleur"],
        "note": "code 9TPGY-JS indéchiffrable supprimé",
    },
    "plafonnier-led-led-465027": {
        "keep": {"Température": ["3 teintes"]},
        "drop_option": ["Température"],
        "note": "réduction 8→2 : une température (warm led / Dimmable by Remote supprimés)",
    },
    "suspension-bois-led-245113": {
        "drop_option": ["Température"],
        "note": "option 3000 K single retirée",
    },
}
PLANS.pop("suspension-bois-832012-", None)


def apply_generic_rules(name: str) -> str:
    out = name
    for pat, repl in GENERIC_RULES:
        out = re.sub(pat, repl, out)
    return re.sub(r"\s+", " ", out).strip(" ·,-") or name


def pick_temp(p: dict, opt_name: str, keeps: dict[str, list[str]]) -> str:
    """Choisit la valeur de température qui maximise la couverture prix-grille."""
    opt = next(o for o in p["options"] if o["name"] == opt_name)
    values = [ov["name"] for ov in opt["optionValues"]]

    def kept_elsewhere(v: dict) -> bool:
        for oname, allowed in keeps.items():
            if oname == opt_name:
                continue
            val = opt_value(v, oname)
            if val is not None and val not in allowed:
                return False
        return True

    scored = []
    for val in values:
        subset = [v for v in p["variants"] if opt_value(v, opt_name) == val and kept_elsewhere(v)]
        grid_n = sum(1 for v in subset if v["price"] in GRID)
        prio = TEMP_PRIORITY.index(val) if val in TEMP_PRIORITY else 99
        scored.append((-grid_n, prio, val))
    scored.sort()
    return scored[0][2]


def reorder_size_values(p: dict) -> None:
    """Trie les valeurs numériques croissantes des options Taille/Format."""
    needs = False
    inputs = []
    for opt in p["options"]:
        names = [ov["name"] for ov in opt["optionValues"]]
        entry = {"name": opt["name"], "values": [{"name": n} for n in names]}
        if opt["name"] in {"Taille", "Format"} and len(names) > 1:
            keys = []
            for n in names:
                m = re.search(r"(\d+(?:[.,]\d+)?)", n)
                keys.append(float(m.group(1).replace(",", ".")) if m else 1e9)
            order = [n for _, n in sorted(zip(keys, names), key=lambda t: t[0])]
            if order != names:
                needs = True
                entry["values"] = [{"name": n} for n in order]
        inputs.append(entry)
    if not needs:
        return
    data = gql(
        """
        mutation R($productId: ID!, $options: [OptionReorderInput!]!) {
          productOptionsReorder(productId: $productId, options: $options) {
            userErrors { field message }
          }
        }
        """,
        {"productId": p["id"], "options": inputs},
    )
    errs = data["productOptionsReorder"]["userErrors"]
    if errs:
        print("  warn reorder", errs[:2])
    time.sleep(THROTTLE)


def process_product(p: dict, plan: dict, report: list[dict]) -> None:
    pid = p["id"]
    handle = p["handle"]
    before = len(p["variants"])
    actions: list[str] = []

    # 1. junk générique (damaged / replacement / spare)
    junk_ids = [v["id"] for v in p["variants"]
                if any(JUNK_RE.search(so["value"]) for so in v["selectedOptions"])]
    if junk_ids and len(junk_ids) < len(p["variants"]):
        delete_variants(pid, junk_ids)
        actions.append(f"junk -{len(junk_ids)}")
        p["variants"] = [v for v in p["variants"] if v["id"] not in set(junk_ids)]

    # 2. réduction par listes keep (+ température auto)
    keeps = dict(plan.get("keep") or {})
    if plan.get("temp_auto"):
        chosen = pick_temp(p, plan["temp_auto"], keeps)
        keeps[plan["temp_auto"]] = [chosen]
        actions.append(f"temp={chosen}")
    if keeps:
        drop = []
        for v in p["variants"]:
            for oname, allowed in keeps.items():
                val = opt_value(v, oname)
                if val is not None and val not in allowed:
                    drop.append(v["id"])
                    break
        if drop and len(drop) < len(p["variants"]):
            delete_variants(pid, drop)
            actions.append(f"reduce -{len(drop)}")
            p["variants"] = [v for v in p["variants"] if v["id"] not in set(drop)]
        elif drop:
            print(f"  STOP {handle}: le plan viderait la fiche, aucune suppression")

    # 3. prix hors grille (fiches signalées seulement)
    if plan.get("drop_nongrid"):
        bad = [v["id"] for v in p["variants"] if v["price"] not in GRID]
        if bad and len(bad) < len(p["variants"]):
            delete_variants(pid, bad)
            actions.append(f"hors-grille -{len(bad)}")
            p["variants"] = [v for v in p["variants"] if v["id"] not in set(bad)]

    purge_unused_values(pid)
    p = fetch_product(pid)

    # 4. renommages (plan puis règles génériques), anti-collision
    for opt in p["options"]:
        plan_map = (plan.get("rename") or {}).get(opt["name"], {})
        current = {ov["name"] for ov in opt["optionValues"]}
        renames: list[tuple[str, str]] = []
        taken = {n.lower() for n in current}
        for ov in opt["optionValues"]:
            new = plan_map.get(ov["name"]) or apply_generic_rules(ov["name"])
            if new == ov["name"]:
                continue
            if new.lower() in taken - {ov["name"].lower()}:
                print(f"  skip collision {handle} [{opt['name']}] {ov['name']!r} → {new!r}")
                continue
            taken.discard(ov["name"].lower())
            taken.add(new.lower())
            renames.append((ov["id"], new))
        if renames:
            update_option_values(pid, opt["id"], renames)
            actions.append(f"rename {opt['name']} ×{len(renames)}")

    # 5. renommage d'option
    for old, new in (plan.get("rename_option") or {}).items():
        opt = next((o for o in p["options"] if o["name"] == old), None)
        if opt and not any(o["name"] == new for o in p["options"]):
            update_option_values(pid, opt["id"], [], new_name=new)
            actions.append(f"option {old}→{new}")

    # 6. options à une seule valeur restante
    p = fetch_product(pid)
    for oname in plan.get("drop_option") or []:
        opt = next((o for o in p["options"] if o["name"] == oname), None)
        if opt and len(opt["optionValues"]) == 1 and len(p["options"]) > 1:
            delete_option(pid, opt["id"])
            actions.append(f"drop option {oname}")
            p["options"] = [o for o in p["options"] if o["id"] != opt["id"]]
        elif opt and len(opt["optionValues"]) > 1:
            print(f"  warn {handle}: option {oname} a encore {len(opt['optionValues'])} valeurs, non supprimée")

    # 7. tri des tailles + images
    p = fetch_product(pid)
    reorder_size_values(p)
    media = p.get("media", {}).get("nodes") or []
    missing = [v["id"] for v in p["variants"] if not (v.get("image") or {}).get("url")]
    if missing and media:
        attach_variant_images(pid, missing, media[0]["id"])
        actions.append(f"images +{len(missing)}")

    after = len(p["variants"])
    nongrid = sorted({v["price"] for v in p["variants"] if v["price"] not in GRID})
    report.append({
        "handle": handle, "before": before, "after": after,
        "actions": actions, "note": plan.get("note", ""),
        "options": [{o["name"]: [ov["name"] for ov in o["optionValues"]]} for o in p["options"]],
        "nongrid_prices": nongrid,
    })
    print(f"  {handle}: {before} → {after} var | {', '.join(actions) or 'rien'}")


def run_plan_check() -> None:
    """Valide les plans contre le dump de travail (valeurs exactes)."""
    products = {p["handle"]: p for p in json.loads(WORK.read_text())}
    problems = 0
    for handle, plan in PLANS.items():
        p = products.get(handle)
        if not p:
            print(f"ABSENT {handle}")
            problems += 1
            continue
        opt_names = {o["name"] for o in p["options"]}
        values = {o["name"]: {ov["name"] for ov in o["optionValues"]} for o in p["options"]}
        for oname, allowed in (plan.get("keep") or {}).items():
            if oname not in opt_names:
                print(f"{handle}: option keep inconnue {oname}")
                problems += 1
                continue
            for val in allowed:
                if val not in values[oname]:
                    print(f"{handle}: valeur keep inconnue [{oname}] {val!r}")
                    problems += 1
        for oname, mapping in (plan.get("rename") or {}).items():
            if oname not in opt_names:
                print(f"{handle}: option rename inconnue {oname}")
                problems += 1
                continue
            for old in mapping:
                if old not in values[oname]:
                    print(f"{handle}: valeur rename inconnue [{oname}] {old!r}")
                    problems += 1
        for oname in (plan.get("rename_option") or {}) | {n: None for n in plan.get("drop_option") or []}:
            if oname not in opt_names:
                print(f"{handle}: option {oname} inconnue (rename/drop)")
                problems += 1
        if plan.get("temp_auto") and plan["temp_auto"] not in opt_names:
            print(f"{handle}: temp_auto option inconnue")
            problems += 1
    print(f"check: {problems} problème(s) sur {len(PLANS)} plans")


def run_apply(only: str | None = None) -> None:
    products = json.loads(WORK.read_text())
    report_path = ROOT / "variants-position-report.json"
    report: list[dict] = []
    if report_path.exists():
        report = json.loads(report_path.read_text())
    done = {r["handle"] for r in report}
    for p in products:
        handle = p["handle"]
        if only and handle != only:
            continue
        plan = PLANS.get(handle)
        needs_generic = any(
            apply_generic_rules(ov["name"]) != ov["name"]
            for o in p["options"] for ov in o["optionValues"]
        )
        junk = any(JUNK_RE.search(so["value"]) for v in p["variants"] for so in v["selectedOptions"])
        if not plan and not needs_generic and not junk:
            # tri de tailles + images seulement
            live = fetch_product(p["id"])
            reorder_size_values(live)
            media = live.get("media", {}).get("nodes") or []
            missing = [v["id"] for v in live["variants"] if not (v.get("image") or {}).get("url")]
            if missing and media:
                attach_variant_images(p["id"], missing, media[0]["id"])
                print(f"  {handle}: images +{len(missing)}")
            continue
        if handle in done:
            print(f"  skip {handle} (déjà traité)")
            continue
        live = fetch_product(p["id"])
        process_product(live, plan or {}, report)
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"apply OK — rapport {report_path.name} ({len(report)} fiches)")


def run_verify() -> None:
    products = fetch_all_products()
    WORK.write_text(json.dumps(products, ensure_ascii=False) + "\n", encoding="utf-8")
    bad_words = re.compile(
        r"damaged|replacement|\bspare\b|\bheads?\b|\bline\b|\bglass\b|\bstone\b|ceramic|inquiry|"
        r"\bballs?\b|\bsku\d|\bstyle [a-e]\b|type [a-e]\b|9TPGY|combination|plug|110v|220v",
        re.I,
    )
    n_junk = 0
    for p in products:
        for o in p["options"]:
            for ov in o["optionValues"]:
                if bad_words.search(ov["name"]):
                    print(f"RESTE {p['handle']} [{o['name']}] {ov['name']!r}")
                    n_junk += 1
    over24 = [(p["handle"], len(p["variants"])) for p in products if len(p["variants"]) > 24]
    over12 = [(p["handle"], len(p["variants"])) for p in products if len(p["variants"]) > 12]
    total = sum(len(p["variants"]) for p in products)
    noimg = [(p["handle"], sum(1 for v in p["variants"] if not (v.get("image") or {}).get("url")))
             for p in products]
    noimg = [x for x in noimg if x[1]]
    print(f"\nvariantes totales: {total} | fiches >24: {len(over24)} | >12: {len(over12)} | libellés suspects: {n_junk}")
    for h, n in over24:
        print(f"  >24: {h} ({n})")
    for h, n in over12:
        if (h, n) not in over24:
            print(f"  >12: {h} ({n})")
    for h, n in noimg:
        print(f"  sans image: {h} ({n})")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    if cmd == "bambou":
        run_bambou()
    elif cmd == "dump":
        run_dump()
    elif cmd == "check":
        run_plan_check()
    elif cmd == "apply":
        run_apply(sys.argv[2] if len(sys.argv) > 2 else None)
    elif cmd == "verify":
        run_verify()
    else:
        print("usage: position_variants.py bambou|dump|check|apply [handle]|verify")
