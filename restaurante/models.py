from django.db import models

# Create your models here.

class Restaurante(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=200)
    capacidade = models.IntegerField()

    def __str__(self):
        return self.nome

class Prato(models.Model):
    nome = models.CharField(max_length=100)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='pratos')

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Reserva(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    numero_pessoas = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='reservas')

    def __str__(self):
        return f"Reserva de {self.cliente.nome} a {self.data}"