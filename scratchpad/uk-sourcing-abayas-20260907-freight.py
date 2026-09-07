import asyncio
import json
from datetime import datetime, timezone

from src.aliexpress_client import AliExpressClient
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
            request = {
                "product_id": item["product_id"],
                "sku_id": item["sku_id"],
                "country_code": "GB",
                "quantity": 1,
            }
            try:
                raw = await client.get_shipping_cost(
                    item["product_id"], item["sku_id"], "GB", 1
                )
                record = {
                    "kind": "freight",
                    "checked_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
                    "request": request,
                    "label": item["label"],
                    "raw": raw,
                }
            except Exception as exc:
                record = {
                    "kind": "freight",
                    "checked_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
                    "request": request,
                    "label": item["label"],
                    "error": f"{type(exc).__name__}: {exc}",
                }
            print(json.dumps(record, ensure_ascii=False, default=str))


if __name__ == "__main__":
    asyncio.run(main())
