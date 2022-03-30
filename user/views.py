from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from django.views.generic import FormView
from django.contrib import messages
from .mixins import LogoutOnlyView
from .forms import LoginForm, SignUpForm
from .models import User
import os
import requests
# Create your views here.

def log_out(request):
    logout(request)
    return redirect(reverse('user:signin'))

@login_required
def mypage(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "GET":
        tag_list = list(user.tag.names())
        return render(request, "user/edit_profile.html", {'tag_list':tag_list})
    if request.method == "POST":
        tags = []
        # print(request.POST, request.FILES)
        tagcount= int(request.POST.get('tag_count','0'))
        # print(tagcount)
        for i in range(tagcount):
            tag=request.POST.get(f'taginput{i}', '')
            #'데이터' 형식으로 들어오는데 양끝 '문자 제거
            tag=tag[:-1][1:]
            tags.append(tag)
            # print(tags[-1])
        # print(tags)
        if request.FILES:
            user.profile_img = request.FILES.get("imgs")
        user.tag.clear()
        user.tag.add(*tags)
        user.save()
        return redirect("/mypage")


    # true_user = auth.authenticate(request, username=username, password=password)
    # if true_user is not None:
    #     auth.login(request, true_user)
    #     return redirect('/main')
    # else:
    #     return render(request, 'user/edit_profile.html', {'error2': ' ID 또는 패스워드를 확인해주세요!'})

# def sign_in(request):
#     if request.method == 'GET':
#         return render(request, "user/signin.html", {})
#     username = request.POST.get('username','')
#     password = request.POST.get('password','')
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect(reverse('user:mypage'))
#     else:
#         return render(request, "user/signin.html", {'msg':'아이디 혹은 비밀번호가 다릅니다.'})

class LoginView(LogoutOnlyView, FormView):
    form_class = LoginForm
    success_url = reverse_lazy("user:mypage")
    template_name = "user/signin.html"

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            messages.success(self.request, f'어서오세요 {username}님 !')
            login(self.request, user)
            if user.tag.names():
                self.success_url = "/"
        return super().form_valid(form)



class SignUpView(LogoutOnlyView, FormView):
    form_class = SignUpForm
    success_url = reverse_lazy("user:mypage")
    template_name = "user/signup.html"

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            messages.success(self.request,f'환영합니다 {username}님 !')
            login(self.request, user)
        return super().form_valid(form)



def is_id(request):
    username = request.POST.get('username','')
    try:
        User.objects.get(username=username)
        return JsonResponse({'msg':'이미 사용중인 아이디 입니다.'})
    except:
        return JsonResponse({'msg':'사용하셔도 좋습니다.'})

def is_email(request):
    email = request.POST.get('email','')
    try:
        User.objects.get(email=email)
        return JsonResponse({'msg':'이미 사용중인 이메일 입니다.'})
    except:
        return JsonResponse({'msg':'사용하셔도 좋습니다.'})

# def sign_up(request):
    
#     if request.method == 'GET':
#         return render(request, "user/signup.html")
#     username = request.POST.get('username','')
#     email = request.POST.get('email','')
#     password1 = request.POST.get('password1','')
#     password2 = request.POST.get('password2','')
#     #비밀번호 일치하지 않으면 돌려보냄
#     if password1 != password2:
#         return JsonResponse({'msg':'비밀번호가 일치하지 않습니다.'})
#     try:

#         #아이디가 존재하는지 확인 후 오류가 난다면 없다는 뜻
#         user = User.objects.get(username=username)
#         #아이디 존재
#         if user:
#             return JsonResponse({'msg':'아이디가 이미 사용중입니다. 중복확인을 해주세요.'})

#     #새로운 아이디를 만드는 곳        
#     except User.DoesNotExist:
#         try:
#             #이메일도 primary 해야하기에 다시한번 확인
#             user = User.objects.get(email=email)
#             if user:
#                 return JsonResponse({'msg':'이메일이 이미 사용중입니다. 중복확인을 해주세요.'})
#         except User.DoesNotExist:
#                 user = User.objects.create_user(username=username,password=password1,email=email)
#                 login(request,user)
#                 return JsonResponse({'ok':'ok'})
    

def to_kakao(request):
    REST_API_KEY = os.environ.get('REST_API_KEY')
    REDIRECT_URI = 'http://localhost:8000/kakao/callback'
    return redirect(
        f'https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code')


def from_kakao(request):
    REST_API_KEY = os.environ.get('REST_API_KEY')
    REDIRECT_URI = 'http://localhost:8000/kakao/callback'
    code = request.GET.get('code', 'None')
    if code is None:
        # 코드 발급 x
        return redirect('/')
    headers = {'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'}
    get_token = requests.post(
        f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&code={code}',
        headers=headers)
    get_token = get_token.json()
    if get_token.get('error', None) is not None:
        # 에러발생
        return redirect('/')
    token = get_token.get('access_token', None)

    headers = {'Authorization': f'Bearer {token}'}
    get_info = requests.post(f'https://kapi.kakao.com/v2/user/me', headers=headers)
    info = get_info.json()
    properties = info.get('properties')
    username = properties.get('nickname', None)
    kakao_account = info.get('kakao_account')
    profile_img = properties.get('profile_image', None)
    email = kakao_account.get('email', None)
    if email is None:
        # 이메일 동의 안하면 로그인 불가 처리..
        return redirect('/sign-in')
    try:
        user = User.objects.get(email=email)

        if user.login_method != User.LOGIN_KAKAO:
            print('카카오로 가입하지 않은 다른 아이디가 존재함')
            return redirect('/')


    except:
        user = User.objects.create(username=username, profile_img=profile_img,
                                                email=email, login_method=User.LOGIN_KAKAO)
        user.set_unusable_password()
        user.save()

    login(request, user)
    return redirect('/mypage')