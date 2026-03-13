from sqlalchemy import Column, Integer, String, Float
from database import Base

class Book(Base):
    __tablename__ = "Book"

    book_id = Column(Integer, primary_key=True)
    title = Column(String(30))
    price = Column(Float)
    year = Column(Integer)
    description = Column(String(155))
    stock_quantity = Column(Integer)
    genre_id = Column(Integer)