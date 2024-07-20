
from django.db import models
from django.contrib.auth.models import User

# Modelo de la aplicación

class Estudios(models.Model):
    titulo = models.CharField(max_length=50)
    institucion = models.CharField(max_length=50)
    fecha = models.CharField(max_length=10)
    degree = models.CharField(max_length=20)

class Habilidades(models.Model):
    nombreHabilidad = models.CharField(max_length=50)
    nivel = models.IntegerField()

class Proyectos(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.CharField(max_length=10)
    descripcion = models.TextField(max_length=300)
    imagen = models.CharField(max_length=15)

class ContactoCoworking(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=12)
    mensaje = models.TextField(max_length=300)

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=12)
    mensaje = models.TextField(max_length=300)

class Experiencia(models.Model):
    nombre = models.CharField(max_length=50)
    inicio = models.CharField(max_length=10)
    fin = models.CharField(max_length=10)
    empresa = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=300)

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"

