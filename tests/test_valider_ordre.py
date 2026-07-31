import copy
import json
from pathlib import Path
from ordres.valider_ordre import valider_ordre, valider_fichier

ROOT = Path(__file__).resolve().parent.parent
EXEMPLES = ROOT / "ordres/inbox/exemples"
EXEMPLES_POUR_CODEX = ROOT / "ordres/pour-codex/inbox/exemples"

EXTRACT_OK = json.loads(
    (EXEMPLES / "20260731-0900-extract_aliexpress_product-tandorio-sub.json").read_text()
)
IMPORT_OK = json.loads(
    (EXEMPLES / "20260731-0905-import_product_to_dsers-bracelet-jubile.json").read_text()
)


def test_exemple_extract_valide_classe_a():
    res = valider_ordre(EXTRACT_OK, nom_fichier="20260731-0900-extract_aliexpress_product-tandorio-sub.json")
    assert res["verdict"] == "VALIDE"
    assert res["classe"] == "A"
    assert res["erreurs"] == []


def test_exemple_import_valide_classe_b():
    res = valider_ordre(IMPORT_OK, nom_fichier="20260731-0905-import_product_to_dsers-bracelet-jubile.json")
    assert res["verdict"] == "VALIDE"
    assert res["classe"] == "B"


def test_item_id_tronque_et_champ_manquant_invalides():
    # L'exemple invalide du dossier (préfixe d'item_id) est bien rejeté.
    res = valider_fichier(str(EXEMPLES / "20260731-0910-extract_aliexpress_product-invalide.json"))
    assert res["verdict"] == "INVALIDE"
    assert any("item_id" in e for e in res["erreurs"])
    # Champ d'enveloppe obligatoire manquant.
    bad = copy.deepcopy(EXTRACT_OK)
    del bad["created_at"]
    res2 = valider_ordre(bad)
    assert res2["verdict"] == "INVALIDE"
    assert any("created_at" in e for e in res2["erreurs"])


def test_update_shopify_active_ou_publication_classe_c():
    ordre = {
        "id": "codex-test-c",
        "type": "update_shopify_product",
        "created_at": "2026-07-31T09:00:00Z",
        "requested_by": "codex",
        "payload": {
            "handle": "eclaireur-bronze-field-36",
            "mutations": {"statut": "ACTIVE", "publier_sur_canaux": ["358599295314"]},
            "sauvegarde_prealable": "backup-avant-test-2026-07-31.json",
        },
    }
    res = valider_ordre(ordre)
    assert res["verdict"] == "VALIDE"
    assert res["classe"] == "C"
    # La même mutation sans passage ACTIVE ni publication reste classe B.
    ordre_b = copy.deepcopy(ordre)
    ordre_b["payload"]["mutations"] = {"editorial": {"titre": "Nouveau titre"}}
    assert valider_ordre(ordre_b)["classe"] == "B"


def test_type_inconnu_classe_c_et_commande_refusee():
    inconnu = {
        "id": "codex-test-x",
        "type": "fonction_future_inconnue",
        "created_at": "2026-07-31T09:00:00Z",
        "requested_by": "codex",
        "payload": {},
    }
    res = valider_ordre(inconnu)
    assert res["verdict"] == "VALIDE"
    assert res["classe"] == "C"
    # Les domaines commande/achat/pub n'existent pas dans le protocole : REFUS.
    commande = copy.deepcopy(inconnu)
    commande["type"] = "place_order_aliexpress"
    res2 = valider_ordre(commande)
    assert res2["verdict"] == "REFUS"
    assert res2["classe"] is None
    # Un champ "classe" fourni par l'ordre est ignoré (jamais obéi).
    triche = copy.deepcopy(EXTRACT_OK)
    triche["classe"] = "A"
    res3 = valider_ordre(triche)
    assert res3["verdict"] == "VALIDE"
    assert any("IGNOR" in a for a in res3["avertissements"])


# --------------------------------------------------------------------------
# Sens inverse Claude Code → Codex : type generate_images (14 §9, doc 15)
# --------------------------------------------------------------------------

GEN_OK = json.loads(
    (EXEMPLES_POUR_CODEX / "20260731-1200-generate_images-explorateur-variantes.json").read_text()
)


def test_generate_images_exemple_valide_classe_a():
    res = valider_ordre(
        GEN_OK, nom_fichier="20260731-1200-generate_images-explorateur-variantes.json"
    )
    assert res["verdict"] == "VALIDE"
    assert res["classe"] == "A"
    assert res["erreurs"] == []


def test_generate_images_chemins_hors_depot_ou_projet_refuses():
    # Chemin absolu hors projet : refusé.
    bad = copy.deepcopy(GEN_OK)
    bad["payload"]["sources"] = ["/tmp/photos-fournisseur/ref.jpg"]
    res = valider_ordre(bad)
    assert res["verdict"] == "INVALIDE"
    assert any("sources" in e and "refus" in e for e in res["erreurs"])
    # Chemin relatif qui s'échappe du dépôt : refusé aussi.
    bad2 = copy.deepcopy(GEN_OK)
    bad2["payload"]["sources"] = ["../../ailleurs/ref.jpg"]
    assert valider_ordre(bad2)["verdict"] == "INVALIDE"
    # Même règle sur le dossier de sortie.
    bad3 = copy.deepcopy(GEN_OK)
    bad3["payload"]["sortie"]["dossier"] = "/var/livraison-images"
    assert valider_ordre(bad3)["verdict"] == "INVALIDE"


def test_generate_images_id_variante_ou_media_interdits_et_champs_requis():
    # Un ID de variante dans le manifeste : invalide (identité = handle + sku + slot).
    bad = copy.deepcopy(GEN_OK)
    bad["payload"]["manifest"][0]["variant_id"] = "54130353340754"
    res = valider_ordre(bad)
    assert res["verdict"] == "INVALIDE"
    assert any("identifiant Shopify interdit" in e for e in res["erreurs"])
    # Un gid Shopify en valeur : invalide aussi.
    bad2 = copy.deepcopy(GEN_OK)
    bad2["payload"]["manifest"][1]["ref"] = "gid://shopify/ProductVariant/54130353340754"
    assert valider_ordre(bad2)["verdict"] == "INVALIDE"
    # Les blocs référencés (da/contraintes/qa_attendue) sont obligatoires.
    bad3 = copy.deepcopy(GEN_OK)
    del bad3["payload"]["qa_attendue"]
    res3 = valider_ordre(bad3)
    assert res3["verdict"] == "INVALIDE"
    assert any("qa_attendue" in e for e in res3["erreurs"])
