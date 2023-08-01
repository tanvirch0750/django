from django.http import HttpResponse
from django.shortcuts import render

from .forms import contactForm


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


def DjangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./form_app/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            return render(request, './form/django_form.html', {'form': form})
    else:
        form = contactForm()
    return render(request, './form/django_form.html', {'form': form})