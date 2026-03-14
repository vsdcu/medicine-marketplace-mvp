from sqlalchemy import Column, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.models.base import UUIDMixin, TimestampMixin
from app.core.database import Base
from app.models.enums import OrderStatus

class Order(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "orders"

    user_id = Column(ForeignKey("users.id"))
    chemist_id = Column(ForeignKey("chemists.id"))
    status = Column(Enum(OrderStatus, name="order_status"))

    user = relationship("User", back_populates="orders")
    chemist = relationship("Chemist", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")