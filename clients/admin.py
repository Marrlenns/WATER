from django.contrib import admin

from .models import Client, Order

# admin.site.register(Client)


class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ['name', 'address', 'bottles_ordered', 'user']
    list_editable = ['bottles_ordered']
    fields = ['user', 'name', 'address', 'active', 'bottles_ordered', 'photo']
    # readonly_fields = ['bottles_ordered']


admin.site.register(Client, ClientAdmin)


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['name', 'contacts', 'created_at', 'finished']
    list_editable = ['contacts', 'finished']
    fields = ['name', 'contacts', 'created_at', 'updated_at', 'description', 'finished']
    readonly_fields = ['contacts', 'created_at', 'updated_at']


admin.site.register(Order, OrderAdmin)