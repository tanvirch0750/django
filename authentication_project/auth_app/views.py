from django.contrib import messages
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       SetPasswordForm)
from django.shortcuts import redirect, render

from .forms import ChangeUserData, RegisterForm

# Create your views here.

def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request, user)
                    return redirect('profile')                  
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
         return redirect('profile')


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created successfully')
                form.save()
                return redirect('login')
            else:
                messages.error(request, 'Account creation failed')
        else:
            form = RegisterForm(request.user)
        return render(request, 'signup.html', {'form': form})
    else:
        return redirect('profile')


def profile(request):
    # change_user_data(request)
     if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
            else:
                messages.error(request, 'Account updation failed')
        else:
            form = ChangeUserData(instance = request.user)
        return render(request, 'profile.html', {'form': form})
     else:
        return redirect('login')
 
 
def home(request):
     return render(request, 'home.html')
 
def user_logout(request):
    logout(request)
    return redirect('login')



def pass_change(request):
     if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data = request.POST)
            
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
            
        else:
            form = PasswordChangeForm(user=request.user)
            
        return render(request, 'passChange.html', {'form': form})
     else:
        return redirect('login')
    
    
def pass_change2(request):
     if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data = request.POST)
            
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
            
        else:
            form = SetPasswordForm(user=request.user)
            
        return render(request, 'passChange.html', {'form': form})
     else:
        return redirect('login')
    
    
    
def change_user_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
            else:
                messages.error(request, 'Account updation failed')
        else:
            form = ChangeUserData(instance = request.user)
        return render(request, 'profile.html', {'form': form})
    else:
        return redirect('login')
        
