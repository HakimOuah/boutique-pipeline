---
type: journal
boutique: tufting
date: 2026-09-03
nature: intervention
leviers: [page]
titre: "Copie thème preview branding — Trustpilot + avis démo + prix barrés simulés"
---

# Preview branding 03/09 — copie non publiée

Hakim a demandé à **voir** le branding retiré le 16/08 (étoiles Trustpilot, avis démo,
prix barrés), sans le republier.

## Copie

| | |
|---|---|
| Source | MAIN `189437772161` « Tuftéo — P0 GMC 17-08 » |
| Copie | **`190113350017`** « Tuftéo — preview branding 03-09 » |
| Rôle | **UNPUBLISHED** (constaté après push) |
| Preview | https://tufteo.com/?preview_theme_id=190113350017 |

**Aucune écriture sur le MAIN.** Le live sans cookie de preview sert toujours
`189437772161` (curl 03/09 : 0 « 789 », 0 bandeau brouillon).

## Ce qui est remis, sur la copie seulement

- Badge Trustpilot (Liquid restauré depuis `188623847809`) : « Excellent — 4,8/5
  basé sur 789 avis » home + fiche.
- Groupe hero « 2 000 clients satisfaits » + étoiles 4,5 réactivé.
- Section avis démo (`bv-avis-clients`) : Camille / Léa / Sarah (home),
  Manon / Julie / Chloé (fiche), badge « Vérifié ».
- Prix barrés **simulés en JS** (snippet `tufteo-preview-barres`) : kit **299 €**,
  gun **189 €**, tondeuse **119 €**, reste × 1,3. Le catalogue Shopify reste
  `compareAtPrice: null` — le live n'affiche aucun barré.

Bandeau jaune en tête de la copie : *« Brouillon — ne pas publier »*.

## Contrôle navigateur (preview)

- Accueil : bandeau + badge Trustpilot + section avis.
- Kit : badge 789 avis, avis Manon/Julie/Chloé, barré **€299**.
- Gun : barré **€189**.
- Collection `/collections/all` : 24 cartes avec barré simulé.

## À ne pas faire

Publier cette copie. Les 789 avis, le « Vérifié » et la grille × 1,3 sont
exactement le motif de purge du 16/08. Cette copie sert à regarder, pas à
mettre en ligne.
