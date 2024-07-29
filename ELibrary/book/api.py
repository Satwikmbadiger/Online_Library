from ninja import NinjaAPI
from .models import Books
from .schemas import BookSchema, BookCreateSchema, BookUpdateSchema, BookOutSchema
from django.shortcuts import get_object_or_404
from typing import List
import os, pathlib

api = NinjaAPI()

#get list of all the books
@api.get("/book", response=List[BookOutSchema])
def list_books(request):
    books = Books.objects.all()
    return books

#get a single book by id
@api.get("/book/{book_id}", response=BookOutSchema)
def get_book(request, book_id: int):
    book = get_object_or_404(Books, id=book_id)
    return book

#create a new book
@api.post("/book", response=BookOutSchema)
def create_book(request, data: BookCreateSchema):
    book = Books.objects.create(**data.dict())
    return book

#update a book by id
@api.put("/book/{book_id}", response=BookOutSchema)
def update_book(request, book_id: int, data: BookUpdateSchema):
    book = get_object_or_404(Books, id=book_id)
    for attr, value in data.dict().items():
        if value is not None:
            setattr(book, attr, value)
    book.save()
    return book

#delete a book
@api.delete("/book/{book_id}", response=dict)
def delete_book(request, book_id: int):
    book = get_object_or_404(Books, id=book_id)
    book.delete()
    return {"success": True}
