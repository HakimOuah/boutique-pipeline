---
type: journal
boutique: seiko-mod
date: 2026-08-11
nature: intervention
leviers: [sourcing, technique]
titre: "Re-sourcing cadrans arabes orientaux — passe indépendante finale"
---

# Re-sourcing cadrans arabes orientaux — passe indépendante finale

Date de contrôle : 2026-08-11  
Source exclusive : AliExpress Open Platform / AE-Dropshipper via VPS à IP autorisée  
Destination de recherche : France  
Verdict : **aucun quatrième produit distinct qualifiable**.

## Critères bloquants appliqués

Un produit ne passe que si toutes les conditions sont réunies :

1. cadran/pièce de cadran compatible avec un mouvement NH ;
2. diamètre ou compatibilité dimensionnelle prouvée ;
3. chiffres arabes orientaux visibles sur l'image de la variante exacte ;
4. aucun nom, logo, mot, lettre ou verbatim physique sur le cadran ;
5. au moins 10 ventes live ;
6. statut en vente, stock positif et fret exact vers la France.

Le contrôle est séquentiel : un produit qui échoue à l'image exacte n'est pas artificiellement promu jusqu'au contrôle fret.

## Couverture de cette passe

- 30 requêtes indépendantes, chacune exécutée avec les tris `orders` et `price_asc` : **60 appels API, 60 succès, 0 erreur**.
- Fenêtre des contrôles API : 2026-08-11T20:13:02Z à 2026-08-11T20:14:51Z.
- 366 IDs uniques remontés, dont **87 absents du corpus antérieur de résultats**.
- Après filtre catégorie + seuil de 10 ventes : quatre résultats seulement.
  - deux simples pieds de cadran, hors catégorie ;
  - deux fiches contrôlées au niveau variantes exactes, toutes deux refusées.

Axes de requête :

- régional : Saudi, Dubai, Middle East, Muslim, Islamic, Hijri ;
- typographique : Kufic, Kufi, Arabic calligraphy, Arabic font, Arabic marker ;
- linguistique : Iranian, Persian, Dari, Pakistani, Urdu, Arabic India ;
- Unicode exact : `١ ٢ ٣ ٤ ٥ ٦ ٧ ٨ ٩`, `۱۲ ۳ ۶ ۹`, `١٢ ٣ ٦ ٩` ;
- terminologie : Arabic Indic digits, Eastern Arabic digits, date/no-date ;
- tailles : 24.5, 27.5, 28.5, 30, 31, 35, 36, 38 et 39 mm.

## Refus exacts

### 1005008821717771 — TMI Store

- Live API au 2026-08-11T20:15:59Z : `onSelling`, 59 ventes, 1 variante, stock 4.
- Titre API : cadran VH31 28,5 mm pour boîtier NH35.
- Variante exacte : SKU `12000046818743268`, propriété `2PCS`, sans image SKU dédiée.
- L'image officielle produit montre uniquement un disque métallique vierge marqué dans l'image promotionnelle « 28.5mm VH31 » : **aucun chiffre arabe oriental**.
- Verdict : refus au critère visuel, avant fret.
- Preuve : `boutique-seiko-mod/preuves/preuves-sourcing-api-2026-08-11-agent/passe-independante/1005008821717771-cover.jpg`
- SHA-256 : `edf35705cb7763537681be5fdda8dd9c8478cf7935d0431c9ed2ec07a22626fc`.

### 1005010301578787 — LRZ WATCH Store

- Live API au 2026-08-11T20:15:59Z : `onSelling`, 14 ventes, 10 variantes, stocks 4–5.
- Titre API : cadran/éléments ajourés 28,5 mm pour NH35/NH36/NH70.
- Images SKU exactes inspectées pour A1 à A10 :
  - A1/A2/A3 : anneaux avec index ronds/bâtons ;
  - A4 : anneau métallique sans index ;
  - A5/A6/A7/A8/A9/A10 : disques/entretoises colorés sans index.
- **Aucune des dix images ne porte de chiffres arabes orientaux.**
- Verdict : refus au critère visuel, avant fret.
- Preuves : `boutique-seiko-mod/preuves/preuves-sourcing-api-2026-08-11-agent/passe-independante/1005010301578787-A1.png` à `A10.png`.

### Hors catégorie

- `1005007953185099` — 1 000+ ventes : pieds de cadran universels en cuivre, pas un cadran.
- `1005009123277752` — 131 ventes : pieds de cadran universels en cuivre, pas un cadran.

## Conclusion

Cette stratégie n'ajoute aucun produit qualifié. Le compteur reste à **3 produits distincts importables** :

- `1005009751528666`
- `1005007348127532`
- `1005007347658552`

Le minimum de quatre n'est donc pas atteint. Le blocage est documentaire et non technique : parmi les nouveaux résultats vendus au moins dix fois, aucune variante exacte ne présente les glyphes orientaux requis sur une pièce de cadran compatible NH. Aucune approximation, variante occidentale, montre complète ou simple composant n'a été retenu.
