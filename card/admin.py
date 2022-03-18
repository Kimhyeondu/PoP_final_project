from django.contrib import admin
from card.models import Gift, Message


# Register your models here.
@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ("gift_name", "gift_desc")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "to_user_id", "gift_id")
