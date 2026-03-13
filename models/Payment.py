from sqlalchemy import Column, Integer, String, Float,DateTime
from database import Base


class Payment (Base):
    __tablename__ = "Payment"
    payment_id = Column(Integer, primary_key=True, index=True)
    payment_date = Column(DateTime, nullable=False)
    amount = Column(Float)
    payment_method = Column(String(30))
    status = Column(String(30))
    order_id = Column(Integer)