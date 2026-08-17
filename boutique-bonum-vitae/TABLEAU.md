# Bonum Vitae — TABLEAU

**LE point d'entrée de cette boutique.** Qui que tu sois — Claude, Codex, Grok ou Hakim — tu
commences ici. Le détail des décisions passées est dans [`journal/`](journal/) ; tu n'y vas jamais
pour savoir *quoi faire*. L'état chiffré est dans [`ETAT.md`](ETAT.md), les pièges dans
[`REGLES.md`](REGLES.md). Format : [`../METHODE-TABLEAU.md`](../METHODE-TABLEAU.md).

**Créé le 17/08/2026.** Chantier ouvert : crible live (rail A) puis redesign FullStack 2.3 (rail B)
pour un test ads en septembre. Prompt de relance :
[`PROMPT-NOUVELLE-CONVERSATION.md`](PROMPT-NOUVELLE-CONVERSATION.md).

**Mets ce fichier à jour avant de rendre la main.**

> 👉 **Hakim, maintenant :** T-H1 (auth CLI Bonum Vitae). Sans ça, aucun écriture admin, aucun
> snapshot thèmes/paiements/GMC, aucun correctif P0. Ne pas `switch-shop`. Ne pas publier de thème.

Dernière mise à jour : **17/08/2026 ~18h** — ouverture. Store confirmé `kw7vak-g0` = Bonum Vitae.
P0 encore publics. Live = Horizon MAIN, pas FullStack. CLI encore sur Tuftéo + Noirmont.
[`journal/2026-08-17-ouverture-crible.md`](journal/2026-08-17-ouverture-crible.md).

---

## Le cadre, en trois phrases

1. **Les faux avis de juillet sont encore en ligne** — Claire M. / Karim B. / Bernard L. « Vérifié »,
   plus « 4.8/5 basé sur 312 avis vérifiés » sur les fiches. Motif exact de la suspension GMC de
   juin. 0 commande client sur le parc.
2. **On ne touche ni Tuftéo ni Noirmont.** On lit leurs builds FullStack. On écrit seulement sur
   `kw7vak-g0.myshopify.com`. MAIN Horizon : rail A uniquement. FullStack : copie UNPUBLISHED,
   Hakim publie.
3. **Persona puis DA puis thème.** Pas de copy, pas de direction artistique, pas de montage
   FullStack avant persona validé par Hakim.

---

## 🔴 BLOQUÉ — attend Hakim

### T-H1 — Auth CLI device-code sur le compte Bonum Vitae
**État** : BLOQUÉ · **Pour** : Hakim · **Gravité** : P0 (bloque tout le rail A)
**Pourquoi** : le CLI de cette machine connaît `et0hua-w1` (Tuftéo) et `v42pzp-h4` (Noirmont).
`shopify store info --store kw7vak-g0.myshopify.com` refuse : *Couldn't find a store with domain
kw7vak-g0… for the current account.* Sans auth, impossible de lister les thèmes non publiés, les
paiements réels, un GMC éventuel, ni d'écrire le crible sur Horizon.
**Comment** :
1. Auth **device-code** sur le compte Shopify de Bonum Vitae — pas le compte Noirmont
   (`contact.noirmont@gmail.com`), pas Tuftéo.
2. **Ne jamais `switch-shop`** sur le connecteur Shopify MCP (ça révoque le token).
3. Cibler ensuite uniquement `--store kw7vak-g0.myshopify.com`.
**Sortie attendue** : `shopify store info --store kw7vak-g0.myshopify.com` rend Bonum Vitae.
**Attention** : ne pas improviser un switch depuis la session Tuftéo/Noirmont.
**Réf.** : `PROMPT-NOUVELLE-CONVERSATION.md`

### T-H2 — Dire si FullStack 2.3 est déjà sur `kw7vak-g0`, sinon l'installer
**État** : BLOQUÉ · **Pour** : Hakim · **Gravité** : P1 (rail B)
**Pourquoi** : le live est Horizon 4.1.1 (`theme id 203569004882`, rôle `main`). Sans admin, on ne
voit pas les copies UNPUBLISHED. Le parc a déjà FullStack sur Tuftéo et Noirmont — licence à
confirmer avant copie/zip.
**Comment** : dans Admin → Thèmes, vérifier la présence de `copie-de-fullstack-2-3` (ou équivalent).
Si absent : Hakim installe (zip vendeur / copie depuis une boutique déjà licenciée). Ne pas publier.
**Sortie attendue** : un thème FullStack 2.3 **unpublished** sur `kw7vak-g0`, id noté dans `ETAT.md`.
**Attention** : ne pas publier, ne pas travailler le MAIN.

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

### T-01 — Retirer les trois faux témoignages « Vérifié » encore publics
**État** : À FAIRE · **Pour** : Claude · **Gravité** : P0 · **Dépend de** : T-H1
**Pourquoi** : motif exact de la suspension GMC de juin. Personas de juillet présentés comme clients
vérifiés, datés « il y a 3 jours / 1 semaine / 2 semaines ». Servis sur l'accueil **et** les fiches
(section `bv-avis-section` / `bv_avis_clients`). Karim = claim santé déguisé (« Ma peau la remercie »,
« moins de tiraillement »).
**Comment** :
1. Backup du fichier thème (section + `index.json` / groupe) dans `backups/2026-08-17-p0-avis/`.
2. Retirer ou vider la section sur **tous** les templates qui la rendent — pas seulement l'accueil.
3. Recharger en navigation privée : 0 « Vérifié », 0 Claire / Karim / Bernard.
**Sortie attendue** : URL rechargée, citation absente. Ticket FAIT seulement sur preuve publique.
**Attention** : « FAIT » écrit n'a pas retiré les faux avis Tuftéo pendant 17 jours. Constater.
**Réf.** : `journal/2026-08-17-ouverture-crible.md` · live `https://bonumvitae.fr`

### T-02 — Retirer la ligne « 4.8/5 basé sur 312 avis vérifiés »
**État** : À FAIRE · **Pour** : Claude · **Gravité** : P0 · **Dépend de** : T-H1
**Pourquoi** : 0 commande client. Compteur codé en dur (référence Horizon `rating-row.liquid`).
Constaté visible sur fiche osmoseur RO 600G ; à grep sur tout le thème.
**Comment** :
1. Localiser le snippet / bloc (probablement `rating-row.liquid` ou équivalent Horizon).
2. Le retirer du template produit, pas le masquer en CSS.
3. Vérifier au moins 3 fiches en anonyme.
**Sortie attendue** : 0 « 312 avis », 0 « 4.8/5 » public.
**Réf.** : `https://bonumvitae.fr/products/osmoseur-ro-600g`

### T-03 — Purger les 6 prix barrés publics
**État** : À FAIRE · **Pour** : Claude · **Gravité** : P0 · **Dépend de** : T-H1
**Pourquoi** : loi Omnibus. Un barré n'est légal que s'il a été réellement pratiqué. Aucune preuve
au dossier. Même bombe que Noirmont T-50 (les brouillons aussi, pas seulement l'actif).
**Comment** :
1. Scan paginé admin de **toutes** les variantes (actifs + brouillons + archivés) — `compare_at_price`
   n'est pas filtrable, un `query:` est ignoré.
2. Backup des valeurs dans `backups/`.
3. Remettre `compareAtPrice` à `null` partout, sauf ticket Hakim qui prouve un prix réellement
   pratiqué.
4. Recharger accueil + 2 fiches en anonyme.
**Sortie attendue** : 0 `compare_at_price` non nul au catalogue ; 0 « Prix régulier » barré public.
**Attention** : 6 barrés **déjà publics** (liste dans `ETAT.md`). Les dormants éventuels sont la
vraie bombe.
**Réf.** : `journal/2026-08-17-ouverture-crible.md`

### T-04 — Retirer le bandeau « Offre d'été : -20% sur les osmoseurs »
**État** : À FAIRE · **Pour** : Claude · **Gravité** : P1 · **Dépend de** : T-H1
**Pourquoi** : promotion publique sans preuve depuis au moins le 18/07. Fausse urgence / fausse
réduction si le -20 % n'a jamais été tenu.
**Comment** : vider l'announcement bar du thème MAIN (rail A). Vérifier en anonyme sur accueil et
fiche.
**Sortie attendue** : 0 « -20% » / « Offre d'été » public.
**Réf.** : bandeau de `https://bonumvitae.fr`

### T-05 — Snapshot admin (thèmes, paiements, apps, GMC, policies)
**État** : À FAIRE · **Pour** : Claude · **Gravité** : P0 · **Dépend de** : T-H1
**Pourquoi** : le live ne dit pas si FullStack est déjà installé, si un GMC existe via Google &
YouTube, ni si Klarna/PayPal 4× sont réellement actifs (le footer les affiche).
**Comment** :
1. `themes { nodes { id name role } }` — noter MAIN vs unpublished. **Ne pas écrire le MAIN** hors
   tickets T-01 à T-04.
2. `shop.enabled_payment_types` + checkout réel. Footer live : Amex, Apple Pay, CB, Klarna,
   Mastercard, PayPal, Visa — recouper.
3. Apps d'avis. Produits : statuts, collections < 5, `compareAtPrice` dormants.
4. GMC : signaler tout de suite s'il existe. **Ne pas créer, ne pas soumettre.**
5. Écrire le résultat dans `ETAT.md`.
**Sortie attendue** : `ETAT.md` à jour côté admin, plus seulement le public.
**Attention** : `themeFilesUpsert` vide ≠ échec. `switch-shop` interdit.

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

_Aucun ticket soldé. Ouverture le 17/08/2026._
