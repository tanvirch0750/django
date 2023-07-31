from django.http import HttpResponse
from django.shortcuts import render


def courses(request):
   return HttpResponse('''
                       <h1>Hello, this is second app courses page</h1>
                       <a href="/">App Home</a>
                       <a href="/first_app/about/">About</a>
                       <a href="/first_app/contact/">Contact</a>
                       <a href="/second_app/feedback/">feedback</a>
                       <a href="/second_app/courses/">courses</a>
                       <a href="/bootstrap_app/">Bootstrap</a>
                       ''')


def feedback(request):
   return HttpResponse('''
                       <h1>Hello, this is second app feedback page</h1>
                       <a href="/">App Home</a>
                       <a href="/first_app/about/">About</a>
                       <a href="/first_app/contact/">Contact</a>
                       <a href="/second_app/feedback/">feedback</a>
                       <a href="/second_app/courses/">courses</a>
                       <a href="/bootstrap_app/">Bootstrap</a>
                       ''')
