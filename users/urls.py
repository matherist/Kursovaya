from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("orders", views.orders, name='orders'),
    path("contacts", views.contacts, name='contacts'),
    path("vacancies", views.vacancies, name='vacancies'),
    path("menu", views.menu, name='menu'),
    path("about", views.about, name='about'),
    path("geo", views.geo, name='geo'),
    path("inter", views.inter, name='inter'),
    path('history', views.history, name='history'),
]