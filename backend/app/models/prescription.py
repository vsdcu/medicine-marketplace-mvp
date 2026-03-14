from sqlalchemy import Column, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.models.base import UUIDMixin, TimestampMixin
from app.core.database import Base
from app.models.enums import PrescriptionStatus

class Prescription(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "prescriptions"

    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"))
    status = Column(Enum(PrescriptionStatus, name="prescription_status"))

    user = relationship("User", back_populates="prescriptions")
    items = relationship("PrescriptionItem", back_populates="prescription")