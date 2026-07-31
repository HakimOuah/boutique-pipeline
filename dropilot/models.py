from __future__ import annotations

from dataclasses import asdict, dataclass, field, fields
from typing import Any


def _optional_float(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(str(value).replace(",", "."))
    except (TypeError, ValueError):
        return None


def _optional_int(value: Any) -> int | None:
    number = _optional_float(value)
    return int(number) if number is not None else None


def _optional_bool(value: Any) -> bool | None:
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        return value
    normalized = str(value).strip().lower()
    if normalized in {"true", "yes", "oui", "1"}:
        return True
    if normalized in {"false", "no", "non", "0"}:
        return False
    return None


@dataclass
class ProductCandidate:
    product_name: str
    source: str = "manual"
    category: str = "unknown"
    market: str = "FR"
    currency: str = "EUR"
    angle: str = ""
    source_url: str = ""
    supplier_url: str = ""
    supplier_name: str = ""
    supplier_verified: bool | None = None
    supplier_rating: float | None = None
    product_rating: float | None = None
    supplier_orders: int | None = None
    ships_from_eu: bool | None = None
    delivery_days: int | None = None
    price_sell: float | None = None
    price_source: float | None = None
    shipping_cost: float | None = None
    net_margin_pct: float | None = None
    cac_break_even: float | None = None
    cpc: float | None = None
    search_volume: int | None = None
    google_verified: bool | None = None
    google_country: str = ""
    keyword_intent: str = ""
    keyword_difficulty: float | None = None
    keyword_variations: str = ""
    google_trends_period: str = ""
    google_trends_index: float | None = None
    google_trends_direction: str = ""
    sells_in_search: bool | None = None
    sells_in_shopping: bool | None = None
    shopping_score: float | None = None
    search_score: float | None = None
    business_score: float | None = None
    competitors_type: str | None = None
    competitors_dtc: str = ""
    marketplace_references: str = ""
    big_retailer_same_product: bool = False
    legal_eu: bool | None = None
    differentiation_thesis: str = ""
    problem_or_desire: str = ""
    marketing_angle: str = ""
    customer_value_add: str = ""
    why_not_a_copy: str = ""
    risks: str = ""
    go_condition: str = ""
    shopify_url: str = ""
    not_available_on_generic_channels: str | None = None
    is_seasonal: bool = False
    trend_spike_pct: float = 0.0
    entry_barrier: str | None = None
    many_big_brands: bool = False
    supplier_available: bool | None = None
    eu_supplier_required: bool = False
    distinct_sources: int = 1
    status: str = "idea"
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def delivered_cost(self) -> float | None:
        if self.price_source is None:
            return None
        return round(self.price_source + (self.shipping_cost or 0.0), 2)

    @property
    def margin_ratio(self) -> float | None:
        if not self.price_sell or not self.delivered_cost or self.delivered_cost <= 0:
            return None
        return round(self.price_sell / self.delivered_cost, 2)

    @classmethod
    def from_mapping(cls, row: dict[str, Any]) -> "ProductCandidate":
        aliases = {
            "name": "product_name",
            "product": "product_name",
            "price_source_ali": "price_source",
            "supplier_price": "price_source",
            "price_sale": "price_sell",
            "url": "source_url",
            "aliexpress_url": "supplier_url",
            "legal": "legal_eu",
        }
        normalized = {aliases.get(str(key).strip().lower(), str(key).strip().lower()): value for key, value in row.items()}
        valid = {item.name for item in fields(cls)}
        values = {key: value for key, value in normalized.items() if key in valid}
        name = str(values.get("product_name") or "").strip()
        if not name:
            raise ValueError("product_name est obligatoire")
        values["product_name"] = name
        for key in {
            "price_sell", "price_source", "shipping_cost", "net_margin_pct", "cac_break_even",
            "cpc", "supplier_rating", "product_rating", "trend_spike_pct", "keyword_difficulty",
            "google_trends_index", "shopping_score", "search_score", "business_score"
        }:
            if key in values:
                values[key] = _optional_float(values[key])
        for key in {"supplier_orders", "delivery_days", "search_volume", "distinct_sources"}:
            if key in values:
                values[key] = _optional_int(values[key])
        for key in {
            "supplier_verified", "ships_from_eu", "google_verified", "sells_in_search",
            "sells_in_shopping", "big_retailer_same_product", "legal_eu", "is_seasonal",
            "many_big_brands", "supplier_available", "eu_supplier_required"
        }:
            if key in values:
                parsed = _optional_bool(values[key])
                values[key] = parsed if parsed is not None else values[key]
        values["market"] = str(values.get("market") or "FR").upper()
        return cls(**values)

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        result["delivered_cost"] = self.delivered_cost
        result["margin_ratio"] = self.margin_ratio
        return result


@dataclass
class ScoringResult:
    product_name: str
    score: int | None
    decision: str
    verdict: str
    rejected_by: str | None = None
    breakdown: dict[str, int] = field(default_factory=dict)
    penalties: dict[str, int] = field(default_factory=dict)
    flags: list[str] = field(default_factory=list)
    required_test_budget: float | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
