from fastapi import APIRouter
from app.api.models.item import Item

message = APIRouter()


@message.get('/v1/message/{name}', tags=['message'])
def get_message(name: str):
    return {"name >> ": name}


@message.post("/v1/message/items")
def post_item(item: Item):
    print(item)
    return {"item": f"Item created = {item.name}"}
