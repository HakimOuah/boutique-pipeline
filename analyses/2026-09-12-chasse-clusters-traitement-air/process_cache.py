#!/usr/bin/env python3
"""Relit le cache Labs, isole les n/a, déduplique le reste. N'appelle pas l'API."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path("/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/.worktrees/c0-20260912-air-scout/scripts")))
import kw_dfs  # noqa: E402


def main() -> None:
    cache = Path(sys.argv[1])
    out_json = Path(sys.argv[2])
    out_md = Path(sys.argv[3])
    graine = sys.argv[4]
    d = json.loads(cache.read_text(encoding="utf-8"))
    lignes = [tuple(x[:4]) + (tuple(x[4]),) if len(x) > 4 else tuple(x) for x in d["lignes"]]
    na = [l[0] for l in lignes if l[1] is None]
    ok = [l for l in lignes if l[1] is not None]
    groupes = kw_dfs.dedupliquer(ok)
    payload = {
        "graine": graine,
        "total_annonce": d.get("total"),
        "provenance": d.get("provenance"),
        "lignes_brutes": len(lignes),
        "na": na,
        "groupes": groupes,
    }
    out_json.write_text(json.dumps(payload, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    txt = kw_dfs.rapport(graine, ok, groupes, d.get("total"), 0.0, 40)
    txt += "\n\n### Volumes n/a (pas 0)\n\n"
    for k in na:
        txt += f"- `{k}`\n"
    out_md.write_text(txt, encoding="utf-8")
    print("graine:", graine)
    print("lignes:", len(lignes), "ok:", len(ok), "na:", len(na), "idees:", len(groupes))
    print("na:", na)
    print("saved:", out_json, out_md)


if __name__ == "__main__":
    main()
