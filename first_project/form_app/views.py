from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
   if(request.method == 'POST'):
       name = request.POST.get('name')
       email = request.POST.get('email')
       return render(request, './form/index.html', {'name': name, 'email': email})
   else:
       return render(request, './form/index.html')

def form(request):
    return render(request, './form/form.html')

