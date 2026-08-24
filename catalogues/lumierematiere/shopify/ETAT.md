# Shopify Lumière Matière — état 24/08/2026 (soir, overlay DSers)

**Store :** `nzefxg-gg.myshopify.com`  
**Admin :** https://admin.shopify.com/store/nzefxg-gg  
**Compte API :** `contact@lumierematiere.fr` (auth CLI `shopify store auth`)  
**Thème de travail (non publié) :** `copie-de-fullstack-2-3` · `gid://shopify/OnlineStoreTheme/186708001104`  
**Prévisualisation :** https://nzefxg-gg.myshopify.com/?preview_theme_id=186708001104  
**Ne pas écrire** sur Horizon (rôle MAIN) ni publier. Hakim publie.

## Fait

- **Policies** collées depuis le pack FR `gmc-acceptance/templates-fr/` (24/08), reformulées pour LM (texte distinct d’Orysbain). Chiffres ops : cut-off **16h Paris**, préparation **1–2 j**, acheminement **6–15 j**, total **7–17 j**, retours **30 j**, annulation **tant que non expédiée**, SAV **10h–18h**, réponse **24 h ouvrées**. Confidentialité OK (gestion auto désactivée).
- **121 fiches API supprimées**, puis **PUSH DSers** (Hakim). Overlay 24/08 soir :
  - **120 fiches** mappées (titres FR, HTML VOC, prix, collections UNIVERS, publiées Online Store).
  - Images Codex g1–g5 (hors **LM-086** REJECT — images DSers conservées).
  - **3 doublons DSers** passés en brouillon.
  - **LM-045** absent (listing AliExpress mort).
- **Thème Full Stack** (`copie-de-fullstack-2-3`) : tokens papier `#F6F3EC` / charbon `#24211B` / ambre `#C08A2D`, Young Serif + Instrument Sans, logos, homepage UNIVERS. Démos avis / Trustpilot retirées.

## Prix (règle maison)

Coût DSers (unité) + **2 € de fret** (quotes FR : 1,99 € / 0 €). Concurrent d’abord (grille 149 / 199 / 249 / 299), on remonte si marge HT < 40 € ou < 25 % du HT. compareAt = ×1,3 entier en 9. SKU DSers (`sku_attr`) **non modifiés**.

| Palier min TTC | SKU |
|---|---|
| 149 € | 1 (LM-062) |
| 199 € | 63 |
| 249 € | 50 |
| 299 € | 4 |
| 349 € min (csv 299, marge) | 2 (LM-070, LM-071 cristal) |

26 fiches ont plusieurs paliers selon la taille (XXL plus cher). 94 fiches = un seul prix.

## À faire Hakim

1. Prévisualiser `copie-de-fullstack-2-3` **avant de publier**.
2. Recette paiement : footer vs checkout vs `/payments/config` (caisse maintenant active — policy Visa/Mastercard à ré-auditer si wallets apparus).
3. CM2C : ajouter lumierematiere.fr si le contrat est par site.
4. Décider du sort de **LM-045** (listing AE mort).
5. 5 fiches « Unmapped » DSers (fantômes API) : à supprimer dans l’app si elles sont encore là.
