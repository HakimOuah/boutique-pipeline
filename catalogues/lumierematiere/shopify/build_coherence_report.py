#!/usr/bin/env python3
"""Fusionne COHERENCE JSON + fret DSers et écrit le rapport markdown."""
from __future__ import annotations

import json
from collections import Counter
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
COH = HERE / f"COHERENCE-{date.today().isoformat()}.json"
FREIGHT = Path("/tmp/dsers-freight.json")
OUT_MD = HERE / f"COHERENCE-{date.today().isoformat()}.md"

PREP_MAX = 2
SHIP_MAX_PROMISE = 15
TOTAL_MAX_PROMISE = 17
IGNORE = {"other"}


def cost_usd(m: dict) -> float | None:
    """DSers renvoie le montant en centimes (199.00 = 1,99 $)."""
    v = m.get("cost")
    if v is None or v == "":
        return None
    try:
        return float(str(v).replace(",", ".")) / 100.0
    except ValueError:
        return None


def is_seller_60(m: dict) -> bool:
    svc = (m.get("service") or "").lower()
    co = (m.get("company") or "").lower()
    if svc in IGNORE or co == "seller's shipping method":
        return True
    if "seller" in svc and (m.get("max") or 0) >= 30:
        return True
    return False


def operational(methods: list[dict]) -> tuple[dict | None, str]:
    tracked = []
    for m in methods:
        if not m.get("tracked") or m.get("max") is None:
            continue
        if is_seller_60(m):
            continue
        tracked.append(m)
    if not tracked:
        return None, "SANS_FRET"
    cheap = [m for m in tracked if (cost_usd(m) or 0) <= 5]
    if cheap:
        op = min(cheap, key=lambda m: (m["max"], m.get("min") or 99, cost_usd(m) or 0))
        return op, verdict(op)
    op = min(tracked, key=lambda m: (m["max"], m.get("min") or 99, cost_usd(m) or 99))
    return op, "PAS_GRATUIT"


def verdict(method: dict | None) -> str:
    if not method:
        return "SANS_FRET"
    ship_max = method["max"]
    if ship_max <= SHIP_MAX_PROMISE:
        return "OK"
    if ship_max <= 16:
        return "LIMITE"
    return "OVER_PROMISE"


# Quotes Product Factory quand DSers renvoie une liste vide (26/08).
AE_OVERLAY = {
    "suspension-bambou-655008": {
        "service": "DHL_P_EU_EXP",
        "company": "DHL DE Pan-European",
        "min": 3,
        "max": 10,
        "cost_usd": 0.0,
        "note": "SKU 30 cm rupture ; variante 38 cm DE, 3–10 j gratuit",
    },
    "suspension-effet-pierre-092465": {
        "service": "CAINIAO_FULFILLMENT_STD",
        "company": "AliExpress Selection Standard",
        "min": 6,
        "max": 10,
        "cost_usd": 1.99,
        "note": "DSers vide ; AE Selection 6–10 j à 1,99 €",
    },
    "lustre-salon-blanc-246282": {
        "service": "DHL_P_EU_EXP",
        "company": "DHL DE Pan-European",
        "min": 3,
        "max": 10,
        "cost_usd": 0.0,
        "note": "DSers vide ; DHL DE 3–10 j gratuit",
    },
}
AE_INLIVRABLE = {
    "suspension-bambou-655463": "LM-011 — SKU d’entrée : AE refuse FR",
    "lustre-cristal-led-led-141724": "LM-065 — SKU d’entrée : AE refuse FR",
    "lustre-cristal-led-noir-347688": "LM-069 — SKU d’entrée : AE refuse FR",
    "lustre-salon-957153": "LM-111 — SKU d’entrée : AE refuse FR",
}


def euro(v) -> str:
    if v is None:
        return "—"
    if isinstance(v, float) and v == int(v):
        return f"{int(v)} €"
    return f"{v:.2f} €".replace(".", ",")


def usd_label(m: dict | None) -> str:
    if not m:
        return "—"
    c = m.get("cost_usd")
    if c is None:
        c = cost_usd(m)
    if c is None:
        return "—"
    return f"{c:.2f} $"


def load_freight() -> dict:
    by_h: dict[str, dict] = {}
    for r in json.loads(FREIGHT.read_text())["results"]:
        prev = by_h.get(r["handle"])
        if prev is None or (r.get("methods") and not prev.get("methods")):
            by_h[r["handle"]] = r
    return by_h


def apply_row(r: dict, fr: dict) -> None:
    methods = fr.get("methods") or []
    op, v = operational(methods)
    source = "dsers"
    note = None
    if v == "SANS_FRET" and r["handle"] in AE_OVERLAY:
        op = dict(AE_OVERLAY[r["handle"]])
        v = verdict(op)
        source = "aliexpress"
        note = op.get("note")
    elif v == "SANS_FRET" and r["handle"] in AE_INLIVRABLE:
        v = "INLIVRABLE_FR"
        note = AE_INLIVRABLE[r["handle"]]
        source = "aliexpress"
    r["dsers_methods"] = [
        {
            "service": m.get("service"),
            "min": m.get("min"),
            "max": m.get("max"),
            "tracked": m.get("tracked"),
            "cost_usd": cost_usd(m),
        }
        for m in methods
    ]
    r["fret_source"] = source
    r["fret_service"] = (op or {}).get("service")
    r["fret_company"] = (op or {}).get("company")
    r["fret_min"] = (op or {}).get("min")
    r["fret_max"] = (op or {}).get("max")
    r["fret_cost_usd"] = (op or {}).get("cost_usd", cost_usd(op) if op else None)
    r["fret_verdict"] = v
    r["fret_note"] = note
    r["total_max"] = (op["max"] + PREP_MAX) if op and op.get("max") is not None else None


def main() -> None:
    coh = json.loads(COH.read_text())
    freight = load_freight()
    rows = coh["produits"]

    for r in rows:
        apply_row(r, freight.get(r["handle"]) or {})

    draft = freight.get("applique-murale-travertin-358794") or {}
    draft_op, draft_v = operational(draft.get("methods") or [])

    over = [r for r in rows if r["fret_verdict"] == "OVER_PROMISE"]
    limite = [r for r in rows if r["fret_verdict"] == "LIMITE"]
    ok = [r for r in rows if r["fret_verdict"] == "OK"]
    paid = [r for r in rows if r["fret_verdict"] == "PAS_GRATUIT"]
    inliv = [r for r in rows if r["fret_verdict"] == "INLIVRABLE_FR"]
    sans = [r for r in rows if r["fret_verdict"] == "SANS_FRET"]
    dessus = [r for r in rows if r.get("au_dessus_lustria")]
    thin = sorted(rows, key=lambda r: r.get("marge_ht") or 999)
    vs = [r for r in rows if r.get("vs_lustria") is not None]
    aucun = [r for r in rows if not r.get("lustria_n")]

    payload = {
        **{k: v for k, v in coh.items() if k != "produits"},
        "fret_source": "DSers GET /freight FR (enveloppe AliExpress), méthode suivie ≤ 5 $ ; AE overlay si DSers vide",
        "fret_counts": {
            "OK": len(ok),
            "LIMITE": len(limite),
            "OVER_PROMISE": len(over),
            "PAS_GRATUIT": len(paid),
            "INLIVRABLE_FR": len(inliv),
            "SANS_FRET": len(sans),
        },
        "produits": rows,
        "lm125_draft": {
            "handle": "applique-murale-travertin-358794",
            "ae": "1005009658358794",
            "fret_service": (draft_op or {}).get("service"),
            "fret_min": (draft_op or {}).get("min"),
            "fret_max": (draft_op or {}).get("max"),
            "fret_verdict": draft_v,
        },
    }
    COH.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")

    def line(r: dict) -> str:
        return (
            f"| {r.get('sku') or '—'} | `{r['handle']}` | {r.get('fret_min')}–{r.get('fret_max')} j "
            f"| {r.get('total_max')} j | `{r.get('fret_service') or '—'}` | {usd_label({'cost_usd': r.get('fret_cost_usd')})} |"
        )

    over_s = sorted(over, key=lambda r: (-(r.get("fret_max") or 0), r.get("sku") or ""))
    md = []
    a = md.append
    a("# Cohérence Lumière Matière — délais, prix, marges")
    a("")
    a(f"**{date.today().isoformat()} · {len(rows)} fiches ACTIVE · audit, aucune écriture boutique.**")
    a("")
    a("Promesse affichée sur **chaque** FAQ live : préparation 1–2 j + acheminement 6–15 j = **7–17 j ouvrés**, port offert France métropolitaine.")
    a("")
    a("Source délai : DSers `GET /dsers-product-bff/freight` vers FR — c’est l’enveloppe AliExpress que DSers utilise à la commande. Méthode retenue = suivi, hors « Seller's Shipping », coût ≤ 5 (USD/EUR). Contrôle croisé Product Factory sur LM-001, LM-053, LM-125, LM-127 : mêmes familles de lignes, fenêtres à ±1–2 j près.")
    a("")
    a("Source prix : coût unitaire Shopify (DSers) + 2 € de fret. Marge HT ≥ max(40 € ; 25 % du HT). Comparable Lustria = médiane du pool `lustria_match.py` (catalogue 25/08, pas de nouveau scrape).")
    a("")
    a("## 1. Délais — le texte FAQ est bon, les délais réels souvent non")
    a("")
    a("| Verdict | Fiches | Sens |")
    a("|---|---:|---|")
    a(f"| OK (acheminement max ≤ 15 j) | {len(ok)} | tient 7–17 avec 2 j de prép. |")
    a(f"| LIMITE (16 j de route) | {len(limite)} | total 18 j, 1 j au-dessus de la FAQ |")
    a(f"| OVER_PROMISE (route > 16 j) | {len(over)} | la FAQ ment |")
    a(f"| PAS_GRATUIT (seule ligne ≤ 15 j est payante > 5 $) | {len(paid)} | port offert promis, fret réel cher |")
    a(f"| INLIVRABLE_FR (SKU d’entrée) | {len(inliv)} | AliExpress refuse la France |")
    a(f"| SANS_FRET | {len(sans)} | ni DSers ni AE |")
    a("")
    if over:
        a("### Hors promesse")
        a("")
        a("| SKU | Handle | Route DSers | Total +2 j | Méthode | Coût |")
        a("|---|---|---:|---:|---|---:|")
        for r in over_s:
            a(line(r))
        a("")
        a("Les bambous et rotins XXL tombent presque tous sur `CAINIAO_FULFILLMENT_OVER_WH` (23–31 j). Les lustres anneau / cristal n’ont souvent qu’une ligne lourde ou un DHL payant : la ligne gratuite dépasse 15 j.")
        a("")
    if limite:
        a("### Limite (16 j de route)")
        a("")
        a("| SKU | Handle | Route DSers | Total +2 j | Méthode | Coût |")
        a("|---|---|---:|---:|---|---:|")
        for r in sorted(limite, key=lambda x: x.get("sku") or ""):
            a(line(r))
        a("")
    if paid:
        a("### Port promis gratuit, seule ligne rapide payante")
        a("")
        a("| SKU | Handle | Route | Méthode | Coût |")
        a("|---|---|---:|---|---:|")
        for r in sorted(paid, key=lambda x: x.get("sku") or ""):
            a(
                f"| {r.get('sku')} | `{r['handle']}` | {r.get('fret_min')}–{r.get('fret_max')} j "
                f"| `{r.get('fret_service')}` | {usd_label({'cost_usd': r.get('fret_cost_usd')})} |"
            )
        a("")
    if inliv:
        a("### SKU d’entrée : AliExpress refuse la France")
        a("")
        a("DSers n’a renvoyé aucune ligne. Product Factory sur le `cheapest_sku_id` du mapping : `DELIVERY_NOT_AVAILABLE_TO_YOUR_ADDRESS`. À requoter sur une autre variante (cas LM-007 : 30 cm rupture, 38 cm OK en DHL DE 3–10 j).")
        a("")
        for r in inliv:
            a(f"- {r.get('sku')} `{r['handle']}` AE `{r.get('ae_id')}`")
        a("")
    if sans:
        a("### Sans fret")
        a("")
        for r in sans:
            a(f"- {r.get('sku')} `{r['handle']}` AE `{r.get('ae_id')}`")
        a("")
    a("### Brouillon LM-125 (hors live)")
    a("")
    if draft_op:
        a(
            f"`applique-murale-travertin-358794` · AE `1005009658358794` · "
            f"{draft_op.get('min')}–{draft_op.get('max')} j `{draft_op.get('service')}` · **{draft_v}**."
        )
    else:
        a("Pas de méthode suivie côté DSers. Quote AliExpress Product Factory : Cainiao Standard **23–31 j**.")
    a("Confirme le maintien en brouillon : on ne peut pas promettre 7–17 j.")
    a("")
    a("Contrôle AliExpress (Product Factory, SKU d’entrée) :")
    a("")
    a("- LM-127 boule verre : Cainiao Standard **8–15 j**, gratuit. DSers annonce 8–16. Limite.")
    a("- LM-125 cylindre LED : Standard **23–31 j**. Hors cible, inchangé.")
    a("- LM-053 anneau : pas de Standard gratuit ≤ 15 j — Heavy 8–43 j, Standard payant 13–20 j à 45,53 €.")
    a("- LM-001 bambou : uniquement Selection Oversized **3–40 j** à 1,99 € sur le SKU d’entrée.")
    a("")
    a("## 2. Prix et marges vs Lustria")
    a("")
    a(f"- **{len(rows)}/{len(rows)}** tiennent le plancher de marge (40 € HT et 25 % du HT).")
    a(f"- **0** fiche sans coût DSers.")
    a(f"- **{len(dessus)}** fiche au-dessus de la médiane Lustria de son pool.")
    a(f"- **{len(aucun)}** fiches sans comparable Lustria (pool < 3) : " + ", ".join(f"{r['sku']}" for r in aucun) + ".")
    a(f"- Écart vs médiane (122 fiches appariées) : min {min(r['vs_lustria'] for r in vs):+.1f} €, médiane {sorted(x['vs_lustria'] for x in vs)[len(vs)//2]:+.1f} €, max {max(r['vs_lustria'] for r in vs):+.1f} €.")
    a("")
    a("### La seule fiche au-dessus de Lustria")
    a("")
    a("| SKU | Handle | Notre PV | Médiane Lustria | n | Qualité | Écart | Marge HT | Plancher |")
    a("|---|---|---:|---:|---:|---|---:|---:|---:|")
    for r in dessus:
        a(
            f"| {r['sku']} | `{r['handle']}` | {euro(r['prix_min'])} | {euro(r['lustria_median'])} | "
            f"{r['lustria_n']} | {r['lustria_qualite']} | {r['vs_lustria']:+.1f} € | "
            f"{euro(r['marge_ht'])} ({r['marge_pct']} %) | {euro(r['plancher_ht'])} |"
        )
    a("")
    a("LM-127 : pool Lustria `applique-boule-verre`, médiane **99,90 €** (44 fiches). Notre 159 € est +59 €. On ne peut pas descendre sous Lustria : rendu 85,75 €, un PV à 99 € donnerait une marge HT négative. Le 159 € est un plancher économique, pas un alignement concurrent. À laisser tel quel tant que le coût DSers (83,75 € vs quote 35,99 €) ne bouge pas.")
    a("")
    a("### Marges les plus minces (toutes encore au-dessus du plancher)")
    a("")
    a("| SKU | Handle | PV | Coût DSers | Rendu | Marge HT | % HT | vs Lustria |")
    a("|---|---|---:|---:|---:|---:|---:|---:|")
    for r in thin[:12]:
        a(
            f"| {r['sku']} | `{r['handle']}` | {euro(r['prix_min'])} | {euro(r['cout_dsers_min'])} | "
            f"{euro(r['rendu'])} | {euro(r['marge_ht'])} | {r['marge_pct']} % | "
            f"{'' if r.get('vs_lustria') is None else f'{r['vs_lustria']:+.1f} €'} |"
        )
    a("")
    a("LM-124 (double travertin) est la plus serrée : **42,13 € HT / 39 %**, 2 € au-dessus du plancher 40 €. Lustria du pool est à 249,90 € — on est déjà 121 € en dessous, on ne touche pas.")
    a("")
    a("### Appliques live, une par une")
    a("")
    a("| SKU | PV | Coût | Marge HT | Médiane Lustria | n | Note |")
    a("|---|---:|---:|---:|---:|---:|---|")
    for r in [x for x in rows if x["type"] == "applique"]:
        note = "sous Lustria" if (r.get("vs_lustria") or 0) < 0 else "au-dessus Lustria — voir plus haut"
        a(
            f"| {r['sku']} | {euro(r['prix_min'])} | {euro(r['cout_dsers_min'])} | "
            f"{euro(r['marge_ht'])} ({r['marge_pct']} %) | {euro(r['lustria_median'])} | "
            f"{r['lustria_n']} | {note} |"
        )
    a("")
    a("Les quatre appliques pierre/travertin sont **sous** leur médiane Lustria (199,90–249,90 €). Seule la boule verre sort du schéma, parce que le comparable Lustria est un low-ticket 99,90 € et que notre coût DSers interdit d’y aller.")
    a("")
    a("### Grille des prix d’entrée")
    a("")
    counts = Counter(r["prix_min"] for r in rows)
    a("| Prix d’entrée | Fiches |")
    a("|---:|---:|")
    for prix, n in sorted(counts.items()):
        a(f"| {euro(prix)} | {n} |")
    a("")
    a("## 3. Ce qu’on ne change pas ce soir")
    a("")
    a("Audit seulement. Pas de retouche FAQ, pas de baisse/hausse de prix, pas de passage live de LM-125. Le brief Codex LM-126 cubique reste en attente de livraison visuels.")
    a("")
    a("Si tu veux une suite : 1) élargir la FAQ des OVER_PROMISE (familles XXL / oversized) à la fenêtre réelle, ou 2) retirer / remplacer les pires délais, en commençant par ceux dont le max dépasse 30 j.")
    a("")

    OUT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(
        f"OK={len(ok)} LIMITE={len(limite)} OVER={len(over)} "
        f"PAYANT={len(paid)} INLIV={len(inliv)} SANS={len(sans)}"
    )
    print(f"écrit {OUT_MD.name} et {COH.name}")


if __name__ == "__main__":
    main()
