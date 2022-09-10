from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Order, Client


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'contacts', 'description']


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'contacts', 'description']


class OrderDeleteForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'contacts', 'description']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'address']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="User", widget=forms.TextInput(attrs={"class": "form-input"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-input"}))