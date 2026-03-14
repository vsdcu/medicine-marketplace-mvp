from pydantic import BaseModel
from uuid import UUID

class AddressCreate(BaseModel):
    line1: str
    city: str
    postal_code: str

class AddressResponse(BaseModel):
    id: UUID
    user_id: UUID
    line1: str
    city: str
    postal_code: str

    model_config = {"from_attributes": True}