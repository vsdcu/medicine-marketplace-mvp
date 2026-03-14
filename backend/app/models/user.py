from sqlalchemy import Column, Enum, String, Boolean
from sqlalchemy.orm import relationship
from app.models.base import UUIDMixin, TimestampMixin
from app.core.database import Base
from app.models.enums import UserRole

class User(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(Enum(UserRole, name="userrole"), server_default=UserRole.customer, nullable=False, index=True)

    addresses = relationship("Address", back_populates="user")
    prescriptions = relationship("Prescription", back_populates="user")
    orders = relationship("Order", back_populates="user")