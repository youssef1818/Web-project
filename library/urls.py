from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='library/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('books/', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/<int:book_id>/borrow/', views.borrow_book, name='borrow_book'),
    path('book/<int:book_id>/return/', views.return_book, name='return_book'),
    path('borrowed-books/', views.borrowed_books, name='borrowed_books'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('book/<int:book_id>/add-to-wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('book/<int:book_id>/remove-from-wishlist/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('manage-books/', views.manage_books, name='manage_books'),
    path('edit-book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete-book/<int:book_id>/', views.delete_book, name='delete_book'),
] 