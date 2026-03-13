from database import SessionLocal
from models.User import User

db = SessionLocal()
users = db.query(User).all()
for user in users:
    print(user.user_id, user.age, user.email, user.name, user.password, user.phone_number)