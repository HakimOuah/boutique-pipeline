# Bonum Vitae — TABLEAU

**LE point d'entrée de cette boutique.** Qui que tu sois — Claude, Codex, Grok ou Hakim — tu
commences ici. Le détail des décisions passées est dans [`journal/`](journal/) ; tu n'y vas jamais
pour savoir *quoi faire*. L'état chiffré est dans [`ETAT.md`](ETAT.md), les pièges dans
[`REGLES.md`](REGLES.md). Format : [`../METHODE-TABLEAU.md`](../METHODE-TABLEAU.md).

**Créé le 17/08/2026.** Chantier ouvert : crible live (rail A) puis redesign FullStack 2.3 (rail B)
pour un test ads en septembre. Prompt de relance :
[`PROMPT-NOUVELLE-CONVERSATION.md`](PROMPT-NOUVELLE-CONVERSATION.md).

**Mets ce fichier à jour avant de rendre la main.**

> 👉 **Hakim, maintenant :** dire si un **GMC / app Google & YouTube** existe (Admin → Canaux de
> vente) — le scope `read_apps` manque au CLI. Puis valider le persona quand T-08 sera livré.

Dernière mise à jour : **17/08/2026 ~19h30** — ✅ **rail A P0 soldé et constaté en anonyme** :
faux avis retirés des 3 templates (dont `product.osmoseur.json`), « 4.8/5 · 312 avis » supprimé,
**8 `compareAtPrice` purgés** (dont 2 dormants sur un brouillon), bandeau -20 % retiré. Auth CLI
Bonum Vitae OK (`contact@bonumvitae.fr`). FullStack **déjà importé** : `copie-de-fullstack-2-3`
id `205568147794`, UNPUBLISHED, zip vendeur brut (démo à purger).
[`journal/2026-08-17-rail-a-p0.md`](journal/2026-08-17-rail-a-p0.md).

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

### T-H3 — Valider le persona avant tout copy et toute DA
**État** : BLOQUÉ · **Pour** : Hakim · **Dépend de** : T-08
**Pourquoi** : les Claire/Karim/Bernard de juillet sont un brief de marque, pas un persona maison.
Aucun fichier dans `boutique-pipeline/personas/` pour cette boutique.
**Comment** : lire le livrable T-08, dire oui / amender / non.
**Sortie attendue** : persona daté coché validé dans `ETAT.md`.

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

### T-08 — Produire le persona maison
**État** : À FAIRE · **Pour** : Claude · **Dépend de** : — (lecture seule, peut commencer)
**Pourquoi** : PLAYBOOK 1d. Particulier qui découvre, pas un pro de l'eau. Preuves `[O]`/`[D]`.
**Comment** :
1. Lire `../templates/persona.template.md` + skill `customer-research`.
2. Sources : `New project/outputs/bonumvitae-branding-2026-07-11/positionnement-marketing-bonumvitae.md`
   (brief, pas preuve), SERP/forums, pas les faux avis live.
3. Écrire `../personas/persona-bonum-vitae-2026-08-17.md`.
4. **Stop** — Hakim valide (T-H3) avant copy et DA.
**Sortie attendue** : fichier persona + ticket T-H3 prêt.
**Attention** : ne pas recycler Claire/Karim/Bernard comme s'ils étaient des clients.

### T-09 — Inventaire FullStack natif vs custom pour Bonum Vitae
**État** : À FAIRE · **Pour** : Claude · **Dépend de** : T-H2 (thème présent) ; lecture possible avant
**Pourquoi** : on ne redécouvre pas le thème. Coder en dur seulement si le natif ne fait pas le rendu.
**Comment** : lire dans l'ordre du prompt (reco Tuftéo → portable-kit → journaux Noirmont → pièges
campement). Lister pour **cette** boutique : hero, comparatif, FAQ, réassurance, panier, mégamenu,
templates produit. Sortie : `journal/YYYY-MM-DD-inventaire-fullstack.md`.
**Sortie attendue** : tableau natif vs custom. **Aucun custom-code** tant que ce tableau n'existe pas.
**Réf.** : `../boutique-tufting/shopify/reco-theme-brouillon-2026-07-21.md`

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
