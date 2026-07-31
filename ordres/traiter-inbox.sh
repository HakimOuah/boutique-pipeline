#!/bin/bash
# traiter-inbox.sh — régime synchrone du protocole d'ordres (Codex → Claude Code).
#
# Point d'entrée UNIQUE appelé par Codex : dépose tes ordres dans ordres/inbox/,
# puis `bash ordres/traiter-inbox.sh`, puis lis ordres/resultats/<nom>.json.
#
# Protocole complet : docs/codex-handoff/14-PROTOCOLE-ORDRES.md (section « Régime synchrone »).
# Mode d'emploi côté Codex : docs/codex-handoff/12-CODEX-INSTRUCTIONS.md §7.
#
# Codes de sortie :
#   0 = dépouillement terminé (ou rien à traiter). Le SUCCÈS PAR ORDRE ne se lit
#       JAMAIS ici : il se lit dans resultats/ / rejetes/ / attente-hakim/.
#   2 = exécutant déjà actif (verrou frais ordres/.lock) — attendre et réessayer,
#       JAMAIS forcer le verrou.
#   3 = échec du lancement de la session headless (claude introuvable ou sortie en erreur).
set -u

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ORDRES_DIR="$REPO_ROOT/ordres"
LOCK_FILE="$ORDRES_DIR/.lock"
JOURNAL_DIR="$ORDRES_DIR/journal"
LOCK_MAX_AGE_MIN=30

# ---------------------------------------------------------------------------
# 1. Verrou d'exécutant unique (la boîte ET le navigateur sont des ressources uniques)
# ---------------------------------------------------------------------------
if [ -f "$LOCK_FILE" ]; then
  now=$(date +%s)
  lock_mtime=$(stat -f %m "$LOCK_FILE" 2>/dev/null || stat -c %Y "$LOCK_FILE" 2>/dev/null || echo 0)
  age_min=$(( (now - lock_mtime) / 60 ))
  if [ "$age_min" -lt "$LOCK_MAX_AGE_MIN" ]; then
    echo "exécutant déjà actif : verrou $LOCK_FILE (âge ${age_min} min < ${LOCK_MAX_AGE_MIN} min)." >&2
    echo "Attendre et réessayer — ne JAMAIS supprimer le verrou à la main." >&2
    exit 2
  fi
  echo "verrou périmé (âge ${age_min} min > ${LOCK_MAX_AGE_MIN} min) — remplacé. Contenu :" >&2
  cat "$LOCK_FILE" >&2 || true
  rm -f "$LOCK_FILE"
fi

# ---------------------------------------------------------------------------
# 2. Inbox vide (hors exemples/) → rien à traiter
# ---------------------------------------------------------------------------
shopt -s nullglob
ordres_en_attente=("$ORDRES_DIR/inbox/"*.json)
shopt -u nullglob
if [ "${#ordres_en_attente[@]}" -eq 0 ]; then
  echo "rien à traiter : ordres/inbox/ est vide (hors exemples/)."
  exit 0
fi
echo "${#ordres_en_attente[@]} ordre(s) en attente dans ordres/inbox/."

# ---------------------------------------------------------------------------
# 3. Pose du verrou (avant claude -p) — retiré dans TOUS les cas par le trap
# ---------------------------------------------------------------------------
printf 'pid=%s\nhorodatage=%s\nscript=%s\n' "$$" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$0" > "$LOCK_FILE"
trap 'rm -f "$LOCK_FILE"' EXIT INT TERM

mkdir -p "$JOURNAL_DIR"
[ -f "$JOURNAL_DIR/.gitkeep" ] || touch "$JOURNAL_DIR/.gitkeep"
JOURNAL="$JOURNAL_DIR/$(date +%Y%m%d-%H%M%S).log"

# ---------------------------------------------------------------------------
# 4. Lancement de la session headless de dépouillement
#
# Le prompt NE duplique PAS le protocole : il renvoie au prompt canonique du §7
# de 14-PROTOCOLE-ORDRES.md, plus les règles propres au régime synchrone :
# navigateur Playwright MCP limité aux 3 types AliExpress de classe A (blocage
# anti-bot constaté le 31/07 → failed `anti_bot_challenge` fail-closed), tout
# le reste sans session → failed `requires_interactive_session`.
# ---------------------------------------------------------------------------
PROMPT="Tu es l'exécutant headless du régime synchrone du protocole d'ordres.
Lis \`ordres/README.md\`, puis applique EXACTEMENT le prompt de dépouillement
canonique du §7 de \`docs/codex-handoff/14-PROTOCOLE-ORDRES.md\` aux ordres de
\`ordres/inbox/\` (hors \`exemples/\`).
Cycle de vie : pour TOUT déplacement d'un ordre entre états, utilise UNIQUEMENT
\`bash ordres/classer_ordre.sh <fichier> <etat>\` (etat : en-cours | resultats |
rejetes | attente-hakim). N'utilise ni mv ni rm directement — le chemin du
dépôt contient un espace et les autorisations les bloquent. Un ordre classé ne
doit JAMAIS rester en inbox.
Règle du régime synchrone (14, section « Régime synchrone ») : tu tournes en
headless, avec un navigateur Playwright MCP (outils \`mcp__playwright__*\`,
profil dédié, JAMAIS le Chrome de Hakim) limité à la navigation et à la
lecture. Ce navigateur autorise UNIQUEMENT les trois types AliExpress de
classe A : \`extract_aliexpress_product\`, \`search_aliexpress_products\`,
\`compare_aliexpress_suppliers\`.
Recette AliExpress (08 §1.2) : passe par l'URL directe
\`https://fr.aliexpress.com/item/<item_id>.html\` (les URL de recherche
déclenchent souvent le challenge anti-bot, les URL directes passent) ;
extrais depuis le snapshot d'accessibilité ; le résultat suit le contrat de
sortie du type (08 §2.2), données vendeur \`annonce_par_vendeur\`, \`releve_le\`
daté. Une redirection de locale (ex. pt.aliexpress.com) n'est pas un échec si
la fiche rend — note-la dans le journal. Si la fiche ne rend PAS (CAPTCHA,
challenge anti-bot, page vide, blocage réseau) : re-navigue UNE fois vers la
même URL, et si le blocage persiste, écris un résultat \`status: \"failed\"\`
fail-closed avec \`payload.statut = \"BLOQUE\"\` et \`payload.erreur.motif =
\"anti_bot_challenge\"\` — ne résous JAMAIS un CAPTCHA, ne contourne JAMAIS un
anti-bot, n'invente JAMAIS une donnée. Ferme le navigateur (browser_close) à
la fin du dépouillement.
DSers et tout le reste restent INTERDITS en headless (décision de prudence,
pas une limite technique) : tout ordre DSers (\`import_product_to_dsers\`,
\`configure_dsers_variants\`, \`push_dsers_product_to_shopify\`,
\`verify_supplier_mapping\`) ou tout autre ordre exigeant une session
interactive dont tu ne disposes pas produit un résultat \`status: \"failed\"\`
fail-closed avec \`payload.statut = \"BLOQUE\"\` et \`payload.erreur.motif =
\"requires_interactive_session\"\`, archivé en \`resultats/<nom>.ordre.json\`
comme tout échec. Même règle pour un outil MCP Shopify absent de ta session :
motif \`requires_interactive_session\`, jamais de contournement ni de donnée
inventée."

# Liste FERMÉE d'outils — le script ne doit jamais l'élargir.
# v2 (31/07 au soir) : navigateur Playwright MCP (serveur « playwright » de
# .mcp.json, chargé via --mcp-config) — navigation + lecture UNIQUEMENT, pour
# les 3 types AliExpress de classe A. Exclus à dessein : evaluate,
# run_code_unsafe, file_upload, fill_form, network_*, tabs — pas de scripting,
# pas de téléchargement/upload. Profil dédié ~/.cache/noirmont-playwright-profile,
# jamais le Chrome de Hakim.
# Les outils mcp__shopify__* ne sont actifs que si un serveur MCP « shopify »
# est configuré pour le CLI ; absents → fail-closed requires_interactive_session.
ALLOWED_TOOLS=(
  "Read" "Write" "Edit" "Glob" "Grep"
  "Bash(/usr/bin/python3 ordres/valider_ordre.py:*)"
  "Bash(bash ordres/classer_ordre.sh:*)"
  "Bash(cp ordres/:*)"
  "Bash(ls ordres/:*)"
  "Bash(mkdir -p ordres/:*)"
  "Bash(date:*)"
  "mcp__playwright__browser_navigate"
  "mcp__playwright__browser_navigate_back"
  "mcp__playwright__browser_snapshot"
  "mcp__playwright__browser_take_screenshot"
  "mcp__playwright__browser_click"
  "mcp__playwright__browser_type"
  "mcp__playwright__browser_press_key"
  "mcp__playwright__browser_wait_for"
  "mcp__playwright__browser_close"
  "mcp__shopify__get-shop-info"
  "mcp__shopify__get-product"
  "mcp__shopify__search_products"
  "mcp__shopify__get-collection"
  "mcp__shopify__search_collections"
  "mcp__shopify__get-inventory-levels"
  "mcp__shopify__graphql_schema"
  "mcp__shopify__graphql_query"
  "mcp__shopify__update-product"
)

if ! command -v claude >/dev/null 2>&1; then
  echo "échec du lancement : binaire \`claude\` introuvable dans le PATH." >&2
  exit 3
fi

echo "dépouillement headless lancé — journal : $JOURNAL"
# --mcp-config charge explicitement le serveur Playwright du dépôt (pas
# d'approbation interactive nécessaire : un chemin passé en --mcp-config est
# réputé approuvé par l'appelant). PAS de --strict-mcp-config : les serveurs
# MCP déjà configurés côté CLI (ex. connecteur Shopify) restent disponibles.
(
  cd "$REPO_ROOT" &&
  claude -p "$PROMPT" \
    --model claude-fable-5 \
    --mcp-config "$REPO_ROOT/.mcp.json" \
    --allowedTools "${ALLOWED_TOOLS[@]}"
) >"$JOURNAL" 2>&1
CODE_CLAUDE=$?

if [ "$CODE_CLAUDE" -ne 0 ]; then
  echo "échec du lancement/de la session headless (code $CODE_CLAUDE) — voir $JOURNAL" >&2
  if grep -q "authentication_error\|Failed to authenticate" "$JOURNAL" 2>/dev/null; then
    echo "cause : CLI \`claude\` non authentifié (jeton OAuth expiré/absent)." >&2
    echo "action HAKIM (jamais Codex) : lancer \`claude\` en interactif et se reconnecter (/login)." >&2
  fi
  exit 3
fi

echo "dépouillement terminé — lire le statut PAR ORDRE dans ordres/resultats/, ordres/rejetes/, ordres/attente-hakim/."
echo "journal : $JOURNAL"
exit 0
