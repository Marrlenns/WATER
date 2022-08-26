from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    bottles_ordered = models.IntegerField(default=1)
    photo = models.ImageField(
        verbose_name="Фото",
        upload_to='photos',
        null=True,
        blank=True
    )

class Order(models.Model):
    created_at = models.DateTimeField(verbose_name="Дата и время создания заказа", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата и время изменения заказа", auto_now=True)
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name
