from pydantic import BaseModel
from uuid import UUID
from typing import List
from decimal import Decimal

class OrderItemCreate(BaseModel):
    medicine_id: UUID
    quantity: int

class OrderCreate(BaseModel):
    chemist_id: UUID
    items: List[OrderItemCreate]

class OrderResponse(BaseModel):
    id: UUID
    user_id: UUID
    chemist_id: UUID
    status: str

    model_config = {"from_attributes": True}