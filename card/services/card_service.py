from card.models import Gift, Message
from .gift_service import all_list_gift, search_list_gift
from asgiref.sync import sync_to_async

async def recommend_gift_list(id:int, msg:str = ""):
    result = await all_list_gift()
    for item in result:
        item.gift_tags = await sync_to_async(list)(item.tags.names())
    result2 = result
    return [result, result2]


async def search_gift_list_service(keyword:str = None):
    if not keyword:
        return 202, {"err_msg":"검색어를 입력하세요."}
    else:
        glist = await search_list_gift(keyword)
        if glist:
            for item in glist:
                item.gift_tags = await sync_to_async(list)(item.tags.names())
            return 200, glist
        else:
            return 202, {"err_msg":"검색 결과가 없습니다."}

