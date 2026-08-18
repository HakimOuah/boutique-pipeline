# Prompt — nouvelle conversation Bonum Vitae

> **17/08/2026.** À coller tel quel dans une conversation neuve. Point d'entrée une fois le chantier ouvert : ce dossier, puis `TABLEAU.md` (à créer en première tâche).

---

## Texte à coller

Tu travailles avec Hakim (ops, SASU OH Ventures) sur **Bonum Vitae**, boutique de traitement de l'eau au point d'usage.

Workspace : `/Users/Hakim/Documents/Boutiques drop`. Repo de travail : `boutique-pipeline/` (GitHub `HakimOuah/boutique-pipeline`, branche `main`). Dossier à créer et à tenir à jour : `boutique-pipeline/boutique-bonum-vitae/` (`TABLEAU.md`, `ETAT.md`, `REGLES.md`, `journal/`, `backups/`). Convention : `boutique-pipeline/METHODE-TABLEAU.md`.

### Boutique

- Marque : **Bonum Vitae**
- Domaine public : **https://bonumvitae.fr** (site **public**, pas de mot de passe)
- Admin Shopify : **`kw7vak-g0.myshopify.com`**
- E-mail vitrine : `contact@bonumvitae.fr`
- Identité légale : OH Ventures, 47 rue Vivienne, 75002 Paris, `+33 7 56 82 80 94`, SIREN 103157251
- Thème **live actuel** : **Horizon MAIN** (c'est ce qu'on quitte)
- Thème **cible du redesign** : **FullStack 2.3** — **exactement le même thème que Tuftéo et Maison Noirmont** (`copie-de-fullstack-2-3`). Pas Horizon. Pas un autre thème.
- Catalogue public relevé le 17/08 : **24 fiches** (osmoseurs, filtres douche, carafes, robinet, nomades, anti-calcaire sans sel, consommables)
- Baseline existante : « L'eau pure, chaque jour. »
- Charte actuelle (juillet) : Bleu Abysse `#0E3A5A` · Vert Source `#35B6AA` · Laiton `#C3A15F` · Lin `#F7F4EE` · Ardoise `#1C2830` · titres Fraunces · corps Inter

Auth Shopify CLI : cibler **`--store kw7vak-g0.myshopify.com`**. `export PATH="/Users/Hakim/.npm-global/bin:$PATH"`. Mutations : `shopify store execute --allow-mutations`. Si l'auth CLI est encore sur Noirmont (`contact.noirmont@gmail.com`), ré-auth **device-code** sur le compte Bonum Vitae — ne pas improviser.

### Ce que Hakim veut

Chantier **large**, pas un correctif. On **passe Bonum Vitae sur FullStack** et on **revoit tout le design** : homepage, fiches, collections, panier, pages de marque, policies visuelles. C'est plus de travail que Noirmont (là on a gelé un storefront déjà propre).

Ordre Q4 (experts, 16/08) : Tuftéo d'abord (GMC déjà approuvé, 30 jours d'observation) → Noirmont ensuite → **osmoseur conservé, test ads relancé en septembre avec un budget suffisant**. Donc Bonum Vitae doit être **propre et redesignée** pour septembre, sans brûler l'entité pendant le chantier.

### Thème = FullStack 2.3 — lire ce qui a déjà été fait AVANT de coder

Le parc a déjà monté FullStack deux fois. **Tu ne redécouvres pas le thème.** Tu lis les builds Tuftéo et Noirmont, tu dresses l'inventaire de ce que FullStack sait faire nativement, et tu t'en sers. Coder en dur seulement si le natif ne permet pas le rendu voulu.

**Règle PLAYBOOK, ici obligatoire :** explorer sections, blocs, snippets et settings FullStack avant d'ajouter du `custom-code`. Horizon n'est plus la base d'implémentation (le skill `webdesign-boutiques` dit encore « implémenter sur Horizon » — **ignorer ça pour ce chantier**). Horizon reste une **ossature CRO à porter** (ordre des blocs, panier, FAQ), pas un thème à recopier.

**Documentation vendeur :** https://themefullstack.com/ · guides Notion du thème : https://fullstack-theme.notion.site/

**À lire avant tout montage FullStack (dans cet ordre) :**

1. Inventaire + mapping natif vs custom : `boutique-pipeline/boutique-tufting/shopify/reco-theme-brouillon-2026-07-21.md` (38 sections, 99 blocs, ce qui est natif, ce qu'il ne faut pas porter).
2. Build réel Tuftéo (home, PDP, panier, pièges) : `boutique-pipeline/boutique-tufting/shopify/structure-templates-log-2026-07-21.md` + `shopify/build-log-2026-07-21.md`.
3. Kit portable déjà extrait (paiement fractionné, bénéfices, réassurance, FAQ, icônes) : `boutique-pipeline/boutique-tufting/shopify/portable-kit/` — **source de portage prioritaire**, devant les extraits Horizon bruts.
4. Noirmont sur le même FullStack 2.3 : `boutique-pipeline/boutique-seiko-mod/journal/2026-07-24-build-site.md`, `2026-07-25-design-modernisation.md`, `2026-07-25-mining-montre-avenue.md` (pastilles, `toggle-cross-sell` natif, badges), `2026-07-31-megamenu-illustre.md`, `2026-07-31-footer-modele-tufteo.md`, `2026-08-15-json-ld-organization.md`.
5. Pièges FullStack du campement : `notion-export/campement/campement-type-lancement-boutique.md` (noms de schéma > 25 caractères, `themeFilesUpsert` vide, CSS de section refusée, SEO title/description à envoyer ensemble) + ticket panier `campement/12b-panier-banniere-upsells.md`.
6. Copies locales du thème (lecture, pas push) : `Bien Brulé/theme_live_published/` et `lihyl-lancement/theme/` si besoin de voir un fichier natif byte-exact.

**Tu t'inspires de Tuftéo et Noirmont pour le montage FullStack, pas pour la DA ni le copy.** Palette, typos, ton, visuels = Bonum Vitae (eau / foyer / pédagogie). Ni pop DIY Tuftéo, ni luxe montres Noirmont.

**Possibilités FullStack déjà éprouvées dans le parc — les utiliser, ne pas les réinventer :**

| Besoin | Natif FullStack (préférer) | Ne pas faire |
|---|---|---|
| Hero / slider | `image-banner` | Recoder un hero Horizon |
| Comparatif | `comparison-table` | Tableau HTML collé si le natif suffit |
| Marquee | `marquee` | — |
| FAQ / objections | `accordions` | — |
| Réassurance icônes | `icon-with-text` + `group` (icônes = **noms Material Symbols**, jamais d'emoji) | — |
| Bénéfices sous le prix | `icon-with-text` ou portable-kit `dp-purchase-support` | Recycler `benefits-osmoseur.liquid` tel quel |
| Estimation livraison | **`delivery-estimation`** (plus honnête que la barre Horizon « +6 jours ») | Porter `delivery-bar.liquid` |
| Paiement fractionné | portable-kit, **seulement si PayPal/Klarna réellement actifs** | Promettre 4× si inactif |
| Cross-sell sous le picker | bloc natif `_toggle-cross-sell` (vu sur montre-avenue) | Une app |
| Contenu du pack | `this-pack-contains` | — |
| Avant/après | `before-after` — **jamais santé / peau / médical** | Claims DGCCRF |
| Stories / étapes | `stories` / `tabs` | — |
| Panier tiroir | drawer natif + bannière + upsell (recette Tuftéo 12b) | App UpCart. Un `custom-code` **ne peut pas** vivre **dans** `_product-form` |
| Mégamenu illustré | blocs mégamenu (Noirmont / montre-avenue) | — |
| Pastilles couleur | donnée Shopify (métaobjets d'option), pas du CSS | Deviner la clé d'option |
| Templates produit | `product.json` + suffixes (`product.osmoseur.json`, etc.) si besoin | Copier les JSON Horizon (IDs, app TrustWILL, CDN BV) |
| HTML/CSS ponctuel | bloc / section `custom-code` | Coder en dur ce que le natif fait |

**Démo FullStack = piège GMC n°1.** Le zip vendeur arrive avec `rating-stars` 4,5/123, « 2 000 clients satisfaits », faux avis « Excellent produit ! », logos/sociaux `themefullstack`, clé Klaviyo étrangère, badge « Powered by FullStack ». **Purge obligatoire** avant toute préview publique — c'est déjà arrivé sur Tuftéo et Noirmont. Vider les 4 URL sociales **dans `settings_schema.json`** (les défauts du schéma survivent à un settings_data vide). Slider et avis de démo = chasse gardée de Hakim : proposer, ne jamais publier.

**Équivalence CRO déjà prouvée (reco Tuftéo) :** le squelette FullStack (`rating` → titre → prix → form → paiements → accordéons → réassurance, puis sections sous la flottaison) est le même ordre que le modèle Horizon osmoseur. On reconstruit sans lutter contre le thème.

### Interdits — ne pas négocier

- **Ne pas toucher Maison Noirmont** (`v42pzp-h4.myshopify.com` / maisonnoirmont.fr). Storefront **gelé** depuis le 17/08 ~15h25. Pas de GMC Noirmont, pas d'activation des 20 brouillons, pas d'écriture live. On **lit** ses journaux FullStack, on n'écrit pas sur la boutique.
- **Ne pas toucher Tuftéo** (`et0hua-w1.myshopify.com` / tufteo.com) sauf demande explicite. Son GMC est un actif (approuvé, 173 produits). On **lit** son build FullStack, on n'écrit pas sur la boutique.
- **Ne jamais `switch-shop`** sur le connecteur Shopify MCP (ça révoque le token). Toujours `--store kw7vak-g0.myshopify.com`.
- **Ne jamais écrire sur le thème MAIN / publié.** Sur Bonum Vitae le MAIN est encore Horizon : on n'y fait que le rail A (crible). FullStack se travaille sur une copie **UNPUBLISHED** → **Hakim publie**. Ne pas publier un thème.
- **Jamais `fileDelete`** sur un média produit. Détacher via `fileUpdate` + `referencesToRemove`.
- Aucune commande, aucun achat, aucun paiement.
- **Ne pas toucher au Merchant Center ni à Google Ads de Bonum Vitae.** Le compte existe déjà (app Shopify Google & YouTube). Le flux a été soumis, les produits ont d'abord été limités puis validés, et ils tiennent depuis des semaines. **On le laisse vivre** : pas de nouveau GMC, pas de resoumission, pas de campagne. Décision Hakim 18/08.
- **Policies jamais identiques mot pour mot** avec Tuftéo, Noirmont ou Bien Brûlé. Google compare entre domaines.
- GitHub = source de vérité. Fin de tâche : `git add` + commit FR + `git push` dans `boutique-pipeline/`. Si la mémoire Claude a bougé : `bash scripts/sync-memoire.sh` dans le hub, puis commit hub.
- Secrets, `.env`, `node_modules/`, `scratchpad/`, `settings.local.json` : hors git.

### Pourquoi ce chantier est plus dangereux que Noirmont

Les quatre boutiques publient **la même adresse et le même téléphone**. Hakim a **assumé le linkage** le 16/08. Une misrepresentation sur Bonum Vitae dégrade **l'entité OH Ventures**, donc le GMC Tuftéo **et** le GMC Bonum Vitae (flux déjà validé, à laisser vivre). Précédent : compte GMC **5806019978** suspendu le 15/06 pour faux avis, puis réintégré.

Le crible entité (`CHANTIER-CRIBLE-ENTITE.md`) classait Bonum Vitae **« jamais auditée »**. Le live du 17/08 montre que ce n'est plus une hypothèse.

### Constat live du 17/08 (à revérifier, pas à tenir pour soldé)

**P0 — faux avis publics, motif exact de la suspension de juin.** Accueil : 3 témoignages « Vérifié », prénoms = personas de juillet (Claire M., Karim B., Bernard L.), datés « il y a 3 jours / 1 semaine / 2 semaines ». Référence Horizon : `bv-avis-clients`. Fiches : ligne **« 4.8/5 basé sur 312 avis vérifiés »** codée en dur (`rating-row.liquid`) — **0 commande client** sur le parc.

**P0 — prix barrés (loi Omnibus).** Exemples publics : osmoseur RO 600G **299 € barré 470 €** ; osmoseur 600 GPD **576,90 € barré 700 €** ; plusieurs anti-calcaire barrés. Un barré n'est légal que s'il a été **réellement pratiqué**.

**P1 — allégations.** Niche eau = DGCCRF + GMC claims santé. Interdit : « adoucit l'eau / élimine le calcaire / réduit la dureté » sur l'anti-calcaire magnétique/électronique ; « prévient / détoxifie / soigne ». L'avis Karim (« Ma peau la remercie », « moins de tiraillement ») est un claim santé déguisé. Pas d'imagerie médicale, pas d'avant/après santé.

**P1 — promesses à recouper.** FAQ : expédition 24–48 h, livraison 6–10 j ouvrés. Newsletter : −10 % première commande. Hero : « sans travaux ni plombier » (un osmoseur sous évier peut nécessiter une intervention). Bandeau historique : « −20 % sur les osmoseurs » (preuve manquante au 18/07).

**Collections publiques :** osmoseurs, filtres-de-douche, carafes-filtrantes, filtres-robinet, purificateurs-nomades, anti-calcaire-sans-sel. Red flag Terry : collection **< 5 produits**.

### Sources à lire (dans cet ordre)

1. `CHANTIER-CRIBLE-ENTITE.md` + `PASSATION.md` (question 0 : identité partagée)
2. Skill `gmc-acceptance` (`.claude/skills/gmc-acceptance/SKILL.md` + `references/checklist-pre-soumission.md`)
3. Skill `webdesign-boutiques` (DA / ui-ux-pro-max / mobile-first) — **implémentation = FullStack, pas Horizon**
4. Skill global `shopify-liquid` + agent `.claude/agents/executant-boutique.md` (recette thème : jamais MAIN, md5, staged upload)
5. Les fichiers FullStack listés plus haut (reco Tuftéo → portable-kit → journaux Noirmont)
6. `New project/outputs/bonumvitae-branding-2026-07-11/positionnement-marketing-bonumvitae.md` (positionnement, 3 piliers, personas Claire/Karim/Bernard, garde-fous DGCCRF)
7. Ossature CRO Horizon (plan de lecture seulement) : `boutique-pipeline/docs/horizon-product-page-reference/` + `notion-export/modeles/modele-*-horizon.md`
8. Mémoire : `memoire/identite-partagee-gmc.md`, `workflow-theme-live-copie-travail.md`, `persona-obligatoire-copywriting.md`, `promesses-verifiables-guide-numerique.md`, `shopify-canal-et-visuels-ia.md`, `da-creative-pas-premium-fade.md` (cette dernière = DIY/Tuftéo ; **ne pas** coller du pop stickers sur de l'eau)
9. Pages légales d'origine : `New project/outputs/bonumvitae-pages-legales-2026-07-12/` — à recouper au live, pas à recoller telles quelles

Pas de persona validé au format maison (`boutique-pipeline/personas/` n'a que Tuftéo et Noirmont). Les Claire/Karim/Bernard de juillet sont un brief de marque, **pas** un persona PLAYBOOK 1d.

### Méthode — deux rails, pas un seul

**Rail A — crible live (d'abord, chirurgical, sur Horizon publié).** Tant que Claire/Karim/Bernard « Vérifié » et les 312 avis sont publics, le GMC Tuftéo est exposé. Corriger les déclencheurs **sur le live**, sans attendre FullStack : faux avis / notes / compteurs, prix barrés injustifiés, claims santé, filigranes, fausse urgence. Vérifier en visiteur anonyme. Ne pas « remettre la boutique à la perfection » sur l'ancien Horizon : juste cesser de nuire.

**Rail B — redesign FullStack (le gros du travail).**

1. **Snapshot.** `get-shop-info`, thèmes (id + role — vérifier si FullStack est déjà installé sur `kw7vak-g0` ou s'il faut que Hakim l'ajoute), catalogue (statuts, compare-at, collections < 5), policies, apps d'avis, paiements réels (`shop.enabled_payment_types`). **GMC : il existe déjà** (app Google & YouTube, flux validé) — le constater, ne pas y toucher. Écrire `ETAT.md`.
2. **Persona.** Produire `boutique-pipeline/personas/persona-bonum-vitae-YYYY-MM-DD.md` depuis `templates/persona.template.md`. Preuves `[O]`/`[D]`. **Hakim valide avant tout copy et avant toute DA.** Persona = particulier qui découvre, pas un pro de l'eau.
3. **DA — 2 ou 3 directions, puis stop.** Skill `webdesign-boutiques` + `python3 ~/.claude/skills/ui-ux-pro-max/scripts/search.py`. Palette + typos + 3 références + anti-patterns. **Attendre le choix de Hakim.** Eau / bien-être / foyer : pédagogie, clarté, confiance. Ni « premium fade » froid, ni pop DIY type Tuftéo, ni luxe montres. La charte Abysse/Source de juillet est un **point de départ**, pas un verrou.
4. **FullStack.** Si le thème n'est pas sur la boutique : Hakim l'installe (zip / copie depuis une autre boutique — licence à confirmer). Dupliquer. Travailler **uniquement** la copie UNPUBLISHED. **Première tâche thème = lire l'inventaire reco Tuftéo + lister, pour Bonum Vitae, ce qui sera natif vs custom.** Purger la démo vendeur. Appliquer la DA validée via `settings_data.json` (schemes, polices). Reconstruire `index.json`, `product.json`, header/footer/panier avec les patterns Tuftéo/Noirmont. Logos paiement ré-uploadés sur le CDN Bonum Vitae (jamais d'URL `cdn` Tuftéo/Noirmont/ancien Horizon).
5. **QA mobile-first** (375 px d'abord, breakpoint FullStack 750 px) sur l'aperçu `preview_theme_id` (session navigateur — `curl` perd le paramètre). Hakim publie.
6. **GMC — actif déjà en production, on le protège.** Bonum Vitae a le même montage que Tuftéo : app Google & YouTube, flux soumis, produits validés après une phase limitée. **Ne pas créer, lier, resoumettre, ni lancer d'ads.** Le skill `gmc-acceptance` sert à auditer le storefront (rail A + cohérence après publication FullStack), pas à ouvrir un compte. Un changement de thème sur un GMC établi est un **changement brutal** : une seule publication propre, puis calme. Workspace / e-mail pro : Hakim s'en occupe ; ne pas changer l'e-mail du GMC d'un coup.

`themeFilesUpsert` peut renvoyer `upsertedThemeFiles: []` sans erreur alors que ça a marché (ou l'inverse). Vérifier par **empreinte md5** + relecture du contenu. Templates JSON ~125 ko : staged upload, pas TEXT. Nom de schéma de bloc > 25 caractères = rejet silencieux.

### Skills à invoquer

- `gmc-acceptance` pour auditer le storefront (pas pour créer/soumettre un GMC)
- `webdesign-boutiques` + `ui-ux-pro-max` dès la DA
- `shopify-liquid` dès le thème
- `copywriting` / `cro` / `ecommerce-copywriting` **après** persona validé
- `customer-research` pour prouver le persona
- `higgsfield-product-photoshoot` / visuels composés si on refait les photos — **jamais** la photo AliExpress brute ; partir de la photo fournisseur, ne changer que la mise en scène ; pas de texte incrusté GMC

### Première réponse attendue

1. Confirmer le store (`kw7vak-g0` = Bonum Vitae) avant toute écriture.
2. Créer `TABLEAU.md` / `ETAT.md` / `REGLES.md` et un journal daté.
3. Rail A : lister les déclencheurs **encore publics** avec URL + citation, proposer le correctif chirurgical (surtout retirer les faux avis).
4. Rail B : dire si FullStack est déjà installé sur la boutique ; **ne pas** poser de DA avant persona validé ; **ne pas** coder avant d'avoir lu la reco Tuftéo et listé natif vs custom.
5. Une liste courte « à faire Hakim » (auth CLI, installer FullStack si absent, publication, persona, DA).

Ne commence pas par coder un thème. Le premier livrable est un état vrai + les P0 qui exposent l'entité.
