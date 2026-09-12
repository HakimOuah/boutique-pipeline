#!/usr/bin/env python3
"""Contrôle de têtes search_volume/live France/French."""
from __future__ import annotations

import json
import os
import urllib.request
from datetime import datetime
from pathlib import Path

API = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"
RAW = Path(__file__).resolve().parent / "raw"

MOTS = [
    "purificateur air",
    "purificateur d air",
    "purificateur d'air",
    "air purificateur",
    "purificateur",
    "épurateur d air",
    "épurateur d'air",
    "épurateur air",
    "purificateur d air hepa",
    "purificateur d air ionique",
    "ioniseur",
    "ioniseur d air",
    "plantes purificateur d air",
    "purificateur d air dyson",
    "purificateur d air philips",
    "purificateur d air xiaomi",
    "filtre hepa purificateur d air",
    "humidificateur purificateur d air",
    "ventilation",
    "ventilation plafond",
    "plafonnier ventilation",
    "ventilation silencieuse",
    "ventilation mécanique contrôlée",
    "vmc",
    "vmc double flux",
    "vmc double-flux",
    "vmc simple flux",
    "vmc hygroréglable",
    "vmc hygrométrique",
    "ventilation mécanique contrôlée double flux",
    "ventilation mécanique contrôlée simple flux",
    "ventilation mécanique contrôlée hygroréglable",
    "colonne ventilation",
    "ventilation poêle à bois",
    "extracteur d air",
    "extracteur d'air",
    "bouche vmc",
    "bouches vmc",
    "gaine vmc",
    "gaines vmc",
    "vmi",
    "ventilation vmi",
    "vmc salle de bains",
    "qualité air intérieur",
    "qualité de l air intérieur",
    "capteur qualité air intérieur",
    "détecteur qualité air intérieur",
    "filtration air",
    "air filtration",
    "closed crankcase ventilation",
    "local exhaust ventilation",
    "castorama ventilation",
    "atlantic climatisation ventilation",
    "humidificateur",
    "humidificateur d air",
    "déshumidificateur",
    "aérateur",
    "aerateur",
]


def auth_header() -> str:
    import base64

    login, pwd = os.environ.get("DATAFORSEO_LOGIN"), os.environ.get("DATAFORSEO_PASSWORD")
    if not login or not pwd:
        raise SystemExit("IDENTIFIANTS ABSENTS")
    return "Basic " + base64.b64encode(f"{login}:{pwd}".encode()).decode()


def main() -> None:
    label = "tetes-1"
    corps = [{
        "keywords": MOTS,
        "location_name": "France",
        "language_name": "French",
        "search_partners": False,
    }]
    req = urllib.request.Request(
        API,
        data=json.dumps(corps).encode(),
        headers={"Authorization": auth_header(), "Content-Type": "application/json"},
    )
    raw = urllib.request.urlopen(req, timeout=180).read()
    rep = json.loads(raw)
    task = (rep.get("tasks") or [{}])[0]
    status = task.get("status_code")
    msg = task.get("status_message")
    print("heure:", datetime.now().isoformat(timespec="seconds"))
    print("status:", status, msg)
    print("cost:", rep.get("cost"))
    print("n_demandes:", len(MOTS))
    if status == 40200 or "Payment Required" in str(msg):
        raise SystemExit("FAIL-CLOSED: quota/paiement")
    if status != 20000:
        raise SystemExit(f"FAIL-CLOSED: status {status} {msg}")
    res = task.get("result")
    if not res:
        raise SystemExit("FAIL-CLOSED: result vide")
    RAW.mkdir(parents=True, exist_ok=True)
    out = RAW / f"{label}.json"
    out.write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding="utf-8")
    print("saved:", out)
    series_out = RAW / f"{label}-series.txt"
    lines = []
    print(f"{'keyword':<52}{'vol':>8}{'cpc':>8}  loc lang")
    for r in res:
        kw = r.get("keyword") or ""
        vol = r.get("search_volume")
        cpc = r.get("cpc")
        loc = r.get("location_code")
        lang = r.get("language_code")
        print(f"{kw:<52}{str(vol):>8}{str(cpc):>8}  {loc} {lang}")
        serie = r.get("monthly_searches") or []
        serie_txt = " ".join(str(m.get("search_volume")) for m in serie[:12])
        lines.append(f"{kw}\t{vol}\t{cpc}\t{loc}\t{lang}\t{serie_txt}")
    series_out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("series:", series_out)
    returned = {r.get("keyword") for r in res}
    missing = [m for m in MOTS if m not in returned]
    if missing:
        print("NON RENDUS (n/a, pas 0):", missing)


if __name__ == "__main__":
    main()
