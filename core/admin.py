from django.contrib import admin
from .models import Bottle, BottlesCount


class BottleAdmin(admin.ModelAdmin):
    model = Bottle
    list_display = ['maker', 'volume', 'expired']
    list_editable = ['expired']
    fields = ['maker', 'volume', 'description', 'expired']


admin.site.register(Bottle, BottleAdmin)


class BottleCountAdmin(admin.ModelAdmin):
    model = BottlesCount
    list_display = ['order', 'bottle', 'count']
    list_editable = ['count']
    fields = ['bottle', 'count', 'order']


admin.site.register(BottlesCount, BottleCountAdmin)