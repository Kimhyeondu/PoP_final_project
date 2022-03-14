from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
app_name = 'user'
urlpatterns = [
    # path('main/', views.main, name='main'),
    # path('detail/<int:id>', views.detail_view, name='detail'),
    # path('detail/comment/<int:id>', views.write_comment, name='write-comment'),
    # path('tweet/comment/delete/<int:id>', views.delete_comment, name='delete-comment'),
    # path('tweet/comment/like/<int:id>',views.comment_like,name='comment_like'),
    path("mypage/", views.mypage, name="mypage"),
    path("edit_user/", views.edit_user),
    path("signin/", views.LoginView.as_view(), name="signin"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("is_id/", views.is_id, name="isid"),
    path("is_email/", views.is_email, name="isemail"),
    path('kakao/', views.to_kakao, name='kakao'),
    path('kakao/callback/', views.from_kakao, name='kakako_login'),
    path('logout/', views.log_out, name='logout'),

]
