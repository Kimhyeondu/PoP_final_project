from asgiref.sync import async_to_sync

from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import redirect, render

from card.models import Message, Gift
from card.services.message_service import create_msg, delete_msg
from user.models import User


# Create your views here.
def card_write(request:HttpRequest, id:int):
    try:
        User.objects.get(id=id)
        if request.method == "POST":
            to_user_id = request.POST["to_user_id"]
            gift_id = request.POST["gift_id"]
            msg = request.POST["msg"]
            deco = request.POST["deco"]
            title = request.POST["title"]
            author = request.POST["author"]
            async_to_sync(create_msg)(to_user_id=to_user_id, gift_id=gift_id, msg=msg, deco=deco, title=title, author=author)
            
            return JsonResponse({"server":"저장 완료!"})
        return render(request, "card/card_write.html", {"to_user_id":id})
    except:
        raise Http404("존재하지 않는 유저입니다.")






def card_read(request:HttpRequest, message_id:int) -> Message:
    card = Message.objects.get(id=message_id)
    gift = Gift.objects.get(id=card.gift_id)
    return render(request, "card/card_read.html", {"card" : card, "gift":gift})


def card_delete(request:HttpRequest, message_id:int) -> None:
    Message.objects.filter(id=message_id).delete()
    return redirect('/')