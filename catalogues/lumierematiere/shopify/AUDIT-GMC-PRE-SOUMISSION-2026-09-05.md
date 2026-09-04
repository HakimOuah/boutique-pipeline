# Audit GMC avant soumission — 05/09/2026

Déroulé contre `gmc-acceptance` : `checklist-pre-soumission.md` §6 + `audit-lecons-noirmont.md`.
Vérifié sur le site public, pas dans l'admin.

**Verdict : la boutique est conforme, mais pas encore soumettable — pour une raison de calendrier.**

## Le seul vrai bloqueur : l'âge du domaine

`lumierematiere.fr` créé le **24/08/2026** → **12 jours**. La règle posée le 26/08
(`TRI-DELAIS-GMC-2026-08-26.md`) est de ne pas soumettre avant 30 jours, soit **le 23/09**.
C'est une précaution maison — le skill la marque explicitement comme telle, pas comme un gate
Google — mais rien de ce qui suit ne justifie de l'écourter.

## Ce qui passe

| Point | État |
|---|---|
| Prix barrés sur les actives | **0** |
| Images fournisseur brutes (`alicdn`) | **0** |
| Images CDN partagées entre deux fiches | **0** |
| Policies (`/policies/*`) | 5/5 en 200 |
| Doublon `/pages/mentions-legales` | absent (404, correct) |
| Liens internes de la home | 25/25 en 200 |
| Suivi de commande (`/apps/parcelpanel`) | 200 |
| JSON-LD `Organization` | parse strict OK, adresse + e-mail pro + URL |
| JSON-LD `Product` | **sans `sku`**, conforme à `identifier_exists: no` |
| Pictos de paiement | mode auto (`aria-labelledby="pi-…"`), donc calés sur les moyens activés |
| Checkout | Klarna et Amex confirmés par Hakim le 05/09 |
| Marque tierce | aucune |

**Deux fausses alertes levées en vérifiant le contexte plutôt qu'en comptant les occurrences :**

- « 6 à 16 jours » et « 7 à 18 jours » coexistent parce que c'est une **décomposition**
  (1–2 j préparation + 6–16 j acheminement = 7–18 j total), écrite à l'identique dans la FAQ, la
  policy d'expédition et le bandeau. Ce n'est pas le flag Noirmont, c'est son contraire.
- Le « 4,5 » repéré dans le HTML : des **coordonnées SVG**. Aucune note de démo ne subsiste.

## Ce qui a été corrigé aujourd'hui

### Un prix faux en dur sur 20 fiches sur 52

Le métachamp `custom.specs` contenait une ligne **« Prix : à partir de N € TTC »** écrite à la
main. Sur **20 fiches, le chiffre était faux**, toujours au-dessus du prix réel :

| Fiche | Annonçait | Prix réel | Écart |
|---|---:|---:|---:|
| `246282`, `134962` | 249 € | **159 €** | +90 |
| `952116`, `121862` | 249 € | **169 €** | +80 |
| `183789` | 199 € | **129 €** | +70 |
| `832012`, `655008`, `630923` | 249 € | **199 €** | +50 |
| `625575` | 249 € | **209 €** | +40 |
| `837156`, `805304`, `348096`, `560098`, `253182`, `037279`, `975417` | 199 € | **169 €** | +30 |
| `245113`, `897170`, `934110` | 249 € | **229 €** | +20 |
| `607504` | 249 € | **239 €** | +10 |

Une page qui affiche 129 € et écrit 199 € trois blocs plus bas, c'est un mismatch visible par un
examinateur, et une infraction consommateur en France.

**Correction : la ligne de prix est supprimée des 52 fiches**, pas corrigée sur 20. Un bloc de
spécifications qui répète un prix dérivera au prochain changement de tarif. Elle est remplacée par
« Prix : affiché toutes taxes comprises (TTC) » — sans montant, donc sans dérive possible.

### Un effet de bord que j'ai créé, puis réparé

La ligne « Prix » était **le seul endroit où figurait « TTC »**. En la supprimant j'ai retiré la
mention des 52 fiches — obligation consommateur FR et item de la checklist. Rétablie dans le même
passage, sans montant. Vérifié : 52/52 portent « TTC », 0/52 portent un prix en dur.

### Des blocs de specs qui décrivaient l'ancien catalogue

Les mêmes métachamps listaient encore les codes aveugles renommés le 04/09 (`Modèle : A, B et C`),
et trois erreurs de fond :

- **`607504`** : « Diamètre : 19, 40 et 50 cm » — **19 et 50 sont des hauteurs**, pas des
  diamètres. Les diamètres réels sont 25 et 40. Corrigé dans `specs`, `usps`, `benefits` et `faq`.
- **`897170`** : « Matière : rotin tressé » alors que **la moitié des variantes sont en fibre
  synthétique**. Corrigé.
- **`272937`** : se décrivait encore comme une suspension en corde de chanvre, alors que c'est un
  plafonnier à fixation directe depuis le 04/09. Corrigé.

### `934110`, le dernier mensonge actif

Le titre disait « Suspension **tube** travertin » au singulier alors que **deux variantes sur
trois sont des doubles tubes** (établi par Codex : `193` = un tube, `173` et `175` = deux tubes sur
rosace commune, ces deux références identiques au SHA-256 près).

→ Titre : **« Suspension travertin cuisine, un ou deux tubes »**.
→ Libellés : `Un tube · travertin`, `Deux tubes · blanc chaud 3000 K`, `Deux tubes · blanc froid
6000 K` — le comptage est prouvé, la température reprend mot pour mot le SKU fournisseur.
→ Description : la différence un/deux tubes est expliquée.

**La température reste à confirmer** : un second axe fournisseur à valeur unique `3000K warm
light` contredit la variante annoncée à 6000 K. Rien dans la fiche ne promet une température
au-delà de ce que le SKU affirme.

## Ce qui reste, et qui n'est pas de mon ressort

1. **`money_format` = `€{{amount_with_comma_separator}}`** → affiche `€199,00`. La convention
   française est `199,00 €`. C'est un réglage Paramètres → Général, pas exposé en écriture par
   l'API Admin. **À faire par Hakim.**
2. **Téléphone** : le site affiche `+33 7 56 91 60 84`, le skill documente la ligne du parc
   `+33 7 56 82 80 94`. Hakim a testé un numéro qui décroche le 31/08 — soit la boutique a sa
   propre ligne et le skill est à jour, soit il y a un écart. **À trancher.** Accessoirement le
   JSON-LD sort `0756916084` en national quand le footer affiche l'international : troisième
   graphie, que la leçon Noirmont proscrit.
3. **`193329` / `338324`** : le même article à 199 € sur deux listings AliExpress distincts.
4. **`147607`** : vendue avec ou sans ampoule — SKU `Warm light 3000K` contre corps de fiche E27.
5. **Commande test** : point 1 de la création GMC, statut inconnu de mon côté.
6. **Collections maigres en visiteur** : `suspensions-xxl` (1) et `plafonniers-cuisine` (2). Ni
   l'une ni l'autre n'est liée depuis la home, donc l'impact est faible.

## Une correction que je dois à Hakim

Le 04/09, en déplaçant `272937`, j'ai écrit que `plafonniers-cuisine` passait « de 4 à 5
produits ». C'était le compte de l'**admin, brouillons inclus**. En visiteur, la collection passe
de **1 à 2**. La leçon Noirmont dit précisément de compter via `products.json` et jamais dans
l'admin — je ne l'ai pas appliquée.
