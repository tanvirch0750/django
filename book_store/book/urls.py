from book.views import delete_book, edit_book, home, show_books, store_book
from django.urls import path

urlpatterns = [
    path('', home, name="home"),
    path('store_book/', store_book, name="store_book"),
    path('show_books/', show_books, name="show_books"),
    path('edit_book/<int:id>', edit_book, name="edit_book"),
    path('delete_book/<int:id>', delete_book, name="delete_book")
]