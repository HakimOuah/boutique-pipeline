---
type: journal
boutique: tufting
date: 2026-08-30
nature: audit
leviers: [conformite, ads, catalogue]
titre: "Contrôle avant relance Google Shopping — 30/08/2026"
---

# Contrôle avant relance Google Shopping — 30/08/2026

Demande de Hakim : dernier coup d'œil avant de lancer les ads. Treize jours après le
dernier relevé (17/08), rien n'avait été réécrit dans `TABLEAU.md` ni `ETAT.md`.
Tout ce qui suit est constaté en direct — API Admin et site live — pas relu dans les fiches.

## Ce qui est confirmé bon

**Le thème P0 a bien été publié.** `189437772161` « Tuftéo — P0 GMC 17-08 » est MAIN
(constaté API). Les quatre correctifs sont donc live, vérifiés sur l'accueil :

| Contrôle | Résultat |
|---|---|
| Prix du kit | 0 occurrence de « 229 € », 2 de « 269 € » |
| « entrepôts » | 0 occurrence |
| « depuis l'Europe » | 0 occurrence |
| FAQ délai | « Livraison offerte en France en 6 à 10 jours ouvrés » présent |
| JSON-LD Organization | parse sans erreur, `legalName: OH Ventures` |

**Le triangle livraison est cohérent**, ce qui était le vrai risque de T-05/T-06.
`shipsToCountries = ["FR"]`. Profil de livraison : une seule zone, France, une seule
méthode « Livraison offerte » active à 0,00 €. Donc la promesse de l'accueil, le texte
des CGV et le tarif réellement appliqué au checkout disent la même chose. Aucun choc de
frais de port n'est possible.

**Les six pages de politiques répondent 200** (CGV, remboursement, livraison, mentions
légales, confidentialité, contact). Identité affichée en pied de fiche : OH VENTURES,
47 rue Vivienne 75002 Paris, `contact@tufteo.com`, téléphone.

**Aucun faux avis rendu.** Les occurrences d'« étoiles » sur les fiches sont les chaînes
de traduction de l'app Trustoo (`{{total_rating}} étoiles basé sur {{total_reviews}} avis`),
pas des avis affichés. Aucun `aggregateRating` dans le JSON-LD produit.

**Aucun `compareAtPrice` non nul** sur les 83 variantes — la purge de faux prix barrés tient.

## Ce qui bloque une dépense

### 1. Le paiement n'a jamais été prouvé — aucune commande n'existe

`orders(first:15)` renvoie **une liste vide**. Zéro commande depuis l'ouverture de la
boutique, pas même une commande de test. `abandonedCheckouts` est vide également.

À rapprocher de la série de mesures : six semaines, 490 sessions, 7 ajouts au panier,
**5 checkouts atteints et 0 paiement** — et d'un test ads antérieur à > 100 € de dépense
pour 3 ajouts au panier et 0 vente.

Le tarif de port est à 0 € pour la France, donc l'hypothèse « choc aux frais de port »
tombe. Il reste : soit ces checkouts étaient internes, soit **le paiement ne passe pas**.
Personne n'a jamais réussi à payer sur `tufteo.com`, et rien dans ce qui est écrit ne
prouve que c'est possible.

La vérification de l'activation Shopify Payments a été refusée en accès. **C'est à Hakim
de passer une vraie commande avec sa carte, puis de rembourser.** Tant que ça n'est pas
fait, tout euro d'ads est misé sur une hypothèse non testée.

### 2. Deux des quatre produits à marge sont à stock 0

Les marges brutes calculées sur les coûts d'achat renseignés :

| Produit | Prix | Coût | Marge | Stock |
|---|---|---|---|---|
| Kit Tufting Complet | 269,00 € | 107,84 € | **161,16 € (59,9 %)** | OK |
| Tufting gun 2-en-1 | 149,00 € | 81,44 € | 67,56 € (45,3 %) | OK |
| Ciseaux électriques | 140,00 € | 98,78 € | 41,22 € (29,4 %) | **0** |
| Tondeuse électrique | 89,90 € | 42,91 € | 46,99 € (52,3 %) | **0** |

Ces deux-là sont ACTIVE, à quantité 0, et `availableForSale = true` — donc en survente
autorisée. Trois autres fiches sont dans le même cas (enfile-laine, toile primaire
0,5 × 1,05 m). Soit le chiffre est faux parce qu'on est en dropshipping et il faut arrêter
de suivre ce stock, soit il est vrai et on s'apprête à payer pour vendre ce qu'on ne peut
pas expédier. Le catalogue mélange les deux politiques (`DENY` sur les fils, `CONTINUE`
ici) sans règle écrite.

**21 variantes sur 83 n'ont aucun coût d'achat renseigné**, dont la toile primaire à
89,90 €. Sur celles-là, la rentabilité d'une campagne est incalculable.

### 3. Le flux Shopping est structurellement handicapé

- **Aucun GTIN** : `barcode` est nul sur les 83 variantes.
- **`productType` vide sur les 40 produits.**

Ni l'un ni l'autre ne fait refuser un produit. Les deux privent Google de ses meilleurs
signaux de catégorisation et de rapprochement de catalogue : moins d'impressions, un CPC
moins bien servi. Remplir `productType` est un travail de trente minutes qui se fait avant
de dépenser, pas après.

Les SKU restent les chaînes AliExpress brutes (`14:202520811#52 yellow`). Shopify les
envoie en `mpn` dans le flux. Invisible du client, mais lisible dans le flux — et illisible
pour nous. Reste en P2 : renommer après lancement ne casse pas l'historique
d'apprentissage, l'`id` du flux étant l'ID de variante.

### 4. Économie du catalogue : ne pas pousser les 36 fiches

24 des 36 produits actifs sont entre 4,90 € et 29,90 €. Un cône de fil à 12,90 € laisse
environ 7,70 € de marge : c'est le budget de clics **total** que peut absorber une vente.
Le kit en laisse 161 € — vingt fois plus de droit à l'erreur. Sur une marque inconnue,
répartir le budget sur tout le catalogue revient à financer les clics sur les accessoires
avec la marge qu'ils n'ont pas.

## Points de vigilance, sans blocage

- **« gun » et lames.** La politique Armes de Google est appliquée automatiquement. Le
  compte est approuvé aujourd'hui, donc ça passe — mais si un refus tombe après le
  lancement, « Tufting gun 2-en-1 Cut & Loop » et « Lames de remplacement (lot de 12) »
  en sont la cause la plus probable. Repli : « Machine à tufter ».
- **Statut CE toujours non tranché** sur la tondeuse 200 W et les ciseaux électriques,
  repassés ACTIVE le 21/07 sans trace de décision. Un des deux est dans la liste des
  produits à pousser. Arbitrage ouvert depuis six semaines.
- **Poids des pages** : 425 Ko de HTML seul sur l'accueil, 315 Ko sur la fiche kit, avant
  images, CSS et JS. Le score PageSpeed n'a pas pu être mesuré (API en quota dépassé) et
  ne l'a jamais été. À lancer avant d'acheter du trafic mobile.
- **Aucune icône de paiement** rendue sur l'accueil. Signal de confiance absent, et point
  explicite de la checklist Terry.

## Ce qui n'a pas pu être vérifié

| Sujet | Raison |
|---|---|
| Activation Shopify Payments | accès refusé |
| Statuts produits GMC au 30/08 | pas d'accès au Merchant Center — relevé Hakim nécessaire |
| Score PageSpeed mobile | API PSI en 429 |
| Canaux de vente / publication Google | scope `read_publications` absent |

## Verdict

Rien dans la conformité ne justifie de retarder le lancement : les correctifs P0 sont
live, le triangle livraison est cohérent, les politiques répondent, il n'y a pas de faux
avis ni de faux prix barrés. Ce qui n'est pas prêt n'est pas la défendabilité, c'est la
**preuve commerciale** — personne n'a jamais payé sur cette boutique, et deux des quatre
produits qui méritent un budget affichent zéro stock.

Séquence recommandée avant le premier euro : commande de test réelle puis remboursement ·
trancher le stock des deux électriques · relevé GMC · `productType` sur les fiches
poussées. Puis démarrer sur le kit et le gun seuls.
