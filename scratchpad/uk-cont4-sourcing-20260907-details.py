import asyncio
import json
from datetime import datetime, timezone
from src.aliexpress_client import AliExpressClient, METHOD_PRODUCT_GET
from src.config import load_config

IDS=[
 '1005006404879088',
 '1005006786141635','1005012217866893',
 '1005008635238967','32839469711',
]

async def main():
    async with AliExpressClient(load_config().aliexpress) as c:
        for pid in IDS:
            req={'product_id':pid,'ship_to_country':'GB','target_currency':'GBP','target_language':'en','remove_personal_benefit':'true'}
            try:
                raw=await c._call_iop(METHOD_PRODUCT_GET,req)
                print(json.dumps({'kind':'product_get','checked_at_utc':datetime.now(timezone.utc).isoformat(),'product_id':pid,'request':req,'raw':raw},ensure_ascii=False,default=str))
            except Exception as e:
                print(json.dumps({'kind':'product_get_error','checked_at_utc':datetime.now(timezone.utc).isoformat(),'product_id':pid,'request':req,'error':repr(e)},ensure_ascii=False))

if __name__=='__main__': asyncio.run(main())
