from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.middleware import get_user
from django.conf import settings
from django.http import HttpRequest
from django.shortcuts import get_object_or_404


# Create your models here.
NIVEL_CHOICES= [
    ("GEN", "General"), 
    ("PRE", "Ciclo Preescolar"), 
    ("BAS", "Ciclo Básico"), 
    ("MED", "Ciclo Medio")
]

class Categoria(models.Model):
    nombre = models.TextField(max_length=50)
    descripcion = models.TextField(max_length=50)


#User = get_user_model()
class Comunicado(models.Model):
    titulo = models.TextField(max_length=50)
    detalle = models.TextField(max_length=50)
    nivel = models.CharField(max_length=20, choices= NIVEL_CHOICES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField()
    fecha_ultima_modificacion = models.DateTimeField()
    #publicado_por=None
    #publicado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    #publicado_por = models.QuerySet(User.username)
    user = get_user(request=User)
    publicado_por = get_object_or_404(user)