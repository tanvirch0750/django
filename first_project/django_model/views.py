from django.http import HttpResponse
from django.shortcuts import redirect, render

from . import models


# Create your views here.
def home(request):
   student = models.Student.objects.all()
   return render(request, './home.html', {'students': student})

def delete_student(request, roll):
   std = models.Student.objects.get(pk = roll).delete()
   return redirect("django_model")