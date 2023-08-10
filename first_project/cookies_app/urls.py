from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='cookies_home'), 
    path('get/', views.get_cookie, name='get_cookies_home'), 
    path('delete/', views.delete_cookie, name='delete_cookies_home'), 
]