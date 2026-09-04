# Phase 5 — Économie A6 rasoir de sûreté — 2026-09-04 23:52 CEST

Rapport de **marge contributive avant Ads** (jamais l’écart prix de vente − prix fournisseur). Aucune commande, aucun panier, aucun contact vendeur, aucune modification Shopify / Ads / GMC. Aucune décision humaine. Chemin versionné : ce fichier. Copie locale datée aussi écrite sous `reports/phase5-marge-rasoir-surete-2026-09-04.md` (le dossier `reports/` est dans le `.gitignore` du dépôt : pas de `git add -f`).

Calculs reproduits par `economie-calculs.py` (arrondi commercial au centime, `ROUND_HALF_UP`). Tables : `economie-calculs.csv`, `economie-calculs.json`.

## 1. Entrée

| Champ | Valeur | Statut |
|---|---|---|
| Candidat | A6 — rasoir de sûreté, kit débutant en option | registre 04/09 |
| Préqualification | `REVIEW_PREQUALIFICATION` | réel daté registre — **pas** un `PASS_PREQUALIFICATION` |
| Mode | PRODUIT PUR / Search, France | critères 01/09 |
| Fourchette prix critères | 50–400 € TTC | réel daté `PRODUCT-RESEARCH-CRITERIA.md` |
| Budget publicitaire hebdomadaire des critères | **non chiffré** dans ce fichier | à confirmer |

**Phase 3 / demande / prix SERP**

- Dossier A6 03/09 : `analyses/2026-09-03-qualification-9-produits-pur/dossiers/A6.md`
- Approfondissement 04/09 : `analyses/2026-09-04-approfondissement-rasoir-surete/README.md`
- Volumes : proxy cœur **13 180**/mois (DataForSEO 03/09). Seuil canonique 12 500. **Pas de nouvelle mesure le 04/09** (`40200 Payment Required`). Les 13 180 mesurent les rasoirs de sûreté, **pas** les kits à 99 € (`kit rasoir de sûreté` = 40 ; `rasoir de surete debutant` = 20).
- CPC DataForSEO tête pondérée dossier A6 : **0,926 USD** → **0,798 €** au change BCE du 03/09 (1 EUR = 1,1615 USD). Recalcul brut 0,926 / 1,1615 = **0,797 €**. Ce n’est **pas** un CPC de campagne OH Ventures.
- Prix PDP concurrents 04/09 (pas de checkout) : Lamier rasoir **69 €** ([lelamier.com/products/lamier](https://lelamier.com/products/lamier)) ; kit **99 €** ([le-kit-complet-lamier](https://lelamier.com/products/le-kit-complet-lamier)) et **119 €** depuis le menu ([kit-de-rasage-lamier](https://lelamier.com/products/kit-de-rasage-lamier)) ; Le Bouc coffret **99,72 €** ; Le Bouc rasoir **34,90 €** ; Bambaw PDP **21,15 €** (carte Shopping historique 20,98 €).

**Phase 4 / coût rendu**

- Détail : `analyses/2026-09-04-approfondissement-rasoir-surete/sourcing-exact.md`
- Synthèse : `reports/phase4-sourcing-rasoir-surete-2026-09-04.md`
- SKU retenu : [1005010200339194](https://fr.aliexpress.com/item/1005010200339194.html) variante `20AL01-A01Y-Grey`, **29,79 €** le 04/09/2026 23:42 CEST, port FR **0 € annoncé**, Choice, délai annoncé 9–14 sep. 2026. Contenu **écrit** : rasoir + 5 lames. Support **non écrit**. Panier **non ouvert**. Statut phase 4 : `FOURNISSEUR À TESTER`.
- Alternatives PDP A : K23 **27,79 €** sans lames ; A99-silvery **32,39 €** rasoir seul (promo jusqu’au 07/09/2026 23:59 CET).

**Hypothèses de prix de vente (aucune n’est un prix OH Ventures)**

| Scénario | Prix TTC | Ancrage observé | Comparabilité au SKU sourcé |
|---|---:|---|---|
| Prix réaliste du SKU | 69,00 € | Rasoir Lamier 04/09 | Plus proche : rasoir + 5 lames vs rasoir d’entrée. Bambaw 21,15 € et Bouc 34,90 € sont plus bas. |
| Ancrage kit observé | 99,00 € | Lamier kit 99 € + Bouc 99,72 € | **Non comparable** : kits observés = rasoir + accessoires (blaireau / support / étui / savon selon page). SKU sourcé = rasoir + 5 lames **annoncées**. |
| Ancrage kit menu | 119,00 € | Lamier kit menu 04/09 | Même réserve de contenu. |

Un kit **équivalent Lamier** (rasoir + blaireau + support + étui) n’a **pas** de coût rendu daté : incalculable ici.

## 2. Calcul détaillé par candidat

Cadre SASU / OH Ventures : TVA au réel, HT, IS. Prestataire de paiement et plan Shopify **non lus sur contrat** dans cette passe.

**Formule** (même chaîne que `economics.py` du 04/09, coût désormais renseigné) :

`marge contributive avant Ads` = `TTC / 1,20` − frais de paiement − provision retours/SAV − coût rendu − emballage.

`CPA max` = cette contribution (seuil où la vente hors Ads ne perd plus d’argent **avant** coûts fixes). L’IS 25 % s’applique au résultat fiscal, **pas** au CPA max ; une illustration « si Ads = 0 » figure en annexe JSON, ce n’est pas un indicateur de lancement.

### 2.1 Lignes de coût — SKU kit lames 29,79 €

| Ligne | Montant | Statut | Source / portée |
|---|---:|---|---|
| Coût produit + port affiché | 29,79 € | réel daté **affiché PDP**, pas panier | 04/09/2026 23:42 CEST ; TVA incluse **annoncée** ; « droits de douane calculés lors du paiement » **non chiffrés** |
| Douane / ajustement checkout | 0,00 € dans le calcul | à confirmer | Interdit d’ouvrir le panier dans cette phase |
| TVA achat récupérable | non | hypothèse déclarée | Aucune facture AliExpress avec TVA FR récupérable observée → le 29,79 € est traité **TTC non déductible**. Contre-hypothèse (si récupérable) : coût HT 24,83 €, contribution 99 € = 51,09 € — **non retenue** |
| TVA collectée à 69 / 99 / 119 € | 11,50 / 16,50 / 19,83 € | hypothèse déclarée | Taux 20 % France, régime SASU annoncé, liasse non lue ici |
| Frais paiement Stripe | 1,4 % + 0,25 € | hypothèse déclarée, à confirmer contrat | Barème indicatif du rôle phase 5, cartes UE |
| Frais paiement PayPal (prudent) | 2,9 % + 0,35 € | hypothèse déclarée, à confirmer contrat | Idem |
| Barème A6 03/09 | 2 % + 0,30 € | hypothèse déclarée (continuité) | `dossiers/A6.md` — pas une facture |
| Provision retours/SAV | 5 % du TTC (central) ; 8 % (prudent) ; 3 % (favorable) | hypothèse déclarée | Aucun taux de retours OH Ventures observé. Lames = hygiène : un taux réel peut s’écarter fortement |
| Emballage / recomposition | 0,00 € central (dropship Choice) ; 2,00 € prudent | hypothèse déclarée | Aucun colis maison observé |
| Coût d’un retour aller **et** retour | non chiffré | à confirmer | Choice : retour 90 j. annoncé. Un retour FR → filière AliExpress peut dépasser le 29,79 € |
| Plan Shopify, apps, outils | non imputés à la commande | à confirmer | Boutique A6 **non créée**. Aucun montant de compte lu |

Écart 99,00 − 29,79 = 69,21 € : **ce n’est pas une marge contributive**. Il ignore TVA, paiement, SAV, retours, Ads, fixes.

### 2.2 Scénarios prudent / central / favorable

Arrondis au centime. CPC prudent = 1,20 € (stress du README 04/09). CPC central/favorable = 0,798 € (dossier A6).

| Scénario | Prix TTC | Paiement | SAV | Emballage | Coût | CA HT | Marge contributive avant Ads = CPA max |
|---|---:|---|---:|---:|---:|---:|---:|
| **Prudent** — SKU à 69 € | 69,00 € | PayPal 2,35 € | 8 % → 5,52 € | 2,00 € | 29,79 € | 57,50 € | **17,84 €** |
| **Central SKU** — prix réaliste 69 € | 69,00 € | Stripe 1,22 € | 5 % → 3,45 € | 0,00 € | 29,79 € | 57,50 € | **23,04 €** |
| **Central 99 €** — ancrage kit, contenu non équivalent | 99,00 € | Stripe 1,64 € | 5 % → 4,95 € | 0,00 € | 29,79 € | 82,50 € | **46,12 €** |
| Continuité barème A6 03/09 à 99 € | 99,00 € | 2,28 € | 4,95 € | 0,00 € | 29,79 € | 82,50 € | **45,48 €** |
| **Favorable** — 119 € | 119,00 € | Stripe 1,92 € | 3 % → 3,57 € | 0,00 € | 29,79 € | 99,17 € | **63,89 €** |
| Stress 99 € PayPal SAV 8 % | 99,00 € | 3,22 € | 7,92 € | 0,00 € | 29,79 € | 82,50 € | **41,57 €** |

**Contrôle de continuité** avec le README 04/09 : à 99 €, barème A6, hors coût produit, le plafond « produit + port » à CPC 0,80 € / CVR 2 % recalculé = **35,27 €** (identique au README). Le 29,79 € affiché est **sous** ce plafond de **5,48 €**. Ce contrôle valide l’arithmétique, **pas** le prix 99 € ni la CVR 2 %.

### 2.3 Alternatives sourcées (pas le brief kit lames)

| Offre | Coût affiché | Prix testé | Marge contributive avant Ads (Stripe, SAV 5 %, pack 0) |
|---|---:|---:|---:|
| K23 rasoir + support, **sans lames** | 27,79 € | 99,00 € | 48,12 € |
| A99-silvery rasoir seul (promo 07/09) | 32,39 € | 69,00 € | 20,44 € |

K23 ne remplace pas le kit débutant. A99 : prix promotionnel à expiration.

### 2.4 Kit complet type Lamier

**Incalculable.** Blaireau, support écrit, étui, savon : pas de SKU unique daté. Additionner des fiches isolées du 03/09 (Yaqi 24,39 € + brosse 12,19 €) était déjà au-dessus du plafond 35 € **avant** port, lames, support et coffret — et ces fiches ne sont pas le sourcing du 04/09 au soir.

## 3. Indicateurs

CVR 1 / 1,5 / 2 / 3 % = **scénarios**, aucun seuil canonique, aucune CVR OH Ventures.

### 3.1 CAC d’équilibre vs CPC proxy

| Scénario | CPA max | CPC utilisé | CVR d’équilibre | Clics / vente à l’équilibre |
|---|---:|---:|---:|---:|
| Prudent 69 € | 17,84 € | 1,20 € | 6,73 % | 14,87 |
| Central SKU 69 € | 23,04 € | 0,798 € | **3,46 %** | 28,88 |
| Central 99 € | 46,12 € | 0,798 € | **1,73 %** | 57,80 |
| Favorable 119 € | 63,89 € | 0,798 € | 1,25 % | 80,06 |
| Stress 99 € | 41,57 € | 1,20 € | 2,89 % | 34,64 |

### 3.2 Contribution **après** Ads (CPA scénario = CPC / CVR)

Négatif = la vente **perd de l’argent** après acquisition dans ce couple CPC/CVR, **avant** coûts fixes.

| Scénario | CVR 1 % | CVR 1,5 % | CVR 2 % | CVR 3 % |
|---|---:|---:|---:|---:|
| Prudent 69 € / CPC 1,20 | −102,16 € | −62,16 € | −42,16 € | −22,16 € |
| Central SKU 69 € / CPC 0,798 | −56,76 € | −30,16 € | −16,86 € | **−3,56 €** |
| Central 99 € / CPC 0,798 | −33,68 € | −7,08 € | **+6,22 €** | +19,52 € |
| Favorable 119 € / CPC 0,798 | −15,91 € | +10,69 € | +23,99 € | +37,29 € |
| Stress 99 € / CPC 1,20 | −78,43 € | −38,43 € | −18,43 € | +1,57 € |

Lecture contrainte :

1. Au **prix réaliste du SKU (69 €)**, même une CVR 3 % au CPC proxy **ne couvre pas** l’acquisition Search. La thèse « rasoir 69 €, Search seul, coût 29,79 € » est **arithmétique défavorable** sous ces hypothèses.
2. Au **99 €**, la contribution après Ads ne devient positive qu’autour de **CVR 2 %** au CPC 0,798 € (+6,22 €), et reste négative à 1,5 %. Ce n’est pas une preuve que 2 % est atteignable face à Lamier / Proraso / Rasage Classique déjà en Search le 04/09.
3. CPC campagne **MANQUANT**. Si le CPC réel s’approche de 1,20 €, le 99 € exige ~2,9 % de CVR (stress).

### 3.3 Budget test indicatif

Le fichier de critères **ne fixe pas** de budget hebdomadaire. Aucun budget n’est engagé ici.

| Élément | Valeur | Statut |
|---|---|---|
| Ventes pour conclure (ordre de grandeur Search) | 15 ventes sur l’offre testée | hypothèse déclarée, pas un gate |
| CPA scénario central 99 € à CVR 2 % | 39,90 € | hypothèse (0,798 / 0,02) |
| Enveloppe 15 × 39,90 € | 598,50 € | hypothèse déclarée |
| Enveloppe 15 × CPA max 46,12 € | 691,80 € | plafond d’équilibre, pas une cible de dépense |
| Test Search à 69 € | **non soutenable** sous les hypothèses : contribution après Ads encore négative à CVR 3 % | calcul |

Quinze ventes ne prouvent pas un ROAS ; elles permettent seulement de voir si la CVR observée dépasse 1,73 % à 99 €. Compteurs campagne (CTR, CPC, CVR, CPA) : **MANQUANT**.

## 4. Faisabilité opérationnelle

| Sujet | Constat | Statut |
|---|---|---|
| Poids / dimensions SKU kit | non lus sur la PDP retenue | à confirmer. A99 JSON-LD 43×23×103 mm = **annoncé vendeur** sur une **autre** fiche |
| Casse | rasoir métal + lames : casse faible vs verre ; lames = objet tranchant | hypothèse qualitative |
| Emballage | dropship Choice, photos fournisseur **non publiables** telles quelles | réel daté sourcing |
| Stock | **12** pièces annoncées | réel daté PDP ; trop bas pour un test Ads |
| Délai FR | 9–14 sep. 2026 annoncé (~5–10 j.) | réel daté affiché, pas un colis reçu |
| Origine d’expédition kit | **non écrite** dans la modale | à confirmer |
| Consommables | 5 lames **annoncées**, marque / DE **non identifiées** ; réachat lames non chiffré | ne pas financer un CAC déficitaire par une LTV lames |
| Pièces / filetage / géométrie douce | **non mesurés** | `SAMPLE_OK` hors phase ; douceur « annoncée nulle part de façon mesurable » (sourcing) |
| SAV débutant | charge pédagogique élevée ; Lamier a déjà un SAV cité dans des avis Trustpilot **non vérifiés ici** | hypothèse |
| Retour aller+retour | coût non mesuré ; hygiène lames | à confirmer |
| Responsabilité produit | coupure, lame cassée, allégation « zéro coupure » interdite par le dossier A6 | à instruire avant mise en vente |
| Conformité | non électrique ; CE/étiquetage lames **non observés** | à confirmer sur échantillon |
| Vendeur | Shop1105186411, 35 abonnés, 98,1 % positifs, ≠ magasin Hakim 1104699287 | réel daté |

## 5. Droit de gagner

**Éléments observés qui existent :** demande Search générique au-dessus du seuil proxy (13 180 vs 12 500, chevauchements non tranchés) ; fit pédagogique Search ; coût affiché 29,79 € sous le plafond 35,27 € du scénario 99 € / CVR 2 % / CPC 0,80 ; Lamier montre qu’une jeune marque **peut** scaler du trafic (TrendTrack ~287 k visites estimées, juillet, sans preuve de profit).

**Pourquoi c’est insuffisant pour défendre l’offre sourcée :**

- Lamier, Proraso, La Fourche, Trendhim, Rasage Classique **achètent** déjà `rasoir de surete` / `…homme` / `…debutant` le 04/09 (`observations-navigateur.json`). Rasage Classique envoie la requête débutant vers un **guide**, pas seulement une PDP.
- Le SKU à 29,79 € n’est pas le kit 99/119 € observé. Vendre 99 € un rasoir + 5 lames face à un coffret blaireau/support/étui n’est pas le même produit.
- Vendre 69 € (produit plus comparable) **ne finance pas** le Search au CPC proxy, même à CVR 3 %.
- Bambaw ~21 € et Bouc 34,90 € ancrent un plancher bas sur le rasoir seul.
- Géométrie douce, lames DE, support : non prouvés. Sans ça, la thèse « parcours débutant » reste une hypothèse du dossier A6, pas un actif.

## 6. Recommandation technique

**`TECHNICAL_WATCH`**

Pas `TECHNICAL_PASS` : le prix réaliste du SKU ne porte pas Google Ads Search ; le 99 € n’est pas comparable au contenu ; concurrence Search observée ; panier, TVA fournisseur, CPC campagne, douceur et lames manquent. Pas `TECHNICAL_FAIL` global : à 99 € le 29,79 € passe le plafond historique 35,27 € et la contribution après Ads peut être positive **si** une CVR ≥ ~2 % **et** un prix kit sont défendables — deux si non démontrés. Pas `TECHNICAL_INCONCLUSIVE` au sens strict du rôle (coût affiché **daté**, CPC proxy phase 3 **présent**, concurrence **examinée**) ; les trous restants sont des **réserves**, pas une absence de phase 3/4.

Réserves (bloquantes pour une décision humaine, pas pour ce verdict technique) :

1. Coût rendu **non reconfirmé au panier** (douane).
2. Contenu colis (5 lames DE, support) non ouvert.
3. Prix 99 € non justifié par le SKU.
4. CPC / CVR campagne MANQUANT.
5. Préqualification toujours `REVIEW`, investigation sourcing sans PASS rétroactif.
6. Stock 12, vendeur 35 abonnés.

Le mot de lancement commercial n’est pas employé ici.

## 7. Dossier pour décision humaine

Hakim seul choisit `GO_FINAL`, `WATCH_FINAL` ou `NO_GO_FINAL`. Ce rapport ne choisit pas.

**Pour qu’un `WATCH_FINAL` soit informé (minimum) :** garder A6 en recherche bornée ; ne pas lancer Ads ; ne pas commander un sample via un bot ; trancher d’abord l’offre (rasoir 69 € vs kit réellement complet).

**Preuves qui manquent avant d’envisager un `GO_FINAL` (liste, pas un calendrier) :**

1. Panier FR sur `20AL01-A01Y-Grey` : total TTC, TVA, douane (Hakim).
2. Soit un SKU kit **écrit** rasoir + lames + support/accessoires au coût daté, soit un prix de vente aligné sur le rasoir seul **et** un coût rendu assez bas pour un CPA max compatible Search (aujourd’hui 29,79 € est trop haut pour 69 €).
3. Échantillon : alignement, filetage, corrosion, type de lames, notice (`SAMPLE_OK` selon critères §0.5 — **après** décision humaine, pas avant).
4. Contrôle DataForSEO de la tête quand le quota le permet (le 04/09 a échoué).
5. Contrats Stripe/PayPal et facture fournisseur (TVA récupérable ou non).
6. Politique retours lames / objet tranchant.

**Un `NO_GO_FINAL` serait cohérent si** Hakim refuse de vendre 99 € un rasoir + 5 lames, et refuse d’attendre un kit factory moins cher : le Search à 69 € avec ce coût est défavorable sous les hypothèses chiffrées.

Registre central : **non modifié**.

## Traçabilité

- Critères : `PRODUCT-RESEARCH-CRITERIA.md` (lu 04/09)
- Playbook étape 7 : `PRODUCT-RESEARCH-PLAYBOOK.md`
- Registre : `registre-candidats.md` (lu, non écrit)
- Phase 3 : `analyses/2026-09-03-qualification-9-produits-pur/dossiers/A6.md`
- Concurrence 04/09 : `analyses/2026-09-04-approfondissement-rasoir-surete/README.md`, `observations-navigateur.json`
- Phase 4 : `sourcing-exact.md`, `reports/phase4-sourcing-rasoir-surete-2026-09-04.md`
- Script : `economie-calculs.py` exécuté le 04/09/2026 23:52 CEST

Branche de dépôt : `agents/rasoir-economie-2026-09-04`.
