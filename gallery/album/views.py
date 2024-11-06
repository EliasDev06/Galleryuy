from django.shortcuts import render, HttpResponse
from .models import Imagen

# Create your views here.
def index(request):
    obj = Imagen.objects,all()
    return render(request, 'index.html',{'image': obj})
