# Bonum Vitae — règles non négociables et pièges déjà payés

À lire avant d'intervenir, en même temps que [`TABLEAU.md`](TABLEAU.md). Les règles du parc
s'appliquent ; celles-ci sont les plus coûteuses **ici**.

---

## Les trois règles qui gouvernent tout le reste

**1. Une misrepresentation ici dégrade Tuftéo.**

Les quatre boutiques publient la même adresse et le même téléphone. Hakim a assumé le linkage le
16/08. Le compte GMC **5806019978** a déjà été suspendu le 15/06 pour faux avis — c'est l'entité
OH Ventures qui a été blanchie, pas une boutique isolée. Tuftéo a un GMC approuvé. Tant que Claire /
Karim / Bernard « Vérifié » et les 312 avis sont publics, cet actif est exposé.

**2. Rail A sur le live, rail B sur une copie. Hakim publie.**

Le MAIN actuel est Horizon (`203569004882`). On n'y touche **que** pour le crible (faux avis, notes,
barrés, bandeau, claims). FullStack se travaille sur une copie **UNPUBLISHED**. **Ne jamais publier
un thème. Ne jamais écrire le redesign sur le MAIN.**

**3. FullStack natif d'abord. On ne redécouvre pas le thème.**

Le parc l'a déjà monté deux fois (Tuftéo, Noirmont). Lire l'inventaire reco + portable-kit + journaux
**avant** tout `custom-code`. Horizon n'est plus la base d'implémentation (ignorer cette phrase du
skill `webdesign-boutiques`). Palette, copy, visuels = Bonum Vitae (eau / foyer / pédagogie) — ni
pop DIY, ni luxe montres.

---

## Interdits absolus

- **Ne pas toucher Maison Noirmont** (`v42pzp-h4` / maisonnoirmont.fr) — storefront gelé 17/08 ~15h25.
- **Ne pas toucher Tuftéo** (`et0hua-w1` / tufteo.com) sauf demande explicite. GMC = actif.
- **Ne jamais `switch-shop`** sur le connecteur Shopify MCP.
- Toujours `--store kw7vak-g0.myshopify.com`.
- **Jamais `fileDelete`** sur un média produit. Détacher via `fileUpdate` + `referencesToRemove`.
- Aucune commande, aucun achat, aucun paiement. Pas de Google Ads / GMC sauf ticket explicite.
- **Policies jamais identiques mot pour mot** avec Tuftéo, Noirmont ou Bien Brûlé.
- Secrets, `.env`, `node_modules/`, `scratchpad/`, `settings.local.json` : hors git.
- Slider et avis de démo FullStack : chasse gardée de Hakim — proposer, ne jamais publier.

---

## Contenu — eau, DGCCRF, GMC

- **Photos fournisseur : zoom sur le corps avant toute génération.** Si un drapeau, une étiquette
  ou une certification est **sur l'objet** (pas un bandeau hors produit), STOP — ne pas gommer
  **sauf décision Hakim explicite**. LPS 17/08 : Codex a stoppé à juste titre ; Hakim a ensuite
  tranché **voie C** (overlays photo, robe nue autorisée) pour ce SKU seulement. Les images
  Shopping ne peuvent jamais montrer FDA / NSF / 86 %, même si l'étiquette était physique.
- **Specs de raccord : la fiche fabricant prime sur le brief.** DN32 écrit par erreur le 17/08 ;
  la source LPS10 dit G3/4" femelle. Ne jamais inventer un DN.
- **Aucune preuve sociale fabriquée.** 0 commande client au 17/08 (parc). Pas d'avis, pas de note,
  pas de « Vérifié », pas de compteur. **Y compris les notes AliExpress collées dans une
  description** (payé le 17/08 : 4,9/5 et « 1 450 avis » sur 5 fiches).
- **Copy produit :** pas de formule unique sur tout le catalogue (« Ce que ça change au
  quotidien », scène → triple, closer d'urgence). Titre Shopping = type + spec, mot-clé d'abord.
- **Anti-calcaire magnétique / électronique :** jamais « adoucit l'eau / élimine le calcaire /
  réduit la dureté ». Le positionnement de juillet le dit déjà ; le faux avis Karim le viole.
- **Pas d'allégation santé** : prévient, détoxifie, soigne, peau, tiraillement, imagerie médicale,
  avant/après santé. Section FullStack `before-after` : jamais sur ce registre.
- Promesses vérifiables uniquement : délais, -10 %, -20 %, « sans plombier » — seulement si c'est
  vrai pour **ce** produit. Un osmoseur sous évier peut exiger une intervention.
- Handle `pommeau-de-douche-filtrant-parfume-eau-adoucie` et carafe « alcaline » : à recouper, pas
  à reprendre tels quels.

---

## Thème FullStack — pièges déjà payés dans le parc

- Démo vendeur = piège GMC n°1 : `rating-stars` 4,5/123, « 2 000 clients », faux avis, logos
  `themefullstack`, clé Klaviyo étrangère, « Powered by FullStack ». **Purge avant toute préview
  publique.** Vider les 4 URL sociales **dans `settings_schema.json`** (les défauts du schéma
  survivent à un settings_data vide).
- `themeFilesUpsert` peut renvoyer `upsertedThemeFiles: []` sans erreur. Vérifier par **md5** +
  relecture du contenu. Le champ `size` de l'API ne prouve rien.
- Templates JSON ~125 ko : staged upload, pas TEXT. Au-delà, l'upsert « réussit » sans appliquer.
- Nom de schéma de bloc > 25 caractères = rejet silencieux.
- Un `custom-code` **ne peut pas** vivre **dans** `_product-form`.
- `preview_theme_id` ne se transmet pas en `curl` : session navigateur.
- Logos paiement : ré-upload CDN Bonum Vitae, jamais d'URL `cdn` Tuftéo / Noirmont / ancien Horizon.
- Icônes = **noms Material Symbols**, jamais d'emoji.
- Paiement fractionné (portable-kit) **seulement** si PayPal/Klarna sont réellement dans
  `shop.enabled_payment_types`.

---

## Recette d'écriture (quand T-H1 est fait)

1. Repérer le thème : `{ themes(first:10){ nodes{ id name role } } }`. MAIN interdit hors rail A.
2. Backup dans `backups/<date>-<sujet>/` **avant** d'écrire.
3. Gros fichier : staged upload. Vérifier en relisant, puis en rechargeant la page.
4. Ticket FAIT = URL publique (rail A) ou preview navigateur (rail B) constatée. Pas un accusé API.

Auth CLI : `export PATH="/Users/Hakim/.npm-global/bin:$PATH"`. Mutations :
`shopify store execute --allow-mutations`. Si l'auth est encore sur Noirmont / Tuftéo : device-code
sur le compte Bonum Vitae — ne pas improviser.

---

## Ce qui appartient à Hakim

Auth CLI sur le bon compte · installer FullStack si absent · valider le persona · choisir la DA ·
publier le thème · créer / soumettre un GMC · coller les policies si le scope `write_legal_policies`
manque · arbitrer les collections < 5.
