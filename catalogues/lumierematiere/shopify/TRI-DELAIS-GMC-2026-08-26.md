# Tri délais GMC — exécuté 26/08/2026

**Store** `lumierematiere.fr` · reco `RECO-DELAIS-GMC-2026-08-26.md` · audit `COHERENCE-2026-08-26.md`.  
Script `apply_tri_delais.py --apply` · thème `patch_delais_theme.py` · vérif `verify_tri_delais.py`.

Hakim a validé la fenêtre unique **7–18 j**, avec deux amendements : fret payant jusqu’à **20 $** répercuté sur le PV ; **pas** de DHL 550 $ / 800 $. Lustres salon agrémentés. Pampilles / bambou / verre : **pas** d’agrément hors matière — nouveau sourcing.

---

## Ce qui est live

| | Chiffre |
|---|---|
| ACTIVE | **52** (les 37 OK + 12 LIMITE + LM-127 + testers verre LM-128/129/130) |
| Brouillon | **80** (pampilles / papier dépubliés, LM-125, appliques V2, plus anciens) |
| FAQ PDP leftover 7–17 | **0** |
| FAQ PDP 7–18 | **52 / 52** |
| Policy `/policies/shipping-policy` | prép. 1–2 · route **6–16** · total **7–18** |
| CMS FAQ | 6–16 / 7–18 |

Promesse unique : cut-off 16h00 Paris · préparation 1–2 j · acheminement 6–16 j · **7–18 j ouvrés** · franco France métropolitaine.

GMC structuré : **ne pas soumettre maintenant.** Handling 1–2 · transit 6–16 · cut-off 16:00 Europe/Paris · FR métro · 0 € — le jour de la création du compte, pas avant.

---

## Seuil fret 20 $ — personne de plus sauvé

Rescoré : une fiche reste live s’il existe **une** méthode suivie, max ≤ 16 j, coût ≤ 20 $. Les 550 $ / 800 $ restent exclus.

| SKU | Ligne « rapide » | Pourquoi ça ne passe pas |
|---|---|---|
| LM-044 / LM-089 | Cainiao Standard 8–16 j | **~46 $** (> 20) |
| LM-053 / LM-059 | DHL | **551 $ / 816 $** |
| LM-071 | CPAP 9–56 j à 19 $ | le délai casse le plafond 16 j |
| LM-086 | DHL **13 $** | 17–25 j — le délai casse |

Aucun PV n’a été remonté : il n’y avait personne à réabsorber sous 20 $.

---

## Collections — ce qui a « disparu », ce qui reste mince

Les volumes sont les totaux de groupe SEMrush du 25/08 (`MOTS-CLES-TITRES-2026-08-25.md`).  
`productsCount` admin compte les brouillons : les chiffres ci-dessous sont les **ACTIVE vitrine**.

| Collection | Vol. groupe | Avant | Live | Canal | Décision |
|---|---:|---:|---:|---|---|
| Lustres salon | 24 490 | 12 | **10** | publié | agrémenté (pas dépublié) |
| Lustres pampilles | **6 340** | 7 | **0** | **dépublié** | handle conservé, **pas** de 301, **pas** d’agrément |
| Suspensions verre | **6 200** | 10 | **5** | publié | testers LM-128/129/130 live 26/08 |
| Suspensions papier | 4 760 | 1 | **0** | **dépublié** | seule LM-092 était OVER |
| Suspensions bambou | 3 220 | 16 | **3** | publié | reste au menu · à sourcer |
| Suspensions osier | 3 180 | 5 | 2 | publié | mince, pas dépublié |
| Suspensions pierre | — | 9 | 4 | publié | mince |
| Lustres chambre | 10 810 | 10 | 3 | publié | mince |
| Suspensions salon | 4 080 | 29 | 4 | publié | mince |
| Plafonniers cuisine | 6 190 | 4 | 1 | publié | mince |
| Grand format XXL | 1 310 | 15 | 1 | publié | mince |
| Appliques murales | — | 5 | 5 | publié | intact |
| Rotin / bois / métal / déco / LED / anneau | — | — | 5–7 | publié | tenable |

**Pampilles et papier** sont sortis du menu et de `/collections` : une page à 0 fiche ment plus qu’elle n’aide le SEO. L’URL `/collections/lustres-pampilles` fait **404** tant qu’on n’a pas de fiches. Le handle et la redirection `lustres-effet-cristal` → `lustres-pampilles` restent. On republie dès qu’il y a ≥ 5 pampilles tenables.

**Bambou et verre** n’ont pas été dépubliés, malgré la règle « viser 5 ». Hakim : volume SEMrush, et on ne remplit pas avec d’autres matières.

### Agrément lustres salon (ajout, pas déplacement)

LM-007 · LM-014 · LM-016 · LM-018 · LM-082 · LM-095 · LM-099 · LM-108 · LM-113 · LM-121.

Ce sont des pièces de salon déjà live (bambou dôme / disque / double, pétales, LED anneau, laiton 6 bras, oiseau, sputnik, soie, moderne). Pas d’appliques, pas de petits plafonniers cuisine.

---

## File de sourcing (passe 26/08 soir)

Rapport : `SOURCING-DELAIS-PAMPILLES-BAMBOU-VERRE-2026-08-26.md`. JSON : `delais-candidats-2026-08-26.json`. Verre importé et **live 26/08 soir**.

| Rayon | Verdict | Suite |
|---|---|---|
| Pampilles | **`AUCUNE OFFRE EXPLOITABLE`** | bijoux ou hôtel 500 €+, 0 milieu ≤ 16 j. Page 404 tant qu’on n’a pas 5 gouttes. |
| Bambou | **`AUCUNE OFFRE EXPLOITABLE`** | 2 JOYINLED 40 cm neufs = Heavy seule ligne (23–43 j). Les 3 live restent. |
| Verre | **3 testers live** | LM-128 `suspension-verre-405368` 149 € · LM-129 `suspension-verre-bois-910933` 159 € · LM-130 `suspension-verre-538307` 129 €. Collection `suspensions-verre` = **5 ACTIVE**. |

Papier (4 760) après import verre, si Hakim le veut. Les collections pièce minces se remplissent d’elles-mêmes si le sourcing matière tient le délai.

---

## Thème

Footer trust + bannière / accordéon panier : 6–15 / 7–17 → **6–16 / 7–18**.  
`/collections` : vignettes pampilles et papier retirées.  
Sources alignées : `humanise_theme.py`, `humanise_pdp.py`, `patch_cart.py`, `pages/*.md`.

Le HTML storefront peut encore servir l’ancien bandeau quelques minutes (cache Shopify). Les fichiers thème live sont déjà à 7–18.

---

## Ce qu’on ne fait pas

- Remettre un OVER en ligne sans nouvelle carte FR ≤ 16 j.
- Agrémenter pampilles / bambou / verre avec une autre matière.
- 301 pampilles ailleurs.
- Soumettre Merchant Center tant que le domaine n’a pas 30 jours et que ce catalogue n’est pas stable.
- Mettre un brouillon dans le feed Google.
