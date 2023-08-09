from typing import Any, Dict, List

from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from django.views.generic.edit import CreateView, FormView

# Create your views here.

# function based views
def home(request):
    return render(request, 'home.html')

############################################


def store_book(request):
    if request.method == 'POST': 
        bookForm = BookStoreForm(request.POST)
        if bookForm.is_valid():
            bookForm.save()
            return redirect('show_books')
    else:
        bookForm = BookStoreForm
    return render(request, 'store_book.html', {'form': bookForm})

##########################################################


def show_books(request):
    book = BookStoreModel.objects.all()
    return render(request, 'show_book.html', {'books': book})

###############################################################


def edit_book(request, id):
    book = BookStoreModel.objects.get(pk = id)
    bookForm = BookStoreForm(instance=book)
    if request.method == 'POST': 
        bookForm = BookStoreForm(request.POST, instance=book)
        if bookForm.is_valid():
            bookForm.save()
            return redirect('show_books')
        
    return render(request, 'store_book.html', {'form': bookForm, 'edit': True})


################################################################################


def delete_book(request, id):
    book = BookStoreModel.objects.get(pk = id).delete()
    return redirect("show_books")

#################################################################################
#################################################################################
######################  Class based views  ######################################
#################################################################################
#################################################################################


class HomeTemplateView(TemplateView): # Home
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context = {'name': 'rahim', 'age': 22}
        context.update(kwargs) #update dictionary
        return context
    
    
###########################################################################


class BookListView(ListView): # show books - list view
    model = BookStoreModel
    template_name = 'show_book.html'
    context_object_name = 'books' 
    
    # def get_queryset(self) -> QuerySet[Any]:
    #     return BookStoreModel.objects.filter(category='Thriller')
    
    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context = {'books': BookStoreModel.objects.all().order_by('author')}
    #     return context
    
    #ordering = ['-id']
    ordering = ['id']
    
    
    # def get_template_names(self) -> List[str]:
    #     if self.request.user.is_superuser:
    #         template_name = 'superbooks.html'
    #     elif self.request.user.is_staff:
    #         template_name = 'stuffbook.html'
    #     else:
    #         template_name = self.template_name
    #     return [template_name]
    
    
###########################################################################

class BookDetailsView(DetailView): # show book details
    model = BookStoreModel
    template_name = 'book_details.html'
    context_object_name = 'book'
    
    pk_url_kwarg = 'id'
    
    
###########################################################################

# class BookFormView(FormView): # store book
#     template_name =  'store_book.html'
#     form_class = BookStoreForm
#     success_url = reverse_lazy('show_books')
    
#     def form_valid(self, form: Any) -> HttpResponse:
#         form.save()
#         return redirect('show_books')

# another method
class BookFormView(CreateView): # store book
    model = BookStoreModel
    template_name =  'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('show_books')
    
    
###########################################################################


class BookUpdateView(UpdateView): # update book
    model = BookStoreModel
    template_name =  'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('show_books')
    
    
###########################################################################

class BookDeleteView(DeleteView):
    model = BookStoreModel
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('show_books')
    
    

    
    
    

    
    
    

            
    
    

    