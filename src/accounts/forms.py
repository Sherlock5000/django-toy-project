from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django import forms
from .models import Order


class OrderForm(ModelForm):
    '''
    OrderForm for creating forms
    '''
    class Meta:
        model = Order
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    '''
    A form that creates a user, with no privileges, from the given username,
    email id, and password.
    '''
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
