"""Applique les prix cibles de l'alignement Lustria (plan du 26/08/2026).

Idempotent : chaque passe relit les prix en ligne, ne pousse que les variantes
dont le prix diffère de la cible, et ne renvoie rien si tout est déjà à sa place.

    python3 align_prices.py              # simulation, aucune écriture
    python3 align_prices.py --apply      # écrit
    python3 align_prices.py --apply --sku LM-001,LM-002
    python3 align_prices.py --restore backups/2026-08-26-prix/prix-avant-....json --apply

Périmètre d'écriture, volontairement le plus étroit possible :
`productVariantsBulkUpdate` avec `productId` + `variants: [{id, price}]`. Aucun
`compareAtPrice`, aucun SKU, aucune option, aucune variante créée ou supprimée,
aucun titre, aucune description, aucune image, aucune collection.

Les lignes « bloquées par la marge », « inchangé — déjà sous la cible » et
« aucun comparable » ne sont pas touchées.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import client

HERE = Path(__file__).resolve().parent
PLAN = HERE / "prix-alignement-plan-2026-08-26.json"
BACKUP_DIR = HERE / "backups" / "2026-08-26-prix"
JOURNAL = BACKUP_DIR / "journal.json"

DUMP = """
query($cursor: String) {
  products(first: 5, after: $cursor) {
    pageInfo { hasNextPage endCursor }
    nodes {
      id handle title status
      variants(first: 250) {
        pageInfo { hasNextPage }
        nodes { id sku title price compareAtPrice }
      }
    }
  }
}
"""

MUTATION = """
mutation($productId: ID!, $variants: [ProductVariantsBulkInput!]!) {
  productVariantsBulkUpdate(productId: $productId, variants: $variants) {
    productVariants { id price }
    userErrors { field message }
  }
}
"""


def dump_live() -> list[dict]:
    produits, cursor = [], None
    while True:
        conn = client.gql(DUMP, {"cursor": cursor})["products"]
        for node in conn["nodes"]:
            if node["variants"]["pageInfo"]["hasNextPage"]:
                raise RuntimeError(f"{node['handle']}: >250 variantes")
            produits.append(node)
        if not conn["pageInfo"]["hasNextPage"]:
            break
        cursor = conn["pageInfo"]["endCursor"]
    return produits


def sauvegarde(produits: list[dict]) -> Path:
    """Sauvegarde intégrale des prix AVANT toute écriture. Jamais écrasée.

    Une sauvegarde déjà présente et identique est réutilisée : relancer le script
    n'accumule pas de copies du même état.
    """
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    charge = [{
        "id": p["id"], "handle": p["handle"], "title": p["title"], "status": p["status"],
        "variants": [{"id": v["id"], "sku": v["sku"], "title": v["title"],
                      "price": v["price"], "compareAtPrice": v["compareAtPrice"]}
                     for v in p["variants"]["nodes"]],
    } for p in produits]
    texte = json.dumps(charge, ensure_ascii=False, indent=1)
    empreinte = hashlib.sha256(texte.encode()).hexdigest()
    for connu in sorted(BACKUP_DIR.glob("prix-*.json")):
        if hashlib.sha256(connu.read_text(encoding="utf-8").encode()).hexdigest() == empreinte:
            return connu
    horodatage = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    chemin = BACKUP_DIR / f"prix-avant-{horodatage}.json"
    chemin.write_text(texte, encoding="utf-8")
    return chemin


def cible_par_variante(ligne: dict) -> dict[str, str]:
    """Mappe chaque variante sur son prix cible, palier par palier.

    Les paliers de taille gardent leur écart relatif : `paliers_cibles` est déjà
    calculé dans le plan, aligné position par position sur `paliers`.
    """
    paliers = [float(p) for p in ligne["paliers"]]
    cibles = ligne["paliers_cibles"]
    if len(paliers) != len(cibles):
        raise RuntimeError(f"{ligne['sku']}: {len(paliers)} paliers, {len(cibles)} cibles")
    table = {p: c for p, c in zip(paliers, cibles)}
    return {v["id"]: f"{table[v['price']]:.2f}" for v in ligne["variants"]}


def restaure(chemin: Path, appliquer: bool) -> None:
    """Remet les prix d'une sauvegarde. Même périmètre d'écriture que l'aller."""
    ref = {p["id"]: p for p in json.loads(chemin.read_text(encoding="utf-8"))}
    live = {p["id"]: p for p in dump_live()}
    n = 0
    for pid, p in ref.items():
        actuel = live.get(pid)
        if actuel is None:
            print(f"  absent en ligne : {p['handle']}")
            continue
        prix_ref = {v["id"]: v["price"] for v in p["variants"]}
        a_pousser = [{"id": v["id"], "price": prix_ref[v["id"]]}
                     for v in actuel["variants"]["nodes"]
                     if v["id"] in prix_ref and v["price"] != prix_ref[v["id"]]]
        if not a_pousser:
            continue
        print(f"  {'RESTAURE' if appliquer else 'SIMU    '} {p['handle']} "
              f"({len(a_pousser)} variantes)")
        if appliquer:
            data = client.gql(MUTATION, {"productId": pid, "variants": a_pousser})
            erreurs = data["productVariantsBulkUpdate"]["userErrors"]
            if erreurs:
                raise RuntimeError(f"{p['handle']} : {json.dumps(erreurs, ensure_ascii=False)}")
        n += 1
    print(f"{n} fiches {'restaurees' if appliquer else 'a restaurer'} depuis {chemin.name}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="écrit ; sinon simulation")
    ap.add_argument("--sku", help="liste de SKU séparés par des virgules")
    ap.add_argument("--restore", metavar="FICHIER",
                    help="remet les prix d'une sauvegarde de backups/2026-08-26-prix/")
    args = ap.parse_args()

    if args.restore:
        restaure(Path(args.restore), args.apply)
        return

    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    a_baisser = [l for l in plan["lignes"] if l["decision"] == "baisse"]
    if args.sku:
        garde = {s.strip() for s in args.sku.split(",")}
        a_baisser = [l for l in a_baisser if l["sku"] in garde]

    print(f"plan : {len(plan['lignes'])} fiches, {len(a_baisser)} a baisser")
    for etat, libelle in (("bloque_marge", "bloquees par la marge"),
                          ("inchange_deja_sous_cible", "deja sous la cible"),
                          ("inchange_sans_comparable", "sans comparable")):
        n = sum(1 for l in plan["lignes"] if l["decision"] == etat)
        print(f"       {n:3d} {libelle} — non touchees")

    produits = dump_live()
    par_id = {p["id"]: p for p in produits}
    chemin = sauvegarde(produits)
    print(f"sauvegarde : {chemin.relative_to(HERE)} "
          f"({len(produits)} produits, {sum(len(p['variants']['nodes']) for p in produits)} variantes)")

    # Garde-fou : le plan a été calculé sur un dump du 26/08. Si un prix en ligne
    # a bougé depuis, on ne touche pas la fiche — un autre agent est peut-être
    # passé dessus.
    total_ecrit = total_deja = 0
    ignorees: list[str] = []
    journal: list[dict] = []

    for ligne in sorted(a_baisser, key=lambda l: l["sku"]):
        produit = par_id.get(ligne["product_id"])
        if produit is None:
            ignorees.append(f"{ligne['sku']} : produit absent en ligne")
            continue
        live = {v["id"]: v for v in produit["variants"]["nodes"]}
        attendu = {v["id"]: v["price"] for v in ligne["variants"]}
        if set(live) != set(attendu):
            ignorees.append(f"{ligne['sku']} : jeu de variantes different du plan")
            continue
        derive = [vid for vid, prix in attendu.items() if float(live[vid]["price"]) != prix]
        cibles = cible_par_variante(ligne)
        if derive and any(float(live[vid]["price"]) != float(cibles[vid]) for vid in derive):
            ignorees.append(f"{ligne['sku']} : prix en ligne modifie depuis le plan")
            continue

        a_pousser = [{"id": vid, "price": prix} for vid, prix in cibles.items()
                     if float(live[vid]["price"]) != float(prix)]
        if not a_pousser:
            total_deja += 1
            continue

        av = " / ".join(str(int(p)) for p in ligne["paliers"])
        apres = " / ".join(str(p) for p in ligne["paliers_cibles"])
        marque = "ECRIT" if args.apply else "SIMU "
        print(f"  {marque} {ligne['sku']} {av} -> {apres} € "
              f"({len(a_pousser)}/{len(cibles)} variantes) {ligne['handle']}")

        if args.apply:
            data = client.gql(MUTATION, {"productId": ligne["product_id"],
                                         "variants": a_pousser})
            erreurs = data["productVariantsBulkUpdate"]["userErrors"]
            if erreurs:
                raise RuntimeError(f"{ligne['sku']} : {json.dumps(erreurs, ensure_ascii=False)}")
        total_ecrit += 1
        journal.append({
            "sku": ligne["sku"], "handle": ligne["handle"],
            "paliers_avant": [int(p) for p in ligne["paliers"]],
            "paliers_apres": ligne["paliers_cibles"],
            "variantes_modifiees": len(a_pousser),
            "comparable": ligne["comparable_h"],
            "comparable_mediane": ligne["comparable_med"],
            "marge_ht_avant": ligne["marge_avant"],
            "marge_ht_apres": ligne["marge_apres"],
        })

    print()
    print(f"{'ecrites' if args.apply else 'a ecrire'} : {total_ecrit} fiches")
    print(f"deja a la cible  : {total_deja} fiches")
    if ignorees:
        print(f"ignorees ({len(ignorees)}) :")
        for m in ignorees:
            print(f"  - {m}")

    if args.apply:
        JOURNAL.write_text(json.dumps({
            "applique_le": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "sauvegarde": chemin.name,
            "fiches_ecrites": total_ecrit,
            "fiches_deja_a_la_cible": total_deja,
            "ignorees": ignorees,
            "detail": journal,
        }, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"journal : {JOURNAL.relative_to(HERE)}")
    else:
        print("simulation — relancer avec --apply pour ecrire")


if __name__ == "__main__":
    main()
