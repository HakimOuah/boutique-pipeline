from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG_PATH = ROOT / "config" / "pipeline.yaml"


def load_config(path: str | Path | None = None) -> dict[str, Any]:
    config_path = Path(path) if path else DEFAULT_CONFIG_PATH
    data = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Configuration invalide : {config_path}")
    return deepcopy(data)


def market_volume_threshold(config: dict[str, Any], market: str) -> int | None:
    thresholds = config["final_gates"]["minimum_transactional_search_volume"]
    value = thresholds.get(market.upper())
    return int(value) if value is not None else None

