from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('pass_change/', views.pass_change, name='pass_change'),
    path('pass_change2/', views.pass_change2, name='pass_change2'),
    path('profile/', views.profile, name='profile')
]