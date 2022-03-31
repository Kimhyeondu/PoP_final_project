from django.shortcuts import redirect
from card.models import Gift, Message
from user.models import User
from .gift_service import all_list_gift, search_list_gift, filter_list_gift
from .message_service import update_msg, get_msg
from asgiref.sync import sync_to_async
import httpx


async def use_api_reco(msg:str):
    data = {"msg": msg}
    url = ""
    async with httpx.AsyncClient() as client:
        r = await client.post(url, data=data)
        jsondata = r.json()
        tag = jsondata["tag"]
        return tag


async def recommend_gift_list(id:int, msg:str = ""):
    result = []
    # 메시지 분석 후 추천 부분
    # msg_response = await use_api_reco(msg)
    # msg_result = await search_list_gift(msg_response)    
    # msg_result = msg_result[:10]
    # for item in msg_result:
    #     item.gift_tags = await sync_to_async(list)(item.tags.names())
    # result.append(msg_result)

    # 유저 선호 태그 리스트 
    user = await sync_to_async(User.objects.get)(id=id)
    tag_list = await sync_to_async(list)(user.tag.names())
    if not tag_list:
        tag_list = ["음악"]
    for tag in tag_list:
        tag_result = await search_list_gift(tag)    
        tag_result = tag_result[:10]
        for item in tag_result:
            item.gift_tags = await sync_to_async(list)(item.tags.names())
        result.append(tag_result)
    return result


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


async def decoration_move_service(id:int, top:int, left:int):
    msg1 = await get_msg(id=id)
    if msg1.top == top and msg1.left == left:
        return 200, {"url":f"/card/read/{id}"}
    else:
        await update_msg(id=id, top=top, left=left)
        return 204, None

