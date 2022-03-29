from django.urls import path

from . import views

urlpatterns = [
    path("write/<int:id>", views.card_write, name="card_write"),
    path("read/<int:message_id>", views.card_read, name="card_read"),
    path("delete/<int:message_id>", views.card_delete, name="card_delete"),
]
