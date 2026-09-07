import asyncio
import json
from datetime import datetime, timezone
from src.aliexpress_client import AliExpressClient, METHOD_FREIGHT_QUERY
from src.config import load_config

ROWS = [
    {'product_id':'1005008086495961','sku_id':'12000043641691985','sku_label':'chess set / 39cm'},
    {'product_id':'1005012070192886','sku_id':'12000057442920193','sku_label':'1 set / 45cm'},
    {'product_id':'1005009424303397','sku_id':'12000049055056832','sku_label':'5inch A4 crystal bowl + mallet/oring declared'},
]

async def main():
    async with AliExpressClient(load_config().aliexpress) as c:
        for row in ROWS:
            q={'quantity':'1','shipToCountry':'GB','productId':row['product_id'],'provinceCode':'','cityCode':'','selectedSkuId':row['sku_id'],'language':'en_GB','currency':'GBP','locale':'en_GB'}
            req={'queryDeliveryReq':json.dumps(q,separators=(',',':'))}
            try:
                raw=await c._call_iop(METHOD_FREIGHT_QUERY,req)
                print(json.dumps({'kind':'freight_query','checked_at_utc':datetime.now(timezone.utc).isoformat(),**row,'request':req,'raw':raw},ensure_ascii=False,default=str))
            except Exception as e:
                print(json.dumps({'kind':'freight_query_error','checked_at_utc':datetime.now(timezone.utc).isoformat(),**row,'request':req,'error':repr(e)},ensure_ascii=False))

if __name__=='__main__': asyncio.run(main())
