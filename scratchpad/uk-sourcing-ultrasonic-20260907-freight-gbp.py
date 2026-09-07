import asyncio
import json
from datetime import datetime, timezone

from src.aliexpress_client import AliExpressClient, METHOD_FREIGHT_QUERY
from src.config import load_config


SKUS = [
    {"product_id": "1005007383813023", "sku_id": "12000040528232915", "label": "WHITE / EU plug"},
    {"product_id": "1005009784385341", "sku_id": "12000050245030735", "label": "220V EU plug"},
    {"product_id": "1005010394741290", "sku_id": "12000052268170470", "label": "220V EU plug"},
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
