from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

def signup_view(request):
    form = UserCreationForm(request.POST or None)

    for field in form.fields.values():
        field.widget.attrs.update({'class': 'form-control'})

    if request.method == "POST" and form.is_valid():
        user = form.save()
        messages.success(request, f"Usuario {user.username} creado correctamente. ¡Ya podés iniciar sesión!")
        return redirect("/users/login/")

    return render(
        request,
        "users/signup.html",
        {
            "form": form,
            "title": "Registrarse",
            "button_text": "Registrarse"
        }
    )

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, f"Bienvenido/a, {user.username}!")
        return redirect("users:login")

    return render(
        request,
        "users/login.html",
        {
            "form": form,
            "title": "Iniciar sesión",
            "button_text": "Entrar"
        }
    )

def logout_view(request):
    logout(request)
    messages.success(request, "Cerraste sesión correctamente.")
    return redirect("tienda:home")
