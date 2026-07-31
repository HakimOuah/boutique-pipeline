import json

import pytest

from dropilot.adapters import load_candidates
from dropilot.models import ProductCandidate
from dropilot.normalization import candidate_fingerprint, canonical_url


def test_json_adapter_accepts_legacy_aliases(tmp_path):
    path = tmp_path / "products.json"
    path.write_text(
        json.dumps({"name": "Osmoseur", "price_source_ali": 100, "price_sell": 400}),
        encoding="utf-8",
    )
    product = load_candidates(path, source="manual")[0]
    assert product.product_name == "Osmoseur"
    assert product.price_source == 100


def test_missing_product_name_is_reported_cleanly(tmp_path):
    path = tmp_path / "products.json"
    path.write_text(json.dumps({"price_sell": 400}), encoding="utf-8")
    with pytest.raises(ValueError, match="product_name"):
        load_candidates(path)


def test_tracking_parameters_do_not_break_url_dedup():
    left = canonical_url("https://example.com/p/1?utm_source=x&variant=2")
    right = canonical_url("https://example.com/p/1?variant=2&utm_source=y")
    assert left == right


def test_name_fingerprint_ignores_accents_and_stop_words():
    left = ProductCandidate(product_name="Un filtre à eau pour robinet")
    right = ProductCandidate(product_name="Filtre eau robinet")
    ignored = ["un", "pour", "a", "à"]
    assert candidate_fingerprint(left, ignored) == candidate_fingerprint(right, ignored)


def test_angle_keeps_distinct_theses_separate():
    left = ProductCandidate(product_name="Filtre eau", angle="petits appartements")
    right = ProductCandidate(product_name="Filtre eau", angle="familles")
    assert candidate_fingerprint(left, [], True) != candidate_fingerprint(right, [], True)

