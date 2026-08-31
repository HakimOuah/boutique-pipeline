#!/usr/bin/env python3
"""Re-interroge DataForSEO sur les volumes qu'un agent affirme avoir mesurés.

Ne coûte quasiment rien (~0,09 USD les 180 mots-clés) et ferme la faille
constatée le 31/08/2026 : une piste adjacente annoncée à 4 400/mois en valait
480 — le volume d'un mot parent attribué à une longue traîne.

    echo '{"mangeoire anti-nuisible poules": 4400}' | python3 scripts/verifier-volumes.py
    python3 scripts/verifier-volumes.py --fichier affirmations.json
"""
from __future__ import annotations
import argparse, base64, json, os, sys, urllib.request

def volumes(mots: list[str]) -> dict[str, int | None]:
    login, pwd = os.environ.get("DATAFORSEO_LOGIN"), os.environ.get("DATAFORSEO_PASSWORD")
    if not login or not pwd:
        raise SystemExit("DATAFORSEO_LOGIN et DATAFORSEO_PASSWORD doivent être définis.")
    auth = "Basic " + base64.b64encode(f"{login}:{pwd}".encode()).decode()
    out: dict[str, int | None] = {}
    for i in range(0, len(mots), 180):            # limite de l'endpoint
        lot = mots[i:i + 180]
        req = urllib.request.Request(
            "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live",
            data=json.dumps([{"keywords": lot, "location_name": "France",
                              "language_name": "French"}]).encode(),
            headers={"Authorization": auth, "Content-Type": "application/json"})
        d = json.loads(urllib.request.urlopen(req, timeout=90).read())
        for r in (d["tasks"][0]["result"] or []):
            out[r["keyword"]] = r.get("search_volume")
    return out

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fichier", help="JSON {mot_cle: volume_annonce}. Défaut : stdin.")
    ap.add_argument("--tolerance", type=float, default=0.10,
                    help="écart relatif accepté (défaut 10 %%)")
    a = ap.parse_args()
    src = open(a.fichier, encoding="utf-8") if a.fichier else sys.stdin
    annonces = json.load(src)

    reels = volumes(list(annonces))
    faux = 0
    print(f"  {'mot-clé':<40}{'annoncé':>9}{'réel':>9}")
    for k, v in annonces.items():
        r = reels.get(k)
        if r is None:
            verdict, faux = "⚠ non rendu (n/a, pas 0)", faux + 1
        elif v in (None, 0) or abs(r - v) / max(v, 1) > a.tolerance:
            verdict, faux = f"❌ écart ×{r / max(v, 1):.1f}", faux + 1
        else:
            verdict = "✅"
        print(f"  {k:<40}{str(v):>9}{str(r):>9}  {verdict}")
    print(f"\n  {faux} affirmation(s) non confirmée(s) sur {len(annonces)}")
    return 1 if faux else 0

if __name__ == "__main__":
    sys.exit(main())
