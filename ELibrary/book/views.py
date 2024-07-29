from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from .models import Books
from .forms import BookForm

# Function to check if the user is an admin
def is_superuser(user):
    return user.is_superuser

# View to list all the books
@user_passes_test(is_superuser)
@login_required
def book_list(request):
    try:
        books = Books.objects.all()
        return render(request, 'book/book_list.html', {'books': books})
    except Exception as e:
        # Log the error and display a user-friendly message
        return render(request, 'error.html', {'error_code': 500, 'error_message': 'An error occurred while retrieving the book list.'})

# View to show the details of a book
@user_passes_test(is_superuser)
@login_required
def book_detail_admin_view(request, book_id):
    try:
        book = get_object_or_404(Books, id=book_id)
        return render(request, 'book/admin_book_detail.html', {'book': book})
    except Exception as e:
        # Log the error and display a user-friendly message
        return render(request, 'error.html', {'error_code': 500, 'error_message': 'An error occurred while retrieving the book details.'})

# View to create a new book
@user_passes_test(is_superuser)
@login_required
def book_create(request):
    try:
        if request.method == 'POST':
            form = BookForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('book_list')
            else:
                # If the form is invalid, render the form with errors
                return render(request, 'book/add_book.html', {'form': form})
        else:
            form = BookForm()
        return render(request, 'book/add_book.html', {'form': form})
    except Exception as e:
        # Log the error and display a user-friendly message
        return render(request, 'error.html', {'error_code': 500, 'error_message': 'An error occurred while creating the book.'})

# View to update a book
@user_passes_test(is_superuser)
@login_required
def book_update(request, book_id):
    try:
        book = get_object_or_404(Books, id=book_id)
        if request.method == 'POST':
            form = BookForm(request.POST, request.FILES, instance=book)
            if form.is_valid():
                form.save()
                return redirect('book_list')
            else:
                # If the form is invalid, render the form with errors
                return render(request, 'book/update_book.html', {'form': form})
        else:
            form = BookForm(instance=book)
        return render(request, 'book/update_book.html', {'form': form})
    except Exception as e:
        # Log the error and display a user-friendly message
        return render(request, 'error.html', {'error_code': 500, 'error_message': 'An error occurred while updating the book.'})

# View to delete a book
@user_passes_test(is_superuser)
@login_required
def book_delete(request, book_id):
    try:
        book = get_object_or_404(Books, id=book_id)
        if request.method == 'POST':
            book.delete()
            return redirect('book_list')
        return render(request, 'book/delete_book.html', {'book': book})
    except Exception as e:
        # Log the error and display a user-friendly message
        return render(request, 'error.html', {'error_code': 500, 'error_message': 'An error occurred while deleting the book.'})
