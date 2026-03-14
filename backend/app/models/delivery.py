from sqlalchemy import Column, ForeignKey, Enum, String
from sqlalchemy.orm import relationship
from app.models.base import UUIDMixin, TimestampMixin
from app.core.database import Base
from app.models.enums import DeliveryStatus

class Delivery(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "deliveries"

    order_id = Column(ForeignKey("orders.id", ondelete="CASCADE"), unique=True)
    status = Column(Enum(DeliveryStatus, name="delivery_status"))
    tracking_number = Column(String)

    order = relationship("Order")