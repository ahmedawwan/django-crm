""" 
My Forms
"""
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Record


class CreateUserForm(UserCreationForm):
    """ 
    Register/Create a User
    """
    class Meta:
        """ 
        Meta class
        """
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    """ 
    Login User
    """
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class CreateRecordForm(forms.ModelForm):
    """ 
    Create A Record Form
    """
    class Meta:
        """ 
        Meta class
        """
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone',
                  'address', 'city', 'province', 'country',]


class UpdateRecordForm(forms.ModelForm):
    """ 
    Update A Record Form
    """
    class Meta:
        """ 
        Meta class
        """
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone',
                  'address', 'city', 'province', 'country',]
