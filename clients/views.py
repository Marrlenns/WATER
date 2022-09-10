from django.shortcuts import render, HttpResponse
from .models import Client, Order
from core.models import Bottle
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import OrderForm, OrderUpdateForm, OrderDeleteForm, ClientForm


def contacts(request):
    return render(request, "contacts.html")


def info(request):
    return render(request, "info.html")


# def clients_list(request):
#     context = {}
#     bottles_list = Client.objects.all()
#     context["clients_list"] = bottles_list
#     html_page = render(request, 'clients.html', context)
#     return html_page


class ClientListView(ListView):
    model = Client
    template_name = 'clients.html'


# def makers_list(request):
#     context = {}
#     bottles_list = Bottle.objects.all()
#     context["bottles_list"] = bottles_list
#     html_page = render(request, 'makers.html', context)
#     return html_page


class MakersListView(ListView):
    model = Bottle
    template_name = 'makers.html'

# def client_detail(request, id):
#     context = {
#         "client": Client.objects.get(id=id)
#     }
#     return render(request, "client_info.html", context)


class ClientDetailView(DetailView):
    model = Client
    template_name = "client_info.html"

# def client_update(request, id):
#     context = {}
#     client_object = Client.objects.get(id=id)
#     if request.method == 'POST':
#         form = ClientForm(request.POST, instance=client_object)
#         if form.is_valid():
#             form.save()
#
#     context['form'] = ClientForm(instance=client_object)
#     return render(request, 'client_update.html', context)


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'client_update.html'
    fields = ['name', 'address']
    success_url = '/clients/'


# def orders_list(request):
#     context = {}
#     orders_list = Order.objects.all()
#     context["orders_list"] = orders_list
#     return render(request, 'orders.html', context)


class OrdersListView(ListView):
    model = Order
    template_name = 'orders.html'


# def order_detail(request, id):
#     context = {
#         "order": Order.objects.get(id=id)
#     }
#     return render(request, "order_info.html", context)


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_info.html'


# def create_order(request):
#     if request.method == 'POST':
#         data = request.POST
#         order = Order()
#         order.name = data['name']
#         order.contacts = data['contacts']
#         order.description = data['description']
#         order.save()
#         return HttpResponse("Форма обработана")
#     return render(request, 'order_form.html')


class CreateOrderView(View):
    def post(self, request):
        data = request.POST
        order = Order()
        order.name = data["name"]
        order.contacts = data["contacts"]
        order.description = data["description"]
        order.save()
        return HttpResponse("Форма обработана")

    def get(self, request):
        return render(request, 'order_form.html')


# def order_update(request, id):
#     context = {}
#     order_object = Order.objects.get(id=id)
#     if request.method == 'POST':
#         order = OrderUpdateForm(request.POST, instance=order_object)
#         if order.is_valid():
#             order_object.save()
#             return HttpResponse("Ваши изменения сохранились")
#
#     context['order'] = OrderUpdateForm(instance=order_object)
#     return render(request, 'order_update.html', context)


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_update.html'
    fields = ['name', 'contacts', 'description']
    success_url = '/order/'


# def order_djangoform(request):
#     context = {}
#     if request.method == 'POST':
#         order_form = OrderForm(request.POST)
#         if order_form.is_valid():
#             order_form.save()
#             return HttpResponse("Форма обработана")
#         return HttpResponse("Данные неправильно введены")
#     context['order_form'] = OrderForm()
#     return render(request, 'order_djangoform.html', context)


class CreateOrderDjangoView(CreateView):
    model = Order
    template_name = 'order_djangoform.html'
    fields = ['name', 'contacts', 'description']
    success_url = '/order/'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['our_number'] = 7
    #     return context


class CreateOrderView(View):
    def post(self, request):
        data = request.POST
        order = Order()
        order.name = data["name"]
        order.address = data["address"]
        order.contacts = data["contacts"]
        order.descriptions = data["description"]
        order.save()
        return HttpResponse("Форма обработана", )

    def get(self, request):
        return render(request, 'order_form.html')

# def order_delete(request, id):
#     context = {}
#     order_object = Order.objects.get(id=id)
#     if request.method == 'POST':
#         order_object.delete()
#         order = OrderDeleteForm(request.POST, instance=order_object)
#         return HttpResponse("Ваш заказ был удален")
#
#     context['order'] = OrderDeleteForm(instance=order_object)
#     return render(request, 'order_delete.html', context)


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_delete.html'
    fields = ['name', 'contacts', 'description']
    success_url = '/order/'