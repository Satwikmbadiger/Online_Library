from django.urls import path
from .views import book_list, book_detail_admin_view, book_create, book_update, book_delete

urlpatterns = [
    path('book_list/', book_list, name='book_list'),
    path('add/', book_create, name='add_book'),  
     path('admin/book/<uuid:book_id>/', book_detail_admin_view, name='book_detail_admin'),
    path('<int:book_id>/update/', book_update, name='update_book'),
    path('<int:book_id>/delete/', book_delete, name='delete_book'),
]
