""" 
My Views
"""
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from .models import Record


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
        form = LoginForm(request, data=request.POST)

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
    my_records = Record.objects.all()
    context = {'records': my_records}

    return render(request, 'webapp/dashboard.html', context=context)


@login_required(login_url="login")
def create_record(request):
    """ 
    Create a Record
    """
    form = CreateRecordForm()

    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'webapp/create-record.html', context=context)


@login_required(login_url="login")
def update_record(request, pk):
    """ 
    Update a Record
    """
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'webapp/update-record.html', context=context)


@login_required(login_url="login")
def view_record(request, pk):
    """ 
    View a Record
    """
    record = Record.objects.get(id=pk)
    context = {'record': record}
    return render(request, 'webapp/view-record.html', context=context)


@login_required(login_url="login")
def delete_record(request, pk):
    """ 
    Delete a Record
    """
    record = Record.objects.get(id=pk)
    record.delete()
    return redirect("dashboard")
