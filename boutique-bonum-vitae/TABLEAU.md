# Bonum Vitae — TABLEAU

**LE point d'entrée de cette boutique.** Qui que tu sois — Claude, Codex, Grok ou Hakim — tu
commences ici. Le détail des décisions passées est dans [`journal/`](journal/) ; tu n'y vas jamais
pour savoir *quoi faire*. L'état chiffré est dans [`ETAT.md`](ETAT.md), les pièges dans
[`REGLES.md`](REGLES.md). Format : [`../METHODE-TABLEAU.md`](../METHODE-TABLEAU.md).

**Créé le 17/08/2026.** Chantier ouvert : crible live (rail A) puis redesign FullStack 2.3 (rail B)
pour un test ads en septembre. Prompt de relance :
[`PROMPT-NOUVELLE-CONVERSATION.md`](PROMPT-NOUVELLE-CONVERSATION.md).

**Mets ce fichier à jour avant de rendre la main.**

> 👉 **Hakim, maintenant :** ① T-H7 — les prix restants (carafes ALTHY 129-174 €, douche ALTHY
> 111-149 €, magnétiques 153 € — coûts réels découverts : 28-40 €) · ② T-H8 — choisir un
> anti-calcaire électronique sourcé (ou refuser) · ③ T-11 — QA préview FullStack · ④ T-H6 — GMC
> existant ? — ✅ Persona validé (17/08), OSWNKW à 449 € et 11 fiches débaptisées, site adapté.

Dernière mise à jour : **18/08/2026 ~0h** — ✅ **FullStack v1 monté sur la copie `205568147794`** :
démo vendeur purgée (Klaviyo, socials, rating-stars, Powered by), DA appliquée (charte BV,
Fraunces/Inter, 3 schemes), home + template produit reconstruits avec les contenus Horizon
harmonisés policy, footer avec OH Ventures + SIREN. **QA préview à faire par Hakim** :
`https://kw7vak-g0.myshopify.com?preview_theme_id=205568147794`.
[`journal/2026-08-17-fullstack-build-v1.md`](journal/2026-08-17-fullstack-build-v1.md).
— Plus tôt (~19h30) : ✅ rail A P0 soldé et constaté en anonyme (faux avis, 4.8/5, 8 barrés,
bandeau -20 %). [`journal/2026-08-17-rail-a-p0.md`](journal/2026-08-17-rail-a-p0.md).

---

## Le cadre, en trois phrases

1. **Les P0 de juin sont retirés du live depuis le 17/08 au soir** — plus de faux avis, plus de
   compteur, plus de barrés, plus de -20 %. La boutique n'expose plus l'entité sur ces
   déclencheurs ; restent les P1 (T-06, T-07) et l'inconnu GMC.
2. **On ne touche ni Tuftéo ni Noirmont.** On écrit seulement sur `kw7vak-g0.myshopify.com`.
   MAIN Horizon : rail A uniquement. FullStack (`205568147794`) : copie UNPUBLISHED, Hakim publie.
3. **Persona puis DA puis thème.** Pas de copy, pas de direction artistique, pas de montage
   FullStack avant persona validé par Hakim.

---

## 🔴 BLOQUÉ — attend Hakim

### T-H6 — Dire si un GMC / app Google & YouTube existe
**État** : BLOQUÉ · **Pour** : Hakim · **Gravité** : P1
**Pourquoi** : `appInstallations` refuse au CLI (scope `read_apps` absent). Tuftéo a montré qu'un
GMC se crée tout seul via l'app Google & YouTube. S'il en existe un ici, tout changement de thème
est un changement brutal sur compte établi.
**Comment** : Admin → Paramètres → Applications et canaux de vente — dire si « Google & YouTube »
y est, et si un Merchant Center est rattaché.
**Sortie attendue** : réponse notée dans `ETAT.md`. **Ne pas créer, ne pas soumettre.**

### T-H8 — Choisir (ou refuser) un anti-calcaire électronique parmi les candidats sourcés
**État** : BLOQUÉ — **sourcing livré** · **Pour** : Hakim · **Gravité** : P1
**Pourquoi** : sourcing du 17/08
([`journal/2026-08-17-prix-renommage-sourcing-persona.md`](journal/2026-08-17-prix-renommage-sourcing-persona.md)) :
2 candidats crédibles — électronique à impulsions `1005008632801588` (**309 ventes, 4,7★,
29,79 €** coût, prise EU) vendable 129-179 € ; LPS toute-maison `1005006005109143` (**500+ ventes,
4,9★, 61,69 €**) vendable 179-229 €. Fenêtre marché : « adoucisseur sans sel » 8 160/mois, KD 8-19.
**Attention** : le verrou est la **promesse** (Anses : efficacité non démontrée) — vente possible en
« dispositif d'appoint » honnête, pub Shopping déconseillée sur ces produits. Découverte annexe :
nos ALTHY/IPSE actuels coûtent 28-40 € (marge ×3-4), ce qui rend T-H7 encore plus urgent.
**Comment** : dire quel candidat passe à l'étape DSers (fret FR + photos = classe A), ou refuser.
**Sortie attendue** : décision ; si oui, import DSers par Hakim puis fiche montée par Claude.

### T-H7 — Arbitrer les prix avant campagnes (sonde du 17/08)
**État** : BLOQUÉ · **Pour** : Hakim · **Gravité** : P1 (bloque le lancement ads)
**Pourquoi** : sonde SERP France du 17/08
([`journal/2026-08-17-prix-concurrence.md`](journal/2026-08-17-prix-concurrence.md)) :
- ✅ **RO 600G 299 €** : aligné sur le leader (Waterdrop G2P600 à 299,99 €) — produit de campagne.
- ⛔ **OSWNKW 576,90 €** : plus cher que le G3P600 certifié NSF (420-432 €) → 449-479 € ou hors pub.
- ⛔ **IPSE magnétique 152,90-153,90 €** : haut d'une bande 20-150 € **publiquement contestée**
  (Anses, 60M) → ≤ 99 € ou hors acquisition, jamais en Shopping.
- ⛔ **Carafes ALTHY 129,90-173,90 €** : référence mentale Brita = 16-30 € → niche assumée sans pub
  ou repositionnement.
- ⚠ **ALTHY douche 111,90-149,90 €** : marché à 30-60 € → ≤ 79 € ou justification forte.
- ✅ Filtres douche cœur 13,90-46,90 € : dans la bande, 2e famille de campagne possible.
**Comment** : trancher ligne par ligne le tableau §6 du journal ; Claude applique ensuite (prix
sans réintroduire de `compareAtPrice`).
**Sortie attendue** : grille de prix validée, appliquée, constatée en anonyme.

### T-H4 — Choisir une DA parmi 2 ou 3 directions
**État** : BLOQUÉ · **Pour** : Hakim · **Dépend de** : T-H3
**Pourquoi** : la charte Abysse/Source de juillet est un point de départ, pas un verrou. Eau / foyer
/ pédagogie — ni pop Tuftéo, ni luxe Noirmont.
**Sortie attendue** : une direction choisie, notée dans `ETAT.md`. Ensuite seulement : settings
FullStack.

### T-H5 — Publier (thème, jamais par l'agent)
**État** : BLOQUÉ · **Pour** : Hakim · **Dépend de** : rail A soldé + FullStack QA
**Pourquoi** : l'agent ne publie jamais un thème. Sur un GMC éventuel déjà créé via Google & YouTube,
une publication est un changement brutal — une seule, propre, puis calme.
**Sortie attendue** : Hakim publie. L'agent vérifie en visiteur anonyme après.

---

## À FAIRE

### T-06 — Recouper policies live vs pages CMS (doublon mentions légales)
**État** : À FAIRE · **Pour** : Claude · **Gravité** : P1 · **Dépend de** : T-H1
**Pourquoi** : `/policies/legal-notice` **et** `/pages/mentions-legales` répondent toutes les deux
200. Google compare. Footer sans raison sociale ni SIREN (P1 GMC « footer d'abord »).
**Comment** : même recette Noirmont — une seule URL servie, l'autre dépubliée + 301, texte **pas**
identique mot pour mot à Tuftéo/Noirmont/Bien Brûlé. Collage policies = Hakim si scope absent.
**Sortie attendue** : une mentions légales, footer = policies = (plus tard) GMC.
**Réf.** : skill `gmc-acceptance` · `New project/outputs/bonumvitae-pages-legales-2026-07-12/`

### T-07 — Collections sous le seuil de 5
**État** : À FAIRE · **Pour** : Claude · **Gravité** : P1 · **Dépend de** : T-H1
**Pourquoi** : red flag Terry. Public : `purificateurs-nomades` = 1 fiche ; `osmoseurs` = 3 fiches
visibles dont 1 consommable (écart : `collections.json` annonce 5). `frontpage` = 1.
**Comment** : admin pour lever l'écart 3 vs 5. Décision Hakim : repeupler, fusionner, ou dépublier
la collection. Ne pas inventer des fiches.
**Sortie attendue** : chaque collection **publiée** a ≥ 5 produits actifs, ou elle n'est plus
publique.

### ~~T-08 — Produire le persona maison~~ ✅ FAIT le 17/08
Persona sourcé SERP/forums/avis concurrents, format template maison :
[`../personas/persona-bonum-vitae-2026-08-17.md`](../personas/persona-bonum-vitae-2026-08-17.md).
Validation Hakim = T-H3. Volumes SEMrush non mesurés dans cette passe (limite notée au fichier).

### T-11 — QA préview FullStack v1 (mobile 375 px d'abord)
**État** : À FAIRE · **Pour** : Hakim (préview) puis Claude (correctifs) · **Gravité** : P1
**Pourquoi** : la v1 est écrite et vérifiée par API, mais `preview_theme_id` exige une session
navigateur — le rendu réel n'a pas été vu.
**Comment** :
1. Ouvrir `https://kw7vak-g0.myshopify.com?preview_theme_id=205568147794` (mobile d'abord).
2. Contrôler : hero (lisibilité sur image), icônes Material (`water_drop`, `balance`, `lock`…),
   tableau comparatif en mobile, accordéons, sticky ATC, date `delivery-estimation` en français,
   icônes de paiement du footer vs checkout réel.
3. Renvoyer la liste des défauts — Claude corrige sur la copie.
**Sortie attendue** : liste de retours, puis v2.
**Réf.** : `journal/2026-08-17-fullstack-build-v1.md`

### T-12 — Panier tiroir FullStack (recette Tuftéo 12b)
**État** : À FAIRE · **Pour** : Claude · **Dépend de** : T-11
**Pourquoi** : le drawer FullStack est encore en config démo (seuil de progression incohérent avec
« livraison offerte partout »).
**Comment** : bannière « Livraison offerte en France » + upsell consommables (handles réels :
membranes, cartouches), pattern `campement/12b-panier-banniere-upsells.md`. Un `custom-code` ne
peut pas vivre dans `_product-form`.
**Sortie attendue** : drawer propre en préview.

### T-10 — Directions DA (2 ou 3), puis stop
**État** : À FAIRE · **Pour** : Claude · **Dépend de** : T-H3
**Pourquoi** : skill `webdesign-boutiques` + `ui-ux-pro-max`. Palette juillet = point de départ.
**Comment** : 2 ou 3 directions (palette + typos + 3 références + anti-patterns). Attendre T-H4.
Implémentation = FullStack, pas Horizon (ignorer la phrase « implémenter sur Horizon » du skill).
**Sortie attendue** : note DA dans `journal/`, choix Hakim.

---

## FAIT

### ~~T-H1 — Auth CLI device-code Bonum Vitae~~ ✅ 17/08 (Hakim)
`contact@bonumvitae.fr` sur `kw7vak-g0`. Scopes : products, files, themes, content, pages,
legal_policies (pas `read_apps`). Sessions Tuftéo / Noirmont intactes.

### ~~T-H2 — FullStack sur la boutique~~ ✅ 17/08 — déjà importé
`copie-de-fullstack-2-3`, id `205568147794`, UNPUBLISHED, créé 17/08 15h35. **Zip vendeur brut** :
purge démo obligatoire avant toute préview publique (T-09).

### ~~T-01 — Retirer les trois faux témoignages « Vérifié »~~ ✅ 17/08 soir
Section `bv_avis_clients` retirée de `index.json`, `product.json` **et `product.osmoseur.json`**
(seul `osmoseur-ro-600g` porte ce suffixe). Constaté absent en anonyme sur accueil + 2 fiches.
[`journal/2026-08-17-rail-a-p0.md`](journal/2026-08-17-rail-a-p0.md)

### ~~T-02 — Retirer « 4.8/5 basé sur 312 avis vérifiés »~~ ✅ 17/08 soir
Bloc `custom_liquid_bhBnde` (imbriqué dans `product-details`) supprimé des deux templates produit.
0 occurrence publique constatée.

### ~~T-03 — Purger les prix barrés~~ ✅ 17/08 soir
**8 variantes** (6 actives + **2 dormantes** sur le brouillon osmoseur Shuangli) remises à `null`,
0 `userErrors`, valeurs d'origine dans `backups/2026-08-17-rail-a/compare-at-avant-purge.json`.
Re-scan : 0 `compareAtPrice` non nul sur les 26 produits.

### ~~T-04 — Retirer le bandeau « -20% sur les osmoseurs »~~ ✅ 17/08 soir
Bloc `announcement_2` supprimé de `header-group.json`. « Livraison offerte » conservé.

### ~~T-05 — Snapshot admin~~ ✅ 17/08 soir (partiel)
Thèmes, catalogue, compareAt, templates : faits (voir `ETAT.md`). Restent : apps/GMC (T-H6,
scope manquant), paiements réels (au rail B).
