# PHASE 5 — ÉCONOMIE EXACTE — Sommeil & environnement nocturne — 2026-09-05

Mode : **PRODUIT PUR**. Marché : France. Cadre : SASU / OH Ventures (TVA au réel, IS, HT).

**Arrêt déclaré — entrée non conforme.** Aucun candidat `PASS_PREQUALIFICATION`. Aucun coût rendu daté. Aucun concurrent cartographié par le rôle concurrence. Aucune marge contributive calculée. Aucun CPA maximal. Aucun prix de vente commercial fixé. Aucun `GO_FINAL` / `WATCH_FINAL` / `NO_GO_FINAL`. Registre non modifié.

Recommandation technique : **`TECHNICAL_INCONCLUSIVE`**.

Relevés : **2026-09-05, 08:44–08:55 (heure de Paris)**. Aucune nouvelle SERP, aucun AliExpress, aucun Ads, aucun Shopify.

---

## 1. Entrée

### Rapports bruts relus (2026-09-05)

| Rapport | Branche | Commit | Lecture |
|---|---|---|---|
| Phase 3 demande | `agents/c0-demande-sommeil-2026-09-05` | `731a70c` | Daté du 2026-09-05. Un candidat instruit : **surmatelas à mémoire de forme**. Verdict unique : `REVIEW_PREQUALIFICATION`. Phrase §6 : « Pas de `PASS_PREQUALIFICATION`. Concurrence approfondie et sourcing AliExpress **non autorisés** par ce rapport. » Copie versionnée : `analyses/2026-09-05-chasse-clusters-sommeil-environnement-nocturne/phase3-demande-sommeil-environnement-nocturne-2026-09-05.md`. |
| Phase 4 sourcing | `agents/c0-sourcing-sommeil-2026-09-05` | `0d052b8` | Daté du 2026-09-05. Arrêt : 0 PASS ; aucune URL `/item/` ; aucun coût rendu ; chaîne économie **non ouverte**. Copie versionnée : `…/phase4-sourcing-sommeil-environnement-nocturne-2026-09-05.md`. |
| Phase 4 concurrence | `agents/c0-concurrence-sommeil-2026-09-05` | `22df6fa` | Daté du 2026-09-05. `FAIL_CLOSED`. Zéro concurrent cartographié. Aucun prix lu par ce rôle. Copie versionnée : `…/phase4-concurrence-sommeil-environnement-nocturne-2026-09-05.md`. |

Les trois fichiers existent, sont datés du **2026-09-05**, et sont **conformes à un arrêt** — pas à une due diligence économique.

### Référentiels relus

- `PRODUCT-RESEARCH-CRITERIA.md` (1er septembre 2026) : fourchette 50–400 € TTC ; PRODUIT PUR seuil ~12 500 ; AliExpress uniquement après `PASS_PREQUALIFICATION` écrit ; recommandation technique `TECHNICAL_*` ; le mot GO est réservé à Hakim.
- `PRODUCT-RESEARCH-PLAYBOOK.md` étape 7 (calcul business SASU) : prix fournisseur livré, TVA récupérable ou non, TTC cible, CAC break-even. Sans prix livré, le calcul ne s’ouvre pas.
- `registre-candidats.md` : STOP « Surmatelas thermorégulé actif à eau » (2026-07-17) = **objet distinct**, non étendu. Aucune ligne « surmatelas à mémoire de forme » à modifier. **Registre non modifié.**

### Gate de cette mission

Brief `t_365ec3b5` : « au moins un candidat dispose d’un coût rendu daté exploitable ». **Condition non remplie.**

« Entrée manquante/non conforme = arrêt fail-closed. »

Commentaire kanban du 08:07 (« attendre `t_31ac8679` ») : **caduc** comme dépendance scout (`t_31ac8679` = `done`). Le motif d’arrêt **effectif** est le gate métier : zéro PASS, zéro coût rendu, zéro cartographie.

### Candidats reçus

| Candidat | Phase 3 | Sourcing | Concurrence | Économie |
|---|---|---|---|---|
| *(aucun PASS)* | — | — | — | **non ouverte** |
| Surmatelas à mémoire de forme | `REVIEW_PREQUALIFICATION` | non instruit (aucune `/item/`) | non cartographié | **hors rôle sans pass ni coût rendu** |

### Hypothèses de prix de vente

**Aucune.** Interdit de fixer un prix de vente commercial. Les paliers Shopping/SERP de la phase 3 (cœur DTC observé ≈ 85–260 € TTC, GSB 35–279 €, marketplace souvent < 50 €, 2026-09-05) restent des **notes d’amont**. Le rôle concurrence a écrit qu’ils ne sont **pas** des prix comparables de cartographie. Ils ne deviennent pas des scénarios de vente ici.

Scénarios prudent / central / favorable dans les bandes observées : **non calculés** — un scénario de prix sans coût rendu fabriquerait une fausse économie.

---

## 2. Calcul détaillé par candidat

Aucun candidat admissible. Le tableau ci-dessous documente **l’absence** de chaque ligne. Vocabulaire de statut (obligatoire, une étiquette par ligne) : `réel daté` · `hypothèse déclarée` · `à confirmer`. Aucune ligne n’est `réel daté` (rien n’a été lu sur une PDP ni un contrat ce jour). Aucune ligne n’est une `hypothèse déclarée` chiffrée : une hypothèse chiffrée servirait à calculer, ce qui est interdit sans assiette. Rien n’est interpolé depuis un autre dossier (tufting, rasoir, etc.).

### 2.1 Surmatelas à mémoire de forme — hors chaîne

Cadre SASU rappelé, **non appliqué** faute d’assiette.

| Ligne | Montant | Statut | Source / motif |
|---|---|---|---|
| SKU / variante exacte | — | **à confirmer** | Aucune PDP AliExpress ouverte (phase 4 sourcing, 2026-09-05). |
| Prix fournisseur (annonce vendeur) | — | **à confirmer** | Non relevé. Une caractéristique vendeur ne serait de toute façon pas « vérifiée ». |
| Fret France | — | **à confirmer** | Non relevé. |
| **Coût rendu daté** | — | **à confirmer** | **Manquant.** Gate phase 5 fermé. |
| TVA collectée (vente) | — | **à confirmer** | Pas de prix de vente. Taux FR 20 % n’est pas appliqué à un TTC inventé. |
| TVA déductible (achat) | — | **à confirmer** | Facture AliExpress conforme : non vérifiée (aucun vendeur). Hypothèse prudente usuelle « non récupérable » **non activée** : elle servirait à calculer. |
| Frais de paiement Stripe | — | **à confirmer** | Indicatif skill ≈ 1,4 % + 0,25 € cartes UE — **non appliqué**. Contrats en vigueur non relus ce jour. |
| Frais de paiement PayPal | — | **à confirmer** | Indicatif skill ≈ 2,9 % + 0,35 € — **non appliqué**. |
| Provision retours / remboursements | — | **à confirmer** | Phase 3 note « 100 nuits » chez DTC occupants : **note d’amont**, pas un taux de provision. |
| Provision SAV | — | **à confirmer** | Non chiffrée. |
| Emballage / colis volumineux | — | **à confirmer** | Phase 3 : « colis encombrant. Non chiffré (sourcing). » Sourcing n’a pas chiffré. |
| Coût d’un retour (aller **et** retour) | — | **à confirmer** | Poids / dimensions non relevés. |
| Plan Shopify / apps / outils (fixes mensuels imputables) | — | **à confirmer** | Montants réels du compte non lus (interdit de se connecter). |
| Prix de vente TTC cible | — | **non fixé** | Interdit. Bandes phase 3 non converties en cible maison. |

**Écart prix public − coût fournisseur :** **non calculé** et **non appelé marge**. Interdit.

### 2.2 Autres objets de la famille 9

Matelas, rideau occultant, matelas gonflable, protège-matelas, surmatelas chauffant : **rejets ou hors shortlist** dès la phase 2/3. Non requalifiés. Pas de calcul.

STOP registre « surmatelas thermorégulé actif à eau » : **non rouvert**.

---

## 3. Indicateurs

Tous les indicateurs de sortie sont **explicitement incalculables**. Aucune arithmétique de substitution.

| Indicateur | Valeur | Statut |
|---|---|---|
| Marge contributive par commande (après coût rendu, TVA, paiement, provisions retours/SAV, emballage — **avant Ads**) | **incalculable** | Coût rendu absent. |
| Marge contributive après IS | **incalculable** | Pas d’assiette HT. |
| CPA maximal soutenable | **incalculable** | Identique à la marge contributive avant Ads, qui n’existe pas. |
| CAC break-even vs CPC | **incalculable** | Pas de CPA max. |
| Clics par vente supportés | **incalculable** | — |
| CVR break-even | **incalculable** | — |
| Scénario prudent / central / favorable | **incalculable** | Pas de prix de vente, pas de coût. |
| Budget test indicatif | **incalculable** | Pas de ventes nécessaires à conclure sans économie. |
| Sensibilité (fret, TVA, retours, CPC) | **incalculable** | Pas de cas de base. |

### CPC observé en phase 3 — rappel, pas un input de calcul

Source : `keywords_data/google_ads/search_volume/live`, France/French, 2026-09-05. Champ `cpc` présent ; **devise absente** (`currency` = none). Non relabelisé en EUR par la phase 3. **Non relabelisé ici.**

| Formulation | CPC (sans devise API) | `competition` |
|---|---:|---|
| `surmatelas` | 1,28 | HIGH, index 100 (tête soudée) |
| `sur-matelas` | 1,11 | — |
| `surmatelas à mémoire de forme` | 1,83 | — |

Un break-even « clics / vente » qui diviserait un CPA inventé par 1,28 serait une fabrication. **Non fait.**

Ratio prix ÷ CPC ≥ 100 (cible 150–200, docs internes) : **non évalué** — pas de prix maison.

### Volumes phase 3 — rappel, non re-mesurés

Témoins `tufting` 12 100 avant/après (2026-09-05). Famille `surmatelas` 33 100 + `sur-matelas` 14 800 = **47 900**/mois (deux buckets). Spécifique mémoire de forme **3 600**. Parent `matelas` 90 500 **non attribué**. Ces chiffres ne fondent pas une économie.

---

## 4. Faisabilité opérationnelle

Non établie. Le rôle n’a ni SKU, ni poids, ni dimensions, ni origine, ni délai France.

| Point | Constat 2026-09-05 | Statut |
|---|---|---|
| Poids / dimensions | Non relevés | **à confirmer** |
| Risque de casse | Non évalué | **à confirmer** |
| Emballage | Non chiffré | **à confirmer** |
| Retour aller+retour | Non chiffré | **à confirmer** |
| Pièces / consommables | Sans objet sans SKU | **à confirmer** |
| Charge SAV | Phase 3 : norme « 100 nuits » chez DTC — **non chiffrée** | **à confirmer** |
| Responsabilité produit / CE | Non exigée : pas de lancement, pas d’échantillon | **à confirmer** |
| Allégations santé | Phase 3 : claims visibles chez occupants (dos, kinés). Risque ads/Merchant **si** une offre était ouverte. Hors calcul. | note d’amont |
| Conformité électrique | Sans objet pour un surmatelas mousse **si** l’objet reste passif. Le chauffant a déjà été rejeté en phase 2. | — |

Une faisabilité « a priori lourde » (volumétrie literie) **n’est pas transformée** en STOP opérationnel chiffré : ce serait une estimation.

---

## 5. Droit de gagner

**Non documenté** — le rôle concurrence n’a cartographié personne (`FAIL_CLOSED`, 0 fiches).

Notes d’amont **non recyclées en fiches** (phase 3 SERP du 2026-09-05, non relues en navigation ce jour) :

- Occupation PRODUIT PUR déjà écrite : Mello, Nyte, Slome en Search/organique ; IKEA / BUT / Conforama / DODO en page 1 ; Shopping low-ticket < 50 € visible sur la même requête.
- Phase 3 : « Un générique rectangle de mousse n’a pas d’espace évident. » Ce n’est **pas** un droit de gagner établi, ni un verdict concurrentiel de phase 4.
- Places libres identifiées par le rôle concurrence : **aucune** (inventer une place serait un contournement du gate).

Sans coût rendu **et** sans cartographie, aucun actif défensif n’est opposable à l’économie.

---

## 6. Recommandation technique

**`TECHNICAL_INCONCLUSIVE`**

Motif canonique (critères 23/08/2026 et skill phase 5) : **preuves critiques manquantes** — coût rendu non daté, concurrence non examinée par le rôle dédié, pas de `PASS_PREQUALIFICATION`. Le CPC existe en phase 3 mais **sans devise API** et ne sert à rien sans CPA max.

Ce n’est pas `TECHNICAL_FAIL` : l’économie n’a pas été calculée puis rejetée ; elle n’a pas pu commencer.

Ce n’est pas `TECHNICAL_WATCH` : aucune assiette à surveiller.

Ce n’est pas `TECHNICAL_PASS`.

Le mot **GO** n’apparaît pas comme recommandation. Aucun `GO_FINAL` / `WATCH_FINAL` / `NO_GO_FINAL`.

### Réserves conservées des phases précédentes

1. Phase 3 : REVIEW, pas PASS — occupation GSB + DTC + Shopping low-ticket + claims santé ; refus d’attribuer un sous-volume « visco » inventé à 47 900.
2. Phase 3 : CPC sans devise.
3. Phase 3 : pertinent = famille unbranded, pas 100 % mémoire de forme.
4. Phase 4 sourcing : AliExpress **non interrogé** — ce n’est pas « aucune offre ».
5. Phase 4 concurrence : occupants SERP = notes d’amont, pas des fiches.
6. Registre : STOP eau/thermorégulé **distinct**.
7. Carte `[C0]` au niveau famille : aucun tenant produit validé ; le REVIEW n’est pas un produit nommé pour une due diligence.

---

## 7. Dossier pour décision humaine

Hakim seul prononce `GO_FINAL`, `WATCH_FINAL` ou `NO_GO_FINAL`. Ce rapport **n’éclaire pas** un lancement : il constate que la chaîne s’est arrêtée avant l’économie.

### Pour qu’une économie exacte puisse un jour être écrite

Preuves **toutes** nécessaires, aucune n’étant suffisante seule :

1. Décision humaine sur le `REVIEW_PREQUALIFICATION` du surmatelas à mémoire de forme (pass écrit, STOP, ou nouvelle carte **par produit**).
2. Si pass : sourcing AliExpress réel (PDP `/item/`, variante, fret France, **coût rendu daté**).
3. Si pass : cartographie concurrence (fiches, prix comparables, places libres ou absence d’espace).
4. Alors seulement : scénarios dans les bandes de prix **alors** observées, marge contributive, CPA max, break-even vs CPC, provisions.

`WATCH_FINAL` n’autorise rien (ni build, ni commande test). Une commande test n’est pas envisageable : pas de fiche.

### Points à confirmer (liste fermée)

- Coût rendu daté : **absent**.
- TVA récupérable fournisseur : **absente**.
- Frais Stripe / PayPal des contrats en vigueur : **non relus**.
- Provisions retours/SAV literie : **non chiffrées**.
- Poids, dimensions, aller-retour : **absents**.
- Fixes Shopify/apps : **non lus**.
- Devise du CPC DataForSEO : **absente**.
- Droit de gagner vs Mello/Nyte/GSB : **non cartographié**.

### Vérification arithmétique

Aucun nombre de sortie n’a été produit. Contrôle outil du 2026-09-05 : le livrable ne contient aucune valeur numérique pour marge contributive, CPA max, CVR break-even ni budget test (hors rappels de volumes/CPC **déjà écrits** en phase 3, non réutilisés dans une formule).

---

## Limites

- Fail-closed volontaire. Pas un trou d’outillage, pas un CAPTCHA.
- Aucun contact, compte, panier, commande, publication, dépense.
- Aucune modification Shopify / Ads / GMC / registre.
- `reports/` est gitignoré ; la copie versionnable est ce fichier sous `analyses/`.
- Les rapports parents n’ont pas été fusionnés vers `main`.

Chemin du livrable (copie versionnable) :

`/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/analyses/2026-09-05-chasse-clusters-sommeil-environnement-nocturne/phase5-marge-sommeil-environnement-nocturne-2026-09-05.md`

Copie attendue par le brief (gitignorée) :

`/Users/Hakim/Documents/Boutiques drop/boutique-pipeline/reports/phase5-marge-sommeil-environnement-nocturne-2026-09-05.md`

Branche de dépôt : `agents/c0-marge-sommeil-2026-09-05`
