from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'index.html', {})

def subir_imagenes(request):
    return render(request, 'subir_imagenes.html', {})
def validar_cuenta(request):
    return render(request, 'validar_cuenta.html', {})
#def login(request):
    return render(request, 'login.hmtl', {})
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("album:list")
    else: 
        form = UserCreationForm()
    return render(request, "users/register.html", {"form" : form} )