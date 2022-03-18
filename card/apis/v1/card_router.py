from typing import List
from django.shortcuts import render
from ninja import Router, Form
from django.http import HttpRequest
from asgiref.sync import async_to_sync

from .schemas.card_request import CardRequest
from .schemas.card_response import CardResponse, SyncCardResponse
from card.services.card_service import recommend_gift_list

router = Router()

@router.post("/",response = List[CardResponse])
async def gift_list(request: HttpRequest, card_request: CardRequest = Form(...)):
    result = await recommend_gift_list(card_request.id, card_request.msg)
    return result

@router.post("/sync/",response = List[SyncCardResponse])
def sync_gift_list(request: HttpRequest, card_request: CardRequest = Form(...)):
    result = async_to_sync(recommend_gift_list)(card_request.id, card_request.msg)
    return result