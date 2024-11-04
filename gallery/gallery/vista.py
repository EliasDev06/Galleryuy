from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def subir_imagenes(request):
    return render(request, 'subir_imagenes.html', {})
def validar_cuenta(request):
    return render(request, 'validar_cuenta.html', {})