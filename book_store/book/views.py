from typing import Any, Dict

from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

# Create your views here.

# function based views
def home(request):
    return render(request, 'home.html')


def store_book(request):
    if request.method == 'POST': 
        bookForm = BookStoreForm(request.POST)
        if bookForm.is_valid():
            bookForm.save()
            return redirect('show_books')
    else:
        bookForm = BookStoreForm
    return render(request, 'store_book.html', {'form': bookForm})


def show_books(request):
    book = BookStoreModel.objects.all()
    return render(request, 'show_book.html', {'books': book})


def edit_book(request, id):
    book = BookStoreModel.objects.get(pk = id)
    bookForm = BookStoreForm(instance=book)
    if request.method == 'POST': 
        bookForm = BookStoreForm(request.POST, instance=book)
        if bookForm.is_valid():
            bookForm.save()
            return redirect('show_books')
        
    return render(request, 'store_book.html', {'form': bookForm, 'edit': True})


def delete_book(request, id):
    book = BookStoreModel.objects.get(pk = id).delete()
    return redirect("show_books")



# class based views
class HomeTemplateView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context = {'name': 'rahim', 'age': 22}
        context.update(kwargs) #update dictionary
        return context
    