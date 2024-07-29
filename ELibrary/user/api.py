from ninja import NinjaAPI, Schema
from pydantic import EmailStr, Field
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .Schema import UserCreateSchema, UserAuthSchema, UserOutSchema

api = NinjaAPI()

#api function to create a new user
@api.post("/signup", response=UserOutSchema)
def signup(request, data: UserCreateSchema):
    if data.password != data.password_confirm:
        return {"error": "Passwords do not match"}
    
    if User.objects.filter(username=data.username).exists():
        return {"error": "Username already taken"}
    
    user = User.objects.create_user(
        username=data.username,
        email=data.email,
        first_name=data.first_name,
        last_name=data.last_name,
        password=data.password,
        created_at=data.created_at(datetime.now())
    )
    return user

#api function to sign in a user
@api.post("/signin")
def signin(request, data: UserAuthSchema):
    user = authenticate(username=data.username, password=data.password)
    if user is None:
        return {"error": "Invalid credentials"}
    
    login(request, user)
    return {"message": "Signin successful"}

#api function to sign out a user
@api.post("/signout")
def signout(request):
    logout(request)
    return {"message": "Signout successful"}

#api function to get the details of the logged-in user
@api.get("/me", response=UserOutSchema)
def get_me(request):
    user = request.user
    if not user.is_authenticated:
        return {"error": "Not authenticated"}
    
    return {
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
    }

#api function to update the profile of the logged-in user
@api.put("/update-profile", response=dict)
def update_profile(request, data: UserUpdateSchema):
    user = request.user
    if not user.is_authenticated:
        return {"error": "Not authenticated"}
    
    user.first_name = data.first_name
    user.last_name = data.last_name
    user.email = data.email

    if data.password:
        user.set_password(data.password)
    
    user.save()

    return {
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email
    }

#api function to delete the account of the logged-in user
@api.delete("/delete-account", response=dict)
def delete_account(request):
    user = request.user
    if not user.is_authenticated:
        return {"error": "Not authenticated"}
    
    user.delete()
    logout(request)
    
    return {"message": "Account deleted successfully"}

#api function to list all users
@api.get("/users", response=List[UserListSchema])
def list_users(request):
    users = User.objects.all()
    return [
        {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "date_joined": user.date_joined.strftime('%d-%m-%Y %H:%M:%S')
        } for user in users
    ]