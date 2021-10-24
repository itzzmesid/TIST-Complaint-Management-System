from django.contrib.auth import forms, models
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Account



class CreateUserForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['email', 'username', 'empid', 'phone', 'dept', 'password1', 'password2']
