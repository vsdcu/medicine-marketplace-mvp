from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal


class OrderItemCreate(BaseModel):
    medicine_id: UUID
    quantity: int


class OrderItemResponse(BaseModel):
    id: UUID
    order_id: UUID
    medicine_id: UUID
    quantity: int
    unit_price: Decimal

    model_config = {"from_attributes": True}