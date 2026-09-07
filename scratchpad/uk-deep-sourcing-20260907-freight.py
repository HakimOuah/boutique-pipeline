import asyncio
import json
from datetime import datetime, timezone
from src.aliexpress_client import AliExpressClient, METHOD_FREIGHT_QUERY
from src.config import load_config

QUOTES = [
    {'family':'abaya','product_id':'1005009404700712','sku_id':'12000048996914221'},
    {'family':'corset_underbust','product_id':'1005007463741144','sku_id':'12000040858765475'},
    {'family':'watch_winder_3slot','product_id':'1005008970862209','sku_id':'12000047413849598'},
    {'family':'tx850_adult','product_id':'1005006003820202','sku_id':'12000035270477888'},
    {'family':'chess_39cm','product_id':'1005009215859784','sku_id':'12000048343840400'},
]

async def main():
    async with AliExpressClient(load_config().aliexpress) as c:
        for q in QUOTES:
            req_obj={'quantity':'1','shipToCountry':'GB','productId':q['product_id'],'provinceCode':'','cityCode':'',
                     'selectedSkuId':q['sku_id'],'language':'en_GB','currency':'GBP','locale':'en_GB'}
            req={'queryDeliveryReq':json.dumps(req_obj,separators=(',',':'))}
            try:
                raw=await c._call_iop(METHOD_FREIGHT_QUERY,req)
                print(json.dumps({'kind':'freight_query','checked_at_utc':datetime.now(timezone.utc).isoformat(),
                                  **q,'request':req,'raw':raw},ensure_ascii=False,default=str))
            except Exception as e:
                print(json.dumps({'kind':'freight_query_error','checked_at_utc':datetime.now(timezone.utc).isoformat(),
                                  **q,'request':req,'error':repr(e)},ensure_ascii=False))

if __name__=='__main__': asyncio.run(main())
