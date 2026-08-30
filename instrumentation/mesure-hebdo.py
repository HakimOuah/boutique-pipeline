#!/usr/bin/env python3
"""Relève les mesures hebdomadaires d'une ou plusieurs boutiques Shopify.

Écrit une note par boutique et par semaine ISO dans `instrumentation/mesures/`.
**Une note existante n'est jamais réécrite** : une mesure est un fait daté, on
ne réécrit pas l'histoire. Pour corriger un chiffre, écrire une note de
correction (cf. instrumentation/README.md).

Authentification — une application personnalisée par boutique, jamais d'OAuth
interactif : le script doit tourner sans écran. Pour chaque boutique, deux
variables d'environnement, nommées d'après le slug en majuscules :

    SHOPIFY_TUFTING_DOMAIN=xxxxxx.myshopify.com
    SHOPIFY_TUFTING_TOKEN=shpat_...

Le jeton exige le scope **read_reports** (Admin API). Les scopes de la CLI
Shopify (products, themes, content…) ne suffisent pas.

    python3 instrumentation/mesure-hebdo.py --boutiques tufting,bonum-vitae
    python3 instrumentation/mesure-hebdo.py --boutiques bonum-vitae --depuis 2026-08-17
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

RACINE = Path(__file__).resolve().parent
MESURES = RACINE / "mesures"
API_VERSION = os.environ.get("SHOPIFY_API_VERSION", "2026-07")

Q_SESSIONS = (
    "FROM sessions SHOW sessions, sessions_with_cart_additions, "
    "sessions_that_reached_checkout, conversion_rate "
    "TIMESERIES week SINCE {depuis} UNTIL {jusqu}"
)
Q_VENTES = (
    "FROM sales SHOW orders, total_sales, average_order_value, sales_reversals "
    "TIMESERIES week SINCE {depuis} UNTIL {jusqu}"
)


def identifiants(slug: str) -> tuple[str, str]:
    cle = slug.upper().replace("-", "_")
    domaine = os.environ.get(f"SHOPIFY_{cle}_DOMAIN")
    jeton = os.environ.get(f"SHOPIFY_{cle}_TOKEN")
    if not domaine or not jeton:
        raise SystemExit(
            f"SHOPIFY_{cle}_DOMAIN et SHOPIFY_{cle}_TOKEN doivent être définis dans "
            f"l'environnement. Aucune valeur de repli n'est codée en dur."
        )
    return domaine, jeton


def shopifyql(domaine: str, jeton: str, requete: str) -> list[list]:
    """Exécute une requête ShopifyQL et rend les lignes. Lève sur erreur de parse."""
    corps = json.dumps({
        "query": "query($q: String!) { shopifyqlQuery(query: $q) "
                 "{ tableData { columns { name } rows } parseErrors } }",
        "variables": {"q": requete},
    }).encode()
    req = urllib.request.Request(
        f"https://{domaine}/admin/api/{API_VERSION}/graphql.json",
        data=corps,
        headers={"Content-Type": "application/json", "X-Shopify-Access-Token": jeton},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            rep = json.loads(r.read())
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")[:400]
        raise SystemExit(f"HTTP {e.code} sur {domaine} — {detail}")

    if rep.get("errors"):
        raise SystemExit(f"Erreur GraphQL sur {domaine} : {rep['errors']}")
    bloc = (rep.get("data") or {}).get("shopifyqlQuery") or {}
    if bloc.get("parseErrors"):
        raise SystemExit(f"ShopifyQL refusée : {bloc['parseErrors']}\n  → {requete}")
    table = bloc.get("tableData") or {}
    return table.get("rows") or []


def par_semaine(lignes: list[list], nb_valeurs: int) -> dict[str, list]:
    """Indexe les lignes ShopifyQL sur le lundi de la semaine (1re colonne)."""
    out = {}
    for ligne in lignes:
        if not ligne:
            continue
        lundi = str(ligne[0])[:10]
        out[lundi] = (list(ligne[1:]) + [None] * nb_valeurs)[:nb_valeurs]
    return out


def nombre(v, defaut=""):
    if v in (None, "", "null"):
        return defaut
    try:
        f = float(v)
        return int(f) if f == int(f) else round(f, 2)
    except (TypeError, ValueError):
        return defaut


NOTE = """---
type: mesure
boutique: {slug}
periode: {periode}
du: {du}
au: {au}
source: shopify
# --- commerce
sessions: {sessions}
paniers: {paniers}
checkouts_atteints: {checkouts}
commandes: {commandes}
ca_eur: {ca}
aov_eur: {aov}
cvr_pct: {cvr}
remboursements_eur: {remb}
# --- acquisition
depense_ads_eur:
impressions:
clics:
ctr_pct:
cpc_eur:
cpa_eur:
roas:
# --- santé (non récupérable rétroactivement — à relever à la main)
gmc_approuves:
gmc_limites:
gmc_refuses:
pagespeed_mobile:
lcp_s:
---

# {slug} — {periode}

## Fait marquant de la semaine

*(relevé automatique du {aujourdhui}, à commenter si la semaine mérite un mot)*

## Interventions de la période

*(vue `interventions.base`, filtrée sur cette semaine)*
"""


def releve(slug: str, depuis: str, jusqu: str, ecrire: bool) -> None:
    domaine, jeton = identifiants(slug)
    sess = par_semaine(shopifyql(domaine, jeton, Q_SESSIONS.format(depuis=depuis, jusqu=jusqu)), 4)
    vent = par_semaine(shopifyql(domaine, jeton, Q_VENTES.format(depuis=depuis, jusqu=jusqu)), 4)

    MESURES.mkdir(exist_ok=True)
    ecrits = sautes = 0
    for lundi in sorted(set(sess) | set(vent)):
        d = dt.date.fromisoformat(lundi)
        y, w, _ = d.isocalendar()
        periode = f"{y}-W{w:02d}"
        cible = MESURES / f"{slug}-{periode}.md"
        if cible.exists():
            sautes += 1
            continue

        s = sess.get(lundi, [None] * 4)
        v = vent.get(lundi, [None] * 4)
        texte = NOTE.format(
            slug=slug, periode=periode, du=d, au=d + dt.timedelta(days=6),
            sessions=nombre(s[0]), paniers=nombre(s[1]), checkouts=nombre(s[2]),
            cvr=nombre(s[3], "0.0"), commandes=nombre(v[0]), ca=nombre(v[1]),
            aov=nombre(v[2]), remb=nombre(v[3]),
            aujourdhui=dt.date.today().isoformat(),
        )
        if ecrire:
            cible.write_text(texte, encoding="utf-8")
        print(f"  {'écrit ' if ecrire else 'à écrire'} {cible.name}  "
              f"{nombre(s[0], 0)} sessions · {nombre(v[0], 0)} cdes · {nombre(v[1], 0)} €")
        ecrits += 1
    print(f"  → {ecrits} note(s), {sautes} déjà présente(s) et laissée(s) intacte(s)")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--boutiques", required=True, help="slugs séparés par des virgules")
    ap.add_argument("--depuis", default=None, help="AAAA-MM-JJ (défaut : il y a 8 semaines)")
    ap.add_argument("--jusqu", default=None, help="AAAA-MM-JJ (défaut : aujourd'hui)")
    ap.add_argument("--ecrire", action="store_true", help="écrit vraiment (sinon dry-run)")
    a = ap.parse_args()

    jusqu = a.jusqu or dt.date.today().isoformat()
    depuis = a.depuis or (dt.date.today() - dt.timedelta(weeks=8)).isoformat()

    for slug in [s.strip() for s in a.boutiques.split(",") if s.strip()]:
        print(f"\n{slug}  ({depuis} → {jusqu})")
        releve(slug, depuis, jusqu, a.ecrire)

    if not a.ecrire:
        print("\nDRY-RUN — relancer avec --ecrire pour appliquer")
    return 0


if __name__ == "__main__":
    sys.exit(main())
