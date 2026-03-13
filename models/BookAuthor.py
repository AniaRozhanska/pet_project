from sqlalchemy import Column, Integer, String, Float
from database import Base

class BookAuthor(Base):
    __tablename__ = "BookAuthor"

    book_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, primary_key=True)