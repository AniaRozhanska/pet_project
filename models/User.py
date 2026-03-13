from sqlalchemy import Column, Integer, String, Float
from database import Base

class User(Base):
    __tablename__ = "User"

    user_id = Column(Integer, primary_key=True)
    name = Column(String(30))
    phone_number = Column(String(15))
    email = Column(String(55))
    password= Column(String(55))
    age = Column(Integer)