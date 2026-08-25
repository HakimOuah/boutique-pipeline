#!/usr/bin/env python3
"""Humanise les libellés de valeurs d'option et les textes alternatifs des médias.

Renommage seul : jamais de suppression, jamais de split, jamais de création.
Chaque `productOptionUpdate` part avec `variantStrategy: LEAVE_AS_IS` et l'ensemble
des SKU de la fiche est comparé avant / après.

Les libellés de valeur viennent d'une table explicite (RENAMES) : chaque ligne a été
tranchée en lisant le SKU DSers de la variante, seule preuve disponible de ce que le
fournisseur vend réellement. Les alt sont générés à partir du titre nettoyé et d'une
classification des images (packshot studio / gros plan / mise en situation) calculée
sur les pixels, pour ne pas décrire un angle de vue qu'on n'a pas vérifié.

    python3 humanise_options.py --dump     # dump live
    python3 humanise_options.py            # plan (dry-run)
    python3 humanise_options.py --apply    # applique
"""
from __future__ import annotations

import json
import re
import statistics
import sys
import time
import unicodedata
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from client import gql  # noqa: E402

DUMP = ROOT / "variants-humanise-dump.json"
IMG_CACHE = ROOT / "variants-humanise-imgcache.json"
THROTTLE = 0.15
DASHES = "\u2014\u2013"


# ─────────────────────────────── dump live ───────────────────────────────

PRODUCT_Q = """
query ($id: ID!) {
  product(id: $id) {
    id handle title
    featuredMedia { id }
    options { id name position optionValues { id name } }
    media(first: 30) { nodes { id alt ... on MediaImage { image { url } } } }
    variants(first: 100) {
      pageInfo { hasNextPage }
      nodes { id sku title selectedOptions { name value } }
    }
  }
}
"""


def fetch_product(pid: str) -> dict:
    return gql(PRODUCT_Q, {"id": pid})["product"]


def fetch_all() -> list[dict]:
    out: list[dict] = []
    cursor = None
    while True:
        page = gql(
            """
            query ($c: String) {
              products(first: 25, after: $c, query: "status:active") {
                pageInfo { hasNextPage endCursor }
                nodes { id }
              }
            }
            """,
            {"c": cursor},
        )["products"]
        for n in page["nodes"]:
            out.append(fetch_product(n["id"]))
            time.sleep(0.05)
        if not page["pageInfo"]["hasNextPage"]:
            return out
        cursor = page["pageInfo"]["endCursor"]


def skus_of(product: dict) -> list[str]:
    return sorted((v.get("sku") or "") for v in product["variants"]["nodes"])


# ─────────────────────── libellés : table de renommage ───────────────────────

# handle -> [(libellé actuel, libellé humanisé)]. Preuve = SKU DSers, rappelée en
# commentaire quand le libellé actuel ment sur ce qu'on livre.
RENAMES: dict[str, list[tuple[str, str]]] = {
    # SKU `rattan 50cm` / `Plastic 50cm` : deux matières vendues sous le même Ø.
    "suspension-rotin-897170": [
        ("Ø 50 cm", "Ø 50 cm · rotin"),
        ("Ø 50 cm \u2014 (rattan 1)", "Ø 50 cm · rotin 2"),
        ("Ø 50 cm \u2014 (Plastic)", "Ø 50 cm · plastique"),
        ("Ø 60 cm", "Ø 60 cm · plastique"),
        ("Ø 60 cm \u2014 (Plastic 1)", "Ø 60 cm · plastique 2"),
        ("Ø 60 cm \u2014 (rattan)", "Ø 60 cm · rotin"),
        ("Ø 60 cm \u2014 (rattan 1)", "Ø 60 cm · rotin 2"),
    ],
    # SKU `2 X H28cm` vs `H28cm` : c'est un lot de deux ou une pièce seule.
    "suspension-effet-pierre-led-709819": [
        ("Ø 28 cm", "Ø 28 cm · lot de 2"),
        ("Ø 28 cm (28 cm H28cm)", "Ø 28 cm · à l\u2019unité"),
        ("Ø 40 cm", "Ø 40 cm · lot de 2"),
        ("Ø 40 cm (40 cm H40cm)", "Ø 40 cm · à l\u2019unité"),
    ],
    # SKU `40cm 2pcs` vs `40cm 1pcs`.
    "suspension-bambou-104055": [
        ("Ø 40 cm", "Ø 40 cm · lot de 2"),
        ("Ø 40 cm (1 pièce 40 cm)", "Ø 40 cm · à l\u2019unité"),
        ("Ø 50 cm", "Ø 50 cm · lot de 2"),
        ("Ø 50 cm (1 pièce 50 cm)", "Ø 50 cm · à l\u2019unité"),
    ],
    # SKU `white light` / `Neutral light` / `warm light` : trois températures,
    # dont deux étiquetées « Blanc neutre ».
    "suspension-effet-pierre-343987": [
        ("Blanc neutre", "Blanc froid"),
        ("Blanc neutre (Blanc neutre)", "Blanc neutre"),
    ],
    # Le fournisseur duplique chaque émail sous deux références.
    "suspension-deco-led-837156": [
        ("Plum Vert Celadon", "Céladon vert"),
        ("Powder Bleu Celadon", "Céladon bleu poudré"),
        ("Plum Vert Celadon 1", "Céladon vert 2"),
        ("Powder Bleu Celadon 1", "Céladon bleu poudré 2"),
    ],
    # SKU `Dia.45CM` (plafonnier) vs `Pendant Lamp D45CM` (suspension) : même Ø,
    # deux montages. Sans mention, deux fois « Ø 45 cm » dans le sélecteur.
    "plafonnier-led-led-dore-blanc-354637": [
        ("Ø 30 cm", "Ø 30 cm · plafonnier"),
        ("Ø 45 cm", "Ø 45 cm · plafonnier"),
        ("Ø 45 cm · suspension D45CM", "Ø 45 cm · suspension"),
        ("Ø 55 cm", "Ø 55 cm · plafonnier"),
    ],
    "lustre-anneau-led-led-892612": [
        ("Ø 20 cm · Plafonnier", "Ø 20 cm · plafonnier"),
        ("Ø 30 cm · Plafonnier", "Ø 30 cm · plafonnier"),
        ("Ø 46 cm · Plafonnier", "Ø 46 cm · plafonnier"),
        ("Ø 53 cm · Plafonnier", "Ø 53 cm · plafonnier"),
    ],
    "plafonnier-led-led-698635": [("Infinite Dimming", "Variable (sans palier)")],
    # SKU `Black-50cm` : ce « Ø 50 cm » nu est la version noire.
    "lustre-salon-957153": [("Ø 50 cm", "Ø 50 cm · Noir")],
    # SKU `Walnut Base A` / `Wood color A` : noyer contre bois clair, deux formes.
    "suspension-bois-193329": [
        ("Noyer Base A", "Noyer · forme A"),
        ("Bois A", "Bois clair · forme A"),
        ("Noyer Base B", "Noyer · forme B"),
        ("Bois B", "Bois clair · forme B"),
    ],
    # Troisième température d'un produit 3 CCT, laissée en « Blanc chaud · 2 ».
    "suspension-effet-pierre-led-338324": [("Blanc chaud · 2", "Blanc neutre")],
}

# Règles transversales appliquées ensuite, indépendamment de la fiche.
CHROME_RE = re.compile(r"^Chrome$")
HEAD_COUNT_RE = re.compile(r"^(Blanc|Noir|Doré|Gris|Argenté)\s+(\d+)\s+lumières?$")
LETTER_DASH_RE = re.compile(r"^([A-G])-(.+)$")


def generic_rename(value: str) -> str | None:
    """Renommages sûrs qui ne dépendent pas de la fiche."""
    if CHROME_RE.match(value):
        return "Chromé"
    m = HEAD_COUNT_RE.match(value)
    if m:
        n = int(m.group(2))
        return f"{m.group(1)} · {n} lumière" + ("s" if n > 1 else "")
    m = LETTER_DASH_RE.match(value)
    if m:
        return f"{m.group(1)} · {m.group(2)}"
    return None


def table_applies(table: dict[str, str], opt: dict) -> bool:
    """Le renommage a-t-il déjà tourné sur cet axe ?

    Sur `suspension-effet-pierre-343987` le nouveau nom d'une valeur est l'ancien
    nom de sa voisine (« Blanc neutre » devient « Blanc froid », et le doublon
    « Blanc neutre (Blanc neutre) » récupère « Blanc neutre »). Rejouer la table
    sur l'état final créerait deux « Blanc froid ». On la neutralise dès que les
    seules clés encore présentes sont des noms d'arrivée.
    """
    present = [v["name"] for v in opt["optionValues"] if v["name"] in table]
    if not present:
        return False
    targets = set(table.values())
    return any(name not in targets for name in present)


def plan_option_values(products: list[dict]) -> list[dict]:
    plans: list[dict] = []
    for p in products:
        table = dict(RENAMES.get(p["handle"], []))
        renames: list[dict] = []
        for opt in p["options"]:
            opt_table = table if table_applies(table, opt) else {}
            final = {v["name"]: v["name"] for v in opt["optionValues"]}
            for v in opt["optionValues"]:
                after = opt_table.get(v["name"]) or generic_rename(v["name"])
                if not after or after == v["name"]:
                    continue
                final[v["name"]] = after
                renames.append(
                    {
                        "option_id": opt["id"],
                        "option_name": opt["name"],
                        "value_id": v["id"],
                        "before": v["name"],
                        "after": after,
                    }
                )
            names = list(final.values())
            if len(set(names)) != len(names):
                raise SystemExit(f"collision de libellés sur {p['handle']} / {opt['name']}: {names}")
            for name in names:
                if any(d in name for d in DASHES):
                    raise SystemExit(f"cadratin restant sur {p['handle']}: {name!r}")
        if renames:
            plans.append({"handle": p["handle"], "id": p["id"], "renames": renames})
    return plans


# ───────────────────────── alt : sujet et matière ─────────────────────────


def typographic(text: str) -> str:
    return text.replace("'", "\u2019")


def subject_of(product: dict) -> str:
    """Le luminaire (matière + forme) : la première clause du titre nettoyé."""
    first = re.split(r"\s*,\s*", product["title"])[0]
    for dash in DASHES:
        first = first.replace(dash, " ")
    first = re.sub(r"\s{2,}", " ", first).strip()
    # « Suspension nuages en verre soufflé LED » : le LED final n'apprend rien à
    # qui écoute l'alt, sauf quand il tient le titre à lui seul.
    if first.endswith(" LED") and len(first.split()) > 4:
        first = first[: -len(" LED")]
    return typographic(first)


def slugify(text: str) -> str:
    norm = unicodedata.normalize("NFKD", text.lower())
    norm = "".join(c for c in norm if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", norm).strip("-")


# Les noms de fichiers des packshots sont sans accent. Quand le slug ne retombe
# pas sur une valeur d'option de la fiche, on lui rend ses accents à la main.
SLUG_LABELS = {
    "dore": "doré",
    "argente": "argenté",
    "gris-fume": "gris fumé",
    "bois-fonce": "bois foncé",
    "bois-clair": "bois clair",
    "chrome": "chromé",
    "creme": "crème",
    "cafe": "café",
    "celadon": "céladon",
    "opalin": "opalin",
    "fume": "fumé",
}


# ──────────────────── alt : classification des images ────────────────────


def image_features(url: str) -> list[float] | None:
    """Part de pixels hors fond sur chacun des quatre bords de l'image.

    Une photo studio du catalogue est posée sur un fond beige uni : au moins un
    bord reste vide. Une mise en situation montre un intérieur meublé, donc les
    quatre bords sont chargés. C'est le seul écart qui se lit de façon fiable ;
    distinguer un gros plan d'un plan large ne l'est pas, on ne l'affirme donc pas.
    """
    import io

    from PIL import Image  # import tardif : seul le mode alt en a besoin

    sep = "&" if "?" in url else "?"
    try:
        with urllib.request.urlopen(f"{url}{sep}width=160", timeout=45) as resp:
            raw = resp.read()
        im = Image.open(io.BytesIO(raw)).convert("RGB").resize((160, 160))
    except Exception:  # noqa: BLE001
        return None
    px = im.load()
    corners = [px[x, y] for x in (2, 157) for y in (2, 157)]
    bg = [statistics.mean(c[i] for c in corners) for i in range(3)]

    def busy(points: list[tuple[int, int]]) -> float:
        off = sum(
            not all(abs(px[x, y][i] - bg[i]) < 26 for i in range(3)) for x, y in points
        )
        return round(off / len(points), 3)

    axis = range(0, 160, 3)
    return [
        busy([(x, y) for x in (0, 3, 6) for y in axis]),
        busy([(x, y) for x in (153, 156, 159) for y in axis]),
        busy([(x, y) for y in (0, 3, 6) for x in axis]),
        busy([(x, y) for y in (153, 156, 159) for x in axis]),
    ]


def classify(features: list[float] | None) -> str:
    if features and min(features) >= 0.55:
        return "scene"
    return "studio"


def load_features(products: list[dict]) -> dict[str, list[float] | None]:
    cache: dict = json.loads(IMG_CACHE.read_text()) if IMG_CACHE.exists() else {}
    urls = [
        (m["id"], (m.get("image") or {}).get("url"))
        for p in products
        for m in p["media"]["nodes"]
    ]
    todo = [(mid, url) for mid, url in urls if url and mid not in cache]
    if todo:
        print(f"  analyse de {len(todo)} images…")
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(lambda t: (t[0], image_features(t[1])), todo))
        cache.update(dict(results))
        IMG_CACHE.write_text(json.dumps(cache))
    return cache


SUFFIXES = {
    "studio": [
        "",
        "sur fond neutre",
        "autre vue",
        "autre cadrage",
        "vue complémentaire",
        "vue supplémentaire",
    ],
    "scene": ["en situation dans un intérieur", "mise en situation", "dans un intérieur"],
}


def plan_alts(products: list[dict], features: dict) -> list[dict]:
    plans: list[dict] = []
    for p in products:
        subject = subject_of(p)
        # Un packshot de variante porte la valeur d'option dans son nom de fichier.
        # On lit la valeur telle qu'elle sera après renommage, pas telle qu'elle
        # est dans le dump, sinon l'alt réintroduit le libellé fournisseur.
        table = dict(RENAMES.get(p["handle"], []))
        by_slug = {}
        for opt in p["options"]:
            for v in opt["optionValues"]:
                final = table.get(v["name"]) or generic_rename(v["name"]) or v["name"]
                by_slug[slugify(v["name"])] = final
        # Le fichier packshot garde le slug du libellé d'origine même après
        # renommage : on garde donc les deux entrées.
        for before, after in table.items():
            by_slug.setdefault(slugify(before), after)
        used: set[str] = set()
        counters: dict[str, int] = {}
        edits: list[dict] = []
        for m in p["media"]["nodes"]:
            url = (m.get("image") or {}).get("url") or ""
            filename = url.rsplit("/", 1)[-1].split("?")[0]
            stem = re.sub(r"\.(jpg|jpeg|png|webp)$", "", filename, flags=re.I)
            variant_slug = None
            match = re.match(rf"^{re.escape(p['handle'])}-(.+?)-g\d+$", stem)
            if match:
                variant_slug = match.group(1)

            if variant_slug:
                label = (
                    by_slug.get(variant_slug)
                    or SLUG_LABELS.get(variant_slug)
                    or variant_slug.replace("-", " ")
                )
                new = f"{subject}, {label.lower()}"
                # Deux packshots ne doivent pas annoncer la même teinte.
                base = new
                n = 2
                while new in used:
                    new = f"{base} {n}"
                    n += 1
            else:
                bucket = classify(features.get(m["id"]))
                i = counters.get(bucket, 0)
                counters[bucket] = i + 1
                choices = SUFFIXES[bucket]
                # Au-delà de la liste on répète la dernière formule : sur une
                # galerie de trente photos, un alt en double vaut mieux qu'un
                # « vue 27 » qui ne décrit rien.
                suffix = choices[min(i, len(choices) - 1)]
                new = f"{subject}, {suffix}" if suffix else subject

            used.add(new)
            new = typographic(new)
            if any(d in new for d in DASHES):
                raise SystemExit(f"cadratin dans un alt généré : {new!r}")
            if new != (m.get("alt") or ""):
                edits.append({"media_id": m["id"], "before": m.get("alt") or "", "after": new})
        if edits:
            plans.append({"handle": p["handle"], "id": p["id"], "alts": edits})
    return plans


# ───────────────── specs_html qui répètent un libellé renommé ─────────────────

PDP_COPY = ROOT / "pdp-copy.json"

# handle -> {intitulé de la ligne specs : axe d'option qui l'alimente}. Seules
# les lignes qui recopiaient un libellé fournisseur renommé sont reprises ; les
# lignes « Diamètre : 40 cm et 50 cm » restent vraies et ne bougent pas.
SPEC_LINES: dict[str, dict[str, str]] = {
    "lustre-anneau-led-led-134962": {"Modèle": "Modèle"},
    "lustre-cristal-led-677865": {"Finition": "Finition"},
    "plafonnier-led-565566": {"Finition": "Finition"},
    "plafonnier-led-led-698635": {"Modèle": "Modèle", "Lumière": "Température"},
    "suspension-bois-193329": {"Modèle": "Modèle"},
    "suspension-effet-pierre-343987": {"Lumière": "Température"},
    "suspension-effet-pierre-led-338324": {"Lumière": "Température"},
    "suspension-verre-928640": {"Modèle": "Modèle"},
    "suspension-deco-led-837156": {"Émail": "Émail"},
}


def et_join(items: list[str]) -> str:
    if len(items) <= 1:
        return items[0] if items else ""
    return f"{', '.join(items[:-1])} et {items[-1]}"


def refresh_specs(products: list[dict], copies: dict) -> list[str]:
    """Réaligne les lignes de specs sur les libellés d'option actuels."""
    changed: list[str] = []
    by_handle = {p["handle"]: p for p in products}
    for handle, lines in SPEC_LINES.items():
        copy = copies[handle]
        html = copy["specs_html"]
        axes = {o["name"]: [v["name"] for v in o["optionValues"]] for o in by_handle[handle]["options"]}
        for label, axis in lines.items():
            cap = 6 if axis in ("Température", "Éclairage") else 8
            # « Céladon vert » et « Céladon vert 2 » sont la même finition sous
            # deux références fournisseur : le sélecteur doit les distinguer,
            # pas la fiche technique.
            values: list[str] = []
            for name in axes[axis]:
                base = re.sub(r" \d+$", "", name)
                if base not in values:
                    values.append(base)
            joined = et_join(values[:cap])
            pattern = re.compile(rf"(<li><strong>{re.escape(label)} :</strong> ).*?(</li>)")
            new_html, n = pattern.subn(lambda m: m.group(1) + joined + m.group(2), html, count=1)
            if not n:
                print(f"  warn ligne {label!r} introuvable dans {handle}")
                continue
            html = new_html
        if html != copy["specs_html"]:
            copy["specs_html"] = html
            changed.append(handle)
    return changed


def cmd_specs() -> None:
    from apply_pdp import fetch_products, push_copy

    products = json.loads(DUMP.read_text())
    copies = json.loads(PDP_COPY.read_text())
    changed = refresh_specs(products, copies)
    for handle in changed:
        print(f"  {handle}: {copies[handle]['specs_html']}")
    print(f"{len(changed)} specs_html réalignés")
    if "--apply" not in sys.argv:
        print("dry-run (relancer avec --apply)")
        return
    PDP_COPY.write_text(json.dumps(copies, ensure_ascii=False, indent=2) + "\n")
    live = [p for p in fetch_products() if p["handle"] in changed]
    push_copy(live, copies)
    print(f"push_copy sur {len(live)} fiches")


# ───────────────────────────────── mutations ─────────────────────────────────

OPTION_UPDATE = """
mutation U($productId: ID!, $option: OptionUpdateInput!,
           $optionValuesToUpdate: [OptionValueUpdateInput!],
           $variantStrategy: ProductOptionUpdateVariantStrategy) {
  productOptionUpdate(
    productId: $productId
    option: $option
    optionValuesToUpdate: $optionValuesToUpdate
    variantStrategy: $variantStrategy
  ) {
    userErrors { field message }
  }
}
"""

FILE_UPDATE = """
mutation fileUpdate($files: [FileUpdateInput!]!) {
  fileUpdate(files: $files) {
    files { id alt }
    userErrors { field message }
  }
}
"""


def apply_option_renames(pid: str, option_id: str, pairs: list[tuple[str, str]]) -> list:
    return gql(
        OPTION_UPDATE,
        {
            "productId": pid,
            "option": {"id": option_id},
            "optionValuesToUpdate": [{"id": vid, "name": name} for vid, name in pairs],
            "variantStrategy": "LEAVE_AS_IS",
        },
    )["productOptionUpdate"]["userErrors"]


def apply_alts(edits: list[dict]) -> list:
    errors: list = []
    for i in range(0, len(edits), 20):
        chunk = edits[i : i + 20]
        errors.extend(
            gql(FILE_UPDATE, {"files": [{"id": e["media_id"], "alt": e["after"]} for e in chunk]})[
                "fileUpdate"
            ]["userErrors"]
        )
        time.sleep(THROTTLE)
    return errors


# ─────────────────────────────────── main ───────────────────────────────────


def main() -> None:
    if "--dump" in sys.argv:
        products = fetch_all()
        DUMP.write_text(json.dumps(products, ensure_ascii=False))
        print(f"{len(products)} fiches dumpées -> {DUMP.name}")
        return

    if not DUMP.exists():
        raise SystemExit(f"dump absent : lancer --dump d'abord ({DUMP.name})")

    if "--specs" in sys.argv:
        cmd_specs()
        return

    products = json.loads(DUMP.read_text())

    value_plans = plan_option_values(products)
    features = load_features(products)
    alt_plans = plan_alts(products, features)
    n_values = sum(len(p["renames"]) for p in value_plans)
    n_alts = sum(len(p["alts"]) for p in alt_plans)
    print(f"{n_values} valeurs à renommer sur {len(value_plans)} fiches")
    print(f"{n_alts} alts à réécrire sur {len(alt_plans)} fiches")

    if "--apply" not in sys.argv:
        for plan in value_plans:
            for r in plan["renames"]:
                print(f"  VAL {plan['handle']} [{r['option_name']}] {r['before']!r} -> {r['after']!r}")
        for plan in alt_plans[:8]:
            for a in plan["alts"]:
                print(f"  ALT {plan['handle']} {a['before']!r} -> {a['after']!r}")
        print("dry-run (relancer avec --apply)")
        return

    by_handle = {p["handle"]: p for p in products}
    ok_values = ok_alts = 0
    sku_fails: list[str] = []
    errors: list[str] = []

    for plan in value_plans:
        before_skus = skus_of(by_handle[plan["handle"]])
        by_option: dict[str, list[tuple[str, str]]] = {}
        for r in plan["renames"]:
            by_option.setdefault(r["option_id"], []).append((r["value_id"], r["after"]))
        applied = 0
        for option_id, pairs in by_option.items():
            errs = apply_option_renames(plan["id"], option_id, pairs)
            if errs:
                errors.append(f"{plan['handle']} option {option_id}: {errs}")
                continue
            applied += len(pairs)
            time.sleep(THROTTLE)
        after_skus = skus_of(fetch_product(plan["id"]))
        if after_skus != before_skus:
            sku_fails.append(plan["handle"])
            print(f"  SKU FAIL {plan['handle']}")
        ok_values += applied
        print(f"  OK {plan['handle']} ({applied} valeurs, {len(after_skus)} SKU intacts)")

    for plan in alt_plans:
        errs = apply_alts(plan["alts"])
        if errs:
            errors.append(f"{plan['handle']} alts: {errs}")
        else:
            ok_alts += len(plan["alts"])

    print(f"\n{ok_values} valeurs renommées, {ok_alts} alts réécrits")
    print(f"{len(sku_fails)} SKU FAIL, {len(errors)} userErrors")
    for e in errors[:30]:
        print("  ERR", e)


if __name__ == "__main__":
    main()
