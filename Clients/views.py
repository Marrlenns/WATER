from django.shortcuts import render, HttpResponse
from .models import Client

def contacts(request):
    return render(request, "contacts.html")

def info(request):
    return render(request, "info.html")

def clients_list(request):
    context = {}
    bottles_list = Client.objects.all()
    context["clients_list"] = bottles_list
    html_page = render(request, 'clients.html', context)
    return html_page

