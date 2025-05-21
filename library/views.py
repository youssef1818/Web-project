from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .forms import UserRegistrationForm, BookForm
from .models import Book, BorrowedBook, WishList
from django.utils import timezone

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'library/register.html', {'form': form})

def home(request):
    # Get the latest 6 books for the home page
    latest_books = Book.objects.all().order_by('-created_at')[:6]
    return render(request, 'library/home.html', {'books': latest_books})

def book_list(request):
    # Get search query
    query = request.GET.get('q')
    if query:
        # Search in title, author, and description
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(description__icontains=query)
        ).order_by('title')
    else:
        # If no search query, get all books
        books = Book.objects.all().order_by('title')
    return render(request, 'library/book_list.html', {'books': books})

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    is_borrowed = BorrowedBook.objects.filter(
        user=request.user,
        book=book,
        is_returned=False
    ).exists()
    is_wishlisted = WishList.objects.filter(
        user=request.user,
        book=book
    ).exists()
    return render(request, 'library/book_detail.html', {
        'book': book,
        'is_borrowed': is_borrowed,
        'is_wishlisted': is_wishlisted
    })

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.available_copies > 0:
        BorrowedBook.objects.create(user=request.user, book=book)
        book.available_copies -= 1
        book.save()
        messages.success(request, f'You have successfully borrowed {book.title}')
    else:
        messages.error(request, 'This book is currently not available')
    return redirect('book_detail', book_id=book_id)

@login_required
def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    borrowed = get_object_or_404(
        BorrowedBook,
        user=request.user,
        book=book,
        is_returned=False
    )
    borrowed.is_returned = True
    borrowed.save()
    book.available_copies += 1
    book.save()
    messages.success(request, f'You have successfully returned {book.title}')
    return redirect('borrowed_books')

@login_required
def borrowed_books(request):
    borrowed = BorrowedBook.objects.filter(
        user=request.user,
        is_returned=False
    )
    return render(request, 'library/borrowed_books.html', {
        'borrowed_books': borrowed
    })

@login_required
def wishlist(request):
    wishlist = WishList.objects.filter(user=request.user)
    return render(request, 'library/wishlist.html', {'wishlist': wishlist})

@login_required
def add_to_wishlist(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    WishList.objects.get_or_create(user=request.user, book=book)
    messages.success(request, f'{book.title} has been added to your wishlist')
    return redirect('book_detail', book_id=book_id)

@login_required
def remove_from_wishlist(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    WishList.objects.filter(user=request.user, book=book).delete()
    messages.success(request, f'{book.title} has been removed from your wishlist')
    return redirect('wishlist')
