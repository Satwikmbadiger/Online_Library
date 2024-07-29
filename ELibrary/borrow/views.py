from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseBadRequest
from book.models import Books as Book
from .models import Borrow
from django.utils import timezone

@login_required
def available_books_view(request):
    try:
        # Fetch books with available copies
        books = Book.objects.filter(available_copies__gt=0)
        return render(request, 'borrow/available_books.html', {'books': books})
    except Exception as e:
        # Log the error and display a user-friendly message
        return render(request, 'error.html', {'error_code': 500, 'error_message': 'An error occurred while fetching available books.'})

@login_required
def book_detail_view(request, book_id):
    try:
        # Get the book object or return a 404 error if not found
        book = get_object_or_404(Book, id=book_id)
        user_borrowed = Borrow.objects.filter(user=request.user, book=book, returned_at__isnull=True).exists()

        if request.method == "POST":
            if 'borrow' in request.POST:
                if book.available_copies > 0:
                    Borrow.objects.create(user=request.user, book=book)
                    book.available_copies -= 1
                    book.save()
                    return redirect('book_detail', book_id=book.id)
                else:
                    return render(request, 'borrow/book_detail.html', {'book': book, 'error': 'No available copies'})
            elif 'return' in request.POST:
                borrow = Borrow.objects.filter(user=request.user, book=book, returned_at__isnull=True).first()
                if borrow:
                    borrow.returned_at = timezone.now()
                    book.available_copies += 1
                    book.save()
                    borrow.save()
                    return redirect('book_detail', book_id=book.id)
                else:
                    return render(request, 'borrow/book_detail.html', {'book': book, 'error': 'No active borrow record'})
        
        return render(request, 'borrow/book_detail.html', {'book': book, 'user_borrowed': user_borrowed})
    except Exception as e:
        # Log the error and display a user-friendly message
        return render(request, 'error.html', {'error_code': 500, 'error_message': 'An error occurred while processing the book details.'})

@login_required
def user_borrow_history(request):
    try:
        # Fetch borrow history for the logged-in user
        borrows = Borrow.objects.filter(user=request.user)
        return render(request, 'borrow/borrow_history.html', {'borrows': borrows})
    except Exception as e:
        # Log the error and display a user-friendly message
        return render(request, 'error.html', {'error_code': 500, 'error_message': 'An error occurred while fetching your borrow history.'})

@user_passes_test(lambda u: u.is_superuser)
def superuser_borrow_history(request):
    try:
        # Fetch all borrow records for superusers
        borrows = Borrow.objects.all()
        return render(request, 'borrow/superuser_borrow_history.html', {'borrows': borrows})
    except Exception as e:
        # Log the error and display a user-friendly message
        return render(request, 'error.html', {'error_code': 500, 'error_message': 'An error occurred while fetching all borrow records.'})
