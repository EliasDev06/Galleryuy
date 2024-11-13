
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import vista
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('album.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
   # path('login/', vista.login, name= 'login'),
    path('subir_imagenes/', vista.subir_imagenes, name='subir_imagenes'),
    path('validar_cuenta/', vista.validar_cuenta, name='validar_cuenta')
]
