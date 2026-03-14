from pydantic import BaseModel
from uuid import UUID
from typing import List

class PrescriptionItemCreate(BaseModel):
    medicine_id: UUID
    quantity: int

class PrescriptionCreate(BaseModel):
    items: List[PrescriptionItemCreate]

class PrescriptionResponse(BaseModel):
    id: UUID
    user_id: UUID

    model_config = {"from_attributes": True}