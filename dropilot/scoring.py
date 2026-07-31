from __future__ import annotations

from pathlib import Path
from typing import Any

from .config import load_config, market_volume_threshold
from .models import ProductCandidate, ScoringResult


def _in_band(value: float, band: dict[str, Any]) -> bool:
    if "minimum" in band and value < float(band["minimum"]):
        return False
    if "minimum_exclusive" in band and value <= float(band["minimum_exclusive"]):
        return False
    if "maximum" in band and value > float(band["maximum"]):
        return False
    if "maximum_exclusive" in band and value >= float(band["maximum_exclusive"]):
        return False
    return True


def _band_points(value: float | None, bands: list[dict[str, Any]]) -> int:
    if value is None:
        return 0
    for band in bands:
        if _in_band(float(value), band):
            return int(band["points"])
    return 0


class ScoringEngine:
    def __init__(self, config_path: str | Path | None = None):
        self.config = load_config(config_path)

    def _hard_filter(self, product: ProductCandidate) -> str | None:
        rules = self.config["hard_filters"]
        price = product.price_sell
        if price is not None:
            floor = float(rules["ticket_floor"])
            ratio = product.margin_ratio
            if ratio is not None and ratio >= float(rules["exceptional_margin_ratio"]):
                floor = float(rules["exceptional_margin_floor"])
            if price < floor:
                return "ticket_too_low"
            if price > float(rules["ticket_reject_above"]):
                return "ticket_too_high"
        if product.category in set(rules["banned_categories"]):
            return "banned_google"
        if product.legal_eu is False:
            return "illegal_eu"
        if product.category in set(rules["excluded_categories"]):
            return "excluded_category"
        if rules.get("institutional_dominance_reject") and product.big_retailer_same_product:
            return "institutional_dominance"
        if product.category in {"baby", "toys"}:
            override = rules["baby_toys_override"]
            if not (
                price is not None
                and price >= float(override["minimum_price"])
                and product.margin_ratio is not None
                and product.margin_ratio >= float(override["minimum_margin_ratio"])
            ):
                return "baby_toys_low_value"
        return None

    def _score(self, product: ProductCandidate) -> tuple[int, dict[str, int], dict[str, int], list[str]]:
        scoring = self.config["scoring"]
        flags: list[str] = []
        breakdown: dict[str, int] = {}

        breakdown["ticket"] = _band_points(product.price_sell, scoring["ticket"]["bands"])
        breakdown["margin_ratio"] = _band_points(product.margin_ratio, scoring["margin_ratio"]["bands"])
        if product.margin_ratio is None:
            flags.append("margin_ratio_missing")
        margin_gate = scoring["margin_ratio"]["net_margin_gate"]
        if product.net_margin_pct is not None and product.net_margin_pct < float(margin_gate["minimum_percent"]):
            breakdown["margin_ratio"] = min(breakdown["margin_ratio"], int(margin_gate["points_cap_below_minimum"]))

        breakdown["competition"] = int(scoring["competition"].get(product.competitors_type, 0))
        channels = scoring["channel"]
        if product.sells_in_search and product.sells_in_shopping:
            breakdown["channel"] = int(channels["search_and_shopping"])
        elif product.sells_in_search:
            breakdown["channel"] = int(channels["search_only"])
        elif product.sells_in_shopping:
            breakdown["channel"] = int(channels["shopping_only"])
        else:
            breakdown["channel"] = int(channels["neither"])

        sources = scoring["source_signal"]
        source_points = int(sources.get(product.source, 0))
        if product.distinct_sources >= 2:
            source_points += int(sources["multi_source_bonus"])
        breakdown["source_signal"] = min(source_points, int(sources["maximum_with_bonus"]))
        breakdown["niche_defensibility"] = int(
            scoring["niche_defensibility"].get(product.not_available_on_generic_channels, 0)
        )

        penalties: dict[str, int] = {}
        penalty_cfg = scoring["penalties"]
        if product.is_seasonal or product.trend_spike_pct > float(penalty_cfg["trend_spike_above_percent"]):
            penalties["seasonal"] = int(penalty_cfg["seasonal"])
        if product.entry_barrier == "low" and product.many_big_brands:
            penalties["low_entry_barrier"] = int(penalty_cfg["low_entry_barrier_with_big_brands"])
        if product.supplier_available is False and product.eu_supplier_required:
            penalties["hard_to_source"] = int(penalty_cfg["hard_to_source"])

        score = max(0, min(100, sum(breakdown.values()) - sum(penalties.values())))
        return score, breakdown, penalties, flags

    def _final_verdict(self, product: ProductCandidate, decision: str, flags: list[str]) -> str:
        if decision == "reject":
            return "NO_GO"
        gates = self.config["final_gates"]
        blockers: list[str] = []
        threshold = market_volume_threshold(self.config, product.market)
        if threshold is None:
            blockers.append("market_search_threshold_unconfigured")
        elif product.search_volume is None:
            blockers.append("search_volume_missing")
        elif product.search_volume < threshold:
            blockers.append("search_volume_below_threshold")
        if gates["require_google_verification"] and product.google_verified is not True:
            blockers.append("google_not_verified")
        if gates["require_legal_verification"] and product.legal_eu is not True:
            blockers.append("legal_not_verified")
        if gates["require_supplier_verification"] and product.supplier_verified is not True:
            blockers.append("supplier_not_verified")
        minimum_margin = float(gates["minimum_net_margin_percent"])
        if product.net_margin_pct is None:
            blockers.append("net_margin_missing")
        elif product.net_margin_pct < minimum_margin:
            blockers.append("net_margin_below_threshold")
        if gates["require_differentiation_thesis"] and not product.differentiation_thesis.strip():
            blockers.append("differentiation_missing")
        flags.extend(item for item in blockers if item not in flags)
        if decision == "shortlist" and not blockers:
            return "GO"
        return "MAYBE"

    def evaluate(self, product: ProductCandidate) -> ScoringResult:
        rejected_by = self._hard_filter(product)
        if rejected_by:
            return ScoringResult(
                product_name=product.product_name,
                score=None,
                decision="reject",
                verdict="NO_GO",
                rejected_by=rejected_by,
            )
        score, breakdown, penalties, flags = self._score(product)
        thresholds = self.config["scoring"]["thresholds"]
        if score >= int(thresholds["shortlist"]):
            decision = "shortlist"
        elif score >= int(thresholds["review"]):
            decision = "review"
        else:
            decision = "reject"
        if decision == "shortlist" and (product.legal_eu is None or product.margin_ratio is None):
            decision = "review"
        verdict = self._final_verdict(product, decision, flags)
        target_clicks = self.config["testing"].get("target_clicks_per_test")
        required_budget = None
        if target_clicks is not None and product.cpc is not None:
            required_budget = round(float(target_clicks) * product.cpc, 2)
        return ScoringResult(
            product_name=product.product_name,
            score=score,
            decision=decision,
            verdict=verdict,
            breakdown=breakdown,
            penalties=penalties,
            flags=flags,
            required_test_budget=required_budget,
        )

    def evaluate_batch(self, products: list[ProductCandidate]) -> list[ScoringResult]:
        return [self.evaluate(product) for product in products]

