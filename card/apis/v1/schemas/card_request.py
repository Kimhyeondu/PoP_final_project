from ninja import Schema


class CardRequest(Schema):
    id: int
    msg: str


