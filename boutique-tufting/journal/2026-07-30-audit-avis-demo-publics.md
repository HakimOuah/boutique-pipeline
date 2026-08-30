---
type: journal
boutique: tufting
date: 2026-07-30
nature: analyse
leviers: [conformite]
titre: "Audit P0 — avis de démonstration rendus publics sur Tuftéo"
---

# Audit P0 — avis de démonstration rendus publics sur Tuftéo

> Audit en lecture seule effectué le **2026-07-30 à 23:35 (Europe/Lisbon)** sur `https://tufteo.com/` et `https://tufteo.com/products/kit-tufting-complet`.
> Aucune connexion, aucune écriture Shopify, aucune modification d'avis et aucune action Trustoo. [FAIT — navigateur public + HTTP public]

## Verdict

**P0 NON CONFORME — la purge documentée comme obligatoire avant publication n'a pas été faite.** Les six avis explicitement marqués fictifs dans `project-state.md` sont servis sur le site public, avec le libellé « Vérifié ». [FAIT — repo:`boutique-tufting/project-state.md` §22/07 + navigateur public 2026-07-30]

La fiche du kit et la home servent également un badge « Excellent — 4,8/5 basé sur 789 avis ». Le journal local documente ce badge comme placeholder et un import Trustoo de 169 avis, pas 789 : le chiffre 789 est donc une preuve sociale non étayée dans les sources locales. [FAIT — repo:`boutique-tufting/project-state.md` §21/07 et §23/07 + HTTP public 2026-07-30]

## Observé

### Home

URL : `https://tufteo.com/`

- Camille R. — « Mon premier tapis, enfin accroché ! » — « Vérifié ». [FAIT — navigateur public]
- Léa M. — « Parfait pour débuter sans se tromper » — « Vérifié ». [FAIT — navigateur public]
- Sarah D. — « Très bon kit, prévois ton cadre » — « Vérifié ». [FAIT — navigateur public]
- Le HTML public sans cookie contient aussi « Excellent » et « 789 avis ». [FAIT — HTTP public, réponse 200]

### Fiche produit

URL : `https://tufteo.com/products/kit-tufting-complet`

- Manon T. — « La tondeuse fait toute la différence » — « Vérifié ». [FAIT — navigateur public]
- Julie B. — « Machine sérieuse, livraison rapide » — « Vérifié ». [FAIT — navigateur public]
- Chloé P. — « Bien pour se lancer » — « Vérifié ». [FAIT — navigateur public]
- Le badge rendu dit « Excellent — 4,8/5 basé sur 789 avis ». [FAIT — navigateur public + HTTP public, réponse 200]

## Preuves de rendu

- Enregistrement Browser Use, 10 frames : `/Users/Hakim/.config/browser-harness/agent-workspace/recordings/tufteo-p0-audit-2026-07-30/`. [FAIT — fichier local]
- Capture mobile home, viewport vérifié `375 × 812` : `tufteo-home-avis-demo-mobile.png` dans ce dossier d'enregistrement. [FAIT — Browser Use]
- Capture mobile fiche kit, viewport vérifié `375 × 812` : `tufteo-kit-avis-demo-mobile.png` dans ce dossier d'enregistrement. [FAIT — Browser Use]

## Action requise de Hakim

La preuve sociale est un domaine réservé exclusif de Hakim ; aucun agent ne doit effectuer la purge sans sa validation. [FAIT — repo:`docs/codex-handoff/12-CODEX-INSTRUCTIONS.md` §5-6]

1. Masquer ou retirer les deux sections `bv-avis-clients` contenant ces six avis, ou les remplacer uniquement par des avis réels et vérifiés. [À VALIDER HAKIM]
2. Retirer ou corriger le badge « 4,8/5 basé sur 789 avis » sur la home et les fiches produit. [À VALIDER HAKIM]
3. Refaire un contrôle public déconnecté sur la home et la fiche du kit ; le critère de fin est zéro occurrence des six noms et zéro compteur non étayé. [À VALIDER HAKIM]

## Manquant / non conclu

- L'audit ne qualifie pas les 169 avis Trustoo importés : leur existence est documentée, mais leur rendu complet et leur provenance n'ont pas été réaudités ici. [MANQUANT — hors périmètre de ce P0]
- Le statut réel des campagnes Google Ads Tuftéo reste contradictoire entre Notion et le dépôt. [CONTRADICTOIRE — non traité dans cet audit]

## Notes de méthode / pièges

- **2 voies indépendantes** : rendu JavaScript dans Browser Use puis HTML public par requête HTTP sans cookie. Les six noms sont présents dans les deux voies. [FAIT]
- Le Chrome connecté à Shopify injecte une barre d'aperçu marchand en bas de page. Cette barre n'a pas servi de preuve d'exposition publique ; la réponse HTTP anonyme `200` a confirmé que les avis sont bien servis hors session. [FAIT]
- **0 mutation, 0 CAPTCHA, 0 identifiant saisi, 0 avis touché.** [FAIT]
