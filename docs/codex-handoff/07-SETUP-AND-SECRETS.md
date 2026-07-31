# 07 — Installation, connexions et secrets

> Dossier de passation Codex — généré le 2026-07-30. Étiquettes de source obligatoires.
> ⛔ Ce document ne contient **aucune valeur de secret** — uniquement les noms et où récupérer les valeurs.

---

## 1. Installation locale réelle

Ce qui existe et fonctionne sur le Mac de Hakim :

- **Aucun service permanent.** Tout se lance en session (Claude Code + MCP + Chrome). **[FAIT — repo : aucun process, aucun état d'exécution]**
- **Python 3** : scripts starter-kit (`scripts/new_boutique.py`, `validate_tokens.py`, `tokens_to_theme.py`) et tests `python3 -m pytest`. `/usr/bin/python3` a déjà PyYAML et pytest ; **ne pas utiliser le Python Homebrew 3.14 sans installer les dépendances** (piège documenté). **[FAIT — repo:docs/OPERATIONS.md]**
- **Dropilot** (optionnel, prototype) : `python3 -m venv .venv && .venv/bin/pip install -e '.[dev]' && .venv/bin/dropilot init-db`. Aucun `.venv`, aucun `.env`, aucune base SQLite présents dans le dépôt au 30/07 → **jamais installé en l'état**. **[FAIT — repo]**
- **Node** : scripts ad hoc `.mjs` de `boutique-seiko-mod/` (uploads visuels Shopify). Pas de `package.json` au niveau du dépôt : les scripts utilisent Node natif (fetch). **[FAIT — repo]**
- Un venv jetable existe dans `tmp/venv/` (openpyxl, pour construire des xlsx) — outil de session, pas une installation. **[FAIT — repo:tmp/]**

## 2. GitHub / remote

- **Remote privé configuré** : `origin` = `https://github.com/HakimOuah/boutique-pipeline.git` (dépôt privé). **[FAIT — repo:.git, 31/07]** [CORRIGÉ 31/07 : remote créé et dépôt poussé — l'audit initial du 30/07 constatait « aucun remote ».]
- Branche courante `main`, arbre propre, HEAD local = HEAD distant, poussé le 31/07. **[FAIT — repo]**
- Conséquence passation : Codex peut cloner le dépôt privé dès que Hakim lui accorde l'accès GitHub. La purge du mot de passe storefront (§4) reste à faire.

## 3. Connexions et comptes, service par service

### 3.1 Shopify

| Élément | Valeur / où la trouver | Source |
|---|---|---|
| Boutique active du connecteur MCP | **Maison Noirmont** — `v42pzp-h4.myshopify.com` / `maisonnoirmont.fr`, plan Basic, EUR, e-mail compte `contact.noirmont@gmail.com` | **[FAIT — Shopify API get-shop-info, 30/07]** |
| Boutique Tuftéo | `et0hua-w1.myshopify.com` / `tufteo.com`, thème live `188623847809` ; bloc « Accès & Shopify » complété le 30/07 après vérification publique | **[FAIT — HTML/HTTP public `tufteo.com`, 30/07/2026]** |
| Anciennes boutiques | Bien Brûlé `2npa6w-x0.myshopify.com` (bienbrule.com), Lihyl `s001ti-nw.myshopify.com` (lihyl.fr) | **[FAIT — repo parent:CONTEXTE-MEMOIRE-pour-Codex.md]** [OBSOLÈTE POSSIBLE] |
| Accès en écriture | Via connecteur MCP Shopify de Claude (OAuth géré par le connecteur — **aucun token API en clair trouvé dans le dépôt**, ce qui est bien). Pour Codex : créer une app custom Admin API par boutique et stocker le token hors git | **[FAIT — repo : recherche `shpat_`/tokens = 0 résultat]** |
| Permissions constatées | Lecture/écriture produits, collections, publications, metafields, Files, thèmes **non publiés uniquement** | **[FAIT — repo:boutique-seiko-mod/*]** |

**Pièges Shopify vérifiés** (détail dans `boutique-seiko-mod/REPRISE-SESSION.md` §Pièges) **[FAIT — repo]** :
- ⛔ **Ne jamais utiliser `switch-shop`** : invalide la connexion Shopify **pour tout le monde**.
- Le connecteur refuse d'écrire un thème MAIN ; tout passe par le thème brouillon (`204248088914` chez Noirmont), qu'il **reste à republier**.
- `upsertedThemeFiles: []` sans `userErrors` = écriture asynchrone, pas un échec ; valider par taille/MD5.
- Requêtes média plafonnées à 30 (paginer) ; menus partagés entre thèmes (créer un menu neuf).
- Produits DSers/API = ACTIVE mais publiés sur **aucun canal** → `publishablePublish` en batch. **[MÉMOIRE — shopify-canal-et-visuels-ia.md]**

### 3.2 DSers (mapping AliExpress → Shopify)

- Compte Noirmont : session Chrome `contact.noirmont` (98 produits mappés, 0 Unmapped). **[FAIT — repo:boutique-seiko-mod/dsers-mapping-*.md, REPRISE-SESSION.md]**
- Compte Tuftéo : `contact@bonumvitae.fr` est mentionné dans le brief de mission de Hakim, mais **aucune trace dans le dépôt ni dans la mémoire** → [MANQUANT — à confirmer par Hakim, avec le gestionnaire de mots de passe].
- Accès : uniquement par **session Chrome déjà ouverte** ; aucune API, aucun identifiant stocké. Les opérations DSers documentées se font par navigation pilotée. **[FAIT — repo]**

### 3.3 Notion

- Workspace **OH VENTURES**, connecteur MCP. Hub « Pipeline Boutiques Drop » : base Recherches produit (db `b23a48625ace4704980659f165bb0ec6`), base Boutiques (db `3a26f4af523d448a907fce7b45b42bcc`), Campement type (db `da8b39cc1a4248f2aec7494df5ef247b`). **[MÉMOIRE — notion-pipeline-boutiques.md, campement-type-lancement-boutique.md]**
- Rôle : dashboard uniquement ; écrire local d'abord, répliquer ensuite. **[MÉMOIRE]**
- Limite plan : requêtes SQL sur data sources limitées ; création OK. **[MÉMOIRE]**
- Pour Codex : soit intégration Notion API officielle (token d'intégration à créer dans le workspace, non présent dans le dépôt), soit ignorer Notion au début. [MANQUANT — token/intégration côté Codex]

### 3.4 SEMrush

- Compte **payant** (récent), utilisé pour toutes les mesures de volume FR (`marche-complet-semrush.md`, phase 0/3). Accès **par session Chrome connectée**, jamais par API. **[FAIT — repo:boutique-seiko-mod/REPRISE-SESSION.md ; .claude/skills/chasse-clusters/SKILL.md]**
- ⚠️ [CONTRADICTOIRE — `../CONTEXTE-MEMOIRE-pour-Codex.md` (06/2026) : « pas de compte permanent, Semrush OFF par défaut » et PLAYBOOK.md phase 1b « Semrush désactivé par défaut » vs usages intensifs de juillet sur compte payant]. Résolution probable : abonnement pris en juillet ; PLAYBOOK à mettre à jour. **À valider par Hakim.**
- Piège : en formule gratuite, SEMrush rend « 0 mot-clé » **sans erreur** au-delà du quota → toujours utiliser un mot-clé témoin. **[FAIT — repo:REPRISE-SESSION.md]**

### 3.5 Brand Search

- MCP connecté (serveur `909b5b93-…`) + UI web `app.brandsearch.co` (session Chrome de Hakim, filtres plus riches). **[MÉMOIRE — brand-search-source-idees.md]**
- Quota : **10 000 requêtes/mois** — vérifier via `get_usage` en début de session ; budget ≤ 100/session ; < 200 restantes → repli navigateur. **[MÉMOIRE]**
- Pièges : `markets` inopérant (utiliser `country_code: FR`), `avg_price_usd: 0.0` = donnée manquante, revenus = fourchettes modélisées. **[MÉMOIRE]**

### 3.6 Higgsfield (visuels IA)

- MCP connecté ; skills dédiés `higgsfield-*` installés en global. **[FAIT — ~/.claude/skills/]** Compte/crédits : gérés dans le connecteur, aucune clé dans le dépôt. [MANQUANT — modalités du compte]
- Piège : faux logos imprimés sur les cadrans → compositions qui cachent le cadran + inpainting OpenCV local ; vérifier chaque image à l'œil. **[MÉMOIRE — shopify-canal-et-visuels-ia.md]**

### 3.7 Chrome et sessions (le vrai trousseau)

L'accès réel à SEMrush, DSers, AliExpress, Brand Search web, Trustoo et à l'admin Shopify passe par **les sessions déjà ouvertes du Chrome de Hakim**, pilotées via le MCP claude-in-chrome. **[FAIT — repo : dizaines de rapports « session déjà ouverte, aucun identifiant saisi »]**
- Règle absolue observée par les agents : **ne jamais saisir un identifiant ou un mot de passe**, même fourni. **[FAIT — repo:megamenu-illustre.md]**
- Profil(s) Chrome : un seul profil est attesté par les rapports (celui portant `contact.noirmont` + SEMrush + AliExpress). Détail des profils par boutique : [MANQUANT].
- Trustoo (avis) : page bookmarklet `https://appadmin.trustoo.io/bookmark_import` + une `api_key` Trustoo passée en `postMessage` — la clé n'est **pas** stockée dans le dépôt ; elle se récupère dans l'app Trustoo de la boutique. **[MÉMOIRE — import-avis-trustoo-bookmark.md]**

### 3.8 Webhooks / callbacks

- Le seul webhook du projet est le **serveur HTTP dropilot** (`automation/start-webhook.sh` → `dropilot.cli serve` sur `127.0.0.1:8787`, Bearer `DROPILOT_WEBHOOK_TOKEN`), prévu pour n8n/Hermes sur un VPS — **jamais déployé** d'après le dépôt. **[FAIT — repo:automation/, deploy/systemd/]**
- Webhooks Shopify, callbacks OAuth, crons locaux : **[MANQUANT] aucune trace.**

### 3.9 BigBuy

- Connecteur code (`dropilot/sources/bigbuy.py`, sandbox par défaut, `BIGBUY_API_KEY` par env). Aucune clé trouvée, aucun usage réel constaté (inbox vide). Statut : prototype. **[FAIT — repo]**

## 4. Secrets — état des lieux et stockages non sécurisés

Recherche effectuée sur tout le dépôt (`shpat_`, `api_key=`, `Bearer`, `password`, etc.). Résultats :

1. ⚠️ **Mot de passe storefront Noirmont écrit en clair** dans au moins 3 fichiers de livrables/mémoire :
   - `boutique-pipeline/boutique-seiko-mod/build-site-2026-07-24.md` (ligne 4) ;
   - `boutique-pipeline/boutique-seiko-mod/branchement-galeries-codex.md` (ligne 218) ;
   - la fiche mémoire `~/.claude/projects/-Users-Hakim-Documents-Boutiques-drop/memory/shopify-canal-et-visuels-ia.md`.
   **La valeur n'est pas recopiée ici.** Gravité modérée (mot de passe de vitrine « ouverture prochaine », pas un accès admin), mais c'est un **stockage non sécurisé** : à purger des fichiers et à faire tourner dans l'admin Shopify (Préférences) après purge — d'autant plus urgent que le dépôt a été poussé le 31/07 vers le remote privé (voir §2). **[FAIT — repo]**
2. ✅ Aucun token API (Shopify, Notion, BigBuy, Trustoo, Higgsfield) en clair dans le dépôt. **[FAIT — repo]**
3. ✅ `.gitignore` exclut `.env`. **[FAIT — repo:.gitignore]**
4. ℹ️ Données d'entreprise sensibles mais publiques (SIREN, TVA intracom, adresse, téléphone d'OH Ventures) figurent dans `../CONTEXTE-MEMOIRE-pour-Codex.md` — registre public, pas un secret, mais à savoir avant de partager le dossier. **[FAIT — repo parent]**

**Recommandation** : centraliser tous les secrets dans un gestionnaire (1Password/Bitwarden) + un `.env` local jamais commité, en suivant `docs/codex-handoff/.env.example` (créé avec ce dossier). Les mots de passe storefront se lisent dans l'admin Shopify → Préférences, jamais dans un markdown.

## 5. Checklist de connexion pour un repreneur (Codex)

1. Obtenir l'accès au dépôt privé GitHub `HakimOuah/boutique-pipeline` (ou au Mac) — voir §2.
2. Shopify : créer une app custom Admin API sur `v42pzp-h4` (Noirmont) et sur `et0hua-w1` (Tuftéo) ; scopes produits/thèmes/publications ; token dans `.env`.
3. DSers : demander à Hakim les comptes exacts par boutique (seul `contact.noirmont` est attesté) ; l'accès restera par navigateur.
4. SEMrush / Brand Search / Trustoo : accès par sessions navigateur de Hakim ou identifiants via gestionnaire de mots de passe — jamais en clair dans le dépôt.
5. Notion : créer une intégration workspace OH VENTURES si la synchro dashboard doit continuer.
6. Respecter les pièges §3.1 (surtout `switch-shop` et thème MAIN) — ils ont tous coûté du temps réel.
