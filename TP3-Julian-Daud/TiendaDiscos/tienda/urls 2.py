from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artistas/', views.listar_artista, name='listar_artista'),
    path('discos/', views.listar_disco, name='listar_disco'),
    path('discos/buscar/', views.buscar_disco, name='buscar_disco'),
    path('clientes/', views.listar_cliente, name='listar_cliente'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path("pedido/", views.agregar_pedido, name="agregar_pedido"),
]
