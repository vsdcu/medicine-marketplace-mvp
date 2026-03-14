from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from app.models.base import UUIDMixin, TimestampMixin
from app.core.database import Base

class Medicine(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "medicines"

    name = Column(String, index=True, nullable=False)
    description = Column(Text)

    chemist_prices = relationship("ChemistPrice", back_populates="medicine")