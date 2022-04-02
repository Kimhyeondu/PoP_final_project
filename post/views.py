from asgiref.sync import sync_to_async
from django.shortcuts import redirect, render
from card.models import Message
from django.contrib.auth.decorators import login_required
from card.services.message_service import list_to_user_msg


# @login_required(login_url='signin')
from user.models import User


def first_page(request):
    return render(request, "main.html")


async def main(request, username:str):
    user = await sync_to_async(User.objects.get)(username=username)
    user_id = user.id
    listall = await list_to_user_msg(user_id)
    if listall:
        return await sync_to_async(render)(request, "main.html", {"listall": listall, "user_id":user_id})
    else:
        return await sync_to_async(render)(request, "main.html")



def upload(request):
    return redirect(request, "post/upload.html")


