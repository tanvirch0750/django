from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
   if(request.method == 'POST'):
       name = request.POST.get('name')
       genre = request.POST.get('email')
       rating = request.POST.get('select')
       return render(request, './form/index.html', {'name': name, 'genre': genre, 'rating': rating})
   else:
       return render(request, './form/index.html')

def form(request):
    return render(request, './form/form.html')

