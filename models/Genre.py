from sqlalchemy import Column, Integer, String, Float,DateTime
from database import Base


class Genre (Base):
    __tablename__ = "Genre"
    genre_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), nullable=False)
    description = Column(String(30))