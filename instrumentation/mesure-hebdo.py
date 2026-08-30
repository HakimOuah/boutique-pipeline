#!/usr/bin/env python3
"""Relève les mesures hebdomadaires d'une ou plusieurs boutiques Shopify.

Écrit une note par boutique et par semaine ISO dans `instrumentation/mesures/`.
**Une note existante n'est jamais réécrite** : une mesure est un fait daté, on
ne réécrit pas l'histoire. Pour corriger un chiffre, écrire une note de
correction (cf. instrumentation/README.md).

Authentification — jamais d'OAuth interactif : le script doit tourner sans
écran. Shopify ne permet plus de créer une app personnalisée depuis l'admin
d'une boutique (constat du 30/08/2026). La route actuelle est le
**client credentials grant** : une app du dev dashboard donne un ID client et
un secret, qu'on échange contre un jeton de 24 h. Le script en fabrique un à
chaque exécution.

Une seule app suffit pour toutes les boutiques d'une **même organisation** —
c'est la limite du grant : il ne franchit pas la frontière d'organisation.

    SHOPIFY_CLIENT_ID=...            # partagés par toute l'organisation
    SHOPIFY_CLIENT_SECRET=...
    SHOPIFY_TUFTING_DOMAIN=xxxxxx.myshopify.com
    SHOPIFY_BONUM_VITAE_DOMAIN=kw7vak-g0.myshopify.com

L'app doit être **installée** sur chaque boutique, et sa version publiée doit
déclarer le scope **read_reports** — les scopes viennent de la version
publiée, pas de la requête. Les scopes de la CLI Shopify (products, themes,
content…) ne suffisent pas.

Un jeton statique reste accepté s'il existe (`SHOPIFY_<SLUG>_TOKEN`, apps
héritées) : il est alors utilisé tel quel, sans échange.

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
import urllib.parse
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
# Sessions payantes, isolees par le balisage UTM. Rend 0 partout tant que les
# campagnes ne sont pas baliseees — c'est justement le symptome a surveiller.
Q_PAYANT = (
    "FROM sessions SHOW sessions TIMESERIES week WHERE utm_medium = 'cpc' "
    "SINCE {depuis} UNTIL {jusqu}"
)
Q_VENTES = (
    "FROM sales SHOW orders, total_sales, average_order_value, sales_reversals "
    "TIMESERIES week SINCE {depuis} UNTIL {jusqu}"
)


def _jeton_par_echange(domaine: str, cid: str, secret: str) -> str:
    """Client credentials grant : rend un jeton valable 24 h. Sans interaction."""
    corps = urllib.parse.urlencode({
        "grant_type": "client_credentials",
        "client_id": cid,
        "client_secret": secret,
    }).encode()
    req = urllib.request.Request(
        f"https://{domaine}/admin/oauth/access_token",
        data=corps,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            rep = json.loads(r.read())
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")[:300]
        raise SystemExit(
            f"Échange de jeton refusé pour {domaine} (HTTP {e.code}) — {detail}\n"
            f"  Vérifier : l'app est installée sur cette boutique, et elle appartient à\n"
            f"  la même organisation Shopify (le grant ne franchit pas cette frontière)."
        )
    jeton = rep.get("access_token")
    if not jeton:
        raise SystemExit(f"Réponse sans access_token pour {domaine} : {rep}")
    portee = rep.get("scope", "")
    if "read_reports" not in portee:
        raise SystemExit(
            f"Le jeton de {domaine} n'a pas le scope read_reports (obtenu : {portee or 'aucun'}).\n"
            f"  Ajouter read_reports à la configuration de l'app dans le dev dashboard,\n"
            f"  puis PUBLIER une nouvelle version : les scopes viennent de la version publiée."
        )
    return jeton


def identifiants(slug: str) -> tuple[str, str]:
    cle = slug.upper().replace("-", "_")
    domaine = os.environ.get(f"SHOPIFY_{cle}_DOMAIN")
    if not domaine:
        raise SystemExit(f"SHOPIFY_{cle}_DOMAIN doit être défini dans l'environnement.")

    jeton = os.environ.get(f"SHOPIFY_{cle}_TOKEN")
    if jeton:
        return domaine, jeton

    cid = os.environ.get(f"SHOPIFY_{cle}_CLIENT_ID") or os.environ.get("SHOPIFY_CLIENT_ID")
    secret = os.environ.get(f"SHOPIFY_{cle}_CLIENT_SECRET") or os.environ.get("SHOPIFY_CLIENT_SECRET")
    if not cid or not secret:
        raise SystemExit(
            f"Aucun identifiant pour {slug}. Définir soit SHOPIFY_CLIENT_ID et\n"
            f"SHOPIFY_CLIENT_SECRET (partagés par l'organisation), soit un jeton hérité\n"
            f"SHOPIFY_{cle}_TOKEN. Aucune valeur de repli n'est codée en dur."
        )
    return domaine, _jeton_par_echange(domaine, cid, secret)


def shopifyql(domaine: str, jeton: str, requete: str) -> list[dict]:
    """Exécute une requête ShopifyQL et rend les lignes.

    ShopifyQL rend chaque ligne comme un objet indexé par nom de colonne
    (constaté le 30/08/2026), pas comme un tableau : on lit donc par nom,
    ce qui reste juste si Shopify ajoute ou réordonne une colonne.
    """
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


def par_semaine(lignes: list[dict]) -> dict[str, dict]:
    """Indexe les lignes sur le lundi de la semaine (colonne `week`)."""
    return {str(l.get("week", ""))[:10]: l for l in lignes if l.get("week")}


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
sessions_payantes: {payantes}
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
    sess = par_semaine(shopifyql(domaine, jeton, Q_SESSIONS.format(depuis=depuis, jusqu=jusqu)))
    vent = par_semaine(shopifyql(domaine, jeton, Q_VENTES.format(depuis=depuis, jusqu=jusqu)))
    paye = par_semaine(shopifyql(domaine, jeton, Q_PAYANT.format(depuis=depuis, jusqu=jusqu)))

    # Les semaines anterieures a la premiere activite ne sont pas des mesures :
    # ce sont des semaines ou la boutique n'existait pas. On les ecarte. En
    # revanche une semaine a zero APRES l'ouverture est une donnee, on la garde.
    semaines = sorted(set(sess) | set(vent))
    def active(l):
        return any(str(d.get(l, {}).get(c, "0")) not in ("", "0", "0.0", "None")
                   for d, c in ((sess, "sessions"), (vent, "orders"), (vent, "total_sales")))
    premiere = next((l for l in semaines if active(l)), None)
    if premiere is None:
        print("  → aucune activite sur la periode, aucune note ecrite")
        return
    ignorees = semaines.index(premiere)
    if ignorees:
        print(f"  ({ignorees} semaine(s) sans aucune activite avant le {premiere} — ecartees)")
    semaines = semaines[ignorees:]

    MESURES.mkdir(exist_ok=True)
    ecrits = sautes = 0
    for lundi in semaines:
        d = dt.date.fromisoformat(lundi)
        y, w, _ = d.isocalendar()
        periode = f"{y}-W{w:02d}"
        cible = MESURES / f"{slug}-{periode}.md"
        if cible.exists():
            sautes += 1
            continue

        s, v = sess.get(lundi, {}), vent.get(lundi, {})
        texte = NOTE.format(
            slug=slug, periode=periode, du=d, au=d + dt.timedelta(days=6),
            sessions=nombre(s.get("sessions")),
            payantes=nombre(paye.get(lundi, {}).get("sessions")),
            paniers=nombre(s.get("sessions_with_cart_additions")),
            checkouts=nombre(s.get("sessions_that_reached_checkout")),
            cvr=nombre(s.get("conversion_rate"), "0.0"),
            commandes=nombre(v.get("orders")),
            ca=nombre(v.get("total_sales")),
            aov=nombre(v.get("average_order_value")),
            remb=nombre(v.get("sales_reversals")),
            aujourdhui=dt.date.today().isoformat(),
        )
        if ecrire:
            cible.write_text(texte, encoding="utf-8")
        print(f"  {'écrit ' if ecrire else 'à écrire'} {cible.name}  "
              f"{nombre(s.get('sessions'), 0)} sessions · "
              f"{nombre(s.get('sessions_that_reached_checkout'), 0)} checkouts · "
              f"{nombre(v.get('orders'), 0)} cdes · {nombre(v.get('total_sales'), 0)} €")
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
