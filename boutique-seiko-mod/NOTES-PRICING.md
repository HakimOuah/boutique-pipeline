# Maison Noirmont — notes de pricing

Toutes les remarques de prix relevées au fil des études, rassemblées ici en attendant **la passe dédiée de calcul des marges réelles** (décision de Hakim, 14/08/2026).
**Aucun prix n'a été écrit sur la boutique** depuis le 09/08. Prix actuels : montres **279 à 429 €**.

---

## 1. La contrainte de méthode : ratio prix ÷ CPC ≥ 100

Règle Kraken, cible 150-200. Les CPC sont **mesurés**, pas estimés.

| Famille | CPC | Prix plancher pour tenir le ratio | État actuel |
|---|---:|---|---|
| Aiguilles | 0,10 € | 19,90 € → ratio **199** | ✅ cible atteinte |
| Cadrans | 0,17 € | ≥ 24,90 € (ratio 146) ; cible dès **29,90 €** | ✅ |
| Outils d'horloger | 0,20 € | **≥ 19,90 €** | ⚠️ **5 fiches sur 8 tombent** (entrée à 12,90 € → ratio 65) |
| Mouvements | 0,21 € | ≥ 29,90 € | à fixer |
| Verres saphir | 0,30 € | **≥ 29,90 €** | ⚠️ 24,90 € donne 83, **sous le seuil** |
| Boîtes et coffrets | 0,38 € | ≥ 46 € | ⚠️ premier prix à 24,90 € |
| Bracelets | 0,41 € | ≥ 27 € sur la cote mm | ⚠️ **6 fiches sur 10 tombent** |
| Remontoirs | 0,55 € | ≥ 55 € | ✅ tenus |
| Boîtiers de montre | **0,64 €** | **≥ 64 €** | ⚠️ le plus contraignant |
| Écrins et rouleaux | 0,36 € | ≥ 36 € | à vérifier |

**Conséquence directe** : l'entrée de gamme actuelle casse la règle sur trois familles. Soit on remonte les prix, soit on renonce à acheter du trafic dessus.

---

## 2. Ce que le marché autorise réellement (relevé concurrentiel du 14/08)

Ces bandes viennent des SERP et du Shopping français, pas d'une estimation.

| Famille | Bande de marché | Notre position | Lecture |
|---|---|---|---|
| **Montres squelette** | **79 à 239 €** | **399 à 429 €** | ⚠️ **C'est notre prix qui ferme la porte, pas la concurrence.** La tête `montre squelette homme` (2 900) est accessible, mais pas à ce tarif. |
| **Boîtes et coffrets** | Shopping **verrouillé 19 à 48 €** par SONGMICS et consorts | 3 fiches | Vendable seulement **au-dessus de 69 €** — sortir de la bande basse plutôt que s'y battre. Un coffret à 49,90 € est le pire endroit. |
| **Coffrets à sourcer** | 69 à 149 € | — | Cible de sourcing (5-7 fiches, 8-12 emplacements). |
| **Porte-montres et présentoirs** | 35 à 90 € | **0 fiche** | Trou d'offre, collection dédiée chez les 3 spécialistes. |
| **Marmottes de voyage** | 39 à 99 € | — | Cible 2-3 fiches. |
| **Bracelets NATO** | **10 à 22 €** | 0 fiche | Trop bas à l'unité pour le ratio → **lot de 3 à 29-39 €**, ou organique seul sans publicité. |
| **Montres (référence `maisondutemps`)** | **155 à 385 €** sur 162 montres | 279 à 429 € | Le concurrent modèle vit **sous** notre plancher. |

---

## 3. Les coûts réels sont plus bas que prévu

Constat du push DSers (09/08), jamais répercuté :

- Plusieurs coûts réels **inférieurs aux estimations** — exemple relevé : **9,19 € contre 18,49 €** attendus.
- Coût rendu observé par l'API sur les cadrans : **7,48 à 7,68 €** (cadran arabe soleillé), **11,18 à 11,78 €** (cadran rayonné).
- Fret France : **1,99 €**, suivi.
- Deux montres mod : coût **75,24 €** (`montre-pilote-plongee-39`) et **110,77 €** (`montre-sterile-40-nh35-saphir`).

**La marge est donc probablement meilleure que ce que la grille suppose** — le recalcul peut jouer en notre faveur, y compris pour baisser un ticket d'entrée sans perdre de marge.

---

## 4. Les deux stratégies déjà chiffrées (T-H3, non tranchées)

Détail dans `journal/2026-08-09-textes-et-collections.md`, partie 3 :
1. **Encaisser la marge** — garder les prix, profiter des coûts plus bas.
2. **Baisser le ticket d'entrée** — utiliser l'écart de coût pour entrer dans les bandes de marché.

Le relevé concurrentiel du 14/08 penche vers la seconde sur les **montres squelette** (399 € contre une bande à 79-239 €) et vers la première sur les **coffrets** (monter au-dessus de 69 € plutôt que descendre dans la bande verrouillée).

---

## 5. Points à trancher lors de la passe marges

1. **Les squelettes** : reprixer à 199-279 € comme le recommande l'étude concurrentielle, ou assumer le positionnement haut et renoncer à la tête à 2 900 ?
2. **Les trois familles sous le seuil de ratio** (outils, verres, bracelets) : remonter les prix, ou les exclure de toute campagne payante et les garder en organique ?
3. **Les coffrets** : viser 69-149 € confirme-t-il une marge suffisante au coût fournisseur réel ?
4. **Les NATO** : lot de 3 à 29-39 € — la marge tient-elle après fret ?
5. **Le prix plancher des boîtiers à 64 €** est-il compatible avec le coût réel, ou faut-il renoncer à cette collection en payant ?
6. **Recalculer toutes les marges sur les coûts réels de l'API**, pas sur les estimations du registre de sourcing.

---

## 6. Rappels de cadre

- **Aucun prix barré** : les 931 `compareAtPrice` ont été purgés le 08/08. Sur une boutique à 0 vente, un prix de référence est injustifiable et c'est le tueur Merchant Center n°1. **Ne pas les réintroduire.**
- Le budget publicitaire validé est de **30 €/jour**, ce qui suppose un CPC entre 0,16 et 0,25 € pour rester cohérent.
- Objectif de la phase de lancement : **15 conversions** pour débloquer le tROAS, sans chercher la rentabilité.
