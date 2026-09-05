from copy import deepcopy

import yaml

from dropilot.config import load_config
from dropilot.models import ProductCandidate
from dropilot.scoring import ScoringEngine


def complete_candidate(**changes):
    data = {
        "product_name": "Fauteuil suspendu",
        "source": "europages",
        "category": "garden",
        "market": "FR",
        "price_sell": 400,
        "price_source": 90,
        "net_margin_pct": 30,
        "competitors_type": "dropshippers_weak_sites",
        "sells_in_search": True,
        "sells_in_shopping": True,
        "legal_eu": True,
        "supplier_verified": True,
        "google_verified": True,
        "search_volume": 12000,
        "differentiation_thesis": "Une offre spécialisée avec installation guidée.",
        "not_available_on_generic_channels": "partial",
    }
    data.update(changes)
    return ProductCandidate(**data)


def test_legacy_score_cannot_issue_commercial_go():
    result = ScoringEngine().evaluate(complete_candidate())
    assert result.decision == "shortlist"
    assert result.verdict == "TECHNICAL_INCONCLUSIVE"


def test_fr_volume_gate_is_enforced():
    result = ScoringEngine().evaluate(complete_candidate(search_volume=9999))
    assert result.verdict == "TECHNICAL_INCONCLUSIVE"
    assert "search_volume_below_threshold" in result.flags


def test_unconfigured_expansion_market_never_auto_goes():
    result = ScoringEngine().evaluate(complete_candidate(market="UK"))
    assert result.verdict == "TECHNICAL_INCONCLUSIVE"
    assert "market_search_threshold_unconfigured" in result.flags


def test_threshold_change_in_yaml_changes_decision(tmp_path):
    config = deepcopy(load_config())
    config["scoring"]["thresholds"]["shortlist"] = 99
    custom = tmp_path / "pipeline.yaml"
    custom.write_text(yaml.safe_dump(config), encoding="utf-8")
    result = ScoringEngine(custom).evaluate(complete_candidate())
    assert result.decision != "shortlist"


def test_missing_supplier_or_google_proof_stays_maybe():
    result = ScoringEngine().evaluate(
        complete_candidate(supplier_verified=None, google_verified=None)
    )
    assert result.verdict == "TECHNICAL_INCONCLUSIVE"
    assert "supplier_not_verified" in result.flags
    assert "google_not_verified" in result.flags

