from django.shortcuts import render

# Create your views here.
from .models import Restaurante, Cliente

def detalhe_restaurantes(request):
    restaurantes = Restaurante.objects.prefetch_related('pratos', 'reservas__cliente')
    return render(request, 'restaurantes.html', {'restaurantes': restaurantes})

def historico_clientes(request):
    clientes = Cliente.objects.prefetch_related('reservas__restaurante')
    return render(request, 'clientes.html', {'clientes': clientes})