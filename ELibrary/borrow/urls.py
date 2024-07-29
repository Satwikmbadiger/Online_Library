from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.available_books_view, name='available_books'),
    path('book/<int:book_id>/', views.book_detail_view, name='book_detail'),
    path('history/', views.user_borrow_history, name='user_borrow_history'),
    path('admin/history/', views.superuser_borrow_history, name='superuser_borrow_history'),
]
