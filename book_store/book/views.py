from book.forms import BookStoreForm
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def store_book(request):
    bookForm = BookStoreForm
    return render(request, 'store_book.html', {'form': bookForm})