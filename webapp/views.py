""" 
My Views
"""
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm


def home(request):
    """ 
    My Home View
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'webapp/index.html')

def register(request):
    """ 
    My Register View
    """
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}

    return render(request, 'webapp/register.html', context)

def login(request):
    """ 
    My Login View
    """
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data = request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    context = {"form": form}
    return render(request, 'webapp/login.html', context)

def logout(request):
    """ 
    My Logout View
    """
    if request.user.is_authenticated:
        return redirect('dashboard')

    auth.logout(request)
    return redirect("login")

@login_required(login_url="login")
def dashboard(request):
    """ 
    My Dashboard View
    """
    return render(request, 'webapp/dashboard.html')
