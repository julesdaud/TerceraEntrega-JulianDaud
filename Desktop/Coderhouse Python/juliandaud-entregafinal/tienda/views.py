from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Artista, Disco, Pedido
from .forms import (
    DiscoBusquedaForm,
    PedidoDiscoForm,
    PedidoEditarForm
)

# ---------- VISTAS GENERALES ---------- #
def home(request):
    return render(request, "tienda/index.html")

def listar_cliente(request):
    return render(request, "tienda/listar_cliente.html")

def listar_artista(request):
    artistas = Artista.objects.all()
    return render(request, "tienda/listar_artista.html", {"artistas": artistas})

def nosotros(request):
    return render(request, "tienda/nosotros.html")


# ---------- DISCOS (CBV) ---------- #
class DiscoListView(ListView):
    model = Disco
    template_name = "tienda/disco_list.html"
    context_object_name = "discos"

class DiscoDetailView(DetailView):
    model = Disco
    template_name = "tienda/disco_detail.html"
    context_object_name = "disco"

class DiscoCreateView(LoginRequiredMixin, CreateView):
    model = Disco
    template_name = "tienda/disco_form.html"
    fields = ["titulo", "artista", "año_lanzamiento", "genero", "precio"]
    success_url = reverse_lazy("tienda:listar_disco")

class DiscoUpdateView(LoginRequiredMixin, UpdateView):
    model = Disco
    template_name = "tienda/disco_form.html"
    fields = ["titulo", "artista", "año_lanzamiento", "genero", "precio"]
    success_url = reverse_lazy("tienda:listar_disco")

class DiscoDeleteView(LoginRequiredMixin, DeleteView):
    model = Disco
    template_name = "tienda/disco_confirm_delete.html"
    success_url = reverse_lazy("tienda:listar_disco")


# ---------- BUSCAR DISCO ---------- #
def buscar_disco(request):
    form = DiscoBusquedaForm(request.GET or None)
    discos = Disco.objects.none()  # <--- QuerySet vacío

    artista = request.GET.get("artista", "").strip()
    titulo = request.GET.get("titulo", "").strip()
    genero = request.GET.get("genero", "").strip()

    filtros = Q()
    if artista:
        filtros &= Q(artista__nombre__icontains=artista)
    if titulo:
        filtros &= Q(titulo__icontains=titulo)
    if genero:
        filtros &= Q(genero__icontains=genero)

    if artista or titulo or genero:
        discos = Disco.objects.filter(filtros)  

    return render(request, "tienda/buscar_disco.html", {"form": form, "discos": discos})

# ---------- PEDIDOS ---------- #
@login_required
def agregar_pedido(request):
    if request.method == "POST":
        form = PedidoDiscoForm(request.POST)

        if form.is_valid():
            disco_nombre = form.cleaned_data["disco_solicitado"]
            titulo_normalizado = disco_nombre.split("-")[0].strip()

            if Disco.objects.filter(titulo__icontains=titulo_normalizado).exists():
                messages.warning(
                    request,
                    "Este disco ya se encuentra en nuestro catálogo."
                )
            else:
                Pedido.objects.create(
                    nombre=form.cleaned_data["nombre"],
                    email=form.cleaned_data["email"],
                    disco_solicitado=form.cleaned_data["disco_solicitado"],
                    usuario=request.user,
                    cantidad=1,
                    estado="pendiente"
                )
                messages.success(request, "Pedido enviado correctamente.")
                return redirect("tienda:agregar_pedido")
    else:
        form = PedidoDiscoForm()

    return render(request, "tienda/agregar_pedido.html", {"form": form})


@login_required
def mis_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    return render(request, "tienda/mis_pedidos.html", {"pedidos": pedidos})


@login_required
def editar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk, usuario=request.user)

    if request.method == "POST":
        form = PedidoEditarForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            messages.success(request, "Pedido actualizado correctamente")
            return redirect("tienda:mis_pedidos")
    else:
        form = PedidoEditarForm(instance=pedido)

    return render(request, "tienda/agregar_pedido.html", {"form": form})


@login_required
def eliminar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk, usuario=request.user)
    pedido.delete()
    messages.success(request, "Pedido eliminado correctamente")
    return redirect("tienda:mis_pedidos")


@login_required
def agregar_pedido_desde_catalogo(request):
    if request.method == "POST":
        disco_id = request.POST.get("disco_id")
        disco = get_object_or_404(Disco, id=disco_id)

        pedido_existente = Pedido.objects.filter(
            usuario=request.user,
            disco_solicitado__icontains=disco.titulo
        ).first()

        if pedido_existente:
            pedido_existente.cantidad += 1
            pedido_existente.save()
            messages.info(
                request,
                "Este disco ya estaba en tus pedidos. Se actualizó la cantidad."
            )
        else:
            Pedido.objects.create(
                usuario=request.user,
                nombre=request.user.username,
                email=request.user.email,
                disco_solicitado=f"{disco.titulo} - {disco.artista.nombre}",
                cantidad=1,
                estado="procesado"
            )
            messages.success(request, "Pedido agregado correctamente.")

    return redirect("tienda:mis_pedidos")


@login_required
def aumentar_cantidad(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk, usuario=request.user)
    pedido.cantidad += 1
    pedido.save()
    return redirect("tienda:mis_pedidos")


@login_required
def disminuir_cantidad(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk, usuario=request.user)
    if pedido.cantidad > 1:
        pedido.cantidad -= 1
        pedido.save()
    return redirect("tienda:mis_pedidos")
