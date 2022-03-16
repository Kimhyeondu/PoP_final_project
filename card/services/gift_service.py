from typing import cast, List

from django.shortcuts import get_object_or_404
from django.db.models import Q
from card.models import Gift, Message
from asgiref.sync import sync_to_async


async def gift_create(gift_name, gift_img, gift_desc, tags):
    result = await sync_to_async(Gift.objects.create)(gift_name=gift_name, gift_img=gift_img, gift_desc=gift_desc)
    tag_slugs_list = list(map(lambda x: x.strip(), tags.strip().split(",")))
    await sync_to_async(result.tags.add)(*tag_slugs_list)
    await sync_to_async(result.save)()
    return cast(Gift, result)

@sync_to_async
def gift_get(*args, **kwargs):
    return Gift.objects.get(*args, **kwargs)


@sync_to_async
def gift_list_all():
    return list(Gift.objects.all())


@sync_to_async
def gift_list_by_filter(*args, **kwargs):
    return Gift.objects.filter(*args, **kwargs).distinct()


@sync_to_async
def gift_list_by_search(keyword):
    return Gift.objects.filter(Q(gift_name__icontains=keyword) | Q(gift_desc__icontains=keyword) | Q(tags__name=keyword)).distinct()



def gift_update(gift_name, gift_img, gift_desc, tags):
    pass


def gift_delete(q):
    pass

