from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="django_model"),
    path('delete/<int:roll>', views.delete_student, name="delete_student"),
     path('form_model/', views.model_form, name="form_model"),
]