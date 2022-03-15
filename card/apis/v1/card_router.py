from ninja import Router, Form
# from django.http import HttpRequest

# from .schemas import CardResponse, CardRequest

router = Router()

# @router.post("/",response = CardResponse)
# def gift_list(request: HttpRequest,card_request: CardRequest = Form(...)):
#     gift_name = "gift_name"
#     gift_desc = "gift_desc"
#     gift_img = {"title":"title", "image":"image"}
#     return {gift_name:gift_name, gift_desc:gift_desc, gift_img:gift_img}
