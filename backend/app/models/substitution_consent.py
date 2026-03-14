from sqlalchemy import Column, ForeignKey, Boolean
from app.models.base import UUIDMixin, TimestampMixin
from app.core.database import Base

class SubstitutionConsent(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "substitution_consents"

    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"))
    prescription_item_id = Column(ForeignKey("prescription_items.id"))
    allowed = Column(Boolean, default=False)