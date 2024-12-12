from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

user = User(id=1, name="Alice", email="alice@example.com")

print(user.id)  # 1
print(user.name)  # Alice
print(user.dict())  # {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'}