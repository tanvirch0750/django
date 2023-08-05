from book.views import home, show_books, store_book
from django.urls import path

urlpatterns = [
    path('', home, name="home"),
    path('store_book/', store_book, name="store_book"),
    path('show_books/', show_books, name="show_books")
]