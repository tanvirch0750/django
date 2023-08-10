from datetime import datetime, timedelta

from django.http import HttpResponse
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


# session
def set_session(request):
   data = {
      'name': 'israk',
      'age': 23,
      'language': 'Bangla'
   }
   request.session.update(data)
   print(request.session.get_session_cookie_age())
   print(request.session.get_expiry_date())
   return render(request, './cookies/home.html')


def get_session(request):
   name = request.session.get('name')
   age = request.session.get('age')
   language = request.session.get('language')
   return render(request, './cookies/get_session.html', {'name': name, 'age': age, 'language': language})


   # if 'name' in request.session:
   #     name = request.session.get('name')
   #     request.session.modified = True
   #     return render(request, './cookies/get_session.html', {'name': name})
   # else:
   #    return HttpResponse("Your session has been expired. Kindly login again")


def delete_session(request):
   # del request.session['name'] # delete individula
   request.session.flush()
   return render(request, './cookies/del_cookie.html')