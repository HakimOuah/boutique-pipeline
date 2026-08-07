from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "codex-chasse-clusters" / "tools" / "aliexpress_vps_exact_probe.py"
FIXTURE_PATH = Path("/Users/Hakim/aliexpress-mcp-server/tests/fixtures")

spec = importlib.util.spec_from_file_location("aliexpress_vps_exact_probe", MODULE_PATH)
assert spec is not None and spec.loader is not None
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)


def _fixture(name: str) -> dict:
    payload = json.loads((FIXTURE_PATH / name).read_text())
    if name.startswith("real_product"):
        return payload["aliexpress_ds_product_get_response"]["result"]
    return payload["aliexpress_ds_freight_query_response"]["result"]


def test_select_exact_sku_uses_properties_not_position() -> None:
    detail = _fixture("real_product_get_response.json")

    sku, properties = probe.select_exact_sku(detail, ["Cat", "400MMx600MM"])

    assert sku["sku_id"] == "12000044126059462"
    assert sku["sku_available_stock"] == 83
    assert {p["value"] for p in properties} == {"Cat", "400MMx600MM"}


def test_select_exact_sku_rejects_ambiguity() -> None:
    detail = _fixture("real_product_get_response.json")

    with pytest.raises(probe.QualificationError, match="ambiguë"):
        probe.select_exact_sku(detail, ["Cat"])


def test_select_exact_sku_rejects_missing_stock() -> None:
    detail = _fixture("real_product_get_response.json")
    detail["ae_item_sku_info_dtos"]["ae_item_sku_info_d_t_o"][5].pop(
        "sku_available_stock"
    )

    with pytest.raises(probe.QualificationError, match="Stock numérique"):
        probe.select_exact_sku(detail, ["Cat", "400MMx600MM"])


def test_build_record_requires_real_delivery_option() -> None:
    detail = _fixture("real_product_get_response.json")
    sku, properties = probe.select_exact_sku(detail, ["Cat", "400MMx600MM"])

    with pytest.raises(probe.QualificationError, match="Aucune option"):
        probe.build_record(
            "1005008177221739",
            "FR",
            detail,
            sku,
            properties,
            {"success": True, "code": 200, "delivery_options": {}},
        )


def test_build_record_keeps_price_stock_and_fr_freight() -> None:
    detail = _fixture("real_product_get_response.json")
    freight = _fixture("real_freight_query_success_response.json")
    sku, properties = probe.select_exact_sku(detail, ["Cat", "400MMx600MM"])

    record = probe.build_record(
        "1005008177221739", "FR", detail, sku, properties, freight
    )

    assert record["destination"] == "FR"
    assert record["exact_sku"]["sku_id"] == "12000044126059462"
    assert record["exact_sku"]["stock"] == 83
    assert record["exact_sku"]["offer_sale_price"] == "5.19"
    assert record["freight"]["options"][0]["shipping_fee"] == "1,99€"
    assert record["freight"]["options"][0]["min_delivery_days"] == 6
