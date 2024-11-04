
from django.contrib import admin
from django.urls import path
from . import vista
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vista.index, name='index'),
    path('subir_imagenes/', vista.subir_imagenes, name='subir_imagenes'),
    path('validar_cuenta/', vista.validar_cuenta, name='validar_cuenta')
]
