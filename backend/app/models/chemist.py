from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.models.base import UUIDMixin, TimestampMixin
from app.core.database import Base

class Chemist(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "chemists"

    name = Column(String, index=True)
    license_number = Column(String, unique=True)

    prices = relationship("ChemistPrice", back_populates="chemist")
    orders = relationship("Order", back_populates="chemist")