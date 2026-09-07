import asyncio
import json
from datetime import datetime, timezone

from src.aliexpress_client import AliExpressClient, METHOD_PRODUCT_GET
from src.config import load_config


PRODUCT_IDS = [
    "1005013039050983",
    "1005010241648074",
    "1005010122198699",
]


async def main():
    async with AliExpressClient(load_config().aliexpress) as client:
        for product_id in PRODUCT_IDS:
            request = {
                "product_id": product_id,
                "ship_to_country": "GB",
                "target_currency": "GBP",
                "target_language": "en",
                "remove_personal_benefit": "true",
            }
            try:
                raw = await client._call_iop(METHOD_PRODUCT_GET, request)
                record = {
                    "kind": "product_get",
                    "checked_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
                    "request": request,
                    "product_id": product_id,
                    "raw": raw,
                }
            except Exception as exc:
                record = {
                    "kind": "product_get",
                    "checked_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
                    "request": request,
                    "product_id": product_id,
                    "error": f"{type(exc).__name__}: {exc}",
                }
            print(json.dumps(record, ensure_ascii=False, default=str))


if __name__ == "__main__":
    asyncio.run(main())
