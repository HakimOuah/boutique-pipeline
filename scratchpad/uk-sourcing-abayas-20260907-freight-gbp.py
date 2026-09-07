import asyncio
import json
from datetime import datetime, timezone

from src.aliexpress_client import AliExpressClient, METHOD_FREIGHT_QUERY
from src.config import load_config


SKUS = [
    {
        "product_id": "1005012385271194",
        "sku_id": "12000058264898367",
        "label": "Black / M",
    },
    {
        "product_id": "1005012289841477",
        "sku_id": "12000057978139381",
        "label": "Beige 3pcs set / M",
    },
    {
        "product_id": "1005012471812405",
        "sku_id": "12000058450979863",
        "label": "Black / M",
    },
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
