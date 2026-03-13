from sqlalchemy import Column, Integer, String, Float,DateTime
from database import Base


class Store (Base):
    __tablename__ = "Store"
    bookstore_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))
    address = Column(String(30))
