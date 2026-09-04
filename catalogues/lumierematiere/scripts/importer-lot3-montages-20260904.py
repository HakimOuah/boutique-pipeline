#!/usr/bin/env python3
"""Import du lot 3 Codex (montages fournisseur remplaces) sur Lumiere Matiere.

ATTENTION — ce script n'a PAS servi le 04/09. SHOPIFY_LUMIERE_MATIERE_TOKEN du .env
ne porte que le scope `read_reports` (verifie via currentAppInstallation.accessScopes) :
insuffisant pour lire ou ecrire des produits. L'import du 04/09 est passe par le
connecteur MCP Shopify pour les mutations, et par un PUT curl direct sur les URL
pre-signees pour le transfert des fichiers.

Le script reste valable tel quel des qu'un token portant read_products / write_products
est en place. lot3-import-plan.json documente exactement ce qui a ete applique.

Ne touche JAMAIS aux SKU (sku_attr DSers) : aucune mutation de variante autre que
productVariantAppendMedia, qui n'attache qu'un media.

Usage : python3 importer-lot3-montages-20260904.py [--dry-run]
"""
import json, os, sys, time, mimetypes, urllib.request, urllib.error, uuid
from pathlib import Path

RACINE = Path(__file__).resolve().parents[3]          # boutique-pipeline/
BOUTIQUE = Path(__file__).resolve().parents[1]        # catalogues/lumierematiere/
LIVRAISON = BOUTIQUE / "livraisons-visuels-codex" / "montages-2026-09-04"
API = "2025-07"
DRY = "--dry-run" in sys.argv

env = {}
for ligne in (RACINE / ".env").read_text(encoding="utf-8").splitlines():
    if "=" in ligne and not ligne.strip().startswith("#"):
        k, _, v = ligne.partition("=")
        env[k.strip()] = v.strip().strip('"').strip("'")
DOMAINE = env["SHOPIFY_LUMIERE_MATIERE_DOMAIN"]
JETON = env["SHOPIFY_LUMIERE_MATIERE_TOKEN"]


def gql(query, variables=None):
    corps = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(
        f"https://{DOMAINE}/admin/api/{API}/graphql.json", data=corps,
        headers={"X-Shopify-Access-Token": JETON, "Content-Type": "application/json"})
    for essai in range(5):
        try:
            rep = json.load(urllib.request.urlopen(req, timeout=60))
        except urllib.error.HTTPError as e:
            if e.code in (429, 502, 503) and essai < 4:
                time.sleep(2 * (essai + 1)); continue
            raise
        if rep.get("errors"):
            raise SystemExit(f"GraphQL: {json.dumps(rep['errors'], ensure_ascii=False)}")
        return rep["data"]
    raise SystemExit("trop de tentatives")


def erreurs(bloc, *cles):
    for c in cles:
        if bloc.get(c):
            raise SystemExit(f"{c}: {json.dumps(bloc[c], ensure_ascii=False)}")


def televerser(chemin: Path) -> str:
    """stagedUploadsCreate + POST multipart -> resourceUrl."""
    d = gql("""mutation($i:[StagedUploadInput!]!){ stagedUploadsCreate(input:$i){
        stagedTargets{ url resourceUrl parameters{ name value } } userErrors{ field message } } }""",
        {"i": [{"filename": chemin.name, "mimeType": "image/jpeg",
                "resource": "IMAGE", "httpMethod": "POST",
                "fileSize": str(chemin.stat().st_size)}]})["stagedUploadsCreate"]
    erreurs(d, "userErrors")
    cible = d["stagedTargets"][0]
    limite = uuid.uuid4().hex
    corps = b""
    for p in cible["parameters"]:
        corps += (f"--{limite}\r\nContent-Disposition: form-data; name=\"{p['name']}\"\r\n\r\n"
                  f"{p['value']}\r\n").encode()
    corps += (f"--{limite}\r\nContent-Disposition: form-data; name=\"file\"; "
              f"filename=\"{chemin.name}\"\r\nContent-Type: image/jpeg\r\n\r\n").encode()
    corps += chemin.read_bytes() + f"\r\n--{limite}--\r\n".encode()
    req = urllib.request.Request(cible["url"], data=corps,
        headers={"Content-Type": f"multipart/form-data; boundary={limite}"})
    with urllib.request.urlopen(req, timeout=180) as r:
        if r.status not in (200, 201, 204):
            raise SystemExit(f"upload {chemin.name}: HTTP {r.status}")
    return cible["resourceUrl"]


def attendre_pret(product_gid, attendus, timeout=300):
    t0 = time.time()
    while time.time() - t0 < timeout:
        n = gql("""query($id:ID!){ product(id:$id){ media(first:50){ nodes{
                id status ... on MediaImage{ image{ url } } } } } }""",
                {"id": product_gid})["product"]["media"]["nodes"]
        etats = {m["id"]: m.get("status") for m in n if m["id"] in attendus}
        if all(v == "READY" for v in etats.values()) and len(etats) == len(attendus):
            return n
        if any(v == "FAILED" for v in etats.values()):
            raise SystemExit(f"media FAILED: {etats}")
        time.sleep(4)
    raise SystemExit("timeout traitement media")


PLAN = json.loads(Path(__file__).with_name("lot3-import-plan.json").read_text(encoding="utf-8"))

for fiche in PLAN["fiches"]:
    handle, pid = fiche["handle"], fiche["product_id"]
    print(f"\n=== {handle}")
    nouveaux = []
    for img in fiche["ajouts"]:
        chemin = LIVRAISON / handle / img["fichier"]
        if not chemin.exists():
            raise SystemExit(f"absent: {chemin}")
        if DRY:
            print(f"  [dry] {img['fichier']} -> {img['alt']}"); continue
        url = televerser(chemin)
        d = gql("""mutation($id:ID!,$m:[CreateMediaInput!]!){ productCreateMedia(productId:$id, media:$m){
            media{ ... on MediaImage{ id status } } mediaUserErrors{ field message } } }""",
            {"id": pid, "m": [{"originalSource": url, "alt": img["alt"],
                               "mediaContentType": "IMAGE"}]})["productCreateMedia"]
        erreurs(d, "mediaUserErrors")
        mid = d["media"][0]["id"]
        nouveaux.append((img["fichier"], mid))
        print(f"  + {img['fichier']}  {mid}")
    if DRY:
        continue
    if nouveaux:
        attendre_pret(pid, {m for _, m in nouveaux})
        print("  medias READY")
    par_fichier = dict(nouveaux)

    # ordre final : jetons "NEW:<fichier>" (media cree ici) ou "ID:<gid>" (media deja en place)
    ordre = []
    for jeton in fiche["ordre"]:
        if jeton.startswith("NEW:"):
            ordre.append(par_fichier[jeton[4:]])
        else:
            ordre.append(jeton[3:])
    d = gql("""mutation($id:ID!,$m:[MoveInput!]!){ productReorderMedia(id:$id, moves:$m){
        job{ id done } userErrors{ field message } } }""",
        {"id": pid, "m": [{"id": mid, "newPosition": str(i)} for i, mid in enumerate(ordre)]})["productReorderMedia"]
    erreurs(d, "userErrors")
    jid = d["job"]["id"]
    for _ in range(60):
        if gql("query($id:ID!){ job(id:$id){ done } }", {"id": jid})["job"]["done"]:
            break
        time.sleep(2)
    else:
        raise SystemExit("reorder: job non termine")
    print(f"  ordre applique ({len(ordre)} medias)")

    # rattachement aux variantes
    for att in fiche.get("variantes", []):
        d = gql("""mutation($id:ID!,$v:[ProductVariantAppendMediaInput!]!){
            productVariantAppendMedia(productId:$id, variantMedia:$v){
              userErrors{ field message } } }""",
            {"id": pid, "v": [{"variantId": att["variant_id"],
                               "mediaIds": [par_fichier[att["fichier"]]]}]})["productVariantAppendMedia"]
        erreurs(d, "userErrors")
        print(f"  ~ {att['libelle']} <- {att['fichier']}")

    # suppression des anciens medias, par identifiant (les noms de fichier se recouvrent)
    if fiche.get("supprimer"):
        d = gql("""mutation($id:ID!,$m:[ID!]!){ productDeleteMedia(productId:$id, mediaIds:$m){
            deletedMediaIds mediaUserErrors{ field message } } }""",
            {"id": pid, "m": fiche["supprimer"]})["productDeleteMedia"]
        erreurs(d, "mediaUserErrors")
        print(f"  - {len(d['deletedMediaIds'])} montages supprimes")

print("\n=== controle final")
for fiche in PLAN["fiches"]:
    p = gql("""query($id:ID!){ product(id:$id){ handle title
        media(first:50){ nodes{ id alt ... on MediaImage{ image{ url } } } }
        variants(first:20){ nodes{ title sku media(first:3){ nodes{ id } } } } } }""",
        {"id": fiche["product_id"]})["product"]
    noms = [(m.get("image") or {}).get("url", "").split("/")[-1].split("?")[0] for m in p["media"]["nodes"]]
    print(f"\n{p['handle']} — {p['title']}")
    for i, n in enumerate(noms):
        print(f"   {i}. {n}")
    for v in p["variants"]["nodes"]:
        mids = [m["id"] for m in v["media"]["nodes"]]
        nom = next((noms[i] for i, m in enumerate(p["media"]["nodes"]) if m["id"] in mids), "—")
        print(f"   [{v['title']}] {v['sku']}  ->  {nom}")
