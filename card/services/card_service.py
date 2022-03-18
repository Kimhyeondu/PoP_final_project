from card.models import Gift, Message
from .gift_service import all_list_gift

async def recommend_gift_list(id:int, msg:str = ""):
    result = await all_list_gift()
    return result




