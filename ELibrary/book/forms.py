from django import forms
from .models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author', 'description', 'genre', 'published_at', 'isbn', 'available_copies', 'cover']
