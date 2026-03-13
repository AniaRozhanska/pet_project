from sqlalchemy import Column, Integer, String, Float,DateTime
from database import Base


class Orders (Base):
    __tablename__ = "Orders"
    order_id = Column(Integer, primary_key=True, index=True)
    order_date = Column(DateTime, nullable=False)
    status = Column(String(30))
    total_price = Column(Integer)
    cart_id = Column(Integer)