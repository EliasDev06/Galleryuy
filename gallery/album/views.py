from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .models import Imagen

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register_vista(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save()) #va a iniciar sesión del usuario después de crear una cuenta, eliminar si se necesita verificación mas fuerte
            return redirect("album:index")
    else: 
        form = UserCreationForm()
    return render(request, "users/register.html", {"form" : form} )

def login_vista(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request. POST)
        if form.is_valid():
            login(request, form.get_user( ))
            return redirect("album:index")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form" : form})
