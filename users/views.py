from django.shortcuts import render
from .forms import *


def orders(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = OrdersForm()
    return render(request, 'dashboard/orders.html', {'form': form})

def home(request):
    return render(request, 'dashboard/home.html')

def history(request):
    return render(request, 'dashboard/history.html')

def geo(request):
    return render(request, 'dashboard/geo.html')

def inter(request):
    return render(request, 'dashboard/inter.html')

def about(request):
    return render(request, 'dashboard/about.html')

def vacancies(request):
    vacancies = Vacancies.objects.all()
    return render(request, 'dashboard/vacancies.html', {'vacancies': vacancies})

def contacts(request):
    contacts = Contacts.objects.all()
    return render(request, 'dashboard/contacts.html', {'contacts': contacts})

def menu(request):
    menu = Menu.objects.all()
    return render(request, 'dashboard/menu.html', {'menu': menu})