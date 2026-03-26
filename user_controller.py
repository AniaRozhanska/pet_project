from models.User import User
from database import session 

class UserController:

   
    @staticmethod
    def create_user(name, phone_number, email, password, age):
        user = User(
            name=name,
            phone_number=phone_number,
            email=email,
            password=password,
            age=age
        )
        session.add(user)
        session.commit()
        return user

  
    @staticmethod
    def get_all_users():
        return session.query(User).all()

    
    @staticmethod
    def get_user_by_id(user_id):
        return session.query(User).filter(User.user_id == user_id).first()

   
    @staticmethod
    def get_user_by_email(email):
        return session.query(User).filter(User.email == email).first()

    
    @staticmethod
    def update_user(user_id, name=None, phone_number=None, email=None, password=None, age=None):
        user = session.query(User).filter(User.user_id == user_id).first()
        if not user:
            return None
        if name is not None:
            user.name = name
        if phone_number is not None:
            user.phone_number = phone_number
        if email is not None:
            user.email = email
        if password is not None:
            user.password = password
        if age is not None:
            user.age = age
        session.commit()
        return user

    
    @staticmethod
    def delete_user(user_id):
        user = session.query(User).filter(User.user_id == user_id).first()
        if not user:
            return False
        session.delete(user)
        session.commit()
        return True