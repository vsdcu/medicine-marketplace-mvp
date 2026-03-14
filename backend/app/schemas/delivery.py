from pydantic import BaseModel
from uuid import UUID

class DeliveryCreate(BaseModel):
    order_id: UUID
    tracking_number: str | None = None

class DeliveryResponse(BaseModel):
    id: UUID
    order_id: UUID
    status: str
    tracking_number: str | None

    model_config = {"from_attributes": True}