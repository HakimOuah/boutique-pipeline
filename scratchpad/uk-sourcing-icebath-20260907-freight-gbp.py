import asyncio
import json
from datetime import datetime, timezone

from src.aliexpress_client import AliExpressClient, METHOD_FREIGHT_QUERY
from src.config import load_config


SKUS = [
    {"product_id": "1005010151127666", "sku_id": "12000051361428599", "label": "Gold-M"},
    {"product_id": "1005012520238299", "sku_id": "12000058583359698", "label": "75x80"},
    {"product_id": "1005010161523574", "sku_id": "12000051363809036", "label": "black"},
    {"product_id": "1005009944233727", "sku_id": "12000050650202610", "label": "L"},
]


async def main():
    async with AliExpressClient(load_config().aliexpress) as client:
        for item in SKUS:
            query = {
                "quantity": "1",
                "shipToCountry": "GB",
                "productId": item["product_id"],
                "provinceCode": "",
                "cityCode": "",
                "selectedSkuId": item["sku_id"],
                "language": "en_GB",
                "currency": "GBP",
                "locale": "en_GB",
            }
            request = {"queryDeliveryReq": json.dumps(query, separators=(",", ":"))}
            try:
                raw = await client._call_iop(METHOD_FREIGHT_QUERY, request)
                record = {
                    "kind": "freight_gbp_direct",
                    "checked_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
                    "request": request,
                    "query_delivery_req": query,
                    "product_id": item["product_id"],
                    "sku_id": item["sku_id"],
                    "label": item["label"],
                    "raw": raw,
                }
            except Exception as exc:
                record = {
                    "kind": "freight_gbp_direct",
                    "checked_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
                    "request": request,
                    "query_delivery_req": query,
                    "product_id": item["product_id"],
                    "sku_id": item["sku_id"],
                    "label": item["label"],
                    "error": f"{type(exc).__name__}: {exc}",
                }
            print(json.dumps(record, ensure_ascii=False, default=str))


if __name__ == "__main__":
    asyncio.run(main())
