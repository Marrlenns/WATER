from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User
from django import forms

class Client(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.SET_NULL, null=True, blank=True, related_name='client')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, verbose_name="Адрес", null=True, blank=True)
    active = models.BooleanField(default=True)
    bottles_ordered = models.IntegerField(default=1, verbose_name="Количество бутылок")
    photo = models.ImageField(
        verbose_name="Фото",
        upload_to='photos',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(to=Client, null=True, blank=True, on_delete=models.SET_NULL, related_name='order')
    created_at = models.DateTimeField(verbose_name="Дата и время создания заказа", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата и время изменения заказа", auto_now=True)
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class UserRegisterForm(UserCreationForm):
    name = forms.CharField(label = 'Имя')
    username = forms.CharField(label = "Никнейм", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label = "Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label = "Повторите пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('name', 'username', 'password1', 'password2')

