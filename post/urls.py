from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("<str:username>", views.CardList, name="CardList"),
    path("upload", views.upload, name="upload"),
]
