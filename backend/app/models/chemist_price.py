from sqlalchemy import Column, ForeignKey, Numeric, Enum
from sqlalchemy.orm import relationship
from app.models.base import UUIDMixin, TimestampMixin
from app.core.database import Base
from app.models.enums import StockStatus

class ChemistPrice(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "chemist_prices"

    chemist_id = Column(ForeignKey("chemists.id", ondelete="CASCADE"))
    medicine_id = Column(ForeignKey("medicines.id", ondelete="CASCADE"))
    price = Column(Numeric(10, 2), nullable=False)
    stock_status = Column(Enum(StockStatus, name="stock_status"))

    chemist = relationship("Chemist", back_populates="prices")
    medicine = relationship("Medicine", back_populates="chemist_prices")