from typing import Union

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
    description: str | None = None
    tax: float | None = None
