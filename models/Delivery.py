from sqlalchemy import Column, Integer, String, Float,DateTime
from database import Base


class Delivery(Base):
    __tablename__ = "Delivery"
    delivery_id = Column(Integer, primary_key=True, index=True)
    delivery_date = Column(DateTime, nullable=False)
    delivery_address = Column(String(30))
    delivery_method = Column(String(30))
    status = Column(String(30))
    order_id = (Integer)