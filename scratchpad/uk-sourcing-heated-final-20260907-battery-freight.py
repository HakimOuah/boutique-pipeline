import asyncio
import json
from datetime import datetime, timezone
from src.aliexpress_client import AliExpressClient, METHOD_FREIGHT_QUERY
from src.config import load_config

ROW={'product_id':'1005010031480359','sku_id':'12000057722704051','sku_label':'L-XL; 10 000 mah battery'}

async def main():
    async with AliExpressClient(load_config().aliexpress) as c:
        q={'quantity':'1','shipToCountry':'GB','productId':ROW['product_id'],'provinceCode':'','cityCode':'','selectedSkuId':ROW['sku_id'],'language':'en_GB','currency':'GBP','locale':'en_GB'}
        req={'queryDeliveryReq':json.dumps(q,separators=(',',':'))}
        try:
            raw=await c._call_iop(METHOD_FREIGHT_QUERY,req)
            print(json.dumps({'kind':'freight_query','checked_at_utc':datetime.now(timezone.utc).isoformat(),**ROW,'request':req,'raw':raw},ensure_ascii=False,default=str))
        except Exception as e:
            print(json.dumps({'kind':'freight_query_error','checked_at_utc':datetime.now(timezone.utc).isoformat(),**ROW,'request':req,'error':repr(e)},ensure_ascii=False))

if __name__=='__main__': asyncio.run(main())
