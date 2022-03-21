from asgiref.sync import async_to_sync

from django.http import Http404, HttpRequest, JsonResponse
from django.shortcuts import redirect, render
from card.services.message_service import create_msg
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
    