# Charte graphique Sous Abri — 09/09/2026 (proposée sur la DA validée du lot 1 Codex)

## 1. Ce que font les concurrents, et ce qu'on en garde
Observé sur 25 sites et les publicités Meta/Google (`analyses/2026-09-09-carport-persona/`) : anthracite ou noir pour la structure, ciel bleu, SUV gris, pavillon neuf, rendus 3D, badges « à partir de » et note Google ; les GSB en rouge/jaune promotionnel ; les fabricants premium en gris froid et blanc. Personne ne montre la météo, le montage, la vraie maison.
Sous Abri prend le contre-pied sans être bizarre : **chaleur et vérité**. Fond sable au lieu du blanc froid, un accent terre cuite au lieu du bleu ou du rouge, une ardoise profonde pour le texte et les structures, des photos de vrai jardin français avec la pluie, la grêle, le givre et le pollen.

## 2. Couleurs
| Rôle | Nom | Hex | Usage |
|---|---|---|---|
| Fond | Sable | `#F4F1EA` | fond de page, fond studio des packshots |
| Texte | Encre | `#1B1F24` | titres, corps |
| Structure | Ardoise | `#2F4A5A` | poteaux du logo, boutons secondaires, pied de page, bandeaux |
| Accent | Terre cuite | `#C8552B` | toit du logo, bouton principal, liens actifs, puces ; jamais en aplat de fond de page |
| Surface | Blanc | `#FFFFFF` | cartes, formulaires |
| Neutres | Sable foncé `#E6E0D3`, gris chaud `#8A847A` | bordures, textes secondaires |
Contrastes : Encre sur Sable 14,9:1 ; Blanc sur Terre cuite 4,7:1 (AA texte normal) ; Blanc sur Ardoise 8,9:1. Terre cuite sur Sable réservé aux titres et icônes (3,6:1, pas pour le corps de texte).

## 3. Typographie
- Titres : **Archivo** Bold (700), interlettrage −1 %, majuscule initiale seulement, jamais tout en capitales.
- Corps : **Inter** Regular 400 / Medium 500, 16–18 px, interligne 1,55.
- Chiffres (prix, dimensions) : Archivo SemiBold, tabulaires.
- Google Fonts, libres (OFL) ; fichiers dans `assets/brand/fonts/` (non versionnés).

## 4. Logo
- Pictogramme : un poteau ardoise portant un toit cintré terre cuite en porte-à-faux, une voiture ardoise dessous. Il dit le produit (le carport), la promesse (la voiture à l'abri) et l'axe (on regarde d'abord ce qui protège).
- Wordmark : « Sous Abri » Archivo Bold, ardoise.
- Fichiers : `assets/brand/out/logo-sousabri.svg` (vecteur, source), `logo-sousabri.png` (2400 × 760, fond sable), `logo-sousabri-transparent.png`, `logo-sousabri-inverse.png/.svg` (blanc sur ardoise), `logo-sousabri-empile.png` (carré), `favicon-sousabri.png` (pictogramme blanc sur terre cuite, 1024), `monogramme-sousabri.png`. Générateur : `assets/brand/make_logo.py`.
- Zone de protection : la hauteur du poteau tout autour. Taille minimale : 120 px de large (pictogramme seul en dessous). Interdits : recolorer le toit, poser le logo sur une photo chargée sans aplat, étirer, ajouter un slogan collé.

## 5. Photos et illustrations
Règles du brief visuels validé (`BRIEF-VISUELS-CODEX-2026-09-09.md` §2) : photo réaliste, pavillon français ordinaire, météo réelle légère, voitures courantes sans logo, packshots sur fond sable avec une seule ombre. Pas de texte dans l'image, pas de badge, pas de note. Les schémas cotés sont en SVG dans la page, encre sur sable, cotes en terre cuite.

## 6. Composants d'interface
- Bouton principal : fond terre cuite, texte blanc, coins 6 px, hauteur 52 px, libellé à l'infinitif (« Ajouter au panier », « Demander mon devis gratuit »). Secondaire : contour ardoise 1,5 px, texte ardoise.
- Barre d'annonce : ardoise, texte blanc, sans compte à rebours.
- Étiquettes : « Stock France », « Stock Allemagne », « Sur mesure » en sable foncé, texte encre.
- Accordéons (déclaration, montage, ancrage…) : titre Archivo 600, chevron terre cuite.
- Tableau comparatif : lignes alternées sable/blanc, colonne Sous Abri en surface blanche avec bordure terre cuite.
- Balises `[À VÉRIFIER]` en brouillon : surlignage jaune pâle `mark.a-verifier`, à retirer avant publication.

## 7. Ton (rappel)
Vouvoiement, direct, concret, « voisin bricoleur ». Pas de point d'exclamation, pas de superlatif creux, pas d'urgence fabriquée.

## 8. Fichiers thème
`brand-tokens.json` (source des réglages `config/settings_data.json`), logos à téléverser dans Fichiers : `logo-sousabri.png` (en-tête, ~200 px de large affichés), `logo-sousabri-inverse.png` (pied de page ardoise), `favicon-sousabri.png`.
