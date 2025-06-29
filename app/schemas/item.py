from typing import Literal, Union

from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
    description: str | None = None
    tax: float | None = None


class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(10, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []
