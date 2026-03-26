from fastapi import FastAPI
from user_controller import UserController  

app = FastAPI(title="User REST API")


@app.get("/")
def root():
    return {"message": "API працює 🚀"}


@app.post("/users")
def create_user(name: str, phone_number: str, email: str, password: str, age: int):
    user = UserController.create_user(name, phone_number, email, password, age)
    return {"user_id": user.user_id, "name": user.name, "email": user.email}


@app.get("/users")
def get_users():
    users = UserController.get_all_users()
    return [
        {"user_id": u.user_id, "name": u.name, "email": u.email, "age": u.age}
        for u in users
    ]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = UserController.get_user_by_id(user_id)
    if not user:
        return {"error": "User not found"}
    return {"user_id": user.user_id, "name": user.name, "email": user.email, "age": user.age}


@app.put("/users/{user_id}")
def update_user(user_id: int, name: str = None, phone_number: str = None,
                email: str = None, password: str = None, age: int = None):
    user = UserController.update_user(
        user_id,
        name=name,
        phone_number=phone_number,
        email=email,
        password=password,
        age=age
    )
    if not user:
        return {"error": "User not found"}
    return {"message": "User updated", "user_id": user.user_id}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    success = UserController.delete_user(user_id)
    if not success:
        return {"error": "User not found"}
    return {"message": "User deleted"}
