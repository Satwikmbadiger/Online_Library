from django.urls import path
from .views import signup_view, signin_view, signout_view, profile_view, update_profile_view, delete_account_view, user_list_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('signin/', signin_view, name='signin'),
    path('signout/', signout_view, name='signout'),
    path('profile/', profile_view, name='profile'),
    path('update/', update_profile_view, name='update_profile'),
    path('delete/', delete_account_view, name='delete_account'),
    path('users/', user_list_view, name='user_list'), 
]
