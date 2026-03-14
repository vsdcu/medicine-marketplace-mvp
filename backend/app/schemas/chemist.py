from pydantic import BaseModel
from uuid import UUID

class ChemistCreate(BaseModel):
    name: str
    license_number: str

class ChemistResponse(BaseModel):
    id: UUID
    name: str
    license_number: str

    model_config = {"from_attributes": True}