from django.db import models

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
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nombrels
        

class Pedido(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    disco_solicitado = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} - {self.disco_solicitado}"