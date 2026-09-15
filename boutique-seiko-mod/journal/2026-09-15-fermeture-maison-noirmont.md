---
type: journal
boutique: seiko-mod
date: 2026-09-15
nature: decision
leviers: [conformite, strategie]
titre: "Fermeture de Maison Noirmont — boutique, Google Ads et Merchant Center"
---

# Fermeture de Maison Noirmont — 15/09/2026

**Décision de Hakim, exécutée par lui le 15/09/2026** : boutique Shopify désactivée, compte Google
Ads fermé, compte Merchant Center **5840460291** fermé. Le parc en ligne est désormais
**Tuftéo et Bonum Vitae**.

## Ce qui s'est passé

1. Ban GMC « Déclarations trompeuses ou déceptives » le **23/08**.
2. Passes de correction les 23, 30 et 31/08, puis les 1er et 2/09 : marques tierces (Seiko,
   Président, Miyota, Jubilé, Explorateur), options fournisseur (`Ships From : China Mainland`),
   délais contradictoires, policies, JSON-LD, Klarna promis mais absent du checkout.
   Audit §6 complet au 02/09 au soir.
3. Demande de réexamen après la fenêtre de 7–10 jours : **déban obtenu**.
4. **Nouvelle suspension trois jours plus tard.** Motif exact et dates précises non relevés dans
   le dépôt.
5. Fermeture le 15/09.

## Pourquoi, selon Hakim

- **Marché de la montre saturé.**
- **Marché risqué** : la qualité n'est pas forcément au rendez-vous à la livraison.
- **Exposition forte aux rétrofacturations** (chargebacks) qui en découle.
- Choix de couper et de concentrer l'effort sur les boutiques restantes.

## Ce que l'épisode apprend

**Un déban n'est pas une validation.** Le skill `gmc-acceptance` place déjà la fenêtre de risque
principale **après** l'approbation (« 30 j — suspensions surtout après approbation »). Noirmont l'a
vérifié en trois jours. Tout le travail de conformité a obtenu le réexamen ; il n'a pas rendu le
compte durable.

**Hypothèse, non confirmée par Google** : sur un catalogue de montres « mod » et hommage, le risque
de déclaration trompeuse tient au **dessin du produit** autant qu'au texte — lunette cannelée,
bracelet cinq rangs, cadran 3-6-9, GMT bicolore évoquent des modèles de marque même une fois tous
les noms purgés. Une purge de nomenclature corrige le texte ; elle ne change pas ce que montrent
les photos. Si cette lecture est juste, le risque était **structurel à la catégorie**, et aucun
audit de boutique ne pouvait le lever. À garder comme critère d'écartement possible en recherche
produit : *catégorie dont les produits évoquent visuellement une marque établie*. Non promu en
règle sans accord de Hakim.

## Ce qui reste à surveiller après la fermeture

Non vérifié dans le dépôt, listé pour mémoire :
- boîte `contact@maisonnoirmont.fr` : à garder quelques mois (notifications Google et Shopify) ;
- renouvellement automatique du domaine `maisonnoirmont.fr` (AFNIC, créé le 24/07/2026) ;
- facture Shopify et dernière facture Google Ads ;
- demande Klarna restée en attente au moment de la fermeture ;
- profil Chrome « Noirmont » et compte Google associé : à conserver le temps des dernières
  notifications.

La suspension reste attachée à l'entité OH Ventures après la fermeture du compte : ne jamais
rouvrir un Merchant Center pour ce domaine ou ce catalogue.

## Références

- `journal/2026-08-23-corrections-gmc-misrepresentation.md` — le ban initial
- `journal/2026-09-01-audit-post-ban-verification.md`, `…-passe-correction-jubile-options.md`,
  `…-explorateur-devient-repere.md` — les passes de septembre
- `journal/2026-09-02-klarna-promesse-sans-checkout.md` — la dernière contradiction
- `.claude/skills/gmc-acceptance/references/audit-lecons-noirmont.md` (hub) — les leçons, qui
  restent valables pour les autres boutiques
