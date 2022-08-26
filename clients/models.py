from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.SET_NULL, null=True, blank=True, related_name='client')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, verbose_name="Адрес")
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


class Bottle(models.Model):
    volume = models.IntegerField(default=10)
    maker = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    expired = models.BooleanField(default=False)