from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import UUIDMixin, TimestampMixin
from app.core.database import Base

class Address(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "addresses"

    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    line1 = Column(String, nullable=False)
    city = Column(String, index=True)
    postal_code = Column(String, index=True)

    user = relationship("User", back_populates="addresses")