#!/usr/bin/env sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
PYTHON=${PYTHON:-"$ROOT/.venv/bin/python"}

cd "$ROOT"
exec "$PYTHON" -m dropilot.cli serve --host 127.0.0.1 --port "${DROPILOT_PORT:-8787}"

