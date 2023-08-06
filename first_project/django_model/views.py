from django.http import HttpResponse
from django.shortcuts import redirect, render
from django_model.forms import StudentForm

from . import models


# Create your views here.
def home(request):
   student = models.Student.objects.all()
   
   ## one to many / many to many
   # studnet list for one teacher
   teacher = models.Teacher.objects.get(name='Shakib')
   students2 = teacher.student.all()
   
   for stud in students2:
      print(stud.name, stud.roll, stud.class_name)
   
   # teacher list for one student
   students3 = models.Student2.objects.get(name='std2')
   teachers = students3.teachers.all()
   
   for teach in teachers:
      print(teach.name, teach.subject, teach.mobile)
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