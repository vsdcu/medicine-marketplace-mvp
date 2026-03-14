from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.models.base import UUIDMixin, TimestampMixin
from app.core.database import Base

class PrescriptionItem(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "prescription_items"

    prescription_id = Column(ForeignKey("prescriptions.id", ondelete="CASCADE"))
    medicine_id = Column(ForeignKey("medicines.id"))
    quantity = Column(Integer, nullable=False)

    prescription = relationship("Prescription", back_populates="items")