from asgiref.sync import async_to_sync, sync_to_async

from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import redirect, render
from card.services.message_service import create_msg, delete_msg
from card.services.deco_service import all_list_deco

from card.models import Message, Gift
from user.models import User


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
            await create_msg(to_user_id=to_user_id, gift_id=gift_id, msg=msg, deco=deco, title=title, author=author)
            
            return JsonResponse({"server":"저장 완료!"})
        deco_list = await all_list_deco()
        return await sync_to_async(render)(request, "card/card_write.html", {"to_user_id":id, "deco_list":deco_list})
    except User.DoesNotExist:        
        raise Http404("존재하지 않는 유저입니다.")



def card_read(request:HttpRequest, message_id:int) -> Message:
    card = Message.objects.get(id=message_id)
    gift = Gift.objects.get(id=card.gift_id)
    return render(request, "card/card_read.html", {"card" : card, "gift":gift})


@login_required
def card_delete(request:HttpRequest, message_id:int) -> None:
    msg = Message.objects.get(id=message_id)
    user_id = msg.to_user_id
    Message.objects.filter(id=message_id).delete()
    return redirect(f'/{user_id}')
