from ninja import Schema
from typing import Optional
from uuid import UUID

class BookOut(Schema):
    id: UUID
    title: str
    author: str
    description: str
    genre: str
    published_at: str  # Use `date` or `datetime` if preferred
    isbn: str
    available_copies: int
    cover: Optional[str] = None

class BorrowOut(Schema):
    id: UUID
    user_id: UUID
    book_id: UUID
    borrowed_at: str  # Use `datetime` if preferred
    returned_at: Optional[str] = None  # Use `datetime` if preferred
