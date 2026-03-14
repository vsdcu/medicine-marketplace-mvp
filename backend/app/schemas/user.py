from pydantic import BaseModel, EmailStr
from uuid import UUID
from app.models.enums import UserRole


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    role: UserRole

    model_config = {"from_attributes": True}