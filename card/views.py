import time
from django.http import JsonResponse
from django.shortcuts import redirect, render


# Create your views here.
def card_write(request):
    if request.method == "POST":
        # print(request.POST)
        # time.sleep(1)
        return JsonResponse({"msg":"dev"})
    return render(request, "card/card_write.html")
