from django.db import models

# Create your models here.

class Peliculas(models.Model):
    nombre = models.CharField(max_length=70)
    genero = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=50)
    
    
class Series(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=50)
    temporadas = models.IntegerField()
    
class Juegos(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    consola = models.CharField(max_length=50)
    