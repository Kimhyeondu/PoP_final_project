from asgiref.sync import sync_to_async
from django.shortcuts import redirect, render
from card.services.message_service import list_to_user_msg
from user.models import User

def main(request):
    return render(request, "main.html")


async def CardList(request, username:str):
    user = await sync_to_async(User.objects.get)(username=username)
    user_id = user.id
    listall = await list_to_user_msg(user_id)
    if listall:
        return await sync_to_async(render)(request, "card_list.html", {"listall": listall, "user_id":user_id, "username" : username})
    else:
        return await sync_to_async(render)(request, "card_list.html", {"user_id":user_id, "username" : username})

async def id_to_username(request, user_id:int):
    user = await sync_to_async(User.objects.get)(id=user_id)
    return redirect(f'/{user.username}')

def upload(request):
    return redirect(request, "post/upload.html")





