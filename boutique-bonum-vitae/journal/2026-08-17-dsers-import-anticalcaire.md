# 17/08/2026 (nuit) — Import DSers des anti-calcaire électroniques (T-H8)

> Consigne Hakim : « les deux partent en DSers », ouverture via Admin Shopify → Applications →
> DSers. Fait au navigateur (Chrome de Hakim, permission remote debugging accordée). SSO DSers
> vérifié : `contact@bonumvitae.fr` / `seller_id=kw7vak-g0` — le bon compte.

## Résultat

### Candidat 1 (`1005008632801588`, électronique à impulsions) — DÉJÀ EN BOUTIQUE

En ouvrant la liste d'import, la carte « Electronic Water Descaler… Cost $32.56 » était **déjà
présente et déjà poussée vers 1 boutique**. Identification certaine : stock affiché **2085** =
somme exacte des 4 SKU relevés à l'API (943+447+300+395). **C'est le fournisseur d'une des fiches
« Dispositif anti-tartre électronique USB » importées en juillet.** Le sourcing du soir a reconvergé
sur un produit qu'on vend déjà — aucune action DSers nécessaire, pas de doublon créé.

Conséquence pour T-H8 : la « nouveauté » électronique n'en est pas une ; la vraie décision est le
**prix** de la fiche existante (86,90-98,90 € actuels pour ~30 € de coût) et son positionnement.

### Candidat 2 (`1005006005109143`, LPS toute-maison) — IMPORTÉ ET POUSSÉ EN BROUILLON ✅

1. URL ajoutée à la liste d'import (champ React — saisie par setter natif + événement `input`).
2. Poussée vers **kw7vak-g0 uniquement** (l'ancienne boutique morte `solinvictuss.myshopify.com`,
   encore liée au compte DSers, est restée décochée ; sa modale « RELINK » a été fermée par Ok).
3. **Case « Set product status as Draft » : décochée par défaut, cochée, vérifiée 3 fois** avant la
   poussée (piège documenté du campement — confirmé une fois de plus).
4. Constaté API Shopify : produit **DRAFT** créé à 19:30:47Z — « LPS Whole House Scale Inhibition
   Inline Water Softener System Descaler ». Catalogue : 27 produits.
5. **DSers a poussé un `compareAtPrice` égal au prix (65,10 €)** — purgé immédiatement
   (`productVariantsBulkUpdate`, 0 erreur). Règle zéro barré tenue.

**Données fret relevées dans la poussée : coût produit 65,10 €, expédition France 0,00 € — coût
rendu 65,10 €** (classe A, écran DSers). Au prix cible évoqué (179-229 €), marge brute 64-72 %.

## Reste à faire sur la fiche LPS (avant toute activation)

- Titre/description en anglais fournisseur → à réécrire (persona, vouvoiement, sans claim
  d'efficacité : « dispositif d'appoint », jamais « adoucit l'eau »).
- **Photos = brutes fournisseur, dont un logo « GERMAN Filters Technology » visible sur la
  première image** → visuels composés obligatoires, contrôle marque tierce à faire (règle maison :
  jamais de photo AliExpress brute, et le logo tiers peut disqualifier des visuels).
- Prix de vente à fixer (T-H8) ; mapping DSers déjà en place par l'import.
- Ne pas publier sur Boutique en ligne / Google & YouTube avant validation.

## T-H6 — GMC

Hakim, 17/08 : **a priori aucun compte GMC** pour Bonum Vitae. Noté comme déclaratif (pas de
vérification admin canaux ce soir). Conséquence : le futur passage FullStack ne « brutalise » aucun
compte établi ; le GMC se créera selon la checklist, après boutique propre, sur feu vert Hakim.
