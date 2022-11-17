from django.urls import path
from App1.views import *

urlpatterns = [

    path('inicio/', inicio, name="Entrega1-inicio"),
    path('peliculas/', peliculas, name="Entrega1-peliculas"),
    path('series/', series, name="Entrega1-series"),
    path('juegos/', juegos, name="Entrega1-juegos"),
    path('peliculas/agregar/', agregar_peliculas, name="Entrega1-agregar-peliculas"),
    path('series/agregar/', agregar_serie, name="Entrega1-agregar-serie"),
    path('juegos/agregar/', agregar_juego, name="Entrega1-agregar-juego"),
    path('peliculas/buscar/', buscar_pelicula, name="Entrega1-buscar-pelicula"),
    path('peliculas/buscar/resultados', resultados_busqueda_pelicula, name="Entrega1-buscar-pelicula-resultados"),
    path('series/buscar/', buscar_series, name="Entrega1-buscar-series"),
    path('series/buscar/resultados', resultados_busqueda_series, name="Entrega1-buscar-series-resultados"),
    path('juegos/buscar/', buscar_juegos, name="Entrega1-buscar-juegos"),
    path('juegos/buscar/resultados', resultados_busqueda_juegos, name="Entrega1-buscar-juegos-resultados"),
]
