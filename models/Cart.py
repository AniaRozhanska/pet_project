from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from database import Base


class Cart(Base):
    __tablename__ = "Cart"
    cart_id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
    user_id = Column(Integer)
    book_id = Column(Integer)
    delivery_date = Column(DateTime, nullable=False)
    delivery_address = Column(String(255))
    delivery_method = Column(String(50))
    status = Column(String(20))