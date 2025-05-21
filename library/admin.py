from django.contrib import admin
from .models import Book, BorrowedBook, WishList, UserProfile

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'available_copies', 'has_cover')
    list_filter = ('available_copies', 'publication_date')
    search_fields = ('title', 'author', 'isbn')
    readonly_fields = ('created_at',)

    def has_cover(self, obj):
        return bool(obj.cover_image)
    has_cover.boolean = True
    has_cover.short_description = 'Has Cover Image'

@admin.register(BorrowedBook)
class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrow_date', 'is_returned')
    list_filter = ('is_returned', 'borrow_date')
    search_fields = ('user__username', 'book__title')

@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'added_date')
    list_filter = ('added_date',)
    search_fields = ('user__username', 'book__title')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_librarian', 'date_joined')
    list_filter = ('is_librarian', 'date_joined')
    search_fields = ('user__username', 'user__email')
