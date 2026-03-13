from sqlalchemy import Column, Integer, String, Float
from database import Base


class Author(Base):
    __tablename__ = "Author"

    author_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(30), nullable=False)
    country = Column(String(30))
    short_biography = Column(String(90))
    age = Column(Integer)