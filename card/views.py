import time
from django.shortcuts import redirect, render


# Create your views here.
def card_write(request):
    if request.method == "POST":
        print(request.POST)
        time.sleep(1)
        return redirect("card_gift")
    return render(request, "card/card_write.html")

def card_gift(request):
    return render(request, "card/card_gift.html")