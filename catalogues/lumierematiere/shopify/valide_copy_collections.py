#!/usr/bin/env python3
"""Contrôle de la copy de collections-seo.json contre les règles maison.

Refuse : tiret cadratin ou demi-cadratin, Ø, apostrophe droite, vocabulaire interdit,
mot-clé absent en gras de la première phrase, nombre de paragraphes, ouvertures identiques.
Aucune écriture, aucun appel réseau.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SEO = json.loads((ROOT / "collections-seo.json").read_text(encoding="utf-8"))

INTERDITS = ["premium", "atelier", "artisanal", "aliexpress", "avis clients", "4,7/5", "note de"]
CARACTERES = {"—": "tiret cadratin", "–": "demi-cadratin", "Ø": "symbole diamètre", "'": "apostrophe droite"}

# Les 10 collections écrites ou réécrites le 26/08 : mot-clé exigé dès la première phrase.
# Les 14 antérieures sont la copy de référence validée : le mot-clé y est parfois en
# deuxième phrase du paragraphe d'ouverture, on ne les réécrit pas pour autant.
A_MOI = {
    "lustres-pampilles", "plafonniers-led", "lustres-chambre", "plafonniers-salon",
    "suspensions-cuisine", "plafonniers-cuisine", "suspensions-salon",
    "suspensions-papier", "suspensions-xxl", "suspensions-osier",
}

OPS_ATTENDUS = [
    "France métropolitaine",
    "1 à 2 jours",
    "6 à 15 jours",
    "7 à 17 jours",
    "30 jours",
]

soucis: list[str] = []
ouvertures: dict[str, str] = {}

for handle, copy in SEO.items():
    champs = {k: copy[k] for k in ("seo_title", "seo_description", "description_html")}
    blob = " ".join(champs.values())

    for char, nom in CARACTERES.items():
        for champ, valeur in champs.items():
            if char in valeur:
                soucis.append(f"{handle}.{champ} : {nom} « {char} »")

    for mot in INTERDITS:
        if mot in blob.lower():
            soucis.append(f"{handle} : vocabulaire interdit « {mot} »")

    paras = re.findall(r"<p>(.*?)</p>", copy["description_html"], flags=re.S)
    if len(paras) != 2:
        soucis.append(f"{handle} : {len(paras)} paragraphes au lieu de 2")
    if not paras:
        continue

    premiere = re.split(r"(?<=[.!?])\s", paras[0])[0]
    attendu = f"<strong>{copy['keyword']}</strong>"
    variantes = {attendu, attendu.replace("led", "LED"), attendu.replace("xxl", "XXL")}
    portee, ou = (premiere, "1re phrase") if handle in A_MOI else (paras[0], "1er paragraphe")
    if not any(v in portee for v in variantes):
        soucis.append(f"{handle} : mot-clé pas en gras dans la {ou} → {portee[:90]!r}")

    debut = re.sub(r"<[^>]+>", "", paras[0])[:26].lower()
    if debut in ouvertures:
        soucis.append(f"{handle} : même ouverture que {ouvertures[debut]} → {debut!r}")
    ouvertures[debut] = handle

    for champ in ("seo_title", "seo_description"):
        n = len(copy[champ])
        limite = 70 if champ == "seo_title" else 170
        if n > limite:
            soucis.append(f"{handle}.{champ} : {n} caractères (> {limite})")

    # tout chiffre d'ops cité doit être un chiffre d'ops autorisé
    for motif in re.findall(r"\b\d+ à \d+ jours\b", blob):
        if motif not in " ".join(OPS_ATTENDUS):
            soucis.append(f"{handle} : délai non conforme « {motif} »")

print(f"{len(SEO)} collections contrôlées")
if soucis:
    print("\nPROBLÈMES :")
    for s in soucis:
        print("  -", s)
    sys.exit(1)
print("copy conforme")
