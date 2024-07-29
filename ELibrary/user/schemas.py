from ninja import Schema
from pydantic import EmailStr
from datetime import date

class UserCreateSchema(Schema):
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    password: str
    password_confirm: str
    created_at: date

class UserAuthSchema(Schema):
    username: str
    password: str

class UserOutSchema(Schema):
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    created_at: date

class UserListSchema(Schema):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    date_joined: str