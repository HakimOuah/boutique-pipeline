#!/usr/bin/env python3
"""Retire les prix barrés, traduit et réordonne les options de variantes (SKU DSers inchangés)."""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from client import gql  # noqa: E402

STATE = ROOT / "variants-fix-state.json"
REPORT = ROOT / "variants-fix-rapport.json"

WAREHOUSES = {
    "china mainland": "Chine",
    "china": "Chine",
    "cn": "Chine",
    "germany": "Allemagne",
    "united kingdom": "Royaume-Uni",
    "uk": "Royaume-Uni",
    "united states": "États-Unis",
    "usa": "États-Unis",
    "spain": "Espagne",
    "france": "France",
    "poland": "Pologne",
    "italy": "Italie",
    "czech republic": "Tchéquie",
    "netherlands": "Pays-Bas",
    "belgium": "Belgique",
}

# plus longs d'abord
PHRASES: list[tuple[str, str]] = [
    (r"remote with dimmable", "Variable (télécommande)"),
    (r"remote control dim", "Variable (télécommande)"),
    (r"remote control", "Télécommande"),
    (r"3 teintes light", "3 teintes"),
    (r"3-\s*colors", "3 teintes"),
    (r"3 color temperature", "3 teintes"),
    (r"tri color", "3 teintes"),
    (r"chrome light body", "Chrome"),
    (r"(\d+)-light pendant", r"\1 lumières"),
    (r"110v\s*220v", "110–220 V"),
    (r"\bgeen\b", "Vert"),
    (r"(\d+)\s*light\b", r"\1 lumières"),
    (r"\bcolor\b", ""),
    (r"rc-stepless dimming", "Variation continue (télécommande)"),
    (r"stepless dimming", "Variation continue (télécommande)"),
    (r"rc dimmable", "Variable (télécommande)"),
    (r"brightness dimmale", "Variable (télécommande)"),
    (r"brightnes dimmable", "Variable (télécommande)"),
    (r"brightness dimmable", "Variable (télécommande)"),
    (r"dimmable with remote", "Variable (télécommande)"),
    (r"remote dimming", "Variable (télécommande)"),
    (r"three-color light", "3 teintes"),
    (r"3 color light", "3 teintes"),
    (r"tricolor light", "3 teintes"),
    (r"no e27 bulb", "ampoule E27 non fournie"),
    (r"no e27", "sans ampoule E27"),
    (r"noe27", "sans ampoule E27"),
    (r"warm white bulb", "Blanc chaud"),
    (r"cool white bulb", "Blanc froid"),
    (r"cold white bulb", "Blanc froid"),
    (r"whitea\b", "Blanc"),
    (r"goldena\b", "Doré"),
    (r"golda\b", "Doré"),
    (r"blacka\b", "Noir"),
    (r"-a type", ""),
    (r"\bplate\b", "plat"),
    (r"\bround\b", "rond"),
    (r"\blong\b", "allongé"),
    (r"3000k", "3000 K"),
    (r"4000k", "4000 K"),
    (r"6000k", "6000 K"),
    (r"cool white no remote", "Blanc froid"),
    (r"warm white no remote", "Blanc chaud"),
    (r"natural no remote", "Blanc neutre"),
    (r"cool white\(no rc\)", "Blanc froid"),
    (r"warm white\(no rc\)", "Blanc chaud"),
    (r"tricolor \(no rc\)", "3 teintes"),
    (r"tricolor \(no rc\)", "3 teintes"),
    (r"3 color(?:s)? changeable", "3 teintes"),
    (r"3 lights? changeable", "3 teintes"),
    (r"3 lights? bulb", "3 teintes"),
    (r"not included bulb", "Ampoule non fournie"),
    (r"no included bulb", "Ampoule non fournie"),
    (r"body colour golden", "Doré"),
    (r"body colour white", "Blanc"),
    (r"body colour black", "Noir"),
    (r"gold light body", "Doré"),
    (r"black frame", "Noir"),
    (r"gold frame", "Doré"),
    (r"white frame", "Blanc"),
    (r"golden body", "Doré"),
    (r"gold color", "Doré"),
    (r"silver color", "Argenté"),
    (r"clear light", "Transparent"),
    (r"smoke grey", "Gris fumé"),
    (r"smoke gray", "Gris fumé"),
    (r"smoky grey", "Gris fumé"),
    (r"smoky gray", "Gris fumé"),
    (r"warm white 3000k", "Blanc chaud"),
    (r"cool white 6000k", "Blanc froid"),
    (r"neutral light 4000k", "Blanc neutre"),
    (r"white light 6000k", "Blanc froid"),
    (r"warm light 3000k", "Blanc chaud"),
    (r"neutral light", "Blanc neutre"),
    (r"natural light", "Blanc neutre"),
    (r"nature light", "Blanc neutre"),
    (r"white light", "Blanc neutre"),
    (r"cool white", "Blanc froid"),
    (r"cold white", "Blanc froid"),
    (r"cold light", "Blanc froid"),
    (r"warm white", "Blanc chaud"),
    (r"warm light", "Blanc chaud"),
    (r"3-colors", "3 teintes"),
    (r"3-color", "3 teintes"),
    (r"3 colors", "3 teintes"),
    (r"tricolor", "3 teintes"),
    (r"changeable", "Variable"),
    (r"no remote", ""),
    (r"no rc", ""),
    (r"no bulb", "Ampoule non fournie"),
    (r"wall lamp", "Applique"),
    (r"floor lamp", "Lampadaire"),
    (r"ceiling lamp", "Plafonnier"),
    (r"chandelier", "Lustre"),
    (r"stretch cloth", "Tissu"),
    (r"black", "Noir"),
    (r"white", "Blanc"),
    (r"golden", "Doré"),
    (r"gold", "Doré"),
    (r"silver", "Argenté"),
    (r"coffee", "Café"),
    (r"amber", "Ambre"),
    (r"chrome", "Chrome"),
    (r"copper", "Cuivre"),
    (r"bronze", "Bronze"),
    (r"champagne", "Champagne"),
    (r"orange", "Orange"),
    (r"yellow", "Jaune"),
    (r"violet", "Violet"),
    (r"purple", "Violet"),
    (r"pink", "Rose"),
    (r"rose", "Rose"),
    (r"red", "Rouge"),
    (r"blue", "Bleu"),
    (r"green", "Vert"),
    (r"brown", "Brun"),
    (r"grey", "Gris"),
    (r"gray", "Gris"),
    (r"clear", "Transparent"),
]


def _fold(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def format_size_blob(text: str) -> str:
    raw = text
    rings = None
    m = re.search(r"(\d+)\s*rings?\b", raw, re.I)
    if m:
        rings = int(m.group(1))
        raw = raw[: m.start()] + raw[m.end() :]
    m = re.search(r"(\d+)\s*ring\b", raw, re.I)
    if m:
        rings = int(m.group(1))
        raw = raw[: m.start()] + raw[m.end() :]
    m = re.search(r"(\d+)\s*r\b", raw, re.I)
    if m and rings is None:
        rings = int(m.group(1))
        raw = raw[: m.start()] + raw[m.end() :]

    lights = None
    m = re.search(r"(\d+)\s*lights?\b", raw, re.I)
    if m:
        lights = int(m.group(1))
        raw = raw[: m.start()] + raw[m.end() :]
    m = re.search(r"(\d+)\s*heads?\b", raw, re.I)
    if m and lights is None:
        lights = int(m.group(1))
        raw = raw[: m.start()] + raw[m.end() :]

    pcs = None
    m = re.search(r"(\d+)\s*pcs\b", raw, re.I)
    if m:
        pcs = int(m.group(1))
        raw = raw[: m.start()] + raw[m.end() :]

    watts = None
    m = re.search(r"(?:led\s*)?(\d+)\s*w\b", raw, re.I)
    if m:
        watts = int(m.group(1))
        raw = raw[: m.start()] + raw[m.end() :]

    cms: list[int] = []
    for m in re.finditer(r"(?:dia[x.\-]?)?\s*[dD]?(\d{2,3})\s*(?:x\s*[hH]?\s*(\d{2,3})\s*mm)?\s*cm", raw, re.I):
        cms.append(int(m.group(1)))
        raw = raw[: m.start()] + raw[m.end() :]
        # restart simpler: collect then remove
    # re-collect from original for cm numbers
    cms = [int(x) for x in re.findall(r"(\d{2,3})\s*cm", text, flags=re.I)]
    mms = re.findall(r"(\d+)\s*x\s*[hH]?\s*(\d+)\s*mm", text, flags=re.I)

    parts: list[str] = []
    if rings:
        parts.append("1 anneau" if rings == 1 else f"{rings} anneaux")
    if lights:
        parts.append("1 lumière" if lights == 1 else f"{lights} lumières")
    if pcs:
        parts.append("1 pièce" if pcs == 1 else f"lot de {pcs}")
    if cms:
        seen: list[int] = []
        for c in cms:
            if c not in seen:
                seen.append(c)
        parts.append("Ø " + " / ".join(str(c) for c in seen) + " cm")
    if mms:
        w, h = mms[0]
        parts.append(f"Ø {int(w)} × H {int(h)} mm")
    if watts:
        parts.append(f"{watts} W")
    return " · ".join(parts)


def translate_atom(raw: str) -> str:
    s = (raw or "").strip()
    if not s:
        return s
    key = _fold(s).strip()
    if key in WAREHOUSES:
        return WAREHOUSES[key]

    sized = format_size_blob(s)
    # If the string is essentially a size, prefer the formatted size
    if sized and re.fullmatch(r"[\d\sRringsDIAClightscmwWpx./\-]+", s, re.I):
        return sized

    out = s
    for pat, repl in PHRASES:
        out = re.sub(pat, repl, out, flags=re.I)

    out = re.sub(r"\bDIA\b", "Ø", out, flags=re.I)
    out = re.sub(r"\b(\d+)\s*cm\b", lambda m: f"Ø {int(m.group(1))} cm", out, flags=re.I)
    out = re.sub(r"\bD(\d+)\b", lambda m: f"Ø {int(m.group(1))} cm", out)
    out = re.sub(r"\((\s*)\)", "", out)
    out = re.sub(r"\s+", " ", out).strip(" -·/,")
    out = re.sub(r"(Ø )+", "Ø ", out)
    # dedupe Ø Ø
    if sized and not any(tok in _fold(s) for tok in ("black", "white", "gold", "warm", "cool", "cold")):
        # mixed size+other already handled by phrases + size leftover
        if re.search(r"\d+\s*cm|\d+\s*ring", s, re.I) and not re.search(r"[A-Za-z]{4,}", re.sub(r"(ring|rings|cm|dia|led|light|lights|pcs|watt|no|remote)", "", s, flags=re.I)):
            return sized
    if sized and re.search(r"\d+\s*(cm|ring|r\b|lights)", s, re.I):
        # combine color/temp leftovers with size
        leftover = out
        leftover = re.sub(r"Ø\s*\d+(?:\s*/\s*\d+)*\s*cm", "", leftover)
        leftover = re.sub(r"\d+\s*anneaux?", "", leftover, flags=re.I)
        leftover = re.sub(r"\d+\s*lumières?", "", leftover, flags=re.I)
        leftover = re.sub(r"\s+", " ", leftover).strip(" -·/,")
        if leftover and leftover not in sized:
            return f"{sized} — {leftover}" if not leftover[0].isupper() or True else f"{leftover} · {sized}"
        return sized
    return out or s


def translate_value(raw: str) -> str:
    s = (raw or "").strip()
    if "|" in s:
        parts = [translate_atom(p.strip()) for p in s.split("|") if p.strip()]
        # drop Chine if other warehouse/temp remains? keep all
        return " · ".join(dict.fromkeys(parts))
    return translate_atom(s)


def distinguisher(original: str, translated: str) -> str:
    o = _fold(original)
    extras = []
    if "no remote" in o or "no rc" in o:
        extras.append("fixe")
    if "remote" in o or "dimm" in o:
        extras.append("télécommande")
    if "3000k" in o:
        extras.append("3000 K")
    if "4000k" in o:
        extras.append("4000 K")
    if "6000k" in o:
        extras.append("6000 K")
    extra = " ".join(extras)
    if extra and extra.lower() not in _fold(translated):
        return extra
    # last resort: compact original
    compact = re.sub(r"[^A-Za-z0-9]+", " ", original).strip()
    return compact[:24] if compact else original[:24]


def uniquify(items: list[tuple[str, str, str]]) -> list[tuple[str, str]]:
    """(id, translated, original) → (id, unique_name)."""
    used: set[str] = set()
    out: list[tuple[str, str]] = []
    for oid, tr, orig in items:
        name = tr.strip() or orig
        if name in used:
            extra = distinguisher(orig, name)
            candidate = f"{name} ({extra})" if extra else f"{name} · {orig}"
            n = 2
            while candidate in used:
                candidate = f"{name} ({n})"
                n += 1
            name = candidate
        used.add(name)
        out.append((oid, name[:255]))
    return out


def score_size(values: list[str]) -> float:
    n = 0
    for v in values:
        if re.search(r"\d+\s*cm|\d+\s*mm|\bring|\bdia\b|\bØ|\banneau", v, re.I):
            n += 1
        elif re.search(r"\d+\s*lights?", v, re.I):
            n += 0.6
    return n / max(len(values), 1)


def score_temp(values: list[str]) -> float:
    n = 0
    for v in values:
        if re.search(
            r"warm|cool|cold|white light|dimm|remote|3000k|4000k|6000k|tricolor|changeable|3-color|natural light|nature light|emitting|teinte|blanc chaud|blanc froid",
            v,
            re.I,
        ):
            n += 1
    return n / max(len(values), 1)


def score_color(values: list[str]) -> float:
    n = 0
    for v in values:
        if re.search(
            r"black|white|gold|silver|amber|smoke|clear|coffee|chrome|copper|bronze|rose|red|blue|green|brown|grey|gray|champagne|orange|yellow|violet|purple|"
            r"noir|blanc|doré|dore|argenté|argente|ambre|transparent|gris|fumé|fume|cuivre|chrome|bronze|champagne|café|cafe",
            v,
            re.I,
        ):
            n += 1
    return n / max(len(values), 1)


def score_wh(values: list[str]) -> float:
    n = 0
    for v in values:
        if re.search(r"china|germany|united kingdom|united states|spain|france|poland|italy|warehouse|mainland", v, re.I):
            n += 1
    return n / max(len(values), 1)


def classify_option(name: str, values: list[str]) -> str:
    if name in {
        "Taille", "Couleur", "Température", "Ampoule", "Lumières", "Entrepôt",
        "Température et entrepôt", "Taille et entrepôt", "Format", "Finition", "Éclairage",
    }:
        return name
    nl = name.lower()
    if "|" in name:
        has_ship = "ship" in nl or score_wh(values) > 0.4
        has_temp = "emitting" in nl or score_temp(values) > 0.4
        has_size = "size" in nl or "wattage" in nl or score_size(values) > 0.4
        if has_temp and has_ship:
            return "Température et entrepôt"
        if has_size and has_ship:
            return "Taille et entrepôt"
        if has_ship:
            return "Entrepôt"
    sizes, temps, colors, wh = score_size(values), score_temp(values), score_color(values), score_wh(values)
    if "ship" in nl:
        return "Entrepôt"
    if "emitting" in nl:
        return "Température"
    if "blade" in nl:
        return "Couleur"
    if "wattage" in nl:
        if all(re.search(r"bulb|not included|no included|ampoule", v, re.I) for v in values):
            return "Ampoule"
        if temps >= 0.5 and temps >= sizes and temps >= colors:
            return "Température"
        if colors > sizes and colors >= 0.5:
            return "Couleur"
        if sizes >= colors:
            return "Taille"
    if nl == "size" and temps >= 0.5 and temps >= colors and temps >= sizes:
        return "Température"
    if nl == "size" and colors > sizes:
        return "Couleur"
    if nl == "color" and sizes > colors:
        return "Taille"
    if "lampshade" in nl and sizes > colors:
        return "Taille"
    if "number of light" in nl and colors > 0.5 and sizes < 0.3:
        return "Couleur"
    if "number of light" in nl:
        return "Lumières"
    scores = {"Taille": sizes, "Température": temps, "Couleur": colors, "Entrepôt": wh}
    best = max(scores, key=scores.get)
    if scores[best] < 0.35:
        if "body" in nl and sizes >= 0.3:
            return "Taille"
        if "color" in nl or colors >= 0.3:
            return "Couleur" if colors >= sizes else "Taille"
        if "size" in nl:
            return "Taille"
        if colors >= temps and colors >= sizes:
            return "Couleur"
        return "Option"
    return best


def unique_option_names(pairs: list[tuple[str, str]]) -> list[tuple[str, str]]:
    used: set[str] = set()
    alts = {"Taille": "Format", "Couleur": "Finition", "Température": "Éclairage", "Entrepôt": "Expédition"}
    out = []
    for oid, name in pairs:
        final = name
        if final in used:
            final = alts.get(name, f"{name} 2")
            n = 2
            while final in used:
                final = f"{name} {n}"
                n += 1
        used.add(final)
        out.append((oid, final))
    return out


ORDER = ["Taille", "Couleur", "Température", "Ampoule", "Lumières", "Entrepôt", "Température et entrepôt", "Taille et entrepôt", "Format", "Finition", "Éclairage", "Option"]


def order_index(name: str) -> int:
    for i, n in enumerate(ORDER):
        if name.startswith(n):
            return i
    return 50


def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {"compare_at": [], "options": []}


def save_state(state: dict) -> None:
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")


def fetch_all_variants(product_id: str) -> list[dict]:
    cursor = None
    nodes: list[dict] = []
    while True:
        data = gql(
            """
            query ($id: ID!, $c: String) {
              product(id: $id) {
                variants(first: 100, after: $c) {
                  pageInfo { hasNextPage endCursor }
                  nodes { id compareAtPrice }
                }
              }
            }
            """,
            {"id": product_id, "c": cursor},
        )
        conn = data["product"]["variants"]
        nodes.extend(conn["nodes"])
        if not conn["pageInfo"]["hasNextPage"]:
            return nodes
        cursor = conn["pageInfo"]["endCursor"]


def iter_active_products():
    cursor = None
    while True:
        data = gql(
            """
            query ($c: String) {
              products(first: 25, after: $c) {
                pageInfo { hasNextPage endCursor }
                nodes {
                  id handle status
                  options { id name position optionValues { id name } }
                  variants(first: 100) {
                    pageInfo { hasNextPage }
                    nodes { id compareAtPrice }
                  }
                }
              }
            }
            """,
            {"c": cursor},
        )
        for node in data["products"]["nodes"]:
            if node["status"] != "ACTIVE":
                continue
            if node["variants"]["pageInfo"]["hasNextPage"]:
                node["variants"] = {"nodes": fetch_all_variants(node["id"])}
            yield node
        if not data["products"]["pageInfo"]["hasNextPage"]:
            return
        cursor = data["products"]["pageInfo"]["endCursor"]


def clear_compare_at(product: dict) -> int:
    updates = [{"id": v["id"], "compareAtPrice": None} for v in product["variants"]["nodes"] if v.get("compareAtPrice")]
    if not updates:
        return 0
    for i in range(0, len(updates), 50):
        chunk = updates[i : i + 50]
        data = gql(
            """
            mutation V($productId: ID!, $variants: [ProductVariantsBulkInput!]!) {
              productVariantsBulkUpdate(productId: $productId, variants: $variants) {
                userErrors { field message }
              }
            }
            """,
            {"productId": product["id"], "variants": chunk},
        )
        errs = data["productVariantsBulkUpdate"]["userErrors"]
        if errs:
            raise RuntimeError((product["handle"], errs))
        time.sleep(0.15)
    return len(updates)


def delete_option(product_id: str, option_id: str) -> None:
    data = gql(
        """
        mutation D($productId: ID!, $options: [ID!]!, $strategy: ProductOptionDeleteStrategy) {
          productOptionsDelete(productId: $productId, options: $options, strategy: $strategy) {
            userErrors { field message }
          }
        }
        """,
        {"productId": product_id, "options": [option_id], "strategy": "POSITION"},
    )
    errs = data["productOptionsDelete"]["userErrors"]
    if errs:
        print("  warn delete option", errs)


def update_option(product_id: str, option_id: str, new_name: str, values: list[tuple[str, str]], position: int | None = None) -> None:
    option: dict = {"id": option_id, "name": new_name}
    if position is not None:
        option["position"] = position
    data = gql(
        """
            mutation U($productId: ID!, $option: OptionUpdateInput!, $optionValuesToUpdate: [OptionValueUpdateInput!]) {
              productOptionUpdate(
                productId: $productId
                option: $option
                optionValuesToUpdate: $optionValuesToUpdate
              ) {
                userErrors { field message }
              }
            }
        """,
        {
            "productId": product_id,
            "option": option,
            "optionValuesToUpdate": [{"id": vid, "name": vname} for vid, vname in values],
        },
    )
    errs = data["productOptionUpdate"]["userErrors"]
    if errs:
        raise RuntimeError(errs)


def reorder_options(product_id: str, ordered_ids: list[str]) -> None:
    data = gql(
        """
        mutation R($productId: ID!, $options: [OptionReorderInput!]!) {
          productOptionsReorder(productId: $productId, options: $options) {
            userErrors { field message }
          }
        }
        """,
        {
            "productId": product_id,
            "options": [{"id": oid} for oid in ordered_ids],
        },
    )
    errs = data["productOptionsReorder"]["userErrors"]
    if errs:
        print("  warn reorder", errs)


def plan_product(product: dict) -> dict:
    options = []
    drop_ids = []
    for opt in product["options"]:
        originals = [v["name"] for v in opt["optionValues"]]
        kind = classify_option(opt["name"], originals)
        translated = [(v["id"], translate_value(v["name"]), v["name"]) for v in opt["optionValues"]]
        unique_vals = uniquify(translated)
        if opt["name"] == "Title" and originals == ["Default Title"]:
            continue
        china_only = kind == "Entrepôt" and len(originals) == 1 and _fold(originals[0]) in {"china mainland", "china", "cn"}
        combined_china_only = kind == "Entrepôt" and all(
            translate_value(v).lower() == "chine" or _fold(v) in {"china mainland", "china", "cn"}
            for v in originals
        )
        remaining_after = len(product["options"]) - len(drop_ids) - 1
        if (china_only or (combined_china_only and "|" not in opt["name"])) and remaining_after >= 1:
            drop_ids.append(opt["id"])
            continue
        options.append(
            {
                "id": opt["id"],
                "old_name": opt["name"],
                "new_name": kind,
                "values": [{"id": a, "old": c, "new": b} for a, b, c in [(x[0], x[1], translated[i][2]) for i, x in enumerate(unique_vals)]],
            }
        )
    named = unique_option_names([(o["id"], o["new_name"]) for o in options])
    name_by_id = dict(named)
    for o in options:
        o["new_name"] = name_by_id[o["id"]]
    options.sort(key=lambda o: order_index(o["new_name"]))
    return {"handle": product["handle"], "id": product["id"], "options": options, "drop": drop_ids}


def apply_plan(plan: dict) -> None:
    pid = plan["id"]
    for oid in plan["drop"]:
        delete_option(pid, oid)
        time.sleep(0.2)
    for i, opt in enumerate(plan["options"], 1):
        update_option(
            pid,
            opt["id"],
            opt["new_name"],
            [(v["id"], v["new"]) for v in opt["values"]],
            position=i,
        )
        time.sleep(0.2)
    if len(plan["options"]) > 1:
        reorder_options(pid, [o["id"] for o in plan["options"]])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-compare", action="store_true")
    parser.add_argument("--skip-options", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()
    state = load_state()
    done_cmp = set(state.get("compare_at") or [])
    done_opt = set(state.get("options") or [])
    reports = []
    n = 0
    for product in iter_active_products():
        n += 1
        if args.limit and n > args.limit:
            break
        handle = product["handle"]
        plan = plan_product(product)
        reports.append(
            {
                "handle": handle,
                "drop": len(plan["drop"]),
                "options": [
                    {"old": o["old_name"], "new": o["new_name"], "sample": [v["new"] for v in o["values"][:6]]}
                    for o in plan["options"]
                ],
            }
        )
        if args.dry_run:
            continue
        try:
            if not args.skip_compare and handle not in done_cmp:
                cleared = clear_compare_at(product)
                done_cmp.add(handle)
                state["compare_at"] = sorted(done_cmp)
                save_state(state)
                cmp_msg = f"compareAt -{cleared}"
            else:
                cmp_msg = "compareAt skip"
            if not args.skip_options and handle not in done_opt:
                apply_plan(plan)
                done_opt.add(handle)
                state["options"] = sorted(done_opt)
                save_state(state)
                opt_msg = "options OK"
            else:
                opt_msg = "options skip"
            print(f"  {handle} {cmp_msg} {opt_msg}")
        except Exception as err:
            print(f"FAIL {handle} {str(err)[:240]}")
            state.setdefault("failed", []).append({"handle": handle, "error": str(err)})
            save_state(state)
            continue
        if n % 10 == 0:
            print(f"  … {n}")
    if args.dry_run:
        kinds = Counter()
        for r in reports:
            for o in r["options"]:
                kinds[f"{o['old']} → {o['new']}"] += 1
        print("option renames:")
        for k, c in kinds.most_common():
            print(f"  {c:3} {k}")
        print("drops", sum(r["drop"] for r in reports), "products", len(reports))
        REPORT.write_text(json.dumps(reports, ensure_ascii=False, indent=2) + "\n")
        print("wrote", REPORT)
        return
    print("OK", n, "products")


if __name__ == "__main__":
    main()
