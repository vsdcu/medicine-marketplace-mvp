from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal

class ChemistPriceCreate(BaseModel):
    chemist_id: UUID
    medicine_id: UUID
    price: Decimal
    stock_status: str

class ChemistPriceResponse(BaseModel):
    id: UUID
    chemist_id: UUID
    medicine_id: UUID
    price: Decimal
    stock_status: str

    model_config = {"from_attributes": True}