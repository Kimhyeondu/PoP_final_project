from asgiref.sync import sync_to_async
from django.shortcuts import redirect, render
from card.models import Message
from django.contrib.auth.decorators import login_required
from card.services.message_service import list_to_user_msg


# @login_required(login_url='signin')
def first_page(request):
    return render(request, "main.html")


async def main(request, xx):
    listall = await list_to_user_msg(xx)
    if listall:
        return await sync_to_async(render)(request, "main.html", {"listall": listall})
    else:
        return await sync_to_async(render)(request, "main.html")



def upload(request):
    return redirect(request, "post/upload.html")


