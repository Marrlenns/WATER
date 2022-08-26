# Generated by Django 4.1 on 2022-08-26 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0002_client_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания заказа')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения заказа')),
                ('description', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('contacts', models.CharField(max_length=255)),
            ],
        ),
    ]
