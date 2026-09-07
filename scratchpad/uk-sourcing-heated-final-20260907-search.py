import asyncio
import json
from datetime import datetime, timezone
from src.aliexpress_client import AliExpressClient, METHOD_TEXT_SEARCH, _extract_items
from src.config import load_config

QUERY = 'heated vest battery'

async def main():
    async with AliExpressClient(load_config().aliexpress) as c:
        req={'keyWord':QUERY,'local':'en_GB','countryCode':'GB','currency':'GBP','pageSize':'20','pageIndex':'1'}
        try:
            raw=await c._call_iop(METHOD_TEXT_SEARCH,req)
            items=_extract_items(raw,METHOD_TEXT_SEARCH)
            print(json.dumps({'kind':'text_search','checked_at_utc':datetime.now(timezone.utc).isoformat(),'query':QUERY,'request':req,'item_count':len(items),'items':items,'raw':raw},ensure_ascii=False,default=str))
        except Exception as e:
            print(json.dumps({'kind':'text_search_error','checked_at_utc':datetime.now(timezone.utc).isoformat(),'query':QUERY,'request':req,'error':repr(e)},ensure_ascii=False))

if __name__=='__main__': asyncio.run(main())
