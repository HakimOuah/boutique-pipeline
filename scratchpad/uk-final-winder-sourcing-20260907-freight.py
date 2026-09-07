import asyncio
import json
from datetime import datetime, timezone
from src.aliexpress_client import AliExpressClient, METHOD_FREIGHT_QUERY
from src.config import load_config

PRODUCT_ID = '1005007344751830'
SKU_ID = '12000040354079030'

async def main():
    async with AliExpressClient(load_config().aliexpress) as c:
        req_obj = {'quantity':'1', 'shipToCountry':'GB', 'productId':PRODUCT_ID,
                   'provinceCode':'', 'cityCode':'', 'selectedSkuId':SKU_ID,
                   'language':'en_GB', 'currency':'GBP', 'locale':'en_GB'}
        req = {'queryDeliveryReq': json.dumps(req_obj, separators=(',',':'))}
        try:
            raw = await c._call_iop(METHOD_FREIGHT_QUERY, req)
            print(json.dumps({'kind':'freight_query', 'checked_at_utc':datetime.now(timezone.utc).isoformat(),
                              'label':'two_slot_usb_cable_stock2', 'product_id':PRODUCT_ID, 'sku_id':SKU_ID,
                              'request':req, 'raw':raw}, ensure_ascii=False, default=str))
        except Exception as e:
            print(json.dumps({'kind':'freight_query_error', 'checked_at_utc':datetime.now(timezone.utc).isoformat(),
                              'label':'two_slot_usb_cable_stock2', 'product_id':PRODUCT_ID, 'sku_id':SKU_ID,
                              'request':req, 'error':repr(e)}, ensure_ascii=False))

if __name__ == '__main__': asyncio.run(main())
