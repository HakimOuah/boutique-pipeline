---
type: journal
boutique: seiko-mod
date: 2026-07-25
nature: intervention
leviers: [autre]
titre: "Journal de la passe de nuit — 25/07/2026"
---

# Journal de la passe de nuit — 25/07/2026

> Hakim est parti se coucher vers 3 h avec consigne d'autonomie complète. Ce fichier est le compte rendu à lire au réveil. Le runbook principal reste non inscriptible (droits système), d'où ce journal séparé.

## ✅ FAIT — Images de coloris en ligne (le point de départ : « quand je clique sur une variante, l'image ne bouge pas »)

**24 visuels de coloris produits, poussés et assignés à 120 variantes. Zéro erreur.**

| Montre | Coloris | Variantes couvertes |
|---|---:|---:|
| Trente-Neuf — cannelée | 7 (orange, rouge, bleu mer, rose, vert, bleu, noir) | 56 |
| Quarante-et-Un — sport acier | 7 (4 cadrans × acier, 3 × cuir) | 16 |
| Trente-Six — jubilé | 6 (noir, rouge, bleu, rose, doré, or intégral) | 24 |
| Noirmont Un — plongeuse | 2 (acier, bronze) | 12 |
| Trente-Neuf Duo — bicolore | 2 (or rose, doré) | 12 |

Mécanique : un visuel sert **toutes** les variantes qui partagent le coloris — le diamètre, le fond et le mouvement n'ont pas besoin de photo propre. C'est ce qui ramène 120 variantes à 24 images.

Contrôle fait : planche d'homogénéité vérifiée à l'écran (cadrage, lumière et ombre identiques d'un coloris à l'autre), puis vérification API que chaque variante porte le bon média.

Modèle : `nano_banana_pro` 4K, retenu après comparatif. **148 crédits** consommés (18 au-dessus du plafond de 130 : le débit réel est ~5,3 crédits/image en 4K et non 4 comme annoncé par l'API — à retenir pour budgéter les 43 coloris restants, soit ~230 crédits).

### ⚠️ Reste à prouver : le comportement du thème
L'assignation est correcte côté Shopify, mais **il n'est pas encore vérifié que le thème FullStack fait basculer la galerie** au clic. QA non faite : le navigateur est **partagé avec les agents**, et un agent de sourcing naviguait. À faire en priorité au réveil — si le thème ne suit pas, c'est un correctif liquide dans le bloc galerie.

## ✅ FAIT — 10 visuels des futures fiches accessoires
Générés, vérifiés un à un (aucun texte, aucun logo, **comptage exact des 6 emplacements** des coffrets — l'erreur qui nous avait coûté une reprise). 48 crédits. Dossier `scratchpad/noirmont-accessoires-img/`.
Le visuel `jubile-plat-1.jpg` montre un bracelet oyster 3 maillons : ce n'est **pas** un défaut, il est destiné à la fiche « Jubilé & Oyster » qui vend les deux profils.

## ⛔ BLOQUÉ — et pourquoi

**Création des fiches accessoires** : décision technique prise en cours de nuit — il faut les faire **entrer par DSers, pas par l'API Shopify**. Un produit créé à la main n'a pas les SKU portant la chaîne d'attributs AliExpress, donc l'auto-matching DSers ne fonctionne pas et le mapping devient manuel variante par variante (le bracelet jubilé a 5 largeurs). L'import DSers donne les bons SKU **et** le mapping d'un coup. Or DSers passe par le navigateur, occupé. Tout est prêt par ailleurs : textes, prix, options dans `scratchpad/noirmont-fiches-accessoires.md`, visuels générés.

**Carte cadeau** : Shopify refuse la création — la fonctionnalité doit d'abord être **activée dans les réglages** (action marchand, 1 min).

**43 coloris restants** (Voyageur GMT, Noirmont Deux, Contre-la-montre, Intégrale, Héritage) : codes fournisseur opaques, identification visuelle AliExpress nécessaire → navigateur.

## 🔑 Enseignements de la nuit, à garder

1. **Le navigateur est une ressource unique partagée** entre l'orchestrateur et tous les agents. Deux consommateurs simultanés = onglets qui se re-naviguent. **Sérialiser tout usage du navigateur.**
2. **Le coût réel des générations 4K est ~30 % au-dessus du tarif annoncé** par l'API. Budgéter avec une marge.
3. **Créer un produit dropshippé à la main est un faux gain de temps** : sans les SKU DSers, on déplace le travail vers un mapping manuel. Toujours passer par l'import fournisseur.

## Décisions qui t'attendent

1. **Découpage en fiches OU images de variante**, famille par famille — les deux s'excluent. Les images de variante sont maintenant en place sur 5 montres : si tu découpes l'une d'elles, ce travail est remplacé, pas complété.
2. **Valider le plan de nommage communautaire** des coloris (Pepsi, Batman, Panda…) avant de graver les titres du découpage.
3. **Activer les cartes cadeaux** dans les réglages Shopify.
4. **Débloquer les droits d'écriture** du runbook principal.
5. Deux candidats accessoires volontairement non retenus (oyster 3 rangs, ouvre-boîtier) : preuve sociale trop mince, à re-sourcer.
