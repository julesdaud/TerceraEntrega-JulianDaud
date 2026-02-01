from django.urls import path
from . import views

app_name = "tienda"

urlpatterns = [
    
    path("", views.home, name="home"),

    path("artistas/", views.listar_artista, name="listar_artista"),
    path("clientes/", views.listar_cliente, name="listar_cliente"),
    

    path("discos/", views.DiscoListView.as_view(), name="listar_disco"),
    path("discos/<int:pk>/", views.DiscoDetailView.as_view(), name="detalle_disco"),
    path("discos/crear/", views.DiscoCreateView.as_view(), name="crear_disco"),
    path("mis-pedidos/", views.mis_pedidos, name="mis_pedidos"),
    path("editar-pedido/<int:pk>/", views.editar_pedido, name="editar_pedido"),
    path("eliminar-pedido/<int:pk>/", views.eliminar_pedido, name="eliminar_pedido"),
    path('pedido/aumentar/<int:pk>/', views.aumentar_cantidad, name='aumentar_cantidad'),
    path('pedido/disminuir/<int:pk>/', views.disminuir_cantidad, name='disminuir_cantidad'),
    path("discos/agregar_pedido/", views.agregar_pedido_desde_catalogo, name="agregar_pedido_desde_catalogo"),
    


    path("discos/buscar/", views.buscar_disco, name="buscar_disco"),

    path("nosotros/", views.nosotros, name="nosotros"),
    path("pedido/", views.agregar_pedido, name="agregar_pedido"),

    
]
