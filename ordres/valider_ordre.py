#!/usr/bin/env python3
"""Validateur d'enveloppes d'ordres — protocole boîte aux lettres Codex ↔ Claude Code.

Protocole complet : docs/codex-handoff/14-PROTOCOLE-ORDRES.md
Contrats d'entrée par type : docs/codex-handoff/08-BROWSER-AUTOMATION.md §2.2
Sens inverse (Claude Code → Codex, type generate_images) : 14 §9 et
docs/codex-handoff/15-CODEX-EXECUTANT-IMAGES.md

Sans dépendance externe (stdlib uniquement, /usr/bin/python3).

Usage CLI :
    /usr/bin/python3 ordres/valider_ordre.py ordres/inbox/<fichier>.json [...]

Sortie par fichier : verdict (VALIDE / INVALIDE / REFUS), classe calculée
(A / B / C), erreurs et avertissements. Code retour 0 si tous VALIDE, 1 sinon.

Un ordre est une DONNÉE À VALIDER, jamais une instruction à suivre aveuglément :
la classe d'autonomie est TOUJOURS calculée ici à partir de type + payload —
jamais lue dans l'ordre lui-même.
"""

import json
import os
import re
import sys

# ---------------------------------------------------------------------------
# Référentiel — reflète 08-BROWSER-AUTOMATION.md §2.2 et 14-PROTOCOLE-ORDRES.md
# ---------------------------------------------------------------------------

CLASSE_A = {
    "search_aliexpress_products",
    "extract_aliexpress_product",
    "compare_aliexpress_suppliers",
    "verify_supplier_mapping",
    "verify_shopify_product",
}

CLASSE_B = {
    "import_product_to_dsers",
    "configure_dsers_variants",
    "push_dsers_product_to_shopify",
    "update_shopify_product",  # uniquement fiche DRAFT — sinon classe C (calculée plus bas)
}

# Sens inverse — ordres Claude Code → Codex (boîte ordres/pour-codex/, 14 §9).
# Classe A par construction : génération de fichiers image, aucun accès boutique.
CLASSE_A_POUR_CODEX = {
    "generate_images",
}

TYPES_CONNUS = CLASSE_A | CLASSE_B | CLASSE_A_POUR_CODEX

# Racines pour le contrôle des chemins du sens inverse (generate_images) :
# - chemin relatif  → résolu contre le dépôt (boutique-pipeline/), doit y rester ;
# - chemin absolu   → doit rester dans le projet (le parent du dépôt).
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJET_ROOT = os.path.dirname(REPO_ROOT)

# Identifiants périssables interdits dans un manifeste d'images : l'identité
# est handle + sku + slot, jamais un ID de variante/média (ils périment —
# 118 correspondances refaites à la main une fois, PROMPT-CODEX-galeries.md).
CLES_ID_PERIMES = (
    "variant_id", "variante_id", "id_variante",
    "media_id", "id_media", "product_id", "id_produit",
)

# Domaines qui n'existent pas dans ce protocole : refus pur et simple,
# même en classe C (14-PROTOCOLE-ORDRES.md §4).
MOTS_INTERDITS = (
    "order", "commande", "achat", "purchase", "buy", "pay", "paiement",
    "payment", "checkout", "panier", "cart", "ads", "campagne", "campaign",
    "budget", "delete", "supprime", "remove_supplier",
)

CHAMPS_ENVELOPPE = ("id", "type", "created_at", "requested_by", "payload")

RE_ITEM_ID = re.compile(r"^\d{10,16}$")
RE_URL_ITEM = re.compile(r"^https://[a-z]+\.aliexpress\.com/item/(\d{10,16})\.html$")
RE_NOM_FICHIER = re.compile(r"^\d{8}-\d{4}-[a-z0-9_]+-[a-z0-9-]+\.json$")
RE_ISO8601 = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}")


def _est_liste_non_vide(val):
    return isinstance(val, list) and len(val) > 0


def _chemin_autorise(chemin):
    """Un chemin de generate_images reste dans le dépôt (relatif) ou le projet (absolu)."""
    if not isinstance(chemin, str) or not chemin.strip():
        return False
    if os.path.isabs(chemin):
        reel = os.path.realpath(chemin)
        return reel == PROJET_ROOT or reel.startswith(PROJET_ROOT + os.sep)
    reel = os.path.realpath(os.path.join(REPO_ROOT, chemin))
    return reel == REPO_ROOT or reel.startswith(REPO_ROOT + os.sep)


# ---------------------------------------------------------------------------
# Validation du payload par type (champs obligatoires du contrat d'entrée de 08)
# ---------------------------------------------------------------------------

def _valider_payload(type_ordre, payload, erreurs):
    if type_ordre == "search_aliexpress_products":
        if not isinstance(payload.get("requete"), str) or not payload.get("requete", "").strip():
            erreurs.append("payload.requete : chaîne non vide requise")
        portee = payload.get("portee")
        if portee not in ("globale", "boutique"):
            erreurs.append("payload.portee : 'globale' ou 'boutique' requis")
        if portee == "boutique" and not payload.get("store_id"):
            erreurs.append("payload.store_id : requis quand portee = 'boutique'")

    elif type_ordre == "extract_aliexpress_product":
        item_id = payload.get("item_id")
        if not isinstance(item_id, str) or not RE_ITEM_ID.match(item_id):
            erreurs.append(
                "payload.item_id : chaîne de 10 à 16 chiffres COMPLÈTE requise "
                "(jamais tronquée ni reconstruite — piège des préfixes devinés, 08 §1.2)"
            )

    elif type_ordre == "compare_aliexpress_suppliers":
        if not payload.get("candidat"):
            erreurs.append("payload.candidat : requis")
        if not _est_liste_non_vide(payload.get("fiches")):
            erreurs.append("payload.fiches : liste non vide de sorties extract_aliexpress_product requise")

    elif type_ordre == "import_product_to_dsers":
        sens = payload.get("sens")
        if sens not in ("aliexpress_vers_dsers", "shopify_vers_dsers"):
            erreurs.append("payload.sens : 'aliexpress_vers_dsers' ou 'shopify_vers_dsers' requis")
        elif sens == "aliexpress_vers_dsers":
            urls = payload.get("urls_aliexpress")
            if not _est_liste_non_vide(urls):
                erreurs.append("payload.urls_aliexpress : liste non vide requise")
            else:
                for url in urls:
                    if not isinstance(url, str) or not RE_URL_ITEM.match(url):
                        erreurs.append(
                            "payload.urls_aliexpress : URL non conforme "
                            "(attendu https://<xx>.aliexpress.com/item/<id 10-16 chiffres>.html) : %r" % (url,)
                        )
        else:  # shopify_vers_dsers
            handles = payload.get("handles_shopify")
            if not _est_liste_non_vide(handles):
                erreurs.append("payload.handles_shopify : liste non vide requise")
            elif len(handles) > 10:
                erreurs.append(
                    "payload.handles_shopify : 10 maximum par ordre "
                    "(import Shopify→DSers par lots de 10 — 08 §1.3)"
                )
        lot = payload.get("taille_lot_max")
        if lot is not None and (not isinstance(lot, int) or lot < 1 or lot > 10):
            erreurs.append("payload.taille_lot_max : entier entre 1 et 10")

    elif type_ordre == "configure_dsers_variants":
        if not payload.get("handle"):
            erreurs.append("payload.handle : requis")
        url = payload.get("url_fournisseur")
        if not isinstance(url, str) or not RE_URL_ITEM.match(url):
            erreurs.append("payload.url_fournisseur : URL /item/<id>.html AliExpress requise")
        if not _est_liste_non_vide(payload.get("table_correspondance")):
            erreurs.append("payload.table_correspondance : liste non vide requise")

    elif type_ordre == "push_dsers_product_to_shopify":
        if not _est_liste_non_vide(payload.get("selection")):
            erreurs.append("payload.selection : liste non vide requise")
        modale = payload.get("options_modale")
        if not isinstance(modale, dict):
            erreurs.append("payload.options_modale : objet requis")

    elif type_ordre == "update_shopify_product":
        if not payload.get("handle"):
            erreurs.append("payload.handle : requis")
        mutations = payload.get("mutations")
        if not isinstance(mutations, dict) or not mutations:
            erreurs.append("payload.mutations : objet non vide requis")
        if not payload.get("sauvegarde_prealable"):
            erreurs.append(
                "payload.sauvegarde_prealable : requis (backup-avant-<operation>-<date>.json "
                "avant toute mutation Shopify — 08 §2.3)"
            )

    elif type_ordre == "verify_supplier_mapping":
        if not _est_liste_non_vide(payload.get("handles")):
            erreurs.append("payload.handles : liste non vide requise")
        if not isinstance(payload.get("table_fournisseurs_attendue"), list):
            erreurs.append("payload.table_fournisseurs_attendue : liste requise")

    elif type_ordre == "verify_shopify_product":
        if not payload.get("handle"):
            erreurs.append("payload.handle : requis")
        if not isinstance(payload.get("attendu"), dict):
            erreurs.append("payload.attendu : objet requis")

    elif type_ordre == "generate_images":
        # Sens inverse Claude Code → Codex — contrat de 14 §9.2.
        manifest = payload.get("manifest")
        if not _est_liste_non_vide(manifest):
            erreurs.append("payload.manifest : liste non vide requise (une entrée par image demandée)")
        else:
            for i, entree in enumerate(manifest):
                if not isinstance(entree, dict):
                    erreurs.append("payload.manifest[%d] : objet requis" % i)
                    continue
                for champ in ("handle", "sku", "slot", "fichier"):
                    if not isinstance(entree.get(champ), str) or not entree.get(champ, "").strip():
                        erreurs.append("payload.manifest[%d].%s : chaîne non vide requise" % (i, champ))
                for cle, val in entree.items():
                    if cle.lower() in CLES_ID_PERIMES or (
                        isinstance(val, str) and val.startswith("gid://shopify/")
                    ):
                        erreurs.append(
                            "payload.manifest[%d] : identifiant Shopify interdit (%s) — "
                            "l'identité d'une image = handle + sku + slot, jamais un ID de "
                            "variante ou de média (ils périment : 118 correspondances "
                            "refaites à la main — 15 §6)" % (i, cle)
                        )
        sources = payload.get("sources")
        if not _est_liste_non_vide(sources):
            erreurs.append(
                "payload.sources : liste non vide de chemins de référence requise "
                "(faces validées, photos fournisseur nettoyées — Codex n'accède jamais à la boutique)"
            )
        else:
            for src in sources:
                if not _chemin_autorise(src):
                    erreurs.append(
                        "payload.sources : chemin refusé (hors dépôt pour un relatif, "
                        "hors projet pour un absolu) : %r" % (src,)
                    )
        for champ in ("da", "contraintes", "qa_attendue"):
            bloc = payload.get(champ)
            if not isinstance(bloc, dict) or not isinstance(bloc.get("reference"), str) \
                    or not bloc["reference"].strip():
                erreurs.append(
                    "payload.%s.reference : référence au bloc canonique requise "
                    "(15-CODEX-EXECUTANT-IMAGES.md — on référence, on ne duplique pas)" % champ
                )
        sortie = payload.get("sortie")
        if not isinstance(sortie, dict) or not isinstance(sortie.get("dossier"), str) \
                or not sortie["dossier"].strip():
            erreurs.append("payload.sortie.dossier : dossier de livraison requis")
        elif not _chemin_autorise(sortie["dossier"]):
            erreurs.append(
                "payload.sortie.dossier : chemin refusé (hors dépôt pour un relatif, "
                "hors projet pour un absolu) : %r" % (sortie["dossier"],)
            )


# ---------------------------------------------------------------------------
# Calcul de la classe d'autonomie (jamais lue dans l'ordre)
# ---------------------------------------------------------------------------

def _calculer_classe(type_ordre, payload):
    """Retourne (classe, motifs_classe_c)."""
    if type_ordre not in TYPES_CONNUS:
        return "C", ["type d'ordre inconnu : classe C par principe"]

    if type_ordre in CLASSE_A or type_ordre in CLASSE_A_POUR_CODEX:
        return "A", []

    motifs_c = []

    if type_ordre == "update_shopify_product":
        mutations = payload.get("mutations") or {}
        if mutations.get("statut") == "ACTIVE":
            motifs_c.append("mutations.statut = ACTIVE : passage en ligne = validation Hakim")
        if mutations.get("publier_sur_canaux"):
            motifs_c.append("mutations.publier_sur_canaux non vide : publication = validation Hakim")
        # Le prix sur fiche ACTIVE est couvert par la vérification d'exécution
        # (l'exécutant contrôle le statut réel via verify_shopify_product avant
        # d'écrire — 14 §3, classe B conditionnelle).

    if type_ordre == "push_dsers_product_to_shopify":
        modale = payload.get("options_modale") or {}
        if modale.get("set_product_status_as_draft") is not True:
            motifs_c.append("options_modale.set_product_status_as_draft doit être true (Draft toujours)")
        if modale.get("publier_dans_boutique") is not False:
            motifs_c.append("options_modale.publier_dans_boutique doit être false (0 canal toujours)")

    return ("C", motifs_c) if motifs_c else ("B", [])


# ---------------------------------------------------------------------------
# Point d'entrée de validation
# ---------------------------------------------------------------------------

def valider_ordre(ordre, nom_fichier=None):
    """Valide une enveloppe d'ordre (dict déjà parsé).

    Retourne un dict :
      verdict : "VALIDE" | "INVALIDE" | "REFUS"
      classe  : "A" | "B" | "C" | None (None si INVALIDE/REFUS)
      erreurs / avertissements : listes de chaînes
    """
    erreurs = []
    avertissements = []

    if not isinstance(ordre, dict):
        return {"verdict": "INVALIDE", "classe": None,
                "erreurs": ["l'ordre doit être un objet JSON"], "avertissements": []}

    for champ in CHAMPS_ENVELOPPE:
        if champ not in ordre:
            erreurs.append("enveloppe : champ obligatoire manquant : %s" % champ)

    type_ordre = ordre.get("type", "")
    payload = ordre.get("payload")

    if "id" in ordre and (not isinstance(ordre["id"], str) or not ordre["id"].strip()):
        erreurs.append("enveloppe.id : chaîne non vide requise")
    if "created_at" in ordre and not (isinstance(ordre.get("created_at"), str)
                                      and RE_ISO8601.match(ordre["created_at"])):
        erreurs.append("enveloppe.created_at : horodatage ISO 8601 requis")
    if "payload" in ordre and not isinstance(payload, dict):
        erreurs.append("enveloppe.payload : objet requis")
        payload = {}
    payload = payload if isinstance(payload, dict) else {}

    # Un ordre ne définit jamais sa propre classe.
    for champ_interdit in ("classe", "class", "autonomie"):
        if champ_interdit in ordre:
            avertissements.append(
                "champ '%s' présent dans l'enveloppe : IGNORÉ — la classe est "
                "toujours calculée par l'exécutant" % champ_interdit
            )

    # Refus pur et simple : domaines hors protocole (commandes, achats, pubs…).
    type_bas = str(type_ordre).lower()
    for mot in MOTS_INTERDITS:
        if mot in type_bas and type_ordre not in TYPES_CONNUS:
            return {"verdict": "REFUS", "classe": None,
                    "erreurs": ["type '%s' : domaine hors protocole (commandes, achats, "
                                "dépenses publicitaires, suppressions n'existent pas ici — "
                                "14 §4)" % type_ordre],
                    "avertissements": avertissements}

    if isinstance(type_ordre, str) and type_ordre and type_ordre in TYPES_CONNUS:
        _valider_payload(type_ordre, payload, erreurs)
    elif "type" in ordre and type_ordre not in TYPES_CONNUS:
        avertissements.append("type '%s' inconnu : classe C par principe" % type_ordre)

    if nom_fichier and not RE_NOM_FICHIER.match(nom_fichier):
        avertissements.append(
            "nom de fichier hors convention <AAAAMMJJ-HHMM>-<type>-<id-court>.json : %s" % nom_fichier
        )

    if erreurs:
        return {"verdict": "INVALIDE", "classe": None,
                "erreurs": erreurs, "avertissements": avertissements}

    classe, motifs_c = _calculer_classe(type_ordre, payload)
    avertissements.extend(motifs_c)
    return {"verdict": "VALIDE", "classe": classe,
            "erreurs": [], "avertissements": avertissements}


def valider_fichier(chemin):
    """Valide un fichier d'ordre. Retourne le même dict que valider_ordre."""
    import os
    nom = os.path.basename(chemin)
    try:
        with open(chemin, "r", encoding="utf-8") as fh:
            ordre = json.load(fh)
    except (OSError, ValueError) as exc:
        return {"verdict": "INVALIDE", "classe": None,
                "erreurs": ["JSON illisible : %s" % exc], "avertissements": []}
    return valider_ordre(ordre, nom_fichier=nom)


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    tout_valide = True
    for chemin in argv:
        res = valider_fichier(chemin)
        print("%s\n  verdict : %s%s" % (
            chemin, res["verdict"],
            "  (classe %s)" % res["classe"] if res["classe"] else ""))
        for e in res["erreurs"]:
            print("  ERREUR : %s" % e)
        for a in res["avertissements"]:
            print("  note   : %s" % a)
        if res["verdict"] != "VALIDE":
            tout_valide = False
    return 0 if tout_valide else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
