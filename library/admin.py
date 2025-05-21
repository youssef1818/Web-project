from django.contrib import admin
from .models import Book, BorrowedBook, WishList

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'available_copies', 'publication_date')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('available_copies', 'publication_date')
    ordering = ('title',)

@admin.register(BorrowedBook)
class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrow_date', 'return_date', 'is_returned')
    list_filter = ('is_returned', 'borrow_date', 'return_date')
    search_fields = ('user__username', 'book__title')
    ordering = ('-borrow_date',)

@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'added_date')
    list_filter = ('added_date',)
    search_fields = ('user__username', 'book__title')
    ordering = ('-added_date',)
