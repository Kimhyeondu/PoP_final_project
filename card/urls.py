from django.urls import path

from . import views

urlpatterns = [
    path("write/", views.card_write, name="card_write"),
]
