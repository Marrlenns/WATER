from django.contrib import admin
from django.urls import path
from clients.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', contacts),
    path('info/', info),
    path('makers/', makers_list),
    path('clients/', clients_list, name='clients-list'),
    path('client/<int:id>/', client_detail, name="client-detail"),
    path('client/update/<int:id>/', client_update, name="client-update"),
    path('order/create/', create_order, name="create-order"),
    path('order/djangoform/', order_djangoform, name="order-djangoform"),
    path('orders/', orders_list, name='orders-list'),
    path('order/<int:id>/', order_detail, name="order-detail"),
    path('order/update/<int:id>/', order_update, name="order-update"),
    path('order/delete/<int:id>/', order_delete, name="order-delete"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)