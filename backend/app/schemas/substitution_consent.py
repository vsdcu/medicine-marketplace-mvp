from pydantic import BaseModel
from uuid import UUID


class SubstitutionConsentCreate(BaseModel):
    prescription_item_id: UUID
    allowed: bool


class SubstitutionConsentResponse(BaseModel):
    id: UUID
    user_id: UUID
    prescription_item_id: UUID
    allowed: bool

    model_config = {"from_attributes": True}