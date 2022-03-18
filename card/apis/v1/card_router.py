from typing import List
from django.shortcuts import render
from ninja import Router, Form
from django.http import HttpRequest
from asgiref.sync import async_to_sync

from .schemas.card_request import GiftRequest, SearchRequest
from .schemas.card_response import CardResponse, ErrorMessage
from card.services.card_service import recommend_gift_list, search_gift_list_service

router = Router()

@router.post("/",response = List[List[CardResponse]])
async def gift_list(request: HttpRequest, card_request: GiftRequest = Form(...)):
    result = await recommend_gift_list(card_request.id, card_request.msg)
    return result


@router.post("/search/", response = {200: List[CardResponse], 202: ErrorMessage})
async def search_gift(request: HttpRequest, keyword: SearchRequest = Form(...)):
    code, result = await search_gift_list_service(keyword.keyword)
    return code, result

