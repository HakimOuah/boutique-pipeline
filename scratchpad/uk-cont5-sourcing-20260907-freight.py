import asyncio
import json
from datetime import datetime, timezone
from src.aliexpress_client import AliExpressClient, METHOD_FREIGHT_QUERY
from src.config import load_config

QUOTES = [
    {'label':'detector_with_accessories_stock865', 'product_id':'1005009126691172', 'sku_id':'12000050720365393'},
    {'label':'detector_with_accessories_stock6', 'product_id':'1005009126691172', 'sku_id':'12000048435221831'},
    {'label':'watch_winder_alternative', 'product_id':'1005012217866893', 'sku_id':'12000057777061832'},
]

async def main():
    async with AliExpressClient(load_config().aliexpress) as c:
        for q in QUOTES:
            req_obj = {'quantity':'1', 'shipToCountry':'GB', 'productId':q['product_id'],
                       'provinceCode':'', 'cityCode':'', 'selectedSkuId':q['sku_id'],
                       'language':'en_GB', 'currency':'GBP', 'locale':'en_GB'}
            req = {'queryDeliveryReq': json.dumps(req_obj, separators=(',',':'))}
            try:
                raw = await c._call_iop(METHOD_FREIGHT_QUERY, req)
                print(json.dumps({'kind':'freight_query', 'checked_at_utc':datetime.now(timezone.utc).isoformat(),
                                  'label':q['label'], 'product_id':q['product_id'], 'sku_id':q['sku_id'],
                                  'request':req, 'raw':raw}, ensure_ascii=False, default=str))
            except Exception as e:
                print(json.dumps({'kind':'freight_query_error', 'checked_at_utc':datetime.now(timezone.utc).isoformat(),
                                  'label':q['label'], 'product_id':q['product_id'], 'sku_id':q['sku_id'],
                                  'request':req, 'error':repr(e)}, ensure_ascii=False))

if __name__ == '__main__': asyncio.run(main())
