from book.views import home, store_book
from django.urls import path

urlpatterns = [
    path('', home, name="home"),
    path('store_book/', store_book, name="store_book")
]