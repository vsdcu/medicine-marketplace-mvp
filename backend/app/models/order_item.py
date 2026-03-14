from sqlalchemy import Column, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship
from app.models.base import UUIDMixin, TimestampMixin
from app.core.database import Base

class OrderItem(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "order_items"

    order_id = Column(ForeignKey("orders.id", ondelete="CASCADE"))
    medicine_id = Column(ForeignKey("medicines.id"))
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(10, 2))

    order = relationship("Order", back_populates="items")