---
type: journal
boutique: seiko-mod
date: 2026-09-02
nature: audit
leviers: [conformite]
titre: "Klarna promis sur les fiches, absent du checkout — dernier blocage avant examen"
---

# Klarna : promesse sans contrepartie — 02/09/2026

Fin de l'audit §6. Hakim a passé les trois gates manquants : **téléphone testé OK**,
**Trustpilot inexistant**, **commande test complète OK**. Reste un défaut, et il est bloquant.

## Le constat

Klarna est **activé** dans l'admin (Paiements → Moyens de paiement locaux) mais **n'apparaît pas
au checkout**. Vérifié en visiteur anonyme sur un panier à **417 €**, la variante la plus chère du
catalogue, donc très au-dessus de tout seuil de paiement fractionné : le checkout ne propose que
**Carte de crédit** (Visa, Mastercard, Amex, +2) et **PayPal**. Ce n'est donc pas une histoire de
montant minimum.

Pendant ce temps, le site le promet à deux endroits :

| Surface | Ce qui s'affiche | Origine |
|---|---|---|
| Footer, toutes pages | picto **Klarna** | auto, depuis `shop.enabled_payment_types` |
| Fiches ≥ ~239 € | **« Paiement en plusieurs fois avec »** + logo Klarna | bloc de thème fait maison `custom-code-block` / `.mn-fractionne` |

Le bloc `mn-fractionne` est conditionné au prix — absent sur les fiches à 12,90 €, présent dès
239 € — donc quelqu'un l'a construit en pensant au seuil Klarna. Le soin ne change rien : la
promesse est fausse à 417 € comme ailleurs, puisque Klarna n'est jamais proposé.

C'est le défaut exact listé dans `audit-lecons-noirmont.md` : *« Pas de bandeau 4 fois / ou Klarna
si Klarna n'est pas au checkout »*, et dans les erreurs à refus immédiat du skill : *« picto de
paiement affiché alors que le checkout ne l'offre pas »*. Sur un compte banni pour **déclarations
trompeuses**, c'est le pire endroit où laisser une contradiction.

## Apple Pay — pas un défaut

Le picto Apple Pay est au footer et `applePayConfig` est non nul dans `/payments/config`. Il ne
s'affiche pas au checkout sur Chrome parce qu'Apple Pay ne se rend que sur Safari et iOS : la
capacité existe réellement, la promesse est tenue pour qui peut l'utiliser. Rien à corriger.
Google Pay est absent des deux côtés — cohérent.

## Deux issues

**A — Retirer la promesse (recommandé).** Désactiver Klarna dans Admin → Paiements, ce qui fait
disparaître le picto du footer tout seul (les icônes sont automatiques depuis
`shop.enabled_payment_types`), **et** supprimer le bloc `mn-fractionne` du gabarit produit. C'est
un bloc « Code personnalisé » dans la section de la page produit : Personnaliser → page produit →
supprimer le bloc. Réversible : on remet les deux le jour où Klarna fonctionne vraiment.

**B — Faire fonctionner Klarna.** Dépend de l'accord de Klarna et de Shopify, pas de nous, et le
délai est inconnu. Incompatible avec une fenêtre d'examen au 8-11 septembre.

Recommandation : **A maintenant, B plus tard**, une fois le compte réapprouvé et stabilisé.

## Effet sur le calendrier

Ces deux modifications sont crawlables : le compteur repart du jour où elles sont faites. Si c'est
le 02/09, la fenêtre glisse au **9-12 septembre**. Un jour de décalage contre la suppression d'une
contradiction que Google regarde en premier : le calcul est vite fait.

## État de l'audit §6 après ça

Tout le reste est vert : identité et contact cohérents, JSON-LD valide, policies corrigées, zéro
marque tierce sur 221 fiches et 1 770 médias, zéro prix barré, 10 redirections 301, aucune
collection publiée vide, bandeau cookies conforme, téléphone vocal OK, Trustpilot absent,
commande test passée. Klarna est le dernier point.
