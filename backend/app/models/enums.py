import enum

class OrderStatus(str, enum.Enum):
    pending = "pending"
    quoted = "quoted"
    confirmed = "confirmed"
    dispatched = "dispatched"
    delivered = "delivered"
    cancelled = "cancelled"

class StockStatus(str, enum.Enum):
    in_stock = "in_stock"
    low_stock = "low_stock"
    out_of_stock = "out_of_stock"

class PrescriptionStatus(str, enum.Enum):
    uploaded = "uploaded"
    verified = "verified"
    rejected = "rejected"

class DeliveryStatus(str, enum.Enum):
    preparing = "preparing"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"
    failed = "failed"

class UserRole(str, enum.Enum):
    customer = "customer"
    chemist = "chemist"
    admin = "admin"