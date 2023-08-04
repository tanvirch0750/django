from django.http import HttpResponse
from django.shortcuts import redirect, render
from django_model.forms import StudentForm

from . import models


# Create your views here.
def home(request):
   student = models.Student.objects.all()
   return render(request, './home.html', {'students': student})

def delete_student(request, roll):
   std = models.Student.objects.get(pk = roll).delete()
   return redirect("django_model")

def model_form(request):
   if request.method == 'POST':
      form = StudentForm(request.POST)
      if form.is_valid():
         # form.save(commit=False)
         form.save()
         print(form.cleaned_data)
   
   else :
     form = StudentForm()
   return render(request, './form_model.html', {'form': form})