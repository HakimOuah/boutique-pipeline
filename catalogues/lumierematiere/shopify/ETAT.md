# Shopify Lumière Matière — état 24/08/2026 (soir)

**Store :** `nzefxg-gg.myshopify.com`  
**Admin :** https://admin.shopify.com/store/nzefxg-gg  
**Compte API :** `contact@lumierematiere.fr` (auth CLI `shopify store auth`)  
**Thème de travail (non publié) :** `copie-de-fullstack-2-3` · `gid://shopify/OnlineStoreTheme/186708001104`  
**Prévisualisation :** https://nzefxg-gg.myshopify.com/?preview_theme_id=186708001104  
**Ne pas écrire** sur Horizon (rôle MAIN) ni publier. Hakim publie.

## Fait

- **Policies** collées depuis le pack FR `gmc-acceptance/templates-fr/` (24/08), reformulées pour LM (texte distinct d’Orysbain). Chiffres ops : cut-off **16h Paris**, préparation **1–2 j**, acheminement **6–15 j**, total **7–17 j**, retours **30 j**, annulation **tant que non expédiée**, SAV **10h–18h**, réponse **24 h ouvrées**. Confidentialité OK (gestion auto désactivée).
- **121 fiches API supprimées** (0 produit Shopify). Elles n’étaient liées à aucun compte DSers.
- **Thème Full Stack** (`copie-de-fullstack-2-3`) : tokens papier `#F6F3EC` / charbon `#24211B` / ambre `#C08A2D`, Young Serif + Instrument Sans, logos, homepage UNIVERS (6 matières + 3 pièces + sélection 199 €), bandeau vérifiable, footer OH Ventures. Démos avis / Trustpilot / « 96 % » / « 3x cadeau » retirées. Icônes de paiement **auto** (Shop Pay non forcé). PDP : faux 4,5/123, lorem, horaires 8h30–19h et « livraison rapide » corrigés.
- **DSers Import List : 120 / 121** URLs AliExpress importées sur le store `nzefxg-gg` (langue EN : le FR déclenche un upgrade payant). **LM-045** (`1005012474741970`, suspension effet pierre) : listing AliExpress mort (`product status error`). Fichier : `shopify/dsers-urls.txt`.

## DSers — bloqué sur le plan (Hakim)

L’essai affiche encore **14 j / 5 SKU à 1,99 $ / 20 SKU à 6,99 $**. **Ne pas souscrire sans Hakim.**  
**Ne pas PUSH TO STORE** tant que le quota n’autorise pas 120 fiches — sinon le mapping s’arrête à 5 ou 20.

Après upgrade : PUSH en brouillon (`backend_only`, aucun canal), overlay titres/prix/descriptions/images Codex (hors LM-086 REJECT), collections UNIVERS, `publishablePublish` Online Store. Préférer les variantes **entrepôt UE**. 5 fiches « Unmapped » dans My Products = fantômes des fiches API, à supprimer.

## À faire Hakim

1. Adresse boutique : 47 rue Vivienne, 75002 Paris (encore Saint-Prix).
2. Choisir / activer le **plan DSers** pour 120+ SKU, puis PUSH.
3. Brancher **lumierematiere.fr**.
4. Activer la caisse (checkout encore disabled — policy paiement = Visa / Mastercard seulement).
5. Prévisualiser `copie-de-fullstack-2-3` **avant de publier**.
6. CM2C : ajouter lumierematiere.fr si le contrat est par site.
7. Décider du sort de **LM-045** (listing AE mort) : retirer du catalogue ou sourcer un remplaçant.
