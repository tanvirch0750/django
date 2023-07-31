from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='bootstrap_home'),
    path('about/', views.about, name='bootstrap_about'),
   
]