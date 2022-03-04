from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('main/', views.main, name='main'),
    # path('detail/<int:id>', views.detail_view, name='detail'),
    # path('detail/comment/<int:id>', views.write_comment, name='write-comment'),
    # path('tweet/comment/delete/<int:id>', views.delete_comment, name='delete-comment'),
    # path('tweet/comment/like/<int:id>',views.comment_like,name='comment_like'),
    path('mypage/', views.mypage, name='mypage'),
    path('edit_user/', views.edit_user, name='mypage'),
]
