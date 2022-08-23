from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    bottles_ordered = models.IntegerField(default=1)
    photo = models.ImageField(
        verbose_name="Фото",
        upload_to='media/photos',
        null=True,
        blank=True
    )
