from datetime import date
from typing import Optional
from ninja import Schema

class BookSchema(Schema):
    title: str
    author: str
    description: str
    genre: str
    published_at: date
    isbn: str
    available_copies: int
    cover: Optional[str]
    created_at: Optional[date]
    updated_at: Optional[date]

class BookCreateSchema(Schema):
    title: str
    author: str
    description: str
    genre: str
    published_at: date
    isbn: str
    available_copies: int
    cover: Optional[str]

class BookUpdateSchema(Schema):
    title: Optional[str]
    author: Optional[str]
    description: Optional[str]
    genre: Optional[str]
    published_at: Optional[date]
    isbn: Optional[str]
    available_copies: Optional[int]
    cover: Optional[str]

class BookOutSchema(Schema):
    id: int
    title: str
    author: str
    description: str
    genre: str
    published_at: date
    isbn: str
    available_copies: int
    cover: Optional[str]
    created_at: date
    updated_at: date
