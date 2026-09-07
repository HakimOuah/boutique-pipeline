import asyncio
import json
from datetime import datetime, timezone
from src.aliexpress_client import AliExpressClient, METHOD_PRODUCT_GET
from src.config import load_config

PIDS = [
    '1005009404700712',  # open embroidered abaya
    '1005007463741144',  # 24-steel underbust alternative
    '1005008970862209',  # 3-slot USB cable winder
    '1005006823341040',  # USB cable winder box alternative
    '1005006003820202',  # TX850 adult 11-inch coil
    '1005010287452519',  # TX850 alternative
    '1005010332416399',  # 39.37cm magnetic chess complete
    '1005009215859784',  # 3-in-1 wooden chess 32pcs
]

async def main():
    async with AliExpressClient(load_config().aliexpress) as c:
        for pid in PIDS:
            req={'product_id':pid,'ship_to_country':'GB','target_currency':'GBP','target_language':'en','remove_personal_benefit':'true'}
            try:
                raw=await c._call_iop(METHOD_PRODUCT_GET,req)
                print(json.dumps({'kind':'product_get','checked_at_utc':datetime.now(timezone.utc).isoformat(),
                                  'product_id':pid,'request':req,'raw':raw},ensure_ascii=False,default=str))
            except Exception as e:
                print(json.dumps({'kind':'product_get_error','checked_at_utc':datetime.now(timezone.utc).isoformat(),
                                  'product_id':pid,'request':req,'error':repr(e)},ensure_ascii=False))

if __name__=='__main__': asyncio.run(main())
