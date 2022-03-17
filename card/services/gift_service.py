from typing import cast, List

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


async def gift_update(id, gift_name = None, gift_img = None, gift_desc = None, tags = None):
    gift = await gift_get(id=id)
    if gift_name:
        gift.gift_name = gift_name
    if gift_img:
        gift.gift_img = gift_img
    if gift_desc:
        gift.gift_desc = gift_desc
    if tags:
        tag_slugs_list = list(map(lambda x: x.strip(), tags.strip().split(",")))
        await sync_to_async(gift.tags.clear)()        
        await sync_to_async(gift.tags.add)(*tag_slugs_list)
    await sync_to_async(gift.save)()


async def gift_delete(id):
    gift = await gift_get(id=id)
    await sync_to_async(gift.delete)()

