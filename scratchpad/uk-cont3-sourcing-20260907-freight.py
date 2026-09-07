import asyncio
import json
from datetime import datetime, timezone
from src.aliexpress_client import AliExpressClient, METHOD_FREIGHT_QUERY
from src.config import load_config

ROWS=[
 {'family':'orthopedic_dog_bed_large','product_id':'1005009119696851','sku_id':'12000047983252996','sku_label':'107X76X17CM'},
 {'family':'digital_photo_frame_wifi_10in','product_id':'1005005545336780','sku_id':'12000057139115817','sku_label':'BLACK built in 64GB / plug code 201447606'},
 {'family':'hollywood_vanity_mirror_lights','product_id':'1005009302227146','sku_id':'12000048720354462','sku_label':'12 Bulbs'},
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
