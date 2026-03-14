from pydantic import BaseModel
from uuid import UUID

class MedicineCreate(BaseModel):
    name: str
    description: str | None = None

class MedicineUpdate(BaseModel):
    name: str | None = None
    description: str | None = None

class MedicineResponse(BaseModel):
    id: UUID
    name: str
    description: str | None

    model_config = {"from_attributes": True}