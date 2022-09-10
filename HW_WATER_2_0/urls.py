from django.contrib import admin
from django.urls import path
from clients.views import *
from django.conf import settings
from django.conf.urls.static import static
from clients.forms import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', contacts),
    path('', info),
    path('makers/', MakersListView.as_view()),
    path('clients/', ClientListView.as_view(), name='clients-list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name="client-detail"),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name="client-update"),
    path('order/create/', CreateOrderView.as_view(), name="create-order"),
    # path('order/create/', CreateOrderDjangoView.as_view(), name="order-djangoform"),
    path('orders/', OrdersListView.as_view(), name='orders-list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name="order-detail"),
    path('order/update/<int:pk>/', OrderUpdateView.as_view(), name="order-update"),
    path('order/delete/<int:pk>/', OrderDeleteView.as_view(), name="order-delete"),
    path('register/', register, name="register"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout-user")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)