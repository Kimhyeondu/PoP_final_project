from ninja import Schema


class GiftRequest(Schema):
    id: int
    msg: str


class SearchRequest(Schema):
    keyword: str