# QA — visuels machines Tuftéo — 2026-08-16

## Périmètre

- Livraison locale uniquement : `boutique-tufting/images/visuels-2026-08-16-machines/`.
- 12 visuels générés en image-vers-image à partir des sources fournisseur indiquées dans le brief.
- Aucune opération Shopify, aucune publication et aucune suppression de média.
- Prompts complets : `PROMPTS.md`.
- Planche de contrôle : `qa/planche-controle-12.jpg`.

## Contrôle visuel — tondeuse filaire

| Fichier | Contrôle |
|---|---|
| `tondeuse-electrique-tapis-01.png` | Outil seul, forme et couleurs conservées, câble visible et rangé, poignée vierge. |
| `tondeuse-electrique-tapis-02.png` | Macro de la tête noire et de la lame T argentée, aucune surface marquée. |
| `tondeuse-electrique-tapis-03.png` | Boîtier seul, bouton argenté et bague dorée vierge, câble visible. |
| `tondeuse-electrique-tapis-04.png` | Kit physique, non-collage : 1 outil + 1 boîtier + 2 lames + 2 guides + 1 brosse + 1 support. |
| `tondeuse-electrique-tapis-05.png` | Mise en situation sur tapis tufté, câble visible, prise en main sûre. |
| `tondeuse-electrique-tapis-06.png` | Outil posé sur le support à base claire et bras brun-rouge, câble visible. |

## Contrôle visuel — ciseaux sans fil

| Fichier | Contrôle |
|---|---|
| `ciseaux-electriques-sans-fil-sculpture-01.png` | Outil seul, 1 batterie insérée, aucun câble, lame circulaire et patin visibles. |
| `ciseaux-electriques-sans-fil-sculpture-02.png` | Macro de la lame circulaire, du carter teal et du patin métallique. |
| `ciseaux-electriques-sans-fil-sculpture-03.png` | 1 batterie neutre seule, sans marque ni voltage ; simples barres lumineuses non textuelles. |
| `ciseaux-electriques-sans-fil-sculpture-04.png` | Kit physique, non-collage : 1 outil sans batterie montée + 2 batteries séparées + 1 chargeur EU + 1 boîte neutre. |
| `ciseaux-electriques-sans-fil-sculpture-05.png` | Mise en situation, 1 batterie insérée, aucun câble, guide orienté vers le tapis. |
| `ciseaux-electriques-sans-fil-sculpture-06.png` | 1 chargeur EU à deux broches rondes relié à 1 batterie, aucune station inventée. |

## Contrôles transversaux

- Aucun texte, pseudo-texte, logo, marque, filigrane, badge, revendication ou pictogramme de conformité visible.
- Absence vérifiée des marquages interdits : EASYCLIP, ONEVAN, Makita, CE, 88VF, 800W, 1-6MM et 900R/MIN.
- Aucun collage, aucune légende et aucun objet marketing intégré dans les visuels.
- Fond crème très clair cohérent, lumière diffuse, ombre douce et cadrage carré homogène.
- Produit filaire correctement représenté dans la série tondeuse ; produit sans fil correctement représenté dans la série ciseaux.

## Validation mécanique

- `mapping.json` : JSON valide, 12 entrées, 12 noms uniques, quatre champs attendus par entrée.
- Inventaire : 12 PNG mappés et exactement 12 PNG présents dans le dossier de livraison.
- Dimensions : 1600 × 1600 px pour les 12 fichiers.
- Poids : chaque fichier est strictement inférieur à 2 000 000 octets.
- Intégrité : 12 empreintes SHA-256 distinctes ; aucun doublon octet pour octet.

Verdict : **PASS — 12/12**.
