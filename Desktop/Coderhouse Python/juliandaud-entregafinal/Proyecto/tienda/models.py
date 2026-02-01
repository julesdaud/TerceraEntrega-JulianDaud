from django.db import models
from django import forms
from django.contrib.auth.models import User


class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Disco(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    año_lanzamiento = models.IntegerField()
    genero = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.titulo} - {self.artista.nombre}"

class Pedido(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("procesado", "Procesado")
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    disco_solicitado = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField(default=1)  # <--- Agregamos esto
    estado = models.CharField(max_length=10, choices=ESTADOS, default="pendiente")
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.disco_solicitado} ({self.usuario.username})"