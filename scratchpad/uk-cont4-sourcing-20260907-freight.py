import asyncio
import json
from datetime import datetime, timezone
from src.aliexpress_client import AliExpressClient, METHOD_FREIGHT_QUERY
from src.config import load_config

ROWS=[
 {'family':'mirror_new_usb','product_id':'1005006404879088','sku_id':'12000037064826646','sku_label':'30cm Black / plug 201336100'},
 {'family':'watch_winder','product_id':'1005006786141635','sku_id':'12000038298689118','sku_label':'Black / 2 slots'},
 {'family':'wood_watch_box','product_id':'32839469711','sku_id':'12000032606672985','sku_label':'Style 1 / 10 slots'},
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
