---
type: journal
boutique: tufting
date: 2026-08-30
nature: sourcing
leviers: [catalogue, sourcing]
titre: "Ressourcing des 4 références en rupture — aucun remplacement retenu"
---

# Ressourcing des références en rupture — 30/08/2026

Quatre références sont à stock 0 chez le fournisseur AliExpress actuel : tondeuse électrique
(89,90 €), ciseaux électriques sans fil (140 €), enfile-laine Noir, toile primaire 0,5 × 1,05 m.
Sourcing de remplacement lancé avant d'arbitrer les campagnes Shopping.

Le rapport brut est reproduit plus bas. **Il est déposé ici et non dans `reports/`, qui est
ignoré par `.gitignore` — la règle maison interdit de contourner le `.gitignore` avec
`git add -f`, et le journal de boutique est versionné.**

## Ce qu'il faut en retenir

**Aucun fournisseur de remplacement n'est retenu.** Rien ne change pour le lancement : le plan
restait le kit et le gun, tous deux approvisionnés.

**Tondeuse — deux fiches trouvées, aucune exploitable.** Stone's Store (`1005006997315896`) à
54,98 € rendu et Decwls (`1005005972440926`) à 56,98 €, prise EU, 5–10 j — le délai tient la
promesse boutique. Trois réserves qui suffisent à écarter :

- **Stock EU annoncé : 1 unité** sur chacune. Inexploitable en dropshipping, quel que soit le prix.
- **Coût rendu 54,98 € contre 42,91 € aujourd'hui** : la marge tomberait de 52,3 % à ~39 %.
- **Coloris « vert clair » et non Orange/Noir** : les visuels de la fiche ne correspondraient plus.

**Ciseaux sans fil — vraiment rien.** À vérifier contre la fiche : le produit Tuftéo est bien
sans fil (2 batteries rechargeables, chargeur EU, compatibilité annoncée 18 V type Makita). Les
seuls articles remontés sont des 200 W filaires — donc des tondeuses, pas des ciseaux sans fil.
Le rejet est cohérent, pas une confusion produit.

**Enfile-laine et toile 0,5 × 1,05 m — non conclu, pas « inexistant ».** La route de recherche
a échoué, ce n'est pas la même chose qu'une absence d'offre. Dans les deux cas il s'agit d'une
variante sur plusieurs, les autres formats et coloris étant approvisionnés : un réassort DSers
auprès du fournisseur actuel est plus probable qu'un changement de fournisseur.

**Fiabilité du rapport : confiance B au mieux, jamais A.** Aucune page produit n'a pu être
ouverte (anti-bot). Donc note réelle, nombre de ventes, résolution des photos et mention CE ne
sont pas vérifiés sur les deux candidats. Rien n'est décidable en l'état.

## La piste que le sourcing ne pouvait pas voir : elle est déjà dans le catalogue

**« Kit tondeuse + guide de tonte », variante « Avec guide » — statut DRAFT, stock 64.**

| | Tondeuse ACTIVE (en rupture) | Kit tondeuse DRAFT « Avec guide » |
|---|---|---|
| Prix | 89,90 € | 79,90 € |
| Coût d'achat | 42,91 € | **27,35 €** |
| Marge | 46,99 € (52,3 %) | **52,55 € (65,8 %)** |
| Stock | **0** | **64** |
| SKU fournisseur | `14:201441319;200007763:201336342` | `14:200006153#With bracket;…;5:361385#EU Plug` |

C'est un **listing fournisseur différent**, approvisionné, moins cher à l'achat, avec la prise EU
inscrite dans le SKU, et il embarque le guide de tonte. La conformité CE validée par Hakim le
30/08 couvre déjà le kit tondeuse. Si c'est la même machine, le remplacement est là et il est
meilleur que l'existant — sans passer par AliExpress.

À vérifier avant d'y toucher : que ce soit bien la même machine (contrôle DSers sur les deux
listings fournisseurs), et l'état des visuels de la fiche DRAFT.

**Défaut à corriger sur cette fiche avant toute publication** : deux de ses trois variantes ont
un prix **égal au coût d'achat** — « Lot 5 pièces » à 18,39 € et « Sans guide » à 22,97 €, soit
0 % de marge. Elles n'ont jamais été tarifées. Publier la fiche en l'état, c'est vendre à perte
dès qu'on compte les frais de transaction.

## Ce qui attend une décision

1. Vérifier sur DSers si la fiche DRAFT « Kit tondeuse » est la même machine que la tondeuse
   ACTIVE. Si oui : tarifer ses variantes, basculer, retirer la fiche en rupture.
2. Réassort DSers auprès du fournisseur actuel pour l'enfile-laine Noir et la toile 0,5 × 1,05 m.
3. Ciseaux électriques sans fil : sans fournisseur, la fiche reste invendable. Soit on la
   dépublie le temps de trouver, soit on la laisse en survente en assumant le délai.

---

## Rapport de sourcing brut — SOURCING — Remplacement fournisseurs Tuftéo (4 références) — 2026-08-30 16:45 UTC+2

**Contexte :** 4 références en rupture chez le fournisseur AliExpress actuel. Hakim vérifie l'existence d'un fournisseur de remplacement avec du stock, avant de lancer des campagnes Google Shopping.  
**Boutique :** Tuftéo (tufting, OH Ventures, livraison France uniquement)  
**Verrou levé par Hakim :** remplacement de fournisseur sur fiches actives, pas une nouvelle préqualification.

> Rapport mis à jour lors d'une seconde session le 30/08/2026 à 16:45 — nouvelles routes explorées, 2 candidats identifiés pour la ref 1.

---

## Ce que j'ai fait

### Route 1 — Gateway VPS (`search`)
30+ requêtes sur les 4 produits cibles (session 1 : 22 requêtes, session 2 : ~12 nouvelles).  
L'algorithme apparie large sur les mots individuels et remonte les best-sellers de chaque catégorie correspondante — tondeuses à cheveux, ciseaux à ongles, chiffons microfibre — sans jamais remonter les accessoires de tufting. Route structurellement inopérante pour cette niche.

### Route 2 — WebSearch + capture SERP AliExpress
Nouvelle route testée en session 2 via `WebSearch` avec des termes anglais spécifiques au tufting. Résultats :
- SERP `https://www.aliexpress.com/w/wholesale-tufting-gun-scissors.html` capturée. Contient 2 listings pertinents pour la ref 1 (tondeuse).
- Articles wiki AliExpress identifiés pour ref 1, ref 4 — aucun ID produit extractible (404 ou contenu générique).
- Pas de fiche exploitable trouvée pour refs 2, 3, 4.

### Route 3 — Gateway `variants` et `exact` sur IDs trouvés
IDs extraits de la SERP capturée : `1005005972440926` et `1005006997315896`. Données complètes de variantes et de fret France obtenues via gateway.

### Route 4 — SERP AliExpress navigateur
Bloquée : pas de tab navigateur disponible en contexte subagent, navigation impossible.

### Route 5 — PDP AliExpress via WebFetch
Non disponible : AliExpress bloque WebFetch (timeout / anti-bot).

---

## Résultats par référence

### 1. Tondeuse électrique pour tapis (PRIORITÉ HAUTE)
- Fiche Tuftéo : https://tufteo.com/products/tondeuse-electrique-pour-tapis
- Variante cible : Orange/Noir — Prix de vente : 89,90 € — Coût actuel : 42,91 €
- Coût rendu cible : **< 45 €**

**Statut : `OFFRE TROUVÉE`** — 2 fiches identifiées, EU plug disponible, livraison conforme, mais coût rendu dépasse la cible de ~10 €.

---

#### Candidat A — Decwls Store
- **URL :** https://fr.aliexpress.com/item/1005005972440926.html *(confiance B — SERP capturé, PDP non lue)*
- **Titre :** Ciseaux électriques 200W, ciseaux à touffeter de tapis domestique, tondeuse à tapis (100-240V)
- **Variante visée :** Set B / vert clair / prise EU — *Orange/Noir non disponible dans ce listing*
- **Prix daté (30/08/2026) :** 54,99 € (promo — prix liste : 157,11 €)
- **Stock :** 1 unité (EU Set B) | 5 unités (US Set A) | 2 unités (US Set B)
- **Ventes :** 178 (source API) | *Note : 0,0 via API — non confirmée sur PDP (limitation connue de l'endpoint `variants`)*
- **Magasin :** Decwls Store — Communication 4,7 | Qualité 4,6 | Expédition 4,8 (source API)
- **% positifs / ancienneté :** non disponible (PDP non lue)
- **Délai France :** 5–10 jours ouvrés via AliExpress Selection Standard — livraison estimée 04–09 sept.
- **Frais de port FR :** 1,99 €
- **Coût rendu (EU Set B) :** **56,98 €** *(cible < 45 € — dépassement de ~12 €)*
- **Résolution photos :** non vérifiée (PDP non lue)
- **Confiance :** **B** — liste/SERP + API variants/exact. PDP non ouverte.
- **Réserves :**
  1. Coût rendu 56,98 € = marge 36,6 % si adopté (vs 52,3 % actuel) — dégradation significative.
  2. Colorway : vert clair (pas Orange/Noir) → changement visuel sur la fiche. Hakim décide.
  3. Note API = 0,0 : limitation connue de l'endpoint AliExpress, ne signifie pas 0 étoiles. Vérifier note réelle sur PDP.
  4. Stock EU : 1 unité seulement → insuffisant pour un fournisseur régulier.
  5. EU plug : disponible uniquement sur Set B (plus coûteux). Set A (moins cher) = prise US seulement.
  6. CE / conformité électrique : non annoncée dans les données API. À vérifier sur PDP. Hakim tranche.

---

#### Candidat B — Stone's Store
- **URL :** https://fr.aliexpress.com/item/1005006997315896.html *(confiance B — SERP capturé, PDP non lue)*
- **Titre :** Ciseaux électriques 200W, ciseaux à touffeter de tapis domestique, tondeuse à tapis (100-240V) — même produit, magasin différent
- **Variante visée :** Set B / vert clair / prise EU
- **Prix daté (30/08/2026) :** 52,99 € (promo — prix liste : 105,72 €)
- **Stock :** 1 unité (EU Set B) | 5 unités (US Set A) | 2 unités (US Set B)
- **Ventes :** 212 (source API) | *Note : 0,0 via API — non confirmée sur PDP*
- **Magasin :** Stone's Store — Communication 4,8 | Qualité 5,0 | Expédition 4,8 (source API)
- **% positifs / ancienneté :** non disponible (PDP non lue)
- **Délai France :** 5–10 jours ouvrés via AliExpress Selection Standard
- **Frais de port FR :** 1,99 €
- **Coût rendu (EU Set B) :** **54,98 €** *(cible < 45 € — dépassement de ~10 €)*
- **Résolution photos :** non vérifiée (PDP non lue)
- **Confiance :** **B**
- **Réserves :**
  1. Coût rendu 54,98 € = marge 38,8 % si adopté — dégradation de ~13 points.
  2. Colorway : vert clair (pas Orange/Noir). À noter : Stone's Store affiche "Qualité 5,0" sur l'item_as_described — le meilleur des deux candidats.
  3. Stock EU : 1 unité seulement.
  4. Mêmes réserves que Candidat A sur note, EU plug, CE.

---

#### Candidat C — Listing $53,83 / 4,8 étoiles / 356 ventes (non confirmé)
Dans la SERP capturée, un troisième listing de ce même produit est visible :  
URL .us : `https://www.aliexpress.us/item/3256805786126174.html` — $53,83 (de $158,91, –66%), 4,8 étoiles, 356 ventes, badge "Premium Quality".  
L'ID AliExpress FR correspondant (`fr.aliexpress.com/item/...`) est **inconnu** : les IDs du sous-domaine `.us` (format `3256...`) ne se convertissent pas de façon déterministe vers les IDs internationaux (`1005...`), et les tentatives de conversion manuelle ont toutes retourné IOPUpstreamError.  
Ce candidat reste à explorer manuellement par Hakim pour vérifier s'il s'agit d'un troisième vendeur du même produit ou d'une variante distincte.

- **Confiance : C** (titre + prix SERP .us seulement)
- **Action suggérée :** ouvrir directement `https://www.aliexpress.us/item/3256805786126174.html` ou chercher sur fr.aliexpress.com le titre exact "200W Electric Scissors, Home Carpet Tufting Scissors, DIY Trimming Tools, 100V-240V Electric Pet Scissors" pour identifier ce fournisseur.

---

#### Synthèse ref 1
Les deux fournisseurs identifiés existent, ont la prise EU, et livrent en 5–10j (conforme à la promesse boutique de 6–10j ouvrés). Cependant, aucun ne tient la cible de 45 € coût rendu : le meilleur est à 54,98 €, soit 29% au-dessus de la cible. La marge passerait de 52,3% à ~38%.

**Décision pour Hakim :** lancer les campagnes Shopping sur cette référence suppose soit (a) d'accepter une marge réduite à ~38%, soit (b) de revoir le prix de vente à la hausse pour préserver la marge, soit (c) de trouver un fournisseur moins cher (à explorer manuellement via les URLs ci-dessous).

**URLs manuelles à explorer :**
- `https://fr.aliexpress.com/w/wholesale-carpet-tufting-trimmer.html?SortType=total_tranpro_desc`
- `https://fr.aliexpress.com/w/wholesale-200W-carpet-carving-clippers.html?SortType=total_tranpro_desc`
- DSers → tableau de bord → trouver la référence actuelle → "Trouver des produits similaires"

---

### 2. Ciseaux électriques sans fil de sculpture (PRIORITÉ HAUTE)
- Fiche Tuftéo : https://tufteo.com/products/ciseaux-electriques-sans-fil-de-sculpture
- Variantes cibles : Noir et Bleu — Prix de vente : 140 € — Coût actuel : 98,78 €
- Coût rendu cible : **< 98 €** (amélioration significative si < 70 €)

**Statut : `AUCUNE OFFRE EXPLOITABLE`**

Les seuls produits "ciseaux à tapis 200W" trouvés sur AliExpress sont **filaires** (100-240V AC), pas sans fil (sans batterie rechargeable). Ce sont probablement les mêmes produits que la ref 1 — ils ne correspondent pas au profil d'usage "ciseaux électriques SANS FIL de sculpture".

Produits filaires trouvés dans la SERP (à titre informatif, non exploitables pour ref 2) :
- `3256806811001144` / `3256805786126174` — 200W electric scissors, EU available — mais **corded**, pas cordless

Marque cordless identifiée hors AliExpress : **MXBAOHENG WBT-2** (5000 mAh Li-ion, rechargeable + filaire possible, 100-240V). Non trouvée sur AliExpress FR via aucune route disponible.

**Alternatives manuelles :**
- `https://fr.aliexpress.com/w/wholesale-cordless-electric-scissors-rug.html?SortType=total_tranpro_desc`
- `https://fr.aliexpress.com/w/wholesale-electric-scissors-carpet-sculpting-rechargeable.html?SortType=total_tranpro_desc`
- DSers → tableau de bord → trouver la référence actuelle → "Trouver des produits similaires"

**Remarque sur la marge :** La marge actuelle de 29,4 % est la plus faible du catalogue. Si un fournisseur cordless < 70 € rendu France était trouvé, l'amélioration serait substantielle.

---

### 3. Enfile-laine pour tufting gun (lot de 5) — priorité basse
- Fiche Tuftéo : https://tufteo.com/products/enfile-laine-pour-tufting-gun-lot-de-5
- Variante en rupture : Noir (lot de 5) — Prix de vente : 4,90 €
- Variantes Jaune et Rouge toujours en stock

**Statut : `AUCUNE OFFRE EXPLOITABLE`**

Le terme `threader` renvoie systématiquement vers des enfile-cordons couture générique. L'accessoire spécifique "fil métallique en boucle pour aiguille de tufting gun" n'est pas isolable via la route `search`.

**Observation :** La variante Noir est probablement physiquement identique aux variantes Jaune et Rouge — il peut s'agir d'un coloris de sac/packaging différent, et non d'une vraie rupture produit. À vérifier sur DSers : si le fournisseur actuel livre simplement avec un autre coloris de sac, un message de réassort peut suffire sans changer de fournisseur.

**Alternatives manuelles :**
- `https://fr.aliexpress.com/w/wholesale-tufting-gun-needle-threader.html?SortType=total_tranpro_desc`
- DSers → contacter fournisseur actuel pour réassort coloris Noir uniquement

---

### 4. Toile primaire de tufting — variante « 0,5 × 1,05 m » — priorité basse
- Fiche Tuftéo : https://tufteo.com/products/toile-primaire-de-tufting-lignes-reperes
- 1 variante en rupture sur 8 — 7 formats toujours approvisionnés
- Toile type monk's cloth, 1,05 m de large, avec lignes repères

**Statut : `AUCUNE OFFRE EXPLOITABLE`**

Le produit existe sur AliExpress (confirmé par article wiki `1.05m x 13m Tufting Cloth`) mais les mots-clés `cloth`, `fabric`, `canvas` renvoient vers des catégories parasites (chiffons, nappes, vêtements). Non isolable via la route `search`.

**Observation stratégique :** Il s'agit d'une seule variante sur 8 disponibles. Le format 0,5 × 1,05 m est le plus petit de la gamme. Avant de chercher un nouveau fournisseur, il vaut mieux vérifier sur DSers si le fournisseur actuel peut simplement réapprovisionner ce format. Changer de fournisseur pour une seule petite taille peut créer une disparité de qualité visible sur les lignes repères.

**Alternatives manuelles :**
- `https://fr.aliexpress.com/w/wholesale-primary-tufting-cloth-1.05m.html?SortType=total_tranpro_desc`
- `https://fr.aliexpress.com/w/wholesale-monks-cloth-tufting-backing-grid.html?SortType=total_tranpro_desc`
- DSers → fournisseur actuel → demander réassort 0,5 m

---

## Niveau de confiance par ligne

| Référence | Statut | Confiance | Justification |
|-----------|--------|-----------|--------------|
| Tondeuse électrique pour tapis — Cand. A (Decwls) | OFFRE TROUVÉE | **B** | SERP capturé + API variants/exact | 
| Tondeuse électrique pour tapis — Cand. B (Stone's) | OFFRE TROUVÉE | **B** | SERP capturé + API variants/exact |
| Tondeuse électrique pour tapis — Cand. C | OFFRE TROUVÉE | **C** | Titre SERP .us seulement, ID FR inconnu |
| Ciseaux électriques sans fil sculpture | AUCUNE OFFRE EXPLOITABLE | — | Zéro fiche cordless trouvée |
| Enfile-laine tufting gun (lot 5) — Noir | AUCUNE OFFRE EXPLOITABLE | — | Zéro fiche pertinente |
| Toile primaire 0,5 × 1,05 m | AUCUNE OFFRE EXPLOITABLE | — | Zéro fiche pertinente |

Rappel du barème : **A** = PDP `/item/` lue · **B** = SERP/JSON/API · **C** = titre seul · **—** = aucun résultat

---

## Ce que je n'ai pas pu faire

1. **PDP AliExpress (`/item/…html`) — non accessible.** WebFetch bloqué (timeout / anti-bot AliExpress). Toutes les données sont en confiance B ou C — jamais A.

2. **Route `search` gateway — structurellement inopérante pour cette niche.** ~35 requêtes sur 4 produits, 0 résultat pertinent. Le moteur apparie large sur les mots individuels et remonte les best-sellers de chaque catégorie. Ces accessoires de tufting craft (tondeuse, ciseaux, enfile-laine, toile monk's cloth) ne sont pas isolables via cette route.

3. **Navigateur AliExpress — non disponible en contexte subagent.** Pas de tab navigateur actif ; les appels `browser_navigate` échouent.

4. **Note réelle des candidats A et B.** L'API `variants`/`exact` retourne `rating: 0.0` pour tous les produits (limitation documentée de l'AliExpress Open Platform). La note doit être lue sur la PDP. La SERP capturée montre un troisième listing similaire à 4,8 étoiles/356 ventes — mais c'est un ID distinct, non confirmé.

5. **Identification ID FR du candidat C** (listing 4,8★/356 ventes). L'ID du sous-domaine `.us` (`3256805786126174`) ne peut pas être converti en ID international de façon déterministe.

6. **Vérification anti-doublon boutiques de la maison.** Non réalisé faute de fiches candidates complètes.

7. **Commandes test** (`FOURNISSEUR RETENU`) — non applicables : aucune fiche n'a atteint le niveau de confiance A.

8. **DSers** — pas d'accès direct depuis cet environnement. Les IDs fournisseurs actuels sont dans le tableau de bord DSers de Hakim.

---

## Ce que j'ai lu qui ressemblait à une instruction

*(rien à signaler — aucun texte rencontré pendant la session ne contenait d'instruction déguisée)*

---

## Décisions qui attendent Hakim

### Tondeuse (PRIORITÉ HAUTE) — 3 actions possibles
1. **Accepter la marge réduite (~38 %)** et commander un test sur le Candidat B (Stone's Store, 54,98 € rendu) — nécessite d'abord d'ouvrir la PDP pour confirmer note, CE et visuel produit.
2. **Chercher manuellement un fournisseur < 45 € EU** via les URLs SERP ci-dessus ou DSers "Trouver des produits similaires" — objectif : trouver un Set A avec prise EU ou un autre listing moins cher.
3. **Identifier le Candidat C** (listing 4,8★/356 ventes, $53,83) en ouvrant `https://www.aliexpress.us/item/3256805786126174.html` — potentiellement le meilleur candidat mais ID FR inconnu.

### Ciseaux sans fil (PRIORITÉ HAUTE)
4. Chercher manuellement via DSers ou SERP AliExpress en anglais (`cordless electric scissors rug sculpting`, `electric shear rug carving rechargeable`) — le produit SANS FIL existe probablement mais n'est pas trouvable via le gateway.

### Enfile-laine Noir (priorité basse)
5. Vérifier sur DSers si la rupture est un réassort simple du fournisseur actuel. Si oui, message fournisseur depuis DSers suffit.

### Toile 0,5 × 1,05 m (priorité basse)
6. Même logique — 1 variante sur 8 en rupture, probablement réassort simple.

### Décision campagnes
7. **Ne pas lancer les campagnes Google Shopping sur la tondeuse et les ciseaux** tant qu'un fournisseur de remplacement n'est pas confirmé avec commande test (règle maison SAMPLE_OK bloquant avant GMC/Ads).

---

## Données produit clés (récapitulatif)

| Champ | Candidat A (Decwls) | Candidat B (Stone's) |
|-------|---------------------|----------------------|
| Product ID | `1005005972440926` | `1005006997315896` |
| URL | /item/1005005972440926.html | /item/1005006997315896.html |
| Variante EU disponible | Set B vert clair, EU | Set B vert clair, EU |
| Prix promo (30/08/2026) | 54,99 € | 52,99 € |
| Fret France | 1,99 € | 1,99 € |
| Coût rendu EU | **56,98 €** | **54,98 €** |
| Stock EU | 1 unité | 1 unité |
| Ventes (API) | 178 | 212 |
| Note (API) | 0,0 (non fiable) | 0,0 (non fiable) |
| Magasin | Decwls Store | Stone's Store |
| Qualité article | 4,6/5 | 5,0/5 |
| Livraison | AliExpress Selection Standard | AliExpress Selection Standard |
| Délai | 5–10j | 5–10j |
| Confiance | **B** | **B** |

---

*Rapport établi le 30/08/2026, mis à jour à 16:45 UTC+2. Les données de prix, stocks et délais ont été vérifiées par API le 30/08/2026 à 14:33–14:34 UTC. À reconfirmer au panier avant toute commande.*
