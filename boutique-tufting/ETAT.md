# Tuftéo — état courant

**Dernière mise à jour : 30/08/2026** — contrôle avant relance ads.
**La copie P0 `189437772161` a été publiée, elle est MAIN** : les quatre correctifs sont live
(269 €, plus d'« entrepôts » ni d'« Europe », FAQ France 6–10 j, JSON-LD valide). Triangle
livraison cohérent : France seule, 0 €, même promesse partout.
**Bloquant avant dépense : `orders` est vide — aucune commande n'a jamais été passée, le
paiement n'a jamais été prouvé.** Deux des quatre produits à marge (tondeuse 89,90 €,
ciseaux électriques 140 €) sont à stock 0 en survente.
[`journal/2026-08-30-controle-avant-ads.md`](journal/2026-08-30-controle-avant-ads.md).

---

## Identité

| | |
|---|---|
| Domaine | `tufteo.com` |
| Produit | tufting — kits, machines, fils, toiles, accessoires |
| Entité | OH Ventures (SASU), 47 rue Vivienne, 75002 Paris |
| Téléphone | `+33 7 56 82 80 94` — **testé en vocal par Hakim le 16/08, il répond** |
| E-mail de façade | `contact@tufteo.com` — **testé par Hakim le 16/08, il reçoit** |
| E-mail dans Shopify | ✅ `contact@tufteo.com` — les deux champs, constaté API le 17/08 ([T-07](TABLEAU.md) soldé) |
| Compte Google | Gmail dédié, Workspace sur `tufteo.com`, réchauffé par > 100 € de dépense Ads |
| Persona | ✅ validé — `../personas/persona-tufting-2026-07-19.md` |

**Adresse et téléphone sont partagés avec Bien Brûlé, Bonum Vitae et Maison Noirmont.** Linkage
assumé par décision de Hakim du 16/08 — voir `PASSATION.md` question n° 0 dans le hub. Conséquence :
chaque boutique du parc doit être irréprochable, parce qu'une suspension peut se propager.

---

## Merchant Center — le fait qui change tout

**Le compte GMC existe déjà et les produits sont APPROUVÉS — depuis ~48–72 h seulement.**
Relevé Hakim 17/08 nuit, graphe 28 jours (Tous les produits / boutique en ligne) :

| | |
|---|---|
| 21–24/07 | 0 produit dans le graphe |
| ~25/07 → 14/08 | ~196 produits, **tous Limités** |
| 14–15/08 | bascule nette Limités → Approuvés |
| 17/08 | ~175–180 Approuvés · 0 Limités · 0 Non approuvés · 0 En examen |
| Origine | app Google & YouTube Shopify |
| Google Ads | actif, > 100 € dépensés |

Ce n'est pas « toujours vert ». Trois semaines en Limités, puis le vert. L'approbation
produit est **jeune**. On protège ça, on ne lance pas.

Le risque se déplace vers l'après : la checklist est explicite, **la plupart des suspensions arrivent
après l'approbation**, et les 30 premiers jours qui suivent un changement sont les plus sensibles.

---

## Thème — le point le plus urgent

## Thème — soldé

| Thème | Rôle | Contenu |
|---|---|---|
| `189437772161` — « Tuftéo — P0 GMC 17-08 » | **MAIN** | P0/P1 live, revérifiés sur le site le 30/08 |
| `189429678465` — « Tuftéo — correctifs thème 16-08 » | UNPUBLISHED | ancien MAIN, textes P0 non corrigés |
| `188623847809` — « Tuftéo thème » | UNPUBLISHED | encore plus ancien |

**T-05, T-06, T-08, T-19, T-20 sont tous live.** Plus rien du lot P0 n'attend une publication.

---

## Catalogue

| Collection | Produits | Seuil de 5 |
|---|---|---|
| Accessoires & finitions | 13 | ✅ |
| **Fils** | 18 | ✅ — corrigé le 16/08 (était à 1) |
| Machines | 4 | ⛔ |
| Toiles & tissus | 4, dont 1 brouillon → **3 actifs** | ⛔ |
| `frontpage` | 1 | ⛔ et **publiée sur Google & YouTube sans titre ni meta SEO** |

- **5 variantes ACTIVE à stock 0, en survente (`CONTINUE`)**, relevé du 30/08 : tondeuse
  électrique (89,90 €), ciseaux électriques ×2 (140 €), enfile-laine, toile primaire
  0,5 × 1,05 m. Les deux premières sont dans les quatre produits à marge. Politique de
  stock incohérente dans le catalogue (`DENY` sur les fils, `CONTINUE` ici), sans règle écrite.
- **Aucun GTIN** (`barcode` nul sur 83/83 variantes) et **`productType` vide sur 40/40 produits** —
  handicap permanent sur le flux Shopping, sans être un motif de refus.
- **21 variantes sur 83 sans coût d'achat**, dont la toile primaire à 89,90 € : rentabilité
  incalculable sur ces fiches.
- Marges brutes des produits à pousser : kit 161,16 € (59,9 %) · gun 67,56 € (45,3 %) ·
  tondeuse 46,99 € (52,3 %) · ciseaux 41,22 € (29,4 %). 24 des 36 actifs sont sous 30 €.
- **Statut CE non tranché** : tondeuse 200 W, ciseaux électriques et kit tondeuse avaient été passés
  en DRAFT le 21/07 en attente de conformité. Ils sont repassés ACTIVE **sans trace écrite de la
  décision**. Arbitrage ouvert depuis quatre semaines.
- **0 `compareAtPrice` non nul** sur tout le catalogue — purge vérifiée.
- 169 avis Trustoo réels au catalogue (le badge affichait 789).

---

## Publicité

Protocole appliqué : 30 €/jour pendant 5 jours sans y toucher. **≥ 100 € dépensés, 0 vente,
3 ajouts au panier** — les seuls du parc.

Lecture révisée le 16/08 par les experts : le test a été **coupé trop tôt**, on ne conclut pas à
120-130 €. Mais 3 ajouts paniers pour 0 vente reste aussi un signal d'offre et d'expérience, à ne pas
absoudre entièrement. Reprise en septembre, budget proportionné au ticket.

---

## Avant le premier euro d'ads (30/08)

1. **Commande de test réelle, carte de Hakim, puis remboursement.** `orders` est vide :
   0 commande depuis l'ouverture. Sur six semaines, 5 checkouts atteints et 0 paiement,
   alors que le port est à 0 € — l'hypothèse du choc aux frais tombe. Le paiement n'a
   jamais été prouvé et l'activation Shopify Payments n'a pas pu être lue.
2. **Trancher le stock de la tondeuse et des ciseaux électriques** (0 en survente).
3. **Relevé GMC** — aucun depuis le 17/08.
4. **`productType` sur les fiches poussées**, avant dépense.
5. Démarrer sur **le kit et le gun seuls**, pas les 36 fiches.

---

## Ce qui n'a jamais été vérifié

À écrire ici plutôt qu'à découvrir plus tard :

- **Les images produit, une par une** : texte incrusté, collage, filigrane, doublon entre fiches,
  résolution sous 800 px. Non contrôlées.
- **La vitesse** (cible > 65). Non mesurée.
- **Les icônes de paiement contre les moyens réellement proposés** au checkout.
- **L'origine d'expédition par fiche** : seules les toiles (Allemagne, Pologne) et les deux articles
  électriques (Allemagne) sont documentés. Le gun et le kit — les produits phares — ne le sont pas.
- **La consolidation de l'audit final** des trois agents A/B/C n'a jamais été écrite ([T-16](TABLEAU.md)).
