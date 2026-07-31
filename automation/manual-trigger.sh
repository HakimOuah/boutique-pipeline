#!/usr/bin/env sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
PYTHON=${PYTHON:-"$ROOT/.venv/bin/python"}

exec "$PYTHON" -m dropilot.cli --db "$ROOT/data/dropilot.sqlite3" process-inbox \
  --inbox "$ROOT/data/inbox" \
  --config "$ROOT/config/pipeline.yaml" \
  --reports "$ROOT/reports"

