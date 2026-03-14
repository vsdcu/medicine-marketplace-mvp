from pydantic import BaseModel
from uuid import UUID


class PrescriptionItemCreate(BaseModel):
    medicine_id: UUID
    quantity: int


class PrescriptionItemResponse(BaseModel):
    id: UUID
    prescription_id: UUID
    medicine_id: UUID
    quantity: int

    model_config = {"from_attributes": True}