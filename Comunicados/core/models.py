from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

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

def sample_view(request):
    current_user = request.user_id
    user = User.objects.get(pk=current_user)
    Comunicado.publicado_por = user
    print(user)

class Comunicado(models.Model):
    titulo = models.TextField(max_length=50)
    detalle = models.TextField(max_length=50)
    nivel = models.CharField(max_length=20, choices= NIVEL_CHOICES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField()
    fecha_ultima_modificacion = models.DateTimeField()
    user = 
