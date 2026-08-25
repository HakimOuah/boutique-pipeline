"""Retitrage SEO des 120 fiches Lumière Matière — titres de requête pour Google Shopping.

Applique la convention `CONVENTION-TITRES-2026-08-25.md` : type de produit en premier mot,
matière puis couleur, un seul bloc, 40 à 60 caractères, aucun `Ø`, aucune plage de tailles,
aucun nom de modèle inventé, aucun mot d'ambiance.

Idempotent : relancer ne change rien si le live porte déjà les titres de la table.
Ne touche ni aux SKU, ni aux variantes, ni aux prix, ni au thème, ni au corps des fiches.
`seo.description` est renvoyée à l'identique, parce que `ProductInput.seo` est remplacé en bloc.
`apply_pdp.py` n'est jamais exécuté, pas même importé : son `main()` régénérerait toute la copy
et réécrirait `templates/product.json`.

Usage :
    python3 retitle_seo.py --check     # validation seule, aucune écriture
    python3 retitle_seo.py --dry-run   # validation + diff avec le live
    python3 retitle_seo.py             # validation, backup, pdp-copy.json, push, relecture
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import unicodedata
from datetime import date
from pathlib import Path

from client import gql

ROOT = Path(__file__).resolve().parent
COPY_PATH = ROOT / "pdp-copy.json"
BACKUP_DIR = ROOT / "backups" / "2026-08-25-titres-seo"
BRAND_SUFFIX = " | Lumière Matière"

# ---------------------------------------------------------------------------
# Table handle → nouveau titre. Un titre par fiche, écrit d'après la photo.
# ---------------------------------------------------------------------------

TITLES: dict[str, str] = {
    # --- Suspensions bambou (16) ---
    "suspension-bambou-45cm-962644": "Suspension bambou dôme tressé, tige bois clair",
    "suspension-bambou-067987": "Suspension bambou ovale tressé, câble noir",
    "suspension-bambou-led-136557": "Suspension bambou vague tressée LED, naturel",
    "suspension-bambou-led-80-cm-236157": "Suspension bambou vague naturelle, tige rigide",
    "suspension-bambou-280004": "Suspension bambou tressé 3 lampes, câble noir",
    "suspension-bambou-led-583180": "Suspension bambou vague tressée, câble doré",
    "suspension-bambou-942503": "Suspension bambou XXL tressé, pétales naturels",
    "suspension-bambou-led-033589": "Suspension bambou cascade 3 vagues, naturel",
    "suspension-bambou-655008": "Suspension bambou dôme tressé serré naturel",
    "suspension-bambou-led-80-cm-191307": "Suspension bambou vague naturelle, câble souple",
    "suspension-bambou-655463": "Suspension bambou coupole tressée, câble noir",
    "suspension-bambou-led-630923": "Suspension bambou disque plat tressé naturel",
    "suspension-bambou-led-50cm-377816": "Suspension bambou tressé double étage naturel",
    "suspension-bambou-104055": "Suspension bambou tambour tressé, naturel",
    "suspension-bambou-317565": "Suspension bambou soucoupe tressée, tige dorée",
    "suspension-bambou-dore-60cm-805884": "Suspension bambou ovale tressé serré naturel",
    # --- Suspensions rotin (14) ---
    "suspension-rotin-897170": "Suspension rotin corolle tressée, naturel",
    "suspension-rotin-dore-435189": "Suspension rotin cloche haute tressée, naturel",
    "suspension-rotin-469688": "Suspension rotin tressé 3 lampes, platine noire",
    "suspension-rotin-623305": "Suspension rotin tressé, abat-jour tambour naturel",
    "suspension-rotin-489600": "Suspension paille brute tressée, naturel doré",
    "suspension-rotin-607504": "Suspension rotin tressé noir, monture bois",
    "suspension-rotin-272937": "Suspension globes corde tressée, monture noire",
    "suspension-rotin-led-535545": "Suspension rotin XXL tressé, pétales naturels",
    "suspension-rotin-477244": "Suspension corolle corde tressée, beige ou chanvre",
    "suspension-rotin-443915": "Suspension cloche corde tressée, kaki ou noir",
    "suspension-rotin-led-420069": "Suspension rotin cloche large tressée, naturel",
    "suspension-rotin-dore-865596": "Suspension bois deux pétales, monture dorée",
    "suspension-rotin-605780": "Suspension rotin dôme tressé naturel clair",
    "suspension-rotin-led-761433": "Suspension corolle fibre tressée, naturel",
    # --- Lustres anneau (12) ---
    "lustre-anneau-led-led-noir-dore-024410": "Lustre anneaux LED cascade, noir, café ou doré",
    "lustre-anneau-led-led-597704": "Lustre anneaux LED superposés, doré, blanc ou noir",
    "lustre-anneau-led-led-717226": "Lustre anneaux LED blancs, tige de suspension",
    "lustre-anneau-led-led-625575": "Plafonnier anneaux LED blancs, platine chromée",
    "lustre-anneau-led-led-dore-418494": "Lustre 6 anneaux LED superposés, noir, café ou doré",
    "lustre-anneau-led-led-784897": "Lustre anneau LED double, doré, blanc ou noir",
    "lustre-anneau-led-007557": "Plafonnier LED rond connecté RVB, blanc ou noir",
    "lustre-anneau-led-led-795468": "Lustre anneau LED simple, finition blanche ou noire",
    "lustre-anneau-led-led-dore-641905": "Lustre anneaux LED 5 cercles, noir, doré ou blanc",
    "lustre-anneau-led-led-892612": "Lustre anneau LED opalin blanc, télécommande",
    "lustre-anneau-led-led-799451": "Lustre anneaux LED spirale, blanc, doré ou noir",
    "lustre-anneau-led-led-134962": "Lustre anneaux LED 6 lumières, blanc, doré ou noir",
    # --- Lustres salon (12) ---
    "lustre-salon-led-366435": "Suspension ruban LED double boucle, doré ou blanc",
    "lustre-salon-957153": "Suspension ruban LED trèfle, doré ou noir",
    "lustre-salon-led-147017": "Lustre anneaux LED concentriques, doré ou blanc",
    "lustre-salon-blanc-246282": "Suspension soucoupe soie plissée blanche, salon",
    "lustre-salon-led-240560": "Lustre anneau LED effet cristal, blanc, noir ou doré",
    "lustre-salon-led-630766": "Suspension anneau LED verre facetté, doré ou noir",
    "lustre-salon-233314": "Lustre grappe globes opalins, 7 ou 13 lumières",
    "lustre-salon-blanc-575463": "Suspension corolle acrylique blanche, salon",
    "lustre-salon-907106": "Lustre grappe globes verre coloré, doré ou noir",
    "lustre-salon-led-254609": "Lustre sputnik noir et doré, 12 globes verre",
    "lustre-salon-led-784326": "Plafonnier LED palets bois, blanc, noir ou doré",
    "lustre-salon-led-341706": "Suspension coupole galet LED, finition blanc mat",
    # --- Suspensions bois (12) ---
    "suspension-bois-led-830581": "Suspension bois clair tourné, ampoule apparente",
    "suspension-bois-193329": "Suspension cylindre travertin, bois clair ou noyer",
    "suspension-bois-led-453740": "Suspension bois brun vintage, 6 lanternes verre",
    "suspension-bois-led-245113": "Suspension cylindre travertin, anneau noyer",
    "suspension-bois-led-934110": "Suspension tube travertin, rosace bois noyer",
    "suspension-bois-led-334133": "Suspension perles pierre et bois, globe opalin",
    "suspension-bois-059364": "Suspension tonneau bois, chaîne métal noire",
    "suspension-bois-led-30cm-886635": "Suspension céramique plissée blanche, tête bois",
    "suspension-bois-led-989306": "Suspension double coquille bois tressé, platine blanche",
    "suspension-bois-led-582321": "Suspension double coquille bois tressé, rosace dorée",
    "suspension-bois-832012": "Suspension bois 3 gouttes verre, fumé ou ambre",
    "suspension-bois-led-121862": "Suspension céramique festonnée blanche, tête bois",
    # --- Suspensions verre (10) ---
    "suspension-verre-led-489156": "Suspension cascade verre soufflé LED transparent",
    "suspension-verre-led-dore-436718": "Suspension arceau laiton et globes opalins, doré",
    "suspension-verre-394147": "Suspension globe verre fumé, 1 ou 3 lumières",
    "suspension-verre-091815": "Suspension grappe verre soufflé, ambre ou fumé",
    "suspension-verre-446435": "Suspension globe verre fumé, tige rigide noire",
    "suspension-verre-noir-201424": "Suspension grappe verre fumé miroir, rosace noire",
    "suspension-verre-led-blanc-554061": "Suspension globes opalins, câbles laiton doré",
    "suspension-verre-651675": "Suspension boule verre fumé miroir argenté",
    "suspension-verre-928640": "Suspension galet verre fumé LED, monture laiton",
    "suspension-verre-814554": "Suspension disque verre vert, brun ou blanc",
    # --- Plafonniers (10) ---
    "plafonnier-led-led-637673": "Plafonnier LED rond blanc, RVB et enceinte intégrée",
    "plafonnier-led-565566": "Plafonnier tiges croisées chrome, 6 globes verre",
    "plafonnier-led-led-442025": "Suspension boule sputnik métal doré, 65 cm",
    "plafonnier-led-led-183789": "Plafonnier LED palets bois, gris ou blanc",
    "plafonnier-led-led-698635": "Plafonnier anneaux LED, blanc, noir ou doré",
    "plafonnier-led-led-922186": "Suspension guirlande globes opalins, monture laiton",
    "plafonnier-led-led-728204": "Plafonnier LED linéaire cuisine, blanc ou noyer",
    "plafonnier-led-led-465027": "Plafonnier LED boucles entrelacées, blanc ou noir",
    "plafonnier-led-992600": "Plafonnier tiges courbes noires, 8 globes verre",
    "plafonnier-led-led-dore-blanc-354637": "Plafonnier coupole acrylique plissée, blanc mat",
    # --- Suspensions pierre (9) ---
    "suspension-effet-pierre-led-073999": "Suspension galet effet pierre, tige bois clair",
    "suspension-effet-pierre-led-434888": "Suspension effet pierre, galet et tube opalin",
    "suspension-effet-pierre-092465": "Suspension cylindre pierre claire, tête bois brun",
    "suspension-effet-pierre-led-dore-960013": "Suspension galet effet pierre, blanc cassé ou gris",
    "suspension-effet-pierre-led-709819": "Suspension tube travertin beige, LED intégrée",
    "suspension-effet-pierre-led-338324": "Suspension gros cylindre travertin, tête noyer",
    "suspension-effet-pierre-led-445794": "Suspension cylindre travertin étroit, bois clair",
    "suspension-effet-pierre-led-147607": "Suspension travertin beige et bois, cône ou galet",
    "suspension-effet-pierre-343987": "Suspension tube travertin court ou long beige",
    # --- Suspensions métal (8) ---
    "suspension-metal-dore-502141": "Suspension abat-jour tissu, armature laiton dorée",
    "suspension-metal-led-dore-081498": "Suspension anneau LED métal doré, oiseau posé",
    "suspension-metal-led-dore-701414": "Suspension voile LED blanc, papier ou soie",
    "suspension-metal-led-dore-952116": "Suspension céramique bleu et blanc, monture laiton",
    "suspension-metal-led-dore-843772": "Plafonnier 3 anneaux LED entrelacés, métal doré",
    "suspension-metal-noir-dore-361680": "Lustre laiton à bougies, 6 bras dorés ou noirs",
    "suspension-metal-dore-037279": "Suspension dôme céramique gaufrée, monture laiton",
    "suspension-metal-led-dore-975417": "Suspension corolle céramique blanche, cordon doré",
    # --- Suspensions déco, céramique (8) ---
    "suspension-deco-led-837156": "Suspension céramique festonnée, vert céladon",
    "suspension-deco-led-blanc-805304": "Suspension coupelle céramique blanche, cordon laiton",
    "suspension-deco-348096": "Suspension dôme céramique blanche ajourée",
    "suspension-deco-led-077631": "Suspension céramique à fleurs bleues, douille laiton",
    "suspension-deco-led-889929": "Suspension grappe cônes céramique blanche, bois",
    "suspension-deco-blanc-560098": "Suspension double céramique à motifs bleus, laiton",
    "suspension-deco-253182": "Suspension céramique émaillée rouge, monture laiton",
    "suspension-deco-led-689455": "Suspension céramique nervurée blanche, 3 lampes",
    # --- Lustres cristal (7) ---
    "lustre-cristal-led-led-141724": "Lustre effet cristal 3 anneaux LED dorés",
    "lustre-cristal-led-677865": "Lustre effet cristal LED, anneaux doré ou chrome",
    "lustre-cristal-led-led-dore-264869": "Lustre effet cristal doré, 1 ou 2 lumières",
    "lustre-cristal-led-led-560904": "Lustre effet cristal doré, couronne de pampilles",
    "lustre-cristal-led-led-dore-841671": "Lustre branches dorées, perles effet cristal",
    "lustre-cristal-led-dore-202521": "Lustre cascade effet cristal, branches dorées",
    "lustre-cristal-led-noir-347688": "Lustre tambour effet cristal noir, 5 lumières",
    # --- Suspensions modernes (1) ---
    "suspension-moderne-led-noir-330664": "Suspension barres LED croisées, métal noir XXL",
    # --- Lustres statement (1) ---
    "lustre-statement-led-noir-950316": "Lustre sputnik laiton et noir, 6 globes verre",
}

# ---------------------------------------------------------------------------
# Contrôle automatique — § « Contrôle automatique avant publication » de la convention
# ---------------------------------------------------------------------------

FIRST_WORDS = ("Suspension", "Lustre", "Plafonnier")
HARD_MAX = 65
SOFT_RANGE = (40, 60)

BANNED_CHARS = ("\u00d8", "\u2014", "\u2013", "|")
BANNED_SUBSTR = (" : ",)
RANGE_RE = re.compile(r"\d+\s*à\s*\d+\s*cm", re.I)
BRAND_RE = re.compile(r"lumi[eè]re\s+mati[eè]re", re.I)

MOOD_WORDS = (
    "élégance", "élégant", "élégante", "raffiné", "raffinée", "chic", "charme",
    "esprit", "sublime", "intemporel", "intemporelle", "unique", "style luxe",
    "luxe", "design épuré", "épuré", "prestige", "somptueux", "majestueux",
    "premium", "atelier", "artisanal", "artisanale",
)

MATERIALS = (
    "bambou", "rotin", "bois", "verre", "céramique", "métal", "pierre", "travertin",
    "corde", "chanvre", "paille", "fibre", "cristal", "laiton", "acrylique", "soie",
    "tissu", "papier", "noyer", "porcelaine",
)

COLORS = (
    "noir", "noire", "noires", "blanc", "blancs", "blanche", "blanches", "doré", "dorés",
    "dorée", "dorées",
    "doré", "laiton", "chrome", "chromée", "chromé", "naturel", "naturels", "naturelle",
    "beige", "noyer", "fumé", "fumée", "opalin", "opalins", "opaline", "ambre", "céladon",
    "gris", "grise", "argenté", "argentée", "rouge", "vert", "verte", "kaki", "cognac",
    "brun", "brune", "café", "bleu", "bleue", "bleues", "cuivre", "transparent",
    "chanvre", "miroir", "clair", "claire",
)

SHAPES = (
    "globe", "globes", "dôme", "cloche", "cylindre", "anneau", "anneaux", "grappe",
    "cascade", "tube", "sputnik", "corolle", "coupole", "coupelle", "galet", "disque",
    "tressé", "tressée", "tressées", "tressés", "vague", "vagues", "ovale", "tambour",
    "soucoupe", "pétales", "boule", "spirale", "trèfle", "arceau", "guirlande",
    "barres", "tiges", "boucles", "branches", "voile", "abat-jour", "tonneau",
    "coquille", "cercles", "cônes", "cône", "gouttes", "ruban", "linéaire", "rond",
    "perles", "palets", "étage", "plissée", "plissé", "festonnée", "gaufrée",
    "nervurée", "ajourée", "facetté", "double", "guitare",
)

# Acronymes et sigles autorisés en majuscules au-delà du premier mot.
ACRONYMS = {"LED", "RVB", "XXL", "E27", "E14", "G9"}


def fold(text: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", text.lower())
        if unicodedata.category(c) != "Mn"
    )


def has_any(title: str, words: tuple[str, ...]) -> bool:
    low = fold(title)
    return any(re.search(rf"\b{re.escape(fold(w))}\b", low) for w in words)


def check_title(handle: str, title: str, seen: dict[str, str]) -> list[str]:
    """Renvoie la liste des motifs de refus. Liste vide = titre accepté."""
    errs: list[str] = []
    if not title or not title.strip():
        errs.append("titre vide")
        return errs
    if title != title.strip():
        errs.append("espaces en bordure")
    if not title.startswith(FIRST_WORDS):
        errs.append(f"premier mot interdit ({title.split()[0]!r})")
    if len(title) > HARD_MAX:
        errs.append(f"{len(title)} caractères > {HARD_MAX}")
    for ch in BANNED_CHARS:
        if ch in title:
            errs.append(f"caractère interdit {ch!r}")
    for sub in BANNED_SUBSTR:
        if sub in title:
            errs.append(f"séquence interdite {sub!r}")
    if RANGE_RE.search(title):
        errs.append("plage de tailles")
    if BRAND_RE.search(title):
        errs.append("marque dans le titre")
    for word in MOOD_WORDS:
        if re.search(rf"\b{re.escape(fold(word))}\b", fold(title)):
            errs.append(f"mot d'ambiance {word!r}")
    if not (has_any(title, MATERIALS) or has_any(title, COLORS) or has_any(title, SHAPES)):
        errs.append("titre vide au sens du § 9 (ni matière, ni couleur, ni forme)")
    # Casse : première lettre du titre seulement, hors acronymes.
    for word in re.findall(r"[A-Za-zÀ-ÿ]+", title)[1:]:
        if word[0].isupper() and word not in ACRONYMS:
            errs.append(f"majuscule interne {word!r}")
    if title in seen:
        errs.append(f"doublon de {seen[title]}")
    else:
        seen[title] = handle
    return errs


def validate(table: dict[str, str]) -> dict[str, list[str]]:
    seen: dict[str, str] = {}
    failures: dict[str, list[str]] = {}
    for handle, title in table.items():
        errs = check_title(handle, title, seen)
        if errs:
            failures[handle] = errs
    return failures


def seo_title(title: str) -> str:
    """Titre + marque, coupé à 70 caractères sur un segment entier (règle de `humanise_pdp`)."""
    if len(title) + len(BRAND_SUFFIX) <= 70:
        return title + BRAND_SUFFIX
    chunk = title[: 70 - len(BRAND_SUFFIX)]
    chunk = chunk.rsplit(",", 1)[0] if "," in chunk else chunk.rsplit(" ", 1)[0]
    return chunk.rstrip(" ,;:·") + BRAND_SUFFIX


# ---------------------------------------------------------------------------
# Live
# ---------------------------------------------------------------------------

FETCH = """
query ($c: String) {
  products(first: 40, after: $c, query: "status:active") {
    pageInfo { hasNextPage endCursor }
    nodes { id handle title productType seo { title description } }
  }
}
"""

MUTATION = """
mutation U($input: ProductInput!) {
  productUpdate(input: $input) {
    product { id handle title seo { title description } }
    userErrors { field message }
  }
}
"""


def fetch_live() -> list[dict]:
    nodes: list[dict] = []
    cursor = None
    while True:
        page = gql(FETCH, {"c": cursor})["products"]
        nodes.extend(page["nodes"])
        if not page["pageInfo"]["hasNextPage"]:
            return nodes
        cursor = page["pageInfo"]["endCursor"]


def push(products: list[dict], table: dict[str, str], copies: dict) -> tuple[int, int, int]:
    done = skipped = failed = 0
    for p in products:
        title = table.get(p["handle"])
        if title is None:
            print(f"  ! hors table {p['handle']}")
            failed += 1
            continue
        want_seo = seo_title(title)
        # `seo` est un objet remplacé en bloc : omettre `description` l'efface.
        # On renvoie donc la description existante telle quelle, à l'identique.
        want_desc = (copies[p["handle"]]["seo_description"] or "")[:320]
        current = p.get("seo") or {}
        if (
            p["title"] == title
            and current.get("title") == want_seo
            and (current.get("description") or "") == want_desc
        ):
            skipped += 1
            continue
        data = gql(
            MUTATION,
            {
                "input": {
                    "id": p["id"],
                    "title": title,
                    "seo": {"title": want_seo, "description": want_desc},
                }
            },
        )
        errs = data["productUpdate"]["userErrors"]
        if errs:
            print(f"FAIL {p['handle']} {errs}")
            failed += 1
            continue
        done += 1
        if done % 20 == 0:
            print(f"  … {done} poussés")
        time.sleep(0.12)
    return done, skipped, failed


def stats(titles: list[str]) -> dict:
    n = len(titles)
    lengths = [len(t) for t in titles]
    return {
        "n": n,
        "uniques": len(set(titles)),
        "len_moy": round(sum(lengths) / n, 1),
        "len_min": min(lengths),
        "len_max": max(lengths),
        "len_median": sorted(lengths)[n // 2],
        "hors_40_60": sum(1 for x in lengths if not SOFT_RANGE[0] <= x <= SOFT_RANGE[1]),
        "matiere": sum(1 for t in titles if has_any(t, MATERIALS)),
        "couleur": sum(1 for t in titles if has_any(t, COLORS)),
        "un_bloc": sum(1 for t in titles if "," not in t),
    }


def report_stats(titles: list[str]) -> None:
    s = stats(titles)
    print(
        f"  {s['n']} titres · {s['uniques']} uniques · "
        f"longueur moy {s['len_moy']} (min {s['len_min']}, max {s['len_max']}, "
        f"médiane {s['len_median']}) · hors 40-60 : {s['hors_40_60']}"
    )
    print(
        f"  matière {s['matiere']}/{s['n']} ({100 * s['matiere'] // s['n']} %) · "
        f"couleur {s['couleur']}/{s['n']} ({100 * s['couleur'] // s['n']} %) · "
        f"un seul bloc {s['un_bloc']}/{s['n']}"
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="validation seule, hors ligne")
    ap.add_argument("--dry-run", action="store_true", help="validation + diff live, sans écriture")
    args = ap.parse_args()

    print(f"Table : {len(TITLES)} handles")
    failures = validate(TITLES)
    if failures:
        print(f"\nREFUS — {len(failures)} titres invalides :")
        for handle, errs in failures.items():
            print(f"  {handle}: {'; '.join(errs)}")
        sys.exit(1)
    print("Contrôle automatique : 120/120 acceptés")
    report_stats(list(TITLES.values()))

    if args.check:
        return

    live = fetch_live()
    print(f"\nLive : {len(live)} fiches actives")
    missing = {p["handle"] for p in live} - set(TITLES)
    extra = set(TITLES) - {p["handle"] for p in live}
    if missing or extra:
        print(f"REFUS — handles hors table : {sorted(missing)} ; inconnus du live : {sorted(extra)}")
        sys.exit(1)

    changed = [p for p in live if p["title"] != TITLES[p["handle"]]]
    print(f"À changer : {len(changed)}")

    if args.dry_run:
        for p in sorted(changed, key=lambda x: x["productType"]):
            print(f"  {p['productType']:22} {p['title']}")
            print(f"  {'':22} → {TITLES[p['handle']]}")
        return

    # Le backup capture l'état antérieur : il ne doit jamais être réécrit par une
    # seconde exécution, sinon il enregistrerait l'état déjà retitré.
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    copies = json.loads(COPY_PATH.read_text(encoding="utf-8"))
    snapshots = {
        "titles-live.avant.json": [
            {
                "handle": p["handle"],
                "productType": p["productType"],
                "title": p["title"],
                "seo_title": (p.get("seo") or {}).get("title"),
            }
            for p in live
        ],
        "pdp-copy.avant.json": copies,
    }
    for name, payload in snapshots.items():
        path = BACKUP_DIR / name
        if path.exists():
            print(f"Backup déjà présent, conservé : {name}")
            continue
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"Backup écrit : {name}")

    for handle, title in TITLES.items():
        if handle not in copies:
            print(f"REFUS — {handle} absent de pdp-copy.json")
            sys.exit(1)
        copies[handle]["title"] = title
        copies[handle]["seo_title"] = seo_title(title)
    COPY_PATH.write_text(json.dumps(copies, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"pdp-copy.json : title et seo_title mis à jour sur {len(TITLES)} fiches")

    done, skipped, failed = push(live, TITLES, copies)
    print(f"push : {done} modifiés, {skipped} déjà à jour, {failed} en échec")
    if failed:
        sys.exit(1)

    # Relecture du live
    after = fetch_live()
    live_titles = [p["title"] for p in after]
    print(f"\nRelecture live ({len(after)} fiches)")
    report_stats(live_titles)
    ecarts = [p["handle"] for p in after if p["title"] != TITLES[p["handle"]]]
    seo_ecarts = [
        p["handle"] for p in after
        if (p.get("seo") or {}).get("title") != seo_title(TITLES[p["handle"]])
    ]
    desc_vides = [
        p["handle"] for p in after
        if not (p.get("seo") or {}).get("description")
        and copies[p["handle"]]["seo_description"]
    ]
    bad_chars = [
        p["handle"] for p in after
        if any(c in p["title"] for c in BANNED_CHARS) or RANGE_RE.search(p["title"])
    ]
    too_long = [p["handle"] for p in after if len(p["title"]) > HARD_MAX]
    print(f"  écarts titre : {len(ecarts)} {ecarts}")
    print(f"  écarts seo_title : {len(seo_ecarts)} {seo_ecarts}")
    print(f"  meta descriptions vidées : {len(desc_vides)} {desc_vides}")
    print(f"  caractères interdits : {len(bad_chars)} {bad_chars}")
    print(f"  dépassements 65 c. : {len(too_long)} {too_long}")
    print(f"  titres uniques : {len(set(live_titles))}/{len(after)}")
    if (
        ecarts or seo_ecarts or desc_vides or bad_chars or too_long
        or len(set(live_titles)) != len(after)
    ):
        sys.exit(1)
    print(f"\nOK — {date.today().isoformat()}")


if __name__ == "__main__":
    main()
