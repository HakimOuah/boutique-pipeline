---
type: journal
boutique: bonum-vitae
date: 2026-08-17
nature: intervention
leviers: [creative]
titre: "17/08/2026 (nuit) — STOP visuels anti-tartre galvanique"
---

# 17/08/2026 (nuit) — STOP visuels anti-tartre galvanique

Codex a appliqué la règle du brief : **aucune image générée, Shopify non modifié**.

## Motifs (contrôlés sur les 6 sources CDN)

1. **Sources 1 et 2** : drapeau allemand + étiquette bleue (« 86 % », FDA, NSF, « 10+ »)
   apposés sur la robe inox — pas un bandeau hors produit. Source 2 : filigrane AliExpress
   en plus. Gommer = présenter un cylindre potentiellement différent de celui livré.
2. **Sources 3-6** : schémas marketing, écorchés, avant/après bouilloire, textes et filigranes.
   Aucune ne prouve l'apparence externe d'un exemplaire livré sans étiquette.
3. **Source 5 (fiche LPS10)** : raccord **G3/4" female**, Ø 54,5 mm, L 255 mm, 1 kg, 4 m³/h.
   Le brief et la fiche Shopify disaient **DN32** — erreur de rédaction, pas une ambiguïté
   fabricant. DN32 (≈ 1¼") et G3/4" (20×27) ne sont pas interchangeables.

Livraison de contrôle : `livraisons/visuels-anti-tartre-galvanique/RAPPORT.md` + `manifeste.json`.

## Corrections faites dans la foulée

- Fiche Shopify `11036961964370` : « Raccordement DN32 » → **G3/4" femelle (filetage 20×27)**.
- Brief Codex aligné (raccord + image 4 « détail matière »).
- Règle gravée dans `REGLES.md` : zoom corps avant génération ; fiche fabricant prime sur le brief.

## Ce que Hakim doit trancher pour relancer

| Voie | Quoi | Risque |
|---|---|---|
| **A — commander 1 unité** | Photos réelles du SKU expédié | Lent, 65 €, mais preuve unique |
| **B — unboxing fournisseur** | Photos du lot actuel, sans overlay | Rapide si le vendeur répond ; qualité incertaine |
| **C — assumer overlay** | Autoriser un cylindre nu composé depuis 1-2 | Si le drapeau/l'étiquette sont physiques, le client reçoit autre chose |

Même en voie A/B : les images Shopping **ne montreront jamais** FDA, NSF ni 86 % — contrainte GMC,
indépendante de ce qui est collé sur l'objet. Si l'étiquette est permanente et non amovible, on
photographie l'objet **après retrait** (si possible) ou on n'utilise pas ce SKU en acquisition.

## Décision Hakim — voie C (17/08 ~22h20)

Hakim assume que drapeau + étiquette sont des incrustations photo. Brief relancé : robe inox nue
autorisée, STOP « marquage physique » levé **pour ce SKU seulement**. Raccord G3/4" inchangé.
Risque accepté : si le lot réel porte ces marquages, le client reçoit un objet différent des
visuels. À recouper à la première commande (photo colis).
