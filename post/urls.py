from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.first_page, name="first page"),
    path("<str:username>", views.main, name="main"),
    path("upload", views.upload, name="upload"),
]
