from ninja import schema


class CardRequest(schema):
    msg: str
    id: int

