# Shopify Lumière Matière — état 24/08/2026

**Store :** `nzefxg-gg.myshopify.com`  
**Admin :** https://admin.shopify.com/store/nzefxg-gg  
**Compte API :** `contact@lumierematiere.fr` (auth CLI `shopify store auth`)  
**Thème travail (non publié) :** `Lumière Matière — UNIVERS` · `gid://shopify/OnlineStoreTheme/186708066640`  
**Thème live :** Horizon (rôle MAIN) — **ne pas écrire dessus** ; Hakim publie la copie.

## Fait (API)

- Pages : Notre histoire, FAQ, Contact, Paiement
- Policies : CGV, retours, livraison, mentions légales
- 14 collections (13 matières/formes + `selection-199`), covers Codex (échange salon ↔ plafonniers)
- Menus : `main-menu` (matière-first), `footer`, `footer-legal`
- Tokens DA + logos + bandeau + hero + grilles collections + bande 199 € sur le thème **non publié**
- Import catalogue **121/121** (LM-086 DRAFT, 0 image — REJECT QA)
- Tokens DA + logos + bandeau + hero + grilles collections + bande 199 € sur le thème **non publié**

## À faire Hakim (admin, 5 min)

1. **Renommer la boutique** « Ma boutique » → **Lumière Matière** (Réglages → Général — l’API refuse le rename).
2. **Adresse** : passer 13 Allée Georges Brassens (Saint-Prix) → **47 rue Vivienne, 75002 Paris** + tél `+33 7 56 82 80 94`.
3. **Politique confidentialité** : désactiver la gestion automatique Shopify, puis relancer `python3 catalogues/lumierematiere/shopify/bootstrap_pages.py` (ou coller `pages/politique-confidentialite.md`).
4. **Prévisualiser** le thème « Lumière Matière — UNIVERS » **avant de publier**.
5. Brancher **lumierematiere.fr** (identité boutique).
6. DSers : installer + mapper les variantes **UE en priorité** une fois les 121 fiches là.

## Scripts (repo)

`catalogues/lumierematiere/shopify/` — token lu dans l’auth CLI, jamais stocké.
