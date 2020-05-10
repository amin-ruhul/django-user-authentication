from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib import messages

from .forms import SingUpForm,EditProfile

# Create your views here.

def index(request):
    return render(request,'pages/index.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('Yor are looged in'))
            return redirect('index')
        else:
            messages.success(request,('Failed to looged in'))
            return redirect('login')

    else:
        return render(request,'pages/login.html')

def Logout(request):
    logout(request)
    messages.success(request,('You are log out'))
    return redirect('index')


def Registration(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request,user)
            messages.success(request,('You have been Register'))
            return redirect('index')
    else:
        form = SingUpForm()
    contex = {'form':form}
    return render(request,'pages/registration.html',contex)



def edit_user(request):
    if request.method == 'POST':
        form = EditProfile(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request,('You have  Edited Your Profile'))
            return redirect('index')
    else:
        form = EditProfile(instance = request.user)
    contex = {'form':form}
    return render(request,'pages/edit_user.html',contex)



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST,user = request.user)
        if form.is_valid():
            form.save()
            messages.success(request,('You have  Edited Your Password'))
            return redirect('index')
    else:
        form = PasswordChangeForm(user = request.user)
    contex = {'form':form}
    return render(request,'pages/change_password.html',contex)