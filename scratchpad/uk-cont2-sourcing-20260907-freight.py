import asyncio
import json
from datetime import datetime, timezone
from src.aliexpress_client import AliExpressClient, METHOD_FREIGHT_QUERY
from src.config import load_config

ROWS=[
 {'family':'pet_stroller','product_id':'1005008669344944','sku_id':'12000050507875583','sku_label':'1PC Gray'},
 {'family':'bird_feeder_camera','product_id':'1005008831874584','sku_id':'12000046871554273','sku_label':'Feeder Cam'},
 {'family':'wildlife_trail_camera','product_id':'1005007903321651','sku_id':'12000042783566915','sku_label':'S810WIFI'},
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
