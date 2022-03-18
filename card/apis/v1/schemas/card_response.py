from typing import Any, List, Optional
from ninja import Schema
from asgiref.sync import sync_to_async


class CardResponse(Schema):
    gift_name: str
    gift_desc: str
    gift_img: str
    tags: Any

    @staticmethod   
    async def resolve_tags(obj):
        result = await sync_to_async(list)(obj.tags.names())[0]
        return result


class SyncCardResponse(Schema):
    gift_name: str
    gift_desc: str
    gift_img: str
    tags: Any

    @staticmethod  
    def resolve_tags(obj):
        result = list(obj.tags.names())[0]
        return result
