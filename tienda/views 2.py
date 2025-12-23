from django.shortcuts import render, redirect
from .models import Artista, Disco, Cliente
from .forms import DiscoForm, PedidoForm
from django.contrib import messages


# HOME
def home(request):
    return render(request, "tienda/index.html")

def listar_artista(request):
    artistas = Artista.objects.all()
    return render(request, "tienda/listar_artista.html", {"artistas": artistas})

def listar_disco(request):
    discos = Disco.objects.all()
    return render(request, "tienda/listar_disco.html", {"discos": discos})

def listar_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, "tienda/listar_cliente.html", {"clientes": clientes})


def buscar_disco(request):
    form = DiscoForm(request.GET or None)
    discos = None

    if request.GET and form.is_valid():
        artista_nombre = form.cleaned_data.get('artista')
        titulo = form.cleaned_data.get('titulo')
        genero = form.cleaned_data.get('genero')

        discos = Disco.objects.all()
        if artista_nombre:
            discos = discos.filter(artista__nombre__icontains=artista_nombre)
        if titulo:
            discos = discos.filter(titulo__icontains=titulo)
        if genero:
            discos = discos.filter(genero__icontains=genero)

    return render(request, 'tienda/buscar_disco.html', {
        'form': form,
        'discos': discos if discos else None
    })

def nosotros(request):
        return render(request, 'tienda/nosotros.html')
    
def agregar_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tu pedido ya fue registrado. Alguien de nosotros se comunicará con vos a la brevedad. ¡Muchas gracias!")
            return redirect("agregar_pedido") 
    else:
        form = PedidoForm()
    
    return render(request, "tienda/agregar_pedido.html", {"form": form})