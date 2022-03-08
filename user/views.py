from django.contrib import auth
from django.shortcuts import redirect, render

# Create your views here.


def mypage(request):
    return render(request, "user/mypage.html", {})


def edit_user(request):
    if request.method == "GET":
        return render(request, "user/edit_profile.html", {})

    if request.method == "POST":
        return render(request, "user/edit_profile.html", {})

    # true_user = auth.authenticate(request, username=username, password=password)
    # if true_user is not None:
    #     auth.login(request, true_user)
    #     return redirect('/main')
    # else:
    #     return render(request, 'user/edit_profile.html', {'error2': ' ID 또는 패스워드를 확인해주세요!'})
