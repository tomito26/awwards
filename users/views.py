from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created! You can now login')
            return redirect('login')   
    else:
        form = UserRegisterForm()
    return render(request,'registration/register.html',{'form':form})

def  home(request):
    return render(request,'home.html')


def profile(request):
    return(request,'users/profile.html')