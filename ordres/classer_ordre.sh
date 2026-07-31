#!/bin/bash
# classer_ordre.sh — seul mécanisme de déplacement du cycle de vie des ordres.
# Usage : bash ordres/classer_ordre.sh <fichier-source> <etat-destination>
# États légaux : en-cours | resultats | rejetes | attente-hakim
# Refuse tout chemin hors de ordres/ et toute destination hors des états.
set -euo pipefail

ORDRES_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

SRC="${1:?usage: classer_ordre.sh <fichier-source> <etat-destination>}"
DEST_ETAT="${2:?usage: classer_ordre.sh <fichier-source> <etat-destination>}"

case "$DEST_ETAT" in
  en-cours|resultats|rejetes|attente-hakim) ;;
  *) echo "REFUS : destination « $DEST_ETAT » hors des états légaux (en-cours|resultats|rejetes|attente-hakim)" >&2; exit 1 ;;
esac

# Résolution du chemin source (accepte relatif au dépôt, relatif à ordres/, ou absolu)
if [ -f "$SRC" ]; then SRC_ABS="$(cd "$(dirname "$SRC")" && pwd)/$(basename "$SRC")"
elif [ -f "$ORDRES_DIR/$SRC" ]; then SRC_ABS="$ORDRES_DIR/$SRC"
else echo "REFUS : fichier source introuvable : $SRC" >&2; exit 1; fi

case "$SRC_ABS" in
  "$ORDRES_DIR"/*) ;;
  *) echo "REFUS : source hors de ordres/ : $SRC_ABS" >&2; exit 1 ;;
esac
case "$SRC_ABS" in
  */exemples/*) echo "REFUS : les exemples ne se classent jamais" >&2; exit 1 ;;
esac

mv "$SRC_ABS" "$ORDRES_DIR/$DEST_ETAT/"
echo "OK : $(basename "$SRC_ABS") → $DEST_ETAT/"
