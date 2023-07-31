from django.http import HttpResponse
from django.shortcuts import render

data = [
  {"id": 1, "course": "c", "teacher": "rahim"},
  {"id": 2, "course": "java", "teacher": "john"},
  {"id": 3, "course": "python", "teacher": "alice"},
  {"id": 4, "course": "javascript", "teacher": "bob"},
  {"id": 5, "course": "html", "teacher": "emma"},
  {"id": 6, "course": "css", "teacher": "michael"},
  {"id": 7, "course": "php", "teacher": "olivia"},
  {"id": 8, "course": "sql", "teacher": "william"},
  {"id": 9, "course": "ruby", "teacher": "sophia"},
  {"id": 10, "course": "c++", "teacher": "james"}
]

# Create your views here.
def home(request):
   return render(request, './bootstrap/index.html', {"courses": data})
