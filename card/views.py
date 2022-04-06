from asgiref.sync import sync_to_async

from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import redirect, render
from card.services.message_service import create_msg, delete_msg
from card.services.deco_service import all_list_deco

from card.models import Message, Gift
from user.models import User
import random

# Create your views here.
async def card_write(request:HttpRequest, id:int):
    try:
        await sync_to_async(User.objects.get)(id=id)
        if request.method == "POST":
            to_user_id = request.POST.get("to_user_id")
            gift_id = request.POST.get("gift_id")
            msg = request.POST.get("msg")
            deco = request.POST.get("deco")
            title = request.POST.get("title")
            author = request.POST.get("author")
            top = random.randrange(0,520)
            left = random.randrange(0, 400)
            # await create_msg(to_user_id=to_user_id, gift_id=gift_id, msg=msg, deco=deco, title=title, author=author)
            await create_msg(
                to_user_id=to_user_id, gift_id=gift_id, msg=msg, deco=deco, title=title, author=author, top=top, left=left)
            user = await sync_to_async(User.objects.get)(id=to_user_id)
            user.msg_count += 1
            await sync_to_async(user.save)()
            return JsonResponse({"server":"저장 완료!"})
        deco_list = await all_list_deco()
        return await sync_to_async(render)(request, "card/card_write.html", {"to_user_id":id, "deco_list":deco_list})
    except User.DoesNotExist:        
        raise Http404("존재하지 않는 유저입니다.")



async def card_read(request:HttpRequest, message_id:int) -> Message:
    card = await sync_to_async(Message.objects.get)(id=message_id)
    gift = await sync_to_async(Gift.objects.get)(id=card.gift_id)
    return await sync_to_async(render)(request, "card/card_read.html", {"card" : card, "gift":gift})


async def card_delete(request:HttpRequest, message_id:int):
    msg = await sync_to_async(Message.objects.get)(id=message_id)
    user_id = msg.to_user_id
    user= await sync_to_async(User.objects.get)(id=user_id)
    name = user.username
    await delete_msg(message_id)
    return redirect(f'/{name}')


def read_or_unread(request: HttpRequest, message_id:int):
    msg = Message.objects.get(id=message_id)
    msg_receiver = User.objects.get(id=msg.to_user_id)
    click_user = request.user
    if click_user.id == msg.to_user_id:
        Message.objects.filter(id=message_id).update(read=1)
    return redirect(f'/{msg_receiver.username}')