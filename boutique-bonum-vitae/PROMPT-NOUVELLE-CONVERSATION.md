# Prompt — nouvelle conversation Bonum Vitae

> **17/08/2026.** À coller tel quel dans une conversation neuve. Point d'entrée une fois le chantier ouvert : ce dossier, puis `TABLEAU.md` (à créer en première tâche).

---

## Texte à coller

Tu travailles avec Hakim (ops, SASU OH Ventures) sur **Bonum Vitae**, boutique de traitement de l'eau au point d'usage. Hakim l'a nommée **« la boutique de Lost Mother »** : c'est le site actuel qu'on va remplacer (thème + DA + pages). Aucune autre trace de « Lost Mother » dans le dépôt — si c'est un designer, des fichiers ou un contrat, demande-le une fois, puis avance sur le live.

Workspace : `/Users/Hakim/Documents/Boutiques drop`. Repo de travail : `boutique-pipeline/` (GitHub `HakimOuah/boutique-pipeline`, branche `main`). Dossier à créer et à tenir à jour : `boutique-pipeline/boutique-bonum-vitae/` (`TABLEAU.md`, `ETAT.md`, `REGLES.md`, `journal/`, `backups/`). Convention : `boutique-pipeline/METHODE-TABLEAU.md`.

### Boutique

- Marque : **Bonum Vitae**
- Domaine public : **https://bonumvitae.fr** (site **public**, pas de mot de passe)
- Admin Shopify : **`kw7vak-g0.myshopify.com`**
- E-mail vitrine : `contact@bonumvitae.fr`
- Identité légale : OH Ventures, 47 rue Vivienne, 75002 Paris, `+33 7 56 82 80 94`, SIREN 103157251
- Thème live au 18/07 (à revérifier) : **Horizon MAIN**
- Catalogue public relevé le 17/08 : **24 fiches** (osmoseurs, filtres douche, carafes, robinet, nomades, anti-calcaire sans sel, consommables)
- Baseline existante : « L'eau pure, chaque jour. »
- Charte actuelle (juillet) : Bleu Abysse `#0E3A5A` · Vert Source `#35B6AA` · Laiton `#C3A15F` · Lin `#F7F4EE` · Ardoise `#1C2830` · titres Fraunces · corps Inter

Auth Shopify CLI : cibler **`--store kw7vak-g0.myshopify.com`**. `export PATH="/Users/Hakim/.npm-global/bin:$PATH"`. Mutations : `shopify store execute --allow-mutations`. Si l'auth CLI est encore sur Noirmont (`contact.noirmont@gmail.com`), ré-auth **device-code** sur le compte Bonum Vitae — ne pas improviser.

### Ce que Hakim veut

Chantier **large**, pas un correctif. On **change de thème** et on **revoit tout le design** : homepage, fiches, collections, panier, pages de marque, policies visuelles. C'est plus de travail que Noirmont (là on a gelé un storefront déjà propre).

Ordre Q4 (experts, 16/08) : Tuftéo d'abord (GMC déjà approuvé, 30 jours d'observation) → Noirmont ensuite → **osmoseur conservé, test ads relancé en septembre avec un budget suffisant**. Donc Bonum Vitae doit être **propre et redesignée** pour septembre, sans brûler l'entité pendant le chantier.

### Interdits — ne pas négocier

- **Ne pas toucher Maison Noirmont** (`v42pzp-h4.myshopify.com` / maisonnoirmont.fr). Storefront **gelé** depuis le 17/08 ~15h25. Pas de GMC Noirmont, pas d'activation des 20 brouillons, pas d'écriture live.
- **Ne pas toucher Tuftéo** (`et0hua-w1.myshopify.com` / tufteo.com) sauf demande explicite. Son GMC est un actif (approuvé, 173 produits).
- **Ne jamais `switch-shop`** sur le connecteur Shopify MCP (ça révoque le token). Toujours `--store kw7vak-g0.myshopify.com`.
- **Ne jamais écrire sur le thème MAIN / publié.** Dupliquer (`themeDuplicate`) → travailler la copie UNPUBLISHED → **Hakim publie**. Ne pas publier un thème.
- **Jamais `fileDelete`** sur un média produit. Détacher via `fileUpdate` + `referencesToRemove`.
- Aucune commande, aucun achat, aucun paiement. Ne pas modifier Google Ads ni Merchant Center sauf ticket explicite.
- **Policies jamais identiques mot pour mot** avec Tuftéo, Noirmont ou Bien Brûlé. Google compare entre domaines.
- GitHub = source de vérité. Fin de tâche : `git add` + commit FR + `git push` dans `boutique-pipeline/`. Si la mémoire Claude a bougé : `bash scripts/sync-memoire.sh` dans le hub, puis commit hub.
- Secrets, `.env`, `node_modules/`, `scratchpad/`, `settings.local.json` : hors git.

### Pourquoi ce chantier est plus dangereux que Noirmont

Les quatre boutiques publient **la même adresse et le même téléphone**. Hakim a **assumé le linkage** le 16/08. Une misrepresentation sur Bonum Vitae dégrade **l'entité OH Ventures**, donc le GMC Tuftéo. Précédent : compte GMC **5806019978** suspendu le 15/06 pour faux avis, puis réintégré.

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
3. Skill `webdesign-boutiques` (`.claude/skills/webdesign-boutiques/SKILL.md`) + skill global `ui-ux-pro-max`
4. Skill global `shopify-liquid` + agent `.claude/agents/executant-boutique.md` (recette thème : jamais MAIN, md5, staged upload)
5. `New project/outputs/bonumvitae-branding-2026-07-11/positionnement-marketing-bonumvitae.md` (positionnement, 3 piliers, personas Claire/Karim/Bernard, garde-fous DGCCRF)
6. Référence structure (ossature CRO à **porter**, pas à recopier telle quelle) : `boutique-pipeline/docs/horizon-product-page-reference/` + `notion-export/modeles/modele-*-horizon.md`
7. Mémoire : `memoire/identite-partagee-gmc.md`, `workflow-theme-live-copie-travail.md`, `persona-obligatoire-copywriting.md`, `promesses-verifiables-guide-numerique.md`, `da-creative-pas-premium-fade.md` (cette dernière = DIY/Tuftéo ; **ne pas** coller du pop stickers sur de l'eau)
8. Pages légales d'origine : `New project/outputs/bonumvitae-pages-legales-2026-07-12/` — à recouper au live, pas à recoller telles quelles

Pas de persona validé au format maison (`boutique-pipeline/personas/` n'a que Tuftéo et Noirmont). Les Claire/Karim/Bernard de juillet sont un brief de marque, **pas** un persona PLAYBOOK 1d.

### Méthode — deux rails, pas un seul

**Rail A — crible live (d'abord, chirurgical).** Tant que Claire/Karim/Bernard « Vérifié » et les 312 avis sont publics, le GMC Tuftéo est exposé. Corriger les déclencheurs **sur le live**, sans attendre le nouveau thème : faux avis / notes / compteurs, prix barrés injustifiés, claims santé, filigranes, fausse urgence. Vérifier en visiteur anonyme. Ne pas « remettre la boutique à la perfection » sur l'ancien Horizon : juste cesser de nuire.

**Rail B — redesign (le gros du travail).** Changement de thème + DA complète.

1. **Snapshot.** `get-shop-info`, thèmes (id + role), catalogue (statuts, compare-at, collections < 5), policies, apps d'avis, paiements réels (`shop.enabled_payment_types`), GMC existant ou non. Écrire `ETAT.md`.
2. **Persona.** Produire `boutique-pipeline/personas/persona-bonum-vitae-YYYY-MM-DD.md` depuis `templates/persona.template.md`. Preuves `[O]`/`[D]`. **Hakim valide avant tout copy et avant toute DA.** Persona = particulier qui découvre, pas un pro de l'eau.
3. **DA — 2 ou 3 directions, puis stop.** Skill `webdesign-boutiques` + `python3 ~/.claude/skills/ui-ux-pro-max/scripts/search.py`. Palette + typos + 3 références + anti-patterns. **Attendre le choix de Hakim.** Eau / bien-être / foyer : pédagogie, clarté, confiance. Ni « premium fade » froid, ni pop DIY type Tuftéo, ni luxe montres. La charte Abysse/Source de juillet est un **point de départ**, pas un verrou — Hakim change de thème, la DA peut bouger.
4. **Thème.** Hakim installe / choisit le thème. Dupliquer. Travailler **uniquement** la copie. Explorer les sections natives **avant** de coder en dur. Porter l'ossature CRO (bénéfices sous le prix, add-to-cart simple, réassurance vraie, panier avec bannière livraison + upsell, FAQ d'objections) — pas les textes, pas les faux avis, pas les IDs Horizon.
5. **QA mobile-first** (375 px d'abord) sur l'aperçu `preview_theme_id`. Hakim publie.
6. **GMC.** Skill `gmc-acceptance` en pass/fail **après** le thème publié et les policies recoupées. **Ne pas créer / soumettre un GMC** sans verdict PRÊT et sans feu vert Hakim. Si un GMC Bonum Vitae existe déjà (comme Tuftéo via l'app Google & YouTube), le signaler tout de suite : un changement de thème sur un compte établi est un **changement brutal** — une seule publication propre, puis calme.

`themeFilesUpsert` peut renvoyer `upsertedThemeFiles: []` sans erreur alors que ça a marché (ou l'inverse). Vérifier par **empreinte md5** + relecture du contenu. Templates JSON ~125 ko : staged upload, pas TEXT.

### Skills à invoquer

- `gmc-acceptance` dès l'audit et avant tout GMC
- `webdesign-boutiques` + `ui-ux-pro-max` dès la DA
- `shopify-liquid` dès le thème
- `copywriting` / `cro` / `ecommerce-copywriting` **après** persona validé
- `customer-research` pour prouver le persona
- `higgsfield-product-photoshoot` / visuels composés si on refait les photos — **jamais** la photo AliExpress brute ; partir de la photo fournisseur, ne changer que la mise en scène ; pas de texte incrusté GMC

### Première réponse attendue

1. Confirmer le store (`kw7vak-g0` = Bonum Vitae) avant toute écriture.
2. Créer `TABLEAU.md` / `ETAT.md` / `REGLES.md` et un journal daté.
3. Rail A : lister les déclencheurs **encore publics** avec URL + citation, proposer le correctif chirurgical (surtout retirer les faux avis).
4. Rail B : dire où en est le persona, et **ne pas** poser de DA avant validation.
5. Une liste courte « à faire Hakim » (auth CLI, choix du thème, publication, persona, DA).

Ne commence pas par coder un thème. Le premier livrable est un état vrai + les P0 qui exposent l'entité.
