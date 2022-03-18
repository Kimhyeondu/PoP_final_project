import time
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render


# Create your views here.
def card_write(request:HttpRequest, id:int):
    if request.method == "POST":
        to_user_id = request.POST["to_user_id"]
        gift_id = request.POST["gift_id"]
        msg = request.POST["msg"]
        deco = request.POST["deco"]
        title = request.POST["title"]
        author = request.POST["author"]
        
        return JsonResponse({"msg":"저장 완료!"})
    return render(request, "card/card_write.html", {"to_user_id":id})
