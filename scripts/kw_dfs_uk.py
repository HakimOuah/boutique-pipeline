#!/usr/bin/env python3
"""Mesure DataForSEO Royaume-Uni (location United Kingdom / language English).

Enveloppe autour de kw_dfs.py : memes endpoints, meme deduplication (MAX du groupe,
jamais la somme), mais parametres UK. Usage :
    python3 scripts/kw_dfs_uk.py "log store" "watch winder" --json out.json --top 40
Le temoin FR (tufting=12100) sert de controle API avant/apres.
"""
import sys, os, json, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kw_dfs as K

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("graines", nargs="+")
    ap.add_argument("--pages", type=int, default=1)
    ap.add_argument("--top", type=int, default=40)
    ap.add_argument("--json")
    ap.add_argument("--refresh", action="store_true")
    a = ap.parse_args()
    t0, _ = K.verifier_temoin()
    print(f"[temoin FR] tufting = {t0}", file=sys.stderr)
    out, cout = {}, 0.0
    for g in a.graines:
        lignes, total, c = K.suggestions(g, pages=a.pages, location="United Kingdom",
                                         language="English", cache=not a.refresh)
        cout += c
        nulls = [l[0] for l in lignes if l[1] is None]
        lignes = [l for l in lignes if l[1] is not None]
        groupes = K.dedupliquer(lignes)
        prov = dict(K.LAST_PROVENANCE)
        # groupes : liste de dicts ? on s'adapte
        rows = []
        for grp in groupes:
            if isinstance(grp, dict):
                rows.append(grp)
            else:
                rows.append({"repr": grp[0], "volume": grp[1], "formes": grp[2] if len(grp) > 2 else None})
        rows.sort(key=lambda r: -(r.get("volume") or 0))
        somme = sum((r.get("volume") or 0) for r in rows)
        out[g] = {"total_annonce": total, "n_lignes": len(lignes), "n_volume_null": len(nulls), "exemples_null": nulls[:5], "n_idees": len(rows),
                  "somme_idees_brute": somme, "cout": c, "provenance": prov, "groupes": rows}
        print(f"\n### {g} — {len(lignes)} lignes -> {len(rows)} idees ; somme brute (a nettoyer) {somme:,} ; {len(nulls)} lignes volume null ecartees ; total annonce {total} ; {c:.3f} USD")
        for r in rows[:a.top]:
            print(f"  {r.get('volume') or 0:>8,}  {r.get("expression")}"[:140])
    t1, _ = K.verifier_temoin(reference=t0)
    print(f"[temoin FR apres] tufting = {t1} ; cout total {cout:.3f} USD", file=sys.stderr)
    if a.json:
        json.dump(out, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
main()
