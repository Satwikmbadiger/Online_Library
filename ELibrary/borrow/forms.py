from django import forms
from uuid import UUID

class BorrowForm(forms.Form):
    user_id = forms.UUIDField(label="User ID")
    book_id = forms.UUIDField(label="Book ID")

class ReturnForm(forms.Form):
    borrow_id = forms.UUIDField(label="Borrow ID")
