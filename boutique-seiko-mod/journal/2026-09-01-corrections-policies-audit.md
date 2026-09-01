---
type: journal
boutique: seiko-mod
date: 2026-09-01
nature: intervention
leviers: [conformite]
titre: "Quatre corrections policies (audit 23/08 + reliquats)"
---

# Quatre corrections policies — 01/09/2026

Les quatre défauts listés dans la passe du matin (scope MCP absent). Écrits via CLI
`shopPolicyUpdate` (`write_legal_policies` présent sur le connecteur store).

| Policy | Correction |
|---|---|
| CGV art. 15 (`TERMS_OF_SALE`) | `<meta charset="utf-8">` retiré devant le bloc CM2C. Médiateur inchangé. |
| Coordonnées (`CONTACT_INFORMATION`) | SIRET `103 157 251 00010`, TVA `FR55 103157251` |
| CGU §2 (`TERMS_OF_SERVICE`) | `/pages/mentions-legales` → `/policies/legal-notice` |
| Mentions légales §4–5 (`LEGAL_NOTICE`) | trois `<a>` reliés : confidentialité, cookies, CGV |

Dates de version laissées au **15 août 2026** (homogènes avec les autres policies).

Avant / après : `backups/2026-09-01-policies-4-corrections/`.

## Vérifié live

Corps `.shopify-policy__body` : 0 `meta charset`, 0 SIRET/TVA compact, 0 `/pages/mentions-legales`, 0 `<a>` sans `href`. CM2C + `https://www.cm2c.net/` toujours là.
