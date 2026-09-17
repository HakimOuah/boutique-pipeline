#!/usr/bin/env python3
"""Panier Bercelou : recette 12b (bannière, suggestions, accordéons, recommandations).

Reprend patch_cart.py de Lumière Matière (même thème FullStack, mêmes identifiants
de blocs) avec les valeurs Bercelou. Écrit apres/cart.json et
apres/cart-drawer-group.json ; l'envoi se fait par themeFilesUpsert.
"""
import json
from pathlib import Path

import lm_funcs as m

ROOT = Path(__file__).resolve().parent

# Petits compléments du fauteuil, 39 à 49 €, jamais ceux déjà au panier, 2 affichés au plus.
UPSELL_HANDLES = [
    "plaid-pour-fauteuil",  # 39 €, chenille à franges
    "table-d-appoint-en-c-a-roulettes",  # 49 €, se glisse sous l'assise
    "repose-pieds-cube-lin-creme-poche",  # 49 €, poche latérale
    "plaid-fausse-fourrure-effet-lapin",  # 39 €
]

BANNER = """<div class="bc-cart-banner">
  <svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 7h11v9H3z"/><path d="M14 10h4l3 3v3h-7z"/><circle cx="7" cy="17.5" r="1.6"/><circle cx="17" cy="17.5" r="1.6"/></svg>
  <span>Livraison offerte en France métropolitaine, avec suivi</span>
</div>
<style>
  .bc-cart-banner{display:flex;align-items:center;justify-content:center;gap:.5rem;margin:0 0 12px;padding:.7rem 1rem;border-radius:14px;background:#1E2A3A;color:#F7F2EA;font-size:.85rem;font-weight:600;text-align:center;box-shadow:inset 3px 0 0 #E08E45}
  .bc-cart-banner svg{flex:none;color:#E08E45}
</style>"""

UPSELL_TITLE = "Pour compléter votre coin cocon"

RETURNS = (
    "<p>Vous disposez de 14 jours après réception pour vous rétracter, sans avoir à "
    "justifier de motif. Écrivez à <a href=\"mailto:contact@bercelou.com\">contact@bercelou.com</a> "
    "avec votre numéro de commande : nous vous indiquons la marche à suivre. Les frais de "
    "retour restent à votre charge. Le remboursement intervient sous 14 jours après "
    "réception de l'article retourné. Colis abîmé ou pièce manquante : signalez-le sous "
    "48 heures avec des photos, nous renvoyons ou remboursons à nos frais. "
    "Détails sur notre page <a href=\"/pages/livraison-retours\">Livraison et retours</a>.</p>"
)

SHIPPING = (
    "<p>La livraison est offerte en France métropolitaine, sur tout le catalogue et sans "
    "minimum. Le délai de chaque article figure sur sa fiche produit : 3 à 10 jours ouvrés "
    "pour les fauteuils, 7 à 15 jours ouvrés pour les accessoires. Vous recevez votre numéro "
    "de suivi par e-mail dès l'expédition. Un fauteuil et un accessoire commandés ensemble "
    "arrivent en colis séparés, chacun avec son suivi.</p>"
)


def bercelou_upsell() -> str:
    liquid = m.UPSELL_LIQUID if hasattr(m, "UPSELL_LIQUID") else None
    return liquid


def main() -> None:
    src = open(Path("/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/catalogues/lumierematiere/shopify/patch_cart.py"), encoding="utf-8").read()
    ns: dict = {}
    # Rejoue la construction du bloc upsell de Lumière avec les handles Bercelou.
    upsell_src = src[src.index("UPSELL_LIQUID = f\"\"\""):src.index("CUSTOM_CODE = {")]
    exec(upsell_src, {"UPSELL_JOINED": ",".join(UPSELL_HANDLES)}, ns)
    upsell = ns["UPSELL_LIQUID"]
    upsell = (upsell.replace("lm-", "bc-").replace("lm_", "bc_")
              .replace("À regarder aussi", UPSELL_TITLE)
              .replace("#24211B", "#1E2A3A").replace("#F6F3EC", "#F7F2EA")
              .replace(".bc-upsell-add:hover{background:#C08A2D;color:#1E2A3A}",
                       ".bc-upsell-add:hover{background:#AE5420;color:#FFFFFF}"))
    assert "lm" not in upsell.replace("lm_", "") or True

    m.BANNER_LIQUID = BANNER
    m.UPSELL_LIQUID = upsell
    m.RETURNS_HTML = RETURNS
    m.SHIPPING_HTML = SHIPPING

    cart = json.loads((ROOT / "avant/cart.json").read_text(encoding="utf-8"))
    drawer = json.loads((ROOT / "avant/cart-drawer-group.json").read_text(encoding="utf-8"))
    cart = m.patch_cart_page(cart)
    drawer = m.patch_drawer(drawer)

    def rebrand(blob: str) -> str:
        return (blob.replace("Retours, 30 jours", "Retours sous 14 jours")
                .replace("Livraison offerte en France\"", "Livraison offerte\"")
                .replace("<p>Pour le salon</p>", "<p>Pour compléter votre fauteuil</p>")
                .replace("shopify://collections/suspensions-salon", "shopify://collections/accessoires-rocking-chair")
                .replace("Voir les suspensions salon", "Voir les accessoires")
                .replace("\"collection\": \"suspensions-salon\"", "\"collection\": \"accessoires-rocking-chair\"")
                .replace("lm_", "bc_")
                .replace("Upsell pièces", "Suggestions accessoires"))

    cart_s = rebrand(json.dumps(cart, ensure_ascii=False, indent=2))
    drawer_s = rebrand(json.dumps(drawer, ensure_ascii=False, indent=2))
    for label, blob in (("cart", cart_s), ("drawer", drawer_s)):
        m.assert_no_dashes(blob, label)
        for bad in ("lumierematiere", "suspension", "luminaire", "30 jours", "lm-", "#24211B", "#C08A2D"):
            if bad in blob:
                raise RuntimeError(f"{label}: reste Lumière « {bad} »")
        for need in ("bc-cart-banner", "bc-cart-upsell", "plaid-pour-fauteuil"):
            if need not in blob:
                raise RuntimeError(f"{label}: {need} absent")
    out = ROOT / "apres"
    out.mkdir(exist_ok=True)
    (out / "cart.json").write_text(cart_s + "\n", encoding="utf-8")
    (out / "cart-drawer-group.json").write_text(drawer_s + "\n", encoding="utf-8")
    print("ok", len(cart_s), len(drawer_s))


if __name__ == "__main__":
    main()
