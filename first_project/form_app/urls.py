from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='form_home'),
    path('form/', views.form, name='form'),
]