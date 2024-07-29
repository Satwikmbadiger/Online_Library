from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from django.utils import timezone
from typing import List
from .models import Borrow
from book.models import Books
from django.contrib.auth.models import User
from .schemas import BookOut, BorrowOut

api = NinjaAPI()

#api function to list all available books
@api.get("/books/", response=List[BookOut])
def list_available_books(request):
    books = Books.objects.filter(available_copies__gt=0)
    return books

#api function to get the details of a book
@api.get("/book/{book_id}/", response=BookOut)
def get_book_detail(request, book_id: int):
    book = get_object_or_404(Books, id=book_id)
    return book

#api function to borrow a book
@api.post("/book/{book_id}/borrow/")
def borrow_book(request, book_id: int):
    book = get_object_or_404(Books, id=book_id)
    if book.available_copies > 0:
        Borrow.objects.create(user=request.user, book=book)
        book.available_copies -= 1
        book.save()
        return {"message": "Book borrowed successfully"}
    else:
        return {"error": "No available copies"}, 400

#api function to return a book
@api.post("/book/{book_id}/return/")
def return_book(request, book_id: int):
    book = get_object_or_404(Books, id=book_id)
    borrow = Borrow.objects.filter(user=request.user, book=book, returned_at__isnull=True).first()
    if borrow:
        borrow.returned_at = timezone.now()
        book.available_copies += 1
        book.save()
        borrow.save()
        return {"message": "Book returned successfully"}
    else:
        return {"error": "No active borrow record"}, 400

#api function to get the borrow history of a user
@api.get("/user/{user_id}/history/", response=List[BorrowOut])
def user_borrow_history(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    borrows = Borrow.objects.filter(user=user)
    return borrows

#api function to get the borrow history of all users
@api.get("/history/", response=List[BorrowOut])
def superuser_borrow_history(request):
    if not request.user.is_superuser:
        return {"error": "You do not have permission to view this"}, 403
    borrows = Borrow.objects.all()
    return borrows
