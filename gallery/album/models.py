from django.db import models
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse

# Create your models here.
class Usuario(models.Model):
    idusuario = models.CharField(null= True, blank= True, max_length=100)
    nombre_usuario = models.CharField(null=True, blank= True, max_length= 25)
    nombre_real = models.CharField(max_length=40)
    correo = models.CharField(max_length=60)
    contraseña = models.CharField(max_length=16)
    slug = models.SlugField(max_length=500, unique=True, blank= True, null= True)
    fecha_creacion = models.DateTimeField(blank= True, null= True)
    ultima_actualizacion = models.DateTimeField(blank= True, null= True)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.idusuario)
    
    def get_absolute_url(self):
        return reverse('detalle-de-usuario', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if self.fecha_creacion is None:
            self.fecha_creacion = timezone.localtime(timezone.now())
        if self.id_unica is None:
            self.id_unica = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.duegno.nombre, self.id_unica))

        self.slug = slugify('{} {}'.format(self.duegno.nombre, self.id_unica))
        self.ultima_actualizacion = timezone.localtime(timezone.now())
        super(Usuario, self).save(*args, **kwargs)

class Albume(models.Model):
    idalbum = models.CharField(null= True, blank= True, max_length=100)
    duegno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(null=True, blank= True, max_length= 200)
    slug = models.SlugField(max_length=500, unique=True, blank= True, null= True)
    fecha_creacion = models.DateTimeField(blank= True, null= True)
    ultima_actualizacion = models.DateTimeField(blank= True, null= True)

    def __str__(self):
        return '{} {}'.format(self.duegno.nombre, self.idalbum)
    
    def get_absolute_url(self):
        return reverse('detalle-de-imagen', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if self.fecha_creacion is None:
            self.fecha_creacion = timezone.localtime(timezone.now())
        if self.idalbum is None:
            self.idalbum = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.duegno.nombre, self.idalbum))

        self.slug = slugify('{} {}'.format(self.duegno.nombre, self.idalbum))
        self.ultima_actualizacion = timezone.localtime(timezone.now())
        super(Albume, self).save(*args, **kwargs)

        
class Etiqueta (models.Model):
    idetiqueta = models.CharField(null = True, blank= True, max_length= 100 )
    nombre = models.CharField(null = True, blank= True, max_length= 200)
    slug = models.SlugField(max_length= 500, unique= True, blank= True, null = True)
    fecha_creacion = models.DateTimeField(blank= True, null = True)
    ultima_actualizacion = models.DateTimeField(blank= True, null= True)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.idetiqueta)
    def get_absolute_url(self):
        return reverse('detalle-de-etiqueta', kwargs={'slug': self.slug})
            
    def save(self, *args, **kwargs):
        if self.fecha_creacion is None:
            self.fecha_creacion = timezone.localtime(timezone.now())
        if self.id_unica is None:
            self.idetiqueta = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.nombre, self.idetiqueta))


        self.slug = slugify('{} {}'.format(self.nombre, self.idetiqueta))
        self.last_updated = timezone.localtime(timezone.now())
        super(Etiqueta, self).save(*args, **kwargs)
            
class Imagen (models.Model):
    idimagen = models.CharField(null= True, blank= True, max_length= 100 )
    nombre = models.TextField(null= True, blank= True)
    descripcion = models.TextField(null= True, blank= True)
    texto_alt = models.TextField(null= True, blank= True)
    imagen = models.ImageField(upload_to='media/')
    etiqueta = models.ForeignKey(Etiqueta, null = True, blank = True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length= 500, unique= True, blank= True, null= True )
    ultima_actualizacion = models.DateTimeField(blank= True, null= True)

    def __str__(self):
        return '{} {}'.format(self.etiqueta.nombre, self.id_unica)
            
    def get_absolute_url(self):
        return reverse('detalle-de-imagen', kwargs={'slug': self.slug})
            
    def save(self, *args, **kwargs):
        if self.fecha_creacion is None:
            self.fecha_creacion = timezone.localtime(timezone.now())
        if self.id_unica is None:
            self.id_unica = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.categoria.nombre, self.id_unica))


        self.slug = slugify('{} {}'.format(self.categoria.nombre, self.id_unica))
        self.ultima_actualizacion = timezone.localtime(timezone.now())
        super(Imagen, self).save(*args, **kwargs)
            



