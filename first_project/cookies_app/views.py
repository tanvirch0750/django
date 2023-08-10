from datetime import datetime, timedelta

from django.shortcuts import render

# Create your views here.

def home(request):
   response = render(request, './cookies/home.html')
   # response.set_cookie('name', 'tanvir', max_age=60*3) #based on second
   response.set_cookie('name', 'tanvir', expires=datetime.utcnow()+timedelta(days=7)) 
   return response


def get_cookie(request):
   name = request.COOKIES.get('name')
   print(request.COOKIES)
   return render(request, './cookies/get_cookie.html', {'name': name})


def delete_cookie(request):
   response = render(request, './cookies/del_cookie.html')
   response.delete_cookie('name')
   return response