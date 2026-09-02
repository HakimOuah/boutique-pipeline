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

---

## Confirmé — 02/09/2026, soir

L'hypothèse « Klarna n'apparaît qu'une fois l'adresse saisie » est **écartée**. Hakim a refait le
test avec une **adresse française complète**, et Klarna était déjà absent de sa **commande test**
allée à son terme. Mon propre test à 417 € sans adresse donnait le même résultat.

Sont donc écartés : le seuil de montant, le pays, la devise, la catégorie de produit, et le rendu
conditionné à l'adresse. **Klarna est activé côté Shopify et ne sert jamais.** Reste la cause 1 :
activé dans l'admin mais pas opérationnel côté Klarna — examen marchand non terminé, ou moyen
restreint pour ce compte. À lire dans Admin → Paiements → ligne Klarna → « … » → Gérer, pour la
trace et pour savoir quand le réactiver.

La promesse affichée sur les fiches ≥ 239 € et le picto du footer sont donc **des déclarations sans
contrepartie**, sur un compte banni pour déclarations trompeuses. Option A retenue.

### À faire, dans cet ordre

1. Relever le statut Klarna dans « Gérer » (pour le journal, ne bloque rien)
2. Admin → Paiements → **désactiver Klarna** — le picto du footer disparaît seul, les icônes
   suivent `shop.enabled_payment_types`
3. Thème → Personnaliser → page produit → supprimer le bloc « Code personnalisé » `.mn-fractionne`
4. Contrôle : `pi-klarna` absent du footer, `mn-fractionne` absent des fiches à 239 € et plus
5. Compteur : la fenêtre d'examen glisse au **9-12 septembre**

Réversible. On remet les deux le jour où Klarna sert réellement.
