from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import CustomUserCreationForm, UserUpdateForm
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest

def is_superuser(user):
    return user.is_superuser

def signup_view(request):
    try:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                messages.success(request, "Account created successfully!")
                return redirect("signin")
            else:
                messages.error(request, "Error creating account.")
        else:
            form = CustomUserCreationForm()
        
        return render(request, "signup.html", {"form": form})
    except Exception as e:
        # Log the error and display a user-friendly message
        messages.error(request, "An error occurred while creating your account.")
        return render(request, "signup.html", {"form": form})

def signin_view(request):
    try:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            form = AuthenticationForm()
        
        return render(request, "signin.html", {"form": form})
    except Exception as e:
        # Log the error and display a user-friendly message
        messages.error(request, "An error occurred during sign-in.")
        return render(request, "signin.html", {"form": form})

def signout_view(request):
    try:
        logout(request)
        return redirect("signin")
    except Exception as e:
        # Log the error and display a user-friendly message
        messages.error(request, "An error occurred during sign-out.")
        return redirect("dashboard")

@login_required
def profile_view(request):
    try:
        if request.method == "GET":
            user = request.user
            context = {
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "date_joined": user.date_joined,
            }
            return render(request, "profile.html", context)
    except Exception as e:
        # Log the error and display a user-friendly message
        messages.error(request, "An error occurred while fetching your profile.")
        return redirect("dashboard")

@login_required
def update_profile_view(request):
    try:
        if request.method == "POST":
            form = UserUpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                user = form.save(commit=False)
                password = form.cleaned_data.get('password')
                if password:
                    user.set_password(password)
                user.save()
                messages.success(request, "Profile updated successfully!")
                return redirect("profile")
        else:
            form = UserUpdateForm(instance=request.user)
        
        return render(request, "update_profile.html", {"form": form})
    except Exception as e:
        # Log the error and display a user-friendly message
        messages.error(request, "An error occurred while updating your profile.")
        return render(request, "update_profile.html", {"form": form})

@login_required
def delete_account_view(request):
    try:
        if request.method == "POST":
            user = request.user
            user.delete()
            logout(request)
            messages.success(request, "Your account has been deleted successfully.")
            return redirect("signup")  # Redirect to signup or home page

        return render(request, "confirm_delete.html")
    except Exception as e:
        # Log the error and display a user-friendly message
        messages.error(request, "An error occurred while deleting your account.")
        return redirect("profile")

@login_required
@user_passes_test(is_superuser, login_url='index')
def user_list_view(request):
    try:
        users = User.objects.all()
        context = {
            "users": users
        }
        return render(request, "user_list.html", context)
    except Exception as e:
        # Log the error and display a user-friendly message
        messages.error(request, "An error occurred while fetching the user list.")
        return redirect("dashboard")
