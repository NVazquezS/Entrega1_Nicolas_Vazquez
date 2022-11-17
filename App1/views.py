from django.shortcuts import render
from App1.models import *

# Create your views here.
def inicio(request):

        
    return render(request, "app1/index.html")

def peliculas(request):
    peliculas = Peliculas.objects.all()
        
    return render(request, "app1/Peliculas.html", {"peliculas":peliculas})


def series(request):
    series = Series.objects.all()
        
    return render(request, "app1/Series.html", {"series":series})

def juegos(request):
    juegos = Juegos.objects.all()
        
    return render(request, "app1/Juegos.html", {"juegos":juegos})

def agregar_peliculas(request):
        
    if request.method == "POST":
        nombre_pelicula = request.POST["nombre"]
        genero_pelicula = request.POST["genero"]
        plataforma_pelicula = request.POST["plataforma"]
        
        pelicula = Peliculas(nombre=nombre_pelicula, genero=genero_pelicula, plataforma=plataforma_pelicula)
        pelicula.save()
    return render(request, "app1/Agregar_Peliculas.html")

def agregar_serie(request):
        
    if request.method == "POST":
        nombre_serie = request.POST["nombre"]
        genero_serie = request.POST["genero"]
        plataforma_serie = request.POST["plataforma"]
        temporadas_serie = request.POST["temporadas"]
        
        serie = Series(nombre=nombre_serie, genero=genero_serie, plataforma=plataforma_serie, temporadas=temporadas_serie)
        serie.save()
    return render(request, "app1/Agregar_Serie.html")

def agregar_juego(request):
        
    if request.method == "POST":
        nombre_juego = request.POST["nombre"]
        genero_juego = request.POST["genero"]
        consola_juego = request.POST["consola"]
        
        
        juego = Juegos(nombre=nombre_juego, genero=genero_juego, consola=consola_juego)
        juego.save()
    return render(request, "app1/Agregar_Juego.html")


def buscar_pelicula(request):
    
    return render(request, "App1/busqueda_pelicula.html" )

def resultados_busqueda_pelicula(request):
    nombre_pelicula = request.GET["nombre"]
    peliculas = Peliculas.objects.filter(nombre__icontains=nombre_pelicula)
    return render(request, "App1/resultados_busqueda_pelicula.html", {"peliculas":peliculas})

def buscar_series(request):
    
    return render(request, "App1/busqueda_series.html" )

def resultados_busqueda_series(request):
    nombre_serie = request.GET["nombre"]
    series = Series.objects.filter(nombre__icontains=nombre_serie)
    return render(request, "App1/resultados_busqueda_series.html", {"series":series})

def buscar_juegos(request):
    
    return render(request, "App1/busqueda_juegos.html" )

def resultados_busqueda_juegos(request):
    nombre_juego = request.GET["nombre"]
    juegos = Juegos.objects.filter(nombre__icontains=nombre_juego)
    return render(request, "App1/resultados_busqueda_juegos.html", {"juegos":juegos})