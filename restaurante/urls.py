from django.urls import path
from . import views

urlpatterns = [
    path('guia/', views.detalhe_restaurantes, name='restaurantes'),
    path('clientes/', views.historico_clientes, name='clientes'),
]