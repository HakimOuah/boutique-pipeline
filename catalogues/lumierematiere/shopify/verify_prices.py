"""Contrôle post-application : les prix en ligne correspondent-ils au plan ?

Vérifie aussi les invariants promis dans le rapport — aucun `compareAtPrice`,
aucun SKU perdu, aucune variante ajoutée ou supprimée, paliers strictement
croissants — en comparant la boutique à la sauvegarde d'avant écriture.
"""
from __future__ import annotations

import json
import statistics as st
from pathlib import Path

import align_prices as A
import lustria_match as L

HERE = Path(__file__).resolve().parent
BACKUP_DIR = HERE / "backups" / "2026-08-26-prix"


def main() -> None:
    plan = {l["sku"]: l for l in
            json.loads((HERE / "prix-alignement-plan-2026-08-26.json").read_text(
                encoding="utf-8"))["lignes"]}
    avant_fichier = sorted(BACKUP_DIR.glob("prix-avant-*.json"))[0]
    avant = {p["id"]: p for p in json.loads(avant_fichier.read_text(encoding="utf-8"))}
    live = {p["id"]: p for p in A.dump_live()}
    par_id = {l["product_id"]: l for l in plan.values()}

    echecs: list[str] = []

    for pid, l in par_id.items():
        p = live.get(pid)
        if p is None:
            echecs.append(f"{l['sku']} : absent en ligne")
            continue
        vs = p["variants"]["nodes"]
        ref = avant[pid]["variants"]

        if {v["id"] for v in vs} != {v["id"] for v in ref}:
            echecs.append(f"{l['sku']} : identifiants de variantes modifies")
        if {(v["id"], v["sku"]) for v in vs} != {(v["id"], v["sku"]) for v in ref}:
            echecs.append(f"{l['sku']} : un SKU a bouge")
        if any(v["compareAtPrice"] for v in vs):
            echecs.append(f"{l['sku']} : compareAtPrice non nul")

        table = dict(zip([float(x) for x in l["paliers"]], l["paliers_cibles"]))
        attendu = {v["id"]: table[v["price"]] for v in l["variants"]}
        for v in vs:
            if float(v["price"]) != float(attendu[v["id"]]):
                echecs.append(f"{l['sku']} {v['id'].rsplit('/', 1)[-1]} : "
                              f"{v['price']} au lieu de {attendu[v['id']]}")
        paliers = sorted({float(v["price"]) for v in vs})
        if len(paliers) != len(set(l["paliers_cibles"])):
            echecs.append(f"{l['sku']} : {len(paliers)} paliers au lieu de "
                          f"{len(set(l['paliers_cibles']))}")
        if any(round(x) % 10 != 9 for x in paliers):
            echecs.append(f"{l['sku']} : palier hors grille en 9 -> {paliers}")

    mins = [min(float(v["price"]) for v in live[pid]["variants"]["nodes"]) for pid in par_id]
    lus = [x["prix"] for x in L.charge_lustria()]
    print(f"120 fiches controlees, {sum(len(live[p]['variants']['nodes']) for p in par_id)} "
          f"variantes")
    print(f"mediane en ligne : {st.median(mins):.0f} € — Lustria comparable "
          f"{st.median(lus):.2f} € ({100 * (1 - st.median(mins) / st.median(lus)):.0f} % sous)")
    print(f"prix pratiques   : {sorted(set(int(m) for m in mins))}")
    print(f"compareAtPrice non nuls : "
          f"{sum(1 for p in par_id for v in live[p]['variants']['nodes'] if v['compareAtPrice'])}")

    if echecs:
        print(f"\n{len(echecs)} ECHEC(S) :")
        for e in echecs:
            print(f"  - {e}")
        raise SystemExit(1)
    print("\nOK — prix, SKU, variantes, compareAtPrice et grille conformes au plan.")


if __name__ == "__main__":
    main()
