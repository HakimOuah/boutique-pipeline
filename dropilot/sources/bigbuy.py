from __future__ import annotations

import json
import os
from dataclasses import asdict
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from dropilot.models import ProductCandidate


class BigBuyClient:
    def __init__(
        self,
        api_key: str | None = None,
        base_url: str = "https://api.sandbox.bigbuy.eu",
        opener: Callable[..., Any] = urlopen,
        timeout: int = 60,
    ):
        self.api_key = api_key or os.getenv("BIGBUY_API_KEY", "")
        if not self.api_key:
            raise ValueError("BIGBUY_API_KEY est requis")
        if base_url not in {"https://api.bigbuy.eu", "https://api.sandbox.bigbuy.eu"}:
            raise ValueError("Base BigBuy non autorisée")
        self.base_url = base_url.rstrip("/")
        self.opener = opener
        self.timeout = timeout

    def get(self, endpoint: str, **params: Any) -> list[dict[str, Any]]:
        query = urlencode({key: value for key, value in params.items() if value is not None})
        url = f"{self.base_url}{endpoint}"
        if query:
            url += f"?{query}"
        request = Request(
            url,
            headers={"Authorization": f"Bearer {self.api_key}", "Accept": "application/json"},
        )
        with self.opener(request, timeout=self.timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
        if not isinstance(payload, list):
            raise ValueError(f"Réponse BigBuy inattendue pour {endpoint}")
        return [item for item in payload if isinstance(item, dict)]

    def products(self, taxonomy_id: int) -> list[dict[str, Any]]:
        return self.get("/rest/catalog/products.json", parentTaxonomy=taxonomy_id)

    def product_information(self, taxonomy_id: int, iso_code: str = "fr") -> list[dict[str, Any]]:
        return self.get(
            "/rest/catalog/productsinformation.json",
            parentTaxonomy=taxonomy_id,
            isoCode=iso_code,
        )


def fetch_bigbuy_candidates(
    client: BigBuyClient,
    taxonomy_id: int,
    iso_code: str = "fr",
    market: str = "FR",
) -> list[ProductCandidate]:
    products = client.products(taxonomy_id)
    information = client.product_information(taxonomy_id, iso_code)
    info_by_id = {str(item.get("id")): item for item in information}
    candidates: list[ProductCandidate] = []
    for item in products:
        if item.get("active") in {0, "0", False}:
            continue
        info = info_by_id.get(str(item.get("id")), {})
        name = str(info.get("name") or item.get("sku") or "").strip()
        if not name:
            continue
        product_url = str(info.get("url") or "")
        candidates.append(
            ProductCandidate(
                product_name=name,
                source="bigbuy",
                category=f"bigbuy_taxonomy_{taxonomy_id}",
                market=market.upper(),
                currency="GBP" if market.upper() == "UK" else "EUR",
                source_url=product_url,
                supplier_name="BigBuy",
                price_source=float(item["wholesalePrice"]) if item.get("wholesalePrice") is not None else None,
                price_sell=float(item["inShopsPrice"]) if item.get("inShopsPrice") is not None else None,
                supplier_available=True,
                metadata={
                    "bigbuy_id": item.get("id"),
                    "sku": item.get("sku"),
                    "ean13": item.get("ean13"),
                    "retail_price": item.get("retailPrice"),
                    "taxonomy_id": taxonomy_id,
                    "iso_code": iso_code,
                    "date_updated": item.get("dateUpd"),
                },
            )
        )
    return candidates


def write_bigbuy_export(candidates: list[ProductCandidate], path: str | Path) -> Path:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps([candidate.to_dict() for candidate in candidates], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return output

