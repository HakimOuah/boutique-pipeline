#!/usr/bin/env python3
"""Collections de pièce et d'opportunité Lumière Matière (26/08/2026).

Ordre et périmètre : § A de CONCURRENT-LUSTRIA-2026-08-25.md.
Deux renommages, huit créations, rattachement des fiches existantes.

Étapes (idempotentes, à lancer dans l'ordre) :
  renomme    2 handles + redirections 301 + collection_list du thème MAIN
  cree       les 8 collections manquantes, publiées, image reprise d'une fiche membre
  rattache   collectionAddProducts pour chaque collection
  verifie    relit l'API et contrôle handles, publication, effectifs, redirections

N'écrit jamais de titre produit, de SKU, de variante ni de prix.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from apply_fullstack import theme_file, upsert_theme_file  # noqa: E402
from client import gql  # noqa: E402
from import_catalogue import ONLINE, publish  # noqa: E402

STATE = ROOT / "state.json"
CATALOGUE = ROOT / "catalogue-pieces-2026-08-26.json"

# ── renommages ────────────────────────────────────────────────────────────────
# clé = clé CSV dans import_catalogue.COLLECTIONS ; (ancien handle, nouveau handle, nouveau titre)
RENOMMAGES = [
    ("Lustres cristal", "lustres-effet-cristal", "lustres-pampilles", "Lustres pampilles"),
    ("Plafonniers", "plafonniers", "plafonniers-led", "Plafonniers LED"),
]

# ── créations, dans l'ordre du § A ────────────────────────────────────────────
# clé CSV (registre import_catalogue) : (titre, handle, mot-clé, volume, LM de la photo)
NOUVELLES = [
    ("Lustres chambre", "Lustres chambre", "lustres-chambre", "lustre chambre", 10810, "LM-059"),
    ("Plafonniers salon", "Plafonniers salon", "plafonniers-salon", "plafonnier salon", 8970, "LM-084"),
    ("Suspensions cuisine", "Suspensions cuisine", "suspensions-cuisine", "suspension cuisine", 4800, "LM-013"),
    ("Plafonniers cuisine", "Plafonniers cuisine", "plafonniers-cuisine", "plafonnier cuisine", 6190, "LM-086"),
    ("Suspensions salon", "Suspensions salon", "suspensions-salon", "suspension salon", 4080, "LM-010"),
    ("Suspensions papier", "Suspensions papier", "suspensions-papier", "suspension papier", 4760, "LM-092"),
    ("Grandes suspensions XXL", "Grandes suspensions XXL", "suspensions-xxl", "suspension xxl", 1310, "LM-029"),
    ("Suspensions osier", "Suspensions osier", "suspensions-osier", "suspension osier", 3180, "LM-021"),
]

# ── rattachements ─────────────────────────────────────────────────────────────
# Règles appliquées, vérifiées fiche par fiche sur les planches-contacts du 26/08 :
#  · pièce = type de luminaire + fixation (suspension / plafonnier) + diamètre réel des variantes
#  · cuisine  : Ø minimum ≤ 45 cm, ou multi-lampes pour un îlot, ou titre « cuisine »
#  · salon    : suspension de Ø minimum ≥ 40 cm, ou pièce visiblement large, ou titre « salon »
#  · chambre  : Ø ≤ 45 cm dominant, lumière douce, pas de pièce d'apparat
#  · XXL      : au moins une variante de Ø 100 cm ou plus
#  · papier / osier : uniquement si la photo montre la matière
MEMBRES = {
    "lustres-chambre": [
        "LM-059", "LM-062", "LM-064", "LM-065", "LM-066",
        "LM-072", "LM-078", "LM-099", "LM-113", "LM-117",
    ],
    "plafonniers-salon": [
        "LM-056", "LM-061", "LM-083", "LM-084", "LM-087",
        "LM-088", "LM-091", "LM-094", "LM-120",
    ],
    "suspensions-cuisine": [
        "LM-006", "LM-007", "LM-011", "LM-013", "LM-020", "LM-023", "LM-024", "LM-027",
        "LM-028", "LM-032", "LM-033", "LM-036", "LM-042", "LM-044", "LM-047", "LM-049",
        "LM-050", "LM-051", "LM-052", "LM-073", "LM-074", "LM-075", "LM-076", "LM-079",
        "LM-081", "LM-093", "LM-096", "LM-097", "LM-101", "LM-105", "LM-107",
    ],
    "plafonniers-cuisine": ["LM-057", "LM-086", "LM-089", "LM-090"],
    "suspensions-salon": [
        "LM-001", "LM-002", "LM-003", "LM-004", "LM-005", "LM-008", "LM-009", "LM-010",
        "LM-012", "LM-014", "LM-015", "LM-018", "LM-021", "LM-025", "LM-026", "LM-029",
        "LM-030", "LM-041", "LM-048", "LM-082", "LM-085", "LM-092", "LM-098", "LM-109",
        "LM-110", "LM-111", "LM-115", "LM-117", "LM-121",
    ],
    "suspensions-papier": ["LM-092"],
    "suspensions-xxl": [
        "LM-003", "LM-005", "LM-008", "LM-010", "LM-015", "LM-029", "LM-053", "LM-055",
        "LM-058", "LM-059", "LM-067", "LM-070", "LM-071", "LM-092", "LM-121",
    ],
    "suspensions-osier": ["LM-017", "LM-021", "LM-022", "LM-023", "LM-024"],
    # renommée : on complète avec les plafonniers LED encastrés rangés ailleurs
    "plafonniers-led": ["LM-056", "LM-057", "LM-060", "LM-061", "LM-094", "LM-120"],
}

# Deux suspensions à ampoules E27 héritées de l'ancienne collection « Plafonniers ».
# Sous le titre « Plafonniers LED » elles rendent le H1 faux ; elles restent au catalogue
# et sont désormais dans suspensions-salon, où elles étaient attendues.
RETRAITS = {"plafonniers-led": ["LM-082", "LM-085"]}


def catalogue() -> dict[str, dict]:
    rows = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    return {r["lm"]: r for r in rows if r["lm"]}


def charge_state() -> dict:
    return json.loads(STATE.read_text(encoding="utf-8"))


def ecrit_state(state: dict) -> None:
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def collections_live() -> dict[str, dict]:
    out: dict[str, dict] = {}
    cursor = None
    while True:
        data = gql(
            """
            query C($cursor: String) {
              collections(first: 50, after: $cursor) {
                pageInfo { hasNextPage endCursor }
                nodes { id handle title productsCount { count } }
              }
            }
            """,
            {"cursor": cursor},
        )["collections"]
        for n in data["nodes"]:
            out[n["handle"]] = n
        if not data["pageInfo"]["hasNextPage"]:
            return out
        cursor = data["pageInfo"]["endCursor"]


# ── étape 1 : renommages ──────────────────────────────────────────────────────


def redirections_live() -> dict[str, str]:
    out: dict[str, str] = {}
    cursor = None
    while True:
        data = gql(
            """
            query R($cursor: String) {
              urlRedirects(first: 250, after: $cursor) {
                pageInfo { hasNextPage endCursor }
                nodes { id path target }
              }
            }
            """,
            {"cursor": cursor},
        )["urlRedirects"]
        for n in data["nodes"]:
            out[n["path"]] = n["target"]
        if not data["pageInfo"]["hasNextPage"]:
            return out
        cursor = data["pageInfo"]["endCursor"]


def cree_redirection(ancien: str, nouveau: str) -> None:
    payload = gql(
        """
        mutation Redir($input: UrlRedirectInput!) {
          urlRedirectCreate(urlRedirect: $input) {
            urlRedirect { id path target }
            userErrors { field message }
          }
        }
        """,
        {"input": {"path": f"/collections/{ancien}", "target": f"/collections/{nouveau}"}},
    )["urlRedirectCreate"]
    if payload["userErrors"]:
        raise RuntimeError((ancien, payload["userErrors"]))
    print(f"    redirection 301 /collections/{ancien} -> /collections/{nouveau}")


def renomme() -> None:
    live = collections_live()
    for _, ancien, nouveau, titre in RENOMMAGES:
        if nouveau in live:
            print(f"  {nouveau} déjà en place")
            continue
        node = live.get(ancien)
        if not node:
            raise RuntimeError(f"ni {ancien} ni {nouveau} sur la boutique")
        payload = gql(
            """
            mutation U($input: CollectionInput!) {
              collectionUpdate(input: $input) {
                collection { id handle title }
                userErrors { field message }
              }
            }
            """,
            {"input": {"id": node["id"], "handle": nouveau, "title": titre}},
        )["collectionUpdate"]
        if payload["userErrors"]:
            raise RuntimeError((ancien, payload["userErrors"]))
        print(f"  {ancien} -> {payload['collection']['handle']} · « {titre} »")
        time.sleep(0.4)

    # Shopify ne pose pas de redirection lors d'un changement de handle par l'API Admin :
    # on relit et on crée ce qui manque, pour ne laisser aucune 404.
    existantes = redirections_live()
    for _, ancien, nouveau, _ in RENOMMAGES:
        chemin = f"/collections/{ancien}"
        if chemin in existantes:
            print(f"    redirection déjà là : {chemin} -> {existantes[chemin]}")
            continue
        cree_redirection(ancien, nouveau)
        time.sleep(0.3)


def patch_liste_collections() -> None:
    """templates/list-collections.json est volontairement limité aux collections du menu :
    on remplace les deux handles renommés et on ajoute les huit nouvelles."""
    chemin = "templates/list-collections.json"
    data = theme_file(chemin)
    reglages = data["sections"]["main"]["settings"]
    avant = list(reglages["collection_list"])
    liste = list(avant)
    for _, ancien, nouveau, _ in RENOMMAGES:
        liste = [nouveau if h == ancien else h for h in liste]
    for *_, handle, _kw, _vol, _photo in NOUVELLES:
        if handle not in liste:
            liste.append(handle)
    if liste == avant:
        print(f"  {chemin} déjà à jour")
        return
    reglages["collection_list"] = liste
    upsert_theme_file(chemin, data)
    print(f"  collection_list : {len(avant)} -> {len(liste)} entrées")


# ── étape 2 : créations ───────────────────────────────────────────────────────


def cree() -> None:
    live = collections_live()
    cat = catalogue()
    state = charge_state()
    for cle_csv, titre, handle, _kw, _vol, lm_photo in NOUVELLES:
        if handle in live:
            print(f"  {handle} déjà créée")
            state.setdefault("collections", {})[cle_csv] = live[handle]["id"]
            continue
        entree = {"title": titre, "handle": handle, "sortOrder": "BEST_SELLING"}
        photo = cat[lm_photo]["photo"]
        if photo:
            entree["image"] = {"src": photo, "altText": titre}
        payload = gql(
            """
            mutation Coll($input: CollectionInput!) {
              collectionCreate(input: $input) {
                collection { id handle title }
                userErrors { field message }
              }
            }
            """,
            {"input": entree},
        )["collectionCreate"]
        if payload["userErrors"]:
            raise RuntimeError((handle, payload["userErrors"]))
        cid = payload["collection"]["id"]
        publish(cid)
        state.setdefault("collections", {})[cle_csv] = cid
        ecrit_state(state)
        print(f"  {handle} {cid} · image reprise de {lm_photo}")
        time.sleep(0.4)
    ecrit_state(state)


# ── étape 3 : rattachements ──────────────────────────────────────────────────


def rattache() -> None:
    live = collections_live()
    cat = catalogue()
    total = 0
    for handle, codes in MEMBRES.items():
        node = live.get(handle)
        if not node:
            raise RuntimeError(f"collection absente : {handle}")
        deja = membres_actuels(node["id"])
        ids, manquants = [], []
        for code in codes:
            fiche = cat.get(code)
            if not fiche:
                raise RuntimeError(f"{handle}: fiche inconnue {code}")
            if fiche["status"] != "ACTIVE":
                raise RuntimeError(f"{handle}: fiche non active {code}")
            if fiche["id"] in deja:
                continue
            ids.append(fiche["id"])
            manquants.append(code)
        if not ids:
            print(f"  {handle} · {len(codes)} fiches, rien à ajouter")
            continue
        for lot in [ids[i : i + 100] for i in range(0, len(ids), 100)]:
            payload = gql(
                """
                mutation Add($id: ID!, $productIds: [ID!]!) {
                  collectionAddProducts(id: $id, productIds: $productIds) {
                    userErrors { field message }
                  }
                }
                """,
                {"id": node["id"], "productIds": lot},
            )["collectionAddProducts"]
            if payload["userErrors"]:
                raise RuntimeError((handle, payload["userErrors"]))
            time.sleep(0.4)
        total += len(ids)
        print(f"  {handle} · +{len(ids)} : {', '.join(manquants)}")
    print(f"OK {total} rattachements")


def nettoie() -> None:
    """Retire de plafonniers-led les fiches qui ne sont pas des plafonniers LED.
    Refuse d'agir si la fiche n'a pas déjà une autre collection d'accueil."""
    live = collections_live()
    cat = catalogue()
    for handle, codes in RETRAITS.items():
        node = live[handle]
        presents = membres_actuels(node["id"])
        ids, retires = [], []
        for code in codes:
            fiche = cat[code]
            autres = [c for c in fiche["collections"] if c not in (handle, "frontpage")]
            if not any(c in MEMBRES or c != handle for c in autres):
                raise RuntimeError(f"{code} n'a pas d'autre collection : retrait refusé")
            if fiche["id"] not in presents:
                print(f"  {code} déjà retiré de {handle}")
                continue
            ids.append(fiche["id"])
            retires.append(code)
        if not ids:
            continue
        payload = gql(
            """
            mutation Rem($id: ID!, $productIds: [ID!]!) {
              collectionRemoveProducts(id: $id, productIds: $productIds) {
                job { done }
                userErrors { field message }
              }
            }
            """,
            {"id": node["id"], "productIds": ids},
        )["collectionRemoveProducts"]
        if payload["userErrors"]:
            raise RuntimeError((handle, payload["userErrors"]))
        print(f"  {handle} · -{len(ids)} : {', '.join(retires)}")
        time.sleep(1.0)


def membres_actuels(cid: str) -> set[str]:
    data = gql(
        """
        query M($id: ID!) {
          collection(id: $id) { products(first: 250) { nodes { id } } }
        }
        """,
        {"id": cid},
    )
    return {n["id"] for n in data["collection"]["products"]["nodes"]}


# ── étape 4 : vérification ───────────────────────────────────────────────────


def statut_vitrine(url: str, suivre: bool = True):
    """Code HTTP renvoyé par la boutique publique, et la cible quand on ne suit pas."""
    import urllib.error
    import urllib.request

    class SansRedirection(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *_args, **_kwargs):
            return None

    opener = urllib.request.build_opener() if suivre else urllib.request.build_opener(SansRedirection)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with opener.open(req, timeout=45) as resp:
            return resp.status if suivre else (resp.status, resp.headers.get("Location"))
    except urllib.error.HTTPError as err:
        cible = err.headers.get("Location") if err.headers else None
        return err.code if suivre else (err.code, cible)


def verifie() -> None:
    live = collections_live()
    redirs = redirections_live()
    souci = []

    for _, ancien, nouveau, titre in RENOMMAGES:
        if ancien in live:
            souci.append(f"ancien handle toujours présent : {ancien}")
        if nouveau not in live:
            souci.append(f"handle renommé absent : {nouveau}")
        elif live[nouveau]["title"] != titre:
            souci.append(f"titre inattendu sur {nouveau}: {live[nouveau]['title']}")
        chemin = f"/collections/{ancien}"
        if redirs.get(chemin) != f"/collections/{nouveau}":
            souci.append(f"redirection manquante ou fausse : {chemin}")

    for _, titre, handle, _kw, _vol, _p in NOUVELLES:
        if handle not in live:
            souci.append(f"collection non créée : {handle}")
        elif live[handle]["title"] != titre:
            souci.append(f"titre inattendu sur {handle}: {live[handle]['title']}")

    for handle, codes in MEMBRES.items():
        node = live.get(handle)
        if not node:
            souci.append(f"collection absente : {handle}")
            continue
        attendu = len(set(codes))
        obtenu = node["productsCount"]["count"]
        marque = "" if obtenu >= attendu else "  ← INCOMPLET"
        print(f"  {handle:22} {obtenu:3} fiches (attendu >= {attendu}){marque}")
        if obtenu < attendu:
            souci.append(f"{handle}: {obtenu} < {attendu}")

    # publishedOnCurrentPublication demande read_product_listings, que le token CLI n'a pas :
    # on contrôle la publication là où elle compte, sur la vitrine.
    print()
    for handle in [h for *_, h, _kw, _v, _p in NOUVELLES] + [n for _, _, n, _ in RENOMMAGES]:
        code = statut_vitrine(f"https://lumierematiere.fr/collections/{handle}")
        print(f"  /collections/{handle:22} HTTP {code}")
        if code != 200:
            souci.append(f"vitrine {handle} : HTTP {code}")
    for _, ancien, nouveau, _ in RENOMMAGES:
        code, cible = statut_vitrine(f"https://lumierematiere.fr/collections/{ancien}", suivre=False)
        # Shopify renvoie un Location relatif ; on accepte les deux formes.
        attendus = {
            f"/collections/{nouveau}",
            f"https://lumierematiere.fr/collections/{nouveau}",
        }
        print(f"  /collections/{ancien:22} HTTP {code} -> {cible}")
        if code != 301 or cible not in attendus:
            souci.append(f"redirection vitrine {ancien} : {code} -> {cible}")

    if souci:
        print("\nPROBLÈMES :")
        for s in souci:
            print("  -", s)
        raise SystemExit(1)
    print("\nvérification OK")


ETAPES = {
    "renomme": lambda: (renomme(), patch_liste_collections()),
    "cree": cree,
    "rattache": rattache,
    "nettoie": nettoie,
    "verifie": verifie,
}


def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] not in ETAPES:
        raise SystemExit(f"usage: {Path(__file__).name} {{{'|'.join(ETAPES)}}}")
    etape = sys.argv[1]
    print(f"=== {etape} ===")
    ETAPES[etape]()


if __name__ == "__main__":
    main()
