import asyncio
import json
from datetime import datetime, timezone

from src.aliexpress_client import AliExpressClient, METHOD_TEXT_SEARCH, _extract_items
from src.config import load_config


QUERIES = ["ultrasonic cleaner UK plug", "ultrasonic cleaner USB"]


async def main():
    async with AliExpressClient(load_config().aliexpress) as client:
        for query in QUERIES:
            request = {
                "keyWord": query,
                "local": "en_GB",
                "countryCode": "GB",
                "currency": "GBP",
                "pageSize": "10",
                "pageIndex": "1",
            }
            try:
                raw = await client._call_iop(METHOD_TEXT_SEARCH, request)
                items = _extract_items(raw, METHOD_TEXT_SEARCH)
                record = {
                    "kind": "text_search",
                    "checked_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
                    "request": request,
                    "query": query,
                    "item_count": len(items),
                    "items": items,
                    "raw": raw,
                }
            except Exception as exc:
                record = {
                    "kind": "text_search",
                    "checked_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
                    "request": request,
                    "query": query,
                    "error": f"{type(exc).__name__}: {exc}",
                }
            print(json.dumps(record, ensure_ascii=False, default=str))


if __name__ == "__main__":
    asyncio.run(main())
